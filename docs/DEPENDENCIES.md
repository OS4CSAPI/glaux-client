# Dependency provenance and reproducibility

## Selected CSAPI revision

| Item | Selection |
| --- | --- |
| Repository | https://github.com/OS4CSAPI/ogc-client-CSAPI_2 |
| Branch | `phase-10` |
| Full commit | `4ca1d7db9b1ccdf545adbef42ef941139fe11977` |
| Inspection date | 2026-10-23 |
| Previously reviewed checkpoint | `phase-9`, `754411897173c2ec4debaa9bcf4ed9e0f8a9e230` |
| Package identity | `@camptocamp/ogc-client`, `1.3.1-dev` |
| Used export | `@camptocamp/ogc-client/csapi` |
| License | BSD-3-Clause, Copyright (c) 2023, Camptocamp |

Remote refs and commit history were inspected, not selected by newest timestamp.
The remote default still points to the reviewed `phase-9` checkpoint. `phase-10`
is its descendant and documented CSAPI continuation, including the CSAPI public
documentation/export work, Prettier migration, and AD01 upstream-compatibility
delivery handoff. Its current head is selected deliberately instead of the stale
default or an unrelated experimental branch. The handoff is recorded upstream in
`docs/research/phase-10/09-task-ad5-delivery-handoff.md`; those research records
are not copied into this application's documentation.

## Source/build arrangement

The Git gitlink at `.dependencies/ogc-client` pins the exact source revision.
`.gitmodules` records the repository and branch for provenance; builds do not
follow the moving branch. The build script additionally checks the exact SHA
and rejects tracked source modifications. This is a separate dependency checkout,
not copied application source, a fork, or a monorepo.

The upstream package exports `dist/index.js` and the explicit CSAPI subpath
`dist/ogc-api/csapi/index.js`, with corresponding declarations. The distribution
is not tracked and there is no Git-install `prepare` hook. A plain Git dependency
would therefore install without usable exports. The npm registry release is not
substituted for this CSAPI revision.

After a recursive clone, `npm ci` links the local package using the committed
application lockfile. Its postinstall script:

1. Verifies the submodule HEAD and tracked source state.
2. Runs `npm ci` inside the library against its **upstream committed lockfile**.
3. Clears only the library's generated `dist` directory.
4. Runs upstream `build:worker` (including declarations) and `build:node`.
5. Runs the same esbuild browser transpilation as upstream `build:browser`,
   enumerating TypeScript files with Node instead of POSIX `find`, excluding
   `*.spec.ts` and `src/worker/index.ts` as upstream does.

This small orchestration adaptation avoids upstream POSIX `rm`/`find` shell
requirements on Windows without changing upstream source or build configuration.
All compiler/build versions for the library come from its own lockfile, not the
application's tool versions. Both checkouts' generated files and node_modules are
uncommitted. No npm package is published. Public GitHub/npm access is needed for
installation, but runtime checks and tests require no server.

`tests/csapi.smoke.test.ts` imports the actual package subpath, constructs its
`CSAPIQueryBuilder` through `createCSAPIBuilder`, checks a systems URL, and exercises
its SWE Common quantity parser. There are no aliases, copied parsers, or local
CSAPI imitations. The landing page also loads an actual CSAPI resource constant.

## Notices

Preserve the upstream `LICENSE` in the submodule. The BSD-3-Clause license and
Camptocamp attribution are reproduced in `public/THIRD_PARTY_NOTICES.txt`, which
Vite copies unchanged to production output and the landing page links to.
Keep these notices with distributed application builds; do not imply upstream
endorsement. Transitive package licenses remain in their installed packages;
reassess notice requirements if more library functionality is bundled.

## Deliberate updates

1. Inspect upstream refs, CSAPI history, exports, build requirements, and notices;
   confirm the intended CSAPI continuation instead of choosing the newest branch.
2. Fetch in the submodule and explicitly check out the reviewed **full SHA**.
   Do not use `git submodule update --remote` as routine setup.
3. Update the exact SHA guard in `scripts/build-ogc-client.mjs`, the gitlink,
   this record (including branch/date/rationale), and the README together.
4. If upstream package metadata changes, regenerate the application lockfile
   with `npm install`. Never hand-edit either dependency lockfile.
5. Run `npm ci`, type-check, offline tests, and production build; reproduce using
   a fresh recursive checkout. Review notices and output before committing.
6. Commit the gitlink, provenance, build-script, and lockfile changes together.
   Do not modify or push upstream as part of an application dependency update.
