# Cloudflare deployment continuation

## Deployment result

**Completed 23 October 2026.** The latest implementation was built from the exact
pinned submodule and deployed to Cloudflare Pages. Local Wrangler OAuth was already
authenticated to the user's Cloudflare account with Pages write access, so no new
sign-in was required.

Cloudflare's current Wrangler first attempted to delegate new Pages project creation
to Workers and failed before creating a resource because no Worker entry point was
present. Following Wrangler's explicit fallback, the project was created through
the legacy Pages command with `--force`, then deployed with `wrangler pages deploy`.
This is a **Direct Upload**, not Git integration; future pushes will not deploy
automatically. Cloudflare requires a new project to switch this project type.

| Result | Actual value |
| --- | --- |
| Project | `glaux-client` |
| Deployment method | Cloudflare Pages Direct Upload via Wrangler 4.152.0 |
| Production branch metadata | `work/details-view-20261023` |
| Deployed Git commit | `53c3ce532abc484dc421696566a573179635d125` |
| Deployment ID | `602be95e-6fc1-418f-8119-4d63da5ddba5` |
| Production URL | <https://glaux-client.pages.dev> |
| Immutable deployment URL | <https://602be95e.glaux-client.pages.dev> |
| Build result | Passed with Node 26.12.0; pinned library `4ca1d7d` built successfully |
| Live browser verification | 23 checks passed; zero browser script errors |

The live run exercised TRSS ETU-II, OmniSense Core2, OmniSense Core5ADS, and the
synthetic MPSS technical-description example. Overview, Equipment, and Condition
tabs worked across Operator and Standard modes. The run also verified fixture/raw
body access, exact downloaded bytes, keyboard tab behavior, source switching, and
the 390 px layout. These checks establish the bundled static examples, not an
external CSAPI server integration.

## Checked GitHub source

| Item | Selection |
| --- | --- |
| Repository | [OS4CSAPI/glaux-client](https://github.com/OS4CSAPI/glaux-client) |
| Source branch | [work/details-view-20261023](https://github.com/OS4CSAPI/glaux-client/tree/work/details-view-20261023) |
| Implementation commit deployed | [53c3ce532abc484dc421696566a573179635d125](https://github.com/OS4CSAPI/glaux-client/commit/53c3ce532abc484dc421696566a573179635d125) |
| Pinned library gitlink | `4ca1d7db9b1ccdf545adbef42ef941139fe11977` at `.dependencies/ogc-client` |

Use the checked branch containing the implementation when connecting GitHub.
Record the actual deployed commit after Cloudflare finishes its build.

## Prepared Pages configuration

| Setting | Value |
| --- | --- |
| Project type | Cloudflare Pages with Git integration |
| Repository | `OS4CSAPI/glaux-client` |
| Production/source branch | `work/details-view-20261023` |
| Root directory | Repository root; leave blank |
| Framework preset | None; enter the explicit build command below |
| Build output directory | `dist` |
| Build variable | `NODE_VERSION=24` |
| Build variable | `SKIP_DEPENDENCY_INSTALL=1` |

Use these build variables for both production and preview builds. Build command:

```sh
git submodule update --init --recursive && npm ci && npm run build
```

The repository is a static Vite client, so Pages can serve the existing build
without a runtime migration, Worker entry point, or Cloudflare Vite plugin.
Its existing `.nvmrc` selects Node 24. Root `npm ci` runs the postinstall script,
which verifies the exact library SHA and builds the library from its own lockfile.
The submodule must therefore be initialized before dependency installation.
The explicit command and skip-install variable preserve that order. Do not add
`--remote` to the submodule command: the gitlink, not the moving library branch,
selects the dependency. See [dependency provenance](../DEPENDENCIES.md).

## Official configuration references

Checked 23 October 2026:

- [Pages Git integration](https://developers.cloudflare.com/pages/configuration/git-integration/): connected GitHub builds and branch previews.
- [Pages build configuration](https://developers.cloudflare.com/pages/configuration/build-configuration/): repository root, build command, and output directory.
- [Pages build image](https://developers.cloudflare.com/pages/configuration/build-image/): `.nvmrc`/`NODE_VERSION` overrides and `SKIP_DEPENDENCY_INSTALL`; v3 does not detect Node from `package.json.engines`.
- [Pages repository-clone troubleshooting](https://developers.cloudflare.com/pages/configuration/debugging-pages/): valid submodule entries require both path and URL. The repository supplies a public HTTPS URL; the explicit build command ensures recursive initialization.

## Continuation

The current deployment is complete and verified. If automatic deployments are
later required, create a separate Git-integrated Pages project connected to the
same repository and branch using the prepared settings above; do not describe this
Direct Upload project as Git connected.
