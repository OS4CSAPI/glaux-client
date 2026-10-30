# Candidate DIM — Concepts and Donor Comparisons

**Version 0.2 · 30 October 2026 · America/New_York**  
**Iteration 2: existing meanings, relationships and donor contributions consolidated.** Equipment mapping remains Iteration 3; the final verification and next-task decision remain Iteration 4.  
**Workspace:** `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`.  
**Input snapshot:** `258c620dfd5af7bf80fef32cb7b12dbcc7e56bf3`. This is a readable view of existing V2 research, not a replacement or adoption of the candidate Domain Information Model (DIM) manuscript.

[Donor contributions and coverage](Donor_Contributions.md) · [Equipment evidence — not started](Equipment_Evidence.md) · [Plan](../PLAN_DIM_Profile_V2_Concept_Donor_and_Equipment_Comparison_v0.1_30OCT2026.md) · [Drift correction](../DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md)

## 1. What the candidate model currently says

The present foundation distinguishes **the equipment being described, reusable descriptions of its kind, methods it can perform, actual activities, different relationships among its constituents, and the digital resources that describe or expose it**. The argument is not that these are five mandatory classes. It is that conflating these roles would lose information that the examined sources distinguish. This connected reading comes from [candidate v0.2 §§3–5][manuscript].

