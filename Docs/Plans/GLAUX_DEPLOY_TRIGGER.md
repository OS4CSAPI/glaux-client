# Controlled Glaux Client Pages deployment trigger

**Purpose:** Explicitly trigger the `Glaux Client - verified Pages deployment` GitHub Actions workflow on branch `work/details-view-20261023`. This is application deployment administration only, not a DIM/Profile model decision.

**Request logged:** 2026-10-28, to build and validate the new source-grounded Smart Citizen Kit Resource Details page alongside the original template and Activity page.

**Project:** Existing Cloudflare Pages Direct Upload project `glaux-client`.

**Safety controls:** The workflow builds and tests the exact GitHub branch revision, uses its pinned CSAPI library submodule, and deploys only when the repository Actions secret `CLOUDFLARE_API_TOKEN` is supplied. The workflow deliberately does not store or print any credential. If the secret is unavailable, the build remains useful but **the site is not deployed**.

**Research source:** The Smart Citizen case study is maintained separately under `Docs/Research/DIM_Profile_V2/Case_Studies/Real_Equipment_DIM_Validation/` on `research/dim-profile-v2`. The wireframe is source-grounded, not a verified physical-Kit data feed.

**Initial trigger:** 2026-10-28 — validate the build and detect whether the credential is in place.
