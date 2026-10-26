# DIM/Profile V2 — Pedigree of the Emerging Subject-and-Boundary Synthesis

**Version:** 0.1  
**Date:** 26 October 2026  
**Standing:** Pedigree/explanation artifact; not a final DIM scope decision, class definition, module architecture, or application-profile binding  
**Controlling continuity:** `PITON_DIM_Profile_V2_Continuity_v1.3_26OCT2026.md`  
**Primary inputs:** early CSAPI concept baseline; validated/bounded Phase A lineage extractions; C08 calibration audit; Phase A bulk trust triage; Post-Audit Discovery Pass 1  
**Excluded from input:** quarantined Phase B/C/D artifacts and their promoted anatomy decisions

## 1. Purpose

The first post-audit discovery pass produced the following synthesized hypothesis:

> **The DIM appears to be converging on an individually identifiable, persistently describable sensing-oriented technical subject that may be atomic or composite, whose enduring equipment boundary can be distinguished from its host, deployment, network, management and target context, and whose kind/model, capabilities, configuration, state, interactions, outputs/actions, history and provenance can be understood without conflating those with the subject itself.**

This document explains the **pedigree of that sentence**.

The objective is not merely to attach citations after the fact. It is to identify, matter of factly:

1. which donor sources supplied or strongly supported each idea;
2. what the relevant concept means **inside the donor's own model**;
3. which part is a direct donor concept versus a project interpretation or synthesis;
4. what that donor contribution means for the emerging DIM; and
5. what the project must **not** infer merely because two donors use similar words.

The synthesized sentence is therefore treated as a proposition whose parts must be traceable back to source-native distinctions.

## 2. Synthesized result with inline source pedigree

> **The DIM appears to be converging on an individually identifiable, persistently describable sensing-oriented technical subject** (Open Geospatial Consortium 2025a; W3C and Open Geospatial Consortium 2026; Industrial Digital Twin Association 2026; ETSI 2024) **that may be atomic or composite** (Open Geospatial Consortium 2025b; OPC Foundation n.d.; Bosch Sensortec 2024), **whose enduring equipment boundary can be distinguished from its host, deployment, network, management, and target context** (Open Geospatial Consortium 2025a; W3C and Open Geospatial Consortium 2026; The Open Group 2023; PEO IEW&S 2023; OPC Foundation n.d.), **and whose kind/model, capabilities, configuration, state, interactions, outputs/actions, history, and provenance can be understood without conflating those with the subject itself** (Open Geospatial Consortium 2025a, 2025b; Industrial Digital Twin Association 2026; ETSI 2024; W3C 2023a, 2023b; W3C 2013).

No single donor states this sentence. The sentence is a **project synthesis**. Its pedigree is a combination of direct donor concepts, independently recurring distinctions, and operational falsification evidence.

## 3. How pedigree is weighted

The sources do not function as thirty equal votes. Three kinds of pedigree are distinguished.

### 3.1 Native anchor contribution

A source belongs to the standards environment in which the intended profile will ultimately operate or supplies semantics that CSAPI explicitly builds upon. Examples include OGC API – Connected Systems, SensorML, SOSA/SSN, and OMS.

These sources are particularly important for terminology, mapping, and later binding compatibility.

### 3.2 Independent corroboration

An unrelated standards community independently makes a structurally similar distinction. Examples include AAS, OPC UA Devices, SAREF, W3C WoT, Redfish, ISA, and The Open Group SOSA.

Independent corroboration is valuable because it can show that a distinction is not merely an artifact of CSAPI's API design.

### 3.3 Operational or scale falsification

A product/manual/reference-system source demonstrates whether an abstract distinction survives contact with real equipment. The Bosch BME280 and UGS evidence are examples.

These sources do not supply universal vocabulary. Their value is to test whether a proposed abstraction becomes absurd when applied to small or fielded systems.

The sections below identify these roles explicitly.

---

# 4. “Individually identifiable”

