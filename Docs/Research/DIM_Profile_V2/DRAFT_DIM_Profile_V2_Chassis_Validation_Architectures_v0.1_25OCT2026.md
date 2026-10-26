# DIM/Profile V2 Chassis Validation — Reference Architectures and Architectural Frameworks

**Working draft v0.1 — 25 October 2026**  
**Status:** Second cross-group validation of the CIDM Phase D candidate; no clean-DIM promotion in this artifact.  
**Candidate under test:** a physically realized equipment `System` whose defining domain role is sensing/observing, modeled as the complete operational subject.

## 1. Validation question

Can the candidate remain coherent when tested against architecture-level concerns that information models and ontologies alone do not settle—especially whole-system boundary, physical/functional decomposition, host-platform separation, distributed hardware, modularity, sensor networks, and generic IoT abstractions?

The source-type audit classifies eight artifacts as Reference Architecture / Architectural Framework sources:

1. NATO Core Data Framework (NCDF), ADatP-5653 (Study).
2. The Open Group SOSA Reference Architecture, Edition 1.0 (C212).
3. The Open Group SOSA Reference Architecture, Edition 1.1 (C239).
4. The Open Group SOSA Reference Architecture, Edition 2.0, Snapshot 3 (S251).
5. MIMOSA OSA-CBM.
6. ISO/IEC 29182-1 SNRA Part 1.
7. ISO/IEC 29182-3 SNRA Part 3.
8. W3C Web of Things Architecture 1.1.

The three SOSA Technical Standard editions/snapshots are one architectural lineage and are not counted as three independent conceptual votes.

---

## 2. The Open Group SOSA Reference Architecture lineage

### 2.1 Edition 1.1 (C239) — primary architecture evidence

**Evidence depth:** Full source-native project-provided C239 PDF.

Edition 1.1 gives unusually explicit answers to the chassis questions.

### Whole sensor is the architectural subject

Section 4.1.1.1 states that the **main subject of the document is the SOSA sensor**. The sensor consists of one or more SOSA sensor hardware elements, some of which host software components. The sensor may be Communications, EO/IR, EW, Radar, SIGINT, or a combination of those sensor types, including multi-INT configurations.

An interface crossing the SOSA sensor's boundary is an external interface.

**V2 consequence:** this is direct architecture evidence for treating the whole operational sensor as a bounded subject rather than reducing the model to individual detectors/transducers, observations, or processors.

### One sensor need not be one physical box

Section 4.1.1.2 states that a SOSA sensor consists of one or more hardware elements mounted within or on the same host platform and that the hardware elements may be **grouped together and/or distributed in different locations on/in the host platform**.

**V2 consequence:** the candidate physical realization must not be narrowed to “one Device.” A single sensing System may be a composite equipment realization spanning multiple hardware elements. This favors the broader CSAPI `Equipment` realization facet over adopting `Device` as the universal root.

### Host Platform is external to the sensor boundary

Section 4.1.1.3 defines the SOSA Host Platform as the physical entity to which the SOSA sensor is mounted—for example a vehicle, structure, aircraft, surface craft, building, or pod arrangement. The Host Platform Interface later provides a bridge between the SOSA sensor and the host platform.

**V2 consequence:** host Platform and sensing System must remain distinguishable. Physical mounting, power provision, or communications connection does not make the host intrinsically part of the Sensor.

### Internal realization is heterogeneous

The Edition 1.1 taxonomy says a sensor is comprised of sensor components instantiated in **hardware, firmware, or software**. Architecture components include logical modules and infrastructure; the sensor may incorporate hardware elements, software run-time environments, interaction infrastructure, chassis, apertures, plug-in cards, power supplies, operating systems, hypervisors, containers, transports, APIs, and other supporting elements.

The System Management section treats discovery, capacities, configuration, control, health monitoring/logging, fault handling, BIT, and diagnosis as whole sensor-system and component concerns.

**V2 consequence:** a sensing System remains a Sensor at the whole-subject level even though many of its intrinsic constituents are not themselves sensing elements. This strongly supports the V2 “whole operational subject” objective.

### Multi-role sensing configurations are architecturally normal

SOSA explicitly allows a sensor to combine multiple of its five sensing domains. The architecture also includes tasking, management, communications, processing, and—for EW cases—effects-oriented behavior.

**V2 consequence:** the chassis cannot require that every internal function or every outward interaction be “pure sensing.” Domain membership should rest on the defining/primary role of the whole System, not on every component or action being observational.

### Architecture standing

**Result:** strongly supports and refines the candidate.

---

### 2.2 Edition 1.0 (C212)

Edition 1.0 is the predecessor in the same SOSA Technical Standard lineage. It remains part of the frozen corpus, but its architectural evidence should not be counted as an independent vote from Edition 1.1.

The project has direct source-native DSDM material from Edition 1.0 and the later complete Edition 1.1 Technical Standard. For the chassis decision, Edition 1.1 provides the clearer current adopted architectural boundary.

**Result:** supporting lineage; no independent chassis standing.

