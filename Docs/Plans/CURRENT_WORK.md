# Current client work


## Smart Citizen Phase 1–3 review gate and paper v0.7 — 25 October 2026

**Final publication verification:** GitHub Actions run `40195631894` rebuilt paper v0.7 successfully from source commit `d0905f1c` and committed the generated edition at `de034ba4`. The verifier reported 43 cited references, 7 figures, 2 listings, current Word inputs and 18 publication files; the generated DOCX SHA-256 is `1ff723be43386c20a33847c92203eaceaaf5f7d4a0acc68bc140e53d2889b108`. The final edition renders to 33 pages; every page was visually inspected, two stale v0.6-era figure-status labels found during the first review were corrected, and the final render has no observed clipping, overlap, broken tables or missing figures. This is a documentation/research checkpoint only; no application deployment, server write or Phase 4 resource-graph work was performed.

The owner requested the review checkpoint that should have occurred before the prior execution advanced automatically. Phase 1 is now confirmed complete for frozen registration 19639; Phase 2 is reviewed and corrected; Phase 3 contains nine current-state and two aggregate-history mappings at the documented review standing. **Phase 4 has not begun and remains paused for owner discussion.**

The corrective review found several issues worth preserving rather than silently fixing. The native timing cohort is 11 non-SEN5X channels at 02:40:21Z plus 10 SEN5X particulate channels at 02:36:21Z, not the previously written 17+10; Smart Citizen's `_raw` path contains a normalized/pre-calibration value rather than proof of untouched raw output; notification booleans are settings, not live condition assertions; and the earlier RSSI `status` classification overreached the evidence. The mapping ledger now leaves RSSI subject/DataStream type unresolved, models hourly averages as source-platform processing rather than physical-kit output, and distinguishes server-derived DataStream summary fields from adapter-authored content.

Paper v0.7 updates the formal specimen from the earlier feasibility values, adds a sourced Terms and Definitions section, and audits key usages such as telemetry, provenance, measurement, calibration, Observation, DataStream, source time and acquisition time against those definitions. It reports Phase 1–3 acquisition/characterization/mapping results while continuing to state that the adapter, CSAPI publication/round trip, connected Glaux retrieval and matched interface comparison are unexecuted. The next action is owner review of this checkpoint; do not start the CSAPI resource graph until that review authorizes Phase 4.

## Smart Citizen execution roadmap and workbook — 24 October 2026

The owner approved preserving the current end-to-end plan and detailed experiment homework outside the research paper. The new execution roadmap defines eleven phases with explicit gates and milestones; the new workbook supplies living templates for source capture/inventory, mapping lineage, CSAPI resource design, execution evidence, UI/PBI findings, transferability, and material decisions. The existing experiment plan remains as rationale/history, while the roadmap is now the current sequencing authority.

Immediate work remains Phase 1: reacquire and freeze the Smart Citizen specimen, then complete the native inventory before formal target mapping. No adapter code, CSAPI writes, profile changes, or application changes are authorized by creating these planning records.

## Paper version 0.6 vendor presentation baseline — 24 October 2026

The owner requested populating the source-provider side of the interface comparison before the CSAPI/Glaux results exist. Paper v0.6 now includes two unchanged first-party Smart Citizen UI screenshots selected from the official documentation: the core platform's basic measurement-exploration view and the separately documented custom dashboard. Their source pages describe their roles, while a new evidence record preserves exact repository revision, asset path/blob, historical device/time context, and rights notices.

The new section explains what Smart Citizen makes visible—resource/reporting context, multiple current quantities, values and units, a selected property's explanation and history, sensor/model labels, and alternate dashboard organization—without treating those pixels as normative MERLIN requirements. A reconstruction-question table converts those presentation observations into testable questions for the DIM/Profile and Resource Details PBI. Figures 8–10 remain reserved for a contemporaneous selected-registration source view if available, the matched generic/profile-aware Glaux comparison, and the implemented CSAPI relationship/source-to-display trace.

The screenshots are historical examples rather than registration 19639 evidence, and the paper says so explicitly. The adapter, CSAPI loading, live integration, and matched interface evaluation remain unexecuted. The repository paper workflow regenerated the v0.6 Word edition and refreshed publication fingerprints successfully. The exact GitHub Actions-generated 29-page edition was downloaded, rendered, and every page was visually inspected; both source screenshots, captions, continuation tables, references, headers, footers, and page flow are clean.

## Paper version 0.5 experimental Glaux client — 24 October 2026

