# Cloudflare deployment continuation

## Resource Details Activity-table deployment result

**Completed 26 October 2026.** A new page reuses the recovered Resource Details
template and populates only Activity > Table. The table presents Observation,
Command, and System Event wireframe rows with All, Observations, Commands, and
System Events toggles. The original template URL remains available and unchanged.

| Result | Actual value |
| --- | --- |
| Project / environment | `glaux-client` / production |
| Method | Cloudflare Pages Direct Upload via authenticated local Wrangler 4.152.0 |
| Source branch | `work/details-view-20261023` |
| Deployed Git commit | `db96c584fdf52715e4a005be2c4159b1bc131b24` |
| Deployment ID | `ee6812b6-d964-4407-9fac-6652d0db965f` |
| Live Activity page | <https://glaux-client.pages.dev/?page=resource-details-activity> |
| Preserved template | <https://glaux-client.pages.dev/?page=resource-details-template> |
| Immutable deployment | <https://ee6812b6.glaux-client.pages.dev/?page=resource-details-activity> |
| Build result | 74 tests passed; TypeScript and Vite production build passed |
| Live Activity verification | 15 checks passed; zero browser script errors |
| Live template regression | 27 checks passed; zero browser script errors |

The live verification confirmed the 560 x 440 frame, all three required resource
types, each filter and the All reset, reviewed semantic columns, blank Charts
canvas, and no fixture, XHR, or remote-source requests. The template regression
confirmed that its blank default canvas, tabs, overflow, resize behavior, keyboard
navigation, and data-free operation remain intact.

## Resource Details template deployment result

**Completed 24 October 2026 at 4:34:47 p.m. EDT.** The recovered 560 × 440
working frame is live as a standalone, initially blank wireframe canvas and is
listed on the six-page homepage index. The fixed identity, two navigation rows,
and top/bottom marking placeholders surround an internally scrolling body.
Native resize, explicit size/reset controls, and optional layout-only overflow
samples support review without loading source data.

