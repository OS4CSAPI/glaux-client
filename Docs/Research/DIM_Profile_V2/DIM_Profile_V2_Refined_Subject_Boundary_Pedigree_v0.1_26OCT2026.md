# Domain Information Model (DIM)/Profile Version 2 (V2) — Pedigree and Provenance of the Refined Subject-and-Boundary Hypothesis

**Version:** 0.1  
**Date:** 26 October 2026  
**Standing:** Empirical pedigree/provenance research paper; not a final scope definition, class definition, module architecture, or application-profile binding  
**Controlling continuity:** `PITON_DIM_Profile_V2_Continuity_v1.3_26OCT2026.md`  
**Immediate predecessor:** `DIM_Profile_V2_Emerging_Subject_Boundary_Pedigree_v0.2_26OCT2026.md`  
**Stress-test basis:** `DIM_Profile_V2_Subject_and_Boundary_Pass2_Stress_Test_v0.1_26OCT2026.md`  
**Excluded from evidentiary input:** quarantined Phase B/C/D artifacts and their promoted anatomy decisions

## Abstract

The first post-audit pedigree paper traced the donor origins of an emerging description of the subject of the V2 Domain Information Model. Subject-and-Boundary Pass 2 then stress-tested that description against mixed sensing/actuation systems, broader device and Web-of-Things models, host/platform ambiguity, atomic and composite equipment, digital representations, and the Sensing for Asset Protection with Integrated Electronic Networked Technology (SAPIENT) system-of-systems/fusion boundary. The result was a refined hypothesis:

> **The DIM appears to be converging on an individually identifiable, persistently describable, equipment-realized System whose defining operational orientation is sensing/observing, but which may contain or perform non-sensing functions. The subject may be atomic or composite; its enduring composition can be distinguished from hosting, deployment, network, management, target, and digital-representation context; and its kind/model, capabilities, configuration, state, interactions, outputs/actions, history, and provenance can be represented without conflating those concerns with the subject itself.**

This paper traces the empirical pedigree of that refined statement. It decomposes the statement into semantic “bricks,” identifies the donor-native concepts that supply or corroborate each brick, distinguishes direct source contribution from project synthesis, and records the limits of each inference. The purpose is to make the intellectual provenance of the hypothesis inspectable: every major proposition should be traceable to what one or more donors actually model, while the parts authored by V2 synthesis remain explicitly identified as such.

---

## 1. Research question and method

The research question is:

> **What donor-native evidence justifies each semantic proposition in the refined V2 subject-and-boundary hypothesis, and what part of the proposition remains V2 synthesis rather than donor-owned semantics?**

This paper uses four pedigree categories.

### 1.1 Native anchor contribution

A donor belongs to the standards environment in which the intended Open Geospatial Consortium (OGC) Application Programming Interface (API) – Connected Systems (CSAPI) profile will operate, or supplies conceptual semantics explicitly used by that environment. The principal anchor sources are CSAPI, Sensor Model Language (SensorML), the World Wide Web Consortium (W3C)/OGC Sensor, Observation, Sample, and Actuator (SOSA) / Semantic Sensor Network (SSN) ontology, and Observations, Measurements, and Samples (OMS).

### 1.2 Independent corroboration

A donor from a materially different standards community independently preserves a similar distinction. Examples include the Asset Administration Shell (AAS), Open Platform Communications Unified Architecture (OPC UA) Devices, the European Telecommunications Standards Institute (ETSI) Smart Applications REFerence (SAREF) ontology, W3C Web of Things (WoT), Redfish, the Integrated Sensor Architecture (ISA), and The Open Group Sensor Open Systems Architecture (SOSA).

Because “SOSA” is used by two unrelated donor traditions, this paper uses **W3C/OGC SOSA** for Sensor, Observation, Sample, and Actuator and **Open Group SOSA** for Sensor Open Systems Architecture.

### 1.3 Operational or scale falsification

A product, manual, reference implementation, or fielded-system source tests whether an abstraction remains sensible in real equipment. The Bosch BME280 and unattended ground sensor (UGS) evidence are principal examples.

### 1.4 Boundary challenge

A donor deliberately extends beyond the emerging V2 boundary and is therefore useful as a counterexample. Institute of Electrical and Electronics Engineers (IEEE) 1451, SAPIENT, OPC UA Devices, AAS, and WoT all play this role in addition to contributing reusable semantics.

A donor is not counted as an independent “vote” merely because multiple companion publications exist. Common inheritance, normative dependency, and family lineage are preserved.

---

## 2. Refined hypothesis with inline pedigree

> **The DIM appears to be converging on an individually identifiable, persistently describable, equipment-realized System** (Open Geospatial Consortium 2025a; World Wide Web Consortium and Open Geospatial Consortium 2026; European Telecommunications Standards Institute 2024; OPC Foundation n.d.) **whose defining operational orientation is sensing/observing, but which may contain or perform non-sensing functions** (Open Geospatial Consortium 2025a, 2025b; World Wide Web Consortium and Open Geospatial Consortium 2026; The Open Group 2023). **The subject may be atomic or composite** (Open Geospatial Consortium 2025b; OPC Foundation n.d.; Bosch Sensortec 2024); **its enduring composition can be distinguished from hosting, deployment, network, management, target, and digital-representation context** (Open Geospatial Consortium 2025a; World Wide Web Consortium and Open Geospatial Consortium 2026; Open Geospatial Consortium and International Organization for Standardization 2023; OPC Foundation n.d.; World Wide Web Consortium 2023a, 2023b); **and its kind/model, capabilities, configuration, state, interactions, outputs/actions, history, and provenance can be represented without conflating those concerns with the subject itself** (Industrial Digital Twin Association 2026; Open Geospatial Consortium 2025a, 2025b; European Telecommunications Standards Institute 2024; World Wide Web Consortium 2013, 2023b).