---

### 2.3 Edition 2.0, Snapshot 3 (S251)

S251 is a later development snapshot for Edition 2.0, not the adopted Edition 1.1 standard. The prior bounded SOSA assessment treated it separately from C239.

The original S251 bundle is present in project history, but raw-byte retrieval was not available in this validation pass. Therefore no new clause-level S251 claim is introduced here. The chassis validation rests on the fully inspectable C239 architecture, while S251 remains evidence of architectural evolution to revisit only if a candidate decision depends on a changed Edition 2.0 boundary.

**Result:** same lineage; evidence ceiling prevents treating it as an independent architectural basis.

---

## 3. ISO/IEC 29182 Sensor Network Reference Architecture

### 3.1 Part 1 — General overview and requirements

**Evidence depth:** official ISO scope/abstract.

ISO/IEC 29182-1 provides a general overview of the characteristics of a **sensor network**, the organization of entities comprising that network, and general sensor-network requirements.

**V2 consequence:** the architectural subject is larger than the typical individual V2 equipment System. This source validates that a sensor-network aggregate is a legitimate architectural level distinct from the individual sensing System/equipment node.

It therefore argues **against** silently turning V2’s “whole system” into system-of-systems or network scope merely because multiple sensing resources cooperate.

### 3.2 Part 3 — Reference architecture views

**Evidence depth:** official ISO scope/abstract.

ISO/IEC 29182-3 provides business, operational, systems, and technical perspectives, with functional, logical, and/or physical views as applicable. It is explicitly a high-level sensor-network architecture intended for further application-specific development.

Combined with the Part 4 entity-model evidence already reviewed in Phase A, SNRA consistently distinguishes physical and functional views within a network context.

**V2 consequence:** architecture can legitimately describe the same sensing environment through functional and physical viewpoints without requiring those viewpoints to collapse into one class hierarchy. This supports the V2 separation between sensing role and equipment realization.

### Architecture standing

**Result:** supplemental validation. SNRA supports physical/functional separation and establishes the network as a distinct larger boundary; it does not require V2 to adopt Sensor Network as its chassis.

---

## 4. W3C Web of Things Architecture 1.1

**Evidence depth:** full official W3C Recommendation.

WoT defines a **Thing** as an abstraction of a physical or virtual entity whose metadata and interfaces are described by a Thing Description. A virtual entity may itself be a composition of one or more Things. WoT also defines a Thing Model for classes of Things with common capabilities.

Crucially, the architecture explicitly allows domain-specific vocabularies in Thing Descriptions but states that development of particular domain vocabularies is outside the WoT standardization scope; examples include SAREF and SSN.

### V2 consequence

WoT validates several architecture principles but not a chassis noun:

- A generic interaction architecture can remain separate from domain semantics.
- A digital/network-facing description is not identical to the physical entity it describes.
- Composite/virtual representations do not prove that the represented subject is one physical device.
- Generic **Thing** is intentionally too broad to establish V2 membership.
- Domain-specific semantics such as Sensor/Equipment appropriately come from other sources rather than from the generic web architecture.

**Result:** supportive but intentionally domain-neutral; **Thing** is too broad to replace the candidate chassis.

---

## 5. MIMOSA OSA-CBM

**Evidence depth:** official MIMOSA architecture description.

MIMOSA describes OSA-CBM as a standard architecture for moving information in a condition-based maintenance system. It defines six functional blocks and the interfaces/inputs/outputs between them so disparate hardware and software components can interoperate in a CBM system.

### V2 consequence

OSA-CBM is a **functional maintenance/condition-monitoring architecture**, not a classification of the managed equipment itself. It is useful evidence that sensing/acquisition, processing, assessment, diagnostics/prognostics, and decision-support functions can be separated into interoperable architectural blocks around an asset/equipment subject.

It does not challenge the candidate chassis and should not be promoted into a Sensor/Equipment root concept.

**Result:** specialized architectural slice; useful later for lifecycle/condition modules, not chassis-defining.

---

## 6. NATO Core Data Framework (NCDF)

**Evidence depth:** NISP identity/status plus FMN Spiral 5 standards-profile description.

ADatP-5653 is listed as NATO Core Data Framework (NCDF). The publicly available FMN standards-profile description characterizes it as a framework for common NATO metadata elements, XML schema definitions, association/binding of metadata to information objects, and interoperable information sharing.

### V2 consequence

Despite its source-type placement in the frozen audit, the available evidence shows that NCDF is **metadata/information-governance architecture**, not a physical sensor-system architecture. It therefore cannot answer the V2 chassis question.

This is a useful correction to source-type expectations: source-type grouping identifies what deserves review, but a group label does not force every artifact to contribute to the chassis.

**Result:** cross-cutting / non-applicable to chassis.

---

# 7. Cross-architecture comparison