| Result | Actual value |
| --- | --- |
| Project / environment | `glaux-client` / production |
| Method | Existing Pages Direct Upload through the Cloudflare connector and scoped-JWT asset API |
| Source branch | `work/details-view-20261023` |
| Deployed Git commit | `71297c971e2e7532f7c7139600f41e9b58bdcc22` |
| Deployment ID | `97c801c4-c44f-4484-a175-e6651639fe07` |
| Live template | <https://glaux-client.pages.dev/?page=resource-details-template> |
| Production index | <https://glaux-client.pages.dev/> |
| Immutable deployment | <https://97c801c4.glaux-client.pages.dev/> |
| Completed UTC | `2026-10-24T20:34:47.096747Z` |
| Assets | 16 files, 199,951 bytes; 3 changed assets uploaded, all hashes confirmed present |
| Build and CI | 74 offline tests, TypeScript/Vite build, and [GitHub CI](https://github.com/OS4CSAPI/glaux-client/actions/runs/40130331258) passed |
| Local browser checks | 27 template, 44 index, 23 baseline, and 44 power checks passed |
| Production browser checks | 27 template and 44 index checks passed; zero browser script errors |

The source was published to GitHub, fetched, compared with the local files, and
rebuilt from the clean matching revision before upload. The project canonical
deployment was confirmed to match this ID and commit. The previous five examples,
original source artifacts, profile, and pinned library remain unchanged.

[Template live results](../Testing/TEMPLATE_LIVE_BROWSER_RESULTS.json) and
[index live results](../Testing/INDEX_LIVE_BROWSER_RESULTS.json) retain the checks,
origin, and runtime/deployment identity. The managed verification proxy required
`ignoreHTTPSErrors` for Chromium, as in the earlier deployment; it changes only
the verification browser and does not establish the public certificate chain.
Native scrollbar rendering was retained for template visual review. Local blank,
overflow, resized, and narrow screenshots were inspected; the live template and
index passed the same behavior checks.

[The design record](../Design/RESOURCE_DETAILS_TEMPLATE.md) distinguishes the
recovered working frame from provisional navigation labels and the spacing,
scrollbar, and resize choices made for this review canvas. This is not an actual
Dockview-hosted integration or a finalized PBI.

## Experiment-index deployment result

**Completed 24 October 2026 at 12:52:53 p.m. EDT.** The homepage now lists the five
experiment pages with descriptions, latest recorded change summaries, and dates
and times in America/New_York. Each example has a link back to the index. Existing
direct example URLs remain valid, and the selector keeps its URL in sync.

| Result | Actual value |
| --- | --- |
| Project | `glaux-client` |
| Method | Pages Direct Upload through the authenticated Cloudflare connector and documented scoped-JWT asset API |
| Production branch | `work/details-view-20261023` |
| Deployed Git commit | `0d977e366e55363dd997c0f519c7cca2bc814530` |
| Deployment ID | `44f92062-a39a-4f86-9267-a63bd0935f53` |
| Production index | <https://glaux-client.pages.dev/> |
| Immutable deployment | <https://44f92062.glaux-client.pages.dev/> |
| Completed UTC | `2026-10-24T16:52:53.123781Z` |
| Asset manifest | 16 files, 185,000 bytes; 3 changed assets uploaded, all hashes confirmed present |
| Build and checks | 74 offline tests, TypeScript and Vite build, and [GitHub CI](https://github.com/OS4CSAPI/glaux-client/actions/runs/40113200519) passed |
| Local browser checks | 36 index, 23 baseline, and 44 power checks passed |
| Live index checks | 36 passed; zero browser script errors |

The source was saved to GitHub, fetched, checked against the clean local source,
and rebuilt before upload. The connector obtained the existing project's scoped
upload JWT. The asset flow used `check-missing`, `upload`, and `upsert-hashes`, with
the BLAKE3 file-key algorithm from Wrangler 4.152.0, then created the production
deployment with its manifest and exact commit metadata. The canonical project
deployment was confirmed to be the new deployment above. Credentials were not
stored in the repository.

The installed Wrangler 4.152.0 hidden asset-upload command still required general
CLI authentication in this environment despite receiving `CF_PAGES_UPLOAD_JWT`.
Do not assume that command works without local authentication. An authenticated
Wrangler session or the documented scoped-JWT asset API remains the supported
transfer path; the connector can finalize the multipart deployment.

[Live browser results](../Testing/INDEX_LIVE_BROWSER_RESULTS.json) retain the
actual checks. Chromium required a temporary `ignoreHTTPSErrors` context because
the managed execution proxy's certificate was not trusted by that browser. This
is a verification-environment setting, not an application/deployment setting; the
run verifies UI behavior and does not establish the public TLS certificate chain.
The 1280 px and 390 px screenshots were inspected. The original source fixtures,
technical profile, and pinned library remain unchanged.

## Power-arrangement deployment result

**Completed 24 October 2026.** The latest checked GitHub revision was rebuilt with
the exact pinned library, uploaded to the existing Cloudflare Pages project using
the authenticated local Wrangler session, and verified on the production origin.

| Result | Actual value |
| --- | --- |
| Project | `glaux-client` |
| Deployment method | Cloudflare Pages Direct Upload via Wrangler 4.152.0 |
| Production branch metadata | `work/details-view-20261023` |
| Deployed Git commit | `d74b33dabc5fdfcf22574b8efa7f436b4cf32857` |
| Deployment ID | `770d234a-3cb5-415a-aa96-b8fea45180c4` |
| Production URL | <https://glaux-client.pages.dev> |
| Power deep link | <https://glaux-client.pages.dev/?example=power> |
| Immutable deployment URL | <https://770d234a.glaux-client.pages.dev> |
| Build result | 74 tests passed; TypeScript and Vite production build passed |
| Live power verification | 44 checks passed; zero browser script errors |

The live verification exercised the before, replacement-boundary, and after
arrangements; the 12.6 V source-B observation; distinct source A, source B, and
station equipment; exact source-record downloads; local-only fixture requests;
keyboard behavior; and desktop/mobile layouts. It establishes this bounded
synthetic example, not live-server interoperability or actual power flow.

## Earlier four-example deployment result

**Completed 23 October 2026.** The four-example revision was built from the exact
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
| Implementation commit deployed | [71297c971e2e7532f7c7139600f41e9b58bdcc22](https://github.com/OS4CSAPI/glaux-client/commit/71297c971e2e7532f7c7139600f41e9b58bdcc22) |
| Pinned library gitlink | `4ca1d7db9b1ccdf545adbef42ef941139fe11977` at `.dependencies/ogc-client` |

The current Direct Upload contains the template, six-page index, and all five existing data examples.

## Historical Git-integration plan — not applied

These settings were prepared before the Direct Upload deployment. They are not
the current project's configuration or the next deployment procedure. Retain them
only as a reference if a separate Git-integrated project is explicitly requested.

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

The Resource Details template deployment is complete and verified. If automatic deployments
are later required, create a separate Git-integrated Pages project connected to the
same repository and branch using the prepared settings above; do not describe this
Direct Upload project as Git connected.