No source states this paragraph as a whole. The statement is a **V2 synthesis** built from donor-native distinctions. The sections below establish the pedigree of its constituent bricks.

---

## 3. Brick map and evidentiary strength

| Brick | Strongest direct donor(s) | Independent corroboration / challenge | Pedigree strength | V2 synthesis |
| --- | --- | --- | --- | --- |
| individually identifiable | CSAPI | AAS, SAREF, Redfish, Open Standard for Unattended Sensors (OSUS) | **Strong** | subject identity survives representation changes |
| persistently describable | CSAPI | AAS, WoT | **Strong synthesis** | stable referent with changing information |
| equipment-realized System | CSAPI | W3C/OGC SOSA/SSN, OPC UA, SAREF | **Strong** | present realization boundary is equipment |
| defining sensing/observing orientation | CSAPI | W3C/OGC SOSA/SSN, SensorML, Open Group SOSA | **Strong** | sensing defines the whole subject, not every internal function |
| may contain/perform non-sensing functions | SensorML | Open Group SOSA, CSAPI; IEEE 1451/SAPIENT challenge | **Strong with boundary qualification** | mixed function does not defeat sensing identity |
| atomic or composite | SensorML | OPC UA, SAREF, BME280, radiation/UGS | **Strong** | one model must scale without forced decomposition |
| enduring composition | CSAPI | W3C/OGC SOSA/SSN, OPC UA, AAS | **Very strong** | intrinsic part-of is not generic association |
| hosting context | W3C/OGC SOSA/SSN | Open Group SOSA, CSAPI | **Strong** | host relation is distinct from composition |
| deployment context | CSAPI; W3C/OGC SOSA/SSN; OMS | UGS | **Strong** | employment context is not intrinsic composition |
| network context | ISA; OPC UA | Internet Engineering Task Force (IETF), UGS | **Strong** | communications topology is not equipment topology |
| management context | Redfish; Lightweight Machine to Machine (LwM2M) | ISA, OSUS | **Strong** | manager/controller relation is external unless composition says otherwise |
| target context | W3C/OGC SOSA/SSN; OMS | CSAPI, SAREF | **Strong** | observed/controlled target is not the sensing subject |
| digital-representation context | AAS; WoT | CSAPI, OPC UA, OSUS | **Very strong** | representation/proxy/twin identity does not replace equipment identity |
| kind/model | CSAPI; SAREF | AAS, WoT, Matter | **Very strong** | instance ≠ model/kind ≠ Procedure/Method |
| capabilities | AAS; SensorML | SAREF, ISA, SAPIENT | **Strong but semantically overloaded** | ability/potential must remain distinct from config/state/execution |
| configuration | SensorML; ISA | UGS, BME280 | **Strong** | supported, intended, requested, and applied settings may differ |
| state | Redfish | ISA, UGS, BME280, Open Group SOSA | **Strong** | current state is not capability/configuration/history |
| interactions | WoT | SAREF, LwM2M, CSAPI | **Strong** | ways of interacting are related to, not identical with, the subject |
| outputs/actions | CSAPI | SensorML, OSUS, SAPIENT, UGS | **Very strong** | output and tasking/execution are distinct runtime semantics |
| history | CSAPI | Redfish, Machinery Information Management Open Systems Alliance (MIMOSA), UGS | **Strong** | current description/state is not history |
| provenance | W3C Provenance (PROV) | UGS, OMS, CSAPI/AAS references | **Strong cross-cutting** | source/derivation/responsibility should survive integration |
| non-conflation rule | induced across donors | all above | **V2 synthesis** | preserve explicit relationships among distinct concerns |

---

# 4. Brick 1 — “Individually identifiable”

## 4.1 Donor-native evidence

### CSAPI — direct native anchor

CSAPI requires every System resource to carry a `uniqueIdentifier` that is persistent and independent of the System resource's URL. The standard explains that the same real-world object may be described by different services and uses the persistent unique identifier to preserve identity across those representations (Open Geospatial Consortium 2025a, secs. 8.5, 9.2.2).

The donor-native distinction is:

> **real-world System identity ≠ one API resource identity**

### AAS — independent corroboration

AAS separates the represented Asset from its Asset Administration Shell. AssetInformation identifies the represented Asset, while the shell is the digital representation through which information about that Asset is organized (Industrial Digital Twin Association 2026).

### SAREF — independent corroboration

SAREF distinguishes an individual `Device` from `DeviceKind`, its archetypal/model-level description (European Telecommunications Standards Institute 2024).

## 4.2 V2 inference

The DIM must have a concept of **individual subject identity that does not depend on a particular API resource, digital shell, model description, or message**.

## 4.3 Guardrail

This does not mean V2 must standardize one universal identifier syntax or reuse CSAPI's `uniqueIdentifier` as a conceptual-model property. Identifier mechanics belong to later profile/binding decisions.

