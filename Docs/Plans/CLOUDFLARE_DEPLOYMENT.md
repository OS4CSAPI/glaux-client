# Cloudflare deployment continuation

## Request and current status

The user requested a Cloudflare deployment of the latest implementation from
GitHub so the application can be viewed. This record prepares that authorized
deployment; it does not report a completed deployment.

**Status as of 23 October 2026:** configuration prepared; deployment is blocked
at Cloudflare sign-in. The authentication attempt returned to
[Cloudflare login](https://dash.cloudflare.com/login) with the visible error:
"Unable to sign in. Try again or use your email and password."
Automated sign-in has stopped. Manual authentication is the next action; its
completion has not been confirmed. No Cloudflare project, build, deployment,
or live application URL was created or verified during this attempt.

## Checked GitHub source

| Item | Selection |
| --- | --- |
| Repository | [OS4CSAPI/glaux-client](https://github.com/OS4CSAPI/glaux-client) |
| Source branch | [work/details-view-20261023](https://github.com/OS4CSAPI/glaux-client/tree/work/details-view-20261023) |
| Implementation commit | [eb9a7f45aa7db31ef71196e807b69a300d473b40](https://github.com/OS4CSAPI/glaux-client/commit/eb9a7f45aa7db31ef71196e807b69a300d473b40) |
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

## Completion record to fill after deployment

Finish Cloudflare authentication manually first; takeover has not been confirmed
as completed. Then connect the checked repository and branch, apply the settings,
and inspect the actual build outcome. Record the Cloudflare project,
deployment identifier, deployed Git SHA, build result, and live URL here. Verify
the loaded application and its example fixtures at that URL before describing
the deployment as complete. Until authentication succeeds, this remains a prepared
configuration blocked at sign-in; no deployment has started.
