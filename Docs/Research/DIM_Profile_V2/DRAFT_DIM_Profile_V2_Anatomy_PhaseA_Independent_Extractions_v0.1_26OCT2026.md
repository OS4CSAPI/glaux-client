# DIM/Profile V2 Anatomy — Phase A Independent Extractions

**Working draft v0.1 — 26 October 2026**  
**Status:** Phase A in progress; independent lineage extraction only. No cross-source synthesis or clean-DIM edits.  
**Controlling continuity:** `PITON_DIM_Profile_V2_Continuity_v0.7_26OCT2026.md`  
**Frozen population:** `DIM_Profile_V2_Anatomy_Phase0_Population_Decision_v0.1_26OCT2026.md`

## Method

The unit of analysis is the frozen semantic lineage, not an individual document. Every lineage is characterized under the same 15-field template. Source-native terminology and partitions are preserved. Field 15 is an evidence label only and does not create V2 modules.

---

# C01 — Asset Administration Shell (AAS)

## Source basis and evidence ceiling

**Frozen corpus sources:** 94, 95, 96, 97, 98.

**Primary inspected sources:**

- Industrial Digital Twin Association, *Specification of the Asset Administration Shell Part 1: Metamodel*, IDTA 01001 v3.2:
  - `https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/core.html`
  - `https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/submodel-elements.html`
- IDTA 02003, *Generic Frame for Technical Data for Industrial Equipment in Manufacturing*, v2.0, March 2025.
- IDTA 02011-1-1, *Hierarchical Structures enabling Bills of Material*, v1.1, June 2024.
- IDTA 02011-1, *Hierarchical Structures enabling Bills of Material — Extension based on IEC 81346*, v1.0, August 2025.
- IDTA 02020, *Capability Description*, v1.0, published template repository:
  `admin-shell-io/submodel-templates/published/Capability Description/1/0/`.

**Evidence note:** The AAS metamodel and published submodel templates are directly inspectable. The Capability Description structure was checked against the published README and JSON template in the official `admin-shell-io/submodel-templates` repository. This extraction is limited to the five AAS-lineage artifacts frozen in the V2 corpus; it does not import other IDTA submodels merely because they exist.

---

## 1. Source-native structural organization

The AAS lineage separates the digital representation into several levels rather than treating all information about an asset as one record.

### Metamodel level

The central structure is:

- **Asset Administration Shell**
  - contains mandatory **AssetInformation** about the represented asset;
  - references zero or more **Submodels**.
- **AssetInformation**
  - identifies the represented asset;
  - distinguishes asset kinds such as type, instance, batch and role;
  - supports global and supplementary asset identifiers.
- **Submodel**
  - is an identifiable unit of information;
  - defines a **specific aspect** of the represented asset;
  - is used to structure the asset's digital representation and technical functionality into distinguishable parts;
  - may be a template or an instance.
- **SubmodelElements**
  - provide the structural vocabulary inside Submodels.

The v3.2 metamodel explicitly includes SubmodelElement types for:

- data values;
- entities;
- relationships;
- collections/lists;
- capabilities;
- operations;
- events;
- references/files/blobs.

### Selected source-native Submodel Templates in the frozen corpus

The frozen AAS lineage adds four substantial aspect structures:

1. **Technical Data**
   - GeneralInformation;
   - ProductClassifications;
   - TechnicalPropertyAreas;
   - FurtherInformation;
   - SpecificDescriptions.

2. **Hierarchical Structures**
   - EntryNode;
   - Node;
   - parent/child relationships;
   - hierarchy archetypes Full, OneDown and OneUp;
   - self-managed/co-managed asset representation.

3. **IEC 81346 hierarchy extension**
   - Function aspect;
   - Product aspect;
   - Location aspect;
   - Type aspect;
   - Other aspect;
   - aspect-specific hierarchies and references from represented asset entities.

4. **Capability Description**
   - CapabilitySet;
   - CapabilityContainer;
   - Capability;
   - PropertySet / PropertyContainer;
   - ConstraintSet;
   - relationships to the described capability and external/same properties;
   - the source description distinguishes required capabilities from provided/resource capabilities and relates capability to properties, constraints and implementing skills.

The AAS structural pattern is therefore **shell + asset identity + independently scoped aspect Submodels + typed model elements**, with reusable aspect templates layered above the generic metamodel.

---

## 2. Purpose of each partition

### Asset Administration Shell / AssetInformation

Purpose: preserve the identity of the digital representation and identify the asset it represents. The Shell is the representation boundary; AssetInformation supplies identifying metadata about the represented asset.

### Submodel

Purpose: isolate a **well-defined domain, subject or aspect** of the represented asset. The metamodel intentionally treats a Submodel as a distinguishable information unit rather than making every concern a direct attribute of the Shell.

### Data-oriented SubmodelElements

Purpose: express values, ranges, files, references and structured collections.

### Entity / Relationship structures

Purpose: represent parts/entities and explicit semantic relationships, including composite-asset structures.

### Capability

Purpose: describe the asset's potential to achieve an effect independently of the implementation that realizes it.

### Operation

Purpose: describe callable behavior with defined input/output/in-out variables.

### Event

Purpose: represent reactive/event behavior associated with an observed referable and event-message context.

### Technical Data Submodel

Purpose: provide interoperable manufacturer/supplier technical information about an asset, separating minimal general information, market/product classification, technical properties, additional information and use-case-specific descriptions.

### Hierarchical Structures Submodel

Purpose: provide an authoritative asset hierarchy and composition view, including distributed hierarchies and assets that do or do not have their own AAS.

### IEC 81346 extension

Purpose: distinguish different **aspect views of the same technical system/object** rather than treating one hierarchy as sufficient for every engineering purpose.

### Capability Description Submodel

Purpose: model required and provided capabilities in a form that can support comparison, planning and orchestration.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Representation / identity | AssetAdministrationShell, AssetInformation, AssetKind, identifiers |
| Aspect partitioning | Submodel, SubmodelElement |
| Atomic/structured information | Property, MultiLanguageProperty, Range, File, Blob, ReferenceElement, Collection/List |
| Composition/entities | Entity, EntityType, EntryNode, Node, HasPart, IsPartOf, SameAs |
| Relationships | RelationshipElement, AnnotatedRelationshipElement |
| Function/behavior | Capability, Operation, OperationVariable |
| Reactive behavior | EventElement, BasicEventElement, EventPayload |
| Technical description | GeneralInformation, ProductClassifications, TechnicalPropertyAreas, FurtherInformation, SpecificDescriptions |
| Engineering aspect views | FunctionAspectNode, ProductAspectNode, LocationAspectNode, TypeAspectNode, OtherAspectNode |
| Capability description | CapabilitySet, CapabilityContainer, Capability, PropertySet, ConstraintSet, skill relationship |

---

## 4. Primary relationships

The AAS lineage relies heavily on explicit relationships rather than only nesting.

Important source-native relations include:

- AAS **represents** an asset through AssetInformation.
- AAS **references** Submodels.
- A Submodel **contains** SubmodelElements.
- Entity structures model composite assets.
- SelfManagedEntity and CoManagedEntity distinguish whether an entity has its own AAS.
- Hierarchical Structures use **HasPart / IsPartOf** between EntryNode/Node representations.
- **SameAs** can connect representations of the same asset across distributed Submodels.
- IEC 81346 extension links represented asset entities to separate aspect-specific hierarchy nodes.
- RelationshipElement provides general subject/object relationships whose meaning is carried by semantic identification.
- Capability may be related to **skills** implementing it.
- Capability properties and constraints qualify the capability rather than replacing it.

---

## 5. Dependency boundaries

AAS has explicit structural layering.

- Submodel Templates depend on the AAS metamodel.
- The metamodel supplies generic carriers; a Submodel Template supplies the domain/aspect semantics.
- Technical Data relies on external semantic dictionaries such as ECLASS/IEC CDD for interoperable property meaning.
- The IEC 81346 hierarchy extension depends on the generic Hierarchical Structures model and adds aspect-specific semantics.
- Capability Description uses generic AAS Capability, collections, properties, constraints and relationships but supplies a more specific capability-description organization.

The Shell itself therefore does **not** define the full domain anatomy. Meaning is intentionally distributed across metamodel primitives, semantic identifiers and separately standardized Submodel Templates.

---

## 6. Intrinsic vs contextual standing

The AAS lineage does not enforce one universal distinction between intrinsic and contextual information. Instead, it permits different Submodels/aspects to carry different views of the asset.

Within the frozen lineage:

### Strongly intrinsic / asset-description oriented

- AssetInformation;
- technical properties;
- product classification;
- persistent component hierarchy where represented as a Bill of Material;
- provided capabilities.

### Potentially contextual or viewpoint-dependent

- Location aspect;
- required capability in relation to a process/product requirement;
- OneUp installation relationship;
- use-case-specific descriptions;
- some hierarchy views depending on lifecycle/use case.

AAS therefore treats context partly through **separate aspects and relationship structures** rather than through one global intrinsic/context flag.

---

## 7. Cross-cutting concepts

Several AAS mechanisms intentionally span aspect Submodels:

- semanticId / ConceptDescription semantics;
- identifiers and references;
- model/template versus instance distinction;
- qualifiers;
- data specifications;
- relationships;
- administrative information/versioning;
- type/instance asset distinction.

The selected submodels also demonstrate cross-aspect reference patterns: the IEC 81346 extension can be referenced from the generic hierarchy, and capability properties can point to properties represented elsewhere.

---

## 8. State / temporal / lifecycle organization

The frozen AAS lineage does **not** define one universal lifecycle-state model for the asset.

It does provide:

- administrative/version information for model elements;
- type versus instance distinctions;
- events and timestamps in the metamodel;
- Technical Data validity/additional information;
- hierarchy structures intended to be authoritative across lifecycle phases;
- hierarchy archetypes that support centralized or distributed structures and changing integration contexts.

The Hierarchical Structures specification explicitly acknowledges that different lifecycle phases can require different hierarchy detail and that structures can be distributed across independently managed AASs.

Lifecycle-specific semantics are therefore **aspect/template dependent**, not centralized in one AAS lifecycle partition in the selected corpus.

---

## 9. Composition / topology organization

Composition is one of the strongest structures in this lineage.

The generic hierarchy template supports:

- EntryNode as the represented asset's entry point;
- arbitrarily nested Nodes;
- HasPart / IsPartOf;
- Full hierarchy;
- OneDown distributed hierarchy;
- OneUp parent/installation-oriented relationship;
- self-managed entities with their own AAS;
- co-managed entities without their own AAS;
- SameAs relationships across representations;
- bulk/type representations.

The IEC 81346 extension adds a second important distinction: **one physical/composite system can have multiple valid hierarchies depending on aspect**. Function, Product, Location, Type and Other views are not collapsed into one tree.

---

## 10. Capability / function / behavior organization

The metamodel separates **Capability** from **Operation**.

- Capability describes what an asset can potentially achieve, independent of implementation.
- Operation describes callable behavior with explicit input/output variables.
- The metamodel notes that a capability may be mapped to one or more implementing skills.

The Capability Description template adds:

- required versus provided capability use;
- CapabilitySet and CapabilityContainer;
- properties describing a capability;
- property and transition constraints restricting capabilities;
- skills as technical/software realizations.

This creates a clear source-native separation between:

- **what can be done**;
- **how the capability is qualified/restricted**; and
- **what implementation realizes it**.

---

## 11. Information / output organization

The AAS metamodel provides generic typed information carriers rather than an observation/product-specific output model.

Relevant structures include:

- Property / Range / MultiLanguageProperty;
- File / Blob;
- ReferenceElement;
- collections/lists;
- Operation input/output variables;
- EventPayload.

Technical Data organizes descriptive information but does not define measurement/observation results as a distinct scientific information model.

Therefore the frozen AAS lineage provides strong **general information structuring**, but no source-native observation/result partition comparable to an observation-specific model.

---

## 12. Management / condition organization

No single management/condition domain is defined by the five frozen AAS artifacts.

The metamodel enables management behavior through:

- Operations;
- Events;
- values/properties;
- relationships;
- capabilities;
- version/administrative metadata.

The selected Submodel Templates address technical data, hierarchy and capability rather than condition/maintenance as a whole. Other IDTA Submodels exist, but they are outside the frozen 182-source corpus and are not imported into this extraction.

**Evidence result:** management/condition is structurally representable in AAS but is **not a coherent source-native partition in the selected AAS corpus**.

---

## 13. Provenance / identity / reference organization

Identity and reference are foundational rather than optional add-ons.

The lineage distinguishes:

- identity of the AAS;
- identity of the represented asset;
- global and specific asset IDs;
- type/instance/batch/role asset kinds;
- self-managed versus co-managed entities;
- model references versus external references;
- semantic identifiers for concepts;
- administrative/version information;
- SameAs relationships between representations.

Technical Data also separates product classification from technical property semantics, and capability/property structures can refer to equivalent properties in other sources.

The AAS model therefore makes **identity, semantic reference and distributed resolution** cross-cutting infrastructure.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

The following distinctions are source-native and materially important:

1. **Asset vs Asset Administration Shell** — represented thing is not the representation.
2. **AAS vs Submodel** — shell identity and aspect-specific information are different levels.
3. **Submodel Template vs Submodel Instance** — reusable structure and instance content are not the same.
4. **Type asset vs instance/batch/role asset** — lifecycle/model granularity matters.
5. **Self-managed vs co-managed entity** — having a separate AAS is a meaningful management boundary.
6. **Entity/composition vs semantic relationship** — nesting alone does not express every relationship.
7. **Capability vs Operation/Skill** — potential/function and implementation/execution are different.
8. **Property vs Constraint** — descriptive value and restriction on capability are different.
9. **Product hierarchy vs Function/Location/Type aspect hierarchy** — one engineering tree is not sufficient for all viewpoints.
10. **Full vs OneDown vs OneUp hierarchy archetype** — centralized and distributed structure representations have different semantics.
11. **Technical property semantics vs presentation grouping** — TechnicalPropertyAreas may group information for readability, while individual SubmodelElements retain their own semantics.
12. **Internal asset structure vs external/use-case-specific descriptions** — not every information grouping is intrinsic composition.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely core/intrinsic:** persistent subject identity; type/instance distinction; composition/hierarchy; semantic references;
- **likely reusable structural pattern:** independently scoped aspect/domain partitions rather than one monolithic record;
- **likely cross-cutting:** capability vs implementation, reference semantics, version/administrative identity;
- **likely contextual relationship pattern:** location/install/parent views separated from product/composition views;
- **likely specialization/template pattern:** Technical Data and Capability Description structures;
- **binding/representation caution:** AAS Submodel and SubmodelElement constructs are AAS-native carriers and are not automatically V2 modules/classes.

**No V2 module disposition is made in Phase A.**

---

**C01 status: COMPLETE.**

**Next frozen lineage:** C02 — DMTF Redfish / CIM device management.

---

# C02 — DMTF Redfish / CIM device management

## Source basis and evidence ceiling

**Frozen corpus sources:** 89, 90, 91, 92, 93.

**Primary inspected sources:**

- DMTF, *Redfish Resource and Schema Guide*, DSP2046, version 2025.2, 1 May 2025:
  - `https://redfish.dmtf.org/schemas/v1/DSP2046_2025.2.html`
- DMTF, *Redfish Data Model Specification*, DSP0268, version 2025.2, used only to confirm normative schema descriptions where the informational Resource and Schema Guide summarizes them:
  - `https://redfish.dmtf.org/schemas/v1/DSP0268_2025.2.html`
- DMTF CIM Schema 2.31.0, `CIM_Battery`, class version 2.26.0:
  - `https://schemas.dmtf.org/wbem/cim-html/2.31.0/CIM_Battery.html`
- Redfish JSON schema `Battery.v1_4_0.json`:
  - `https://redfish.dmtf.org/schemas/v1/Battery.v1_4_0.json`
- Redfish JSON schema `BatteryMetrics.v1_1_0.json`:
  - `https://redfish.dmtf.org/schemas/v1/BatteryMetrics.v1_1_0.json`
- Redfish JSON schema `PowerDistribution.v1_4_0.json`:
  - `https://redfish.dmtf.org/schemas/v1/PowerDistribution.v1_4_0.json`

**Evidence note:** DSP2046 is an informational guide generated from Redfish schemas; the schema definitions are the authoritative structural source. The frozen corpus separately contains exact versioned battery/power schemas. `Battery.v1_4_0` is the Battery version introduced in the 2025.2 guide. The frozen `BatteryMetrics.v1_1_0` companion is a later exact schema revision than the `BatteryMetrics 1.0.4` shown in DSP2046 2025.2; it is therefore treated as a separately frozen companion artifact rather than silently back-projected into the May 2025 guide. `PowerDistribution.v1_4_0` likewise remains its own exact versioned companion. No later Redfish schema content is imported except where an exact frozen schema version is directly inspected.

---

## 1. Source-native structural organization

The Redfish lineage organizes management information primarily as **typed Resources connected by containment/subordination and explicit Links**, with common objects reused across those resources.

### Resource/service level

The recurring Redfish structure includes:

- resource identity and type:
  - `@odata.id`;
  - `@odata.type`;
  - `Id`;
  - `Name`;
  - `Description`;
- **Resource Collections** grouping like resources;
- **Links** for related resources that are not contained by or subordinate to the resource;
- **Actions** for available operations;
- shared objects such as:
  - Status;
  - Condition;
  - Identifier;
  - Location;
  - Redundancy;
  - Schedule.

The data model therefore distinguishes the identity of a managed resource, its contained/subordinate resources, its related resources, and actions performed on it.

### Major system/equipment partitions in DSP2046 2025.2

The guide provides several different resource boundaries rather than one universal device object:

1. **Chassis**
   - represents physical components of a system;
   - represents containers and logical zones such as racks, enclosures and chassis;
   - links subsystems outside a system's data plane, including sensors;
   - can also represent a location where equipment may be installed by using an `Absent` state.

2. **ComputerSystem**
   - represents a computer/system instance and the resources visible to software in the data plane;
   - links software-visible memory, processors, storage, interfaces and related devices/subsystems.

3. **Manager**
   - represents a systems-management entity;
   - examples include BMCs, enclosure managers and management controllers;
   - can manage Chassis, Systems, other Managers and other resource groups.

4. **Sensor**
   - represents a sensor and its properties;
   - carries a measurement/resource identity separate from the resource whose condition or metric it measures;
   - distinguishes physical, reported and synthesized implementations.

5. **AutomationNode**
   - added in Redfish release 2025.2;
   - represents a node carrying out instructions in an industrial-automation environment;
   - has separate `AutomationInstrumentation` for measurements and set points;
   - can link to Chassis and Control resources.

### Power/energy partitions in the frozen companions

6. **Battery**
   - represents an energy-storage device;
   - carries identity, location, hardware/firmware/product data, capacity, charge state, status and actions;
   - can also represent an empty installation location when Status.State is `Absent`.

7. **BatteryMetrics**
   - separately represents dynamic/derived metrics of a battery;
   - uses Sensor excerpts and `DataSourceUri` to reference the sensor resource supplying a reading.

8. **PowerDistribution**
   - represents a power-distribution component or unit;
   - has equipment identity, circuits, power-capacity data, transfer behavior, contained/associated chassis, facility and management links.

### CIM companion structure

9. **CIM_Battery**
   - is a specialization of `CIM_LogicalDevice`;
   - inherits identity, availability, status, health, enabled state, power-management and system-association semantics from the CIM class hierarchy;
   - adds battery-specific design, charge, runtime, health, lifetime and recharge semantics.

The source-native pattern is therefore **resource identity + physical/data-plane/management partitions + explicit measurement resources + subsystem-specific resources + common status/action/location/link structures**.

---

## 2. Purpose of each partition

### Resource identity / collection

Purpose: give every managed resource a typed, addressable identity and organize collections of homogeneous resource types.

### Chassis

Purpose: describe **physical containment, installation space and out-of-band physical components**. Chassis is explicitly not identical to the software-visible system/data-plane view.

### ComputerSystem

Purpose: describe the **software-visible system instance and resources accessible in its data plane**.

### Manager

Purpose: represent the **management authority/controller** responsible for managing systems, chassis or other managers.

### Sensor

Purpose: represent a **measurement source and its measurement semantics**, independently of the resource being measured.

### AutomationNode / AutomationInstrumentation

Purpose: separate an industrial-automation execution/control node from its **instrumentation, measurements and set points**.

### Battery

Purpose: represent the energy-storage component itself, including product identity, location, rated/actual characteristics, current high-level state, lifecycle-related dates and actions.

### BatteryMetrics

Purpose: isolate changing/derived battery readings from the battery's descriptive/resource identity.

### PowerDistribution

Purpose: model a complete power-distribution equipment resource, its capacity, circuits, transfer behavior and relationships to physical containers, facilities and managers.

### CIM_Battery

Purpose: model the capabilities and management of a battery as a logical device within the broader CIM managed-element hierarchy.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Common resource structure | Resource, ResourceCollection, Id, Name, @odata.id, @odata.type, Links, Actions |
| Common state/context | Status, Condition, Identifier, Location, Redundancy, Schedule |
| Physical equipment/container | Chassis, ChassisType, Assembly, physical location/bay/slot, contained components |
| Software-visible system | ComputerSystem, processors, memory, storage, interfaces, composition capability |
| Management authority | Manager, ManagerType, ManagedBy, ManagerForChassis, ManagerForServers/Systems, redundancy |
| Measurement | Sensor, Reading, ReadingType, Implementation, thresholds, calibration, physical context/subcontext |
| Automation | AutomationNode, AutomationInstrumentation, NodeState, Control/SetPoint, instrumentation links |
| Energy storage | Battery, BatteryMetrics, charge state, rated/actual capacity, state of health, discharge cycles |
| Power distribution | PowerDistribution, circuits/feeders/branches/outlets, capacity, transfer criteria/configuration |
| CIM logical-device battery | CIM_Battery, CIM_LogicalDevice, BatteryStatus, ChargingStatus, DesignCapacity, FullChargeCapacity, RemainingCapacity, HealthPercent |

---

## 4. Primary relationships

Redfish makes a structural distinction between **subordinate/contained resources** and resources reachable through `Links`.

Important source-native relationships include:

- **Chassis → physical/subordinate resources**
  - sensors, power/thermal subsystems, assemblies, bays and other physical resources can be subordinate to Chassis.

- **ComputerSystem ↔ Chassis**
  - the system's data-plane/software-visible resources and the containing physical chassis are related but not collapsed into one resource.

- **Manager → managed resources**
  - `ManagerForChassis`, system-management links and manager-to-manager relationships identify management responsibility separately from containment.

- **ManagedBy**
  - equipment resources can link to the managers responsible for managing them.

- **Sensor → measured source / excerpt use**
  - other resources use Sensor excerpts containing `DataSourceUri` and `Reading`;
  - the URI points to the source Sensor resource, preserving a distinction between embedded reading presentation and sensor identity.

- **AutomationNode → AutomationInstrumentation**
  - instrumentation is a separate linked resource;
  - instrumentation can in turn point to Sensor and Control resources.

- **Battery → Metrics**
  - Battery links to its BatteryMetrics resource.

- **Battery → Assembly / Chassis / location**
  - physical placement and assembly are explicit relationships rather than implicit from the battery's identity.

- **PowerDistribution → Chassis / Facility / Manager**
  - the exact schema uses Links to distinguish containing physical chassis, containing facility and responsible managers.

- **CIM_Battery → system/physical realization**
  - the CIM class hierarchy treats Battery as a LogicalDevice; the broader CIM model supplies associations to systems, physical packages, sensors and capabilities.

---

## 5. Dependency boundaries

The Redfish lineage has several explicit dependency layers.

### Schema/resource dependency

A Redfish Resource depends on:

- core Resource definitions;
- common objects such as Status and Location;
- schema-specific properties;
- links to other resource schemas.

A URI path or nested collection can indicate a subordinate resource relationship, while `Links` are expressly used for related resources that are not contained by or subordinate to the current resource.

### Physical vs data-plane dependency

Chassis and ComputerSystem are separate dependency domains:

- Chassis describes physical containers/components and out-of-band subsystems;
- ComputerSystem describes software-visible/data-plane resources.

The model allows health and dependencies to cross those resource hierarchies: a resource in one hierarchy can affect the health rollup of another without becoming subordinate to it.

### Management dependency

Manager is a separate management entity, and equipment/system resources can identify which managers control or manage them.

### Measurement dependency

Sensor identity is independent from metric excerpts. A BatteryMetrics or AutomationInstrumentation object can expose a reading while retaining a `DataSourceUri` to the Sensor resource that is the reading source.

### Companion-schema dependency

The frozen battery/power schemas reuse the generic Redfish Resource, Sensor, Status, Location, Assembly and link structures rather than defining their own parallel identity/state system.

---

## 6. Intrinsic vs contextual standing

Redfish does not use one global intrinsic/context flag, but the resource and link structure exposes a practical distinction.

### Strongly intrinsic to a resource

Examples include:

- model/serial/manufacturer/firmware data;
- resource-specific state;
- capacities and design characteristics;
- actions supported by that resource;
- subordinate parts/resources that the schema treats as contained.

### Contextual/relational

Examples include:

- facility containing equipment;
- manager responsible for a resource;
- related items;
- links to external/peer resources;
- location within a chassis or facility;
- power-source relationships;
- software/data-plane dependency on physical resources in another hierarchy.

### Hybrid

A Chassis can represent both an actual physical container and an **available installation location** through an absent-state resource. Similarly, Battery can represent an installed device or an empty slot/bay location. The resource identity therefore sometimes represents a **managed position/capability** as well as a currently present physical object.

---

## 7. Cross-cutting concepts

The following structures recur across many Redfish schemas:

- resource identity:
  - `@odata.id`;
  - `@odata.type`;
  - `Id`;
  - `Name`;
- Status:
  - State;
  - Health;
  - HealthRollup;
  - Conditions;
- Location;
- Actions;
- Links;
- manufacturer/model/serial/part identifiers;
- firmware/software version information;
- Oem extensions;
- metrics linked to source Sensor resources;
- related-item links;
- resource collections;
- redundancy.

These are model-wide structural conventions rather than one equipment-specific partition.

---

## 8. State / temporal / lifecycle organization

Redfish separates several kinds of change.

### Operational state

The common Status object carries resource state and health. State values distinguish conditions such as:

- Enabled;
- Disabled;
- Absent;
- Starting;
- Updating;
- Degraded;
- standby/offline conditions.

### Resource-specific state

Examples include:

- ComputerSystem PowerState and boot/progress information;
- Manager PowerState and management/security state;
- AutomationInstrumentation NodeState;
- Battery ChargeState;
- circuit/power-transfer state.

### Conditions/events

Status can carry Conditions; Redfish also has message/event/log/telemetry resources elsewhere in the same guide.

### Lifecycle/service information

Selected component schemas can carry:

- production/manufacture date;
- serviced date;
- firmware/hardware versions;
- replaceability/hot-plug information;
- lifetime/recharge/discharge counters;
- accumulated operating measures.

### CIM_Battery lifecycle/state

CIM_Battery separately distinguishes:

- design capacity;
- full-charge capacity;
- remaining capacity;
- estimated run time;
- expected life;
- recharge count;
- health percent;
- time on battery;
- enabled/operating/health states inherited from CIM.

There is no single Redfish lifecycle object that subsumes all of these; state and lifecycle semantics are distributed across common objects and resource-specific schemas.

---

## 9. Composition / topology organization

Physical and logical organization are deliberately separated.

### Physical composition

Chassis is the principal physical/container resource. It can represent:

- a complete chassis;
- enclosure;
- module/component;
- rack;
- rack group;
- pod;
- bays and installation locations;
- subsystem containers.

The 2025.2 release notes further moved some device-parent relationships toward Chassis, reinforcing Chassis as the physical parent for physical devices.

### Software-visible composition

ComputerSystem organizes resources visible to software/data plane, such as:

- processors;
- memory;
- storage;
- interfaces/controllers;
- composable resources.

### Management topology

Manager relationships express which controller manages:

- Chassis;
- ComputerSystems;
- other Managers;
- fabrics or broader managed sets.

### Automation topology

AutomationNode links execution nodes, instrumentation, control and Chassis without making those all the same resource.

### Power topology

PowerDistribution has explicit:

- feeders;
- branches;
- outlets;
- supplies;
- containing Chassis;
- Facility;
- ManagedBy relationships.

The model therefore supports **multiple overlapping topologies**—physical containment, software visibility, management control, measurement-source linkage and power distribution—rather than one universal component tree.

---

## 10. Capability / function / behavior organization

Redfish usually expresses behavior through a combination of **resource type, properties, Actions and linked functional resources**, rather than one universal Capability class.

Examples:

- ComputerSystem actions such as reset/power transitions;
- Manager actions for reset, failover, redundancy and security-mode changes;
- Battery actions including self-test and calibration;
- AutomationNode actions such as start, stop, wait, reset and trigger;
- controls and set points represented through Control/AutomationInstrumentation structures;
- Composition/Collection capability annotations for supported resource composition/creation behavior.

Resource type itself also implies functional responsibility:

- Manager manages;
- Sensor measures/reports;
- AutomationNode executes automation instructions;
- Battery stores/provides energy;
- PowerDistribution distributes power.

The source-native pattern therefore separates **what resource type a thing is**, **what state/configuration it has**, and **what actions can be invoked on it**.

---

## 11. Information / output organization

Redfish distinguishes descriptive resource state from measurement/metric data.

### Resource description

A resource commonly exposes:

- identity;
- product information;
- state;
- relationships;
- configuration;
- supported actions.

### Sensor readings

Sensor is a first-class resource. Other schemas frequently reuse **Sensor excerpts** containing a reading and `DataSourceUri` back to the source Sensor.

### Metrics resources

Resource-specific metrics are often separated from the resource itself:

- Battery → BatteryMetrics;
- PowerDistribution → PowerDistributionMetrics;
- processor/storage/power/thermal resources similarly have metrics resources elsewhere in the guide.

### Automation instrumentation

AutomationInstrumentation groups measurements and set points around an AutomationNode but can still point to independent Sensor and Control resources.

### Telemetry/events/logs

The broader 2025.2 data model also has telemetry, event and log structures, indicating that persistent resource description and time-varying output/event information are not treated as one homogeneous property set.

---

## 12. Management / condition organization

Management and condition are first-class, cross-cutting concerns.

### Management

Manager is explicitly separate from the managed system/equipment. Manager types distinguish management responsibilities such as:

- BMC;
- enclosure manager;
- rack manager;
- auxiliary/management controller;
- fabric manager;
- software-based management service.

Managed resources can identify responsible managers through links.

### Condition / health

Common Status carries:

- State;
- Health;
- HealthRollup;
- Conditions.

A resource's health rollup can include subordinate or dependent resources even when those dependencies live in another resource hierarchy.

### Component-specific condition

Battery adds:

- charge state;
- state of health;
- actual versus rated capacity;
- metrics;
- self-test/calibration behavior.

CIM_Battery adds a separate logical-device vocabulary for:

- charging/discharging/idle state;
- battery status;
- health percent;
- capacity degradation;
- remaining runtime;
- error/availability/operational status.

The frozen lineage therefore has a strong source-native **management + status/condition** organization, but it is expressed through resource relationships and common objects rather than one monolithic condition module.

---

## 13. Provenance / identity / reference organization

Redfish identity/reference is highly explicit.

### Resource identity

- `@odata.id` identifies a resource URI.
- `@odata.type` identifies schema/resource type.
- `Id` is the resource identifier within its collection.
- durable/global identifiers are available in common Identifier structures where applicable.

### Product/equipment identity

Many physical/device resources carry:

- Manufacturer;
- Model;
- SerialNumber;
- PartNumber;
- SparePartNumber;
- AssetTag;
- hardware/firmware version.

### Cross-resource reference

- `Links` relate non-subordinate resources.
- subordinate resources are reachable through resource properties/collections.
- `DataSourceUri` preserves the identity of the Sensor source behind a copied/excerpted reading.
- `RelatedItem` provides weaker association than schema-defined relationships.

### CIM identity

CIM_Battery inherits:

- DeviceID;
- InstanceID;
- SystemName;
- SystemCreationClassName;
- identifying descriptions and related managed-element identity.

The lineage therefore treats **resource identity, product identity and relationship/reference identity as separate but connected concerns**.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

The following source-native distinctions are materially important:

1. **Chassis vs ComputerSystem** — physical containment/out-of-band components are not identical to software-visible/data-plane resources.
2. **Manager vs managed resource** — management authority is distinct from the equipment/system being managed.
3. **Sensor resource vs measured resource** — the reading source is distinct from the battery, chassis, node or subsystem whose condition is being described.
4. **Resource vs Metrics resource** — persistent identity/configuration and changing measurements are deliberately separable.
5. **Contained/subordinate relationship vs Links relationship** — structural containment and external/peer association are not interchangeable.
6. **Physical presence vs managed installation location** — an `Absent` resource can represent an empty bay/slot capability without asserting a currently present device.
7. **Status.State vs Status.Health vs Condition** — operational state, health assessment and specific conditions are separate concepts.
8. **Hardware/product characteristics vs operational readings** — rated/design information is distinct from actual/live metrics.
9. **Rated capacity vs actual capacity vs remaining/stored energy** — design/maximum/current state must not be collapsed.
10. **AutomationNode vs AutomationInstrumentation vs Control/Sensor** — execution identity, instrumentation and measurement/control sources are distinct resources.
11. **PowerDistribution equipment vs Chassis/Facility/Manager** — equipment identity, physical container, site context and management responsibility are separate.
12. **Redfish resource identity vs manufacturer/product identity** — API resource IDs and durable equipment identifiers serve different purposes.
13. **CIM LogicalDevice vs physical realization** — the managed logical-device abstraction is not the same thing as the physical package that realizes it.
14. **Direct reading vs reported vs synthesized Sensor implementation** — measurement provenance/derivation affects meaning.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely core/intrinsic:** resource/equipment identity; product identifiers; physical composition; status/health; actions/behavior; persistent resource relationships;
- **likely reusable structural pattern:** separation of physical containment, software-visible system, management authority and measurement-source identity;
- **likely cross-cutting:** Status/Condition, Location, Actions, Links, metrics-source references, management responsibility;
- **likely contextual relationship pattern:** Facility/Chassis/Manager/power-source relationships separated from the resource's intrinsic identity;
- **likely specialized substructure:** battery/power distribution, automation-node instrumentation, CIM battery-management semantics;
- **likely dynamic-information pattern:** separate Metrics/Telemetry/Event resources instead of treating changing readings as ordinary static description;
- **binding/representation caution:** Redfish Resource/URI hierarchy and `Links` are Redfish-native representation mechanisms and are not automatically V2 resource classes or relationship carriers.

**No V2 module disposition is made in Phase A.**

---

**C02 status: COMPLETE.**

**Next frozen lineage:** C03 — IEEE 1451 / ISO 2145x.

---

# C03 — IEEE 1451 / ISO 2145x smart-transducer lineage

## Source basis and evidence ceiling

**Frozen primary source IDs:** 110, 114, 124.  
**Frozen companion IDs:** 109, 111–113, 115, 123, 125–131.

**Primary/current source standing:**

- IEEE 1451.0-2024, *IEEE Standard for a Smart Transducer Interface for Sensors and Actuators—Common Functions, Communication Protocols, and Transducer Electronic Data Sheet (TEDS) Formats*:
  - active IEEE standard;
  - published 26 June 2024;
  - supersedes IEEE 1451.0-2007;
  - official scope: `https://standards.ieee.org/ieee/1451.0/11001/`.
- IEEE 1451.1-1999, *Network Capable Application Processor Information Model*:
  - historical/inactive-reserved IEEE standard;
  - official scope: `https://standards.ieee.org/ieee/1451.1/2164/`.
- ISO/IEC/IEEE 21451-1:2010, *NCAP information model*:
  - published international standard;
  - confirmed in 2025;
  - explicitly an adoption of IEEE 1451.1-1999;
  - official scope: `https://www.iso.org/standard/54357.html`.

**Current public first-party evidence also inspected:**

- NIST, “IEEE 1451.0-2024 Standard Published Under Leadership of NIST Researchers,” 1 July 2024.
- NIST, “The IEEE 1451 Playground: A Web-Based Tool for Standard Education,” published 6 November 2025.
- NIST, *IEEE 1451.0-based Web of Thing (WoT) Ontology*, published 10 March 2025.
- NIST historical engineering literature on IEEE 1451 smart-transducer architecture and TEDS.

**Project evidence control:** The supplied `MERLIN_IEEE1451_TEDS_Public_Source_Technical_Reconstruction_v0.1_14OCT2026.docx` remains explicitly **INTERIM — PUBLIC-SOURCE RECONSTRUCTION — NORMATIVE VERIFICATION PENDING**. It is used here as a locator and synthesis of first-party public evidence, not as a substitute for the licensed standard.

### Evidence ceiling

The full IEEE 1451.0-2024 and ISO/IEC/IEEE 21450/21451 normative texts are not available in this environment. Therefore:

- exact current mandatory/optional TEDS status;
- exact field definitions;
- datatypes;
- cardinalities;
- conditional rules;
- conformance obligations; and
- exact current relationships among all specialized TEDS

are **not** asserted unless supported by an openly available first-party source.

The current structural architecture—APP, NCAP, TIM, network services, transducer services, TEDS, smart transducers—is directly supported by the official IEEE/NIST public record. Historical TEDS partition details are used as lineage evidence and are clearly identified as such.

---

## 1. Source-native structural organization

The IEEE 1451 lineage has two related but distinct structural eras represented in the frozen corpus.

### A. IEEE 1451.1-1999 / ISO/IEC/IEEE 21451-1:2010 NCAP information model

The 1999/2010 information-model lineage defines a **network-neutral object model** connecting processors to communication networks, sensors and actuators.

Its publicly described organization contains:

- **blocks**;
- **services**;
- **components**;
- sensor/actuator interactions;
- application code executing in the processor.

Historical IEEE/ANSI descriptions identify four principal object-model blocks:

1. **Transducer Block**
2. **Function Block**
3. **Physical Block**
4. **Network Block**

with underlying structures and services.

This is an NCAP-side information/object model rather than a generic equipment lifecycle model.

### B. IEEE 1451.0-2024 current common architecture

The official 2024 scope organizes interoperability around four principal participant classes and two service boundaries:

1. **Application (APP)**
   - 1451 client;
   - consumes network services.

2. **Network Capable Application Processor (NCAP)**
   - 1451 server;
   - provides network services to APPs;
   - accesses/controls transducer-side functions.

3. **Transducer Interface Module (TIM)**
   - module containing/serving smart transducers;
   - provides transducer-side services and TEDS/data to NCAP.

4. **Smart transducer**
   - sensor and/or actuator;
   - represented/accessed through TIM/channel structures.

### Service partitions

5. **Network services**
   - commands/replies between APP and NCAP;
   - access transducer data and TEDS through the NCAP.

6. **Transducer services**
   - commands/replies between NCAP and TIM;
   - support TIM setup/control and reading/writing transducer data.

### Self-description partition

7. **Transducer Electronic Data Sheets (TEDS)**
   - standardized electronic self-description;
   - support identification, characteristics, configuration and specialized metadata.

### Channel partition

8. **TransducerChannel**
   - the addressed logical sensing/actuation endpoint/path within the TIM architecture;
   - carries channel-specific type, data, performance, timing and related descriptive semantics.

### Current public semantic projection

The NIST-led 1451.0-based WoT work models APPs, NCAPs, TIMs and smart transducers as 1451 WoT Things and organizes their web description into:

- identification/context;
- behaviors;
- properties/data schema;
- security;
- time synchronization;
- protocol bindings.

This projection is not the IEEE normative architecture itself, but it is first-party evidence that the current IEEE concepts are separable into reusable semantic partitions rather than being inseparable from one wire encoding.

---

## 2. Purpose of each partition

### APP

Purpose: application-side consumer/client of standardized IEEE 1451 network services.

### NCAP

Purpose: network-capable processor/server that mediates between applications/network services and smart-transducer/TIM services.

### TIM

Purpose: transducer-side module that groups smart transducer functionality and supports standardized access/control/data/TEDS interactions through the NCAP.

### TransducerChannel

Purpose: identify and describe an individually addressable sensing or actuation channel/path within a TIM, including channel-specific data and performance characteristics.

### Network services

Purpose: standardize APP-to-NCAP access to transducer data and TEDS.

### Transducer services

Purpose: standardize NCAP-to-TIM setup, control, and data read/write interactions.

### TEDS

Purpose: supply machine-readable self-description and metadata so a smart transducer/module/channel can identify and describe itself and support plug-and-play integration.

### NCAP object-model blocks (1999/2010)

Purpose: separate network, physical, transducer and application/function concerns within the network-capable processor information model.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Application/network side | APP, client, NCAP/server, network services, commands/replies, APIs |
| Transducer side | TIM, smart transducer, sensor, actuator, TransducerChannel |
| Transducer interaction | transducer services, setup/control, read/write data, service messages |
| Self-description | TEDS, identity, metadata, channel description, calibration/performance descriptions |
| Historical NCAP object model | Transducer Block, Function Block, Physical Block, Network Block, services/components |
| Channel characterization | channel type, physical units, operating limits/range, uncertainty, sampling/timing, self-test, data representation, calibration linkage |
| Grouping/context | TIM identity, channel count, control/vector grouping, proxy/group relationships where supported |
| Specialized TEDS lineage | calibration, frequency response, names/identification, application-specific/extensions; current 2024 exact partition/optionality remains access-gated |

---

## 4. Primary relationships

The principal architecture is relational rather than a flat device record.

### APP ↔ NCAP

- APP is a 1451 client.
- NCAP is a 1451 server.
- APP accesses transducer data/TEDS through **network services** exposed by NCAP.

### NCAP ↔ TIM

- NCAP communicates with TIM through **transducer services**.
- services support TIM setup/control and reading/writing transducer data.

### TIM ↔ TransducerChannels

- a TIM may contain/support multiple TransducerChannels;
- Meta-TEDS lineage includes the number/grouping of channels;
- channels can participate in control/vector/group structures.

### TransducerChannel ↔ physical transducer

- a channel represents the addressable sensing/actuation endpoint/path;
- it is related to a physical sensor/actuator but is **not automatically identical to the physical transducer**.

### TEDS ↔ described subject

TEDS structures describe different scopes in the lineage:

- TIM/shared/module context;
- individual transducer channel;
- calibration/performance;
- human-readable/identification/application-specific information;
- specialized communication/security/timing information where applicable.

### NCAP information-model blocks

The older NCAP model relates physical/network/transducer/function blocks through services/components rather than reducing all responsibilities to one block.

---

## 5. Dependency boundaries

The IEEE 1451 family deliberately separates several dependency layers.

### Application/network dependency

APPs depend on NCAP network services, not directly on transducer-interface details.

### NCAP/transducer dependency

NCAP mediates access to TIMs and their channels; TIM implementation is not the APP-facing application interface.

### Common family layer vs physical-interface family members

IEEE 1451.0 supplies common functions, services and TEDS semantics for the family, while other family standards specialize physical/wireless/mixed-mode interfaces.

The public 2008 NIST architecture explicitly describes IEEE 1451.x physical-interface modules beneath the common 1451.0 services.

### TEDS vs runtime data

TEDS describes the transducer/module/channel; runtime transducer data is accessed through services. Self-description and measurement/control exchange are therefore separate responsibilities.

### Current vs historical lineage

ISO/IEC/IEEE 21451-1:2010 is explicitly an adoption of IEEE 1451.1-1999, so the two are one conceptual NCAP lineage rather than independent architecture votes.

IEEE 1451.0-2024 is a materially revised/current common-family architecture and must not silently inherit every 2007/2010 field or mandatory/optional rule.

---

## 6. Intrinsic vs contextual standing

The IEEE 1451 architecture centers on information intrinsic to a smart-transducer network interface, but several contextual layers are distinguishable.

### Strongly intrinsic to TIM/channel/transducer description

- identity/self-description;
- channel type;
- physical units;
- design/operating range;
- uncertainty;
- data representation;
- sampling/timing characteristics;
- self-test support;
- calibration linkage;
- frequency-response/performance metadata where supported.

### Interface/contextual

- APP/NCAP client-server role;
- network binding/protocol;
- physical-interface family;
- security framework;
- time-synchronization framework;
- geographic location metadata;
- grouping/proxy relationships.

### External to the IEEE 1451 core equipment description

The public evidence does not establish a whole deployment, maintenance organization, host-platform, mission, or enterprise asset model comparable to broader whole-system frameworks. Those may be represented by consuming systems but are not the central architecture of IEEE 1451.

---

## 7. Cross-cutting concepts

The following span multiple IEEE 1451 partitions:

- universally unique identification / self-identification;
- TEDS access;
- command/reply service pattern;
- client/server roles;
- timing;
- security;
- grouping;
- calibration;
- self-test/diagnostics;
- transducer type/direction;
- protocol binding.

The current IEEE public scope also treats APIs as cross-boundary mechanisms for both network and transducer services.

---

## 8. State / temporal / lifecycle organization

IEEE 1451 has rich **operational and timing semantics**, but the frozen/public evidence does not expose one unified equipment-lifecycle model.

### Operational state/interaction

Public lineage evidence supports:

- initialization/discovery;
- TIM announcements;
- setup/control;
- data read/write;
- alerts;
- self-test;
- service commands/replies.

### Timing

The public 2024 Playground reconstruction exposes distinct channel timing concepts such as:

- sampling period;
- update time;
- setup/read/write timing;
- warm-up/read delay;
- self-test timing;
- sample-time source;
- propagation/trigger timing and uncertainty.

Exact 2024 field definitions remain access-gated.

### Calibration

Calibration TEDS lineage distinguishes calibration coefficients/model information from the live transducer result. Historical/public evidence supports self-calibration and calibration metadata, but not a complete maintenance-event history.

### Lifecycle

TEDS self-description can support installation, diagnostics, maintenance and replacement by providing machine-readable identity/calibration information, but **service history and asset lifecycle are not organized as a first-class lifecycle partition in the frozen IEEE 1451 lineage**.

---

## 9. Composition / topology organization

IEEE 1451 supplies a strong **interface topology**, but it is not a general physical bill of materials.

### Primary topology

`APP → NCAP → TIM → TransducerChannel → transducer interaction/data`

### TIM/channel composition

A TIM can support multiple channels/sensors/actuators.

Historical/public descriptions also associate a TIM with:

- transducers;
- signal conversion/processing electronics;
- TEDS;
- a 1451.x communication module.

### Group topology

Current public reconstruction indicates channel-level grouping concepts such as:

- ControlGroup;
- VectorGroup;
- geographic-location vector grouping;
- proxy-channel relationships.

These are functional/logical groupings, not automatically physical containment.

### Network topology

NCAP provides network access to one or more TIMs through family-specific communication/physical interfaces.

The IEEE 1451 topology therefore distinguishes **network hierarchy, module grouping, channel addressing and physical transducer realization**.

---

## 10. Capability / function / behavior organization

IEEE 1451 distributes capability semantics across channel metadata and services rather than using one generic Capability class.

### Channel capability/performance

Public current evidence exposes candidate concepts for:

- sensor vs actuator/channel direction/type;
- design operating range;
- multi-range behavior;
- data model/representation;
- sampling;
- uncertainty;
- self-test;
- event behavior;
- frequency response;
- timing.

### Behavior

Network and transducer services define:

- data access;
- TEDS access;
- setup;
- control;
- read/write behavior.

### Function vs implementation

The same channel/service semantics can operate over different physical-interface family members, which is a source-native separation between **common transducer function** and **physical communication realization**.

---

## 11. Information / output organization

The IEEE 1451 lineage distinguishes at least three information classes.

### 1. TEDS/self-description

Persistent/descriptive metadata about:

- TIM;
- channel;
- identity;
- calibration;
- performance;
- interface/specialized metadata.

### 2. Runtime transducer data

Sensor readings or actuator data exchanged through standardized services.

### 3. Service messages

Commands/replies for:

- network services;
- transducer services;
- setup/control;
- metadata access.

Public lineage material also distinguishes data representation/dataset organization from the physical quantity/channel description itself.

TEDS is therefore **not the measurement output**; it describes the transducer/channel and how its data should be understood/accessed.

---

## 12. Management / condition organization

IEEE 1451 provides **device/interface management functions**, but not a whole enterprise equipment-management domain.

Source-supported management concerns include:

- discovery/announcement;
- self-identification;
- setup/control;
- TEDS management/access;
- self-test;
- self-diagnosis;
- self-calibration;
- alert notification;
- security;
- time synchronization;
- interface configuration.

The NCAP is also a management/mediation point between application clients and transducer modules.

However, the frozen/public lineage does not organize:

- work orders;
- repair history;
- maintenance organization;
- inventory lifecycle;
- persistent operational deployment history

as a comparable first-class domain.

---

## 13. Provenance / identity / reference organization

Identity and self-description are central IEEE 1451 concerns.

### Identity

Current first-party public evidence supports:

- UUID/global identity in the 2024 architecture;
- self-identification through TEDS;
- TIM/channel identification;
- manufacturer/device/serial information in the TEDS lineage.

### Description/reference

TEDS binds descriptive information to the relevant module/channel/transducer scope.

Historical TEDS organization distinguishes shared/module information from channel-specific information and application/extension/calibration information.

### Source traceability

Runtime data can be associated with a particular TIM/channel because the architecture addresses channels through the NCAP/TIM hierarchy.

The model therefore provides strong **native source identity at the transducer/channel boundary**, though it does not supply a general enterprise provenance graph.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

The following distinctions are fundamental to the lineage:

1. **APP vs NCAP** — application client and network-capable server are different roles.
2. **NCAP vs TIM** — network/application mediation and transducer-interface module are distinct architectural subjects.
3. **TIM vs TransducerChannel** — module/grouping boundary and individually addressable channel are different levels.
4. **TransducerChannel vs physical transducer** — a logical/addressable channel is not automatically identical to a physical sensor/actuator.
5. **Sensor vs actuator direction/role** — sensing and actuation are distinct transducer behaviors even when shared infrastructure is used.
6. **TEDS vs runtime transducer data** — self-description is not the measured/commanded data stream.
7. **Meta/shared TIM description vs channel-specific description** — module-level and channel-level metadata scopes must remain distinct.
8. **Calibration/performance metadata vs live output** — descriptive transformation/performance information is not an observation result.
9. **Network services vs transducer services** — APP↔NCAP and NCAP↔TIM service boundaries are different.
10. **Common 1451.0 semantics vs family-specific physical interfaces** — common domain/service semantics are not the same as the transport/PHY realization.
11. **Object-model block roles in 1451.1/21451-1** — transducer, function, physical and network blocks should not be flattened into one processor/device record.
12. **Current 1451.0-2024 semantics vs legacy 2007/2010 exact structures** — lineage continuity does not permit silent normative inheritance.
13. **Identification/grouping vs physical containment** — channel/vector/control groupings are not necessarily equipment-parent relationships.
14. **Security/time synchronization metadata vs application-domain security/time governance** — interface-specific concerns should not be silently generalized.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely core/intrinsic:** explicit transducer/channel identity; separation of module and channel; quantitative channel characteristics; timing/sampling; calibration/performance metadata;
- **likely reusable structural pattern:** layered application/network processor/transducer-module/channel organization;
- **likely cross-cutting:** self-description, UUID/source identity, self-test, calibration, timing, security and service semantics;
- **likely composition/topology pattern:** TIM contains/supports multiple channels, while logical channel groupings remain distinct from physical containment;
- **likely dynamic-information pattern:** runtime transducer data separated from TEDS/self-description and service-command messages;
- **likely specialization:** IEEE 1451-native network/transducer services and family-specific physical interfaces;
- **evidence ceiling:** exact 1451.0-2024 TEDS definitions, optionality, cardinalities and conformance obligations remain pending normative access;
- **binding/representation caution:** TEDS byte/TLV formats and IEEE service protocols are native IEEE realizations and are not automatically V2/OGC carriers.

**No V2 module disposition is made in Phase A.**

---

**C03 status: COMPLETE.**

**Next frozen lineage:** C04 — Integrated Sensor Architecture (ISA).

---

# C04 — Integrated Sensor Architecture (ISA)

## Source basis and evidence ceiling

**Frozen primary source IDs:** 37, 42.  
**Frozen companion IDs:** 28, 35, 36, 38–41, 43–45.

**Controlling source-native artifacts inspected:**

- PEO IEW&S, *Integrated Sensor Architecture (ISA): Data Model Specification*, Release 6.0, document revision 12, 31 October 2023.
- PEO IEW&S, *Integrated Sensor Architecture (ISA): Software Design Document*, Document 6.0, revision 5, 31 October 2023.

**Companion evidence used only to clarify the controlling structure:**

- *ISA Component Requirements*, 6.0r4.
- *ISA Controller Requirements*, 6.0r4.
- *ISA Interface Control Document*, 6.0r5.
- *ISA Introductory Guide*, 6.0r2.
- other frozen ISA guidance/artifacts in the lineage.

**Evidence note:** The project contains the complete Distribution A ISA 6.0 documents. This extraction stays centered on what ISA itself structures and standardizes. It does not treat the earlier MERLIN ISA assessment as independent authority and does not turn ISA interface behaviors into V2 truths.

---

## 1. Source-native structural organization

ISA separates its model into several interacting structural layers.

### A. System architecture

The Software Design Document defines:

1. **ISA Component**
   - a component that complies with the ISA interface and supports required ISA capabilities/behaviors.

2. **ISA Controller**
   - an ISA Component that supplies the core ISA services.

3. **ISA Composition**
   - a collection of components that interoperates with a broader ISA network through a single ISA Component.

4. **Composition Interface Component (CIC)**
   - the ISA Component representing/accessing the composition to the broader ISA network.

5. **Composition Member**
   - a component contained in the composition other than the CIC;
   - may or may not itself be an ISA Component.

6. **ISA Network**
   - a virtual network of interconnected ISA Components;
   - relies on physical wired/wireless networks but is conceptually distinct from them.

### B. Service architecture

ISA 6.0 defines three core services:

- **Communication Service**
- **Authorization Service**
- **Live Data Service**

and allows optional services.

The Communication Service is the keystone entry point for ISA communications and manages registration/configuration/status/request behaviors.

### C. Capability architecture

The DMS/SDD defines **ISA capability** as one of:

- **Property**
- **Observable**
- **Command**

The complete set of declarations supported by a component is the:

- **Component Capability Description (CCD)**

The DMS further defines:

- Capability Declaration;
- Property Declaration;
- Observable Declaration;
- Command Declaration;
- Parameter Declaration;
- Result Declaration;
- Threshold/Range/Structure declarations;
- Custom Type declarations.

### D. Message architecture

The DMS defines distinct ISA messages:

- Administrative;
- Config;
- Event;
- Registration;
- Request;
- Response;
- Status.

These are carried inside an Envelope/Header structure.

### E. Reporting/data architecture

The DMS separately defines a large set of:

- Properties;
- Observables;
- Commands;
- reporting data types;
- common primitive/composite data types;
- modality-specific data types.

Examples span identity, position, relationship, power, status, sensor settings, detections, chemical/radiological information, imagery-related data and more.

### F. Deployment architecture

The SDD defines distributed deployment of Controllers and Components across tactical platforms and interconnected ISA networks.

### G. Lifecycle architecture

ISA defines explicit **communication lifecycle phases**:

1. Connection
2. Registration
3. Configuration
4. Operational
5. Deregistration

This is a lifecycle of ISA network participation, not an asset-service lifecycle.

---

## 2. Purpose of each partition

### ISA Component

Purpose: provide a common interoperable participant abstraction for networked devices, algorithms, adapters, user-facing systems and other integrating systems.

### ISA Composition

Purpose: expose a complex system or a collection of subcomponents through a single ISA-facing component while allowing different levels of visibility and mediation for internal members.

### CIC

Purpose: provide the composition's external ISA access point and mediate capabilities, data and tasking between the wider network and internal members.

### ISA Network

Purpose: define the virtual interoperability fabric through which components discover, report, publish, subscribe and task one another.

### Core Services

Purpose:
- Communication Service: connectivity, registration, configuration management, status, availability, discovery/request handling;
- Authorization Service: determine whether requested actions are permitted;
- Live Data Service: support subscriptions/live data dissemination.

### Capability declarations

Purpose: advertise **what a component can report or do** before/independently of a particular live value or execution.

### Properties

Purpose: represent state information **about the component itself**.

### Observables

Purpose: declare information about **observations made by the component**.

### Commands

Purpose: declare tasks/actions that the component can execute upon request.

### Messages

Purpose: distinguish operational interactions:
- component/network administration;
- configuration/capability declaration;
- observation publication;
- registration;
- task/property requests;
- execution responses;
- periodic/current status.

### Lifecycle phases

Purpose: control the component's progression from connection through participation/configuration to operational use and eventual deregistration.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Participation identity | ISA Component, UCI/identifier, ISA Controller |
| Composition | ISA Composition, CIC, composition member, virtual ISA component |
| Network | ISA Network, ISA interface, connections, client/server roles |
| Services | Communication Service, Authorization Service, Live Data Service, optional services |
| Capability | Capability Declaration, CCD, Property Declaration, Observable Declaration, Command Declaration, Custom Type Declaration |
| Capability state | ready state, reporting state, property/observable/command state |
| Messages | Administrative, Config, Event, Registration, Request, Response, Status |
| Reporting/data | Properties, Observables, Commands, Reporting data types, modality-specific values |
| Deployment | Controllers/components distributed on tactical platforms and interconnected across networks |
| Lifecycle | Connection, Registration, Configuration, Operational, Deregistration |
| History/query | Discover, History, subscriptions, message retrieval/query |
| Relationship/context | Relationship property, position, owner/program/support contacts, resource descriptors |

---

## 4. Primary relationships

ISA makes several relationship types explicit.

### Component ↔ Controller

- a non-Controller ISA Component connects to an ISA Controller;
- the Controller accepts connections and supplies core services;
- Controllers may interconnect with other Controllers.

### Composition ↔ CIC ↔ members

- an ISA Composition exposes itself to the broader ISA network through a CIC;
- members may communicate with the CIC through ISA or native interfaces;
- member capabilities may be represented individually or aggregated at the CIC.

### Visibility relationship

A composition member may be:

- **visible** — announced and independently represented;
- **opaque** — not announced; exposed capability appears to belong to the CIC;
- **virtual ISA component** — a non-ISA member presented externally as though it were an ISA Component;
- **transparent** — visible and externally taskable through the CIC;
- **translucent** — visible but not directly taskable from outside.

This is a source-native distinction between **physical/internal membership** and **external representation/visibility**.

### Component ↔ capability

A Component's CCD declares its:

- Properties;
- Observables;
- Commands;
- custom types.

### Declaration ↔ current state/value

Declarations define capability support. Config carries declarations and ready/reporting states. Status carries property values. Event carries observable values. Request/Response realizes commands and property queries.

### Component ↔ relationship/context

The DMS includes a `Relationship` property described as the physical relationship between a device and other devices, useful for deriving absolute position/orientation when mounted to another platform.

### Component ↔ resources

A component may expose Resource Descriptors for accessible media/streams generated by it.

---

## 5. Dependency boundaries

ISA has unusually explicit dependency layering.

### Domain content vs interface

The **ISA interface** is defined by:

- protocols/security technologies/encodings in the ICD;
- message content in the DMS.

Thus the semantic/message model and wire/presentation model are separate documents.

### Component vs service

Components provide/use services; services are not identical to Components.

### Capability declaration vs execution/reporting

A capability can be declared before it is ready, currently reporting, or actually executed/published.

### Composition vs member visibility

Internal composition does not force external resource visibility. The CIC decides whether member identity/capability is exposed, mediated or hidden.

### ISA network vs physical network

The ISA network is a **virtual network** relying on existing physical networks. Network membership must not be equated with physical network topology.

### Deployment vs component identity

Controllers/components are deployed on tactical platforms for availability/fault-tolerance reasons; platform placement is contextual to the component's ISA identity.

---

## 6. Intrinsic vs contextual standing

ISA mixes device/component state and network context, but source-native partitions make the distinction visible.

### Intrinsic to a component's ISA-facing description

- UCI/identifier;
- declared capabilities;
- current property state;
- current readiness/reporting state;
- supported commands;
- supported observables;
- component-specific configuration;
- manufacturer/model/serial/hardware/software information where reported;
- operational properties such as position/power/mode.

### Contextual/relational

- network membership;
- connected Controller;
- deployment/platform placement;
- ownership/support/program contacts;
- physical relationship to another device/platform;
- composition visibility and mediation through CIC;
- subscription/query relationships;
- authorization context.

### Representation-dependent

- whether an internal member is visible, opaque, virtual, transparent or translucent;
- whether a capability is presented as belonging to the member or to the CIC.

This is not intrinsic physical truth; it is an interoperability-presentation choice.

---

## 7. Cross-cutting concepts

The following span multiple ISA partitions:

- UCI/source identity;
- time and stale time;
- priority;
- capability declaration;
- ready state;
- reporting state;
- component availability;
- authorization;
- configuration;
- queries/subscriptions;
- ownership/support metadata;
- physical relationship and position;
- custom data types.

Every message carries common metadata such as source, identifier, timing and priority.

---

## 8. State / temporal / lifecycle organization

ISA has two distinct state structures.

### A. ISA participation lifecycle

The SDD explicitly defines:

1. **Connection**
   - establish secure connection/presentation format with Controller.

2. **Registration**
   - become a participant in the ISA network.

3. **Configuration**
   - declare capabilities to the network.

4. **Operational**
   - publish/subscribe/discover/task/execute/report while periodically sending status.

5. **Deregistration**
   - end network participation.

This lifecycle is message/connection oriented.

### B. Component state

Capabilities have:

- ready state;
- reporting state where applicable.

Properties carry current component state values.

Status messages periodically communicate those values.

Availability monitoring uses expected status reporting to determine component availability and can trigger re-registration/deregistration behavior.

### Temporal message semantics

ISA messages can carry:

- time;
- stale time;
- history query before/after windows;
- periodic reporting intervals.

### Distinction

**Participation lifecycle is not the same as equipment lifecycle.** ISA does not make service/repair/installation history the same thing as registration/configuration state.

---

## 9. Composition / topology organization

ISA provides one of the strongest source-native distinctions between **composition topology** and **network topology**.

### Composition topology

An ISA Composition contains:

- one CIC;
- zero or more composition members.

Members can be:

- native ISA Components;
- non-ISA components reached through native interfaces;
- visible/opaque;
- transparent/translucent;
- virtualized as ISA Components.

Composition-level capabilities can be synthesized from multiple member capabilities.

### Network topology

An ISA Network is a set of interconnected ISA Components using Controllers/services.

Multiple Controllers can be interconnected to expand access across platforms.

### Deployment topology

Controllers may be distributed across tactical platforms for resilience and local access.

### Physical relationship

The DMS separately permits a physical `Relationship` property among devices/platforms.

These structures must not be collapsed:

- physical containment;
- ISA composition;
- ISA network membership;
- tactical deployment;
- external visibility

are different source-native relationships.

---

## 10. Capability / function / behavior organization

ISA defines capability unusually explicitly.

### Capability categories

A CCD contains declarations for:

1. **Properties**
   - state information the component can report about itself.

2. **Observables**
   - information the component can publish about observations it makes.

3. **Commands**
   - tasks the component can execute upon request.

4. **Custom data types**
   - component-defined structures built from ISA types.

### Declarations

The DMS separately defines:

- ranges;
- structures;
- thresholds;
- fields;
- parameters;
- command results;
- mutability;
- reporting constraints.

### Capability state

A declared capability can be:

- ready/not ready;
- reporting/not reporting where relevant.

### Behavior realization

Commands are invoked through Request and reported through Response.

Observables are published through Event messages.

Properties are reported through Status or queried through requests.

Thus ISA preserves a four-way distinction:

> **declared capability → current capability state → live value/output → invoked behavior/result**

---

## 11. Information / output organization

ISA explicitly separates several information flows.

### Configuration/self-description

**Config** messages carry:

- CCD;
- property/observable/command states;
- additional configuration data.

### Component state

**Status** messages carry current values of declared properties.

### Observation output

**Event** messages publish declared observables.

### Command interaction

**Request** invokes commands or queries properties.

**Response** reports command execution state/result.

### Administrative/network information

**Administrative** messages report network/device connection changes and noteworthy network events.

**Registration** messages control network participation.

### Historical/query information

The DMS includes:
- `Discover` for current components/capabilities/state/property values;
- `History` for querying previously published ISA messages;
- live-data subscription mechanisms.

This is a strong source-native separation among **description, state, observation, command, administration and history**.

---

## 12. Management / condition organization

ISA management is first-class but primarily focused on interoperability/operation.

### Configuration management

Communication Service exchanges:

- capability declarations;
- readiness/reporting state;
- configuration changes.

### Status management

Periodic Status reporting communicates component properties.

### Availability management

Controller monitors ongoing availability and responds to missed status/registration behavior.

### Authorization

Authorization Service evaluates permission for commands/actions.

### Discovery

Components/capabilities can be queried and discovered.

### Condition data

The DMS contains numerous properties representing:

- Built-In Test result;
- power state;
- temperature;
- reserve capacity;
- receive/transmit power/data rate;
- quality;
- readiness/health-like operational status.

ISA therefore carries condition/operational state strongly, but it does **not** define a full maintenance/service/work-order lifecycle comparable to an asset-management model.

---

## 13. Provenance / identity / reference organization

Identity is foundational to ISA messaging.

### UCI

A Unique Component Identifier (UCI) identifies ISA Components.

Messages cite:

- source;
- subject/about component(s);
- target/destination as applicable.

### Virtual-component identity

A virtual ISA Component's identifier incorporates/associates it with its CIC.

This preserves the distinction between:

- externally represented component identity;
- mediating CIC identity.

### Product identity

The DMS includes manufacturer/model/serial/version properties and describes manufacturer+model+serial as an expected globally unique equipment triplet where applicable.

### Message identity/history

Messages have conversation/message identifiers and timestamps.

History/query mechanisms preserve references to past messages/results.

ISA therefore combines:

- component identity;
- product/equipment identity;
- message/source identity;
- virtual/mediated identity

without treating them as interchangeable.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

The following ISA distinctions are structurally important:

1. **ISA Component vs physical device/system** — a Component is an ISA interface participant and can be software, adapter, controller or virtualized representation.
2. **ISA Composition vs ISA Network** — internal integration boundary and interoperability network are different structures.
3. **CIC vs composition member** — access/mediation responsibility is not the same as member identity.
4. **Physical member vs virtual ISA Component** — external representation can differ from physical/native implementation.
5. **Visible vs opaque member** — existence/identity exposure is independent of internal composition.
6. **Transparent vs translucent member** — visibility and taskability are different.
7. **Member capability vs composition-level capability** — the CIC can expose synthesized/aggregate capability.
8. **Property vs Observable vs Command** — component state, observation output and executable task are distinct capability kinds.
9. **Capability declaration vs capability state** — support and current readiness/reporting are different.
10. **Capability state vs live value** — readiness does not equal current property/observation content.
11. **Config vs Status vs Event vs Request/Response** — description, state, observation and task interaction are different message responsibilities.
12. **ISA participation lifecycle vs equipment lifecycle** — connect/register/configure/operate/deregister is not maintenance/deployment/service history.
13. **ISA Network vs physical network** — virtual interoperability topology and physical communications topology are distinct.
14. **Deployment/platform placement vs component identity** — co-location on a platform does not make the platform the Component.
15. **Message/source identity vs manufacturer/product identity** — protocol identity and durable equipment identity serve different functions.
16. **Physical relationship vs interface composition** — being mounted to a platform is not the same as being represented behind a CIC.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely core/intrinsic:** explicit separation of system/component identity, capability declarations, current state, observable output and executable commands;
- **likely reusable structural pattern:** composition with mediated/virtual member visibility;
- **likely cross-cutting:** capability readiness/reporting state, authorization, discovery, availability, message provenance/time;
- **likely contextual relationship pattern:** network participation, platform deployment, ownership/support, physical relationship;
- **likely dynamic-information pattern:** Config/Status/Event/Request/Response separation plus History/Discover;
- **likely management pattern:** explicit interoperability lifecycle and availability/configuration management;
- **likely topology pattern:** composition topology, network topology and deployment topology remain distinct;
- **binding/representation caution:** UCI, ISA messages, CIC visibility states and ISA services are ISA-native architecture/interface constructs and are not automatically V2 resources or conformance requirements.

**No V2 module disposition is made in Phase A.**

---

**C04 status: COMPLETE.**

**Next frozen lineage:** C05 — ISO/IEC 29182 Sensor Network Reference Architecture (SNRA).

---

# C05 — ISO/IEC 29182 Sensor Network Reference Architecture (SNRA)

## Source basis and evidence ceiling

**Frozen primary source IDs:** 116, 118, 120.  
**Frozen companion IDs:** 117, 119, 121, 122.

**Primary source basis:**

- ISO/IEC 29182-1:2013, *Sensor Network Reference Architecture (SNRA) — Part 1: General overview and requirements*.
- ISO/IEC 29182-3:2014, *SNRA — Part 3: Reference architecture views*.
- ISO/IEC 29182-4:2013, *SNRA — Part 4: Entity models*.

**Companion lineage:**

- Part 2 Vocabulary and terminology;
- Part 5 Interface definitions;
- Part 6 Applications;
- Part 7 Interoperability guidelines.

**Evidence ceiling:** Official ISO scopes for Parts 1, 3 and 4 are available. A publisher preview of Part 4 was inspected through its overview and beginning of the physical-entity section, including the table of contents, physical/functional entity overview, functional-layer diagram, and physical-to-functional association table. The full normative texts of Parts 1, 3 and 4 were not available locally. Therefore this extraction records the explicit high-level structure and previewed entity organization without inventing lower-level definitions from unavailable clauses.

---

## 1. Source-native structural organization

SNRA organizes the sensor-network domain through **multiple architectural viewpoints** and an explicit split between **physical entities** and **functional entities**.

### A. Architecture viewpoints

Part 3 defines architecture views spanning:

- business;
- operational;
- systems;
- technical perspectives;

expressed through functional, logical and/or physical views where applicable.

### B. Physical entities

Part 4's source-native physical entity classes include:

- **sensor nodes**;
- **gateways**;
- **other networks**;
- **service providers**;
- **users**.

The sensor-node physical structure includes hardware/device/component entities such as:

- sensors;
- actuators;
- communications module;
- processor;
- memory;
- power supply.

The preview explicitly treats a sensor node and the sensors within it as physical entities. Actuators can be associated with a sensor node without necessarily residing physically inside it.

### C. Functional entities

Part 4 organizes functions into five major areas:

1. **Sensor node hardware layer**
   - data acquisition;
   - actuation;
   - power generation / energy harvesting.

2. **Basic functions layer**
   - data processing;
   - data communications;
   - data storage;
   - hardware drivers;
   - sensor/actuator identification.

3. **Service layer**
   - common services such as:
     - communications support;
     - self-localization;
     - service/resource discovery;
     - data management;
     - code management;
     - time synchronization;
     - group management/clustering;
   - domain-specific services.

4. **Application layer**
   - applications;
   - software agents;
   - rules engines;
   - collaborative information processing.

5. **Cross-layer management**
   - device management;
   - resource management;
   - service management;
   - network management;
   - security management;
   - privacy management;
   - safety management;
   - business management;
   - quality-of-service management;
   - system monitoring.

### D. Physical-functional association

SNRA does not require each function to belong to exactly one physical component. The entity model explicitly associates functional entities with one or more physical entity types.

The overall source-native pattern is therefore:

> **network architecture viewpoints + physical entities + layered functional entities + many-to-many physical/function realization relationships + interfaces**

---

## 2. Purpose of each partition

### Architecture viewpoints

Purpose: allow the same sensor network to be understood from stakeholder/business, operational, system and technical perspectives instead of forcing all concerns into one representation.

### Physical entities

Purpose: identify the tangible hardware/devices/components and larger participating actors that form the deployed sensor-network environment.

### Sensor node

Purpose: supply a bounded physical network element containing at least the sensing/hardware functionality required for the node, with optional processing, communications, power and actuation capabilities.

### Functional entities

Purpose: represent **tasks/roles**, not hardware. A functional entity can be implemented on one or more kinds of physical entity.

### Functional layers

Purpose: partition functional responsibility by level:

- interaction with sensing/actuation hardware;
- foundational processing/communications/storage;
- reusable/common/domain services;
- applications and collaborative processing;
- management spanning layers.

### Interfaces

Part 5's source role is to define interfaces:

- between functional layers;
- between entities enabling sensor-network services/applications.

Thus entity structure and interface structure remain distinct responsibilities.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Network whole | Sensor network, sensor node, gateway, other network, service provider, user |
| Sensor-node physical structure | Sensor, actuator, communications module, processor, memory, power supply |
| Hardware functions | Data acquisition, actuation, power generation/energy harvesting |
| Basic functions | Data processing, communications, storage, hardware drivers, sensor/actuator identification |
| Common services | Communications support, self-localization, discovery, data/code management, time synchronization, group management |
| Domain services | Domain-specific services |
| Application functions | Application, software agent, rules engine, collaborative information processing |
| Management | Device, resource, service, network, security, privacy, safety, business, QoS management, system monitoring |
| Architecture viewpoints | Business, operational, systems, technical; functional/logical/physical views |
| Interface structure | Inter-layer service access and entity-to-entity interfaces |

---

## 4. Primary relationships

SNRA's strongest relationship pattern is **realization/association between function and physical entity**.

### Physical containment/association

- sensor node contains/uses physical sub-entities;
- sensors are physical entities within a sensor node;
- actuators can be associated with the node without necessarily being physically contained in it;
- gateways connect sensor-network and broader network/service contexts.

### Functional realization

A functional entity may be carried out by one or more physical entity types.

Examples in the source include:

- data acquisition realized by sensors;
- collaborative processing distributed across nodes/service providers/users;
- communications, processing, storage and management functions realized across multiple physical entities.

### Network connectivity

Physical entities are connected into the sensor-network architecture.

### Layer/service relationship

Part 5 distinguishes interfaces between functional layers from interfaces between physical/architectural entities.

The source therefore separates:

- **is physically part of / connected to**;
- **performs or realizes a function**;
- **uses/provides a service/interface**.

---

## 5. Dependency boundaries

SNRA distributes responsibilities across the series.

### Part 1

Defines general characteristics/requirements and overall organization.

### Part 2

Provides terminology/vocabulary.

### Part 3

Provides architecture viewpoints.

### Part 4

Provides physical and functional entity models.

### Part 5

Defines interfaces among entities and functional layers.

### Part 6

Describes application structures/use cases.

### Part 7

Provides interoperability principles/guidelines.

This series structure is itself semantically significant: **entity identity, functional responsibility, interface, application and interoperability guidance are separate artifacts**.

Within Part 4:

- physical entities do not imply one fixed functional allocation;
- functional entities depend on physical entities for realization but remain conceptually distinct;
- cross-layer management spans rather than sits inside one functional layer.

---

## 6. Intrinsic vs contextual standing

SNRA is primarily a **network architecture**, so its intrinsic/context boundary differs from an individual-equipment model.

### Intrinsic to the sensor-node physical entity

Potentially intrinsic:

- sensors;
- communications module;
- processor;
- memory;
- power supply;
- associated actuation where implemented as part of the node.

### Contextual to an individual sensor node but intrinsic to the sensor network

- gateway;
- access/backbone network;
- service provider;
- user;
- peer nodes;
- network-wide services.

### Functional/contextual

A function such as collaborative processing, group management or network management may span multiple physical entities and therefore cannot be assumed intrinsic to one device.

This is an important source-native distinction between:

> **what belongs to the physical node** and **what the node participates in functionally as part of a network**.

---

## 7. Cross-cutting concepts

Cross-layer management is explicitly cross-cutting.

SNRA's management functions include:

- device management;
- resource management;
- service management;
- network management;
- security management;
- privacy management;
- safety management;
- business management;
- QoS management;
- system monitoring.

Other cross-cutting concepts include:

- time synchronization;
- discovery;
- group management/clustering;
- identification;
- communication support.

The architecture viewpoints are also cross-cutting because a single entity/function can appear differently in business, operational, system and technical views.

---

## 8. State / temporal / lifecycle organization

The inspected SNRA material does **not** expose a single source-native lifecycle-state model for a sensor node.

Temporal/state-related concerns appear through functions such as:

- system monitoring;
- device/resource/network management;
- time synchronization;
- service discovery;
- code management;
- group management.

Part 1 supplies general requirements, and Part 6 addresses applications, but the available evidence does not justify inventing a deployment/maintenance lifecycle structure.

**Evidence result:** state/lifecycle is present as distributed management/monitoring/time functions rather than one explicit equipment-lifecycle partition in the inspected SNRA material.

---

## 9. Composition / topology organization

SNRA has two simultaneous topology models.

### Physical topology

A sensor network contains connected physical entities such as:

- sensor nodes;
- gateways;
- other/access/backbone networks;
- service-provider/user-side physical resources.

A sensor node itself contains multiple physical sub-entities.

### Functional topology

The same network is decomposed into layered functional entities, including cross-layer management.

### Physical-functional mapping

Table 1 explicitly maps which physical entity types can realize which functional entities.

This means **function topology and hardware topology are not isomorphic**.

One function can span several physical entities, and one physical entity can implement several functions.

---

## 10. Capability / function / behavior organization

SNRA's functional entity model is directly capability/function oriented.

The Part 4 overview states that a detailed entity model can include:

- input-output relationship for what the entity does;
- features characterizing capability;
- implementation taxonomy.

This gives a source-native structural pattern:

> **function/role → inputs/outputs → capability characteristics → implementation alternatives**

The architecture further distinguishes:

- sensing/data acquisition;
- actuation;
- processing;
- communications;
- storage;
- service functions;
- applications;
- management.

Capability is therefore organized primarily through **functional entities and their realizations**, not a single capability list attached to every physical object.

---

## 11. Information / output organization

SNRA's inspected material organizes information flow functionally rather than as a detailed observation schema.

Relevant partitions include:

- data acquisition;
- data processing;
- data communications;
- data storage;
- data management;
- collaborative information processing;
- applications.

The source therefore distinguishes:

- obtaining data;
- processing data;
- moving data;
- storing/managing data;
- using/fusing data in applications.

The available evidence does not define a detailed observation/result object model comparable to OMS; it defines the **architectural functions that create and move information**.

---

## 12. Management / condition organization

Management is one of SNRA's most explicit structural areas.

**Cross-layer management** contains separate management functions for:

- device;
- resource;
- service;
- network;
- security;
- privacy;
- safety;
- business;
- QoS;
- system monitoring.

This is notable because management is not placed inside the sensor-node hardware layer or application layer. It is intentionally modeled as **cross-layer responsibility**.

The available preview does not establish detailed condition/health data structures, but it clearly establishes management/system-monitoring as a distinct source-native semantic area.

---

## 13. Provenance / identity / reference organization

The inspected SNRA material contains less explicit identity/provenance structure than several other lineages.

Source-native identity-related functions include:

- sensor/actuator identification;
- service/resource discovery;
- self-localization;
- group management/clustering.

Physical entities are distinguished by their architectural role/type.

However, the available evidence does not establish:

- durable asset identity;
- manufacturer/product identity;
- provenance graphs;
- detailed source-history records.

**Evidence result:** identity/discovery/localization are present functionally; full equipment/provenance identity is not a dominant structural partition in the inspected material.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

The following SNRA distinctions are source-native and important:

1. **Sensor network vs sensor node** — the network aggregate and individual node are different architecture levels.
2. **Physical entity vs functional entity** — hardware/device/component and task/role must not be conflated.
3. **Sensor node vs sensor** — a node can contain multiple physical sub-entities; sensor is not synonymous with the whole node.
4. **Associated actuator vs physically contained actuator** — functional association does not prove physical containment.
5. **Physical topology vs functional topology** — hardware structure and functional allocation are independent.
6. **Function vs implementation** — a functional entity can be implemented on multiple physical entity types.
7. **Hardware/basic/service/application layers** — acquisition, foundational processing, reusable service and application responsibilities are distinct.
8. **Cross-layer management vs ordinary service/application function** — management intentionally spans layers.
9. **Common service vs domain-specific service** — reusable platform-level functions and application-domain functions are distinct.
10. **Architecture viewpoint vs modeled entity** — business/operational/system/technical views are viewpoints, not separate real-world objects.
11. **Entity model vs interface definition** — what entities/functions are and how they interact are distinct standardization responsibilities.
12. **Network identity vs individual-equipment identity** — architecture membership does not collapse all nodes/gateways into one System.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely core/intrinsic:** explicit physical sub-entity structure for sensors/communications/processing/memory/power within a node;
- **likely reusable structural pattern:** physical-entity vs functional-entity separation;
- **likely functional pattern:** layered acquisition/processing/communications/storage/services/application structure;
- **likely cross-cutting:** management, monitoring, synchronization, discovery and grouping;
- **likely contextual relationship pattern:** gateway/network/service-provider/user context outside an individual node;
- **likely topology pattern:** physical and functional topologies mapped many-to-many rather than collapsed;
- **likely specialization:** network-wide clustering/collaborative processing structures for distributed sensing;
- **evidence ceiling:** detailed Part 3/4 entity models beyond the public preview and exact normative interface requirements remain unavailable;
- **binding/representation caution:** SNRA functional layers and entity diagrams are architecture abstractions, not automatically V2 modules, classes or API resources.

**No V2 module disposition is made in Phase A.**

---

**C05 status: COMPLETE.**

**Next frozen lineage:** C06 — Matter.

---

# C06 — Matter 1.3

## Source basis and evidence ceiling

**Frozen primary source ID:** 107.

**Primary source:**
- Connectivity Standards Alliance, *Matter Core Specification*, Release 1.3, April 17, 2024.
- Connectivity Standards Alliance, *Matter Device Library Specification*, Release 1.3 / 1.3.0.1, April 17 / May 29, 2024, used to inspect the source-native Device Type and endpoint-composition rules referenced by the Core specification.

**Evidence note:** The exact Matter Core 1.3 PDF in the frozen corpus is large enough that direct page retrieval was limited in the available web environment. The exact Device Library 1.3 PDF was directly inspected, including the Root Node, sensor Device Types, endpoint composition, and Room Air Conditioner composition example. Core-model structural statements are limited to the published Matter R1.3 material and source-linked specification extracts; no later Matter release is silently substituted.

---

## 1. Source-native structural organization

Matter organizes a node's application data model hierarchically:

1. **Node**
   - the addressable Matter participant;
   - contains one or more Endpoints;
   - Endpoint 0 is the Root Node endpoint.

2. **Endpoint**
   - an individually addressable functional partition on a Node;
   - carries one or more Device Types and Cluster instances;
   - can be a leaf endpoint or participate in composed-device structures.

3. **Device Type**
   - identifies the functional classification and conformance requirements of an Endpoint;
   - Device Types define required/optional Clusters, elements, conditions, and in some cases required child Device Types.

4. **Cluster**
   - modular functional/data-model building block instantiated on an Endpoint;
   - exposes a coherent feature/interface such as sensing, control, configuration, identification, power, or diagnostics.

5. **Cluster elements**
   - **Attributes** — readable/writable state/data;
   - **Commands** — requestable actions;
   - **Events** — reported occurrences/history-like event information.

6. **Descriptor Cluster**
   - describes an Endpoint's Device Types and composition;
   - `DeviceTypeList` identifies the Device Types implemented on the Endpoint;
   - `PartsList` identifies child Endpoints that form a composed Device Type;
   - `TagList` supplies semantic tags used to disambiguate otherwise similar child Endpoints.

7. **Root Node**
   - a utility Device Type on Endpoint 0;
   - its PartsList covers the other Endpoints on the Node.

8. **Composed Device Types**
   - a Device Type can be represented by a parent Endpoint plus child Endpoints supplying additional capabilities/parts;
   - child Endpoints can themselves carry different Device Types and Clusters.

9. **Fabric**
   - the secure logical/administrative network context in which Nodes participate;
   - Node identity and interaction occur within Fabric scope.

The source-native anatomy is therefore:

> **Node → Endpoint → Device Type + Cluster → Attribute / Command / Event**, with **Descriptor/PartsList/TagList** providing composition and semantic disambiguation.

---

## 2. Purpose of each partition

### Node

Purpose: provide the network-addressable Matter participant boundary that hosts the complete Matter data model exposed by one commissioned node.

### Root Node / Endpoint 0

Purpose: expose Node-level utility/servicing information and identify the complete Endpoint family on the Node.

### Endpoint

Purpose: partition a Node into separately addressable units of functionality. An Endpoint can represent one Device Type instance or a parent/child position in a composed Device.

### Device Type

Purpose: state **what functional kind of device/role an Endpoint represents** and define conformance requirements over Clusters, elements and composition.

### Cluster

Purpose: package one coherent functional interface/data-model concern into a reusable building block.

### Attribute

Purpose: represent persistent/current data or state exposed by a Cluster.

### Command

Purpose: represent requestable behavior/actions of a Cluster.

### Event

Purpose: report occurrences that consumers may subscribe to or retrieve through the interaction model.

### Descriptor Cluster

Purpose: make endpoint structure self-describing:
- what Device Types an Endpoint implements;
- what child Endpoints compose it;
- semantic tags distinguishing repeated similar children.

### Fabric

Purpose: provide secure logical membership/administrative context for Nodes and scoped interactions; Fabric is not the physical composition boundary of the device.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Node level | Node, Node ID, Root Node, Fabric membership |
| Functional partition | Endpoint, Endpoint ID, leaf/composed endpoint |
| Functional classification | Device Type, DeviceTypeList, Device Type class/scope/superset |
| Composition | PartsList, parent Endpoint, child Endpoint, composed Device Type |
| Functional interface | Cluster, client/server role, Cluster requirements, Features |
| State/data | Attribute |
| Behavior | Command |
| Occurrence | Event |
| Semantic disambiguation | Descriptor Cluster, TagList, semantic tags |
| Utility/maintenance | Root Node utility Clusters, Basic Information, diagnostics/update/power source Device Types |
| Device specialization | sensor Device Types, controllers, actuators, appliances, energy devices and others |

---

## 4. Primary relationships

### Node → Endpoint

A Node contains/addressably exposes multiple Endpoints.

### Endpoint → Device Type

An Endpoint's Descriptor `DeviceTypeList` identifies one or more Device Types implemented on that Endpoint.

### Endpoint → Cluster

The Device Type's conformance requirements determine the Clusters an Endpoint shall/may implement.

### Cluster → Attribute / Command / Event

Clusters contain the data, actions and occurrences that make up the functional interface.

### Parent Endpoint → child Endpoints

A composed Device Type uses Descriptor `PartsList` to identify child Endpoints forming part of the composed device representation.

### Child Endpoint → semantic tag

`TagList` can distinguish repeated child Device Types according to semantic role/location.

### Client Cluster ↔ Server Cluster

Matter interactions are generally between Cluster roles on Endpoints/Nodes. Client/server role is an interaction relationship, not physical containment.

### Node ↔ Fabric

A Node participates in one or more Fabric contexts for secure identity/access/interaction.

---

## 5. Dependency boundaries

Matter makes several important structural dependencies explicit.

### Device Type depends on Cluster definitions

Device Types do not redefine all behavior/data. They compose/restrict reusable Cluster definitions and specify conformance.

### Endpoint composition depends on Descriptor

Composition is made explicit through Descriptor `PartsList`, rather than inferred from Endpoint numbering or Cluster co-location.

### Semantic disambiguation depends on TagList

If multiple child Endpoints share the same Device Type, semantic tags can identify their distinct roles.

### Node-level utility vs application functionality

Endpoint 0 / Root Node carries Node-wide utility/servicing responsibilities, while application Device Types occupy other Endpoints.

### Fabric/network vs device data model

Fabric controls secure network membership and scope; it does not define physical product composition.

### Device Library vs Core/System Model

The Device Library defines concrete Device Type conformance while relying on the Core/System Model for Node, Endpoint, Cluster and composition semantics.

---

## 6. Intrinsic vs contextual standing

### Intrinsic to the Matter-exposed Node

- Endpoints;
- Device Types;
- Clusters;
- supported features;
- Attributes;
- Commands;
- Events;
- Descriptor composition metadata;
- Node-level utility information.

### Contextual

- Fabric membership;
- group/binding relationships to other Nodes/Endpoints;
- commissioning/access-control context;
- remote target relationships;
- ecosystem-specific controller relationships.

### Representation caution

An Endpoint is a Matter functional/addressable partition. It is **not automatically one physical component**. A physical product may expose several Endpoints, and a composed Device Type may use several child Endpoints to represent one product/function.

---

## 7. Cross-cutting concepts

Cross-cutting Matter structures include:

- Descriptor/DeviceTypeList/PartsList/TagList;
- Features/FeatureMap;
- conformance conditions;
- client/server Cluster roles;
- access control;
- fabric scoping;
- identification;
- diagnostics;
- software update;
- power source;
- groups/scenes;
- binding;
- semantic tags.

These structures can apply across many Device Types without defining the primary device function themselves.

---

## 8. State / temporal / lifecycle organization

Matter's principal lifecycle concepts are **network/commissioning and operational state**, not a full physical-asset lifecycle.

### Network/administrative lifecycle

The Core architecture includes concepts such as:

- commissioning;
- Fabric membership;
- operational credentials;
- software update;
- Node/fabric administration.

### Operational state

Clusters and Device Types expose:
- state Attributes;
- operational-state Clusters for applicable device classes;
- modes;
- errors;
- configuration;
- diagnostic information.

### Events

Cluster Events capture/report occurrences and can be subscribed to through Matter interactions.

### Lifecycle limit

The frozen Matter source does not provide a universal maintenance/service/history model for all equipment comparable to an asset-lifecycle standard. Product/service history is not a single core anatomy partition.

---

## 9. Composition / topology organization

Matter has a strong **functional composition topology**.

### Node family

Endpoint 0 Root Node's PartsList identifies all other Endpoints on the Node.

### Composed Device Type

A parent Endpoint can represent a composed device and list child Endpoints as parts.

The R1.3 Device Library Room Air Conditioner example demonstrates:

- Endpoint 0 = Root Node;
- Endpoint 1 = Room Air Conditioner parent Endpoint;
- Endpoints 2 and 3 = Temperature Sensor child Endpoints;
- parent PartsList = child sensor Endpoints;
- semantic tags distinguish indoor and outdoor temperature-sensor roles.

This is explicitly a source-native **composed device** representation.

### Important limit

Endpoint composition is **not equivalent to a physical bill of materials**. Endpoints represent functional/addressable units and Device Types. A child Endpoint may correspond to a physical component, logical function, application component, or some combination depending on the Device Type architecture.

### Network topology

Fabric and binding/group relationships connect Nodes/Endpoints for interaction and control. These relationships are distinct from Endpoint composition.

---

## 10. Capability / function / behavior organization

Matter distributes capability across Device Types and Clusters.

### Device Type

Device Type identifies the overall functional role of an Endpoint and specifies which Clusters/features are required or optional.

### Cluster

Cluster is the reusable unit of functional behavior/data.

### Features

A Cluster's FeatureMap declares optional functional features.

### Attributes

Expose state/configuration/data.

### Commands

Expose callable behavior.

### Events

Expose reportable occurrences.

### Composition

Additional child Device Types can add capabilities to a composed product.

The source-native capability model is therefore:

> **Device Type role + required/optional Cluster set + Cluster Features + Attributes/Commands/Events + optional composed child Device Types.**

---

## 11. Information / output organization

Matter clearly distinguishes three cluster-level information/interaction forms.

### Attributes

Current/persistent data and state values accessed through read/write interactions and subscriptions.

### Events

Occurrence records emitted by Cluster instances and available through event/subscription interactions.

### Commands

Request/response interaction for actions.

### Device/endpoint description

Descriptor Cluster carries static/self-descriptive structural information.

### Measurement

Sensor Device Types use measurement Clusters to publish measured values as Attributes and related Events where defined.

The model therefore does not collapse **description, state/measurement, event, and action** into one generic property list.

---

## 12. Management / condition organization

Matter has substantial device/Node management, but it is distributed among utility Clusters/Device Types.

Management-oriented structures include:

- Root Node;
- Basic Information;
- Descriptor;
- commissioning;
- access control;
- Operational Credentials;
- Network Commissioning;
- General Commissioning;
- diagnostics;
- OTA software update;
- Power Source;
- time synchronization;
- localization/user labels;
- Device Energy Management.

Condition/error information appears through:

- operational state Clusters;
- diagnostic Clusters;
- device-specific status Attributes;
- Events;
- mode/error semantics.

There is no single generic management/condition partition containing all of these; management is modularized through utility Clusters and Device Types.

---

## 13. Provenance / identity / reference organization

Matter distinguishes several identities.

### Network identity

A Node receives/uses Node identity within Fabric context.

### Endpoint identity

Endpoints are numbered/addressable within the Node.

### Device Type identity

Device Type IDs classify an Endpoint's functional role.

### Cluster/element identity

Clusters, Attributes, Commands and Events each have standardized IDs.

### Semantic reference

TagList/semantic tags can qualify the role/location of otherwise identical Device Types.

### Product identity

Basic Information and related utility Clusters provide product/vendor/software/hardware identification at Node level.

### Cross-node reference

Bindings/groups reference remote Node/Endpoint/Cluster targets for interaction.

These identities serve different purposes and should not be collapsed.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Node vs Endpoint** — network participant and addressable functional partition are different levels.
2. **Endpoint vs physical component** — Endpoint is a data-model/functional boundary, not automatically a hardware part.
3. **Device Type vs Cluster** — functional classification and reusable functional interface are distinct.
4. **Cluster vs Attribute/Command/Event** — interface grouping and individual data/behavior/occurrence elements are different.
5. **Attribute vs Event vs Command** — state/data, occurrence, and action are distinct interaction semantics.
6. **Root Node vs application Endpoint** — Node-wide utility identity and application functionality are separate.
7. **Composed Device Type vs Node** — one product/function can be represented as a parent Endpoint with child Endpoints inside a larger Node.
8. **PartsList composition vs network Binding** — internal endpoint composition and remote interaction relationship are different.
9. **PartsList vs physical BOM** — functional composition does not prove physical containment.
10. **DeviceTypeList vs TagList** — class/type and semantic role/location are different.
11. **Repeated same Device Type vs distinct semantic role** — identical child types may require disambiguation.
12. **Fabric membership vs physical/device composition** — secure network context is not the equipment hierarchy.
13. **Client vs server Cluster role** — interaction direction/role is independent of physical ownership.
14. **Feature support vs Device Type identity** — optional functional features do not create a new Device Type automatically.
15. **Conformance condition vs live state** — what an implementation is required/allowed to support is not the current runtime value.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely reusable structural pattern:** hierarchy of whole participant → addressable functional unit → functional type → reusable behavior/data interface;
- **likely composition pattern:** explicit parent/child composition with semantic disambiguation of repeated child roles;
- **likely core/intrinsic:** separate description, state/measurement, action and event semantics;
- **likely cross-cutting:** semantic tags, identity layers, conformance/features, diagnostics, software/update and power-management utilities;
- **likely contextual relationship pattern:** Fabric, Binding, Groups and remote interaction separate from intrinsic composition;
- **likely specialization pattern:** sensor Device Types and measurement Clusters as reusable modality-specific/phenomenon-specific functional units;
- **binding/representation caution:** Matter Node/Endpoint/Cluster are Matter protocol/data-model constructs and are not automatically V2 Systems/components/modules;
- **composition caution:** Matter `PartsList` is endpoint composition, not proof of physical equipment containment.

**No V2 module disposition is made in Phase A.**

---

**C06 status: COMPLETE.**

**Next frozen lineage:** C07 — MIMOSA.

---

# C07 — MIMOSA

## Source basis and evidence ceiling

**Frozen primary source IDs:** 99, 100, 101.  
**Frozen companion ID:** 102.

**Primary inspected sources:**

- MIMOSA, *CCOM UML Class Model*, Version 4.1.0 / 4.1.0-RC1 package:
  - official release page identifies 4.1.0-RC1, release date 20 March 2020, Release Candidate;
  - class-model PDF generated 27 June 2018 and marked Version 4.1.0 Proposed.
- MIMOSA, *OSA-CBM*:
  - official MIMOSA architecture description;
  - official MIMOSA presentation material used to inspect the six CBM functional blocks and relationship to OSA-EAI.
- MIMOSA, *OSA-EAI*:
  - official MIMOSA description of the enterprise asset-information exchange/storage architecture.
- MIMOSA OIIE Scenario 11, *Publish Asset Removal/Installation Events from MMS to O&M*.

**Evidence note:** CCOM 4.1.0-RC1 is a Release Candidate, not a final adopted 4.1.0 release. The frozen bibliography inherited an earlier 2018 date from the generated UML artifact; the official MIMOSA release page identifies 20 March 2020 as the RC1 release date. This extraction preserves both provenance facts. OSA-EAI 3.2.3a and OSA-CBM 3.3.1 are separate MIMOSA specifications; their concepts are not silently treated as if they were classes in CCOM 4.1.0.

---

## 1. Source-native structural organization

The MIMOSA lineage contains three complementary organizations.

### A. CCOM — Common Conceptual Object Model

The CCOM 4.1.0 diagram set is explicitly divided into source-native subject diagrams:

1. Core Types
2. Core
3. Attribute Sets
4. Registry
5. Registry Configuration
6. Logistic Resources
7. Agents
8. Measurement Locations
9. Networks
10. Network Connections
11. Functions
12. Engineering Studies
13. Ordered Lists
14. Signal Processing Setups
15. Algorithms
16. State Regions
17. Measurements
18. Tests
19. Triggered State Regions
20. Events
21. Event Relationships
22. Geospatial Tracking
23. Ambiguity Sets
24. Health and Prognostic Assessments
25. Recommendations
26. Solution Packages
27. Requests
28. Work Management
29. Completed Work
30. Documents

This is already a strong source-native anatomy rather than one flat Asset record.

### B. OSA-CBM — condition-based-maintenance functional architecture

OSA-CBM standardizes six functional blocks:

1. **Data Acquisition**
2. **Data Manipulation**
3. **State Detection**
4. **Health Assessment**
5. **Prognostic Assessment**
6. **Advisory Generation**

The architecture specifies information exchanged and interfaces among the blocks while leaving internal algorithms proprietary.

### C. OSA-EAI — enterprise asset information integration

OSA-EAI organizes exchange/storage around broad physical-asset information areas including:

- asset registry;
- condition;
- reliability;
- maintenance/work;
- configuration;
- operational measurements/alarms;
- diagnostics/prognostics/health assessment;
- physical-asset tracking;
- model/reliability information;
- work/resources;
- calibration/configuration management.

OSA-EAI uses a layered architecture so components can be used independently and provides exchange plus relational storage models.

### D. OIIE lifecycle scenario

Scenario 11 explicitly organizes a configuration-change event around:

- serialized Asset;
- functional location;
- installation/removal event;
- timestamp;
- optional responsible agent;
- optional work order.

The overall lineage therefore combines:

> **persistent asset registry + configuration/location relationships + measurements/events + condition/assessment + recommendations/work + functional CBM processing + enterprise exchange/storage**

---

## 2. Purpose of each partition

### Core / Core Types / Attribute Sets

Purpose: provide common identity, typing, values, units, source, naming and reusable attribute/property structures.

### Registry

Purpose: represent durable equipment/asset identity and reference structures:

- Asset;
- AssetType;
- Model;
- ModelRevision;
- ModelVariant;
- Manufacturer;
- Site;
- Segment;
- SegmentType;
- Organization;
- component relationships.

### Registry Configuration

Purpose: represent changes to the registered asset configuration and lifecycle status through events such as:

- AssetSegmentEvent;
- AssetModelEvent;
- AssetOwnerEvent;
- lifecycle-status structures.

### Logistic Resources / Agents

Purpose: describe human/organizational/material resources that participate in asset operations and work.

### Measurement Locations / Measurements / Tests

Purpose: distinguish:

- where/what is measured;
- the source/transducer;
- measurement setup;
- measurement result;
- tests/samples;
- association of measurements to Asset or Segment at measurement time.

### Networks / Network Connections

Purpose: model connectivity/network structures separately from physical asset registry.

### Functions / Algorithms / Signal Processing Setups

Purpose: represent functional/processing structures independently of equipment identity.

### State Regions / Triggered State Regions

Purpose: model state/threshold/condition regions and transitions associated with measurements/events.

### Events / Event Relationships

Purpose: represent actual, hypothetical and proposed events, time and relationships among events.

### Geospatial Tracking

Purpose: track asset/location relationships over time.

### Health and Prognostic Assessments

Purpose: represent evaluated health and remaining-life assessments independently from the measurements/events that substantiate them.

### Recommendations / Solution Packages / Requests

Purpose: move from assessment to recommended/desired action and structured requests/solutions.

### Work Management / Completed Work

Purpose: represent planned and executed work, resources, causes/effects and work results.

### OSA-CBM functional blocks

Purpose: partition the information-processing chain from raw acquisition through advisory/decision support.

### OSA-EAI

Purpose: integrate the otherwise separated registry, condition, reliability, maintenance and operational information across enterprise applications.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Registry | Asset, AssetType, Model, ModelRevision, ModelVariant, Manufacturer, Segment, SegmentType, Site, Organization, AssetComponent, SegmentComponent |
| Registry configuration | AssetSegmentEvent, AssetModelEvent, AssetOwnerEvent, LifecycleStatus, LifecycleStatusHistory |
| Common identity/properties | Entity, Nameable, InfoSource, Attribute/Property, AttributeSet, UnitOfMeasure |
| Agents/resources | Agent, Organization, Material/LogisticResource, roles |
| Measurement | MeasurementLocation, MeasurementSource, MeasurementAssociation, Measurement, transducer, setup |
| Tests | Test, TestGroup, TestComponent, Sample |
| Functions/processing | Function, Algorithm, SignalProcessSetup, Vector/FFT/waveform setup |
| State/condition | StateRegion, TriggeredStateRegion, threshold/condition structures |
| Events | Event, ActualEvent, HypotheticalEvent, ProposedEvent, TimestampedEvent, EventLink |
| Health | Assessment, HealthAssessment, RemainingLifeAssessment, HealthLevelType, ChangePatternType |
| Recommendations/work | Recommendation, SolutionPackage, Request, Work, CalendaredWork, CompletedWork |
| Location/topology | Segment, Site, geospatial tracking, networks/connections |
| OSA-CBM | Data Acquisition, Data Manipulation, State Detection, Health Assessment, Prognostic Assessment, Advisory Generation |
| OSA-EAI | Registry, condition, reliability, maintenance/work, tracking, operational data, diagnostic/prognostic information |

---

## 4. Primary relationships

MIMOSA uses explicit relationships to preserve continuity across different information concerns.

### Asset ↔ Model / AssetType

A serialized Asset is distinguished from the reusable Model/ModelRevision/ModelVariant and AssetType that characterize it.

### Asset ↔ components

AssetComponent provides parent/child asset relationships.

### Segment ↔ components / Site

Segment represents a functional/location-oriented structure and can have SegmentComponents and Site relationships.

### Asset ↔ Segment over time

AssetSegmentEvent records changing association between a serialized Asset and a Segment.

Scenario 11 uses the same pattern concretely as Asset installation/removal at a functional location.

### Asset ↔ Model over time

AssetModelEvent records model association/change separately from Asset identity.

### Asset ↔ Owner over time

AssetOwnerEvent records ownership-related configuration/change.

### Measurement ↔ Asset or Segment

MeasurementAssociation is explicitly designed so a measurement can record:

- the currently installed serialized Asset for a Segment-based measurement location; or
- the Segment in which an Asset-based measurement location was located

at the time of measurement.

### Assessment ↔ subject/evidence

HealthAssessment / RemainingLifeAssessment relate to Asset/Segment and can be substantiated by Events/measurements.

### Recommendation ↔ assessment/event

Recommendations can derive from HealthAssessment or Event.

### Work ↔ resources/events/results

Work/CompletedWork relate resources used/consumed, causes/effects and resulting Events.

---

## 5. Dependency boundaries

The MIMOSA lineage makes several layer boundaries explicit.

### CCOM vs OSA-EAI

CCOM is the conceptual information model. OSA-EAI database/XML/service artifacts derive from common conceptual structures but add exchange/storage technology.

### CCOM vs OSA-CBM

OSA-CBM is a functional condition-monitoring architecture. It uses many OSA-EAI data elements and is intended to map into OSA-EAI, but its six processing blocks are not the same thing as CCOM subject classes.

### Asset registry vs current configuration

Persistent Asset identity/model information is distinct from configuration-change Events such as installation/removal/model/owner events.

### Measurement vs assessment

Measurements provide evidence; Health/RemainingLife Assessment is an interpretation/evaluation over evidence.

### Assessment vs recommendation vs work

Assessment, advice, requested/planned work and completed work are separate semantic stages.

### Segment/location vs Asset

A functional location/Segment can persist while different serialized Assets are installed/removed over time.

---

## 6. Intrinsic vs contextual standing

### Strongly intrinsic to persistent Asset identity

- serialized Asset;
- AssetType;
- manufacturer/model/revision/variant;
- component relationships;
- selected persistent properties.

### Contextual/configurational

- installation on a Segment/functional location;
- ownership;
- site;
- current readiness/lifecycle status;
- geospatial location;
- network relationship;
- responsible agent/organization.

### Evidence/operational

- measurements;
- tests;
- events;
- state regions;
- alarms.

### Interpretive/derived

- HealthAssessment;
- RemainingLifeAssessment;
- recommendations;
- prognostic outputs.

### Process/work context

- requests;
- work orders;
- calendared work;
- completed work;
- logistic resources.

MIMOSA therefore strongly separates **the persistent equipment subject** from **its changing context, evidence, evaluations and actions**.

---

## 7. Cross-cutting concepts

Cross-cutting structures include:

- Entity identity/UUID;
- Nameable;
- InfoSource;
- units/value types;
- Attribute/Property/AttributeSet;
- EffectiveStatus and effective dates;
- Event/time;
- Agent/role;
- Documents;
- data quality;
- ordered lists;
- source/evidence relationships.

These are reused across registry, measurement, assessment and work structures.

---

## 8. State / temporal / lifecycle organization

MIMOSA has one of the richest explicit time/lifecycle organizations in the frozen anatomy population.

### Persistent identity with changing configuration

Asset identity persists while:

- Segment/location association changes;
- Model association changes;
- ownership changes;
- lifecycle/readiness status changes.

### Lifecycle status

CCOM includes:

- LifecycleStatus;
- LifecycleStatusType;
- LifecycleStatusHistory;
- effective/start dates.

### Event model

Events can be:

- Actual;
- Hypothetical;
- Proposed;
- Timestamped;
- linked to one another.

### Installation/removal

OIIE Scenario 11 explicitly binds:

- serialized Asset;
- functional location;
- install/remove Event;
- event time;
- agent/work context.

### Condition/prognostic time

RemainingLifeAssessment projects future condition; HealthAssessment evaluates current condition. OSA-CBM explicitly progresses from current data/state into future prognosis and advisory.

### Work time

CalendaredWork and CompletedWork distinguish planned from performed work.

This lineage therefore separates:

> **persistent equipment identity → configuration/status history → observed events/evidence → current assessment → future prognosis → recommendation/work**

without treating those as the same record.

---

## 9. Composition / topology organization

MIMOSA supports multiple structural topologies.

### Asset composition

AssetComponent defines parent/child structure among Assets.

### Functional/location structure

Segment and SegmentComponent define a separate functional/location hierarchy.

### Site organization

Sites contain/register relevant structures and locations.

### Model hierarchy

Models have:

- ModelRevision;
- ModelVariant;
- parent/child relationships.

### Network topology

Networks and NetworkConnections are modeled separately from Asset/Segment hierarchy.

### Measurement topology

MeasurementLocation and MeasurementAssociation connect sensing/measurement points to Asset or Segment context.

### Key source-native distinction

**Asset composition is not the same as functional-location/Segment hierarchy.**

Scenario 11 depends on this separation: the same functional location can receive/remove different serialized assets while retaining its own identity.

---

## 10. Capability / function / behavior organization

MIMOSA organizes function/capability across several structures rather than one generic Capability class.

### Functions

The CCOM Functions diagram provides explicit functional entities separate from Asset identity.

### Algorithms / signal processing

Algorithm and SignalProcessSetup structures represent data-processing methods/configurations.

### OSA-CBM

Function is strongly organized into six processing stages:

1. Data Acquisition
2. Data Manipulation
3. State Detection
4. Health Assessment
5. Prognostic Assessment
6. Advisory Generation

OSA-CBM specifies:

- data;
- configuration;
- explanation;
- interfaces

for these levels while leaving proprietary algorithms internal.

### Capability forecasting

OSA-EAI's broader information scope includes forecasting/projection information.

The source-native pattern separates:

- **equipment identity**;
- **functional/processing role**;
- **implementation algorithm**;
- **derived assessment/advice**.

---

## 11. Information / output organization

MIMOSA separates information classes according to meaning and processing stage.

### Registry information

Persistent asset/model/site/segment identity and configuration.

### Measurement data

- scalar/single data;
- time waveform;
- FFT;
- CPB;
- samples/tests;
- signal-processing setup;
- measurement source/location/association.

### Event data

Actual/proposed/hypothetical events and relationships.

### State/condition information

State regions and threshold/triggered-state structures.

### Assessments

Health and remaining-life evaluations.

### Recommendations

Recommended actions with priority/evidence relationships.

### Work information

Requests, planned work, completed work and resources.

### OSA-CBM information flow

Data is progressively transformed from acquisition to manipulation/state detection/assessment/prognosis/advisory, with interfaces carrying data/configuration/explanation.

This is a strong source-native distinction between **raw/processed evidence, interpreted condition, forecast, advice and action**.

---

## 12. Management / condition organization

Management and condition are central to the lineage.

### Registry/configuration management

- Asset registry;
- Model/AssetType;
- component configuration;
- install/remove events;
- model/owner changes;
- lifecycle/readiness status.

### Condition monitoring

OSA-CBM and CCOM structures support:

- acquisition;
- state detection;
- alarms;
- tests;
- condition evidence.

### Diagnostics/health

HealthAssessment represents current evaluated condition with health level/confidence and supporting evidence.

### Prognostics

RemainingLifeAssessment represents future-state/remaining-life evaluation with estimate/error/confidence.

### Recommendations

Recommendation structures link assessments/events to advised actions.

### Maintenance/work

Requests, Work, CalendaredWork and CompletedWork model the planning/execution side rather than collapsing it into health status.

OSA-EAI explicitly integrates registry, condition, reliability and maintenance information across applications.

---

## 13. Provenance / identity / reference organization

MIMOSA uses persistent identity and source/evidence relationships throughout.

### Entity identity

CCOM Entity provides UUID and information-source identity fields.

### Asset identity

Serialized Asset is separate from:

- AssetType;
- Model;
- ModelRevision;
- ModelVariant.

### InfoSource

Information source is explicitly represented and can register entities.

### Temporal provenance

Created/LastEdited/effective-time/event-time structures support temporal traceability.

### Assessment provenance

Health/remaining-life assessments can be substantiated by Event/evidence and associated with responsible AgentRole and data quality.

### Work/event provenance

Completed work has causes/effects/resources and resulting events.

### OIIE exchange

Scenario 11 preserves Asset, location, time, agent/work order context and a typed event.

The lineage therefore treats identity continuity and evidentiary traceability as cross-cutting architecture.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Asset vs Model** — serialized equipment instance and reusable product/model description are different subjects.
2. **Model vs ModelRevision vs ModelVariant** — revision and variant are distinct model-evolution structures.
3. **Asset vs Segment** — persistent serialized equipment and functional/location position are different identities.
4. **AssetComponent vs SegmentComponent** — physical/equipment composition and functional-location hierarchy are distinct.
5. **Asset-Segment relationship vs Asset identity** — installation/removal changes context without changing the Asset's identity.
6. **Registry vs configuration Event** — persistent registered identity and a change to configuration are different.
7. **MeasurementLocation vs Asset/Segment** — measurement point/context is not automatically identical to the equipment being measured.
8. **Measurement vs Test vs Event** — evidence types have different semantics.
9. **Measurement vs Assessment** — observed data and interpreted health/prognosis are different.
10. **HealthAssessment vs RemainingLifeAssessment** — current condition and future-life projection are distinct.
11. **Assessment vs Recommendation** — evaluation and advice are separate.
12. **Recommendation vs Request/Work** — advice is not the same as authorized/planned/executed action.
13. **CalendaredWork vs CompletedWork** — planned and performed work are distinct.
14. **OSA-CBM functional block vs equipment object** — processing stage is not a physical asset.
15. **OSA-CBM algorithm internals vs open interface/data** — standardized information flow does not standardize proprietary processing implementation.
16. **CCOM conceptual model vs OSA-EAI exchange/storage realization** — domain meaning and integration technology are different.
17. **Asset lifecycle status vs condition/health assessment** — administrative/lifecycle status and diagnostic health evaluation should not be collapsed.
18. **Event cause/effect/evidence relationships vs simple chronological history** — time order alone does not preserve event meaning.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely core/intrinsic:** persistent equipment identity; model/type/instance separation; component hierarchy;
- **likely contextual relationship pattern:** functional location/Segment, Site, ownership, geospatial tracking and changing installation relationships;
- **likely reusable lifecycle pattern:** persistent subject identity plus typed configuration/status Events rather than rewriting current state only;
- **likely evidence/assessment pattern:** Measurement/Test/Event → Health Assessment → Prognosis → Recommendation → Work;
- **likely cross-cutting:** InfoSource, Agent/role, time, data quality, documents and provenance;
- **likely functional pattern:** OSA-CBM six-stage condition-processing chain with open interfaces and proprietary algorithm internals;
- **likely management pattern:** registry, configuration, reliability, maintenance and completed-work structures remain semantically distinct;
- **specialization caution:** MIMOSA is physical-asset-management oriented and should not automatically define every V2 equipment concern;
- **binding/representation caution:** CCOM classes, OSA-EAI XML/database structures and OSA-CBM service interfaces are MIMOSA-native realizations, not automatically V2 classes or API resources.

**No V2 module disposition is made in Phase A.**

---

**C07 status: COMPLETE.**

**Next frozen lineage:** C08 — OGC API – Connected Systems.

---

# C08 — OGC API – Connected Systems Parts 1–2

## Source basis and evidence ceiling

**Frozen primary source IDs:** 10, 11.  
**Frozen companion IDs:** 3, 9, 12, 17.

**Primary inspected sources:**

- OGC API – Connected Systems – Part 1: Feature Resources, OGC 23-001, v1.0, published 16 July 2025.
- OGC API – Connected Systems – Part 2: Dynamic Data, OGC 23-002, v1.0, published 16 July 2025.

**Evidence note:** These are approved OGC implementation standards and the intended future binding environment for V2. This anatomy extraction therefore makes a strict distinction between:

1. **semantic distinctions the standards explicitly define**, which may inform the DIM; and
2. **resource/endpoint/encoding mechanics**, which remain binding-level implementation structures unless independent domain evidence supports promotion.

The NATO STANAG/AEP artifact is treated as a profile/adoption companion, not an independent model.

---

## 1. Source-native structural organization

Connected Systems divides the connected-system domain into **feature resources describing persistent/contextual subjects** and **dynamic resources representing flows, observations, commands and events**.

### Part 1 — feature/static-context resources

Primary resource types include:

1. **System**
   - the represented system/agent/process;
   - classified by `systemType`;
   - optionally classified by `assetType`;
   - has persistent unique identifier, validity, location and associations.

2. **Subsystem**
   - a regular System related hierarchically to a parent System.

3. **Deployment**
   - describes deployment/employment context for Systems;
   - can identify a Platform and deployed Systems;
   - can contain Subdeployments.

4. **Procedure**
   - reusable description of a process/procedure/system kind;
   - System can reference a Procedure via `systemKind`.

5. **Sampling Feature / Feature of Interest**
   - represent the sampled/observed/control context and ultimate target features.

6. **Property**
   - defines an observable/controllable property concept independently from one System or stream.

### Part 2 — dynamic resources

7. **DataStream**
   - a collection/channel of observations produced by one System output;
   - all Observations share the same observed properties and result schema.

8. **Observation**
   - individual observation in a DataStream.

9. **ControlStream**
   - a control/actuation channel receiving commands for one System;
   - all Commands share controlled properties and parameter schema.

10. **Command**
    - individual actuation/tasking request.

11. **CommandStatus**
    - status report about a Command.

12. **CommandResult**
    - result produced by command execution.

13. **Feasibility**
    - a command-like request used to determine feasibility before command execution;
    - has status/result structures parallel to Command.

14. **SystemEvent**
    - captures system events/maintenance operations over time.

The source-native pattern is therefore:

> **persistent System + reusable Procedure + deployment/context + explicit properties/targets + observation flows + command flows + event/history**

---

## 2. Purpose of each partition

### System

Purpose: provide the persistent addressable description of a System while keeping role (`systemType`) and realization (`assetType`) distinguishable.

### Subsystem

Purpose: represent System components recursively while preserving each component as a full System resource.

### Deployment

Purpose: represent a time/context-scoped grouping and use of Systems, Platform, configuration and related observed/controlled features.

### Procedure / systemKind

Purpose: separate a particular System instance from the reusable description of its kind/procedure/datasheet.

### Sampling Feature / Feature of Interest

Purpose: distinguish the proxy/sampling geometry/context from the ultimate real-world feature that observations/control concern.

### Property

Purpose: define observable/controllable property meaning independently of individual stream values.

### DataStream

Purpose: factor common observation metadata/schema out of individual observations and organize real-time and/or historical output data.

### Observation

Purpose: represent individual results/acts within a DataStream.

### ControlStream

Purpose: factor common control/command metadata/schema out of individual commands and represent real-time/historical command channels.

### Command

Purpose: represent an individual requested actuation/task.

### CommandStatus / CommandResult

Purpose: separate progress/state of command execution from the command request and from its result.

### Feasibility

Purpose: request/check whether a command-like action can be performed, using the same parameter semantics without executing the regular command.

### SystemEvent

Purpose: represent time-stamped system lifecycle/maintenance/configuration events such as calibration, configuration change, software update, part replacement, relocation/deployment and handoff.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| System identity | System, uniqueIdentifier, name, description, validTime, location |
| Role/realization | systemType, assetType |
| Reusable kind | systemKind, Procedure |
| Composition | parentSystem, subsystems, Composition |
| Temporary association | Aggregation, Deployment, platform, deployedSystems |
| Deployment hierarchy | parentDeployment, subdeployments |
| Observation context | SamplingFeature, FeatureOfInterest, Property |
| Output channel | DataStream, observed properties, result schema |
| Observation | Observation, phenomenon/result time, result |
| Control channel | ControlStream, controlled properties, parameter schema |
| Tasking | Command, CommandStatus, CommandResult |
| Pre-tasking analysis | Feasibility, feasibility status/result |
| History/lifecycle | SystemEvent, event type, eventTime |
| Identifiers | resource local ID, canonical URL, persistent uniqueIdentifier/UID |

---

## 4. Primary relationships

### System ↔ Procedure

`systemKind` links a System to one reusable Procedure description.

### System ↔ Subsystems

Systems can contain/nest other Systems recursively.

CSAPI distinguishes two source-native association meanings:

- **Composition** — subsystem is integral/ordinarily enduring and not usually separated except for maintenance.
- **Aggregation** — subsystem is not permanently attached and can be associated with different parent Systems at different times.

### Aggregation ↔ Deployment

Aggregation is represented through Deployment: Deployment describes what Systems are mounted/associated with a parent/Platform at a given time.

### Deployment ↔ Systems/context

Deployment can link:

- Platform;
- deployed Systems;
- features of interest;
- sampling features;
- DataStreams;
- ControlStreams;
- subdeployments.

### System ↔ DataStreams / ControlStreams / Events

Dynamic resources are associated back to the System that produces/receives them.

### DataStream ↔ Observations

Observation belongs to a parent DataStream whose common schema/properties apply.

### ControlStream ↔ Commands

Command belongs to a parent ControlStream whose controlled properties/schema apply.

### Command ↔ status/result

Command can create multiple CommandStatus records and CommandResult.

### Stream ↔ Property / target features

DataStream references observed properties; ControlStream references controlled properties. Both can reference sampling/feature-of-interest context.

---

## 5. Dependency boundaries

Connected Systems has explicit layering.

### Domain/resource semantics vs encoding

Part 1/2 define resource attributes/associations independently of whether a resource is encoded as GeoJSON, SensorML, JSON, SWE Common, etc.

### Persistent feature vs dynamic data

Part 1 persistent/context resources are separate from Part 2 time-varying resources.

### System instance vs reusable kind

System and Procedure/systemKind are separate.

### Composition vs deployment context

Enduring subsystem relationship and time-scoped aggregation are separate.

### Stream metadata vs individual values

DataStream/ControlStream provide common schema/context; Observation/Command supply individual instances.

### Command request vs execution status vs result

Task, execution state and output are separate.

### Property definition vs value

Property resource identifies semantic property; Observation/result or current dynamic data supplies values.

### Base feature model vs OGC API mechanics

Canonical URLs, collections, nested endpoints, pagination and filters are API structures, not automatically DIM concepts.

---

## 6. Intrinsic vs contextual standing

### Strongly intrinsic to System description

- persistent unique identifier;
- systemType;
- assetType;
- reusable kind link;
- enduring Composition/subsystem structure;
- applicable name/description;
- intrinsic capabilities represented by related outputs/control definitions where semantically tied.

### Contextual/time-scoped

- Deployment;
- Aggregation;
- Platform carrying a System;
- deployment-specific configuration;
- Feature of Interest/Sampling Feature for a particular observing/control context;
- current location where not inherently fixed.

### Dynamic/evidentiary

- Observations;
- Commands;
- CommandStatus/Result;
- SystemEvents.

The source explicitly prevents temporary aggregation from being mistaken for enduring composition.

---

## 7. Cross-cutting concepts

Cross-cutting structures include:

- persistent UID vs local API ID;
- canonical URL;
- validTime;
- geometry/location;
- feature links;
- property definitions;
- schemas;
- encodings;
- temporal filtering;
- collections/search/filtering;
- links between static and dynamic resources.

The System/Deployment/Procedure/SamplingFeature resources also map to SOSA/SSN concepts, making semantic alignment cross-cutting.

---

## 8. State / temporal / lifecycle organization

CSAPI has multiple temporal structures.

### Description validity

System descriptions can have `validTime`.

### Deployment time

Deployments are time-scoped contexts and can form nested deployment histories.

### Observation time

Observations carry their own temporal semantics within DataStreams.

### Command lifecycle

Command is separate from CommandStatus and CommandResult, allowing multiple status updates over time.

### Feasibility lifecycle

Feasibility uses command-like status/result structure before actual command execution.

### System lifecycle/history

SystemEvent explicitly records events such as:

- Calibration;
- ConfigurationChange;
- SoftwareUpdate;
- PartReplacement;
- Relocation;
- Deployment;
- operator handoff;
- decommissioning.

This is a **history/event structure**, not the same as current System description.

---

## 9. Composition / topology organization

CSAPI defines both persistent and time-scoped structure.

### Persistent system composition

Subsystems are full System resources and can be nested indefinitely.

Composition means the component is an integral/ordinarily enduring part of the parent.

### Time-scoped aggregation

Interchangeable/non-permanent relationships are modeled by Deployment, not by changing the persistent composition tree.

### Mixed systems

A parent can simultaneously have:

- composed built-in subsystems;
- aggregated/interchangeable subsystems active for a deployment.

### Deployment hierarchy

Deployments can have subdeployments; associated Systems, features, DataStreams and ControlStreams can be retrieved recursively across the deployment tree.

### Important distinction

**System topology and deployment topology are different source-native structures.**

---

## 10. Capability / function / behavior organization

Connected Systems does not have one generic Capability resource in Parts 1–2. Capability/behavior is expressed through several structures.

### System role

`systemType` classifies the principal role/activity:
- Sensor;
- Actuator;
- Sampler;
- Platform;
- System.

### Realization

`assetType` separately identifies realization such as:
- Equipment;
- Human;
- LivingThing;
- Simulation;
- Process;
- Group;
- Other.

### Procedure/systemKind

Reusable Procedure describes how/kind of System behavior.

### DataStream

Outputs expose what the System observes/produces.

### ControlStream

Controlled properties and parameter schemas expose what can be affected/commanded.

### Feasibility

Allows capability/task feasibility to be evaluated before execution.

The source-native capability picture is therefore distributed across **role + reusable procedure + outputs + controlled properties + schemas/feasibility**, not one Capability object.

---

## 11. Information / output organization

CSAPI deliberately separates static/contextual description from several dynamic information types.

### Output description

DataStream describes one System output, observed properties and result schema.

### Observation values

Observation is the actual observation/result.

### Command-channel description

ControlStream describes controlled properties and command/parameter/result schemas.

### Command

Command is the request instance.

### Command status/result

Execution progress and final/produced result are separate resources.

### System events

Lifecycle/maintenance/configuration events are a separate dynamic resource family.

### Real-time vs historical access

DataStream and ControlStream can expose:

- real-time only;
- historical only;
- both.

This is explicit metadata, not inferred from endpoint location.

---

## 12. Management / condition organization

Parts 1–2 do not define a generic equipment-management domain comparable to Redfish/MIMOSA, but they provide carriers for management interactions and history.

Relevant structures include:

- Command/ControlStream for management actions;
- DataStream/Observation for state/telemetry;
- SystemEvent for maintenance/configuration history;
- Deployment for employment/configuration context;
- Procedure for reusable system kind/procedure;
- Property resources for observed/controlled properties.

The standard intentionally leaves detailed family-specific condition/management vocabularies to profiles/extensions/domain descriptions.

**Evidence result:** CSAPI supplies interoperable structural carriers but does not itself define a complete generic condition/service taxonomy.

---

## 13. Provenance / identity / reference organization

Identity is deliberately layered.

### Persistent System UID

`uniqueIdentifier` is intended to be persistent and independent of the resource URL.

### API-local resource identity

Each resource also has a local identifier and canonical URL.

### Reusable-kind reference

System references Procedure through `systemKind`.

### Source/subject relationships

Dynamic resources reference their producing/receiving System and target features/properties.

### Parent/context references

Subsystem and Deployment associations are explicit links rather than inferred from names/URLs alone.

### Event/source continuity

SystemEvent remains related to the persistent System while recording changes occurring to it over time.

The standard therefore distinguishes **persistent domain identity, API resource identity, reusable type/kind identity and contextual relationship identity**.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **System vs Procedure/systemKind** — particular System and reusable kind/procedure are different subjects.
2. **systemType vs assetType** — operational role and realization are independent dimensions.
3. **System vs Subsystem** — a subsystem is still a full System, not merely an untyped embedded record.
4. **Composition vs Aggregation** — enduring/integral and time-varying/interchangeable relationships are semantically different.
5. **System topology vs Deployment topology** — component structure and employment grouping are different.
6. **Deployment Platform vs deployed System** — host/context and carried/associated systems remain distinct.
7. **Property definition vs property value** — semantic property concept and observed/controlled value are different.
8. **DataStream vs Observation** — output/channel description and individual observation are different.
9. **ControlStream vs Command** — command channel/capability description and individual command are different.
10. **Command vs CommandStatus vs CommandResult** — requested action, execution state and produced result are separate.
11. **Command vs Feasibility** — checking whether an action can be performed is not the same as executing it.
12. **Observation vs SystemEvent** — observation result and lifecycle/maintenance event are different information kinds.
13. **SamplingFeature vs ultimate FeatureOfInterest** — proxy/sampling context and real target are distinct.
14. **Persistent UID vs local ID/canonical URL** — domain identity and API address/resource identity are different.
15. **Real-time vs historical stream access** — access mode is explicit and should not be inferred.
16. **Resource semantics vs endpoint/encoding mechanics** — API nesting and serialization are not automatically domain relationships.
17. **Current System description vs history/event record** — updates to current description do not replace the need for explicit historical events.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely core/intrinsic:** persistent System identity; role/realization separation; reusable kind/procedure; enduring subsystem composition;
- **likely contextual relationship pattern:** Deployment, Aggregation, Platform, SamplingFeature and FeatureOfInterest;
- **likely dynamic-information pattern:** DataStream/Observation and ControlStream/Command separation;
- **likely behavior pattern:** Command vs Status vs Result vs Feasibility;
- **likely lifecycle/history pattern:** explicit SystemEvent separate from current System description;
- **likely cross-cutting:** Property definitions, persistent UID/local ID distinction, validTime, schemas and semantic links;
- **likely reusable topology pattern:** persistent composition and deployment aggregation maintained as separate structures;
- **binding caution:** resource types, canonical URLs, nested endpoints, HTTP methods, collections and encodings are OGC API realization mechanisms and are not automatically DIM classes/relationships;
- **profile-gap signal:** detailed condition, lifecycle, communications, power and family-specific capability semantics are not fully standardized by CSAPI Parts 1–2 and must come from applicable domain evidence rather than local API invention.

**No V2 module disposition is made in Phase A.**

---

**C08 status: COMPLETE.**

**Next frozen lineage:** C09 — OGC SensorML.

---

# C09 — OGC SensorML 3.0

## Source basis and evidence ceiling

**Frozen primary source ID:** 13.  
**Frozen companion IDs:** 1, 2, 4, 6, 16.

**Primary inspected source:**

- Open Geospatial Consortium, *OGC SensorML Encoding Standard*, OGC 23-000, version 3.0, published 16 July 2025:
  - `https://docs.ogc.org/is/23-000/23-000.html`
  - normative conceptual UML plus normative JSON encodings.

**Companion evidence:**

- SensorML 3.0 JSON schema collection;
- historical marine/discovery profiling material in the frozen corpus.

**Evidence note:** SensorML 3.0 itself defines both the conceptual models and JSON encodings. This extraction treats the UML/process semantics as the source-native structural evidence and keeps JSON members/schema mechanics as implementation details unless they directly implement a conceptual distinction. Historical profile material is used only as lineage/context and not as authority over SensorML 3.0.

---

## 1. Source-native structural organization

SensorML is organized around a **general process model** in which physical hardware, software/computational processes, sensors, actuators and whole systems are all modeled as processes with explicit inputs, outputs, parameters and methods.

The principal source-native conceptual partitions are:

1. **DescribedObject**
   - common identification/discovery/qualification metadata;
   - unique identifier;
   - identifiers/classifiers/keywords;
   - security/legal constraints;
   - valid time;
   - capabilities;
   - characteristics;
   - contacts;
   - documentation;
   - history;
   - extensions.

2. **AbstractProcess**
   - common process semantics:
     - inputs;
     - outputs;
     - parameters;
     - `typeOf`;
     - feature of interest;
     - configuration;
     - modes.

3. **SimpleProcess**
   - atomic/non-decomposed process;
   - method represented by a ProcessMethod.

4. **AggregateProcess**
   - collection of autonomous component processes;
   - explicit data-flow connections among components;
   - components may be physical or non-physical and may themselves be aggregate.

5. **AbstractPhysicalProcess**
   - adds physical/spatiotemporal semantics to AbstractProcess:
     - attachment;
     - local reference frames;
     - position;
     - dynamic state;
     - spatial/temporal frames.

6. **PhysicalComponent**
   - atomic/non-decomposed physical processing device whose location matters.

7. **PhysicalSystem**
   - physical hardware device/system modeled as an aggregate process with one or more component subprocesses and explicit connections.

8. **Configurable Process**
   - general process description with selectable modes/options and allowable parameter ranges.

9. **Configured Process**
   - specific process inheriting from a configurable process and supplying concrete settings/restrictions.

10. **Mode**
    - named operational configuration that can set groups of parameter/settings values.

11. **Settings / configuration**
    - set values, arrays, constraints and enable/disable choices for configurable process elements.

12. **Deployment / DeployedSystem**
    - represents when, where, why and how physical or non-physical systems are deployed;
    - captures deployment-specific configuration and description.

13. **DerivedProperty**
    - defines a domain-specific property by specialization/derivation from a more general property/quantity concept.

14. **SWE Common data dependencies**
    - ObservableProperty and SWE Common Data Components define typed inputs/outputs/parameters and data aggregates.

The source-native pattern is therefore:

> **common described object → process interface/behavior → atomic vs aggregate decomposition → physical specialization where location matters → configuration/modes → deployment context → typed data/property semantics**

---

## 2. Purpose of each partition

### DescribedObject

Purpose: supply reusable identity, discovery, qualification, provenance/history and descriptive metadata common to processes, systems, modes and deployments.

### AbstractProcess

Purpose: establish the universal process interface/semantic contract: inputs, method/parameters, outputs, reusable kind, feature of interest and configuration.

### SimpleProcess

Purpose: describe an atomic/black-box process whose internal subprocess decomposition is not modeled.

### AggregateProcess

Purpose: model a process whose internal components and data flows matter. The aggregate itself still has its own external inputs, outputs, parameters and metadata.

### PhysicalComponent

Purpose: model an atomic physical processing device when its real-world position is important and there is no intent to decompose it into subprocess components.

### PhysicalSystem

Purpose: model a physical hardware device/system whose internal component subprocesses and data flows are explicitly represented and whose real-world position is important.

### Configurable/Configured Process

Purpose: separate:
- what options/modes/parameter ranges are allowed for a general process/model; from
- the actual settings/configuration of a particular process instance.

### Mode

Purpose: package a named operational state/configuration as a group of coordinated settings.

### Deployment

Purpose: represent deployment context separately from the persistent process/system description:
- where;
- when;
- why;
- platform;
- deployed system;
- deployment-specific configuration;
- responsible contacts/mission classifiers/characteristics.

### DerivedProperty

Purpose: specialize a general property/quantity into a domain-specific property while retaining semantic derivation.

### SWE Common dependency

Purpose: give inputs, outputs and parameters explicit typed structure, units, ranges, quality and aggregate semantics without re-inventing a separate SensorML data-model language.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Common description | DescribedObject, uniqueId, identifier, classifier, keyword, validTime, capabilities, characteristics, contacts, documentation, history |
| Process core | AbstractProcess, input, output, parameter, ProcessMethod, featureOfInterest |
| Reusable model/instance | typeOf, general process, specific process |
| Atomic process | SimpleProcess, ProcessMethod |
| Aggregate process | AggregateProcess, component, connection, data flow |
| Physical semantics | AbstractPhysicalProcess, attachedTo, spatial frame, temporal frame, position, pose, trajectory/dynamic state |
| Atomic physical device | PhysicalComponent |
| Composite physical device/system | PhysicalSystem, components, connections |
| Configuration | ConfigurableProcess, configured process, Mode, Settings, allowed values/constraints |
| Deployment | Deployment, DeployedSystem, platform, location, system, deployment-specific configuration |
| Property semantics | ObservableProperty, DerivedProperty |
| Data typing | SWE Common scalar, range, record, vector, array, stream, choice components |
| History | Event, EventList |

---

## 4. Primary relationships

### Process → inputs / outputs / parameters

Every SensorML process can expose explicit interface elements. Inputs can include physical observable properties; outputs/parameters use typed SWE Common data components or interfaces.

### Process → method

Atomic processes use ProcessMethod to describe the algorithm/methodology.

### AggregateProcess → components

Aggregate process contains/references one or more component processes.

### AggregateProcess → connections

Connections explicitly map data flow from component outputs to component inputs/parameters and to the aggregate's external interface.

### PhysicalSystem → components/connections

PhysicalSystem uses aggregate-process decomposition while also carrying physical/spatial semantics.

### Physical process → attachedTo parent

`attachedTo` represents a positional dependency: movement of the parent affects the child's position.

### Physical process → reference frames / position

The physical object's local/intrinsic reference frame is related to an external frame through location/orientation/trajectory/dynamic state.

### Specific process → general process

`typeOf` links a specific process/instance to a reusable general/base process.

### Configured process → configurable process

A configured process:
- inherits through `typeOf`;
- applies settings/restrictions in `configuration`.

### Process → Mode

A process can define/select Modes, each carrying a coordinated set of settings.

### Deployment → platform / deployedSystem

Deployment relates:
- geographic location;
- platform;
- one or more DeployedSystem entries;
- each DeployedSystem references a persistent system/process and may provide deployment-specific configuration.

### DescribedObject → history Events

History records time-scoped events such as calibration, maintenance, algorithm/parameter changes and deployment.

---

## 5. Dependency boundaries

SensorML has strong conceptual layering.

### DescribedObject vs process semantics

Identity/metadata is reusable across process types; process interface/behavior is added by AbstractProcess.

### Process semantics vs data semantics

SensorML delegates typed values/records/arrays/ranges/encodings to SWE Common rather than defining an independent data type system.

### Process vs ProcessMethod

The process instance/interface and the method/algorithm describing how it works are separate.

### Atomic vs aggregate

Simple/PhysicalComponent do not expose internal subprocess decomposition; AggregateProcess/PhysicalSystem do.

### Physical vs non-physical

Location/reference-frame semantics apply when physical position matters. Non-physical aggregate/simple processes can use the same core process model without physical frames.

### General vs specific process

Reusable model/type descriptions and particular instances are separated through `typeOf`.

### Configurable vs configured

Allowed configuration space and selected concrete settings are distinct.

### Persistent process/system vs Deployment

Deployment-specific context/configuration is not merged into the durable process/system description.

### Conceptual model vs JSON encoding

The JSON schemas are direct implementations of UML models, but object members/links are encoding choices; the conceptual distinctions control the semantics.

---

## 6. Intrinsic vs contextual standing

### Strongly intrinsic/process-defining

- unique identity;
- inputs/outputs/parameters;
- process method;
- component decomposition where modeled;
- data-flow connections;
- physical characteristics;
- capabilities;
- characteristics;
- allowed configuration/modes;
- intrinsic/local reference frame.

### Instance/model-specific but durable

- identifiers;
- classifiers;
- manufacturer/contacts/documentation;
- reusable `typeOf`;
- configured parameter values;
- component arrangement where persistent.

### Contextual

- deployment location;
- deployment platform;
- mission/deployment identifiers/classifiers;
- deployment-specific description/configuration;
- feature of interest when describing intended/actual operational target context;
- external reference frame.

### Historical/evidentiary

- calibration;
- maintenance;
- algorithm/parameter changes;
- deployment events.

SensorML explicitly allows multiple process descriptions with different `validTime` periods, separating configuration history from a single timeless description.

---

## 7. Cross-cutting concepts

Cross-cutting SensorML structures include:

- unique identifiers;
- identifiers/classifiers/keywords;
- security/legal constraints;
- validTime;
- capabilities;
- characteristics;
- contacts;
- documentation;
- history;
- extensions;
- semantic definitions/URIs;
- `typeOf`;
- feature of interest;
- modes/configuration;
- SWE Common typed values and constraints.

Because DescribedObject is inherited by many classes, these semantics span physical systems, computational processes, modes and deployments.

---

## 8. State / temporal / lifecycle organization

SensorML has several distinct temporal structures.

### Validity of description

`validTime` states the time over which a process description/configuration is valid.

The standard explicitly allows several SensorML descriptions for the same sensor/system with different validity periods.

### Dynamic physical state

Physical processes can carry:

- position;
- orientation;
- trajectory;
- velocity;
- angular velocity;
- higher derivatives;
- temporal reference frames.

### Operational modes/configuration

Modes and Settings represent selectable/selected operational configurations.

### History

EventList supports:
- calibration;
- maintenance;
- algorithm changes;
- parameter changes;
- deployment/maintenance events.

### Deployment

Deployment captures a separate operational/employment time/context with deployment-specific system configuration.

### Distinction

SensorML therefore distinguishes:

> **description validity, current/selected configuration, physical dynamic state, deployment context and historical Event record**

rather than treating all temporal change as one lifecycle field.

---

## 9. Composition / topology organization

SensorML supports both **process/data-flow topology** and **physical attachment topology**.

### Process composition

AggregateProcess/PhysicalSystem contain component processes.

Components can be:

- atomic or aggregate;
- physical or non-physical;
- inline or referenced.

### Data-flow topology

Connections explicitly define how component outputs feed:
- other component inputs;
- parameters;
- aggregate outputs/interfaces.

### Physical attachment topology

`attachedTo` describes a positional dependency between physical processes such that parent movement affects child position.

### Reference-frame topology

Physical position is modeled as the relationship between:
- intrinsic/local reference frame;
- external/geographic/parent reference frame.

### Deployment topology

Deployment separately associates:
- platform;
- deployed systems;
- deployment-specific configuration/location.

### Important source-native distinction

**Component decomposition, data-flow connection, physical attachment and deployment association are four different relationships.**

They must not be inferred from one another.

---

## 10. Capability / function / behavior organization

SensorML splits behavior/function across several structures.

### Process role

Inputs, outputs and parameters define the process interface.

### ProcessMethod

Defines the method/algorithm for atomic process behavior.

### Capabilities

DescribedObject `capabilities` further qualify input/output performance for discovery and use, e.g. measurement range/performance.

### Characteristics

Describe properties of the process/device that do not directly qualify its output, e.g. dimensions, material, power demand, anticipated lifetime.

### Configurable behavior

ConfigurableProcess defines:
- allowed parameter ranges;
- options;
- modes;
- enabled/disabled inputs/outputs/components.

Configured process selects/restricts these.

### Aggregate behavior

Whole system behavior can emerge from coordinated physical/nonphysical components and explicit data flows.

This gives a source-native separation among:

> **interface → method → performance capability → non-output physical characteristic → configuration/mode → composed behavior**

---

## 11. Information / output organization

SensorML is primarily descriptive rather than the runtime observation store, but it explicitly models data interfaces.

### Inputs

Can represent physical stimulus using ObservableProperty or typed data.

### Outputs

Can represent typed digital outputs with SWE Common DataComponents or DataInterfaces.

### Parameters

Represent process configuration/control variables rather than external observed inputs/outputs.

### Data aggregates

Related values should be represented as coherent SWE Common aggregates such as:
- DataRecord;
- Vector;
- DataArray;
- Matrix;
- DataStream;
- Choice.

### DataInterface

Can describe an accessible/encoded output interface and data flow.

### Process lineage

AggregateProcess connections and ProcessMethod can explicitly describe how an output was generated.

### Sensor-related data

The standard recognizes ancillary sensor-related data such as:
- status;
- quality;
- QoS;
- battery life

as distinct from the measured observable values even when transported in the same stream.

The source therefore distinguishes **process description, output schema/interface, actual observation value, ancillary status/quality data and processing lineage**.

---

## 12. Management / condition organization

SensorML supplies rich descriptive carriers but not a single universal management object model.

Management/condition-relevant structures include:

- configuration/settings;
- modes;
- capability/characteristic descriptions;
- status-related outputs/interfaces;
- history Events;
- contacts/responsible parties;
- documentation;
- deployment;
- security/legal constraints;
- component structure;
- location/dynamic state.

History can record:
- calibration;
- maintenance;
- parameter changes;
- deployment.

Characteristics can represent:
- physical dimensions;
- weight;
- material;
- power demand;
- anticipated lifetime.

Capabilities can represent performance/limits relevant to condition/use.

**Evidence result:** SensorML provides a strong whole-description framework for management information, but detailed condition/fault/work/service taxonomies must come from domain profiles or other sources.

---

## 13. Provenance / identity / reference organization

SensorML has extensive identity/reference/provenance structure.

### Unique identity

Every process description has a required `uniqueId`.

### Additional identifiers/classifiers

Terms can represent:
- serial number;
- model/manufacturer identifiers;
- mission IDs;
- short/long names;
- process/sensor/application classifiers.

### Reusable-kind reference

`typeOf` links specific process to general/model process.

### Component/reference identity

Components may be inline or referenced by link/UID.

### Process lineage

ProcessMethod + AggregateProcess component/data-flow structure can document how observation output was derived.

### History provenance

Event history can record changes affecting configuration/algorithm/maintenance/deployment.

### Contacts/documents

Responsible parties and external documentation are explicit.

### Semantic references

Definitions/semantic URIs attach meanings to parameters, capabilities, classifiers and data components.

The lineage therefore supports both **equipment/process identity** and **derivation/process provenance**.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **DescribedObject vs AbstractProcess** — descriptive metadata and process semantics are separate abstraction layers.
2. **Process vs ProcessMethod** — a process subject and the method/algorithm describing how it operates are different.
3. **Input vs output vs parameter** — observed stimulus/result/configuration variables have distinct roles.
4. **ObservableProperty vs output data value/schema** — phenomenon/property semantics are not the same as encoded measurement values.
5. **SimpleProcess vs AggregateProcess** — atomic black-box and decomposed process are different modeling choices.
6. **PhysicalComponent vs PhysicalSystem** — atomic physical device and decomposed aggregate hardware system are different classes.
7. **Physical vs non-physical process** — location/reference-frame importance is a real semantic distinction.
8. **Component relation vs connection/data flow** — what is part of a process and how data flows among parts are different.
9. **Component relation vs attachedTo** — process decomposition and physical positional attachment are different.
10. **attachedTo vs Deployment/platform** — persistent physical positional relationship and operational deployment context are different.
11. **typeOf vs configuration** — reusable model inheritance and selected instance settings are different.
12. **Configurable process vs configured process** — allowed configuration space and chosen configuration are different.
13. **Mode vs individual setting** — named coordinated operational mode and single parameter value are different.
14. **Capability vs characteristic** — output-qualifying performance and other descriptive properties are distinct.
15. **validTime vs history Event** — description validity and explicit historical event are different temporal semantics.
16. **persistent process/system vs DeployedSystem entry** — equipment/process identity and deployment-specific description/configuration are different.
17. **local reference frame vs external reference frame** — intrinsic pose frame and contextual frame are distinct.
18. **sensor-related ancillary data vs measured observable values** — status/quality/battery/QoS should not be silently treated as the observed phenomenon.
19. **conceptual UML vs JSON schema representation** — implementation encoding must not define domain truth.
20. **aggregate process execution model vs process description** — SensorML defines process/data-flow semantics but remains agnostic to execution engine/protocol.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely core/intrinsic:** persistent process/system identity; process interface; atomic vs aggregate distinction; component decomposition; physical spatial semantics;
- **likely reusable structural pattern:** model/type → configured instance → deployment-specific configuration;
- **likely functional pattern:** input/output/parameter + ProcessMethod + explicit component/data-flow topology;
- **likely capability pattern:** capabilities distinct from characteristics and settings;
- **likely configuration pattern:** ConfigurableProcess, Mode and Settings with allowed values/constraints;
- **likely contextual relationship pattern:** Deployment, platform, FeatureOfInterest and external reference frames separated from persistent system identity;
- **likely lifecycle/provenance pattern:** validTime plus explicit history Events and process lineage;
- **likely dynamic-information pattern:** typed DataInterface/output descriptions separated from actual observations and ancillary sensor-related status/quality data;
- **binding caution:** SensorML classes and JSON members are implementation/model constructs; V2 must not assume every whole sensing System is necessarily encoded as `PhysicalSystem` rather than `PhysicalComponent`;
- **profile-gap signal:** detailed management/condition/lifecycle vocabularies require additional donor semantics even though SensorML can carry them.

**No V2 module disposition is made in Phase A.**

---

**C09 status: COMPLETE.**

**Next frozen lineage:** C10 — OPC UA Devices / PA-DIM.

---

# C10 — OPC UA Devices / PA-DIM

## Source basis and evidence ceiling

**Frozen primary source IDs:** 103, 104.  
**Frozen companion ID:** 105.

**Primary inspected sources:**

- OPC Foundation, *OPC Unified Architecture Part 100: Devices*, version 1.05.0.
- OPC Foundation / FieldComm Group, *OPC UA for Process Automation Devices — PA-DIM*, version 1.02.0, OPC 30081.

**Companion evidence:**
- OPC UA Part 7 Profiles is retained as conformance/profile context only and is not treated as an independent anatomy model.

**Evidence note:** The OPC Foundation online reference is the current official structured publication. Part 100 defines a generic device information model; PA-DIM is a companion specification specializing it for Process Automation Devices. PA-DIM is therefore treated as a specialization within the same lineage, not as an independent structural vote.

---

## 1. Source-native structural organization

Part 100 explicitly defines **three models that build on one another**:

1. **Base Device Model**
   - unified view of Devices and their hardware/software parts independent of underlying protocol.

2. **Device Communication Model**
   - adds Networks, ConnectionPoints, Protocols and topological relationships.

3. **Device Integration Host Model**
   - adds host/integration structures for managing multiple Devices and reflecting configured/online automation-system topology.

It also defines reusable AddIns for:

- locking/concurrent access;
- software update.

### Base Device Model hierarchy

The primary source-native type hierarchy is:

- **TopologyElementType**
  - common base for elements in device topology;
  - has functional grouping concept.

- **ComponentType**
  - generic representation of Device or parts of Device;
  - parts can be mechanical or software;
  - applies vendor/tag nameplate interfaces.

- **DeviceType**
  - subtype of ComponentType;
  - commonly represents field Devices;
  - adds device health/support semantics and ConnectionPoints.

- **SoftwareType**
  - sibling subtype of ComponentType;
  - represents software as a component.

Additional structural types include:

- Modular Devices;
- Blocks;
- ConfigurableObjectType;
- FunctionalGroupType;
- ConnectionPointType;
- NetworkType;
- ProtocolType;
- DeviceSet;
- NetworkSet;
- DeviceTopology.

### PA-DIM specialization

PA-DIM defines:

- **PADIMType**
  - subtype of ComponentType;
  - real-world Process Automation Device representation.

It composes reusable interfaces/objects:

- vendor nameplate;
- tag nameplate/AssetId;
- **IDeviceHealthType**;
- **IAdministrationType**;
- **ISignalSetType**;
- DeviceConditionSet;
- SubDevices;
- dictionary/class reference.

PA-DIM then specializes PADIMType into domain Device Types such as ProcessAnalyserType and concrete analyzer/sensor classes.

The source-native pattern is therefore:

> **generic topology element → component → device/software → modular components/functional groups → communication topology → integration host**, with PA-DIM adding **device identity + health + process signals + administration + condition + subdevice specialization**.

---

## 2. Purpose of each partition

### TopologyElementType

Purpose: provide common topology/parameter/functional-group structure for objects participating in device topology.

### ComponentType

Purpose: represent a generic Device or a part of a Device without requiring the mandatory Device properties. It can represent mechanical or software parts.

### DeviceType

Purpose: represent a physical Device with common identity, support, health and connection information.

### SoftwareType

Purpose: represent software as a component independently from physical Device identity.

### FunctionalGroupType

Purpose: organize Properties, Parameters and Methods **by application/use**, e.g.:

- maintenance;
- diagnostics;
- condition monitoring;
- identification.

The same underlying element can appear in more than one FunctionalGroup, and FunctionalGroups can nest.

### Modular Device / SubDevices / ConfigurableObject

Purpose: represent device internals that can vary by installed module/subdevice/block configuration.

### Device Communication Model

Purpose: model communication independently from device composition:
- Network;
- ConnectionPoint;
- Protocol/Communication Profile;
- topological connection.

### Device Integration Host

Purpose: represent a server/host that integrates/manages multiple Devices and reflects configured and online topology.

### PA-DIM identity/nameplate

Purpose: provide vendor/product/asset identity for Process Automation Devices across lifecycle use cases.

### SignalSet

Purpose: contain process variables/signals.

### DeviceHealth / DeviceConditionSet

Purpose: represent general device health plus condition variables/alarms and component-specific condition sets.

### IAdministration

Purpose: expose administrative/configuration functions such as display language, date of last change and reset behavior.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Generic topology | TopologyElementType, ParameterSet, MethodSet, FunctionalGroup |
| Generic component | ComponentType, VendorNameplate, TagNameplate, AssetId |
| Device | DeviceType, Manufacturer, Model, SerialNumber, RevisionCounter, support info, DeviceHealth |
| Software | SoftwareType |
| Device internals | ModularDevice, ConfigurableObject, Blocks, SubDevices |
| Functional organization | FunctionalGroupType, Identification, Configuration, Diagnostics, Maintenance, ConditionMonitoring |
| Communication | NetworkType, ConnectionPointType, ProtocolType, Communication Profile, ConnectsTo |
| Device integration | DeviceIntegrationHost, DeviceTopology, DeviceSet, NetworkSet, online/offline representation |
| PA-DIM device | PADIMType, process-automation device class/dictionary entry |
| PA-DIM process values | ISignalSetType, SignalSet |
| PA-DIM condition | DeviceHealth, DeviceHealthAlarms, DeviceConditionSet, GeneralDeviceConditions, component conditions |
| PA-DIM lifecycle/admin | IAdministrationType, DateOfLastChange, FactoryReset, commissioning/replacement/calibration use cases |

---

## 4. Primary relationships

### ComponentType → DeviceType / SoftwareType

Device and software are sibling specializations of a more general Component.

### Device → components/subdevices

A complex Device can contain:

- other Devices;
- mechanical components;
- software components;
- modules;
- Blocks.

Only the root of a complex Device needs to appear in DeviceSet; components can be reached through hierarchical references.

### FunctionalGroup → underlying elements

FunctionalGroup **organizes** Parameters/Properties/Methods that may physically/model-wise be components elsewhere. An element can appear in more than one functional group.

### Device → ConnectionPoint → Network

ConnectionPoint is the logical interface between Device and Network.

`ConnectsTo` relates Network and ConnectionPoint/Device topologically.

### Network → Protocol/Communication Profile

Network and ConnectionPoint can carry ProtocolType / communication-profile information.

### DeviceIntegrationHost → Device topology

Host exposes configured/online information about Devices, Networks and ConnectionPoints, even when native device protocols differ.

### Offline ↔ Online representation

DeviceTopology can maintain two schematically equivalent representations:
- offline/configured/engineering data;
- online/current physical-device data.

They are related but have different Node IDs and access semantics.

### PA-DIM → SubDevices

PADIMType can contain SubDevices, and those subdevices must themselves be PADIMType or subtype instances.

### PA-DIM → SignalSet / DeviceConditionSet

Process values/signals and condition information are distinct substructures of the same Device.

---

## 5. Dependency boundaries

Part 100 has explicit model layering.

### Device Model vs Communication Model

Device identity/composition is independent from how it connects to a Network.

### Communication Model vs Integration Host

Network/device topology can exist independently; Device Integration Host adds engineering/management and online/offline integration semantics.

### Component vs FunctionalGroup

FunctionalGroup is an **application-oriented organizational view**, not the physical ownership location of the underlying element.

### Device vs Software

Software is separately modeled as ComponentType subtype instead of being collapsed into Device.

### Type vs concrete companion specialization

Part 100 supplies generic abstract Device/Component types; domain Companion Specifications define concrete Device subtypes.

### PA-DIM vs Part 100

PA-DIM reuses Part 100 Component/Device interfaces and adds process-automation domain information; it does not replace the generic topology/communication framework.

### Online vs Offline

Configured engineering representation and current physical-device representation are explicitly separated but structurally correlated.

---

## 6. Intrinsic vs contextual standing

### Strongly intrinsic to Device/component

- manufacturer/model/serial/revisions;
- AssetId/ComponentName;
- hardware/software parts;
- subdevices/modules;
- parameters/properties;
- process signals;
- DeviceHealth;
- condition variables;
- supported methods/functions.

### Contextual/relational

- Network membership;
- ConnectionPoint/network address;
- communication profile;
- integration host;
- containing automation topology;
- online/offline engineering state;
- facility/system context;
- functional grouping by application use.

### Viewpoint-dependent

FunctionalGroups such as Maintenance or Diagnostics are **views/groupings of elements**, not necessarily independent intrinsic subobjects. The same Parameter/Method can participate in several FunctionalGroups.

---

## 7. Cross-cutting concepts

The following recur across Part 100 and PA-DIM:

- vendor/product identity;
- AssetId/tag identity;
- support information;
- DeviceHealth;
- Parameters/Properties/Methods;
- FunctionalGroups;
- status/alarms;
- dictionary/semantic identifiers;
- software revision/update;
- locking/concurrent access;
- modularity;
- connection/network semantics;
- online/offline correspondence.

Part 100 Annex C also recognizes that the same real-world Device may be represented through multiple Companion Specifications; combination/merging of aspects is therefore a cross-cutting modeling concern.

---

## 8. State / temporal / lifecycle organization

The lineage distinguishes several state/time structures.

### Device health

IDeviceHealthType provides general health state and diagnostic alarms.

Multiple abnormal Conditions can be active simultaneously.

### Condition

PA-DIM DeviceConditionSet provides device-wide and component-specific condition variables.

### Configuration/administrative change

PA-DIM can expose DateOfLastChange and reset/configuration functions.

### Online/offline state

Device Integration Host separates:
- configured/offline values;
- current online physical-device values.

Transfer methods can synchronize the two.

### Software lifecycle

Part 100 software-update AddIn distinguishes:
- current version;
- pending version;
- fallback version;
- transfer/install behaviors.

### PA-DIM lifecycle use cases

PA-DIM explicitly states support for lifecycle activities including:
- procurement/engineering;
- commissioning;
- operation;
- monitoring/diagnosis;
- backup;
- replacement;
- repair;
- calibration;
- proof testing;
- batch configuration;
- regulatory audit.

However, these use cases do not imply that all lifecycle events are represented as one generic event-history model. The actual information is distributed across identity, configuration, health, conditions, signals, revisions and domain extensions.

---

## 9. Composition / topology organization

OPC UA Devices has several overlapping topologies.

### Component topology

A root Device can contain:
- subdevices;
- components;
- software;
- blocks.

DeviceSet exposes only root instances for complex systems; hierarchical references reveal internal components.

### Functional topology

FunctionalGroups organize elements by application concern independently from physical/component hierarchy.

### Communication topology

Network, ConnectionPoint and `ConnectsTo` form a separate communication topology.

### Integration topology

DeviceTopology represents:
- Devices;
- Networks;
- communication elements;
- gateway/nested networks;
- online/offline counterparts.

### PA-DIM modularity

SubDevices gives an explicit modular device structure restricted to PA-DIM Device types.

### Important distinction

**Physical/device composition, functional grouping and communication topology are separate structures.**

---

## 10. Capability / function / behavior organization

The lineage distributes capability through:

- Device/Component ObjectType;
- Parameters;
- Methods;
- FunctionalGroups;
- Interfaces/AddIns;
- process signals;
- domain-specific Device subtypes.

### FunctionalGroup

Groups behavior/data according to use such as:
- Identification;
- Configuration;
- Diagnostics;
- Maintenance;
- condition monitoring.

### Methods

Represent callable behavior/actions.

### Parameters

Represent Device variables used for:
- configuration;
- monitoring;
- control.

### PA-DIM process function

ISignalSetType groups process values/signals.

Device class dictionary references identify the process-automation class, e.g. transmitter/analyzer types.

### Capability vs implementation

Part 100 permits multiple Companion Specifications to represent different aspects of the same real-world Device. Thus one Device's functional semantics can be composed from multiple standardized aspect models rather than one monolithic type.

---

## 11. Information / output organization

Part 100 / PA-DIM distinguish multiple information classes.

### Product/nameplate information

- manufacturer;
- model;
- serial;
- product code;
- hardware/software/device revision;
- AssetId;
- ProductInstanceUri.

### Parameters

Configuration/monitoring/control variables.

### Process values

PA-DIM SignalSet collects process variables.

### Health/condition

DeviceHealth plus alarms and condition sets.

### Methods

Callable device behavior.

### Network information

ConnectionPoint, address and communication profile.

### Online/offline values

Same conceptual Parameter can have separate offline engineering and online current representations.

The source therefore distinguishes **identity, configuration/control parameter, process signal, condition/health, communication and behavior**, even when all are reachable under the same Device node.

---

## 12. Management / condition organization

Management/condition is a major source-native concern.

### Support/administration

- support information;
- tag/nameplate;
- date of last change;
- factory reset;
- display/locale information.

### Health

DeviceHealth gives general health state.

### Diagnostics

Health alarms indicate abnormal states and can carry possible causes/suggested actions.

### Condition

DeviceConditionSet supports device-specific and component-specific condition variables.

### Configuration

Parameters and offline/online model support engineering/configuration workflows.

### Lifecycle use cases

PA-DIM's use cases explicitly include:
- monitoring;
- commissioning;
- replacement;
- repair;
- calibration;
- proof testing;
- configuration backup/download.

### Management authority

Device Integration Host manages integration across many Devices while remaining a separate system entity.

---

## 13. Provenance / identity / reference organization

The lineage distinguishes multiple identity layers.

### OPC UA Node identity

NodeId uniquely identifies AddressSpace Nodes; BrowseName is not globally unique.

### Product/device identity

- Manufacturer;
- Model;
- SerialNumber;
- ProductCode;
- ProductInstanceUri;
- AssetId;
- ComponentName;
- revision fields.

### Semantic dictionary identity

PA-DIM uses IRDI/dictionary references to identify:
- device classes;
- parameters;
- units;
- properties.

### Online/offline reference identity

Online and offline counterparts are separate Nodes linked by an explicit reference.

### Device/Component relationship identity

Hierarchical references identify component ownership; `ConnectsTo` identifies communication topology.

The model therefore separates **address-space identity, durable product identity, semantic-term identity and topology-reference identity**.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **TopologyElement vs Component vs Device** — generic topology element, component/part and complete Device have different abstraction levels.
2. **Device vs Software** — software is a sibling Component specialization, not merely an attribute of Device.
3. **root Device vs subdevice/component** — complex Device identity and internal part identities are distinct.
4. **component hierarchy vs FunctionalGroup** — ownership/structure and application-oriented grouping are not interchangeable.
5. **FunctionalGroup membership vs physical containment** — the same element can appear in multiple groups.
6. **Device Model vs Communication Model** — equipment structure and communication topology are separate.
7. **Device vs ConnectionPoint vs Network** — equipment, logical interface and communication medium are different.
8. **ConnectsTo vs hierarchical reference** — communication adjacency and component ownership are different relationship kinds.
9. **Device vs Device Integration Host** — managed equipment and integrating/management server are different subjects.
10. **offline/configured representation vs online/current representation** — engineered expectation and actual connected Device state are distinct.
11. **NodeId vs AssetId/product identity** — AddressSpace identity and real-world equipment identity serve different roles.
12. **DeviceHealth vs diagnostic Condition** — overall health state and specific abnormal conditions are distinct.
13. **identity/nameplate vs process signals** — product description and dynamic process values are separate information classes.
14. **process signal vs condition variable** — operational measurement and device-condition/diagnostic information are different.
15. **generic DeviceType vs PA-DIM specialization** — base device semantics and domain Device classes should not be flattened.
16. **same real-world Device vs multiple Companion-Spec representations** — multiple standardized aspects can describe one Device without creating multiple physical Devices.
17. **software update version states** — current, pending and fallback versions are semantically distinct.
18. **modular Device structure vs communication gateway topology** — internal device composition and access through nested networks are different.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely core/intrinsic:** durable device/product identity; hardware/software component distinction; modular/subdevice composition;
- **likely reusable structural pattern:** one real-world equipment subject described through multiple standardized aspect models;
- **likely viewpoint pattern:** FunctionalGroups for maintenance/diagnostics/configuration/condition without duplicating underlying properties/methods;
- **likely cross-cutting:** health, condition, support info, semantic dictionary references, software revision/update;
- **likely communications pattern:** Device → ConnectionPoint → Network separated from device composition;
- **likely management pattern:** online/current vs offline/engineered representation and separate Device Integration Host;
- **likely dynamic-information pattern:** process signals separated from configuration parameters and health/condition;
- **specialization evidence:** PA-DIM shows how generic Device semantics can be specialized into a bounded operational family while reusing base identity/health/topology;
- **binding/representation caution:** OPC UA ObjectTypes, Nodes, FunctionalGroups, interfaces and References are OPC-native information-model mechanisms and are not automatically V2 classes/resources;
- **viewpoint caution:** FunctionalGroup is an organizational view, not proof that each group should become a V2 module.

**No V2 module disposition is made in Phase A.**

---

**C10 status: COMPLETE.**

**Next frozen lineage:** C11 — OSUS / OSUS-R.

---

# C11 — OSUS / OSUS-R

## Source basis and evidence ceiling

**Frozen primary source ID:** 34.  
**Frozen companion IDs:** 27, 59.

**Primary inspected source:** OSUS-R repository pinned at revision:

`d09088fbe56d4b64f0544d72e98c3cb70fa941f6`

Key source-native artifacts inspected include:

- `mil.dod.th.core.asset.Asset`
- `mil.dod.th.core.asset.AssetProxy`
- `AssetFactory`
- `AssetCapabilities.xsd`
- `BaseCapabilities.xsd`
- `Observation.xsd`
- representative command/status/capability structures in the pinned code/schema tree.

**Evidence note:** OSUS-R is a reference implementation and executable information/interface model, not a normative external SDO standard in the same sense as OGC/ISO/IEEE. Its strength here is direct implementation evidence from the unattended-sensor community. The frozen bibliography labels the pinned artifact “OSUS-R Contributors. 2026,” while the pinned revision itself resolves to a 22 February 2023 commit; this provenance discrepancy remains recorded and is not silently corrected in the frozen bibliography.

---

## 1. Source-native structural organization

OSUS-R organizes the unattended-sensor domain around the **Asset** as the consumer-facing whole device.

### A. Asset

`Asset` is defined as a physical device that typically:

- produces data; or
- responds to commands.

Examples include:
- motion detector;
- camera;
- UAV;
- security gate;
- valve actuator;
- engine;
- radio.

One Asset may have multiple sensors.

The Asset interface exposes the consumer-facing operational contract.

### B. AssetProxy

`AssetProxy` is the plug-in/implementation-side adapter for interacting with the physical hardware.

The core intentionally hides this plug-in implementation from consumers; all functionality needed by consumers should be reachable through `Asset`.

### C. AssetFactory / product type

Asset factories describe an Asset product/type and provide its `AssetCapabilities`.

This separates:
- product/factory capability definition; from
- individual Asset instance identity/state.

### D. AssetCapabilities

`AssetCapabilities` extends BaseCapabilities and organizes advertised support for:

- product name/description/manufacturer;
- sensing modalities;
- min/max/nominal range;
- min/max/nominal field of view;
- supported cameras;
- status capabilities;
- detection capabilities;
- digital-media capabilities;
- audio capabilities;
- image capabilities;
- video capabilities;
- command capabilities;
- observation capabilities;
- zeroize capabilities.

### E. Observation

`Observation` is a persistent data/result object with:

- its own UUID/version;
- source Asset UUID/name/type;
- optional sensor ID;
- observed and created timestamps;
- Asset position/orientation;
- platform orientation;
- pointing location;
- sensing modalities;
- test-mode state;
- related observations;
- one major observation payload type.

Observation payload types include:

- Detection;
- Status;
- Weather;
- WaterQuality;
- CBRNE trigger;
- Biological;
- Chemical;
- Power;
- digital media plus audio/image/video/channel metadata.

### F. Commands / Responses

Assets expose:

- generic command execution;
- command-specific schemas/types;
- Response types;
- event notifications for command responses/updates.

### G. Status / BIT

Asset status is represented through **Status Observations** and summary status values.

Built-In Test (BIT) returns Status and can update/persist status observations.

### H. Activation lifecycle

Asset has explicit operational lifecycle transitions:

- will activate;
- activation complete/failed;
- will deactivate;
- deactivation complete/failed.

The source-native pattern is therefore:

> **physical Asset instance → product/factory capabilities → hidden hardware plug-in → observations/status → commands/responses → operational activation/BIT/events**

---

## 2. Purpose of each partition

### Asset

Purpose: define the stable consumer-facing operational identity/contract for the whole physical device.

### AssetProxy

Purpose: isolate device-specific protocol/hardware implementation from the common Asset interface.

### AssetFactory / capabilities

Purpose: define what a product type supports and make capability information available before/independently from one runtime observation.

### AssetCapabilities

Purpose: advertise supported sensing modalities, outputs, performance envelope, status fields and commands.

### Observation

Purpose: persist source-attributed data produced by the Asset, including both sensing outputs and status/condition outputs.

### Command / Response

Purpose: represent control/tasking interaction separately from observation publication.

### Status

Purpose: represent current Asset/component operating state/health information.

### BIT

Purpose: explicitly test the Asset itself and return status after the test.

### Activation/deactivation

Purpose: govern when the OSUS runtime should initiate or cease communication/data/control behavior with the physical Asset.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Whole equipment | Asset, physical device, UUID/name/product type |
| Implementation adapter | AssetProxy, AssetContext, plug-in |
| Product/type | AssetFactory, FactoryDescriptor, product type |
| Capability | AssetCapabilities, modality, range/FOV, command/status/detection/media capability |
| Sensing internals | sensorId, supported cameras/sensors |
| Observation | Observation UUID, timestamps, source Asset, modality, payload type, related observations |
| Status | Status, SummaryStatusEnum, component status, status observation |
| Detection | Detection type, classification, location/range/orientation/speed, signatures, probability |
| Media | DigitalMedia, audio/image/video/channel metadata |
| Control | Command, Response, command capability, pan/tilt, mode, position, capture, zeroize, recording |
| Lifecycle | activation/deactivation events/state |
| Self-test | BIT / performBit |
| Communications | Asset-owned communication behavior/protocol handling |

---

## 4. Primary relationships

### Asset ↔ AssetProxy

One Asset consumer-facing object delegates custom/device-specific behavior to its plug-in AssetProxy.

The two are intentionally not the same interface role.

### Asset ↔ AssetFactory/product type

Asset instance is created/managed from an AssetFactory/product type whose capabilities describe the supported product behavior.

### Asset ↔ sensors

One Asset may have multiple sensors.

`captureData(sensorId)` and Observation `sensorId` preserve internal sensor/source identity without making every sensor the whole Asset.

### Asset ↔ Observation

Observation carries:
- Asset UUID;
- Asset name;
- Asset type;
- Asset position/orientation;
- optional internal sensor ID.

The core automatically fills many of these provenance fields.

### Observation ↔ related Observation

Observation can reference other observations with an explicit relationship type and description.

### Asset ↔ Status

The current/latest status is persisted as a Status Observation.

### Asset ↔ Command/Response

Command targets the Asset operational interface; Response returns command result/data.

### Asset ↔ communications

The Asset plug-in owns/handles the native communications/protocol to physical hardware.

The communications mechanism is implementation support, not the Asset identity itself.

---

## 5. Dependency boundaries

OSUS-R has several explicit implementation/domain boundaries.

### Consumer contract vs implementation

Consumers interact with `Asset`; they should not directly call `AssetProxy`.

This is a strong source-native separation between:
- domain/operational interface; and
- device-specific implementation adapter.

### Product/type vs instance

Capabilities are supplied by the AssetFactory/product definition, while runtime state/identity belongs to the individual Asset.

### Capability vs runtime output

AssetCapabilities says what the Asset can support; Observations/Status/Responses contain runtime information.

### Observation vs status

Status is modeled as an Observation subtype/content rather than as a separate unrelated storage system, but its semantic role remains distinct.

### Asset vs internal sensor

One Asset can expose multiple sensor IDs. Internal sensing element identity is subordinate to the whole Asset identity.

### Core-filled provenance vs plug-in payload

AssetProxy creates/returns Observation content; the core automatically sets:
- system ID;
- observation version;
- test mode;
- Asset UUID/name/type;
- timestamps;
- UUID;
- Asset location/orientation where applicable.

This separates domain-source provenance responsibility from device-specific content production.

---

## 6. Intrinsic vs contextual standing

### Intrinsic to Asset

- Asset UUID/name/product type;
- supported modalities/capabilities;
- native command support;
- internal sensors/cameras;
- Asset communication implementation;
- activation state;
- BIT support;
- status capability;
- intrinsic range/FOV/performance characteristics.

### Contextual/operational

- current Asset location/orientation;
- platform orientation;
- pointing location;
- test mode;
- current status;
- current captured observation;
- current command interaction.

### External/platform context

Platform orientation is carried distinctly from Asset orientation, showing that the platform is contextual rather than automatically identical to the Asset.

---

## 7. Cross-cutting concepts

Cross-cutting structures include:

- UUID identity;
- factory/product type;
- sensing modality;
- sensor ID;
- timestamps;
- location/orientation;
- test mode;
- status summary;
- observation provenance;
- event topics;
- command/response typing;
- media types;
- classifications.

These span multiple Observation and Asset interaction types.

---

## 8. State / temporal / lifecycle organization

OSUS-R has a clear **operational runtime lifecycle**.

### Activation lifecycle

- WILL_BE_ACTIVATED
- ACTIVATION_COMPLETE
- ACTIVATION_FAILED
- WILL_BE_DEACTIVATED
- DEACTIVATION_COMPLETE
- DEACTIVATION_FAILED

Activation generally begins communications with hardware and data/status behavior; deactivation generally ceases communication.

### Capture/activity state

Asset exposes whether it is:
- capturing data;
- performing BIT.

### Status state

Status uses summary status values and description.

Status change is published as an event and persisted as a Status Observation.

### Observation time

Observation distinguishes:
- observed timestamp;
- created timestamp.

### Test mode

Observation records whether the producing system was in test mode.

### Limit

The pinned OSUS-R model does not expose a comprehensive long-term equipment lifecycle equivalent to procurement/installation/service/work history; its strongest lifecycle structure is operational/runtime state plus persisted observations/events.

---

## 9. Composition / topology organization

OSUS-R is less explicit about general physical composition than AAS/MIMOSA/OPC, but it has several useful structures.

### Whole Asset vs internal sensors

An Asset can contain/support multiple sensor IDs.

### Cameras

AssetCapabilities can enumerate supported cameras and media capabilities.

### Component status

StatusCapabilities can enumerate component types for which the plug-in provides status.

### Communications

Every Asset is expected to have some communications mechanism handled by the plug-in.

### Platform context

Observation carries both:
- Asset orientation;
- platform orientation.

This implies distinction between the Asset and a platform it may be mounted on.

### Important limit

The pinned core does **not** define a generic recursive physical BOM/component hierarchy for arbitrary Asset internals. Its composition model is operationally oriented around sensors/cameras/status components rather than a universal assembly model.

---

## 10. Capability / function / behavior organization

Capability is a first-class source-native structure.

### Base product capability

BaseCapabilities supplies:
- product name;
- description;
- manufacturer;
- representative media/images.

### Asset capability

AssetCapabilities adds:
- sensing modalities;
- performance ranges/FOV;
- supported cameras;
- detection capability;
- status capability;
- media capability;
- command capability;
- observation capability;
- security/zeroize capability.

### Command capability

Command capability says whether the Asset supports operations such as:
- capture data;
- capture by sensor ID;
- BIT;
- mode/control operations;
- other command-specific functions.

### Observation capability

ObservationCapabilities says what optional fields/data the Asset can populate.

### Detection capability

DetectionCapabilities says what target/detection features can be provided.

The source therefore distinguishes:

> **supported capability → actual command/observation execution → produced result/status**

---

## 11. Information / output organization

OSUS-R has a rich observation taxonomy.

### Observation base

Every Observation carries common:
- source Asset identity;
- timing;
- test mode;
- location/orientation;
- modality;
- optional sensor ID.

### Observation payload specialization

A single Observation can carry one major payload family such as:
- Detection;
- Status;
- Weather;
- Water Quality;
- CBRNE trigger;
- Biological;
- Chemical;
- Power;
- Digital Media + audio/image/video/channel metadata.

### Related Observations

Observations can reference other observations by UUID with explicit relationship type.

### Status Observation

Status is represented/persisted as observation information while retaining its distinct semantic subtype.

### Command result

Command Response is separate from Observation.

The source-native information architecture therefore distinguishes **observation/result data, status observation, media payload, command response and event notification**.

---

## 12. Management / condition organization

OSUS-R has strong runtime management semantics.

### Activation/deactivation

Controls whether the Asset is actively communicating/operating.

### Status

The Asset maintains/persists current status and publishes changes.

### BIT

Built-In Test evaluates the Asset itself and yields Status.

### Command/control

Command interface supports:
- mode;
- position;
- pan/tilt;
- profiles;
- tune settings;
- recording;
- capture;
- zeroize;
- other device-specific behaviors.

### Configuration

AssetProxy receives Asset configuration properties through AssetContext.

### Security/zeroize

Capabilities can explicitly indicate support for zeroizing:
- keys;
- configuration;
- stored sensor data;
- code/firmware.

### Limit

The pinned model is strong on operational management and condition/status, but comparatively weak on maintenance work history, durable parts inventory and organizational asset lifecycle.

---

## 13. Provenance / identity / reference organization

OSUS-R makes source identity explicit in observations and events.

### Asset identity

Assets have:
- UUID;
- name;
- product/factory type.

### Observation identity

Observation has its own:
- UUID;
- version;
- created time;
- observed time;
- source Asset UUID/name/type;
- optional sensor ID;
- originating Terra Harvest system ID.

### Related observations

ObservationRef preserves related Observation UUID plus relationship type.

### Automatic provenance

Core populates source/provenance fields so plug-ins do not have to reproduce them independently.

### Product identity

AssetFactory/capabilities supply product name/description/manufacturer/type-level semantics.

The source therefore distinguishes **Asset instance identity, product/type identity, internal sensor identity and observation identity**.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Asset vs AssetProxy** — consumer-facing whole-device abstraction and device-specific implementation adapter are different.
2. **Asset instance vs AssetFactory/product type** — runtime instance and reusable product/capability definition are different.
3. **Asset vs internal sensor ID** — whole equipment and individual sensing element/channel are different scopes.
4. **Capability vs runtime observation/command** — supported functionality and actual output/execution are different.
5. **Observation vs Command Response** — sensed/status data and control result are different information types.
6. **Status Observation vs ordinary sensing Observation** — shared persistence envelope does not erase semantic difference.
7. **Asset orientation vs Platform orientation** — equipment pose and host-platform pose are distinct.
8. **observed timestamp vs created timestamp** — phenomenon/source time and object-creation time are different.
9. **Asset UUID vs Observation UUID** — persistent source identity and data-item identity are different.
10. **Asset type/product type vs Asset name/UUID** — product classification and instance identity differ.
11. **internal sensor identity vs modality** — which internal sensor produced data and what phenomenology/modalities are involved are different.
12. **activation state vs health/status** — being activated and being healthy are not the same.
13. **BIT result vs continuous/current status** — explicit self-test output and ongoing status should not be collapsed.
14. **native communications implementation vs Asset domain identity** — protocol handling is deliberately hidden behind the Asset interface.
15. **event topic vs persisted domain data** — runtime event notification and persistent Observation/Response are different mechanisms.
16. **component status availability vs recursive physical composition** — knowing status for a component type does not establish a complete BOM.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely core/intrinsic:** whole-device identity; product/type vs instance separation; internal sensor identity; advertised capability;
- **likely reusable structural pattern:** consumer-facing equipment abstraction separated from source-specific hardware/protocol adapter;
- **likely dynamic-information pattern:** observation/status/command-response separation with common source provenance;
- **likely management pattern:** activation, status, BIT, configuration and command behavior;
- **likely capability pattern:** modality/performance/output/command/status/media capability declared before runtime use;
- **likely provenance pattern:** automatic persistent source identity on every Observation plus internal sensor ID;
- **likely contextual relationship pattern:** Asset vs host-platform orientation/pose;
- **specialization evidence:** UGS/device operations such as capture, pan/tilt, recording, zeroize, detection features;
- **composition limit:** OSUS-R does not itself supply a universal recursive equipment BOM, so its internal-sensor/component structures should not be over-generalized;
- **binding/implementation caution:** Asset, AssetProxy, event topics, JAXB/protobuf structures and Java interfaces are OSUS-R implementation constructs and are not automatically V2 resources/classes.

**No V2 module disposition is made in Phase A.**

---

**C11 status: COMPLETE.**

**Next frozen lineage:** C12 — SAPIENT.

---

# C12 — SAPIENT / BSI Flex 335 v2.0

## Source basis and evidence ceiling

**Frozen primary source ID:** 21.  
**Frozen companion IDs:** 22–25.

**Primary inspected source:**

- British Standards Institution, *BSI Flex 335 v2.0:2024-03: SAPIENT Network of Autonomous Sensors and Effectors — Interface Control Document — Specification*, March 2024.

**Companion evidence:**

- official Dstl guidance;
- pinned SAPIENT Protocol Buffer schemas;
- Apex SAPIENT Middleware;
- BSI Flex 335 v2 Test Harness.

**Evidence note:** BSI Flex 335 is primarily an interface-control specification, but it defines substantive source-native domain structure and therefore participates in anatomy Phase A. Companion schemas/test/middleware are implementation evidence only; they do not receive independent semantic weight.

---

## 1. Source-native structural organization

SAPIENT organizes its domain around a **system-of-systems network of Nodes** communicating at the information level.

### A. System architecture

The typical architecture contains:

1. **Edge Nodes**
   - sensor edge nodes;
   - effector nodes;
   - nodes that can act as both sensor and effector.

2. **Fusion Node**
   - receives node declarations/detections/status;
   - performs fusion/correlation/de-confliction/task optimization;
   - generates tracks/entities/alerts/tasking.

3. **Message Handling Application**
   - optional transparent middleware layer between edge/fusion nodes;
   - does not own/change message semantics when used in the transparent configuration.

4. **GUI / external systems**
   - outside the core standardized node-to-fusion interface in v2.0.

### B. Node classification

Registration uses one or more **NodeDefinition / NodeType** values such as:

- Radar;
- Lidar;
- Camera;
- Seismic;
- Acoustic;
- Proximity Sensor;
- Passive RF;
- Human;
- Chemical;
- Biological;
- Radiation;
- Kinetic;
- Jammer;
- Cyber;
- Laser/RF directed-energy;
- Mobile Node;
- Pointable Node;
- Fusion Node.

### C. Node self-description / registration

Registration includes:

- node definition/type;
- ICD version;
- name/short name;
- capabilities;
- status-message definition;
- supported modes;
- dependent-node IDs;
- ConfigurationData.

### D. Capability and mode

A Node declares:

- capability category/type/value/units;
- supported Modes;
- mode behavior;
- mode timing;
- detection definitions;
- tracking type;
- scan type;
- tasking interactions;
- performance implications.

### E. Configuration / subcomponents

ConfigurationData includes:

- manufacturer;
- model;
- serial number;
- hardware version;
- software version;
- recursive `sub_components`.

### F. Runtime message partitions

The core message families include:

- Registration;
- Status;
- Detection;
- Task;
- Task Acknowledgement;
- Alert;
- Error;
- corresponding acknowledgements/responses.

All are wrapped in a common SapientMessage with source node ID/timestamp and optional destination.

### G. Platform architecture

SAPIENT explicitly models:

- Mobile Node;
- Pointable Node;
- dependent edge/platform nodes;
- stacked platform dependencies.

### H. Hierarchical fusion architecture

Fusion Nodes can be recursively arranged:
- lower-level fusion node behaves upward as an edge node;
- declares aggregated detection/tasking capability;
- higher-level fusion nodes can aggregate regions/platforms.

The source-native pattern is therefore:

> **Node type + registration/self-description + capability/mode + recursive configuration + status/detection/task/alert runtime exchange + platform dependency + recursive fusion hierarchy**

---

## 2. Purpose of each partition

### Edge Node

Purpose: provide a modular autonomous sensing/effecting participant whose modality-specific implementation is hidden behind one common interface.

### Fusion Node

Purpose: combine information from multiple Nodes and coordinate tasking/decision support.

### Registration

Purpose: declare **what the Node is and what it can do** before regular operations:
- type;
- capability;
- modes;
- status fields;
- configuration;
- dependencies.

### Capability

Purpose: communicate modality/function/performance information that helps the Fusion Node interpret and task the Node.

### Mode

Purpose: describe a distinct way of operating, including:
- behavior;
- timing;
- detections;
- tracking/scan behavior;
- tasking options;
- performance implications.

### Status

Purpose: heartbeat/current Node state:
- overall system status;
- current task;
- current mode;
- power;
- location;
- field of view;
- coverage;
- obscuration;
- status values.

### Detection

Purpose: report detection/classification/track information about real-world objects.

### Task

Purpose: direct taskable Nodes to start/stop/pause/default a region-based or command-based task.

### Task Acknowledgement

Purpose: represent acceptance/rejection/completion/failure of a task separately from the task request.

### Alert

Purpose: represent non-detection notable information/conditions requiring GUI or Fusion Node attention and possible permission/response.

### Platform Node

Purpose: represent movement/pointing dependencies that affect subordinate edge Nodes.

### Hierarchical Fusion

Purpose: allow recursively nested fusion/coordination while preserving a level-agnostic Node interface.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Whole architecture | Edge Node, Fusion Node, Message Handling Application, GUI |
| Node identity/type | node_id UUID, NodeDefinition, NodeType, name/short name |
| Self-description | Registration, Capability, ModeDefinition, StatusDefinition, ConfigurationData |
| Product/configuration | manufacturer, model, serial, hardware/software version, sub_components |
| Capability | category, type, value, units, modality/function |
| Mode | mode name/behavior/timing, detection definition, scan type, tracking type, mode parameters |
| State | StatusReport, System status, Info/newness, active task, mode, power, location, FOV, coverage, obscuration |
| Observation-like output | DetectionReport, object_id, location/range-bearing, confidence, track/object info, classification |
| Tasking | Task, Region, Command, task start/end time, control, TaskAck |
| Alerting | Alert, AlertType, AlertStatus, priority, ranking, location/region |
| Platform dependency | MobileNode, PointableNode, dependent_nodes, FollowObject |
| Hierarchy | parent/child Fusion Nodes, aggregated capabilities, coverage areas |
| Message identity | report/task/alert ULIDs, source/destination Node IDs, timestamps |

---

## 4. Primary relationships

### Edge Node ↔ Fusion Node

Edge Nodes register to a Fusion Node, report status/detections/alerts and receive Tasks.

### Node ↔ capabilities/modes/status definition

Registration binds a Node's identity to the capabilities, status fields and operating modes it supports.

### Node ↔ subcomponents

ConfigurationData can recursively describe subcomponents.

### Platform Node ↔ dependent Nodes

A Mobile/Pointable platform Node declares UUIDs of dependent Nodes affected by platform commands/motion.

### Fusion hierarchy

A child Fusion Node can:
- register with a parent Fusion Node;
- appear as an edge Node upward;
- present aggregated detection/tasking capabilities of lower Nodes.

### Task ↔ Detection

Detection reports may reference the task ID active when the detection occurred.

### Detection ↔ object/track

Detection report has:
- report ID;
- object ID;
- classification;
- location;
- confidence;
- track/object metadata;
- predicted location.

### Task ↔ acknowledgement

TaskAck references task ID and reports:
- accepted;
- rejected;
- completed;
- failed.

### Alert ↔ response/status

Alert can be:
- active;
- acknowledged;
- rejected;
- ignored;
- cleared.

### Node ↔ platform/location/FOV

Status reports provide current spatial/operational context separately from registration identity.

---

## 5. Dependency boundaries

SAPIENT intentionally separates several layers.

### Registration/self-description vs runtime messages

Registration declares what Node data/actions/status/modes are possible; Status/Detection/Task/Alert carry current runtime interactions.

### Node domain model vs middleware

Message Handling Application may transport/store messages but is transparent to Node/Fusion semantics.

### Node vs modality-specific implementation

Different sensor/effector modalities use the same interface and expose only supported/available fields.

### Capability vs Mode

Capability identifies general functionality; Mode describes a distinct operational configuration/behavior and its performance/tasking implications.

### Edge/fusion identity vs hierarchy role

A child Fusion Node remains a Fusion Node internally but behaves toward its parent as an edge Node, demonstrating that interface role and internal architecture can differ.

### Platform dependency vs sensor/effector function

Platform Node handles movement/pointing dependencies; dependent sensor/effector Nodes retain their own intrinsic tasking/capabilities.

### Summary information vs raw data

SAPIENT is deliberately information-level; raw sensor data is outside the core concept, even though implementations may add access mechanisms.

---

## 6. Intrinsic vs contextual standing

### Intrinsic to Node self-description

- Node type(s);
- capabilities;
- supported modes;
- product/configuration metadata;
- recursive subcomponents;
- accepted task types;
- status field definitions.

### Current operational state

- active task;
- current mode;
- power;
- system status;
- location;
- FOV;
- coverage;
- obscuration;
- performance/status values.

### Contextual/relational

- parent Fusion Node;
- dependent Nodes;
- platform relationship;
- hierarchy level;
- regions/tasks assigned by Fusion Node;
- network/server/client role.

### Derived/aggregated

Child Fusion Node can advertise aggregated capability and coverage of subordinate Nodes. These are **network/fusion-level representations**, not necessarily intrinsic physical capability of one device.

---

## 7. Cross-cutting concepts

Cross-cutting SAPIENT structures include:

- Node UUID;
- ULID message/object/task/alert identifiers;
- timestamp;
- location/range-bearing;
- region;
- mode;
- task ID;
- capability;
- classification;
- confidence/probability;
- units;
- performance/error;
- hierarchy/dependency;
- acknowledgements;
- connection/heartbeat status.

These recur across registration, status, detections and tasking.

---

## 8. State / temporal / lifecycle organization

SAPIENT has a clear **network participation and operational lifecycle**.

### Initialization

1. Node connects.
2. Node sends Registration.
3. Registration acknowledgement.
4. Node sends initial Status.
5. Sensor edge Node begins default detection or effector awaits tasking.

### Normal operation

- regular Status heartbeats;
- Detection reports;
- Alerts;
- Tasks;
- task acknowledgements;
- fusion processing.

### Task lifecycle

Task:
- start;
- pause;
- stop;
- default.

Task status:
- accepted;
- rejected;
- completed;
- failed.

### Node shutdown

Node sends Status with system field GOODBYE.

### Connection recovery

Nodes/fusion monitor connection and reconnect. Re-registration depends on outage duration.

### Hierarchy dynamics

Edge/fusion Nodes may go on/off-line; child Fusion Nodes update coverage/status accordingly.

### Limit

This is an operational/network lifecycle, not a durable equipment maintenance/service lifecycle.

---

## 9. Composition / topology organization

SAPIENT has three separate topology structures.

### A. Configuration/subcomponent hierarchy

ConfigurationData recursively describes product subcomponents.

### B. Platform dependency topology

Platform Nodes declare dependent Node IDs.

Dependencies can be stacked:
- mobile platform;
- pointable platform;
- sensor/effector edge Nodes.

This relationship means tasking/movement of platform affects dependent Nodes.

### C. Fusion/network hierarchy

Fusion Nodes can be recursively nested across:
- local regions;
- vehicles/structures;
- higher-level multi-structure coordination.

### Important distinction

**subcomponent hierarchy, platform dependency and fusion hierarchy are not the same relationship.**

A Fusion Node may physically reside on a platform but still has distinct Fusion and Platform Node definitions/roles.

---

## 10. Capability / function / behavior organization

SAPIENT capability is explicitly declared and mode-dependent.

### General capability

Registration Capability fields state:
- category;
- type;
- value;
- units.

### Sensor/effector Node type

NodeDefinition establishes broad modality/role.

### Mode-specific capability

Mode defines:
- detection content;
- task acceptance;
- scan behavior;
- tracking behavior;
- performance implications.

### Status-field capability

Registration declares what status categories/fields will be reported and whether values are periodic or on-change.

### Aggregated capability

Child Fusion Node can present combined capability of subordinate Nodes.

### Behavior/tasking

Tasks can specify:
- region;
- command;
- start/end;
- start/stop/pause/default.

This yields a source-native distinction among:

> **general capability → mode-specific behavior/performance → current mode/status → task request → task acknowledgement/resulting detections**

---

## 11. Information / output organization

SAPIENT deliberately separates several runtime information kinds.

### Registration

Static/self-descriptive declaration.

### Status

Current operational/health/context heartbeat.

### Detection

Object detection/classification/track information.

### Alert

Non-detection event/attention/permission information.

### Task

Requested action/objective.

### TaskAck

Task response/progress status.

### Error

Interface/validation error.

### Fused output

Fusion Nodes can produce:
- fused detections/tracks;
- alerts;
- subsequent tasking.

### Raw data

Raw sensor data is explicitly not the core information-level SAPIENT exchange, though an implementation may provide it separately.

---

## 12. Management / condition organization

Management is central to SAPIENT's operational concept.

### Registration/configuration management

Fusion Node knows:
- what Nodes are present;
- what they can do;
- modes;
- configuration;
- dependencies.

### Status/heartbeat

All Nodes send regular status.

Status covers:
- internal/external faults;
- power;
- mode;
- sensor performance;
- weather/clutter/exposure;
- location/FOV/coverage;
- platform state.

### Task management

Fusion Node allocates Tasks and receives acknowledgement/status/detections.

### Alert/permission management

Nodes can request/report conditions requiring accept/reject/acknowledge/clear behavior.

### Connectivity management

Nodes/Fusion monitor and restore message-channel connectivity.

### Limit

The standard does not define a universal maintenance/work-order/service-history domain; management is focused on real-time autonomous network operation.

---

## 13. Provenance / identity / reference organization

SAPIENT uses explicit source and message identifiers.

### Node identity

Every Node has UUID.

### Message identity

Reports/tasks/alerts use ULIDs and timestamps.

### Object identity

Detection has `object_id`, distinct from report ID.

### Task relationship

Detection can cite task ID; TaskAck cites task ID.

### Configuration identity

Manufacturer/model/serial/hardware/software version identify the product/subcomponent.

### Dependency reference

Platform dependencies and hierarchy use Node UUIDs.

### Version identity

Registration declares ICD version.

The source therefore distinguishes:

- Node identity;
- product/component identity;
- message/report identity;
- detected-object identity;
- task identity;
- protocol/version identity.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Node vs physical device** — Node is an interoperability/domain participant and can represent sensor, effector, platform, fusion, human or other roles.
2. **Edge Node vs Fusion Node** — local sensing/effecting and higher-level fusion/coordination are distinct functions.
3. **Node type vs capability** — broad role/modality and detailed supported function/performance are separate.
4. **Capability vs Mode** — general functionality and one distinct operational behavior/configuration are different.
5. **Mode definition vs current mode** — supported modes and runtime selected mode are different.
6. **Registration status definition vs Status message** — what will be reported and current reported values are distinct.
7. **Registration vs runtime Status/Detection/Task/Alert** — self-description and live interaction are separate.
8. **Status vs Detection vs Alert** — Node state, observed object information and exceptional/attention information have different semantics.
9. **Task vs TaskAck** — requested action and acceptance/completion/failure are separate.
10. **Detection report ID vs detected object ID** — message identity and target/object identity differ.
11. **Node location vs detection location** — sensor/platform position and observed-object position are different.
12. **FOV vs coverage vs obscuration** — current viewed area, total reachable area and blocked area are distinct.
13. **subcomponent hierarchy vs dependent-node/platform relationship** — product structure and operational dependency are different.
14. **platform dependency vs Fusion hierarchy** — movement/pointing dependency and information-fusion hierarchy are different.
15. **child Fusion Node internal role vs edge-node interface role to parent** — internal architecture and external role can differ.
16. **individual capability vs aggregated fusion capability** — aggregate representation is not intrinsic to a single subordinate device.
17. **information-level summary vs raw sensor data** — core SAPIENT exchange and raw payload are intentionally different.
18. **message handling middleware vs Fusion Node semantics** — transparent transport/storage layer does not own domain meaning.
19. **connection lifecycle vs equipment lifecycle** — initialization/reconnect/shutdown should not become maintenance history.
20. **sensor task vs platform task** — sensing behavior and movement/pointing control have different responsibility.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely reusable structural pattern:** self-description/registration separated from runtime state, observations, alerts and tasking;
- **likely capability pattern:** general capability + mode-specific behavior/performance + current mode;
- **likely composition pattern:** recursive subcomponent metadata distinct from operational dependency;
- **likely contextual relationship pattern:** platform/dependent-Node structure and hierarchical fusion;
- **likely dynamic-information pattern:** Status, Detection, Alert, Task, TaskAck as distinct information kinds;
- **likely management pattern:** heartbeat/status, connectivity, autonomous task allocation and permission/alert handling;
- **likely provenance pattern:** distinct Node/message/object/task/product identities;
- **likely specialization evidence:** distributed autonomous multi-sensor/effector systems and fused track/tasking structures;
- **binding/architecture caution:** Node, Fusion Node, messages, client/server roles and SAPIENT hierarchy are SAPIENT-native interoperability constructs, not automatically V2 classes/resources;
- **aggregation caution:** fusion-level aggregated capability/coverage must not be mistaken for intrinsic capability of one physical equipment System.

**No V2 module disposition is made in Phase A.**

---

**C12 status: COMPLETE.**

**Next frozen lineage:** C13 — SAREF.

---

# C13 — SAREF Core 4.1.1

## Source basis and evidence ceiling

**Frozen primary source ID:** 144.

**Primary inspected source:**

- ETSI, *SAREF: Smart Applications REFerence Ontology — Core*, version 4.1.1:
  - `https://saref.etsi.org/core/v4.1.1/`

**Evidence note:** SAREF Core is an ontology, not an API or device-management protocol. It intentionally separates generic kinds/archetypes from specific real-world entities and network-exposed services/operations. The extraction stays within SAREF Core 4.1.1 plus the SAREF4SYST relationships explicitly referenced by SAREF Core; it does not import unrelated SAREF extensions merely because they exist.

---

## 1. Source-native structural organization

SAREF Core organizes its domain into a set of interrelated semantic layers.

### A. Real-world feature layer

- **FeatureOfInterest**
  - any specific real-world entity whose properties/states can be observed or controlled.

- **FeatureKind**
  - archetype/kind of features.

- **Device**
  - tangible FeatureOfInterest designed to accomplish a task by performing functions;
  - also a `s4syst:System`.

- **DeviceKind**
  - archetype/model of devices;
  - can specify common properties, states, functions, services and targets.

### B. Device-role specializations

Examples include:

- Sensor;
- Actuator;
- Meter;
- Appliance.

Sensor is a Device designed to observe/measure properties or states of features of interest.

### C. Composition/system layer

- `saref:consistsOf` for composite features/devices/kinds;
- SAREF4SYST System, Connection and ConnectionPoint when system engineering detail is needed.

### D. Property/state semantics

SAREF distinguishes:

- **Property**
  - generic quality that can apply to different feature kinds/entities.

- **PropertyOfInterest**
  - property specific to exactly one FeatureOfInterest.

- **PropertyValue**
  - value for a property/property of interest.

- **State**
  - generic state.

- **StateOfInterest**
  - state specific to one feature.

- **StateValue**
  - value of a State/StateOfInterest.

### E. Function/capability semantics

- **Task**
- **Function**
  - reusable logical group of commands a device can support.
- **FunctionOfInterest**
  - actual function supported by exactly one Device.
- **Command**
  - reusable command kind.
- **CommandOfInterest**
  - command specific to a FunctionOfInterest/device.

### F. Network-service semantics

- **Service**
  - digital representation of a FunctionOfInterest in a network.

- **Operation**
  - network-exposed operation belonging to exactly one Service;
  - represents one or more CommandOfInterest instances.

### G. Execution/result semantics

- **ProcedureExecution**
- **Observation**
- **Actuation**
- **CommandExecution**
- **OperationExecution**

Executions can have:
- inputs;
- outputs;
- result;
- phenomenon time;
- executor/device;
- targeted feature/property/state.

### H. Profile/commodity semantics

- **Profile**
  - device/profile information relevant to consumption/production/storage over conditions/time.
- **Commodity**
  - what a device consumes, produces or stores.

The source-native pattern is therefore:

> **feature/device identity + kind/archetype + composition/system + property/state semantics + task/function/command + network service/operation + execution/result**

---

## 2. Purpose of each partition

### FeatureOfInterest / FeatureKind

Purpose: distinguish a particular real-world entity from its reusable archetype/kind.

### Device / DeviceKind

Purpose: specialize FeatureOfInterest/FeatureKind for tangible task-performing systems and product/model-like descriptions.

### Sensor/Actuator/Meter/Appliance

Purpose: classify Devices by functional role without changing their tangible Device nature.

### Property vs PropertyOfInterest

Purpose: distinguish a generic property kind (e.g. temperature) from the particular temperature property **of one specific feature**.

### State vs StateOfInterest

Purpose: make the same distinction for states.

### Function vs FunctionOfInterest

Purpose: distinguish reusable logical function kinds from the actual function supported by one particular Device.

### Command vs CommandOfInterest

Purpose: distinguish reusable command semantics from the concrete command supported by one particular Function/Device.

### Service

Purpose: represent a Device's FunctionOfInterest digitally in a network.

### Operation

Purpose: provide a network-operation realization of one or more CommandsOfInterest.

### ProcedureExecution

Purpose: represent an actual execution/occurrence of a command/operation/observation/actuation with inputs, outputs, result and time.

### Profile

Purpose: describe device behavior/performance related to commodity consumption/production/storage under relevant conditions.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Real-world subject | FeatureOfInterest, Device |
| Kind/model | FeatureKind, DeviceKind |
| Composition/system | consistsOf, s4syst:System, Connection, ConnectionPoint |
| Functional role | Sensor, Actuator, Meter, Appliance |
| Property | Property, PropertyOfInterest, PropertyValue, UnitOfMeasure |
| State | State, StateOfInterest, StateValue |
| Task/function | Task, Function, FunctionOfInterest |
| Command | Command, CommandOfInterest |
| Network representation | Service, Operation |
| Execution | ProcedureExecution, Observation, Actuation, CommandExecution, OperationExecution |
| Target relationship | targets, observes, controls |
| Profile/energy | Profile, Commodity, consumes, produces, stores |

---

## 4. Primary relationships

### Feature/Device → kind

- `hasFeatureKind`
- `hasDeviceKind`

Specific entities inherit broader kind semantics.

### Composite entity → parts

- `consistsOf`

Can apply to:
- FeatureKind;
- FeatureOfInterest;
- Device structures;
- composite property/state values.

### Device → functions

- `hasFunction` for reusable/general function semantics.
- `hasFunctionOfInterest` for the concrete function of one Device.

### Function → commands

Functions can have:
- mandatory commands;
- optional commands.

FunctionOfInterest can have concrete CommandOfInterest.

### Device → Service → Operation

- Device `offers` Service.
- Service represents FunctionOfInterest.
- Service `hasOperation`.
- Operation represents Command/CommandOfInterest.

### Device/function/command/execution → target

- `targets`;
- `observes`;
- `controls`

can point to:
- FeatureOfInterest;
- Property/PropertyOfInterest;
- State/StateOfInterest.

### Feature → PropertyOfInterest / StateOfInterest

A PropertyOfInterest/StateOfInterest belongs to exactly one FeatureOfInterest.

### Execution → executor/result/time

ProcedureExecution can be:
- madeBy a Device/Feature;
- linked to executed command/operation;
- given input/output/result;
- assigned phenomenon time.

---

## 5. Dependency boundaries

SAREF makes several semantic layers independent.

### Kind vs individual

FeatureKind/DeviceKind describe reusable archetypes; FeatureOfInterest/Device describe specific real-world entities.

### Generic property/function vs instance-specific property/function

Property, State, Function and Command can apply broadly; the corresponding *OfInterest* classes bind the concept to a specific entity.

### Device domain vs network service

Service/Operation are digital/network representations of Device functions/commands, not the Device itself.

### Function vs command

Function is a logical grouping of commands; Command is one action.

### Command vs execution

Command semantics and one actual CommandExecution are different.

### Property vs value

Property meaning and PropertyValue are different.

### Device vs system engineering detail

Device is also a SAREF4SYST System, but SAREF Core refers to SAREF4SYST when Connection/ConnectionPoint/system-topology detail is needed.

---

## 6. Intrinsic vs contextual standing

### Intrinsic to Device

- Device identity;
- DeviceKind/model;
- functions;
- FunctionsOfInterest;
- offered services;
- composition;
- manufacturer/model;
- intrinsic properties/states;
- commodity consumption/production/storage patterns.

### Contextual/target-related

- FeatureOfInterest being observed/controlled;
- PropertyOfInterest/StateOfInterest of that feature;
- network Service/Operation;
- spatial geometry/topological relationship;
- actual execution time/results.

### Execution/event-specific

- Observation;
- Actuation;
- CommandExecution;
- inputs;
- outputs;
- phenomenon time;
- result.

The model therefore distinguishes **what a Device is/can do** from **what it targets** and **what happened in one execution**.

---

## 7. Cross-cutting concepts

Cross-cutting structures include:

- `consistsOf`;
- kind/archetype inheritance;
- targets/observes/controls;
- manufacturer/model;
- tasks;
- units;
- time;
- inputs/outputs/results;
- profiles;
- geometry/spatial relations;
- commodity relations.

The *OfInterest* pattern is itself cross-cutting, appearing for:
- property;
- state;
- function;
- command.

---

## 8. State / temporal / lifecycle organization

SAREF Core has strong **state and execution-time semantics**, but not a general equipment-service lifecycle.

### State semantics

- State;
- StateOfInterest;
- StateValue.

A Device/Feature can have current/state-related values distinct from Property values.

### Execution time

ProcedureExecution can have:
- phenomenon time;
- result time/applicable time where modeled through supporting time semantics.

### Profile time/conditions

Profiles can describe behavior under time/conditions.

### Limit

SAREF Core does not define:
- installation history;
- maintenance work;
- replacement events;
- service lifecycle

as one core model. Those are extension/application concerns.

---

## 9. Composition / topology organization

### Composition

`consistsOf` supports composite FeatureKinds/Features/Devices and composite values.

### System structure

Device is also a `s4syst:System`.

When detailed system topology matters, SAREF recommends SAREF4SYST:
- System;
- Connection;
- ConnectionPoint.

### Spatial topology

FeatureOfInterest/Device can use GeoSPARQL geometry and topological relations.

### Important distinction

**composition, system connection and spatial relation are separate relationships.**

`consistsOf` should not be used as a substitute for Connection or spatial containment merely because two things are related.

---

## 10. Capability / function / behavior organization

SAREF has a highly explicit function/command hierarchy.

### Task

Represents what an entity accomplishes.

### Function

Reusable logical grouping of Commands.

### FunctionOfInterest

Concrete Function supported by one Device.

### Commands

Functions can declare:
- mandatory Commands;
- optional Commands.

### CommandOfInterest

Actual command supported by one FunctionOfInterest.

### Service/Operation

Network Service exposes FunctionOfInterest.

Operation exposes CommandOfInterest.

This creates a source-native chain:

> **Device → FunctionOfInterest → CommandOfInterest → Service → Operation → Execution**

with reusable **Function/Command kinds** separate from instance-specific functions/commands.

---

## 11. Information / output organization

SAREF distinguishes several information forms.

### Property/State value

Represents descriptive/current values about a Feature/Device.

### Observation

Represents a procedure execution that observes a Feature/Property/State and yields a result.

### Actuation

Represents a procedure execution controlling a target.

### Command/Operation execution

Represents execution of action semantics.

### Composite values

PropertyValue/StateValue can themselves be composed to represent richer result structures.

### Network Service output

Operations can have explicit inputs/outputs.

The source therefore distinguishes **property/state semantics, value, observation/actuation execution and service/operation output**.

---

## 12. Management / condition organization

SAREF Core has no monolithic management module, but several management-relevant structures.

### Device state/properties

Device-specific PropertiesOfInterest/StatesOfInterest and their values can express operating/condition state.

### Functions/commands

Management actions can be modeled through Functions/Commands.

### Service/operation

Remote management exposure is modeled as Service/Operation rather than fused into Device identity.

### Profiles

Profiles can express expected behavior/consumption patterns.

### Limit

Health/fault/maintenance/work concepts are not a comprehensive source-native partition in Core 4.1.1.

---

## 13. Provenance / identity / reference organization

SAREF distinguishes multiple semantic identity levels.

### Real-world entity identity

FeatureOfInterest / Device identify specific entities.

### Kind/model identity

FeatureKind / DeviceKind identify archetypes/models.

### Instance-specific semantic identity

- PropertyOfInterest;
- StateOfInterest;
- FunctionOfInterest;
- CommandOfInterest

tie reusable semantics to one entity.

### Execution identity

Observation/Actuation/CommandExecution/OperationExecution identify particular occurrences.

### Network representation identity

Service and Operation identify discoverable network representations separate from real-world Device identity.

### Result provenance

`madeExecution` / `madeBy` links execution to Device/Feature, while observation/actuation links execution to the target and result.

This provides explicit **source/executor provenance** without equating network service and physical source.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **FeatureOfInterest vs Device** — all Devices are Features of Interest, but not every Feature of Interest is a Device.
2. **Device vs DeviceKind** — specific real-world equipment and reusable model/archetype are different.
3. **Device vs Sensor/Actuator/Meter role** — Device is the tangible subject; subclasses characterize intended function.
4. **FeatureKind vs FeatureOfInterest** — type/archetype and individual entity are different.
5. **Property vs PropertyOfInterest** — generic property and the property of one specific feature are different.
6. **State vs StateOfInterest** — generic state and specific entity state are different.
7. **Property/State vs PropertyValue/StateValue** — meaning and value are separate.
8. **Function vs FunctionOfInterest** — reusable function kind and the actual function of one Device are different.
9. **Command vs CommandOfInterest** — generic command semantics and specific device-supported command are different.
10. **Function vs Command** — function groups actions; command is an action.
11. **Device vs Service** — tangible real-world equipment and digital network representation are different.
12. **Service vs Operation** — service groups/exposes function; operation is one network-accessible command interface.
13. **Command/Operation vs Execution** — action definition and one occurrence are different.
14. **Device/Function/Command vs target Feature/Property/State** — actor and target are different.
15. **consistsOf vs system Connection** — composition and connection are distinct.
16. **composition vs spatial relation** — being composed of and being spatially within/adjacent are different.
17. **Observation vs PropertyValue** — execution/result event and value object are different.
18. **kind inheritance vs current instance state** — inherited model semantics and live values are different.
19. **network representation vs physical composition** — Services/Operations do not become physical subcomponents.
20. **Core semantics vs extension-specific domain semantics** — Core provides reusable primitives rather than every domain vocabulary.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely core/intrinsic:** Device vs DeviceKind; composition; function/action semantics; intrinsic property/state distinctions;
- **likely reusable semantic pattern:** generic kind → entity-specific *OfInterest* → value/execution;
- **likely capability pattern:** Task → Function → Command, with instance-specific Function/CommandOfInterest;
- **likely network/binding separation:** Device → Service → Operation distinct from physical/domain identity;
- **likely output pattern:** Observation/Actuation/Execution separated from Property/State values;
- **likely target/context pattern:** Device/function/action can target Feature, Property or State without absorbing that target into the Device;
- **likely topology pattern:** composition, connection and spatial relation remain distinct;
- **likely provenance pattern:** madeBy/madeExecution plus target/result relationships;
- **profile-gap signal:** detailed equipment health, maintenance and lifecycle structures require other donors/extensions;
- **binding/ontology caution:** OWL class/property structure and SAREF4SYST references are ontology mechanisms; V2 must not mechanically mirror the class hierarchy without testing its information needs.

**No V2 module disposition is made in Phase A.**

---

**C13 status: COMPLETE.**

**Next frozen lineage:** C14 — SOSA/SSN.

---

# C14 — SOSA/SSN

## Source basis and evidence ceiling

**Frozen primary source ID:** 19.  
**Frozen companion IDs:** 18, 20.

**Controlling source:**

- W3C/OGC, *Semantic Sensor Network Ontology — 2023 Edition*, Working Draft, **21 October 2026**, OGC 25-022:
  - `https://www.w3.org/TR/vocab-ssn-2023/`

**Companion lineage:**

- 12 October 2026 Working Draft.
- 2017 W3C Recommendation.

**Evidence note:** The 21 October 2026 document is a Working Draft, not yet a W3C Recommendation. It controls current structural interpretation because it is the later frozen source. The 2017 Recommendation is retained as historical lineage evidence where the 2023 Edition explicitly changes/deprecates structures.

---

## 1. Source-native structural organization

The 2023 Edition is explicitly **modular**.

### A. SOSA core modules

The minimal/core vocabulary is split into:

- **SOSA Common**
- **SOSA Actuation**
- **SOSA Observation**
- **SOSA Sampling**
- combined SOSA

### B. SSN modules

Fuller axiomatization mirrors the same partition:

- **SSN Common**
- **SSN Actuation**
- **SSN Observation**
- **SSN Sampling**
- combined SSN

### C. Common domain structure

SOSA Common organizes:

1. **FeatureOfInterest and Property**
2. **Procedure**
3. **Execution / ExecutionCollection**
4. **Asset / System / Platform / Deployment**
5. **Collections / membership**

### D. Specialized execution structures

#### Observation module
- Sensor
- ObservingProcedure
- Observation
- ObservationCollection
- Stimulus
- observed Property
- FeatureOfInterest
- result / result quality

#### Actuation module
- Actuator
- ActuatingProcedure
- Actuation
- ActuationCollection
- Property acted on
- FeatureOfInterest
- result

#### Sampling module
- Sampler
- SamplingProcedure
- Sampling
- SamplingCollection
- Sample
- MaterialSample
- SpatialSample
- StatisticalSample
- SampleCollection
- original/ultimate sample relationships

### E. Deployment/system structure

- Asset
- System
- Platform
- Deployment
- hasSubSystem
- hosts / isHostedBy
- deployedAsset / deployedSystem / deployedOnPlatform
- implements Procedure
- madeExecution

### F. Extension modules

The document separately provides:

- OMS extension;
- Sample Relations;
- **System Capabilities** extension.

### G. System Capabilities extension

The non-normative System Capabilities Module separates:

- System capabilities;
- Operating Conditions;
- Normal Operating Conditions;
- Suboptimal Operating Conditions;
- Survivable Conditions;
- validity context.

Capabilities and operating conditions are represented using Observation/ObservationCollection patterns rather than the 2017 edition's explicit SystemProperty/OperatingProperty/SurvivalProperty hierarchies.

The source-native anatomy is therefore:

> **Feature/Property + reusable Procedure + Execution + System/Deployment + specialized Observation/Actuation/Sampling modules + optional Capability/Operating-Condition extensions**

---

## 2. Purpose of each partition

### FeatureOfInterest / Property

Purpose: identify the real-world target and quality/state/property relevant to an execution.

### Procedure

Purpose: define a reusable workflow, protocol, plan, algorithm, program or computational method that can be applied in many Executions.

### Execution

Purpose: represent one actual carrying-out of a Procedure, with:
- system/executor;
- target FeatureOfInterest;
- inputs;
- result;
- time;
- used Procedure.

### System

Purpose: represent an Asset capable of implementing Procedures in Executions.

### Platform

Purpose: represent an Asset that hosts other Assets, especially Systems and other Platforms.

### Deployment

Purpose: represent a time/context-specific arrangement of Assets intended to execute Procedures with respect to FeaturesOfInterest.

### Observation / Sensor / ObservingProcedure

Purpose: specialize the generic Execution/System/Procedure pattern for observation.

### Actuation / Actuator / ActuatingProcedure

Purpose: specialize the same pattern for changing the value of a Property of a FeatureOfInterest.

### Sampling / Sampler / SamplingProcedure / Sample

Purpose: specialize the same pattern for creating/obtaining a Sample that acts as a proxy for an ultimate FeatureOfInterest.

### Collections

Purpose: group Executions/results/entities while constraining shared properties or preserving membership semantics.

### System Capabilities

Purpose: describe system performance and the conditions/context in which that performance is valid, separately from the system's Executions.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Target/property | FeatureOfInterest, Property, hasProperty, forProperty |
| Reusable behavior | Procedure, hasInput, hasOutput, implementedBy |
| Execution | Execution, ExecutionCollection, usedProcedure, madeBySystem, hasResult, input value, start/end/result/phenomenon time |
| System/deployment | Asset, System, Platform, Deployment, hasSubSystem, hosts, deployedSystem |
| Observation | Sensor, ObservingProcedure, Observation, ObservationCollection, Stimulus, observedProperty, resultQuality |
| Actuation | Actuator, ActuatingProcedure, Actuation, ActuationCollection, actsOn |
| Sampling | Sampler, SamplingProcedure, Sampling, Sample, SampleCollection, original/ultimate sample relationships |
| Collection | hasMember, isMemberOf, specialized Execution collections |
| Capability/conditions | hasSystemCapability, OperatingConditions, Normal/Suboptimal/SurvivableConditions, hasValidityContext |
| Capability representation | Observation, ObservationCollection, vocabulary of capability/environment properties |
| Extension/alignment | OMS, Sample Relations, PROV/SAREF/other alignments |

---

## 4. Primary relationships

### System → Procedure

`implements` relates a System to a Procedure it is capable of executing.

### Procedure → Execution

`usedForExecution` / `usedProcedure` relates reusable method to one or more actual Executions.

### System → Execution

`madeExecution` / `madeBySystem` records the executor.

### Execution → FeatureOfInterest

Execution targets a FeatureOfInterest; ultimate FeatureOfInterest can be separately represented.

### Execution → Result

Execution has result / simple result and result time.

### System → subsystem

`hasSubSystem` relates a System to component Systems.

### Platform → hosted Asset

`hosts` / `isHostedBy` represents hosting/mounting independently from subsystem composition.

### Deployment → Assets / Platform / System

Deployment arranges Assets, can identify:
- deployed System;
- deployed Platform;
- FeatureOfInterest.

### Sensor → Observation

Sensor makes Observation; Observation is made by Sensor.

### Sensor → observed Property

Sensor `observes` Property.

### Observation → observed Property / Feature / result

Observation specializes Execution and binds:
- Sensor;
- ObservingProcedure;
- observed Property;
- FeatureOfInterest;
- result.

### Actuator → Actuation → Property

Actuator can act on Property; an Actuation represents the actual change attempt.

### Sampler → Sampling → Sample

Sampling uses a Sampler/Procedure and produces a Sample, which relates to its original/ultimate FeatureOfInterest.

### System → capability → validity context

System Capability is represented by Observation/ObservationCollection and may point to an OperatingConditions Observation/Collection as the context where the capability holds.

---

## 5. Dependency boundaries

The ontology deliberately separates semantic layers.

### SOSA vs SSN

SOSA supplies a lightweight/minimal set of core terms; SSN adds fuller axiomatization/restrictions.

### Common vs Observation/Actuation/Sampling

Generic patterns are defined once in Common and specialized into three concrete execution domains.

### Procedure vs Execution

Reusable specification/method and actual occurrence are distinct.

### System vs Procedure

System implements Procedure but is not the Procedure.

### System vs Platform

System executes Procedures; Platform hosts Assets. An object may play more than one role in an application, but the ontology does not collapse the roles.

### System vs Deployment

System persists as an Asset; Deployment is the contextual arrangement/time-bound use of Assets.

### Core vs System Capabilities extension

Capability/operating-condition descriptions are not required to model the basic system/execution pattern.

### 2017 vs 2023 capability model

The 2023 extension removes the 2017 explicit SystemProperty/OperatingProperty/SurvivalProperty hierarchy and reuses Observation/ObservationCollection plus property vocabularies.

---

## 6. Intrinsic vs contextual standing

### Intrinsic/system-defining

- System identity/class;
- subsystem relationships;
- implemented Procedures;
- Properties the System is capable of observing/acting on;
- class/type-level capability statements where applicable.

### Contextual

- Deployment;
- hosting Platform;
- FeatureOfInterest for a specific Execution;
- operating-condition validity context;
- spatial location;
- execution inputs.

### Execution-specific

- Observation/Actuation/Sampling occurrence;
- phenomenon/start/end/result times;
- result;
- result quality;
- specific FeatureOfInterest.

### Proxy/context structure

Sample can serve as proxy for an ultimate FeatureOfInterest and must not be treated as identical to it.

---

## 7. Cross-cutting concepts

Cross-cutting ontology patterns include:

- FeatureOfInterest;
- Property;
- Procedure;
- Execution;
- System;
- Collection;
- result;
- time;
- deployment;
- location/geometry patterns;
- proximate vs ultimate FeatureOfInterest;
- class/type vs individual System;
- alignments to other ontologies.

The generic Execution pattern is especially cross-cutting: Observation, Actuation and Sampling inherit the same executor/procedure/target/result/time architecture.

---

## 8. State / temporal / lifecycle organization

SOSA/SSN has strong **execution and deployment temporality**, but it is not a full asset-service lifecycle ontology.

### Execution time

Execution supports:

- startTime;
- endTime;
- phenomenonTime;
- resultTime.

These times are intentionally distinct.

For example:
- phenomenonTime can be before or after resultTime;
- resultTime is when result became available;
- start/end describe execution interval.

### Deployment time

Deployment can be for a specified time interval and can have start/end semantics.

### Historical/forecast use

The time model explicitly supports:
- plans;
- forecasts;
- predictions;
- historical scenarios.

### Capability validity

System capabilities can have validity contexts expressed as observations/collections of operating/environmental conditions.

### Limit

Maintenance, repair, calibration history, ownership history and work orders are not core lifecycle structures in SOSA/SSN.

---

## 9. Composition / topology organization

SOSA/SSN separates several topologies.

### System composition

`hasSubSystem` / `isSubSystemOf`:
- System → component System.

### Hosting topology

`hosts` / `isHostedBy`:
- Platform → hosted Asset/System/Platform.

### Deployment topology

Deployment relates:
- deployed Systems;
- deployed Platforms;
- FeaturesOfInterest.

### Sample/proxy topology

Sampling creates Samples related through:
- original sample;
- sample of;
- ultimate FeatureOfInterest;
- sample chains.

### Collection topology

Observation/Actuation/Sampling/Execution collections group members without implying subsystem composition.

### Important distinction

**subsystem composition, hosting, deployment, collection membership and sample/proxy relationships are separate source-native relationship types.**

---

## 10. Capability / function / behavior organization

### System function

A System `implements` one or more Procedures.

### Role specialization

System specializes into:
- Sensor;
- Actuator;
- Sampler.

The role is tied to the kind of Procedure/Execution:
- Sensor → ObservingProcedure/Observation;
- Actuator → ActuatingProcedure/Actuation;
- Sampler → SamplingProcedure/Sampling.

### System Capability extension

Capability is described with Observation/ObservationCollection whose FeatureOfInterest is the System itself.

Capability properties can include:
- accuracy;
- resolution;
- frequency;
- measurable range;
- latency;
- drift;
- battery lifetime
through controlled vocabularies.

### Operating conditions

Separate Observations/Collections describe:
- normal;
- suboptimal;
- survivable
conditions.

### Validity context

Capability can depend on environmental/operating conditions.

The source-native model therefore separates:

> **Procedure implemented → execution performed → performance capability → operating/survival context**

---

## 11. Information / output organization

SOSA/SSN distinguishes several result/information structures.

### Observation result

Observation has:
- observed Property;
- FeatureOfInterest;
- result;
- simple result;
- result quality.

### Actuation result

Actuation can have result describing the property value after actuation, while related Observation can verify actual effect.

### Sampling result

Sampling produces a Sample rather than a conventional measured value.

### Collections

ObservationCollection/ActuationCollection/SamplingCollection group related executions/results and may provide common property constraints.

### Capability information

System capability and operating-condition information reuse Observation/ObservationCollection structures but are semantically about the System and its environment rather than ordinary external observation targets.

The ontology therefore distinguishes **execution type and result semantics**, even when it reuses common Observation structures for system description.

---

## 12. Management / condition organization

Core SOSA/SSN has limited management semantics.

### System capabilities/operating conditions

The extension models:
- performance;
- acceptable operating environment;
- survival limits;
- validity context.

### Deployment

Provides operational arrangement context.

### System composition/hosting

Provides structural context needed for equipment management.

### Limit

The ontology does not provide a comprehensive generic model for:
- health/fault;
- diagnostics;
- maintenance;
- service history;
- work;
- configuration management.

Those require additional ontologies/profiles/domain models.

---

## 13. Provenance / identity / reference organization

SOSA/SSN's provenance architecture is relational rather than product-identity focused.

### System → Execution

`madeBySystem` / `madeExecution` identifies the executor/source.

### Execution → Procedure

`usedProcedure` identifies the reusable method.

### Execution → target/property/result

Preserves what was acted on/observed/sampled and what result was produced.

### Observation origin/quality

Observation can identify:
- originating Stimulus;
- related Observations;
- result quality.

### Deployment provenance/context

System/Platform can be related to Deployment.

### Sample lineage

Sample relationships support chains from derived sample to original/ultimate feature.

### Alignment to PROV

A dedicated PROV alignment module maps SOSA/SSN execution semantics to provenance concepts.

### Limit

Manufacturer/model/serial/product-asset identity is not a central source-native partition of the core ontology.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Asset vs System vs Platform** — deployment resource, procedure-executing system and hosting platform are different semantic roles.
2. **System vs Procedure** — executor/capable agent and reusable method are different.
3. **Procedure vs Execution** — specification and occurrence are different.
4. **System vs Deployment** — persistent System and time/context-specific arrangement are different.
5. **System composition vs Platform hosting** — subsystem relationship and hosting/mounting are distinct.
6. **hosting vs deployment** — persistent/structural hosting and deployment participation are not identical.
7. **FeatureOfInterest vs Property** — target entity and quality/state being observed/acted on are different.
8. **proximate vs ultimate FeatureOfInterest** — immediate target/proxy and ultimate subject are distinct.
9. **Sensor vs Observation** — System role and execution/result occurrence are different.
10. **Sensor vs ObservingProcedure** — implementing System and reusable method are different.
11. **Observation vs result** — execution and its output are different.
12. **Observation vs Actuation vs Sampling** — concrete execution types have different semantics despite shared base structure.
13. **Sampler/Sampling vs Sample** — execution/executor and the material/spatial/statistical result entity are distinct.
14. **Sample vs FeatureOfInterest** — proxy/sample is not the ultimate feature.
15. **Execution vs ExecutionCollection** — occurrence and collection/grouping are different.
16. **collection membership vs subsystem composition** — group membership does not imply part-of.
17. **phenomenonTime vs resultTime vs execution start/end** — temporal semantics are deliberately distinct.
18. **system capability vs ordinary external observation** — same Observation carrier can represent different semantic roles.
19. **capability vs operating conditions** — performance and environment/context must remain distinct.
20. **normal/suboptimal/survivable conditions** — desirability/operability levels are not interchangeable.
21. **core ontology vs optional capability extension** — capability modeling is not required for base execution/system semantics.
22. **2017 capability hierarchy vs 2023 Observation-based capability pattern** — edition change must not be silently erased.
23. **class/system type vs individual System** — datasheet-like type description and particular instance are different.
24. **ontology role classification vs CSAPI classification token** — formal RDF class assertion and application-profile classification must not be assumed equivalent without explicit mapping.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely core/intrinsic:** System/Procedure/Execution separation; subsystem composition; role specialization; target Property/Feature semantics;
- **likely reusable structural pattern:** generic Execution architecture specialized consistently into Observation, Actuation and Sampling;
- **likely contextual relationship pattern:** Platform hosting and Deployment separated from System composition;
- **likely capability pattern:** capability/performance represented separately from operating/survival context with explicit validity context;
- **likely temporal pattern:** phenomenon time, result time and execution interval remain distinct;
- **likely information/output pattern:** result, quality, collection and sample/proxy semantics separated from execution;
- **likely provenance pattern:** executor + procedure + target + result + time + sample lineage;
- **likely cross-cutting:** FeatureOfInterest, Property, Collection, Procedure and Deployment;
- **profile-gap signal:** equipment identity/nameplate, detailed configuration, health/fault, communications, power and maintenance require additional donors;
- **ontology caution:** SOSA/SSN classes/properties are semantic primitives; V2 must not mirror every OWL class as a DIM module or equate application-profile classification with RDF type automatically.

**No V2 module disposition is made in Phase A.**

---

**C14 status: COMPLETE.**

**Next frozen lineage:** C15 — The Open Group SOSA.

---

# C15 — The Open Group SOSA

## Source basis and evidence ceiling

**Frozen primary source IDs:** 48, 49.  
**Frozen companion IDs:** 47, 50–58.

**Primary inspected sources:**

- The Open Group, *Technical Standard for SOSA Reference Architecture, Edition 1.1*, C239, June 2023 with September 2023 erratum.
- The Open Group, *Technical Standard for SOSA Reference Architecture, Edition 1.0: SOSA Domain-Specific Data Model*, 2022.

**Companion lineage:**

- Edition 1.0 Technical Standard.
- SOSA DSDM IDL.
- Edition 1.1 System Management OpenAPI companion artifacts.
- Edition 2.0 Snapshot 3 / bundle as later draft-development lineage.

**Evidence note:** Edition 1.1 is the adopted Technical Standard in the frozen corpus and controls the architecture extraction. The complete Edition 1.0 DSDM is the frozen source-native data-model artifact and controls detailed entity-model extraction. The later Edition 2.0 Snapshot 3 is a draft snapshot; its raw bundle was not re-inspected here, so no new clause-level claims are imported from it. The W3C/OGC SOSA ontology is a different lineage and is handled separately as C14.

---

## 1. Source-native structural organization

The Open Group SOSA lineage organizes the Sensor simultaneously through **architecture modules/infrastructure**, **physical context**, **system management**, and a **domain-specific data model**.

### A. Whole Sensor boundary

Edition 1.1 identifies the **SOSA Sensor** as the main subject.

A SOSA Sensor:

- consists of one or more hardware elements;
- may include software/firmware;
- can implement one or more of the SOSA sensing domains;
- has an external boundary; interfaces crossing it are external Sensor interfaces.

### B. Sensor Component taxonomy

SOSA divides Sensor Components into two major categories:

1. **SOSA Modules**
   - logical building blocks implementing specified functions/behaviors/interfaces.

2. **SOSA Infrastructure**
   - building blocks enabling Modules to execute/interoperate.

Infrastructure is further separated into:

- **Hardware Elements**
  - PIC;
  - aperture;
  - chassis;
  - power supply;
  - connectors/mount/backplane;
  - chassis manager.

- **Run-Time Environment**
  - operating system;
  - container engine;
  - hypervisor;
  - related runtime execution environment.

- **Interaction Infrastructure**
  - transport/API;
  - interaction binding;
  - inter-module communication infrastructure.

### C. Functional module decomposition

Edition 1.1 organizes SOSA functions into top-level module families such as:

1. **SOSA Sensor Management**
   - System Manager;
   - Task Manager.

2. **Transmission / Reception**
   - Emitter/Collector;
   - Conditioner-Receiver-Exciter.

3. **Process Signals / Targets**
   - Signal/Object Detector and Extractor;
   - Signal/Object Characterizer;
   - Image Pre-processor;
   - Tracker.

4. **Analyze / Exploit**
   - External Data Ingestor;
   - Encoded Data Extractor;
   - Situation Assessor;
   - Impact Assessor and Responder;
   - Storage/Retrieval Manager.

5. **Convey**
   - Reporting Services.

6. **Support System Operation**
   - Security Services;
   - Encryptor/Decryptor;
   - Guard/Cross-Domain Service;
   - Network Subsystem;
   - Calibration Service;
   - Navigation Data Service;
   - Time & Frequency Service;
   - Compressor/Decompressor;
   - Host Platform Interface;
   - Power.

### D. Physical context

Edition 1.1 separately defines:

- SOSA Sensor;
- Sensor hardware element;
- SOSA Host Platform.

Hardware elements can be grouped or physically distributed on/in the Host Platform while remaining parts of one Sensor.

### E. System management structure

SOSA explicitly separates:

- **mission/task execution**; from
- **system management / housekeeping**.

System management covers:

- discovery;
- capacity information;
- configuration;
- control/state/mode;
- health monitoring;
- faults;
- BIT;
- diagnostics;
- logs/events;
- software/firmware management;
- security management.

Sensor components can be:
- managed;
- unmanaged;
- directly managed;
- indirectly managed by another component representing/managing them.

### F. DSDM Entity Model

The Edition 1.0 DSDM adds conceptual entities/associations including:

- Sensor;
- Component_;
- Platform;
- Controller;
- Chassis;
- Slot;
- Product;
- ProductInstance;
- Function_;
- Network;
- NetworkInterface;
- File;
- SoftwareElement;
- Fault;
- Action;
- Test;
- LogEntry;
- SecurityClassification;
- many measurements/states.

Important associations include:

- SensorComponent;
- HostPlatform;
- ChassisSlot;
- PICPluggedIntoSlot;
- ProductInstance;
- ModuleImplementation;
- ComponentActiveFaults;
- ComponentFaultOrigination;
- SensorFaultOrigination;
- SensorBuiltInTest / BITResult;
- DynamicDiscovery;
- StaticConfiguration;
- FirmwareUpdate / SoftwareUpdate;
- controller-issued commands.

The source-native anatomy is therefore:

> **whole Sensor boundary + functional module decomposition + infrastructure decomposition + physical Host Platform context + separate system-management concern + DSDM entity/relationship model for components, state, faults, configuration, products and commands**

---

## 2. Purpose of each partition

### SOSA Sensor

Purpose: define the complete operational Sensor boundary within which components, infrastructure and functions are integrated.

### SOSA Module

Purpose: encapsulate a coherent function/behavior/interface so implementations can be modular and interchangeable.

### Infrastructure

Purpose: provide the hardware/runtime/interaction substrate needed to realize and connect Modules.

### Hardware Element

Purpose: represent physical realization elements:
- cards;
- chassis;
- apertures;
- power;
- connectors/mounts.

### RTE

Purpose: decouple software module functionality from particular execution environment.

### Interaction Infrastructure

Purpose: standardize how modules communicate without making transport implementation identical to module function.

### System Management

Purpose: keep the Sensor and its components operational, configured, healthy and secure, independently from mission-task semantics.

### Task Management

Purpose: coordinate mission/operational tasking, distinct from housekeeping/system management.

### Host Platform

Purpose: represent the physical host on which the Sensor is mounted, separately from the Sensor boundary.

### DSDM

Purpose: provide conceptual/logical/physical data structures and message content for interoperable module/component interactions and management.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Whole subject | Sensor, sensor types, external boundary |
| Component | Component_, SensorComponent, Module, HardwareElement, SoftwareElement |
| Functional architecture | System Manager, Task Manager, transmission/reception, signal processing, analysis/exploitation, convey, support services |
| Infrastructure | PIC, aperture, chassis, power supply, RTE, OS, VM/container, transport/API/binding |
| Host context | Platform, HostPlatform, Host Platform Interface |
| Physical assembly | Chassis, Slot, ChassisSlot, PIC, SlotProfile, connectors, mounts |
| Product realization | Product, ProductInstance, ModuleImplementation |
| State | operationalState, healthStatus, configurationState, mode |
| Management | DynamicDiscovery, StaticConfiguration, logs, reset/restart/sanitize/zeroize, firmware/software update |
| Condition | Fault, active fault, fault origination, severity, category, suggested Action |
| Test | Test, SensorBuiltInTest, BITResult |
| Control | Controller, command associations, mode/state/configuration actions |
| Communications | Network, NetworkInterface, NetworkConnection, NetworkGateway |
| Security | classification, compartments, crypto channels, keys/certificates |
| Information/data model | DIV-1 Entity model, DIV-2 logical model, DIV-3 physical message model |

---

## 4. Primary relationships

### Sensor → Sensor Components

`SensorComponent` explicitly states that a Component_ is part of a Sensor.

### Sensor ↔ Host Platform

`HostPlatform` associates a Sensor with the physical Platform on which it is mounted.

This is not the SensorComponent relation.

### Component → Modules

Component_ can be made of hardware/software Modules and participates in ModuleImplementation relationships.

### Product → Component

`ProductInstance` associates a manufactured Product with a functional Component_.

### Chassis → Slot → PIC

Separate associations represent:
- ChassisSlot;
- slot profile;
- PIC plugged into Slot;
- Chassis Management.

### Component → faults/logs/configuration

Components have:
- active faults;
- fault origination;
- logs;
- state;
- mode;
- discovery/configuration behavior.

### Sensor → health/BIT/fault

Sensor has:
- health/configuration/operational state;
- built-in tests;
- sensor-level fault origination;
- component statuses rolled into Sensor health information.

### Controller → Sensor/Component command

Controller is a functional item exerting control over another entity.

Command associations bind:
- issuing Controller;
- target Sensor/Component;
- requested state/mode/action.

### Module ↔ interactions

Modules interact through standard interactions implemented over the interaction infrastructure/interconnects.

---

## 5. Dependency boundaries

The lineage deliberately separates multiple architectural levels.

### Architecture function vs implementation realization

SOSA Modules define function/behavior/interface; hardware/firmware/software realization can vary.

### Module vs infrastructure

Module function is distinct from:
- hardware substrate;
- RTE;
- communication/interaction infrastructure.

### Sensor vs Host Platform

Sensor boundary and physical hosting platform are separate.

### Mission/task vs management

Mission processing/tasking is distinct from system-management housekeeping.

### Functional Component vs manufactured Product

ProductInstance links product identity to functional Component, showing they are not the same concept.

### Component vs module implementation

Component can implement/be realized by different hardware/software module patterns.

### DIV-1 vs DIV-2 vs DIV-3

Conceptual entity semantics, logical data organization and physical message representation are different data-model levels.

### Managed entity vs management representative

A managed component can be managed directly or indirectly through a second component; management representation does not necessarily equal physical component identity.

---

## 6. Intrinsic vs contextual standing

### Strongly intrinsic to Sensor

- SensorComponents;
- functional modules;
- hardware/software/runtime infrastructure;
- Sensor state/health/configuration;
- internal networks/interconnects;
- power infrastructure;
- calibration/time/navigation/security support where part of the Sensor;
- internal faults/tests/logging;
- internal command/control structures.

### Contextual/external

- Host Platform;
- Platform C2;
- external network/system interfaces;
- external tasking/products;
- broader mission environment.

### Representation/management-specific

- a component indirectly managed through another component;
- dynamic discovery vs static configuration;
- product-vs-functional-component mapping;
- module implementation choice.

These are not automatically physical containment distinctions.

---

## 7. Cross-cutting concepts

Cross-cutting SOSA structures include:

- component identity;
- health;
- operational state;
- mode;
- configuration state;
- faults;
- logs;
- BIT;
- security classification;
- power;
- time/frequency;
- navigation;
- calibration;
- network/interactions;
- Controller/action semantics;
- software/firmware update;
- product/version.

System Manager services span both the whole Sensor and individual components.

---

## 8. State / temporal / lifecycle organization

SOSA provides strong operational/configuration state but not a full acquisition-to-disposal asset lifecycle.

### Component state

Component_ carries:
- operationalState;
- healthStatus;
- mode;
- version.

### Sensor state

Sensor carries:
- health;
- operational state;
- configuration state.

### Operational state examples

General operational states include:
- starting;
- operational;
- degraded;
- reconfiguring;
- testing;
- shutting down;
- restarting;
- zeroizing;
- sanitizing.

### Configuration state

Examples include:
- configured;
- not configured;
- sanitized;
- zeroized.

### Fault time

Fault origination and BIT results can carry timestamps.

### Update/configuration lifecycle

- static configuration;
- dynamic discovery;
- firmware updates;
- software updates;
- reset/restart/sanitize/zeroize;
- log deletion/management.

### Task lifecycle

Functional module/task decomposition includes:
- accept/start/pause/resume/cancel;
- task status monitoring.

### Limit

The Technical Standard focuses on operational system/component lifecycle and modular upgrade/maintenance, not a generic enterprise work-order/procurement/service history model.

---

## 9. Composition / topology organization

SOSA defines several different topologies.

### Sensor composition

SensorComponent defines which Components are part of a Sensor.

### Hardware assembly

Chassis/Slot/PIC/profile/mount/backplane relationships define physical hardware assembly.

### Functional/module topology

SOSA Modules and functional groups define logical decomposition of mission/system functions.

### Network/interconnect topology

Network, interface, gateway, interaction infrastructure and interconnects define communication topology.

### Host topology

HostPlatform links Sensor to external Platform.

### Product/implementation topology

ProductInstance and ModuleImplementation relate manufactured products and hardware/software modules to functional components.

### Management topology

Managed/unmanaged and direct/indirect management relationships define management responsibility.

### Important distinction

**functional decomposition, physical assembly, communication topology, product realization, management responsibility and host-platform relation are separate source-native structures.**

---

## 10. Capability / function / behavior organization

SOSA's main architecture is strongly function-oriented.

### Module encapsulation

Each Module encapsulates specified:
- functions;
- behaviors;
- interfaces.

### Functional decomposition

Modules can have multi-level functional groups, e.g.:
- manage task;
- execute task;
- process data;
- characterize target;
- assess situation;
- support operation.

### Mission behavior

Top-level responsibilities include:
- transmission/reception;
- signal/object detection;
- characterization;
- tracking;
- external-data ingestion;
- exploitation/assessment;
- reporting/conveyance.

### Support behavior

Separate modules provide:
- security;
- network;
- calibration;
- navigation;
- time/frequency;
- compression;
- power;
- platform interface.

### Management behavior

System Manager functions include:
- Discovery;
- Configuration;
- Control;
- Health Management;
- Security Management.

### Task behavior

Task Manager and module-specific task interactions handle operational task execution separately from System Manager.

The source-native pattern separates **mission function, support function, management function and infrastructure realization**.

---

## 11. Information / output organization

SOSA defines information flow at multiple levels.

### Module interactions

Interactions represent data/resource flow between Modules.

### DIV-2 / DSDM message content

Logical data entities define content used by system-management/mission interactions.

### DIV-3 physical data model

Maps logical/entity semantics into physical message structures/templates.

### Management information

Examples include:
- Sensor health;
- Component status;
- faults;
- configuration;
- mode;
- state;
- firmware info;
- logs;
- security information.

### Mission information

Examples include:
- signal data;
- detections;
- tracks;
- imagery;
- characterizations;
- reports/products;
- tasking parameters/status.

The architecture therefore keeps **mission data products** and **system-management/condition data** distinct even though both use common inter-module infrastructure.

---

## 12. Management / condition organization

Management/condition is a major first-class partition.

### System management

Covers:
- discovery;
- capacity;
- configuration;
- control;
- health;
- faults;
- BIT;
- diagnostics;
- logging;
- security;
- software/firmware update.

### Managed vs unmanaged component

Not every component must expose direct management.

### Indirect management

One component can implement the management interfaces/capabilities on behalf of another.

### Health

Sensor Health can roll up:
- whole Sensor status;
- per-component status.

### Fault

Fault structures preserve:
- originator component/Sensor;
- active state;
- severity;
- category;
- message/description;
- timestamp;
- suggested action.

### BIT

SensorBuiltInTest and BITResult separate:
- test definition;
- test execution/result;
- Sensor association.

### Configuration

StaticConfiguration and DynamicDiscovery are distinct management concepts.

This is a highly explicit source-native separation between **operational mission function** and **keeping the Sensor/components capable of mission function**.

---

## 13. Provenance / identity / reference organization

The DSDM distinguishes several identity/provenance layers.

### Entity identifiers

Most DSDM entities/associations carry `elementID`.

### Sensor/component identity

Sensor and Component_ have IDs/names/address/kind/state.

### Product identity

Product is separate from Component_ and can be associated through ProductInstance.

### Version identity

Component and software/firmware structures carry version information.

### Source/origin identity

Fault origination, log entry and command associations identify:
- originating component/Sensor;
- issuing Controller;
- target.

### Platform identity

Platform is independently identified/positioned and related through HostPlatform.

### Data model provenance

DIV-1 conceptual entities are explicitly authoritative over diagrams when discrepancies exist; logical/physical models derive from the entity semantics.

This supports a strong distinction between **functional identity, manufactured product identity, host identity and message/data identity**.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Sensor vs Sensor Component** — whole Sensor and constituent component are different levels.
2. **Sensor Component vs SOSA Module** — component and logical functional module are not identical.
3. **SOSA Module vs infrastructure** — mission/support function and execution substrate are separate.
4. **Hardware Element vs software/RTE** — physical and software/runtime realization differ.
5. **Sensor vs Host Platform** — sensing system and physical host are explicitly separate.
6. **SensorComponent vs HostPlatform relationship** — part-of and hosted-on are different.
7. **functional module topology vs physical assembly** — function and hardware structure are not isomorphic.
8. **functional Component vs Product/ProductInstance** — functional role and manufactured product are distinct.
9. **component composition vs module implementation** — component identity and implementation mapping differ.
10. **component topology vs communication topology** — part-of and network/interconnect relationships are different.
11. **management topology vs physical topology** — a component can be managed indirectly by another component.
12. **mission/tasking vs system management** — performing the mission and maintaining system readiness are separate concerns.
13. **System Manager vs Task Manager** — housekeeping/control and mission task coordination are separate responsibilities.
14. **health vs operational state vs configuration state vs mode** — these are distinct state dimensions.
15. **fault vs health status** — detailed fault event/origin/severity and summarized health are different.
16. **fault vs BIT result** — fault information and explicit self-test result are different.
17. **static configuration vs dynamic discovery** — configuration source and presence/discovery behavior differ.
18. **software update vs firmware update** — distinct realization/update targets.
19. **Chassis vs Slot vs PIC** — physical container, receptacle and inserted component are distinct.
20. **PowerPort/PowerBus vs component identity** — power topology and equipment identity differ.
21. **Network vs NetworkInterface vs Component** — communication substrate/interface/device are distinct.
22. **mission product/data vs management/condition information** — same infrastructure does not erase different semantic roles.
23. **DIV-1 vs DIV-2 vs DIV-3** — conceptual meaning, logical data structure and physical message representation are different abstraction levels.
24. **Edition 1.0 DSDM vs Edition 1.1 architecture** — later architecture and earlier DSDM should be related deliberately rather than silently merged as one normative edition.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely core/intrinsic:** whole Sensor vs component distinction; heterogeneous hardware/software component realization; host Platform separation;
- **likely reusable structural pattern:** simultaneous functional, physical, communication, product-realization and management topologies kept distinct;
- **likely functional pattern:** mission functions, support functions, task management and system management partitioned explicitly;
- **likely management/condition pattern:** discovery/configuration/control/health/fault/BIT/log/update structures;
- **likely state pattern:** health, operational state, configuration state and mode represented as independent dimensions;
- **likely provenance/identity pattern:** functional Component vs Product instance vs Host Platform vs Controller/source identities;
- **likely information pattern:** mission data/products and management/condition information separated despite shared infrastructure;
- **likely modularity pattern:** Modules encapsulate function/interface while infrastructure is independently replaceable/standardized;
- **specialization caution:** The Open Group SOSA is defense C5ISR sensor architecture and its module taxonomy is not automatically universal across all V2 sensing equipment;
- **binding/conformance caution:** SOSA Module IDs, hardware profiles, interaction bindings, OpenAPI interfaces and DSDM physical messages are native SOSA implementation/conformance structures and are not automatically V2 DIM modules or CSAPI profile requirements.

**No V2 module disposition is made in Phase A.**

---

**C15 status: COMPLETE.**

**Core structural donor group C01–C15: COMPLETE.**

**Next frozen lineage:** X01 — I-ADOPT.

---

# X01 — I-ADOPT Framework Ontology

## Source basis and evidence ceiling

**Frozen primary source IDs:** 145, 146.  
**Frozen companion IDs:** 147, 150.

**Primary inspected source:**

- I-ADOPT Framework Ontology, version **1.1.0**, release 28 May 2025:
  - `https://i-adopt.github.io/ontology/`
  - version IRI `https://w3id.org/iadopt/ont/1.1.0`.

**Companion evidence:**

- I-ADOPT Overview / OMS extension roadmap.
- RDA I-ADOPT WG outputs and recommendations.

**Evidence note:** I-ADOPT is intentionally a **variable-description semantic framework**, not an instrument/system ontology. Its structural value is therefore cross-cutting. Version 1.1.0 adds StatisticalModifier and multi-entity System structures beyond earlier versions; those current additions are preserved rather than silently using the older four-class simplified diagram as the whole ontology.

---

## 1. Source-native structural organization

I-ADOPT 1.1.0 organizes a variable description around a small set of atomic semantic roles.

### Core variable structure

1. **Variable**
   - description of something observed or derived;
   - minimally requires:
     - exactly one Property;
     - exactly one ObjectOfInterest.

2. **Property**
   - type of characteristic of the ObjectOfInterest.

3. **Entity**
   - any object/process participating in the variable description.

Entities can play roles through relationships:

4. **ObjectOfInterest**
   - Entity whose Property is observed.

5. **Matrix**
   - Entity in which the ObjectOfInterest is contained;
   - specialized ContextObject relation.

6. **ContextObject**
   - Entity supplying additional background/context around the ObjectOfInterest.

7. **Constraint**
   - confines/qualifies one or more variable-description components.

8. **StatisticalModifier**
   - statistical measure/modifier applied to the variable.

### Variable grouping

9. **VariableSet**
   - aggregation/grouping of Variables for a purpose;
   - can define applicable Property, ObjectOfInterest, Matrix, ContextObject and StatisticalModifier without requiring every member to share one fully specified Variable structure.

### Multi-entity systems added in 1.1.0

10. **System**
    - combination of two or more Entities.

11. **AsymmetricSystem**
    - System whose constituent Entities have differentiated roles;
    - relations include:
      - numerator/denominator;
      - source/target.

12. **SymmetricSystem**
    - System whose constituent Entity roles are mutually interchangeable;
    - uses `hasPart` at least twice.

The source-native anatomy is therefore:

> **Variable = Property + ObjectOfInterest + optional contextual/qualifying components**, with optional **VariableSet** grouping and specialized **multi-Entity Systems** for compound variable semantics.

---

## 2. Purpose of each partition

### Variable

Purpose: create a machine-interpretable semantic description of the quantity/quality being observed or derived.

### Property

Purpose: provide the reusable/general characteristic whose meaning survives across more-specific Variables.

### ObjectOfInterest

Purpose: identify **what Entity's Property** is being described.

### Matrix

Purpose: identify the Entity/material/context **in which the ObjectOfInterest is contained** when that distinction matters.

### ContextObject

Purpose: add additional background Entity context without making it the observed object itself.

### Constraint

Purpose: narrow/confine the meaning of a variable-description component by describing a relevant condition/state/qualification.

### StatisticalModifier

Purpose: state which statistical transformation/measure has been applied.

### VariableSet

Purpose: group Variables under broader machine-interpretable criteria for discovery/aggregation without requiring one fully specified shared Variable.

### Symmetric/Asymmetric System

Purpose: describe a compound Entity made from multiple Entities where constituent role symmetry matters, e.g.:
- ratios;
- flows/fluxes;
- interchangeable-part systems.

---

## 3. Central concepts per partition

| Partition | Central concepts |
| --- | --- |
| Variable | Variable, hasProperty, hasObjectOfInterest |
| Variable context | Entity, hasContextObject, hasMatrix |
| Qualification | Constraint, constrains |
| Statistical semantics | StatisticalModifier, hasStatisticalModifier |
| Grouping | VariableSet, applicable Property/Object/Matrix/Context/Modifier, membership |
| Compound Entity | System, SymmetricSystem, AsymmetricSystem |
| Asymmetric roles | hasNumerator, hasDenominator, hasSource, hasTarget |
| Symmetric composition | hasPart |

---

## 4. Primary relationships

### Variable → Property

Exactly one Property.

### Variable → ObjectOfInterest

Exactly one Entity in ObjectOfInterest role.

### Variable → Matrix

Optional Matrix Entity.

### Variable → ContextObject

Zero or more additional ContextObject Entities.

### Variable → Constraint

Zero or more Constraints.

### Constraint → constrained component

In 1.1.0, Constraint may constrain:
- Entity;
- Property;
- StatisticalModifier.

### Variable → StatisticalModifier

Optional statistical modifier(s).

### VariableSet → applicable components

VariableSet can identify applicable:
- Property;
- ObjectOfInterest;
- Matrix;
- ContextObject;
- StatisticalModifier.

### System → Entities

Symmetric/Asymmetric Systems are composed from Entities through role-specific relations.

---

## 5. Dependency boundaries

I-ADOPT intentionally keeps its scope narrow.

### Variable semantics vs observation event

I-ADOPT describes **what a variable means**, not the Observation/Measurement event that produced one value.

### Variable semantics vs units

Units are explicitly outside the core Variable description and should be modeled independently through complementary ontologies.

### Variable semantics vs instrument

Instrument/device is explicitly outside I-ADOPT scope.

### Variable semantics vs method

Procedure/method is outside the core framework and should be linked through observational ontologies when needed.

### Variable semantics vs location

Geographical location is outside the core Variable semantics.

### Core Entity role vs term vocabulary

I-ADOPT expects terms for Property/Entity/Constraint etc. to be reused from external FAIR vocabularies rather than defining every domain term itself.

---

## 6. Intrinsic vs contextual standing

I-ADOPT makes this distinction explicit inside the **variable semantic description**.

### Essential/intrinsic to Variable meaning

- Property;
- ObjectOfInterest.

Both are mandatory.

### Contextual/optional

- Matrix;
- ContextObject(s);
- Constraints;
- StatisticalModifier(s).

These are included when needed to distinguish the Variable's meaning.

### External contextual information

Outside core Variable semantics:
- unit;
- instrument;
- method;
- geographic location;
- actual observation event/result.

This is a source-native boundary, not merely an implementation simplification.

---

## 7. Cross-cutting concepts

I-ADOPT itself is cross-cutting.

Important reusable patterns include:

- reusable external vocabulary concepts;
- role assignment to Entities;
- composition by semantic relations rather than compound labels;
- constraints applied explicitly to the components they qualify;
- statistical modification separated from base Property;
- grouping via VariableSet.

The framework's primary value is enabling semantically equivalent Variables from different communities to be decomposed and compared.

---

## 8. State / temporal / lifecycle organization

I-ADOPT does **not** define a lifecycle/state model for instruments, systems or Variables.

A Constraint may describe a state/condition relevant to variable meaning, but that is a semantic qualifier, not temporal state history.

Time can appear as a domain Entity/Property/Constraint term where relevant, but no generic temporal lifecycle structure is part of the framework.

**Evidence result:** lifecycle/state is non-applicable except where a state becomes part of Variable semantics.

---

## 9. Composition / topology organization

Composition appears in two semantic forms.

### Variable semantic composition

Variable meaning is composed from:
- Property;
- ObjectOfInterest;
- optional Matrix;
- ContextObject;
- Constraints;
- StatisticalModifier.

### Entity System composition

Version 1.1.0 adds:

- System;
- SymmetricSystem;
- AsymmetricSystem.

These allow compound Entities to be described structurally rather than encoded in one term.

The topology is **semantic/role composition**, not equipment assembly or physical topology.

---

## 10. Capability / function / behavior organization

I-ADOPT does **not** model equipment capability/function/behavior.

It only describes variable semantics.

A Property or Entity vocabulary term could refer to a functional concept, but the ontology provides no general:
- capability;
- command;
- service;
- operation;
- device function model.

**Evidence result:** non-applicable to capability anatomy except as the semantic structure of what a capability/observation might concern.

---

## 11. Information / output organization

I-ADOPT distinguishes:

- **Variable description** — semantic specification of what is observed/derived;
- **actual result/value** — outside the framework;
- **unit** — outside core framework;
- **observation/measurement/simulation/calculation event** — complementary observational ontology concern.

VariableSet provides grouping/discovery semantics but does not replace individual Variable descriptions.

This separation is fundamental to its interoperability purpose.

---

## 12. Management / condition organization

No equipment-management/condition model is defined.

Constraint can qualify a Variable by state/condition, but:
- health;
- faults;
- configuration;
- maintenance;
- management actions

are outside the I-ADOPT core scope.

---

## 13. Provenance / identity / reference organization

I-ADOPT assumes globally referenceable vocabulary concepts.

Its provenance/identity pattern is therefore primarily semantic:

- reuse identifiers for Property/Entity/Constraint/Modifier concepts;
- attach I-ADOPT relationships to existing Variable concepts where possible;
- avoid relying on opaque compound labels.

VariableSet can group variables under community/product-specific criteria.

Actual data-source/instrument provenance is outside core I-ADOPT and should be supplied by complementary ontologies.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Variable vs Property** — a fully qualified variable is more specific than its generic property.
2. **Property vs ObjectOfInterest** — characteristic and entity bearing that characteristic are different.
3. **ObjectOfInterest vs Matrix** — observed entity and containing medium/material are different roles.
4. **ObjectOfInterest vs ContextObject** — primary observed subject and supporting contextual entity are distinct.
5. **Matrix vs general ContextObject** — Matrix is a specialized containing-context relationship.
6. **Constraint vs constrained concept** — qualifier and the Entity/Property/Modifier it qualifies are distinct.
7. **StatisticalModifier vs Property** — statistical transformation and base characteristic must not be conflated.
8. **Variable vs VariableSet** — precise variable meaning and discovery/grouping category are different.
9. **Entity vs role** — ObjectOfInterest/Matrix/ContextObject are roles played by Entities, not necessarily disjoint real-world classes.
10. **System vs individual Entity** — compound semantic entity and atomic constituent differ.
11. **SymmetricSystem vs AsymmetricSystem** — interchangeable-role and role-specific compositions are different.
12. **numerator/denominator vs source/target** — different asymmetric role semantics.
13. **variable semantics vs unit** — meaning of what is measured and unit of a particular representation are different.
14. **variable semantics vs instrument** — measured-variable meaning does not identify the equipment making the observation.
15. **variable semantics vs procedure/method** — what is observed and how it is obtained are distinct.
16. **Variable description vs Observation/result** — semantic description and data-producing occurrence/value are different.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely cross-cutting semantic pattern:** decomposed observed/derived Variable meaning rather than compound uncontrolled labels;
- **likely core observation semantics:** Property + ObjectOfInterest as mandatory semantic minimum;
- **likely contextual semantics:** Matrix, ContextObject and explicit Constraint role;
- **likely quantitative semantics:** StatisticalModifier separated from base Property;
- **likely grouping pattern:** VariableSet for discovery/aggregation without weakening individual Variable meaning;
- **likely compound-property pattern:** Symmetric/Asymmetric multi-Entity structures for ratios/flows and similar variables;
- **scope guardrail:** unit, instrument, procedure, location and observation/result must remain separate linked concerns;
- **ontology caution:** I-ADOPT is not a device/System anatomy and should not be inflated into an equipment module merely because Variables are important to sensing.

**No V2 module disposition is made in Phase A.**

---

**X01 status: COMPLETE.**

**Next frozen lineage:** X02 — IETF EMAN.

---

# X02 — IETF Energy Management (EMAN)

## Source basis and evidence ceiling

**Frozen primary source IDs:** 135, 139, 140, 141.

**Primary inspected sources:**

- RFC 7326, *Energy Management Framework* (2014).
- RFC 7460, *Monitoring and Control MIB for Power and Energy* (2015).
- RFC 7461, *Energy Object Context MIB* (2015).
- RFC 7577, *Definition of Managed Objects for Battery Monitoring* (2015).

**Evidence note:** RFC 7326 is Informational and defines the conceptual/reference model; RFCs 7460, 7461 and 7577 are Standards Track MIB realizations of portions of that model. The conceptual framework and its MIB bindings are kept distinct.

---

## 1. Source-native structural organization

EMAN organizes energy-management information around the abstract **Energy Object**.

### Energy Object classes

- **Energy Object**
  - abstract equipment-management subject.

- **Device**
  - physical piece of equipment;
  - can consume, produce, meter, distribute or store energy;
  - may contain Components.

- **Component**
  - part of a physical Device.

- **Power Interface**
  - physical inlet/outlet through which energy is received/provided.

### Energy Object information partitions

RFC 7326 separates:

- identity;
- classification/category;
- business/site/organizational context;
- role;
- importance;
- power state;
- power measurements;
- power attributes;
- energy;
- demand;
- battery;
- control;
- relationships.

### Relationship model

Key Energy Object relationships include:

- **Power Source** — energy flows from source to target;
- **Metering** — one object meters another;
- **Aggregation** — one object aggregates information about others.

### MIB realization

RFC 7460 separates:
- Energy Object identity;
- power state;
- usage;
- power attributes;
- energy measurements;
- faults.

RFC 7461 separates:
- identity;
- context;
- relationships.

RFC 7577 organizes one conceptual row per Battery into:
1. static properties;
2. current operational/charge state;
3. alarm/notification thresholds.

---

## 2. Purpose of each partition

### Energy Object

Purpose: provide one management abstraction for equipment participating in energy management.

### Device / Component

Purpose: preserve whole-equipment versus constituent-part scope.

### Power Interface

Purpose: represent energy-transfer boundaries independently from Device/Component identity.

### Identity/context

Purpose: connect Energy Objects to persistent identifiers and deployment/business/site/organizational context.

### Power state/control

Purpose: represent administrative/operational energy states and control transitions.

### Measurements

Purpose: distinguish:
- power;
- electrical attributes;
- energy accumulation;
- demand over interval;
- measurement quality/caliber/source.

### Relationships

Purpose: explicitly represent energy-source, metering and aggregation relationships rather than infer them from physical proximity.

### Battery model

Purpose: distinguish battery design/static characteristics, live operating state, and alarm thresholds.

---

## 3. Central concepts per partition

| Partition | Central concepts |
| --- | --- |
| Whole equipment | EnergyObject, Device, Component |
| Energy boundary | PowerInterface, inlet, outlet |
| Identity/context | UUID, name, alternate key, category, role, importance, domain/site/org context |
| State/control | PowerStateSet, PowerState, admin/oper state |
| Power measurement | nameplate power, actual/estimated/static caliber, accuracy, direction |
| Energy/demand | accumulated energy, demand interval, energy used/produced/stored |
| Relationships | PowerSource, Metering, Aggregation |
| Battery | identifier, technology, design voltage/capacity, actual capacity/charge/voltage/current/temp, cycle count |
| Alarm | low/high charge/voltage/capacity/cycles/temperature thresholds |

---

## 4. Primary relationships

### Device → Component

Component is explicitly a part of Device.

### Device/Component → Power Interface

Power Interface represents physical energy-transfer point for a Device/Component.

### Energy Object → context

Energy Object can be assigned:
- domain;
- role;
- category;
- importance;
- organizational/site/business context.

### Energy Object → Energy Object

Relationship type explicitly states:
- supplies power;
- meters;
- aggregates.

### Battery → physical entity

Battery MIB indexes each Battery through ENTITY-MIB physical identity.

### Measurement → source/caliber

Power measurement records whether it is:
- actual;
- estimated;
- static;
and whether measured locally/remotely, plus accuracy/method.

---

## 5. Dependency boundaries

### Framework vs MIB implementation

RFC 7326 defines conceptual classes/relationships; MIB RFCs bind subsets into SNMP management objects.

### Equipment vs energy interface

Device/Component identity and PowerInterface are separate.

### Physical containment vs energy relationship

Part-of does not imply PowerSource/Metering/Aggregation.

### Static/nameplate vs live measurement

Nominal/manufacturer values are distinct from current measured/estimated values.

### Energy vs power vs demand

Instantaneous/rate, accumulated quantity and interval average are different information semantics.

### Battery identity vs replacement position

Battery MIB can reuse physical index when a Battery is replaced at the same connector, exposing a distinction between managed position/index and physical Battery instance.

---

## 6. Intrinsic vs contextual standing

### Intrinsic

- Device/component identity;
- power interfaces;
- battery design characteristics;
- capability/state sets;
- nameplate values.

### Contextual

- business/site/organizational domain;
- energy-source relationship;
- metering relationship;
- aggregation relationship;
- role/importance;
- remote measurement source.

### Dynamic

- current power state;
- current power/energy/demand;
- battery charge/current/temperature;
- alarms.

---

## 7. Cross-cutting concepts

- UUID/alternate keys;
- role/category;
- context;
- state;
- measurement quality/caliber;
- time interval;
- direction of flow;
- alarm/fault;
- relationships;
- ENTITY-MIB physical identity.

---

## 8. State / temporal / lifecycle organization

EMAN has rich operational state but limited whole-asset lifecycle.

### Power state

Power State Set defines available/current energy-control state.

### Demand

Demand explicitly averages power over time interval.

### Energy

Energy accumulates over time.

### Battery state

Battery model separates:
- charging operational state;
- charging administrative state;
- current charge/capacity;
- cycle count;
- last charging-cycle time;
- temperature/voltage/current.

### Replacement

Battery MIB's physical index rule exposes replacement continuity at the connector/location level.

### Limit

No general maintenance/work/service history is defined.

---

## 9. Composition / topology organization

### Physical hierarchy

Device contains Components.

### Energy topology

PowerSource relationship models directed energy flow independently from physical containment.

### Metering topology

Metering relationship says one Energy Object measures another.

### Aggregation topology

Aggregation relationship says one Energy Object aggregates energy information about others.

### Interface topology

PowerInterface explicitly models inlet/outlet.

These topologies are distinct and cannot be collapsed into one parent-child tree.

---

## 10. Capability / function / behavior organization

Energy behavior is modeled through:

- role as consumer/producer/meter/distributor/store;
- supported Power State Sets;
- control of Power State;
- measurement capability;
- battery characteristics;
- PowerInterface direction.

Function is purpose-specific to energy management, not a general device-function framework.

---

## 11. Information / output organization

EMAN distinguishes:

- static/nameplate information;
- current power;
- Power Attributes;
- accumulated energy;
- demand;
- current state;
- battery current state;
- fault/alarm/notification information.

Measurement metadata preserves method/caliber/accuracy and flow direction.

---

## 12. Management / condition organization

Energy management is the lineage's central purpose.

It includes:

- monitoring;
- Power State control;
- power/energy/demand reporting;
- fault management;
- context;
- relationship discovery;
- battery status;
- alarm thresholds.

Condition is purpose-specific to energy/battery rather than whole-device health.

---

## 13. Provenance / identity / reference organization

- persistent UUID for Energy Object;
- human-readable name;
- alternate key linking other management models;
- ENTITY-MIB physical index;
- context MIB links to other identifiers;
- measurement caliber records source/method/accuracy;
- relationship IDs/types identify connected Energy Objects.

Identity of the managed position/index can differ from replaceable Battery identity.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Energy Object vs Device/Component/PowerInterface** — abstract management subject and concrete subtypes differ.
2. **Device vs Component** — whole equipment and part differ.
3. **Component vs PowerInterface** — part and energy-transfer boundary differ.
4. **physical containment vs PowerSource relationship** — part-of and supplies-energy are distinct.
5. **PowerSource vs Metering vs Aggregation** — three relationship semantics are distinct.
6. **nameplate power vs current power** — nominal and live values differ.
7. **actual vs estimated vs static measurement** — measurement provenance/caliber matters.
8. **power vs energy vs demand** — rate, accumulated quantity and interval average differ.
9. **Power State vs power measurement** — control/operating state and measured consumption differ.
10. **context role/category vs physical class** — deployment/business role is not equipment type.
11. **battery design capacity vs actual capacity vs charge** — design, degraded maximum and current stored amount differ.
12. **charging administrative vs operational state** — desired/control and actual state differ.
13. **battery physical index vs physical Battery instance** — connector/managed position continuity can survive replacement.
14. **battery state vs alarm threshold** — current value and notification rule differ.
15. **conceptual framework vs SNMP MIB carrier** — domain semantics and management-protocol realization differ.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely cross-cutting power structure:** Device/Component/PowerInterface separation;
- **likely relationship pattern:** power source, metering and aggregation modeled explicitly and independently from physical containment;
- **likely information pattern:** nameplate/static vs live measurement vs accumulated energy vs interval demand;
- **likely provenance pattern:** actual/estimated/static measurement caliber, method and accuracy;
- **likely state pattern:** Power State distinct from measured power/energy;
- **likely battery specialization:** design characteristics, current state, cycle history and alarm thresholds;
- **likely identity caution:** managed position/index and replaceable battery instance can differ;
- **scope caution:** EMAN defines energy-management anatomy, not the whole sensing equipment DIM;
- **binding caution:** MIB tables/OIDs/SNMP compliance are implementation bindings, not V2 classes/resources.

**No V2 module disposition is made in Phase A.**

---

**X02 status: COMPLETE.**

**Next frozen lineage:** X03 — IETF hardware management.

---

# X03 — IETF Hardware Management (RFC 8348)

## Source basis and evidence ceiling

**Frozen primary source ID:** 133.

**Primary inspected source:**

- RFC 8348, *A YANG Data Model for Hardware Management*, March 2018, Standards Track.

**Evidence note:** RFC 8348 is explicitly a YANG management data model for hardware on a single server. It is admitted as a cross-cutting physical-composition donor, not as a whole sensing-system model.

---

## 1. Source-native structural organization

RFC 8348 organizes hardware around one flat list of **Components**, with explicit parent/child references reconstructing physical hierarchy.

Each Component carries:

- name;
- hardware class;
- description;
- parent;
- parent-relative position;
- contained children;
- hardware/firmware/software revision;
- serial number;
- manufacturer;
- model;
- alias;
- asset ID;
- field-replaceable-unit flag;
- manufacture date;
- URI(s);
- UUID.

Optional substructures add:

- **state**
  - admin state;
  - operational state;
  - usage state;
  - alarm state;
  - standby state;
  - last state change.

- **sensor-data**
  - measured value;
  - value type;
  - scale;
  - precision;
  - sensor operational status;
  - units display;
  - timestamp;
  - update rate.

The model aligns Component classes to the IANA/ENTITY-MIB physical-class taxonomy.

---

## 2. Purpose of each partition

### Component

Purpose: provide a common identity/configuration/state record for any managed physical hardware component.

### Class

Purpose: identify what physical hardware class the Component represents.

### Parent / parent-rel-pos / contains-child

Purpose: reconstruct physical containment and sibling position while retaining a flat addressable component list.

### Identity/product fields

Purpose: preserve product/asset identity separately from topology.

### State

Purpose: distinguish several independent management-state dimensions.

### Sensor data

Purpose: allow a hardware component that acts as a sensor to publish its current measurement and measurement metadata without creating a second physical entity record.

### Notifications

Purpose: report hardware state transitions independently from polling current state.

---

## 3. Central concepts per partition

| Partition | Central concepts |
| --- | --- |
| Hardware inventory | hardware, component list, component name |
| Physical class | chassis, container, module, port, stack, fan, sensor, power supply, battery, CPU, storage drive, etc. |
| Physical hierarchy | parent, parent-rel-pos, contains-child |
| Product identity | serial-num, mfg-name, model-name, asset-id, UUID, revisions |
| Replaceability | is-fru |
| State | admin-state, oper-state, usage-state, alarm-state, standby-state |
| Measurement | sensor-data, value, type, scale, precision, status, units, timestamp, update rate |
| Change | last-change, hardware-state-change notifications |

---

## 4. Primary relationships

### Component → parent Component

Parent identifies the containing physical component.

### Parent → child Components

`contains-child` is the inverse operational-state view.

### Component → class

Hardware class identifies physical type.

### Component → sensor data

A component can carry sensor-data when it performs a sensor role.

### Component → state

State substructure belongs to the physical component.

### Component → external identity

physical-index maps to ENTITY-MIB when present; UUID/asset-id/URI provide additional identity keys.

---

## 5. Dependency boundaries

### Flat inventory vs hierarchy

The source stores Components in one flat list; parent references create containment. List membership itself does not imply hierarchy.

### Physical hierarchy vs class

Class says what a component is; parent says where it sits.

### Component vs sensor reading

Physical component identity and current sensor-data are separate structures.

### Configuration vs operational state

RFC 8348 follows NMDA and separates writable/intended configuration from operational/system state.

### YANG binding vs conceptual hardware distinctions

YANG tree paths and feature statements are the management representation, not physical-domain truth by themselves.

---

## 6. Intrinsic vs contextual standing

### Intrinsic

- hardware class;
- manufacturer/model/serial;
- hardware/firmware/software revision;
- UUID/asset identity;
- field replaceability;
- current component state;
- sensor capability/current reading where applicable.

### Contextual

- parent containment;
- parent-relative position;
- URI/external management references;
- system/server context.

The model is intentionally local to one managed hardware system/server.

---

## 7. Cross-cutting concepts

- component identity;
- physical class;
- containment;
- revisions;
- state;
- alarm;
- sensor reading;
- timestamp;
- UUID/asset ID;
- replaceability.

---

## 8. State / temporal / lifecycle organization

### Hardware state

Independent dimensions:
- administrative;
- operational;
- usage;
- alarm;
- standby.

### Temporal change

- state-last-changed;
- hardware collection last-change;
- state-change notifications.

### Product/lifecycle metadata

- manufacture date;
- revisions;
- FRU status.

### Limit

No full maintenance/service/work lifecycle is defined.

---

## 9. Composition / topology organization

Physical topology is explicit:

- flat Component inventory;
- parent link;
- relative position among siblings of same class;
- child inverse.

This is a **physical-containment topology**.

It does not model:
- functional grouping;
- deployment;
- network topology;
- power topology

as equivalent relationships.

---

## 10. Capability / function / behavior organization

RFC 8348 has limited function/capability semantics.

Hardware class and optional feature containers identify what kind of hardware/management data exists.

Sensor components can expose sensor-data.

It does not define general:
- device functions;
- commands;
- capabilities;
- mission behavior.

---

## 11. Information / output organization

The source distinguishes:

- inventory/product information;
- configuration;
- current state;
- sensor measurement;
- state-change notifications.

Sensor-data includes measurement value plus:
- type;
- scale;
- precision;
- units;
- operational status;
- timestamp;
- update rate.

---

## 12. Management / condition organization

Management/condition is central.

- state dimensions;
- alarm state;
- sensor operational status;
- revisions;
- replaceability;
- configuration;
- state-change notification.

The model is hardware-management oriented rather than application/mission oriented.

---

## 13. Provenance / identity / reference organization

Identity layers include:

- component name within model;
- physical-index into ENTITY-MIB;
- UUID;
- asset-id;
- manufacturer/model/serial;
- alias;
- URI(s).

Parent references use component names.

The source explicitly maps to ENTITY-MIB/ENTITY-SENSOR-MIB/ENTITY-STATE-MIB, preserving cross-management-model correspondence.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Component list membership vs physical parentage** — flat inventory does not imply containment.
2. **hardware class vs component identity** — type and instance differ.
3. **Component vs sensor-data** — physical hardware and its current reading differ.
4. **sensor hardware class vs whole-system sensing role** — one component class does not classify the entire equipment.
5. **parent vs parent-relative-position** — containing parent and sibling position are different.
6. **configuration vs operational state** — desired/writable settings and observed state differ.
7. **admin vs oper vs usage vs alarm vs standby state** — independent state dimensions must not collapse.
8. **asset-id vs UUID vs serial vs component name** — identity schemes serve different scopes.
9. **hardware revision vs firmware/software revision** — realization-version dimensions differ.
10. **physical-index vs durable component identity** — management-table index and real-world identity differ.
11. **current sensor value vs sensor operational status** — measurement and measurement-source condition differ.
12. **measurement timestamp vs state-last-changed** — data time and component-state-change time differ.
13. **FRU status vs component class** — replaceability is not equipment type.
14. **physical containment vs functional/network/power topology** — RFC 8348 only defines the physical hierarchy.
15. **YANG path vs physical relationship** — representation location should not be mistaken for domain containment.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely cross-cutting physical-composition pattern:** flat inventory plus explicit parent/relative-position hierarchy;
- **likely core equipment identity:** manufacturer/model/serial/revisions/UUID/asset ID kept distinct;
- **likely state pattern:** multiple independent administrative/operational/usage/alarm/standby dimensions;
- **likely measurement pattern:** component sensor reading separated from component identity and condition;
- **likely lifecycle detail:** manufacture date and FRU status without implying full service history;
- **scope caution:** hardware management does not supply sensing-function, deployment, observation or mission semantics;
- **binding caution:** YANG nodes/features/paths and ENTITY-MIB indexes are management-protocol/data-model carriers, not automatically V2 classes/relations.

**No V2 module disposition is made in Phase A.**

---

**X03 status: COMPLETE.**

**Next frozen lineage:** X04 — IETF interfaces / topology.

---

# X04 — IETF Interfaces / Network Topology

## Source basis and evidence ceiling

**Frozen primary source IDs:** 134, 136, 137.

**Primary inspected sources:**

- RFC 8343, *A YANG Data Model for Interface Management* (2018).
- RFC 8345, *A YANG Data Model for Network Topologies* (2018).
- RFC 2863, *The Interfaces Group MIB* (2000).

**Evidence note:** These RFCs define generic communications/interface/topology management, not sensor-equipment composition. They are admitted because they provide mature distinctions among interface identity, layering, network nodes, termination points, links and topology stacks.

---

## 1. Source-native structural organization

### Interface model

RFC 8343 organizes:

- Interface;
- interface type;
- enabled/configured state;
- admin/oper status;
- physical address;
- higher-layer interface(s);
- lower-layer interface(s);
- speed;
- statistics.

RFC 2863 provides the historical/architectural basis for:
- interface sublayers;
- interface stacks;
- multiplexing;
- physical/logical/virtual interface identity;
- separate administrative and operational state.

### Network topology model

RFC 8345 organizes:

- Network;
- Network Node;
- Termination Point;
- Link;
- Supporting Network;
- Supporting Node;
- Supporting Termination Point;
- network hierarchy/topology stack.

The abstract base network/topology model is designed to be augmented by:
- L1;
- L2;
- L3;
- service;
- technology-specific topology models.

---

## 2. Purpose of each partition

### Interface

Purpose: provide a generic, media-independent managed identity for a network interface.

### Interface layering

Purpose: represent protocol/media sublayers, aggregation and multiplexing without creating one opaque compound interface.

### Interface state/statistics

Purpose: separate configuration, operational status and traffic/error counters.

### Network

Purpose: represent one topology/inventory context.

### Node

Purpose: represent a topology vertex/network element abstraction.

### Termination Point

Purpose: anchor Links at a Node and represent connectivity endpoints.

### Link

Purpose: represent directed/undirected connectivity edge between Termination Points.

### Supporting network/topology

Purpose: map overlay/service/topology structures onto underlying topology structures.

---

## 3. Central concepts per partition

| Partition | Central concepts |
| --- | --- |
| Interface identity | interface name, type, ifIndex, physical address |
| Interface state | enabled, admin-status, oper-status, last-change |
| Interface layering | higher-layer-if, lower-layer-if, stack |
| Interface statistics | in/out octets/packets/errors/discards, discontinuity time |
| Network | network ID/type, supporting network |
| Node | node ID, supporting node |
| Termination point | termination-point ID, supporting termination point |
| Connectivity | Link, source/destination node/TP |
| Topology hierarchy | overlay/underlay, supporting networks, mappings |
| Model extension | technology-specific augmentation |

---

## 4. Primary relationships

### Interface ↔ higher/lower interface

Interfaces form layers/stacks:
- one-on-one;
- one-over-many aggregation;
- many-over-one multiplexing.

### Node → Termination Point

Node contains/owns termination points in topology model.

### Link → source/destination TP

Link connects termination points.

### Network → supporting network

A topology/network can be supported by one or more lower/underlying networks.

### Node/TP → supporting nodes/TPs

Specific topology elements can map to elements in supporting networks.

### Same device → multiple network nodes

RFC 8345 permits the same real device to have representations in multiple networks/topologies.

---

## 5. Dependency boundaries

### Physical interface vs logical interface

RFC 8343 supports both; interface identity is not automatically physical connector identity.

### Interface vs hardware component

Network interface model is separate from RFC 8348 physical hardware model.

### Interface layering vs physical containment

higher/lower protocol relation is not part-of hardware.

### Network node vs physical device

Topology Node is an abstract topology vertex and may represent:
- physical device;
- virtual function;
- service function;
- another topology-specific entity.

### Overlay vs underlay

A service/upper topology maps to but is not identical with supporting lower topology.

### Generic base vs technology-specific augmentation

Base structure remains stable while domain/network-specific data is added through augmentation.

---

## 6. Intrinsic vs contextual standing

### Intrinsic to interface

- type;
- configured state;
- operational state;
- interface counters;
- speed;
- address.

### Relational/contextual

- higher/lower layering;
- network membership;
- topology node;
- termination point;
- links;
- supporting topology mappings.

### Network-contextual

The same physical/virtual entity can have multiple topology representations depending on network layer/view.

---

## 7. Cross-cutting concepts

- identity;
- type;
- operational/admin state;
- statistics;
- layering;
- topology mapping;
- augmentation;
- client-configured vs system-controlled resources;
- overlay/underlay.

---

## 8. State / temporal / lifecycle organization

### Interface state

RFC 8343/RFC 2863 distinguish:
- enabled/configuration;
- administrative state;
- operational state;
- last change;
- statistics discontinuity.

### Interface creation

Interfaces can be:
- system-controlled/dynamically appearing;
- user-controlled/configured;
- pre-provisioned even when hardware absent.

### Network topology state

RFC 8345 supports:
- system-controlled/dynamically learned topology;
- client-configured topology;
- changes in underlay networks.

No equipment lifecycle beyond network/interface management is defined.

---

## 9. Composition / topology organization

This lineage defines **communications topology**, not physical equipment composition.

### Interface stack

higher/lower-layer relationships.

### Network graph

Network contains:
- Nodes;
- Termination Points;
- Links.

### Topology stack

Upper networks/topologies rely on lower supporting topologies.

### Mapping

Many-to-one and one-to-many mapping is explicitly allowed across layers.

### Important distinction

**interface stack, graph topology, topology hierarchy and physical assembly are separate concepts.**

---

## 10. Capability / function / behavior organization

Capability is limited to communications behavior:

- interface type;
- configured/operational state;
- bandwidth/speed;
- packet/counter behavior;
- topology-layer role.

Technology-specific capabilities are expected through augmentation.

No generic equipment-function model exists.

---

## 11. Information / output organization

Interface outputs include:
- counters;
- errors/discards;
- state;
- speed;
- addresses.

Topology output is graph/inventory structure.

These are management/state descriptions, not sensor observations.

---

## 12. Management / condition organization

Strong interface/network-management semantics include:

- enable/disable;
- admin/oper state;
- counters/errors;
- last change;
- topology changes;
- system-controlled vs configured resources.

Condition is limited to communication/interface health/status.

---

## 13. Provenance / identity / reference organization

Identity layers include:

- interface name;
- ifIndex;
- physical address;
- Node ID;
- Termination Point ID;
- Link ID;
- Network ID;
- URI/string identifiers.

Supporting/mapping relationships preserve lineage between topology representations.

The same device can be represented in multiple networks, so topology identity is explicitly view/context dependent.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Interface vs hardware component** — logical/managed interface and physical device are different.
2. **physical vs logical interface** — both are valid interface types.
3. **interface identity vs physical address** — managed identity and link-layer address differ.
4. **admin vs oper state** — intended/control and actual runtime state differ.
5. **interface vs interface layer** — one interface can be layered over/under others.
6. **layering vs physical containment** — protocol stack relation is not hardware part-of.
7. **aggregation vs multiplexing** — many-lower-to-one-upper and many-upper-to-one-lower are different structures.
8. **Node vs physical device** — topology vertex is an abstract network representation.
9. **Node vs Termination Point** — network element and connectivity endpoint differ.
10. **Termination Point vs Link** — endpoint and connectivity relation differ.
11. **network topology vs equipment composition** — communications graph is not a BOM.
12. **overlay vs underlay** — service/upper topology and supporting lower network differ.
13. **supporting mapping vs identity** — mapped objects across topology layers are related but not identical.
14. **same real device vs topology representation** — one device may have multiple Node representations.
15. **system-controlled vs client-configured topology/interface** — discovered/runtime and intended/configured structures differ.
16. **base model vs technology-specific augmentation** — generic graph semantics and domain-specific attributes differ.
17. **current counters vs historical continuity** — statistics discontinuity affects interpretation.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely communications structure:** Interface identity/layering separated from physical equipment identity;
- **likely topology pattern:** Node → TerminationPoint → Link graph;
- **likely cross-cutting:** admin/oper state, statistics, last change and configuration;
- **likely mapping pattern:** overlay/underlay/supporting topology correspondence without identity collapse;
- **likely identity caution:** same physical equipment can have multiple topology/network representations;
- **likely binding pattern:** generic base model plus technology-specific augmentation;
- **scope caution:** communications topology is contextual/cross-cutting and must not become the physical System composition tree;
- **binding caution:** YANG leafrefs/paths/ifIndex/network IDs are management-model representations rather than universal DIM identifiers.

**No V2 module disposition is made in Phase A.**

---

**X04 status: COMPLETE.**

**Next frozen lineage:** X05 — MIP / JC3IEDM.

---

# X05 — MIP / JC3IEDM

## Source basis and evidence ceiling

**Frozen primary source ID:** 29.  
**Frozen companion IDs:** 26, 30, 46.

**Primary identity/status evidence:**

- NATO/NISP record for *Joint C3 Information Exchange Data Model Baseline 3.1.4*, dated 14 February 2012.
- STANAG 5525 Edition 1 adopts JC3IEDM.

**Structural evidence inspected:**

- exact-version public transcription of *JC3IEDM — Overview — IPT3 — V3.1.4*;
- earlier public JC3IEDM overview material used only where the exact-version structure is unchanged/consistent.

**Evidence ceiling:** The complete JC3IEDM 3.1.4 specification package is not locally available. The public exact-version overview is sufficient to recover the high-level entity organization, item/type distinction, Action structure, Location, Capability, Context, Reporting-Data, status/affiliation and major relationships. This extraction does **not** assert lower-level schema details that are absent from that overview.

---

## 1. Source-native structural organization

JC3IEDM organizes multinational C2 information into two broad structural regions linked by reporting and associative entities.

### A. Object/situational structure

The lower/model-inventory side centers on:

1. **OBJECT-TYPE**
   - class/type-level description;
   - relatively persistent/static characteristics.

2. **OBJECT-ITEM**
   - individually identified instance;
   - more dynamic/current characteristics.

Major first-level Object categories include:

- Facility;
- Feature;
- Materiel;
- Organisation;
- Person.

Materiel-Type contains Equipment-type specializations.

The object side further includes:

- type classification of Items;
- Object-Item Status;
- Object-Item Location;
- Object-Item Association;
- Organisation Structure;
- Holding;
- Affiliation;
- Group Characteristic;
- Address;
- Object-Type Establishment.

### B. Location structure

- LOCATION;
- OBJECT-ITEM-LOCATION;
- vertical distance;
- coordinate systems;
- geometry/position semantics.

### C. Action/operational structure

The upper part centers on:

- **ACTION**
  - divided into Action-Task and Action-Event;
- ACTION-RESOURCE;
- ACTION-OBJECTIVE;
- ACTION-EFFECT;
- functional Action associations;
- temporal Action associations;
- Action Location;
- plans/orders;
- rules of engagement;
- candidate target lists.

### D. Capability structure

- CAPABILITY;
- Object-Type Capability;
- Object-Item Capability;
- Action-oriented capability/use relationships.

### E. Context structure

- CONTEXT;
- ACTION-CONTEXT;
- CONTEXT-OBJECT-ITEM relationships;
- Operational Information Groups;
- reporting-agent/organisation relationships;
- context status.

### F. Reporting / information pedigree structure

- **REPORTING-DATA**
  - records reporting information about much of the lower/object model;
  - allows information to be reused in planning, allocation, orders and execution;
- REFERENCE;
- SECURITY-CLASSIFICATION.

### G. Planning/order structure

- PLAN-ORDER;
- candidate targets;
- actions/resources/objectives/effects;
- Context/ROE.

The source-native high-level pattern is therefore:

> **persistent Type + dynamic Item + Location/Status/Associations + Action/Capability/Context + Reporting-Data/Reference/Security + Plans/Orders**

---

## 2. Purpose of each partition

### OBJECT-TYPE

Purpose: store relatively stable characteristics that apply to a class of objects and can be inherited/applied to classified Items.

### OBJECT-ITEM

Purpose: represent an individually identified object whose location, status, holdings, relationships and other operational information change over time.

### Item-Type classification

Purpose: avoid duplicating type-level characteristics on each instance while permitting an Item to be classified by one or more Types.

### LOCATION

Purpose: represent geometric/geospatial position separately from the Object or Action it locates.

### STATUS

Purpose: describe changing operational state without replacing persistent Object identity.

### HOLDING

Purpose: represent resources/types possessed/held by an Object-Item.

### AFFILIATION

Purpose: assign national, ethnic, functional, exercise, religious or other allegiance/group affiliation.

### ACTION

Purpose: describe military/civil operational activity, including both planned Tasks and unplanned Events.

### ACTION-RESOURCE / OBJECTIVE / EFFECT

Purpose: distinguish what participates in an Action, what the Action focuses on, and what effect is assessed/expected.

### CAPABILITY

Purpose: express potential ability to perform a function/mission, achieve an objective or provide a service.

### CONTEXT

Purpose: package background/circumstances/constraints/operational-overlay information relevant to Objects and Actions.

### REPORTING-DATA

Purpose: preserve reporting/source information and make reported object/status/location/capability information reusable across situational awareness, planning and execution.

---

## 3. Central concepts per partition

| Partition | Central concepts |
| --- | --- |
| Type/model | OBJECT-TYPE, Facility-Type, Feature-Type, Materiel-Type, Organisation-Type, Person-Type |
| Instance | OBJECT-ITEM, Facility, Feature, Materiel, Organisation, Person |
| Classification | OBJECT-ITEM-TYPE |
| State | OBJECT-ITEM-STATUS |
| Location | LOCATION, OBJECT-ITEM-LOCATION, ACTION-LOCATION, coordinate systems |
| Composition/organisation | OBJECT-ITEM-ASSOCIATION, ORGANISATION-STRUCTURE, HOLDING |
| Affiliation | AFFILIATION, Object-Item Affiliation |
| Capability | CAPABILITY, Object-Type/Item capability |
| Activity | ACTION, ACTION-TASK, ACTION-EVENT |
| Action roles | ACTION-RESOURCE, ACTION-OBJECTIVE, ACTION-EFFECT |
| Action structure | functional association, temporal association, action hierarchy |
| Context | CONTEXT, ACTION-CONTEXT, Operational Information Group |
| Reporting/provenance | REPORTING-DATA, REFERENCE, SECURITY-CLASSIFICATION |
| Planning | PLAN-ORDER, Candidate Target List, Rule of Engagement |

---

## 4. Primary relationships

### OBJECT-ITEM → OBJECT-TYPE

Every specific Item must be associated with at least one Type.

Type characteristics then apply to the Item.

### OBJECT-ITEM → LOCATION

Associative structure relates an Item to one or more Locations.

### OBJECT-ITEM → STATUS

Status is attached to the Item without becoming its identity.

### OBJECT-ITEM ↔ OBJECT-ITEM

Object associations and Organisation Structure express relationships among individual objects.

### OBJECT-ITEM → HOLDING / Type

Holding relates an Item to types/resources it possesses.

### Object → CAPABILITY

Capabilities can apply at Type or Item level.

### ACTION → Object roles

Objects/Types participate in Action as:
- Resource;
- Objective;
- subject of Effect.

### ACTION ↔ ACTION

Functional and temporal associations build hierarchies and ordering.

### ACTION → LOCATION

Action can be directly located independent of resource/objective location.

### ACTION → CONTEXT

Context supplies background, constraints, preconditions/resulting conditions and historical snapshots.

### CONTEXT → Objects / Reporting / Organisations

Context can relate to Object-Items, Operational Information Groups, reporting data and reporting organisations.

### Reported data → domain information

REPORTING-DATA supplies report/source information to many lower-level situational facts.

---

## 5. Dependency boundaries

### Type vs Item

Stable class characteristics and dynamic instance information are explicitly separated.

### Object vs Location

Geometry/position is a related entity, not embedded identity.

### Object vs Status

Current state is separate from persistent object identity/type.

### Object vs Action

What exists and what happens/gets planned are separate model nuclei.

### Action vs Plan/Order

Actions are operational activities; plans/orders organize/authorize them.

### Action vs Context

Context constrains/backgrounds Action but is not the Action.

### Domain fact vs Reporting-Data

Reported information and its pedigree/report metadata are separate from the fact it supports.

### Lower vs upper model

The exact-version overview explicitly describes:
- lower part focused on situational objects and their current information;
- upper part focused on plans/orders/actions/capability/context;
- associative/reporting structures connecting them.

---

## 6. Intrinsic vs contextual standing

### Type-level intrinsic

- relatively persistent equipment/type characteristics;
- establishment/authorized structure;
- general capabilities.

### Item-level current/intrinsic

- individual identity;
- current status;
- holdings;
- item-specific capability.

### Contextual/relational

- location;
- affiliation;
- organisational association;
- holdings relative to another object/type;
- operational Context;
- reporting organisation;
- Action role.

### Event/activity-specific

- Action;
- task/event;
- resource/objective/effect;
- time/location of Action.

The model explicitly expects instance-level information to change independently from type identity.

---

## 7. Cross-cutting concepts

- reporting/pedigree;
- security classification;
- reference;
- status;
- time;
- location;
- affiliation;
- capability;
- context;
- organisation;
- Action relationships.

REPORTING-DATA is especially cross-cutting because it records pedigree/report information for facts across the lower object model.

---

## 8. State / temporal / lifecycle organization

JC3IEDM models operational time/state strongly.

### Object state

OBJECT-ITEM-STATUS records changing operational state.

### Item location/time

Location associations can be time-sensitive/report-driven.

### Action time

Action has:
- Tasks;
- Events;
- temporal associations;
- direct Location;
- planning/execution relationships.

### Context history

Context can preserve historical snapshots/traces of actual plan execution.

### Reporting time

Reporting data provides temporal/report context to facts.

### Limit

The model is operational C2 lifecycle, not detailed maintenance/service asset lifecycle.

---

## 9. Composition / topology organization

Several different structural relations coexist.

### Object association

General relationships between Object-Items.

### Organisation structure

Explicit organisational hierarchy/structure.

### Holding

Possession/resource relationship.

### Type establishment

Authorized/establishment composition at Type level.

### Location topology

Object-to-location relation is independent.

### Action hierarchy

Functional Action associations create higher/lower activity structures.

### Context grouping

Operational Information Groups/Context organize related facts.

These are not one universal part-of tree.

---

## 10. Capability / function / behavior organization

Capability is explicit and can be associated with Object-Type or Object-Item.

Action describes actual/planned behavior.

The model therefore distinguishes:

- **potential ability** — Capability;
- **object/type possessing ability**;
- **actual/planned activity** — Action;
- **role in activity** — Resource/Objective;
- **effect** — Action Effect.

This is a strong source-native capability/behavior separation.

---

## 11. Information / output organization

JC3IEDM is an information-exchange model rather than sensor-output model.

It organizes:

- object facts;
- status;
- location;
- capability;
- holdings;
- Action;
- plans/orders;
- context;
- reporting pedigree;
- reference/security information.

Reports can describe events/activity even where no suitable physical Object-Item exists, using direct Action-Location and Object-Type as needed.

---

## 12. Management / condition organization

Management/condition is operational rather than equipment-maintenance oriented.

Relevant structures include:

- status;
- readiness/capability;
- holdings;
- organisation;
- affiliation;
- plan/order/action;
- context;
- reporting.

No detailed generic health/fault/BIT/service/work model is exposed by the reviewed overview.

---

## 13. Provenance / identity / reference organization

### Object identity

OBJECT-ITEM identifies individual entities.

### Type identity

OBJECT-TYPE identifies class/type.

### Reporting provenance

REPORTING-DATA records report/pedigree information associated with operational facts.

### Reference

REFERENCE allows external/document references.

### Security

SECURITY-CLASSIFICATION is separately modeled.

### Context/reporting agent

CONTEXT and organisation associations can identify reporting/establishing organisations.

The model therefore distinguishes domain object identity from reporting/provenance/security metadata.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **OBJECT-TYPE vs OBJECT-ITEM** — class/type and individual instance are foundationally distinct.
2. **type characteristics vs item state** — persistent classification semantics and dynamic current information differ.
3. **classification vs identity** — an Item can have multiple Type classifications without becoming those Types.
4. **OBJECT-ITEM vs LOCATION** — object and geometry are different entities.
5. **OBJECT-ITEM vs STATUS** — persistent subject and changing operational state differ.
6. **OBJECT-ITEM vs ACTION** — object and activity are separate.
7. **ACTION-TASK vs ACTION-EVENT** — planned task and occurrence/event differ.
8. **ACTION-RESOURCE vs ACTION-OBJECTIVE vs ACTION-EFFECT** — participant, focus and result/effect are distinct roles.
9. **Action functional vs temporal association** — hierarchy/function and timing relationships differ.
10. **Capability vs Action** — potential ability and actual/planned behavior differ.
11. **Context vs Action** — background/constraint/snapshot and activity differ.
12. **reporting data vs reported fact** — provenance/report metadata and domain information differ.
13. **holding vs component/organisation structure** — possession/resource allocation is not automatically physical part-of.
14. **Organisation Structure vs general Object association** — formal structure and arbitrary relationship differ.
15. **Affiliation vs organisation membership/structure** — allegiance/classification and structural relationship differ.
16. **Location of Action vs location of resource/objective** — activity can have independent geometry.
17. **lower situational model vs upper planning/action model** — current world state and planning/execution structures differ.
18. **security classification vs object/type classification** — information security and domain type semantics differ.
19. **candidate target vs ordinary Object** — planning designation is contextual, not intrinsic object identity.
20. **broad C2 object model vs sensing-equipment anatomy** — JC3IEDM context structures should not be promoted as whole equipment modules merely because they are mature.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely operational-context pattern:** persistent object/type identity separated from changing status, location and affiliation;
- **likely model/instance pattern:** OBJECT-TYPE vs OBJECT-ITEM;
- **likely capability pattern:** Capability distinct from Action and Action roles;
- **likely mission/activity pattern:** Action with Resource, Objective, Effect, hierarchy and temporal relations;
- **likely contextual grouping:** Context as background/constraint/snapshot separate from Action;
- **likely provenance pattern:** REPORTING-DATA/REFERENCE/SECURITY separate from reported domain facts;
- **likely organizational pattern:** organisation structure, affiliation and holdings remain distinct relationship kinds;
- **scope caution:** JC3IEDM is much broader than the V2 equipment domain and is useful mainly for operational/mission relationships around the System;
- **evidence ceiling:** detailed exact 3.1.4 entity/cardinality semantics beyond the public overview remain unavailable;
- **binding caution:** JC3IEDM relational entities and MIP exchange realization are not automatically V2 classes/resources or NATO/MIP conformance obligations.

**No V2 module disposition is made in Phase A.**

---

**X05 status: COMPLETE.**

**Next frozen lineage:** X06 — NIEM.

---

# X06 — NIEM 6.0

## Source basis and evidence ceiling

**Frozen primary source IDs:** 64, 75, 76, 78–86.  
**Frozen companion IDs:** 60–63, 65–74, 77, 87, 88.

**Primary inspected sources:**

- OASIS NIEMOpen, *NIEM Model Version 6.0*, OASIS Standard.
- NIEM Core Schema 6.0.
- frozen NIEM 6.0 domain schemas:
  - CBRN;
  - Cyber;
  - Intelligence;
  - Military Operations;
  - Military Operations–USMTF;
  - Screening.
- frozen Auxiliary, GML Adapter, JSON-LD context and Domain Schema Collection artifacts.

**Architecture companion inspected:**

- NIEM Naming and Design Rules (NDR) 6.0 for the architecture mechanisms explicitly referenced by the NIEM Model:
  - associations;
  - augmentations;
  - roles;
  - representations;
  - references;
  - adapters.

**Evidence note:** NIEM is a multi-domain exchange model, not a sensing-equipment ontology. This extraction therefore focuses on the source-native way NIEM partitions and composes information, not on enumerating the thousands of domain properties/types. Machine-readable reference schemas are normative for the Work Product; the prose architecture governs how those components are understood and reused.

---

## 1. Source-native structural organization

NIEM 6.0 is explicitly a **collection of reusable properties and types defined in namespaces organized by governance/authoritative source**.

### A. Model content partitions

The NIEM Model defines seven major namespace/content categories:

1. **NIEM Core**
   - general-purpose, cross-domain content;
   - collaboratively governed;
   - intended for reuse across communities.

2. **Domains**
   - community-of-interest namespaces with formal governance bodies;
   - frozen corpus includes CBRN, Cyber, Intelligence, Military Operations, Military Operations–USMTF and Screening.

3. **Codes**
   - code-set namespaces.

4. **Adapters**
   - mechanisms wrapping non-NIEM-conformant external standards for use inside NIEM exchanges.

5. **Auxiliary**
   - community/standard content without the formal governance requirements of a NIEM Domain.

6. **External**
   - schemas/standards defined outside NIEM and intentionally kept non-conformant where external reuse yields greater interoperability.

7. **Utility**
   - architecture/support namespaces for:
     - identifiers/references;
     - linked data;
     - security markup;
     - code lists;
     - schema/serialization infrastructure.

### B. Model components

The basic reusable building blocks are:

- **Types**
  - classes/data structures.

- **Properties**
  - elements/attributes defining facts/relationships/values.

- **Objects**
  - instances of structured types.

- **Simple values / codes**
  - literal/controlled values.

### C. Relationship architecture

The NDR provides reusable mechanisms for:

- **Associations**
  - explicit relationship objects among properties/entities.

- **Augmentations**
  - add properties from one namespace/community to a class owned by another namespace without modifying/redefining the original class.

- **Roles**
  - represent related but distinct roles of the same entity in one message/exchange.

- **Representations**
  - alternate representations of the same conceptual property/type, supporting multiple representation choices.

- **References**
  - refer to an object elsewhere in a message rather than duplicate it.

- **Adapters**
  - incorporate external-standard structures.

### D. Exchange specialization

Implementations select needed NIEM components and can add local extension content when the reference model does not satisfy the business requirement.

The source-native pattern is therefore:

> **governed reusable component library → Core/domain ownership → explicit relationships/roles/augmentations → exchange-specific selection/extension → serialization**

rather than one universal object hierarchy.

---

## 2. Purpose of each partition

### NIEM Core

Purpose: own semantics that are sufficiently general and reusable across multiple domains.

### Domain

Purpose: let an authoritative community govern specialized concepts without forcing them into Core.

### Code namespace

Purpose: maintain controlled value sets separately from object/property semantics.

### Adapter

Purpose: preserve and reuse an external standard's structure rather than re-authoring it merely to satisfy NIEM syntax.

### Auxiliary

Purpose: support useful community/standard content that does not have a formally governed NIEM Domain.

### External

Purpose: retain genuinely external standards as external, when that provides greater interoperability.

### Utility

Purpose: provide structural/technical mechanisms supporting reference, security, linked data, code lists and exchange architecture.

### Association

Purpose: model relationships explicitly as first-class content when a simple property reference is insufficient.

### Augmentation

Purpose: allow one domain/namespace to add content to another namespace's type without taking ownership of or modifying that type.

### Role

Purpose: allow the same underlying entity to appear in distinct semantic roles in an exchange.

### Representation

Purpose: allow alternate ways to represent the same conceptual information while preserving common semantics.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Reusable model component | Property, Type, Object, simple value |
| Governance | Namespace, Core, Domain, authoritative source |
| Controlled vocabulary | Code namespace, code type/list |
| Relationship | Association, AssociationType |
| Cross-domain extension | Augmentation, AugmentationType/Point |
| Entity role | Role/object extension, shared URI/reference identity |
| Alternate form | Representation |
| Object reuse | reference, URI/ID, referenceable object |
| External-standard integration | Adapter, External namespace |
| Exchange specialization | reference schema subset, extension schema, message model |
| Security/context infrastructure | utility/auxiliary namespaces, security markup |
| Serialization | XML reference schemas, JSON/JSON-LD representation support |

---

## 4. Primary relationships

### Type → Properties

A NIEM Type defines which properties can describe an object/value of that type.

### Property → Type/value

Properties are typed and can represent:
- objects;
- simple values;
- relationships;
- references.

### Core ↔ Domain

Domains reuse Core components and can specialize/add domain-owned semantics without duplicating Core meaning.

### Namespace A → augmentation of Namespace B type

An augmenting namespace can add a property to a type owned by another namespace without changing the augmented namespace.

This is specifically designed for multi-domain composition.

### Association → participating objects/properties

Associations create explicit relationship objects among domain entities.

### Role → same underlying entity

Different Role objects can be linked to one entity identity in the message, preserving role-specific information without asserting multiple real-world entities.

### Adapter → external content

Adapter wraps external-standard content so it can participate in a NIEM-conformant exchange without claiming that the external standard itself is NIEM-conformant.

### Exchange → selected model components

A conforming exchange uses the subset of NIEM components required for the business need and extends only when necessary.

---

## 5. Dependency boundaries

### Core vs Domain

General reusable semantics and community-specific semantics have different governance ownership.

### Domain vs local extension

A NIEM Domain is a governed reference-model namespace; an exchange-specific extension does not become Domain/Core simply because one implementation needs it.

### NIEM component vs external standard

Adapters/external namespaces explicitly protect this boundary.

### Model vs serialization

NIEM architecture has an underlying model with language-specific representations. XML is normative in the frozen 6.0 Work Product, while JSON-LD/other serializations are separate representations.

### Class/type vs augmentation

Augmented content is not part of the original owning namespace merely because it is usable on that type.

### Entity vs role

Role-specific message objects can refer back to the same entity.

### Reference model vs message model

The reference model supplies reusable semantics; a message/exchange model selects and constrains what is actually exchanged.

---

## 6. Intrinsic vs contextual standing

NIEM does not define one universal intrinsic/context split because it spans many domains.

Instead, source-native ownership and relationship mechanisms distinguish concerns:

### Potentially intrinsic

Properties owned by the object's reference type/core/domain definition.

### Contextual/relationship-specific

- Association objects;
- role objects;
- augmentations from another domain;
- exchange-specific extension content;
- metadata/security/reference objects.

### Governance contextual

The namespace that defines a property signals the authority/community responsible for its semantics, but namespace ownership is not itself a real-world part-of relation.

---

## 7. Cross-cutting concepts

NIEM is built for cross-cutting reuse.

Major cross-cutting mechanisms include:

- NIEM Core;
- identifiers;
- names;
- locations;
- dates/times;
- organisations/persons;
- associations;
- augmentation;
- metadata;
- references;
- roles;
- code lists;
- security markup;
- external-standard adapters.

A single domain object can therefore be described by:
- Core content;
- its owning Domain;
- augmentations from other Domains;
- exchange-local extensions
without duplicating the base object.

---

## 8. State / temporal / lifecycle organization

NIEM has no universal lifecycle model.

Time/state semantics are defined by reusable/domain components relevant to the business exchange:

- dates;
- status objects/codes;
- events/activities;
- effective periods;
- domain-specific history structures.

Metadata in NIEM 6.0 is treated like ordinary objects and can be included/augmented where applicable.

**Evidence result:** lifecycle/state is domain/exchange-specific rather than a central architecture partition.

---

## 9. Composition / topology organization

NIEM provides **relationship composition mechanisms**, not one fixed equipment topology.

### Object composition

Types contain properties that may be nested object properties.

### Association

Explicit relationship object can join multiple entities.

### Augmentation

Adds cross-domain content to an existing object without changing its source type.

### Role

Represents one entity playing multiple semantic roles.

### Reference

Allows graph-like object reuse instead of duplication.

### Domain/core structure

Namespace organization is governance/model ownership, not equipment topology.

The architecture supports many topology models but does not prescribe one generic part-of tree.

---

## 10. Capability / function / behavior organization

NIEM itself does not define one generic equipment-capability architecture.

Capabilities/functions are represented where Core or Domains define applicable:
- capability;
- activity;
- function;
- resource;
- action;
- status
components.

Military/CBRN/Screening/etc. Domains can supply specialized operational semantics.

The architecture contribution is instead:
- reuse existing component if semantics match;
- derive/augment rather than needlessly duplicate;
- keep specialized ownership visible.

---

## 11. Information / output organization

NIEM structures information as reusable components assembled into **business information exchanges**.

Different information kinds can be modeled through:
- object types;
- associations;
- activities/events;
- status;
- measures;
- documents;
- reports;
- domain-specific structures.

The model does not impose a universal split analogous to Observation vs Command; those distinctions depend on the selected domain content.

The exchange model selects only information required for the business exchange from the larger reference model.

---

## 12. Management / condition organization

No universal equipment-management/condition partition exists.

Condition/management semantics appear in relevant Domain/Core structures and can be:

- reused;
- augmented;
- extended;
- related through associations.

The architecture's main contribution is preventing a domain from redefining another domain's established semantics when reuse/augmentation can preserve them.

---

## 13. Provenance / identity / reference organization

NIEM has substantial identity/reference architecture.

### IDs/references

Utility structures support:
- identifiers;
- object references;
- URI-based linkage;
- linked-data interpretation.

### Roles

NIEM 6.0 uses standard type extension plus shared URI/reference identity to relate different roles of the same entity.

### Metadata

Metadata is treated as normal object content in 6.0 and can be included/augmented.

### Namespace provenance

Namespace indicates governance/source of component semantics.

### External/adapters

Adapter/external namespaces preserve the pedigree of external standards.

The architecture therefore separates:
- entity identity;
- role representation;
- reference identity;
- semantic ownership/governance;
- exchange-local representation.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Core vs Domain** — general cross-domain semantics and community-owned specialization have different ownership.
2. **Domain vs exchange extension** — governed reference content and local message need are different.
3. **NIEM component vs external standard content** — adapter use does not make the external standard NIEM-native.
4. **Adapter vs re-authored NIEM concept** — wrapping external semantics and recreating them are different.
5. **Type vs Property** — class/structure and one fact/relationship are distinct model components.
6. **object vs reference to object** — repeated occurrence/reference must not create false duplicate entities.
7. **entity vs role** — one entity can play multiple roles without becoming multiple real-world entities.
8. **role-specific data vs base entity data** — contextual role content should not pollute the entity's universal intrinsic definition.
9. **augmentation vs ownership** — property from another namespace does not become part of the original namespace's definition.
10. **augmentation vs type extension** — multi-domain augmentation has different governance/combination semantics than single-inheritance extension.
11. **Association vs simple containment/property** — explicit relationship object can carry meaning beyond nested structure.
12. **Representation vs concept** — alternate representation forms do not create different domain concepts.
13. **reference model vs message/exchange model** — broad reusable vocabulary and one business exchange are different abstraction levels.
14. **namespace structure vs real-world topology** — governance packaging must not be interpreted as equipment/module composition.
15. **code list vs domain property** — controlled values and the property they qualify are different.
16. **security/metadata vs substantive object semantics** — cross-cutting markup/content should not redefine the subject.
17. **serialization vs semantic model** — XML/JSON-LD syntax does not own business meaning.
18. **reuse vs duplication** — NIEM conformance explicitly discourages needless duplicate semantics.
19. **multi-domain overlap vs one universal class** — harmonization does not erase domain-specific authority or distinctions.
20. **model conformance vs application-profile conformance** — using NIEM components correctly is not the same as conforming to the future V2 profile.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely architecture/governance pattern:** common Core semantics separated from domain/specialization ownership;
- **likely extension pattern:** augment established concepts rather than fork/redefine them for every specialization;
- **likely relationship pattern:** Associations and Roles for contextual semantics that should not become intrinsic properties;
- **likely external-source pattern:** Adapters preserve externally owned structures without falsely claiming native implementation;
- **likely identity/reference pattern:** one entity can be referenced/reused across roles and message contexts;
- **likely profile pattern:** broad reference model vs selected exchange/profile model;
- **likely cross-cutting:** metadata/security/reference mechanisms independent from substantive domain classes;
- **scope caution:** NIEM's namespace/domain architecture is governance/information-model structure, not a candidate physical sensing-system module taxonomy;
- **binding caution:** XSD namespaces/substitution/augmentation points are NIEM representation mechanisms and must not be copied mechanically into the V2 DIM.

**No V2 module disposition is made in Phase A.**

---

**X06 status: COMPLETE.**

**Next frozen lineage:** X07 — NIST IoT Device Cybersecurity Capability Core Baseline.

---

# X07 — NISTIR 8259A IoT Device Cybersecurity Capability Core Baseline

## Source basis and evidence ceiling

**Frozen primary source ID:** 108.

**Primary inspected source:**

- NISTIR 8259A, *IoT Device Cybersecurity Capability Core Baseline*, May 2020.

**Evidence note:** The frozen source defines **six** baseline technical capabilities. NIST's later online Technical Device Cybersecurity Capabilities Catalog has subsequently expanded/refined the catalog and currently includes an additional Device Security capability. That later addition is outside the frozen 2020 NISTIR 8259A source and is not imported into this extraction.

NISTIR 8259A is a cybersecurity capability baseline for IoT devices, not a whole device/domain information model.

---

## 1. Source-native structural organization

NISTIR 8259A organizes IoT device cybersecurity into six technical capability partitions:

1. **Device Identification**
2. **Device Configuration**
3. **Data Protection**
4. **Logical Access to Interfaces**
5. **Software Update**
6. **Cybersecurity State Awareness**

Each capability is described through:

- a capability statement;
- common elements;
- rationale;
- reference examples.

The baseline treats these as capabilities implemented through the IoT device's **hardware and software**.

---

## 2. Purpose of each partition

### Device Identification

Purpose: ensure the device can be uniquely identified both:
- logically; and
- physically.

### Device Configuration

Purpose: permit authorized change of device software configuration and restoration of a secure configuration.

### Data Protection

Purpose: protect device-stored/transmitted data against unauthorized access/modification.

### Logical Access to Interfaces

Purpose: restrict logical access to local/network interfaces, protocols and services to authorized entities.

### Software Update

Purpose: allow authorized secure/configurable device software update.

### Cybersecurity State Awareness

Purpose: make cybersecurity-relevant device state/events available to authorized entities for monitoring, incident detection, investigation and maintenance of secure operation.

---

## 3. Central concepts per partition

| Partition | Central concepts |
| --- | --- |
| Identification | logical identifier, physical identifier, authorized access to identifier |
| Configuration | configuration settings, authorized entity, secure configuration, restore |
| Data protection | stored data, transmitted data, confidentiality/integrity, authorized access |
| Interface access | local interface, network interface, protocol, service, authorization/authentication |
| Software update | update mechanism, authorization, integrity/authenticity, rollback/configurability where applicable |
| State awareness | cybersecurity state, event information, logging/monitoring, authorized access |

---

## 4. Primary relationships

### Device → identifiers

One IoT device can have:
- logical identity;
- physical identity.

The values may be the same but need not be.

### Device → configuration

Authorized entities can change/restore device software configuration.

### Device → data

The device stores/transmits data requiring protection.

### Device → interfaces/protocols/services

Logical access controls apply to the device's interaction surfaces.

### Device → software update

Authorized update changes the device software state.

### Device → cybersecurity state

The device reports/retains information needed to understand security condition/events.

The source is capability-centric; it does not define a generic topology among internal components.

---

## 5. Dependency boundaries

### Device capability vs manufacturer support process

8259A covers **technical device capabilities**. NISTIR 8259B separately covers non-technical supporting capabilities by manufacturers/third parties.

### Identification vs authentication

Unique identification supports management/authentication but is not automatically authentication itself.

### Configuration vs access control

Configuration is one capability; restriction of interface access is another, though they interact.

### Data protection vs interface access

Protecting data and controlling who can reach interfaces are separate control objectives.

### Software update vs configuration

Updating executable software and changing configuration settings are different operations.

### State awareness vs device state itself

Reporting cybersecurity-relevant state and the state/condition being reported are distinct.

---

## 6. Intrinsic vs contextual standing

### Intrinsic device capabilities

All six baseline areas are intended as capabilities of the IoT device itself, implemented through its hardware/software.

### Contextual/organizational

- which entities are authorized;
- what cybersecurity events/states must be reported;
- which data require protection;
- policy for configuration/update/access;
- organizational cybersecurity controls.

The baseline deliberately leaves specific organizational requirements/profile tailoring outside the universal core baseline.

---

## 7. Cross-cutting concepts

Cross-cutting themes include:

- authorization;
- identity;
- interfaces;
- configuration;
- data;
- software;
- cybersecurity state/event awareness;
- device lifecycle operations such as deployment/decommissioning/recovery;
- physical vs logical access/identity.

Many capabilities depend partly on configuration and authorization.

---

## 8. State / temporal / lifecycle organization

NISTIR 8259A does not define a universal device lifecycle model, but several capabilities imply temporal/lifecycle behavior.

### Identification across lifecycle

Physical identity remains useful when logical identity is unavailable, including deployment/decommissioning/failure contexts.

### Configuration state

Device can change configuration and restore a secure configuration.

### Software version/update state

Device software can transition through authorized updates.

### Cybersecurity state

Device can report current security state/events and preserve information useful for investigation.

### Limit

Procurement, installation, maintenance work and operational mission history are outside the capability baseline.

---

## 9. Composition / topology organization

No generic device composition/BOM/topology model is defined.

The baseline treats the IoT device as the capability-bearing subject.

Interfaces are exposed attack/interaction surfaces but are not modeled as a physical topology.

---

## 10. Capability / function / behavior organization

Capability is the central organizing concept.

Each baseline capability is:

- an ability the device provides through its hardware/software;
- decomposed into common functional elements;
- justified by cybersecurity controls/outcomes.

The source therefore provides a reusable pattern for **cross-cutting device capability areas** rather than a device-function taxonomy.

---

## 11. Information / output organization

The baseline distinguishes several information concerns:

- identifiers;
- configuration information;
- protected stored/transmitted data;
- interface/protocol/service access;
- software/update data;
- cybersecurity state/event/log information.

Cybersecurity State Awareness may require:
- persistent event records;
- external monitoring signals;
- local alerts.

The mechanism is implementation/context dependent.

---

## 12. Management / condition organization

The entire baseline is management/security oriented.

It establishes device-manageable concerns around:

- inventory/identity;
- authorized configuration;
- access control;
- data protection;
- software update;
- cybersecurity state monitoring.

Cybersecurity state is not equivalent to generic operational health; it is the state needed to support security controls, vulnerability management and incident detection.

---

## 13. Provenance / identity / reference organization

Identity is explicit.

### Logical identifier

Used for automated management/monitoring and potentially authentication.

### Physical identifier

Accessible physically to authorized entities and useful when logical access is unavailable.

The source explicitly says physical and logical identifiers may share a value but need not.

Cybersecurity-event information can preserve evidence about state changes, but a general provenance graph is not defined.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **logical identifier vs physical identifier** — different access/use contexts even when values happen to match.
2. **identification vs authentication/authorization** — knowing which device and proving/allowing access are distinct.
3. **configuration vs software update** — settings and executable software transitions differ.
4. **configuration capability vs current configuration** — ability to change and actual values differ.
5. **data protection vs interface access** — safeguarding information and restricting interaction surfaces are different.
6. **local interface vs network interface** — physical/local and remote/network exposure may require different controls.
7. **interface vs protocol vs service** — access surface, communication rules and provided functionality are distinct.
8. **authorized entity vs device capability** — policy/actor context is not an intrinsic device component.
9. **cybersecurity state vs ordinary operational state** — security-relevant awareness has a specific purpose.
10. **state event/log vs state itself** — evidence about changes and current condition differ.
11. **technical device capability vs non-technical manufacturer support** — 8259A and 8259B deliberately separate them.
12. **core baseline vs tailored profile** — broadly applicable capability baseline and sector/application requirements are different.
13. **2020 six-capability baseline vs later NIST catalog expansion** — later catalog content must not be silently back-ported into the frozen source.
14. **IoT device security capability vs sensing-domain function** — cybersecurity cross-cutting structure should not become the V2 system chassis or mission-function taxonomy.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely cross-cutting capability partition:** identification, configuration, data protection, interface access, software update and security-state awareness;
- **likely identity pattern:** logical vs physical identity deliberately separate;
- **likely management pattern:** configuration/update/access/state are independent management concerns;
- **likely state/provenance pattern:** security-state awareness may require persistent events/logs separate from current state;
- **likely profile-tailoring pattern:** common baseline can be specialized by application/sector requirements;
- **scope caution:** NISTIR 8259A is cybersecurity-specific and does not define sensing/equipment anatomy beyond the cross-cutting device capabilities;
- **edition caution:** later NIST catalog additions are outside the frozen 2020 baseline.

**No V2 module disposition is made in Phase A.**

---

**X07 status: COMPLETE.**

**Next frozen lineage:** X08 — OGC Observations, Measurements and Samples (OMS).

---

# X08 — OGC Observations, Measurements and Samples (OMS) 3.0

## Source basis and evidence ceiling

**Frozen primary source ID:** 8.  
**Frozen companion ID:** 15.

**Primary inspected source:**

- Open Geospatial Consortium, *Abstract Specification Topic 20 — Observations, Measurements and Samples*, OGC 20-082r4, version 3.0.0.
- Jointly aligned with ISO 19156:2023.

**Companion evidence:**

- ISO 19156:2023 publication metadata/lineage as represented in the frozen corpus.

**Evidence note:** The complete OGC 20-082r4 PDF is available in the project and was used directly. This extraction uses the 2023/3.0 structure, not the older ISO 19156:2011 OM model except where the current standard itself explains migration/lineage differences.

---

## 1. Source-native structural organization

OMS 3.0 is deliberately organized into separate **Observation** and **Sample** conceptual schemas, each with multiple abstraction levels.

### A. Three abstraction levels

For both Observations and Samples, the standard distinguishes:

1. **Conceptual schema**
   - interface-level semantics;
   - technology/application-schema neutral.

2. **Abstract Core application schema**
   - abstract classes realizing the conceptual interfaces.

3. **Basic application schema**
   - ready-to-use concrete classes that can be adopted or specialized.

This is itself an important structural pattern: meaning is defined first, then abstract realization, then concrete reusable application-schema classes.

### B. Observation conceptual structure

Primary concepts include:

- **Observation**
- **ObservationCharacteristics**
- **ObservationCollection**
- **ObservingCapability**
- **ObservableProperty**
- **ObservingProcedure**
- **Observer**
- **Host**
- **Deployment**
- **GenericDomainFeature**

The Observation act relates:

- feature(s)-of-interest;
- observed property;
- observing procedure;
- observer(s);
- host(s);
- phenomenon time;
- result time;
- result;
- valid time;
- related observations.

### C. Observer / Host / Deployment structure

The 2023 model explicitly separates:

- **Observer**
  - identifiable entity that generates Observations by implementing an ObservingProcedure;
  - may be sensor, instrument, algorithm implementation, person, etc.

- **Host**
  - grouping/hosting context such as:
    - physical platform;
    - monitoring station;
    - observing campaign.

- **Deployment**
  - describes the hosting/attachment/assignment of Observer(s) to Host(s).

This replaces the older tendency to use SamplingFeature/Station as the host/instrument structure.

### D. ObservingCapability

ObservationCharacteristics can describe the common structure of related/similar Observations and the observing capability of facilities/observers before a specific Observation occurs.

### E. Sample conceptual structure

Primary concepts include:

- **Sample**
- **Sampling**
- **SamplingProcedure**
- **Sampler**
- **PreparationStep**
- **PreparationProcedure**
- **SampleCollection**

Sample has subtypes such as:

- SpatialSample;
- StatisticalSample;
- MaterialSample.

### F. Feature-of-interest structure

OMS explicitly distinguishes:

- **proximate feature-of-interest**
- **ultimate feature-of-interest**

and supports intermediate Samples/features within processing chains.

The source-native pattern is therefore:

> **observation act + procedure + observer/host/deployment + observable property + target feature + result + capability**, alongside a separate **sampling/sample/preparation chain**.

---

## 2. Purpose of each partition

### Observation

Purpose: represent an **act** carried out to determine the value of an ObservableProperty of a feature-of-interest by using an ObservingProcedure, with the value provided as the Result.

### ObservationCharacteristics

Purpose: factor common characteristics out of individual Observations so the same structure can describe:

- sets of similar Observations;
- observing capabilities;
- recurring observation patterns.

### ObservationCollection

Purpose: group similar/related Observations without making collection membership identical to the Observation itself.

### ObservingCapability

Purpose: describe potential/expected observing characteristics **before or independently of a particular Observation event**.

### ObservableProperty

Purpose: represent the property/phenomenon whose value is determined through Observation.

### ObservingProcedure

Purpose: represent the specified way/process used to determine the ObservableProperty.

### Observer

Purpose: identify the entity actually implementing the procedure and participating in creation of the Observation.

### Host

Purpose: identify the platform/station/campaign or other host grouping/context around observers and observations.

### Deployment

Purpose: describe the relationship/attachment of an Observer to a Host.

### Sample

Purpose: represent an object that stands in for a broader concept, real-world object or phenomenon.

### Sampling

Purpose: represent the act/event that creates/transforms a Sample.

### Sampler

Purpose: identify the device/entity/person implementing the SamplingProcedure.

### PreparationStep / Procedure

Purpose: describe processing/transformation of a Sample after sampling and before/among Observations.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Observation act | Observation, phenomenonTime, resultTime, validTime, relatedObservation |
| Common observation description | ObservationCharacteristics, ObservationCollection |
| Capability | ObservingCapability |
| Property | ObservableProperty |
| Method | Procedure, ObservingProcedure |
| Actor/source | Observer |
| Host/context | Host, Deployment |
| Target | proximateFeatureOfInterest, ultimateFeatureOfInterest, GenericDomainFeature |
| Result | result, resultQuality, metadata, parameter |
| Sample | Sample, SpatialSample, StatisticalSample, MaterialSample |
| Sampling act | Sampling, SamplingProcedure |
| Sampling actor | Sampler |
| Preparation | PreparationStep, PreparationProcedure |
| Sample grouping | SampleCollection, relatedSample |
| Processing chain | Sample → preparation → Observation → result / ultimate feature |

---

## 4. Primary relationships

### Observation → feature-of-interest

Observation is about one or more target entities/features.

The current model can distinguish:
- proximate feature directly participating in the act;
- ultimate feature ultimately of interest.

### Observation → ObservableProperty

Exactly one observed property is determined for an individual Observation in the basic/abstract model constraints.

### Observation → ObservingProcedure

Exactly one procedure is used for the Observation.

### Observation → Observer / Host

At least one Observer or Host should be provided.

Observer and Host are separate roles.

### Observer ↔ Host through Deployment

Deployment describes Observer-to-Host assignment/hosting/attachment.

### Observer → ObservingProcedure

Observer can advertise/support available ObservingProcedures.

### ObservingCapability → ObservationCharacteristics

Capability reuses/relaxes the same observation-characteristic structure to describe what can be observed/generated.

### Observation → result

Observation has exactly one Result, whose type must be suitable for the ObservableProperty.

### Sample → sampledFeature

Sample stands for one or more sampled features.

### Sampling → Sample / SamplingProcedure / Sampler

Sampling act creates/transforms Sample through a Procedure implemented by Sampler.

### Sample → PreparationStep

Sample can undergo one or more preparation/processing steps.

### Sample → related Observation

Observations can be organized/accessed through a Sample.

---

## 5. Dependency boundaries

OMS has unusually explicit semantic layering.

### Conceptual interface vs application-schema class

The conceptual interfaces define meaning independent of implementation inheritance/class design.

### Observation semantics vs Sample semantics

Observation and Sample are separate conceptual schemas with explicit associations between them.

### Observer vs Procedure

Who performs/implements the observing and how observation is performed are distinct.

### Observer vs Host

Observing entity and hosting/platform/campaign context are distinct.

### Deployment vs Observation

Hosting context is a relationship between Observer and Host, not the Observation event itself.

### ObservableProperty vs Result

Property meaning and observed value/result are separate.

### Feature-of-interest vs Result

Target entity/property carrier and value produced are separate.

### Sample vs ultimate sampled feature

Sample is an intermediate/proxy object, not automatically the ultimate real-world target.

### Capability vs event

ObservingCapability describes potential/characteristics; Observation describes an actual act.

---

## 6. Intrinsic vs contextual standing

OMS is event/process-centric rather than equipment-centric.

### Intrinsic to one Observation act

- observed property;
- procedure;
- result;
- phenomenon time;
- result time;
- feature-of-interest;
- observer/host participation;
- result quality/parameters/metadata where supplied.

### Intrinsic to Observer capability

- supported ObservingProcedure;
- potentially reusable ObservationCharacteristics/ObservingCapability.

### Contextual

- Host;
- Deployment;
- observation collection;
- campaign/station;
- ultimate feature beyond the proximate feature;
- metadata and related observations.

### Sampling context

Samples and Sampling acts may become contextual/intermediate objects in a processing chain rather than being part of the observing equipment itself.

---

## 7. Cross-cutting concepts

Cross-cutting OMS structures include:

- Procedure;
- time;
- metadata;
- parameters;
- quality;
- collections;
- related observations/samples;
- feature-of-interest;
- capability;
- deployment/hosting;
- processing chain.

The same conceptual interfaces can be realized by domain-specific application-schema classes.

---

## 8. State / temporal / lifecycle organization

OMS has rich **event time** semantics but does not define a generic equipment lifecycle.

### Observation time

Observation distinguishes:

- phenomenon time — when the property applies/is observed;
- result time — when the result becomes available;
- valid time — period over which the result/observation is valid.

### Sampling time

Sampling is itself an event/act with temporal context.

### Preparation chain

PreparationStep can introduce further processing stages between sampling and later observation.

### Deployment time

Deployment can describe time-bounded hosting/attachment context.

### Collections/related observations

Related observations can form temporal or processing sequences.

### Limit

Calibration/service/replacement/decommissioning are not organized as a universal equipment lifecycle in OMS itself.

---

## 9. Composition / topology organization

OMS's main topology is **process/participation topology**, not physical composition.

### Observer–Host topology

Observer can be deployed on/with Host through Deployment.

### Observation participation

Observation links:
- Observer;
- Host;
- Procedure;
- FeatureOfInterest;
- Result.

### Sample chain topology

Sample can link:
- sampled feature;
- Sampling;
- Sampler;
- preparation steps;
- related Samples;
- related Observations.

### Processing chain

OMS explicitly supports intermediate feature/sample chains where:
- ultimate target;
- sample;
- measured property;
- processing step;
- final interpreted property/result

are not collapsed.

### Important limit

Observer–Host deployment is not a physical BOM/component hierarchy for the instrument.

---

## 10. Capability / function / behavior organization

OMS has a dedicated **ObservingCapability** concept.

### ObservingCapability

Represents potential to create Observations with specified common characteristics.

It can capture combinations of:

- observable properties;
- observing procedures;
- observers;
- hosts;
- features/context;
- time/result characteristics.

### Procedure

ObservingProcedure represents how the observation is carried out.

### Observer

Observer implements/supports procedure(s).

### Sampling behavior

Sampler + SamplingProcedure define sample-creation/transformation behavior.

The source-native capability pattern is therefore:

> **Observer + supported Procedure + possible Observation characteristics**, separate from actual Observation events.

---

## 11. Information / output organization

OMS strongly separates information semantics.

### Observation

The act/event.

### Result

The value produced by that act.

### Result quality

Quality information about the result.

### ObservationCharacteristics

Reusable/common description of observation shape/context.

### ObservationCollection

Grouping of observations.

### Sample

Intermediate/proxy object that can organize related observations.

### Metadata/parameters

Ancillary context, not the observed value itself.

The source explicitly warns that some communities use “observation” to mean the result, but the model keeps **act and result distinct**.

---

## 12. Management / condition organization

OMS does not define a generic equipment-management domain.

Relevant management-adjacent structures include:

- ObservingCapability;
- Observer;
- Host;
- Deployment;
- procedures;
- result quality;
- metadata.

These can describe whether an Observer is capable of certain observations and how it is deployed, but OMS itself does not define:
- current equipment health;
- BIT;
- work orders;
- software update;
- maintenance state.

Those concerns require other models.

---

## 13. Provenance / identity / reference organization

OMS provides strong **observation provenance-by-participation**.

An Observation can identify:

- Observer(s);
- Host(s);
- Procedure;
- feature-of-interest;
- property;
- phenomenon time;
- result time;
- related Observation(s);
- metadata/parameters.

Samples can identify:

- sampled feature;
- Sampler;
- SamplingProcedure;
- Sampling event;
- preparation steps;
- related observations/samples.

This supports traceability of a result through:
- actor;
- procedure;
- target;
- time;
- sampling/preparation chain.

It is not a general provenance graph, but it is a rigorous domain-specific provenance structure.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Observation act vs Result** — the act/event and produced value are different.
2. **Observer vs ObservingProcedure** — who performs and how it is performed are different.
3. **Observer vs Host** — observing entity and hosting/platform/campaign context are different.
4. **Observer–Host relationship vs Deployment** — deployment describes the association; it is not either endpoint.
5. **ObservableProperty vs Result value** — property meaning and observed value are different.
6. **proximate vs ultimate FeatureOfInterest** — immediate observation target and ultimate scientific/operational target may differ.
7. **Observation vs ObservationCharacteristics** — actual act and reusable/common characteristics are different.
8. **Observation vs ObservingCapability** — actual occurrence and potential to produce such occurrences are different.
9. **Observation vs ObservationCollection** — item and grouping are different.
10. **Sample vs sampledFeature** — proxy/representative object and represented target are different.
11. **Sampling vs Sample** — creation/transformation act and resulting representative object are different.
12. **Sampler vs SamplingProcedure** — actor/device and method are different.
13. **Sampling vs PreparationStep** — initial sample creation and later processing are different.
14. **Sample vs Observer/Host** — samples should not be used to represent monitoring stations/instruments in the 2023 model.
15. **Host/station vs Sample** — monitoring facility belongs in Host, not Sample.
16. **result quality vs result** — value and quality/evaluation metadata differ.
17. **phenomenon time vs result time vs valid time** — three temporal meanings must remain distinct.
18. **conceptual interface vs concrete application-schema class** — semantic interface and one concrete realization are different.
19. **observation provenance vs general equipment lifecycle** — OMS traceability should not be mistaken for maintenance history.
20. **processing chain intermediate feature vs ultimate target** — intermediate sample/result semantics should not be flattened.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely cross-cutting observation structure:** Observer, Procedure, ObservableProperty, FeatureOfInterest, Result and time roles kept distinct;
- **likely capability pattern:** ObservingCapability separate from actual Observation;
- **likely contextual relationship pattern:** Host and Deployment separate from Observer;
- **likely provenance pattern:** observation source/procedure/target/time and sampling/preparation chains;
- **likely target-model pattern:** proximate vs ultimate FeatureOfInterest;
- **likely information/output pattern:** act vs result vs quality vs collection;
- **likely sampling specialization:** Sample/Sampling/Sampler/Preparation should remain separate from equipment identity;
- **profile-gap signal:** equipment condition, maintenance and whole-device management are intentionally outside OMS;
- **binding/ontology caution:** OMS conceptual interfaces and application-schema classes are domain-model constructs; V2 should reuse distinctions without assuming the entire OMS class package becomes a V2 module.

**No V2 module disposition is made in Phase A.**

---

**X08 status: COMPLETE.**

**Next frozen lineage:** X09 — OMA Lightweight M2M.

---

# X09 — OMA Lightweight M2M (LwM2M) 1.2.2

## Source basis and evidence ceiling

**Frozen primary source ID:** 129.

**Primary inspected source:**

- Open Mobile Alliance, *Lightweight Machine to Machine Technical Specification: Core*, Approved Version 1.2.2, 13 June 2024, OMA-TS-LightweightM2M_Core-V1_2_2-20240613-A.

**Evidence note:** The exact frozen 1.2.2 specification was inspected from the official OMA publication. The mutable OMNA Object Registry contains later Object versions; those later registry revisions are not silently substituted for the exact Object versions embedded in Core 1.2.2. Where the Core itself uses an Object version newer than the Device Object, that version is recorded source-natively.

---

## 1. Source-native structural organization

LwM2M organizes device management around a **Client resource model plus four principal interfaces**.

### A. Principal actors

1. **LwM2M Client**
   - runs on/for the managed device side;
   - exposes Objects/Object Instances/Resources.

2. **LwM2M Server**
   - manages/monitors Clients through standardized interfaces.

3. **LwM2M Bootstrap-Server**
   - provisions initial/security/server/bootstrap information.

4. **LwM2M Gateway**
   - optional structure for exposing devices connected behind a gateway.

### B. Resource model

The native model is:

- **LwM2M Client**
  - **Object**
    - **Object Instance**
      - **Resource**
        - optionally **Resource Instance**

Each Resource:

- has an identifier unique within its Object;
- has a datatype;
- may be readable, writable and/or executable;
- may be mandatory or optional.

Objects define groups of Resources; Object Instances instantiate a subset of those Resources.

### C. Interface partitions

1. **Bootstrap Interface**
2. **Client Registration Interface**
3. **Device Management and Service Enablement Interface**
4. **Information Reporting Interface**

### D. Standard Object partitions

The Core defines standard Objects including:

- LwM2M Security;
- LwM2M Server;
- Access Control;
- Device;
- Connectivity Monitoring;
- Firmware Update;
- Location;
- Connectivity Statistics;
- security/OSCORE/COSE;
- MQTT Server;
- LwM2M Gateway;
- Gateway Routing;
- 5G NR Connectivity.

### E. Operation partitions

Device-management operations include:

- Read;
- Discover;
- Write;
- Write-Attributes;
- Execute;
- Create;
- Delete;
- Read-Composite;
- Write-Composite.

Information-reporting operations include:

- Observe;
- Notify;
- Cancel Observation;
- Observe-Composite;
- Send.

The source-native anatomy is therefore:

> **Client-managed object space + Object/Instance/Resource hierarchy + management interfaces + reporting operations + dedicated management/configuration Objects**.

---

## 2. Purpose of each partition

### LwM2M Client

Purpose: provide the managed endpoint/client boundary exposing standardized and extensible Objects to Servers.

### Object

Purpose: define a reusable **grouping/schema of Resources** for one management/service concern.

### Object Instance

Purpose: instantiate an Object for one concrete managed occurrence/context.

### Resource

Purpose: represent one typed piece of information or executable action.

### Resource Instance

Purpose: represent one member/value of a multi-instance Resource.

### Bootstrap Interface

Purpose: provision initial security/server configuration and establish a usable Client configuration.

### Registration Interface

Purpose: announce Client presence, endpoint identity, registration lifetime, binding mode and supported Objects/Object Instances.

### Device Management / Service Enablement

Purpose: allow authorized Server management of Object Instances/Resources and invocation of executable functions.

### Information Reporting

Purpose: allow Server-controlled or Client-initiated reporting of Resource values via Observe/Notify/Send.

### Access Control

Purpose: associate Server-specific permissions with Objects/Object Instances and their operations.

### Device Object

Purpose: expose generic whole-device identity, firmware, reboot/reset, power-source/battery/memory/error/time information.

### Connectivity / Location / Firmware Update Objects

Purpose: keep network state, spatial telemetry and software-update lifecycle separate from generic Device identity.

### Gateway / Routing Objects

Purpose: expose downstream devices and route/mapping their Objects through a gateway without pretending they are native Client Objects of the gateway itself.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Managed endpoint | LwM2M Client, Endpoint Client Name |
| Management authority | LwM2M Server, Short Server ID |
| Provisioning | Bootstrap-Server, bootstrap information |
| Information model | Object, Object Instance, Resource, Resource Instance |
| Operations | Read, Write, Execute, Create, Delete, Discover, Composite operations |
| Reporting | Observe, Notify, Send, observation attributes |
| Access | Access Control Object, ACL, Access Control Owner |
| Device identity/state | Manufacturer, Model Number, Serial Number, Firmware Version, errors, time, memory |
| Power | Available Power Sources, Voltage, Current, Battery Level, Battery Status |
| Connectivity | bearer, signal strength, cell/network data |
| Software lifecycle | Firmware Update Object, State, Update Result, package/URI |
| Location | latitude, longitude, altitude, radius, timestamp/velocity where defined |
| Gateway | connected Device ID, Prefix, routing mapping |
| Registration | Objects/Object Instances, lifetime, binding mode, Profile ID |

---

## 4. Primary relationships

### Client → Object → Object Instance → Resource

The resource model is a logical management hierarchy.

### Registration → supported Objects/Object Instances

Client registration announces the Object/Object Instance set currently available to a Server.

### Object Instance → Access Control Object Instance

Access Control can point to a target Object/Object Instance and assign Server-specific rights.

### Server → operations → Resources/Object Instances

Server invokes management operations according to access rights and each Resource's defined operations.

### Server → Observe → Client Notify

Observation/reporting creates a subscription-like relationship over Resources/Object Instances.

### Client → Send → Server

Client may proactively report selected Resource values.

### Device Object → external device info

`ExtDevInfo` can reference an external Device Object instance, e.g. a Host Device into which the LwM2M Client's device is embedded.

### Gateway → connected device

Gateway Object identifies downstream Device ID and a Prefix used to access that device's Objects.

### Firmware Update → state/result

Firmware Update State Machine separates update state from update-result/error and transport/package location.

---

## 5. Dependency boundaries

### Client identity vs Device Object

LwM2M Client is the protocol/management endpoint; Device Object contains generic device information. These are related but not identical concepts.

### Object definition vs Object Instance

Object is schema/grouping; Object Instance is one realization.

### Resource definition vs Resource value

Resource semantics/operations/datatype and current instantiated value are separate.

### Resource model vs physical topology

Object/Instance/Resource nesting is a management-information hierarchy, not a physical BOM.

### Registration vs management state

Registration says what is exposed/available to a Server; it does not constitute the complete device configuration or physical identity.

### Observe/Notify vs Resource state

Information-reporting mechanics are separate from the value/state being reported.

### Device Object vs specialized Objects

Connectivity, Location, Firmware Update and Access Control remain separate concerns rather than being flattened into one generic Device property bag.

### Gateway vs downstream device

Gateway mediates access to connected devices while preserving separate downstream Device IDs/prefixes.

---

## 6. Intrinsic vs contextual standing

### Intrinsic/device-oriented

- manufacturer/model/serial;
- firmware version;
- power-source information;
- memory;
- supported Objects;
- reboot/reset capability;
- internal battery state where applicable.

### Management/runtime

- registration lifetime;
- Server relationships;
- access-control rights;
- observed Resources;
- firmware-update state;
- current connectivity;
- current location;
- error codes.

### Contextual/network

- bearer/network identity;
- Server/bootstrap relationships;
- registration binding;
- gateway/routing context.

### External-host relationship

Device Object may point to external/Host Device information, showing that the LwM2M endpoint's device and a containing/host device can remain distinct.

---

## 7. Cross-cutting concepts

Cross-cutting LwM2M structures include:

- identifiers/URIs;
- Object version;
- mandatory/optional;
- access operations;
- attributes;
- access control;
- Server authorization;
- serialization formats;
- observation/reporting;
- bootstrap/configuration;
- version compatibility.

Every Object/Resource participates in common operation, identity and access semantics.

---

## 8. State / temporal / lifecycle organization

LwM2M defines several distinct management lifecycles.

### Registration lifecycle

- Register;
- Update;
- De-register;
- lifetime/expiry;
- re-registration after reset/state loss.

### Bootstrap lifecycle

- factory/bootstrap configuration;
- client/server-initiated bootstrap;
- bootstrap finish.

### Firmware lifecycle

Firmware Update has an explicit state machine with:
- package acquisition;
- downloading;
- downloaded;
- updating;
- idle;
- Update Result/error reporting.

### Observation lifecycle

Observe establishes reporting; Notify reports changes; Cancel Observation terminates it.

### Device reset lifecycle

Factory Reset causes re-entry into deployment/bootstrap sequence.

### Limit

This is management/protocol/software lifecycle, not full physical asset service/maintenance history.

---

## 9. Composition / topology organization

LwM2M's principal topology is **management namespace topology**.

### Object hierarchy

Client/Object/Object Instance/Resource hierarchy organizes management information.

### Gateway topology

Gateway Object and Gateway Routing map connected downstream devices/Objects through:
- Device ID;
- prefix;
- Object routing entries.

### Host relationship

Device Object can link to an external Host Device Object instance.

### Important limit

Neither Object nesting nor URI path means physical containment.

An Object can represent:
- firmware update;
- connectivity;
- location;
- access control;
- device identity

without being a physical component.

---

## 10. Capability / function / behavior organization

LwM2M expresses capability through **Resource operation definitions** and instantiated Objects.

### Resource operations

Resources can support:
- Read;
- Write;
- Execute.

### Object support

Registration advertises which Objects/Object Instances are implemented.

### Executable Resources

Actions such as:
- Reboot;
- Factory Reset;
- Firmware Update

are modeled as executable Resources rather than ordinary values.

### Management capability

Read/Write/Create/Delete/Observe availability is constrained by:
- Object definition;
- Resource definition;
- access control;
- current instantiation.

The source-native capability pattern is therefore **implemented Object/Resource + supported operations + authorization**, not a generic domain Capability class.

---

## 11. Information / output organization

### Resource values

Current/persistent information is exposed through Resource values.

### Executable actions

Executable Resources represent behavior, not data values.

### Reporting

Observe/Notify and Send report Resource values over time.

### Composite reporting

Composite operations can read/write/observe heterogeneous Resources across Objects.

### Specialized Objects

Information is separated into coherent management domains:
- Device;
- connectivity;
- location;
- software update;
- statistics;
- security.

### Data serialization

SenML JSON/CBOR, TLV and LwM2M CBOR are transport/encoding choices for Resource values, not separate domain information types.

---

## 12. Management / condition organization

Management is the central purpose of LwM2M.

### Device management

- read/write settings;
- execute actions;
- create/delete instances;
- discover resource model.

### Monitoring

- observe/notify;
- connectivity monitoring/statistics;
- error state;
- power/battery state;
- location.

### Software management

- firmware update state machine;
- update result/error;
- update package/pull/push behavior.

### Security/access

- Security Object;
- Access Control;
- OSCORE/COSE;
- Server authorization.

### Provisioning

Bootstrap and Registration establish manageable operational state.

The model therefore supplies a strong management anatomy, but it is intentionally generic and not sensing-specific.

---

## 13. Provenance / identity / reference organization

### Endpoint identity

Endpoint Client Name identifies a Client for registration.

### Server identity

Short Server ID identifies management authorities and ACL entries.

### Object identity

Object ID + version identify information model definitions.

### Object-instance identity

Object Instance ID identifies one instance.

### Resource identity

Resource ID identifies one property/action within Object scope.

### Object Link

Objlnk references other Object Instances.

### Gateway identity

Gateway Device ID/prefix preserve identity of downstream devices.

### Product identity

Device Object supplies manufacturer/model/serial separately from Client endpoint/protocol identity.

Thus **protocol endpoint, product device, Object, Object Instance and Resource each have different identity scopes**.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **LwM2M Client vs physical Device** — protocol endpoint and real-world product are related but not necessarily identical.
2. **Object vs Object Instance** — schema/grouping and concrete instance are different.
3. **Resource vs Resource Instance** — property/action type and one multi-instance member are different.
4. **Object hierarchy vs physical composition** — management namespace is not a BOM.
5. **Resource value vs Execute Resource** — data/state and action are different.
6. **Registration vs persistent device identity** — protocol participation and product identity differ.
7. **Bootstrap vs Registration** — provisioning and ongoing server participation are distinct.
8. **Device Object vs Connectivity/Location/Firmware Objects** — generic identity/device info and specialist management concerns are intentionally partitioned.
9. **Observe vs Notify** — subscription/request and reporting event are different.
10. **Observe/Notify vs Resource state** — reporting mechanism and underlying value differ.
11. **Access Control Object vs target Object Instance** — authorization metadata and protected subject are separate.
12. **Firmware update State vs Update Result** — process phase and outcome/error are different.
13. **current firmware version vs firmware-update process** — installed identity and transition process differ.
14. **Gateway vs connected device** — mediator and downstream device remain distinct.
15. **Gateway routing mapping vs device composition** — namespace routing does not imply physical containment.
16. **Host Device link vs Client's Device** — embedded device and containing host can be separate.
17. **Object version vs LwM2M protocol version** — information-model edition and protocol edition are different.
18. **Read/Write/Execute permission vs domain capability** — management access operation is not the same as equipment mission function.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely reusable management pattern:** description/state/action represented as typed Objects/Resources with explicit operations;
- **likely cross-cutting:** bootstrap, registration, access control, observation/reporting and software update;
- **likely identity pattern:** protocol endpoint vs durable product identity vs Object/Resource identifiers;
- **likely dynamic-information pattern:** Observe/Notify/Send separated from underlying Resource semantics;
- **likely management lifecycle pattern:** bootstrap, registration and firmware-update state machines;
- **likely contextual pattern:** connectivity and location as separate Objects rather than intrinsic physical composition;
- **likely mediation pattern:** Gateway preserves downstream device identity while routing management namespace;
- **profile-gap signal:** LwM2M provides generic device management but not a sensing-system domain model, observation semantics or physical BOM;
- **binding caution:** Object/Instance/Resource URI hierarchy and CRUD/Execute operations are LwM2M management mechanisms and are not automatically V2 modules/classes.

**No V2 module disposition is made in Phase A.**

---

**X09 status: COMPLETE.**

**Next frozen lineage:** X10 — W3C PROV.

---

# X10 — W3C PROV

## Source basis and evidence ceiling

**Frozen primary source IDs:** 159, 160.

**Primary inspected sources:**

- W3C, *PROV-DM: The PROV Data Model*, Recommendation, 30 April 2013.
- W3C, *PROV-O: The PROV Ontology*, Recommendation, 30 April 2013.

**Evidence note:** PROV-DM is the conceptual provenance model; PROV-O is its OWL2 encoding. They form one semantic lineage and are not counted independently. Other PROV-family documents are acknowledged by the standards but are not part of the frozen primary lineage unless needed to explain a concept already present in PROV-DM/O.

---

## 1. Source-native structural organization

PROV-DM is explicitly organized into six components.

### Component 1 — Entities and Activities

Core concepts:

- **Entity**
- **Activity**
- Generation
- Usage
- Communication
- Start
- End
- Invalidation

### Component 2 — Derivations

- Derivation
- Revision
- Quotation
- Primary Source

### Component 3 — Agents, Responsibility and Influence

- **Agent**
- Attribution
- Association
- Delegation
- Influence

### Component 4 — Bundles

- **Bundle**
- provenance of provenance.

### Component 5 — Alternate Entities

- Specialization
- Alternate

### Component 6 — Collections

- **Collection**
- Membership

PROV-O encodes the same structure as OWL classes/properties and distinguishes:

- starting-point terms;
- expanded terms;
- qualified terms.

The source-native pattern is therefore:

> **Entity / Activity / Agent as the core provenance triad, connected through generation/use/derivation/responsibility/influence, with bundles, specialization/alternate relations and collections as extended structures**.

---

## 2. Purpose of each partition

### Entity

Purpose: represent a physical, digital, conceptual or other thing with some fixed aspects relevant to a provenance account.

### Activity

Purpose: represent something that occurs over a period of time and acts upon/with Entities, including generation, transformation, use or invalidation.

### Agent

Purpose: represent something bearing responsibility for Activity occurrence or Entity existence.

### Generation

Purpose: identify when/how an Entity becomes available/existent as a result of an Activity.

### Usage

Purpose: identify an Activity's use of an Entity.

### Derivation

Purpose: state that one Entity is derived from another through some process/activity.

### Attribution

Purpose: assign responsibility for an Entity to an Agent.

### Association

Purpose: associate an Agent with an Activity, optionally according to a plan/role.

### Delegation

Purpose: represent one Agent acting on behalf of another.

### Bundle

Purpose: package a named set of provenance descriptions so provenance statements themselves can have provenance.

### Specialization / Alternate

Purpose: relate different provenance views/descriptions of the same underlying thing without claiming identity.

### Collection

Purpose: represent an Entity with members and preserve membership semantics.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Core things | Entity, Activity, Agent |
| Entity lifecycle | Generation, Invalidation |
| Activity interaction | Usage, Start, End, Communication |
| Lineage | Derivation, Revision, Quotation, PrimarySource |
| Responsibility | Attribution, Association, Delegation, Influence |
| Provenance packaging | Bundle |
| Multiple descriptions | Specialization, Alternate |
| Grouping | Collection, Membership |
| Qualifiers | role, location, time, plan, value, type, label |
| Qualified relations | qualifiedGeneration, qualifiedUsage, qualifiedAssociation, qualifiedDerivation, etc. |

---

## 4. Primary relationships

### Activity → Entity

- Activity **uses** Entity.
- Activity **generates** Entity.
- Activity can invalidate Entity.

### Entity → Entity

- Entity may be **derived from** another Entity.
- Entity can be a **revision of**, **quotation of**, or use a **primary source**.

### Agent → Entity

- Entity can be **attributed to** Agent.

### Agent → Activity

- Activity can be **associated with** Agent.

### Agent → Agent

- one Agent can **act on behalf of** another.

### Activity → Activity

- Communication links one Activity's generated Entity/use context to another Activity.

### Entity ↔ specialization/alternate

- multiple Entities can describe specialized states/views of the same underlying thing.
- Alternate relates Entities that are aspects/versions of the same underlying thing.

### Collection → Entity

- Collection has members, while Collection remains an Entity itself.

### Bundle → provenance statements

- Bundle packages provenance descriptions and is itself an Entity capable of participating in further provenance.

---

## 5. Dependency boundaries

PROV intentionally separates **domain semantics from provenance semantics**.

### Domain object vs provenance Entity

A sensor, document, observation, configuration or software artifact can be represented as a PROV Entity, but PROV does not define its domain-internal structure.

### Action vs Activity

Domain events/actions may be represented as Activities, but PROV Activity semantics are provenance-oriented and do not define the complete domain event taxonomy.

### Responsibility vs identity

Agent/association/attribution describe responsibility and influence; they do not redefine the domain identity of the Entity.

### Derivation vs ordinary relationship

Derivation is specifically about one Entity depending on another through transformation/use; it is not a generic association.

### Bundle vs Collection

Bundle packages provenance assertions; Collection groups Entity members. These are different structures.

### PROV-DM vs PROV-O

Conceptual model and OWL encoding are distinct specification layers.

---

## 6. Intrinsic vs contextual standing

PROV is inherently **cross-cutting/contextual**.

It does not determine which equipment information is intrinsic. Instead, it describes provenance relationships around:

- equipment descriptions;
- observations;
- files/products;
- configurations;
- software;
- assessments;
- commands/results;
- events.

### Potentially intrinsic provenance facts

For a particular information item:
- who/what generated it;
- what it used;
- when it was generated;
- what it derived from.

### Contextual responsibility

- responsible Agent;
- role;
- plan;
- delegation;
- organization/person/software Agent.

PROV therefore attaches historical/source context to domain information without replacing that domain model.

---

## 7. Cross-cutting concepts

Cross-cutting PROV concepts include:

- identifier;
- type;
- label;
- value;
- role;
- location;
- time;
- plan;
- influence;
- responsibility;
- qualification of relations;
- specialization/alternate views.

The qualification pattern allows a simple relation to be expanded when additional provenance attributes are needed.

---

## 8. State / temporal / lifecycle organization

PROV has strong event/time semantics but models **provenance state transitions**, not equipment lifecycle as such.

### Entity lifecycle markers

- Generation
- Invalidation

### Activity temporal boundaries

- Start
- End

### Usage/generation times

Qualified relations can carry time.

### Entity versions/views

- Revision;
- Specialization;
- Alternate.

### Provenance history

Chains of generation/use/derivation can represent how information evolves through successive Activities.

### Limit

PROV does not prescribe procurement/commissioning/maintenance phases; those must be supplied by the domain model and can then be linked with provenance.

---

## 9. Composition / topology organization

PROV does not define physical equipment composition.

### Provenance graph topology

Its topology is instead a directed semantic graph among:

- Entities;
- Activities;
- Agents.

### Collections

Collection/Membership organizes Entity membership.

### Bundles

Bundles group provenance assertions.

### Specialization

Specialization can model more specific states/views of one underlying thing.

### Important limit

Collection membership and Bundle containment are **not physical-part relationships**.

---

## 10. Capability / function / behavior organization

PROV does not define capability/function taxonomy.

Behavior appears through **Activity**:

- an Activity happens;
- uses Entities;
- generates/invalidates Entities;
- associates with Agents;
- may follow a Plan.

A device capability should therefore come from another donor; PROV can describe provenance of:
- its declaration;
- its configuration;
- an execution;
- a result.

---

## 11. Information / output organization

PROV is especially relevant to information lineage.

### Entity as information/product

An Entity can represent:
- observation result;
- document;
- file;
- configuration;
- model;
- data product;
- software version.

### Activity as production/processing

Activity can represent:
- sensing/collection;
- processing;
- transformation;
- fusion;
- calibration;
- assessment;
- publication.

### Derivation

Explicitly relates output Entity to source/input Entity.

### Qualified relations

Can record:
- role;
- time;
- plan;
- responsible Agent;
- generation/use details.

Thus PROV provides a generic **information lineage/output-production graph**, not a specific observation schema.

---

## 12. Management / condition organization

PROV has no generic equipment-management or health model.

It can record provenance of management/condition information such as:

- configuration changed by an Activity;
- software update generated a new software Entity;
- maintenance Activity used parts and generated a revised equipment-state description;
- health assessment Activity used observations and generated an assessment.

But terms such as fault, readiness, repair, calibration state or work order must come from domain sources.

---

## 13. Provenance / identity / reference organization

This is the lineage's core strength.

### Identity

Each Entity/Activity/Agent may have a qualified name/identifier.

### Responsibility

- Attribution;
- Association;
- Delegation.

### Lineage

- Generation;
- Usage;
- Derivation;
- Revision;
- Quotation;
- PrimarySource.

### Multiple views

- specializationOf;
- alternateOf.

### Provenance of provenance

Bundles can themselves be described as Entities.

### Qualified relations

Simple binary relations can be expanded into qualification nodes carrying:
- role;
- time;
- plan;
- additional attributes.

This supports traceability without forcing all provenance detail into the source Entity itself.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Entity vs Activity** — thing/state and process/event are different.
2. **Entity vs Agent** — thing and responsible actor are different, even though an Agent can also be an Entity.
3. **Activity vs Agent** — what happened and who/what was responsible differ.
4. **Generation vs Usage** — producing an Entity and consuming an Entity are distinct.
5. **Generation vs Derivation** — event of creation and lineage dependency are different.
6. **Derivation vs Revision** — general dependency and revision-specific relation differ.
7. **Attribution vs Association** — responsibility for Entity and participation in Activity differ.
8. **Association vs Delegation** — Agent participation and acting-on-behalf-of relationships differ.
9. **Bundle vs Collection** — provenance package and member grouping are different.
10. **Collection membership vs physical composition** — provenance grouping is not BOM structure.
11. **Specialization vs identity** — specialized provenance views should not be treated as identical records.
12. **Alternate vs derivation** — alternate descriptions and produced-from relationships differ.
13. **domain Entity vs domain class semantics** — calling something a PROV Entity does not define whether it is a Sensor, Observation or Component.
14. **provenance Activity vs domain lifecycle stage** — provenance process semantics do not define the domain's maintenance lifecycle.
15. **simple relation vs qualified relation** — additional role/time/context cannot always be collapsed into a binary link.
16. **provenance graph vs current state model** — lineage/history does not replace present equipment state.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely cross-cutting provenance pattern:** Entity/Activity/Agent with generation, use and derivation;
- **likely responsibility pattern:** attribution, association, delegation and roles;
- **likely information-lineage pattern:** derived/revised data products and assessments retain source/process relationships;
- **likely version/view pattern:** specialization/alternate distinctions for different descriptions of the same underlying thing;
- **likely packaging pattern:** Bundle for provenance-of-provenance, Collection for member grouping;
- **likely event/history support:** generation/invalidation/start/end/time relationships can enrich lifecycle events without defining them;
- **profile-gap signal:** PROV intentionally lacks equipment identity, capability, health, composition and observation-domain semantics;
- **ontology/binding caution:** PROV-O is one RDF/OWL realization of PROV-DM; V2 should preserve provenance semantics without assuming every domain resource must be natively expressed as a PROV graph.

**No V2 module disposition is made in Phase A.**

---

**X10 status: COMPLETE.**

**Next frozen lineage:** X11 — W3C Web of Things.

---

# X11 — W3C Web of Things Architecture 1.1

## Source basis and evidence ceiling

**Frozen primary source ID:** 132.

**Primary inspected source:**

- W3C, *Web of Things (WoT) Architecture 1.1*, Recommendation, 5 December 2023.

**Evidence note:** This source is an abstract architecture. It defines core concepts and relations among WoT building blocks but does not prescribe one concrete deployment, protocol, or implementation. The anatomy extraction therefore distinguishes abstract WoT semantics from protocol bindings, Thing Description serialization, Scripting API/runtime implementation, and example deployments.

---

## 1. Source-native structural organization

WoT organizes its architecture around several interacting layers.

### A. Thing abstraction

- **Thing / Web Thing**
  - abstraction of a physical or virtual entity;
  - must have at least one Thing Description representation available.

- **Device**
  - physical entity with a network interface;
  - a kind of Thing.

- **Service**
  - software entity with a network interface;
  - a kind of Thing.

- **Virtual Thing**
  - Service that represents, augments, provides an improved interface to, or stands in place of one or more other Things;
  - includes Shadows and Digital Twins.

### B. Metadata/model layer

1. **Thing Description (TD)**
   - instance-specific metadata for one Thing.

2. **Thing Model (TM)**
   - class/template-level common metadata and capabilities for groups of Things;
   - omits instance-specific details such as concrete protocol address, serial number or location.

3. **Links**
   - relate Things, Thing Models and other Web resources.

### C. Interaction model

Interaction Affordances are separated into:

- **Property**
  - exposes Thing state;
- **Action**
  - invokes function/process;
- **Event**
  - asynchronously communicates state transitions/event data.

### D. Web/interface layer

- WoT Interface
- Hypermedia Controls
- Forms
- Protocol Bindings
- Media Types

### E. Security layer

- public security metadata;
- private security data;
- security configuration.

### F. Runtime/role layer

- **Servient**
- **Exposed Thing**
- **Consumed Thing**
- **Consumer**
- **Intermediary**

### G. Discovery layer

- Thing Description Directory;
- discovery/introduction/exploration.

### H. Lifecycle layer

- system lifecycle;
- Thing lifecycle;
- bootstrapping;
- onboarding/registration;
- activation;
- operation;
- offboarding;
- decommissioning.

The source-native anatomy is therefore:

> **Thing abstraction + class/instance metadata + Properties/Actions/Events + Web/protocol exposure + security + runtime roles/intermediaries + discovery + lifecycle**.

---

## 2. Purpose of each partition

### Thing

Purpose: provide a protocol-neutral abstraction of a physical or virtual entity that can be described and interacted with through WoT metadata.

### Thing Description

Purpose: describe one Thing instance, including:
- general metadata;
- domain-specific annotations;
- Interaction Affordances;
- public security metadata;
- communication/protocol metadata;
- related links.

### Thing Model

Purpose: describe common capabilities/interface structure for a class of Things without requiring instance-specific deployment/identity/communication details.

### Property

Purpose: expose readable, optionally writable/observable Thing state.

### Action

Purpose: expose an invocable Thing function/process, potentially affecting one or multiple states over time.

### Event

Purpose: expose an asynchronous event source/state-transition notification.

### Protocol Binding

Purpose: map abstract affordances to concrete messages/protocols/data formats.

### Servient

Purpose: provide runtime stack capable of exposing and/or consuming Things.

### Exposed Thing

Purpose: software representation of a Thing's exposed network interface.

### Consumed Thing

Purpose: local software abstraction representing a remote Thing to a Consumer.

### Intermediary

Purpose: proxy/bridge/augment/compose Things and possibly transform protocols/security/metadata.

### Discovery/Directory

Purpose: distribute, register and retrieve Thing Descriptions.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Entity abstraction | Thing, Device, Service, Virtual Thing, Digital Twin, Shadow |
| Instance metadata | Thing Description, general metadata, domain metadata, links |
| Class/template metadata | Thing Model |
| Interaction | Interaction Affordance, Property, Action, Event |
| Data description | Data Schema |
| Hypermedia | Links, Forms |
| Protocol realization | Protocol Binding, media type, URI |
| Security | Public Security Metadata, Private Security Data, Security Configuration |
| Runtime | Servient, WoT Runtime, Exposed Thing, Consumed Thing |
| Roles | Consumer, Intermediary |
| Discovery | Thing Description Directory, Discoverer, introduction/exploration |
| Lifecycle | bootstrap, onboard/register, activate, operate, offboard, decommission |

---

## 4. Primary relationships

### Thing → Thing Description

A Thing instance is described by at least one TD.

### Thing class → Thing Model

TM describes common capabilities of a set/class of Things and acts as a template for TD instances.

### Thing → Affordances

Thing exposes:
- Properties;
- Actions;
- Events.

### Affordance → Protocol Binding

Abstract interaction is mapped through Forms/Bindings to concrete protocol messages.

### Thing → links

TD/TM can link to:
- other Things;
- sub-Things;
- Thing Models;
- documentation;
- external Web resources.

### Servient → Exposed Thing / Consumed Thing

A Servient can:
- expose a local Thing;
- consume a remote Thing;
- do both as an Intermediary.

### Intermediary → original Thing / Consumer

Intermediary consumes one Thing and exposes another interface outward, potentially:
- proxying;
- augmenting;
- translating;
- composing.

### Virtual Thing → one or more Things

Virtual Thing can represent/aggregate/augment multiple Things.

### Consumer → TD → Consumed Thing

Consumer gets a TD through discovery and creates a local consumed abstraction.

---

## 5. Dependency boundaries

### Thing vs TD

The Thing/entity and its metadata representation are different.

### Thing vs Exposed Thing

Domain abstraction and runtime software representation are different.

### Thing vs Device

Thing can be physical or virtual; Device is specifically physical/networked.

### Thing vs Service

Physical Device and software Service are sibling Thing realizations.

### TD vs TM

Instance description and reusable class/template model are different.

### Affordance vs Protocol Binding

Abstract behavior/state/event semantics are independent of concrete protocol mechanics.

### Thing behavior vs affordance

Autonomous internal behavior and consumer-accessible Interaction Affordances are separate architectural aspects.

### Consumer vs Thing

Client/consumer role and server/exposed-thing role are distinct.

### Intermediary vs original Thing

Proxy/digital-twin/bridge identity can differ from the underlying Thing.

### Domain vocabulary vs WoT core vocabulary

WoT deliberately allows domain-specific vocabularies (e.g. external ontologies) instead of defining all domain semantics itself.

---

## 6. Intrinsic vs contextual standing

### Intrinsic to Thing description

Potentially:
- Thing ID/name;
- affordances;
- data schemas;
- semantic types;
- security schemes;
- links;
- common metadata.

### Class/model level

Thing Model captures common/shared capabilities without instance data.

### Deployment/contextual

- concrete protocol addresses;
- network location;
- concrete bindings;
- discovery directory;
- intermediary/proxy;
- current security credentials/private security data.

### Virtualization context

A Virtual Thing may add:
- history;
- predictive behavior;
- higher-level operations;
- merged capabilities.

Those additions are not automatically intrinsic to the underlying physical Device.

---

## 7. Cross-cutting concepts

Cross-cutting WoT concepts include:

- semantic annotations/Linked Data;
- links;
- data schemas;
- security;
- protocol bindings;
- discovery;
- profiles;
- metadata;
- lifecycle;
- identity;
- internationalization.

Security is explicitly cross-cutting and split between public metadata and private data.

---

## 8. State / temporal / lifecycle organization

WoT distinguishes **Thing/system lifecycle** from Property/Event state.

### System lifecycle

Typical sequence includes:
- bootstrap;
- onboarding/registration;
- activation/provision/configure;
- regular operation;
- offboarding;
- decommissioning/destruction.

### Thing lifecycle

Thing-specific provisioning/discovery/metadata availability can evolve over deployment.

### Runtime state

Property exposes current Thing state.

### State transition

Event communicates state transitions asynchronously.

### Action

Action can trigger a process whose effect unfolds over time.

### Digital Twin history/prediction

Virtual Thing/Digital Twin may maintain historical or predictive state beyond the physical Thing's direct interface.

---

## 9. Composition / topology organization

WoT supports several kinds of composition but does not define a physical BOM.

### Virtual composition

A Virtual Thing can compose one or more Things and expose:
- merged capabilities;
- higher-level functions;
- consolidated TD.

### Hierarchical sub-Things

Complex Thing TD can link to sub-Things.

### Link topology

Things and TMs form a navigable Web through typed links.

### Deployment topology

Things, Consumers, Intermediaries and directories can interact directly or through proxy/cloud/gateway topologies.

### Runtime topology

Exposed/Consumed Thing abstractions exist inside Servients.

### Important limit

Thing composition/hierarchy can be logical/virtual/service-based and must not be assumed to equal physical equipment composition.

---

## 10. Capability / function / behavior organization

WoT's capability model is interaction-oriented.

### Thing Model

Defines common interface/capabilities of a class of Things.

### Property

Capability to expose/update/observe state.

### Action

Capability to invoke functionality.

### Event

Capability to emit asynchronous event information.

### Behavior

Thing can also have autonomous internal behavior not directly represented as an Affordance.

### Intermediary augmentation

An Intermediary/Virtual Thing can add capabilities that did not exist in the underlying Thing.

Thus **exposed capability and intrinsic device capability are not necessarily identical**.

---

## 11. Information / output organization

### Thing Description

Persistent/self-descriptive metadata.

### Property

Current/readable/writable/observable state.

### Event

Asynchronous event/state-transition data.

### Action input/output

Action may have input/output schemas and invocation semantics.

### Data Schema

Defines payload information structure used across interactions.

### TD links

Point to supporting/related resources and other Things.

### Digital Twin/Shadow

May maintain cached, historical or predicted state distinct from direct physical-device output.

The architecture therefore distinguishes **description, state, event, action interaction and protocol payload structure**.

---

## 12. Management / condition organization

WoT is not a device-management standard in the same sense as LwM2M, but provides relevant architecture.

### Lifecycle

Bootstrap/onboard/activate/offboard/decommission.

### Discovery

Register/discover TDs.

### Security

Public security metadata + private credentials/configuration.

### Protocol/interface management

Bindings/forms describe how to interact.

### Digital Twin/Shadow

Can cache/mediate state and support synchronization.

### Limit

Fault/health, maintenance work, firmware/update, asset lifecycle and detailed condition semantics are not universal WoT Core concepts and must come from domain vocabularies or other protocols.

---

## 13. Provenance / identity / reference organization

### Thing identity

TD can have Thing identifier.

### Model identity

TM identifies shared class/template semantics separately from instance.

### Link relationships

Links explicitly connect:
- Things;
- Thing Models;
- documents;
- other resources.

### Proxy identity

An Intermediary-generated TD may use:
- same identifier as original Thing; or
- new identifier.

This is a deliberate source-native ambiguity/choice that must be managed.

### Runtime representation identity

Exposed Thing and Consumed Thing are software representations, not necessarily separate domain entities.

### Discovery provenance

TD may be supplied by:
- Thing itself;
- directory;
- external service;
- intermediary.

The model supports metadata distribution but does not define a generic provenance graph like PROV.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **Thing vs Device** — Thing can be physical or virtual; Device is physical.
2. **Thing vs Service** — physical and software realizations differ.
3. **Thing vs Thing Description** — entity and metadata representation are different.
4. **Thing Description vs Thing Model** — instance description and class/template are different.
5. **Thing Model vs deployed instance** — common capability model omits instance-specific data.
6. **Property vs Action vs Event** — state, invocation and asynchronous occurrence have different semantics.
7. **Affordance vs behavior implementation** — exposed interaction and internal/autonomous behavior are different.
8. **Affordance vs Protocol Binding** — abstract interaction semantics and concrete network realization are different.
9. **Thing vs Exposed Thing** — domain abstraction and runtime representation are different.
10. **remote Thing vs Consumed Thing** — remote subject and local proxy abstraction are different.
11. **original Thing vs Intermediary/Virtual Thing** — proxy/augmentation/composition can create a distinct exposed identity.
12. **Virtual composition vs physical composition** — aggregating Things in software does not prove hardware containment.
13. **TD links vs composition** — generic Web links need typed semantics and are not automatically part-of.
14. **public security metadata vs private security data** — discoverable security description and secrets/credentials differ.
15. **Thing identity vs TD location/URI** — domain identity and metadata/network location differ.
16. **current Property state vs Event** — state and state transition are different.
17. **Action invocation vs Event output** — commanded behavior and asynchronous event are different.
18. **Discovery directory vs Thing** — catalog/metadata broker and managed/exposed Thing are distinct.
19. **WoT core vocabulary vs domain-specific vocabulary** — WoT does not own sensor/equipment semantics simply because TD can carry them.
20. **Thing lifecycle vs physical asset service lifecycle** — WoT provisioning/offboarding semantics are not full maintenance history.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **likely reusable model/instance pattern:** Thing Model vs Thing Description;
- **likely binding-separation pattern:** abstract Properties/Actions/Events vs Protocol Bindings;
- **likely information pattern:** metadata description vs state vs action vs event;
- **likely mediation pattern:** Exposed Thing, Consumed Thing, Intermediary and Virtual Thing preserve separation between physical subject and Web-facing representation;
- **likely contextual relationship pattern:** typed links and discovery directories rather than inferred containment;
- **likely lifecycle pattern:** bootstrap/onboard/activate/offboard/decommission as network/system lifecycle, not maintenance lifecycle;
- **likely cross-cutting:** security metadata, semantic annotations, links, discovery and profiles;
- **profile-gap signal:** WoT intentionally leaves sensor/equipment, health, lifecycle-work and modality semantics to external domain vocabularies;
- **binding caution:** Thing/TD/TM/Affordance/Servient are Web architecture constructs; they may inform V2 representation but do not replace the DIM's equipment System concepts.

**No V2 module disposition is made in Phase A.**

---

**X11 status: COMPLETE.**

**Next frozen lineage:** S01 — Atomic sensor product evidence.

---

# S01 — Atomic sensor product evidence: Bosch BME280

## Source basis and evidence ceiling

**Frozen primary source ID:** 170.

**Primary inspected source:**

- Bosch Sensortec, *BME280 Combined Humidity and Pressure Sensor: Data Sheet*, Revision 1.24, February 2024, document BST-BME280-DS001-24.

**Evidence note:** This is a single commercial product datasheet used as a **scale-down falsifier**, not a standards authority. It tests whether the emerging anatomy can describe a small atomic sensing product without requiring every System to expose a rich recursive subsystem model. Only structures explicitly supported by the datasheet are recorded.

---

## 1. Source-native structural organization

The BME280 is described as one compact integrated digital sensor product whose internal functional structure includes:

1. **three sensing elements**
   - pressure sensing element;
   - humidity sensing element;
   - temperature sensing element;

2. **three corresponding analog front ends**;

3. **shared conversion/control electronics**
   - ADC;
   - logic;
   - oscillator;
   - power-on reset;
   - nonvolatile memory;
   - voltage regulator/reference;

4. **digital interface**
   - I²C;
   - SPI;
   - interface pins/signals;

5. **power partition**
   - VDD for internal analog/digital functional blocks;
   - VDDIO for digital interface supply;

6. **operational modes**
   - Sleep;
   - Forced;
   - Normal;

7. **measurement/configuration pipeline**
   - selectable temperature, pressure and humidity measurements;
   - independently skippable/oversampled channels;
   - optional IIR filtering for pressure/temperature;
   - result/output registers;

8. **configuration/state registers**
   - humidity oversampling;
   - pressure/temperature oversampling;
   - mode;
   - filter;
   - standby time;
   - status bits;

9. **calibration/compensation data**
   - NVM trimming/compensation coefficients;
   - formulas converting raw values to compensated engineering values;

10. **product/performance specifications**
    - measurement ranges;
    - accuracy;
    - noise;
    - response time;
    - current consumption;
    - package and electrical limits.

The source-native product anatomy is therefore **one equipment item with multiple internal sensing channels sharing conversion, logic, calibration, power and interface infrastructure**.

---

## 2. Purpose of each partition

### Sensing elements/front ends

Purpose: physically respond to pressure, humidity and temperature phenomena and condition the signals for conversion.

### ADC / logic

Purpose: convert and sequence the sensor channels, manage settings and place measurement results into registers.

### Temperature channel

Purpose: provide temperature measurement and, importantly, supply temperature information used to compensate pressure and humidity outputs.

### Power partition

Purpose: separately power:
- internal sensing/analog/digital logic;
- digital interface.

### Modes

Purpose:
- Sleep — minimum-power idle, register access retained;
- Forced — perform one measurement cycle and return to Sleep;
- Normal — repeat measurement cycles with inactive standby intervals.

### Oversampling/filter/data-rate configuration

Purpose: trade:
- noise;
- response time;
- data rate;
- current consumption.

### Compensation coefficients

Purpose: transform raw ADC outputs into usable compensated engineering measurements.

### Digital interface/register map

Purpose: expose configuration, status, calibration and output data to the host.

---

## 3. Central concepts per partition

| Source-native partition | Central concepts |
| --- | --- |
| Product identity | BME280, document/product number, chip ID |
| Sensing | pressure, humidity, temperature sensing elements |
| Signal conditioning | pressure/humidity/temperature front ends |
| Conversion | ADC, measurement sequencing |
| Control | logic, control/configuration registers |
| Power | VDD, VDDIO, voltage regulator/reference, sleep current |
| Mode | Sleep, Forced, Normal |
| Configuration | oversampling, IIR filter, standby time, mode bits |
| Status | measuring, NVM image-update state |
| Output | pressure, temperature and humidity data registers |
| Calibration | NVM trimming coefficients, compensation formulas |
| Interface | I²C, SPI, SDI/SDO/SCK/CSB |
| Performance | range, accuracy, noise, response time, current consumption |

---

## 4. Primary relationships

### Whole product → sensing elements

The BME280 remains one product even though it contains separate pressure, humidity and temperature sensing elements.

### Sensing element → front end → ADC

Each phenomenon-specific sensing element is conditioned before shared digital conversion/control.

### Temperature measurement → pressure/humidity compensation

Temperature output is used internally to compensate the pressure and humidity measurements, showing a functional dependency among measurement channels.

### Configuration → measurement pipeline

Oversampling and mode settings determine:
- whether a channel is measured or skipped;
- conversion behavior;
- resolution/noise/current trade-offs.

### Measurement → filter → output register

Temperature/pressure data can pass through the optional IIR filter before being copied to output registers; humidity bypasses that filter.

### NVM coefficients → compensation

Calibration/trimming coefficients stored in device NVM are applied to raw readings during compensation.

### Host → digital interface → registers

External host configures/reads the device through I²C/SPI rather than interacting directly with internal sensing elements.

---

## 5. Dependency boundaries

The product has clear internal boundaries despite being physically atomic from an external equipment perspective.

### Phenomenon-specific sensing vs shared electronics

Pressure/humidity/temperature sensing channels are distinct, while ADC, logic, power and interface are shared.

### Raw measurement vs compensated output

Raw ADC data and calibrated/compensated engineering output are separate stages.

### Sensor configuration vs measurement result

Registers controlling mode/oversampling/filter are different from output registers.

### Internal sensing function vs host interface

I²C/SPI access is an integration mechanism; it is not the sensing function itself.

### Product-level description vs host/application behavior

The datasheet describes what the sensor can do and how to interface to it, not the larger host device/system in which it is installed.

---

## 6. Intrinsic vs contextual standing

### Intrinsic to BME280

- sensing elements;
- shared ADC/logic;
- NVM/calibration coefficients;
- power rails;
- supported modes;
- measurement ranges/performance;
- configuration registers;
- output register structure;
- digital interfaces.

### Contextual/application-specific

- host processor;
- larger device using the BME280;
- final application;
- external mounting/location;
- host sampling policy;
- meaning assigned to measurements by the application.

The datasheet does not model deployment, platform, owner or mission context.

---

## 7. Cross-cutting concepts

Cross-cutting product concepts include:

- power/current consumption;
- temperature compensation;
- oversampling;
- timing;
- mode;
- interface;
- calibration coefficients;
- register access;
- electrical operating limits.

Temperature is particularly cross-cutting because it is both:
- an output measurement; and
- an internal compensation input for other channels.

---

## 8. State / temporal / lifecycle organization

The product has a compact operational state machine.

### Power-off

No valid operation without required supplies.

### Sleep

- default after power-on reset;
- no measurements;
- lowest power;
- registers/calibration data remain accessible.

### Forced

- one measurement cycle;
- results stored;
- automatic return to Sleep.

### Normal

- recurring measurement cycles;
- programmable standby/inactive intervals.

### Measurement state

Status register distinguishes whether:
- a conversion is currently running;
- NVM calibration data are being copied to image registers.

### Temporal configuration

Timing depends on:
- oversampling;
- measurement cycle;
- standby;
- filtering.

### Limit

There is no long-term equipment lifecycle, deployment history or maintenance history in the datasheet.

---

## 9. Composition / topology organization

The BME280 is a useful counterexample to assuming that every whole sensing System needs externally meaningful subresources.

### Internal physical/functional composition

Internally it contains:
- three sensing elements/front ends;
- shared ADC;
- shared logic;
- NVM;
- regulator/reference;
- interface.

### Shared-resource topology

Multiple sensing channels share:
- ADC/conversion infrastructure;
- logic;
- power;
- interface;
- calibration/compensation processing.

### External topology

Externally the product presents:
- one package;
- one digital interface endpoint/register space;
- separate supply pins.

### Important lesson from source

Internal functions are real and semantically distinct, but the datasheet does not give each sensing element an independent product identity, management endpoint or externally addressable subsystem resource.

---

## 10. Capability / function / behavior organization

Capability is expressed through product specifications and configuration choices rather than a generic Capability class.

### Measurement capabilities

- humidity;
- pressure;
- temperature.

### Configurable behavior

- independently enable/skip channels;
- oversampling;
- IIR filter;
- standby interval;
- operating mode.

### Performance capability

- range;
- accuracy;
- resolution/noise;
- response time;
- current consumption.

### Behavior

- host-triggered single measurement;
- cyclic autonomous measurement;
- sleep;
- register read/write.

The source therefore shows that **capability, configuration and current mode are distinct even for an atomic sensor**.

---

## 11. Information / output organization

### Raw data

ADC/raw sensor values are represented in output registers.

### Compensated measurement

Raw values require stored trimming coefficients and compensation formulas to produce engineering values.

### Three measurement outputs

- pressure;
- humidity;
- temperature.

### Configuration information

Separate registers hold:
- oversampling;
- mode;
- filter;
- standby settings.

### Status information

Status bits indicate:
- conversion activity;
- calibration/NVM update activity.

### Calibration information

Dedicated calibration/trimming registers store coefficients.

The product therefore distinguishes **measurement output, configuration, status and calibration information**.

---

## 12. Management / condition organization

Management is minimal but explicit.

### Configuration

Host can set modes, oversampling, filtering and standby.

### Reset

Device supports power-on reset and software reset behavior.

### Status

Status register exposes conversion/NVM-update activity.

### Self-check / plausibility

The datasheet includes product-level self-test/verification guidance, but this specialization extraction does not promote that into a universal condition model.

### Limit

There is no generic:
- health state;
- fault history;
- service record;
- work order;
- replaceable component inventory.

This is exactly the scale-down constraint: a useful DIM cannot require rich management structures to exist for every atomic sensing product.

---

## 13. Provenance / identity / reference organization

### Product/model identity

The datasheet identifies:
- BME280 product/model;
- sales/document numbers.

### Device identity

A chip-ID register identifies device type, but the datasheet does not expose a globally unique per-unit identity comparable to an asset UUID/serial-number model.

### Calibration provenance

NVM trimming coefficients are device-specific calibration data needed to interpret raw output.

### Measurement provenance

Pressure/humidity/temperature values originate from one integrated device and shared measurement pipeline.

### Limit

The product itself does not define a general provenance graph, observer/deployment model or external source-record lineage.

---

## 14. Semantic invariants that would be damaged by collapsing distinctions

1. **whole BME280 vs individual sensing element** — one product contains several sensing elements without making each a separately managed product.
2. **pressure vs humidity vs temperature channel** — different phenomena and performance/configuration semantics.
3. **temperature output vs temperature-compensation role** — one channel can serve both external output and internal correction.
4. **sensing element vs front end vs ADC/logic** — transduction, conditioning and conversion/control are different functions.
5. **raw value vs compensated engineering value** — calibration processing materially changes interpretation.
6. **calibration coefficient vs measurement result** — descriptive correction data and runtime output differ.
7. **configuration vs status vs output** — what the device is set to do, what it is currently doing and what it measured are different.
8. **Sleep vs Forced vs Normal** — distinct operating states/behaviors.
9. **mode vs oversampling/filter setting** — operating-state selection and performance/configuration parameters are different.
10. **measurement channel skipped vs product absent/unavailable** — disabling one channel does not remove the whole sensor.
11. **VDD vs VDDIO** — internal sensor supply and digital-interface supply are different electrical concerns.
12. **I²C/SPI interface vs sensing function** — communication mechanism does not define the measurement domain.
13. **status register activity vs equipment health** — measuring/NVM-update bits are not generic health/readiness.
14. **internal block diagram vs externally addressable subsystem model** — real internal structure does not imply each block should be a top-level information resource.
15. **product model identity vs per-instance asset identity** — datasheet identifies a product type, not necessarily a unique deployed instance.

---

## 15. Potential V2 structural contribution — evidence label only

**Potential contribution labels:**

- **atomic-equipment stress test:** V2 anatomy must remain useful when the whole System is one small integrated sensor with no meaningful externally managed subsystem tree;
- **likely intrinsic pattern:** measurement channels, configuration, operating mode, performance, calibration, power and interface remain separable concerns even in a tiny device;
- **likely information pattern:** measurement output vs status vs configuration vs calibration data;
- **likely capability pattern:** supported measurement/performance capability separated from selected settings/current mode;
- **likely composition caution:** internal functional blocks need not become independently addressable V2 components;
- **likely model/instance caution:** product datasheet semantics are mostly model/type-level; deployed-instance identity/context must come from other sources;
- **profile-gap signal:** an atomic sensor may lack rich health/lifecycle/work/communications structures, so optionality/specialization is essential;
- **authority caution:** Bosch product semantics can validate scale and practical organization but do not supply universal V2 vocabulary.

**No V2 module disposition is made in Phase A.**

---

**S01 status: COMPLETE.**

**Next frozen lineage:** S02 — Radiation detection / instrument family.