---

# 5. Brick 2 — “Persistently describable”

## 5.1 Donor-native evidence

“Persistently describable” is V2 language, but its ingredients are donor-native.

CSAPI gives the System a persistent identifier while its description can have a validity interval and while Deployments, Observations, Commands, SystemEvents, and current location can change (Open Geospatial Consortium 2025a).

WoT distinguishes a Thing from a Thing Description; the Thing Description can even be hosted separately from the Thing (World Wide Web Consortium 2023b).

AAS distinguishes the Asset from its shell and from multiple Submodels that describe different aspects of it (Industrial Digital Twin Association 2026).

## 5.2 V2 inference

The subject should remain a stable referent while **descriptions, state, configuration, deployment, outputs, actions, and representations change over time**.

## 5.3 Guardrail

The phrase does not assert one universal temporal persistence mechanism. It expresses the semantic continuity of the subject.

---

# 6. Brick 3 — “Equipment-realized System”

This is one of the most important refinements from Pass 1.

## 6.1 CSAPI — direct source of the two-facet characterization

CSAPI requires a `systemType` and optionally supplies an independent `assetType`. The standard's examples explicitly include digital temperature probes, Global Positioning System receivers, and video cameras as `Sensor + Equipment`, while also permitting `Sensor + Simulation`, `Sensor + Human`, `Actuator + Equipment`, and `Platform + Equipment` (Open Geospatial Consortium 2025a, sec. 9.2.2).

Thus:

- **System** identifies the represented System resource/conceptual subject;
- **Sensor** expresses its principal role/activity;
- **Equipment** expresses the asset realization.

These are not three peer nouns and are not a compound class.

## 6.2 W3C/OGC SOSA/SSN — semantic corroboration

The 2023 Edition defines a `System` as an instrument or equipment, including software systems and agents where relevant, that implements a Procedure in the context of Executions. It separately defines Platform and Deployment and permits Systems to contain subsystems (World Wide Web Consortium and Open Geospatial Consortium 2026).

## 6.3 OPC UA and SAREF — independent equipment/device corroboration

OPC UA defines a Device as an independent physical entity capable of performing one or more functions and delimited by its interfaces; Devices can provide sensing, actuating, communication, or control functionality and can themselves contain other Devices/components/parts (OPC Foundation n.d.).

SAREF defines Device as a tangible real-world entity designed to accomplish tasks by performing functions (European Telecommunications Standards Institute 2024).

## 6.4 V2 inference

The present V2 target is **a System with an equipment/hardware realization**, not every possible System realization that the broader anchor ontologies can represent.

## 6.5 Guardrail

Equipment realization is a **current boundary supported by evidence**, not an invented universal definition of System. Human, Simulation, Process, Group, and other realizations remain possible future profiles or out-of-scope cases.

---

# 7. Brick 4 — “Whose defining operational orientation is sensing/observing”

## 7.1 CSAPI — strongest direct source

CSAPI defines `systemType = Sensor` for a System whose **primary activity is sensing or observing** (Open Geospatial Consortium 2025a, sec. 9.2.2).

The word **primary** is decisive. The classification is about the defining activity of the whole subject, not a claim that every internal component performs sensing.

## 7.2 W3C/OGC SOSA/SSN — semantic meaning of Sensor

The ontology defines Sensor within the general System/Execution pattern and associates it with observing/Observations (World Wide Web Consortium and Open Geospatial Consortium 2026).

## 7.3 SensorML — whole-system sensing

SensorML states that a sensor system's overall application can be sensing even when the system contains sensing, actuation, and computational components (Open Geospatial Consortium 2025b, sec. 8.6).

## 7.4 Open Group SOSA — independent sensing-domain corroboration

Open Group SOSA treats the Sensor as a bounded architectural subject while allowing substantial internal hardware, software, processing, power, communications, system-management, and support infrastructure (The Open Group 2023).

## 7.5 V2 inference

“Sensing/observing” presently describes the **defining operational orientation of the top-level subject**.

## 7.6 Guardrail

The statement does not yet claim that every possible future V2 subject must be a Sensor. It defines the current bounded problem based on the evidence available.

---

# 8. Brick 5 — “But which may contain or perform non-sensing functions”

This brick is the central refinement produced by the stress test.

## 8.1 SensorML — direct evidence

SensorML explicitly states that a sensor system whose overall application is sensing can contain sensing components, actuators/robotic subsystems, and computational components (Open Geospatial Consortium 2025b, sec. 8.6).

This establishes a clean distinction:

> **whole-system orientation ≠ every component's function**

## 8.2 CSAPI — commandability does not redefine System type

CSAPI's classification is semantic rather than an API-functionality restriction. Systems of different types can expose dynamic data and command structures; therefore the presence of commands or effecting behavior does not automatically reclassify a Sensor as an Actuator (Open Geospatial Consortium 2025a).

## 8.3 Open Group SOSA — independent corroboration

Open Group SOSA places heterogeneous support and mission functions inside a bounded Sensor, including processing, networking, management, power, and other supporting functions (The Open Group 2023).

## 8.4 IEEE 1451 and SAPIENT — boundary challengers

IEEE 1451 deliberately standardizes smart transducers that can be sensors and/or actuators (IEEE 2024; National Institute of Standards and Technology [NIST] 2024).

