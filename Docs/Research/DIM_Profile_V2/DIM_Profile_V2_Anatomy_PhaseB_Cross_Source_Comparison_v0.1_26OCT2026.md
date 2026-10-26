# DIM/Profile V2 Anatomy — Phase B Cross-Source Structural Comparison

**Working draft v0.1 — 26 October 2026**  
**Status:** Phase B comparison complete. This artifact identifies recurring structures and propositions eligible for Phase C consideration; it does **not** adopt final V2 modules or edit the clean DIM.  
**Controlling continuity:** PITON_DIM_Profile_V2_Continuity_v0.9_26OCT2026.md  
**Phase A evidence:** DRAFT_DIM_Profile_V2_Anatomy_PhaseA_Independent_Extractions_v0.1_26OCT2026.md

## 1. Purpose and method

Phase A independently extracted the source-native anatomy of all **30 frozen semantic lineages** before any cross-source comparison. Phase B now asks:

> Across those lineages, which structural distinctions recur, which terms are overloaded or conflicting, which information is intrinsic to the bounded sensing System, which belongs to context or cross-cutting concerns, and which structures remain domain specializations?

The comparison follows five controls:

1. **Semantic lineage, not publication count, is the unit of evidence.**
2. Similar labels are not treated as equivalent until their source semantics are compared.
3. API/resource hierarchy, ontology hierarchy, UI grouping and physical composition are not presumed equivalent.
4. A recurring concern is not automatically a future V2 module.
5. No Version 1 subject names are used as comparison bins.

The working chassis remains outside the comparison as a fixed boundary:

> **physically realized equipment Systems whose defining operational role is sensing/observing, modeled as complete operational subjects.**

---

# 2. Neutral structural comparison matrix

