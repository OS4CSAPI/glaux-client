# Domain Information Model (DIM) / Application Profile Version 2 (V2)
## Canonical Concept Consolidation — Pass 4: Composition and Component Standing

**Date:** 26 October 2026  
**Standing:** **Cited candidate research finding**, not an adopted DIM component taxonomy, class model, application-profile requirement, or conformance claim.  
**Controlling continuity:** [Incremental concept plan](DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md), [Pass 1 — Individual System Identity](DIM_Profile_V2_Canonical_Concept_Pass1_Individual_System_Identity_v0.1_26OCT2026.md), [Pass 2 — Product / Model / Kind](DIM_Profile_V2_Canonical_Concept_Pass2_Product_Model_Kind_v0.1_26OCT2026.md), [Pass 3 — Procedure / Method](DIM_Profile_V2_Canonical_Concept_Pass3_Procedure_Method_v0.1_26OCT2026.md), and the [C08 audit](DIM_Profile_V2_Anatomy_PhaseA_Validation_Audit_v0.1_26OCT2026.md).  
**Source standing:** The World Wide Web Consortium/Open Geospatial Consortium Sensor, Observation, Sample, and Actuator / Semantic Sensor Network (SOSA/SSN) **21 October 2026 Working Draft** is used for current ontology evidence; published Connected Systems 1.0 has a different normative ontology-edition dependency. Operational unattended-ground-sensor examples retain the frozen S04 **YELLOW evidence limit**.

## 1. The question

**What is meaningfully part of an individual sensing System, what is related to it without being part of it, and when should an internal element be represented separately?**

These are **two questions, not one**. An element's **relationship to the whole** (integral, temporarily attached, hosted, functionally connected, etc.) is not the same question as its **level of description** (unmodeled internal detail, functional channel, identified component, independently described subsystem). Nor does the physical fact that an object contains smaller parts determine how every source must model those parts.

## 2. Synthesized candidate meaning, with Chicago author–date pedigree

> **An equipment-realized sensing System may be understood as a whole or through meaningful constituent elements; a described subsystem can itself be a System, while an internal functional element does not automatically have that standing** (Open Geospatial Consortium 2025a, §§ 10.1–10.3; World Wide Web Consortium and Open Geospatial Consortium 2026, §§ 5.3.5.2.4, 5.3.5.2.9, 8.15; Open Geospatial Consortium 2025b, §§ 8.4–8.6). **The relationship between the System and another element must preserve the difference between an integral, ordinarily enduring part and a non-permanent or interchangeable association** (Open Geospatial Consortium 2025a, § 10.2), **without confusing either with Platform hosting, Deployment, communication topology, or functional/data-flow connections** (World Wide Web Consortium and Open Geospatial Consortium 2026, §§ 5.3.5.2.2–5.3.5.2.14; Open Geospatial Consortium 2025b, §§ 8.4.1, 8.6.2; OPC Foundation n.d., §§ 4.1, 5.1, 6.2). **How deeply the System is described should reflect the distinct information that matters about its components, rather than requiring every physical element to become a separate System** (Open Geospatial Consortium 2025b, §§ 8.5.2, 8.6.2; World Wide Web Consortium and Open Geospatial Consortium 2026, § 8.15; Bosch Sensortec 2024, § 3.1; OPC Foundation n.d., §§ 4.1, 4.9, 9.4).

**Standing:** The donor concepts and contrasts cited above are source-native. The combined language **“reflect the distinct information that matters” is our provisional V2 interpretation of modeling granularity**, not a universal normative decision threshold supplied by a donor. No new `SystemComponent`, `EquipmentPart`, or universal `PartOf` class or relation is proposed.

## 3. The building blocks: donor-native meaning and contribution to V2

### 3.1 A subsystem may be a System in its own right — Connected Systems

**What the donor defines.** In the Open Geospatial Consortium (OGC) Application Programming Interface (API) – Connected Systems (**CSAPI**) Part 1, the optional **Subsystems** requirements class describes complex Systems using recursively nested **regular System resources**. The standard permits indefinitely nested subsystems and treats them as full System resources, not as anonymous fields of a parent System (Open Geospatial Consortium 2025a, §§ 10.1, 10.3).

