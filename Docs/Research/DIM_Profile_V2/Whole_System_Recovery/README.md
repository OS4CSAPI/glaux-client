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

## 5. Step 02 — How we will judge whether meaning survives

**Status: Step 02 COMPLETE, 31 October 2026.** This is a common testing method, **not** a new DIM class, an adopted Profile rule, or an executed cross-vendor test. It answers one human question: *Can the same client accurately understand what two different equipment sources mean, or does information become lost, invented, or confused along the way?*

For example, if a manufacturer says **one external probe measures temperature and humidity**, it would be wrong for our client to show **two installed probes** simply because two outputs exist. Our rubric must identify the original fact, the intended common meaning, how we encoded it, what the client actually displayed, and **where an error first appeared**.

### 5.1 Five questions for every claim or relationship

| Question | What we must write down |
| --- | --- |
| **1. Source: What was actually established?** | Original source wording, link/edition/locator, value and units if relevant, **which subject** the fact concerns, its time and scope, and its evidence standing. Do not silently replace manufacturer terminology with ours. |
| **2. DIM: What does it mean beyond that manufacturer?** | Proposed source-neutral meaning and relationships, original donor support and exact qualifiers. State **fits / needs revision / unresolved**; do not force new material into the existing five candidate headings. |
| **3. Profile/producer: How can it be communicated?** | Relevant CSAPI/SensorML/SWE Common resource, field, link or vocabulary, with the standard’s actual authority versus our proposed binding identified. Record **actual encoded output** if produced; otherwise mark **not tested**. |
| **4. Client: What did Glaux really understand and show?** | Actual interpreted subject/relationship, visible text, source/uncertainty qualifiers and raw fields. Disclose any **vendor-name or case-ID-specific rule** instead of claiming a common interpreter. |
| **5. Fidelity: Did the meaning survive?** | Compare source against actual encoded and displayed results; assign the result below, identify the **first demonstrated loss/misstatement point**, and link the evidence. A build passing is not enough. |

**Minimum reusable test record:** case; source document/locator and native claim; evidence category; subject, time and applicability; candidate DIM meaning with rationale; proposed Profile binding; actual produced CSAPI record (or “not produced”); actual shared Glaux output (or “not run”); fidelity result; first supportable fault location; source/implementation/test links. Make one comparison per independently testable **fact or relationship**, not one per pretty UI card. Retain different representations of the *same* observation as one underlying source event, not different measurements.

### 5.2 Two separate classifications — *what kind of evidence* versus *did it work*

The project’s evidence labels from the [plan](../PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md) are attached **to individual claims**, not indiscriminately to an entire device or standard. A report can contain source-backed product-design information, project calculations and a later successful software test at the same time.

| Evidence label | What it means — and does not mean |
| --- | --- |
| `SOURCE_FACT` | Explicitly supported source information **within its actual scope**. A manufacturer’s design claim is a fact *about the design*, not a verified field installation. |
| `SOURCE_EXAMPLE` | A source-published sample/record, **not** evidence that our selected hardware actually emitted it. Preserve its publication context. |
| `DERIVED` | A reproducible calculation or join made by this project from named source inputs; for example, Bennett’s Point UTC conversion or equipment-history attribution. Do not say the CSV supplied the serial. |
| `CANDIDATE_MAPPING` | Our interpretation or proposed DIM/Profile correspondence, **not** an adopted donor or OGC requirement. |
| `VERIFIED_RUNTIME` | An actual, versioned software/server test with recorded input, output and assertion. It proves only those assertions, not source authenticity or universal interoperability. |
| `UNKNOWN` | The source did not establish the fact or its applicability. Keep it unknown; **not zero, false, absent hardware, or a current status value**. |
| `REJECTED_EQUIVALENCE` | A source-grounded bad identification explicitly ruled out; e.g., **two measured properties ≠ two physical probes**. Useful for negative tests. |

**Fidelity result** is independently assigned *after* comparing inputs and outputs:

| Result | Exact use |
| --- | --- |
| **PRESERVED** | Executed check confirms source subject, value/meaning, relationship and qualifiers remain correct. |
| **PRESERVED WITH QUALIFICATION** | Meaning survives, explicitly identified as, for example, **documented capability** or **historical report**, not installed state or current telemetry. |
| **SOURCE UNAVAILABLE / NOT ASSERTED** | No source evidence for that requested fact. Correctly saying “unknown” is **not** an integration failure. |
| **NOT TESTED** | One or more required model/producer/client stages haven’t actually been exercised; documentation or a plausible mapping is not a pass. |
| **LOST / OMITTED** | The source-established fact disappears from an inspected later stage where our defined test expected it. Cite both sides. |
| **MISREPRESENTED** | A later stage invents, changes, merges or overstates source subject, identity, state, meaning, time, unit or relationship. **Hard failure**, however attractive the page. |
| **CONFLICT / UNRESOLVED** | Source claims conflict or sound competing meanings/bindings remain unsettled. Show alternatives, not fake completion. |

**Do not compute a success percentage yet.** Counts of PASS in old research plans, records returned by a server and display cards are not a shared denominator for source-to-client meaning.

