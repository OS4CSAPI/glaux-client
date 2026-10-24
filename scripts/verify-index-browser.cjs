// Optional, read-only verification of the experiment index and its navigation.
// Uses the same external Playwright/browser environment variables as the other browser checks.
const { chromium } = require(process.env.GLAUX_PLAYWRIGHT_MODULE || 'playwright-core');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');

const repo = path.resolve(__dirname, '..');
const output = process.env.GLAUX_QA_OUTPUT || path.join(repo, 'artifacts/index-browser-qa');
const baseURL = (process.env.GLAUX_BASE_URL || 'http://127.0.0.1:5173').replace(/\/$/, '');
const examples = [
  { id: 'power', heading: 'Demonstration field station 01', updatedAt: '2026-10-24T06:00:19-04:00' },
  { id: 'trss', heading: 'TRSS ETU-II', updatedAt: '2026-10-24T05:50:09-04:00' },
  { id: 'core2', heading: 'OmniSense Core2', updatedAt: '2026-10-24T05:50:09-04:00' },
  { id: 'core5', heading: 'OmniSense Core5ADS', updatedAt: '2026-10-24T05:50:09-04:00' },
  { id: 'mpss', heading: 'MPSS technical-description contract example', updatedAt: '2026-10-24T05:50:09-04:00' },
];
const template = {
  id: 'resource-details-template',
  heading: 'Resource Details View template',
  updatedAt: '2026-10-24T16:24:47-04:00',
};
const pages = [template, ...examples];
const pageHref = entry => `/?${entry.id === template.id ? 'page' : 'example'}=${entry.id}`;