| Architecture | Primary architectural boundary | Physical/functional separation | Composite/distributed support | Host/environment distinction | Effect on V2 candidate |
|---|---|---|---|---|---|
| SOSA Edition 1.1 | Whole SOSA Sensor | Strong | **Yes — one or more hardware elements; may be distributed on/in host platform** | **Explicit Sensor vs Host Platform** | **Strongly validates and refines** |
| SOSA Ed. 1.0 / Ed. 2 Snapshot 3 | Same evolving architecture lineage | Same lineage | Same lineage | Same lineage | Supporting lineage, not independent votes |
| SNRA Part 1 | Sensor Network | Yes across series | Network is inherently multi-entity | Network context larger than node/device | Validates larger aggregate as separate level |
| SNRA Part 3 | Sensor Network views | **Explicit functional/logical/physical viewpoints** | Architecture-level | Yes through multi-view structure | Supports role/realization separation |
| WoT Architecture | Thing abstraction | Physical **or virtual** | Yes, including virtual composition | Generic/network-facing abstraction | Too broad; supports domain-semantics separation |
| OSA-CBM | CBM functional system | Strong functional-block decomposition | Integrates disparate HW/SW | Equipment is subject/context of CBM functions | Specialized lifecycle slice |
| NCDF | Metadata framework | Not chassis-relevant | Not chassis-relevant | Not chassis-relevant | Cross-cutting / non-applicable |

---

# 8. Architecture-level answers to the open chassis questions

## 8.1 Must one V2 System be one physical device?

**No.**

SOSA explicitly allows one Sensor to consist of multiple hardware elements and allows those elements to be physically distributed in different locations on/in the same Host Platform.

### Refinement

The V2 realization facet should remain **Equipment**, not be narrowed to “Device.” A physical sensing System can be a composite equipment realization.

---

## 8.2 Is a host Platform part of the sensing System merely because it carries or powers it?

**No.**

SOSA explicitly defines the Host Platform as the physical entity to which the Sensor is mounted and provides an interface across that boundary.

### Refinement

Platform/host should remain external context unless source evidence for a particular System establishes that the platform itself is an enduring constituent of the sensing System rather than merely its host.

---

## 8.3 Does a network of sensors become one V2 System automatically?

**No.**

SNRA treats the **sensor network** as an architectural subject in its own right. This provides evidence that a network/aggregate is a distinct level of organization rather than merely a large Sensor.

### Refinement

Multiple cooperating sensing Systems should remain an aggregation/network unless there is independent evidence of one enduring operational System identity and composition boundary.

---

## 8.4 Can one Sensor contain non-sensing components?

**Yes.**

SOSA's whole Sensor contains hardware, firmware, software, run-time, interaction, management, power, and other supporting components. OSA-CBM and WoT likewise demonstrate functional heterogeneity around a managed/interactive subject.

### Refinement

Internal components need not individually qualify as Sensors. The chassis classification applies to the whole System.

---

## 8.5 Can the whole System be multi-INT or multifunctional?

**Yes, within the evidence reviewed.**

SOSA expressly permits combinations of its sensor types and supports sensor management, processing, communications, and effects-related domains around the Sensor.

### Refinement

The chassis should use the **defining/primary operational role** of the whole System, not demand sensing exclusivity.

---

# 9. Architecture-level synthesis

The candidate survives architecture validation and becomes materially stronger.

The architecture evidence supports this refined boundary:

> **The V2 domain concerns physically realized equipment Systems whose defining operational role is sensing/observing. A System may be realized by one or multiple hardware elements and may contain heterogeneous hardware, firmware, software, communications, power, processing, management, and other supporting components. Hosting Platform, deployment environment, and cooperating peer Systems remain external context unless an enduring composition relationship makes them intrinsic to the System.**

This remains a **boundary statement**, not a new class.

The architecture group also explains why `Equipment` is preferable to replacing it with `Device`: the target subject may be a distributed or composite physical realization rather than one device-shaped box.

---

# 10. Validation standing after architecture group

| Question | Architecture result |
|---|---|
| Is a new umbrella chassis term required? | **No** |
| Does one Sensor have to be one hardware device? | **No** |
| Can the Sensor contain heterogeneous non-sensing components? | **Yes** |
| Can one Sensor contain multiple/distributed hardware elements? | **Yes; SOSA provides direct precedent** |
| Is Host Platform automatically part of the Sensor? | **No; SOSA separates it explicitly** |
| Is Sensor Network automatically the same boundary as one Sensor/System? | **No; SNRA treats network as a larger architectural subject** |
| Is generic WoT Thing a better chassis? | **No; intentionally physical-or-virtual and domain-neutral** |
| Does `Equipment` remain a better realization facet than narrowing to `Device`? | **Yes** |
| Does the candidate survive architecture validation? | **Yes, with stronger composite-equipment and host-boundary semantics** |
| Clean V2 DIM promotion | **Still blocked pending Requirements / Capability / Operational Specification validation** |

# 11. Immediate next step

Proceed to the Requirements / Capability / Operational Specification source group and try to falsify the refined boundary against concrete operational expectations, multifunction systems, management/state requirements, and real system-family constraints.
