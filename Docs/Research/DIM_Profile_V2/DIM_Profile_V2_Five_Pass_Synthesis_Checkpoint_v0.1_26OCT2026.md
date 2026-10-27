# Domain Information Model (DIM) / Application Profile Version 2 (V2) — Five-Pass Synthesis Checkpoint

**Date:** 26 October 2026  
**Version:** 0.1  
**Standing:** **Human-readable synthesis checkpoint** of five cited **candidate** concept findings; **not** an adopted DIM class model, final domain boundary, canonical ontology, module architecture, binding, or profile conformance requirement.  
**Controlling plan:** [Incremental Canonical Concept Consolidation Plan](DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md).  
**Reviewed inputs:** [Pass 1 — Individual System Identity](DIM_Profile_V2_Canonical_Concept_Pass1_Individual_System_Identity_v0.1_26OCT2026.md), [Pass 2 — Product / Model / Kind](DIM_Profile_V2_Canonical_Concept_Pass2_Product_Model_Kind_v0.1_26OCT2026.md), [Pass 3 — Procedure / Method](DIM_Profile_V2_Canonical_Concept_Pass3_Procedure_Method_v0.1_26OCT2026.md), [Pass 4 — Composition and Component Standing](DIM_Profile_V2_Canonical_Concept_Pass4_Composition_and_Component_Standing_v0.1_26OCT2026.md), and [Pass 5 — Digital Representation / Proxy Identity](DIM_Profile_V2_Canonical_Concept_Pass5_Digital_Representation_and_Proxy_Identity_v0.1_26OCT2026.md).  
**Authority limits:** This checkpoint **does not use or ratify** the quarantined earlier anatomy Phase B/C/D syntheses; no donor's complete native model is assumed equivalent to V2. Publicly accessible approved standards, a **21 October 2026 working draft** ontology, and independently described engineering/implementation sources retain their different authority levels.

## 1. Checkpoint answer

**The five passes converge on a small but substantive common understanding—not five new classes.**

> **For the present investigation, an individual equipment-realized sensing System is distinguishable from the reusable kind/model descriptions that characterize it, the Procedures it can implement, the particular activities or results associated with it, and the digital descriptions or services through which it is represented. The System may have meaningful constituent elements, but enduring composition must not be confused with non-permanent attachment, hosting, deployment, communication, or functional association. What is separately modeled, and through which existing donor concepts, must follow the available source meaning rather than presumed universal structure** (Open Geospatial Consortium 2025a, §§ 8.5, 9.2.2, 10.1–10.3, 13.1; Open Geospatial Consortium 2025b, §§ 7–8; World Wide Web Consortium and Open Geospatial Consortium 2026, §§ 5.3.3–5.3.5, 8.15–8.16; European Telecommunications Standards Institute 2024, “Device kinds and devices”; Industrial Digital Twin Association 2026, “Asset Administration Shell Attributes,” “Types and Instances”; World Wide Web Consortium 2023a, 2023b; OPC Foundation n.d., §§ 4–6).

This paragraph is **V2 synthesis**. Its source citations support the distinctions, **not** a claim that the donors jointly promulgated this paragraph, agree on one class hierarchy, or require every in-scope source to provide the same information.

Our ongoing descriptive boundary remains the working Open Geospatial Consortium (OGC) Application Programming Interface (API) – Connected Systems (CSAPI) combination `systemType = Sensor` and `assetType = Equipment`, with sensing/observing as the whole's defining activity; non-sensing internal functions do not automatically invalidate that orientation (Open Geospatial Consortium 2025a, § 9.2.2; Open Geospatial Consortium 2025b, § 8.6). **This is not yet a finalized domain name or adopted root-class decision.**

## 2. What each pass contributes to the *whole*