## Donor-native meaning

### OGC API – Connected Systems — direct native anchor

CSAPI requires a `System` resource to carry a `uniqueIdentifier` that is intended to be persistent and independent of the API resource URL. The standard explains why: different services may hold different representations or descriptions of the same real-world object, and the UID permits those representations to refer to the same underlying identity (Open Geospatial Consortium 2025a, secs. 8.5, 9.2.2).

This is the most direct donor for the words **individually identifiable**.

The important CSAPI distinction is:

> **identity of the real-world System ≠ identity/address of one API resource representation**

The local resource ID and canonical URL are implementation/API identifiers. The UID is intended to carry the identity of the represented thing across services.

### AAS — independent corroboration

AAS likewise distinguishes the represented **Asset** from the Asset Administration Shell that digitally represents it. `AssetInformation` carries identifying metadata for the represented asset, including global and domain-specific identifiers, and distinguishes kinds such as type and instance assets (Industrial Digital Twin Association 2026).

AAS therefore independently reinforces:

> **represented subject ≠ its digital shell/representation**

### SAREF — independent corroboration

SAREF defines `saref:Device` as a tangible object and says that an instance of Device represents one specific real-world entity. It separately provides `DeviceKind` for archetypal/model-level description (ETSI 2024).

SAREF therefore reinforces both individual identity and the later instance-versus-kind distinction.

## What the DIM takes from this

The DIM should be capable of representing **an individual subject that remains the same subject across representations, descriptions, services, deployments, and changing runtime information**.

This does **not** require the DIM to adopt CSAPI's UID field, AAS identifiers, or SAREF IRIs as its implementation mechanism. Those are donor/binding mechanisms.

The DIM-level requirement is the semantic distinction:

> **the modeled individual has identity independent of any one representation of it.**

---

# 5. “Persistently describable”

## Donor-native meaning

“Persistently describable” is **our synthesis phrase**, not a term defined by one donor.

It is derived from several source-native distinctions.

### CSAPI — persistent subject identity plus changing description

CSAPI's persistent `uniqueIdentifier` identifies the System while `validTime`, location, Deployments, DataStreams, ControlStreams, Observations, Commands, and SystemEvents can vary over time (Open Geospatial Consortium 2025a).

The System remains the referent even when information about it changes.

### W3C WoT — Thing versus representation

W3C WoT distinguishes the **Thing** from its Thing Description. A Thing is the abstraction of a physical or virtual entity; the Thing Description is a machine-readable representation of its metadata and interfaces. WoT also allows the description to be hosted separately from the physical Thing (W3C 2023a, 2023b).

This independently supports:

> **the subject is not exhausted by one digital representation of it.**

### AAS — Asset versus shell and Submodels

AAS separates the represented Asset from the AAS and from the multiple Submodels that describe different aspects of that Asset (Industrial Digital Twin Association 2026).

## What the DIM takes from this

“Persistently describable” means:

> **the DIM's subject must be able to remain conceptually stable while descriptions, representations, configuration, state, deployment, observations, commands, and other information about it change.**

This is not a claim that every donor implements temporal persistence in the same way. It is a synthesis of the repeated separation between **subject identity** and **information about the subject**.

---

# 6. “Sensing-oriented”

## Donor-native meaning

### CSAPI — strongest direct source for “orientation”

CSAPI's `systemType` classifies the principal activity of a System. `Sensor` is used when the System's **primary activity is sensing or observing**. `Actuator`, `Sampler`, `Platform`, and generic `System` are separate alternatives (Open Geospatial Consortium 2025a, sec. 9.2.2).

This is why the synthesis deliberately says **sensing-oriented**, rather than simply asserting that every subject must already be an ontology instance of one universal Sensor class.

CSAPI donates the idea:

> **the whole subject can be characterized by its principal operational role.**

### SOSA/SSN — semantic anchor

