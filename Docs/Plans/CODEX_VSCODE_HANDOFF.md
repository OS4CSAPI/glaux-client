# Codex in VS Code: finish the Cloudflare deployment

## Authorized objective

The user has authorized deploying the latest Glaux Client implementation from
GitHub to Cloudflare so they can view it. Continue that deployment in the user's
existing VS Code environment. The application is already implemented; this task
does not require redesign, renewed research, a replacement library, profile
changes, upstream-library changes, device commands, or writes to existing CSAPI
servers. Building the existing application for deployment is part of the task.

## Read first

1. [AGENTS.md](../../AGENTS.md).
2. [CURRENT_WORK.md](CURRENT_WORK.md).
3. [CLOUDFLARE_DEPLOYMENT.md](CLOUDFLARE_DEPLOYMENT.md).

## Known repository state at handoff

| Item | Last checked value |
| --- | --- |
| Repository | [OS4CSAPI/glaux-client](https://github.com/OS4CSAPI/glaux-client) |
| Implementation branch | `work/details-view-20261023` |
| Implementation commit | `eb9a7f45aa7db31ef71196e807b69a300d473b40` |
| Continuity checkpoint before this handoff | `44b94809b526c94fc37d374d276e6192d94c08de` |
| Review | [Draft PR #1](https://github.com/OS4CSAPI/glaux-client/pull/1) |
| `main` | Bootstrap at the last check; the implementation remains on the branch above |
| Library gitlink | `4ca1d7db9b1ccdf545adbef42ef941139fe11977` at `.dependencies/ogc-client` |

The previous workspace was clean at the continuity checkpoint. This handoff will
have a subsequent commit; verify the actual remote head instead of resetting to
one of these historical SHAs. Deploy the implementation branch directly. Do not
merge the draft PR merely to make deployment possible.

## First actions in the actual local workspace

1. Locate the user's real checkout and inspect its status, branch, remotes and
   HEAD before changing anything. Confirm the origin is the repository above.
2. Preserve all existing user changes. Do not reset, clean, discard, or silently
   stash them. Use a separate worktree/checkout if deployment preparation would
   interfere with ongoing work.
3. Fetch the remote branch and inspect its current head and intervening commits.
   Confirm the selected deployment revision contains the implementation commit.
   Keep the actual selected SHA in the continuation record.
4. Read the local build settings and initialize the pinned submodule before
   dependency installation. Its branch name is provenance; the gitlink is the pin.

The chat workspace path, browser tabs, cookies, installed tools and authenticated
sessions are not assumed to exist on the user's machine. No secret or filesystem
sharing between those environments has been established.

## Cloudflare status and authentication

The latest retry in the prior browser still returned the generic error:
"Unable to sign in. Try again or use your email and password."
No Cloudflare project, build, deployment or live URL was created or verified.
The user's local Cloudflare authentication has not been checked by this handoff.

First check available local authentication, including an existing browser or CLI
session. Use official CLI/API operations that support the selected deployment method.
Only if a valid authorized session is unavailable, have the user
complete the official secure login in their local browser. Do not copy cookies,
tokens, passwords or authentication codes out of the prior environment, request
them in chat, or commit them.

Use the user-selected Cloudflare account. Prefer **Pages Git integration** so
future pushes to the selected GitHub branch can build automatically. If a local
Wrangler deployment is the practical way to deliver the authorized Cloudflare
preview, build only the verified GitHub revision and record that deployment
method explicitly. A Direct Upload is not a Git-connected automatic deployment.
Cloudflare requires a new project to change Direct Upload to Git integration;
see its [Direct Upload guide](https://developers.cloudflare.com/pages/get-started/direct-upload/).
Keep the deployment on Cloudflare; no custom domain or DNS change is needed.

If hosting authentication blocks again, preserve the exact observed blocker and
provide a working local preview so the user can inspect the existing client.
Start `npm run dev`, or `npm run preview` after a successful build, and verify the
actual local URL reported by that process before returning it. A local preview
is not a completed Cloudflare deployment.

## Exact prepared build settings

| Setting | Value |
| --- | --- |
| Project type | Pages with Git integration |
| Repository | `OS4CSAPI/glaux-client` |
| Production/source branch | `work/details-view-20261023` |
| Root directory | Repository root; leave blank |
| Framework preset | None; enter the explicit build command |
| Build output directory | `dist` |
| Build variables, production and preview | `NODE_VERSION=24`, `SKIP_DEPENDENCY_INSTALL=1` |

```sh
git submodule update --init --recursive && npm ci && npm run build
```

Keep install scripts and development dependencies enabled. `npm ci` invokes
`scripts/build-ogc-client.mjs`, which verifies the exact library SHA, installs its
own locked dependencies and builds its exports. Root `npm run build` runs
TypeScript checking and Vite. The existing `.nvmrc` selects Node 24. Do not use
`--ignore-scripts`, `--omit=dev`, or `git submodule update --remote`.

This is a static Vite application. Pages serves the existing `dist` output;
no runtime migration, Worker entry point or Cloudflare Vite plugin is needed.
The deployment note links the checked official Cloudflare build documentation.

## Previous validation and present limits

The prior workspace recorded 45 passing tests across four files, a successful
production build, and 23 passing browser checks with no browser script errors.
These results do not establish the state of this local machine or a deployment.
See the [recorded browser results](../Testing/BROWSER_RESULTS.json),
[earlier implementation CI run](https://github.com/OS4CSAPI/glaux-client/actions/runs/39995569307),
[PR checks](https://github.com/OS4CSAPI/glaux-client/pull/1/checks), and
[GitHub Actions](https://github.com/OS4CSAPI/glaux-client/actions) for actual evidence.
Check the result for the selected head; do not attribute an older green run to it.
Repeat checks only for an actual change, failed build or concrete deployment risk.

## Completion and writeback

1. Complete the Pages deployment from the selected GitHub revision using the
   settings above, recording whether it uses Git integration or a local upload.
   Confirm the deployed build corresponds to the revision actually selected.
2. Open the resulting live URL. Verify the Details View loads and its Overview,
   Equipment and Condition tabs work in Operator and Standard modes.
3. Check all four bundled examples: TRSS ETU-II, Core 2 equipment, separate Core 5
   ADS condition, and the synthetic MPSS technical-description record. Confirm
   fixture requests and built assets succeed; do not infer server integration.
4. Record the actual project, deployment identifier, deployed SHA, build outcome,
   live URL and verification in `CLOUDFLARE_DEPLOYMENT.md`. Update `CURRENT_WORK.md`
   and the README's deployment status. Preserve any unresolved limitations.
5. Commit and push the relevant continuation/configuration changes to the working
   branch, excluding secrets and unrelated user work. Report the live URL and
   actual deployed SHA. If blocked, record the observed blocker and next concrete
   action instead of claiming completion.
