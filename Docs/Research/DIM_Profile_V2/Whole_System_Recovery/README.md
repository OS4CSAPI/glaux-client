# Whole-System DIM/Profile V2 — Working Workbook

**Step 01 baseline · 31 October 2026 · Read this first**

**Status:** Initial project/evidence baseline **verified and recorded**. No new Domain Information Model (DIM) class, OGC API – Connected Systems (CSAPI) Profile requirement, data transformation, or client behavior is adopted here. This workbook is the **cumulative, human-readable working area** for the [43-step plan](../PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md), not another independent research campaign.

## 1. What we are trying to build

Imagine opening the same Resource Details view for two very different sensing systems. One has a single cabled probe producing temperature and humidity; another has numerous internal sensing modules; another has a separate logger and weather sensor; yet another replaced a physical temperature probe halfway through its historical record.

A good client must recognize **what the equipment is, what it can do, what it actually did, how the pieces relate, and how much the source really establishes**. It must make those facts understandable without needing new, hard-coded presentation rules for each manufacturer. At the same time, it must not pretend that an advertised option is installed, a device manual is an actual unit record, a logger is necessarily the sensing element, or an old observation is today's equipment condition.

The intended outputs remain **three different things**:

- **DIM:** a defensible, *implementation-independent* set of common meanings and relationships for the whole sensing System, with appropriate specializations and explicit limits.
- **CSAPI application Profile:** a separate, testable way for producers to communicate those justified meanings through existing CSAPI, Sensor Model Language (SensorML), SWE Common, and other appropriate standard structures.
- **Glaux proof:** the **same meaning-aware reading path** interprets more than one independently documented equipment arrangement, then displays useful and correctly qualified information in the existing Resource Details UI.

**The project can be successful within a stated scope without claiming all vendors, all 182 source artifacts, or adoption as an OGC standard.** The final scope and overarching domain/chassis name remain research questions, not decisions made by this workbook.

## 2. Starting evidence: four cases with different standing

The cases below are **starting evidence**, not completed cross-case comparisons or proven installations. Their detailed source fact audit and content-area reconciliation belong to **Step 03**; their source-native system reconstructions belong to **Steps 05–08**.

| Starting case | Why it helps challenge a common model | What the current source actually supports |
| --- | --- | --- |
| [Dragino S31-LB](../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md) | A cabled external probe, two measured properties, node, battery, LoRaWAN and documented settings | Manufacturer reference design and published message examples; **no authenticated individual installation or present settings** |
| [AirGradient Open Air Max](../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md) | A more complex assembly of boards, sensors, communications and reporting roles | Documented product arrangement and source examples; **not a verified fielded unit or joined configuration/history** |
| [Campbell CR1000X + first-generation ClimaVue 50](../Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md) | The sensing assembly and the logger/reporting equipment have distinct jobs | Documented reference pairing and separate publisher examples; **the examples are not evidence of one complete running installation** |
| [Bennett’s Point (ACE Basin)](../Candidate_Specification/examples/bennetts-point-ee181.json) | A real historical measurement record and dated replacement of two individually identifiable EE181 probes | **Two source-published historical temperature measurements** and separate operator equipment-use history, joined by a project attribution; **not** complete station configuration, current telemetry or a verified CSAPI Deployment graph |

**One concrete question that still matters:** At Bennett’s Point, the physical probe senses the air; station equipment logs an average. Our [offline representation](../Candidate_Specification/examples/bennetts-point-wire/README.md) is station-oriented, while the [live 52°North experiment](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/BENNETT_OBSERVATION_CONTEXT_BRIDGE.md) uses probe-owned DataStreams plus parallel archival report streams. That difference is an **unresolved modeling/representation choice**, not evidence that one approach is universally correct. The source CSV itself does **not** identify a probe serial; the association comes from separate equipment history.

**Historical context only:** TRSS and OmniSense motivated the original problem, but their preserved examples are not compulsory experimental anchors and include synthetic/unverified cases. Smart Citizen Kit 2.3 remains valuable product-design research; it does not establish an authenticated physical kit.

## 3. Verified starting state — what already works

This is a **31 October repository/Actions snapshot**, not a new audit of all original standards or a test of every current UI behavior.