(async () => {
  await fs.mkdir(output, { recursive: true });
  const browser = await chromium.launch({
    executablePath: process.env.GLAUX_CHROMIUM_EXECUTABLE || undefined,
    headless: true,
  });
  const page = await browser.newPage({ viewport: { width: 1280, height: 1000 } });
  page.setDefaultTimeout(10000);
  const checks = [];
  const errors = [];
  const requests = [];
  const screenshots = [];
  let failure;
  page.on('pageerror', error => errors.push(error.message));
  page.on('request', request => requests.push({ url: request.url(), type: request.resourceType() }));
  const check = (name, passed) => { assert(passed, name); checks.push(name); };
  const waitForIndex = () => page.getByRole('heading', { name: 'Experiment index', level: 1, exact: true }).waitFor();
  const waitForExample = example => page.getByRole('heading', { name: example.heading, exact: true }).waitFor();
  const waitForTemplate = () => page.getByRole('heading', { name: template.heading, level: 1, exact: true }).waitFor();
  const titleLink = id => page.locator(`article.experiment-page[data-page-id="${id}"] h2 a`);
  const noOverflow = () => page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth);
  const screenshot = async filename => {
    await page.screenshot({ path: path.join(output, filename), fullPage: true });
    screenshots.push(filename);
  };
  const noSourceReads = list => list.every(request =>
    !['fetch', 'xhr'].includes(request.type)
    && !new URL(request.url).pathname.includes('/fixtures/')
    && (!request.url.startsWith('http') || new URL(request.url).origin === new URL(baseURL).origin));

  try {
    await page.goto(`${baseURL}/`);
    await waitForIndex();
    await page.waitForLoadState('networkidle');
    check('Root opens the experiment index without a fixture or remote source read', noSourceReads(requests));
    check('Index contains the template and five existing example pages', await page.locator('article.experiment-page').count() === pages.length);
    check('Newest page is listed first', await page.locator('article.experiment-page h2 a').first().getAttribute('href') === pageHref(template));
    for (const entry of pages) {
      const link = titleLink(entry.id);
      const article = page.locator(`article.experiment-page[data-page-id="${entry.id}"]`);
      const text = await article.innerText();
      const time = article.locator('time[datetime]');
      const value = await time.getAttribute('datetime');
      check(`Page metadata includes a title, description and latest update: ${entry.id}`,
        await link.count() === 1 && (await link.innerText()).trim().length > 3
        && await link.getAttribute('href') === pageHref(entry)
        && (await article.locator('.experiment-description p').innerText()).trim().length > 30
        && text.toLowerCase().includes('latest update')
        && (await article.locator('.update-summary').innerText()).trim().length > 30);
      check(`Page timestamp matches its recorded implementation change: ${entry.id}`,
        await time.count() === 1 && Number.isFinite(Date.parse(value))
        && Date.parse(value) === Date.parse(entry.updatedAt)
        && /EDT|EST|Eastern/.test(await time.innerText()));
    }
    check('Desktop index has no horizontal overflow', await noOverflow());
    await screenshot('experiment-index-1280.png');
    const initialTimes = await page.locator('article.experiment-page time').evaluateAll(elements => elements.map(element => element.dateTime));
    await page.reload();
    await waitForIndex();
    check('Reload preserves recorded page dates', JSON.stringify(initialTimes)
      === JSON.stringify(await page.locator('article.experiment-page time').evaluateAll(elements => elements.map(element => element.dateTime))));

    const templateStart = requests.length;
    await titleLink(template.id).click();
    await waitForTemplate();
    await page.waitForLoadState('networkidle');
    check('Template index link opens the standalone layout page',
      new URL(page.url()).searchParams.get('page') === template.id
      && new URL(page.url()).searchParams.get('example') === null
      && await page.locator('#example-select').count() === 0);
    check('Template opens without a fixture or remote source read', noSourceReads(requests.slice(templateStart)));
    await page.reload();
    await waitForTemplate();
    await page.waitForLoadState('networkidle');
    check('Reload preserves the template route without a source read',
      new URL(page.url()).searchParams.get('page') === template.id
      && noSourceReads(requests.slice(templateStart)));
    await page.getByRole('link', { name: 'Page index', exact: true }).click();
    await waitForIndex();
    check('Template returns to the index', new URL(page.url()).search === '');

    for (const example of examples) {
      await titleLink(example.id).click();
      await waitForExample(example);
      check(`Index link opens the correct example: ${example.id}`,
        await page.locator('#example-select').inputValue() === example.id
        && new URL(page.url()).searchParams.get('example') === example.id
        && await page.locator('#details-tab-overview').getAttribute('aria-selected') === 'true');
      await page.getByRole('link', { name: 'Page index', exact: true }).click();
      await waitForIndex();
      check(`Example returns to the index: ${example.id}`, new URL(page.url()).searchParams.get('example') === null);
    }

    await titleLink('power').click();
    await waitForExample(examples[0]);
    check('Data example selector retains five examples and excludes the template',
      JSON.stringify(await page.locator('#example-select option:not([disabled])').evaluateAll(options => options.map(option => option.value).sort()))
      === JSON.stringify(examples.map(example => example.id).sort()));
    await page.goBack();
    await waitForIndex();
    check('Browser Back returns from an example to the index', new URL(page.url()).searchParams.get('example') === null);
    await page.goForward();
    await waitForExample(examples[0]);
    check('Browser Forward restores the linked example', await page.locator('#example-select').inputValue() === 'power');
    await page.locator('#example-select').selectOption('core2');
    await waitForExample(examples.find(example => example.id === 'core2'));
    check('Changing the example keeps its URL in sync', new URL(page.url()).searchParams.get('example') === 'core2');
    await page.reload();
    await waitForExample(examples.find(example => example.id === 'core2'));
    check('Reload retains the selected example', await page.locator('#example-select').inputValue() === 'core2');
    await page.goBack();
    await waitForIndex();
    check('Dropdown selection does not add an extra history entry', new URL(page.url()).searchParams.get('example') === null);

    const unknownStart = requests.length;
    await page.goto(`${baseURL}/?example=unknown-index-check`);
    await waitForIndex();
    await page.waitForLoadState('networkidle');
    check('Unknown example opens an index notice without reading a fixture',
      await page.locator('[role="status"], [role="alert"]').count() > 0
      && noSourceReads(requests.slice(unknownStart))
      && await page.locator('#example-select').count() === 0);

    const unknownPageStart = requests.length;
    await page.goto(`${baseURL}/?page=unknown-index-check`);
    await waitForIndex();
    await page.waitForLoadState('networkidle');
    check('Unknown template route opens an index notice without reading a fixture',
      await page.locator('[role="status"], [role="alert"]').count() > 0
      && noSourceReads(requests.slice(unknownPageStart))
      && await page.locator('#example-select').count() === 0);

    await page.goto(`${baseURL}/`);
    await waitForIndex();
    const firstLink = titleLink(template.id);
    let focused = false;
    for (let attempt = 0; attempt < 20 && !focused; attempt++) {
      await page.keyboard.press('Tab');
      focused = await firstLink.evaluate(element => document.activeElement === element);
    }
    check('Index page links are keyboard reachable with a visible focus indicator',
      focused && await firstLink.evaluate(element => getComputedStyle(element).outlineStyle !== 'none'
        || getComputedStyle(element).boxShadow !== 'none'));
    await page.keyboard.press('Enter');
    await waitForTemplate();
    check('Enter opens the focused page link', new URL(page.url()).searchParams.get('page') === template.id);
    await page.getByRole('link', { name: 'Page index', exact: true }).click();
    await waitForIndex();
    await page.setViewportSize({ width: 390, height: 844 });
    check('Mobile index has no horizontal overflow', await noOverflow());
    check('Mobile titles and update dates remain within the viewport',
      await page.locator('article.experiment-page h2 a, article.experiment-page time').evaluateAll(elements => elements.every(element => {
        const rect = element.getBoundingClientRect();
        return rect.left >= 0 && rect.right <= window.innerWidth;
      })));
    await screenshot('experiment-index-390.png');
    check('No browser script errors', errors.length === 0);
  } catch (error) {
    failure = error.stack || String(error);
    await page.screenshot({ path: path.join(output, 'experiment-index-failure.png'), fullPage: true }).catch(() => {});
  } finally {
    const result = { passed: checks.length, checks, errors, browser: browser.version(), baseURL, screenshots,
      ...(failure ? { failure } : {}) };
    await fs.writeFile(path.join(output, 'index-verification-results.json'), JSON.stringify(result, null, 2));
    console.log(JSON.stringify(result, null, 2));
    await browser.close();
  }
  if (failure) process.exitCode = 1;
})().catch(error => { console.error(error); process.exitCode = 1; });
