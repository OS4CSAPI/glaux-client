# Browser verification

The first Details View increment includes a portable browser check at
[`scripts/verify-browser.cjs`](../../scripts/verify-browser.cjs). It tests the actual
running client with synthetic fixtures and intercepts its additional test URLs;
it does not connect to a device or an external CSAPI server.

## Run

Start `npm run dev` in one terminal. In another, use a separately available
Playwright-compatible installation and Chromium browser:

```sh
GLAUX_PLAYWRIGHT_MODULE="/absolute/path/to/playwright-core" \
GLAUX_CHROMIUM_EXECUTABLE="/absolute/path/to/chromium" \
npm run test:browser
```

If `playwright-core` is resolvable from Node and its matching Chromium is installed,
the two variables may be omitted. `GLAUX_BASE_URL` defaults to
`http://127.0.0.1:5173`. `GLAUX_QA_OUTPUT` optionally changes the output folder;
the default `artifacts/browser-qa/` is ignored by Git. Playwright and the browser
are verification tools, not new application dependencies. Browser execution must
be permitted by the host environment.

The script fails on a failed assertion, emits its check list, and saves screenshots
and a JSON result. It exercises the rendered DOM, real source capture/download
behavior, browser focus, tabs, loading races, and mobile layout. It does not
replace source review or the offline data/interpretation tests.

## Recorded run — 23 October 2026

**23 checks passed; no browser script errors.** Chromium Headless Shell
151.0.7922.34 ran with the existing runtime Playwright installation. The portable
repository script was rerun successfully after its paths were parameterized.
[`BROWSER_RESULTS.json`](BROWSER_RESULTS.json) retains the actual emitted check
list and empty error list. Current code verification is recorded in
[`CURRENT_WORK.md`](../Plans/CURRENT_WORK.md).

Coverage includes the three separate historical examples, the synthetic MPSS
technical-description contract, original-body byte equality, raw and unknown data,
safe text rendering, source labeling, rejection of a stale response, keyboard
navigation/focus, disclosure preservation, and absence of horizontal overflow at
390 px. Six generated screenshots were visually inspected for clipped or
misplaced content. Supported options and estimator inputs are disclosed separately
from the primary equipment/condition values.

Live-server interoperability, authentication, collection discovery, profile
conformance, and measured operator benefit are not established by this run.