| Lineage | Persistent subject / model structure | Composition / topology | Capability / configuration / state | Dynamic information / interaction | Context / provenance emphasis |
| --- | --- | --- | --- | --- | --- |
| **C01 AAS** | Asset distinct from AAS; type/instance/batch/role; Submodel templates vs instances | Entity hierarchy; self/co-managed parts; multiple aspect hierarchies | Capability distinct Operation/Skill; properties vs constraints | Generic events/operations, not observation-specific | Semantic IDs, references, versions; location/install views separate product structure |
| **C02 Redfish/CIM** | Resource identity distinct product identity; Chassis/System/Manager/Sensor separated | Physical containment distinct links, management and network relations | State, Health and Condition distinct; Actions; offline/online patterns | Metrics/telemetry/events separate persistent resource | Facility, manager, power source and metric source references |
| **C03 IEEE 1451** | APP/NCAP/TIM/channel layers; module vs channel; TEDS description | TIM/channel grouping distinct physical containment | Channel capability/performance, calibration, timing, self-test | Runtime transducer data and service messages separate TEDS | UUID/source identity; interface/security/time metadata distinct application governance |
| **C04 ISA** | ISA Component may be physical/logical/virtual; CCD self-description | Composition, network, deployment and visibility topologies distinct | Capability declaration → readiness/reporting state → live value | Config, Status, Event, Request, Response, History distinct | UCI/message/product identities; authorization, platform and ownership context |
| **C05 SNRA** | Sensor network vs sensor node vs sensor | Physical topology and functional topology mapped many-to-many | Function separated implementation; layered services/management | Data acquisition/processing/comms/storage/application functions | Gateway/network/provider/user context outside individual node |
| **C06 Matter** | Node vs Endpoint vs Device Type vs Cluster | Endpoint composition via PartsList distinct network Binding and physical BOM | Device Type/feature/conformance distinct live state | Attribute, Command and Event distinct | Fabric and semantic tags contextualize endpoints |
| **C07 MIMOSA** | Asset vs Model/Revision/Variant; persistent Asset vs Segment/location | AssetComponent vs SegmentComponent; network separate | Registry/config status distinct condition assessment | Measurement/Test/Event → Assessment → Prognosis → Recommendation → Work | InfoSource, Agent, time, quality, work/evidence provenance |
| **C08 CSAPI** | System vs Procedure/systemKind; role vs realization; persistent UID vs URL/local ID | Composition vs Aggregation; System topology vs Deployment topology | Role/procedure/stream/control feasibility distributed | DataStream/Observation; ControlStream/Command/Status/Result; SystemEvent | Deployment/Platform/FOI/SamplingFeature context; persistent links |
| **C09 SensorML** | General process vs specific/configured instance; model via typeOf | Component decomposition, data-flow connection, attachment and Deployment distinct | Capability vs characteristic vs configuration/mode/settings | Interface/output schema separate actual observation; history Events | validTime, Deployment, platform, FOI, reference frames, lineage |
| **C10 OPC/PA-DIM** | Device vs software/component; generic DeviceType vs specialization | Component hierarchy, FunctionalGroups, network topology and integration topology distinct | Parameters/Methods/health/condition; offline vs online | Process signals separate configuration and condition | Product IDs, semantic dictionary IDs, ConnectionPoints, host/manager |
| **C11 OSUS** | Whole Asset instance vs product/factory type; internal sensor IDs | Whole Asset with internal sensors; no universal recursive BOM | Advertised capability vs activation/status/BIT/config | Observation/status vs command/response vs runtime event | Asset/product/sensor/Observation identities; platform pose context |
| **C12 SAPIENT** | Node role broader than physical device; Edge/Fusion/Platform distinctions | Subcomponent hierarchy, platform dependency and fusion hierarchy distinct | General capability vs Mode vs current mode/status | Registration, Status, Detection, Alert, Task, TaskAck distinct | Node/message/object/task/product IDs; hierarchy/platform context |
| **C13 SAREF** | Device vs DeviceKind; generic concepts vs entity-specific OfInterest | consistsOf distinct system Connection and spatial relation | Task → Function → Command; Function/CommandOfInterest; State | Observation/Actuation/Execution separate values | Service/Operation separate Device; target Feature/Property/State |
| **C14 SOSA/SSN** | Asset/System/Platform roles; System vs Procedure vs Execution | Subsystem composition distinct Platform hosting and Deployment | Capability separated operating/survival conditions | Observation, Actuation, Sampling and Collections distinct | Observer/executor, target, procedure, time, sample/deployment lineage |
| **C15 Open Group SOSA** | Whole Sensor vs Component vs Product/ProductInstance | Functional, physical, comms, product and management topologies distinct | health, operational state, configuration state, mode, BIT/fault separate | Mission products/data separated management/condition info | Host Platform, Controller/Manager, product realization and module identity |
| **X01 I-ADOPT** | Variable meaning decomposed; Entity roles rather than device model | Symmetric/asymmetric conceptual systems, not equipment topology | Constraints/modifiers qualify variable semantics | Variable description separate Observation/result | ObjectOfInterest, Matrix, ContextObject and role-qualified Entities |
| **X02 EMAN** | Energy Object vs Device/Component/PowerInterface | Power-source, metering and aggregation relations distinct containment | Power State separate measurements; battery admin/oper states | nameplate/static vs live power vs accumulated energy/demand | measurement caliber/method/accuracy; context role/category |
| **X03 RFC 8348** | Hardware component identity with several identifier types | explicit physical parent/relative position hierarchy | admin/oper/usage/alarm/standby states distinct | component sensor readings separate identity/state | manufacture/FRU metadata; physical index vs durable identity |
| **X04 IETF Interfaces/Topology** | Interface/node IDs are network-management identities | Node→TP→Link, layering, overlay/underlay distinct hardware composition | admin vs oper state; configuration and counters | counters/events, not sensing outputs | supporting topology mappings; same device can have multiple representations |
| **X05 JC3IEDM** | OBJECT-TYPE vs OBJECT-ITEM; identity vs status/location | holdings/org structure/action relations distinct physical parts | Capability distinct Action/task/event | Action, status and reporting facts separate | Location, affiliation, Context, ReportingData, security/reference |
| **X06 NIEM** | Core vs Domain; Type vs Property; entity vs role | Associations and augmentations, not physical hierarchy | extension/profile selection rather than runtime state | exchange/message models selected from broader reference model | Adapters, references, roles, namespace ownership, metadata/security |
| **X07 NIST 8259A** | Device identity includes logical/physical identifier distinction | no equipment BOM | six cross-cutting cybersecurity capabilities | security-state awareness/events/logs distinct state | authorized entities/access and manufacturer-support boundary |
| **X08 OMS** | Observer vs Procedure; ObservationCharacteristics vs actual Observation | Observer–Host Deployment and sampling chain, not equipment BOM | ObservingCapability separate Observation | Observation act vs Result/quality/collection; Sampling/Preparation chain | proximate/ultimate FOI; observer/procedure/time/host provenance |
| **X09 LwM2M** | Client vs physical Device; Object vs Instance vs Resource | management namespace/gateway routing distinct physical composition | supported operations/access; configuration and update state machines | Resource value vs Execute; Observe/Notify/Send | Server/ACL/gateway/host context; endpoint/product/Object IDs distinct |
| **X10 PROV** | Entity/Activity/Agent roles; specialization/alternate views | provenance graph/Collection/Bundle, not physical topology | no device capability model | generation/use/derivation/revision/responsibility | provenance is the core concern: source, agent, activity, role, time |
| **X11 WoT** | Thing vs Device/Service; TD instance vs TM class | virtual composition/links distinct physical composition | Property/Action/Event affordances; network lifecycle | description vs state vs Action vs Event | Exposed/Consumed/Virtual Thing, intermediary, discovery/security/binding |
| **S01 BME280** | product model vs deployed instance; one whole atomic sensor | internal functional blocks but no independently managed subresources | supported performance vs selected settings/current mode | measurements vs status vs configuration vs calibration | host/application/deployment outside product datasheet |
| **S02 Radiation** | whole instrument vs detector/channel | handheld through multi-detector portal; host/site separate | instrument/detector capability, calibration, status/alarm | measurement vs analysis vs alarm; spectra/counts/dose/stream | detector/calibration/source/time and screening context |
| **S03 SWEET** | Equipment → Instrument/Device → Sensor/specialized instrument | taxonomy only; no physical composition | class/property restriction, not runtime capability | measured-property relationship, not Observation records | class URI/ontology semantics only |
| **S04 UGS** | persistent device vs detector/transducer vs product/variant | physical part, trigger/cue, communications and deployment grouping distinct | supported/installed → configured/enabled → requested → reported/applied | status, detection, imagery and commands have different roles | field-level source/time/authority; emplacement/network/operator context |