SOSA/SSN defines `Sensor` as a specialization of System associated with observing, while System itself is broader and may implement Procedures. The current 2023 Edition also distinguishes System composition, Platform hosting, and Deployment (W3C and Open Geospatial Consortium 2026).

SOSA/SSN contributes the semantic meaning of sensing within the anchor ontology.

### SensorML — whole-system sensing despite heterogeneous internals

SensorML provides an especially important refinement. A PhysicalSystem can represent a sensor system whose **overall application is sensing** even though its internal components can include sensing, actuation, and computation. SensorML's camera example explicitly contains detectors, computation, and an actuator while the camera remains a sensing system overall (Open Geospatial Consortium 2025b, sec. 8.6).

SensorML therefore contributes:

> **heterogeneous internal functions do not necessarily change the defining role of the whole.**

### The Open Group SOSA — independent sensing-domain corroboration

The Open Group SOSA architecture treats the Sensor as a bounded architectural subject containing heterogeneous hardware, software, infrastructure, processing, management, power, and other supporting elements while maintaining an external boundary to the Host Platform and other external elements (The Open Group 2023).

## What the DIM takes from this

The current evidence supports using **sensing as the defining orientation of the whole subject**, while not requiring every internal component or function to be itself a Sensor.

It does **not yet prove** that every eventual V2 top-level target must have sensing as its primary role. That remains one of the explicit open boundary questions.

---

# 7. “Technical subject” and “equipment”

## Donor-native meaning

“Technical subject” is another **project synthesis phrase**. It exists because the donors use different native nouns.

### CSAPI — Equipment realization

CSAPI's independent `assetType` facet classifies what kind of realization is involved. `Equipment` means a System composed of one or more hardware devices or pieces of equipment that interact directly with the real world. Other asset types include Human, LivingThing, Simulation, Process, Group, and Other (Open Geospatial Consortium 2025a, sec. 9.2.2).

CSAPI therefore provides the strongest native basis for the **equipment-realization** part of the current boundary.

### SAREF — Device as a tangible real-world entity

SAREF defines Device as a tangible object designed to accomplish a task by performing one or more functions (ETSI 2024).

### OPC UA Devices — Device and its hardware/software parts

OPC UA Part 100 defines a Device Model intended to provide a unified view of Devices and their hardware and software parts independently of underlying device protocols (OPC Foundation n.d.).

### AAS — Asset as the represented subject

AAS uses Asset as the represented real-world/business/technical subject and separates it from its digital administration shell (Industrial Digital Twin Association 2026).

## What the DIM takes from this

We are not presently adopting **Asset**, **Device**, **Equipment**, or **System** as a new universal V2 root solely because several communities use them.

The synthesized phrase **technical subject** intentionally stays neutral while the research remains open.

The current substantive point is:

> **the target is not merely an observation act or information service; it is a real technical subject with an equipment/device realization that can itself be identified and understood.**

---

# 8. “May be atomic or composite”

## Donor-native meaning

### SensorML — direct conceptual donor for atomic versus aggregate description

SensorML explicitly distinguishes:

- **PhysicalComponent** — a physical processing device for which there is no intent to further divide the description into component subprocesses; and
- **PhysicalSystem** — an aggregate hardware device whose description is divided into subprocess components (Open Geospatial Consortium 2025b, secs. 8.5–8.6).

This is the strongest standards-level donor for the atomic/composite idea.

Importantly, this is a **modeling boundary**, not merely a statement about whether microscopic parts physically exist.

### OPC UA Devices — recursive modular composition

OPC UA Part 100 supports Devices composed of subdevices/modules, and subdevices may themselves be modular Devices (OPC Foundation n.d.).

### SAREF — composite device semantics

SAREF provides `consistsOf`, including examples such as a temperature/humidity sensor consisting of separate temperature and humidity sensors (ETSI 2024).

### Bosch BME280 — operational/scale falsifier