| Pass | Donor-native anchor and corroboration | Contribution to the combined understanding | What is **not** established |
| --- | --- | --- | --- |
| **1. Individual System** | CSAPI System instances and identifiers; Sensor, Observation, Sample, and Actuator (SOSA) / Semantic Sensor Network (SSN) individual Systems; Smart Applications REFerence (SAREF) Device; Asset Administration Shell (AAS) asset identity | One distinguishable individual is the subject, not its identifier, model, observation or resource Uniform Resource Locator (URL) (Open Geospatial Consortium 2025a, §§ 8.5, 9.2.2; World Wide Web Consortium and Open Geospatial Consortium 2026, § 8.16). | New `IndividualSystem` class; unconditional lifetime identity rules or global ID reconciliation. |
| **2. Product / Model / Kind** | CSAPI `systemKind`; Sensor Model Language (SensorML) `typeOf`; SAREF `DeviceKind`; AAS Type/Instance Asset; Web of Things (WoT) Thing Model; Open Platform Communications Unified Architecture (OPC UA) nameplate versus ObjectType | Reusable descriptions can characterize multiple individuals, but *manufacturer product model*, *ontology class*, *device information-model type*, and *interaction template* are different source meanings (Open Geospatial Consortium 2025a, §§ 9.2.2, 13.1; European Telecommunications Standards Institute 2024; Industrial Digital Twin Association 2026; World Wide Web Consortium 2023a, 2023b; OPC Foundation n.d.). | One uniform `ProductModel` class, universal single model association, or full datasheet inferred from a model-name string. |
| **3. Procedure / Method** | SOSA/SSN `System implements Procedure` and `Execution usedProcedure`; CSAPI `procedures` versus `systemKind`; SensorML `ProcessMethod`; Observations, Measurements, and Samples (OMS) ObservingProcedure | The System capable of following a method, the reusable method itself, and a particular execution **using** that method must be differentiated (World Wide Web Consortium and Open Geospatial Consortium 2026, §§ 5.3.3–5.3.4; Open Geospatial Consortium and International Organization for Standardization 2023, §§ 8.2, 8.5; Open Geospatial Consortium 2025a, § 13.1). | A mandatory independent Procedure resource for every method, disjoint “kind” versus “procedure” documents, or one universal execution cardinality. |
| **4. Composition and Component Standing** | CSAPI Composition versus Aggregation; SOSA/SSN `hasSubSystem` versus `hosts` and Deployment; SensorML PhysicalComponent/PhysicalSystem; OPC UA Devices; Bosch BME280 | **Relationship type** and **granularity of independent description** are separate decisions. No universal component tree or automatic elevation of every internal element to a System (Open Geospatial Consortium 2025a, § 10.2; Open Geospatial Consortium 2025b, §§ 8.4–8.6; OPC Foundation n.d.; Bosch Sensortec 2024). | Universal `Component` superclass, Unified Modeling Language (UML) composition diamonds by shared name, or mandatory recursive decomposition. |
| **5. Digital Representation / Proxy Identity** | CSAPI resource versus System; AAS Shell versus Asset; WoT Thing Description / Intermediary; OPC UA online/offline Nodes; SAREF Service; Open Standard for Unattended Sensors reference implementation (OSUS-R) Asset versus AssetProxy | Equipment is distinguishable from digital descriptions, interface/service representations and mediating software. They can have different identities and describe different scopes (Open Geospatial Consortium 2025a, § 8.5; Industrial Digital Twin Association 2026; World Wide Web Consortium 2023a, 2023b; OPC Foundation n.d.). | Universal `DigitalRepresentation` class or `representedBy` predicate, one proxy-to-device cardinality, or identical identifier policy across standards. |

**How to read the table:** These are **candidate semantic distinctions**, not an adopted ontology inventory. CSAPI and SOSA/SSN share an OGC semantic lineage, so they are **not counted as independent votes**. AAS, SAREF, OPC UA and WoT supply useful independent corroboration, **not automatic class equivalences**. OSUS-R is directly checked implementation evidence, **not normative OGC or SDO authority**.

## 3. The first connected relationship picture—without inventing its UML

The following **relationship statements** are already supported sufficiently to guide further conceptual work. Their *donor-native meanings* are sourced; translating them into one DIM class diagram and its associations **remains a separate modeling decision**.