---

# 3. Recurring structural patterns

## 3.1 Persistent subject, reusable model/type, and representation are repeatedly different

A strong cross-lineage pattern separates:

1. the persistent real-world subject;
2. a reusable kind/model/type/template;
3. one digital/API/runtime representation of the subject.

Representative evidence:

- AAS: Asset vs AAS; type/instance; Submodel Template vs instance.
- MIMOSA: Asset vs Model/Revision/Variant.
- SensorML: general process via typeOf vs configured/specific process.
- SAREF: DeviceKind vs Device.
- WoT: Thing Model vs Thing Description vs Thing.
- OPC: DeviceType vs Device instance, NodeId vs Asset/product identity.
- CSAPI: persistent UID vs local ID/canonical URL; System vs Procedure/systemKind.
- Redfish/LwM2M/ISA: management/interface resource identity is not automatically the durable physical identity.

**Phase B finding:** V2 must preserve at least the distinction between **persistent subject identity**, **reusable model/kind semantics**, and **representation/binding identity**. The exact V2 carriers remain a Phase C/binding question.

---

## 3.2 One universal component tree is contradicted by the donor evidence

The sources repeatedly expose multiple simultaneous topologies:

- **physical composition / part-of**;
- **functional grouping**;
- **communications/network topology**;
- **host/platform/deployment relationships**;
- **power-source/metrology relationships**;
- **virtual/interface-mediated composition**;
- **operational dependency/cue/task relationships**.

Representative examples:

- OPC: component hierarchy vs FunctionalGroups vs Device→ConnectionPoint→Network.
- Open Group SOSA: functional, physical, communications, product-realization and management topologies.
- SensorML: component relation vs data-flow connection vs attachedTo vs Deployment.
- ISA: composition vs network vs deployment; visible/opaque/virtual members.
- SAPIENT: subcomponents vs platform dependencies vs fusion hierarchy.
- Matter: PartsList endpoint composition vs Binding; PartsList is not a physical BOM.
- CSAPI: Composition vs Deployment-based Aggregation.
- SOSA/SSN: subsystem composition vs Platform hosting vs Deployment.
- EMAN: power source/metering/aggregation vs physical containment.
- UGS: part-of vs cue/trigger vs communications vs deployment grouping.

**Phase B finding:** a single undifferentiated parent/child relationship would destroy donor meaning. V2 needs relationship semantics rich enough to distinguish at least persistent composition from hosting/deployment, functional grouping, communications connectivity and mediated/operational relationships.

---

## 3.3 Whole equipment and internal sensing element/channel are different scopes

This distinction recurs across otherwise unrelated communities:

- IEEE 1451: TIM vs TransducerChannel vs physical transducer.
- OSUS: one Asset may have multiple sensor IDs.
- Open Group SOSA: whole Sensor vs Sensor Component.
- Radiation: whole instrument/portal vs detector/channel.
- UGS: whole device vs detector slot/transducer.
- SNRA: sensor node vs sensor.
- BME280: one product containing three sensing elements.
- Redfish: Sensor resource can measure a different managed resource.

