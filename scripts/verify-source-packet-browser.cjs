// Step 38 read-only browser smoke for the EXISTING Resource Details profile-test page.
// Requires a running local Vite server and external playwright-core/Chromium.
// No Oracle/52North requests, device commands or deployment are performed.
// This is NOT a native OGC/CSAPI source-provenance conformance suite.
const assert = require('node:assert/strict');
const { chromium } = require(process.env.GLAUX_PLAYWRIGHT_MODULE || 'playwright-core');

const base = (process.env.GLAUX_BASE_URL || 'http://127.0.0.1:5173').replace(/\/$/, '');
const url = base + '/?page=resource-details-profile-test&case=step38-bennett';

(async () => {
  const browser = await chromium.launch({
    executablePath: process.env.GLAUX_CHROMIUM_EXECUTABLE || undefined, headless: true,
  });
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  page.setDefaultTimeout(15000);
  const errors = [];
  const requests = [];
  page.on('pageerror', err => errors.push(err.message));
  page.on('request', request => requests.push(request.url()));
  let count = 0;
  const check = (description, truth) => { assert(truth, description); count++; };
  const panel = () => page.locator('#rd-content-panel');
  const select = async (category, view) => {
    await page.locator('#rd-category-' + category).click();
    await page.locator('#rd-view-' + view).click();
  };
  const settled = async fragment => page.waitForFunction(
    value => (document.querySelector('.rdp-count')?.textContent ?? '').includes(value), fragment,
  );

  try {
    await page.goto(url);
    await settled('4 historical experiment copies');
    check('Direct Step 38 Bennett route uses the existing Resource Details template',
      await page.locator('#rd-module').count() === 1
      && await page.locator('#rdp-case-select').inputValue() === 'step38-bennett');
    check('Research standing is visible, not misrepresented as native CSAPI',
      (await panel().innerText()).includes('SOURCE_IDENTIFIED_STATION')
      && (await panel().innerText()).includes('not native CSAPI'));
    check('Bennett Overview counts two source events and four previous copies',
      (await panel().innerText()).includes('Original source-report anchors')
      && (await panel().innerText()).includes('Prior experimental API representations')
      && (await page.locator('.rdp-count').innerText()).includes('2 original source-event anchors'));

    await select('activity','table');
    const activity=await panel().innerText();
    check('Activity distinguishes two original NOAA source rows',
      activity.includes('CSV line 10130') && activity.includes('CSV line 10418')
      && activity.includes('count each original ONCE'));
    check('Activity renders both original means and exact source QA qualifier',
      activity.includes('29.1 °C') && activity.includes('27.3 °C')
      && activity.includes('"<0> "') && activity.includes('DERIVED')
      && activity.includes('UNKNOWN'));

    await select('management','record');
    const raw=await panel().innerText();
    check('Management Record retains complete raw source text and copy IDs',
      raw.includes('"F_ATemp"') && raw.includes('"<0> "')
      && raw.includes('"originalEventId"'));

    await select('operational','map');
    check('Shared Map falls back safely without an unsupported station/probe pin',
      await page.locator('.rd-map-empty').count() === 1
      && await page.locator('.rd-map-canvas').count() === 0
      && (await panel().innerText()).includes('No validated subject-specific geographic position'));

    await page.locator('#rdp-case-select').selectOption('step38-airgradient');
    await settled('0 historical experiment copies');
    await select('operational','equipment');
    const equipment=await panel().innerText();
    check('AirGradient names two PM socket components as reference equipment',
      equipment.includes('PM1') && equipment.includes('PM2')
      && equipment.includes('REFERENCE_COMPONENT'));
    await select('operational','communications');
    const properties=await panel().innerText();
    check('AirGradient displays three output fields without creating physical sensor identities',
      properties.includes('pm01') && properties.includes('pm25') && properties.includes('pm10'));

    await page.getByRole('button',{name:'Raw packet · not native CSAPI'}).click();
    check('Raw mode remains available and does not claim to be native CSAPI',
      (await panel().innerText()).includes('Uninterpreted project evidence — not native CSAPI'));
    await select('management','record');
    check('Raw mode can still inspect full original project packet',
      (await panel().innerText()).includes('"format"'));

    await page.locator('#rdp-case-select').selectOption('sck23');
    await page.getByRole('button',{name:'Candidate profile-aware'}).click();
    check('Legacy Smart Citizen case survives the Step 38 integration',
      (await page.locator('.rd-resource-name').innerText()).includes('Smart Citizen'));

    check('No live Oracle/52North or device-command requests issued by this local test page',
      requests.every(x => !/csapi-pygeoapi|\/commands(?:\/|\?)/i.test(x)));
    check('No uncaught browser script errors', errors.length === 0);
    process.stdout.write(JSON.stringify({ checks:count, result:'passed',
      scope:'local Resource Details UI, NOT native CSAPI conformance', errors },null,2)+'\n');
  } finally {
    await browser.close();
  }
})().catch(error => { process.stderr.write(String(error.stack || error)+'\n'); process.exitCode=1; });
