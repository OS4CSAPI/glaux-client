import type { CapturedResource, DetailsActions, DetailsModel, DetailsState, DetailsTab, PresentedFact, StandardFact, StandardGroup, StandardLink, ViewSection } from '../domain';

interface FocusMemory { key: string; start?: number | null; end?: number | null; }
interface UiMemory { open: Set<string>; resourceDraft: string; stateResourceUrl: string; focusOverride?: string; }
const memories = new WeakMap<HTMLElement, UiMemory>();
const tabLabels: Record<DetailsTab, string> = { overview: 'Overview', equipment: 'Equipment', condition: 'Condition' };
const tabOrder: DetailsTab[] = ['overview', 'equipment', 'condition'];

function element<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}
function button(label: string, key: string, action: () => void, className = ''): HTMLButtonElement {
  const node = element('button', className, label);
  node.type = 'button'; node.dataset.focusKey = key;
  node.addEventListener('click', action);
  return node;
}
function disclosure(label: string, key: string, memory: UiMemory, className = ''): HTMLDetailsElement {
  const node = element('details', className);
  node.dataset.stateKey = key; node.open = memory.open.has(key);
  const summary = element('summary', undefined, label);
  summary.dataset.focusKey = `disclosure:${key}`; node.append(summary);
  node.addEventListener('toggle', () => { if (node.open) memory.open.add(key); else memory.open.delete(key); });
  return node;
}
function textValue(value: unknown): string {
  if (value === undefined) return 'Value not supplied';
  if (typeof value === 'string') return value.length ? value : '"" (empty text)';
  if (typeof value === 'object') return JSON.stringify(value, null, 2) ?? 'Value not supplied';
  return String(value);
}
function safeLink(value: string, label = value): HTMLElement {
  try {
    const url = new URL(value, document.baseURI);
    if (url.protocol === 'http:' || url.protocol === 'https:') {
      const link = element('a', undefined, label);
      link.href = url.href; link.target = '_blank'; link.rel = 'noopener noreferrer';
      return link;
    }
  } catch { /* Non-URL identifiers remain visible as text. */ }
  return element('span', undefined, label);
}
function definitionValue(value: string): HTMLElement {
  return /^https?:\/\//i.test(value) ? safeLink(value) : element('code', undefined, value);
}
function metadataRow(list: HTMLDListElement, label: string, value: string | Node): void {
  const row = element('div', 'metadata-row');
  const detail = element('dd');
  if (typeof value === 'string') detail.textContent = value; else detail.append(value);
  row.append(element('dt', undefined, label), detail); list.append(row);
}
function renderFactSource(fact: StandardFact): HTMLDListElement {
  const list = element('dl', 'metadata-list');
  metadataRow(list, 'Source label', fact.label);
  metadataRow(list, 'Definition', fact.definition ? definitionValue(fact.definition) : 'Not supplied');
  metadataRow(list, 'Standard component', fact.kind);
  if (fact.codeSpace) metadataRow(list, 'Code space', definitionValue(fact.codeSpace));
  if (fact.unit) metadataRow(list, 'Reported unit', fact.unit);
  metadataRow(list, 'Subject', fact.subject ?? 'Not supplied');
  metadataRow(list, 'Source group', fact.groupLabel);
  if (fact.groupDefinition) metadataRow(list, 'Group definition', definitionValue(fact.groupDefinition));
  metadataRow(list, 'Group path', element('code', undefined, fact.groupPath));
  metadataRow(list, 'Exact value path', element('code', undefined, fact.path));
  metadataRow(list, 'Source record', safeLink(fact.sourceUrl));
  metadataRow(list, 'Source time', fact.sourceTime ?? 'Not supplied');
  if (fact.sourceTimeMeaning) metadataRow(list, 'Time meaning', fact.sourceTimeMeaning);
  metadataRow(list, 'Retrieved at', fact.retrievedAt);
  return list;
}
function renderPresentedFact(fact: PresentedFact, key: string, memory: UiMemory): HTMLElement {
  const row = element('div', 'fact-row');
  const list = element('dl', 'fact-pair');
  list.append(element('dt', undefined, fact.label), element('dd', undefined, fact.value)); row.append(list);
  if (fact.notice) row.append(element('p', 'fact-notice', fact.notice));
  const details = disclosure('Meaning and source', key, memory, 'fact-source');
  details.append(renderFactSource(fact.source));
  const mapping = element('dl', 'metadata-list mapping-details');
  const label = fact.mapping.kind === 'mpss' ? 'MPSS profile binding' : fact.mapping.kind === 'experiment' ? 'Experimental presentation mapping' : 'Standard field presentation';
  metadataRow(mapping, 'Presentation basis', label);
  metadataRow(mapping, 'Mapping identifier', element('code', undefined, fact.mapping.id));
  metadataRow(mapping, 'Mapping explanation', fact.mapping.explanation);
  details.append(mapping); row.append(details);
  return row;
}
function renderViewSection(section: ViewSection, key: string, memory: UiMemory): HTMLElement {
  const block = section.collapsible
    ? disclosure(section.title, `${key}:section`, memory, 'view-section collapsible-section')
    : element('section', 'view-section');
  if (!section.collapsible) block.append(element('h3', undefined, section.title));
  const hero = section.heroFactKey ? section.facts.find(fact => fact.key === section.heroFactKey) : undefined;
  if (hero) block.append(element('p', 'hero-value', hero.value));
  if (section.description) block.append(element('p', 'section-description', section.description));
  if (!section.facts.length) block.append(element('p', 'empty-note', section.emptyText ?? 'No information has been supplied for this section.'));
  for (const fact of section.facts) block.append(renderPresentedFact(fact, `${key}:fact:${fact.key}`, memory));
  return block;
}
function identity(model: DetailsModel, key: string, memory: UiMemory): HTMLDetailsElement {
  const standard = model.standard;
  const details = disclosure('Identity and record', `${key}:identity`, memory, 'identity-details');
  const list = element('dl', 'metadata-list');
  metadataRow(list, 'Resource type', standard.resourceType);
  metadataRow(list, 'Resource ID', standard.id || 'Not supplied');
  if (standard.uniqueId) metadataRow(list, 'Unique identifier', standard.uniqueId);
  if (standard.description) metadataRow(list, 'Description', standard.description);
  for (const [index, capture] of standard.captures.entries()) {
    metadataRow(list, `Record ${index + 1}`, safeLink(capture.url));
    metadataRow(list, `Record ${index + 1} retrieved at`, capture.retrievedAt);
  }
  details.append(list); return details;
}
function recordSource(model: DetailsModel): string {
  const url = model.standard.captures[0]?.url;
  if (!url) return 'Not supplied';
  try { return new URL(url, document.baseURI).host; } catch { return url; }
}
function renderOperatorCard(state: DetailsState, model: DetailsModel, actions: DetailsActions, memory: UiMemory, key: string): HTMLElement {
  const card = element('article', 'system-card');
  card.setAttribute('aria-label', 'System details'); card.setAttribute('aria-busy', String(state.loading));
  const banner = state.sourceKind === 'synthetic' ? 'Synthetic test data · Not an operational display' : 'Read-only view of the selected source';
  card.append(element('p', 'record-banner', banner));
  const header = element('header', 'card-header');
  header.append(element('h2', undefined, model.standard.name || 'Unnamed resource'));
  const meta = element('ul', 'record-meta');
  meta.append(element('li', undefined, `Type: ${model.standard.resourceType}`), element('li', undefined, `ID: ${model.standard.id || 'Not supplied'}`), element('li', undefined, `Source: ${recordSource(model)}`));
  header.append(meta, identity(model, key, memory)); card.append(header);
  const category = element('div', 'category-bar');
  category.append(element('span', 'current-category', 'Operational')); card.append(category);
  const tabs = element('div', 'details-tabs');
  tabs.setAttribute('role', 'tablist'); tabs.setAttribute('aria-label', 'Operational details');
  for (const tab of tabOrder) {
    const tabButton = button(tabLabels[tab], `tab:${tab}`, () => actions.selectTab(tab), 'tab-button');
    tabButton.id = `details-tab-${tab}`; tabButton.setAttribute('role', 'tab');
    tabButton.setAttribute('aria-selected', String(state.tab === tab)); tabButton.setAttribute('aria-controls', `details-panel-${tab}`);
    tabButton.tabIndex = state.tab === tab ? 0 : -1;
    tabButton.addEventListener('keydown', event => {
      let index = tabOrder.indexOf(tab);
      if (event.key === 'ArrowRight') index = (index + 1) % tabOrder.length;
      else if (event.key === 'ArrowLeft') index = (index + tabOrder.length - 1) % tabOrder.length;
      else if (event.key === 'Home') index = 0;
      else if (event.key === 'End') index = tabOrder.length - 1;
      else return;
      event.preventDefault();
      const next = tabOrder[index]; memory.focusOverride = `tab:${next}`; actions.selectTab(next);
    });
    tabs.append(tabButton);
  }
  card.append(tabs);
  for (const tab of tabOrder) {
    const panel = element('div', 'tab-panel');
    panel.id = `details-panel-${tab}`; panel.setAttribute('role', 'tabpanel');
    panel.setAttribute('aria-labelledby', `details-tab-${tab}`); panel.tabIndex = 0;
    panel.dataset.focusKey = `panel:${tab}`; panel.hidden = tab !== state.tab;
    const sections = model.views[tab];
    if (!sections.length) panel.append(element('p', 'empty-note', `No ${tabLabels[tab].toLowerCase()} information is available in the selected records. Standard view retains all supplied content.`));
    for (const section of sections) panel.append(renderViewSection(section, `${key}:${tab}:${section.id}`, memory));
    card.append(panel);
  }
  const footer = element('footer', 'card-footer');
  footer.append(element('p', undefined, state.sourceKind === 'synthetic' ? 'Illustrative source replay · No live device state' : 'Source records as retrieved · Retrieval time does not establish current device state'));
  const refresh = button(state.loading ? 'Refreshing…' : 'Refresh view', 'refresh:operator', () => { if (!state.loading) actions.refresh(); }, 'quiet-button');
  refresh.setAttribute('aria-disabled', String(state.loading)); footer.append(refresh);
  card.append(footer, element('p', 'record-banner', banner)); return card;
}
function standardFact(fact: StandardFact, key: string, memory: UiMemory): HTMLElement {
  const row = element('div', 'standard-fact');
  const list = element('dl', 'fact-pair'); list.append(element('dt', undefined, fact.label));
  const value = element('dd');
  if (typeof fact.value === 'object' && fact.value !== null) value.append(element('pre', 'structured-value', textValue(fact.value)));
  else value.append(element('span', undefined, textValue(fact.value)));
  if (fact.unit) value.append(element('span', 'reported-unit', ` ${fact.unit}`));
  list.append(value); row.append(list);
  const definition = element('p', 'standard-definition');
  definition.append(element('span', undefined, 'Definition: '), fact.definition ? definitionValue(fact.definition) : element('span', undefined, 'Not supplied'));
  const path = element('p', 'standard-path');
  path.append(element('span', undefined, 'Path: '), element('code', undefined, fact.path)); row.append(definition, path);
  const details = disclosure('Full source metadata', `${key}:standard:${fact.key}`, memory, 'fact-source');
  details.append(renderFactSource(fact)); row.append(details); return row;
}
function standardGroup(group: StandardGroup, key: string, memory: UiMemory): HTMLElement {
  const block = element('section', 'standard-group'); block.append(element('h3', undefined, group.label));
  if (group.definition) {
    const description = element('p', 'standard-definition');
    description.append(element('span', undefined, 'Group definition: '), definitionValue(group.definition)); block.append(description);
  }
  const metadata = element('p', 'standard-path');
  metadata.append(element('span', undefined, `${group.kind} · `), element('code', undefined, group.path)); block.append(metadata);
  if (!group.facts.length) block.append(element('p', 'empty-note', 'No scalar fields are present in this group. Its original content remains available below.'));
  for (const fact of group.facts) block.append(standardFact(fact, `${key}:${group.key}`, memory));
  return block;
}
function standardLink(link: StandardLink): HTMLElement {
  const item = element('li', 'relationship');
  const title = element('p', 'relationship-title'); title.append(element('strong', undefined, link.title || link.rel || 'Related resource')); item.append(title);
  const list = element('dl', 'metadata-list');
  metadataRow(list, 'Relationship', link.rel || 'Not supplied'); metadataRow(list, 'Target', safeLink(link.href));
  if (link.mediaType) metadataRow(list, 'Media type', link.mediaType);
  metadataRow(list, 'Path', element('code', undefined, link.path)); metadataRow(list, 'Source record', safeLink(link.sourceUrl)); item.append(list);
  return item;
}
function downloadCapture(capture: CapturedResource, index: number): void {
  const blob = new Blob([new Uint8Array(capture.bytes).buffer], { type: capture.contentType || 'application/octet-stream' });
  const url = URL.createObjectURL(blob); const link = element('a');
  link.href = url; link.download = `source-response-${index + 1}${capture.contentType.includes('json') ? '.json' : '.bin'}`;
  link.hidden = true; document.body.append(link); link.click(); link.remove();
  window.setTimeout(() => URL.revokeObjectURL(url), 1000);
}
function renderCapture(capture: CapturedResource, index: number, key: string, memory: UiMemory): HTMLElement {
  const details = disclosure(`Response ${index + 1}: ${capture.url}`, `${key}:capture:${index}`, memory, 'capture');
  const list = element('dl', 'metadata-list');
  metadataRow(list, 'Requested URL', safeLink(capture.requestedUrl)); metadataRow(list, 'Response URL', safeLink(capture.url));
  metadataRow(list, 'HTTP status', String(capture.status)); metadataRow(list, 'Content type', capture.contentType || 'Not supplied');
  metadataRow(list, 'Retrieved at', capture.retrievedAt); metadataRow(list, 'Original body size', `${capture.bytes.byteLength.toLocaleString()} bytes`);
  details.append(list, button('Download original body', `download:${index}`, () => downloadCapture(capture, index), 'quiet-button'));
  const headers = disclosure('Response headers', `${key}:capture:${index}:headers`, memory, 'capture-part');
  headers.append(element('pre', 'raw-content', JSON.stringify(capture.headers, null, 2)));
  const body = disclosure('Original response text', `${key}:capture:${index}:text`, memory, 'capture-part'); body.append(element('pre', 'raw-content', capture.text));
  const json = disclosure('Parsed JSON including unfamiliar fields', `${key}:capture:${index}:json`, memory, 'capture-part');
  json.append(element('pre', 'raw-content', JSON.stringify(capture.json, null, 2) ?? 'No parsed JSON value is available.'));
  details.append(headers, body, json); return details;
}
function renderStandardView(state: DetailsState, model: DetailsModel, actions: DetailsActions, memory: UiMemory, key: string): HTMLElement {
  const panel = element('article', 'standard-view');
  panel.setAttribute('aria-label', 'Standard resource view'); panel.setAttribute('aria-busy', String(state.loading));
  const heading = element('header', 'standard-header'); heading.append(element('h2', undefined, model.standard.name || 'Unnamed resource'));
  heading.append(element('p', 'section-description', 'Standard properties and relationships from the same captured records. Original responses retain all unfamiliar content.'), identity(model, key, memory));
  const refresh = button(state.loading ? 'Refreshing…' : 'Refresh view', 'refresh:standard', () => { if (!state.loading) actions.refresh(); }, 'quiet-button');
  refresh.setAttribute('aria-disabled', String(state.loading)); heading.append(refresh); panel.append(heading);
  const facts = element('section', 'standard-properties'); facts.append(element('h2', 'section-heading', 'Standard properties'));
  if (!model.standard.groups.length) facts.append(element('p', 'empty-note', 'No recognized scalar property groups are available. The complete original response remains accessible below.'));
  for (const group of model.standard.groups) facts.append(standardGroup(group, key, memory)); panel.append(facts);
  const relationships = element('section', 'standard-relationships'); relationships.append(element('h2', 'section-heading', 'Relationships and links'));
  if (!model.standard.links.length) relationships.append(element('p', 'empty-note', 'No standard links were supplied in the inspected records.'));
  const list = element('ul', 'relationship-list'); for (const link of model.standard.links) list.append(standardLink(link)); relationships.append(list); panel.append(relationships);
  const captures = element('section', 'standard-captures'); captures.append(element('h2', 'section-heading', 'Original responses'));
  captures.append(element('p', 'section-description', 'Response bodies, metadata, and unknown fields are preserved independently of the displayed interpretation. The downloaded body contains the original bytes.'));
  if (!model.standard.captures.length) captures.append(element('p', 'empty-note', 'No captured response is available.'));
  model.standard.captures.forEach((capture, index) => captures.append(renderCapture(capture, index, key, memory))); panel.append(captures);
  return panel;
}
function renderInterpretation(model: DetailsModel, state: DetailsState, actions: DetailsActions, key: string, memory: UiMemory): HTMLElement {
  const details = disclosure('Interpretation and retrieval details', `${key}:interpretation`, memory, 'interpretation');
  details.append(element('p', undefined, model.interpretationSummary));
  const notes = element('ul', 'interpretation-notes');
  for (const note of model.interpretationNotes) notes.append(element('li', undefined, note));
  if (model.unmappedFactCount > 0) notes.append(element('li', undefined, `${model.unmappedFactCount} standard ${model.unmappedFactCount === 1 ? 'fact is' : 'facts are'} not arranged in the operator sections. ${state.mode === 'operator' ? 'Open Standard view to inspect all supplied standard fields.' : 'All extracted standard fields are shown above.'}`));
  if (notes.childElementCount) details.append(notes);
  const captureList = element('dl', 'metadata-list');
  metadataRow(captureList, 'Library status', state.libraryStatus);
  metadataRow(captureList, 'Library parse', model.standard.libraryParsed ? 'Available' : 'Not available for the selected response');
  metadataRow(captureList, 'Captured responses', String(model.standard.captures.length));
  for (const [index, capture] of model.standard.captures.entries()) metadataRow(captureList, `Response ${index + 1} retrieved at`, capture.retrievedAt);
  details.append(captureList);
  if (state.mode === 'operator') details.append(button('Open Standard view and original responses', 'inspect-standard', () => {
    memory.focusOverride = 'mode:standard'; actions.selectMode('standard');
  }, 'quiet-button'));
  return details;
}
function captureFocus(container: HTMLElement): FocusMemory | undefined {
  const active = document.activeElement;
  if (!(active instanceof HTMLElement) || !container.contains(active) || !active.dataset.focusKey) return undefined;
  const memory: FocusMemory = { key: active.dataset.focusKey };
  if (active instanceof HTMLInputElement && ['text', 'url', 'search'].includes(active.type)) {
    try { memory.start = active.selectionStart; memory.end = active.selectionEnd; } catch { /* URL selection support varies. */ }
  }
  return memory;
}
function restoreFocus(container: HTMLElement, focus: FocusMemory | undefined): void {
  if (!focus) return;
  const target = Array.from(container.querySelectorAll<HTMLElement>('[data-focus-key]')).find(node => node.dataset.focusKey === focus.key);
  if (!target || target instanceof HTMLButtonElement && target.disabled) return;
  target.focus({ preventScroll: true });
  if (target instanceof HTMLInputElement && focus.start !== undefined && focus.start !== null) {
    try { target.setSelectionRange(focus.start, focus.end ?? focus.start); } catch { /* URL selection support varies. */ }
  }
}

