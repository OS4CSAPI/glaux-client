# Step 39 — Read-only Connected Systems API end-to-end validation

**3 November 2026 · STEP 39 COMPLETE as bounded, actually executed read-only validation · STEP 40 NEXT.** Gate E remains NOT CLOSED; Gate F remains NOT CLOSED as a complete cross-vendor Profile chain.

**Exact app source revision tested:** branch **work/details-view-20261023**, commit **60a22d66e3481f6d0832330bfc0ae2c2788ba211**. **Authoritative evidence:** [GitHub Actions validation run 41609815744](https://github.com/OS4CSAPI/glaux-client/actions/runs/41609815744), [native GET evidence artifact](https://github.com/OS4CSAPI/glaux-client/actions/runs/41609815744/artifacts/13218132241) and [live browser evidence artifact](https://github.com/OS4CSAPI/glaux-client/actions/runs/41609815744/artifacts/13218028418). Original source context remains [Bennett's Point NOAA/operator frozen selection](../Candidate_Specification/examples/bennetts-point-ee181.json) and [Step 38 workbook §42](README.md#42-step-38--shared-packet-interpretation-in-the-existing-resource-details-ui-with-source-fidelity-and-browser-limits).

## 1. What this establishes, in plain language

**The current committed Glaux app really builds and passes its installed tests, and a Chromium browser running its local Vite page really retrieves and displays the previously published Bennett's Point historical CSAPI resources from the Oracle-hosted 52°North server.** This is stronger than the isolated JavaScript tests in Steps 33–38: the exact current repo was checked out with its pinned OGC client submodule on GitHub Actions, built with Node 24, and used to exercise a real browser with actual cross-origin HTTP responses. The read-only runner confirmed separate transport, client decoding and display behavior, while retaining the source-time/QA/identity limitations.

**It does NOT prove the larger DIM/Profile goal is complete.** The previously published Bennett page is a **specialized readback** of known experimental resource IDs; the Step 38 **generic source-packet Profile-aware UI consumes separate local project-authored JSON files**. Those two working paths have NOT been proven to join through one standard-grounded, discoverable server-side Profile carrier that an unknown compatible client could interpret without a case-specific map. HTTP 200, valid JSON, green tests or visible values do not establish source issuer authenticity, normative SWE Common structure or the meaning of the original historical resultTime.

The original service was inaccessible through the local ChatGPT web fetch path and this environment's container DNS. **That was a local-access BLOCK, not evidence of server outage.** A separate GitHub-hosted runner successfully reached the documented service, providing a reliable bounded test path.

## 2. Exact executions and evidence standing

| Test layer | Actual test | Observed result | Limitation |
| --- | --- | --- | --- |
| App checkout | [CI-only workflow](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/.github/workflows/dim-step39-readonly-validation.yml), exact commit **60a22d66...** | **SUCCESS**. Pinned OGC client submodule; Node **24.22.1**, npm **11.19.1** | Not a production deployment |
| TypeScript/build | **npm ci; npm run typecheck; npm run build** | **PASS**. Vite **8.3.5**, **72 application modules transformed** | A static build does not certify a CSAPI Profile |
| Real offline tests | **npm test**, actual Vitest | **16/16 test files, 198/198 tests PASS** | Includes expected detections of source-FALSE but structurally accepted packets; not 198 source-valid facts |
| Source-packet browser | **npm run test:browser:source-packet**, local Chromium | **14/14 PASS**, no uncaught page errors; four local packet selections/Resource Details behaviors checked | No native server-based Profile discovery; local source packets only |
| Native Node HTTP | [GET-only probe script](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/scripts/verify-step39-csapi-readonly.mjs), at **2026-11-03T09:17:32.080Z** | **14/14 HTTP 200 with parseable JSON**, zero transport blocks, byte counts/media types/SHA-256 captured | Native standards and source authenticity NOT certified |
| Actual native CSAPI in browser | [Live browser script](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/scripts/verify-step39-live-browser.cjs), at **2026-11-03T09:19:25.238Z** | **10/10 browser assertions PASS; 10/10 native GET responses HTTP 200; no page errors** | Specialized Bennett page, NOT generic server-delivered Profile interpretation |
| Production Pages | Cloudflare Pages connected project read-only metadata queried **3 November 2026** | Latest production deployment still dated **31 October 2026 22:31:16 UTC**, successful, source commit **54b4e576472d89d4dbb3e67fdce0733c8bb84926** | Neither new Step 38 nor Step 39 source is claimed deployed |

**No mutations:** the CI workflow has **contents: read** permissions and no deployment step, no Cloudflare secret usage, and no server write. The native probe made only **GETs**, with no cookies/credentials, no cross-origin redirects, bounded timeouts, and one explicitly configured server base. The browser also made only **GETs** to the native service, no Commands, POST/PATCH/PUT/DELETE or physical actions. No new NOAA records, CSAPI resources or deployments were created.

## 3. Native read-only server findings, including the exact format ceilings

Tested server base: **https://129-80-248-53.sslip.io/csapi-pygeoapi/**. These results come from the machine-readable read-only artifact, not a guess or prior screenshot.

| GET request group | Actual HTTP response and content type | What could be checked |
| --- | --- | --- |
| Root | **200, application/json** | Object with **7 links** |
| Conformance | **200, application/json** | **Only one advertised URI**: http://www.opengis.net/spec/ogcapi-common-1/1.0/conf/core |
| Systems collection with a 2-resource limit | **200, application/sml+json** even when **application/json** was requested | FeatureCollection with **2 members** |
| Two Bennett probe Systems | **2 × 200, application/sml+json** | JSON **PhysicalSystem** descriptions |
| Four scalar/archival-report DataStreams | **4 × 200, application/json** | JSON DataStream objects |
| Four corresponding Observation collections | **4 × 200, application/json** | Four FeatureCollections, **one API record in each** |
| One archived-report Observation collection requested with SWE media | **200, application/swe+json** | JSON object, one returned member; **normative SWE structure NOT tested** |

**Current conformance advertisement (G30-01/G30-07):** the checked /conformance response advertised **OGC API – Common Part 1 core only**. No Connected Systems Part 1/2 conformance URI was present in that response's advertised list. This is a verifiable absence in the **tested declaration**, **not** proof that every available Connected Systems endpoint is incorrectly implemented.

**Format/negotiation standing:** the tested Systems response returned **application/sml+json** even for the recorded application/json request. The SWE-request response itself did **return application/swe+json**, but a matching media header and JSON parse cannot validate its SWE Common model, observation record layout, period-valued phenomenonTime, resultQuality or source-provenance carrier. Do not repeat an earlier unqualified “SWE broken” statement as a fresh finding, or call this SWE conformance PASS.

**Historic event identity standing:** each of the four existing scalar/report Observation collections returned **one** item, consistent with the four older experimental API resources. The prior independent NOAA source selection supports **two** original April 2024 mean temperature reports; two scalar and two report records are **parallel representations, not four source measurements**. The returned API resources did **not establish an independently discoverable standards-native same-original-event link or an original source-authenticated provenance contract**.

## 4. Native Chromium cross-origin readback

The **existing** local Glaux route **/?page=resource-details-live-bennett** was opened in Chromium against a locally running Vite server. Unlike the separate local source-packet tests, this route made **10 actual cross-origin GETs**: two Bennett physical probe Systems, four scalar/archival-report DataStreams, and four Observation collections. **All ten returned HTTP 200**, with application/sml+json Systems, application/json Streams/Observations, and **Access-Control-Allow-Origin: * in every tested native response**. Browser CORS access succeeded from the local test origin; this does not establish every possible browser origin.

The **10/10 browser assertions** verified the controlled live Bennett case rendered, two physical probes were retrieved, scalar/report resource counts appeared, the two historical source temperatures **29.1 °C** and **27.3 °C** were displayed, the original **F_ATemp quality token "<0> "** (including trailing whitespace) survived, and the UI explicitly stated that independent historical result-generation time was unavailable. The existing shared Map correctly produced a **no-position fallback** with no invented per-EE181 location, and Management → Record retained the actual native server responses. There were **no uncaught page errors or non-GET native requests**.

**Important qualification:** these were the **previously published project experiment Systems/DataStreams/Observations**, including the report-style preservation bridge; the original NOAA 2024 annual CSV was **not re-downloaded or rehashed** in Step 39. The original 15-minute interval was source-derived in earlier work, while the live native fields still cannot be claimed to supply an independently known original resultTime. This is real, bounded **client/browser/server** evidence, not independent physical device measurement or final native CSAPI Profile semantics.

## 5. What is PASSED, HELD or EXCLUDED

| Original whole-System objective | Step 39 standing | Source/reason |
| --- | --- | --- |
| Four different source packets through one shared parser | **PASS, LOCAL research input layer only** | Full offline suite plus real local browser; packet claims are still self-declared and can be source-false |
| Current Glaux TypeScript, Vitest, Vite and Resource Details browser behavior | **PASS at exact tested revision** | Actual Node 24, **198/198** Vitest and **14/14** local browser |
| Read-only native CSAPI HTTP, JSON and browser CORS | **PASS for checked requests/origin** | **14 Node GETs and 10 browser GETs**, all 200; CORS * on 10 browser responses |
| Specialized historic Bennett server readback and visible QA | **PASS with source/time qualifications** | **10/10 live-browser checks**, including source mean values, original flag and truthful Map |
| Independently advertised CSAPI requirements classes | **HOLD / NOT ESTABLISHED** | /conformance only advertised Common core in current checked response |
| Correct native SWE/OMS average period, original resultTime and resultQuality | **HOLD / NOT ESTABLISHED** | SWE header observed, but normative body/time/quality validation not performed |
| Exact source day-only Deployment, per-probe map position and completed-mean producer | **HOLD** | Original metadata does not supply exact swap instant/probe coordinates; station vs logger producer unresolved |
| Independent original-source authenticity and a portable discoverable Profile (G30-01) | **BLOCKING — Gate E NOT CLOSED** | Local Step 32 packets are NOT served as an approved standard association to the native Systems |
| Complete generic Profile-aware end-to-end client (Gate F) | **NOT CLOSED** | Specialized native Bennett page and generic local packet UI are **two separate paths**, not one common discovered server-carried interpretation |
| Actual authorized Commands, execution and physical effects | **EXCLUDED** | No control endpoint, permission, write, acknowledgement or real hardware action performed |

**Step 39 is COMPLETE** because the planned bounded validation was actually run, preserved with versions and honest negative findings. This **does not** close Gate E, approve native Observation class/format compliance, or retroactively establish complete Profile portability. The remaining original donor/profile source gaps and all Step 34–37 source-FALSE cases stay visible.

## 6. Reproduction and next step

The durable execution entry point is [read-only workflow](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/.github/workflows/dim-step39-readonly-validation.yml), which runs the exact [native GET script](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/scripts/verify-step39-csapi-readonly.mjs) alongside installed TypeScript, Vitest, local source-packet browser and [read-only live browser](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/scripts/verify-step39-live-browser.cjs). [GitHub run 41609815744](https://github.com/OS4CSAPI/glaux-client/actions/runs/41609815744) is the verification baseline. The project experiment tests and source packets remain separate from live service resource discovery.

**NEXT ON ONE FUTURE OWNER “PROCEED”: STEP 40 ONLY.** Complete the **four-case original source → DIM → candidate Profile/CSAPI → Glaux source-fidelity scorecard**, separating independently original, preserved, derived, qualified, source-to-packet omitted, client/transport lost, unsupported and untested data. Do **not** perform Step 41 repairs, Step 42 publication, Step 43 release, new Oracle/52°North writes, device Commands or Cloudflare deployment in the same iteration.