| Source-grounded relationship or distinction | Meaning we can carry forward | Boundary that must remain visible |
| --- | --- | --- |
| **Individual System / kind description** | A System can be associated with reusable information about what kind of System it is: CSAPI `systemKind`, SAREF `hasDeviceKind`, SensorML `typeOf`, and AAS Type/Instance distinctions are useful alignment candidates (Open Geospatial Consortium 2025a, § 9.2.2; European Telecommunications Standards Institute 2024; Industrial Digital Twin Association 2026). | These source roles may have **different carriers and structures**; one source's optional cardinality is not a universal DIM constraint. |
| **System / implemented Procedure** | SOSA/SSN `implements` and CSAPI `procedures` indicate a Procedure a System is capable of executing (World Wide Web Consortium and Open Geospatial Consortium 2026, § 5.3.5.2; Open Geospatial Consortium 2025a, § 9.2.2). | **Can implement** does not mean **actually executed**. Missing links do not establish absence of capability. |
| **Execution / System / Procedure** | The actual Execution is distinct from its performer and reusable method, with `madeBySystem` and `usedProcedure` in SOSA/SSN; OMS uses a parallel observer/procedure/observation distinction (World Wide Web Consortium and Open Geospatial Consortium 2026, § 5.3.4.2; Open Geospatial Consortium and International Organization for Standardization 2023, § 8). | This is a **related boundary**, not completion of an entire observation or execution model. |
| **System / subsystem and context** | Subordinate Systems are representable; **integral composition**, **interchangeable/Deployment-scoped association**, **hosting**, and **network connections** are materially different relationships (Open Geospatial Consortium 2025a, § 10.2; World Wide Web Consortium and Open Geospatial Consortium 2026, § 5.3.5.2; Open Geospatial Consortium 2025b, § 8.4). | `hasSubSystem` is not a declaration of CSAPI Composition permanence; physical/process/function parts need not all be full System instances. |
| **Real System / digital descriptions and software** | Donors distinguish an equipment subject from identifiable resource descriptions, shells, Nodes, services and adapters (Open Geospatial Consortium 2025a, § 8.5; Industrial Digital Twin Association 2026; World Wide Web Consortium 2023a, 2023b; OPC Foundation n.d.). | There is **no one common donor-native relation** with uniform subject, multiplicity or identity semantics. Some relationships may belong in a future binding or provenance layer. |

Two particularly important **cross-pass corrections** follow:

1. **One resource can serve more than one role.** CSAPI's `Procedure` resource can describe the `systemKind` (product/datasheet) **or** a Procedure the System implements; the two **relationship meanings** remain distinct. OMS further permits a Procedure to describe a sensor *type*, not an individual instance (Open Geospatial Consortium 2025a, §§ 9.2.2, 13.1; Open Geospatial Consortium and International Organization for Standardization 2023, § 8.5.2). Thus semantic separation does **not** authorize two universally disjoint new classes.
2. **The same words need not carry the same meanings.** AAS `assetType` refers to an asset's type, while CSAPI `assetType` describes the System's realization (Equipment, Human, Simulation, etc.). OPC UA `DeviceType` is an information-model ObjectType, **not automatically** the vendor product model. WoT `Thing Model` mainly characterizes reusable interactions. CSAPI Composition is **not automatically** UML composite aggregation (Industrial Digital Twin Association 2026, “Asset Information Attributes”; Open Geospatial Consortium 2025a, §§ 9.2.2, 10.2; OPC Foundation n.d., § 4.7; World Wide Web Consortium 2023b). **Semantic roles outrank matching vocabulary labels.**

## 4. One worked thought experiment: why these distinctions buy interoperability

Consider a **hypothetical** equipment-realized weather station with two integral measurement sensors and one detachable sensing module. It has one individual equipment identity, a manufacturer model/datasheet, supported observing procedures, and observation records. One information service exposes it as a CSAPI System; another might describe it through an AAS Shell or OPC UA online/offline representation.

The integrated description should **not** mistake two weather stations of the same product model for one individual; describe an observation as proof of an entire product datasheet; treat an observation's used Procedure as identical to the kind of station; flatten the detachable module into enduring Composition; create a new physical device because an API resource or proxy has a different identifier; or infer that every internal sensor element has an independent managed System identity (Open Geospatial Consortium 2025a, §§ 8.5–10.2, 13; Open Geospatial Consortium 2025b, §§ 8.4–8.6; Industrial Digital Twin Association 2026; OPC Foundation n.d.).

**What this illustrates:** The five distinctions allow **more faithful mapping and interpretation** of real system information **without** demanding five new concepts invented by V2. **What it does not establish:** this scenario is a *thought experiment*, not a completed mapping of one verified fielded station across those protocols, a demonstrated interoperability result, or profile conformance.

## 5. Does a formal UML class diagram now add value?

**Checkpoint decision: not yet as the authoritative *combined* five-pass model.** There is now enough direct donor evidence to make small **source-native UML views** of `System` with `Procedure` and sub-Systems if useful, but a single consolidated DIM class diagram would presently require choices we have *not* earned:

- whether “product model/kind” becomes a DIM class or remains a sourced description with diverse source-specific relations;
- how a physical subpart, software process, logical sensor channel, and independently identifiable System are represented without a fictional universal `Component` class;
- whether digital representation is even an intrinsic **DIM relation** rather than primarily profile/binding/provenance;
- which multiplicities, specializations, source ontologies, and identifiers carry over into the conceptual model.