SAPIENT supports sensors **and effectors**, and its fusion node coordinates both (Defence Science and Technology Laboratory 2026).

These sources do not disprove the V2 hypothesis. They identify the boundary condition: **pure effectors exist and are not automatically in scope merely because a donor also covers them**.

## 8.5 V2 inference

An in-scope sensing subject may contain or perform **actuation, computation, communication, management, power, or other non-sensing functions** without losing its sensing-oriented identity.

## 8.6 Guardrail

A pure actuator/effector whose defining orientation is not sensing remains outside the present boundary unless explicitly brought into scope later.

---

# 9. Brick 6 — “The subject may be atomic or composite”

## 9.1 SensorML — direct conceptual source

SensorML distinguishes:

- `PhysicalComponent`: a physical processing device for which the description is not intended to be further decomposed into component subprocesses; and
- `PhysicalSystem`: an aggregate hardware device modeled as one or more components (Open Geospatial Consortium 2025b, secs. 8.5–8.6).

The distinction is about **meaningful modeling granularity**, not whether microscopic parts physically exist.

## 9.2 OPC UA — recursive composition

OPC UA explicitly allows a Device to be a system/topology of other Devices, components, or parts (OPC Foundation n.d.).

## 9.3 BME280 — negative control

The Bosch BME280 contains multiple sensing elements, electronics, memory, conversion logic, power functions, and digital interfaces, but those internals are not separately managed equipment subjects in the product model (Bosch Sensortec 2024).

## 9.4 UGS and radiation systems — positive composite controls

UGS products and radiation instruments demonstrate the other end of the scale, where detectors/channels/cameras or other internal elements can have operationally meaningful identity, configuration, outputs, calibration, or service relationships.

## 9.5 V2 inference

The common DIM must scale from **atomic equipment** to **meaningfully decomposed systems** without forcing one granularity onto all equipment.

## 9.6 Guardrail

“Composite” does not mean “represent every physical part.”

---

# 10. Brick 7 — “Its enduring composition”

## 10.1 CSAPI — strongest direct source

CSAPI explicitly distinguishes Composition from Aggregation.

Composition means a subsystem is an integral part of the parent and is not normally taken apart during the parent's lifetime except for maintenance. Aggregation means the subsystem is non-permanent/interchangeable and is represented through Deployment (Open Geospatial Consortium 2025a, sec. 10.2).

The standard gives concrete examples:

- built-in weather-station sensors → Composition;
- interchangeable weather-station sensors → Aggregation;
- a vehicle with built-in flight equipment plus interchangeable payloads → both.

## 10.2 W3C/OGC SOSA/SSN — independent semantic partitioning

SOSA/SSN separately represents subsystem relations, hosting, and Deployment (World Wide Web Consortium and Open Geospatial Consortium 2026).

## 10.3 OPC UA and AAS — independent composition structures

OPC UA provides Device/subdevice/component structures, while AAS provides part/hierarchy relationships and multiple engineering views of asset structure.

## 10.4 V2 inference

The DIM needs an **enduring part-of/composition concept** that is not used as a generic relationship for every association.

## 10.5 Guardrail

The final V2 relation need not be named “Composition,” and it must not mechanically copy CSAPI endpoint nesting or Unified Modeling Language diamond semantics.

---

# 11. Brick 8 — “Distinguished from hosting context”

## 11.1 W3C/OGC SOSA/SSN — direct semantic source

SOSA/SSN defines Platform hosting separately from subsystem composition. A Platform can host Systems/Assets in a Deployment (World Wide Web Consortium and Open Geospatial Consortium 2026).

## 11.2 Open Group SOSA — strong independent corroboration

Open Group SOSA places the Host Platform outside the Sensor boundary and defines interfaces across that boundary (The Open Group 2023).

## 11.3 Pass 2 refinement

The correct rule is not “a host is always external.” A housing, mast, chassis, vehicle, or platform-like structure can be intrinsic if source semantics establish it as enduring composition.

## 11.4 V2 inference

V2 needs to preserve the semantic difference between:

> **part of the enduring subject** and **hosts/carries the subject**

## 11.5 Guardrail

Classification must follow relationship meaning, not the noun used by one donor.

---

# 12. Brick 9 — “Distinguished from deployment context”

## 12.1 CSAPI

Deployment is a first-class contextual resource and is the mechanism used to represent Aggregation/non-permanent mounting (Open Geospatial Consortium 2025a).

## 12.2 W3C/OGC SOSA/SSN

Deployment is an arrangement of Assets, typically Systems and Platforms, for executing Procedures with respect to designated Features of Interest during a specified interval (World Wide Web Consortium and Open Geospatial Consortium 2026).

## 12.3 OMS

OMS likewise separates Observer, Host, Deployment, Procedure, Feature of Interest, and Observation roles (Open Geospatial Consortium and International Organization for Standardization 2023).

## 12.4 UGS operational evidence

UGS manuals distinguish persistent device identity from emplacement/location, implant/removal planning, and other operational deployment context.

## 12.5 V2 inference

Where/how/when the equipment is employed is important information **about** the subject but is not automatically intrinsic equipment composition.

---

# 13. Brick 10 — “Distinguished from network context”

## 13.1 ISA

ISA distinguishes Composition topology from broader network participation and mediated visibility.

## 13.2 OPC UA

