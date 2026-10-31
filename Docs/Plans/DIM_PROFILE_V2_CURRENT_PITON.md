# DIM / CSAPI Profile V2 — current continuity pointer

**31 October 2026 · Application branch only.** This short pointer exists because the live Glaux code and the full V2 research documents are **not on the same Git branch**.

**[READ CANONICAL PITON v1.9 — 31 OCTOBER 2026](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/PITON_DIM_Profile_V2_Continuity_v1.9_31OCT2026.md)**

The full PITON lives on branch `research/dim-profile-v2` in `Docs/Research/DIM_Profile_V2/`. It supersedes v1.8 for current state and explains the original 182-artifact donor corpus, the owner-requested research-drift correction, the candidate DIM/Profile, the real Bennett's Point data, the 52°North server round trips, source-quality/time preservation, actual Glaux pages, exact GitHub Actions, all unresolved semantic limitations, and safe restart instructions. **Do not merge this application branch with the research branch blindly.**

## Live application context

- **Code branch:** `work/details-view-20261023`; initial handoff snapshot HEAD `bb44bcc64551034aa21e7bf63a9a7e28993e184c` (before this pointer was added).
- **Live Bennett's Point page:** https://glaux-client.pages.dev/?page=resource-details-live-bennett — real HTTP GET of two historical probe Systems and associated scalar/context-report Observations; not current physical telemetry or a general machine-readable Profile client.
- **Historical prepared Bennett's Point page:** https://glaux-client.pages.dev/?page=resource-details-profile-test&case=bennetts-point — source-grounded, prepared client-side case; not a live CSAPI fetch for these records.
- **Codex Map page:** https://glaux-client.pages.dev/?page=resource-details-live-map — shared Leaflet map, reused by the dedicated Bennett page.
- **Server and client evidence:** [archival-report bridge](../Design/BENNETT_OBSERVATION_CONTEXT_BRIDGE.md), [map integration](../Design/BENNETT_LIVE_MAP_INTEGRATION.md), [original source setup loader](../../scripts/load-bennett-v2-csapi.py) and [additional preservation loader](../../scripts/load-bennett-archival-report-csapi.py).
- **Last verified successful app deployment:** [GitHub Actions run 41248473107](https://github.com/OS4CSAPI/glaux-client/actions/runs/41248473107), source `54b4e576472d89d4dbb3e67fdce0733c8bb84926`. Subsequent documentation commits **are not live deployments**.
- **Last verified successful source/context round trip:** [GitHub Actions run 41248245591](https://github.com/OS4CSAPI/glaux-client/actions/runs/41248245591).

## Current control

The owner said **“idk man, this stinks”** after the 31-October standards-encoding discussion, then requested a robust PITON. The previously suggested SWE JSON test is **not an authorized next task**, even though the decision document lists it. Recover first and explain in ordinary language. **No production deploy, server change, automatic standards experiment, donor priority or Profile adoption is authorized by this pointer.**

The earlier [MERLIN/MPSS continuity document](CONTINUITY.md) retains its 24-October historical context and is **not the controlling V2 restart source**.
