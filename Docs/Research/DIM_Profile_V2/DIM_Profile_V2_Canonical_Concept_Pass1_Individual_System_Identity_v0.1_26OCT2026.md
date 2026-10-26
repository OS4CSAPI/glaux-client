# Domain Information Model (DIM) / Application Profile Version 2 (V2)
## Canonical Concept Consolidation — Pass 1: Individual System Identity

**Date:** 26 October 2026  
**Standing:** Sourced candidate for human review; **not** an adopted DIM class, root concept, domain name, or profile requirement.  
**Revision:** Cited synthesis and donor-to-synthesis narrative pedigree retained; wording revised to use established donor terminology rather than the project-coined phrase “remains the referent.”  
**Method:** One concept only, under the [incremental consolidation plan](DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md). The [refined subject-and-boundary hypothesis](DIM_Profile_V2_Refined_Subject_Boundary_Pedigree_v0.1_26OCT2026.md) remains provisional.

## 1. The question

**What is the particular thing being described, independently of its identifier, product type, implemented method, observations, deployments, or the services through which it is represented?**

Consider two thermometers of the same product model. They are not the same individual. One thermometer might later be relocated, reconfigured, or described by another server, yet a new description or server address alone does not demonstrate that a different thermometer exists. This is an explanatory example, **not** a universal identity-continuity or component-replacement rule.

## 2. Synthesized candidate meaning, with inline source pedigree

> **For the present V2 investigation, the subject is an individual System, characterized in CSAPI by `systemType = Sensor` and `assetType = Equipment`** (Open Geospatial Consortium 2025a, secs. 9.1–9.2.2; World Wide Web Consortium and Open Geospatial Consortium 2026, secs. 5.3.5.2.4 and 8.16). **An individual System is distinct from its product kind or model, the Procedures it implements, and the identifiers, API resources, or digital descriptions used to identify or represent it** (Open Geospatial Consortium 2025a, secs. 9.2.2–9.3 and 13.1–13.2; European Telecommunications Standards Institute 2024, “Device kinds and devices”; Industrial Digital Twin Association 2026, “Asset Administration Shell Attributes” and “Asset Information Attributes”; OPC Foundation n.d., secs. 3.3.2, 4.5.2, and 4.9). **The same System may be described by different services and associated with information that changes over time, including its configuration, state, deployments, observations, and events** (Open Geospatial Consortium 2025a, secs. 8.5, 9.2.2, and 11.2; Open Geospatial Consortium 2025b, secs. 9.7 and 12.2; World Wide Web Consortium and Open Geospatial Consortium 2026, secs. 5.3.4.2.11 and 5.3.5.2). **Changes to that information do not, by themselves, establish that a different individual System is being described.**

**Standing of this wording:** No cited donor states these four sentences as one definition. The citations identify the donor-native distinctions behind the synthesis. The final sentence is **our narrow inference from those distinctions**, not an assertion that every repair, component exchange, or replacement preserves System identity. The wording deliberately uses the donors' existing terms—*individual System* and *System instance*—instead of inventing a new V2 label.

## 3. Where each building block comes from—and what it means in its donor

### 3.1 “For the present V2 investigation” — a bounded selection, not a donor definition

**What the donor means.** Open Geospatial Consortium (OGC) Application Programming Interface (API) – Connected Systems (CSAPI) covers multiple kinds of Systems and asset realizations, including hardware Sensors, simulated Sensors, humans, Actuators, and Platforms. The `systemType` and `assetType` facets are independent; `Sensor + Equipment` is an expressly illustrated combination rather than a distinct CSAPI class (Open Geospatial Consortium 2025a, secs. 9.1–9.2.2). The wider Sensor, Observation, Sample, and Actuator / Semantic Sensor Network (SOSA/SSN) ontology likewise permits System realizations other than equipment (World Wide Web Consortium and Open Geospatial Consortium 2026, sec. 5.3.5.2.4).

**How it contributes to the synthesis.** The words *for the present V2 investigation* are deliberate scope restraint: V2 currently investigates equipment-realized Systems whose primary role is sensing. Neither the whole CSAPI universe nor every instance of SOSA/SSN System becomes automatically in scope. This is **our selection of a research boundary**, not a new requirement imposed by either donor.

### 3.2 “An individual System” — a particular System instance, not a general type

