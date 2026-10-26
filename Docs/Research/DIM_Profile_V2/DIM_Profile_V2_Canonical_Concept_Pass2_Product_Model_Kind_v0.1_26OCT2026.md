# Domain Information Model (DIM) / Application Profile Version 2 (V2)
## Canonical Concept Consolidation — Pass 2: Product / Model / Kind

**Date:** 26 October 2026  
**Standing:** Sourced **candidate concept meaning for human review**. Not a new V2 class, adopted relationship, final model architecture, or application-profile requirement.  
**Controlling method:** [Incremental concept plan](DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md); [Pass 1—Individual System Identity](DIM_Profile_V2_Canonical_Concept_Pass1_Individual_System_Identity_v0.1_26OCT2026.md); [C08 validation audit](DIM_Profile_V2_Anatomy_PhaseA_Validation_Audit_v0.1_26OCT2026.md).  
**Evidence discipline:** Donor-native meaning is distinguished from our synthesis, eventual API binding and conformance. The World Wide Web Consortium (W3C)/Open Geospatial Consortium (OGC) Sensor, Observation, Sample, and Actuator / Semantic Sensor Network (SOSA/SSN) “2023 Edition” source is a **21 October 2026 Working Draft**, not the edition normatively cited by published Connected Systems 1.0.

## 1. Question

**How should information about what kind of sensing equipment a System is—its reusable product/model/type description—relate to an individual System, without assuming that every donor's “type” or “model” means the same thing?**

This is an identity-versus-kind investigation. **Procedure/Method** is deliberately held for Pass 3, **composition** for Pass 4, and digital representation/proxy identity for Pass 5.

## 2. Synthesized candidate meaning, with inline source pedigree

> **For the present V2 investigation, an individual System can be described in terms of a reusable kind or model—such as a sensor manufacturer's product model or datasheet—whose common characteristics can apply to multiple individual Systems of that kind** (Open Geospatial Consortium 2025a, §§ 9.2.2, 13.1; Open Geospatial Consortium 2025b, §§ 7.2, 8.2.9.3; European Telecommunications Standards Institute 2024, “Device kinds and devices”; Industrial Digital Twin Association 2026, “Types and Instances”). **The kind/model description is distinct from an individual System's identity and from information specific to that individual, such as its serial number, installed configuration, deployment, or current state** (Open Geospatial Consortium 2025b, §§ 7.2, 8.2.9.3; Industrial Digital Twin Association 2026, “Types and Instances”; OPC Foundation n.d., § 4.5.2; World Wide Web Consortium and Open Geospatial Consortium 2026, § 8.16). **Descriptions called “type” or “model” in other standards must retain their native roles; a reusable interaction template or an information-model ObjectType is not automatically the manufacturer's product model** (World Wide Web Consortium 2023, §§ 1.2, 9.1; OPC Foundation n.d., §§ 4.5.2, 4.7). **A description of the kind of System also remains distinct from a Procedure or Method that a System can implement, even when Connected Systems uses the same Procedure resource type to carry both kinds of description** (Open Geospatial Consortium 2025a, §§ 9.2.2, 13.1).

**Status of this synthesis:** The distinction between an individual and reusable kind/type information is **directly donor-supported**. The wording above connects those native distinctions for our bounded V2 target; **it is not a proposed `ProductModel`, `SystemKind`, or other new V2 class**, nor a claim that all source-specific descriptions are interchangeable.

## 3. The building blocks—what they mean to each donor, and what V2 takes from them

### 3.1 “Individual System” versus “kind of System” — CSAPI supplies the immediate native relationship

**Donor-native meaning.** In Open Geospatial Consortium (OGC) Application Programming Interface (API) – Connected Systems (CSAPI) Part 1, `System` resources describe **individual system instances**. The optional `systemKind` association points to **one `Procedure` resource** describing the *kind* of that System—for example a product datasheet. Separately, the optional `procedures` association points to **the Procedures the System can implement**. Section 13.1 explicitly distinguishes using a Procedure resource to describe a sensor model from using one to describe an observing or sampling methodology (Open Geospatial Consortium 2025a, §§ 9.2.2, 13.1).

