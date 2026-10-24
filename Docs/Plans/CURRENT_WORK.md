# Current Details View work

Updated 23 October 2026. **Power-arrangement implementation and local verification
are complete. Deployment of this increment is still pending.** The public site
remains the earlier four-example version.

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
- Last verified public deployment: `53c3ce532abc484dc421696566a573179635d125`,
  Cloudflare Pages deployment `602be95e-6fc1-418f-8119-4d63da5ddba5`,
  <https://glaux-client.pages.dev>.

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
[Details View mapping](../Design/DETAILS_VIEW_MAPPING.md). Original research
archives and internal documents remain outside this public repository.

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
| New live deployment | Not performed from this workspace |

The [browser verification record](../Testing/BROWSER_VERIFICATION.md) links the
actual emitted results, reproducible scripts, and selected local screenshots.

Checks use explicitly synthetic local data. They establish this bounded behavior,
not complete OGC/MPSS/RFC conformance, live-server interoperability, production
readiness, or measured comparative operator benefit.

## Deployment boundary and next action

The existing Pages project is **Direct Upload**. Pushing GitHub does not deploy it.
The earlier upload succeeded through an authenticated Wrangler session in the
user's local Codex/VS Code environment. That session is not available here: this
workspace has no Wrangler OAuth configuration or Cloudflare API credential, and
the available Cloudflare browser is at its ordinary sign-in screen.

Deploy the latest checked GitHub revision through the existing authenticated local
environment. The concrete
[Codex deployment handoff](CODEX_VSCODE_HANDOFF.md) records the existing project,
branch, command and required live verification. Do not create another project,
merge the PR just to deploy, transfer credentials between environments, or assume
that an older green run or old public URL proves the new example is live.

Update [the deployment record](CLOUDFLARE_DEPLOYMENT.md) only after a successful
upload and live verification. Preserve any unrelated local changes. Save each
meaningful continuation to the working branch; chat commentary is not a source
checkpoint.
