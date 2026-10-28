# Iteration I10 — Critical Model/View Review and Gate C Decision

**Date:** 28 October 2026  
**Status:** **I10 COMPLETE — Gate C CONDITIONAL PASS for a bounded, source-traceable textual candidate DIM slice; I11 NEXT, not begun.**  
**Standing:** Critical audit of [I09's candidate conceptual slice](I09_Candidate_DIM_Conceptual_Slice_v0.1_28OCT2026.md), not an adopted Domain Information Model (DIM), UML metamodel, physical equipment instance, normative application profile, standards conformance finding, or empirical interoperability demonstration.  
**Repository and branch:** [OS4CSAPI/glaux-client](https://github.com/OS4CSAPI/glaux-client), **research/dim-profile-v2**.  
**Case-study control:** [README](README.md), [13-iteration plan](PLAN_13_ITERATIONS_v0.1_27OCT2026.md), [I03 fact register](I03_Source_Native_Fact_Register_v0.1_27OCT2026.md), [I04 / Gate A](I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md), [I05 identity/kind](I05_Individual_System_and_Product_Kind_Mapping_v0.1_27OCT2026.md), [I06 method](I06_Procedure_and_Method_Mapping_v0.1_28OCT2026.md), [I07 composition](I07_Composition_and_Component_Standing_Mapping_v0.1_28OCT2026.md), [I08 / Gate B](I08_Digital_Representation_and_Five_Pass_Reconciliation_v0.1_28OCT2026.md), [PITON B](PITON_B_Real_Equipment_DIM_Validation_v0.1_28OCT2026.md).  
**Method:** [DIM Concept and Method Basis](../../DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md), [modeling convention](../../DIM_Profile_V2_Modeling_Convention_v0.1_26OCT2026.md) and [visualization guide](../../DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md). **Quarantined earlier anatomy Phase B/C/D artifacts were not used as authority.**

## 1. Critical finding

**The I09 slice survives a targeted adversarial source and notation review as a bounded set of semantic relationships and source-granularity distinctions, not as six adopted classes or a verified Smart Citizen Kit instance.** Its strongest earned contribution is preventing specific false equivalences: the individual System is not its product model or vendor record; a System kind description is not necessarily a method that System implements; an available method is not an observed execution; a physical constituent is not automatically a separately identifiable System; and a software sensor association is not a physical part.

The resulting **candidate model representation is textual**: I09's C01–C06 candidate entries, R01–R06 relationship statements and T01–T06 source-to-donor-to-V2 trace matrix, critically tested here. **No UML class or instance diagram is adopted in I10**, because the plausible drawings would either add little beyond the existing sources or silently introduce unsupported classes, attributes, instances, or cardinalities. This is a documented no-diagram decision under the approved visualization rules, not a rendering failure.

**Precision correction (D01):** The official backend class called **Component** is a database association linking a **Device record to a Sensor definition**, with access to sensor-associated readings. Do **not** rephrase this as proof of a physical component **or** as a universal one-Component-to-one-measurement-channel relationship. The distinction is directly confirmed by the [pinned Component model](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/app/models/component.rb#L1-L7) and [Component presenter](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/app/lib/presenters/component_presenter.rb#L10-L27). I09 receives a visible corrective note and a narrow wording revision rather than a silent rewrite.

## 2. What was independently inspected

This is a **targeted recheck**, not a complete audit of I03's 60 facts, all 182 donor records, or production Smart Citizen equipment. Primary standards examined directly were the approved [CSAPI Part 1 v1.0](https://docs.ogc.org/is/23-001/23-001.html), [SensorML 3.0](https://docs.ogc.org/is/23-000/23-000.html), the [21 October 2026 SOSA/SSN Working Draft](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/), [SAREF 4.1.1](https://saref.etsi.org/core/v4.1.1/), [AAS 3.2](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/core.html), [WoT Architecture 1.1](https://www.w3.org/TR/wot-architecture11/), [Thing Description 1.1](https://www.w3.org/TR/wot-thing-description11/) and [OPC UA Part 100 Devices 1.05.0](https://reference.opcfoundation.org/specs/OPC-10000-100/full). For *Observations, Measurements and Samples* (OMS) 3.0 we retained the earlier documented Pass 3 interpretation; its complete text was **not independently re-audited in I10**.

Original manufacturer files directly rechecked, at the immutable commits frozen by I02, were the [SCK2.3 product/sensor table](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/kit/index.md#L39-L123), [normal assembly procedure](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/guides/getting-started/kit-assembly.md#L114-L149), [advanced hardware/platform ID explanation](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/guides/getting-started/kit-assembly.md#L256-L273), [SHT31 firmware acquisition routine](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/sam/src/SckUrban.cpp#L842-L895), [SEN5X conditional acquisition](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/sam/src/SckUrban.cpp#L2022-L2100), [AS7331 processing](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/sam/src/SckUrban.cpp#L2760-L2817), [advanced sc_air processing blueprint](https://github.com/fablabbcn/smartcitizen-data/blob/4f024f4d42cb40c2cd515062ee7e4815bd2798eb/blueprints/sc_air.json#L1-L44), and the backend **Component / Device** source. The source audit from I04 still controls its 34/60 sampled fact count and the remaining 26-fact ceiling.

| Check | Source-native question and answer | Verdict for I09 |
| --- | --- | --- |
| **S01: individual, kind, identifier** | [CSAPI § 9.2.2, Tables 4–7](https://docs.ogc.org/is/23-001/23-001.html) distinguishes individual System resource, classification facets, required System identifier and optional kind link. **System UID is required; being persistent and independent of the resource URL is a SHOULD**, not unconditional lifetime SHALL. The SCK2.3 sources describe a manufacturer design, not a physically authenticated unit. | **PASS semantic distinction; no actual System instance** |
| **S02: kind vs method carrier** | CSAPI Table 5 calls the **systemKind** target a single **Procedure resource describing a kind/datasheet**, separately from **procedures**, the Methods a System can implement. AAS **AssetInformation.assetType** links an asset to a *type asset*, while CSAPI **assetType = Equipment** means hardware realization. [AAS 3.2 AssetInformation](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/core.html). | **PASS with source-role qualification** |
| **S03: method vs execution** | A real firmware routine handles SHT31 acquisition/check/conversion and a SEN5X warm-up state machine; neither proves installed firmware or historical use. [SOSA/SSN Working Draft](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/) distinguishes **implements**, **madeBySystem**, and **usedProcedure**. Advanced sc_air is a separate processing blueprint. | **PASS for source method meaning; execution NOT TESTED** |
| **S04: physical vs software components** | The manufacturer instructions place a **cabled particulate sensor in the normal enclosure assembly**; the same SHT31 design supports temperature and humidity and AS7331 supports three UV measurements. [CSAPI § 10.1–10.3](https://docs.ogc.org/is/23-001/23-001.html) describes subsystems as *regular System resources*, and contrasts Composition versus temporary Deployment/Aggregation. A software Component is not evidence of any such independent physical System. | **PASS design-level relationship; independent subsystem standing OPEN** |
| **S05: representation identity** | Advanced station guidance distinguishes a stationary Hardware ID from potentially changing platform registration ID. [WoT Architecture § 6.10.2](https://www.w3.org/TR/wot-architecture11/) permits proxy Thing Descriptions retaining **or changing** the originating identifier; AAS Shell vs Asset also distinguishes referent from representation. **No actual Smart Citizen WoT/AAS/CSAPI representation or physical-to-platform join has been verified.** | **PASS non-equivalence; positive identity mapping NOT VERIFIED** |

**Authority/edition control:** CSAPI 1.0 and SensorML 3.0 are approved 2025 OGC standards. The October 2026 SOSA/SSN text is explicitly a **Working Draft**, not the earlier ontology edition referenced normatively by CSAPI 1.0. SAREF, AAS, OPC UA and WoT have their own native terms and constraints; the Smart Citizen repositories provide implementation/design evidence, **not normative ontology authority**. Related donor standards and companion files are not counted as independent votes.

## 3. Adversarial semantic-loss tests

These tests challenge the **truth conditions** of the candidate relationships, not whether a figure is attractive. They are **hypothetical integrations grounded in actual source structures**, not observed deployments.

| Test | Incorrect inference to challenge | Correct interpretation permitted by the candidate slice | Disposition |
| --- | --- | --- | --- |
| **E01: same model, different individuals** | Use **SCK2.3** as a serial number identifying one actual Kit. | A model/generation describes potentially many individuals. The case establishes *zero authenticated individual Kits*. | **PASS, R01** |
| **E02: PM product alternatives** | Treat all SEN50, SEN54 and SEN55 options as installed in the same individual, or claim every Kit offers optional NOx/VOC measurements. | Preserve catalogued variants while withholding real installed component, supported individual capabilities and readings. | **PASS, R01/R04** |
| **E03: multi-output IC vs backend record** | Convert a temperature/humidity pair, three UV channels, or each backend Component to a separate physical System. | Distinguish physical part, supported measurement/function, Device–Sensor-definition association, and independently identified System. | **PASS with D01 correction, R05** |
| **E04: connected does not mean temporary** | Because the PM unit has a cable, call it a mission-swappable payload and assert CSAPI Aggregation. | The source specifies normal **in-enclosure assembly**. Actual changing parent/mission history and System standing remain unknown. | **PASS, R04** |
| **E05: firmware equals execution** | Claim one notebook ID ran the SHT31 method at a particular interval because firmware code and product guidance exist. | Source code describes available routine; actual firmware, settings, usage and observations remain unverified. | **PASS, R02/R03** |
| **E06: advanced blueprint equals kit capability** | Infer standard SCK2.3 electrochemical sensors or an executed NO2 calculation from a **sc_air** JSON blueprint in the same project. | Preserve separate processing description and applicability; do not populate actual standard-kit hardware or method history. | **PASS, R02/R03** |
| **E07: any identifier is a physical UID** | Equate platform device ID, MAC address, UUID, token, box code and hardware serial merely because each is an ID-like value. | Preserve identity **roles**, registration contexts and source-specific stability; demand evidence for equivalence. | **PASS, R06** |
| **E08: analytic entries become six classes** | Draw I09 C01–C06 as six classes with associations and 1:1 cardinalities. | C01 is the chosen candidate System subject; C02/C03 express distinct meanings and links; C04 a relation/granularity decision; C05/C06 deliberately unpopulated boundaries. | **PASS, no UML adoption** |
| **E09: similarly named donor fields** | Make CSAPI **assetType** equivalent to AAS **assetType** or OPC UA **DeviceType**. | The first classifies realization, the second references a type asset, the last is an information-model ObjectType. | **PASS, donor-specific** |

**Interpretation of PASS:** The candidate slice instructs an integrator to **avoid** the false mapping. These tests do **not** constitute positive verification of the right mapping or successful transport of a real observation.

## 4. Granularity check: what the source actually identifies

| Native object or description | Proven level | Independent physical System standing? | Model disposition |
| --- | --- | --- | --- |
| **Smart Citizen Kit 2.3** | Manufacturer product/generation design. | **No specific individual authenticated.** | A kind-level description; not a populated System instance. |
| **Data Board / Urban Board** | Separately documented boards and normal assembly. | **Not established.** No stand-alone physical ID or managed history obtained. | Design constituents, not automatically System resources. |
| **SEN5X PM module** | Model family/options and documented cabled in-enclosure arrangement. | **Not established.** Installed variant, real serial and replacement unknown. | Separate source-describable part; not automatically Deployment/Aggregation. |
| **SHT31 / AS7331** | Physical component *design types* with multiple measured channels. | **Not established.** Channel ≠ individually serialised device. | Preserve actual sensor part versus measurement descriptions. |
| **Backend Device** | Software/database registration object with metadata. | **No verified equipment referent.** | Vendor service representation, not itself a physical kit. |
| **Backend Component** | Device-to-Sensor-definition association exposing reading data. | **No; not a physical board or chip.** | Software/data role; no forced one-channel relationship. |
| **IDs 18486–18489** | Code literals in official unexecuted notebook (I04 F058–F059). | **Not established.** | Example code only, no fielded system or observation instance. |

**Crucial distinction:** An independently described physical component need not have **independent CSAPI System identity**. Conversely, absence of proof here is not a general prohibition against representing individually identified subsystems once a later source supports them.

## 5. Figure decision: explicit **NO UML DIAGRAM**

Under the [visualization guide](../../DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md), a maintained UML figure must represent already justified concepts and relationships, add value beyond prose, remain semantically accurate, and have reproducible source. Considered options:

| Proposed view | What it would require or add | Decision |
| --- | --- | --- |
| **Six-box C01–C06 class diagram** | Would promote *roles, relationship questions and boundaries* into six classes by mere visual arrangement. | **REJECTED: semantic invention.** |
| **Two classes, System and Procedure, with two relations** | Can faithfully reproduce CSAPI Table 5 kind-versus-implemented-Procedure **in that donor's own terms**, but would not establish a V2 class model or add content beyond I09 R01/R02. | **NOT SELECTED: source-native excerpt, little new analytical value.** |
| **One actual SCK2.3 object diagram** | Would need a verified physical Kit, its actual installed parts, identity joins and—if shown—observations; no such source is available. | **REJECTED: fictional instance could masquerade as observed.** |
| **Full physical/electronic/API component tree** | Would impose a common part hierarchy across physical boards, logical channels and backend software objects. | **REJECTED: source meanings conflict.** |
| **DIM → profile → binding architecture chart** | Describes an already settled **method distinction**, not the novel I10 semantic challenge. | **NOT SELECTED: redundant context figure.** |

**Recorded decision:** The reviewed conceptual **representation** for this iteration is I09's **defined textual roles, R## relation statements and T## traceability matrix**, together with I10's counterexample and discrepancy matrices. Because no diagram is authorized, there is **no diagram source/render artifact to preserve**. Future formal class UML remains possible when source-grounded class/association decisions yield meaningful structure; a real object view needs actual instance evidence. **Not every future conceptual UML requires live data**—only the claims depicted must have the corresponding basis.

## 6. Discrepancy register (explicit dispositions)

| ID | Challenged issue | Result | Status |
| --- | --- | --- | --- |
| **D01 — backend Component wording** | The I09 C06 phrase “channel association” risks implying every database Component corresponds to one channel. | Correct to **Device–Sensor-definition association with associated readings**, while keeping physical-to-software distinction. Place visible I10 correction note on I09. | **CORRECTED** |
| **D02 — analytical entries as classes** | C01–C06 labels could be visually promoted as six classes. | Only the semantic subject and relations are candidates. Boundaries and information roles are not automatically classes. | **CONTROLLED — no diagram** |
| **D03 — type-to-instance leakage** | Source product/assembly descriptions could be presented as a real configured Kit. | Keep all positive unit/installed-hardware/method claims unpopulated. | **NOT VERIFIED** |
| **D04 — kind versus method** | The two CSAPI roles share a Procedure resource type. | Keep distinct relationship meanings, without disjoint universal ProductModel and Method classes. | **PASS** |
| **D05 — composition/temporal standing** | Cabled in-enclosure module may be permanently installed in a specific Kit—or may be exchanged. | The assembly design cannot decide a specific unit's permanence, independent identity or replacement record. | **OPEN / QUALIFIED** |
| **D06 — representation identity** | Advanced-station ID behavior might be overgeneralized to a basic Kit; backend device IDs might stand in for real hardware. | Preserve source scope. No physical-to-digital join, general proxy rule or actual CSAPI UID established. | **OPEN / QUALIFIED** |
| **D07 — standards/corpus authority** | Current SOSA/SSN draft and vendor implementation code could masquerade as published standard requirements. | Clearly retain source type, edition and evidence ceiling; prior Phase A quarantined anatomy stays excluded. | **CONTROL RETAINED** |
| **D08 — fabricated observation** | Unexecuted notebook date range/IDs could be treated as live observations. | Preserve I04 result: 17 code cells with zero saved executions/outputs. No real observation or method-use assertion. | **NOT TESTED** |

**No contradiction requiring rejection of the *bounded* I09 semantic slice was found in the targeted direct sources.** This does not establish that all 182 donor artifacts have been exhaustively reconciled, or that every I03 fact has been independently verified. I04's earlier **retracted** part-number conflict stays retracted; its separate 4 MB versus 8 MB manufacturer storage-description conflict was adjudicated **only at specified design level** and is not reopened as a new DIM fact.

## 7. Gate C assessment and remaining evidence limits

**Gate C: CONDITIONAL PASS — strictly for internal coherence, source-to-donor-to-DIM traceability and the bounded candidate *textual* conceptual representation.** This means I09 and this critical check are fit to inform **I11 semantic accommodation research**; it does **not** mean the DIM is adopted, a deployed Kit described, or standards implementation demonstrated.

| Gate criterion | Result |
| --- | --- |
| Relationship meanings and chosen System subject remain coherent | **PASS — limited conceptual scope;** individual ≠ kind, kind role ≠ implemented method, method ≠ execution, physical constituent ≠ software association, physical subject ≠ digital representation. |
| Cited paths support the material distinctions | **PASS within targeted checks** of I09 T01–T06; not a full vendor facts or donor corpus audit. |
| Representation avoids unsupported classes/instance/cardinalities | **PASS — documented no-diagram decision** and an auditable semantic matrix. |
| Challenged issues repaired and residual uncertainty preserved | **PASS with D01 precision correction** and explicit D02–D08 controls. |
| Authenticated physical unit, real parts/configuration, live observation, working cross-service identity join | **NOT VERIFIED / NOT TESTED** (inherits conditional Gates A and B). |
| Authoritative UML metamodel, full DIM, normative profile or conformance | **NOT CREATED / NOT CLAIMED**; these are outside I10's bounded gate. |

**Gate interpretation:** A semantic relationship can be justified by manufacturer design plus donor meaning even when no particular fielded unit is known; but **a source limit is not itself evidence that CSAPI lacks a semantic capability**. At I11, classify support as *direct, partial, specialized, unpopulated for lack of source data, or genuinely unsupported*; do not turn unpopulated fields into invented profile obligations.

### I11 guardrails

1. Map I09/I10 **meaning** to exact CSAPI Parts 1–2 and SensorML clauses, without replacing the DIM with API paths or JSON structures.
2. Do not mint a placeholder physical System UID to pretend the case has a real unit; published CSAPI requires one for a real System resource, but our corpus does not supply a verified value.
3. Preserve two CSAPI Procedure **relationship roles**, donor-specific type semantics and System-vs-subsystem standing.
4. Keep actual fielded identity, installed PM sensor, firmware/method execution, data and timestamps explicitly **unpopulated**.
5. Avoid claiming Smart Citizen runs CSAPI, WoT, OPC UA or AAS, or that a standards-native mapping is a verified interoperation.
6. Preserve the exact source editions and distinguish a missing source record from an inability of the standard to represent one.

## 8. Completion and exact next iteration

**I10 complete — 10 of 13 case-study iterations.** Phase C now contains the **I09 candidate textual model slice plus this critical review**, with **Gate C CONDITIONAL** at the described semantic scope. PITON B remains a historical evidence checkpoint, not the latest progress authority; current README and plan control restart.

**Next: Iteration I11 — CSAPI/OGC Accommodation.** Evaluate the reviewed candidate meanings against exact CSAPI Part 1 and Part 2 / SensorML provisions with a sourced accommodation matrix and explanatory narrative; preserve source gaps and partial support, do not invent profile SHALLs or test claims, commit and verify, update README/plan, and stop before I12. One user **“proceed”** authorizes only I11.

## References (Chicago Manual of Style, 18th edition, author–date)

European Telecommunications Standards Institute. 2024. *SAREF: Smart Applications REFerence Ontology—Core*, version 4.1.1. https://saref.etsi.org/core/v4.1.1/.

Fab Lab Barcelona. 2026a. *Smart Citizen Kit 2.X Hardware and Firmware*, full pinned commit 3dbbc1061509920aca2dda2aca32abe82563500b. https://github.com/fablabbcn/smartcitizen-kit-2x/tree/3dbbc1061509920aca2dda2aca32abe82563500b.

Fab Lab Barcelona. 2026b. *Smart Citizen Data Tooling and Example Notebook*, full pinned commit 4f024f4d42cb40c2cd515062ee7e4815bd2798eb. https://github.com/fablabbcn/smartcitizen-data/tree/4f024f4d42cb40c2cd515062ee7e4815bd2798eb.

Fab Lab Barcelona. 2026c. *SmartCitizen API Backend*, full pinned commit 25a524cbfb036f8950c247b847d8884a4e776297. https://github.com/fablabbcn/smartcitizen-api/tree/25a524cbfb036f8950c247b847d8884a4e776297.

Industrial Digital Twin Association. 2026. *Specification of the Asset Administration Shell, Part 1: Metamodel*, version 3.2. https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/core.html.

Object Management Group. 2017. *Unified Modeling Language*, version 2.5.1. https://www.omg.org/spec/UML/2.5.1.

Open Geospatial Consortium. 2025a. *OGC API – Connected Systems – Part 1: Feature Resources*, OGC 23-001, version 1.0. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC SensorML Encoding Standard*, OGC 23-000, version 3.0. https://docs.ogc.org/is/23-000/23-000.html.

Open Geospatial Consortium. 2025c. *OGC API – Connected Systems – Part 2: Dynamic Data*, OGC 23-002, version 1.0. https://docs.ogc.org/is/23-002/23-002.html.

Open Geospatial Consortium and International Organization for Standardization. 2023. *Observations, Measurements, and Samples*, OGC 20-082r4 / ISO 19156:2023. https://docs.ogc.org/as/20-082r4/20-082r4.html.

OPC Foundation. n.d. *OPC Unified Architecture Part 100: Devices*, version 1.05.0. https://reference.opcfoundation.org/specs/OPC-10000-100/full.

Smart Citizen. 2026. *Smart Citizen Documentation*, full pinned commit 0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f. https://github.com/fablabbcn/smartcitizen-docs/tree/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs.

World Wide Web Consortium. 2023a. *Web of Things (WoT) Architecture 1.1*, W3C Recommendation, December 5. https://www.w3.org/TR/wot-architecture11/.

World Wide Web Consortium. 2023b. *Web of Things (WoT) Thing Description 1.1*, W3C Recommendation, December 5. https://www.w3.org/TR/wot-thing-description11/.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology – 2023 Edition*, **Working Draft, October 21**, OGC 25-022. https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/.
