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