The owner required the paper to describe the client side of the experiment as rigorously as the CSAPI server. Paper v0.5 now records the standalone `OS4CSAPI/glaux-client` lineage, why Explorer and `cs-client-ts` were not selected as the experimental foundation, the exact pinned `OS4CSAPI/ogc-client-CSAPI_2` phase-10 dependency, and the separate `src/data`, `src/profile`, and `src/presentation` responsibilities. A new evidence record and architecture figure make the Standard View / Operator View comparison boundary explicit.

The paper also records the public Cloudflare Pages runtime, deployed Git commit and deployment ID, the recovered 560 × 440 review frame, and the current direct-System remote-read limitations. It explicitly states that authenticated service access, collection discovery, and full System-to-DataStream/schema/Observation traversal are not yet deployed and are part of the Smart Citizen client increment. Documentation changes do not alter the current public runtime.

The local v0.5 review copy renders to 26 pages. All pages were visually inspected after the client-section and figure revisions; a final wording correction changed only page 22 relative to that inspected render, and page 22 was re-inspected. The repository paper workflow regenerates the Word edition from the maintained manuscript and refreshes its publication fingerprints so the committed reading copy remains source-consistent.

## Paper version 0.4 experimental CSAPI server — 24 October 2026

The owner required the research paper to explain the 52°North/pygeoapi CSAPI server as part of the experiment rather than treating it as an unnamed transport. Paper v0.4 now documents pygeoapi's role, 52°North's Connected Systems proof of concept, the exact tested upstream revision, the Oracle-hosted OS4CSAPI deployment, image identity, deployment adaptations, and the bounded cross-server evidence that supports using it as the first Smart Citizen target. The paper also records the deployment details that are still unknown instead of inferring them from upstream examples.

A new repository evidence record preserves the server baseline and an authored figure distinguishes implemented server lineage from the proposed Smart Citizen adapter and Glaux path. The server selection is explicitly bounded: on the October 19 preservation sample, CS-GO rejected the tested characteristics, OpenSensorHub accepted but failed to return selected group IDs and conditions, while 52°North/pygeoapi accepted and returned all submitted fields. This does not establish complete CSAPI conformance, restart durability, observation publication, command support, or universal superiority.

The dedicated paper workflow completed successfully for v0.4 and committed the generated Word edition. The final 21-page edition was rendered and visually reviewed; the server-lineage figure, deployment table, citations, references, code/listing content, headers, footers, and page flow are clean. The final one-word version correction affected only page 18 in the rendered comparison, while the other 20 pages were pixel-identical to the already inspected v0.4 render. The deployed Glaux runtime remains unchanged because this is documentation and research-method work.

## Paper version 0.3 illustrated system overview — 24 October 2026

The owner requested an early explanation of the system type and selected case,
supported by an authentic image. [Paper v0.3](../Research/Studies/Smart_Citizen/README.md)
adds an illustrated overview of Smart Citizen as an environmental-monitoring
system and identifies SCK 2.3 as the model reported by public registration 19639.
The model reference photograph does not verify that registration's physical
installation, component inventory, or placement.

The immediate proposal remains public Smart Citizen readings → documented adapter
→ CSAPI → Glaux, accompanied by deterministic captures. An owned kit is a later
route to physical-context evidence, and AirGradient is a later independent
comparison. The existing mapping-lineage requirements, three-to-five-sentence
narrative policy, MPSS v0.3.5 baseline, and original imported artifacts remain in
force.

Verification passed: all eighteen rendered Word pages were visually reviewed,
including the photograph and caption on page 2 and complete system-identification
table on page 3. All 72 narrative/explanatory-caption paragraphs meet the required
length: 25 have three sentences, 37 have four, and 10 have five. The paper checks
passed for 22 cited references, three figures, two listings, current Word inputs,
and fourteen publication-file fingerprints; the six tables were also reviewed.

Repository verification passed for all fourteen original artifacts and 302 local
links across 27 documentation files. The photograph matches its official source
blob byte-for-byte, with source credit and both published rights notices retained.
The counts and verification results in the v0.2 and v0.1 sections below describe
those earlier editions. This document revision does not execute the adapter,
CSAPI publication, live experiment, or interface comparison, and the deployed
runtime remains `71297c97`.

## Paper version 0.2 donor explanations and paragraph structure — 24 October 2026