**Why it matters to V2.** The same established System concept can describe a meaningful whole and a meaningful subordinate System. This avoids inventing a special class just because a System occupies a component role. However, **a CSAPI subsystem is not synonymous with every internal part**: the Subsystems API feature models Systems that warrant System-resource representation. Whether another donor's processing block or channel qualifies is a separate question. The nested resource URL is a CSAPI carrier mechanism, **not automatically the DIM's intrinsic relation encoding**.

### 3.2 “Composition” versus “Aggregation” — CSAPI's directly relevant distinction

**What the donor defines.** CSAPI § 10.2 calls **Composition** an association where a subsystem is **integral** to its parent and cannot or is not ordinarily removed during the parent's lifetime except for maintenance. The standard explicitly permits its Composition semantics where a part *could* exist independently but is rarely removed. **Aggregation** instead describes **non-permanent/interchangeable association** that may change parent over time. CSAPI expresses the former with nested System resources and the latter using **Deployment** resources. It illustrates built-in and interchangeable sensors on weather stations, unmanned vehicles, and mobile phones (Open Geospatial Consortium 2025a, § 10.2).

**Why it matters to V2.** An integral detector and an interchangeable sensor payload may both be physical equipment and both important enough to identify, but they **do not have the same relationship to the whole**. The donor gives V2 a compelling distinction to preserve. Its definition of Composition is **explicitly looser than strict Unified Modeling Language (UML) composite aggregation**; do **not** draw UML diamonds or import UML ownership/lifetime assumptions merely because CSAPI uses the same English term (Open Geospatial Consortium 2025a, § 10.2).

### 3.3 Subsystem, hosted-by, and deployed-in are different — SOSA/SSN

**What the donor defines.** The World Wide Web Consortium (W3C)/OGC SOSA/SSN Working Draft uses `sosa:hasSubSystem`/`sosa:isSubSystemOf` for a **System–component System** relationship. It separately defines `sosa:hosts`/`sosa:isHostedBy` for a **Platform hosting an Asset**, and `sosa:Deployment` and related properties for how Systems and Platforms are arranged for operational use, usually during an interval (World Wide Web Consortium and Open Geospatial Consortium 2026, §§ 5.3.5.2.2–5.3.5.2.14). The draft's **complex-device example** (§ 8.15) shows one temperature/humidity device package and its temperature and humidity sensing Systems separately represented as subsystems.

**Why it matters to V2.** The ontology confirms that **subsystem, host, and deployment are distinct predicates**, not three names for physical containment. Its complex-device example shows that two sensing channels/functions in one package **can** be separately modeled as component Sensors; it does **not** compel identical decomposition for every integrated multisensor device. SOSA/SSN's generic `hasSubSystem` relation does **not itself specify** CSAPI's permanence-based Composition/Aggregation choice. Likewise, a CSAPI `System` tagged `systemType = Sensor` does not thereby acquire a new OWL `sosa:Sensor` type assertion. This draft is research evidence, not a change to published CSAPI's normative ontology reference.

### 3.4 Physical Component versus Physical System is a description choice — SensorML

**What the donor defines.** OGC **Sensor Model Language (SensorML)** 3.0 distinguishes a `PhysicalComponent` when a physical process has defined inputs/outputs and **there is no intention to divide its description into component subprocesses** (§ 8.5.2). A `PhysicalSystem` describes hardware **as an aggregate of component processes**, with components and their connections; its constituents may have sensing, actuation or computation roles (§ 8.6.2). SensorML's `AggregateProcess` also permits **physical and non-physical component processes** and explicit **data-flow connections** (§ 8.4.1) (Open Geospatial Consortium 2025b, §§ 8.4–8.6).

**Why it matters to V2.** SensorML establishes a powerful **granularity** distinction: the same general kind of whole sensing equipment can be described without a component process tree or, when useful, decomposed into subprocesses. This is not an assertion that a `PhysicalComponent` has no real physical parts, or that every `PhysicalSystem` subprocess deserves **individual CSAPI System identity**. Process/data-flow relationships also do not prove physical attachment or equipment ownership. V2 should borrow the source-owned distinctions while keeping the later choice of SensorML representation separate from the domain question.

### 3.5 Device parts, modularity and communications are separate models — OPC UA Devices

