# Codex in VS Code: deployment procedure

**Status, 24 October 2026: the power, index, and Resource Details template deployments are complete.**
The latest verified runtime is `71297c971e2e7532f7c7139600f41e9b58bdcc22`; see
[the deployment record](CLOUDFLARE_DEPLOYMENT.md). This document retains the
repeatable procedure for a subsequent implementation revision. Read
[CURRENT_WORK](CURRENT_WORK.md) and [MERLIN continuity](CONTINUITY.md) first;
an artifact-only publication is not a request to rerun the completed upload.

## Procedure for a later implementation revision

For a later authorized runtime update, build and deploy the checked current head of
`OS4CSAPI/glaux-client`, branch `work/details-view-20261023`, to the existing
Cloudflare Pages project **glaux-client**. The template and index are already live; these
instructions do not request another upload.
Use the local Wrangler session that performed the earlier upload if still valid.
No new research, UI redesign, profile changes, upstream-library changes, device
commands or writes to CSAPI servers are required.

Read `AGENTS.md`, `Docs/Plans/CURRENT_WORK.md`, and
`Docs/Plans/CLOUDFLARE_DEPLOYMENT.md` first. The initial power checkpoint is
`64e2287b8b6366eed7fdf0bd83ca502997caeb9d`; use the latest branch head, including
subsequent verification/UI fixes, rather than resetting to that initial commit.

## Preserve and build the actual GitHub revision

1. Inspect the existing checkout, branch, remote, status and local authentication.
   Preserve all user changes. Use a separate checkout/worktree if necessary.
2. Fetch `origin work/details-view-20261023` and inspect intervening commits.
   Use the exact current GitHub revision; record its SHA. Do not merge draft PR #1
   solely to make deployment possible.
3. Initialize the pinned submodule. Its gitlink remains
   `4ca1d7db9b1ccdf545adbef42ef941139fe11977`; do not use `--remote`.
4. Build using the existing lockfiles and Node 24 or the already working Node 26:

```sh
git submodule update --init --recursive
npm ci --no-audit --no-fund
npm test
npm run build
```

The application has no new runtime dependency. The completed verification scope
and counts are in CURRENT_WORK. Do not attribute earlier results to untested changes.

## Deploy to the existing project

The project is **Pages Direct Upload**, with production branch metadata
`work/details-view-20261023`. Git pushes do not trigger uploads. Do not recreate
it, switch hosting, or assume it became Git-integrated.

Check the local CLI authentication using the existing Wrangler installation.
The preceding deployment used Wrangler 4.152.0. Run its corresponding Pages command:

```sh
wrangler pages deploy dist --project-name glaux-client --branch work/details-view-20261023
```

If the existing setup invokes Wrangler through npm, use the equivalent
`npx wrangler pages deploy ...` command. It is not an application dependency.
Run from the clean checkout of the selected GitHub revision so commit metadata
matches the built source. Record the deployment ID, immutable deployment URL,
production URL, deployed SHA and result. Use normal secure login if this local
session has expired; never paste credentials in chat or commit them.

## Verify the uploaded example

Open the returned deployment and <https://glaux-client.pages.dev/?example=power>.
Use `scripts/verify-power-browser.cjs` against that URL when Playwright/Chromium is
available; its `GLAUX_BASE_URL` should be the origin without a query string.
Also run the original browser script if the deployment itself needs regression
verification. Inspect the actual UI and requests, not just the HTML title.

The new example must show:

- After replacement: source B supplies the same station, with a 12.6 V observation
  describing B, reported by the station at 2026-09-02T10:10:00Z.
- Before replacement: source A supplies the station; no voltage observation is
  shown because no earlier sample was supplied.
- At 10:00 UTC replacement: B's interval is applicable and A's has ended; the
  10:10 reading remains future evidence, not a displayed reading.
- Equipment inspection keeps A and B distinct. The sources are not declared
  batteries, and the relationship does not establish actual power flow.
- Standard view can select each original record and download unchanged bytes.

## Write back

Update CURRENT_WORK, CLOUDFLARE_DEPLOYMENT and README with the actual outcome,
exact deployed GitHub SHA and verified link. Commit and push the documentation
on the same working branch. Report the new power deep-link to the user only after
verifying that it loads this increment. If authentication or deployment blocks,
record the exact observed blocker; the prior live site remains the old version.

The chat workspace's filesystem, cookies and authentication are not assumed to be
shared with this VS Code environment. All implementation and continuation material
needed for this task belongs in GitHub; no chat-only source artifact is required.
