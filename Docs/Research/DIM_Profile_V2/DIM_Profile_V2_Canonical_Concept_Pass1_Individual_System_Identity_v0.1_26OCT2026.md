# Domain Information Model (DIM) / Application Profile Version 2 (V2)
## Canonical Concept Consolidation — Pass 1: Individual System Identity

**Date:** 26 October 2026  
**Status:** Candidate research finding for human review; **not** a frozen DIM class, root, or profile requirement.  
**Method:** One-concept comparison under the [incremental plan](DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md). The [refined subject-and-boundary hypothesis](DIM_Profile_V2_Refined_Subject_Boundary_Pedigree_v0.1_26OCT2026.md) remains provisional.

### 1. The question, in ordinary terms

**What is the particular thing we are describing, independently of what it is called, what model it belongs to, where it is deployed, what it produces, or which service currently represents it?**

A temperature sensor may be relocated, reconfigured, or represented by two servers without becoming a different sensor simply because those descriptions change. Conversely, two sensors of the same product model are not the same individual. This is an explanatory test case, **not** a claim that every source defines the same identity or replacement rules.

### 2. What the donors actually contribute

**Open Geospatial Consortium (OGC) Application Programming Interface (API) – Connected Systems (CSAPI) — primary implementation anchor.** Its `System` resource represents an instance of a system. Part 1 requires `uniqueIdentifier` (a uniform resource identifier) and a separate canonical API resource URL. The standard says the unique identifier **should** be persistent and independent of the URL; it does not make lifetime persistence an unconditional `SHALL`. A resource also carries `systemType` (required) and may carry `assetType` (optional). For the sensing-equipment cases motivating V2, `Sensor + Equipment` is the sourced **role/realization characterization**, not a newly named class (Open Geospatial Consortium 2025, secs. 9.1–9.3). **Contribution:** distinguish the individual System referent from its API address and descriptive classifications.

**Sensor, Observation, Sample, and Actuator / Semantic Sensor Network (SOSA/SSN) — conceptual anchor, with edition caution.** The World Wide Web Consortium (W3C)/OGC *Semantic Sensor Network Ontology—2023 Edition* Working Draft defines `sosa:System` as an Asset implementing a Procedure in the context of an Execution. Its § 8.16 explicitly distinguishes a **system type represented by an ontology class** from an **individual system represented by an individual of that class**. It also covers non-equipment Systems, including software and human agents, and distinguishes `Platform` from `System` in its class structure (W3C and Open Geospatial Consortium 2026, secs. 5.3.5.2, 8.16). **Contribution:** instance-versus-type and system-versus-execution distinctions. **Limit:** this is a 2026 Working Draft, not the 2017 Recommendation cited by published CSAPI 1.0. CSAPI's `systemType = Sensor` must not be treated automatically as a new Resource Description Framework/Web Ontology Language class assertion.

**European Telecommunications Standards Institute (ETSI) Smart Applications REFerence (SAREF) — independent ontology corroboration.** In SAREF Core 4.1.1, `saref:Device` is a *tangible* entity performing functions, and each Device instance denotes one specific real-world entity. `saref:DeviceKind` separately describes a reusable archetype/model; the Device can be associated with its kind through `saref:hasDeviceKind`. A Device is also classified as a SAREF4SYST System (ETSI 2024, “Device kinds and devices”). **Contribution:** a concrete individual is distinct from its reusable kind. **Limit:** `saref:Device` and a CSAPI `System` are not automatically equivalent across their full definitions.

**Open Platform Communications Unified Architecture (OPC UA) Part 100: Devices — independent engineering corroboration.** Part 100 defines Device as an independent physical entity, delimited by its interfaces, capable of sensing, actuation, communication, or control. Its information model distinguishes **manufacturer/product identifiers** (for example, `SerialNumber` and `ProductInstanceUri`) from OPC UA AddressSpace Nodes and their identifiers. A Device may itself comprise other Devices or parts, and a DeviceSet can expose one root Device or multiple independently represented Devices (OPC Foundation n.d., secs. 3.1.5, 4.5, 4.9). **Contribution:** identifying an equipment instance and describing its digital node are different matters. **Limit:** Part 100's Device is physically scoped and broader in function than our sensing-oriented V2 target.