**What the donor defines.** **Open Platform Communications Unified Architecture (OPC UA)** Part 100 provides a Device Model for equipment **and hardware/software parts**, a separate **Device Communication Model** for network and connection topology, and a **Device Integration Host Model** for host-managed integration. `ComponentType` can represent a Device or its parts, including mechanical or software parts. In a complex Device, a `DeviceSet` can lead to one root Device while nested components are found through hierarchical references. **Modular Devices** support top-Devices and `SubDevices`, including preconfigured or interchangeable module types, and subdevices can themselves be modular (OPC Foundation n.d., §§ 1, 4.1, 4.6, 4.9, 5.1, 9.4).

**Why it matters to V2.** This is strong independent evidence that meaningful device substructure need not be collapsed into one opaque node. Yet **OPC UA component, Device, ObjectType and hierarchical AddressSpace references are OPC-native representation concepts**. Its configurable `SubDevices` organization—even where OPC calls modules “aggregated”—must **not** be equated automatically with CSAPI § 10.2 **Aggregation**. Neither a network connection nor an OPC FunctionalGroup is proof of physical part-of. The donor helps V2 distinguish **device description**, **component structure**, **communication topology**, and **integration host**.

### 3.6 Not every “consists of” means equipment composition — SAREF

**What the donor defines.** The **European Telecommunications Standards Institute (ETSI)** Smart Applications REFerence (**SAREF**) 4.1.1 ontology provides `saref:consistsOf` for composite entities, including the example of a temperature/humidity sensor consisting of temperature and humidity Sensors. But the same predicate is also used for **composite features, properties, states and values** (European Telecommunications Standards Institute 2024, “Composite Features of Interest,” “Composite Properties and Property Values,” and `saref:consistsOf`).

**Why it matters to V2.** This reinforces the need to **interpret the subject and object of a part–whole statement**, not map any use of a common word into equipment composition. For source-equipped component descriptions, `consistsOf` is a useful alignment candidate; it is not a universal physical-assembly or lifetime semantics that automatically matches CSAPI Composition.

### 3.7 Small integrated products falsify mandatory decomposition — Bosch BME280

**What the product actually describes.** The **Bosch Sensortec BME280** is one compact packaged humidity, pressure and temperature sensor. Its manufacturer's block diagram depicts **three sensing elements/front ends**, shared conversion/logic, regulators, memory and one digital interface (§ 3.1). The published datasheet documents supported measurements and settings but does **not** assign an independent product identity or device-management resource to each sensing element (Bosch Sensortec 2024, pp. 2–3, 14).

**Why it matters to V2.** A DIM that forces every physically real sensing element, analog block, or power component into its own independent `System` would impose structure **the source does not supply**. The BME280 does not forbid a future source from modeling its temperature or humidity function separately; it falsifies the **assumption that decomposition must be universal and mandatory**. Contrast the optional detailed complex-device example in the SOSA/SSN draft (§ 8.15).

**Operational scale check:** Our frozen unattended-ground-sensor (UGS) evidence distinguishes attached transducers/detector slots, separate imagers used for cueing, communications relays, and deployment groupings. A detector may merit a separate description; an imager cueing another sensor is not therefore a physical part of the cueing sensor. That is **bounded project source evidence**, recorded in the [Phase A S04 extraction](DRAFT_DIM_Profile_V2_Anatomy_PhaseA_Independent_Extractions_v0.1_26OCT2026.md), **not** a verified universal UGS taxonomy; S04 remains YELLOW.

## 4. What these findings jointly establish

Two **independent modeling questions** now have strong source support:

| Question | Source-grounded distinctions | What is still a V2 inference |
| --- | --- | --- |
| **A. Relationship to the whole:** what kind of association is present? | CSAPI integral Composition versus non-permanent Aggregation; SOSA/SSN `hasSubSystem`, `hosts`, Deployment; OPC UA communication topology; SensorML component/process/data flow | Whether a particular real-world relationship should map to one of those meanings when the source evidence is incomplete |
| **B. Level of separate description:** what needs to be described independently? | CSAPI full System subsystems; SensorML physical component versus decomposed system; OPC UA Device/component/subdevice; SOSA/SSN complex-device Systems; BME280's unseparated internals | A **case-dependent** choice to represent an internal element separately because its identity, configuration, performance, state, output, calibration, replaceability, addressability, or external relationships matter to the intended integration |

