# Donor Alignment — Step 04: Individual System Identity

**Version:** 0.1 · **28 October 2026**  
**Plan:** [Twelve-step donor alignment and DIM foundation plan](../PLAN_DIM_Profile_V2_Donor_Alignment_and_Foundation_v0.1_28OCT2026.md), **Step 04 ONLY**  
**Status:** **COMPLETE as a bounded, sourced concept-alignment exercise**, including one unresolved Open Group SOSA comparison and a version-sensitive SOSA/SSN nomenclature conflict. No DIM class/property has been adopted, no application-Profile obligation specified, and no data transformation or runtime interoperability tested.  
**Repository/branch:** `OS4CSAPI/glaux-client` / `research/dim-profile-v2`. **No client/UI code or original 182-row frozen source is changed by this alignment note.**  
**Prior analysis:** [Pass 1 — Individual System Identity](../DIM_Profile_V2_Canonical_Concept_Pass1_Individual_System_Identity_v0.1_26OCT2026.md), [five-pass synthesis](../DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md), [Step 02 register method](02_Register_Method_and_Schema.md), [Step 03 source accountability register](03_Source_Accountability_Register.csv).  
**Work scope:** One semantic question, **not** Step 05 Product / Model / Kind. The latter appears below only when an identity-versus-kind distinction prevents a wrong identification.

## 1. Outcome in ordinary language

**Which thing are we actually describing?** The emerging DIM needs to describe an **individual, real-world sensing-equipment System** as distinct from the names, product models, API resources, software records, observations and other information that can describe it. Our current working focus is equipment-realized Systems whose primary role is sensing, while the full DIM domain name/root class remains open.

The strongest common evidence is a real **individual versus description/identifier/type** distinction; it is **not** evidence that the donor communities use identical definitions of `System`, `Device`, `Asset`, or `Sensor`. **No new `IndividualSystem` class is justified by this result.** The right course is to preserve the existing individual identity meaning, record qualified donor mappings and explicitly reject automatic one-to-one equivalence across systems or digital records.

**Seven primary-source/lineage records are considered** below: **six directly inspected, source-specific comparisons** (CSAPI Part 1, 2017 SOSA/SSN, 2026 SOSA/SSN Working Draft, SAREF Core, AAS, and OPC UA Devices) and **one explicitly deferred Open Group SOSA whole-Sensor architecture comparison** based on earlier cited research rather than a newly reviewed clause. The historical corpus has 182 artifacts; this selection is **not** a ranking, a claim that the other 175 are irrelevant, or seven independent votes. AAS, SAREF, OPC and W3C/OGC SOSA/SSN each cover partly different real-world domains and representation contracts.

**Two precise cautions emerge:**
1. CSAPI 1.0 normatively cites the **2017 W3C/OGC SSN Recommendation**. The 2017 source defines **`ssn:System`**, while the **21 October 2026 Working Draft** defines **`sosa:System`**. Published CSAPI Part 1's own prose uses both names in different locations. **Do not silently equate the IRIs or import the later Working Draft into the published 2025 standard's normative dependencies**; see §5.
2. CSAPI `uniqueIdentifier` is a required URI-valued attribute. The standard requires server-level UID uniqueness/URI validity and **recommends** global uniqueness; it **should** be persistent and separate from the resource URL. This does **not** establish a universal lifetime hardware identity or permit merging two vendor records just because they have the same model.

## 2. Narrow candidate meaning and register conventions

### TOPIC-01-INDIVIDUAL-SYSTEM

> **Candidate V2 meaning, for review:** The individual System is the particular real-world subject described by sensing-equipment information. It must be understood separately from (a) its identifying strings and resource addresses, (b) any reusable kind/type description, (c) the Procedures it is capable of performing, (d) individual Observations or other Executions and results, and (e) the digital descriptions, servers, software associations or proxies through which the subject appears. Configuration, state, location, deployment, records and source representation may change without *automatically* establishing a new individual. **Whether identity continues through major component replacement, repair or re-registration is deliberately unresolved.**

