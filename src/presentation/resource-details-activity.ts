import { node, renderResourceDetailsTemplate } from './resource-details-template';

type ActivityType = 'Observation' | 'Command' | 'System Event';

interface ActivityWireframeRow {
  type: ActivityType;
  start: string;
  end: string;
  resultOrIssue: string;
  content: string;
  context: string;
  status: string;
}

const rows: readonly ActivityWireframeRow[] = [
  {
    type: 'Observation',
    start: '[phenomenon time]',
    end: '[phenomenon time]',
    resultOrIssue: '[result time]',
    content: '[observation result]',
    context: '[DataStream / producer]',
    status: '—',
  },
  {
    type: 'Command',
    start: '[execution start]',
    end: '[execution end]',
    resultOrIssue: '[issue time]',
    content: '[command parameters]',
    context: '[ControlStream / receiver]',
    status: '[current status]',
  },
  {
    type: 'System Event',
    start: '[event start]',
    end: '[event end]',
    resultOrIssue: '—',
    content: '[event message]',
    context: '[System / event source]',
    status: '—',
  },
];

function renderActivityTable(content: HTMLElement): void {
  const shell = node('section', 'rd-activity-table');
  shell.setAttribute('aria-label', 'System-scoped activity table wireframe');

  const heading = node('div', 'rd-activity-heading');
  heading.append(node('h3', undefined, 'System activity'),
    node('p', undefined, 'Cross-type history · wireframe placeholders'));

  const filters = node('div', 'rd-activity-filters');
  filters.setAttribute('role', 'group');
  filters.setAttribute('aria-label', 'Activity resource type');
  const filterTypes: readonly ['All', ...ActivityType[]] = ['All', 'Observation', 'Command', 'System Event'];

  const tableRegion = node('div', 'rd-activity-table-region');
  tableRegion.tabIndex = 0;
  const table = node('table', 'rd-activity-grid');
  table.setAttribute('aria-label', 'Observations, Commands, and System Events');
  const caption = node('caption', 'visually-hidden', 'System-scoped Activity records filtered by resource type');
  const head = node('thead');
  const headingRow = node('tr');
  for (const label of ['Resource Type', 'Start Time', 'End Time', 'Result / Issue Time', 'Result / Parameters / Message', 'Origin / scope', 'Status']) {
    const cell = node('th', undefined, label); cell.scope = 'col'; headingRow.append(cell);
  }
  head.append(headingRow);
  const body = node('tbody');
  const summary = node('p', 'rd-activity-summary');
  summary.setAttribute('aria-live', 'polite');

  const renderRows = (filter: typeof filterTypes[number]): void => {
    body.replaceChildren();
    const visible = filter === 'All' ? rows : rows.filter(row => row.type === filter);
    for (const record of visible) {
      const row = node('tr');
      row.dataset.resourceType = record.type;
      const type = node('th', undefined, record.type); type.scope = 'row'; row.append(type);
      for (const value of [record.start, record.end, record.resultOrIssue, record.content, record.context, record.status]) {
        row.append(node('td', undefined, value));
      }
      body.append(row);
    }
    summary.textContent = `${visible.length} ${visible.length === 1 ? 'resource type' : 'resource types'} shown`;
  };

  for (const filter of filterTypes) {
    const label = filter === 'All' ? 'All' : `${filter}s`;
    const button = node('button', 'rd-activity-filter', label); button.type = 'button';
    button.dataset.filter = filter;
    button.setAttribute('aria-pressed', String(filter === 'All'));
    button.addEventListener('click', () => {
      for (const sibling of filters.querySelectorAll<HTMLButtonElement>('button')) {
        sibling.setAttribute('aria-pressed', String(sibling === button));
      }
      renderRows(filter);
    });
    filters.append(button);
  }

  table.append(caption, head, body);
  tableRegion.append(table);
  renderRows('All');
  shell.append(heading, filters, summary, tableRegion);
  content.append(shell);
}

export function renderResourceDetailsActivity(container: HTMLElement): void {
  renderResourceDetailsTemplate(container, {
    pageTitle: 'Resource Details View · Activity table',
    pageIntro: 'A separate review page using the unchanged Resource Details template, with the researched System-scoped Activity table added.',
    renderBlankContent({ categoryId, view, content }) {
      if (categoryId !== 'activity' || view !== 'Table') return false;
      renderActivityTable(content);
      return true;
    },
    sourceSummary: 'Activity-table source and scope',
    sourceDescription: 'Only Activity / Table differs from the blank template. It co-displays Observation, Command, and System Event resources with type filters and explicit System/member context. The placeholders define presentation roles without claiming a universal activity endpoint or operational data.',
    designRecord: 'Design/RESOURCE_DETAILS_ACTIVITY_TABLE.md',
  });
}