OPC UA deliberately layers a Device Communication Model on top of the base Device Model, adding Networks and ConnectionPoints to construct communications topology (OPC Foundation n.d.).

## 13.3 IETF interface/topology standards

Internet Engineering Task Force interface and topology models distinguish interface identity, layering, network nodes, termination points, and links from physical equipment composition.

## 13.4 V2 inference

> **network-connected-to ≠ part-of**

Communications interfaces and topology may be essential to understanding the subject, but they must not silently become its physical/equipment composition tree.

---

# 14. Brick 11 — “Distinguished from management context”

## 14.1 Redfish

Redfish distinguishes managed equipment resources from `Manager` resources and explicit management relationships such as `ManagedBy`.

## 14.2 LwM2M

LwM2M separates the managed Client/device-side resource model from the LwM2M Server and Bootstrap Server.

## 14.3 ISA and OSUS

ISA Controller roles and Open Standard for Unattended Sensors (OSUS) proxy/adapter structures independently show that the entity or software that manages, mediates, or exposes equipment need not be the equipment itself.

## 14.4 V2 inference

> **managed-by / controlled-by / mediated-by ≠ part-of by default**

---

# 15. Brick 12 — “Distinguished from target context”

## 15.1 W3C/OGC SOSA/SSN

SOSA/SSN explicitly distinguishes a Sensor/System from the Feature of Interest and Property involved in an Observation (World Wide Web Consortium and Open Geospatial Consortium 2026).

## 15.2 OMS

OMS independently preserves Observer, Feature of Interest, observable Property, Procedure, and Result as different conceptual roles (Open Geospatial Consortium and International Organization for Standardization 2023).

## 15.3 CSAPI and SAREF

CSAPI separates Sampling Features and Features of Interest from Systems, while SAREF separates Devices from Features of Interest and target Properties/States.

## 15.4 V2 inference

> **the thing being sensed, observed, sampled, detected, or controlled is not the sensing subject itself**

---

# 16. Brick 13 — “Distinguished from digital-representation context”

This is the other major refinement from Pass 2.

## 16.1 AAS — Asset versus digital shell

AAS explicitly distinguishes the represented Asset from the Asset Administration Shell and the Submodels that provide digital information about it (Industrial Digital Twin Association 2026).

## 16.2 WoT — Thing versus Thing Description, Thing Model, and Virtual Thing

WoT distinguishes:

- Thing — physical or virtual entity abstraction;
- Thing Description — machine-readable description of one Thing's metadata and interfaces;
- Thing Model — model/class-level description without instance-specific information;
- Virtual Thing — a Service that can represent, augment, improve the interface to, or stand in place of one or more Things; Shadows and Digital Twins are examples (World Wide Web Consortium 2023a, 2023b).

A Thing Description can be hosted externally rather than on the represented Thing itself.

## 16.3 CSAPI — subject identifier versus API address

CSAPI's persistent System identifier is distinct from the API resource URL (Open Geospatial Consortium 2025a).

## 16.4 OPC UA and OSUS — representation/mediation corroboration

OPC UA separates Device semantics from server/AddressSpace and Device Integration Host concerns. OSUS separates its consumer-facing Asset abstraction from source-specific AssetProxy/adapter behavior.

## 16.5 V2 inference

Digital representation/proxy/twin/service identity may be important enough to model as a relationship, but:

> **representation identity ≠ equipment-subject identity**

## 16.6 Guardrail

This does not mean the DIM must become a digital-twin ontology. Concrete API, proxy, AddressSpace, serialization, and service mechanics remain profile/binding/implementation concerns.

---

# 17. Brick 14 — “Kind/model”

## 17.1 CSAPI — systemKind versus implemented Procedures

CSAPI's `systemKind` relationship points from a System instance to one reusable Procedure resource describing the kind of System, such as a model/datasheet. The System separately links to Procedures it implements.

The C08 validation audit identified the importance of not collapsing these relationships.

## 17.2 SAREF

SAREF separates `Device` from `DeviceKind`.

## 17.3 AAS

AAS distinguishes type assets from instance assets and supports template-versus-instance information structures.

## 17.4 WoT

Thing Model captures class/model-level interactions without instance-specific protocol address, serial number, or location; Thing Description represents a particular Thing (World Wide Web Consortium 2023b).

## 17.5 V2 inference

The evidence strongly supports:

> **individual subject ≠ product/model/kind ≠ Procedure/Method**

This distinction should be settled before downstream concept modeling.

---

# 18. Brick 15 — “Capabilities”

## 18.1 AAS

AAS distinguishes `Capability` from `Operation` and from skills/implementation. Capability describes what an Asset can potentially achieve; constraints and properties qualify it.

## 18.2 SensorML

SensorML contains capabilities/characteristics separately from inputs, outputs, parameters, methods, modes, and settings.

## 18.3 SAREF

SAREF uses Function/FunctionOfInterest and Command structures rather than an AAS-style Capability object.

## 18.4 ISA and SAPIENT

ISA and SAPIENT separately expose declared/supported capability, mode/performance, current state, and tasking.

## 18.5 V2 inference

The donors do **not** prove one universal Capability class.

They do strongly support the distinction:

> **what a subject can do ≠ what it is configured to do ≠ what it is currently doing ≠ one action/request**

---

# 19. Brick 16 — “Configuration”

## 19.1 SensorML