Drawing generic `ProductModel`, `Component`, `DigitalRepresentation` and arrows would **turn analytical headings into presumed classes**. Drawing only a `System`–`Procedure` line and a self-association would add less explanatory value than the **cited relationship table above**, and risks repeating the low-value two-object pilot.

**Therefore this checkpoint records an explicit *no-diagram decision*, not a failure to apply the UML convention.** Under the existing modeling guide, diagrams must represent established meanings and add demonstrable value; a UML class view remains available when source-level concepts and mappings are justified (Object Management Group 2017; Open Geospatial Consortium 2022, § 8).

## 6. Checkpoint disposition and next decision

**Outcome:** All five candidate meanings are **mutually compatible at the level investigated**. The reviewed evidence reveals **no contradiction** requiring a new umbrella domain name, an enlarged top-level scope, a new DIM-owned root class, or five corresponding DIM classes. This is **limited convergence**, not proof that the entire 182-source donor corpus has been exhaustively reconciled or that V2 is already a completed domain information model.

**Carried-forward working distinctions:** Individual System versus identifiers/representations; kind/model versus individual; kind-description versus implemented-method **relationship roles**; method capability versus actual use; integral versus temporary/hosted/networked association; independently described subsystem versus every physical internal element; represented equipment versus digital service/proxy identity.

**Unresolved matters most likely to affect the first *real* model view:** actual kind-to-instance mapping structure; independent component standing and identity through replacement; evidence-backed representation-to-equipment relationship(s); source identity reconciliation; applicability, cardinality and authoritative edition of any adopted relation. These are unresolved **because the donor meanings differ**, not because one more decorative diagram is needed.

**Recommended next bounded move:** Begin a **single concept-family investigation of *capability and performance***, separating *what a System can do* from *what its type/model promises*, *what its components contribute*, *its selected configuration and actual state*, and *a particular execution or result*. This is the closest substantive extension of Passes 1–5 and is strongly represented in SensorML, Asset Administration Shell capability descriptions, SAREF functions, and actual sensing-equipment specifications (Open Geospatial Consortium 2025b; Industrial Digital Twin Association 2026; European Telecommunications Standards Institute 2024). Treat this as a **recommendation for a later authorized pass**, not permission to start it as part of the present checkpoint.

Do **not** adopt the earlier quarantined anatomy, initialize a full ontology/UML package, invent profile requirements, or claim implementation of contributing standards. Maintain the DIM/profile/OGC-binding separation and the user-approved **donor-language-first** rule.

## References — Chicago Manual of Style, 18th ed., author–date

Bosch Sensortec. 2024. *BME280 Data Sheet*. Revision 1.24, February. https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf.

European Telecommunications Standards Institute. 2024. *SAREF: Smart Applications REFerence Ontology—Core*. Version 4.1.1. https://saref.etsi.org/core/v4.1.1/.

Industrial Digital Twin Association. 2026. *Specification of the Asset Administration Shell, Part 1: Metamodel*. Version 3.2. https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/core.html.

Object Management Group. 2017. *Unified Modeling Language (UML)*, version 2.5.1. https://www.omg.org/spec/UML/2.5.1.

Open Geospatial Consortium. 2022. *OGC Testbed-17: UML Modeling Best Practice Engineering Report*. OGC 21-031, February 8. https://docs.ogc.org/per/21-031.html.

Open Geospatial Consortium. 2025a. *OGC API—Connected Systems—Part 1: Feature Resources*. OGC 23-001, version 1.0, July 16. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC SensorML Encoding Standard*. OGC 23-000, version 3.0, July 16. https://docs.ogc.org/is/23-000/23-000.html.

Open Geospatial Consortium and International Organization for Standardization. 2023. *Observations, Measurements and Samples*. OGC 20-082r4 / ISO 19156:2023. https://docs.ogc.org/as/20-082r4/20-082r4.html.

OPC Foundation. n.d. *OPC Unified Architecture Part 100: Devices*. Version 1.05.0. https://reference.opcfoundation.org/specs/OPC-10000-100/full.

World Wide Web Consortium. 2023a. *Web of Things (WoT) Architecture 1.1*. W3C Recommendation, December 5. https://www.w3.org/TR/wot-architecture11/.

World Wide Web Consortium. 2023b. *Web of Things (WoT) Thing Description 1.1*. W3C Recommendation, December 5. https://www.w3.org/TR/wot-thing-description11/.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology—2023 Edition*. Working Draft, October 21. https://www.w3.org/TR/vocab-ssn-2023/.
