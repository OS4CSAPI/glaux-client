import type { DetailsActions, DetailsTab, PowerViewState } from '../domain';
import type { PowerExampleRole } from '../data/power-example';
import type { PowerEntity, PowerEvidence, PowerObservation, PowerReference, PowerRelationship } from '../profile/power';

interface Memory { open: Set<string>; focusOverride?: string; }
const roleLabels: Record<PowerExampleRole | 'manifest', string> = {
  station: 'Station description', 'source-a': 'Source A description', 'source-b': 'Source B description',
  deployment: 'Deployment and source history', datastream: 'Voltage data stream',
  schema: 'Voltage result schema', observation: 'Voltage observation', manifest: 'Local example catalogue',
};
function node<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const result = document.createElement(tag);
  if (className) result.className = className;
  if (text !== undefined) result.textContent = text;
  return result;
}
function action(label: string, key: string, run: () => void, className = 'quiet-button'): HTMLButtonElement {
  const result = node('button', className, label);
  result.type = 'button'; result.dataset.focusKey = key; result.addEventListener('click', run);
  return result;
}
function details(label: string, key: string, memory: Memory, className = 'power-evidence'): HTMLDetailsElement {
  const result = node('details', className);
  result.dataset.stateKey = key; result.open = memory.open.has(key);
  const summary = node('summary', undefined, label); summary.dataset.focusKey = `disclosure:${key}`;
  result.append(summary);
  result.addEventListener('toggle', () => { if (result.open) memory.open.add(key); else memory.open.delete(key); });
  return result;
}
function pair(list: HTMLDListElement, label: string, value: string | Node): void {
  const row = node('div', 'metadata-row'); const body = node('dd');
  if (typeof value === 'string') body.textContent = value; else body.append(value);
  row.append(node('dt', undefined, label), body); list.append(row);
}
function link(href: string, label: string): HTMLAnchorElement {
  const result = node('a', undefined, label); result.href = href;
  result.target = '_blank'; result.rel = 'noopener noreferrer'; return result;
}
function timeLabel(value?: string): string {
  if (!value || !Number.isFinite(Date.parse(value))) return value || 'Not supplied';
  return new Intl.DateTimeFormat('en-US', { timeZone: 'UTC', month: 'short', day: 'numeric', year: 'numeric',
    hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false }).format(new Date(value)) + ' UTC';
}
function name(entity?: PowerEntity): string { return entity?.label || entity?.id || entity?.ref || 'Unresolved equipment'; }
function refName(reference?: PowerReference): string {
  return reference?.target ? name(reference.target) : typeof reference?.value === 'string' ? reference.value : 'Not supplied';
}
function stationRef(power: PowerViewState): string | undefined {
  return power.bundle.records.find(record => record.role === 'station')?.canonicalUrl;
}
function supplies(power: PowerViewState): PowerRelationship[] {
  return power.model.relationships.filter(relationship => relationship.kind === 'powers'
    && relationship.status === 'valid' && relationship.applicability === 'applicable'
    && relationship.object?.resolvedRef === stationRef(power));
}
function recordButton(evidence: PowerEvidence, power: PowerViewState, actions: DetailsActions, memory: Memory, key: string): HTMLElement {
  const record = power.bundle.records.find(item => item.canonicalUrl === evidence.canonicalUrl);
  if (!record) return node('span', 'empty-note', 'The referenced record is not included in this example.');
  return action('Inspect original record', key, () => {
    memory.focusOverride = 'power-record-select'; actions.selectPowerRecord(record.role);
  });
}
function evidencePanel(label: string, evidence: Array<PowerEvidence | undefined>, power: PowerViewState,
  actions: DetailsActions, memory: Memory, key: string, meaning: string): HTMLElement {
  const disclosure = details(label, key, memory);
  disclosure.append(node('p', 'section-description', meaning));
  const seen = new Set<string>();
  for (const item of evidence) {
    if (!item || seen.has(`${item.canonicalUrl}:${item.path}`)) continue;
    seen.add(`${item.canonicalUrl}:${item.path}`);
    const entry = node('div', 'power-evidence-entry'); const list = node('dl', 'metadata-list');
    const record = power.bundle.records.find(record => record.canonicalUrl === item.canonicalUrl);
    pair(list, 'Source file', record?.file ?? item.sourceUrl);
    pair(list, 'Exact source path', node('code', undefined, item.path || '/'));
    pair(list, 'Resource reference', node('code', undefined, item.canonicalUrl));
    if (item.retrievedAt) pair(list, 'Retrieved at', timeLabel(item.retrievedAt));
    entry.append(list, recordButton(item, power, actions, memory, `power:${key}:${item.path}:record`));
    disclosure.append(entry);
  }
  return disclosure;
}
function entityButton(entity: PowerEntity, power: PowerViewState, actions: DetailsActions, key: string, role?: string): HTMLButtonElement {
  const result = action('', key, () => actions.selectPowerEntity(entity.ref), 'power-entity-button');
  result.dataset.entityRef = entity.ref;
  result.setAttribute('aria-pressed', String(power.selectedRef === entity.ref));
  if (role) result.append(node('span', 'power-entity-role', role));
  result.append(node('span', 'power-entity-name', name(entity)));
  if (entity.id) result.append(node('span', 'power-entity-id', entity.id));
  return result;
}
function eligibleObservation(observation: PowerObservation, power: PowerViewState): boolean {
  const at = Date.parse(power.at); const phenomenon = Date.parse(observation.phenomenonTime ?? '');
  const result = Date.parse(observation.resultTime ?? observation.phenomenonTime ?? '');
  return observation.status === 'valid' && observation.value !== undefined
    && Number.isFinite(phenomenon) && phenomenon <= at && Number.isFinite(result) && result <= at;
}
function observationCard(observation: PowerObservation, power: PowerViewState, actions: DetailsActions,
  memory: Memory, key: string): HTMLElement {
  const result = node('section', 'power-reading'); result.dataset.observationId = observation.id ?? observation.key;
  result.append(node('h4', undefined, 'Reported supply terminal voltage'));
  result.append(node('p', 'hero-value', `${observation.value} ${observation.unit ?? ''}`.trim()));
  const list = node('dl', 'metadata-list');
  pair(list, 'Describes', refName(observation.observedSubject));
  pair(list, 'Measurement point', 'Supply output terminals');
  pair(list, 'Reported by', refName(observation.reportingSystem));
  const observedAt = node('time', undefined, timeLabel(observation.phenomenonTime));
  observedAt.dateTime = observation.phenomenonTime ?? ''; pair(list, 'Observed at', observedAt);
  pair(list, 'Result time', timeLabel(observation.resultTime));
  result.append(list, node('p', 'fact-notice', 'One historical observation. No charge percentage or remaining runtime is supplied.'));
  result.append(evidencePanel('Meaning and source', [observation.evidence, observation.schemaEvidence,
    observation.observedSubject?.evidence, observation.reportingSystem?.evidence, observation.outputEvidence],
  power, actions, memory, `${key}:evidence`,
  'The MPSS supply-terminal-voltage definition identifies the measured property and point. The result schema supplies V. The stream identifies the reporting system separately from the source being observed. This is the external-supply example, not the RFC 7577 battery-voltage conversion case.'));
  return result;
}
function selectedEquipment(power: PowerViewState, actions: DetailsActions, memory: Memory, key: string): HTMLElement {
  const selected = power.model.entities.find(entity => entity.ref === power.selectedRef);
  const section = node('section', 'power-inspection'); section.dataset.selectedEntity = power.selectedRef;
  section.append(node('h3', undefined, 'Selected equipment'), node('h4', 'power-selected-name', name(selected)));
  if (!selected) { section.append(node('p', 'empty-note', 'Select available equipment to inspect its record.')); return section; }
  const list = node('dl', 'metadata-list');
  if (selected.id) pair(list, 'Record ID', selected.id);
  if (selected.uniqueId) pair(list, 'Unique identity', node('code', undefined, selected.uniqueId));
  const relevant = power.model.relationships.filter(relationship => relationship.status === 'valid'
    && relationship.applicability === 'applicable'
    && (relationship.subject?.resolvedRef === selected.ref || relationship.object?.resolvedRef === selected.ref));
  for (const relationship of relevant) {
    const from = relationship.subject?.resolvedRef === selected.ref;
    const label = relationship.kind === 'powers' ? from ? 'Supplies' : 'Supplied by'
      : relationship.kind === 'meters' ? from ? 'Meters' : 'Metered by' : from ? 'Aggregates' : 'Aggregated by';
    pair(list, label, refName(from ? relationship.object : relationship.subject));
  }
  section.append(list);
  if (!relevant.length) section.append(node('p', 'empty-note', 'No applicable power relationship for this equipment at the selected time is established by these records.'));
  section.append(evidencePanel('Identity and source', [selected.evidence], power, actions, memory, `${key}:identity`,
    'Equipment names and identities come from the selected source descriptions. A source role does not establish a battery type or a measured operating state.'));
  const readings = power.model.observations.filter(observation => eligibleObservation(observation, power)
    && observation.observedSubject?.resolvedRef === selected.ref);
  if (!readings.length) section.append(node('p', 'empty-note power-no-reading', 'No observation for this equipment at or before the selected time is supplied.'));
  for (const observation of readings) section.append(observationCard(observation, power, actions, memory, `${key}:${observation.key}`));
  return section;
}
function history(power: PowerViewState, actions: DetailsActions, memory: Memory, key: string): HTMLElement {
  const section = node('section', 'power-history'); section.append(node('h3', undefined, 'Source replacement history'));
  const events = power.model.replacementEvents.filter(event => event.status === 'valid');
  if (!events.length) section.append(node('p', 'empty-note', 'No resolved replacement event is supplied.'));
  for (const event of events) {
    const later = Date.parse(event.time ?? '') > Date.parse(power.at);
    const card = node('div', 'power-history-event'); card.dataset.eventId = event.id ?? event.key;
    card.append(node('p', 'power-history-status', later ? 'Later in this example' : 'Recorded change by the selected time'));
    const date = node('time', 'power-history-time', timeLabel(event.time)); date.dateTime = event.time ?? '';
    card.append(date); const list = node('dl', 'metadata-list');
    pair(list, 'Removed', refName(event.replaced)); pair(list, 'Installed', refName(event.replacement));
    pair(list, 'Affected equipment', event.affectedSubjects.map(refName).join(', ') || 'Not supplied'); card.append(list);
    card.append(evidencePanel('Meaning and source', [event.evidence, event.replaced?.evidence, event.replacement?.evidence],
      power, actions, memory, `${key}:${event.key}`, 'The deployment history records the replacement. The time-bounded supply relationships separately establish which source supplies the same station for each interval.'));
    section.append(card);
  }
  return section;
}

