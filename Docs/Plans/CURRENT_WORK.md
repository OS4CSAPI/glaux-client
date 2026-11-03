# Current client work

## DIM / CSAPI Profile V2 — Step 41R-03 Dragino/AirGradient reference source-coverage increment (3 November 2026)

**BOUNDED LOCAL RESEARCH-PACKET INTERPRETATION / NONDEPLOYED APP CODE — no native Profile claim, Oracle mutation or Cloudflare deployment.** The [full original-source→expanded packet→same Glaux Reader/Resource Details crosswalk](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Whole_System_Recovery/Step41R03_Dragino_AirGradient_Whole_System_Coverage_and_Client_Evidence_03NOV2026.md) records 14 additional Dragino design/example/UNKNOWN claims (**7→21** assertions) and 15 additional AirGradient design claims (**7→22** assertions, **3→9** reference subjects, including six additional source-known reference modules). Both preserve **zero performed original events**, no installed unit or active firmware, and all original Step 32 historical packet/test baselines. The current [research plan](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md) marks **41R-03 COMPLETE, 41R-04 NEXT** only after final research-branch readback.

**Code scope:** existing `src/profile/source-packet.ts` gained generic message/configuration/power/communications/software concept recognition, with **format-gated** project input version `dim-csapi-source-packet.s41r03.v0.1` separate from historical `dim-csapi-source-packet.s32.v0.1`. Existing `src/profile/source-packet-presentation.ts` routes those concepts under common tabs, without manufacturer-name conditions. Existing `src/presentation/resource-details-profile-test.ts` selects two new **local** coverage JSON files from `public/fixtures/source-packets/`, and `src/experiments.ts` records the same page's update, not a new page. [17 new read-only source/example/version/adversarial regression tests](../../tests/source-packet.coverage-41r03.test.ts) are on this branch. Original four local source packet fixtures remain unchanged.

**Actually executed:** deterministic V8 execution of the checked-in TypeScript reader/projection/test logic, with only TS type syntax removed, **17/17 targeted test outcomes PASS**, plus previously frozen 41R-02 source oracle **4/4 selected original packets, 23/23 historic deliberate source-false mutations and 4/4 issuer controls** unchanged. New source JSON research/app copies and local allowed-concept/reference checks were read back. **NOT freshly verified as passed:** Node 24 npm/Vitest suite, TypeScript full-build, Chromium/browser interaction, actual native 52°North HTTP retrieval, OGC conformance, deployed Cloudflare revision or source issuer cryptographic authentication. The previous Step 39 read-only GitHub Actions run remains historically valid at its older exact commit; no claim of a new CI result merely because the workflow has push triggers.

**Outstanding:** known original manufacturer information remains outside the selected packets, including Dragino many commands/history fields and AirGradient additional full example/cloud fields, power-mode source editions and operating state. F40-06 coverage improved but is not source-complete. G30-01/Gate E and full Gate F remain OPEN; the selected project packet format remains local, not a standards-native served `profile`/`describedby` carrier. Real control and new deployed operation remain excluded.

**NEXT on owner's separate “proceed”: STEP 41R-04 ONLY** for Campbell + Bennett source-coverage expansion at their source-true reference/historical standing. No native producer 41R-05, native generic Glaux 41R-06, original Steps 42–43 or live service/deployment work during this iteration.


## DIM / CSAPI Profile V2 — Step 40 fidelity assessment (3 November 2026)

