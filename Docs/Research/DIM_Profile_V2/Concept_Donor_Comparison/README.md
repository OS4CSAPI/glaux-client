# Candidate DIM — Concepts and Donor Comparisons

**Version 0.1 · 30 October 2026 · America/New_York**  
**Iteration 1: coverage and one worked comparison.** The broader comparison, equipment mapping and final review remain unfinished.  
**Workspace:** `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`.  
**Input snapshot:** `8a4a2a082d18b0806a5df85f4b387a8f9ed14a31`. This page consolidates existing V2 findings; it does not adopt or rewrite the Domain Information Model (DIM).

[Donor coverage and contributions](Donor_Contributions.md) · [Equipment evidence — not started](Equipment_Evidence.md) · [Four-iteration plan](../PLAN_DIM_Profile_V2_Concept_Donor_and_Equipment_Comparison_v0.1_30OCT2026.md) · [Drift correction](../DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md)

## 1. Start here

This section is intended to answer a practical question: **What are we proposing the model should mean, what did each donor contribute, and what remains undecided?** The first worked example is the already-researched distinction between a particular System and information about its model or kind. It was selected to demonstrate the presentation because the existing research contains both useful correspondences and an explicit rejected equivalence—not because product/model/kind has been chosen as the root of the DIM.

**The central finding is not that every donor has a different name for the same thing.** Several sources distinguish an individual from reusable descriptive information, but a product designation, device-kind description, ontology class, interface type, interaction template and channel datasheet can answer different questions. The tables below show those differences before presenting the current candidate synthesis. [Existing product/model/kind research, §§1–4](../Donor_Alignment/05_Product_Model_Kind_Alignment_v0.1_28OCT2026.md); [candidate v0.2, §4.2](../Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md).

**How to read the evidence:** the native-meaning columns summarize donor findings recorded in the linked V2 research. The proposed correspondence is the project's analysis, not a donor-declared equivalence. This iteration reread those project records; it did not independently re-audit all primary standards. Exact original editions and clauses are provided in §5 so a reader can follow the trail without treating our report as the donor itself. All existing mappings retain their candidate/not-adopted and no-transformation-test standing.

## 2. What existing work is being brought together?

| Existing material | What it contributes to this section | Boundary to preserve |
| --- | --- | --- |
| [Five original topic reports and their reconciliation](../Donor_Alignment/09_Cross_Concept_Reconciliation.md) | The documented 48 topic-scoped records on identity, kind/model, method/execution, composition and digital representation. | Some records are deferred or reject a proposed equivalence. This is not 48 independent standards or complete donor coverage. |
| [Four additional donor reviews and reconciliation](../Donor_Challenge/05_Challenge_Reconciliation.md) | SAPIENT, IEEE 1451, Integrated Sensor Architecture, and The Open Group SOSA; source-specific distinctions and five grouped open questions. | Their historical “challenge” framing does not privilege the earlier model. New contributions may change the organizing questions. |
| [Candidate manuscript v0.2](../Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md) | Five current meaning treatments and ten proposed relationship passages. | These are the current candidate record, not five immutable classes or an exhaustive model. |
| [Prior 30-lineage coverage screen](../Donor_Challenge/01_Coverage_and_Challenge_Selection.md) | Identifies examined, preliminary and deferred material beyond the worked example. | A screen of prior research, not equal-depth review of all 182 inventoried artifacts. See the donor page for later updates and omissions. |
| [Three system data sheets](../Controlled_Corpus/System_Data_Sheets/README.md) | Itemized equipment facts and published examples for later evidence connections. | No equipment-to-concept mapping is performed in Iteration 1. These are not complete joined operating datasets. |

The [donor page](Donor_Contributions.md) is the reverse view: it retains source contributions even where the current candidate model has no developed destination. Its historical family keys are navigation aids, not a ranking or new model taxonomy.

## 3. Worked comparison — what does “model or kind” describe?

### The candidate meaning under examination

**Current candidate interpretation, restated from v0.2 §4.2:** reusable descriptive information can characterize a kind of equipment or a shared specification without describing the actual configuration, calibration, condition or history of a particular unit. The source's intended descriptive role must remain visible. This is a proposed meaning distinction, not a universal `ProductModel` class.

**Related proposed relationship:** v0.2 `REL-01` says an individual System may be characterized by reusable kind/model information. It does not establish one universal cardinality, inheritance mechanism, identifier or required kind resource. [Candidate manuscript, §§4.2 and 5](../Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md).

### 3.1 Sources describing reusable kinds or type/individual distinctions

The direction in the third column is **the named source meaning toward the candidate distinction**, not an assertion that any two donors are interchangeable. “Close, qualified” and “partial overlap” summarize the existing alignment judgments. Each source link leads to its exact recorded provenance in §5.

