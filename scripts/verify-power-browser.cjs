// Optional, read-only browser verification for the connected synthetic power example.
// Uses the same external Playwright/browser environment variables as verify-browser.cjs.
const { chromium } = require(process.env.GLAUX_PLAYWRIGHT_MODULE || 'playwright-core');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');

const repo = path.resolve(__dirname, '..');
const output = process.env.GLAUX_QA_OUTPUT || path.join(repo, 'artifacts/power-browser-qa');
const baseURL = (process.env.GLAUX_BASE_URL || 'http://127.0.0.1:5173').replace(/\/$/, '');
const fixtureDirectory = path.join(repo, 'public/fixtures/power-arrangement');
const refs = {
  station: 'https://demo.example/csapi/systems/station-01',
  a: 'https://demo.example/csapi/systems/power-a',
  b: 'https://demo.example/csapi/systems/power-b',
  deployment: 'https://demo.example/csapi/deployments/site-01',
};
const times = {
  before: '2026-09-01T08:00:00Z',
  swap: '2026-09-02T10:00:00Z',
  after: '2026-09-02T10:10:00Z',
};
const labels = {
  station: 'Demonstration field station 01',
  a: 'Demonstration external source A',
  b: 'Demonstration external source B',
};

(async () => {
  await fs.mkdir(output, { recursive: true });
  const manifestBytes = await fs.readFile(path.join(fixtureDirectory, 'manifest.json'));
  const manifest = JSON.parse(manifestBytes.toString());
  const browser = await chromium.launch({
    executablePath: process.env.GLAUX_CHROMIUM_EXECUTABLE || undefined,
    headless: true,
  });
  const page = await browser.newPage({ viewport: { width: 1280, height: 1000 }, acceptDownloads: true });
  page.setDefaultTimeout(10000);
  const checks = [];
  const errors = [];
  const requests = [];
  const screenshots = [];
  let failure;
  page.on('pageerror', error => errors.push(error.message));
  page.on('request', request => requests.push({ url: request.url(), method: request.method(), type: request.resourceType() }));
  // The example must resolve canonical identities locally, never fetch these hosts.
  await page.route(/^https?:\/\/(demo|schemas)\.example\//, route => route.abort());
  const check = (name, passed) => { assert(passed, name); checks.push(name); };
  const panel = tab => page.locator(`#details-panel-${tab}`);
  const visiblePanel = () => page.locator('.tab-panel:visible');
  const entityButton = (tab, ref) => panel(tab).locator(`.power-entity-button[data-entity-ref="${ref}"]`);
  const metadata = (scope, label) => scope.locator('.metadata-row')
    .filter({ has: page.locator('dt').getByText(label, { exact: true }) }).locator('dd').innerText();
  const selectTab = async tab => page.getByRole('tab', {
    name: tab[0].toUpperCase() + tab.slice(1), exact: true,
  }).click();
  const openDetails = async locator => {
    if (!await locator.evaluate(element => element.open)) await locator.locator(':scope > summary').click();
  };
  const screenshot = async filename => {
    await page.screenshot({ path: path.join(output, filename), fullPage: true });
    screenshots.push(filename);
  };
  const noOverflow = () => page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth);
  const waitForPower = async () => {
    await page.locator('#power-time-select').waitFor();
    await page.waitForFunction(() => document.querySelector('.system-card')?.getAttribute('aria-busy') === 'false');
  };
  const originalText = async () => {
    const capture = page.locator('.standard-view .capture').first();
    await openDetails(capture);
    const body = capture.locator('.capture-part').filter({ has: page.getByText('Original response text', { exact: true }) });
    await openDetails(body);
    return body.locator('pre').textContent();
  };
  const downloadOriginal = async () => {
    const pending = page.waitForEvent('download');
    await page.getByRole('button', { name: 'Download original body', exact: true }).click();
    const download = await pending;
    return fs.readFile(await download.path());
  };
  const arrangementRefs = () => panel('overview').locator('.power-arrangement-row .power-entity-button')
    .evaluateAll(elements => elements.map(element => element.dataset.entityRef));

  try {
    await page.goto(`${baseURL}/?example=power`);
    await waitForPower();
    check('Power deep-link opens the synthetic example in Overview',
      await page.locator('#example-select').inputValue() === 'power'
      && await page.locator('#details-tab-overview').getAttribute('aria-selected') === 'true'
      && (await page.locator('.source-notice').innerText()).includes('Synthetic'));
    check('Default historical arrangement is source B supplying the unchanged station',
      await page.locator('#power-time-select').inputValue() === times.after
      && JSON.stringify(await arrangementRefs()) === JSON.stringify([refs.b, refs.station])
      && await panel('overview').locator('.power-arrangement-row').getAttribute('data-relationship-id') === 'power-after'
      && await panel('overview').locator('.power-inspection').getAttribute('data-selected-entity') === refs.b);
    const reading = panel('overview').locator('.power-reading[data-observation-id="power-01"]');
    check('Voltage retains its unit, external-source subject, separate reporter and measurement point',
      await reading.locator('.hero-value').innerText() === '12.6 V'
      && await metadata(reading, 'Describes') === labels.b
      && await metadata(reading, 'Reported by') === labels.station
      && await metadata(reading, 'Measurement point') === 'Supply output terminals');
    check('Observation and replacement retain distinct historical instants',
      await reading.locator('time').getAttribute('datetime') === times.after
      && await panel('overview').locator('.power-history-event[data-event-id="event-swap"] time').getAttribute('datetime') === times.swap
      && await metadata(panel('overview').locator('.power-history-event'), 'Removed') === labels.a
      && await metadata(panel('overview').locator('.power-history-event'), 'Installed') === labels.b);
    const primaryLabels = await panel('overview').locator('dt:visible, h3:visible, h4:visible, .power-entity-name:visible').allTextContents();
    check('Overview invents no battery identity, physical interface, charge percentage, runtime or readiness metric',
      !primaryLabels.some(label => /\bbattery\b|\binterface\b|state of charge|remaining runtime|readiness/i.test(label))
      && !(await reading.locator('.hero-value').innerText()).includes('%')
      && (await page.locator('.power-context').innerText()).includes('do not measure power flow'));
    check('Desktop layout has no horizontal document overflow', await noOverflow());
    await screenshot('power-after-overview-1280.png');

    const readingEvidence = reading.locator('.power-evidence');
    await openDetails(readingEvidence);
    const evidenceText = await readingEvidence.innerText();
    check('Reading evidence exposes original observation, stream, schema and producer output locators',
      ['18_power_observation.json', '16_power_stream.json', '17_power_schema.json', '02_station.sml.json',
        '/resultSchema', '/outputs/2', 'Exact source path', 'Retrieved at'].every(value => evidenceText.includes(value)));
    await readingEvidence.getByRole('button', { name: 'Inspect original record', exact: true }).first().click();
    check('Inspect original record opens the matching record and retains keyboard focus',
      await page.locator('#power-record-select').inputValue() === 'observation'
      && await page.locator('#power-record-select').evaluate(element => document.activeElement === element));

    for (const record of [...manifest.records, { role: 'manifest', file: 'manifest.json' }]) {
      await page.locator('#power-record-select').selectOption(record.role);
      const expected = record.role === 'manifest' ? manifestBytes : await fs.readFile(path.join(fixtureDirectory, record.file));
      check(`Original text and downloaded bytes are unchanged: ${record.role}`,
        await originalText() === expected.toString() && (await downloadOriginal()).equals(expected));
    }
    await page.locator('#power-record-select').selectOption('deployment');
    const deploymentText = await originalText();
    check('Unrelated native deployment content remains accessible in Standard view',
      deploymentText.includes('communication-link') && deploymentText.includes('event-service-review')
      && deploymentText.includes('controlstreams'));

    await page.getByRole('button', { name: 'Operator view', exact: true }).click();
    check('Reading disclosure survives record inspection and return to Operator view',
      await panel('overview').locator('.power-reading .power-evidence').evaluate(element => element.open));
    await panel('overview').locator('.power-reading .power-evidence > summary').click();
    await page.locator('#power-time-select').focus();
    await page.keyboard.press('Home');
    await page.waitForFunction(value => document.querySelector('#power-time-select')?.value === value, times.before);
    check('Keyboard time selection preserves focus and shows source A before replacement',
      await page.locator('#power-time-select').evaluate(element => document.activeElement === element)
      && JSON.stringify(await arrangementRefs()) === JSON.stringify([refs.a, refs.station])
      && await panel('overview').locator('.power-inspection').getAttribute('data-selected-entity') === refs.a);
    check('Earlier arrangement shows no future voltage and labels the replacement as later',
      !(await visiblePanel().innerText()).includes('12.6')
      && await panel('overview').locator('.power-reading').count() === 0
      && (await panel('overview').locator('.power-no-reading').innerText()).includes('No observation')
      && (await panel('overview').locator('.power-history-status').innerText()).includes('Later in this example'));
    await screenshot('power-before-overview-1280.png');
    await selectTab('equipment');
    await entityButton('equipment', refs.b).click();
    await selectTab('condition');
    check('Inspecting source B early does not reveal its later observation',
      await panel('condition').locator('.power-reading').count() === 0
      && !(await panel('condition').innerText()).includes('12.6'));
    await page.getByRole('button', { name: 'Standard view', exact: true }).click();
    await page.locator('#power-record-select').selectOption('observation');
    check('Future observation remains retained in original records at an earlier arrangement time',
      (await originalText()).includes('"result": 12.6') && (await originalText()).includes(times.after));
    await page.getByRole('button', { name: 'Operator view', exact: true }).click();
    await selectTab('overview');
    await page.locator('#power-time-select').selectOption(times.swap);
    check('Exact replacement boundary selects only source B and still withholds the later voltage',
      JSON.stringify(await arrangementRefs()) === JSON.stringify([refs.b, refs.station])
      && await panel('overview').locator('.power-reading').count() === 0
      && !(await visiblePanel().innerText()).includes('12.6')
      && (await panel('overview').locator('.power-history-status').innerText()).includes('Recorded change'));
    await selectTab('condition');
    check('Condition also withholds the 10:10 observation at the 10:00 replacement instant',
      await panel('condition').locator('.power-reading').count() === 0
      && !(await panel('condition').innerText()).includes('12.6'));
    await selectTab('overview');
    await screenshot('power-at-replacement-1280.png');
    await page.locator('#power-time-select').focus();
    await page.keyboard.press('End');
    await page.waitForFunction(value => document.querySelector('#power-time-select')?.value === value, times.after);
    check('Returning to the observation instant restores the original source B reading',
      await panel('overview').locator('.power-reading').count() === 1
      && await metadata(panel('overview').locator('.power-reading'), 'Describes') === labels.b);

    await selectTab('equipment');
    const equipmentRefs = await panel('equipment').locator('.power-entity-button').evaluateAll(elements => elements.map(element => element.dataset.entityRef));
    check('Equipment contains exactly the two external sources and the station, with no invented interface',
      JSON.stringify([...equipmentRefs].sort()) === JSON.stringify([refs.a, refs.b, refs.station].sort()));
    const oldSource = entityButton('equipment', refs.a);
    await oldSource.focus();
    await page.keyboard.press('Space');
    check('Keyboard equipment selection preserves focus, selected state and a visible focus indicator',
      await oldSource.getAttribute('aria-pressed') === 'true'
      && await oldSource.evaluate(element => document.activeElement === element && getComputedStyle(element).outlineStyle !== 'none')
      && await panel('equipment').locator('.power-inspection').getAttribute('data-selected-entity') === refs.a);
    check('Former source A has no invented or reassigned observation',
      await panel('equipment').locator('.power-reading').count() === 0
      && (await panel('equipment').locator('.power-no-reading').innerText()).includes('No observation'));
    await screenshot('power-source-a-equipment-1280.png');
    await selectTab('condition');
    check('Source A condition remains empty after replacement',
      await panel('condition').locator('.power-reading').count() === 0
      && !(await panel('condition').innerText()).includes('12.6'));
    await selectTab('equipment');
    await entityButton('equipment', refs.station).click();
    await selectTab('condition');
    check('Station condition separates its missing own observation from a report about source B',
      await panel('condition').locator('.power-no-reading').count() === 1
      && await panel('condition').getByRole('heading', { name: 'Reports about other equipment', exact: true }).count() === 1
      && await metadata(panel('condition').locator('.power-reading'), 'Describes') === labels.b
      && await metadata(panel('condition').locator('.power-reading'), 'Reported by') === labels.station);
    await screenshot('power-station-condition-1280.png');
    await page.getByRole('tab', { name: 'Condition', exact: true }).focus();
    await page.keyboard.press('Home');
    check('Power tabs retain Home navigation and focus',
      await page.locator('#details-tab-overview').evaluate(element => document.activeElement === element && element.getAttribute('aria-selected') === 'true'));
    await entityButton('overview', refs.b).click();
    const identity = panel('overview').locator('.power-inspection > .power-evidence');
    await identity.locator(':scope > summary').focus();
    await page.keyboard.press('Space');
    await selectTab('condition');
    await selectTab('overview');
    check('Keyboard-opened equipment evidence survives tab changes', await identity.evaluate(element => element.open));
    await identity.locator(':scope > summary').click();
    const historicalTime = await panel('overview').locator('.power-reading time').getAttribute('datetime');
    await page.getByRole('button', { name: 'Refresh view', exact: true }).click();
    await waitForPower();
    check('Refresh preserves selected source, historical arrangement and observation time',
      await page.locator('#power-time-select').inputValue() === times.after
      && await panel('overview').locator('.power-inspection').getAttribute('data-selected-entity') === refs.b
      && await panel('overview').locator('.power-reading time').getAttribute('datetime') === historicalTime
      && await page.getByRole('button', { name: 'Refresh view', exact: true }).evaluate(element => document.activeElement === element));

    await page.setViewportSize({ width: 390, height: 844 });
    check('Mobile Overview preserves source and station cards without horizontal overflow',
      await noOverflow() && await panel('overview').locator('.power-arrangement-row .power-entity-button').count() === 2);
    await screenshot('power-after-overview-390.png');
    await selectTab('equipment');
    check('Mobile Equipment keeps all three selectable identities within the viewport',
      await noOverflow() && await panel('equipment').locator('.power-entity-button').evaluateAll(elements =>
        elements.length === 3 && elements.every(element => {
          const rect = element.getBoundingClientRect();
          return rect.left >= 0 && rect.right <= window.innerWidth && rect.height >= 40;
        })));
    await screenshot('power-equipment-390.png');
    await selectTab('condition');
    check('Mobile Condition retains value, subject, reporter, point and observation time',
      await noOverflow() && await metadata(panel('condition').locator('.power-reading'), 'Describes') === labels.b
      && await metadata(panel('condition').locator('.power-reading'), 'Reported by') === labels.station
      && await panel('condition').locator('.power-reading time').getAttribute('datetime') === times.after);
    await screenshot('power-source-b-condition-390.png');
    await openDetails(panel('condition').locator('.power-reading .power-evidence'));
    check('Expanded mobile provenance remains readable without horizontal overflow', await noOverflow());
    await screenshot('power-evidence-390.png');

    await page.setViewportSize({ width: 1280, height: 1000 });
    await page.locator('#example-select').selectOption('core2');
    await page.getByRole('heading', { name: 'OmniSense Core2', exact: true }).waitFor();
    check('Changing examples removes power controls and does not lend voltage to Core2',
      await page.locator('#power-time-select').count() === 0 && await page.locator('.power-reading').count() === 0
      && !(await panel('condition').innerText()).includes('12.6'));
    await page.locator('#example-select').selectOption('power');
    await waitForPower();
    check('Returning to power starts a coherent Overview with the source B observation',
      await page.locator('#details-tab-overview').getAttribute('aria-selected') === 'true'
      && await panel('overview').locator('.power-inspection').getAttribute('data-selected-entity') === refs.b);

    // One targeted rendered regression: an addressable Event is not equipment.
    const deployment = JSON.parse(await fs.readFile(path.join(fixtureDirectory, '08_site_deployment.sml.json'), 'utf8'));
    const invalidRef = `${refs.deployment}#event-swap`;
    deployment.characteristics[4].characteristics[0].value = invalidRef;
    const changedDeployment = JSON.stringify(deployment, null, 2);
    await page.route('**/fixtures/power-arrangement/08_site_deployment.sml.json', route =>
      route.fulfill({ status: 200, contentType: 'application/sml+json', body: changedDeployment }));
    await page.reload();
    await waitForPower();
    await selectTab('equipment');
    const rejectedRefs = await panel('equipment').locator('.power-entity-button').evaluateAll(elements => elements.map(element => element.dataset.entityRef));
    check('Invalid Event relationship endpoint never becomes a selectable equipment item',
      !rejectedRefs.includes(invalidRef) && !rejectedRefs.includes(refs.b)
      && JSON.stringify([...rejectedRefs].sort()) === JSON.stringify([refs.a, refs.station].sort()));
    await openDetails(page.locator('.power-basis'));
    const issueText = await page.locator('.power-basis').innerText();
    check('Rejected endpoint has an accessible explanation and exact evidence path',
      issueText.includes('not equipment or a Power Interface')
      && issueText.includes('/characteristics/4/characteristics/0'));
    await screenshot('power-invalid-endpoint-1280.png');
    await page.getByRole('button', { name: 'Standard view', exact: true }).click();
    await page.locator('#power-record-select').selectOption('deployment');
    check('Rejected endpoint remains byte-preserved and inspectable in its original record',
      await originalText() === changedDeployment && (await downloadOriginal()).equals(Buffer.from(changedDeployment)));

    check('Example retrieval uses only local GET requests without canonical host traversal',
      requests.every(request => request.method === 'GET')
      && requests.filter(request => ['fetch', 'xhr'].includes(request.type)).every(request => new URL(request.url).origin === new URL(baseURL).origin));
    check('No browser script errors', errors.length === 0);
  } catch (error) {
    failure = error.stack || String(error);
    await page.screenshot({ path: path.join(output, 'power-failure.png'), fullPage: true }).catch(() => {});
  } finally {
    const result = { passed: checks.length, checks, errors, browser: browser.version(), baseURL, screenshots,
      ...(failure ? { failure } : {}) };
    await fs.writeFile(path.join(output, 'power-verification-results.json'), JSON.stringify(result, null, 2));
    console.log(JSON.stringify(result, null, 2));
    await browser.close();
  }
  if (failure) process.exitCode = 1;
})().catch(error => { console.error(error); process.exitCode = 1; });