export function renderPowerContext(power: PowerViewState, actions: DetailsActions, loading: boolean): HTMLElement {
  const result = node('div', 'power-context');
  const label = node('label', undefined, 'View arrangement at'); label.htmlFor = 'power-time-select';
  const select = node('select'); select.id = 'power-time-select'; select.dataset.focusKey = 'power-time-select'; select.disabled = loading;
  for (const item of power.bundle.times) {
    const option = node('option', undefined, item.label); option.value = item.time; select.append(option);
  }
  select.value = power.at; select.addEventListener('change', () => actions.selectPowerTime(select.value));
  const date = node('time', 'power-arrangement-time', timeLabel(power.at)); date.id = 'power-arrangement-time'; date.dateTime = power.at;
  result.append(label, select, date, node('p', 'fact-notice', 'Historical example time. Supply relationships describe the recorded arrangement; they do not measure power flow.'));
  return result;
}

export function renderPowerPanel(tab: DetailsTab, power: PowerViewState, actions: DetailsActions, memory: Memory): HTMLElement {
  const result = node('div', 'power-panel'); const key = `power:${tab}`;
  if (tab === 'overview') {
    const arrangement = node('section', 'power-arrangement'); arrangement.append(node('h3', undefined, 'Power arrangement'));
    arrangement.append(node('p', 'section-description', 'Select equipment to inspect its identity and readings.'));
    const relations = supplies(power);
    if (!relations.length) arrangement.append(node('p', 'empty-note', 'A resolved supply relationship for the station is not available at this time.'));
    for (const relationship of relations) {
      const source = relationship.subject?.target; const station = relationship.object?.target;
      if (!source || !station) continue;
      const flow = node('div', 'power-arrangement-row'); flow.dataset.relationshipId = relationship.id ?? relationship.key;
      flow.append(entityButton(source, power, actions, `${key}:source:${source.ref}`, 'Supply source'),
        node('span', 'power-relation-label', 'supplies →'), entityButton(station, power, actions, `${key}:station:${station.ref}`, 'Supplied equipment'));
      arrangement.append(flow, evidencePanel('Relationship meaning and source', [relationship.evidence,
        relationship.subject?.evidence, relationship.object?.evidence, relationship.interval.fromEvidence, relationship.interval.untilEvidence],
      power, actions, memory, `${key}:relationship:${relationship.key}`,
      'RFC 7326 supplies the power-supply relationship concept. MPSS v0.3.5 R16 provides this authored OGC binding. The applicable interval includes its start and excludes its end. Source identity, relationship direction, and time come from the records.'));
    }
    result.append(arrangement, selectedEquipment(power, actions, memory, key), history(power, actions, memory, `${key}:history`));
  } else if (tab === 'equipment') {
    result.append(node('h3', undefined, 'Equipment in the recorded arrangement'));
    const refs = new Set<string>();
    for (const relationship of power.model.relationships) {
      if (relationship.kind !== 'powers' || relationship.object?.resolvedRef !== stationRef(power)) continue;
      if (relationship.subject?.resolvedRef) refs.add(relationship.subject.resolvedRef);
      if (relationship.object?.resolvedRef) refs.add(relationship.object.resolvedRef);
    }
    const list = node('div', 'power-equipment-list');
    for (const ref of refs) {
      const entity = power.model.entities.find(entity => entity.ref === ref); if (!entity) continue;
      const role = ref === stationRef(power) ? 'Supplied equipment'
        : supplies(power).some(relationship => relationship.subject?.resolvedRef === ref) ? 'Source at selected time' : 'Other recorded source';
      list.append(entityButton(entity, power, actions, `${key}:entity:${ref}`, role));
    }
    result.append(list, selectedEquipment(power, actions, memory, key), history(power, actions, memory, `${key}:history`));
  } else {
    const selected = power.model.entities.find(entity => entity.ref === power.selectedRef);
    result.append(node('h3', undefined, 'Condition evidence'), node('p', 'section-description', `Selected equipment: ${name(selected)}`));
    const readings = power.model.observations.filter(observation => eligibleObservation(observation, power));
    const own = readings.filter(observation => observation.observedSubject?.resolvedRef === power.selectedRef);
    if (!own.length) result.append(node('p', 'empty-note power-no-reading', 'No observation for this equipment at or before the selected time is supplied.'));
    for (const observation of own) result.append(observationCard(observation, power, actions, memory, `${key}:${observation.key}`));
    const reported = readings.filter(observation => observation.reportingSystem?.resolvedRef === power.selectedRef
      && observation.observedSubject?.resolvedRef !== power.selectedRef);
    if (reported.length) result.append(node('h3', undefined, 'Reports about other equipment'));
    for (const observation of reported) result.append(observationCard(observation, power, actions, memory, `${key}:reported:${observation.key}`));
    result.append(node('p', 'fact-notice', 'Changing the arrangement time does not move an observation to a different source. Refresh retrieves the same historical records.'));
  }
  return result;
}

