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
