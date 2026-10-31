# PITON v1.9 — DIM / CSAPI Profile V2 and live Glaux recovery

**31 October 2026 (America/New_York) · Recovery/handoff document, NOT a new execution plan or adopted specification.**

**Canonical repository:** [OS4CSAPI/glaux-client](https://github.com/OS4CSAPI/glaux-client)  
**Research branch:** `research/dim-profile-v2` · **application/deployment branch:** `work/details-view-20261023`  
**Research home:** `Docs/Research/DIM_Profile_V2/`  
**Branch snapshot immediately BEFORE this PITON:** research HEAD `4a68e5753481bf57dd4d12e3c64ef634324da40f`; application HEAD `bb44bcc64551034aa21e7bf63a9a7e28993e184c`. These are **checkpoints**, not assumptions that branch heads will never move.  
**Supersedes for status and restart:** [PITON v1.8, 30 October](PITON_DIM_Profile_V2_Continuity_v1.8_30OCT2026.md). Preserve v1.8 and all preceding documents for the earlier research, its corrections and source trail. **The v1.9 number identifies this recovery note, not the DIM or Profile edition.**

## 0. Read this first — the whole situation in ordinary language

**We have done real work; we have not solved the larger problem.** The aim is a useful, standards-grounded, vendor-neutral way for a single OGC API – Connected Systems (CSAPI) client to understand and display meaningful information about different sensing systems. We want a defensible, implementation-independent **Domain Information Model (DIM)**, a separate, implementable CSAPI **application Profile**, and a real, Profile-aware Glaux Resource Details experience. A technically successful experiment is evidence toward those goals, **not proof that the DIM or Profile is finished**.

Before 31 October, the V2 effort had candidate conceptual distinctions, donor-comparison research, three well-documented reference/example equipment sheets, and a primitive but useful client comparison. It did **not** have complete cross-vendor operational equipment datasets or a finished model. On 31 October, work expanded into official standard excerpts, candidate DIM/Profile sections, an evidence-backed **Bennett's Point** historical temperature/probe-swap example, and actual reads/writes against our running 52°North/pygeoapi CSAPI service.

**What definitely works now:** the live Oracle-hosted server contains **two individually identified Campbell Scientific EE181 probe Systems**, with two original scalar historical temperature Observations. A separate pair of *archival-report* DataStreams holds richer records, allowing the original NOAA temperature flag and calculated nominal 15-minute averaging period to be read back exactly. The [dedicated Glaux live Bennett's Point page](https://glaux-client.pages.dev/?page=resource-details-live-bennett) actually queries these resources and displays them in the Resource Details views. Codex's independent Map component is reused; no probe coordinates were fabricated. GitHub Actions and deployed-browser checks passed.

**What is not resolved:** those additional DataStreams are a **preservation bridge**, not a fully satisfactory semantic binding. The current API `application/json` Observation's `phenomenonTime` is an **instant** even though OMS treats the phenomenon time of an average as a **period**; the source does not independently tell us the true `resultTime`; the 52°North implementation drops observation-level `parameters`; and requesting `application/swe+json` did **not** establish a genuine alternate SWE observation encoding. We have **two historical measurements represented through four Observation resources**, not four independent measurements. No complete station System, actual Deployment resource, location geometry, universal discovery rule, or general cross-vendor Profile conformance test has been completed.

**Current owner feedback overrides the assistant's momentum.** After the latest technical standards analysis, the owner said **“idk man, this stinks”**, then explicitly requested **a new robust piton**. The exact reason for the dissatisfaction was not specified: **do not invent one or treat the suggestion to build a SWE JSON contract test as an accepted next step**. The right handoff is an accurate recovery, not an automatic commitment to more encoding work. This request authorizes the PITON and discoverability links only; it does **not** authorize deploying, changing server records, selecting a new DIM class, or executing the old “next: proceed.”

### Starting-point links

| Need | Start here |
| --- | --- |
| What we are trying to accomplish, without bookkeeping | [Problem and outcome baseline](DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md) and [plain-language research story](DIM_Profile_V2_Research_Story_and_Current_Position_v0.1_29OCT2026.md), with later corrections |
| What was complete before the latest experiments | [PITON v1.8](PITON_DIM_Profile_V2_Continuity_v1.8_30OCT2026.md), [closed concept/donor/equipment comparison](Concept_Donor_Comparison/README.md) |
| Why premature priorities and “AI for AI” reports are dangerous here | [Owner-requested AI drift/hallucination case study](DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md) |
| What the current draft *proposes*, but has not adopted | [Candidate DIM text](Candidate_Specification/DIM.md); [candidate CSAPI Profile](Candidate_Specification/CSAPI_Profile.md); [side-by-side donor terms](Concept_Donor_Comparison/Donor_Terms_Side_by_Side.md) |
| What the new live experiment proved and did not prove | [Bennett's Point evidence and source rows](Candidate_Specification/examples/bennetts-point-ee181.json), [live implementation/context-bridge report](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/BENNETT_OBSERVATION_CONTEXT_BRIDGE.md) |
| Where the standards/encoding investigation stopped | [Observation encoding options and decision record, 31 Oct](Candidate_Specification/Observation_Encoding_Decision_31OCT2026.md) |
| What the Resource Details tabs are supposed to mean | [Candidate placement matrix](Candidate_Specification/Resource_Details_Placement_Matrix.md) and [original wireframe template design](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/RESOURCE_DETAILS_TEMPLATE.md) |

## 1. The deliverables and scope — do not reduce this to an observation-format project

The larger problem began with TRSS and OmniSense unattended ground sensing systems and the difficulty of rendering different manufacturers' resource details in one common client. The desired scope includes **the whole sensing System**, not just its observations: identity, product/model information, equipment, functional capability, actual activities, reported states, configuration, communication, control/commands, relationships, and provenance wherever source evidence supports them. Relevant output-specific data, including its subject, method, quality and time, matters within that whole-system problem.

The end products are distinct:

1. **DIM:** explain what the real-world and information subjects *mean* and how they relate, independent of any one JSON shape, server implementation or tab.
2. **CSAPI application Profile:** specify defensible, testable conventions for communicating those DIM meanings using existing CSAPI, Sensor Model Language (SensorML), SWE Common and other justified standards. State what is optional, required, still unknown and source-specific; do not invent OGC “SHALLs.”
3. **Glaux client / producer experiments:** exercise actual source-to-CSAPI-to-UI interpretation, preserve differences and unknowns, and reveal whether the proposed semantics support meaningful operator views. A screen layout is evidence about presentation, **not** an adopted DIM ontology.

**Do not prematurely name the universal chassis.** The owner has repeatedly insisted that the right bounded subject/name/structural foundation must emerge from the donor evidence, with the provisional focus around “system and sensor and equipment.” Do not reintroduce a *Managed Physical Sensing Systems* (MPSS) or MERLIN-specific root solely because V1 had one. Earlier MPSS/V1 artifacts are useful historical evidence, not automatic V2 design authority.

The five researched candidate distinctions remain a **starting hypothesis, not immutable classes**:

- **F-01 — Individual System:** which actual physical System is being described?
- **F-02 — Model/kind:** which reusable description concerns the kind of equipment rather than one unit?
- **F-03 — Procedure/capability/activity/result:** what could be done versus what was done and reported?
- **F-04 — Composition and relationship standing:** physical constituent, function, addressable channel and other relations are not interchangeable.
- **F-05 — Digital description/proxy:** a description, service or proxy of equipment is not automatically the equipment.

The candidate [DIM foundation v0.2](Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md), [cross-comparison](Concept_Donor_Comparison/README.md), and [31-Oct candidate DIM](Candidate_Specification/DIM.md) are **research/specification drafts**, not a completed, voted or independently validated structure. The newer candidate DIM has worked text on components/channels, what property is observed, and which configuration value applies. The [candidate Profile](Candidate_Specification/CSAPI_Profile.md) covers model-versus-instance, the probe-swap scenario, components/channels, temperature subjects, configuration and task replies. Do not mistake the existence of headings or prose for implementation conformance.

## 2. What had already been completed before this handoff

The prior [PITON v1.8](PITON_DIM_Profile_V2_Continuity_v1.8_30OCT2026.md) governs the detail through 30 October. Here is only the essential carry-forward:

| Workstream | What exists and actual status |
| --- | --- |
| Donor alignment | [12-iteration plan](PLAN_DIM_Profile_V2_Donor_Alignment_and_Foundation_v0.1_28OCT2026.md) **12/12 closed**; five candidate meanings and donor/relationship evidence, **not** a complete DIM or exhaustive all-donor audit |
| Further donor examination | [6-iteration plan](PLAN_DIM_Profile_V2_Donor_Challenge_v0.1_28OCT2026.md) **6/6 closed**; SAPIENT v2, substantial public IEEE 1451 material, Integrated Sensor Architecture (ISA) and The Open Group Sensor Open Systems Architecture (SOSA) reviewed, but “later donors challenge the incumbent” was **not** the owner's preferred neutral method |
| Equipment corpus qualification | [8-iteration plan](PLAN_DIM_Profile_V2_Controlled_Sensing_Equipment_Corpus_Qualification_v0.1_29OCT2026.md) **8/8 closed**; [AirGradient Open Air Max, Dragino S31-LB, Campbell CR1000X + ClimaVue 50](Controlled_Corpus/System_Data_Sheets/README.md) qualify as **reference/example material**, not actual complete fielded unit histories; Raspberry Shake & Boom was conditional, not silently selected |
| Concept/donor/equipment comparison | [4-iteration plan](PLAN_DIM_Profile_V2_Concept_Donor_and_Equipment_Comparison_v0.1_30OCT2026.md) **4/4 closed**; [three connected comparison pages](Concept_Donor_Comparison/README.md), not a completed mapping or transformation |
| Smart Citizen Kit 2.3 | [I01–I13](Case_Studies/Real_Equipment_DIM_Validation/README.md) ended in conditional acceptance **of the written case study**, not a fielded kit, live observations or accepted Profile |
| Original source preservation | [OMS 3.0.0 preservation record](Primary_Sources/OGC_20-082r4_OMS_3.0.0.md) links the *complete* PDF and page-marked text in the owner's connected Google Drive, with hash and exact IDs |
| Old Resource Details implementation | 560 × 440 working frame, two-level navigation, several synthetic/prototype pages; **not** a universal semantic model |

**Coverage limits:** the research corpus contains **182 recorded source artifacts, not 182 independent standards**. The pre-31-Oct comparison references 30 screened donor lineage/family keys, 48 original alignment record IDs and 27 grouped source-sheet comparisons. These are **bookkeeping coverage measures**, not proof every standard received equal-depth original-source review or that every meaningful system fact was mapped. PA-DIM, IEEE 1451, ISA, SAPIENT, OMS and other late contributors must retain their full potential to change the model; do not force them under F-01–F-05 merely because those headings already exist.

**Explicitly rejected drift:** the earlier assistant's habit of treating **“operational condition/status,” especially power**, as the obvious next model subject was not justified by equivalent donor pedigree or owner acceptance. See the [drift case study](DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md). Do not restart V1 power work or a closed “next iteration” when a fresh chat begins.

## 3. What changed on 31 October — reconstruct in this order

### 3.1 Candidate specification and real-world evidence work

The research branch acquired a fuller [candidate DIM](Candidate_Specification/DIM.md), [candidate CSAPI Profile](Candidate_Specification/CSAPI_Profile.md) and [side-by-side donor terminology](Concept_Donor_Comparison/Donor_Terms_Side_by_Side.md). Worked distinctions include **model versus identified unit versus Deployment; physical component versus function/channel/output field; temperature of the environment versus temperature of the instrument; documented defaults versus actual settings; requested Task versus resulting state**. Source editions and scope qualifiers matter; none is a newly adopted universal class or normative requirement.

Real published measurement examples were first used for Dragino/Campbell cases. We then selected **Bennett's Point**, a station in the ACE Basin National Estuarine Research Reserve (South Carolina), to test the harder issue of **two different individual physical probes of the SAME model serving the SAME station at different times**. It was selected because the archive and operator equipment history can be joined, not because two rows amount to a complete System dataset.

The [pinned Bennett source-evidence record](Candidate_Specification/examples/bennetts-point-ee181.json) has station code `acebpmet`, original CSV URLs and row locators, hash, year-round Eastern Standard Time (UTC−05:00), the operator’s probe-use history and a rejected counterexample. Key facts:

| Source CSV row | Station timestamp (EST) | UTC stamp | ATemp | Original F_ATemp (raw text) | Attributed particular probe |
| --- | --- | --- | ---: | --- | --- |
| **10130** | **15 Apr 2024, 12:00** | 2024-04-15T17:00:00Z | 29.1 °C | `"<0> "` (trailing space retained) | EE181 **sensor 4** serial `222016000109CE` |
| **10418** | **18 Apr 2024, 12:00** | 2024-04-18T17:00:00Z | 27.3 °C | `"<0> "` | EE181 **sensor 3** serial `21281600077814` |

The temperature is a **15-minute mean of 5-second samples**, with the source timestamp at the end of its nominal averaging period. Hence the calculated *nominal* UTC windows are **16:45–17:00 on each of those dates**. The flag `<0>` means *passed initial QA/QC*, not independent calibration approval. The two source CSV rows do **not** carry probe serials: attribution is a separately reasoned join to the operator’s dated equipment history. **The precise swap minute is unknown.** Sensor 4 is recorded in use from 8 June 2023 to 16 April 2024; sensor 3 returned on 16 April 2024 and is recorded as still in use at the end of 2024. Earlier sensor 3 use belongs to **the same identified probe**, not an additional piece of hardware. A rejected 17 April noon value (`<-3> [GPR] (CSM)`) is a **negative control**, not one of the two accepted readings.

Primary links: [2024 CSV](https://cdmo.baruch.sc.edu/waf/swmp_data_archives/acebpmet2024.csv), [ACE Basin operator metadata](https://cdmo.baruch.sc.edu/waf/YearlyFiles/ACE%20Basin/meteorological/metadata/acemet01-12.24m.pdf), [source-evidence/citation record](Candidate_Specification/examples/bennetts-point-ee181.json). Preserve the distinction between **original source values**, **our UTC conversion**, **calculated nominal window**, and **our separate serial attribution**.

### 3.2 Offline candidate encoding and controls

The [offline SWE JSON worked example and README](Candidate_Specification/examples/bennetts-point-wire/README.md) contain a `recordSchema` with `stamp` (`Time`), `window` (`TimeRange`), `air` (`Quantity`), `qc` (`Text`) and `probe` (attributed unit UID as `Text`). [`check.py`](Candidate_Specification/examples/bennetts-point-wire/check.py) reads the encoded fields by declared roles, resolves the physical unit and checks the expected values against separate source/history evidence. The recorded study passed two positives and five negative controls; **it was offline**, not a served CSAPI endpoint or independently certified conformance.

**Important modeling discrepancy:** this offline source-oriented example describes **one station air-temperature summary stream with per-record probe attribution**. The later live implementation chose **one scalar DataStream under each probe System**, and subsequently another archival-report DataStream under each probe. These are **different modeling/representation decisions**. Do not quietly call them equivalent, adopt one as the Profile, or erase the need to decide how the reporting station/logger, physical observing probe and parent stream relate. The physical sensing unit and the data publisher need not be the same entity.

### 3.3 A historical client-side display, then actual CSAPI

**Prepared historical test:** [`?page=resource-details-profile-test&case=bennetts-point`](https://glaux-client.pages.dev/?page=resource-details-profile-test&case=bennetts-point) uses source-grounded records **prepared in TypeScript**, not a live server query for Bennett data. It preserves previous SCK, TRSS, OmniSense and published examples. Its source representation, attribution and UI placement are deliberate experiment fixtures. Do not confuse it with the live page.

**Generic live-server browser:** [`?page=resource-details-live-csapi`](https://glaux-client.pages.dev/?page=resource-details-live-csapi) really performs browser-side GETs to the Oracle-hosted **52°North / pygeoapi Connected Systems API** at [`https://129-80-248-53.sslip.io/csapi-pygeoapi/`](https://129-80-248-53.sslip.io/csapi-pygeoapi/). It enumerates returned Systems and queries a selected System, DataStreams, Deployments, Subsystems and up to the tested limit of associated Observations. This proved that live HTTP retrieval and the Resource Details UI can be joined; **it did not prove all sources are live sensor feeds or establish a complete Profile**.

**Controlled live Bennett case:** [`?page=resource-details-live-bennett`](https://glaux-client.pages.dev/?page=resource-details-live-bennett) targets **known server-assigned resource IDs** for the two probe Systems, streams and observations. The client calls the live server; its underlying values/records are not TypeScript-only fixtures. However, **the case is selected and joined with hard-coded test IDs/assumptions**, not discovered by a general machine-readable Profile, and some display sections still use case-specific fallback values. Do **not** claim a fully generic source-independent CSAPI client implementation or standards conformance.

**Systems and original scalar Observations on 52°North (loaded and read back):**

| Physical unit and stable UID suffix | Live System local ID | Scalar DataStream ID | Historical scalar Observation ID |
| --- | --- | --- | --- |
| **Probe 4**, `...:probe4`, serial `222016000109CE` | `b171318e-8efe-550d-be99-bec5364984c0` | `351545ac-6ad6-418e-9688-7bba0329bb38` | `4f3d3010-9e46-4227-9ba0-7d7014405efa` |
| **Probe 3**, `...:probe3`, serial `21281600077814` | `378df868-d52f-4847-b783-865ec0c1df5e` | `d97c6dcc-d09d-4c70-aae9-a1b63c29e4b9` | `33599d37-7992-4e14-a4c1-b0df85d62fc2` |

Each System links via `typeOf` to the **same** project-authored [EE181 model description fixture](https://glaux-client.pages.dev/fixtures/bennetts-point-ee181-model.sml.json). That JSON is **not a Campbell-issued datasheet or a separately published live server `Procedure` resource**. The server assigns/normalizes its local identifiers; stable `uniqueId` is the loader’s identity anchor. The two records have no actual CSAPI `Deployment` resources and no demonstrated probe coordinates. Do not infer current location from station name or a 2024 history interval.

Implementation record: [first loader](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/scripts/load-bennett-v2-csapi.py), [successful round-trip Action run 41232435599](https://github.com/OS4CSAPI/glaux-client/actions/runs/41232435599), and [dedicated live view code](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/src/presentation/resource-details-live-bennett.ts).

### 3.4 Tab allocation and Codex’s map

A user correction established that **Overview must not become a dumping ground**. The [candidate Profile → Resource Details placement matrix](Candidate_Specification/Resource_Details_Placement_Matrix.md) is a proposed application-design tool, based on the existing UI requirements, with decisions labeled **Supported**, **Candidate** or **Unresolved**:

- **Fixed identity frame:** resource name/type/local ID/source, not buried in Overview.
- **Operational → Overview:** concise summary only; **Equipment:** actual units, model and composition; **Map:** evidenced position, not inferred placement; **Communications:** actual interface context, not every CSAPI DataStream by default; **Condition:** current/recent reported condition, not historical measurements.
- **Activity → Table/Charts:** historical Observations and quality beside their values; histories of changes when evidenced.
- **Commands → Available/Requests:** available control versus requested actions, responses and outcomes, not automatically effective equipment state.
- **Management → Record/Configuration/Sources:** raw representation, qualified settings and defaults, and provenance/mapping evidence.

Do not treat this as a universally settled tab taxonomy; **DataStream versus Communications, operating mode versus Configuration/Condition, Deployment versus Map/Equipment, and Overview inclusion limits remain open**.

Codex independently built a shared Leaflet-based Map component, [`renderResourceMap()`](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/src/presentation/resource-details-map.ts), tested on its [separate live-map page](https://glaux-client.pages.dev/?page=resource-details-live-map). It respects GeoJSON longitude/latitude ordering, a qualified alternative-axis interpretation, raw coordinates, no tracking/accuracy claims and missing/invalid-position fallbacks. The dedicated Bennett page **reuses it rather than copying it**. When Probe 4 or Probe 3 is selected, both currently show **“No position was supplied for this System”**, without inventing a map marker. The source record is [Bennett Map integration report](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/BENNETT_LIVE_MAP_INTEGRATION.md), [successful UI deployment run 41247110981](https://github.com/OS4CSAPI/glaux-client/actions/runs/41247110981).

### 3.5 The quality/averaging interval bridge — verified preservation, NOT resolved semantics

The original 52°North scalar Observations contained **temperature and timestamp**, but neither the original `F_ATemp` flag nor the nominal 15-minute interval. To preserve those fields without editing existing observations, a separate loader created **one additional “archival-report” DataStream per probe**. Each uses a SWE Common-style `DataRecord` **inside an `application/json` Observation’s `result`**, with typed `stamp`, `window`, `air`, `qc` and `probe` fields. These are **project-defined semantics in a declared SWE record**, not a claim that the outer standard Observation has native time-interval or quality semantics.

| Physical unit | Parallel archival-report DataStream ID | Archival-report Observation ID | Retrieved report’s exact source fields |
| --- | --- | --- | --- |
| Probe 4 | `c1870c01-4c61-43a2-ace5-14e86d317c36` | `a742b704-c2cd-4c1d-970a-b97b5f628130` | `air=29.1`, `window=[2024-04-15T16:45:00Z, 17:00:00Z]`, `qc="<0> "`, correct probe UID |
| Probe 3 | `8b8f9361-e2fa-4179-b1bb-947d3cd3d86d` | `50bf940e-55a0-45b6-9331-e6391704f6c7` | `air=27.3`, `window=[2024-04-18T16:45:00Z, 17:00:00Z]`, `qc="<0> "`, correct probe UID |

**Important: the four server Observation IDs describe only TWO distinct historical NOAA measurements.** Avoid double-counting in charts, analytics, source-to-UI tests or claims about dataset size. The original scalar Observation is still available for each measurement; the extra record is a parallel, more complete **representation**, not an additional physical measurement or separate station event. This duplication is intentionally provisional and needs an architecture decision before a final Profile.

The [archival-report loader](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/scripts/load-bennett-archival-report-csapi.py) verified returned field definitions, exact raw flag token including trailing space, and nominal interval, without modifying the scalar originals. [Successful server load/read-back run 41248245591](https://github.com/OS4CSAPI/glaux-client/actions/runs/41248245591). The live [Activity → Table](https://glaux-client.pages.dev/?page=resource-details-live-bennett) uses a [definition-driven decoder](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/src/profile/archival-report-context.ts), with [tests](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/tests/archival-report-context.test.ts) for rejected/missing QA, wrong observer and wrong averaging duration. [UI TypeScript/tests/build/deploy run 41248473107](https://github.com/OS4CSAPI/glaux-client/actions/runs/41248473107) passed; rendered production browser displayed the two report cards and qualified meanings. [Detailed bridge report](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/BENNETT_OBSERVATION_CONTEXT_BRIDGE.md).

**Do NOT write:** “the server supports interval-valued `Observation.phenomenonTime`,” “the timestamp is the measured `resultTime`,” “the source flag is an accepted `resultQuality` API member,” “fully conformant SWE JSON,” “live sensor reading,” or “complete provenance-preserving DIM/Profile interoperability.” None has been shown. **The server-required outer `resultTime` was assigned the source station stamp as a test surrogate**; the archive did not independently establish when the result became available. The interval belongs conceptually to the averaged phenomenon (OMS), but in this experiment it survives **as a separately labeled report field**.

### 3.6 The last standards/server investigation — why the work stopped

The [31 October observation-encoding decision record](Candidate_Specification/Observation_Encoding_Decision_31OCT2026.md) reviewed actual published CSAPI/SWE schemas and the preserved 198-page OMS 3.0 document, examined the pinned 52°North source, and performed **read-only** probes of the running service.

- **OMS 3.0 §8.2.3, Note 2 (printed p. 48):** the `phenomenonTime` of an average is the time interval of the measurements. **§8.2.4 (p. 49)** distinguishes `resultTime` as when the result became available. Original PDF is [preserved in connected Drive](Primary_Sources/OGC_20-082r4_OMS_3.0.0.md).
- **CSAPI Part 2 v1.0 `application/json` Observation schema:** `phenomenonTime` and `resultTime` reference `TimeInstant`, and `resultTime` is required in the representation. `parameters` is allowed with a corresponding stream schema, but **this 52°North decoder does not carry it through**. [Official schema](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observation.json).
- **SWE Common JSON:** CSAPI Part 2 has a separately defined `application/swe+json` observation format with `recordSchema` / `JSONEncoding`; SWE Common provides `TimeRange` and `Text`. But **having an extra `TimeRange` field alone does not prove it is mapped as the Observation’s normative `phenomenonTime`**. The exact mapping question remains for review/possible Standards Working Group clarification.
- **Deployed service behavior:** `.../observations?f=application%2Fswe%2Bjson` returned HTTP **200** and SWE media type, **but its body remained conventional JSON Observation objects**, while `.../schema?obsFormat=application%2Fswe%2Bjson&f=json` still returned `obsFormat:"application/json"` / `resultSchema`, not the SWE `recordSchema` and encoding. `f=swe%2Bjson` returned HTTP **400**. The service’s `conformance?f=json` advertised only OGC API Common core when checked. None establishes verified Part 2 SWE JSON conformance.
- **Pinned 52°North upstream source:** [`OMJsonSchemaParser`](https://github.com/52North/connected-systems-pygeoapi/blob/6ad75aa7fbfc76517c8a24c21446471845007855/connected-systems-api/provider/part2/formats/om_json_scalar.py) parses times with `datetime.fromisoformat` and omits `parameters`; [provider database code](https://github.com/52North/connected-systems-pygeoapi/blob/6ad75aa7fbfc76517c8a24c21446471845007855/connected-systems-api/provider/part2/part2.py) uses timestamp columns rather than native period storage. The deployed instance may have local adaptations; do not claim byte-for-byte identity with pinned upstream.

The latest assistant recommendation was **a read-only executable SWE JSON contract test** on the offline Bennett fixture, then possibly an **isolated** server implementation, plus separate normative time-mapping clarification. **This recommendation was NOT executed. It is NOT owner-approved.** Following that suggestion, the owner expressed dissatisfaction and requested this PITON instead. *This is the exact work boundary.*

## 4. What is actually proven? Six levels, not one success/failure label

| Layer | Grounded result | Not proven / cannot be silently inferred |
| --- | --- | --- |
| **Original historical evidence** | Two real selected NOAA/CDMO rows and a separately sourced equipment-use history support a bounded attribution | Exact swap minute, full operational station configuration, independent result-generation timestamp, current unit placement |
| **Offline profile interpretation** | Typed SWE-like candidate fields and reader pass bounded positives and negative controls | A compliant served CSAPI SWE JSON representation; universal client interpretation |
| **Actual live CSAPI storage** | Two real server-resident individual Systems, same model link, original scalar temperature Observations; round-trip successful | Server produced the data from physical sensors in real time; correct station/host/Deployment graph; broad conformance |
| **Data/context preservation** | Parallel DataRecord report results read back exact nominal averaging windows and raw QA flags | Native interval-valued `phenomenonTime`, true `resultTime`, preserved `Observation.parameters`, a final Profile rule |
| **Deployed Glaux UI** | Live HTTP GET, Resource Details placement, Codex map reuse, source-qualified Activity cards; successful CI and browser checks | Fully generic Profile-driven discovery/interpretation or final Resource Details UX |
| **DIM/Profile and donor synthesis** | Candidate concepts, donor comparisons, evidence-backed worked subsections | Final chassis/scope, complete DIM/Profile, exhaustive donor fairness, comprehensive cross-vendor actual equipment datasets, broad source-to-CSAPI interoperability |

**This distinction is essential:** “the workflow passed” means a workflow passed its specified checks, not that the scientific/domain goal was met. “Live” means HTTP retrieval from our active server, **not** current hardware telemetry. “Real” describes the provenance of the historical source readings and operator history, **not** every synthetic or project-authored resource in the experiment.

## 5. Important unresolved design choices and technical debt

These are reasons to review the strategy, **not** instructions to launch parallel implementation campaigns.

1. **Station-led versus probe-led DataStream:** Offline one station summary stream with per-record probe attribution versus live probe-owned scalar streams plus duplicate archival-report streams. Decide source/observer/reporter roles before promoting either pattern to Profile.
2. **True measurement period and independent result availability:** The native CSAPI JSON time members and 52°North storage cannot truthfully carry the source-average interval as `phenomenonTime` on the tested path; the source itself lacks an independently verified `resultTime`. Do not invent either.
3. **Per-observation QA:** Standard permits `parameters` with `parametersSchema`, but tested server drops that field; current bridge keeps operator QA inside `result` instead. Do not generalize `qc` into sensor health, an OMS-native quality property or a universal field name.
4. **Resource graph is incomplete:** No published Bennett **station/host System**, **Deployment** records, or independently supported geometry. Server’s exposed documented operations and storage capabilities need separate investigation before assuming `Deployment` writes are possible.
5. **Model is project-authored:** Static `typeOf.href` fixture is not Campbell’s authoritative SensorML datasheet or a server-managed `Procedure` with tested CSAPI lookup; it demonstrates a distinction, not a completed interoperability solution.
6. **Prototype is manually curated:** Bennett live page enumerates two known System IDs and two stream IDs in its code. Some comparison views preserve fixtures and manual attribution; unit data may have fallback fields. A general machine-readable Profile discovery and parser are **not** established.
7. **Observation duplication risk:** Counts, charts or client views that combine scalar and archival-report streams must de-duplicate or explicitly separate two representations of the same historical measurement. There has not been a standards/architecture decision that endorses this split.
8. **Tab allocations remain partly candidate:** Overview is a summary; Activity carries observations/QA; Equipment carries identities; Map only evidenced positions. Ambiguous DataStream versus Communications, Condition versus Configuration and Deployment presentation remain unresolved in the candidate matrix.
9. **Real-system corpus remains too thin:** Bennett provides one compelling real historical probe-swap link; the earlier A/C/D sheets remain published reference/example material. Neither equals a comprehensive, varied cross-vendor test set for a whole-system DIM.
10. **Donor challenge framing and architecture bias are not solved by more code:** The owner’s donor-fairness objection survives every successful experiment. Strong semantic claims require renewed **actual original-source** comparison, not just convenient vocabulary mappings.
11. **Research and production branches diverge:** A simplistic early Bennett standalone experiment was also written on the research branch (`public/fixtures/bennetts-point-attribution.json`, `src/presentation/observation-attribution.ts`, `src/main.ts`) **separately from the application’s production route**. It was not the live solution; **do not merge blindly**. Compare branches by file and preserve the actual deployed application code.
12. **Loader and fixture quality:** The initial loader originally submitted local IDs that the server normalized/assigned differently, then adjusted to discover by stable UID. It also has an awkward Probe 3 serial correction in the loader source; the *verified deployed value* is `21281600077814`. Treat such test scaffolding as revisitable, not Profile authority.

## 6. Where each artifact lives — avoid cross-branch false links

### Canonical research (`research/dim-profile-v2`)

- [Research home](README.md), [previous PITON v1.8](PITON_DIM_Profile_V2_Continuity_v1.8_30OCT2026.md), [AI drift corrective case](DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md).
- [Problem and outcome baseline](DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md), [candidate DIM v0.2](Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md), [concept/donor comparison](Concept_Donor_Comparison/README.md), [donor-first view](Concept_Donor_Comparison/Donor_Contributions.md), [equipment evidence view](Concept_Donor_Comparison/Equipment_Evidence.md).
- [New candidate DIM](Candidate_Specification/DIM.md), [candidate CSAPI Profile](Candidate_Specification/CSAPI_Profile.md), [donor side-by-side terms](Concept_Donor_Comparison/Donor_Terms_Side_by_Side.md).
- [Bennett source evidence](Candidate_Specification/examples/bennetts-point-ee181.json), [offline wire example](Candidate_Specification/examples/bennetts-point-wire/README.md), [offline reader](Candidate_Specification/examples/bennetts-point-wire/check.py).
- [Candidate Resource Details placement matrix](Candidate_Specification/Resource_Details_Placement_Matrix.md), [latest standards/encoding review](Candidate_Specification/Observation_Encoding_Decision_31OCT2026.md).
- [OMS original-document recovery index](Primary_Sources/OGC_20-082r4_OMS_3.0.0.md): original **198-page PDF in connected Drive** (file ID `1QNBXosCb_TcSP96tppQAyLv42WdnU7G2`) and page-marked extracted text (ID `10B6djSL1kCDFSZ_vJipx5h_kpNZ8wSPW`), with recorded checksums. The PDF is **not** stored as GitHub binary. Its §§8.2.3–4 were revisited directly in the 31-Oct observation review; this does **not** mean every old OMS donor alignment was comprehensively re-audited.

### Live app/deployment (`work/details-view-20261023`)

- [Resource Details template](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/RESOURCE_DETAILS_TEMPLATE.md), [original mapping notes](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/DETAILS_VIEW_MAPPING.md), [profile experiment notes](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/RESOURCE_DETAILS_PROFILE_TEST.md).
- [Bennett live client](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/src/presentation/resource-details-live-bennett.ts), [generic live client](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/src/presentation/resource-details-live-csapi.ts), [historical profile test](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/src/presentation/resource-details-profile-test.ts), [shared map renderer](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/src/presentation/resource-details-map.ts).
- [Historical prepared Bennett fixture](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/src/profile/bennetts-point.ts), [source-quality/interval decoder](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/src/profile/archival-report-context.ts), [decoder tests](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/tests/archival-report-context.test.ts), [model fixture](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/public/fixtures/bennetts-point-ee181-model.sml.json).
- [Original server loader](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/scripts/load-bennett-v2-csapi.py), [parallel archival-report loader](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/scripts/load-bennett-archival-report-csapi.py), [load workflow](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/.github/workflows/load-bennett-v2-csapi.yml) and its [trigger](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Plans/BENNETT_LIVE_LOAD_TRIGGER.md).
- [Preservation bridge interpretation + verification](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/BENNETT_OBSERVATION_CONTEXT_BRIDGE.md), [Codex map original design](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/RESOURCE_DETAILS_LIVE_MAP.md), [Bennett map integration](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/BENNETT_LIVE_MAP_INTEGRATION.md).
- [Explicit production Pages workflow](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/.github/workflows/deploy-glaux-pages.yml), [deployment trigger](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Plans/GLAUX_DEPLOY_TRIGGER.md). This Cloudflare Pages project has **direct** deployment via GitHub Action; committing ordinary files does not itself publish to production.

### Which live page is which

| URL / page key | Source of displayed information | Standing |
| --- | --- | --- |
| [`resource-details-profile-test&case=bennetts-point`](https://glaux-client.pages.dev/?page=resource-details-profile-test&case=bennetts-point) | Prepared historical fixture with real source values and separately prepared attribution | **Not** live CSAPI case fetching |
| [`resource-details-live-csapi`](https://glaux-client.pages.dev/?page=resource-details-live-csapi) | Live generic selected System + related server resources | Demonstrates generic HTTP retrieval, not final Profile |
| [`resource-details-live-map`](https://glaux-client.pages.dev/?page=resource-details-live-map) | Codex's independent Map experiment on live System `position` | Shared renderer; original route preserved |
| [`resource-details-live-bennett`](https://glaux-client.pages.dev/?page=resource-details-live-bennett) | Actual server Systems, scalar and archival-report Observations; bounded curated IDs | **Live read-back of historical data**, qualified UI presentation |
| [`resource-details-smart-citizen`](https://glaux-client.pages.dev/?page=resource-details-smart-citizen) | Earlier manufacturer-design research walkthrough | Historical, **not** proof of a physical individual or CSAPI conformance |

### Executed GitHub Actions — do not invent success

| What was checked | Verified successful workflow |
| --- | --- |
| First Bennett historical case deployment | [41226683585](https://github.com/OS4CSAPI/glaux-client/actions/runs/41226683585) |
| Reallocated Bennett facts into correct tabs | [41230836115](https://github.com/OS4CSAPI/glaux-client/actions/runs/41230836115) |
| Generic live 52°North CSAPI page | [41231346909](https://github.com/OS4CSAPI/glaux-client/actions/runs/41231346909) |
| Two physical Systems + scalar observations round-trip | [41232435599](https://github.com/OS4CSAPI/glaux-client/actions/runs/41232435599) |
| Dedicated live Bennett page deployment | [41232545716](https://github.com/OS4CSAPI/glaux-client/actions/runs/41232545716) |
| Shared Codex map reused in Bennett page | [41247110981](https://github.com/OS4CSAPI/glaux-client/actions/runs/41247110981) |
| Additional report streams, exact QA and window read-back | [41248245591](https://github.com/OS4CSAPI/glaux-client/actions/runs/41248245591) |
| Latest source-quality/interval UI deployment | [41248473107](https://github.com/OS4CSAPI/glaux-client/actions/runs/41248473107), **source revision `54b4e576472d89d4dbb3e67fdce0733c8bb84926`** |

These runs were rechecked as **completed/success** on 31 October. Later documentation commits to either branch are **not application deployments**. New chats should recheck the live branch/Actions when claiming present deployment state.

## 7. Important original-source and authority rules

1. **Actual standards text controls claims**, not summaries, metadata, an impressive number of donor artifacts, or a self-review. A living GitHub implementation is primary evidence for its **own code and server behavior**, not automatically a normative OGC requirement.
2. **Complete OMS is available.** [Recovery index](Primary_Sources/OGC_20-082r4_OMS_3.0.0.md) holds exact Drive IDs, hashes and instructions. Read the actual original before asserting an OMS interpretation. Saving it did not retroactively validate all historical alignment.
3. **IEEE 1451 is not “unavailable.”** Public NIST material and a 1451 Playground were identified and used for technical study. Do not ignore them or pretend uninspected edition-specific normative requirements were verified. [Corrected source trail](Donor_Challenge/03_IEEE1451_Challenge.md).
4. **SAPIENT v2, ISA, The Open Group SOSA, W3C Web of Things, OPC UA Devices, PA-DIM, SOSA/SSN, AAS, SAREF and others** contribute on their native terms and with distinct editions/source authority. [Donor coverage](Concept_Donor_Comparison/Donor_Contributions.md), [original source registers](Donor_Challenge/04_Other_Structural_Challenges.md) preserve what was actually inspected and what was deferred.
5. **Part 1/Part 2 CSAPI, SensorML 3.0, SWE Common 3.0 and OGC API – Features** are foundational carriers, not automatic proof of a vendor mapping. Published OGC normative text and schemas prevail over convenience/example code.
6. **No manufactured empirical evidence.** A fixture may use real published values while other labels/UIDs/links are authored by the project. Source-original data, calculated conversions, mappings, mock fixtures, server-created resources and present telemetry are different provenance categories.
7. **Preserve donor equality:** late donors may change/split/replace early candidate meanings. No default root, power-first module, predetermined chassis or required new “next concept.”
8. **Academic output:** spell out acronyms at first use, cite original editions/clauses precisely (Chicago Manual of Style, 18th edition, where requested), and identify project synthesis versus source requirements. Do not invent complete normative mappings or references.

## 8. How to recover safely in a fresh chat

**First: read, verify, and explain. Do not automatically execute an old proposed step.**

1. **Read this PITON**, then its predecessor [v1.8](PITON_DIM_Profile_V2_Continuity_v1.8_30OCT2026.md) for the longer donor-corpus/equipment history. Read the [owner drift correction](DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md) before making model-priority recommendations.
2. **Read current [research README](README.md)** and verify branch HEADs. Use GitHub `fetch_file(repository_full_name="OS4CSAPI/glaux-client", path, ref="research/dim-profile-v2")` for research and `ref="work/details-view-20261023"` for application. Default-branch code search is not a safe substitute for reading these non-default branches.
3. For **why the project exists** and donor fairness, read the [purpose baseline](DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md), [research story](DIM_Profile_V2_Research_Story_and_Current_Position_v0.1_29OCT2026.md), [comparison](Concept_Donor_Comparison/README.md) and its source trail.
4. For **the latest concrete worked example**, read [Bennett source evidence](Candidate_Specification/examples/bennetts-point-ee181.json), the [offline SWE example](Candidate_Specification/examples/bennetts-point-wire/README.md), [31-Oct encoding decision](Candidate_Specification/Observation_Encoding_Decision_31OCT2026.md), and the [live bridge/verification report](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/BENNETT_OBSERVATION_CONTEXT_BRIDGE.md). Examine code only for the actual step being requested.
5. If the task is to **inspect the live page**, verify its current deployment workflow and current HTTP/browser results. If production must be changed, use the documented `work/details-view-20261023` branch and its **explicit deployment-trigger mechanism**; never assume code commits auto-publish. Do not write to the live server while merely recovering state.
6. **Do not merge branches blindly.** The research branch is not the deployed app and carries an earlier independent Bennett rendering experiment. Do not replace the production page with the research prototype. Preserve Codex's reusable map code.
7. **Use one bounded prompt-sized step per “proceed”** only after a current task and plan are actually agreed. Avoid gratuitous approval layers inside approved work, but do not promote a previous assistant's recommended test into a new mandate. Explain: **what changed, why it matters to the actual DIM/Profile/client goal, what is not proved, and one meaningful next choice**.
8. **Communicate in plain language first.** The owner rejects unnecessarily jargon-heavy “AI for AI” output, forced domain labels, unexplained tables, wandering plans, and spurious “completed” claims. Prefer short paragraphs (five sentences or fewer), source-grounded figures when genuinely useful, GitHub links rather than unsolicited ZIP bundles, and end each authorized iteration with what is next so “proceed” is enough.

### Recovery-only opening prompt — ready to paste

> Recover the MERLIN DIM / OGC API – Connected Systems Profile V2 project from PITON v1.9 dated 31 October 2026 in `OS4CSAPI/glaux-client`, research branch `research/dim-profile-v2`, path `Docs/Research/DIM_Profile_V2/PITON_DIM_Profile_V2_Continuity_v1.9_31OCT2026.md`. Read the previous v1.8 for donor/equipment history, the owner-requested AI-drift correction, and the latest Observation Encoding Decision. Check the `work/details-view-20261023` branch separately for the actual live Glaux Bennett's Point code and verified server loaders. Explain in normal language what we have achieved, what remains experimental, which parts of the current server encoding are workarounds, and which decisions are open. The owner said the latest direction “stinks” and then requested this PITON; **do not automatically build the proposed SWE JSON test, start a donor campaign, change the server, change the UI, or adopt a Profile rule. Stop at recovery and ask for direction only after reporting state.**

## 9. What is actually next? **No automatic step**

The immediately prior assistant **proposed** a read-only SWE JSON contract test and eventual isolated server implementation. That suggestion is fully recorded in the [31-Oct decision paper](Candidate_Specification/Observation_Encoding_Decision_31OCT2026.md). **It is not the approved project path simply because it appears last in the chronology.**

Other legitimate questions remain at a broader level: whether the Bennett **station-led or probe-led reporting model** is right; how to return to **vendor-neutral whole-System DIM/Profile work** and fair donor coverage; whether a stronger complete cross-vendor dataset should be obtained; and how to limit server-specific workaround investment. These are **alternatives for the owner to decide among**, not an assistant-created multi-step plan. The most useful next conversation may be a strategic re-evaluation of what value the last experiment produced and why the owner is dissatisfied, before any more coding.

**Handoff rule:** finish this PITON, link it in the research home and in the application branch's continuity pointer, verify both writes, then **stop**. If the next user message says “proceed” in a fresh chat without a mutually established scope, explain the available nearest meaningful next step from the recovered state rather than blindly executing the old last proposal.