**SOURCE-RESEARCH/DOCUMENTATION ONLY — NO APP CODE OR LIVE SERVICE CHANGE.** The [authoritative four-case original-source→DIM→candidate Profile/native CSAPI→Glaux scorecard](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Whole_System_Recovery/Step40_Four_Case_Source_to_Client_Fidelity_Scorecard_03NOV2026.md) and [workbook §44](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Whole_System_Recovery/README.md#44-step-40--original-source-to-dimprofileglaux-fidelity-scorecard-four-cases) are committed on **research/dim-profile-v2**. The [43-step plan](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md) now records **40/43 complete; Step 41 next**. This app-branch documentation index is the only app-side action of Step 40; the original source packet reader, tests, presentation, source fixtures and native live service code are **unchanged**.

**Finding:** all four source situations are interpretable at their *selected* reference/historical standing through the shared local project-packet UI. The selected packets have **13 described referents, 45 assertions, two original NOAA source events and four old API copies**. Three manufacturer cases are design/reference evidence **without actual fielded observations**, whereas Bennett has independently source-identified historical equipment. The scorecard separates preserved source facts, SOURCE_EXAMPLE, DERIVED/UNKNOWN, omitted original-source coverage and unproven native CSAPI semantics. **Twenty-three intentionally source-FALSE packet mutations** still pass structural parsing but are caught by source-specific test oracles; these do **not** invalidate the unchanged original source records.

**Runtime evidence stays as actually established:** [Step 39 successful GitHub Actions run 41609815744](https://github.com/OS4CSAPI/glaux-client/actions/runs/41609815744) tested executable app revision **60a22d66e3481f6d0832330bfc0ae2c2788ba211** with **198/198 Vitest, Node24 TypeScript/build, 14/14 local source-packet Chromium, 14 native CSAPI GETs HTTP 200, 10/10 specialized Bennett live Chromium and ten cross-origin native GETs HTTP 200**. The **generic packet UI still reads local project JSON**; the live native Bennett page is **case-specific**, not one portable published Profile carrier. No Step 40 app change or deployed Cloudflare production update follows from those tests; Gate E **G30-01** remains **BLOCKING**, and Gate F remains open as a complete cross-vendor claim.

**NEXT owner's “proceed”: STEP 41 ONLY** — review the source-linked [F40-01–08 blocker questions](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Whole_System_Recovery/Step40_Four_Case_Source_to_Client_Fidelity_Scorecard_03NOV2026.md#8-candidate-step-41-blocker-handoff--no-repairs-performed-here) and decide which small *future* repairs or evidence-qualified exclusions can support a candidate release. Do not implement them, execute Steps 42–43, write server resources, issue device Commands or deploy Cloudflare as part of this scorecard step.


## DIM / CSAPI Profile V2 — Step 39 READ-ONLY end-to-end validation (3 November 2026)

**STEP 39 COMPLETE as bounded executed validation; STEP 40 NEXT.** The code under test was the application branch **work/details-view-20261023** at Git revision **60a22d66e3481f6d0832330bfc0ae2c2788ba211**, verified in [GitHub Actions run 41609815744](https://github.com/OS4CSAPI/glaux-client/actions/runs/41609815744). A new [CI-only workflow](../../.github/workflows/dim-step39-readonly-validation.yml) ran **npm ci**, **Node 24.22.1/npm 11.19.1**, **full TypeScript** (PASS), **full Vitest suite** (**198/198 passing tests, 16 files**), **Vite 8.3.5 production build** (PASS, 72 application modules), and a real local Chromium [14-check source-packet browser test](../../scripts/verify-source-packet-browser.cjs) (**14/14 PASS, no page errors**). This is now actual repository/runtime/browser evidence rather than the earlier transient V8-only checks; no Cloudflare deployment occurred.

**Native CSAPI transport actually tested:** the separate [GET-only endpoint script](../../scripts/verify-step39-csapi-readonly.mjs) retrieved **14/14 HTTP 200 JSON responses** from the documented Oracle-hosted 52°North URL, including root, conformance, Systems, both historical probe Systems, four scalar/archival-report DataStreams, their Observation collections and one SWE-media response. The [native evidence artifact](https://github.com/OS4CSAPI/glaux-client/actions/runs/41609815744/artifacts/13218132241) records exact request paths, Content-Type, payload byte counts, SHA-256 and selected shape summaries. **Current /conformance advertised only OGC API – Common Part 1 core**, not Connected Systems requirements classes; application/json requests to System resources returned application/sml+json, while the separately requested application/swe+json response reported that media type without normative SWE body verification. These are bounded format/advertisement facts, NOT an established CSAPI/SWE conformance certificate.

**Native browser→server→Resource Details actually tested:** the [live read-only browser script](../../scripts/verify-step39-live-browser.cjs) opened the **existing** local Vite-rendered Bennett live CSAPI page and made **10 actual GETs to the remote native service**, **10/10 HTTP 200**, with **Access-Control-Allow-Origin: * for all ten**. Its [browser evidence artifact](https://github.com/OS4CSAPI/glaux-client/actions/runs/41609815744/artifacts/13218028418) documents **10/10 passing checks, zero page errors**, two historical source probes, native scalar/report counts, actual display of **29.1 °C/27.3 °C**, exact historical original **F_ATemp="<0> "** token, truthful UNKNOWN original result availability, safe Map fallback and raw server response inspection. **The native live route is an older specialized Bennett implementation** and is distinct from the Step 38 new generic **local research source-packet** UI; therefore a single discoverable cross-vendor Profile producer→unknown client chain has NOT been proved.

**Gate status:** **Gate E NOT CLOSED (G30-01 BLOCKING)** because self-declared project packets still lack a source-authenticated and standards-grounded **native CSAPI discovery/evidence carrier**, and the present checked /conformance response does not advertise CSAPI requirements classes. Gate F remains NOT CLOSED as a complete shared source-to-native-to-UI result, although bounded real transport/browser validation has succeeded. Bennett's completed-average producer, day-only Deployment, original independent resultTime, native TimeRange/resultQuality, SWE body structure and authenticated Command gaps are retained. The original NOAA annual CSV was **not newly downloaded/rehashed**; we used the previously frozen source extract. **No Oracle data was created/modified, no actual device action was issued, and no Cloudflare Pages deployment was made.**

**Cloudflare independent read:** the connected Pages project **glaux-client** still reported its latest successful production deployment as **31 October 2026 22:31:16 UTC**, source commit **54b4e576472d89d4dbb3e67fdce0733c8bb84926**. That is **older than this tested application revision**, so do NOT claim Step 38/39 integration is deployed. The full evidence-level comparison and conclusions are preserved in [Step 39 research report](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Whole_System_Recovery/Step39_ReadOnly_E2E_Validation_03NOV2026.md).

**NEXT on the owner's next “proceed”: STEP 40 ONLY** — original-source→DIM→candidate Profile/CSAPI→Glaux **four-case fidelity scorecard**, recording preserved, derived, missing, source-false and untested details. No Step 41 model repairs, Step 42 publication, Step 43 release work, deployment or server mutation without separate later iteration.


## DIM / CSAPI Profile V2 — Step 38 common Resource Details integration (3 November 2026)

**Actual app change, NOT a deployment:** the existing [Resource Details profile-test page](../../src/presentation/resource-details-profile-test.ts) now supports four **local read-only** project evidence packets with deep links `/?page=resource-details-profile-test&case=step38-dragino`, `step38-airgradient`, `step38-campbell`, and `step38-bennett`. It calls the **unchanged, verified Step 33 [source reader](../../src/profile/source-packet.ts)** (Git blob `346d682cbff6a2e97770feba088452df6a067c4e`) through one new [typed projection](../../src/profile/source-packet-presentation.ts) and one common [Resource Details evidence renderer](../../src/presentation/source-packet-details.ts). Source-case selection only chooses local input paths; no manufacturer/case-ID branches were added to the interpretation rules. The existing 560 × 440 frame, tabs, Smart Citizen/published/legacy synthetic examples, generic/raw flow, live/native CSAPI pages and `src/data` boundary are not replaced.

**Original data:** four files in [`public/fixtures/source-packets/`](../../public/fixtures/source-packets/) are exact byte-for-byte copies of the research Step 32 inputs (Dragino Git blob `5d7931846ff88b0752dab81402a4df1703fa8077`, AirGradient `f3684d6e1e8285f9f766420a379cef8c0dc60201`, Campbell `3671babc4d415d480022d9372851eeb5f1c82ae3`, Bennett `83bd92f22b19a1f6a1f9a4c1e3444e64e546bf60`). These are **project-authored evidence packets, not native CSAPI responses, authenticated live resources or a standards-published Profile format**. A visible warning identifies that distinction even when a packet passes the local structural parser. Management → Record/Sources retain all raw original JSON, native lexical values, full issuer/edition/locator, G30 blockers, and unrecognized future fields.

**Common presentation:** Overview summarizes referent standing and event/copy count; Equipment preserves source-described physical/functional distinctions; Communications retains source-native field/property semantics; Condition leaves unknown effective state separate from rated design; Activity/Table preserves **two Bennett source originals versus four historical experimental copies**, QA `F_ATemp="<0> "`, DERIVED intervals/probe attribution and UNKNOWN result availability. Commands remain unavailable without authorization. Operational → Map calls the existing **Codex shared Map renderer** with **null geometry** and preserves its no-position fallback; site coordinates are never promoted to an individual EE181's position. The full [design/limits](../Design/RESOURCE_DETAILS_PROFILE_TEST.md#step-38--same-shared-evidence-interpretation-in-the-existing-resource-details-tabs-3-november-2026) documents where local packet meanings end and native OGC/CSAPI carriage would begin.

**Observed checks only:** [12 typed presentation tests](../../tests/source-packet.presentation.test.ts) passed **12/12** in a transient V8 compatibility harness and [9 Resource Details component tests](../../tests/source-packet.details.test.ts) passed **9/9** with a minimal fake DOM/stubbed Map call. The test-oracle checks include source example versus original event, original mean counts, exact raw source QA, rejected/invalid packet raw retention, source-false accepted packet warning, no unsupported map marker and no executable Commands. The [read-only browser smoke script](../../scripts/verify-source-packet-browser.cjs) (registered as `npm run test:browser:source-packet`) was created **but NOT executed**. Full repository Vitest, `npm ci`, app-wide TypeScript checking, production `vite build`, browser run, live/native CSAPI protocol conformance, and deployment **were NOT run in this restricted environment**.

**Fidelity and gate:** source-false but internally consistent claims remain an **unsolved producer/source-authentication obligation**—the new UI warns rather than adding vendor-specific patches or claiming a source-authentic Profile. **Gate E still NOT CLOSED (G30-01); Gate F is NOT yet demonstrated**, and historical Bennett producer, exact Deployment, original `resultTime`, standard interval/quality and 52°North SWE evidence limits remain. No upstream library, live server, actual physical device, Command, Cloudflare deployment trigger or Pages asset was modified. The controlling research workbook and 43-step plan govern the next step.

**NEXT on the owner's following “proceed”: STEP 39 ONLY**, a bounded end-to-end CSAPI validation with explicit source/transport/conformance limits. Do not automatically execute Step 40 source-to-display scorecard, release planning, Oracle/52°North write, authenticated control or Cloudflare deploy.


## DIM / CSAPI Profile V2 — Step 37 Bennett's Point historical source challenge (3 November 2026)

**Scope:** the first genuine historical station/instrument/measurement test of the **unchanged Step 33 shared interpreter**, not a deployed Resource Details UI or approved OGC Profile. Both research files were copied exactly into app tests: [Bennett source packet](../../tests/fixtures/source-packets/bennetts-point.historical.packet.json), Git blob `83bd92f22b19a1f6a1f9a4c1e3444e64e546bf60`, and [original NOAA/operator source selection](../../tests/fixtures/source-packets/bennetts-point.source-selection.json), blob `38d226842d1b88bda9940748ebb1763a34fa2376`. The original [2024 operator metadata PDF](https://cdmo.baruch.sc.edu/waf/YearlyFiles/ACE%20Basin/meteorological/metadata/acemet01-12.24m.pdf) was also independently read/visually inspected at printed pp. 2, 6 and 11 for the fixed-EST/average method, two EE181 serial/service histories, CR1000X logger 13916 and TX321 GOES transmitter 2335. **The preserved two NOAA archival CSV rows, original raw flag tokens and snapshot SHA are from the earlier frozen selection; the full annual CSV was not downloaded or rehashed in this step.**

**What survives through one source-independent reader:** an actual continuing station `acebpmet`, two source-identified EE181 physical individuals across **three calendar-day service periods** (one returning), separate logger/transmitter identities, **two original** 2024 NOAA temperature means 29.1 °C / 27.3 °C with original 12:00 fixed-EST station stamps and `F_ATemp="<0> "` including its trailing space and separately empty `F_Record`, nominal 15-minute UTC intervals and likely physical contributor-probe relations explicitly labeled **DERIVED**, original `resultTime` and single station-versus-logger producing System **UNKNOWN**, and **four old experimental CSAPI Observation representations of only two original station reports**. Station site position is **not** surveyed EE181 unit geometry, and 16 April station maintenance times are **not** a precise EE181 exchange instant.

**Actual tests:** [30-case Bennett suite](../../tests/source-packet.bennetts-point.test.ts) executed **30/30 expected outcomes** in the same transient **V8 JavaScript compatibility harness** used in Steps 34–36, by stripping TypeScript-only syntax from the exact committed reader/test files. This was **not Vitest**, a project-wide TypeScript check, full npm build, browser/Resource Details rendering, live CSAPI/SWE conformance or Oracle/Cloudflare update. Positive preservation includes actual source identities/two events/four copies, lexical fidelity, source versus derived time, UNKNOWN result availability and independent source/edition references. **Six malformed inputs were REJECTED**; **eleven coherent but SOURCE-FALSE packets were structurally ACCEPTED** and rejected by the separate original-source oracle, including fabricated third probe, exact swap/removal, fake original availability, misattributed producer/probe, corrupted QA/period, extra original event and wrong historical copy linkage. Those eleven are **FAILs of source authenticity at the local reader layer**, not eleven successful Profile interpretations. The source-specific QA and historic IDs remain in tests, never as a case-dependent branch in the shared reader.

**Source→packet coverage and current gate:** the packet is a *small selected historical excerpt*, not a full original weather-station DIM. It omits additional operator-confirmed station geometry, service/OS events, program, other meteorological instruments and more source detail. Unlike the original PDF, the frozen selection does not itself record the transmitter serial; direct PDF verification supports the declared TX321 2335 but the selection ledger should be enriched only with traceable source grounds in an appropriate repair step. The outstanding Profile **G30-01 portable issuer/standing/DERIVED/UNKNOWN/original-event carrier and independent discoverability remains BLOCKING**, alongside Bennett historical `resultTime`, period/quality mapping, actual completed-mean producer, date-only Deployment and 52°North SWE schema issues. The **generic interpreter remained byte-identical** to blob `346d682cbff6a2e97770feba088452df6a067c4e`; no existing app UI/route, upstream client, server resources, actual Commands or Cloudflare deployment changed.

**Next owner “proceed”: STEP 38 ONLY** per [current research plan](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md): integrate common source-qualified interpretation into the **existing Resource Details working views**, retain original source/Standard/Raw evidence, and reuse the existing shared Codex Map renderer. Do not confuse a local project packet with native CSAPI Profile wire discovery, begin live server writes or deploy by implication. [Complete Step 37 workbook §41](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Whole_System_Recovery/README.md#41-step-37--bennetts-point-historical-source-packet-challenge-and-fidelity-limits) retains source and negative findings.


## DIM / CSAPI Profile V2 — Step 36 Campbell/ClimaVue source challenge (3 November 2026)

**One source-case step only.** The established [Step 33 shared reader](../../src/profile/source-packet.ts), Git blob `346d682cbff6a2e97770feba088452df6a067c4e`, is **unchanged**. The original [Campbell/first-gen ClimaVue research packet](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Candidate_Specification/examples/step32-source-packets/campbell.reference.packet.json) was copied byte-for-byte into [this app fixture](../../tests/fixtures/source-packets/campbell.reference.packet.json), both verified as Git blob **`3671babc4d415d480022d9372851eeb5f1c82ae3`**. [Test code](../../tests/source-packet.campbell.test.ts) is a **separate source-specific oracle**, not a new vendor interpretation branch; source authority is the [original Campbell source sheet D](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md) and its references D02/D07.

**Positive result:** one documented potential assembly of **two separately manufactured reference kinds**, CR1000X logger and first-generation ClimaVue 50; a documentary **SDI-12 design connection**, not verified installed wiring or a running command. One `aR7!` response from the ClimaVue has **14 numbered output positions** (the packet retains the count and position 8 air-temperature definition, not actual weather values or 14 physical sensors). The separate CR1000X Status publisher example has **`PanelTemp=25.91098 °C`**, temperature of the **logger panel**, not an actual ambient-air result or a ClimaVue measurement. The joined installed station, active address, running program, firmware and historical events remain UNKNOWN/unverified. Two reported values in °C are **not automatically the same observed property or observed object**.

**18/18 committed tests' expected outcomes were observed in a temporary V8 compatibility runner** executing the exact reader/test logic with TypeScript-only annotations removed; this **was NOT** a run of the repository Vitest suite, full TypeScript/npm build, browser, live CSAPI service or original OGC conformance tests. Five malformed inputs (missing target, unknown source, UNKNOWN with a made-up value, fake event from a reference kind, duplicate claim identifier) were **rejected** by the unchanged reader. **Five structurally coherent but SOURCE-FALSE claims were accepted** and identified by separate test-only original-source checks: a model presented as an actual individual, logger `PanelTemp` reassigned to ClimaVue, a publisher example promoted into SOURCE_FACT, 14 output positions turned into 14 physical sensors, and a reference SDI-12 design connection promoted to a historical role-service fact. These are **known negative fidelity results**, not five successful interpretations.

**Coverage gap:** the original D02 manual defines **all 14 aR7! positions**, but the selected packet covers only one field plus the count; the D07 example has **31 Status fields**, but the packet selects just **PanelTemp**. No source-backed original numerical ClimaVue weather values or actual joined station exist, and prior D03/D04 program/edition sources are not one verified active installation. Do not fabricate missing output fields, an observed climate series, configured bus address, calibrated condition or a Command.

**Gate and handoff:** Gate E **remains NOT CLOSED** (portable producer/source authority and discoverability G30-01), and full Gate F requires more than source-consistent packet interpretation. The unchanged reader now has **three** manufacturer-reference case studies with honest source failures; actual historical Bennett station challenge is **Step 37 only** on the next owner “proceed.” No existing Glaux UI, `src/data`, upstream client, 52°North/Oracle server resource, Cloudflare deployment or physical hardware was altered. The complete source→DIM→packet→reader report and *informative-only* Resource Details preview are in [research workbook §40](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Whole_System_Recovery/README.md#40-step-36--campbell-logger-climavue-50-source-packet-challenge-and-fidelity-limits).


## DIM / CSAPI Profile V2 — Step 35 AirGradient original-source challenge (3 November 2026)

**Scope:** one manufacturer-reference-only case run against **the existing Step 33 interpreter**, with **no production Resource Details modification, source-to-CSAPI conversion, server data load, or deployment**. Primary evidence is the pinned [A01 hardware README](https://github.com/Open-Air-Foundation/pcb-openair-max-main/blob/89aacf5013fc0ffe4b988a2e3c5a227bce3c4983/README.md), [A02 firmware README](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/README.md) and [research sheet A](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md). The app's [test fixture](../../tests/fixtures/source-packets/airgradient.reference.packet.json) was read back byte-identical to the [Step 32 research packet](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Candidate_Specification/examples/step32-source-packets/airgradient.reference.packet.json), Git blob **`f3684d6e1e8285f9f766420a379cef8c0dc60201`**. Shared reader [`src/profile/source-packet.ts`](../../src/profile/source-packet.ts), blob **`346d682cbff6a2e97770feba088452df6a067c4e`**, remains unchanged.

**Source-positive result:** Manufacturer reference O-M-1PPSTON-CE includes **two physical PMS5003 design modules at sockets PM1 and PM2**, while `pm01`, `pm25`, `pm10` are **PM1.0/PM2.5/PM10 particulate output fields**, not physical sockets or proof of source-specific direct hardware attribution. The packet's 27.7 µg/m³ `pm25` value is **SOURCE_EXAMPLE**, not a running observation; no identified installed unit, actual firmware pair, installed network/solar state or qualified gas reading was acquired. The packet has no original performed event or representation copies.

**Checks:** [`tests/source-packet.airgradient.test.ts`](../../tests/source-packet.airgradient.test.ts) defines **16 source-positive, malformed-input, source-false and selected coverage checks**. Its exact committed TypeScript logical test bodies passed **16/16 via a transient V8 compatibility runner** after TypeScript-only syntax removal; this is **NOT** a normal Vitest run, full-project typecheck, build, browser test or independent native OGC validation. Five malformed inputs were rejected as intended, while **four source-false packets were accepted by the structural reader** and detected by the **test-only original-source oracle**: a model-as-individual promotion, an output field reclassified as a physical socket, a published example promoted to SOURCE_FACT and an invented third PMS5003 module. **16/16 expectation checks are not a 16/16 source-fidelity PASS.**

**Coverage limits:** selected Step 32 input omits much of original A01/A02/A06/A07 evidence, including other physical sensing modules (CO₂, SHT4x, SGP41, gas), power/communications arrangements, supported settings and edition-dependent firmware context. No generic reader can recover omitted source material. Do not invent calibration or synchronized Wi-Fi/cellular/cloud results to fill gaps. The project must maintain a source-vs-packet-vs-reader fidelity ledger and qualified exclusions; it must not add brand-based code to make the test appear to pass.

**Next:** controlling [research plan Step 36](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md) is the bounded Campbell CR1000X + first-generation ClimaVue 50 case. Steps 37–43, UI, Oracle/52°North, Command operations and Cloudflare remain untouched. **Gate E NOT CLOSED; Gate F still provisional**.


## DIM / CSAPI Profile V2 — Step 34 Dragino evidence fidelity test (3 November 2026)

**Source input:** the actual [Dragino S31-LB Step 32 reference packet](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Candidate_Specification/examples/step32-source-packets/dragino.reference.packet.json), evidence from [original C system sheet](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md) (C-I01/02/04, C-F05/06, C-O03), with original manufacturer manual C02 and pinned decoder C03 source pointers. The app-side [fixture](../../tests/fixtures/source-packets/dragino.reference.packet.json) was read back as exactly the same Git blob **`5d7931846ff88b0752dab81402a4df1703fa8077`** as the research source. No new fielded-unit evidence, manufacturer manual edition or sensor data was acquired.

**Implementation:** the **existing Step 33 interpreter is unchanged** ([`src/profile/source-packet.ts`](../../src/profile/source-packet.ts), Git blob `346d682cbff6a2e97770feba088452df6a067c4e`). [`tests/source-packet.dragino.test.ts`](../../tests/source-packet.dragino.test.ts) performs 13 scoped tests against this true source-reference fixture and a *test-only* original-source oracle; no manufacturer-based branches were introduced in Glaux. This is a source-case exercise, **not** a production UI release or a completed original CSAPI encoder.

**Observed local checks:** the exact source reader/committed test logic passed **13/13** in a temporary V8 JavaScript compatibility runner that removed TypeScript type annotations and supplied test assertions. This was **not** a repository Vitest execution. Positives preserved manufacturer **REFERENCE_ARRANGEMENT + one REFERENCE_COMPONENT**, one external SHT31 yielding two environmental fields, manufacturer scalar **26.1 °C** as `SOURCE_EXAMPLE`, **8,500 mAh** nameplate rating as `SOURCE_FACT`, two explicit `UNKNOWN` claims (installed unit and effective setting), and zero original field Observations. Negative controls for broken references, invented UNKNOWN values and converting reference examples to source events were rejected.

**Three important non-passing source-fidelity controls:** the unchanged reader **still accepts structurally valid but source-false input** when (1) a model identifier is promoted to a physical identified unit, (2) a printed example is promoted to `SOURCE_FACT`, or (3) a second nonexistent SHT31 is attached. The source-specific test oracle rejected these three false source claims. An input accepted structurally is therefore **not** independently validated against original manufacturer data. Research [workbook §38](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Whole_System_Recovery/README.md#38-step-34--dragino-s31-lb-source-packet-challenge-and-fidelity-limits) records the exact pass/fail layers; do **not** count the source-false interpretations as successful cross-vendor fidelity or Gate E closure.

**Coverage gap found:** C-O03 source-documented **20-minute default uplink interval** is omitted from the current research input packet, although the effective installed interval remains correctly `UNKNOWN`. This is a **source→packet gap**, not a value the reader lost. It should be explicitly repaired or excluded after the bounded case testing; no universal new vocabulary was adopted to hide the omission.

**Scope and status:** no `src/data`, existing presentation routes, Cloudflare trigger, deployment, Oracle/52°North service, real commands or connected hardware were altered. The app did not run a full `npm ci`, `npm test`, `npm run build`, typecheck of all files, browser or official OGC schema test in this isolated environment. **Step 34 is complete as a bounded, source-falsifiable case exercise with documented fidelity failures; Gate E remains NOT CLOSED**. The controlling research plan is **34/43, Step 35 next**, and the existing packet interpreter remains unchanged for the next source case.


## DIM / CSAPI Profile V2 — Step 33 source-independent packet reader (3 November 2026)

**Scope: a pure, first interpreter increment only; not a deployed or fully Profile-aware Resource Details route.** Research authority: [controlling 43-step plan](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md) and [Step 32 contract](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Candidate_Specification/Step32_Source_Packet_Contract.md). This increment adds [`src/profile/source-packet.ts`](../../src/profile/source-packet.ts) with type-safe, read-only interpretation of the local `dim-csapi-source-packet.s32.v0.1` research input, plus [`tests/source-packet.test.ts`](../../tests/source-packet.test.ts) with **11 synthetic source-neutral positive and negative tests**. The real four case packets remain in the separate research branch for Steps 34–37.

**Observed local check:** the exact committed TypeScript module passed `tsc --noEmit --strict --target ES2022 --module ESNext --moduleResolution bundler` using available TypeScript **5.8.3**, and the exact committed test logic passed **11/11** isolated Node **22.16.0** built-in test runs using a temporary compatibility harness/transpilation. This is **not the full app's Vitest execution**: `npm ci`, `npm run typecheck` against all project files, `npm test`, `npm run build`, browsers, live CSAPI and GitHub Actions were **not run for this increment** because local project dependencies were unavailable and no production deployment was authorized. The GitHub blob content was read back and matched the locally tested files.

**Positive meaning preserved:** subject standing (reference versus actual *as declared*), source issuer/evidence locator and exact raw value including whitespace, printed example versus performed event, DERIVED method and cited assertion inputs, and explicit UNKNOWN without inventing zero or availability. The reader groups multiple project representation links under **one** original source event, and holds the input object/raw foreign concepts unchanged. **Rejected:** UNKNOWN carrying fabricated values, missing source references, an identified unit lacking source-scoped identity, a reference-only subject promoted to an actual event, invalid derivation inputs and a copy without its source-event anchor. Changing IDs and labels did not change the semantic interpretation.

**Limitations and gate:** this code implements no CSAPI Profile discovery/carrier, independent source authenticity assessment, original-standard JSON Schema conformance, final DataStream producer/Observation time or quality binding, historical Deployment, enabled commands or client rendering. **Gate E remains NOT CLOSED; G30-01 remains the chief portable evidence/unknown-client blocker.** No existing Glaux page, `src/data`, upstream client, Oracle/52°North resource, GitHub Pages deployment trigger or Cloudflare site was modified. The deployment workflow is explicit/manual or trigger-file-scoped, and neither was activated.

**Next owner “proceed”: STEP 34 ONLY** — exercise the same reader against the original documented Dragino S31-LB packet and a false-source mutation, with an honest reference-design result. Do not run subsequent manufacturer cases or deploy by implication.


## Live Resource Details map — 31 October 2026

The separate `resource-details-live-map` page reuses the live CSAPI Resource
Details view and adds a map for the selected System's reported point. It shows
historical satellite or street imagery, a resource marker, zoom and recentering,
the original position, and an explicit coordinate interpretation. Unsupported,
missing, or unresolved positions receive a readable fallback; the map does not
assert live tracking, position time, or accuracy. Related-resource failures do not
block an available System position. The prior live page and other routes remain.

Cloudflare Pages production deployment `bf7b7ea1-a6f1-4542-9424-dbdce0e54ed9`
publishes commit `db6961d270eb568e0a3a36f140570b23b296d0aa` at
<https://glaux-client.pages.dev/?page=resource-details-live-map>. Clean install,
83 offline tests, TypeScript and production build passed. The production map
passed 15 controlled browser checks, and Edge loaded real System data and both
basemaps; the local index and template checks passed 77 and 27 checks respectively.
The [design record](../Design/RESOURCE_DETAILS_LIVE_MAP.md) records research,
coordinate assumptions, attribution, and service limitations.

## Resource Details Activity-table wireframe and deployment - 26 October 2026

The separate `resource-details-activity` page now reuses the complete recovered
Resource Details template while populating only Activity > Table. Its cross-type
wireframe contains Observation, Command, and System Event rows and exposes All,
Observations, Commands, and System Events filters. The design follows the explicit
Activity requirements recovered from the Resource Details research paper; it does
not imply a universal Activity API endpoint. The original
`resource-details-template` page remains available as the blank reusable template.

Production deployment `ee6812b6-d964-4407-9fac-6652d0db965f` publishes commit
`db96c584fdf52715e4a005be2c4159b1bc131b24` at
<https://glaux-client.pages.dev/?page=resource-details-activity>. The production
Activity suite passed 15 checks and the original-template regression suite passed
27 checks, both with zero browser script errors. The implementation, research
basis, build, deployment, and live verification are complete.


## Smart Citizen corrective model-currency / paper v0.10 closeout — 25 October 2026

The owner identified a material research-continuity failure in paper v0.9: the paper had summarized an earlier, narrower profile-era donor table as though it represented the current DIM/MPSS research program. A proof-level corrective audit is now complete in [06_MODEL_CURRENCY_AUDIT.md](../Research/Studies/Smart_Citizen/Workbook/06_MODEL_CURRENCY_AUDIT.md). The audit distinguishes the frozen Smart Citizen source evidence, accepted MPSS v0.3.5 technical rules, the larger v0.10 research corpus, and experiment-specific authored transformations instead of treating any one summary as authority for all four.

The audit **did not invalidate the experiment wholesale**. Phase 1 frozen evidence and Phase 2 source characterization are retained; Phase 3 retains its core semantic mappings with repaired current-donor traceability; Phase 4 retains the 2-System / 2-Procedure / 10-DataStream / 56-Observation resource count. Required corrections are now in the mapping ledger and resource graph: accepted R15 representation-source provenance is carried on SC-SYS-001; the aggregate process System, reusable aggregation Procedure and one frozen query/execution are explicitly distinct; authored aggregate-property definitions state their base property/statistical/procedure/authorship scope.

Paper v0.10 has been rebuilt from that audited baseline. It explicitly distinguishes accepted MPSS v0.3.5 rules from the wider v0.10 research corpus; restores later ISA, SAPIENT v2, The Open Group SOSA, IEEE 1451/TEDS, OMS, SOSA/SSN, I-ADOPT, QUDT/UCUM/SWEET and OSCAR work with their actual standing; places the DIM/research synthesis before the Smart Citizen case; moves acronyms and definitions to appendices; removes the standalone power-special-case narrative; and replaces the v0.9 conceptual figure with one evidence-to-design diagram plus three UML-style R01–R20 relationship diagrams.

**Final publication verification:** GitHub Actions run `40218125110` rebuilt v0.10 from source commit `0848cba3` and committed the generated Word edition at `501ba4b8`. The verifier passed 51 cited references, 11 figures, 2 listings, current Word inputs and 22 publication files. The final DOCX SHA-256 is `1c284838bbc15d94edad69b8804093beadc4174768adc46982b1c9b0a8043a31`; it renders to 50 pages. Every page of the successful pre-final build was visually inspected; the only final correction was a stale figure cross-reference on page 38, rendered-page hash comparison confirmed that page 38 alone changed, and the final page 38 was re-inspected cleanly.

**Current gate:** the corrective model-currency/paper v0.10 closeout is complete. No Phase 5 adapter code, CSAPI server write, Glaux behavior change, deployment, or MPSS v0.3.5 revision was performed. Phase 5 deterministic adapter implementation is the next experiment phase when the owner resumes it.



## Smart Citizen paper v0.9 DIM/Profile architecture closeout — 25 October 2026

Before Phase 5 begins, the owner identified that the paper evaluated the MERLIN domain information model and Managed Physical Sensing Systems profile without adequately explaining that work near the front of the paper. Version 0.9 corrects that structural deficiency by adding a dedicated section before the experimental infrastructure covering the problem/purpose, domain-model versus application-profile versus OGC-binding versus implementation layers, the eight whole-system information subjects, bounded donor/reuse lineage, the R01–R20 relationship/binding method, reusable group contracts, and generic versus profile-aware consumption.

The revision also adds a generic DIM/Profile architecture figure and three explanatory tables. It deliberately does not turn the Smart Citizen paper into a duplicate profile specification: detailed normative obligations remain in MPSS v0.3.5, while the paper gives readers enough architecture and provenance to understand what the experiment is testing. Existing later sections are renumbered, and the Smart Citizen-specific conceptual figure remains separate from the new generic profile figure.

**Final publication verification:** GitHub Actions run `40206986860` rebuilt paper v0.9 successfully from source commit `22a05d08` and committed the generated Word edition at `a73285ae`. The verifier passed 45 cited references, 8 figures, 2 listings, the paragraph and acronym policies, current Word inputs, and 19 publication files. The final DOCX SHA-256 is `39307527446579faab6de7c3a11479fe576fd6d8fad1501386582ff85a52f97d`; the edition renders to 44 pages. The full first v0.9 render was visually inspected, and after correcting the DIM/Profile figure spacing plus one vendor-figure cross-reference, page-hash comparison showed only pages 11 and 38 changed; both final pages were re-inspected and are clean.

**Current gate:** the v0.9 DIM/Profile architecture closeout is complete. No Phase 5 adapter code, CSAPI server write, Glaux behavior change, deployment, or MPSS v0.3.5 revision was performed. Phase 5 deterministic adapter implementation is the next experiment phase when the owner resumes it.



## Smart Citizen paper v0.8 Phase 4 closeout and acronym control — 25 October 2026

The owner stopped Phase 5 before any adapter code was changed and directed that the completed Phase 4 findings be incorporated into the research paper first. Paper v0.8 now records the reviewed Phase 4 resource graph, negative-resource decisions, deterministic study identity policy, current/aggregate time projections, and bounded 52°North target constraints while continuing to state that deterministic adapter execution and all CSAPI server writes are unexecuted.

The owner also identified excessive acronym use as a usability problem. Version 0.8 adds a dedicated Acronyms and Abbreviations section, expands uncommon shorthand on first substantive use where practical, and uses Smart Citizen's source wording **received signal strength indication (RSSI)**. Repository maintenance instructions and the paper verifier now require the core acronym inventory and flag recurring narrative shorthand that is missing from the maintained table.

**Final publication verification:** GitHub Actions run `40202562737` rebuilt paper v0.8 successfully from source commit `58f4811f` and committed the generated Word edition at `377eca29`. The verifier passed 45 cited references, 7 figures, 2 listings, the three-to-five-sentence paragraph policy, the maintained acronym policy, current Word inputs, and 18 publication files. The final DOCX SHA-256 is `a5e70eb9099424b14e67261fa1faa632184d69c4438341a2e9a3d635f43687c0`; the edition renders to 38 pages and every final page has been visually accounted for, with all changed/reflowed pages re-inspected after the QA corrections.

**Current gate:** the Phase 4 paper/acronym closeout is complete. No Phase 5 adapter code or CSAPI server write was performed during this correction. Phase 5 deterministic adapter implementation is the next work item when the owner resumes the experiment.



## Smart Citizen Phase 4 resource-graph checkpoint — 25 October 2026

The owner authorized **Phase 4 only** after accepting the reviewed Phase 1–3 baseline and the principle that Smart Citizen/Kairos hourly averages are source-platform processing products rather than direct physical-kit output. Phase 4 is now complete in [the CSAPI resource-graph workbook](../Research/Studies/Smart_Citizen/Workbook/03_CSAPI_RESOURCE_GRAPH.md). **No adapter code, CSAPI write, Glaux change, deployment, or MPSS v0.3.5 revision was performed.**

The reviewed first-load graph contains two Systems (the represented SCK case and a source-platform aggregation process), two Procedures (SCK2.3 model/datasheet and one-hour aggregation method), ten DataStreams with ten per-stream observation schemas, and 56 frozen Observations. It deliberately creates no SamplingFeature, Deployment, installed component Systems, battery System, Wi-Fi interface System, SD-card System, controls, source-registration resource, current-value processing System, or first-target Property resources. Stable study feature identities use deterministic UUIDv5 URNs and are explicitly scoped to MERLIN study representations rather than manufacturer/physical identity.

Phase 4 resolves the executable time policy without hiding source under-specification. Current observations send both phenomenonTime and resultTime using the channel reading timestamp as a documented coincident-time projection; experiment acquisition time remains separate provenance. Aggregate observations keep the returned tuple timestamp as phenomenonTime and use the corresponding frozen HTTP response Date as a qualified source-response resultTime proxy, while one-hour averaging meaning remains in the derived property and aggregation Procedure rather than fabricated interval bounds.

Target-source inspection at 52°North revision `6ad75aa7...` exposed four implementation constraints now recorded in the findings register: no POST route for Property resources despite create logic/example files; a generic Part 1 replace path unsafe as a Property-create workaround; a target observation schema more permissive than approved CSAPI on phenomenonTime; and incomplete cascade deletion. The first-load design therefore uses stable derived-property URIs instead of local Property resources, sends both required Observation times, avoids implementation-specific meta-datastream behavior, and requires explicit child-first cleanup.

**Next action: owner review of Phase 4. Phase 5 adapter implementation is not authorized merely by completion of this checkpoint.**


## Smart Citizen Phase 1–3 review gate and paper v0.7 — 25 October 2026

**Final publication verification:** GitHub Actions run `40195631894` rebuilt paper v0.7 successfully from source commit `d0905f1c` and committed the generated edition at `de034ba4`. The verifier reported 43 cited references, 7 figures, 2 listings, current Word inputs and 18 publication files; the generated DOCX SHA-256 is `1ff723be43386c20a33847c92203eaceaaf5f7d4a0acc68bc140e53d2889b108`. The final edition renders to 33 pages; every page was visually inspected, two stale v0.6-era figure-status labels found during the first review were corrected, and the final render has no observed clipping, overlap, broken tables or missing figures. This is a documentation/research checkpoint only; no application deployment, server write or Phase 4 resource-graph work was performed.

The owner requested the review checkpoint that should have occurred before the prior execution advanced automatically. Phase 1 is now confirmed complete for frozen registration 19639; Phase 2 is reviewed and corrected; Phase 3 contains nine current-state and two aggregate-history mappings at the documented review standing. **Historical checkpoint:** Phase 4 had not begun at this point; it was subsequently authorized and completed in the Phase 4 section above.

The corrective review found several issues worth preserving rather than silently fixing. The native timing cohort is 11 non-SEN5X channels at 02:40:21Z plus 10 SEN5X particulate channels at 02:36:21Z, not the previously written 17+10; Smart Citizen's `_raw` path contains a normalized/pre-calibration value rather than proof of untouched raw output; notification booleans are settings, not live condition assertions; and the earlier RSSI `status` classification overreached the evidence. The mapping ledger now leaves RSSI subject/DataStream type unresolved, models hourly averages as source-platform processing rather than physical-kit output, and distinguishes server-derived DataStream summary fields from adapter-authored content.

Paper v0.7 updates the formal specimen from the earlier feasibility values, adds a sourced Terms and Definitions section, and audits key usages such as telemetry, provenance, measurement, calibration, Observation, DataStream, source time and acquisition time against those definitions. It reports Phase 1–3 acquisition/characterization/mapping results while continuing to state that the adapter, CSAPI publication/round trip, connected Glaux retrieval and matched interface comparison are unexecuted. This was the Phase 1–3 checkpoint; the owner subsequently authorized Phase 4, whose completed design and new review gate are recorded above.

## Smart Citizen execution roadmap and workbook — 24 October 2026

The owner approved preserving the current end-to-end plan and detailed experiment homework outside the research paper. The new execution roadmap defines eleven phases with explicit gates and milestones; the new workbook supplies living templates for source capture/inventory, mapping lineage, CSAPI resource design, execution evidence, UI/PBI findings, transferability, and material decisions. The existing experiment plan remains as rationale/history, while the roadmap is now the current sequencing authority.

**Historical planning checkpoint:** at the time this section was written, immediate work was Phase 1 specimen capture and inventory. Phases 1–4 have since been completed through the reviewed resource-graph design recorded above; this historical paragraph does not override the current Phase 4 owner-review gate.

## Paper version 0.6 vendor presentation baseline — 24 October 2026

The owner requested populating the source-provider side of the interface comparison before the CSAPI/Glaux results exist. Paper v0.6 now includes two unchanged first-party Smart Citizen UI screenshots selected from the official documentation: the core platform's basic measurement-exploration view and the separately documented custom dashboard. Their source pages describe their roles, while a new evidence record preserves exact repository revision, asset path/blob, historical device/time context, and rights notices.

The new section explains what Smart Citizen makes visible—resource/reporting context, multiple current quantities, values and units, a selected property's explanation and history, sensor/model labels, and alternate dashboard organization—without treating those pixels as normative MERLIN requirements. A reconstruction-question table converts those presentation observations into testable questions for the DIM/Profile and Resource Details PBI. Figures 8–10 remain reserved for a contemporaneous selected-registration source view if available, the matched generic/profile-aware Glaux comparison, and the implemented CSAPI relationship/source-to-display trace.

The screenshots are historical examples rather than registration 19639 evidence, and the paper says so explicitly. The adapter, CSAPI loading, live integration, and matched interface evaluation remain unexecuted. The repository paper workflow regenerated the v0.6 Word edition and refreshed publication fingerprints successfully. The exact GitHub Actions-generated 29-page edition was downloaded, rendered, and every page was visually inspected; both source screenshots, captions, continuation tables, references, headers, footers, and page flow are clean.

## Paper version 0.5 experimental Glaux client — 24 October 2026

The owner required the paper to describe the client side of the experiment as rigorously as the CSAPI server. Paper v0.5 now records the standalone `OS4CSAPI/glaux-client` lineage, why Explorer and `cs-client-ts` were not selected as the experimental foundation, the exact pinned `OS4CSAPI/ogc-client-CSAPI_2` phase-10 dependency, and the separate `src/data`, `src/profile`, and `src/presentation` responsibilities. A new evidence record and architecture figure make the Standard View / Operator View comparison boundary explicit.

The paper also records the public Cloudflare Pages runtime, deployed Git commit and deployment ID, the recovered 560 × 440 review frame, and the current direct-System remote-read limitations. It explicitly states that authenticated service access, collection discovery, and full System-to-DataStream/schema/Observation traversal are not yet deployed and are part of the Smart Citizen client increment. Documentation changes do not alter the current public runtime.

The local v0.5 review copy renders to 26 pages. All pages were visually inspected after the client-section and figure revisions; a final wording correction changed only page 22 relative to that inspected render, and page 22 was re-inspected. The repository paper workflow regenerates the Word edition from the maintained manuscript and refreshes its publication fingerprints so the committed reading copy remains source-consistent.

## Paper version 0.4 experimental CSAPI server — 24 October 2026

The owner required the research paper to explain the 52°North/pygeoapi CSAPI server as part of the experiment rather than treating it as an unnamed transport. Paper v0.4 now documents pygeoapi's role, 52°North's Connected Systems proof of concept, the exact tested upstream revision, the Oracle-hosted OS4CSAPI deployment, image identity, deployment adaptations, and the bounded cross-server evidence that supports using it as the first Smart Citizen target. The paper also records the deployment details that are still unknown instead of inferring them from upstream examples.

A new repository evidence record preserves the server baseline and an authored figure distinguishes implemented server lineage from the proposed Smart Citizen adapter and Glaux path. The server selection is explicitly bounded: on the October 19 preservation sample, CS-GO rejected the tested characteristics, OpenSensorHub accepted but failed to return selected group IDs and conditions, while 52°North/pygeoapi accepted and returned all submitted fields. This does not establish complete CSAPI conformance, restart durability, observation publication, command support, or universal superiority.

The dedicated paper workflow completed successfully for v0.4 and committed the generated Word edition. The final 21-page edition was rendered and visually reviewed; the server-lineage figure, deployment table, citations, references, code/listing content, headers, footers, and page flow are clean. The final one-word version correction affected only page 18 in the rendered comparison, while the other 20 pages were pixel-identical to the already inspected v0.4 render. The deployed Glaux runtime remains unchanged because this is documentation and research-method work.

## Paper version 0.3 illustrated system overview — 24 October 2026

The owner requested an early explanation of the system type and selected case,
supported by an authentic image. [Paper v0.3](../Research/Studies/Smart_Citizen/README.md)
adds an illustrated overview of Smart Citizen as an environmental-monitoring
system and identifies SCK 2.3 as the model reported by public registration 19639.
The model reference photograph does not verify that registration's physical
installation, component inventory, or placement.

The immediate proposal remains public Smart Citizen readings → documented adapter
→ CSAPI → Glaux, accompanied by deterministic captures. An owned kit is a later
route to physical-context evidence, and AirGradient is a later independent
comparison. The existing mapping-lineage requirements, three-to-five-sentence
narrative policy, MPSS v0.3.5 baseline, and original imported artifacts remain in
force.

Verification passed: all eighteen rendered Word pages were visually reviewed,
including the photograph and caption on page 2 and complete system-identification
table on page 3. All 72 narrative/explanatory-caption paragraphs meet the required
length: 25 have three sentences, 37 have four, and 10 have five. The paper checks
passed for 22 cited references, three figures, two listings, current Word inputs,
and fourteen publication-file fingerprints; the six tables were also reviewed.

Repository verification passed for all fourteen original artifacts and 302 local
links across 27 documentation files. The photograph matches its official source
blob byte-for-byte, with source credit and both published rights notices retained.
The counts and verification results in the v0.2 and v0.1 sections below describe
those earlier editions. This document revision does not execute the adapter,
CSAPI publication, live experiment, or interface comparison, and the deployed
runtime remains `71297c97`.

## Paper version 0.2 donor explanations and paragraph structure — 24 October 2026

The owner clarified that every mapping must explain its CSAPI concepts and
SensorML/SWE representation, underlying DIM concept, exact MPSS rule, and each
individual donor-source concept invoked. [Paper v0.2](https://github.com/OS4CSAPI/glaux-client/blob/387363d5f83d6193fa11ef3342a5db707fe6a7f9/Docs/Research/Studies/Smart_Citizen/README.md)
now sets that requirement in a seven-layer mapping matrix and illustrates it with
`SC-TEMP-01` and `SC-BATT-01`. The examples identify observation-concept lineage,
source property and unit vocabularies, representation mechanisms, authored choices,
and RFC battery/topology limits without claiming completed mappings or execution.

The paper now contains twenty-two references and five tables alongside its two
figures and two JSON listings. All narrative paragraphs, including the abstract
and explanatory captions, have three to five sentences. The publication verifier
enforces the requested range and reports paragraph locations and counts; the
maintenance guide, experiment plan, indexes and AGENTS instructions preserve both
requirements for later work.

Verification passed for all 66 narrative/explanatory-caption paragraphs: 23 have
three sentences, 33 have four, and 10 have five. All sixteen rendered Word pages
were visually reviewed, and the illustrative lineage was checked against retained
project evidence and primary sources. The publication checks confirmed twenty-two
cited references, consistent listings and current Word inputs; repository checks
confirmed all fourteen original artifacts and 292 local documentation links, with
a clean whitespace check.

This remains a protocol and preliminary assessment. The adapter, CSAPI publication,
live run and screenshot comparison remain unexecuted, and the fourteen imported
originals retain their existing bytes and versions. The deployed runtime remains
`71297c97`, so this documentation increment requires no application upload.

## Initial Smart Citizen experiment paper version 0.1 — 24 October 2026

The owner requested an academic-style document that develops with the experiment.
[Paper v0.1](https://github.com/OS4CSAPI/glaux-client/blob/57a2d1b68ad5c30a0a005c6095306e050fa9e4a9/Docs/Research/Studies/Smart_Citizen/README.md) established a drafted protocol
and preliminary source assessment, with a canonical Markdown manuscript and a
generated Word edition. It contains an abstract, eleven numbered sections, nineteen
CMOS 18 author-date references, two authored diagrams, four tables, and two explained
JSON listings. Source-interface and matched Glaux screenshots have a defined
capture/comparison protocol and reserved figure slots; none is reported as captured.

The methods describe public Smart Citizen data flowing through a documented adapter
and CSAPI service into Glaux, with reproducible captures and competent generic/profile
comparison. Owned hardware is a later extension. The earlier
[experiment plan](SMART_CITIZEN_EXPERIMENT_PLAN.md) is reconciled with this sequence
and the broader specimen scope discussed with the owner. The first two fields can
start a trace, but metadata, multiple quantity types, indicators, history and
provenance are part of the intended dataset.

The paper has its own publication manifest and reference records. The repository
verification command checks citation/reference agreement, source-excerpt fidelity,
listing consistency, figure presence, Word input freshness, and publication-file
fingerprints in addition to the fourteen original artifact hashes and local links.
The original artifact manifest and MPSS v0.3.5 baseline are unchanged.

Verification passed: all thirteen rendered Word pages were visually reviewed;
the paper verifier confirmed nineteen cited references, two figures, two listings
and ten publication-file fingerprints. The repository verifier confirmed all
fourteen original artifacts (27,555,946 bytes) and 292 local documentation links.
Technical/source review and the whitespace check passed. These documentation
checks do not establish OGC conformance or experiment results.

This increment creates research documentation and its maintenance tooling. No
adapter, CSAPI dataset, live integration, screenshot comparison, new application
page, or measured UI benefit is implemented by it. The deployed runtime remains
`71297c97`; no Cloudflare upload is needed. Continue by recording the initial
field mapping and selected service capabilities, then use the paper's execution
protocol to record actual integration evidence.

## Open sensor research and Smart Citizen proposal — 24 October 2026

The owner requested filing the device-candidate findings and proposing a Smart
Citizen experiment. The [research report](../Research/Reports/OPEN_SENSOR_CANDIDATES_2026-10-24.md)
preserves the shortlist, recommendations, source links, access results, prices
and limits. The [evidence record](../Research/Evidence/OPEN_SENSOR_ACCESS_2026-10-24.json)
preserves 15 study-local observations with selected excerpts and available
response fingerprints. The [experiment plan](SMART_CITIZEN_EXPERIMENT_PLAN.md)
initially proposed one public specimen, explicit mapping, a deterministic 560 × 440
review, then owned hardware and live access. The current paper and reconciled plan
supersede that ordering by placing public live integration before acquisition;
AirGradient remains an independent later comparison.

This is a documentation increment. The study and proposal are complete; the
Smart Citizen adapter, recorded-data page and live integration are not present.
The 14 imported originals, their manifest, the technical profile and application
code retain their existing versions. The runtime remains `71297c97` and the
six-page production site recorded below. No Cloudflare upload is needed for
this documentation publication. Git history records the actual publication commit.

Documentation verification passed: all **14 original artifact hashes and
27,555,946 bytes**, **247 local links across 24 documentation files**, valid
evidence JSON with 15 unique record IDs, and a clean whitespace check. The
evidence was compared with the retained captures: **10 body hashes/lengths and
136 selected fields or source lines** matched, including all 24 historical
temperature groups. An independent review checked the Smart Citizen facts and
the boundary between proposed and implemented behavior. Runtime browser checks
were not rerun for this documentation-only increment.

Continue from the proposed evidence-to-mapping specimen, with implementation
status distinguished from plan status. The [broader continuity note](CONTINUITY.md)
reconciles this sequencing with the retained research backlog.

## Resource Details View template — 24 October 2026

The owner requested a blank template using the framework recovered from the
earlier Resource Details PBI work. The new `/?page=resource-details-template`
route retains the **560 × 440 CSS-pixel working frame**, fixed identity and top/
bottom marking placeholders, adjacent category/subcategory rows, and internally
scrolling content. The later working-view labels remain provisional. Exact
source sections, PDF pages, and current implementation choices are in the
[template design record](../Design/RESOURCE_DETAILS_TEMPLATE.md).

The page starts blank and makes no fixture or remote data requests. Optional
layout-only samples demonstrate vertical, horizontal, and combined overflow.
Native resizing and keyboard-accessible size controls include a reset to the
recovered default. The homepage now lists six pages; the data-example selector
retains its original five entries. Existing examples and source bytes are intact.

Local verification passed: **74 offline tests**, TypeScript/production build,
**27 template browser checks**, **44 index checks**, **23 baseline checks**, and
**44 power checks**, with no script errors. Native scrollbar rendering was enabled
for visual inspection, including blank, overflowing, resized, and narrow canvases.
The implementation is saved on GitHub and deployed. **All 27 template checks and
44 index checks passed again on production**, with no browser script errors.
The current runtime is
[`71297c97`](https://github.com/OS4CSAPI/glaux-client/commit/71297c971e2e7532f7c7139600f41e9b58bdcc22),
with [passing GitHub CI](https://github.com/OS4CSAPI/glaux-client/actions/runs/40130331258).
Pages deployment `97c801c4-c44f-4484-a175-e6651639fe07` completed at
**4:34:47 p.m. EDT on 24 October 2026**. Open the
[live template](https://glaux-client.pages.dev/?page=resource-details-template)
or [six-page index](https://glaux-client.pages.dev/).
The [deployment record](CLOUDFLARE_DEPLOYMENT.md) retains the runtime identity and
live checks. This increment is complete; the preceding checkpoints below are history.

## Experiment index — 24 October 2026

The user requested a deployed index listing the experiment pages, descriptions,
latest updates, and update dates/times. The deployed implementation includes a homepage
index for the five existing examples, links back from every example, and URL
synchronization when selecting an example. One typed catalogue supplies both the
index and selector; [the maintenance guide](../Design/PAGE_INDEX.md) records the
update procedure and the Git evidence for the initial dates.

Local verification passed: 74 offline tests, TypeScript/production build, 36 index
browser checks, 23 existing example checks, and 44 power checks. No browser script
errors occurred. The 36 index checks passed again against the production origin.
The current deployed runtime is
[`0d977e36`](https://github.com/OS4CSAPI/glaux-client/commit/0d977e366e55363dd997c0f519c7cca2bc814530),
with [passing GitHub checks](https://github.com/OS4CSAPI/glaux-client/actions/runs/40113200519).
Cloudflare Pages deployment `44f92062-a39a-4f86-9267-a63bd0935f53` completed at
**12:52:53 p.m. EDT on 24 October 2026**. The index is live at
<https://glaux-client.pages.dev/>; the immutable deployment is
<https://44f92062.glaux-client.pages.dev/>.

The [deployment record](CLOUDFLARE_DEPLOYMENT.md) preserves the actual upload
method, runtime identity, and live verification. Keep the catalogue current as
pages are added or their behavior changes. The records below preserve the earlier
power implementation and deployment checkpoint; they do not supersede this one.

## Previous implementation and deployment checkpoint

Updated 24 October 2026. **Power-arrangement implementation, local verification,
Cloudflare deployment, and live verification are complete.**

The owner subsequently authorized publication of the maintained project artifacts.
The [Artifact Register](../ARTIFACT_REGISTER.md) and [manifest](../ARTIFACTS.json)
now identify the original source files. [MERLIN continuity](CONTINUITY.md)
reconciles their 22 October checkpoint with the completed client work. This
documentation increment does not change the deployed runtime revision below.

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
- Verified public deployment: `d74b33dabc5fdfcf22574b8efa7f436b4cf32857`,
  Cloudflare Pages deployment `770d234a-3cb5-415a-aa96-b8fea45180c4`,
  <https://glaux-client.pages.dev/?example=power>.

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
[Details View mapping](../Design/DETAILS_VIEW_MAPPING.md). The identified original
project artifacts are published at their registered paths; their original
versions, bytes, and proposal boundaries remain explicit.

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
| New live deployment | 44 power checks passed against `https://glaux-client.pages.dev`; zero browser script errors |

The [browser verification record](../Testing/BROWSER_VERIFICATION.md) links the
actual emitted results, reproducible scripts, and selected local screenshots.

Checks use explicitly synthetic local data. They establish this bounded behavior,
not complete OGC/MPSS/RFC conformance, live-server interoperability, production
readiness, or measured comparative operator benefit.

## Deployment boundary and next action

The existing Pages project remains **Direct Upload**. Pushing GitHub does not deploy
it. The authenticated local Wrangler session uploaded the verified checkpoint and
the production deep link now serves the power example. The exact outcome is in
[the deployment record](CLOUDFLARE_DEPLOYMENT.md).

Review the deployed power example and continue the existing draft PR. Any later
implementation revision requires another explicit build, upload, and live check.
Preserve unrelated local changes and save each meaningful continuation to the
working branch; chat commentary is not a source checkpoint.

For artifact changes, run `python3 scripts/verify-artifacts.py` and update the
register, manifest, and continuity notes together. The earlier PITON/plan files
preserve their source checkpoint; use CONTINUITY.md for current locations and
sequencing. A repository documentation commit can be newer than the runtime
commit without requiring another Cloudflare upload.
