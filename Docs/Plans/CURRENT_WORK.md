# Current Details View work

Updated 23 October 2026. **Status: first increment reconstructed, locally verified,
and saved for review; Cloudflare deployment is blocked at sign-in.**

- Repository: `OS4CSAPI/glaux-client`.
- Working branch: `work/details-view-20261023`.
- Review: [draft PR #1](https://github.com/OS4CSAPI/glaux-client/pull/1).
- Original baseline: `d2386062871ff8caaa7021d38f39f1af7c74dd12`.
- Reconstructed implementation checkpoint:
  [`ddac23a3`](https://github.com/OS4CSAPI/glaux-client/commit/ddac23a3e74f5b4a5fe3bfddc344e004d6dc683f),
  followed by the final guard/verification commit on the same branch.
- Pinned library: `OS4CSAPI/ogc-client-CSAPI_2`,
  `4ca1d7db9b1ccdf545adbef42ef941139fe11977` (phase-10 provenance).

## Recovery and authorization

The prior local implementation was unavailable. Recovered screen images and
activity descriptions are design evidence, not recovered source code or proof
of its checks. This branch is a **new reconstruction** of the already-authorized
first increment, using the actual source documents and preserved UI evidence.
Bootstrap-only exclusions were superseded only for these views, bounded profile
interpretation, and explicitly synthetic evaluation records.

Do not restart research or choose another client library. Read this note, the
[source index](../Research/SOURCE_INDEX.md), and the
[exact source-to-view mapping](../Design/DETAILS_VIEW_MAPPING.md) before continuing.
The full source documents remain outside this public repository. The index records
versions, fingerprints, locators, and evidence limits; screenshots are not code.

## Implemented

The compact System card supplies **Operational → Overview, Equipment, Condition**.
Operator and Standard modes consume the same captured model. Four local HTTP
fixtures keep TRSS ETU-II configuration/estimation, Core2 reported equipment,
Core5ADS condition, and a fully synthetic MPSS technical-description contract
separate. Supported options, estimator inputs, and detailed provenance use
accessible disclosures.

Data retrieval, standard extraction, interpretation, and presentation are separate.
The actual pinned CSAPI/SensorML/SWE library is used. Original Fetch-exposed bytes,
text, JSON, exposed headers, URLs, status, and retrieval time are independently
retained; Standard view exposes unknown fields, links, metadata, and exact-body
downloads. Direct resource reads use GET with credentials omitted and follow at
most one explicitly advertised SensorML alternate, without guessed routes.

The interpreter recognizes only MPSS technical-description's four Text terms.
Device-specific concepts use a separate explicit experiment namespace, with profile
gaps recorded. It checks source carriers, definitions, value types, units, code
spaces, declared nil tokens, per-group cardinality, supplied labels where required,
and subject identity. Foreign-subject and failed-HTTP content remains inspectable
without populating operator readings. Source clocks are not parsed into trusted
timestamps; retrieval time is separate. No state of charge, runtime, aggregate
health, readiness, physical equipment identity, or resource relationship is invented.

## Verification

| Check | Actual result |
| --- | --- |
| `npm ci --no-audit --no-fund` | Passed, including the exact pinned library build |
| `npm test` | 45 tests passed across 4 files |
| `npm run build` | TypeScript checking and Vite production compilation passed |
| `npm run test:browser` with available Playwright/Chromium | 23 checks passed; zero browser script errors |
| Visual inspection | Six desktop/mobile views inspected; no clipping or overlap; 390 px has no horizontal overflow |
| Exact-body download | Browser-downloaded bytes matched the original fixture byte for byte |
| GitHub CI | [Implementation checkpoint passed](https://github.com/OS4CSAPI/glaux-client/actions/runs/39995569307); PR checks identify the result for each subsequent head |

The final review added regression coverage for foreign subjects when the viewed
process identity is unknown, and valid-looking JSON received with an HTTP error.
The tests also cover unknown properties, zero/false/empty values, failed reads,
cancellation, bounded link following, conflicting singleton terms, wrong carriers,
code spaces/units/types, nil values, and the separation of source examples.

[Browser instructions](../Testing/BROWSER_VERIFICATION.md), the
[recorded check list](../Testing/BROWSER_RESULTS.json), and the executable script
are saved in this repository. Browser checks are optional local verification;
standard CI runs install, type-check, offline tests, and production build.

## Open limits

- The device-specific experimental bindings still need profile decisions; no profile
  changes or whole-profile conformance are claimed.
- Source-based synthetic fixtures are not native manufacturer API responses.
- No supplied existing-server System URL was available for validation. Browser CORS
  applies; authentication and collection discovery are outside this increment.
- Comparative operator benefit has not been measured.
- No upstream-library, infrastructure, deployment, live device command, or server
  write was performed. Source manuals, private documents, credentials, and chat
  transcripts were not committed.

## Next concrete action

The user requested continuation by Codex already running in VS Code on their
machine. Start with the [Codex VS Code handoff](CODEX_VSCODE_HANDOFF.md), fetch
the implementation branch, and inspect the local environment and authentication.
The prior chat's browser session and filesystem are not established as shared
with that local Codex session.

The user has now requested a Cloudflare deployment directly from GitHub. Build
configuration is prepared in [Cloudflare deployment](CLOUDFLARE_DEPLOYMENT.md);
authentication returned to [Cloudflare login](https://dash.cloudflare.com/login)
with the visible error "Unable to sign in. Try again or use your email and
password." Automated sign-in stopped in that browser. Authentication in the
local Codex environment must be checked. No Cloudflare project, build,
deployment, or live URL was created or verified during this attempt.

Finish Cloudflare authentication, configure Pages from the implementation branch,
deploy, and verify the application. Record the actual deployed commit and verified
URL in the deployment note after those steps succeed.

Review the runnable increment through PR #1. For the next server-validation step,
use a supplied existing CSAPI System resource URL in **Use your existing CSAPI
server**, inspect its standard capture first, and record actual supported and
unresolved bindings. Do not modify that server or manufacture missing values to
make the operator view look complete.

Keep this note current and save source changes on the working branch at meaningful
increments. A chat progress statement is not a source-code checkpoint.
