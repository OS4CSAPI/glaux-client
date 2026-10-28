# PITON C — DIM/Profile V2 Case Study 01: Completion, Gate D, and Post-Case Continuity

**Date:** 28 October 2026  
**Version:** 0.1  
**Standing:** **AUTHORITATIVE CASE-STUDY RECOVERY CHECKPOINT AT THE END OF I13**, subject to newer verified README/plan status if later changed. **The complete I01–I13 research sequence is finished. No I14 exists.**  
**Project:** Version 2 of the Domain Information Model (DIM) and eventual OGC API – Connected Systems (CSAPI) application profile. This case study is a **bounded research test**, not the project-wide final DIM.  
**Repository:** [OS4CSAPI/glaux-client](https://github.com/OS4CSAPI/glaux-client)  
**ONLY working branch:** **research/dim-profile-v2** — **DO NOT use main by default**.  
**Case folder:** **Docs/Research/DIM_Profile_V2/Case_Studies/Real_Equipment_DIM_Validation/**  
**Primary result:** [I13 Integrated Smart Citizen Case Study and Gate D Decision](I13_Integrated_Smart_Citizen_Case_Study_and_Gate_D_v0.1_28OCT2026.md).  
**Phase D challenge:** [I12 Critical Interoperability Challenge](I12_Critical_Interoperability_Challenge_v0.1_28OCT2026.md), which explicitly corrects/qualifies [I11 OGC Accommodation](I11_CSAPI_OGC_Accommodation_v0.1_28OCT2026.md).

> **NEW-CHAT RESTART — do not recover this effort from memory alone.** Fetch the **current** [case README](README.md) and [13-iteration plan](PLAN_13_ITERATIONS_v0.1_27OCT2026.md) directly from **research/dim-profile-v2**, then **read [I13 integrated report](I13_Integrated_Smart_Citizen_Case_Study_and_Gate_D_v0.1_28OCT2026.md)**, **[I12 correction/challenge](I12_Critical_Interoperability_Challenge_v0.1_28OCT2026.md)** and the source studies listed below as necessary. **Do not reopen I13 or mistake the older PITON A/B progress checkpoints for current status.** If a later README/plan has been verified and supersedes this PITON's historical status, its live progress is controlling. A user **“proceed”** after this PITON authorizes **only the post-case-study research decision checkpoint described in § 8**, not a fictitious I14, spontaneous implementation, extra donor survey, or automatic acceptance of the candidate model.

## 1. Exact completed status and what Gate D actually means

**All thirteen planned case-study iterations are COMPLETE as documented research artifacts.** Phase A (I01–I04) established version-pinned product/engineering evidence and audited its scope; Phase B (I05–I08) applied five prior candidate distinctions to the Smart Citizen Kit 2.3 sources; Phase C (I09–I10) described and critically checked a bounded **textual** conceptual DIM slice; Phase D (I11–I13) tested OGC carrier availability, rejected invalid transformations, and integrated the case study.

| Evidence gate | Earned result | What was NOT established |
| --- | --- | --- |
| **Gate A — I04** | **CONDITIONAL PASS for manufacturer product/design evidence**, 34 of 60 original F### fact records independently sampled; specific research errors corrected. | A physically authenticated SCK2.3 individual, actual installed parts/firmware, live readings, verified physical-to-platform identity join. |
| **Gate B — I08** | **CONDITIONAL PASS** for source-grounded coherence of the five meaning distinctions and concrete error prevention, including backend **Component** versus physical hardware. | Positive real-unit identity correlation, executed method or result, implemented CSAPI or conformance. |
| **Gate C — I10** | **CONDITIONAL PASS** for internally coherent **candidate textual conceptual slice** with source-to-donor-to-V2 traceability and a deliberate **NO UML DIAGRAM** decision. | Adopted DIM class diagram, complete model, full donor-model equivalence or instance. |
| **Gate D — I13** | **CONDITIONAL ACCEPTANCE of the complete, traceable research case study**, including I12's falsification of four incorrect candidate mapping rules. | **Empirical positive equipment-to-platform-to-CSAPI interoperability NOT PASSED/NOT TESTED**; no actual lossless transformation or standards-conformance result. |

**Never describe Gate D as an unqualified PASS.** Completion of 13 *research iterations* is not equivalent to an achieved end-to-end technical deployment, and a conditional gate is not a deferred task secretly accomplished. I13's principal earned conclusion is **source-grounded semantic integrity and demonstrated prevention of incorrect mappings**, with a clear evidence ceiling. The source-backed case has **not proved a full version 2 DIM nor a normative application profile**.

## 2. Read-order and original research controls

**Read in this order for a post-case decision or new working session:**

1. [Current README](README.md) and [13-iteration plan](PLAN_13_ITERATIONS_v0.1_27OCT2026.md) — **live status and explicit next action**. The plan's old I13 exit criteria remain the record of what this phase was authorized to do, not a new open iteration.
2. [I13 integrated case study](I13_Integrated_Smart_Citizen_Case_Study_and_Gate_D_v0.1_28OCT2026.md) — core synthesis, actual contribution, four falsified mapping rules, Gate D and recommended next decision. **Read this before drawing overall conclusions.**
3. [I12 critical interoperability challenge](I12_Critical_Interoperability_Challenge_v0.1_28OCT2026.md) — **controlling correction of I11**. Then read [I11 accommodation](I11_CSAPI_OGC_Accommodation_v0.1_28OCT2026.md) when a specific OGC provision, mapping status or potential gap matters.
4. [I09 bounded candidate conceptual slice](I09_Candidate_DIM_Conceptual_Slice_v0.1_28OCT2026.md) and [I10 model/view source-critical audit](I10_Model_View_Critical_Check_and_Gate_C_v0.1_28OCT2026.md) — what is *only candidate*, what is a role/relationship rather than a class, and why no authoritative UML was created. I10's **Device–Sensor-definition** correction governs I09 terminology.
5. [I08 digital representation and five-pass reconciliation](I08_Digital_Representation_and_Five_Pass_Reconciliation_v0.1_28OCT2026.md), [I07 physical composition](I07_Composition_and_Component_Standing_Mapping_v0.1_28OCT2026.md), [I06 Method/Procedure](I06_Procedure_and_Method_Mapping_v0.1_28OCT2026.md) and [I05 identity/model/kind](I05_Individual_System_and_Product_Kind_Mapping_v0.1_27OCT2026.md) — original detailed application to case evidence. **Do not substitute I13 summary when making a fine-grained claim.**
6. [I04 independent evidence audit](I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md) **before citing** older [I03 F001–F060 extraction](I03_Source_Native_Fact_Register_v0.1_27OCT2026.md), [I02 25-file corpus](I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md) and [I01 selection](I01_Equipment_Selection_and_Qualification_v0.1_27OCT2026.md). **I04 corrections override misleading older I02/I03 discovery language**.
7. For **main-program scope, method or next subject decisions** additionally read [DIM Concept Baseline](../../DRAFT_Concept_Baseline_v0.1_25OCT2026.md), [DIM Concept and Method Basis](../../DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md), [five-pass synthesis checkpoint](../../DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md), [canonical concept consolidation plan](../../DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md), [parent PITON v1.4](../../PITON_DIM_Profile_V2_Continuity_v1.4_26OCT2026.md), and the original donor passages that can change a claim.

**Rule for document authority:** PITONs A/B/C preserve recovery state **at a point in time**. The actual dated research notes and corrections establish their specific claims; the newest verified README/plan control progress; neither a summary nor repeated AI output is independent evidence. Older PITON A (I05 next), PITON B (I09 next), parent PITON v1.4 (Pass 2 next), and I11's historical I12-next heading have **outdated progress statements**; they must never cause a restart of completed work.

## 3. Immutable upstream evidence (do not confuse with production observations)

Four **full-commit** pins were frozen in I02; the project selected 25 original files, not "all source files" and not a production data export:

| Source | Full immutable Git commit | Scope/limit |
| --- | --- | --- |
| **D — documentation** | [fablabbcn/smartcitizen-docs@0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f](https://github.com/fablabbcn/smartcitizen-docs/tree/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f) | Model, assembly, platform and advanced calibration *descriptions*. |
| **H — hardware/firmware** | [fablabbcn/smartcitizen-kit-2x@3dbbc1061509920aca2dda2aca32abe82563500b](https://github.com/fablabbcn/smartcitizen-kit-2x/tree/3dbbc1061509920aca2dda2aca32abe82563500b) | Designs, schematics/manufacturing and firmware paths, **not installed/running state**. |
| **R — data/examples** | [fablabbcn/smartcitizen-data@4f024f4d42cb40c2cd515062ee7e4815bd2798eb](https://github.com/fablabbcn/smartcitizen-data/tree/4f024f4d42cb40c2cd515062ee7e4815bd2798eb) | Processing blueprint and **unexecuted** notebook; code literals are not observations. |
| **A — backend software** | [fablabbcn/smartcitizen-api@25a524cbfb036f8950c247b847d8884a4e776297](https://github.com/fablabbcn/smartcitizen-api/tree/25a524cbfb036f8950c247b847d8884a4e776297) | Code's Device/Component association semantics, **not verified deployed revision**. |

**Unresolved individual-data gaps from I03 remain GAP-01–GAP-06:** verified physical Kit identity; Kit-to-platform record association; actual installed boards/PM model/firmware/settings; deployment and event history; real time-stamped measurements with used Method and result; and actual deployed software revision. The frozen notebook lists candidate platform IDs **18486, 18487, 18488, 18489**, dates **12 February–7 March 2025**, **27 cells, 17 code cells, no saved executions/results** (I04 FLAG-05). **Do not call these physical serial numbers or data records.** Failure to fetch live data was not proof of platform outage, invalid IDs or nonexistent operational records.

**Mandatory corrections from I04:**

- The supposed public HTML versus pinned Git sensor-part-name mismatch was **RETRACTED as AI research error**. Exact source part models supported by the SCK2.3 schematic include **MPL3115A2, AS7331, ICS-43432, SHT31, BH1730FVC**; do not revive fabricated inconsistent spellings.
- **4 MB vs 8 MB buffer descriptions:** manufacturing pick-and-place and firmware documentation support **S25FL064L, 8 MB as specified SCK2.3 design's dedicated reading buffer**. The older Data Board **4 MB extra flash** wording remains a true *source statement* but is not the preferred technical conclusion about the design. The ESP module has separate storage; no physical chip verified on a specific unit.
- F023 citation broadened to include 2.2/2.3 pressure comparison; F025 PM size-designated concentrations in **µg/m³**, not generalized mass fractions; F035 WARNING can preserve reading collection when **SD or network publication** is impaired; F047 source's "four-digit" registration code phrase conflicts with its alphanumeric wording. **Stable F001–F060 numbers never changed**.
- Original I04 audit sampled **34/60** facts; remaining 26 are **not blanket independently checked**. Target any later consequential new claim at exact frozen source, rather than reopening every fact or promoting all as confirmed.

## 4. Five candidate meanings, what I13 established and what is NOT a model class

| Candidate distinction | Source-based result | Non-adoption guard |
| --- | --- | --- |
| **Individual System and identity** | One physical Kit, if authenticated, is distinct from the manufacturer generation **SCK2.3**, the vendor API record, a MAC, UUID, token, URL, or advanced-station Hardware ID. | No source-verified System individual/UID or universal lifetime ID rule; no new IndividualSystem class. |
| **Reusable kind/model** | Product generation, board models and compatible SEN5X variants are type/option evidence. CSAPI **systemKind** is a kind-description relationship, **not** the separately implementable **procedures** relationship. | No universal ProductModel class, source-equivalent SAREF/AAS/WoT type class, forced type cardinality or published SCK2.3 CSAPI Procedure. |
| **Reusable Procedure vs actual execution** | Pinned SHT31/SEN5X/AS7331 code describes acquisition/processing, and separate advanced **sc_air** describes off-device processing. | No actual installed firmware, used Procedure, historical Observation, or assumption that basic Kit has advanced electrochemical sensors. |
| **Physical composition, independent component standing and channels** | Two normally mating boards, mounted ICs, a separate **cabled in-enclosure** PM module, battery/storage and several output channels per IC. | No rule that a cable means temporary Aggregation, that a software channel equals a physical chip, or that every part is a CSAPI System/subsystem. No UML composition diamond without UML semantics. |
| **Digital representation / proxy** | Pinned backend **Component** is explicitly a **database Device–Sensor-definition association** with sensor-related readings, not necessarily one measurement channel or a hardware part; advanced station physical ID differs from platform page ID. | No vendor WoT/AAS/OPC UA/CSAPI implementation, no universal representedBy relation or DigitalRepresentation class, and no proven physical-to-platform ID join. |

**Current model standing:** I09 has **C01–C06 candidate roles/boundaries**, **R01–R06 qualified relationship statements** and **T01–T06 citations**; I10 reviewed them and chose **NO authoritative UML** rather than visually invent classes or a fictional equipment instance. A **small textual candidate** exists, **not a formalized, adopted or complete V2 DIM**. There are **no normative CSAPI profile conformance classes or SHALL requirements** resulting from I13.

**V2 methodological boundary:** The subject remains a working **equipment-realized sensing System**; CSAPI **systemType = Sensor** and **assetType = Equipment** are *two native facets*, **not three peer classes or a newly named compound class**. No forced final domain name, root-class architecture or V1-derived eight modules. **Model for the profile, not to the profile**: DIM meanings first, selected application profile after a justified interoperability need, and API/SensorML binding thereafter.

**Parent-source quarantine:** Earlier Anatomy **Phase B/C/D** results and promoted model architecture were **QUARANTINED** after an audit and must **not** be treated as accepted V2 semantics, even if visible in the repository. Parent PITON v1.3/v1.4 preserves that rule. The original **182-artifact donor population** and **30 Phase A semantic lineages** are research infrastructure; their full content is **not** adopted by this bounded Smart Citizen case. Donors such as SAPIENT, ISA, OSUS/OSUS-R, OPC UA, AAS, WoT, OMS and other families must not disappear by organizational convenience or be counted as implementation/conformance merely by conceptual analogy.

## 5. I11 accepted meanings and I12 falsified shortcuts — both must survive

**What the approved OGC standards already supply for the studied role meanings:** [CSAPI Part 1 23-001 v1.0](https://docs.ogc.org/is/23-001/23-001.html) describes **System** individual/UID versus resource URL, **systemKind** versus implementable **procedures**, independent System subsystems, Composition/Aggregation and Deployment. [CSAPI Part 2 23-002 v1.0](https://docs.ogc.org/is/23-002/23-002.html) distinguishes producing Systems, DataStreams, real Observations, optional used-Procedure references and SystemEvents. [SensorML 3.0 23-000](https://docs.ogc.org/is/23-000/23-000.html) supports physical/process details, general-versus-configured processes, ProcessMethod and component descriptions. These are **standard-defined options and roles**, **not** proof the vendor operates any chosen requirements class or has actual device records.

**I12's four falsified naive mapping rules, explicitly controlling I11's more favorable conclusions:**

1. **Product list is not observed DataStream metadata:** Part 2 **§ 9.2.2, Table 2** requires observedProperties, phenomenonTime, resultTime and resultType to be **server-derived from linked Observations, null without them**. Manufacturer advertised measurements cannot populate the actual stream.
2. **Parent DataStream discovery is not direct producer evidence:** Part 1 **§ 10.7, Requirement 13/Table 9** recursively includes child subsystems' streams in parent associations, while Part 2 **DataStream.system** identifies the producing System.
3. **Nested subsystem is not proof of permanent attachment:** Part 1 **§ 10.5, Requirement 9(C)** allows the subsystem endpoint to include **currently deployed** items as well as permanent ones; relationship semantics still require evidence under **§ 10.2**.
4. **Backend Component is not physical equipment:** Source explicitly defines a **Device-to-Sensor-definition database association**; it cannot be automatically turned into a physical CSAPI System resource or one-channel-per-chip inventory.

**Other conditional I12 matters:** actual DataStream grouping needs source Observation schema and producer; **GROUP_TIME** acquisition time is not necessarily both phenomenonTime/resultTime; optional Procedure links do not prove actual method/version/calibration; a SensorML Deployment-carried configuration is not a base CSAPI Deployment property; separate requirements/conformance classes are not automatically implemented. No invented positive source-to-standard transformation occurred.

**Status of standards gap finding:** **No new CSAPI/SensorML semantic defect CONFIRMED within this restricted five-distinction case**, and four faulty **mapping shortcuts** demonstrably fail. **This is neither a universal completeness proof nor evidence of lossless mapping, deployed interoperability, or standard conformance.** Treat "mapping possible" and "mapping verified" as different results.

## 6. Essential case-study source-to-result trace

For direct statements, follow the complete recorded evidence rather than citing this PITON as primary source:

| Research path | Exact case artifact |
| --- | --- |
| Source family and source version selection | [I01 equipment selection](I01_Equipment_Selection_and_Qualification_v0.1_27OCT2026.md) → [I02 pinned source register](I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md) |
| Original manufacturer/firmware statements and limitations | [I03 F001–F060](I03_Source_Native_Fact_Register_v0.1_27OCT2026.md) → [I04 audited corrections/Gate A](I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md) |
| Identity, kind, Procedure and physical component mapping | [I05](I05_Individual_System_and_Product_Kind_Mapping_v0.1_27OCT2026.md), [I06](I06_Procedure_and_Method_Mapping_v0.1_28OCT2026.md), [I07](I07_Composition_and_Component_Standing_Mapping_v0.1_28OCT2026.md) |
| Digital software/identity collision and cross-pass conclusion | [I08](I08_Digital_Representation_and_Five_Pass_Reconciliation_v0.1_28OCT2026.md) |
| Candidate conceptual DIM and adversarial model review | [I09](I09_Candidate_DIM_Conceptual_Slice_v0.1_28OCT2026.md) → [I10](I10_Model_View_Critical_Check_and_Gate_C_v0.1_28OCT2026.md) |
| OGC source clauses and mapping/failure analysis | [I11](I11_CSAPI_OGC_Accommodation_v0.1_28OCT2026.md) **as qualified by** [I12](I12_Critical_Interoperability_Challenge_v0.1_28OCT2026.md) |
| Integrated narrative, research value and Gate D | **[I13 report](I13_Integrated_Smart_Citizen_Case_Study_and_Gate_D_v0.1_28OCT2026.md)** |

This handoff exists because earlier conversational compression and PITON reuse caused real project drift. **Do not extrapolate from labels, invent artifacts that are not in GitHub, report a unit test merely because a notebook exists, or mistake a source-data gap for a standards deficiency.** When an original statement is consequential, reopen its cited *pinned original source*.

## 7. What the completed work has NOT done

The completed project increment has **not** authenticated a physical Kit; retrieved or converted verified live device measurements; shown a serial-specific installed sensor/firmware/calibration state; verified an individual-to-platform ID crosswalk; exercised a live CSAPI service; built a Smart Citizen adapter/server/client; generated a normative profile; created formal adopted UML classes/modules; demonstrated Part 1/2 conformance; or established a full DIM for every whole-system information subject. The unexecuted original notebook and example algorithm are **not** an empirical substitute for any of these results.

The non-adoption decision is equally important: the project has **not** named a new universal domain category, created a combined SensorEquipmentSystem root, forced donor implementations into OGC resources, or adopted a universal proxy/cardinality/ID rule. The case established **qualified relational meaning and mapping hazards**, and the parent program still needs careful research before broad architectural decisions. Do not restart the earlier 182-source donor census just to finish the case.

## 8. Next authorized action after I13 — clear boundary

**The thirteen-iteration case-study plan is COMPLETE. The next step is not I14.** A newly prompted **post-case-study research decision checkpoint** is recommended, expressly *separate from the completed case*.

The checkpoint should evaluate two separate possibilities using existing evidence **without automatically executing either**:

- **Empirical branch:** Seek one authenticated SCK2.3 physical unit with a verified product revision, a real linked platform Device record, actual installed PM model/configuration, timestamped values and enough provenance to test a positive CSAPI mapping, **if** demonstrating physical-to-service interoperability with this product is valuable and feasible.
- **DIM research branch:** Return to the wider V2 research program for the next **donor-grounded concept family**, with **capability/performance** the specific next candidate identified in the [original five-pass synthesis](../../DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md). This must remain an evidence-led, incremental investigation rather than a premature formal architecture or profile draft.

**If the owner says “proceed” immediately after the completed I13 report**, **first** fetch the current README and this PITON plus I13, then undertake **only that decision checkpoint**: compare these two paths against the documented objectives, evidence gaps and research method; recommend one or a bounded sequence, record any owner-established choice, and identify a precise next research iteration. **Do not automatically perform the empirical test, start capability/performance research, decide the final V2 name or draft new conformance SHALLs in the same turn.** If the owner explicitly names another next task, follow it instead.

**New-chat reporting discipline:** Explain in ordinary language **what is established, what is conditional, what cannot be claimed, where the actual GitHub evidence is, what was completed, and one clearly named next step**. End each authorized substantive iteration with its verified document link and a simple **“proceed”** invitation where a named next step exists; do not ask the owner to repeat established facts or approve routine file operations. Do not carry out unrequested additional substantive iterations.

**Suggested handoff sentence:** “The Smart Citizen Case Study I01–I13 is complete as a source-grounded semantic-fidelity exercise. Gate D conditionally accepts the report, but empirical Kit/CSAPI interoperability remains untested. I13 and PITON C are committed on research/dim-profile-v2. Next is a post-case research decision checkpoint—not I14—to choose between authenticated field-unit evidence and the next donor-grounded DIM concept study. Say ‘proceed’ to begin that checkpoint.”