| Working evidence | What we can legitimately say |
| --- | --- |
| [Candidate foundation v0.2](../Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md), [donor comparisons](../Concept_Donor_Comparison/README.md) and [candidate DIM](../Candidate_Specification/DIM.md) | Substantive candidate distinctions exist among individual units, models/kinds, physical and functional roles, methods/activities and digital representations. **No completed whole-System DIM or final chassis is established.** |
| [Candidate CSAPI Profile](../Candidate_Specification/CSAPI_Profile.md) and [Resource Details placement matrix](../Candidate_Specification/Resource_Details_Placement_Matrix.md) | We have proposed source-qualified bindings and ways to organize facts. **They are not final requirements or universally validated UI placements.** |
| [Controlled evidence handoff](../Controlled_Corpus/08_Frozen_Corpus_Manifest_and_Handoff.md) | The old **12/12**, **6/6**, **8/8**, and **4/4** research plans are *closed in their own bounded scope*. The selected equipment sheets are documentary/example evidence, **not real deployment histories**. |
| [Live Bennett experiment](https://glaux-client.pages.dev/?page=resource-details-live-bennett), [server round-trip result](https://github.com/OS4CSAPI/glaux-client/actions/runs/41248245591), [Glaux deployment](https://github.com/OS4CSAPI/glaux-client/actions/runs/41248473107) | Prior read-back and deployment workflows **passed**. The server holds two historical temperature measurements represented using original scalar observations and separate archival-context observations. Glaux retrieves selected records by actual HTTP requests. |
| [Bennett app code](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/src/presentation/resource-details-live-bennett.ts), [candidate interpretation rules](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/src/profile/resource-details-proof.ts) | Case IDs and term rules are still partly **manually prepared**. This is **not** a verified general Profile-driven reader for diverse real deployments. |

**Baseline repository heads verified before Step 01 documentation changes:**

- Research `research/dim-profile-v2`: `25f0c4747285e46d9b6975ff7fd078f4a1ec09a8`.
- Application `work/details-view-20261023`: `61601169619282220525b9fd41a5d0ae203b0625`.

The application branch contains the production code; the research branch contains this workbook and candidate papers. Do **not** merge them blindly or mistake documentation commits for a Cloudflare deployment.

## 4. What we have NOT proved — and must keep visible

**No common reader yet.** Existing experiments include particular rendering paths and manually authored terms. Passing a demo does not mean we can interpret another independently described System without new vendor/case code.

**No integrated, accepted whole-System DIM yet.** The first five conceptual meanings are promising but are not mandatory classes. Earlier source selection was not fully neutral; later donors may introduce, split, combine or replace those distinctions. The [corrective drift study](../DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md) prohibits automatically choosing power/“operational condition” or any other unearned priority.

**No comprehensive, equivalent real dataset for all cases.** A reference design is useful for testing design-time semantics but cannot establish an installed component, selected setting, current condition or actual command outcome.

**No fully solved Bennett time/quality/Profile encoding.** The [31-October observation-encoding review](../Candidate_Specification/Observation_Encoding_Decision_31OCT2026.md) documents real server limitations. The preserved 15-minute window and original NOAA QA token are additional **archival report context**, not native interval-valued `phenomenonTime` or a certified source `resultTime`. **Two distinct measurements are represented by four server Observation resources.** No physical installation geometry was inferred.

**No assumed donor equality or conformance.** The research corpus contains 182 *artifacts*, not 182 independently assessed standards. The [donor-first review](../Concept_Donor_Comparison/Donor_Contributions.md) records incomplete and uneven coverage. The original source documents govern actual definitions; a mapping asserted by this project is not a donor-standard requirement.

## 5. How we will tell whether we are getting closer

The central question is **whether the same source-grounded meanings can explain multiple real differences and can be carried through to one reusable client without losing the important qualifications**. A narrower successful test (for example, preserving a QA token in one server) is useful evidence but does not answer that whole question.

**The future comparison must trace** original source information → justified DIM meaning → proposed Profile/CSAPI representation → shared client interpretation → explicit fidelity result. When a fact is unavailable, the client must say so rather than fill it in. If an implementation cannot carry a meaning correctly, identify whether it is a source-data, model, Profile-binding, server or client limitation, rather than calling all failures the same thing.

**Important boundary:** This is the *project re-anchor*, **not Step 02's formal scoring or pass/fail rubric**. The success rubric, evidence classifications and missing-field treatment are the sole subject of the next prompt.

## 6. Exact next step

**Step 01 — COMPLETE:** We verified both GitHub branches, the documentary and live-experiment baselines, the current candidate material, and the known evidence limitations; this initial workbook now exists. No DIM/Profile content, app code, CSAPI server data or production deployment was changed.

**Step 02 — NEXT on “proceed”:** Add a small, reusable **source → DIM → Profile → client → fidelity** acceptance rubric *to this workbook*, with the agreed evidence labels, missing-information handling, and at least one concrete positive/negative example. This becomes the common yardstick for every later equipment comparison and implementation step.

**Plan status:** [Step tracker](../PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md) controls execution. Earlier closed research plans remain closed. For safe recovery read [PITON v2.0](../PITON_DIM_Profile_V2_Continuity_v2.0_31OCT2026.md) and, where needed, its [v1.9 evidence handoff](../PITON_DIM_Profile_V2_Continuity_v1.9_31OCT2026.md).
