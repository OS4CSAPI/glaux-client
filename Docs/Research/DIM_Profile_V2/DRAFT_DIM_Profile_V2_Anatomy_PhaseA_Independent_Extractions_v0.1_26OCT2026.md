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