/** Present the same captured source through operator and standard views. */
export function renderDetails(container: HTMLElement, state: DetailsState, actions: DetailsActions): void {
  let memory = memories.get(container);
  if (!memory) { memory = { open: new Set(), resourceDraft: state.sourceKind === 'remote' ? state.resourceUrl : '', stateResourceUrl: state.resourceUrl }; memories.set(container, memory); }
  for (const details of container.querySelectorAll<HTMLDetailsElement>('details[data-state-key]')) {
    const key = details.dataset.stateKey!;
    if (details.open) memory.open.add(key); else memory.open.delete(key);
  }
  const previousDraft = container.querySelector<HTMLInputElement>('#resource-url');
  if (previousDraft) memory.resourceDraft = previousDraft.value;
  if (memory.stateResourceUrl !== state.resourceUrl) {
    if (state.sourceKind === 'remote') memory.resourceDraft = state.resourceUrl;
    memory.stateResourceUrl = state.resourceUrl;
  }
  const focus = memory.focusOverride ? { key: memory.focusOverride } : captureFocus(container); memory.focusOverride = undefined;
  const body = document.createDocumentFragment(); const header = element('header', 'page-header');
  header.append(element('p', 'eyebrow', 'Glaux Client / Details View'), element('h1', undefined, 'Glaux Client'), element('p', 'intro', 'Explore the same sensor-system records in an operator view and a standard view.')); body.append(header);
  const controls = element('section', 'source-controls'); controls.setAttribute('aria-label', 'Select source records');
  const exampleRow = element('div', 'example-control'); const label = element('label', undefined, 'Evaluation example'); label.htmlFor = 'example-select';
  const select = element('select'); select.id = 'example-select'; select.dataset.focusKey = 'example-select';
  const placeholder = element('option', undefined, 'Select an illustrative example'); placeholder.value = ''; placeholder.disabled = true; select.append(placeholder);
  for (const example of state.examples) { const option = element('option', undefined, example.label); option.value = example.id; select.append(option); }
  select.value = state.sourceKind === 'synthetic' ? state.selectedExampleId : '';
  select.addEventListener('change', () => { if (select.value) actions.selectExample(select.value); }); exampleRow.append(label, select); controls.append(exampleRow);
  const remote = disclosure('Use your existing CSAPI server', 'remote-form', memory, 'remote-source');
  if (state.sourceKind === 'remote') remote.open = true;
  const form = element('form'); const urlLabel = element('label', undefined, 'System resource URL'); urlLabel.htmlFor = 'resource-url';
  const input = element('input'); input.id = 'resource-url'; input.type = 'url'; input.required = true;
  input.placeholder = 'https://your-server.example/systems/system-id'; input.autocomplete = 'off'; input.spellcheck = false;
  input.value = memory.resourceDraft; input.dataset.focusKey = 'resource-url'; input.setAttribute('aria-describedby', 'resource-url-help');
  input.addEventListener('input', () => { memory.resourceDraft = input.value; });
  const load = element('button', 'primary-button', state.loading ? 'Loading…' : 'Load resource');
  load.type = 'submit'; load.dataset.focusKey = 'load-resource'; load.setAttribute('aria-disabled', String(state.loading));
  const inputRow = element('div', 'url-input-row'); inputRow.append(input, load); form.append(urlLabel, inputRow);
  const help = element('p', 'input-help', 'Enter a direct CSAPI System resource URL. Requests are read-only. The server must permit this browser to read its responses.');
  help.id = 'resource-url-help'; form.append(help);
  form.addEventListener('submit', event => { event.preventDefault(); if (!state.loading && form.reportValidity()) actions.loadResource(input.value.trim()); });
  remote.append(form); controls.append(remote); body.append(controls);
  const modes = element('div', 'mode-switch'); modes.setAttribute('role', 'group'); modes.setAttribute('aria-label', 'Presentation mode');
  for (const mode of ['operator', 'standard'] as const) {
    const modeButton = button(mode === 'operator' ? 'Operator view' : 'Standard view', `mode:${mode}`, () => actions.selectMode(mode), 'mode-button');
    modeButton.setAttribute('aria-pressed', String(state.mode === mode)); modes.append(modeButton);
  }
  body.append(modes);
  body.append(element('p', 'source-notice', state.sourceKind === 'synthetic' ? 'Synthetic examples · Local fixture HTTP reads, not a live manufacturer integration.' : 'Remote source · Read-only retrieval. Reported facts retain their source meaning and time.'));
  const status = element('p', 'loading-status', state.loading ? 'Loading source records…' : '');
  status.setAttribute('role', 'status'); status.setAttribute('aria-live', 'polite'); status.setAttribute('aria-atomic', 'true');
  if (!state.loading) status.classList.add('visually-hidden'); body.append(status);
  if (state.error) {
    const error = element('div', 'load-error'); error.setAttribute('role', 'alert');
    error.append(element('h2', undefined, 'Unable to load the selected resource'), element('p', undefined, state.error)); body.append(error);
  }
  if (state.model) {
    const key = `record:${state.resourceUrl}:${state.model.standard.id}`;
    if (state.model.standard.warnings.length) {
      const warning = disclosure('Source and interpretation notices', `${key}:warnings`, memory, 'source-warnings');
      const list = element('ul'); state.model.standard.warnings.forEach(message => list.append(element('li', undefined, message))); warning.append(list); body.append(warning);
    }
    body.append(state.mode === 'operator' ? renderOperatorCard(state, state.model, actions, memory, key) : renderStandardView(state, state.model, actions, memory, key));
    body.append(renderInterpretation(state.model, state, actions, key, memory));
  } else if (!state.loading && !state.error) body.append(element('p', 'empty-state', 'Select an illustrative example or load a System resource to inspect its details.'));
  const footer = element('footer', 'page-footer');
  footer.append(element('p', undefined, 'Read-only prototype · MPSS v0.3.5 unchanged · No device commands or server writes'));
  const notices = element('a', undefined, 'Third-party notices'); notices.href = '/THIRD_PARTY_NOTICES.txt'; footer.append(notices); body.append(footer);
  container.classList.add('details-app'); container.replaceChildren(body); restoreFocus(container, focus);
}