export function renderPowerRecordSelector(power: PowerViewState, actions: DetailsActions): HTMLElement {
  const result = node('section', 'power-record-selector');
  result.append(node('h2', undefined, 'Inspect an original example record'));
  const label = node('label', undefined, 'Record'); label.htmlFor = 'power-record-select';
  const select = node('select'); select.id = 'power-record-select'; select.dataset.focusKey = 'power-record-select';
  for (const role of [...power.bundle.records.map(record => record.role), 'manifest'] as const) {
    const option = node('option', undefined, roleLabels[role]); option.value = role; select.append(option);
  }
  select.value = power.standardRecordRole;
  select.addEventListener('change', () => actions.selectPowerRecord(select.value as PowerExampleRole | 'manifest'));
  result.append(label, select, node('p', 'section-description', 'Each resource keeps its own identity, standard properties, and original response bytes. The local catalogue connects the fixed example files; it is not a CSAPI discovery response.'));
  const record = power.bundle.records.find(record => record.role === power.standardRecordRole);
  if (record?.error) result.append(node('p', 'power-issue', record.error));
  if (record) {
    const list = node('dl', 'metadata-list'); pair(list, 'Original example file', record.file);
    pair(list, 'Catalogue resource reference', node('code', undefined, record.canonicalUrl));
    pair(list, 'Expected source SHA-256', node('code', undefined, record.sha256)); result.append(list);
  }
  return result;
}

