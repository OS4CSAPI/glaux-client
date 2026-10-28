# Donor Alignment — Step 05: Product / Model / Kind

**Version:** 0.1 · **28 October 2026**  
**Plan:** [Controlled Donor Alignment and Foundational DIM Construction](../PLAN_DIM_Profile_V2_Donor_Alignment_and_Foundation_v0.1_28OCT2026.md), **Step 05 only**  
**Standing:** **Completed, bounded, evidence-qualified alignment of previously researched candidate meaning. NOT an adopted DIM concept/class, an accepted module, a normative CSAPI application Profile, or a demonstrated translation/interoperability result.**  
**Branch:** `OS4CSAPI/glaux-client` / `research/dim-profile-v2`; no application code, fixtures, frozen 182-artifact source ledger or deployed site changed.  
**Controlling research:** [Canonical Concept Pass 2](../DIM_Profile_V2_Canonical_Concept_Pass2_Product_Model_Kind_v0.1_26OCT2026.md), [five-pass checkpoint](../DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md), [C08 source correction](../DIM_Profile_V2_Anatomy_PhaseA_Validation_Audit_v0.1_26OCT2026.md), [Step 02 register method](02_Register_Method_and_Schema.md), [Step 03 frozen accountability snapshot](03_Source_Accountability_Register.csv), and [Step 04 individual identity alignment](04_Individual_System_Identity_Alignment_v0.1_28OCT2026.md).

## 1. Finding: reusable descriptions are real, but "model" does not mean the same thing in every donor

**Question:** How do we describe the *reusable kind, product model, generic process or interaction/ontology type* of an individual sensing-equipment System, without confusing that information with a **specific unit**, a **Method**, its **selected configuration**, or its **observed state**?

The independently useful conclusion from the source corpus is a **qualified distinction**, not a new V2 `ProductModel` class:

> **A particular sensing-equipment System may have reusable descriptive information that characterizes what kind of system it is, independently of the individual system's identity, selected configuration, deployment or actual activity. But a manufacturer product specification, process inheritance target, ontology type/class, device-kind description, industrial type asset, information-model ObjectType, and Web interaction template have different source-defined meanings; they cannot be treated as one interchangeable kind resource without a verified mapping of those meanings.**

This is **V2 researcher synthesis**, not text jointly promulgated by the donors. It is source-grounded by [Pass 2](../DIM_Profile_V2_Canonical_Concept_Pass2_Product_Model_Kind_v0.1_26OCT2026.md), with the exact donor comparisons below. **Do not infer one universal Type/Kind class, mandatory association, global cardinality or inherited-configuration rule** from this result.

For the future UI, the practical requirement *question* is: can a profile-aware client show **documented model capabilities and available options** separately from **the particular unit's installed configuration, observed health and history**, without guessing which source description was supplied?

**Reviewed inventory:** **seven frozen artifact IDs** (**10, 13, 19, 97, 104, 132, 144**) representing seven named standard/semantic lineages and **eight alignment records** (the OPC UA artifact needs two, one explicitly rejecting a tempting false equivalence). These are **seven source artifacts, not seven independent votes**: CSAPI/SensorML/SOSA/SSN have explicit standard relationships, and W3C WoT Architecture refers to an additional **out-of-corpus** Thing Description specification. No other one of the 182 sources is globally excluded. The word **“reviewed”** here means the **specific concepts/clauses** identified below, *not* that all seven source standards were independently audited in full.

## 2. Topic identity, source standing and decision controls

**Local research topic:** `TOPIC-02-PRODUCT-MODEL-KIND`.  
**Candidate standing:** `SUPPORTED_FOR_CANDIDATE_DIM` for a *meaning distinction*, **not** a new class, final relationship/multiplicity or adopted ontology alignment.

A repeatable source entry below includes the Step 02 fields: `alignment_id`, `topic_id/candidate_meaning`, `artifact_id/lineage/source_role`, `source_ed/source_concept/source_locator`, `source_native_meaning`, `mapping_direction/relation_kind`, `reused_role/qualification_or_loss`, `evidence_status/source_claim_standing`, `mapping_review_status/adoption_status`, `validation_evidence/compatibility_limit`, `donor_declarations`, `source_to_client_consequence`, `open_question/record_provenance`.

