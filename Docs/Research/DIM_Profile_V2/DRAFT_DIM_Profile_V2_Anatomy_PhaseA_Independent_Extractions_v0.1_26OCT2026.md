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