| Question a reader should be able to answer | Current candidate meaning | What has not been settled |
| --- | --- | --- |
| [Which particular subject is being described?](#individual-system) | **F-01:** the individual System differs from its label, model, identifier and record. | Final subject boundary/root, identity continuity and actual cross-source identity joins. |
| [What does its model or kind describe?](#kind-model) | **F-02:** reusable information differs from individual configuration/history; not every “type” means product model. | A common description structure, inheritance, versioning and source-specific specializations. |
| [What can it do, and what actually happened?](#method-and-activity) | **F-03:** a method and its implementability differ from an occurrence and result. | Detailed treatment of capabilities, modes, selected state, requests and outcomes. |
| [How are its parts and associated things related?](#composition) | **F-04:** relationship meaning differs from whether an element is separately described or managed. | How physical, functional, manufactured, hosted and interface relationships fit together. |
| [Whose resource or report are we reading?](#representation) | **F-05:** equipment differs from its descriptions, services and proxies. | A general representation/identity/time model and evidence for particular joins. |

**How the pieces connect:** an individual can be characterized by kind information and described as capable of a method; an actual occurrence needs its own performer, method and result evidence. Parts, hosts, functions and exposed interfaces have different relationship meanings. A digital description can concern any of these subjects without becoming the subject itself. The [ten recorded relationship passages](#relationships) make those connections explicit; the [additional open questions](#open-questions) show what the foundation still does not explain.

These headings organize the existing record, not all future donor contributions. The [reverse donor view](Donor_Contributions.md) retains relevant material without a developed destination, including preliminary/deferred sources. Neither the five headings nor the order in this page determines the next model subject.

## 2. How to read the comparisons

The native-meaning columns summarize **findings already recorded in V2**. The contribution column is the project's interpretation in the direction **source meaning → candidate distinction**. It is not a declaration that donors are equivalent to one another. “Close, qualified,” “partial overlap,” and “rejected direct equivalence” retain the existing judgments; explanatory phrases for later findings do not invent new formal alignment records.

**Evidence boundary:** this iteration reads project reports and the candidate manuscript. It does not freshly verify every primary standard, resolve an edition discrepancy, or execute a transformation. All current concepts and relations remain **candidate / not adopted / no transformation test**. Source-local requiredness, cardinality and protocol rules are not universal DIM rules.

The [source trail](#source-trail) gives exact recorded editions, clauses and report links. The [donor page's record index](Donor_Contributions.md#record-index) accounts for all 48 original alignment IDs, the later findings, and their exceptions. Readers need not decode those IDs to understand the tables.

<a id="individual-system"></a>
## 3. Which individual System are we describing? — F-01

**Candidate definition, restated:** the individual is the particular real-world, equipment-realized System to which information refers. A name, product description, network participant or database record can concern it without being the same thing. Changing a representation does not automatically establish a new individual; continuity after repair or replacement remains unresolved. Basis: [identity report §§1–3][identity] and [v0.2 §4.1][manuscript].

| Donor / native concept | Meaning recorded in the research | Contribution toward this distinction | Boundary or alternative to retain |
| --- | --- | --- | --- |
| **Asset Administration Shell (AAS)** — Asset, Shell, AssetInformation ([source](#source-aas)) | An asset and its separately identifiable Shell have different roles; assets can be types or instances. | Separate represented subject from representation and kind. | The asset universe is broader than physical sensing equipment; not every Shell describes a deployed unit. |
| **OGC API – Connected Systems (CSAPI)** — System, `uniqueIdentifier`, resource ID ([source](#source-csapi)) | A System resource describes an individual; subject UID differs from the server-local identifier/address. | Close, qualified support for individual-versus-record identity. | URI rules and persistence recommendations are CSAPI-specific; they do not prove a physical identity join. |
| **Institute of Electrical and Electronics Engineers (IEEE) 1451** — application, NCAP, TIM ([source](#source-ieee)) | Application, network-capable application processor and transducer interface module are distinct interface/mediation roles. | Qualify which participant actually concerns the equipment. | A network or module role is not automatically the complete physical subject. |
| **Integrated Sensor Architecture (ISA)** — Component, Controller, Composition ([source](#source-isa)) | Interface participants can expose or mediate members, including virtualized representations. | Physical equipment and interface participation can overlap without being identical. | Participant IDs and visible-member counts cannot establish physical identity or inventory. |
| **OPC Unified Architecture (OPC UA) Devices** — device nameplate versus AddressSpace Node ([source](#source-opc)) | Equipment-identifying information and its representation have distinct roles. | Keep the described device separate from the Node that exposes it. | Node identity alone does not prove equipment identity or lifetime continuity. |
| **SAPIENT v2** — Node / `node_id` ([source](#source-sapient)) | A message/interface participant can have sensing, software, platform or fusion roles. | Partial overlap: a Node may describe equipment, subject to evidence. | Sender identity is not automatically a physical serial or CSAPI System UID. |
| **Smart Applications REFerence ontology (SAREF)** — Device versus DeviceKind ([source](#source-saref)) | An individual device differs from its kind description. | Supports the individual/kind distinction. | SAREF Device scope is not asserted identical to the proposed sensing-equipment scope. |
| **The Open Group Sensor Open Systems Architecture (SOSA)** — Sensor / HostPlatform ([source](#source-open-group)) | A whole sensing subject can span multiple hardware elements on a distinct host. | Provides a whole-System perspective beyond one enclosure. | The defense-architecture scope is not adopted as a universal root; original deferred and later reviewed records remain separate. |
| **W3C/OGC Sensor, Observation, Sample, and Actuator / Semantic Sensor Network (SOSA/SSN)** — edition-specific System ([source](#source-ssn)) | Published `ssn:System` and recorded draft `sosa:System` belong to different editions. | Supports a System subject distinct from descriptions and activities. | Do not silently substitute draft identifiers or equate all donor classes. |

**How the synthesis follows:** the first set of identity records distinguishes individual, kind and representation. The later interface-oriented sources show why “one sender” or “one exposed component” is not a sufficient physical-boundary test; Open Group SOSA adds a distributed whole-System perspective. Together they support identifying what each statement concerns, not one common identifier syntax or an automatically adopted superclass. [Original R09-01/10][original-reconciliation]; [later F-01 and DC05-S01][later-reconciliation].

**Unresolved choice:** how the final model describes its subjects and identity continuity, and how actual source records establish sameness. The tables do not resolve this by selecting either a hardware-first or interface-first root. The client consequence is a research implication: do not invent an equipment unit merely because a record exists.

<a id="kind-model"></a>
<a id="3-worked-comparison--what-does-model-or-kind-describe"></a>
## 4. What does “model or kind” describe? — F-02

**Candidate definition, restated:** reusable descriptive information characterizes a kind or shared specification without asserting a particular unit's installed configuration, calibration, condition or history. A product designation, ontology type, process template, interface type and channel description can answer different questions. This retains the Iteration 1 example, not a universal `ProductModel` class. Basis: [kind/model report §§1–4][kind] and [v0.2 §4.2][manuscript].

### 4.1 Reusable kinds and type/individual distinctions

| Donor / native term | Meaning recorded in the research | Contribution toward this distinction | Qualification that must survive |
| --- | --- | --- | --- |
| **AAS** — Type Asset / Instance Asset; `assetKind`, `assetType` ([source](#source-aas)) | Shared type information and separately identified assets; the Shell has its own identity. | Close, qualified type/individual distinction. | A type asset is not a Shell template. AAS `assetType` is not the CSAPI Equipment classification. |
| **CSAPI** — `System.systemKind` ([source](#source-csapi)) | Optional kind/datasheet association to a Procedure resource, distinct from implementable `procedures`. | Close, qualified individual-to-kind relationship. | Shared carrier does not make a datasheet an observing method; optional single target is source-local. |
| **SAREF** — `DeviceKind`, `hasDeviceKind` ([source](#source-saref)) | Kinds and common characteristics, distinct from model/manufacturer literals. | Close, qualified reusable-kind relationship. | A model-name string is not automatically a resolved DeviceKind or CSAPI Procedure. |
| **Sensor Model Language (SensorML)** — `typeOf` ([source](#source-sensorml)) | Specific/general process descriptions, inheritance and configuration. | Partial overlap: shared descriptions can inform individual descriptions. | Applies to physical and nonphysical processes; not every link identifies a manufactured product. |
| **W3C/OGC SOSA/SSN** — System type and individual ([source](#source-ssn)) | The recorded 2026 draft describes ontology classes and particular individuals. | Partial overlap: type and individual are different levels. | Ontology typing is not a datasheet/product identity; draft is not the 2017 Recommendation. |

### 4.2 Different descriptive roles that must remain visible

| Donor / native term | Meaning recorded in the research | Contribution or alternative role | Qualification that must survive |
| --- | --- | --- | --- |
| **IEEE 1451** — Meta and Transducer Channel Transducer Electronic Data Sheets (TEDS) ([source](#source-ieee)) | Module/channel characteristics, potentially including unit-specific identification/calibration. | Partial overlap / different scope: identify what the description applies to. | Not automatically a reusable whole-product description. Public technical evidence is usable; uninspected normative requirements remain unverified. |
| **ISA** — Component Capability Description (CCD) ([source](#source-isa)) | Declared Properties, Observables and Commands of an interface participant. | Capability description, not manufacturer designation. | A capability bin is not a manufactured kind, physical assembly or current state. |
| **OPC UA Devices** — `Model` ([source](#source-opc)) | Manufacturer-model metadata separate from serial identity and structural typing. | Partial overlap: identifies a kind without supplying its specification. | No datasheet URL follows from a string; an unsupported empty value stays empty. |
| **OPC UA Devices** — `DeviceType` ([source](#source-opc)) | ObjectType defining the structure of a device's representation. | **Rejected direct equivalence:** not manufacturer product model. Retain interface-typing role. | Rejection concerns one mapping, not the donor; placement of interface typing remains open. |
| **SAPIENT v2** — `model` versus `node_type` ([source](#source-sapient)) | Manufacturer designation versus modality/architectural role. | Partial overlap / different scope. | A seismic role is not a product model or `systemKind` reference. |
| **Open Group SOSA** — `Product`, `ProductInstance`, `Component_` ([source](#source-open-group)) | Manufactured product and association to a functional component. | Distinguish manufactured realization from functional role. | Not a universal whole-System kind relationship; keep data-model and architecture editions separate. |
| **W3C Web of Things (WoT)** — Thing Model ([source](#source-wot)) | Reusable interactions/metadata for a particular Thing Description. | Partial overlap: an interaction template. | Not necessarily a hardware datasheet; Thing Description 1.1 remains an out-of-inventory companion. |

<a id="4-how-the-current-synthesis-follows--and-what-is-still-a-choice"></a>
**How the synthesis follows:** CSAPI, SAREF and AAS provide kind/type distinctions; SensorML and SOSA/SSN offer differently scoped mechanisms. OPC UA and WoT prevent the word “type” from being flattened into product specification. SAPIENT, ISA, IEEE and Open Group SOSA add modality, capability, technical-description scope and realization. The supported conclusion is to preserve descriptive role and applicability, not make all entries one interchangeable ProductModel. [R09-02/03][original-reconciliation]; [F-02, DC05-S02 and DC05-G03][later-reconciliation].

**Unresolved choices:** separate descriptive roles versus qualified relationships or specializations; model versions and inheritance; source-specific kind cardinalities; and applicability of descriptions mixing type-level and unit-specific information. No choice is adopted here. The example's original source trail remains available below.

<a id="method-and-activity"></a>
## 5. What can the System do, and what actually happened? — F-03

**Candidate definition, restated:** a reusable Procedure/Method describes how something is done. A System's ability to implement it is different from a particular occasion on which it was used, the performer, occurrence-specific parameters and result. Later donor findings distinguish declarations, supported modes, selected state and action outcomes more finely; the complete common treatment remains open. Basis: [method report §§1–2][method] and [v0.2 §4.3][manuscript].

| Donor / native terms | Meaning recorded in the research | Contribution toward this distinction | Boundary or missing treatment |
| --- | --- | --- | --- |
| **CSAPI Part 1** — `procedures`, `systemKind`, Procedure ([source](#source-csapi)) | Implementable methods and kind/datasheet information use different associations despite a shared resource type. | Close, qualified association distinction; broad Procedure carrier only partially overlaps “method.” | Not every Procedure is an algorithm; an available association does not prove execution. |
| **CSAPI Part 2** — DataStream/Observation procedure, parameters, result ([source](#source-csapi)) | Stream-level descriptions and individual occurrence information have distinct roles. | Keep applicable method and actual occurrence context distinct. | Do not manufacture observations from capability documents or generalize optional references into mandatory DIM links. |
| **IEEE 1451** — TEDS / service availability / transducer data ([source](#source-ieee)) | Technical self-description differs from actual data and acts. | Source-scope qualification of what is described versus performed. | Calibration/uncertainty descriptors do not prove an executed measurement. |
| **ISA** — CCD; Status/Event/Request/Response ([source](#source-isa)) | Declaration, current property reporting and requested/result actions are separate communication roles. | Adds distinctions missing from method-versus-execution alone. | No direct equation of every Property, Observable or Command to one Procedure. |
| **Observations, Measurements and Samples (OMS) 3.0** — Observer, ObservingProcedure, Observation, result ([source](#source-oms)) | Performer, procedure, occurrence and result are related but distinct. | Supports actual-use versus reusable-description distinction. | Original full-text access was limited; source-specific cardinality is not a DIM-wide requirement. |
| **SAPIENT v2** — Registration, ModeDefinition, StatusReport, Task, TaskAck, DetectionReport ([source](#source-sapient)) | Supported behavior, current report, request, acceptance/completion/failure and detection are different claims. | Partial overlap plus additional roles; acceptance is not completion. | No universal state machine, automatic Task-to-Observation implication or exact CSAPI conversion. |
| **SensorML** — ProcessMethod, SimpleProcess, AggregateProcess ([source](#source-sensorml)) | Method detail and process/dataflow structure can be described at different granularity. | Reusable method representation without a separate method object for every process. | Description is not runtime execution evidence or hardware inventory. |
| **Open Group SOSA** — System Manager, Task Manager, built-in test/result ([source](#source-open-group)) | Equipment management and mission tasking differ; a test definition differs from its result. | Adds responsibility and test/outcome distinctions. | A manager is not itself a method or an observation; health, fault and mode do not collapse into one state. |
| **W3C/OGC SOSA/SSN** — implements / usedProcedure / draft specializations ([source](#source-ssn)) | Implementability and actual use are different relations in edition-specific vocabularies. | Supports method, performer and event separation. | Preserve 2017/draft namespaces; the draft observing-procedure treatment is not a finalized universal obligation. |

**How the synthesis follows:** the original sources separate method, capability and actual use. SAPIENT and ISA show that these three are not enough to explain declarations, modes, requests and reports; Open Group SOSA further separates management and mission/test responsibilities. IEEE technical descriptions reinforce why self-description is not execution. The existing synthesis therefore identifies distinct claim/activity roles, without establishing all their definitions, relationships or a common lifecycle. [R09-03/04][original-reconciliation]; [DC05-S03/04/09, G01/02][later-reconciliation].

**Unresolved choice:** how to organize and relate these additional meanings. They may require revisions or distinctions beyond this heading; “operational condition” is not a defined destination. A universal Command, Mode, Condition or Execution class is not adopted by displaying these rows. The practical consequence is to distinguish “can,” “requested,” “accepted,” “completed” and “reported,” rather than silently infer one from another.

<a id="composition"></a>
## 6. How are the System's parts and associated things related? — F-04

**Candidate definition, restated:** how something relates to a whole is a different question from whether it has separate identity, description or management. The later findings add multiple relationship dimensions beyond the original two-question formulation. A physical part, process component, addressable channel, hosted object and visible interface do not automatically occupy one interchangeable parent/child tree. Basis: [composition report §1][composition] and [v0.2 §4.4][manuscript].

| Donor / native terms | Meaning recorded in the research | Contribution toward this distinction | Boundary or alternative to retain |
| --- | --- | --- | --- |
| **CSAPI Part 1** — subsystem; Composition / Aggregation / Deployment ([source](#source-csapi)) | A subsystem is a regular System resource; integral and non-permanent associations differ. Nested discovery can include currently deployed items. | Separate independent System standing, relationship meaning and discovery. | Not every physical part requires a System resource; a cable or nested URL does not prove permanence or UML composition. |
| **CSAPI Parts 1–2** — parent stream discovery / `DataStream.system` ([source](#source-csapi)) | A parent's navigation may expose descendant streams; producer attribution is a separate relation. | Keep discoverability separate from actual production. | Do not substitute the parent as producer solely because its endpoint lists the stream. |
| **IEEE 1451** — TIM, TransducerChannel, TEDS ([source](#source-ieee)) | Addressed transducer access and channel metadata differ from physical transducer/module composition. | Adds functional-access and description-scope dimensions. | A channel is not automatically a chip, physical subsystem or CSAPI DataStream. |
| **ISA** — Composition and Composition Interface Component (CIC) ([source](#source-isa)) | Member existence, visibility and external taskability can differ; native interfaces may be mediated. | Physical membership, outward exposure and control are independent questions. | Opaque/virtual/visible/transparent/translucent roles do not establish a hardware count or a single physical tree. |
| **OPC UA Devices** — ComponentType, DeviceType, ModularDevice/SubDevice ([source](#source-opc)) | Representation topology includes hardware and software; modular-device relationships have their own scope. | Partial overlap with component/independent-description questions. | OPC aggregation is not automatically CSAPI lifecycle aggregation or permanent physical ownership. |
| **SAPIENT v2** — `sub_components`, `dependent_nodes`, fusion hierarchy ([source](#source-sapient)) | Configuration description, operational dependency and message organization are distinct structures. | Preserve different kinds of relationship rather than one containment link. | None alone proves physical membership, independent unit identity or permanence. |
| **SAREF** — `consistsOf` ([source](#source-saref)) | Composite descriptions are broader than hardware, including properties/values. | Partial overlap for applicable device compositions. | Not a hardware-only part-of relation or a mandatory component taxonomy. |
| **SensorML** — AggregateProcess, PhysicalComponent, PhysicalSystem ([source](#source-sensorml)) | Process decomposition and dataflow differ from the physical realization being described. | Keep functional/process relationships and physical arrangement distinguishable. | A process edge or output does not prove a separately installed part. |
| **Open Group SOSA** — SensorComponent, Module_, ModuleImplementation, ProductInstance, HostPlatform ([source](#source-open-group)) | Part-of, function, manufactured realization, implementation and hosting are separately represented. | Adds several relationship dimensions that one component tree would hide. | Source cardinalities remain edition-local; host is not automatically part of Sensor. |
| **W3C/OGC SOSA/SSN** — subsystem, hosting, Deployment ([source](#source-ssn)) | Subsystems and their context/hosting are separate relations, with edition-sensitive terms. | Preserve whole/part versus contextual association. | No silent namespace substitution or equation of host with intrinsic part. |

**How the synthesis follows:** original CSAPI, SensorML and ontology comparisons separate relationship kind from description granularity. The additional sources supply materially different structures—functional implementation, manufactured product, channel addressing, operational dependency and mediated visibility. The candidate conclusion is to preserve these roles where supported; it is not to declare a fixed number of new edges or force their reconciliation into one universal component class. [R09-05–08/12][original-reconciliation]; [DC05-S05–07, G03–05][later-reconciliation].

**Unresolved choices:** which relations should be distinct in the DIM; how they combine; when a part has independent standing; temporal association and replacement rules; and how source-specific perspectives are expressed. AAS component/aspect material and other preliminary leads remain visible on the donor page rather than being silently counted as completed F-04 mappings. The practical consequence is that a client must not mistake channels or interface members for an authenticated physical inventory.

<a id="representation"></a>
## 7. Whose description or report are we reading? — F-05

**Candidate definition, restated:** a description, service, proxy or record is distinct from what it describes. It may concern an individual, a kind, a function, a part, a group or a virtual subject. Identifiers and apparent currentness require evidence of source scope, mediation and time; they do not become equipment facts by appearing in an interface. Basis: [representation report §§1–2][representation-report] and [v0.2 §4.5][manuscript].

| Donor / native terms | Meaning recorded in the research | Contribution toward this distinction | Boundary or alternative to retain |
| --- | --- | --- | --- |
| **AAS** — Asset / Shell / Submodel ([source](#source-aas)) | Separate Shell identity and represented Asset; Submodels describe aspects. | Close, qualified subject/representation separation. | One represented asset per Shell is source-local; a Submodel is not automatically another physical part. |
| **CSAPI** — System UID / resource ID / URL ([source](#source-csapi)) | Multiple services can describe a subject while retaining their own resource identifiers. | Close, qualified separation of subject and served record. | Matching strings do not establish a cross-server or physical identity join. |
| **IEEE 1451** — NCAP/TIM/TEDS ([source](#source-ieee)) | Mediation, technical description and underlying transducer information have different scopes. | Qualify publisher, described subject and metadata applicability. | No automatic same-ID or whole-equipment interpretation. Research mappings are not normative equivalences. |
| **ISA** — CIC, opaque and virtual members ([source](#source-isa)) | A mediator may expose member capabilities under different interface identities. | Outward identity/authority differs from physical membership. | Resource count and publisher identity cannot reconstruct the original hardware producer. |
| **OPC UA Devices** — AddressSpace, online/offline parameter models ([source](#source-opc)) | Device metadata and digital Nodes differ; offline settings can be separate from online parameters. | Preserve representation and state-authority distinctions. | Offline value is not current device state; source NodeId rules are not universal DIM rules. |
| **OSUS-R** — `Asset` / `AssetProxy` ([source](#source-osus)) | Pinned code separates consumer-facing proxy/interface from device-specific implementation. | Useful implementation pattern for mediated access. | This is code evidence, not a normative universal asset ontology or real-equipment identity proof. |
| **SAPIENT v2 / Apex** — wrapper, sender, cached/replayed messages ([source](#source-sapient)) | Message identity, content time and intermediary behavior can differ from physical source/state. | Qualify whose assertion and which time are exposed. | Cached reports are not fresh observations; content-time/send-time wording discrepancy remains unresolved. |
| **SAREF** — Function / Service ([source](#source-saref)) | A service can digitally represent a function rather than an entire device. | Partial overlap: represented scope can be an aspect/function. | One service does not imply one whole physical System. |
| **Open Group SOSA** — representation levels / indirect management ([source](#source-open-group)) | Conceptual, logical, physical representations and management roles are distinct. | Qualify the level and authority of a description. | These levels are not automatic physical identities or a universal digital twin. |
| **WoT** — Thing / Thing Description / Intermediary / Digital Twin ([source](#source-wot)) | Descriptions, proxies and twins can have different identity and aggregation scopes. | Partial overlap with description/mediation roles. | A proxy may use another ID; a twin may concern more than one Thing. Do not impose AAS cardinality on WoT. |

**How the synthesis follows:** the original sources independently separate represented subjects, aspects, descriptions and services. Later donor findings add mediated identity, hidden/virtual members and report timing. They support recording what a claim concerns and where it came from, not one universal `representedBy` relation, alias rule or precedence algorithm. [R09-09/10][original-reconciliation]; [DC05-S07/08/10 and G05][later-reconciliation].

**Unresolved choices:** how representations, source authority and temporal qualifications relate in the DIM, and what evidence establishes a particular identity correspondence. Detailed provenance remains a coverage gap; listing this need does not mean W3C PROV has already been fully integrated. The practical consequence is to avoid presenting mediated, configured or stale values as newly measured hardware facts.

<a id="relationships"></a>
## 8. How the candidate meanings are connected

These are the manuscript's **ten existing relationship passages**, restated for reading. The identifiers are editorial references, not adopted property names, formal axioms or new relationships created by this iteration. Full native terms and provenance appear in [v0.2 §5][manuscript] and the topic records linked below.

| Existing passage | Candidate relationship meaning | Recorded donor basis | What is not established |
| --- | --- | --- | --- |
| **REL-01 — individual and kind** | An individual may be characterized by reusable kind/model information. | CSAPI `systemKind`; SensorML `typeOf`; SAREF DeviceKind; AAS Type/Instance. [Kind report][kind] | Universal cardinality, inheritance or resolved kind identifier. |
| **REL-02 — implementability** | A System can be described as capable of implementing a Procedure. | CSAPI `procedures`; edition-specific SSN implements relations. [Method report][method] | Actual occurrence; resolution of vocabulary-edition mismatch. |
| **REL-03 — actual activity** | An occurrence, when evidenced, has distinct method, performer and result roles. | OMS; CSAPI Part 2; published/draft SOSA/SSN. [Method report][method] | Fabricated execution or universal method multiplicity. |
| **REL-04 — whole and subsystem** | A subordinate System may have independent information while associated with a whole. | CSAPI subsystem; edition-specific SSN relations. [Composition report][composition] | Every chip/channel becomes a System. |
| **REL-05 — integral or temporary association** | Integral composition and non-permanent deployed association differ. | CSAPI §10.2. [Composition report][composition] | Cable/URL determines permanence or UML lifecycle. |
| **REL-06 — process relationships** | Functional/process connections need not be physical assembly. | SensorML AggregateProcess and physical process descriptions. [Composition report][composition] | Dataflow proves mechanical part-of. |
| **REL-07 — hosting and deployment** | A host and deployment context differ from intrinsic equipment composition. | SOSA/SSN hosting/Deployment; CSAPI deployment. [Composition report][composition] | Universal host=part-of or completed temporal model. |
| **REL-08 — discovery and producer** | A parent's discovery route need not identify the producer of a listed stream. | CSAPI Part 1 §10.7; Part 2 `DataStream.system`. [Composition report][composition] | Parent listing proves parent production. |
| **REL-09 — subject and representations** | Separate records/descriptions can concern the same subject under source-specific identity rules. | CSAPI, AAS, OPC UA, WoT, SAREF. [Representation report][representation-report] | Verified identity join or one-to-one mapping. |
| **REL-10 — mediation and state authority** | A proxy/service can expose functions, cache data or model offline settings. | WoT; OPC UA online/offline; SAREF Service; OSUS-R proxy. [Representation report][representation-report] | Universal proxy type, live state or original producer. |

**Later findings do not silently create REL-11–REL-15.** The manuscript separately records additional questions about behavior, actions, channels, relationship structures and mediation. These appear next, with their unresolved standing intact. Nor are the existing ten exhaustive: the donor contributions may justify revising their organization in later work.

<a id="open-questions"></a>
## 9. What has evidence but no developed model treatment yet?

The following are the existing five grouped questions, not five new modules. **DC05-G01–G05** are the reconciliation's labels; **Q-DC05-01–05** are their manuscript counterparts. Original source flags remain visible in the [donor view](Donor_Contributions.md#open-contributions). Their placement need not stay within the five headings above.

| Existing question | Source-backed distinction | Unresolved construction question |
| --- | --- | --- |
| **G01 / Q-01 — declarations and state** | SAPIENT declarations/modes/status; ISA capabilities/reports; IEEE descriptions versus data. | What separates supported, allowed, selected, reported and measured information, and how are their subject/time scopes represented? |
| **G02 / Q-02 — requests and outcomes** | SAPIENT tasks/acknowledgements/detections; ISA requests/responses; SOSA management and test results. | Which action/result relationships are common and which remain source-specific? No universal lifecycle or completion-to-observation implication. |
| **G03 / Q-03 — channels and self-description** | IEEE addressed channels and detailed module/channel TEDS, including public Playground evidence. | Which subject owns units, range, uncertainty, calibration and timing; how does channel identity relate to physical realization? |
| **G04 / Q-04 — several relationship structures** | SOSA part/function/product/host; SensorML process; CSAPI composition/deployment. | How can these structures coexist without one forced hierarchy or imported source cardinality? |
| **G05 / Q-05 — outward visibility and source authority** | ISA member visibility/taskability; SAPIENT mediation; SOSA indirect management. | How do actual members, exposed representations, permitted actions and original sources relate? |

Basis: [later reconciliation §5][later-reconciliation] and [v0.2 §5.3][manuscript]. The historical DC05-S09 heading about condition records a distinction among value claims, not a developed concept or current priority; the [drift correction](../DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md) governs its interpretation.

There are also unresolved alternatives already identified within the five meanings: subject versus interface-centered descriptions; different type/template roles; method versus richer behavior contracts; multiple part/function/hosting perspectives; and representations of a whole versus an aspect or group. This page exposes those alternatives rather than deciding new classes, a final chassis or a winning donor. The preliminary/deferred donor leads are **additional** to these questions, not excluded by them.

<a id="source-trail"></a>
## 10. Follow the evidence to its source

These are **recorded source locators**, not claims of fresh primary-source verification. Topic reports preserve exact alignment judgments, constraints, exceptions and original references. The wider [record index](Donor_Contributions.md#record-index) prevents a summary row from hiding deferred or rejected entries. Existing source-authority limits override shorthand here.

<a id="source-aas"></a>
**AAS:** Industrial Digital Twin Association, IDTA 01001 Part 1 v3.2. [General — Types and Instances](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/annex/general.html), [Core — Shell/AssetInformation](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/core.html), metamodel/Submodel material. [Identity][identity], [kind][kind] and [representation][representation-report] records for artifact 97. Source asset kinds and one-asset-per-Shell condition stay source-local.

<a id="source-csapi"></a>
**CSAPI:** [OGC 23-001, Part 1 v1.0](https://docs.ogc.org/is/23-001/23-001.html), §§8.4–8.5, 9.2.2, 10.1–10.7, 13.1–13.2; [OGC 23-002, Part 2 v1.0](https://docs.ogc.org/is/23-002/23-002.html), §§9.2.2, 9.7. Artifact 10/11 records across all five topic reports. The published correspondence column's SSN term/edition issue remains open; no formal equivalence is inferred from it.

<a id="source-ieee"></a>
**IEEE 1451:** [corrected report §0 and IE03-S01–S08][ieee]. Historical IEEE 1451.1-1999 / ISO/IEC/IEEE 21451-1:2010 roles stay distinct from IEEE 1451.0-2024-linked technical evidence. [Meta TEDS](https://iml.ubi.pt/playground/docs/ieee1451/teds/meta-teds/), [Transducer Channel TEDS](https://iml.ubi.pt/playground/docs/ieee1451/teds/transducer-channel-teds/), [Optional TEDS](https://iml.ubi.pt/playground/docs/ieee1451/teds/optional-teds/) and recorded National Institute of Standards and Technology (NIST) material support technical study. Exact uninspected normative obligations/cardinality remain unverified; public technical accessibility is not denied.

<a id="source-isa"></a>
**ISA:** [structural-donor report ISA04-S01–S05][structural]; Software Design Document 6.0r5, §§3, 4.2.1–4.2.2, 5.1.1; Data Model Specification 6.0r12, §2 and Document Notes, both 31 October 2023. Original document provenance is in the report; no public file URL is invented. Custom/Nominated/Accepted extensions retain their different source standing.

<a id="source-oms"></a>
**OMS:** [OGC 20-082r4, version 3.0](https://docs.ogc.org/as/20-082r4/20-082r4.html), §§8.2, 8.5–8.6 as recorded in [ALN-T03-A008-01 and ISSUE-T03-03][method]. The prior reader obtained official excerpts, not the entire large HTML; exact cardinality reuse remains subject to that limit.

<a id="source-opc"></a>
**OPC UA Devices:** [Part 100](https://reference.opcfoundation.org/specs/OPC-10000-100/full), recorded v1.05.0, §§3–4, 4.5.2, 4.7, 6.1–6.3 and modular-device §9, under artifact 104 in [identity][identity], [kind][kind], [composition][composition] and [representation][representation-report]. URL is not asserted immutable. PA-DIM artifact 103 is not silently covered by this Part 100 work.

<a id="source-osus"></a>
**OSUS-R:** [ALN-T05-A034-01][representation-report] records `Asset` / `AssetProxy` Java sources at commit `d09088f`. This is pinned 2023 implementation evidence, not a normative 2026 ontology. Exact repository/file locators remain in that record.

<a id="source-sapient"></a>
**SAPIENT:** [report S2-N01–N10 and issues][sapient], BSI Flex 335 v2.0:2024-03, §§4.1, 4.10–4.11, 6.2–6.5, including Tables 17–18/32 and status/task tables; [official protobuf directory at commit 244a741](https://github.com/dstl/SAPIENT-Proto-Files/tree/244a741c13bcee628f84944aef91e4a66854bd7d/bsi_flex_335_v2_0). The report separately pins Apex documentation. Registration field-number and content-time/send-time discrepancies remain open; no v3 substitution or source-declared CSAPI equivalence is assumed.

<a id="source-saref"></a>
**SAREF:** [Core 4.1.1](https://saref.etsi.org/core/v4.1.1/), Device/DeviceKind, `hasDeviceKind`, model/manufacturer literals, `consistsOf`, Function/Service; artifact 144 records in [identity][identity], [kind][kind], [composition][composition], [representation][representation-report]. The SAREF4SYST source relationship has its own review limit; source ontology axioms are not automatically DIM constraints.

<a id="source-sensorml"></a>
**SensorML:** [OGC 23-000 v3.0](https://docs.ogc.org/is/23-000/23-000.html), §§7.2, 8.2.9.3 (Requirements 13–15), 8.3–8.6, as recorded in artifact 13 entries in [kind][kind], [method][method], [composition][composition]. Inheritance and process semantics remain source-qualified.

<a id="source-ssn"></a>
**W3C/OGC SOSA/SSN:** [2017 Recommendation](https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/), §§4.8–4.9; [recorded 21 October 2026 Working Draft](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/), §§5.3.3–5.3.5, 8.16 and applicable subsystem/hosting sections recorded in the topic reports. Artifacts 19/20 are editions of one lineage, not independent votes. Draft crosswalks are not formal equivalence axioms; original namespace disputes stay open. This is distinct from The Open Group SOSA.

<a id="source-open-group"></a>
**The Open Group SOSA:** [structural report SOSA04-S01–S07][structural]; Reference Architecture Edition 1.1 C239 (2023), §§4.1.1, 4.2, 5.7, 6; separate Domain-Specific Data Model Edition 1.0 (April 2022), §§1.1.3.15, .54, .68–69, .82–83, .89–92. Original ALN-T01-A049-01 remains historically deferred; later primary review is separately evidenced, not a retroactive change.

<a id="source-wot"></a>
**WoT:** [Architecture 1.1](https://www.w3.org/TR/wot-architecture11/), §§3, 5, 6.1.1.2, 6.10.2, 7.1, 9.2.2; [Thing Description 1.1](https://www.w3.org/TR/wot-thing-description/), §9.1 and identifier provisions as recorded in [kind][kind] and [representation][representation-report]. The reports identify both as 5 December 2023 Recommendations. TD 1.1 is an official companion outside the frozen 182-artifact inventory, not an invented artifact 183.

## 11. What this iteration completed

The comparison now presents the five existing candidate meanings, ten relationship passages, five additional question groups and donor-native contributions together. It preserves the original kind/model example's distinctions, expands the source trail, and links to a donor-first account with explicit unrepresented and deferred material. The source-to-candidate statements are consolidated research, not newly executed mappings or a neutral re-synthesis of every possible donor.

**Content checks in this iteration:** correspondence summaries were checked against the cited manuscript/report passages; the editorial record index was checked for 48 unique original IDs, including deferred/rejected entries; relation and question references, local anchors and table structure were checked. This is not the final Iteration 4 review, primary-source revalidation, or equal-depth donor assessment. Actual equipment mapping, data acquisition, Profile obligations and application changes were not performed.

**Next separate “proceed”: Iteration 3 only — connect applicable meanings to the exact existing system-data-sheet entries, distinguishing supported links, proposed mappings and model/donor/data gaps.** Final verification and an evidence-based next-task recommendation remain Iteration 4. No power/condition subject is selected by this continuation.

[identity]: ../Donor_Alignment/04_Individual_System_Identity_Alignment_v0.1_28OCT2026.md
[kind]: ../Donor_Alignment/05_Product_Model_Kind_Alignment_v0.1_28OCT2026.md
[method]: ../Donor_Alignment/06_Procedure_Method_Alignment_v0.1_28OCT2026.md
[composition]: ../Donor_Alignment/07_Composition_Component_Standing_Alignment_v0.1_28OCT2026.md
[representation-report]: ../Donor_Alignment/08_Digital_Representation_Proxy_Identity_Alignment_v0.1_28OCT2026.md
[original-reconciliation]: ../Donor_Alignment/09_Cross_Concept_Reconciliation.md
[later-reconciliation]: ../Donor_Challenge/05_Challenge_Reconciliation.md
[manuscript]: ../Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md
[sapient]: ../Donor_Challenge/02_SAPIENT_Challenge.md
[ieee]: ../Donor_Challenge/03_IEEE1451_Challenge.md
[structural]: ../Donor_Challenge/04_Other_Structural_Challenges.md