**What the donors mean.** CSAPI defines a `System` resource describing an instance of a System, with its own attributes, associations, and canonical resource representation (Open Geospatial Consortium 2025a, sec. 9.2). The World Wide Web Consortium (W3C)/OGC 2023-edition Working Draft defines `sosa:System` as an Asset implementing a Procedure in the context of an Execution. Crucially, its section 8.16 distinguishes an **individual System**—modeled as an instance—from a **system type**, which can be modeled as a Web Ontology Language (OWL) class (World Wide Web Consortium and Open Geospatial Consortium 2026, secs. 5.3.5.2.4 and 8.16).

The European Telecommunications Standards Institute (ETSI) Smart Applications REFerence (SAREF) ontology independently says that a `saref:Device` instance represents one specific tangible real-world entity, distinct from an archetypal `DeviceKind` (European Telecommunications Standards Institute 2024, “Device kinds and devices”). The Open Group **Sensor Open Systems Architecture** (Open Group SOSA)—not the W3C/OGC SOSA vocabulary—supplies complementary evidence for describing a complete bounded Sensor, not only one detector, with hardware and software supporting its functions (The Open Group 2023).

**How it contributes to the synthesis.** We are describing **one particular equipment System** at whatever coherent whole-system scale is justified, not a generic product family, measurement stream, or ontology class. This is **alignment in the intended individual-versus-type distinction**, not a claim that CSAPI `System`, `sosa:System`, `saref:Device`, and the Open Group SOSA Sensor are interchangeable classes. CSAPI's published standard and the 2026 SOSA/SSN Working Draft must also retain their edition/dependency distinction; the draft does not silently revise CSAPI 1.0's original normative references.

### 3.3 “Distinct from its identifiers” — the System versus ways of identifying it

**What the donors mean.** CSAPI requires a System `uniqueIdentifier` in Uniform Resource Identifier (URI) form and separately requires a canonical Uniform Resource Locator (URL). The standard says the unique identifier **should** be persistent and independent of the URL; its being a required field does **not** turn the persistence recommendation into an unconditional lifetime `SHALL` (Open Geospatial Consortium 2025a, secs. 9.2.2–9.3).

Open Platform Communications Unified Architecture (OPC UA) Devices independently distinguishes identifiers associated with a manufactured Device, including `SerialNumber` and `ProductInstanceUri`, from OPC UA AddressSpace Node identifiers. Its Device definition concerns an independent physical entity delimited by interfaces, including composite Devices (OPC Foundation n.d., secs. 3.1.5, 3.3.2, 4.5.2, and 4.9). The Industrial Digital Twin Association (IDTA) Asset Administration Shell (AAS) likewise separates identification of the **represented Asset** in `AssetInformation` from identification of the **Shell** itself. In AAS 3.2, `globalAssetId` can initially be absent, but `globalAssetId` or at least one `specificAssetId` must be supplied under constraint AASd-131; `specificAssetId` need not itself be globally unique (Industrial Digital Twin Association 2026, “Asset Administration Shell Attributes,” “Asset Information Attributes,” and “Specific Asset ID Attributes”).

**How it contributes to the synthesis.** “Distinguishable” means that two physical units, even if they share a product kind, must be capable of being understood as different individuals. An identifier **refers to** an individual; it is not the individual. These standards provide useful but different identity mechanisms. V2 has **not** selected a universal identifier syntax, reconciliation policy, or identity-continuity rule by recognizing that distinction.

### 3.4 “`systemType = Sensor` and `assetType = Equipment`” — separate role and realization

**What the donors mean.** CSAPI's `systemType = Sensor` identifies Systems whose **primary activity** is sensing or observing. Its independent `assetType = Equipment` denotes a System made of one or more hardware devices or pieces of equipment interacting directly with the real world. The standard explicitly uses digital probes, Global Positioning System receivers, and video cameras as Sensor + Equipment examples, while also supplying other role/realization combinations (Open Geospatial Consortium 2025a, secs. 9.1–9.2.2).

W3C/OGC SOSA/SSN supplies the broader conceptual `Sensor` specialization of `System`; SAREF separately recognizes tangible `Device` instances including Sensors. Open Group SOSA supplies a bounded whole-Sensor architectural example whose support functions need not themselves be sensing functions (World Wide Web Consortium and Open Geospatial Consortium 2026, secs. 5.3.5.2.4 and 5.5.2.4; European Telecommunications Standards Institute 2024, “Device kinds and devices”; The Open Group 2023).

**How it contributes to the synthesis.** **System** identifies what is being represented, **Sensor** its defining role, and **Equipment** its realization, using CSAPI's native facets. We **do not** coin a `SensorEquipmentSystem` class, infer that every supporting part is a Sensor, or treat “physical” as equivalent to CSAPI's narrower Equipment category. This same role/realization distinction was established before the donor comparison and remains the V2 baseline.