The BME280 datasheet describes one integrated sensor product containing multiple sensing elements, analog front ends, conversion/control electronics, memory, power circuitry, and interfaces. Yet those internals are not independently managed product subjects with their own persistent equipment identity (Bosch Sensortec 2024).

The BME280 therefore prevents the project from making the opposite mistake:

> **real internal structure does not imply that every internal block deserves an independent DIM subject.**

## What the DIM takes from this

The synthesis is:

> **the same common model must be able to describe both an atomic equipment subject and a meaningfully decomposed composite subject.**

A likely later modeling rule is that independent representation of an internal element must be justified by meaningful identity, state, configuration, capability, outputs/actions, serviceability, or relationships.

That rule is still a **project interpretation** to test; no single donor states it exactly in those words.

---

# 9. “Enduring equipment boundary”

## Donor-native meaning

This phrase synthesizes two ideas:

1. an **equipment/device realization**; and
2. a meaningful distinction between what belongs to the subject and what is only related to it.

### CSAPI — strongest direct donor for enduring versus temporary association

CSAPI explicitly distinguishes **Composition** from **Aggregation**.

Composition means a subsystem is an integral part of the parent and is not normally separated during its lifetime except for maintenance. Aggregation means the subsystem is not permanently attached and may be associated with different parents at different times; CSAPI represents this through Deployment (Open Geospatial Consortium 2025a, sec. 10.2).

This is the clearest direct source for the word **enduring** in our synthesized boundary concept.

### SOSA/SSN — subsystem, hosting, and Deployment are different relationships

SOSA/SSN separately provides:

- `hasSubSystem` / `isSubSystemOf`;
- `hosts` / `isHostedBy` for Platform hosting; and
- Deployment relationships (W3C and Open Geospatial Consortium 2026).

That is strong semantic evidence that part-of, hosted-by, and deployed-in should not be collapsed.

### The Open Group SOSA — bounded Sensor versus Host Platform

The Open Group SOSA architecture independently treats the Sensor as having a boundary and distinguishes the external Host Platform from the Sensor itself (The Open Group 2023).

### ISA — composition topology versus network topology

ISA separately structures Compositions/components and their broader ISA network relationships (PEO IEW&S 2023). This independently warns against interpreting communications participation as physical composition.

### OPC UA Devices — device topology versus communications/integration topology

OPC UA Part 100 explicitly builds separate Device, Device Communication, and Device Integration Host models (OPC Foundation n.d.).

## What the DIM takes from this

This is one of the strongest convergent findings in the corpus:

> **the DIM must be able to say what belongs to the persistent subject without using one generic relationship for every association around it.**

The exact final relationship names are still open.

---

# 10. “Distinguished from host, deployment, network, management, and target context”

These words each have a different pedigree.

## 10.1 Host

### SOSA/SSN

A System may be hosted by a Platform; Platform hosting is distinct from subsystem composition (W3C and Open Geospatial Consortium 2026).

### The Open Group SOSA

The Host Platform sits outside the Sensor boundary and interacts across a defined Host Platform Interface (The Open Group 2023).

**DIM implication:** being carried by or hosted on something does not automatically make that host part of the sensing equipment.

## 10.2 Deployment

### CSAPI

Deployment carries time-scoped employment/association information and is also the mechanism CSAPI uses for non-permanent Aggregation (Open Geospatial Consortium 2025a).

### SOSA/SSN and OMS

Both provide explicit Deployment concepts connecting Systems/Observers to hosting or operational context (W3C and Open Geospatial Consortium 2026; Open Geospatial Consortium and ISO 2023).

**DIM implication:** where/how/when a subject is employed is not automatically intrinsic composition.

## 10.3 Network

### ISA

ISA's Composition structure and network participation are different architectural structures (PEO IEW&S 2023).

### OPC UA Devices

The Device Communication Model adds Networks and ConnectionPoints on top of the base Device Model rather than treating communication topology as the same thing as device composition (OPC Foundation n.d.).

### IETF interface/topology donors

