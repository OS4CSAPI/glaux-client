import './resource-details-template.css';

/** A presentation-only canvas. Source lineage and the remaining open choices are
 * recorded in Docs/Design/RESOURCE_DETAILS_TEMPLATE.md. No resource is loaded. */
const categories = [
  { id: 'operational', label: 'Operational', views: ['Overview', 'Map', 'Equipment', 'Communications', 'Condition'] },
  { id: 'activity', label: 'Activity', views: ['Table', 'Charts'] },
  { id: 'commands', label: 'Commands', views: ['Available', 'Requests'] },
  { id: 'management', label: 'Management', views: ['Record', 'Configuration', 'Sources'] },
] as const;

const defaultSize = { width: 560, height: 440 };
const reviewBounds = { minWidth: 320, maxWidth: 1200, minHeight: 280, maxHeight: 1000 };
const docsRoot = 'https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/';

export function node<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text !== undefined) element.textContent = text;
  return element;
}

/** Keyboard selection stays local; focusing a tab never loads data or performs work. */
function tabKeyboard(list: HTMLElement): void {
  list.addEventListener('keydown', event => {
    if (!(event.target instanceof HTMLButtonElement)) return;
    const tabs = Array.from(list.querySelectorAll<HTMLButtonElement>('[role="tab"]'));
    const current = tabs.indexOf(event.target);
    if (current < 0) return;
    let next: number;
    if (event.key === 'ArrowRight') next = (current + 1) % tabs.length;
    else if (event.key === 'ArrowLeft') next = (current - 1 + tabs.length) % tabs.length;
    else if (event.key === 'Home') next = 0;
    else if (event.key === 'End') next = tabs.length - 1;
    else return;
    event.preventDefault();
    tabs[next].focus(); tabs[next].click();
    tabs[next].scrollIntoView({ block: 'nearest', inline: 'nearest' });
  });
}

export interface ResourceDetailsCanvasContext {
  categoryId: string;
  view: string;
  content: HTMLElement;
}

export interface ResourceDetailsCanvasOptions {
  pageTitle?: string;
  pageIntro?: string;
  renderBlankContent?: (context: ResourceDetailsCanvasContext) => boolean;
  sourceSummary?: string;
  sourceDescription?: string;
  designRecord?: string;
}

