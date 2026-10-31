# Controlled Glaux Client Pages deployment trigger

**Purpose:** Explicitly trigger the `Glaux Client - verified Pages deployment` GitHub Actions workflow on branch `work/details-view-20261023`. This is application deployment administration only, not a DIM/Profile model decision.

**Request logged:** 2026-10-28, to build and validate the new source-grounded Smart Citizen Kit Resource Details page alongside the original template and Activity page.

**Project:** Existing Cloudflare Pages Direct Upload project `glaux-client`.

**Safety controls:** The workflow builds and tests the exact GitHub branch revision, uses its pinned CSAPI library submodule, and deploys only when the repository Actions secret `CLOUDFLARE_API_TOKEN` is supplied. The workflow deliberately does not store or print any credential. If the secret is unavailable, the build remains useful but **the site is not deployed**.

**Research source:** The Smart Citizen case study is maintained separately under `Docs/Research/DIM_Profile_V2/Case_Studies/Real_Equipment_DIM_Validation/` on `research/dim-profile-v2`. The wireframe is source-grounded, not a verified physical-Kit data feed.

**Initial trigger:** 2026-10-28 — validate the build and detect whether the credential is in place.

**Build-only validation trigger (2026-10-28):** Rerun after workflow YAML correction; deploy remains conditional on the GitHub Actions secret.

**Wireframe build validation rerun:** Restrict this deployment workflow to executable TypeScript/test/build checks. The repository-wide historical artifact-register audit is known to fail on unrelated missing v0.5/v0.6 document links; these are left untouched by the wireframe change.

**Deployment request after GitHub Actions secret configured:** 2026-10-28. Owner confirmed the deployment secret was added to repository Actions settings. Trigger a fresh checked, tested production deployment of the existing Smart Citizen Resource Details page using the workflow's secured GitHub secret; do not log secret values. Verify the resulting Pages deployment ID and deployed source commit before declaring the page live.

**Wrangler 4 retry:** 28 October 2026. First secret-backed build passed dependency install, type-check, 74 tests and production build, but Wrangler 3.90 returned Cloudflare authentication error 10000. Cloudflare account token metadata confirms active account token with Pages Write and Account Settings Read/Write. Retry using cloudflare/wrangler-action v4.1.3 and Wrangler 4.154.0; record real deployment evidence before calling it live.

**Token preflight:** 28 October 2026. Wrangler 4.154.0 also rejected the stored GitHub secret with Cloudflare API errors 10000 and 9109. Run a narrow read-only account-token verification and Pages project access check using the Actions secret without printing credentials. Only proceed to dependency install/build and deployment if both succeed; do not change existing Pages deployment on failed check.

**Retry after corrected repository secret (2026-10-28):** Owner confirmed the stored CLOUDFLARE_API_TOKEN secret value has been updated. Trigger the configured GitHub Actions workflow again. The workflow first verifies the credential through the Cloudflare account API, then installs/builds/tests the exact branch, and deploys only upon successful checks. Preserve current production on failure.

**Profile-aware comparison deployment request — 28 October 2026:** Rebuild, type-check, run offline tests, and deploy the separate four-case candidate profile-aware Resource Details test view to the existing glaux-client Cloudflare Pages production project. Preserve the previous Smart Citizen walk-through, blank template and Activity page. This is explicitly a non-normative source-to-UI demonstration with NO actual individual Kit or live Observation; do not change research branch or conformance claims. Production deployment is allowed only after the checked CI steps succeed.

**Published measurement examples — 30 October 2026:** Build, validate and publish the addition to the existing Resource Details comparison. Direct entry: `/?page=resource-details-profile-test&case=temperature`. The new source choice reads the pinned Dragino and Campbell draft mappings; it displays published examples separately from documented fields for which no readings were supplied. It neither reads a live station nor changes the CSAPI service. Prior source choices and unrelated routes are retained. Source revision before this trigger: `d0496a8eaf6f591d0d97de0d5bf8d71f4e78ad06`.

## 31 October 2026 — Bennett's Point observation attribution

Trigger verified production deployment after adding the real Bennett's Point EE181 probe-swap observation case to the existing profile-aware Resource Details test. The workflow must type-check, run offline tests, and build before publishing.

## 31 October 2026 — Bennett's Point placement matrix application

Trigger verified production deployment after redistributing the Bennett's Point case across Overview, Equipment, Activity, Management Record, and Sources according to the candidate placement matrix. No new evidence was invented; unsupported tabs remain empty with explicit messages.

## 31 October 2026 — separate live 52°North CSAPI page

Trigger verified production deployment for a new Resource Details page that performs read-only browser GETs against the Oracle-hosted 52°North/pygeoapi CSAPI service. The existing profile-test page is preserved unchanged. The new page retrieves Systems and, for the selected System, DataStreams, Deployments, Subsystems, and available Observations.

## 31 October 2026 — dedicated live Bennett V2 page

Trigger verified production deployment for a dedicated Bennett's Point live-CSAPI page that reads the two controlled EE181 Systems, their DataStreams, and historical Observations directly from the Oracle-hosted 52°North/pygeoapi service. Existing historical and generic live pages remain separate.

## 31 October 2026 — reuse Codex Map renderer in dedicated live Bennett's Point page

Run the verified build/test/deploy workflow for the bounded Map subtab integration on the live Bennett's Point page. This change reuses `renderResourceMap()` from the separate live-map experiment without modifying the renderer, preserves both identified probe Systems, and renders the shared missing-position fallback when a selected System has no reported geometry. No server write or invented site/probe coordinates are involved. See [the integration design note](../Design/BENNETT_LIVE_MAP_INTEGRATION.md).

## 31 October 2026 — display source-qualified averaging interval and QA in live Bennett's Point Activity

Run verified TypeScript, offline tests, production build, and Cloudflare Pages deployment for the bounded Activity presentation of two additional archival-report DataStreams. The server already completed the exact-field read-back verification in [workflow run 41248245591](https://github.com/OS4CSAPI/glaux-client/actions/runs/41248245591). Preserve older scalar streams and the historical Profile demo; retain the server's native interval/parameters limitation in [the research-design record](../Design/BENNETT_OBSERVATION_CONTEXT_BRIDGE.md).