The IETF interface/topology lineage independently reinforces that interface identity, layering, nodes, termination points, and links form a network topology rather than a physical bill of materials.

**DIM implication:** network-connected does not mean part-of.

## 10.4 Management

### Redfish

Redfish distinguishes physical Chassis/Systems from `Manager` resources and explicit `ManagedBy`/management relationships.

### LwM2M

LwM2M separates the managed Client/device-side resource model from the LwM2M Server and Bootstrap Server that manage it.

**DIM implication:** the entity that manages or controls the subject is not automatically inside the subject's equipment boundary.

## 10.5 Target context

### SOSA/SSN and OMS

Observation semantics explicitly distinguish the observing System/Observer from the FeatureOfInterest whose property is being observed (W3C and Open Geospatial Consortium 2026; Open Geospatial Consortium and ISO 2023).

### CSAPI

CSAPI separately represents Sampling Features and links to ultimate features of interest (Open Geospatial Consortium 2025a).

### SAREF

SAREF likewise separates Device from FeatureOfInterest and the properties/states that may be targeted by observation or control (ETSI 2024).

**DIM implication:** what the sensing subject observes, measures, detects, samples, or controls is not the sensing subject itself.

---

# 11. “Kind/model”

## Donor-native meaning

This concept is unusually well corroborated, but the donor mechanisms are not identical.

### CSAPI

`systemKind` links a System instance to a single Procedure resource describing the **kind of System**, such as a datasheet. CSAPI separately links the System to Procedures it can implement. The C08 audit established that these two uses must not be conflated (Open Geospatial Consortium 2025a).

### SAREF

`DeviceKind` represents an archetype/model of Devices and can carry common functions/properties/states inherited by individual Device instances (ETSI 2024).

### AAS

AAS distinguishes type assets from instance assets and permits template versus instance Submodels (Industrial Digital Twin Association 2026).

### W3C WoT

Thing Model describes a class of Things with common capabilities; Thing Description describes a particular Thing instance and contains instance-specific interaction information (W3C 2023a, 2023b).

### Matter — corroborating but binding-specific

Matter Device Types classify Endpoint functionality and conformance expectations. This is useful corroboration of type-versus-instance structure but remains a Matter protocol/data-model construct.

## What the DIM takes from this

The donor evidence strongly supports keeping at least these ideas separate:

> **individual subject ≠ reusable product/model/kind description ≠ reusable Procedure/Method**

The exact common concepts and mappings still require later consolidation.

---

# 12. “Capabilities”

## Donor-native meaning

The word **capability** is overloaded across donors; the synthesis must not pretend they all define the same class.

### AAS

AAS defines `Capability` separately from `Operation`. Capability expresses what an asset can potentially achieve; Operations/skills concern callable or implementing behavior. Capability Description templates add properties and constraints around capabilities (Industrial Digital Twin Association 2026).

### SensorML

SensorML's core description includes capabilities and characteristics, while its process model separately represents inputs, outputs, parameters, methods, and configuration (Open Geospatial Consortium 2025b).

### SAREF

SAREF uses functions and functions of interest to represent what a Device can do and relates them to Commands and targets rather than using AAS's Capability class (ETSI 2024).

### ISA / SAPIENT

Both expose declared/supported capabilities in their own architecture/interface terms, alongside current state and tasking.

## What the DIM takes from this

The common lesson is **not** “everyone has the same Capability concept.”

It is:

> **what a subject is able or designed to do must remain distinguishable from what it is currently configured to do, what state it is currently in, and an individual action/request executed at runtime.**

That is a cross-donor synthesis.

---

# 13. “Configuration”

## Donor-native meaning

### SensorML

SensorML models configurable parameters, modes, settings, and component/process descriptions, including the distinction between generic model/type description and deployed configuration (Open Geospatial Consortium 2025b).

### ISA

ISA exposes component configuration separately from capabilities, current state/status, and runtime requests.

### UGS operational evidence

