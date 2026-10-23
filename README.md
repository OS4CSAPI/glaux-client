# Glaux Client

An experimental **OS4CSAPI** application evaluating whether the MERLIN domain
information model and Managed Physical Sensing Systems (MPSS) profile can support
a consistent, useful sensor-surveillance operator interface.

TRSS unattended ground sensors and McQ OmniSense II are the motivating systems.
Their information must remain meaningfully distinct while being organized through
CSAPI, SensorML, and SWE Common. Future evaluation will compare competent generic
standards-based access with profile-aware interpretation of the **same
server-hosted information**, using selected existing Resource Details wireframes.

This prototype is intended for possible future contribution to the Glaux effort.
It does not claim adoption or endorsement by DGIWG or another organization.

## Setup

Prerequisites: Git and Node.js 24 LTS (with npm); Node 26 is also supported.
No server, credentials, private configuration, or research collection is needed.

```sh
git clone --recurse-submodules https://github.com/OS4CSAPI/glaux-client.git
cd glaux-client
npm ci
npm run dev
```

For an existing non-recursive clone, run `git submodule update --init --recursive`
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

## Library dependency

This application uses the CSAPI-enabled
[OS4CSAPI/ogc-client-CSAPI_2](https://github.com/OS4CSAPI/ogc-client-CSAPI_2)
library, not an assumed-equivalent npm release. It is a separate, commit-pinned
Git submodule in `.dependencies/ogc-client`, linked as a local npm dependency
under its upstream package name, `@camptocamp/ogc-client`.

Selected branch: **phase-10**; commit:
`4ca1d7db9b1ccdf545adbef42ef941139fe11977` (inspected 2026-10-23).
See [dependency provenance and build details](Docs/DEPENDENCIES.md).

## Current status and boundaries

**Bootstrap only:** a TypeScript/Vite landing page, actual CSAPI import and
offline smoke tests, reproducible dependency builds, and local-check CI.
There is no completed TRSS/OmniSense integration, demonstrated profile benefit,
profile resolver, vendor adapter, device control, or implemented operator view.

- `src/data`: standard library access and, later, independent original response
  capture. Original bytes and metadata must remain separate from parsed models.
- `src/profile`: reserved for evidence-based profile interpretation; no rules yet.
- `src/presentation`: operator-facing presentation; currently just the landing page.

No unknown content may be silently discarded. Manufacturer names, display labels,
and identifier spelling are not semantic evidence. Generic mode must remain
competent at standard properties and relationships.

The future starting UI scope is the existing **Overview, Equipment, and Condition**
wireframes, not a new interface inferred from this brief. Actual wireframe/profile
source materials must be consulted when that work starts; none are imported here.
The existing pygeoapi CSAPI test server is intended for later evaluation and is
unchanged by this bootstrap. No infrastructure or live-server work is included.

See the [documentation index](Docs/README.md), [development boundaries](AGENTS.md), and
[third-party notices](public/THIRD_PARTY_NOTICES.txt).
