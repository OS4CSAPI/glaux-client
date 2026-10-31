// Independent browser verification with explicitly synthetic CSAPI responses.
const { chromium } = require(process.env.GLAUX_PLAYWRIGHT_MODULE || 'playwright-core');
const assert = require('node:assert/strict');

const origin = (process.env.GLAUX_BASE_URL || 'http://127.0.0.1:4175').replace(/\/$/, '');
const tinyPng = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jRZkAAAAASUVORK5CYII=', 'base64');
const resources = [
  { id: 'first', label: 'Synthetic first', position: { type: 'Point', coordinates: [12.5, 47.25] } },
  { id: 'second', label: 'Synthetic second', position: { type: 'Point', coordinates: [-74.006, 40.7128] } },
  { id: 'missing', label: 'Synthetic missing' },
  { id: 'invalid', label: 'Synthetic invalid', position: { type: 'Point', coordinates: [12, 100] } },
  { id: 'unsupported', label: 'Synthetic pose', position: { type: 'GeoPose', position: { lat: 47, lon: 12 } } },
  { id: 'partial', label: 'Synthetic partial', position: { type: 'Point', coordinates: [2.5, 48.5] } },
  { id: 'slow', label: 'Synthetic slow', position: { type: 'Point', coordinates: [0.5, 1.5] } },
];

(async () => {
  const browser = await chromium.launch({ executablePath: process.env.GLAUX_CHROMIUM_EXECUTABLE || undefined, headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 1000 } });
  page.setDefaultTimeout(7000);
  const failures = []; const checks = []; let failTiles = false;
  const check = (label, value) => { assert(value, label); checks.push(label); };
  page.on('pageerror', error => failures.push(error.stack || error.message));
  await page.route('**/*', async route => {
    const url = new URL(route.request().url());
    if (url.hostname === '129-80-248-53.sslip.io') {
      const path = url.pathname.replace('/csapi-pygeoapi', '');
      if (path === '/systems') return route.fulfill({ json: { features: resources } });
      const match = path.match(/^\/systems\/([^/]+)(?:\/(datastreams|deployments|subsystems))?$/);
      if (match) {
        if (match[1] === 'partial' && match[2] === 'datastreams') return route.fulfill({ status: 503, json: {} });
        if (match[1] === 'partial' && match[2] === 'deployments') await new Promise(resolve => setTimeout(resolve, 1000));
        if (match[2]) return route.fulfill({ json: { features: [] } });
        if (match[1] === 'slow') await new Promise(resolve => setTimeout(resolve, 1200));
        const found = resources.find(resource => resource.id === decodeURIComponent(match[1]));
        return route.fulfill({ json: found || {} });
      }
      return route.fulfill({ status: 404, json: {} });
    }
    if (['tiles.maps.eox.at', 'tile.openstreetmap.org'].includes(url.hostname)) {
      return failTiles ? route.abort('failed') : route.fulfill({ status: 200, contentType: 'image/png', body: tinyPng });
    }
    return route.continue();
  });
  try {
    await page.goto(`${origin}/?page=resource-details-live-map`);
    await page.locator('#live-system-select option').first().waitFor({ state: 'attached' });
    await page.locator('#rd-view-map').click();
    await page.locator('.rd-map-canvas .leaflet-marker-icon').waitFor();
    check('GeoJSON Point maps longitude first and latitude second', (await page.locator('.rd-map-status').innerText()).includes('47.25° latitude, 12.5° longitude'));
    check('Reported source coordinates remain visible', (await page.locator('.rd-map-raw').innerText()).includes('[12.5,47.25]'));
    await page.locator('.rd-map-axis').selectOption('alternate');
    check('Explicit alternate axis selection changes the displayed interpretation', (await page.locator('.rd-map-status').innerText()).includes('12.5° latitude, 47.25° longitude'));
    await page.locator('.rd-map-axis').selectOption('standard');
    await page.locator('.rd-map-basemap').selectOption('streets');
    check('Street basemap includes source attribution', (await page.locator('.leaflet-control-attribution').innerText()).includes('OpenStreetMap'));
    await page.locator('.leaflet-control-zoom-in').click();
    await page.locator('.rd-map-recenter').click();
    check('Zoom and recenter preserve the resource marker', await page.locator('.rd-map-canvas .leaflet-marker-icon').count() === 1);
    failTiles = true;
    await page.locator('.rd-map-basemap').selectOption('imagery');
    await page.locator('.rd-map-status').getByText('map tiles failed', { exact: false }).waitFor();
    check('Tile failure is reported without losing the marker', await page.locator('.rd-map-canvas .leaflet-marker-icon').count() === 1);
    failTiles = false;
    await page.locator('#live-system-select').selectOption('second');
    await page.waitForFunction(() => document.querySelector('.rd-resource-name')?.textContent === 'Synthetic second');
    await page.waitForFunction(() => document.querySelector('.rd-map-status')?.textContent?.includes('40.7128° latitude, -74.006° longitude'));
    check('Changing System replaces the position and marker', (await page.locator('.rd-map-raw').innerText()).includes('[-74.006,40.7128]') && await page.locator('.rd-map-canvas .leaflet-marker-icon').count() === 1);
    for (const id of ['missing', 'invalid', 'unsupported']) {
      await page.locator('#live-system-select').selectOption(id);
      await page.waitForFunction(name => document.querySelector('.rd-resource-name')?.textContent === name, `Synthetic ${id === 'unsupported' ? 'pose' : id}`);
      await page.locator('.rd-map-empty').waitFor();
      check(`${id} position produces a readable fallback and no stale marker`, await page.locator('.rd-map-empty').count() === 1 && await page.locator('.leaflet-marker-icon').count() === 0);
    }
    await page.locator('#live-system-select').selectOption('partial');
    await page.waitForFunction(() => document.querySelector('.rd-map-status')?.textContent?.includes('48.5° latitude, 2.5° longitude'));
    check('Location is available while related resources are still loading', (await page.locator('.rdp-count').innerText()).includes('Loading related resources'));
    await page.locator('.rd-map-axis').selectOption('alternate');
    await page.locator('.rd-map-basemap').selectOption('streets');
    await page.getByText('Some related resources failed to load', { exact: false }).waitFor();
    check('A related-resource failure leaves the selected position available', await page.locator('.rd-map-canvas .leaflet-marker-icon').count() === 1);
    check('Related-resource updates preserve the chosen map interpretation and basemap', await page.locator('.rd-map-axis').inputValue() === 'alternate' && await page.locator('.rd-map-basemap').inputValue() === 'streets');
    await page.locator('#live-system-select').selectOption('slow');
    await page.waitForTimeout(100);
    await page.locator('#live-system-select').selectOption('second');
    await page.waitForTimeout(1800);
    check('A late response for an older selection cannot replace the selected System',
      (await page.locator('#live-system-select').inputValue()) === 'second' && (await page.locator('.rd-resource-name').innerText()) === 'Synthetic second'
      && (await page.locator('.rd-map-status').innerText()).includes('40.7128° latitude, -74.006° longitude'));
    check('No uncaught browser errors', failures.length === 0);
    console.log(JSON.stringify({ passed: checks.length, checks, errors: failures }, null, 2));
  } catch (error) {
    console.error(JSON.stringify({ checks, errors: failures, identity: await page.locator('.rd-resource-name').allTextContents(), status: await page.locator('.rd-map-status').allTextContents(), panel: await page.locator('#rd-content-panel').allTextContents() }, null, 2));
    throw error;
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exit(1); });
