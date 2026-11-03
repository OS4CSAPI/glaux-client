# Deployed experiment page index

The site root `/` lists the experiment pages, their descriptions, the latest
recorded change to each page, and that change's date and time. Existing
`/?example=...` links open the same examples as before. The separate
`/?page=resource-details-template` route opens the Resource Details View wireframe
canvas. `/?page=resource-details-activity` reuses that frame and adds the researched
Activity table wireframe. Every page has a **Page index** link back to the homepage. The example
selector also updates the address, so copying or refreshing its URL opens the
selected example.

## Current Step 38 update — 3 November 2026

The existing `/?page=resource-details-profile-test` page now supports four **local read-only project evidence packets** using `&case=step38-dragino`, `step38-airgradient`, `step38-campbell` or `step38-bennett`. These are **case selections within the existing template page**, not new index entries or native CSAPI System resources. The [source-packet integration design](RESOURCE_DETAILS_PROFILE_TEST.md#step-38--same-shared-evidence-interpretation-in-the-existing-resource-details-tabs-3-november-2026) explains its unchanged common reader, raw evidence, qualified UI and Map fallback; the `latestUpdate` metadata in `src/experiments.ts` uses a recorded GitHub implementation timestamp. The browser smoke script `npm run test:browser:source-packet` is committed but **was not executed** in this environment. No Step 38 Cloudflare deployment or modification of the live CSAPI route occurred.

## One catalogue for the index and selector

[`src/experiments.ts`](../../src/experiments.ts) is the maintained page catalogue.
The current catalogue includes twelve entries (five data examples and seven template-derived pages). The example selector uses the same
catalogue's five entries with `kind: 'example'`: TRSS ETU-II, OmniSense Core2,
OmniSense Core5ADS, the MPSS technical-description contract, and the connected
power-arrangement example. Overview, Equipment, and Condition remain shared tabs
within each example; Standard view remains a mode.

Seven entries have `kind: 'template'`. The original opens the recovered 560 × 440 Resource
Details View frame as a blank layout canvas, separate from the source-loading
flow. The derived page changes only Activity / Table, adding the three-resource
wireframe and its filters. A template has no fixture URL and does not appear in the example selector.
Its route invokes its presentation renderer directly and does not load a source
record. The two page kinds preserve this distinction in TypeScript as well as in
the index copy.

Another standalone template-derived page, `/?page=resource-details-smart-citizen`, uses the same 560 × 440 Resource Details view with source-linked manufacturer design facts from the I01–I13 Smart Citizen DIM case study on `research/dim-profile-v2`. It explicitly marks individual identifiers, live Observations, configuration and operational state as unverified. It does not claim any actual System resource or request live data; the original blank template and Activity table remain unchanged.

The separate `/?page=resource-details-live-map` page reuses the live CSAPI
Resource Details view and adds an interactive map for supported reported System
positions. See [the map design record](RESOURCE_DETAILS_LIVE_MAP.md) for its
coordinate interpretation, source and basemap limitations.

When adding or changing a page, update its catalogue entry in the same change:

- Keep the `id` stable so existing page links continue to work.
- Supply its page kind, visible title, and plain-language description of what the
  page actually does. A data example also needs its selector label and fixture
  URL. A standalone template needs its supported page ID and renderer route;
  never provide a dummy fixture URL to make it fit the example type.
- Record `latestUpdate.summary` and an ISO 8601 `latestUpdate.at` with an explicit
  offset or `Z`. Use the actual relevant implementation-change time.
- Link `latestUpdate.commit` when the supporting commit already exists. It is
  optional so a new page can be saved with its metadata in one commit; never put
  an invented or placeholder commit SHA in a public link.
- Keep the browser verification's page expectations consistent with additions.

The index sorts by recorded update time, newest first. Dates and times are
formatted in **America/New_York**, with the applicable EST/EDT label. The original
ISO timestamp remains in the HTML `time` element. Dates do not reset when the
browser opens, a source record is retrieved, or the application is rebuilt or
redeployed. Source observation, applicability, and retrieval times retain their
separate meanings inside the examples.

## Initial recorded changes

The initial dates were recovered from Git history rather than assigned from the
index's publication time:

| Examples | Recorded page change | Timestamp |
| --- | --- | --- |
| TRSS, Core2, Core5ADS, MPSS technical description | [64e2287b](https://github.com/OS4CSAPI/glaux-client/commit/64e2287b8b6366eed7fdf0bd83ca502997caeb9d) added direct example links and per-example descriptions. | 24 October 2026, 05:50:09 EDT |
| Power arrangement | [d74b33da](https://github.com/OS4CSAPI/glaux-client/commit/d74b33dabc5fdfcf22574b8efa7f436b4cf32857) excluded rejected relationship endpoints from equipment and clarified the supply direction on mobile. | 24 October 2026, 06:00:19 EDT |

The shared index/navigation addition has its own Git history. It does not imply a
new profile binding or a new source-data update in each example. The template's
24 October 2026, 16:24:47 EDT catalogue timestamp records creation of that page;
the original five example dates and descriptions remain unchanged.

## Verification and publication

Run the existing offline tests and production build. With the documented browser
environment, run `npm run test:browser:index`; this verifies the actual homepage,
metadata, destinations, return links, address updates, unknown-link handling, and
desktop/mobile layout. The index browser script was originally written for an earlier eight-page/two-template baseline; its previous acceptance count must not be used as proof of all twelve current pages without rerunning and updating its checks. The example selector still retains only the five data-example entries. The baseline browser script starts at the explicit TRSS URL;
the power script retains its existing explicit URL. The template's own browser
checks cover its recovered dimensions and scrolling behavior; the Activity check
covers its resource types, filters, columns, and unchanged sibling views.

Save the implementation to the existing working branch, deploy that exact GitHub
revision to the existing Pages project, and record its deployment and live check
in [the deployment record](../Plans/CLOUDFLARE_DEPLOYMENT.md). The project remains
Direct Upload, so a Git push alone does not change the deployed site.