This is **project synthesis**, based on [Pass 1 §2](../DIM_Profile_V2_Canonical_Concept_Pass1_Individual_System_Identity_v0.1_26OCT2026.md), **not verbatim donor text**. Its present CSAPI-relevant scope is the working `systemType=Sensor` + `assetType=Equipment` *pair of classifications*; the combination **does not create a new source-standard class or DIM root**.

**All mapping entries below use the Step 02 method.** IDs beginning `ALN-`, `DECL-` and `ISSUE-` are **local research keys**, not DIM concept identifiers or vocabulary URIs. The standardized relationship labels remain owned by their donors.

**Status key:** `PRIMARY_TEXT_CHECKED` means a narrow section in the exact edition was inspected for this task, not a full standard audit. `PRIOR_CITED_RESEARCH` does not claim this iteration independently verified the primary source. `SUPPORTED_FOR_CANDIDATE_DIM` permits use as *qualified candidate manuscript material*, not adoption. All **`adoption_status=NOT_ADOPTED`**. All **`validation_evidence=NO_TRANSFORMATION_TEST`**.

## 3. Donor concept-to-candidate alignments — scoped and directional

### ALN-T01-A010-01 — OGC API – Connected Systems Part 1: individual `System` resource and UID

| Step 02 field | Recorded value |
| --- | --- |
| `alignment_id`, `topic_id`, `candidate_meaning` | `ALN-T01-A010-01` / `TOPIC-01-INDIVIDUAL-SYSTEM` / the particular subject is not its product kind, API record, URL or data history. |
| `artifact_id`, `lineage`, `source_role` | **10**, `OGC Connected Systems`, **primary anatomy evidence** (frozen historical classification). |
| `source_ed`, `source_concept`, `source_locator` | **OGC 23-001 v1.0 (16 July 2025)**, `System` instance, `uniqueIdentifier`, `systemType`, `assetType`, `systemKind`. [Official CSAPI Part 1](https://docs.ogc.org/is/23-001/23-001.html) **§§8.4–8.5, 9.1–9.3; Tables 4–7**. |
| `source_native_meaning` | A `System` resource **describes an instance** (e.g. one instrument), with a required **URI-valued** UID and a canonical API URL; the local resource ID is a separate scope. `System` has separate required `systemType` and optional `assetType` facets, and optional `systemKind` association for its reusable type description. The standard requires uniqueness of resource UIDs **across one server's collections** and recommends global uniqueness. |
| `mapping_direction` / `relation_kind` | `CSAPI System-instance/identity meanings → candidate V2 individual-System distinction` / **`CLOSE_ALIGNMENT_WITH_QUALIFICATION`**. |
| `reused_role` / `qualification_or_loss` | Retain individual-versus-description, UID-versus-resource ID/URL, and role (`Sensor`) versus realization (`Equipment`) distinctions. **CSAPI endpoint, field/URI syntax, local ID uniqueness and optional association cardinalities are *binding rules*, not automatically binding-independent DIM rules.** `uniqueIdentifier` being required is NOT an unconditional hardware lifetime/replacement rule. |
| `evidence_status` / `source_claim_standing` | **`PRIMARY_TEXT_CHECKED`** for the listed 2025 clauses and `DONOR_TEXT` for their own semantics; `V2_ANALYST_INFERENCE` for any cross-service identity interpretation. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` **for the narrow distinction only** / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; strong CSAPI-native anchor for a **future** binding, not proof of source-system→CSAPI↔client conversion or profile conformance. |
| `donor_declarations` | `DECL-T01-01` (Part 1 explicitly cites **2017 SSN** normatively and claims a System resource implements SSN/SOSA concepts). **`ISSUE-T01-01`** records the edition/term problem. |
| `source_to_client_consequence` | A common Details view should show **the individual subject and its actual source identifiers**, not turn a product designation or a resource URL into an equipment UID. |
| `open_question` / `record_provenance` | Physical identity correlation across servers, replacements and source-native serial numbers not resolved; source sections checked in this Step 04 on **28 October 2026**. |

**Extra binding-level care:** In Part 1 **§8.5**, server uniqueness and URI validity are requirements; `SHOULD` global uniqueness and `should` persistence should not be rewritten as universal `SHALL`. Part 1 **§9.1** provides Sensor+Equipment examples; the class/tagging mechanics do not make a new subclass of `System` in our DIM.

### ALN-T01-A020-01 — SOSA/SSN 2017 Recommendation: `ssn:System`

| Field | Recorded value |
| --- | --- |
| `alignment_id`, `topic_id`, `candidate_meaning` | `ALN-T01-A020-01` / `TOPIC-01-INDIVIDUAL-SYSTEM` / recognize distinct real-world System individuals, without inheriting all ontology classes. |
| `artifact_id`, `lineage`, `source_role` | **20**, `SOSA/SSN`, **companion/lineage evidence** (older normative edition cited by CSAPI 1.0, not an independent source-family vote). |
| `source_ed`, `source_concept`, `source_locator` | **W3C Recommendation, 19 October 2017**, `ssn:System` (`http://www.w3.org/ns/ssn/System`); [2017 Semantic Sensor Network Ontology](https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/), **§4.9.2.4**; `ssn:implements`, `ssn:hasSubSystem`, `ssn:hasDeployment` in §§4.8–4.9. |
| `source_native_meaning` | `ssn:System` is a **unit of abstraction for pieces of infrastructure implementing Procedures**; it can have subsystems that are also Systems. The 2017 ontology separately describes Sensors, Actuators and Samplers and their procedures and deployments. |
| `mapping_direction` / `relation_kind` | `2017 ssn:System → candidate V2 individual sensing-equipment System` / **`SOURCE_BROADER`**. The ontology System scope is not restricted to the equipment-realized sensing case. |
| `reused_role` / `qualification_or_loss` | Shared domain importance of a System subject distinct from its operations and constituents. **Do not replace `ssn:System` with `sosa:System` merely because the later Working Draft moved to that IRI.** The ontology form/OWL entailments are not silently adopted by the DIM. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` / `DONOR_TEXT` for 2017 vocabulary; `V2_ANALYST_INFERENCE` for the V2 boundary comparison. |
| `mapping_review_status` / `adoption_status` | `CANDIDATE_RECORDED` / `NOT_ADOPTED`; older version's intended cross-edition mapping remains an open detail. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; no claim of graph, ontology or inference-rule equivalence between 2017 and 2026 editions. |
| `donor_declarations` | Referenced explicitly by the **published CSAPI Part 1** standard: `DECL-T01-01`. |
| `source_to_client_consequence` | Do not assume a class IRI found in an older source has the same current versioned vocabulary meaning; a client should interpret the actual declared source/profile vocabulary and context. |
| `open_question` / `record_provenance` | `ISSUE-T01-01`: which precise class/property URI and qualified mapping is appropriate for future V2 formal alignment? Checked 2017 original on **28 October 2026**. |

### ALN-T01-A019-01 — SOSA/SSN 21 October 2026 Working Draft: `sosa:System` and type/individual distinction

| Field | Recorded value |
| --- | --- |
| `alignment_id`, `topic_id`, `candidate_meaning` | `ALN-T01-A019-01` / `TOPIC-01-INDIVIDUAL-SYSTEM` / an individual System is a particular instance, distinct from a type and from its Executions. |
| `artifact_id`, `lineage`, `source_role` | **19**, `SOSA/SSN`, historical **primary anatomy evidence**; same **semantic lineage** as ID 20 (2017) and ID 18 (earlier October 2026 Working Draft). |
| `source_ed`, `source_concept`, `source_locator` | **W3C Working Draft dated 21 October 2026 (OGC 25-022)**, not a final W3C Recommendation. **Pinned version**: [2026-10-21 WD](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/), **§5.3.5.2.4 `sosa:System`**, **§8.16 “Systems Types and Individuals”**. |
| `source_native_meaning` | `sosa:System` is an Asset implementing a Procedure in an Execution; may be physical infrastructure, a device, a human agent or software. Its **type/model may be an OWL Class**, while an **individual System instance is an OWL Individual** typed by that class. It separates a System from Executions, Platform hosting, Deployment and subsystem associations. |
| `mapping_direction` / `relation_kind` | `2026 sosa:System individual → candidate V2 equipment-realized individual sensing System` / **`SOURCE_BROADER`** (candidate V2 excludes many legitimate non-equipment and non-sensing Systems in the source's full scope). |
| `reused_role` / `qualification_or_loss` | Strong evidence for individual-versus-type and individual-versus-execution distinctions, **not a command to reproduce this OWL class hierarchy or to type CSAPI resource records in RDF**. 2026 Working Draft terms are edition- and status-specific. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` / `DONOR_TEXT` for the pinned Working Draft; `V2_ANALYST_INFERENCE` for the bounded source-to-V2 narrowing. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` **as research evidence only** / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; no accepted RDF/OWL equivalence with 2017 or CSAPI 1.0 and no donor-conformance claim. |
| `donor_declarations` | **No newly validated cross-standard formal equivalence** is asserted here. `ISSUE-T01-01` captures dated editions and CSAPI's 2017 dependency; the draft itself discusses OGC API alignment, but its exact term-by-term mapping is **not resolved by this step**. |
| `source_to_client_consequence` | An instrument model page or shared kind specification must not masquerade as **the actual fielded System**, and an Observation must not become its identifying record. |
| `open_question` / `record_provenance` | Which subset of ontology typing/relationships is needed for V2 without over-restricting the DIM? Primary text checked on **28 October 2026**. |

### ALN-T01-A144-01 — SAREF Core 4.1.1: `saref:Device` is one real entity, `DeviceKind` is not it

| Field | Recorded value |
| --- | --- |
| `alignment_id`, `topic_id`, `candidate_meaning` | `ALN-T01-A144-01` / `TOPIC-01-INDIVIDUAL-SYSTEM` / tangible individual identity is separate from device kind. |
| `artifact_id`, `lineage`, `source_role` | **144**, `SAREF`, primary anatomy evidence. |
| `source_ed`, `source_concept`, `source_locator` | **ETSI SAREF Core 4.1.1**, 31 October 2024, [official versioned ontology](https://saref.etsi.org/core/v4.1.1/), **“Device kinds and devices”**, `saref:Device`, `saref:DeviceKind`, `saref:hasDeviceKind`. |
| `source_native_meaning` | A `saref:Device` is a **tangible object designed to accomplish tasks through functions**; an instance denotes **one specific real entity**. `saref:DeviceKind` captures reusable kinds. SAREF states that Devices also are `s4syst:System`, referring to its separately published SAREF4SYST framework; it also treats Devices as Features of Interest. |
| `mapping_direction` / `relation_kind` | `SAREF individual Device → candidate V2 individual sensing-equipment System` / **`PARTIAL_OVERLAP`**: the overlap is a particular tangible functional device with a sensing role. SAREF also covers many non-sensing Devices, while a V2 composite sensing-equipment System is not necessarily one SAREF Device at the same granularity. Neither source concept is assumed to subsume the other. This is **bounded interpretation**, not an OWL assertion. |
| `reused_role` / `qualification_or_loss` | Preserve tangible **device instance ≠ device kind**. Do not impose SAREF's `DeviceKind`, `FeatureOfInterest` or `s4syst:System` class graph as the DIM's root hierarchy, and do not assume the original source provides hardware serial/identity reconciliation. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` / `DONOR_TEXT` for the cited versioned SAREF text; `V2_ANALYST_INFERENCE` for alignment with equipment sensing Systems. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for its individual-versus-kind contrast / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; no universally compatible SAREF→CSAPI mapping or SAREF conformance established. |
| `donor_declarations` | `DECL-T01-02` notes the **source-stated SAREF4SYST** relationship; its external dependency's exact version and a V2 formal ontology mapping are **NOT VERIFIED** in this step. |
| `source_to_client_consequence` | Display **a particular vendor device** separately from the reusable device catalogue/model; avoid fabricating an individual from a generic model or product list. |
| `open_question` / `record_provenance` | Whether a particular composite sensing System and internal parts should be separate SAREF Devices (or be represented differently) is Step 07 territory; checked on **28 October 2026**. |

### ALN-T01-A097-01 — AAS Part 1: represented Asset versus Administration Shell and their IDs

| Field | Recorded value |
| --- | --- |
| `alignment_id`, `topic_id`, `candidate_meaning` | `ALN-T01-A097-01` / `TOPIC-01-INDIVIDUAL-SYSTEM` / the physical subject is not the digital Shell or its identifiers. |
| `artifact_id`, `lineage`, `source_role` | **97**, `Asset Administration Shell`, primary anatomy evidence. |
| `source_ed`, `source_concept`, `source_locator` | **IDTA 01001, Part 1: Metamodel, v3.2 (July 2026)**, [official version index](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/index.html), [“Overview Metamodel”](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/overview.html), [“Core Classes” → “Asset Administration Shell Attributes” and “Asset Information Attributes”](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/core.html). |
| `source_native_meaning` | A uniquely identifiable `AssetAdministrationShell` **represents** an Asset; its `AssetInformation` refers to the represented Asset and distinguishes `assetKind` values **Type**, **Instance**, **Batch**, **Role**, **NotApplicable**. The Shell's own ID is distinct from the Asset's `globalAssetId` / `specificAssetId`. Constraint **AASd-131** requires `globalAssetId` **or at least one `specificAssetId`**; a global ID may be temporarily absent in an early lifecycle stage. A specific ID can be domain/proprietary scoped. |
| `mapping_direction` / `relation_kind` | `AAS represented instance Asset vs Shell → candidate V2 individual subject vs digital representation` / **`PARTIAL_OVERLAP`**. Asset and AAS concepts cover other kinds and digital realization mechanics; V2 System sensing role is absent from this identity pattern alone. |
| `reused_role` / `qualification_or_loss` | Keep **Asset identity distinct from Shell identity**, keep type versus instance semantics when sourced, and retain scoped identifiers. Do **not** treat `globalAssetId` as universally compulsory at all times or equate AAS `assetType` (reference to type asset) with CSAPI `assetType=Equipment` (asset-realization classification). |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` / `DONOR_TEXT` for exact v3.2 clauses; `V2_ANALYST_INFERENCE` for how the distinction may inform our DIM. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for *identity/representation separation only* / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; no AAS asset ID ↔ actual physical equipment ↔ CSAPI UID join verified. |
| `donor_declarations` | No external donor equivalence promoted; AAS references its own aligned companion specifications in the v3.2 index. Detailed inter-donor dependency is not needed for this topic. |
| `source_to_client_consequence` | A client can distinguish **the actual described equipment** from the manufacturer's/enterprise's digital shell and its local/account-scoped identifiers, once the link is evidence-backed. |
| `open_question` / `record_provenance` | Who asserts and verifies physical asset ID correlation, especially where multiple systems publish differing identifiers? Exact source content checked **28 October 2026**. |

### ALN-T01-A104-01 — OPC UA Part 100: physical Device identity versus address-space representation

| Field | Recorded value |
| --- | --- |
| `alignment_id`, `topic_id`, `candidate_meaning` | `ALN-T01-A104-01` / `TOPIC-01-INDIVIDUAL-SYSTEM` / physical individual identity and digital Node references are separate concerns. |
| `artifact_id`, `lineage`, `source_role` | **104**, `OPC UA Devices / PA-DIM`, primary anatomy evidence; **PA-DIM specialization (ID 103) is not an additional independent vote** for this particular Device identity conclusion. |
| `source_ed`, `source_concept`, `source_locator` | **OPC UA Part 100: Devices v1.05.0 (OPC 10000-100)**, [official full standard](https://reference.opcfoundation.org/specs/OPC-10000-100/full), **§3.1.5 Device; §3.3.2 NodeIds; §4.5.2 IVendorNameplateType; §4.9 DeviceSet**. |
| `source_native_meaning` | A Device is an **independent physical entity** capable of specified functions and delimited by interfaces; a Device may itself comprise Devices/components. The nameplate separates product-specific `Model`/`ProductCode` from instance-specific `SerialNumber`/`ProductInstanceUri`. OPC UA's `NodeId` and `DeviceSet` concern the server's AddressSpace representation, not a proof that two Nodes from separate servers refer to one physical item. |
| `mapping_direction` / `relation_kind` | `OPC UA physical Device / nameplate individual identification → candidate V2 sensing-equipment individual System` / **`PARTIAL_OVERLAP`**. A Device can be non-sensing, one constituent of a sensing whole, a gateway, or the whole; source does not force one universal V2 System scale. |
| `reused_role` / `qualification_or_loss` | Preserve manufacturer/product information versus individual serial/instance references and distinguish equipment from its server Node. **Do not** assert `ProductInstanceUri`, CSAPI `uniqueIdentifier`, and AAS `globalAssetId` are automatically the same ID, or that an OPC UA ObjectType is a manufacturer product model. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` / `DONOR_TEXT` for exact cited Part 100 clauses; `V2_ANALYST_INFERENCE` for V2 subject granularity. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for distinctions / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; no physical-device matching/CSAPI transform or full OPC UA device information model equivalence established. |
| `donor_declarations` | No independently checked normative OPC-UA-to-CSAPI ontology equivalence; do not invent one. |
| `source_to_client_consequence` | Preserve **actual equipment identity and component granularity** rather than displaying OPC UA server Node identity as the fielded equipment serial; distinguish model from unit. |
| `open_question` / `record_provenance` | Device versus subsystem boundary and multi-server correlation remain open. Exact Part 100 text checked **28 October 2026**. |

### ALN-T01-A049-01 — Open Group SOSA Edition 1.1: whole Sensor boundary **deferred**

| Field | Recorded value |
| --- | --- |
| `alignment_id`, `topic_id`, `candidate_meaning` | `ALN-T01-A049-01` / `TOPIC-01-INDIVIDUAL-SYSTEM` / check whether a bounded whole Sensor warrants shared subject identity semantics. |
| `artifact_id`, `lineage`, `source_role` | **49**, `The Open Group SOSA`, primary anatomy evidence; **48** (Edition 1.0 DSDM) is a **separate source artifact of the same source lineage**, not a second independent vote. |
| `source_ed`, `source_concept`, `source_locator` | **The Open Group, Technical Standard for SOSA Reference Architecture Edition 1.1, C239 (June 2023; September erratum)**; earlier [frozen C15 extraction](../DRAFT_DIM_Profile_V2_Anatomy_PhaseA_Independent_Extractions_v0.1_26OCT2026.md) discusses `SOSA Sensor` boundary and DSDM `Sensor`, `ProductInstance`/component entities. **A precise Edition 1.1 primary clause has NOT been independently rechecked for this Step 04.** |
| `source_native_meaning` | **PRIOR_CITED_RESEARCH only:** C15 describes a **whole bounded Sensor** with hardware, optional software, supporting functions, host Platform distinction and DSDM entities including a ProductInstance. This is not a verified claim of the source's exact persistent UID or replacement continuity rules. |
| `mapping_direction` / `relation_kind` | `Open Group whole Sensor boundary → V2 individual sensing-equipment subject` / **`UNRESOLVED`** as a *precise individual-identity mapping*. Architectural relevance is plausible, but exact identity semantics not confirmed. |
| `reused_role` / `qualification_or_loss` | Potential whole-System granularity corroboration; **not** evidence that Open Group SOSA's Module, Chassis, PIC or Sensor has the same meaning as CSAPI System or SOSA/SSN System. No DSDM `ProductInstance` definition has been adopted by the DIM. |
| `evidence_status` / `source_claim_standing` | `PRIOR_CITED_RESEARCH` / `PRIOR_RESEARCH_PARAPHRASE`, **not** `PRIMARY_TEXT_CHECKED` in this Step 04. |
| `mapping_review_status` / `adoption_status` | **`DEFERRED_UNRESOLVED`** / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`, exact source identity correspondence not assessed. |
| `donor_declarations` | **NOT_ASSESSED** at edition/clause level; do not infer any W3C/OGC SOSA association from the shared acronym. |
| `source_to_client_consequence` | Potential whole-Sensor boundary relevance for the TRSS/OmniSense common Details view, **not** yet independently proved identity alignment. |
| `open_question` / `record_provenance` | Targeted original C239/DSDM clause review needed **when a consequential model identity/assembly decision depends on it**. Deferred under Step 04 scope, **28 October 2026**. |

**No other sources have received a detailed Step 04 identity mapping by inclusion in this document.** Notably, CSAPI Part 2 (artifact 11), SensorML 3.0 (13), the 12-item Open Group SOSA family, OSUS-R, SAPIENT and PA-DIM remain important to later topics. An existing Phase 0 “primary anatomy evidence” label or Step 03 `NOT_ASSESSED` is neither a new accepted alignment nor a global exclusion.

## 4. Verified *donor-declared* relationships — distinct from our comparisons

These records **do not** assert that the target donor adopted an identical meaning; they record what the **declaring source itself** states.

| `declaration_id` | `declaring_artifact_id` and exact source clause | Source-declared relation and target | Authority as source says | Evidence, limits and disposition |
| --- | --- | --- | --- | --- |
| **`DECL-T01-01`** | **10**, [OGC 23-001 v1.0](https://docs.ogc.org/is/23-001/23-001.html), **§3 Normative references; §§1, 9.1–9.2** | Explicit **normative reference** to *Semantic Sensor Network Ontology (19 October 2017)* = corpus **ID 20**. Its `System` resources implement SOSA/SSN concepts. | **Normative reference to dated 2017 Recommendation**; the scope of CSAPI's implementation/semantic correspondences is specific to its own clauses. | **`PRIMARY_TEXT_CHECKED`**. CSAPI §§9.1–9.2 alternately use `sosa:System` and `ssn:System` while the referenced 2017 ontology defines `ssn:System`. **`ISSUE-T01-01` unresolved**; neither a formal mapping to the 2026 WD nor universal OWL equivalence is asserted. |
| **`DECL-T01-02`** | **144**, [SAREF Core 4.1.1](https://saref.etsi.org/core/v4.1.1/), **“Device kinds and devices”** and **“Relation to other documents”** | SAREF states that `saref:Device` instances are also **`s4syst:System`**, explicitly referring to the **SAREF4SYST/ETSI TS 103 548** system framework. | **Source-stated ontology/class relationship**, not a claim about CSAPI/SOSA/SSN classes. | **`PRIMARY_TEXT_CHECKED`** for the SAREF 4.1.1 declaration; exact separate SAREF4SYST edition, implementation restrictions and eventual DIM adoption **NOT VERIFIED** in Step 04. |

**Neither declaration constitutes a third-party conformance certification**. The full inter-source dependency and equivalence reconciliation is scheduled for **Step 09**, not silently performed here.

## 5. Adversarial controls, unresolved issues, and practical use-case relevance

### ISSUE-T01-01 — SOSA/SSN class IRI and edition discrepancy — preserve, do not “fix”

**Directly inspected sources:**

- Published [OGC CSAPI Part 1 v1.0](https://docs.ogc.org/is/23-001/23-001.html), **§3** normatively names **SSN 2017**; **§9.1** discusses `sosa:System`, while **§9.2.1** describes `ssn:System`.
- The [2017 SSN Recommendation](https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/), **§4.9.2.4**, defines the class **`ssn:System`** in namespace `http://www.w3.org/ns/ssn/`.
- The [21 October 2026 Working Draft](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/), **§5.3.5.2.4**, defines **`sosa:System`** in `http://www.w3.org/ns/sosa/`, with a revised system/asset organization; **§8.16** describes type-versus-instance modeling.

**Disposition:** **OPEN version-sensitive source inconsistency / migration question**, not a conclusion that a given published specification is invalid, and not permission to silently switch source class IRIs. **The shared individual-vs-type distinction remains credible**, but any formal RDF/OWL implementation mapping must explicitly select edition/namespace, analyze the actual relationship and source constraints, and assess consistency with the published CSAPI version. Do not claim `owl:equivalentClass`, `rdfs:subClassOf`, or identical obligations between `ssn:System`, `sosa:System`, CSAPI `System` or the future V2 DIM merely from the English word.

### ISSUE-T01-02 — identity continuity and multi-server reconciliation — deliberately unresolved

A shared product/model label, resource path, OPC UA NodeId, AAS Shell ID, backend Device record or reported sensor label **does not independently authenticate physical identity or justify merging representations**. CSAPI has UID rules, OPC UA and AAS have distinct identifier mechanisms, and OSUS/Open Group sources may have additional participant/proxy distinctions. **No cross-vendor reconciliation algorithm, authoritative issuer policy, replacement threshold or equivalence test exists in our current candidate DIM.**

**Needed later, when testable:** source-assigned equipment serial or UID with issuer/scope, evidence of actual source→digital identity association, precise equivalence conditions, and negative cases for similarly named product units. Some questions may belong to the eventual CSAPI Profile or integration process rather than to an invariant DIM class.

### One truthful source-to-client example

- **TRSS ETU-II historical fixture:** a given source record may represent a whole sensor-equipment unit and include detector slots. The fixture's identifiers are **synthetic example identifiers**, not verified recovered physical serials. A shared UI may show the record and its equipment data, but not claim the source detector slots are each separately identified physical Systems.
- **OmniSense Core2 versus Core5ADS historical fixtures:** these are **different source cases**; five Core2 transducer labels are not independent equipment UIDs, and the Core5ADS voltage record is not proof it describes the Core2 unit.
- **Smart Citizen Kit 2.3 research:** the [I05 study](../Case_Studies/Real_Equipment_DIM_Validation/I05_Individual_System_and_Product_Kind_Mapping_v0.1_27OCT2026.md) verifies *manufacturer product design* and a candidate kind description, **not one actual physical Kit and its platform record join**. No fictional device UID, Observation or physical-to-backend association may be introduced.

**Future UI requirement question (not a Profile SHALL):** Can a profile-aware client show **which individual is described, its evidence-backed identity scope, its reusable kind, and the digital/source representation being viewed** without confusing them, leaving unsupported physical identity as **unverified**? This is a concrete goal of the shared Resource Details interface, not a test that this Step 04 executed.

## 6. Review result: conceptual candidate preserved, no model adopted

| Step 04 acceptance check | Result |
| --- | --- |
| One topic only, source-derived from completed Pass 1 | **PASS** — `TOPIC-01-INDIVIDUAL-SYSTEM`; other four passes not begun in this new plan |
| Existing frozen source IDs and lineages used; no invented donor numbering | **PASS** — IDs **10, 20, 19, 144, 97, 104, 49** correspond to the [Step 03 register](03_Source_Accountability_Register.csv) |
| Exact primary-edition text checked where claims depend on it | **SIX SOURCE RECORDS DIRECTLY CHECKED**, one Open Group comparison expressly deferred |
| Qualitative mapping type and direction with non-equivalent meaning | **RECORDED** — `CLOSE_ALIGNMENT_WITH_QUALIFICATION`, `SOURCE_BROADER`, `PARTIAL_OVERLAP`, and `UNRESOLVED` appropriately qualified |
| Donor-declared links vs V2 researcher comparisons | **TWO VERIFIED SOURCE DECLARATIONS**, no unsupported universal equivalence |
| Edition, ID, scope and source-access caveats | **EXPLICIT** — 2017 Recommendation versus 2026 Working Draft, CSAPI 2025 wording issue, source identity scope, C15 ceiling |
| Source-to-DIM-to-Profile-to-client value explained | **QUALIFIED** — useful negative/positive information-preservation questions, not an executed interchange |
| New classes/relationships, formal conformance, UI code or broad donor survey | **NONE** |
| Proposed adoption decision | **NONE**. `adoption_status=NOT_ADOPTED` throughout. |

**Candidate DIM implications that survive:** keep a distinguished *individual System referent*, and separate it from *how it is identified*, *which reusable kind characterizes it*, *what it can do / what it actually did*, and *how software/services represent it*. The donors support these distinctions, **not one standardized universal identity carrier**. Existing donor classes/URIs remain theirs; adopting a V2 class hierarchy or normative Profile constraints requires later evidence and owner review.

**What remains unverified:** real same-equipment identity correlation, replacement/repair continuity, exact formal cross-edition SOSA/SSN mapping, detailed Open Group SOSA identity semantics, and actual source→CSAPI→client information preservation. **These are explicit limitations, not failed tasks to silently fix before proceeding.** Later work may selectively address them when consequential.

**Next only after a new user “proceed”: Step 05 — Product / Model / Kind donor alignment**, using the completed Pass 2 and relevant source clauses. Do **not** perform Step 05 within this iteration or treat Step 04's references to kind as Step 05 completion.