**Phase B finding:** V2 must support internal sensing elements/channels without requiring them all to become top-level peer Systems, and it must not reduce the whole System to the semantics of one detector/channel.

---

## 3.4 Capability, configuration, current state, execution and result are distinct semantic layers

This is one of the strongest cross-source convergences.

Representative chains:

- ISA: capability declaration → capability state → live property/observable → command execution/result.
- SAPIENT: capability → supported Mode → current Mode → Task → TaskAck/detections.
- SensorML: capability/characteristics → ConfigurableProcess/Mode/Settings → configured process → output.
- SAREF: Function/Command kind → Function/CommandOfInterest → Service/Operation → Execution.
- AAS: Capability → constraint/property → Skill/Operation realization.
- Matter: Device Type/Feature support → Attributes/Commands/Events → live state/execution.
- CSAPI: Procedure/role/output/control description → Command → CommandStatus → CommandResult.
- UGS: supported/installed → configured/enabled → requested/queued → reported/applied.
- BME280: product capability → settings/mode → measurement/status.

**Phase B finding:** V2 must not use one overloaded capability or state structure for all five meanings. At minimum, **supported potential**, **selected configuration**, **current condition/state**, **requested/performed action**, and **result/evidence** remain distinguishable.

---

## 3.5 Static description and dynamic information are repeatedly separated

Across the corpus, mature models avoid treating every changing value as an ordinary descriptive property.

Examples:

- Redfish Resource vs Metrics/Telemetry/Event.
- CSAPI System/Procedure/Deployment vs DataStream/Observation/ControlStream/Command/SystemEvent.
- ISA Config vs Status vs Event vs Request/Response.
- Matter Descriptor/DeviceType vs Attributes/Events/Commands.
- IEEE 1451 TEDS vs runtime transducer data.
- OSUS capabilities vs Observation/status/Response.
- LwM2M Object semantics vs Observe/Notify.
- WoT TD/TM vs Property/Event/Action interactions.
- radiation instrument description/calibration vs measurement/status/analysis/alarm.
- BME280 configuration/calibration vs measurement/status.

**Phase B finding:** V2 anatomy should distinguish the **enduring description of the System and its supported interfaces** from **time-varying telemetry, observations, actions, status and events**.

---

## 3.6 Observation, measurement result and analysis/assessment are not equivalent

Several independent lineages draw a layered evidence chain.

- OMS: Observation act ≠ Result; result quality is separate.
- SOSA/SSN: Observation/Execution ≠ result.
- MIMOSA: Measurement/Test/Event ≠ HealthAssessment ≠ RemainingLifeAssessment ≠ Recommendation/Work.
- radiation: measurement ≠ analysis ≠ alarm.
- PROV: Entity output ≠ Activity that generated/derived it.
- UGS: detection ≠ image/evidence ≠ operator/system state.
- I-ADOPT: Variable semantics ≠ Observation/result.

**Phase B finding:** raw or observed evidence, derived analysis/assessment, decision/alarm/recommendation and subsequent action/work must not be collapsed merely because all are outputs.

---

## 3.7 Property/variable meaning is separate from the value that instantiates it

Strong semantic-model convergence exists around this distinction:

- CSAPI Property definition vs observed/controlled value.
- OMS ObservableProperty vs Result.
- SOSA/SSN Property vs result.
- SAREF Property/PropertyOfInterest vs PropertyValue.
- I-ADOPT Variable decomposition into Property + ObjectOfInterest + contextual qualifiers.
- SWEET instrument class vs measured property.
- IEEE channel metadata vs runtime reading.

**Phase B finding:** V2 needs a traceable distinction between **what a quantity/property/variable means** and **a particular value/result of that meaning**.

---

## 3.8 Deployment, hosting and operational context are consistently outside intrinsic composition

This distinction is unusually stable.

- SOSA/SSN: Platform hosting and Deployment distinct subsystem composition.
- Open Group SOSA: Sensor vs Host Platform.
- CSAPI: Composition vs Deployment-based Aggregation.
- SensorML: component vs attachedTo vs Deployment/platform.
- OMS: Observer vs Host vs Deployment.
- MIMOSA: Asset vs Segment/Site installation.
- SAPIENT: Node vs Platform dependency.
- radiation: instrument vs host vehicle/site/lane.
- UGS: persistent device vs emplacement/network/operator context.

**Phase B finding:** operational placement/host/deployment should be related to the persistent System, not absorbed into its identity or permanent component tree by default.

---

## 3.9 Lifecycle is not one thing

The corpus contains several semantically different lifecycles:

- **asset/equipment lifecycle** — MIMOSA;
- **configuration/history events** — CSAPI/SensorML;
- **network participation lifecycle** — ISA/SAPIENT;
- **bootstrap/registration lifecycle** — LwM2M;
- **Thing onboarding/offboarding lifecycle** — WoT;
- **software/firmware update lifecycle** — Redfish/OPC/LwM2M/NIST;
- **command/task lifecycle** — CSAPI/SAPIENT;
- **observation/sampling process time** — OMS/SOSA;
- **provenance generation/invalidation** — PROV.

**Phase B finding:** one generic lifecycle bucket would be semantically weak. Phase C should consider a narrower distinction between **persistent-history/event semantics** and several specialized process lifecycles rather than presuming one universal lifecycle structure.

---

## 3.10 Identity is layered and source-qualified

Repeated identity layers include:

- persistent equipment/System identity;
- product/model/type identity;
- internal component/channel/sensor identity;
- API/resource/endpoint identity;
- network/protocol identity;
- message/observation/task/event identity;
- target/feature/object identity;
- semantic-term/class identity;
- provenance/source/agent identity.

The UGS evidence adds an operational warning: database/operator-entered and device-reported values can coexist, so source/authority cannot always be inferred from the field name.

**Phase B finding:** V2 needs identity/reference semantics that preserve **scope and authority**, not one unqualified identifier list.

---

## 3.11 Physical and logical/virtual representation must remain distinguishable

The cross-type audit brought this pattern into sharp focus.

- AAS: Asset vs AAS representation.
- ISA: physical member vs virtual ISA Component; opaque/visible mediation.
- WoT: Thing vs Exposed/Consumed/Virtual Thing/Intermediary.
- Redfish: CIM LogicalDevice vs physical realization.
- LwM2M: Client vs physical Device; gateway routing.
- Matter: Endpoint is functional/addressable, not necessarily physical part.
- SAPIENT: Node can represent fusion/platform/software/human roles.
- OPC: online/offline AddressSpace representation vs real-world Device.
- NIEM: Adapter/Representation vs source concept.

**Phase B finding:** V2 must be explicit when a modeled object is the physical subject, a logical function, an interface participant, or a mediated/virtual representation.

---

## 3.12 Scale and optionality are structural requirements, not afterthoughts

The specialization evidence spans:

- BME280: one compact integrated product with no useful independently managed component tree;
- radiation portal: multi-detector installed equipment with ancillary occupancy/video;
- UGS: remotely deployed systems with variant-dependent detectors, batteries, communications and configuration;
- Open Group SOSA: complex modular defense sensors;
- PA-DIM: process automation devices;
- SensorML: atomic PhysicalComponent vs aggregate PhysicalSystem.

**Phase B finding:** common anatomy must support **atomic through composite** equipment without mandatory empty structures or forced subsystem identities. Specialization and optionality are inherent design requirements.

---

# 4. Overloaded and conflicting terminology

| Term | Material source meanings | Phase B consequence |
| --- | --- | --- |
| **Asset** | AAS: physical/digital/intangible represented thing; MIMOSA: lifecycle-managed physical asset; OSUS: physical device; SOSA/SSN: broad superconcept above System/Platform | Never treat unqualified Asset as one cross-source class without a mapped scope. |
| **Device** | OPC: physical Device specialization of Component; SAREF: tangible task-performing System; SWEET: equivalent to Instrument; LwM2M: generic managed device behind Client; Matter: Device Type is endpoint functional classification | Device is not a stable universal root term. |
| **Sensor** | SOSA/SSN: observing System that may be device/human/software; SAREF: tangible Device; SWEET: Instrument + SOSA Sensor; Open Group SOSA: whole defense Sensor; OSUS/UGS: can mean internal sensing element | Always preserve whether Sensor denotes role, whole equipment or internal element. |
| **System** | SOSA/SSN: broad procedure-implementing Asset; CSAPI: general persistent resource; SensorML: process/system abstraction; Open Group SOSA: sensor architecture subject | System is broad and requires role/realization/context qualifiers. |
| **Component** | OPC: physical or software part; Open Group SOSA: functional physical/software unit; RFC8348: hardware component; ISA: interface participant, possibly virtual; Matter: endpoint structure is not necessarily physical | Component must be typed by relationship/scope; it cannot imply physical part automatically. |
| **Platform** | SOSA/SSN: Asset that hosts; Open Group SOSA: physical host; SAPIENT: taskable Mobile/Pointable Node; CSAPI: system role and deployment host | Host role, platform-node role and system classification must not be conflated. |
| **Capability** | AAS: potential to achieve effect independent implementation; ISA: Property/Observable/Command declarations; SAPIENT: modality/function/performance declaration; NIST: cybersecurity capability; SOSA: observing capability pattern | A common capability concept, if proposed later, needs explicit semantics and cannot simply union all source meanings. |
| **State / Status / Health / Condition** | Redfish distinguishes all; RFC8348 has multiple state dimensions; SOSA capability uses operating conditions; UGS has vendor status; MIMOSA distinguishes lifecycle status and assessment | A single status field is inadequate. Phase C must preserve dimensions/source ownership. |
| **Observation** | OMS/SOSA: an act/execution; CSAPI: observation resource; OSUS: persisted data envelope that can include Status; SAPIENT uses Detection instead | Do not equate all observation-like records by label. |
| **Deployment** | CSAPI: time/context resource for Systems/aggregation; SOSA/SSN: System–Platform deployment; SensorML: descriptive deployment with configuration; OMS: Observer–Host deployment | Shared theme is contextual employment/hosting, but exact participants/semantics differ. |
| **Composition** | physical part-of, endpoint composition, ISA interface composition, AAS hierarchy, PROV Collection, NIEM message structures | Only explicitly physical/enduring composition should be treated as equipment part-of. |
| **Model / Type** | product model, DeviceKind, Thing Model, SensorML general process, OBJECT-TYPE, schema type | Reusable class/kind/model meanings converge structurally but are not identical representations. |
| **Interface** | hardware port, logical connection point, API/service, ISA interface stack, network interface, process input/output | Every interface must retain its layer/role. |