SensorML supports configurable processes, modes, settings, parameters, and allowed values/constraints.

## 19.2 ISA

ISA separates component configuration from capability declarations, status/state, and runtime requests.

## 19.3 UGS operational evidence

TRSS and OmniSense distinguish stored/editor configuration, requested or queued changes, and later device-returned/reported state.

## 19.4 BME280

Even a small atomic sensor separates supported behavior/performance from selected mode, oversampling, filter/standby settings, runtime status, and measured outputs (Bosch Sensortec 2024).

## 19.5 V2 inference

V2 should preserve, where applicable:

- supported/configurable space;
- selected/intended configuration;
- requested/queued changes;
- effective/applied/reported configuration.

The exact canonical configuration model remains to be consolidated.

---

# 20. Brick 17 — “State”

## 20.1 Redfish

Redfish provides distinct Status, State, Health, Condition, and resource-specific state structures.

## 20.2 ISA, UGS, and Open Group SOSA

These donors expose operating state, readiness, health/fault, mode, communications status, battery/power state, and other state dimensions without collapsing them into one value.

## 20.3 BME280

The BME280 distinguishes operating mode, selected configuration, runtime status bits, and measurement outputs.

## 20.4 V2 inference

The evidence supports:

> **capability ≠ configuration ≠ current reported state ≠ historical event**

It does not support inventing one universal status/health/readiness enumeration for all equipment families.

---

# 21. Brick 18 — “Interactions”

## 21.1 WoT — direct interaction-model donor

WoT Thing Description defines Properties, Actions, and Events as Interaction Affordances for interaction with a Thing (World Wide Web Consortium 2023b).

## 21.2 SAREF

SAREF separates Device, Service, Operation, Function, Command, Property/State, and Execution concepts.

## 21.3 LwM2M

LwM2M supplies device-management operations and observation/reporting mechanisms while separating them from underlying device identity.

## 21.4 V2 inference

The DIM may need to describe **how the subject can be interacted with** while keeping interface/service mechanics distinct from the subject itself.

---

# 22. Brick 19 — “Outputs/actions”

## 22.1 CSAPI — strongest native anchor

CSAPI Part 2 separates:

- DataStream from individual Observation;
- ControlStream from individual Command;
- Command from CommandStatus and CommandResult;
- Feasibility from actual Command execution;
- SystemEvent from Observation data.

This is a particularly strong contribution because it separates output/channel semantics, tasking semantics, execution state, and result semantics.

## 22.2 SensorML

SensorML models inputs, outputs, parameters, ProcessMethod, and explicit process connections.

## 22.3 OSUS, SAPIENT, and UGS

These operational donors demonstrate equipment that both produces detections/status/media and accepts commands/tasking/configuration actions.

## 22.4 V2 inference

The subject's produced information and requested/executed actions must remain distinguishable from:

- capability declarations;
- interface definitions;
- configuration;
- current state.

---

# 23. Brick 20 — “History”

## 23.1 CSAPI — direct native anchor

CSAPI `SystemEvent` provides explicit time-stamped event/history structure for calibration, configuration changes, software updates, part replacement, relocation/deployment, handoff, and related system events.

## 23.2 Redfish, Machinery Information Management Open Systems Alliance (MIMOSA), and UGS

These sources independently expose event/log/service/maintenance/configuration-history concerns.

## 23.3 V2 inference

> **current description/state ≠ history of what happened to the subject**

Whether V2 eventually uses one common event pattern, specialized histories, or a combination remains a later concept-design question.

---

# 24. Brick 21 — “Provenance”

## 24.1 W3C Provenance (PROV) — direct cross-cutting donor

The W3C PROV Data Model (PROV-DM) supplies domain-independent concepts for Entity, Activity, Agent, generation, usage, derivation, attribution, association, and responsibility (World Wide Web Consortium 2013).

PROV is deliberately not an equipment anatomy model. Its role is cross-cutting information provenance.

## 24.2 UGS — operational need for source/authority

UGS evidence distinguishes database/editor values, requested/queued values, device-reported values, entered location versus device Global Positioning System (GPS) location, and cases where detecting and imaging devices differ.

This demonstrates that source/authority is not one coarse metadata field.

## 24.3 OMS, CSAPI, and AAS — corroboration

OMS preserves observer/procedure/target/result/time roles; CSAPI preserves System/resource identity and event relationships; AAS provides semantic references and representation/asset identity.

## 24.4 V2 inference

Where material, V2 should preserve:

- source/authority;
- derivation;
- producing or changing activity;
- responsibility/agent;
- time/version context.

## 24.5 Guardrail

V2 need not represent every concept as a PROV graph or claim native PROV conformance merely because PROV semantics inform the DIM.

---

# 25. Synthesis rule — “Without conflating those concerns with the subject itself”

This is the most important **V2-owned** brick.

No donor provides this exact umbrella rule.

It is induced from repeated source-native distinctions:

- System identity ≠ API resource identity (CSAPI);
- Asset ≠ Asset Administration Shell (AAS);
- Thing ≠ Thing Description ≠ Thing Model ≠ Virtual Thing (WoT);
- Device ≠ DeviceKind (SAREF);
- System ≠ Platform ≠ Deployment (W3C/OGC SOSA/SSN);
- Device composition ≠ communication topology ≠ integration host (OPC UA);
- Composition ≠ network topology (ISA);
- System ≠ Observation ≠ Command ≠ SystemEvent (CSAPI);
- capability ≠ operation/skill (AAS);
- configuration ≠ current state ≠ measurement output (UGS/BME280);
- observer/system ≠ Feature of Interest/target (OMS, W3C/OGC SOSA/SSN);
- equipment subject ≠ manager/controller/server (Redfish/LwM2M);
- enduring subsystem ≠ Deployment-scoped Aggregation (CSAPI).

The empirical pattern is not that every donor uses the same nouns. It is that mature models repeatedly **preserve role and identity distinctions instead of flattening all related information into one record or one hierarchy**.

The V2 synthesis is therefore:

> **The common subject should remain explicitly identifiable while its kinds, components, contexts, representations, capabilities, configurations, states, interactions, evidence, history, and provenance remain separately meaningful concepts or relationships.**

That is V2-authored synthesis justified by donor convergence.

---

## 26. The donor-accommodation envelope as a scope control

Pass 2 introduced a second empirical route to the DIM boundary.

The interoperability goal should not be read as:

> **A system conforming to any donor standard must have the entire donor standard represented by V2.**

That would make V2 unbounded.

Instead:

> **When an in-scope CSAPI-integrated System carries a donor semantic that V2 adopts, maps, or deliberately accommodates, the common DIM should be capable of preserving the material meaning and distinctions of that semantic.**

This principle explains why:

- OPC UA can donate Device/composition/communication distinctions without placing every drive, valve controller, or programmable logic controller in V2 scope;
- WoT can donate Thing/Thing Description/Thing Model/Virtual Thing distinctions without making every Web Thing an in-scope equipment System;
- AAS can donate Asset/representation/type-instance/capability semantics without making V2 a universal industrial-asset model;
- SAPIENT can donate capabilities, state, detections, tasks, subcomponents, and platform relationships without forcing its Fusion Node and complete system-of-systems hierarchy into one equipment subject;
- IEEE 1451 can donate smart-transducer/channel/self-description semantics without automatically admitting every actuator as an in-scope top-level subject.

This is the **inside-out compatibility test** for scope.

---

## 27. Empirical counterexamples and what they teach

| Counterexample | Evidence | Why it does not invalidate the refined hypothesis | Boundary lesson |
| --- | --- | --- | --- |
| atomic BME280 | product datasheet | internal parts need not become independent subjects | physical existence alone does not set modeling granularity |
| composite weather station | CSAPI/SensorML | one sensing subject can contain several sensors/computation | sensing orientation survives composition |
| camera with internal actuator/computation | SensorML | whole system remains sensing-oriented | non-sensing internal functions are allowed |
| radiation portal | radiation donor family | one subject can contain meaningful detector substructure | component standing depends on semantic significance |
| UGS sensor cueing imager | UGS evidence | cueing relationship need not imply composition | operational relation ≠ part-of |
| sensor payload on reusable unmanned aerial vehicle | CSAPI Composition/Aggregation; SOSA/SSN hosting | payload can remain separate System | host ≠ intrinsic composition by default |
| pure actuator/valve controller | OPC UA; IEEE 1451 | useful donor semantics do not imply current V2 scope | donor universe is broader than donor contribution |
| SAPIENT soft-kill effector | SAPIENT | pure effector has non-sensing defining orientation | deliberate expansion required for pure effectors |
| SAPIENT Fusion Node hierarchy | SAPIENT | fusion/system-of-systems semantics operate above one equipment subject | integration boundary ≠ enduring equipment boundary |
| WoT Virtual Thing/cloud service | WoT | representation/mediation may describe equipment without being equipment | digital representation is contextual/relational |
| human observer | CSAPI/SOSA/SSN | anchor standards permit it, but `assetType = Equipment` does not | broad anchor ontology does not force broad profile scope |
| simulation/prediction System | CSAPI | `Sensor + Simulation` is valid CSAPI but outside current equipment realization | role and realization are separate scope axes |

---

## 28. What the refined statement means empirically

The refined statement can now be read as a sequence of evidence-backed propositions.

### Proposition A — there is a stable subject

The donors repeatedly require identity of a real or managed subject that survives changes in representation, state, configuration, deployment, outputs, and history.

### Proposition B — the present subject is equipment-realized

The target cases motivating V2 are hardware/equipment Systems. The broader donor and anchor universes demonstrate other realizations, but those do not have to enter the current V2 boundary.

### Proposition C — the whole is sensing-oriented

Sensing/observing is the defining orientation of the whole subject, while mixed internal function remains allowed.

### Proposition D — scale is flexible

The subject can be atomic or composite. Internal elements earn independent standing from semantic/operational significance, not merely from physical existence.

### Proposition E — boundary is relational

Part-of, hosted-by, deployed-in, network-connected-to, managed-by, targets, and represented-by are materially different relationships.

### Proposition F — descriptive concerns are not identities

Kind/model, capability, configuration, state, interactions, outputs/actions, history, and provenance describe or relate to the subject; they are not interchangeable with the subject.

These propositions are the substantive content of the refined hypothesis.

---

## 29. What remains unresolved

This paper strengthens the refined hypothesis but does not close several questions.