**Contribution to V2.** This is the clearest intended **CSAPI binding anchor** for the reusable-kind relationship. It establishes that the same reusable description can apply to several individual Systems, but that a *kind/model association* and *implements-a-method association* are two different relationships. **The single-target cardinality and use of a Procedure resource are CSAPI-native mechanics; we have not promoted either into a DIM-wide class or mandatory cardinality.** This is exactly the distinction recovered in the C08 audit.

### 3.2 “Manufacturer's sensor model versus a configured instance” — SensorML supplies a rich native description pattern

**Donor-native meaning.** OGC Sensor Model Language (SensorML) 3.0 explicitly distinguishes a **general process description** from a **specific process instance**. A manufacturer may publish common model-level inputs, outputs, characteristics, capabilities and allowed configuration options; the owner of a particular unit adds its serial number, location, calibration and selected settings. A specific process can reference a more general process via `typeOf`; its configuration can further restrict choices made available by that model. SensorML calls this process inheritance/configuration, not a universal physical-product ontology (Open Geospatial Consortium 2025b, §§ 7.2, 8.2.9.3.1–8.2.9.3.2).

**Contribution to V2.** This supplies the most concrete OGC-standard example of **reusing a shared technical model without copying or confusing instance-specific facts**. It also shows why a model's *permitted* settings or *rated* performance cannot be equated with an individual unit's selected configuration or measured condition. The `typeOf` and `configuration` properties remain **SensorML-specific representations**; deciding whether they appear in a CSAPI profile is later work.

### 3.3 “System type versus individual” — SOSA/SSN supplies an ontology pattern, not an industrial product registry

**Donor-native meaning.** Section 8.16 of the W3C/OGC SOSA/SSN Working Draft says that individual Systems often share a primary description by type or model number; such type-level specifications traditionally occur in datasheets. Its recommended ontology pattern represents a **system type as a Web Ontology Language (OWL) class** (a subclass of `sosa:System` or a specialization), and an **individual System as an instance** of that class (World Wide Web Consortium and Open Geospatial Consortium 2026, § 8.16).

**Contribution to V2.** This strengthens the type/instance distinction *in the intended semantic environment*, but it is **not independent corroboration of CSAPI's lineage** and does **not require** V2 to mint one OWL class for every commercial product, nor turn CSAPI's `systemKind` association into a Resource Description Framework (RDF) `rdf:type` assertion. Ontological classification, product identification, and the CSAPI relation are not automatically identical.

### 3.4 “DeviceKind” — an explicit device-kind semantic donor

**Donor-native meaning.** European Telecommunications Standards Institute (ETSI) Smart Applications REFerence (SAREF) Core 4.1.1 defines `saref:Device` for a specific tangible entity and `saref:DeviceKind` for prototypical descriptions that can populate device taxonomies and catalogues. `saref:hasDeviceKind` connects a particular Device to a kind. Device kinds can specify **shared functions, services, properties and states**, and may describe commercial models. SAREF **also has** `saref:hasModel` and `saref:hasManufacturer` data properties: a model-name string is not automatically the same thing as a modeled `DeviceKind` resource (European Telecommunications Standards Institute 2024, “Device kinds and devices”; “Functions”).

**Contribution to V2.** SAREF offers a source-owned, explicit **individual-to-reusable-kind** concept that aligns closely with the purpose of CSAPI's `systemKind`. It is a strong **semantic mapping candidate**, not proof that the exact SAREF `DeviceKind` class is equivalent to a CSAPI `Procedure` resource or that the DIM needs to create a new `DeviceKind` surrogate.

### 3.5 “Type asset versus instance asset” — the industrial-product/lifecycle perspective

**Donor-native meaning.** Industrial Digital Twin Association (IDTA) Asset Administration Shell (AAS) version 3.2 distinguishes **type assets** and **instance assets** using `AssetInformation.assetKind`; Batch, Role and NotApplicable are other native values. The standard's example creates **one type asset for a temperature-sensor model and two individually identified physical sensors of that type**, with shared type information and different operational instance information. An instance's `AssetInformation.assetType` can identify the **type asset** it is of; links among Shells and assets require their own proper interpretation (Industrial Digital Twin Association 2026, “Types and Instances,” especially “Asset Administration Shells Representing Type Assets and Instance Assets”; “Asset Information Attributes”).

