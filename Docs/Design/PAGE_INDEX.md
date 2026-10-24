# Deployed experiment page index

The site root `/` lists the experiment pages, their descriptions, the latest
recorded change to each example, and that change's date and time. Existing
`/?example=...` links open the same examples as before. Each example has a
**Page index** link back to the homepage. The example selector also updates the
address, so copying or refreshing its URL opens the selected example.

## One catalogue for the index and selector

[`src/experiments.ts`](../../src/experiments.ts) is the maintained page catalogue.
The index and the existing example selector both consume it. The initial entries
are TRSS ETU-II, OmniSense Core2, OmniSense Core5ADS, the MPSS technical-description
contract, and the connected power-arrangement example. Overview, Equipment, and
Condition remain shared tabs within each example; Standard view remains a mode.

When adding or changing an example, update its catalogue entry in the same change:

- Keep the `id` stable so existing page links continue to work.
- Supply its visible title, selector label, fixture URL, and plain-language
  description of what the page actually does.
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
new profile binding or a new source-data update in each example.

## Verification and publication

Run the existing offline tests and production build. With the documented browser
environment, run `npm run test:browser:index`; this verifies the actual homepage,
metadata, destinations, return links, address updates, unknown-link handling, and
desktop/mobile layout. The baseline browser script now starts at the explicit
TRSS URL; the power script retains its existing explicit URL.

Save the implementation to the existing working branch, deploy that exact GitHub
revision to the existing Pages project, and record its deployment and live check
in [the deployment record](../Plans/CLOUDFLARE_DEPLOYMENT.md). The project remains
Direct Upload, so a Git push alone does not change the deployed site.