1. **Pure effectors:** V2 currently excludes them as top-level subjects unless sensing remains the defining orientation. Future scope expansion remains possible.
2. **Component threshold:** the evidence supports criteria for independent representation but not one universal cardinality or rule.
3. **Host/composition edge cases:** relationship semantics must be assessed case-by-case rather than by labels such as “platform,” “chassis,” or “vehicle.”
4. **Digital representation:** a common represented-by/exposed-by concept may belong in the DIM, but exact digital-twin/proxy structures require later consolidation.
5. **Capability semantics:** donors use “capability,” “function,” “feature,” and supported behavior differently; canonical meaning is not yet settled.
6. **Configuration/state:** the distinctions are strong, but a common conceptual pattern still needs consolidation.
7. **Final domain name:** no existing noun has yet been proven superior to the descriptive boundary. No new umbrella term should be coined merely to make the model tidy.

---

## 30. Conclusion

The refined hypothesis has a traceable empirical pedigree.

Its strongest claims are not dependent on one donor:

- CSAPI supplies the clearest native role/realization and Composition/Aggregation semantics.
- W3C/OGC SOSA/SSN supplies System, Sensor, Platform, subsystem, Deployment, Procedure, and target semantics.
- SensorML supplies whole-system sensing, heterogeneous internal function, and atomic/aggregate physical-system modeling.
- Open Group SOSA independently reinforces the bounded Sensor and Host Platform distinction.
- OPC UA Devices reinforces equipment/device identity, recursive composition, and separation of Device, communications topology, and integration host.
- AAS, SAREF, and WoT reinforce subject-versus-representation and instance-versus-kind/model distinctions.
- Redfish, LwM2M, ISA, OSUS, and UGS evidence reinforce management, state, interface, mediation, and operational-boundary distinctions.
- W3C PROV supplies mature provenance semantics.
- Real product/system evidence prevents the conceptual model from requiring every possible structure on every piece of equipment.

The resulting statement remains V2 synthesis, but it is no longer an unsupported abstraction:

> **The DIM appears to be converging on an individually identifiable, persistently describable, equipment-realized System whose defining operational orientation is sensing/observing, but which may contain or perform non-sensing functions. The subject may be atomic or composite; its enduring composition can be distinguished from hosting, deployment, network, management, target, and digital-representation context; and its kind/model, capabilities, configuration, state, interactions, outputs/actions, history, and provenance can be represented without conflating those concerns with the subject itself.**

The empirical significance of the statement is that the **outside-in donor boundary analysis and the inside-out donor-accommodation analysis now converge on substantially the same subject**. That convergence is evidence that the emerging boundary is not merely a CSAPI naming artifact or an AI-generated taxonomy. It is a working hypothesis grounded in recurring donor-native distinctions and tested against counterexamples.

The next appropriate research step is canonical concept consolidation, not further broadening of the boundary unless contradictory evidence emerges.

---

## References

Bosch Sensortec. 2024. *BME280 Combined Humidity and Pressure Sensor: Data Sheet*. Revision 1.24. February.

British Standards Institution (BSI). 2024. *BSI Flex 335 v2.0:2024-03: SAPIENT Network of Autonomous Sensors and Effectors—Interface Control Document—Specification*. March.

Defence Science and Technology Laboratory. 2026. “SAPIENT: How It Works.” GOV.UK. October 14. https://www.gov.uk/government/publications/sapient-how-it-works/sapient-how-it-works.

European Telecommunications Standards Institute. 2024. *SAREF: Smart Applications REFerence Ontology—Core*. Version 4.1.1.

IEEE. 2024. *IEEE Standard for a Smart Transducer Interface for Sensors and Actuators—Common Functions, Communication Protocols, and Transducer Electronic Data Sheet (TEDS) Formats*. IEEE 1451.0-2024.

Industrial Digital Twin Association. 2026. *Specification of the Asset Administration Shell, Part 1: Metamodel*. IDTA 01001, version 3.2. July.

National Institute of Standards and Technology. 2024. “IEEE 1451.0-2024 Standard Published Under Leadership of NIST Researchers.” July 1.

Open Geospatial Consortium. 2025a. *OGC API—Connected Systems—Part 1: Feature Resources*. OGC 23-001, version 1.0. July 16. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC SensorML Encoding Standard*. OGC 23-000, version 3.0. July 16. https://docs.ogc.org/is/23-000/23-000.html.

Open Geospatial Consortium and International Organization for Standardization. 2023. *Observations, Measurements and Samples*. OGC 20-082r4 / ISO 19156:2023.

OPC Foundation. n.d. *OPC Unified Architecture Part 100: Devices*. Version 1.05.0. https://reference.opcfoundation.org/specs/OPC-10000-100/full.

The Open Group. 2023. *Technical Standard for SOSA Reference Architecture, Edition 1.1*. C239. June, with September 2023 erratum.

World Wide Web Consortium. 2013. *PROV-DM: The PROV Data Model*. W3C Recommendation. April 30.

World Wide Web Consortium. 2023a. *Web of Things (WoT) Architecture 1.1*. W3C Recommendation. December 5. https://www.w3.org/TR/wot-architecture11/.

World Wide Web Consortium. 2023b. *Web of Things (WoT) Thing Description 1.1*. W3C Recommendation. December 5. https://www.w3.org/TR/wot-thing-description11/.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology—2023 Edition*. Working Draft, October 21. OGC 25-022. https://www.w3.org/TR/vocab-ssn-2023/.