### 3.5 “The same System … information that changes over time” — a System versus information about it

**What the donors mean.** CSAPI associates a System with its description, validity interval, location and deployment context; the same System is separately linked to observations, commands and `SystemEvent` records. Part 2 explicitly links `SystemEvent` to the System it concerns and models Observation as a resource distinct from System (Open Geospatial Consortium 2025a, secs. 9.2.2, 11.2; Open Geospatial Consortium 2025b, secs. 9.7 and 12.2). SOSA/SSN separately relates a System to Executions through `madeBySystem`/`madeExecution` and to Deployment through distinct relationships (World Wide Web Consortium and Open Geospatial Consortium 2026, secs. 5.3.4.2.11 and 5.3.5.2).

AAS separately organizes digital descriptions of an Asset through a Shell and aspect-specific Submodels. A Shell or Submodel can be identified and changed without those information structures becoming the Asset itself (Industrial Digital Twin Association 2026, “Asset Administration Shell Attributes” and “Submodel Attributes”).

**How it contributes to the synthesis.** The donors distinguish **an individual System from changing information about that System**: its location, reported condition, settings, deployments, descriptions, and generated records may vary. From that distinction, V2 infers that updating those descriptions or records does not, by itself, establish a new System instance. This is **our limited inference**, not a promise that hardware replacement, reconstruction, or administrative relabeling necessarily preserves identity. That unresolved question remains below.

### 3.6 “Not identical to a product kind” — an instance is not its reusable archetype

**What the donors mean.** The 2026 SOSA/SSN Working Draft expressly represents system **types** as ontology classes and **individuals** as their instances; system-type capabilities and datasheets can describe numerous physical units (World Wide Web Consortium and Open Geospatial Consortium 2026, sec. 8.16). SAREF's `DeviceKind` describes a reusable archetype and can be linked through `hasDeviceKind` to an individual `Device` (European Telecommunications Standards Institute 2024, “Device kinds and devices”). AAS distinguishes Type and Instance in `AssetKind` and allows a type asset to be referenced by an instance asset; OPC UA Devices distinguishes `Model` from production-level `SerialNumber` or `ProductInstanceUri` (Industrial Digital Twin Association 2026, “Asset Information Attributes”; OPC Foundation n.d., sec. 4.5.2).

**How it contributes to the synthesis.** Two instances can share a product specification without becoming one individual. This recurring distinction justifies excluding **kind/model identity from individual identity**. It does **not** decide whether V2 should adopt an OWL class pattern, `DeviceKind`, an AAS Type Asset, or CSAPI's `systemKind` carrier. **Pass 2** investigates that further.

### 3.7 “Not identical to an implemented method” — performer versus Procedure

**What the donors mean.** SOSA/SSN's `System` implements a reusable `Procedure`; the System that performs an Execution is not the Procedure it uses (World Wide Web Consortium and Open Geospatial Consortium 2026, secs. 5.3.5.2.4 and 5.3.4.2). CSAPI uses `Procedure` resources in more than one role. Its `systemKind` relation points to **one Procedure resource describing the kind of System**, such as a datasheet; its separately defined `procedures` relation points to **Procedures the System implements** (Open Geospatial Consortium 2025a, secs. 9.2.2 and 13.1–13.2).

**How it contributes to the synthesis.** **An individual instrument is not the repeatable method it can execute**, even where a native standard happens to reuse the same resource type to carry kind descriptions and procedures. The distinct meanings of `systemKind` and `procedures` were specifically corrected in the project's C08 calibration audit; they must not be collapsed. **Pass 3** handles detailed Procedure/Method consolidation.

### 3.8 “Not identical to an identifier string, API resource, or digital representation”

**What the donors mean.** CSAPI's System has a URI-valued `uniqueIdentifier` and an independently specified canonical API URL. AAS distinguishes the represented Asset from its separately identifiable Shell and Submodels. OPC UA distinguishes manufactured Device identification from AddressSpace Node identity and permits one Server to expose multiple Devices or a gateway for multiple Devices (Open Geospatial Consortium 2025a, secs. 9.2.2–9.3; Industrial Digital Twin Association 2026, “Asset Administration Shell Attributes”; OPC Foundation n.d., secs. 3.3.2, 4.5.2, and 4.9).

**How it contributes to the synthesis.** Names, IDs, resource paths, Nodes, Shells, and digital representations are **ways to refer to, expose, or describe the underlying subject**; they are not interchangeable with it. This is the strongest *cross-community* corroboration of our non-conflation rule. It does **not** prove that any two separate representations refer to the same individual without evidence linking them, nor does it settle digital-twin/proxy relationships. **Pass 5** addresses representation semantics.