All **positive primary-source notes** use `evidence_status=PRIMARY_TEXT_CHECKED` **only for the named source sections**; the passage's meaning comes from the donor, whereas cross-donor correspondence is `V2_ANALYST_INFERENCE`. Every mapping has `adoption_status=NOT_ADOPTED` and `validation_evidence=NO_TRANSFORMATION_TEST`. Mapping categories are the narrow [Step 02 decision vocabulary](02_Register_Method_and_Schema.md#5-controlled-terminology-what-each-status-means): close alignment with qualification; partial overlap; and, for **one specifically proposed false equivalence**, incompatible/rejected. They **are not** RDF/OWL axioms.

### ALN-T02-A010-01 — CSAPI Part 1 `System.systemKind` → one kind-description `Procedure`

| Field | Evidence-backed value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | `ALN-T02-A010-01` / `TOPIC-02-PRODUCT-MODEL-KIND` / reusable kind is not the individual System or its implementable method. |
| `artifact_id` / `lineage` / `source_role` | **10** / **OGC Connected Systems** / frozen **primary anatomy evidence**; CSAPI is also the intended **future binding**. |
| `source_ed` / `source_concept` / `source_locator` | [OGC API – Connected Systems Part 1 v1.0, OGC 23-001](https://docs.ogc.org/is/23-001/23-001.html), **§9.1 Notes 1–2, §9.2.2 Table 5, §13.1**: `systemKind` versus `procedures` associations. |
| `source_native_meaning` | `System` resources describe **individual systems**. `systemKind` optionally targets **one `Procedure` resource describing the *kind* of System**, such as a datasheet; `procedures` separately identifies **Procedures the System can implement**. Using a `Procedure` resource as the carrier for both roles does **not** equate the roles. |
| `mapping_direction` / `relation_kind` | `CSAPI systemKind semantics → candidate V2 individual-to-kind meaning` / **`CLOSE_ALIGNMENT_WITH_QUALIFICATION`**. |
| `reused_role` / `qualification_or_loss` | Strongest **target-binding precedent** for referring to a reusable description. **Optional single Procedure target** is CSAPI's own association/cardinality, **not an automatically universal DIM relationship or a statement that every donor's kind is a Procedure**. This field does not establish a real model URL, valid physical unit or inherited setting. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for cited CSAPI clauses; `DONOR_TEXT` for the native relationships; `V2_ANALYST_INFERENCE` for candidate V2 reuse. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` **for the relation distinction** / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`. A fitting CSAPI relation is not a source-conversion test, complete donor conformance or a future Profile requirement. |
| `donor_declarations` | `DECL-T02-01` (CSAPI's own `ssn:hasSystemKind` column); `DECL-T02-02` (dated 2017 SSN and SensorML 3.0 normative references). |
| `source_to_client_consequence` | Show **System kind/model documentation** separately from the unit's selected detector/firmware/settings and separate from executable observing Methods. |
| `open_question` / `record_provenance` | How to resolve/version a real kind resource and represent source-specific distinctions in a future Profile; direct clause review on **28 October 2026**. |

**Material source correction retained from C08:** A CSAPI kind description and an implementable Method **may share the `Procedure` API resource type**, but `systemKind` and `procedures` are **different associations with different meanings**. No false "all product models are observing algorithms" mapping is permitted.

### ALN-T02-A013-01 — SensorML 3.0 `typeOf`, simple inheritance, configuration

| Field | Evidence-backed value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | `ALN-T02-A013-01` / `TOPIC-02-PRODUCT-MODEL-KIND` / a reusable process description may characterize and constrain individual configurations. |
| `artifact_id` / `lineage` / `source_role` | **13** / **OGC SensorML** / frozen primary anatomy evidence; implementation/description framework, not necessarily a product-identity ontology. |
| `source_ed` / `source_concept` / `source_locator` | [SensorML Encoding Standard v3.0, OGC 23-000](https://docs.ogc.org/is/23-000/23-000.html), **§7.2 and §8.2.9.3, Requirements 13–15 (`typeOf`, simple inheritance, configuration)**. |
| `source_native_meaning` | A **specific process** may reference a **general process** through the resolvable `typeOf` process link. Under simple inheritance it augments a general process description; with `configuration`, it can restrict options/values. The standard's OEM example distinguishes shared sensor model inputs/outputs/capabilities from serial number, location, calibration and selected settings of a particular unit. This inheritance mechanism applies to **physical and nonphysical processes**, not solely commercial product kinds. |
| `mapping_direction` / `relation_kind` | `SensorML general process/typeOf → candidate V2 reusable-kind relation` / **`PARTIAL_OVERLAP`**. |
| `reused_role` / `qualification_or_loss` | Strong established **process-description and inheritance carrier** for shared equipment model information where actually sourced. **Do not equate any `typeOf` link with a manufacturer's product model**: general process inheritance can express broader behavior/process typing. SensorML's particular `typeOf`/configuration rules are not silently imposed on all future DIM relations or non-SensorML bindings. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for exact official SensorML 3.0 sections; `DONOR_TEXT` native process relations and `V2_ANALYST_INFERENCE` mapping. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for a source-qualified reusable-model distinction / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; no actual `typeOf` link or inherited properties resolved from a TRSS/OmniSense/SCK System by this step. |
| `donor_declarations` | CSAPI's normative SensorML reference and concrete encoding relationship: `DECL-T02-02`; **no declared logical equivalence of `typeOf` and `systemKind`** claimed. |
| `source_to_client_consequence` | A client can distinguish the manufacturer's **allowed modes** from the fielded unit's **selected modes**, and model-level capabilities from actual measurements. |
| `open_question` / `record_provenance` | Inheritance resolution, multiple levels/versions, availability/access rights to model descriptions and encoding-specific behavior; direct source check **28 October 2026**. |

### ALN-T02-A019-01 — SOSA/SSN 21 October 2026 Working Draft: OWL System type vs individual

| Field | Evidence-backed value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | `ALN-T02-A019-01` / `TOPIC-02-PRODUCT-MODEL-KIND` / System type and individual can be distinguished independently of one product registry. |
| `artifact_id` / `lineage` / `source_role` | **19** / **W3C–OGC SOSA/SSN** / frozen primary anatomy evidence. **Do not double-count** the 2017 Recommendation (ID 20) and 12 October 2026 Working Draft (ID 18) as independent endorsements; the 2017 edition remains the one referenced by CSAPI 1.0. |
| `source_ed` / `source_concept` / `source_locator` | [W3C/OGC SSN “2023 Edition,” **21 October 2026 Working Draft**](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/), **§8.16 “Systems Types and Individuals”**; source `sosa:System` ontology class. |
| `source_native_meaning` | A **System type** can be represented as an **OWL Class** (subclass of the appropriate system/sensor class); a **particular System** can be an OWL Individual of that class. The draft explains that model/type specifications often describe many individual instruments. This is an ontology modeling pattern, not itself a manufacturer product catalogue or CSAPI `Procedure` resource. |
| `mapping_direction` / `relation_kind` | `SOSA/SSN system-type class typing → V2 reusable-kind description` / **`PARTIAL_OVERLAP`**. |
| `reused_role` / `qualification_or_loss` | Confirms **type-versus-instance** as distinct semantic levels. **A source's `rdf:type` or OWL subclass assertion is not automatically a product-kind resource, resolved datasheet, `systemKind` link, or commercial model identity**. The Working Draft is **not** the earlier normative SSN edition named by published CSAPI 1.0. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for pinned Working Draft §8.16; `DONOR_TEXT` native OWL representation; `V2_ANALYST_INFERENCE` cross-model reading. |
| `mapping_review_status` / `adoption_status` | `CANDIDATE_RECORDED` for ontology perspective / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; no `owl:equivalentClass`, `rdfs:subClassOf`, formal graph-conversion or 2017↔2026 edition migration asserted by this study. |
| `donor_declarations` | Source is within the SOSA/SSN lineage referenced by CSAPI but **no new cross-edition normative mapping verified here**; see prior [Step 04 ISSUE-T01-01](04_Individual_System_Identity_Alignment_v0.1_28OCT2026.md#issue-t01-01--sosassn-class-iri-and-edition-discrepancy--preserve-do-not-fix). |
| `source_to_client_consequence` | An ontology class such as "temperature sensor type" must not be presented as an authenticated particular product model or individual unit without additional evidence. |
| `open_question` / `record_provenance` | How a future DIM would expose or map formal typing without requiring OWL as its own canonical structure; reviewed **28 October 2026**. |

### ALN-T02-A144-01 — SAREF Core 4.1.1: `DeviceKind` and `hasDeviceKind`

| Field | Evidence-backed value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | `ALN-T02-A144-01` / `TOPIC-02-PRODUCT-MODEL-KIND` / reusable DeviceKind differs from the individual tangible Device. |
| `artifact_id` / `lineage` / `source_role` | **144** / **ETSI SAREF** / frozen primary anatomy evidence. |
| `source_ed` / `source_concept` / `source_locator` | [SAREF Core version 4.1.1, published 31 October 2024](https://saref.etsi.org/core/v4.1.1/), **“Device kinds and devices”** and property **`saref:hasDeviceKind`**; also `saref:hasModel`, `saref:hasManufacturer`. |
| `source_native_meaning` | `saref:DeviceKind` describes kinds/models of Devices with common properties/states/functions/services; `saref:hasDeviceKind` links one `saref:Device` to such a kind. The separate **literal model/manufacturer data properties** are not interchangeable with a resolved `DeviceKind` concept or identity. |
| `mapping_direction` / `relation_kind` | `SAREF DeviceKind / hasDeviceKind → V2 reusable-kind relation` / **`CLOSE_ALIGNMENT_WITH_QUALIFICATION`**. |
| `reused_role` / `qualification_or_loss` | Strong source-native semantic model for **individual → reusable device archetype** and declared common functions/characteristics. **Do not equate the SAREF class to a CSAPI Procedure carrier**, impose the ontology's taxonomic/inheritance axioms on a binding-independent DIM or treat a manufacturer/model text label as a resolvable `DeviceKind`. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for SAREF v4.1.1 passage; `DONOR_TEXT` plus `V2_ANALYST_INFERENCE` for V2 comparison. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for qualified kind relation / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; no proof that a SAREF DeviceKind can be converted losslessly to a CSAPI kind resource, or that implementing one implies conformance to the other. |
| `donor_declarations` | Source directly defines `saref:hasDeviceKind`; **no SAREF-to-CSAPI equivalence declared by the donor**. The source-stated SAREF4SYST relationship is covered by [Step 04 DECL-T01-02](04_Individual_System_Identity_Alignment_v0.1_28OCT2026.md). |
| `source_to_client_consequence` | A profile-aware Details view could present shared product-kind characteristics without converting a SAREF archetype into multiple fictitious fielded devices. |
| `open_question` / `record_provenance` | How to preserve richer SAREF device-kind relationships when the Profile uses CSAPI/SensorML carriers, if actually necessary; checked **28 October 2026**. |

### ALN-T02-A097-01 — AAS Part 1 v3.2: Type Asset, Instance Asset, Shell

| Field | Evidence-backed value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | `ALN-T02-A097-01` / `TOPIC-02-PRODUCT-MODEL-KIND` / reusable industrial asset type is distinguishable from its individual realization. |
| `artifact_id` / `lineage` / `source_role` | **97** / **Asset Administration Shell (AAS)** / frozen primary anatomy evidence; one donor lineage, not several counts for its companion versions. |
| `source_ed` / `source_concept` / `source_locator` | [IDTA 01001, **Part 1: Metamodel v3.2**](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/index.html), [General, “Types and Instances,” particularly “Asset Administration Shells Representing Type Assets and Instance Assets”](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/annex/general.html); [Core, `AssetInformation.assetKind`/`assetType`](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/core.html). |
| `source_native_meaning` | `AssetInformation.assetKind` classifies **Type, Instance, Batch, Role, NotApplicable**. A documented example has **one sensor type asset and two separately identified sensor instance assets**, with shared type attributes but distinct operating measurements; the type/instance relation has industrial lifecycle meaning. `AssetInformation.assetType` refers to the **identifier of the *type asset***, where applicable. The Asset Administration Shell has **its own separate identity** and may relate to other Shells through `derivedFrom`. |
| `mapping_direction` / `relation_kind` | `AAS Type Asset / Instance Asset → V2 reusable-kind/individual distinction` / **`CLOSE_ALIGNMENT_WITH_QUALIFICATION`** for product/equipment asset cases; the complete AAS asset universe is wider. |
| `reused_role` / `qualification_or_loss` | Reuse the **type versus individual realization** distinction, including source lifecycle and evidence about shared versus instance-only values. **AAS `assetType` is not CSAPI `assetType=Equipment`**, and **AAS type asset is not an AAS Shell type/template**. AAS asset kinds are not limited to product kinds; an instance asset need not have a corresponding type asset. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for v3.2 General/Core clauses; donor-native asset types versus V2 synthesis explicitly separated. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for the source-qualified type/instance distinction / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; no AAS↔CSAPI ID reconciliation, digital-shell transfer, shared-type version lookup or physical unit proof. |
| `donor_declarations` | AAS v3.2 metadata identifies aligned internal AAS companion specifications; **no AAS-to-CSAPI/SAREF/OPC equivalence** declared or implied. |
| `source_to_client_consequence` | Show the documented manufacturing-model specifications separately from a particular unit's use/maintenance/measurement records; show Shell/asset identifiers only when their relationships are established. |
| `open_question` / `record_provenance` | Is the source a reusable type asset, a manufacturer string, or a digital description template? How is type inheritance/versioned description resolved? Checked **28 October 2026**. |

### ALN-T02-A104-01 — OPC UA Devices Part 100: product `Model` nameplate value

| Field | Evidence-backed value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | `ALN-T02-A104-01` / `TOPIC-02-PRODUCT-MODEL-KIND` / a manufacturer model designation contributes to kind information, but is not automatically a reusable model specification. |
| `artifact_id` / `lineage` / `source_role` | **104** / **OPC UA Devices/PA-DIM** / frozen primary anatomy evidence; **PA-DIM (ID 103)** is a specialization in the same donor lineage, not an independent instance of this Part 100 proposition. |
| `source_ed` / `source_concept` / `source_locator` | [OPC UA Part 100: Devices v1.05.0 (OPC 10000-100)](https://reference.opcfoundation.org/specs/OPC-10000-100/full), **§4.5.2 `IVendorNameplateType`** and **§4.7 `DeviceType`**. |
| `source_native_meaning` | Device nameplate properties include manufacturer/product **`Manufacturer`, `Model`, `ProductCode`, `DeviceManual`**, and separate particular-unit properties **`SerialNumber`, `ProductInstanceUri`**. A `Model` value is typically identifying metadata, **not automatically a resolvable reusable specification resource**. |
| `mapping_direction` / `relation_kind` | `OPC UA Model/nameplate → V2 reusable-kind description` / **`PARTIAL_OVERLAP`**: a label identifies a kind but need not supply the shared semantic details or links the candidate DIM might accommodate. |
| `reused_role` / `qualification_or_loss` | Keep **manufacturer model-name literal** distinct from physical serial, standardized information-model ObjectType and resolved datasheet. In the source's §4.7, nominally mandatory `Model` on an appropriate DeviceType instance can be an **empty default when not supported**, so an empty value cannot be repaired into a real model identity. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED`, `DONOR_TEXT` on source nameplate/data rules, `V2_ANALYST_INFERENCE` for a possible V2 model linkage. |
| `mapping_review_status` / `adoption_status` | `CANDIDATE_RECORDED` for source-aware metadata contribution / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; no ability to infer model-document URI, product specifications or actual unit association from a string. |
| `donor_declarations` | Internal OPC UA interface/DeviceType relation is **source-native**; no explicitly source-declared equivalence with `CSAPI systemKind` found in the examined clause. |
| `source_to_client_consequence` | A common UI can show "Model: [manufacturer label]" without falsely claiming a complete documented kind definition, and keep serial/instance values separate. |
| `open_question` / `record_provenance` | Do we require a separate profile-governed model-document relation when a label is all that exists? That would be a justified later binding decision, not a new DIM class inferred from the label. Checked **28 October 2026**. |

### ALN-T02-A104-02 — OPC UA Devices `DeviceType` ObjectType **is NOT the product model**

| Field | Evidence-backed value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | `ALN-T02-A104-02` / `TOPIC-02-PRODUCT-MODEL-KIND` / **test and reject** the proposed equivalence "OPC UA `DeviceType` = manufacturer's model/kind description". |
| `artifact_id` / `lineage` / `source_role` | **104**, same independently inspected Part 100 source as `A104-01`; **not an additional donor vote**. |
| `source_ed` / `source_concept` / `source_locator` | [OPC UA Part 100: Devices, v1.05.0](https://reference.opcfoundation.org/specs/OPC-10000-100/full), **§4.7 `DeviceType`, Table 35**, and §4.5.2 model nameplate. |
| `source_native_meaning` | `DeviceType` is an **abstract OPC UA ObjectType defining the structure of a Device's OPC UA representation**; a specific concrete subtype can have instances. `Model` is a **separate nameplate Property**. Standardized AddressSpace typing does not, by itself, prove a manufacturer product-model designation. |
| `mapping_direction` / `relation_kind` | `OPC UA DeviceType ObjectType → V2 manufacturer product model` / **`INCOMPATIBLE` for this proposed direct equivalence only**. The ObjectType is valuable in its **own structural/interface typing role**. |
| `reused_role` / `qualification_or_loss` | **Rejected mapping:** do not transform every `DeviceType` ObjectType assertion into a physical product-kind record/datasheet or conflate it with an individual Device's `Model` attribute. Future model may separately retain *information-model typing* where required. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` and `DONOR_TEXT` for `DeviceType` definition; incompatibility of the attempted **equivalence** is `V2_ANALYST_INFERENCE` from the two native meanings. |
| `mapping_review_status` / `adoption_status` | **`REJECTED_MAPPING`** / `NOT_ADOPTED`. This does **not** mark OPC UA Devices as broadly incompatible with V2. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; non-equivalence is a **semantic distinction** grounded in the inspected standard, not evidence of failed live OPC-UA→CSAPI conversion. |
| `donor_declarations` | No donor-declared CSAPI product-model equivalence in this checked section. |
| `source_to_client_consequence` | Avoid mislabeling an OPC UA structural ObjectType as an equipment manufacturer's model; present available **product identification** and **interface type** distinctly if relevant. |
| `open_question` / `record_provenance` | Does a future separate interface-typing area need this information? Out of scope of Product/Model/Kind alignment; reviewed **28 October 2026**. |

### ALN-T02-A132-01 — W3C WoT Architecture 1.1: `Thing Model` describes interaction capabilities

| Field | Evidence-backed value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | `ALN-T02-A132-01` / `TOPIC-02-PRODUCT-MODEL-KIND` / reusable interface model information is distinct from an individual Thing. |
| `artifact_id` / `lineage` / `source_role` | **132** / **W3C Web of Things** / frozen **primary anatomy evidence** for a reference architecture; **NOT** a claim that W3C WoT Thing Description 1.1 is a separately inventoried artifact. |
| `source_ed` / `source_concept` / `source_locator` | [W3C WoT Architecture 1.1, Recommendation 5 December 2023](https://www.w3.org/TR/wot-architecture11/), **§3 “Thing Model,” §6.1.1.2 “Thing Models,” §7.1 “WoT Thing Description”**. Supplementary direct source, **outside the frozen 182 artifact IDs**: [W3C WoT Thing Description 1.1, Recommendation 5 December 2023](https://www.w3.org/TR/wot-thing-description/), **§9.1 Thing Model**. |
| `source_native_meaning` | `Thing Model` captures reusable **Properties, Actions, Events**, common metadata and interaction capabilities shared by a set of Things, while omitting concrete instance details such as serial, location or protocol address. It can act as a template for an individual `Thing Description`. It is **not necessarily a model of the manufactured hardware or datasheet**. |
| `mapping_direction` / `relation_kind` | `WoT Thing Model → candidate V2 reusable product-kind description` / **`PARTIAL_OVERLAP`**: reusable descriptions overlap, but the WoT model describes **network-facing interaction affordances**, not necessarily manufacturer-defined product type/engineering characteristics. |
| `reused_role` / `qualification_or_loss` | Retain the distinction between **reusable interface capability template** and **instance-specific TD/physical-unit evidence**. Avoid inferring rated sensitivity, hardware serial or model datasheet from the existence of a Thing Model. Different sources' multiplicity/composition constraints cannot be imposed on a general DIM kind relation. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for inventoried W3C Architecture 1.1 and directly accessed supplementary TD 1.1 §9.1; native WoT meanings versus our **`V2_ANALYST_INFERENCE`** held separate. |
| `mapping_review_status` / `adoption_status` | `CANDIDATE_RECORDED` for **interface type perspective**, not a settled physical product mapping / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; no implemented WoT→CSAPI binding, confirmed equivalence with `systemKind`, or complete TD profile. |
| `donor_declarations` | **`DECL-T02-03`**: WoT Architecture 1.1 explicitly refers to WoT Thing Description as the specification of the TD information model/format. **The target TD 1.1 source is not separately present in the 182-row corpus: `ISSUE-T02-01`.** |
| `source_to_client_consequence` | Present a **reusable interaction template** when one is available, without automatically calling it the manufacturer's product model or inferring equipment installed state. |
| `open_question` / `record_provenance` | If future V2 interoperability claims depend on TD 1.1's precise `Thing Model` encoding/constraints, how will that external artifact be admitted and versioned in the donor ledger? Frozen corpus unchanged; reviewed **28 October 2026**. |

## 3. Explicit donor-declared relationships and their **bounded** authority

These are **source declarations, not our invented source-to-source equivalence claims**. Their semantics and target editions matter. Link IDs are local research references and will be revisited at Step 09.

| Declaration | Declaring source and clause | What is actually declared | Target and limits |
| --- | --- | --- | --- |
| **`DECL-T02-01`** | **10**, [CSAPI 1.0 §9.2.2 Table 5](https://docs.ogc.org/is/23-001/23-001.html) | In the published **SOSA/SSN Property** correspondence column, `systemKind` is labeled `ssn:hasSystemKind`. | **Table column correspondence in CSAPI**, not evidence that every cited SSN edition defines that exact property or that `systemKind` is formally equivalent to a commercial product-model ontology class. The 2017 SSN Recommendation and 2026 Working Draft have different editions; see [Step 04 ISSUE-T01-01](04_Individual_System_Identity_Alignment_v0.1_28OCT2026.md#issue-t01-01--sosassn-class-iri-and-edition-discrepancy--preserve-do-not-fix). |
| **`DECL-T02-02`** | **10**, [CSAPI 1.0 §3 Normative References; Annex C.2](https://docs.ogc.org/is/23-001/23-001.html) | The standard formally cites **2017 W3C SSN** (corpus **20**) and **SensorML 3.0** (corpus **13**) as normative references and describes SensorML as an advanced system-description carrier. | Explicit **standard/dependency relation**; not a declared semantic equivalence of `SensorML typeOf` and `CSAPI systemKind`. |
| **`DECL-T02-03`** | **132**, [W3C WoT Architecture 1.1 §§6.1.1.2,7.1](https://www.w3.org/TR/wot-architecture11/) | Architecture defines the relationship of reusable **Thing Model** to instance-oriented **Thing Description**, and cites the **WoT Thing Description** specification for the information model/serialization. | Source-declared **companion specification relationship**, not equivalence with CSAPI/SensorML/SAREF kinds. WoT TD 1.1 is **outside the frozen 182 artifact register**, recorded below, and must not be assigned an invented artifact ID. |

There is **no verified direct declaration in the named clauses** that SAREF `DeviceKind`, AAS Type Asset, OPC UA `DeviceType`, and WoT Thing Model are mutually equivalent or one can be converted without loss to the others. Our conceptual correspondence is explicitly **analyst inference**, not donor consensus. SAREF's separate reference to SAREF4SYST was recorded earlier as [`DECL-T01-02`](04_Individual_System_Identity_Alignment_v0.1_28OCT2026.md).

## 4. New and continuing exceptions, counterexamples and unresolved questions

### ISSUE-T02-01 — W3C WoT Thing Description 1.1 is **not** a separate frozen source artifact

**Verified discovery, not a new donor survey:** The [Step 03 source-accountability register](03_Source_Accountability_Register.csv) has one W3C WoT Architecture 1.1 artifact (**ID 132**) but **no distinct entry for W3C WoT Thing Description 1.1**. Pass 2 nevertheless used [the Thing Description specification](https://www.w3.org/TR/wot-thing-description/) as a source for Thing Model syntax. WoT Architecture is sufficiently explicit to substantiate the high-level distinction in this Step 05; TD 1.1 supplies corroborating normative detail.

**Disposition:** `OUTSIDE_FROZEN_CORPUS` supplementary official source, directly identified by **title, edition and URI**. **Do not add ID 183, reuse an ID, inflate the 182-artifact count, infer malicious omission, or quietly amend the frozen source inventory.** When a future formal WoT mapping or corpus expansion is authorized, explicitly decide whether/how this previously missing separate specification becomes part of the maintained source population. For this step, its absence is a **documented traceability gap**, not a block to the scoped Thing Model comparison.

### ISSUE-T02-02 — four distinct kinds of "type" must remain separate

| Tempting shortcut | Why it would be a mistake |
| --- | --- |
| **An individual System's manufacturer model label = a complete reusable specification** | OPC UA may supply only a literal `Model` or default; neither the URL of a model document nor its attributes follow from that string. |
| **CSAPI `systemKind` `Procedure` = a method the equipment executed** | CSAPI distinguishes kind/datasheet and implementable `procedures` **by association role**, even when both use Procedure resources. No actual execution is inferred. |
| **AAS `assetType` = CSAPI `assetType`** | AAS `AssetInformation.assetType` references a **type asset's ID**, while CSAPI `assetType=Equipment` classifies a **realization**. Same name, different meaning. |
| **OPC UA `DeviceType` ObjectType = product model; or WoT `Thing Model` = product datasheet** | The first is a **standardized representation-structure type**; the second is an **interface/interaction template**. Either can relate to product information but does not, by definition, assert a physical product model. |

**Other open commitments:** Does our DIM need zero, one or several source-qualified kinds/classifications per System? How would kind-document URI/version/inheritance be handled? When multiple representations differ, who asserts the correct relation? A CSAPI Profile may ultimately constrain such matters, but **we cannot derive its SHALLs here**.

### Worked client-fidelity check — no fabricated equipment

- **Smart Citizen Kit 2.3:** The completed [I05 source analysis](../Case_Studies/Real_Equipment_DIM_Validation/I05_Individual_System_and_Product_Kind_Mapping_v0.1_27OCT2026.md) establishes documentation for an **SCK2.3 product generation** and possible options; it **does not prove** that a particular Kit instance is fielded, which options are installed or how its hardware ID joins a platform record. A source-aware client can show **documented product kind**, but not label those values as an actual individual's current settings.
- **TRSS ETU-II:** The existing [Resource Details proof](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/RESOURCE_DETAILS_PROFILE_TEST.md) contains a **synthetic historical** example with selected detector slots and possible detector choices. **Supported alternatives (kind/capability-level evidence) are not the selected installed configuration**; do not infer separate authenticated detector IDs.
- **OmniSense Core2/Core5ADS:** Source-reported transducer labels and historical voltage are **two distinct synthetic cases**, not proof of one individual with one complete model specification. A source-specific label is not a resolvable type description.

**Future profile/client question, not an implemented requirement:** Can different producer systems expose a **qualified kind-description role** to a CSAPI Profile-aware client so it can label the information accurately ("manufacturer model," "ontology type," "process inheritance," "interface template," or "model name only"), while retaining actual unit settings/state and unknowns separately? No source→profile→client transformation was performed in Step 05.

## 5. Step 05 acceptance, limits and next action

| Exit check | Step 05 result |
| --- | --- |
| One concept-family question only | **YES** — `TOPIC-02-PRODUCT-MODEL-KIND`; Procedure/Method work reserved for Step 06 |
| Frozen IDs and source/edition lineage | **YES** — seven **inventoried** source IDs **10, 13, 19, 97, 104, 132, 144**, with eight source-concept mappings; the TD source is explicitly **outside corpus** |
| Exact qualified donor-native semantics | **YES** — primary source sections listed per record, with narrow source-native meaning separated from V2 interpretation |
| Comparison direction and non-equivalence | **YES** — `CLOSE_ALIGNMENT_WITH_QUALIFICATION`, `PARTIAL_OVERLAP`, and one specifically **`REJECTED_MAPPING`** for DeviceType≠manufacturer product model |
| Donor-to-donor source declarations versus our interpretations | **YES** — three scoped references, **no inferred universal donor equivalence** |
| Identity, version, multiplicity, actual-state and source-data limits | **PRESERVED** — empty OPC model possibility, AAS `assetType` collision, normative 2017 versus WD 2026, unresolved model URI and hardware/product joins |
| Positive transform or real CSAPI implementation | **NONE** — `NO_TRANSFORMATION_TEST` for all records |
| New DIM class, module, profile SHALL, client change | **NONE** — all `NOT_ADOPTED` |

**What earns advancement toward the published DIM:** A reusable-kind-to-individual distinction is technically defensible and has traceable donor roots, **provided the model continues to distinguish the nature and authority of a source's "kind" information and does not fabricate a uniform kind class or resource**. This makes the eventual Profile able to express source knowledge more truthfully and can prevent client-facing loss/misclassification. It **does not yet prove lossless donor compatibility or implement a DIM**.

**Source-review limit:** The exact online standard editions/clauses cited above were checked for this step. Other portions of those standards, the rest of the 182 artifacts, licensed/blocked sources, and actual vendor hardware are **not** blanket verified by this finding. The original Phase A donor triage and Pass 2 research remain the broader starting evidence; no quarantined anatomy decision has been used as model authority.

**Next, only after a new user “proceed”: Step 06 — Procedure / Method donor alignment.** Preserve the distinction between supported Method, System kind, actual execution/result, and the different ways donors express each. Do **not** conduct Step 06 as part of this step or adopt any new Profile requirements.