**Contribution to V2.** This is especially useful corroboration of **a genuinely reusable manufactured-product type, with multiple independently identified fielded units**. But **AAS `assetType` and CSAPI `assetType` are *different concepts despite sharing a property name***: the AAS property identifies a type asset, whereas the CSAPI property classifies a realization such as Equipment, Human or Simulation (Industrial Digital Twin Association 2026, “Asset Information Attributes”; Open Geospatial Consortium 2025a, § 9.2.2). AAS type assets also must not be confused with AAS *Submodel templates* or with software programming class definitions.

### 3.6 “Manufacturer Model” versus “DeviceType” — nameplate versus information-model typing

**Donor-native meaning.** Open Platform Communications Unified Architecture (OPC UA) Part 100: Devices defines manufacturer/product **nameplate properties** such as `Manufacturer`, `Model`, `ProductCode`, `DeviceManual` and product-instance properties such as `SerialNumber` and `ProductInstanceUri` (§ 4.5.2). Its `DeviceType` (§ 4.7) is instead an **abstract OPC UA ObjectType** for the *structure of a Device representation*; only concrete subtypes can have instances. It is **not, by definition, a manufacturer's model designation** (OPC Foundation n.d., §§ 4.5.2, 4.7).

**Contribution to V2.** The practical distinction is between a **manufacturer product identification**, a **particular manufactured item**, and a **standardized information-model type**. A `Model` value by itself may be useful information but does not necessarily supply a resolvable, reusable technical specification. Conversely, `DeviceType` tells a client something about OPC UA structure but does not prove which product model the represented System is.

### 3.7 “Thing Model” — reusable interface typing, not automatically a product datasheet

**Donor-native meaning.** W3C Web of Things (WoT) Thing Description 1.1 defines a `Thing Model` as a reusable description/template primarily for common **Properties, Actions and Events**; it need not supply instance-specific communication endpoints, serial numbers or locations. It can help produce an individual `Thing Description`, including a link indicating its associated model (World Wide Web Consortium 2023, §§ 1.2, 9.1, 9.4).

**Contribution to V2.** This is good corroboration that descriptions at a **reusable type level differ from individual descriptions**. But a Thing Model is primarily about **the Web-visible interaction contract**, not necessarily about a physical product model, its calibrated performance, or hardware specification. For V2 it may be a *related but partial mapping* or specialized interface viewpoint; it is not a substitute for a manufacturer model or a donor-neutral DIM kind class.

**Additional boundary check—Matter 1.3.** The frozen Matter Phase A extraction describes `Device Type` as a **functional/conformance classification of an Endpoint**, distinct from product identity carried elsewhere in Matter. This is useful caution against treating every “device type” as a product model, but C06 remains **YELLOW** because Core 1.3 normative details were not fully rechecked here. It is **not** affirmative evidence for a V2 cardinality or class.

## 4. What aligns, what only partially maps, and what would be a mistake

| Source-native concept | What it actually describes | Relevant relationship to V2 | Mapping caution |
| --- | --- | --- | --- |
| CSAPI `systemKind` → `Procedure` | Kind of System, e.g., datasheet | **Direct target-binding anchor** | Procedure carrier ≠ implemented method |
| SensorML `typeOf` | Specific process referring to a general process, possibly with settings | **Detailed shared-specification pattern** | Process inheritance ≠ all kinds of product classification |
| SOSA/SSN system-type OWL class | An ontology class for instances of a system type | **Ontology correspondence** | Class assertion ≠ CSAPI `systemKind` link |
| SAREF `DeviceKind` | Reusable device archetype and common characteristics | **Close semantic alignment** | Not declared equivalent to a CSAPI Procedure |
| AAS Type Asset | Industrial asset/product type with its own identity and lifecycle | **Close industrial type/instance analogy** | AAS `assetType` ≠ CSAPI `assetType` |
| OPC UA `Model`; `DeviceType` | Manufacturer model name; separate structural ObjectType | **Two complementary kinds of information** | Neither automatically supplies the other's semantics |
| WoT `Thing Model` | Reusable Thing interaction/interface description | **Partial, interface-specific alignment** | Not necessarily a physical product specification |