TRSS/OmniSense evidence is especially useful operationally because it distinguishes stored configuration, queued/requested changes, and later device-reported/applied state.

### Bosch BME280

Even an atomic sensor distinguishes supported performance/capability, selected settings such as oversampling/filter/mode, runtime status, and actual measurement output (Bosch Sensortec 2024).

## What the DIM takes from this

Configuration is not merely another word for capability or current state.

The project should preserve the distinction among:

- what settings/modes are supported;
- what settings are selected/intended;
- what changes are requested;
- and what the device actually reports/applies.

The exact common configuration model remains open.

---

# 14. “State”

## Donor-native meaning

### Redfish

Redfish has explicit resource `Status`, `Condition`, state, health, and resource-specific state semantics.

### ISA / UGS

Operational systems expose device/component status, readiness, mode, faults, battery, communications state, and other reported values.

### BME280

The BME280 demonstrates on a small scale that operating mode, configuration registers, status bits, and measurement outputs are distinct information categories (Bosch Sensortec 2024).

## What the DIM takes from this

There is strong evidence that **current reported condition/state** is meaningful, but there is not strong evidence for one universal Status enum covering all domains.

The donor evidence supports keeping:

> **capability ≠ configuration ≠ current reported state ≠ historical event**

The vocabulary and dimensions of state may remain specialized.

---

# 15. “Interactions” and “outputs/actions”

## Donor-native meaning

### CSAPI

CSAPI/Part 2 separates:

- DataStream from individual Observation;
- ControlStream from individual Command;
- Command from CommandStatus and CommandResult;
- Feasibility from execution;
- SystemEvent from observation data.

This is the strongest native OGC source for outputs/actions and runtime interaction structure.

### W3C WoT

WoT defines three principal Interaction Affordances in Thing Descriptions/Models: **Properties, Actions, and Events** (W3C 2023a, 2023b).

### SensorML

SensorML describes processes through inputs, outputs, parameters, methods, and connections (Open Geospatial Consortium 2025b).

### SAREF

SAREF connects Device functions, Commands, Properties/States, observations/actuations, and target entities (ETSI 2024).

### OSUS / SAPIENT / UGS

Operational donor evidence repeatedly demonstrates subjects that both produce information and accept tasking/commands.

## What the DIM takes from this

The phrase **interactions, outputs/actions** is deliberately broader than any one donor's API model.

It captures the recurring need to understand:

- what information the subject produces;
- what interactions it supports;
- what may be requested of it;
- and how runtime execution/results differ from capability declarations.

It does not mean the DIM must reproduce CSAPI's resource graph or WoT's affordance model.

---

# 16. “History”

## Donor-native meaning

### CSAPI

`SystemEvent` explicitly represents events over the life/operation of a System, including calibration, configuration change, software update, part replacement, relocation/deployment, and related events (Open Geospatial Consortium 2025a).

### Redfish / MIMOSA / UGS

These donors independently expose logs, service/maintenance information, events, condition history, or operational event records in their respective domains.

## What the DIM takes from this

The important distinction is:

> **current description/state ≠ history of what happened to the subject**

History may later prove to be represented through a common event pattern, specialized lifecycle structures, or both. That remains open.

---

# 17. “Provenance”

## Donor-native meaning

### W3C PROV — direct cross-cutting donor

PROV-DM defines domain-agnostic provenance in terms of Entities, Activities, Agents, generation, usage, derivation, attribution, association, and responsibility. Its purpose is to capture how data or things came to exist and who/what was involved (W3C 2013).

PROV is not an equipment model. Its contribution is cross-cutting.

### UGS operational evidence — operational need for authority/source

UGS evidence distinguishes database/editor values, requested/queued settings, returned device values, device GPS versus entered location, and potentially different equipment producing detections and imagery.

This demonstrates why “source” cannot be one coarse field if information from different authorities is combined.

### CSAPI / AAS