### 3.9 “Not identical to an observation” — an enduring source is not an execution/result

**What the donors mean.** The SOSA/SSN pattern separates System/Sensor from Observation, an Execution that can refer to its executing System through `madeBySystem`/`madeBySensor` (World Wide Web Consortium and Open Geospatial Consortium 2026, secs. 5.3.4.2.11 and 5.5.2). CSAPI likewise distinguishes the System resource from its DataStreams and individual Observations; the same System may be associated with multiple records over time (Open Geospatial Consortium 2025a, sec. 9.2; Open Geospatial Consortium 2025b, secs. 9.2 and 9.7).

**How it contributes to the synthesis.** The equipment System is **the subject/source being described**. Observation is information about an occurrence or result associated with it, not its individual identity. This preserves the original whole-system objective: understanding the System is broader than retrieving the measurements it produces.

## 4. What this pass establishes—and what it does not

The strongest convergence is the **distinction between an individual System and the different information or representations associated with it**. CSAPI and the current SOSA/SSN draft share an explicit semantic lineage and must not be counted as independent discoveries; SAREF, OPC UA, AAS, and Open Group SOSA contribute independent but **not fully equivalent** perspectives. Open Group SOSA's role here is evidence for a bounded heterogeneous Sensor as the whole subject, **not** a claim that its architecture offers the same instance identity rules as the other donors.

The term **individual System** remains plain research wording, not a newly adopted canonical ontology class. This paper recommends retaining the distinction in subsequent concept consolidation, without choosing identifier syntax, kind/model realization, procedure encoding, component cardinalities, digital-twin constructs, or conformance tests.

The Open Group SOSA claims rely on the project's frozen C15 extraction from the Edition 1.1 architecture and Edition 1.0 Domain-Specific Data Model. They have **not** been newly clause-verified in this pass. The W3C/OGC SOSA/SSN source is the **21 October 2026 Working Draft**, distinct from the earlier edition cited normatively by published CSAPI 1.0.

## 5. Material open questions

**Identity through replacement.** Does the System remain the same individual after repair, exchange of a major component, or wholesale replacement? There is no universal answer established by this pass; defer the threshold question rather than invent it.

**Cross-source reconciliation.** When different services or donor implementations use different identifiers, evidence or an explicit mapping is required to assert that they refer to one individual. Matching product names, model numbers, or labels is insufficient.

**Granularity of individuals.** Whether a transducer channel, detachable detector, component, or assembled whole should be represented as its own individual System belongs to **Pass 4**.

**Disposition:** Pass 1 yields a cited, traceable **candidate meaning**, not a final adopted DIM concept. The next authorized increment under the plan is **Pass 2 — Product / Model / Kind**, after review of this meaning.

**Modeling-pilot follow-up:** [Pass 1 UML instance-view pilot](DIM_Profile_V2_Pass1_Modeling_Pilot_v0.1_26OCT2026.md) tested the candidate meaning against established notation. It illustrates two distinct instances without establishing a new `IndividualSystem` class, source-identifier reconciliation rule, or premature relationships to later concepts.

## References — Chicago Manual of Style, 18th ed., author-date

European Telecommunications Standards Institute. 2024. *SAREF: Smart Applications REFerence Ontology—Core*. Version 4.1.1. https://saref.etsi.org/core/v4.1.1/.

Industrial Digital Twin Association. 2026. *Specification of the Asset Administration Shell, Part 1: Metamodel*. Version 3.2, July. https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/index.html.

Open Geospatial Consortium. 2025a. *OGC API—Connected Systems—Part 1: Feature Resources*. OGC 23-001, version 1.0, July 16. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC API—Connected Systems—Part 2: Dynamic Data*. OGC 23-002, version 1.0, July 16. https://docs.ogc.org/is/23-002/23-002.html.

OPC Foundation. n.d. *OPC Unified Architecture Part 100: Devices*. Version 1.05.0. https://reference.opcfoundation.org/specs/OPC-10000-100/full.

The Open Group. 2022. *SOSA Domain-Specific Data Model*, Edition 1.0. Frozen project reference artifact.

The Open Group. 2023. *Technical Standard for SOSA Reference Architecture*, Edition 1.1. C239, June, with September erratum. Frozen project reference artifact.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology—2023 Edition*. Working Draft, October 21. https://www.w3.org/TR/vocab-ssn-2023/.