### 5.3 Diagnose the earliest supported problem, not the most visible symptom

| Where the problem begins | What to check |
| --- | --- |
| **Source/evidence gap** | Was this fact ever documented for this subject, time and product version? If no, use `UNKNOWN`, not “lost in CSAPI.” |
| **DIM meaning gap** | Does our model collapse distinct physical components, functions, channels, observer/reporting roles, settings or events? |
| **Profile/binding gap** | Is the DIM distinction clear, but the specified standards carrier, semantic definition or required link wrong, unjustified or missing? |
| **Producer/adapter loss** | Was a source-backed meaning dropped or changed while producing the CSAPI representation? |
| **API/server/format loss** | Did a correct submitted value fail the actual API round trip because of this implementation or encoding? Record endpoint and response. |
| **Shared reader/UI error** | Was the correct meaning retrieved but misinterpreted, put in the wrong view or presented as a stronger claim? |
| **Cannot localize yet** | We lack adjacent before/after artifacts. Record the needed comparison; **do not guess the cause**. |

An error may appear in Glaux but originate earlier. More than one problem may exist. The aim is to fix **the first justified cause**, not patch the screen until it looks convincing.

### 5.4 Concrete positive and negative examples — Dragino external probe

The [Dragino S31-LB source sheet, C-I01–C-I03, C-I08 and C-I10](../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md) documents the manufacturer’s **reference design**: one cabled external **SHT31 temperature/humidity probe** and the two supported measurement properties. The sheet explicitly has **no authenticated physical unit or current telemetry**. So the source supports a product-design fact—not a claim that any specific unit is deployed or taking a reading.

**Positive scenario (NOT YET EXECUTED):** one common set of DIM/Profile meanings communicates **one physical sensing component** with **two supported measured properties/outputs**. Without a manufacturer-specific rule, Glaux shows one *documented* probe arrangement and two *supported* outputs, clearly qualified as reference design. If this succeeds with a second independently documented, different system using the **same interpretation path**, the specific design-level relation can earn **PRESERVED WITH QUALIFICATION**. Today it is **NOT TESTED**.

**Negative scenario (would be MISREPRESENTED):** a client turns the two outputs into **two separately installed probes**, or shows a present temperature reading simply because the product manual says temperature is supported. Both would exceed the source evidence. If the produced CSAPI resource already invents the second probe, the fault starts in the **producer** (or earlier model/binding); if the representation correctly describes one probe and the client renders two, the fault is in the **reader/UI**. If the DIM *requires* one physical sensor per output, that is the **DIM's error**. This is a `REJECTED_EQUIVALENCE` test, not a newly invented standard rule.

**Existing historical counterexample (not a new test):** [Bennett’s Point](../Candidate_Specification/examples/bennetts-point-ee181.json) contains **two real historical temperature measurements** while the [current preservation experiment](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/BENNETT_OBSERVATION_CONTEXT_BRIDGE.md) has four server Observation resources: two original scalar records and two richer representations. A client showing **four physical measurements** would be **MISREPRESENTED**. A client that shows all four as explicitly labeled *resources* might preserve raw source transparency, but has **not automatically proved general, source-neutral deduplication**. Prior round-trip tests cover specific data preservation, not broad interoperability.

### 5.5 Later success requires cross-case interpretation, not merely a successful endpoint

Within a bounded case, report what actually passed **at its evidence level**, and what remains unknown or untested. A source design can test *design-level meanings*; it cannot prove installed state, executed control or current condition. A server response can prove a response was returned, but not the underlying historical truth of a manufacturer/field record.

For the plan’s eventual cross-vendor proof, require at least **two meaningfully different, independently documented arrangements** processed through **one common interpretation**, without vendor- or case-ID-dependent meaning rules. The same interpretation must preserve important differences and unknowns instead of filling gaps with plausible but invented facts. Bennett’s Point is a candidate *separate historical-unit/time test*, not equivalent to all the model-level cases.

**Outcome of Step 02:** We have defined a falsifiable testing method, but **no new Profile conformance result, software test, model choice or cross-vendor PASS**. Case-source coverage and permissible evidence claims will be reconciled in Step 03.

## 6. Current step and handoff

**Step 01 — COMPLETE:** Branches, goal and evidence limitations documented in §§1–4.

**Step 02 — COMPLETE:** Five-question source→DIM→Profile→client→fidelity rubric, original evidence labels, outcome rules, fault diagnosis and example recorded in §5. **No production or client changes.**

**Step 03 — NEXT on “proceed”:** Reconcile the original sources, versions and exact available whole-System information areas for **Dragino, AirGradient, Campbell and Bennett’s Point**, with known gaps and evidence standing. Add a readable case coverage comparison **to this workbook**. Do not yet perform the full system-by-system reconstructions planned for Steps 05–08.

**Plan status:** [43-step tracker](../PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md) records 2/43 complete. For recovery use [PITON v2.0](../PITON_DIM_Profile_V2_Continuity_v2.0_31OCT2026.md) and [v1.9](../PITON_DIM_Profile_V2_Continuity_v1.9_31OCT2026.md). No new server writes, code changes, deploys or standards decisions were made.