The owner clarified that every mapping must explain its CSAPI concepts and
SensorML/SWE representation, underlying DIM concept, exact MPSS rule, and each
individual donor-source concept invoked. [Paper v0.2](https://github.com/OS4CSAPI/glaux-client/blob/387363d5f83d6193fa11ef3342a5db707fe6a7f9/Docs/Research/Studies/Smart_Citizen/README.md)
now sets that requirement in a seven-layer mapping matrix and illustrates it with
`SC-TEMP-01` and `SC-BATT-01`. The examples identify observation-concept lineage,
source property and unit vocabularies, representation mechanisms, authored choices,
and RFC battery/topology limits without claiming completed mappings or execution.

The paper now contains twenty-two references and five tables alongside its two
figures and two JSON listings. All narrative paragraphs, including the abstract
and explanatory captions, have three to five sentences. The publication verifier
enforces the requested range and reports paragraph locations and counts; the
maintenance guide, experiment plan, indexes and AGENTS instructions preserve both
requirements for later work.

Verification passed for all 66 narrative/explanatory-caption paragraphs: 23 have
three sentences, 33 have four, and 10 have five. All sixteen rendered Word pages
were visually reviewed, and the illustrative lineage was checked against retained
project evidence and primary sources. The publication checks confirmed twenty-two
cited references, consistent listings and current Word inputs; repository checks
confirmed all fourteen original artifacts and 292 local documentation links, with
a clean whitespace check.

This remains a protocol and preliminary assessment. The adapter, CSAPI publication,
live run and screenshot comparison remain unexecuted, and the fourteen imported
originals retain their existing bytes and versions. The deployed runtime remains
`71297c97`, so this documentation increment requires no application upload.

## Initial Smart Citizen experiment paper version 0.1 — 24 October 2026

The owner requested an academic-style document that develops with the experiment.
[Paper v0.1](https://github.com/OS4CSAPI/glaux-client/blob/57a2d1b68ad5c30a0a005c6095306e050fa9e4a9/Docs/Research/Studies/Smart_Citizen/README.md) established a drafted protocol
and preliminary source assessment, with a canonical Markdown manuscript and a
generated Word edition. It contains an abstract, eleven numbered sections, nineteen
CMOS 18 author-date references, two authored diagrams, four tables, and two explained
JSON listings. Source-interface and matched Glaux screenshots have a defined
capture/comparison protocol and reserved figure slots; none is reported as captured.

The methods describe public Smart Citizen data flowing through a documented adapter
and CSAPI service into Glaux, with reproducible captures and competent generic/profile
comparison. Owned hardware is a later extension. The earlier
[experiment plan](SMART_CITIZEN_EXPERIMENT_PLAN.md) is reconciled with this sequence
and the broader specimen scope discussed with the owner. The first two fields can
start a trace, but metadata, multiple quantity types, indicators, history and
provenance are part of the intended dataset.

The paper has its own publication manifest and reference records. The repository
verification command checks citation/reference agreement, source-excerpt fidelity,
listing consistency, figure presence, Word input freshness, and publication-file
fingerprints in addition to the fourteen original artifact hashes and local links.
The original artifact manifest and MPSS v0.3.5 baseline are unchanged.

Verification passed: all thirteen rendered Word pages were visually reviewed;
the paper verifier confirmed nineteen cited references, two figures, two listings
and ten publication-file fingerprints. The repository verifier confirmed all
fourteen original artifacts (27,555,946 bytes) and 292 local documentation links.
Technical/source review and the whitespace check passed. These documentation
checks do not establish OGC conformance or experiment results.

This increment creates research documentation and its maintenance tooling. No
adapter, CSAPI dataset, live integration, screenshot comparison, new application
page, or measured UI benefit is implemented by it. The deployed runtime remains
`71297c97`; no Cloudflare upload is needed. Continue by recording the initial
field mapping and selected service capabilities, then use the paper's execution
protocol to record actual integration evidence.

## Open sensor research and Smart Citizen proposal — 24 October 2026

The owner requested filing the device-candidate findings and proposing a Smart
Citizen experiment. The [research report](../Research/Reports/OPEN_SENSOR_CANDIDATES_2026-10-24.md)
preserves the shortlist, recommendations, source links, access results, prices
and limits. The [evidence record](../Research/Evidence/OPEN_SENSOR_ACCESS_2026-10-24.json)
preserves 15 study-local observations with selected excerpts and available
response fingerprints. The [experiment plan](SMART_CITIZEN_EXPERIMENT_PLAN.md)
initially proposed one public specimen, explicit mapping, a deterministic 560 × 440
review, then owned hardware and live access. The current paper and reconciled plan
supersede that ordering by placing public live integration before acquisition;
AirGradient remains an independent later comparison.

This is a documentation increment. The study and proposal are complete; the
Smart Citizen adapter, recorded-data page and live integration are not present.
The 14 imported originals, their manifest, the technical profile and application
code retain their existing versions. The runtime remains `71297c97` and the
six-page production site recorded below. No Cloudflare upload is needed for
this documentation publication. Git history records the actual publication commit.

Documentation verification passed: all **14 original artifact hashes and
27,555,946 bytes**, **247 local links across 24 documentation files**, valid
evidence JSON with 15 unique record IDs, and a clean whitespace check. The
evidence was compared with the retained captures: **10 body hashes/lengths and
136 selected fields or source lines** matched, including all 24 historical
temperature groups. An independent review checked the Smart Citizen facts and
the boundary between proposed and implemented behavior. Runtime browser checks
were not rerun for this documentation-only increment.

Continue from the proposed evidence-to-mapping specimen, with implementation
status distinguished from plan status. The [broader continuity note](CONTINUITY.md)
reconciles this sequencing with the retained research backlog.

## Resource Details View template — 24 October 2026

The owner requested a blank template using the framework recovered from the
earlier Resource Details PBI work. The new `/?page=resource-details-template`
route retains the **560 × 440 CSS-pixel working frame**, fixed identity and top/
bottom marking placeholders, adjacent category/subcategory rows, and internally
scrolling content. The later working-view labels remain provisional. Exact
source sections, PDF pages, and current implementation choices are in the
[template design record](../Design/RESOURCE_DETAILS_TEMPLATE.md).

The page starts blank and makes no fixture or remote data requests. Optional
layout-only samples demonstrate vertical, horizontal, and combined overflow.
Native resizing and keyboard-accessible size controls include a reset to the
recovered default. The homepage now lists six pages; the data-example selector
retains its original five entries. Existing examples and source bytes are intact.

Local verification passed: **74 offline tests**, TypeScript/production build,
**27 template browser checks**, **44 index checks**, **23 baseline checks**, and
**44 power checks**, with no script errors. Native scrollbar rendering was enabled
for visual inspection, including blank, overflowing, resized, and narrow canvases.
The implementation is saved on GitHub and deployed. **All 27 template checks and
44 index checks passed again on production**, with no browser script errors.
The current runtime is
[`71297c97`](https://github.com/OS4CSAPI/glaux-client/commit/71297c971e2e7532f7c7139600f41e9b58bdcc22),
with [passing GitHub CI](https://github.com/OS4CSAPI/glaux-client/actions/runs/40130331258).
Pages deployment `97c801c4-c44f-4484-a175-e6651639fe07` completed at
**4:34:47 p.m. EDT on 24 October 2026**. Open the
[live template](https://glaux-client.pages.dev/?page=resource-details-template)
or [six-page index](https://glaux-client.pages.dev/).
The [deployment record](CLOUDFLARE_DEPLOYMENT.md) retains the runtime identity and
live checks. This increment is complete; the preceding checkpoints below are history.

## Experiment index — 24 October 2026

The user requested a deployed index listing the experiment pages, descriptions,
latest updates, and update dates/times. The deployed implementation includes a homepage
index for the five existing examples, links back from every example, and URL
synchronization when selecting an example. One typed catalogue supplies both the
index and selector; [the maintenance guide](../Design/PAGE_INDEX.md) records the
update procedure and the Git evidence for the initial dates.

Local verification passed: 74 offline tests, TypeScript/production build, 36 index
browser checks, 23 existing example checks, and 44 power checks. No browser script
errors occurred. The 36 index checks passed again against the production origin.
The current deployed runtime is
[`0d977e36`](https://github.com/OS4CSAPI/glaux-client/commit/0d977e366e55363dd997c0f519c7cca2bc814530),
with [passing GitHub checks](https://github.com/OS4CSAPI/glaux-client/actions/runs/40113200519).
Cloudflare Pages deployment `44f92062-a39a-4f86-9267-a63bd0935f53` completed at
**12:52:53 p.m. EDT on 24 October 2026**. The index is live at
<https://glaux-client.pages.dev/>; the immutable deployment is
<https://44f92062.glaux-client.pages.dev/>.

The [deployment record](CLOUDFLARE_DEPLOYMENT.md) preserves the actual upload
method, runtime identity, and live verification. Keep the catalogue current as
pages are added or their behavior changes. The records below preserve the earlier
power implementation and deployment checkpoint; they do not supersede this one.

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