export function renderResourceDetailsTemplate(container: HTMLElement, options: ResourceDetailsCanvasOptions = {}): void {
  container.classList.remove('experiment-index', 'details-app');
  container.classList.add('resource-template-page');
  const fragment = document.createDocumentFragment();
  const navigation = node('nav', 'experiment-navigation');
  navigation.setAttribute('aria-label', 'Experiment navigation');
  const back = node('a', undefined, 'Page index'); back.href = '/'; navigation.append(back);

  const header = node('header', 'rd-page-header');
  header.append(node('p', 'eyebrow', 'Glaux Client / Interface canvas'),
    node('h1', undefined, options.pageTitle ?? 'Resource Details View template'),
    node('p', 'rd-page-intro', options.pageIntro ?? 'Our shared starting canvas for the Resource Details View Module, using the recovered 560 × 440 working frame.'));
  fragment.append(navigation, header);

  const toolbar = node('div', 'rd-preview-toolbar');
  const sizeLabel = node('div', 'rd-size-label');
  sizeLabel.append(node('span', undefined, 'Canvas size'));
  const sizeOutput = node('output', 'rd-size-output', '560 × 440 px'); sizeOutput.id = 'rd-size-output';
  sizeOutput.setAttribute('aria-label', 'Current canvas size');
  sizeLabel.append(sizeOutput);
  const previewLabel = node('label', 'rd-preview-label', 'Content preview'); previewLabel.htmlFor = 'rd-content-preview';
  const preview = node('select'); preview.id = 'rd-content-preview';
  for (const [value, label] of [['blank', 'Blank canvas'], ['vertical', 'Vertical scrolling sample'], ['horizontal', 'Wide content sample'], ['both', 'Both scroll directions']]) {
    const option = node('option', undefined, label); option.value = value; preview.append(option);
  }
  const previewControl = node('div', 'rd-preview-control'); previewControl.append(previewLabel, preview);
  toolbar.append(sizeLabel, previewControl);

  const stage = node('div', 'rd-canvas-stage');
  stage.setAttribute('role', 'region'); stage.setAttribute('aria-label', 'Full-size module canvas');
  stage.tabIndex = 0;
  const frame = node('section', 'rd-module'); frame.id = 'rd-module';
  frame.setAttribute('aria-label', 'Resource Details View wireframe');

  const topMarking = node('div', 'rd-marking rd-marking-top', 'Marking banner · placeholder');
  const bottomMarking = node('div', 'rd-marking rd-marking-bottom', 'Marking banner · placeholder');
  const identity = node('header', 'rd-identity');
  identity.append(node('h2', 'rd-resource-name', '[Resource name]'));
  const identityFields = node('dl', 'rd-identity-fields');
  for (const [label, value] of [['Resource Type', '[Type]'], ['ID', '[ID]'], ['Source', '[Source]']]) {
    const field = node('div'); field.append(node('dt', undefined, label), node('dd', undefined, value)); identityFields.append(field);
  }
  identity.append(identityFields);

  const categoryTabs = node('div', 'rd-category-tabs rd-scrollable'); categoryTabs.id = 'rd-category-tabs';
  categoryTabs.setAttribute('role', 'tablist'); categoryTabs.setAttribute('aria-label', 'Information categories');
  const categoryPanel = node('div', 'rd-category-panel'); categoryPanel.id = 'rd-category-panel';
  categoryPanel.setAttribute('role', 'tabpanel');
  const viewTabs = node('div', 'rd-view-tabs rd-scrollable'); viewTabs.id = 'rd-subcategory-tabs';
  viewTabs.setAttribute('role', 'tablist');
  const content = node('div', 'rd-content rd-scrollable'); content.id = 'rd-content-panel';
  content.setAttribute('role', 'tabpanel'); content.tabIndex = 0;
  categoryPanel.append(viewTabs, content);

  const footer = node('footer', 'rd-module-footer');
  const refresh = node('button', 'rd-refresh', 'Refresh view'); refresh.type = 'button'; refresh.disabled = true;
  refresh.title = 'This template has no connected resource.';
  footer.append(node('span', undefined, 'Wireframe · no resource loaded'), refresh);
  frame.append(topMarking, identity, categoryTabs, categoryPanel, footer, bottomMarking);
  stage.append(frame);

  let activeCategory: typeof categories[number] = categories[0];
  const selections = new Map<string, string>(categories.map(category => [category.id, category.views[0]]));

  function renderContent(): void {
    const selectedView = selections.get(activeCategory.id)!;
    content.setAttribute('aria-labelledby', `rd-view-${selectedView.toLowerCase()}`);
    content.replaceChildren();
    content.scrollTop = 0; content.scrollLeft = 0;
    content.dataset.preview = preview.value;
    if (preview.value === 'blank') {
      if (options.renderBlankContent?.({ categoryId: activeCategory.id, view: selectedView, content })) return;
      const empty = node('div', 'rd-empty-canvas');
      empty.append(node('p', 'rd-canvas-title', 'Content canvas'), node('p', undefined, `${activeCategory.label} / ${selectedView}`));
      content.append(empty);
      return;
    }
    const sample = node('div', 'rd-layout-sample');
    sample.append(node('p', 'rd-sample-caption', 'Layout sample · no resource data'));
    if (preview.value === 'vertical') {
      for (let index = 1; index <= 18; index++) {
        const row = node('div', 'rd-sample-row');
        row.append(node('span', undefined, `Layout row ${String(index).padStart(2, '0')}`), node('span', 'rd-sample-line'));
        sample.append(row);
      }
    } else {
      const table = node('table', 'rd-sample-table');
      table.setAttribute('aria-label', 'Wide layout sample');
      const thead = node('thead'); const headings = node('tr');
      for (let column = 1; column <= 7; column++) {
        const heading = node('th', undefined, `Column ${column}`); heading.scope = 'col'; headings.append(heading);
      }
      thead.append(headings); table.append(thead);
      const tbody = node('tbody');
      const rows = preview.value === 'both' ? 18 : 3;
      for (let index = 1; index <= rows; index++) {
        const row = node('tr');
        for (let column = 1; column <= 7; column++) row.append(node('td', undefined, column === 1 ? `Layout row ${index}` : '—'));
        tbody.append(row);
      }
      table.append(tbody); sample.append(table);
    }
    content.append(sample);
  }

  function renderViewTabs(): void {
    viewTabs.replaceChildren();
    viewTabs.setAttribute('aria-label', `${activeCategory.label} views`);
    viewTabs.hidden = activeCategory.views.length < 2;
    for (const view of activeCategory.views) {
      const button = node('button', 'rd-tab', view); button.type = 'button';
      button.id = `rd-view-${view.toLowerCase()}`;
      button.setAttribute('role', 'tab'); button.setAttribute('aria-controls', content.id);
      const selected = selections.get(activeCategory.id) === view;
      button.setAttribute('aria-selected', String(selected)); button.tabIndex = selected ? 0 : -1;
      button.addEventListener('click', () => {
        selections.set(activeCategory.id, view);
        for (const sibling of viewTabs.querySelectorAll<HTMLButtonElement>('[role="tab"]')) {
          const isSelected = sibling === button;
          sibling.setAttribute('aria-selected', String(isSelected)); sibling.tabIndex = isSelected ? 0 : -1;
        }
        renderContent();
      });
      viewTabs.append(button);
    }
    renderContent();
  }

  for (const category of categories) {
    const button = node('button', 'rd-tab', category.label); button.type = 'button'; button.id = `rd-category-${category.id}`;
    button.setAttribute('role', 'tab'); button.setAttribute('aria-controls', categoryPanel.id);
    const selected = category === activeCategory;
    button.setAttribute('aria-selected', String(selected)); button.tabIndex = selected ? 0 : -1;
    button.addEventListener('click', () => {
      activeCategory = category;
      for (const sibling of categoryTabs.querySelectorAll<HTMLButtonElement>('[role="tab"]')) {
        const isSelected = sibling === button;
        sibling.setAttribute('aria-selected', String(isSelected)); sibling.tabIndex = isSelected ? 0 : -1;
      }
      categoryPanel.setAttribute('aria-labelledby', button.id);
      renderViewTabs();
    });
    categoryTabs.append(button);
  }
  categoryPanel.setAttribute('aria-labelledby', 'rd-category-operational');
  tabKeyboard(categoryTabs); tabKeyboard(viewTabs); renderViewTabs();
  preview.addEventListener('change', renderContent);

  const sizeControls = node('div', 'rd-size-controls');
  const resizeHint = node('p', 'rd-resize-hint', 'Drag the lower-right corner to resize. On a narrow screen, scroll the canvas sideways to see the full frame.');
  const reset = node('button', 'rd-small-button', 'Reset to 560 × 440'); reset.type = 'button'; reset.id = 'rd-reset-size';
  sizeControls.append(resizeHint, reset);
  const adjust = node('details', 'rd-adjust-size'); adjust.append(node('summary', undefined, 'Set canvas dimensions'));
  const dimensionsForm = node('form', 'rd-dimensions-form');
  const widthLabel = node('label', undefined, 'Width (px)'); widthLabel.htmlFor = 'rd-width';
  const widthInput = node('input'); widthInput.type = 'number'; widthInput.id = 'rd-width'; widthInput.required = true;
  widthInput.min = String(reviewBounds.minWidth); widthInput.max = String(reviewBounds.maxWidth); widthInput.step = '1'; widthInput.value = String(defaultSize.width);
  const heightLabel = node('label', undefined, 'Height (px)'); heightLabel.htmlFor = 'rd-height';
  const heightInput = node('input'); heightInput.type = 'number'; heightInput.id = 'rd-height'; heightInput.required = true;
  heightInput.min = String(reviewBounds.minHeight); heightInput.max = String(reviewBounds.maxHeight); heightInput.step = '1'; heightInput.value = String(defaultSize.height);
  const apply = node('button', 'rd-small-button', 'Apply size'); apply.type = 'submit'; apply.id = 'rd-apply-size';
  dimensionsForm.append(widthLabel, widthInput, heightLabel, heightInput, apply); adjust.append(dimensionsForm);
  const setSize = (width: number, height: number): void => {
    frame.style.width = `${width}px`; frame.style.height = `${height}px`;
    widthInput.value = String(width); heightInput.value = String(height);
    sizeOutput.value = `${width} × ${height} px`;
  };
  reset.addEventListener('click', () => { setSize(defaultSize.width, defaultSize.height); stage.scrollLeft = 0; });
  dimensionsForm.addEventListener('submit', event => {
    event.preventDefault();
    if (dimensionsForm.reportValidity()) setSize(widthInput.valueAsNumber, heightInput.valueAsNumber);
  });

  const sourceNote = node('details', 'rd-source-note'); sourceNote.append(node('summary', undefined, options.sourceSummary ?? 'Recovered specifications and open choices'));
  sourceNote.append(node('p', undefined, '560 × 440 is the earlier working frame retained in Requirements v0.8, §6.1.1. The later Working Views packet supplies the visible tab arrangement. Its temporary 640-pixel preview did not establish a new fixed-height default.'));
  sourceNote.append(node('p', undefined, options.sourceDescription ?? 'The identity area, marking bands and tab rows remain in place while content scrolls. Blank labels and optional layout samples reserve space for our future design. Tab labels remain provisional; compact spacing, scrollbar styling and resize limits are choices for this canvas.'));
  const designLink = node('a', undefined, 'Design record and source references'); designLink.href = `${docsRoot}${options.designRecord ?? 'Design/RESOURCE_DETAILS_TEMPLATE.md'}`;
  sourceNote.append(designLink);
  fragment.append(toolbar, stage, sizeControls, adjust, sourceNote);
  container.replaceChildren(fragment);

  const observer = new ResizeObserver(() => {
    const width = Math.round(frame.getBoundingClientRect().width);
    const height = Math.round(frame.getBoundingClientRect().height);
    sizeOutput.value = `${width} × ${height} px`;
    // Do not overwrite a keyboard user's unfinished dimension entry.
    if (document.activeElement !== widthInput) widthInput.value = String(width);
    if (document.activeElement !== heightInput) heightInput.value = String(height);
  });
  observer.observe(frame);
}