| Donor and native term | What the source describes | Contribution to the candidate meaning | Qualification that must survive |
| --- | --- | --- | --- |
| **Asset Administration Shell (AAS)** — Type Asset / Instance Asset; `AssetInformation.assetKind`, `assetType` ([source](#source-aas)) | Shared type information and separately identified assets; the Shell has its own identity. | **Close, qualified:** type-level information differs from an individual realization. | A type asset is not a Shell template. AAS `assetType` is not the CSAPI Equipment classification; no universal requirement that every individual has a type asset. |
| **OGC API – Connected Systems (CSAPI)** — `System.systemKind` ([source](#source-csapi)) | A System's optional kind/datasheet association to a Procedure resource, distinct from implementable `procedures`. | **Close, qualified:** an individual-to-kind descriptive relationship. | A shared Procedure carrier does not make a product description an observing method. CSAPI's optional single target is source-local, not a DIM-wide multiplicity. |
| **Smart Applications REFerence ontology (SAREF)** — `DeviceKind`, `hasDeviceKind` ([source](#source-saref)) | Kinds of Devices and their common properties/functions, separately from model/manufacturer literals. | **Close, qualified:** an individual can be related to reusable device-kind information. | A model-name string is not automatically a resolved DeviceKind; a DeviceKind is not automatically a CSAPI Procedure. |
| **Sensor Model Language (SensorML)** — `typeOf`, general/specific process ([source](#source-sensorml)) | Process-description inheritance and configuration; this can describe equipment models but also nonphysical processes. | **Partial overlap:** shared descriptions can inform individual descriptions. | Not every `typeOf` link denotes a manufactured product. Do not transfer source inheritance rules to every DIM relationship. |
| **W3C/OGC SOSA/SSN** — System type and individual ([source](#source-ssn)) | The recorded 21 October 2026 Working Draft discusses a System type as an ontology class and a particular System as an individual. | **Partial overlap:** type and individual are distinct descriptive levels. | Ontology typing is not itself a datasheet or product identity. This draft is not the 2017 Recommendation cited by published CSAPI. |

### 3.2 Other source meanings that must not disappear into “product model”

These rows are equally important contributions, not obstacles that later donors must overcome. The two OPC rows retain an explicit rejection of one proposed equivalence. The other source-specific findings remain qualified comparisons; they are not silently converted into new alignment records.

| Donor and native term | What the source describes | Contribution or alternative role | Qualification that must survive |
| --- | --- | --- | --- |
| **IEEE 1451** — Meta and Transducer Channel Transducer Electronic Data Sheets (TEDS) ([source](#source-ieee)) | Module/channel self-description, including technical characteristics and potentially unit-specific identification or calibration. | **Partial overlap / different scope:** a description needs an identified subject and applicability, not merely a “type” label. | A TEDS is not automatically a reusable whole-product description. Public Playground material is usable technical evidence; exact uninspected normative requirements remain unverified. |
| **Integrated Sensor Architecture (ISA)** — Component Capability Description ([source](#source-isa)) | Declared Properties, Observables and Commands of an interface participant. | **Different scope:** capability description contributes information distinct from manufacturer product designation. | A declared capability bin is not a manufactured kind, physical assembly or current operating state. |
| **OPC Unified Architecture (OPC UA) Devices** — nameplate `Model` ([source](#source-opc)) | Manufacturer model-identifying metadata, separate from serial/instance identity and structural typing. | **Partial overlap:** the designation can identify a kind without supplying its complete specification. | No datasheet URL or complete kind description follows from a string. An unsupported empty value must remain empty. |
| **OPC UA Devices** — `DeviceType` ObjectType ([source](#source-opc)) | The structure of a device's OPC UA representation. | **Rejected direct equivalence:** `DeviceType` must not be mapped directly to “manufacturer product model.” Retain its interface-typing role. | This rejects one mapping, not the donor. A possible model place for interface typing remains open. |
| **SAPIENT v2** — `ConfigurationData.model` versus `NodeDefinition.node_type` ([source](#source-sapient)) | A manufacturer model designation versus a participant's sensing modality or architectural role. | **Partial overlap / different scope:** product name and modality/role must remain distinct. | A seismic role is not a product model or a CSAPI `systemKind` reference by itself. No physical unit is authenticated by the example or sender role. |
| **The Open Group Sensor Open Systems Architecture (SOSA)** — `Product`, `ProductInstance`, `Component_` ([source](#source-open-group)) | Manufactured product and its association to a functional component in the cited domain-specific data model. | **Partial overlap / different scope:** manufactured realization and functional role are related but distinct. | The source relation is not a universal product-kind/whole-System relationship. Keep 2022 data-model and 2023 architecture editions distinct. |
| **W3C Web of Things (WoT)** — Thing Model ([source](#source-wot)) | Reusable interaction capabilities and metadata that can support a particular Thing Description. | **Partial overlap:** reusable information, specifically an interaction template. | A network-interaction template is not necessarily a manufactured-equipment datasheet. Thing Description 1.1 is recorded companion evidence outside the frozen artifact list. |

SOSA/SSN in §3.1 means the W3C/OGC Sensor, Observation, Sample, and Actuator / Semantic Sensor Network work. It is a different lineage from The Open Group SOSA in §3.2. Combining them because of the shared acronym would falsify the donor trail.

## 4. How the current synthesis follows — and what is still a choice

The existing argument has three parts. First, CSAPI, SAREF and AAS provide explicit kind/type-versus-individual distinctions; SensorML and the recorded SSN draft provide related but differently scoped mechanisms. Second, OPC UA and WoT show why a structural type or interaction template cannot be assumed to be a physical product specification. Third, the SAPIENT, ISA, IEEE and Open Group findings add modality, capability, technical-description scope and manufactured/functional relationships that the phrase “product model” would otherwise conceal.

**The resulting candidate conclusion is narrower than “all these are ProductModel.”** Preserve what a description is about and the role it plays, while keeping shared descriptive information separate from facts about a particular unit. This restates the existing synthesis in [original reconciliation R09-02/03](../Donor_Alignment/09_Cross_Concept_Reconciliation.md) and [later reconciliation F-02 / DC05-S02 / DC05-G03](../Donor_Challenge/05_Challenge_Reconciliation.md); it is not a new donor consensus or completed transformation.

| Question | What the current record supports | What remains open |
| --- | --- | --- |
| Is a kind/model description the individual equipment? | No; their roles must be distinguished. | How a real individual is linked to the correct applicable description and version. |
| Should all donor notions become one `ProductModel` class? | No such equivalence has been justified; one specific OPC shortcut is rejected. | Whether separate description roles, qualified relationships, specialized types, or another structure best represents the evidence. None is selected here. |
| Are technical data sheets always reusable type information? | No; the IEEE findings can include channel/unit-specific identification or calibration. | How mixed applicability is represented without inventing additional facts. |
| Does shared information establish installed configuration or current readings? | No. | Actual unit/configuration/record evidence and later equipment mappings. |
| Can we impose one source's multiplicity, inheritance or protocol? | Not from the comparison alone. | Explicit DIM rationale and, separately, justified Profile binding requirements. |

For a reader of a future client, the practical consequence is straightforward: a manufacturer designation, interface type and reusable interaction template should not all be presented as the same “model.” That is an evaluation implication of the existing research, not client behavior implemented or tested by this iteration.

## 5. Follow the evidence to its source

The following locators are retained from the inspected V2 records. A primary-source link is not a claim that it was opened or reverified during this consolidation. The public record's evidence ceiling controls, including draft editions, access limits and unresolved source discrepancies. The existing record IDs are retained rather than replaced with a new numbering scheme.

<a id="source-aas"></a>
**AAS:** [Original alignment `ALN-T02-A097-01`](../Donor_Alignment/05_Product_Model_Kind_Alignment_v0.1_28OCT2026.md), IDTA 01001 Part 1, v3.2; [General — Types and Instances](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/annex/general.html) and [Core — AssetInformation](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/core.html). Native asset semantics and the proposed V2 fit are separate claims.

<a id="source-csapi"></a>
**CSAPI:** [Original alignment `ALN-T02-A010-01`](../Donor_Alignment/05_Product_Model_Kind_Alignment_v0.1_28OCT2026.md); [OGC 23-001 v1.0](https://docs.ogc.org/is/23-001/23-001.html), §§9.1, 9.2.2 Table 5 and 13.1. Its source-authored vocabulary column does not resolve the recorded 2017/2026 SSN term discrepancy; no formal ontology equivalence is asserted here.

<a id="source-ieee"></a>
**IEEE 1451:** [Corrected IEEE report, §0 and IE03-S03/S05](../Donor_Challenge/03_IEEE1451_Challenge.md); [Meta TEDS](https://iml.ubi.pt/playground/docs/ieee1451/teds/meta-teds/), [Transducer Channel TEDS](https://iml.ubi.pt/playground/docs/ieee1451/teds/transducer-channel-teds/), and [Optional TEDS](https://iml.ubi.pt/playground/docs/ieee1451/teds/optional-teds/), as 2024-linked technical evidence. Candidate scope interpretation is in reconciliation DC05-S02/G03 and v0.2 §4.2. Exact uninspected normative requiredness/cardinality is not supplied by this table.

<a id="source-isa"></a>
**ISA:** [Structural-donor report, ISA04-S04](../Donor_Challenge/04_Other_Structural_Challenges.md); *Software Design Document* 6.0 revision 5, §5.1.1, and *Data Model Specification* 6.0 revision 12, §2, both 31 October 2023. The report supplies original document/section provenance; no public original-file URL is invented.

<a id="source-opc"></a>
**OPC UA Devices:** [Original alignments `ALN-T02-A104-01` and `ALN-T02-A104-02`](../Donor_Alignment/05_Product_Model_Kind_Alignment_v0.1_28OCT2026.md); [Part 100, Devices](https://reference.opcfoundation.org/specs/OPC-10000-100/full), recorded edition v1.05.0, §4.5.2 `IVendorNameplateType` and §4.7 `DeviceType`, Table 35. The source URL is not asserted immutable. The rejection applies only to the direct product-model equivalence.

<a id="source-sapient"></a>
**SAPIENT:** [SAPIENT report, S2-N02 and F-02](../Donor_Challenge/02_SAPIENT_Challenge.md); BSI Flex 335 v2.0:2024-03, §§6.2.5.1–.2 and 6.2.5.15, Tables 17–18/32; [official `registration.proto` at recorded commit 244a741](https://github.com/dstl/SAPIENT-Proto-Files/blob/244a741c13bcee628f84944aef91e4a66854bd7d/bsi_flex_335_v2_0/registration.proto). The separate BSI/protobuf field-number discrepancy remains unresolved, not repaired by a conceptual comparison.

<a id="source-saref"></a>
**SAREF:** [Original alignment `ALN-T02-A144-01`](../Donor_Alignment/05_Product_Model_Kind_Alignment_v0.1_28OCT2026.md); [SAREF Core 4.1.1](https://saref.etsi.org/core/v4.1.1/), “Device kinds and devices,” `DeviceKind`, `hasDeviceKind`, `hasModel`, `hasManufacturer`. The project proposes reuse of the distinction, not import of all ontology axioms.

<a id="source-sensorml"></a>
**SensorML:** [Original alignment `ALN-T02-A013-01`](../Donor_Alignment/05_Product_Model_Kind_Alignment_v0.1_28OCT2026.md); [OGC 23-000 v3.0](https://docs.ogc.org/is/23-000/23-000.html), §§7.2 and 8.2.9.3, Requirements 13–15. The source's process inheritance obligations are not general DIM obligations.

<a id="source-ssn"></a>
**W3C/OGC SOSA/SSN:** [Original alignment `ALN-T02-A019-01`](../Donor_Alignment/05_Product_Model_Kind_Alignment_v0.1_28OCT2026.md); [21 October 2026 Working Draft](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/), §8.16 “Systems Types and Individuals.” This is the specifically recorded draft perspective, not an assertion about the 2017 edition or later releases.

<a id="source-open-group"></a>
**The Open Group SOSA:** [Structural-donor report, SOSA04-S04](../Donor_Challenge/04_Other_Structural_Challenges.md); *SOSA Domain-Specific Data Model*, Edition 1.0, April 2022, §§1.1.3.15, .82–83; architecture Edition 1.1, 2023, is separate contextual evidence. Native ProductInstance association does not establish a universal DIM relationship or multiplicity.

<a id="source-wot"></a>
**WoT:** [Original alignment `ALN-T02-A132-01` and ISSUE-T02-01](../Donor_Alignment/05_Product_Model_Kind_Alignment_v0.1_28OCT2026.md); [WoT Architecture 1.1](https://www.w3.org/TR/wot-architecture11/), §§3, 6.1.1.2 and 7.1; [Thing Description 1.1](https://www.w3.org/TR/wot-thing-description/), §9.1. Both are recorded as 5 December 2023 Recommendations; the second remains companion evidence outside the frozen 182-artifact inventory, not an invented new inventory ID.

## 6. Work boundary and continuation

**What is populated:** one candidate-meaning/relationship example, covering the eight original product/model/kind alignment records and the four later donor contributions recorded against that subject. The donor page covers the 30 previously screened lineages and makes open contributions visible. The rest of the central comparison and all equipment mapping remain unstarted; source/claim checking in this iteration is not the plan's final verification.

This page does not rank donors, declare a final chassis, decide that the five meanings must survive unchanged, or turn an unrepresented question into an adopted concept. Historical source records and candidate v0.2 remain unchanged. Power and TRSS/OmniSense have no preferred role in this presentation.

**Next separate “proceed”: Iteration 2 — populate the broader concept-and-relationship comparison and donor view from existing V2 findings, preserving alternatives and contributions without a settled model destination.** Equipment mapping remains Iteration 3; verification and the next-subject recommendation remain Iteration 4.
