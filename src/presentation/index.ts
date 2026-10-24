import { examplePages, experimentHref, experimentPages } from '../experiments';

const timeZone = 'America/New_York';
const dateFormat = new Intl.DateTimeFormat('en-US', {
  timeZone, month: 'short', day: 'numeric', year: 'numeric',
});
const timeFormat = new Intl.DateTimeFormat('en-US', {
  timeZone, hour: 'numeric', minute: '2-digit', second: '2-digit', timeZoneName: 'short',
});

function element<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

/** The deployed site's entry point. Dates describe recorded page changes. */
export function renderExperimentIndex(container: HTMLElement, unknownPage = false): void {
  const body = document.createDocumentFragment();
  const header = element('header', 'index-header');
  header.append(
    element('p', 'eyebrow', 'Glaux Client / Experiment'),
    element('h1', undefined, 'Experiment index'),
    element('p', 'index-intro', 'The pages we’re building for the Resource Details View and to explore the MERLIN domain model and MPSS profile. Open a page to review its current behavior and source evidence.'),
  );
  const context = element('div', 'index-context');
  context.append(
    element('span', 'page-count', `${experimentPages.length} pages`),
    element('span', undefined, 'Resource Details wireframe'),
    element('span', undefined, `${examplePages.length} synthetic examples`),
  );
  header.append(context); body.append(header);

  if (unknownPage) {
    const notice = element('p', 'index-notice', 'That page is not in this experiment. Choose one of the pages below.');
    notice.setAttribute('role', 'status'); body.append(notice);
  }

  const guidance = element('p', 'index-date-note', 'Newest recorded updates first. Dates track changes to each page, not deployment or device data. All times are Eastern Time (America/New_York).');
  body.append(guidance);
  const list = element('ol', 'experiment-list');
  list.setAttribute('aria-label', 'Experiment pages');
  const pages = [...experimentPages].sort((a, b) => Date.parse(b.latestUpdate.at) - Date.parse(a.latestUpdate.at));
  for (const page of pages) {
    const item = element('li');
    const article = element('article', 'experiment-page'); article.dataset.pageId = page.id;
    const overview = element('div', 'experiment-description');
    const title = element('h2'); const link = element('a', 'experiment-link', page.title);
    link.href = experimentHref(page); title.append(link);
    overview.append(title, element('p', undefined, page.description));
    const open = element('a', 'open-experiment', 'Open page →'); open.href = link.href;
    open.setAttribute('aria-label', `Open ${page.title}`); overview.append(open);

    const update = element('div', 'experiment-update');
    update.append(element('h3', undefined, 'Latest update'), element('p', 'update-summary', page.latestUpdate.summary));
    const timestamp = element('time', 'update-time'); timestamp.dateTime = page.latestUpdate.at;
    const date = new Date(page.latestUpdate.at);
    timestamp.append(element('span', 'update-date', dateFormat.format(date)), element('span', 'update-clock', timeFormat.format(date)));
    update.append(timestamp);
    if (page.latestUpdate.commit) {
      const evidence = element('a', 'update-evidence', 'View recorded change');
      evidence.href = `https://github.com/OS4CSAPI/glaux-client/commit/${page.latestUpdate.commit}`;
      evidence.target = '_blank'; evidence.rel = 'noopener noreferrer';
      evidence.setAttribute('aria-label', `View recorded change for ${page.title} on GitHub`);
      update.append(evidence);
    }
    article.append(overview, update); item.append(article); list.append(item);
  }
  body.append(list);
  const footer = element('footer', 'index-footer');
  const docs = element('a', undefined, 'Project documents and source artifacts');
  docs.href = 'https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/ARTIFACT_REGISTER.md';
  const notices = element('a', undefined, 'Third-party notices'); notices.href = '/THIRD_PARTY_NOTICES.txt';
  footer.append(element('p', undefined, `The ${examplePages.length} synthetic examples offer Operator and Standard views of the same source records. The wireframe page provides a blank layout canvas.`), docs, notices);
  body.append(footer);
  container.classList.remove('details-app'); container.classList.add('experiment-index');
  container.replaceChildren(body);
}