**Synthesis:** V2 needs to preserve the distinction **individual System ↔ reusable kind/model description** as a semantic relationship **where such a description is available**. The donor corpus **does not yet justify** one uniform canonical data structure or class called `ProductModel`, nor an obligation that every System has exactly one such linked resource. Not all sources provide the same degree of product or type description; **we should preserve the information they actually provide rather than manufacture missing detail**.

## 5. Why this has practical value

Imagine two deployed temperature sensors of the **same manufacturer model**, each with a different serial number, configuration, location, calibration history and observations. A reusable model specification may state the *supported range and available modes*; the individual descriptions state *which unit is deployed, how it is configured, and what it reports*. Those are not interchangeable facts (Open Geospatial Consortium 2025b, §§ 7.2, 8.2.9.3; Industrial Digital Twin Association 2026, “Types and Instances”).

An integrated CSAPI view should be able to preserve that source distinction while allowing equipment descriptions to reuse common model-level knowledge. If its source instead provides only an OPC UA `Model` string or a WoT `Thing Model`, V2 should not silently assert that a manufacturer datasheet or full equipment product kind has been resolved. **Compatibility requires preserving meaning, including partial information and absent relationships—not filling in the gaps with a convenient universal class.**

## 6. Material questions deliberately left open

1. **Reuse and multiplicity.** Does the eventual conceptual model need to express more than one kind/classification or version for a System? CSAPI's optional single `systemKind` link, SAREF's kind descriptions, and other donors do not justify imposing one global DIM multiplicity now.
2. **Description identity and version.** How should a model description be identified, versioned or resolved across vendors and revisions, especially when only a manufacturer/model label is supplied? This cannot be inferred from a string alone.
3. **Relationship to implemented Procedures.** Pass 3 must determine the exact semantics of methodologies and implemented behavior **without collapsing them into the kind/model descriptions** merely because CSAPI uses one resource type for both roles.

**Disposition:** **Candidate meaning supported; adoption of a new V2 term/class or universal type syntax is *not* justified.** Stop here. **Next pass under the plan, only when directed: Pass 3 — Procedure / Method.**

## References — Chicago Manual of Style, 18th ed., author-date

European Telecommunications Standards Institute. 2024. *SAREF: Smart Applications REFerence Ontology—Core*. Version 4.1.1. https://saref.etsi.org/core/v4.1.1/.

Industrial Digital Twin Association. 2026. *Specification of the Asset Administration Shell, Part 1: Metamodel*. Version 3.2, especially “Types and Instances” and “Asset Information Attributes.” https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/annex/general.html; https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/core.html.

Open Geospatial Consortium. 2025a. *OGC API—Connected Systems—Part 1: Feature Resources*. OGC 23-001, version 1.0, July 16. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC SensorML Encoding Standard*. OGC 23-000, version 3.0, July 16. https://docs.ogc.org/is/23-000/23-000.html.

OPC Foundation. n.d. *OPC Unified Architecture Part 100: Devices*. Version 1.05.0. https://reference.opcfoundation.org/specs/OPC-10000-100/full.

World Wide Web Consortium. 2023. *Web of Things (WoT) Thing Description 1.1*. W3C Recommendation, December 5. https://www.w3.org/TR/wot-thing-description11/.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology—2023 Edition*. Working Draft, October 21, § 8.16. https://www.w3.org/TR/vocab-ssn-2023/.

*Evidence note:* The Matter 1.3 comment is a bounded use of the frozen C06 extraction under its **YELLOW** evidence ceiling; it is not a new normative-verification claim. All other material source distinctions above were cross-checked against the cited, publicly accessible, official source editions. The source model's normative obligations have **not** been adopted as V2 obligations.
