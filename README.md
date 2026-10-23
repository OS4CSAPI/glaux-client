# Glaux Client

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

The client provides a compact System card with **Operational → Overview,
Equipment, Condition**, plus Operator and Standard views over one captured model.
Switching view or tab does not retrieve different information.

Four explicitly synthetic local HTTP examples are included:

| Example | What it exercises |
| --- | --- |
| TRSS ETU-II | Selected detector configurations, separately disclosed supported options, and qualified battery estimator values |
| OmniSense Core2 | Five source-reported transducer labels, without invented physical identities or discovery times |
| OmniSense Core5ADS | A distinct historical condition case: 15.43 V DC, a literal unverified source clock, and six individual diagnostic findings |
| MPSS technical-description contract | Fully invented manufacturer/model/revision values exercising the exact bounded MPSS binding |

These newly authored records are source-informed test fixtures, not recovered
native device responses or current device state. The companion
[source index](Docs/Research/SOURCE_INDEX.md) records the reviewed source versions
and locators without redistributing the original documents.

Standard view exposes supplied properties and groups, SWE types, units,
definitions, subjects, source paths, relationships, warnings, full JSON/text,
and response-body downloads. Unknown content is retained. Each Operator fact has
a **Meaning and source** disclosure identifying its source and mapping.

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

MPSS v0.3.5 does not yet define all device-specific bindings required by these
screens. The only recognized MPSS subset here is the technical-description group
with its four Text terms. Device examples instead carry explicit definitions in
`https://example.invalid/glaux-client/experiment/v1/`. These provisional mappings
are visibly identified and documented in the
[source-to-view mapping](Docs/Design/DETAILS_VIEW_MAPPING.md); they do not revise
MPSS or demonstrate whole-profile conformance or a measured profile benefit.

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
- `public/fixtures`: the four synthetic records, served through the same HTTP path
  as remote data.
- `tests`: offline retrieval/preservation, interpretation, and pinned-library checks.

[Current work](Docs/Plans/CURRENT_WORK.md) is the durable continuation point. It
records what was reconstructed, what was verified, open limits, and the next step.
The missing prior local implementation was **not recovered**; this branch is a
new implementation based on the recovered source evidence.

No deployment, device controls, server writes, infrastructure modifications,
profile changes, or upstream-library changes are included.

See the [documentation index](Docs/README.md), [development boundaries](AGENTS.md), and
[third-party notices](public/THIRD_PARTY_NOTICES.txt).
