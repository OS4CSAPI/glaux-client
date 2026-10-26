// Optional browser verification for the Resource Details Activity-table wireframe.
const { chromium } = require(process.env.GLAUX_PLAYWRIGHT_MODULE || 'playwright-core');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');

const repo = path.resolve(__dirname, '..');
const output = process.env.GLAUX_QA_OUTPUT || path.join(repo, 'artifacts/activity-browser-qa');
const baseURL = (process.env.GLAUX_BASE_URL || 'http://127.0.0.1:5173').replace(/\/$/, '');

(async () => {
  await fs.mkdir(output, { recursive: true });
  const browser = await chromium.launch({ executablePath: process.env.GLAUX_CHROMIUM_EXECUTABLE || undefined, headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  const checks = []; const errors = []; const requests = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('request', request => requests.push({ url: request.url(), type: request.resourceType() }));
  const check = (name, passed) => { assert(passed, name); checks.push(name); };
  const visibleTypes = () => page.locator('.rd-activity-grid tbody tr').evaluateAll(rows => rows.map(row => row.dataset.resourceType));
  try {
    await page.goto(`${baseURL}/?page=resource-details-activity`);
    await page.getByRole('heading', { name: 'Resource Details View · Activity table', level: 1, exact: true }).waitFor();
    check('Direct URL opens the separate Activity-table page', new URL(page.url()).searchParams.get('page') === 'resource-details-activity');
    check('Derived page preserves the recovered 560 by 440 frame', await page.locator('#rd-module').evaluate(element => {
      const rect = element.getBoundingClientRect(); return Math.abs(rect.width - 560) <= 1 && Math.abs(rect.height - 440) <= 1;
    }));
    check('Derived page initially preserves the blank Operational Overview template state',
      await page.locator('#rd-category-operational').getAttribute('aria-selected') === 'true'
      && await page.locator('#rd-view-overview').getAttribute('aria-selected') === 'true'
      && await page.locator('.rd-activity-table').count() === 0);
    await page.locator('#rd-category-activity').click();
    check('Activity opens its Table subtab',
      await page.locator('#rd-category-activity').getAttribute('aria-selected') === 'true'
      && await page.locator('#rd-view-table').getAttribute('aria-selected') === 'true');
    check('Activity table contains exactly Observation, Command, and System Event wireframe rows',
      JSON.stringify(await visibleTypes()) === JSON.stringify(['Observation', 'Command', 'System Event']));
    check('Activity table uses the reviewed cross-resource semantic columns',
      JSON.stringify(await page.locator('.rd-activity-grid thead th').allTextContents()) === JSON.stringify([
        'Resource Type', 'Start Time', 'End Time', 'Result / Issue Time',
        'Result / Parameters / Message', 'Origin / scope', 'Status',
      ]));
    for (const [filter, expected] of [
      ['Observations', ['Observation']], ['Commands', ['Command']], ['System Events', ['System Event']],
    ]) {
      await page.getByRole('button', { name: filter, exact: true }).click();
      check(`${filter} filter shows only its resource type`, JSON.stringify(await visibleTypes()) === JSON.stringify(expected));
    }
    await page.getByRole('button', { name: 'All', exact: true }).click();
    check('All filter restores all three resource types', (await visibleTypes()).length === 3);
    check('Filters expose one pressed selection', await page.locator('.rd-activity-filter[aria-pressed="true"]').count() === 1);
    await page.locator('#rd-view-charts').click();
    check('Charts remains the unchanged blank-template canvas',
      await page.locator('.rd-activity-table').count() === 0
      && (await page.locator('#rd-content-panel').innerText()).includes('Activity / Charts'));
    await page.locator('#rd-view-table').click();
    check('Returning to Table restores the Activity wireframe', await page.locator('.rd-activity-table').count() === 1);
    check('Page makes no fixture, XHR, or remote-source requests', requests.every(request =>
      !['fetch', 'xhr'].includes(request.type) && !new URL(request.url).pathname.includes('/fixtures/')));
    check('No browser script errors', errors.length === 0);
    await page.screenshot({ path: path.join(output, 'resource-details-activity-1280.png'), fullPage: true });
  } finally {
    const result = { passed: checks.length, checks, errors, browser: browser.version(), baseURL };
    await fs.writeFile(path.join(output, 'activity-verification-results.json'), JSON.stringify(result, null, 2));
    console.log(JSON.stringify(result, null, 2));
    await browser.close();
  }
})().catch(error => { console.error(error); process.exit(1); });