Both preserve resource/representation identity and references sufficiently to support source traceability, but neither should be treated as a replacement for a general provenance model.

## What the DIM takes from this

The DIM likely needs to support **where information came from, what process/activity produced or changed it, and who/what is responsible**, where that matters.

It does not follow that every DIM concept must be encoded as a PROV Entity/Activity/Agent graph.

---

# 18. “Without conflating those with the subject itself”

This final clause is the most synthetic part of the sentence.

No donor contributes it as one explicit rule.

It is induced from repeated source-native separations:

- Asset ≠ AAS representation (IDTA);
- Thing ≠ Thing Description ≠ Thing Model (W3C WoT);
- System instance ≠ system kind ≠ implemented Procedure (CSAPI);
- Device ≠ DeviceKind (SAREF);
- System ≠ Deployment ≠ hosted Platform (SOSA/SSN);
- Device composition ≠ communications/integration topology (OPC UA);
- composition ≠ network participation (ISA);
- System ≠ Observation ≠ Command ≠ SystemEvent (CSAPI);
- capability ≠ operation/skill (AAS);
- configuration ≠ status ≠ measurement output (BME280/UGS);
- sensing subject ≠ FeatureOfInterest/target (SOSA/SSN, OMS, SAREF).

The recurring empirical pattern is that mature donor models often **preserve distinctions rather than flatten all information into one object record or hierarchy**.

The DIM synthesis therefore takes the position:

> **The common subject should remain conceptually identifiable while related descriptions, kinds, internal parts, contexts, capabilities, configurations, states, interactions, evidence, history, and provenance remain explicitly related to it rather than being silently treated as interchangeable aspects of one concept.**

That is a **V2 analytical conclusion**, not donor-owned vocabulary.

---

# 19. Pedigree summary matrix

| Synthesized phrase | Strongest direct donors | Independent corroboration / falsification | What the donor actually contributes | What V2 synthesizes |
| --- | --- | --- | --- | --- |
| individually identifiable | CSAPI | AAS, SAREF, Redfish | subject identity distinct from resource/representation identity | an individual modeled subject persists across representations |
| persistently describable | CSAPI | AAS, WoT | stable referent with changing descriptions/representations | subject remains conceptually stable while information changes |
| sensing-oriented | CSAPI, SOSA/SSN | SensorML, Open Group SOSA, SAREF | sensing as whole-System role; Sensor semantics | sensing presently appears to define the whole subject's orientation |
| technical/equipment subject | CSAPI Equipment | SAREF Device, OPC UA Device, AAS Asset | hardware/device realization of the subject | neutral technical-subject wording pending final domain name |
| atomic or composite | SensorML | OPC UA, SAREF, BME280, radiation/UGS | atomic component vs aggregate/system structures | common model must scale without forced decomposition |
| enduring boundary | CSAPI Composition/Aggregation | SOSA/SSN, Open Group SOSA, ISA, OPC UA | enduring part versus contextual/temporary/hosting/network relation | part-of must not collapse with all other relationships |
| host context | SOSA/SSN | Open Group SOSA | Platform hosting separate from subsystem | host is not automatically intrinsic equipment |
| deployment context | CSAPI, SOSA/SSN, OMS | UGS | time/purpose-scoped employment/association | deployment belongs around the subject, not automatically inside it |
| network context | ISA, OPC UA | IETF topology, UGS | communication topology distinct from composition | connected-to is not part-of |
| management context | Redfish, LwM2M | ISA/OSUS | manager/server/controller relationships | managed-by is not intrinsic composition |
| target context | SOSA/SSN, OMS | CSAPI, SAREF | FeatureOfInterest/target distinct from observer/device | sensed/controlled thing is not the sensing subject |
| kind/model | CSAPI, SAREF | AAS, WoT, Matter | reusable type/kind/model distinct from instance | preserve instance vs model/kind vs Procedure |
| capability | AAS, SensorML | SAREF, ISA, SAPIENT | supported function/potential behavior | keep capability distinct from config/state/execution |
| configuration | SensorML, ISA | UGS, BME280 | settings/modes and requested/applied distinctions | model configuration separately from capability/state |
| state | Redfish | ISA, UGS, BME280 | current status/condition/operating state | avoid one universal state enum; preserve current-state role |
| interactions | WoT | CSAPI, SAREF, LwM2M | interaction affordances/operations | describe how the subject can be interacted with without making interface the subject |
| outputs/actions | CSAPI | SensorML, OSUS, SAPIENT, UGS | observations/data output versus commands/actions | preserve production and tasking semantics distinctly |
| history | CSAPI SystemEvent | Redfish, MIMOSA, UGS | event/service/configuration history | current description is not history |
| provenance | W3C PROV | UGS, CSAPI/AAS references | source, derivation, activity, responsibility | retain source/authority lineage without forcing PROV everywhere |