---

# 5. Intrinsic, contextual, dynamic and cross-cutting standing

The 30 lineages do not support one flat information list. A more stable comparison is by **relationship to the persistent sensing System**.

## 5.1 Recurrently intrinsic or subject-defining

The following repeatedly attach to the persistent equipment subject when applicable:

- persistent identity and product/model/type association;
- physical realization/equipment classification;
- enduring component/subsystem relationships;
- supported sensing elements/channels;
- capabilities/performance envelope;
- supported functions/actions/interfaces;
- configuration space/modes/settings;
- intrinsic physical characteristics;
- calibration/performance metadata;
- product/software/firmware revisions;
- supported communications/power interfaces.

These may still be optional for an atomic or simple device.

## 5.2 Recurrently contextual or relational

The following are commonly modeled **around** the subject rather than as its permanent contents:

- Deployment/emplacement;
- Host Platform;
- Site/facility/functional location;
- current location when not inherent;
- network/Fabric/topology membership;
- gateway/intermediary/manager/controller relationship;
- operator/organization/owner/responsible party;
- mission/task/operational action;
- FeatureOfInterest/target;
- peer/fusion/group membership;
- temporary aggregation/cue/dependency relationships.

## 5.3 Recurrently dynamic/evidentiary

Changing or event-like information often has its own structures:

- Observations/detections/measurements;
- current telemetry/status;
- commands/tasks/requests;
- command/task status and results;
- alerts;
- events/history;
- analysis/assessment products;
- software/firmware update state;
- work/service records.

These should not be forced into timeless descriptive properties.

## 5.4 Recurrently cross-cutting

Cross-cutting semantics repeatedly span several concerns:

- source/provenance/responsibility;
- time and validity;
- identity/reference;
- semantic definitions/property/variable meaning;
- units/quality/uncertainty;
- security/access/authorization;
- version/revision;
- documentation/external artifacts;
- relationship qualification.

---

# 6. Source-lineage convergence and dependency notes

Apparent convergence must be interpreted carefully.

- **IEEE 1451.1-1999 and ISO/IEC/IEEE 21451-1:2010** are one NCAP conceptual lineage, not two votes.
- **OPC UA Part 100 and PA-DIM** are generic base + specialization.
- **SOSA/SSN 2017 and 2026 drafts** are one evolving ontology lineage; the 21 October 2026 draft controls current interpretation.
- **Open Group SOSA DSDM and Technical Standard** are one architecture/data-model lineage.
- **N42.42 / IEC 62755 / N42.61 / N42.38 / IAEA / ISO 22188** are a radiation specialization family with overlapping but distinct exchange/performance/operational purposes.
- **PROV-DM and PROV-O** are conceptual model + ontology encoding.
- **Matter Core and Device Library** are core model + concrete Device-Type specification.
- **AAS Part 1 and selected IDTA Submodel Templates** are metamodel + standardized aspect templates.
- **MIMOSA CCOM / OSA-EAI / OSA-CBM** are conceptual model + integration architecture + functional condition-processing architecture, not identical artifacts.
- **ISA DMS/SDD/requirements/ICD** are one architecture/data/interface lineage whose documents partition responsibility.
- **SensorML + SWE Common + CSAPI** are related OGC/SWE/Connected Systems families, but their standards own different semantics and must not be counted as one or assumed mutually equivalent.