**Provisional synthesis, not a normative threshold:** An internal element **may warrant** its own description when the source establishes meaningful information about that element that would be lost or misattributed if only the whole were described. This is **not** equivalent to declaring it a stand-alone CSAPI System. A process step, logical channel, feature, part with a parent-relative identifier, and independently identifiable deployed device can require different representations; they should **not be promoted to the same V2 class by analogy**. Physical existence, a data-flow link, a mount, or a vendor interface label is not independently sufficient evidence of System-level standing.

This is a **decision heuristic to test**, not a universal standard. The native standards already provide the primary semantic concepts needed to discuss it; **Pass 4 identifies no demonstrated gap requiring a newly named V2 class or predicate**.

## 5. Focused examples and mapping risks

A **weather station with permanently integrated sensors** matches CSAPI's example of Composition. A station with **interchangeable measurement payloads** matches its Aggregation/Deployment pattern; both relationships can coexist on one station (Open Geospatial Consortium 2025a, § 10.2). If a particular sensor module carries its own identity, calibration or output source information, independent representation may be valuable—but the evidence must establish those facts before selecting a modeling carrier.

A **vehicle hosting an interchangeable sensor payload** should not have its host, communications network or temporary payload assigned to the Sensor's enduring composition by default. By contrast, a purpose-built integral sensing subsystem within a whole camera/weather station might be part of that whole: **“Platform,” “mount,” and “host” are not magic words determining composition** (Open Geospatial Consortium 2025a, § 10.2; World Wide Web Consortium and Open Geospatial Consortium 2026, §§ 5.3.5.2.2–5.3.5.2.14).

A **physical transducer channel** is not automatically an individually deployed sensing System, just as a **functional process component** is not automatically a separately maintained piece of hardware. The IEEE 1451 transducer-module/channel lineage illustrates this further, but the frozen C03 extraction is **YELLOW** on exact current transducer-data-sheet definitions and conformance. We therefore do not use it to establish new detailed constraints.

## 6. Material questions left open

1. **Independent standing versus component details.** Which identity, calibration, output, serviceability, or configuration distinctions must be preserved as an **independent source-recognized entity**, and which can remain properties, functional subdescriptions, or a parent-scoped element? Pass 4 supports assessing this for each use case; it does not establish one compulsory test or cardinality.
2. **Temporal change in part-of and host relations.** When a part is replaced or temporarily moved, which individual System identities and relationship histories continue? This depends on actual source and deployment semantics and intersects the Pass 1 replacement question.
3. **Model-to-binding mapping.** How should an in-scope source's physical parts, process components, channels, and hosted/interchangeable equipment map to CSAPI `subsystems`, `Deployment`, SensorML component descriptions, or other selected representations? Exact profile constraints belong later and must follow these meanings, not define them.

**Disposition:** **Composition/context distinction strongly supported; variable description granularity supported; independent component standing is conditional and source/use-case dependent.** No universal `Component` class, new part-of relation, mandatory decomposition, UML composition diamond, JSON layout, or profile conformance requirement has been established.

**Next planned increment, when directed:** **Pass 5 — Digital Representation / Proxy Identity.** Stop after Pass 4.

## References — Chicago Manual of Style, 18th ed., author–date

Bosch Sensortec. 2024. *BME280 Data Sheet*. Revision 1.24, February, esp. pp. 2–3, 14. https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf.

European Telecommunications Standards Institute. 2024. *SAREF: Smart Applications REFerence Ontology—Core*. Version 4.1.1. https://saref.etsi.org/core/v4.1.1/.

Open Geospatial Consortium. 2025a. *OGC API—Connected Systems—Part 1: Feature Resources*. OGC 23-001, version 1.0, July 16. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC SensorML Encoding Standard*. OGC 23-000, version 3.0, July 16. https://docs.ogc.org/is/23-000/23-000.html.

OPC Foundation. n.d. *OPC Unified Architecture Part 100: Devices*. Version 1.05.0. https://reference.opcfoundation.org/specs/OPC-10000-100/full.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology—2023 Edition*. Working Draft, October 21, esp. §§ 5.3.5.2 and 8.15. https://www.w3.org/TR/vocab-ssn-2023/.

*Donor-limit note:* The Open Group SOSA and Asset Administration Shell supply additional supportive distinctions in the frozen C15/C01 extractions, but their detailed structures were not re-audited for this narrow pass and have not been silently promoted into independent normative requirements. The UGS and IEEE 1451 references are bounded operational/high-level controls only.