export function renderPowerBasis(power: PowerViewState, actions: DetailsActions, memory: Memory): HTMLElement {
  const result = details('Model, mapping, and evidence', 'power:basis', memory, 'interpretation power-basis');
  result.append(node('p', undefined, 'This demonstration interprets selected MPSS v0.3.5 relationships and observation context. It does not implement an SNMP agent or the complete EMAN or battery model.'));
  const list = node('dl', 'metadata-list');
  pair(list, 'Donor concept', link('https://www.rfc-editor.org/rfc/rfc7326.html#section-6.6', 'RFC 7326: energy relationships'));
  pair(list, 'Profile binding', 'MPSS v0.3.5: R16 supply relationships; R11 producer and observed subject; R17 quantity meaning; typed replacement history.');
  pair(list, 'Input records', 'Seven unchanged, explicitly synthetic JSON files from the connected profile example.');
  pair(list, 'Client decisions', 'Equipment selection, historical time controls, and this compact presentation are application choices.');
  pair(list, 'Implementation trace', link('https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/POWER_ARRANGEMENT.md', 'Source-to-behavior mapping and limits'));
  result.append(list, action('Inspect local example catalogue', 'power:catalogue', () => {
    memory.focusOverride = 'power-record-select'; actions.selectPowerRecord('manifest');
  }));
  const notices = [...power.bundle.warnings, ...power.model.issues.map(issue => `${issue.message} (${issue.evidence.path || '/'})`)];
  if (notices.length) {
    result.append(node('h3', undefined, 'Unresolved or unsupported evidence'));
    const issues = node('ul', 'interpretation-notes'); for (const notice of new Set(notices)) issues.append(node('li', undefined, notice));
    result.append(issues);
  }
  return result;
}