---

# 20. What is now stronger than before

The synthesized sentence is no longer merely a plausible paragraph generated from a large donor set.

Its individual propositions now have visible pedigree:

1. **Identity** is strongly sourced.
2. **Sensing orientation** is strongly sourced within the native anchor stack and independently corroborated.
3. **Equipment/device realization** is strongly sourced but the final umbrella name remains open.
4. **Atomic/composite scale** has both conceptual and real-product evidence.
5. **Boundary versus context** is one of the strongest cross-donor convergences.
6. **Instance versus kind/model/representation** is strongly cross-donor.
7. **Capability/configuration/state/runtime execution/history** are repeatedly separated, although exact common concepts remain to be consolidated.
8. **Provenance** has a mature external semantic donor and clear operational need.
9. The final rule against conflation is **our synthesis**, justified by repeated donor-native distinctions rather than donated as one ready-made concept.

This is sufficient to use the sentence as a **research hypothesis with traceable pedigree**.

It is not yet sufficient to freeze it as the final formal scope definition of the DIM.

## 21. References

Bosch Sensortec. 2024. *BME280 Combined Humidity and Pressure Sensor: Data Sheet*. Revision 1.24. February.

British Standards Institution. 2024. *BSI Flex 335 v2.0:2024-03: SAPIENT Network of Autonomous Sensors and Effectors—Interface Control Document—Specification*. March.

ETSI. 2024. *SAREF: Smart Applications REFerence Ontology—Core*. Version 4.1.1.

Industrial Digital Twin Association. 2026. *Specification of the Asset Administration Shell, Part 1: Metamodel*. IDTA 01001, version 3.2.

Open Geospatial Consortium. 2025a. *OGC API—Connected Systems—Part 1: Feature Resources*. OGC 23-001, version 1.0. July 16.

Open Geospatial Consortium. 2025b. *OGC SensorML Encoding Standard*. OGC 23-000, version 3.0. July 16.

Open Geospatial Consortium and International Organization for Standardization. 2023. *Observations, Measurements and Samples*. OGC 20-082r4 / ISO 19156:2023.

OPC Foundation. n.d. *OPC Unified Architecture Part 100: Devices*. Version 1.05.0.

PEO IEW&S. 2023. *Integrated Sensor Architecture (ISA): Data Model Specification*. Release 6.0, rev. 12. October 31.

PEO IEW&S. 2023. *Integrated Sensor Architecture (ISA): Software Design Document*. Release 6.0, rev. 5. October 31.

The Open Group. 2023. *Technical Standard for SOSA Reference Architecture, Edition 1.1*. C239. June, with September 2023 erratum.

W3C. 2013. *PROV-DM: The PROV Data Model*. W3C Recommendation. April 30.

W3C. 2023a. *Web of Things (WoT) Architecture 1.1*. W3C Recommendation. December 5.

W3C. 2023b. *Web of Things (WoT) Thing Description 1.1*. W3C Recommendation. December 5.

W3C and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology—2023 Edition*. Working Draft, October 21. OGC 25-022.
