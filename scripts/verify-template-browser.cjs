// Read-only browser checks for the recovered Resource Details View shell.
// Uses the external Playwright/Chromium configuration shared by the other checks.
const { chromium } = require(process.env.GLAUX_PLAYWRIGHT_MODULE || 'playwright-core');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');

const repo = path.resolve(__dirname, '..');
const output = process.env.GLAUX_QA_OUTPUT || path.join(repo, 'artifacts/template-browser-qa');
const baseURL = (process.env.GLAUX_BASE_URL || 'http://127.0.0.1:5173').replace(/\/$/, '');
const ignoreHTTPSErrors = process.env.GLAUX_IGNORE_HTTPS_ERRORS === '1';
const route = '/?page=resource-details-template';
const fixedSelectors = ['.rd-marking-top', '.rd-identity', '#rd-category-tabs', '#rd-subcategory-tabs', '.rd-marking-bottom'];
const approximately = (actual, expected) => Math.abs(actual - expected) <= 1;

(async () => {
  await fs.mkdir(output, { recursive: true });
  const browser = await chromium.launch({
    executablePath: process.env.GLAUX_CHROMIUM_EXECUTABLE || undefined,
    headless: true,
    // Preserve native scrollbar rendering for the scrollbar-focused visual review.
    ignoreDefaultArgs: ['--hide-scrollbars'],
  });
  const page = await browser.newPage({
    viewport: { width: 1280, height: 960 },
    ignoreHTTPSErrors,
  });
  page.setDefaultTimeout(10000);
  const checks = [];
  const errors = [];
  const requests = [];
  const screenshots = [];
  let failure;
  page.on('pageerror', error => errors.push(error.message));
  page.on('request', request => requests.push({ url: request.url(), type: request.resourceType() }));
  const check = (name, passed) => { assert(passed, name); checks.push(name); };
  const panel = () => page.locator('#rd-content-panel');
  const selectedAndFocused = locator => locator.evaluate(element =>
    element.getAttribute('aria-selected') === 'true' && document.activeElement === element);
  const waitForTemplate = () => page.getByRole('heading', {
    name: 'Resource Details View template', level: 1, exact: true,
  }).waitFor();
  const frame = () => page.locator('#rd-module').boundingBox();
  const isSize = (box, width, height) => box && approximately(box.width, width) && approximately(box.height, height);
  const scrollState = () => panel().evaluate(element => ({
    horizontal: element.scrollWidth > element.clientWidth + 1,
    vertical: element.scrollHeight > element.clientHeight + 1,
    left: element.scrollLeft,
    top: element.scrollTop,
    width: element.clientWidth,
    height: element.clientHeight,
  }));
  const fixedGeometry = () => page.evaluate(selectors => {
    const module = document.querySelector('#rd-module').getBoundingClientRect();
    return selectors.map(selector => {
      const rect = document.querySelector(selector).getBoundingClientRect();
      return { selector, top: rect.top - module.top, left: rect.left - module.left, width: rect.width, height: rect.height };
    });
  }, fixedSelectors);
  const sameGeometry = (before, after) => before.every((rect, index) =>
    ['top', 'left', 'width', 'height'].every(key => approximately(rect[key], after[index][key])));
  const choosePreview = async value => {
    await page.locator('#rd-content-preview').selectOption(value);
    await page.waitForFunction(expected => document.querySelector('#rd-content-preview').value === expected, value);
  };
  const screenshot = async name => {
    await page.screenshot({ path: path.join(output, name), fullPage: true });
    screenshots.push(name);
  };
  const onlyLocalShellRequests = () => requests.every(request =>
    !['fetch', 'xhr'].includes(request.type)
    && !new URL(request.url).pathname.includes('/fixtures/')
    && (!request.url.startsWith('http') || new URL(request.url).origin === new URL(baseURL).origin));

  try {
    await page.goto(`${baseURL}${route}`);
    await waitForTemplate();
    await page.waitForLoadState('networkidle');
    check('Direct URL opens the standalone template without an example selector',
      new URL(page.url()).searchParams.get('page') === 'resource-details-template'
      && await page.locator('#example-select').count() === 0);
    check('Default module preserves the recovered 560 by 440 CSS-pixel frame', isSize(await frame(), 560, 440));
    check('Default selection opens Operational and Overview with a blank canvas',
      await page.locator('#rd-category-operational').getAttribute('aria-selected') === 'true'
      && await page.locator('#rd-view-overview').getAttribute('aria-selected') === 'true'
      && await page.locator('#rd-content-preview').inputValue() === 'blank');
    check('Identity, adjacent tab rows, and both marking strips surround the content area',
      await page.evaluate(() => {
        const box = selector => document.querySelector(selector).getBoundingClientRect();
        const [module, top, identity, categories, views, content, bottom] =
          ['#rd-module', '.rd-marking-top', '.rd-identity', '#rd-category-tabs', '#rd-subcategory-tabs', '#rd-content-panel', '.rd-marking-bottom'].map(box);
        return top.top >= module.top && top.bottom <= identity.top + 1
          && identity.bottom <= categories.top + 1
          && Math.abs(categories.bottom - views.top) <= 2
          && views.bottom <= content.top + 1 && content.bottom <= bottom.top + 1
          && bottom.bottom <= module.bottom;
      }));
    const blankState = await scrollState();
    check('Blank content fits without scrolling or a reserved scrollbar gutter',
      !blankState.horizontal && !blankState.vertical
      && await panel().evaluate(element => {
        const style = getComputedStyle(element);
        const border = parseFloat(style.borderLeftWidth) + parseFloat(style.borderRightWidth);
        return element.offsetWidth - element.clientWidth - border <= 1
          && style.scrollbarGutter === 'auto';
      }));
    check('The shell contains no device names or readings borrowed from the data examples',
      !/TRSS|OmniSense|Demonstration field station|15\.43\s*V|12\.6\s*V|SEISMIC\/ACOUSTIC|IRID-II/.test(await page.locator('#rd-module').innerText()));
    await screenshot('template-default-560.png');

    await choosePreview('vertical');
    let scrolling = await scrollState();
    check('Vertical overflow stays inside the unchanged default frame without horizontal scrolling',
      scrolling.vertical && !scrolling.horizontal && isSize(await frame(), 560, 440));
    const bandsBeforeScroll = await fixedGeometry();
    const documentScrollBefore = await page.evaluate(() => window.scrollY);
    await panel().focus();
    await page.keyboard.press('PageDown');
    await page.waitForFunction(() => document.querySelector('#rd-content-panel').scrollTop > 0);
    check('Keyboard scrolling moves content while identity, tabs, and markings remain stationary',
      (await scrollState()).top > 0
      && sameGeometry(bandsBeforeScroll, await fixedGeometry())
      && approximately(documentScrollBefore, await page.evaluate(() => window.scrollY)));
    check('Overflow scrollbars use visible thin native styling and appear only as needed',
      await panel().evaluate(element => {
        const style = getComputedStyle(element);
        const fallback = parseFloat(getComputedStyle(element, '::-webkit-scrollbar').width);
        return style.overflowY === 'auto' && style.overflowX === 'auto'
          && style.scrollbarWidth !== 'none'
          && (style.scrollbarWidth === 'thin' || Number.isFinite(fallback) && fallback > 0 && fallback <= 12);
      }));
    await screenshot('template-vertical-scrolled.png');

    await choosePreview('horizontal');
    scrolling = await scrollState();
    check('Wide content scrolls horizontally without making the module wider or creating vertical overflow',
      scrolling.horizontal && !scrolling.vertical && isSize(await frame(), 560, 440));
    await choosePreview('both');
    scrolling = await scrollState();
    const bandsBeforeBoth = await fixedGeometry();
    await panel().evaluate(element => { element.scrollLeft = element.scrollWidth; element.scrollTop = element.scrollHeight; });
    check('Content can scroll on both axes while the surrounding frame remains fixed',
      scrolling.horizontal && scrolling.vertical
      && (await scrollState()).left > 0 && (await scrollState()).top > 0
      && sameGeometry(bandsBeforeBoth, await fixedGeometry())
      && isSize(await frame(), 560, 440));
    await screenshot('template-both-scrolled.png');
    await choosePreview('blank');
    scrolling = await scrollState();
    check('Returning to the blank canvas removes overflow and resets the content position',
      !scrolling.horizontal && !scrolling.vertical && scrolling.left === 0 && scrolling.top === 0);

    await page.locator('#rd-category-operational').focus();
    await page.keyboard.press('ArrowRight');
    check('Primary-tab arrow navigation activates Activity and focuses its tab',
      await selectedAndFocused(page.locator('#rd-category-activity'))
      && await page.locator('#rd-view-table').getAttribute('aria-selected') === 'true');
    await page.keyboard.press('End');
    const endWorks = await selectedAndFocused(page.locator('#rd-category-management'));
    await page.keyboard.press('Home');
    const homeWorks = await selectedAndFocused(page.locator('#rd-category-operational'));
    await page.keyboard.press('ArrowLeft');
    check('Primary tabs support Home, End, and wrapped arrow navigation',
      endWorks && homeWorks && await selectedAndFocused(page.locator('#rd-category-management')));
    await page.locator('#rd-category-activity').click();
    await page.locator('#rd-view-table').focus();
    await page.keyboard.press('ArrowRight');
    check('Secondary-tab arrow navigation activates Charts and focuses its tab',
      await selectedAndFocused(page.locator('#rd-view-charts')));
    await page.keyboard.press('Home');
    const secondaryHome = await selectedAndFocused(page.locator('#rd-view-table'));
    await page.keyboard.press('End');
    const secondaryEnd = await selectedAndFocused(page.locator('#rd-view-charts'));
    await page.keyboard.press('ArrowRight');
    check('Secondary tabs support Home, End, and wrapped arrow navigation',
      secondaryHome && secondaryEnd && await selectedAndFocused(page.locator('#rd-view-table')));
    await page.locator('#rd-view-charts').click();
    await page.locator('#rd-category-commands').click();
    await page.locator('#rd-category-activity').click();
    check('Returning to a category preserves its selected subtab',
      await page.locator('#rd-view-charts').getAttribute('aria-selected') === 'true');
    check('Both tab rows expose one selected keyboard stop and the content panel is labelled by its tab',
      await page.evaluate(() => {
        const rows = ['#rd-category-tabs', '#rd-subcategory-tabs'].map(selector => document.querySelector(selector));
        const validRows = rows.every(row => row.getAttribute('role') === 'tablist'
          && row.querySelectorAll('[role="tab"][aria-selected="true"]').length === 1
          && row.querySelectorAll('[role="tab"][tabindex="0"]').length === 1);
        const content = document.querySelector('#rd-content-panel');
        const label = content.getAttribute('aria-labelledby');
        return validRows && content.getAttribute('role') === 'tabpanel'
          && label && document.getElementById(label)?.getAttribute('aria-selected') === 'true';
      }));
    await page.locator('#rd-category-operational').click();
    await page.locator('#rd-view-overview').click();

    await page.getByText('Set canvas dimensions', { exact: true }).click();
    await page.locator('#rd-width').fill('640');
    await page.locator('#rd-height').fill('520');
    await page.locator('#rd-apply-size').click();
    await page.waitForFunction(() => {
      const rect = document.querySelector('#rd-module').getBoundingClientRect();
      return Math.abs(rect.width - 640) <= 1 && Math.abs(rect.height - 520) <= 1;
    });
    check('Size controls resize the module to 640 by 520 and report its actual dimensions',
      isSize(await frame(), 640, 520)
      && /640/.test(await page.locator('#rd-size-output').innerText())
      && /520/.test(await page.locator('#rd-size-output').innerText()));
    check('Resizing increases the usable canvas and retains a native resize handle',
      (await scrollState()).height > blankState.height
      && (await scrollState()).width > blankState.width
      && await page.locator('#rd-module').evaluate(element => getComputedStyle(element).resize === 'both'));
    await screenshot('template-resized-640.png');
    await page.locator('#rd-reset-size').click();
    check('Reset restores the recovered 560 by 440 frame and size controls',
      isSize(await frame(), 560, 440)
      && await page.locator('#rd-width').inputValue() === '560'
      && await page.locator('#rd-height').inputValue() === '440');

    await page.locator('#rd-module').scrollIntoViewIfNeeded();
    const beforeDrag = await frame();
    await page.mouse.move(beforeDrag.x + beforeDrag.width - 3, beforeDrag.y + beforeDrag.height - 3);
    await page.mouse.down();
    await page.mouse.move(beforeDrag.x + beforeDrag.width + 37, beforeDrag.y + beforeDrag.height + 27, { steps: 5 });
    await page.mouse.up();
    check('Dragging the native resize handle changes the frame in both dimensions', isSize(await frame(), 600, 470));
    await page.locator('#rd-reset-size').click();

    await page.setViewportSize({ width: 390, height: 844 });
    check('A narrow viewport preserves the default module size without overflowing the document',
      isSize(await frame(), 560, 440)
      && await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth));
    const stage = page.locator('.rd-canvas-stage');
    await stage.evaluate(element => { element.scrollLeft = element.scrollWidth; });
    check('The narrow-page canvas can scroll to the right edge of the full-size module',
      await stage.evaluate(element => {
        const outer = element.getBoundingClientRect();
        const module = document.querySelector('#rd-module').getBoundingClientRect();
        return element.scrollWidth > element.clientWidth && element.scrollLeft > 0
          && module.right <= outer.right + 1;
      }) && isSize(await frame(), 560, 440));
    await stage.evaluate(element => { element.scrollLeft = 0; });
    await screenshot('template-narrow-390.png');
    await page.getByRole('link', { name: 'Page index', exact: true }).click();
    await page.getByRole('heading', { name: 'Experiment index', level: 1, exact: true }).waitFor();
    check('Page index navigation returns to the experiment directory', new URL(page.url()).search === '');
    check('Template review and navigation made no fixture, data-fetch, or external-source requests', onlyLocalShellRequests());
    check('No browser script errors', errors.length === 0);
  } catch (error) {
    failure = error.stack || String(error);
    await page.screenshot({ path: path.join(output, 'template-failure.png'), fullPage: true }).catch(() => {});
  } finally {
    const result = {
      passed: checks.length, checks, errors, browser: browser.version(), baseURL,
      verifiedAt: new Date().toISOString(), screenshots,
      verificationContext: { ignoreHTTPSErrors },
      ...(failure ? { failure } : {}),
    };
    await fs.writeFile(path.join(output, 'template-verification-results.json'), JSON.stringify(result, null, 2));
    console.log(JSON.stringify(result, null, 2));
    await browser.close();
  }
  if (failure) process.exitCode = 1;
})().catch(error => { console.error(error); process.exitCode = 1; });