---

# 7. Specialization-only findings

The following structures have strong evidence but should remain specialization candidates unless later Phase C/validation proves broader applicability.

### Radiation

- gamma/neutron quantities;
- spectra/channel calibration;
- radionuclide identification;
- radiation alarm semantics;
- portal-lane screening workflow;
- primary/secondary inspection.

### UGS

- vendor detector-slot labels;
- specific sleep/recovery/tamper rules;
- device-specific cueing/triggering semantics;
- source-specific status values;
- vendor configuration panels/commands.

### Scientific instruments

- radar/lidar/thermometer and other SWEET instrument classes.

### IEEE 1451 native mechanisms

- TEDS fields and byte formats;
- APP/NCAP/TIM service protocols;
- family-specific physical interfaces.

### Matter/LwM2M/Redfish native management mechanics

- Cluster/Object/Resource paths;
- protocol lifecycle;
- management-resource schemas.

**Phase B finding:** specialization can reuse a common structural distinction without making its domain vocabulary mandatory in the common DIM.

---

# 8. Unresolved contradictions and gaps

## 8.1 No single cross-source capability model has yet emerged

The sources agree that **capability differs from current state/execution**, but they disagree on what capability itself contains:

- effect potential;
- property/observable/command declarations;
- modes/performance;
- security management capabilities;
- observing characteristics;
- function/command hierarchy.

Phase C must decide whether the common DIM needs:
- one narrow generic capability concept;
- several typed capability relationships; or
- only source-owned specialized capability structures.

This cannot be decided from label convergence alone.

## 8.2 Condition/health/state remains multi-dimensional

The sources repeatedly distinguish:
- operating state;
- health;
- condition/fault;
- readiness/availability;
- mode;
- configuration state;
- alarm;
- BIT/self-test;
- lifecycle status;
- cybersecurity state.

A common status object would erase meaning. Phase C must determine which dimensions belong in common anatomy and which remain specialized/source-defined.

## 8.3 Lifecycle/history scope is unresolved

There is strong need for history, but sources describe different processes:
- equipment/service lifecycle;
- deployment history;
- configuration history;
- software update;
- network registration;
- command/task lifecycle;
- provenance lineage.

The common anatomy may need a generic historical-event backbone plus specialized process semantics, but Phase B does not establish the final structure.

## 8.4 Analysis/assessment/derived information may be common but needs validation

MIMOSA, radiation, SAPIENT fusion and PROV expose strong evidence/evaluation chains. However, not all sensing systems generate:
- assessments;
- fusion products;
- alarms;
- recommendations;
- reports.

A reusable derived-information relationship is plausible; a mandatory analysis structure is not yet earned.

## 8.5 Communications and power are structurally recurring but not universal as rich submodels

Nearly every real equipment family has communications and power, but:
- atomic devices may expose only pins/interfaces;
- externally powered/fixed systems may have little battery information;
- network models can become much larger than the sensing System;
- energy management standards are purpose-specific.

Phase C must distinguish **common relationship hooks/basic semantics** from optional rich specializations.

## 8.6 Security is cross-cutting but common-DIM depth is unresolved

NIST, WoT, ISA, LwM2M, IEEE and other sources separate security/access concerns from equipment mission semantics. The DIM likely needs enough semantics to identify relevant security/interface constraints and provenance, but enterprise authorization infrastructure and credential material are clearly outside the equipment anatomy.

## 8.7 Operational-episode grouping remains unproven as a universal common concept

The radiation/OSCAR work suggests value in grouping heterogeneous evidence around one real-world passage/event, but the frozen Phase A population does not yet establish a cross-domain universal episode construct. It should not be promoted simply because one specialization benefits from it.

## 8.8 Exact common relationship vocabulary remains open

The evidence strongly requires separate relationship meanings, but exact names/cardinalities for:
- part-of;
- hosted-by;
- deployed-with;
- connected-to;
- supplied-by;
- measured-by;
- controlled-by;
- represented-by;
- mediated-by;
- triggered/cued-by

remain a Phase C/validation task.

---

# 9. Structural propositions eligible for Phase C consideration

These are **propositions**, not adopted modules, classes or profile requirements.

### P01 — Persistent subject identity should be structurally distinct from reusable model/kind and representation identity

Supported broadly by AAS, MIMOSA, SensorML, SAREF, WoT, OPC, CSAPI, Redfish, LwM2M and specialization evidence.

