# Browser verification

The original Details View increment includes a portable browser check at
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

## Power-arrangement verification — 23 October 2026

The separate [`scripts/verify-power-browser.cjs`](../../scripts/verify-power-browser.cjs)
exercises the connected synthetic source A/B replacement example. With the same
server and browser setup described above, run:

```sh
GLAUX_PLAYWRIGHT_MODULE="/absolute/path/to/playwright-core" \
GLAUX_CHROMIUM_EXECUTABLE="/absolute/path/to/chromium" \
npm run test:browser:power
```

`GLAUX_BASE_URL` again defaults to `http://127.0.0.1:5173`. The default power
output directory is `artifacts/power-browser-qa/`, ignored by Git; override it with
`GLAUX_QA_OUTPUT` if needed. The script may also target a deployed origin, without
a query string. It makes GET requests, uses local fixtures for its intentionally
invalid-endpoint case, and performs no device commands or server writes.

**44 checks passed; no browser script errors.** The original 23-check script also
passed again. Chromium Headless Shell 151.0.7922.34 used the runtime Playwright
installation. [`POWER_BROWSER_RESULTS.json`](POWER_BROWSER_RESULTS.json) preserves
the actual new check list, browser version, local origin, and empty error list.

The checks establish:

- A before replacement and only B at the exact 10:00 UTC interval boundary.
- No 10:10 voltage in earlier views, while the original later observation remains
  inspectable. At 10:10, the reading describes B and is reported by the station.
- No invented A observation, battery identity, charge, runtime, interface, or
  readiness value; the station's own condition stays separate from its B report.
- Byte-identical original text and downloads for all seven bodies and the catalogue.
- Local record retrieval without canonical example-host traversal; rejected Event
  endpoints never become selectable equipment, and their original evidence survives.
- Keyboard operation, focus, tab/disclosure state, refresh, example switching, and
  readable layouts with no horizontal overflow at 390 px.

All ten generated power screenshots were visually inspected. These selected
screenshots are committed as evidence of the **local verified implementation**;
they do not establish a Cloudflare deployment:

- [Overview after replacement, 1280 px](power/power-after-overview-1280.png).
- [Source B Condition, 390 px](power/power-source-b-condition-390.png).

The complete screenshot set is reproducible with the script. The fixture meaning
and limits are recorded in the [power mapping](../Design/POWER_ARRANGEMENT.md).
These tests do not establish full profile/RFC conformance, live integration,
physical power flow, or measured operator benefit.
