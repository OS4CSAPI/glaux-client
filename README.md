# Glaux Client

**Project documents and current implementation:** open the
[artifact register](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/ARTIFACT_REGISTER.md)
or the [documentation index](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/README.md).
The current collection is maintained on `work/details-view-20261023` while
[PR #1](https://github.com/OS4CSAPI/glaux-client/pull/1) is under review.

**Latest research:** the maintained Smart Citizen paper, **Evaluating Sensor
Information Preservation Through OGC Integration**, v0.6, 24 October 2026, is
available as a [manuscript](Docs/Research/Studies/Smart_Citizen/MANUSCRIPT.md) and
[Word edition](Docs/Research/Studies/Smart_Citizen/SMART_CITIZEN_EXPERIMENT_PAPER.docx).
Its [maintenance guide](Docs/Research/Studies/Smart_Citizen/README.md) links the
publication manifest, figures and listings. The paper develops a study protocol
and preliminary source assessment; the proposed public source → adapter → CSAPI
→ Glaux experiment and matched interface comparison have not been executed.

Version 0.6 fixes the Smart Citizen vendor-presentation baseline before the experiment produces its own UI results, using two unchanged first-party Smart Citizen screenshots and documenting their intended roles, historical limits, exact provenance, and reconstruction questions. Version 0.5 gives the experimental Glaux client the same explicit treatment as the server: standalone origin, selection rationale, pinned CSAPI library, three-layer architecture, Cloudflare runtime, current remote-read limits, and the Smart Citizen traversal still to be implemented. Version 0.4 documents the experimental CSAPI server, including the pygeoapi/52°North lineage, tested Oracle deployment, exact revision/image, bounded preservation rationale, deployment adaptations, and remaining configuration gaps. Version 0.3 introduced the environmental-monitoring system early, with an authentic
Smart Citizen Kit 2.3 model reference photograph. The photograph illustrates the
model; the physical installation associated with selected public registration
19639 remains unverified. Public readings remain the immediate experiment source; an owned kit and
the independent AirGradient comparison are later extensions.

The paper retains its seven-layer mapping explanation matrix and illustrative
`SC-TEMP-01` and `SC-BATT-01` cases. Each mapping must explain its standard
carriers, underlying DIM concept, exact MPSS rule, individually cited donor
concepts and their reuse status, and project-authored choices. The maintenance
guide also preserves the ongoing requirement for three to five sentences in
each paper narrative paragraph, including abstract and caption explanations.

The [candidate study](Docs/Research/Reports/OPEN_SENSOR_CANDIDATES_2026-10-24.md),
[access evidence](Docs/Research/Evidence/OPEN_SENSOR_ACCESS_2026-10-24.json), and
[experiment plan](Docs/Plans/SMART_CITIZEN_EXPERIMENT_PLAN.md) preserve the supporting
research and proposed sequence. Captured replay supports the public-data experiment;
owned hardware is a later extension.

An experimental **OS4CSAPI** application evaluating whether the MERLIN domain
information model and Managed Physical Sensing Systems (MPSS) profile can support
a consistent, useful sensor-surveillance operator interface.

TRSS unattended ground sensors and McQ OmniSense II are the motivating systems.
Their information must remain meaningfully distinct while being organized through
CSAPI, SensorML, and SWE Common. The first Details View increment compares competent generic standards-based
access with bounded interpretation of the **same retrieved information**, using
the existing Overview, Equipment, and Condition wireframes.

This prototype is intended for possible future contribution to the Glaux effort.
It does not claim adoption or endorsement by DGIWG or another organization.

## Setup

Prerequisites: Git and Node.js 24 LTS (with npm); Node 26 is also supported.
No server, credentials, private configuration, or research collection is needed.

```sh
git clone --recurse-submodules https://github.com/OS4CSAPI/glaux-client.git
cd glaux-client
git switch work/details-view-20261023
npm ci
npm run dev
```

The Details View increment is on `work/details-view-20261023` while its review
is pending. For an existing non-recursive clone, run `git submodule update --init --recursive`
before `npm ci`. Installation builds the exact pinned library from its own
committed lockfile, then makes its package exports available to the application.
Initial installation needs access to public GitHub and npm, not a CSAPI server.
Do not use `--ignore-scripts` or omit dev dependencies for this source/build setup.

```sh
npm run typecheck
npm test
npm run build
npm run preview
```

The development server defaults to <http://127.0.0.1:5173>; production output is
in `dist`. Tests are offline and use only explicitly synthetic inputs and
`example.invalid` URLs; no device records or operational readings are included.
CI runs install, type-check, tests, and build without deployment or server access.
Optional [browser verification](Docs/Testing/BROWSER_VERIFICATION.md) is reproducible
with a separately available Playwright/Chromium installation; it is not a new
application dependency.

## Library dependency

This application uses the CSAPI-enabled
[OS4CSAPI/ogc-client-CSAPI_2](https://github.com/OS4CSAPI/ogc-client-CSAPI_2)
library, not an assumed-equivalent npm release. It is a separate, commit-pinned
Git submodule in `.dependencies/ogc-client`, linked as a local npm dependency
under its upstream package name, `@camptocamp/ogc-client`.

Selected branch: **phase-10**; commit:
`4ca1d7db9b1ccdf545adbef42ef941139fe11977` (inspected 2026-10-23).
See [dependency provenance and build details](Docs/DEPENDENCIES.md).

## Current implementation

The homepage is an **Experiment index** linking the Resource Details template and
five example pages. Each entry
shows a description, its latest recorded change, and a date/time in Eastern Time.
The dates are recorded implementation changes, not rebuild or deployment times.
Every example links back to the index, and selecting another example updates its
shareable URL. Keep [the page catalogue](src/experiments.ts) current using the
[index maintenance guide](Docs/Design/PAGE_INDEX.md).

### Resource Details template

Open `/?page=resource-details-template` for a blank review canvas using the earlier
PBI work's **560 × 440 CSS-pixel working frame**. It retains identity and marking
placeholders, adjacent category/subcategory rows, and an internally scrolling
content area. Size controls and optional overflow samples support layout review.
The page is a standalone template; its bodies contain no resource data or device
operations. The [template design note](Docs/Design/RESOURCE_DETAILS_TEMPLATE.md)
distinguishes the recovered source specifications from current implementation
choices and the final PBI decisions still open.

### Source examples

The client provides a compact System card with **Operational → Overview,
Equipment, Condition**, plus Operator and Standard views over the same captured records.
Switching view or tab does not retrieve different information.

Five explicitly synthetic local HTTP examples are included:

| Example | What it exercises |
| --- | --- |
| TRSS ETU-II | Selected detector configurations, separately disclosed supported options, and qualified battery estimator values |
| OmniSense Core2 | Five source-reported transducer labels, without invented physical identities or discovery times |
| OmniSense Core5ADS | A distinct historical condition case: 15.43 V DC, a literal unverified source clock, and six individual diagnostic findings |
| MPSS technical-description contract | Fully invented manufacturer/model/revision values exercising the exact bounded MPSS binding |
| Power arrangement and replacement | Seven unchanged original MPSS example records: source A/B supply intervals, replacement history, and a 12.6 V observation with separate reporter and observed subject |

The first four cases use newly authored source-informed fixtures. The power case
copies seven original, explicitly synthetic example bodies byte for byte; its
new local catalogue only maps their canonical identities to the bundled files.
None is a native manufacturer response or current device state. The companion
[source index](Docs/Research/SOURCE_INDEX.md) records the reviewed source versions
and locators. The original project documents are now published through the
[artifact register](Docs/ARTIFACT_REGISTER.md), with their original versions and
bytes preserved.

Standard view exposes supplied properties and groups, SWE types, units,
definitions, subjects, source paths, relationships, warnings, full JSON/text,
and response-body downloads. Unknown content is retained. Each Operator fact has
a **Meaning and source** disclosure identifying its source and mapping.

### Inspect the power arrangement

Select **Power arrangement · source replacement**, or open `/?example=power`.
Overview connects the source and station for the selected historical time;
Equipment lets you inspect the two distinct sources and the station; Condition
keeps a reading's subject separate from its reporting system. The three supplied
time choices show A before replacement, B at replacement, and B's one 12.6 V
observation at 10:10 UTC. No observation is displayed before its supplied time.
All times belong to the synthetic September 2026 example, not the current clock.

**Meaning and source**, **Model, mapping, and evidence**, and the Standard-view
record selector expose exact source paths, original bodies, and the distinction
between RFC donor concepts, MPSS binding rules, and application presentation.
See [the power source-to-behavior mapping](Docs/Design/POWER_ARRANGEMENT.md).

### Read an existing resource

Open **Use your existing CSAPI server** and enter a direct System resource URL. The client
issues GET with credentials omitted. If the response advertises a typed SensorML
`alternate` or `describedby` link, at most one is followed and both responses are
retained. There is no guessed `/details` route or fixed server configuration.
Browser CORS must allow the request; authenticated services and collection browsing
are outside this increment. HTTP errors and invalid JSON retain any received body
for Standard-view inspection. No existing test server was changed or claimed as
validated by the local fixture checks.

### Interpretation limits

MPSS v0.3.5 does not yet define all device-specific bindings required by the
historical device screens. Those cases recognize the technical-description group
with its four Text terms; their other device facts carry explicit definitions in
`https://example.invalid/glaux-client/experiment/v1/`. These provisional mappings
are visibly identified and documented in the
[source-to-view mapping](Docs/Design/DETAILS_VIEW_MAPPING.md); they do not revise
MPSS or demonstrate whole-profile conformance or a measured profile benefit.

The separate power example recognizes selected existing R16 relationships,
replacement history, and R11/R17 observation context. It resolves the fixed bundle
through an explicit local catalogue; it does not discover a server's equipment,
deployments, streams or schemas. The supplied external sources are not established
as batteries. The full proposed power/battery module and native RFC MIBs remain
outside this implementation. Other quantities or unresolved subject contexts
remain source evidence without an invented reading.

The interpreter checks supplied group/term definitions, carrier, subject, type,
unit, code space, nil markers, and applicable cardinality. It never selects
semantics using manufacturer names, display labels, or identifier spelling.
Conflicts and unsupported data remain inspectable in Standard view. Estimates,
measurements, configuration choices, reported labels, source clocks, and retrieval
timestamps retain their separate meanings. No overall health or readiness is
inferred.

### Code and continuity

- `src/data`: read-only retrieval, independent source capture, actual pinned-library
  parsing, and generic extraction.
- `src/profile`: bounded interpretation using the published-in-this-repo mapping;
  no vendor adapter or generalized ontology engine.
- `src/presentation`: accessible views, tabs, source disclosures, and raw inspection.
- `public/fixtures`: synthetic records, including the seven-body power example,
  served through the source-preserving HTTP boundary.
- `tests`: offline retrieval/preservation, interpretation, and pinned-library checks.

[Current work](Docs/Plans/CURRENT_WORK.md) is the durable continuation point. It
records what was reconstructed, what was verified, open limits, and the next step.
The missing prior local implementation was **not recovered**; this branch is a
new implementation based on the recovered source evidence.

The public experiment is hosted at <https://glaux-client.pages.dev/>.
[Deployment details](Docs/Plans/CLOUDFLARE_DEPLOYMENT.md) record the runtime commit
actually uploaded, Cloudflare deployment, immutable URL, and live checks for each
increment. The project uses Direct Upload: a GitHub push does not update it;
later runtime revisions require another explicit upload.

Device controls, server writes, existing-server infrastructure modifications,
profile changes, and upstream-library changes remain outside this increment.

See the [documentation index](Docs/README.md), [development boundaries](AGENTS.md), and
[third-party notices](public/THIRD_PARTY_NOTICES.txt).