### P02 — The common model should support atomic and composite equipment without requiring every internal function to become an independently addressable component

Supported by BME280, SensorML, OSUS, radiation, UGS, Open Group SOSA, OPC.

### P03 — Relationship semantics should distinguish enduring physical composition from hosting/deployment, network/connectivity, functional grouping and operational/virtual mediation

Supported across CSAPI, SOSA/SSN, SensorML, OPC, ISA, SAPIENT, Matter, EMAN, Open Group SOSA, UGS.

### P04 — Capability/support semantics should remain distinct from selected configuration, current state, execution and result

Supported strongly across ISA, SAPIENT, SensorML, SAREF, AAS, Matter, CSAPI, OSUS, UGS, BME280.

### P05 — Static/system description should remain distinct from dynamic observations/telemetry, actions/commands, alerts and events

Supported across Redfish, CSAPI, ISA, Matter, IEEE 1451, OSUS, LwM2M, WoT, radiation.

### P06 — Property/variable definitions should be reusable semantic objects distinct from particular values/results

Supported by I-ADOPT, OMS, SOSA/SSN, SAREF, CSAPI, SWEET, IEEE.

### P07 — Observation/execution should remain distinct from result/value and from derived analysis/assessment

Supported by OMS, SOSA/SSN, MIMOSA, radiation, PROV, I-ADOPT.

### P08 — Request/action/task should remain distinct from execution status/progress and result

Supported by CSAPI, ISA, SAPIENT, OSUS, Matter/SAREF interaction patterns.

### P09 — Current state should remain distinct from historical event/transition and from longer equipment/service lifecycle

Supported by CSAPI, MIMOSA, SensorML, PROV, LwM2M, Redfish/OPC and UGS.

### P10 — Provenance/source/responsibility should be cross-cutting and capable of qualifying individual facts/results, not only the whole resource

Supported by PROV, MIMOSA, OMS/SOSA, OSUS, ISA, UGS, radiation.

### P11 — Identity should be scoped by role: equipment, model/type, component/channel, representation/resource, message/data item and semantic definition should not share one unqualified identifier model

Supported across nearly every core and cross-cutting lineage.

### P12 — Physical subject and logical/virtual/interface representation should be explicitly distinguishable

Supported by AAS, ISA, WoT, Redfish/CIM, LwM2M, Matter, SAPIENT, OPC/PA-DIM, NIEM.

### P13 — Deployment/host/location/operational context should be related to the persistent System rather than assumed intrinsic composition

Supported by SOSA/SSN, Open Group SOSA, CSAPI, SensorML, OMS, MIMOSA, SAPIENT, radiation, UGS.

### P14 — Rich management concerns should be decomposable rather than one generic status/configuration bucket

Potential dimensions include:
- configuration;
- condition/health;
- diagnostics/BIT;
- availability;
- software/firmware;
- power;
- communications;
- security state.

Supported by Redfish, OPC, MIMOSA, OSUS, ISA, NIST, LwM2M, Open Group SOSA and UGS.

### P15 — Derived information should preserve evidence relationships and should not erase the source observations/data products

Supported by MIMOSA, radiation, SAPIENT fusion, PROV, OMS/SOSA.

### P16 — Common anatomy should support specialization/optional aspect structures rather than making every concern mandatory for every System

Supported by AAS aspect pattern, NIEM augmentation/profile pattern, OPC companion specifications, atomic BME280, radiation, UGS, SWEET, SensorML atomic/aggregate distinction.

---

# 10. Phase B conclusion

Phase B does **not** support returning to the Version 1 eight information subjects as a ready-made taxonomy.

The donor evidence instead converges first on a set of **semantic separations and relationship rules**:

- persistent subject vs model vs representation;
- physical composition vs other topologies;
- capability vs configuration vs current state vs execution/result;
- static description vs dynamic evidence/action;
- property meaning vs value;
- observation act vs result;
- raw evidence vs analysis/assessment;
- host/deployment context vs intrinsic composition;
- current state vs history;
- physical subject vs virtual/interface representation;
- scoped identity/provenance;
- specialization/optionality across atomic and composite equipment.

These distinctions are stronger and more cross-community than any single donor's package/tab/module names.

**Disposition: Phase B COMPLETE.**

The sixteen propositions in Section 9 are **eligible for Phase C consideration**. They are not yet adopted V2 anatomy. Phase C must determine which propositions imply:

- core concepts/relationships;
- cross-cutting semantic structures;
- optional/aspect structures;
- specialization hooks; or
- concerns that should remain outside the common DIM.

The clean V2 DIM remains unchanged.