**Industrial Digital Twin Association (IDTA) Asset Administration Shell (AAS) — independent representation/identity corroboration.** The AAS is itself identifiable but **represents an Asset** recorded in its `AssetInformation`. The metamodel distinguishes type, instance, batch, role, and non-applicable asset kinds. A `globalAssetId` is not always available at the beginning of an asset's lifecycle; the specification permits asset identification with at least one `specificAssetId` under its constraints (IDTA 2026, Part 1, “Asset Administration Shell Attributes” and “Asset Information Attributes”). **Contribution:** the represented asset is not the digital shell, and identifying information can have multiple scopes. **Limit:** an AAS may represent kinds of assets beyond our present sensing-equipment boundary.

**The Open Group Sensor Open Systems Architecture (Open Group SOSA) — bounded sensing-subject corroboration.** The Edition 1.1 Sensor architecture treats a Sensor as a whole subject containing sensor components and supporting hardware/software while distinguishing an external Host Platform. Its Domain-Specific Data Model separately identifies Sensor, components, Product, and ProductInstance (The Open Group 2023; 2022). **Contribution:** the individual can be a bounded, heterogeneous sensing System rather than one detector or one hardware box. **Limit:** these are architecture/data-model constructs, **not** a direct identity-class equivalence or identifier mandate for V2. This paragraph relies on the frozen C15 source extraction; it has not been independently clause-rechecked in this pass.

### 3. What aligns—and what does not

The strongest common proposition is **the individual referent is distinguishable from its description and from a reusable kind/type**. CSAPI, SAREF, OPC UA, and AAS substantiate this through different mechanisms; the SOSA/SSN draft states the instance/type distinction explicitly. Open Group SOSA adds evidence for a bounded *whole sensing subject*, rather than supplying the same identity formalism.

This is **agreement in modeling purpose, not equivalence of classes**. `System`, `Device`, `Asset`, `Sensor`, digital shell, and API node have different donor-native scope and meaning. The OGC and W3C/OGC sources also share a semantic lineage and must not be counted as two independent conceptual inventions. A named or identified **individual** can be composed of significant components; “individual” does not mean physically indivisible.

For V2, distinguish four things without prematurely defining the next passes: **(a)** the represented individual, **(b)** the identifier(s) used to refer to it, **(c)** the reusable model/kind or method associated with it, and **(d)** its digital descriptions/resources. The boundaries of **(c)** and **(d)** will be investigated in Passes 2, 3, and 5, not settled here.

### 4. Proposed V2 meaning — candidate, not new vocabulary

> **For the present V2 investigation, an individual System is a particular, distinguishable sensing-oriented equipment subject that remains the referent of information about it across changes in descriptions, configuration, state, deployments, outputs, interactions, and representations. Its identity is not identical to a product kind, method, identifier string, API resource, or observation.**

“Individual System” is **plain research wording**, not a proposed new class or universal root. It retains the working CSAPI-derived `System` / `Sensor` / `Equipment` frame without claiming that every donor defines this exact composite concept.

### 5. Open points that actually matter

- **Identity through replacement:** when a unit or major component is replaced, does the “same System” continue? The reviewed donors do not establish one universal answer. Do not invent one.
- **Identity reconciliation:** different source identifiers may refer to the same equipment, but equivalence requires evidence or an explicit mapping—not matching names, model numbers, or URLs.
- **Granularity:** which detector, channel, subdevice, or assembled whole deserves individual standing is the question for **Pass 4**, not this note.

**Pass 1 outcome:** a **candidate definition with strong donor pedigree**, but **not** an adopted DIM class or frozen final boundary. **Next under the plan:** Pass 2, Product / Model / Kind, only after this result has been made intelligible for human review.

### References

ETSI. 2024. *SAREF: Smart Applications REFerence Ontology—Core*. Version 4.1.1. https://saref.etsi.org/core/v4.1.1/.

IDTA. 2026. *Specification of the Asset Administration Shell, Part 1: Metamodel*. Version 3.2. https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/core.html.

OGC. 2025. *OGC API—Connected Systems—Part 1: Feature Resources*. OGC 23-001, version 1.0. https://docs.ogc.org/is/23-001/23-001.html.

OPC Foundation. n.d. *OPC Unified Architecture Part 100: Devices*. Version 1.05.0. https://reference.opcfoundation.org/specs/OPC-10000-100/full.

The Open Group. 2022. *SOSA Domain-Specific Data Model*, Edition 1.0, accompanying technical standard (frozen project source).

The Open Group. 2023. *Technical Standard for SOSA Reference Architecture*, Edition 1.1. C239, June (September erratum; frozen project source).

W3C and OGC. 2026. *Semantic Sensor Network Ontology—2023 Edition*. Working Draft, October 21. https://www.w3.org/TR/vocab-ssn-2023/.
