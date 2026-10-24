# Current client work

## Experiment index — 24 October 2026

The user requested a deployed index listing the experiment pages, descriptions,
latest updates, and update dates/times. The implementation now includes a homepage
index for the five existing examples, links back from every example, and URL
synchronization when selecting an example. One typed catalogue supplies both the
index and selector; [the maintenance guide](../Design/PAGE_INDEX.md) records the
update procedure and the Git evidence for the initial dates.

Local verification passed: 74 offline tests, TypeScript/production build, 36 index
browser checks, 23 existing example checks, and 44 power checks. No browser script
errors occurred. The implementation is ready for publication and deployment;
the last verified production runtime is recorded below until the new upload and
live checks complete.

## Previous implementation and deployment checkpoint

Updated 24 October 2026. **Power-arrangement implementation, local verification,
Cloudflare deployment, and live verification are complete.**

The owner subsequently authorized publication of the maintained project artifacts.
The [Artifact Register](../ARTIFACT_REGISTER.md) and [manifest](../ARTIFACTS.json)
now identify the original source files. [MERLIN continuity](CONTINUITY.md)
reconciles their 22 October checkpoint with the completed client work. This
documentation increment does not change the deployed runtime revision below.

## Repository and durable source

- Repository: `OS4CSAPI/glaux-client`.
- Working branch: `work/details-view-20261023`.
- Existing review: [draft PR #1](https://github.com/OS4CSAPI/glaux-client/pull/1).
- First saved power implementation:
  [`64e2287b`](https://github.com/OS4CSAPI/glaux-client/commit/64e2287b8b6366eed7fdf0bd83ca502997caeb9d).
  Follow-up commits on this same branch contain final UI corrections, verification
  and continuity notes. Fetch and inspect the current head before continuing.
- Pinned library: `OS4CSAPI/ogc-client-CSAPI_2`, phase-10 commit
  `4ca1d7db9b1ccdf545adbef42ef941139fe11977`.
- Verified public deployment: `d74b33dabc5fdfcf22574b8efa7f436b4cf32857`,
  Cloudflare Pages deployment `770d234a-3cb5-415a-aa96-b8fea45180c4`,
  <https://glaux-client.pages.dev/?example=power>.

## Authorized objective and implementation

The user asked why the deployed client did not demonstrate the organized power
model, then authorized implementing the existing synthetic source A/B replacement
example. This adds a bounded demonstration; it does not reopen donor selection,
revise MPSS, approve the proposed battery/interface module, or integrate live
manufacturer data. The four earlier examples remain separate.

Select **Power arrangement · source replacement** or use `/?example=power`.
The compact Operational > Overview / Equipment / Condition card now provides:

- The supplied source-to-station relationship at three source-grounded instants.
- Distinct source identities and selectable equipment details.
- A replacement history identifying removed A and installed B on the same station.
- One 12.6 V observation describing B, reported by the station at 10:10 UTC.
- No future reading in the before/replacement views; no invented A observation.
- Per-fact evidence, a model/binding/presentation explanation, and an independent
  Standard view and exact original-body download for each source record.

The seven original JSON bodies remain byte-identical to the supplied synthetic
profile example. A separate local catalogue maps their original canonical IDs to
fixed local files and explicitly associates the result schema with its stream.
It never requests `demo.example` or guesses server routes. Each record retains its
own source capture and standard projection; bundle data is not merged into one
station identity. Partial failed responses remain inspectable.

The profile interpreter resolves supported native equipment references, checks the
exact R16 group/term/code-space contract and half-open applicability intervals,
and preserves producer/observed-subject/schema/output correspondence. Unsupported
or ambiguous evidence cannot become a reading. A review corrected arbitrary
fragment endpoints, non-process reporters, and unsupported observation subject
overrides; regression tests retain those cases.

Read [the exact source-to-behavior mapping](../Design/POWER_ARRANGEMENT.md),
[the source index](../Research/SOURCE_INDEX.md), and the original
[Details View mapping](../Design/DETAILS_VIEW_MAPPING.md). The identified original
project artifacts are published at their registered paths; their original
versions, bytes, and proposal boundaries remain explicit.

## Verification of this increment

| Check | Actual result |
| --- | --- |
| `npm test` | 74 tests passed across 6 files |
| `npm run build` | TypeScript checking and Vite production build passed |
| Original fixture preservation | Seven bodies byte-compared and SHA-256 checked |
| GitHub checkpoint CI | [64e2287b passed](https://github.com/OS4CSAPI/glaux-client/actions/runs/40083557766) |
| Existing browser regression | 23 checks passed; zero script errors |
| New power browser verification | 44 checks passed; zero script errors |
| Visual inspection | All 10 power screenshots inspected at 1280 px or 390 px; no clipped facts or horizontal overflow |
| New live deployment | 44 power checks passed against `https://glaux-client.pages.dev`; zero browser script errors |

The [browser verification record](../Testing/BROWSER_VERIFICATION.md) links the
actual emitted results, reproducible scripts, and selected local screenshots.

Checks use explicitly synthetic local data. They establish this bounded behavior,
not complete OGC/MPSS/RFC conformance, live-server interoperability, production
readiness, or measured comparative operator benefit.

## Deployment boundary and next action

The existing Pages project remains **Direct Upload**. Pushing GitHub does not deploy
it. The authenticated local Wrangler session uploaded the verified checkpoint and
the production deep link now serves the power example. The exact outcome is in
[the deployment record](CLOUDFLARE_DEPLOYMENT.md).

Review the deployed power example and continue the existing draft PR. Any later
implementation revision requires another explicit build, upload, and live check.
Preserve unrelated local changes and save each meaningful continuation to the
working branch; chat commentary is not a source checkpoint.

For artifact changes, run `python3 scripts/verify-artifacts.py` and update the
register, manifest, and continuity notes together. The earlier PITON/plan files
preserve their source checkpoint; use CONTINUITY.md for current locations and
sequencing. A repository documentation commit can be newer than the runtime
commit without requiring another Cloudflare upload.
