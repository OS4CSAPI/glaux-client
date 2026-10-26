# DIM/Profile V2 Anatomy — Phase D Validation and Falsification

**Working draft v0.1 — 26 October 2026**  
**Status:** Phase D complete. Candidate anatomy validated with refinements; promotion decision recorded at the end.  
**Controlling continuity:** PITON_DIM_Profile_V2_Continuity_v1.1_26OCT2026.md  
**Inputs:** completed Phase A extraction, Phase B comparison, and Phase C candidate structure.

## 1. Validation purpose

Phase D attempts to falsify the Phase C candidate across structurally different cases rather than asking whether each source can merely be mapped into it.

The challenge set spans:

1. atomic sensing product — Bosch BME280;
2. composite installed system — radiation portal/instrument family;
3. complex modular defense sensor — Open Group SOSA;
4. distributed/remote UGS — TRSS/OmniSense;
5. industrial device/digital-twin family — OPC UA Devices/PA-DIM/AAS;
6. virtual/mediated participants — ISA/SAPIENT/WoT/LwM2M;
7. formal observation semantics — OMS/SOSA/SSN/I-ADOPT;
8. lifecycle/assessment-heavy model — MIMOSA;
9. operational whole-device implementation — OSUS;
10. intended OGC binding environment — CSAPI/SensorML;
11. network/power cross-cutting models — IETF topology/EMAN;
12. provenance/derived-information model — W3C PROV.

A candidate passes only when it preserves source-native distinctions without requiring the source to be distorted into the candidate organization.

---

# 2. Stress-test matrix

| Challenge case | Persistent subject spine | Context / typed relationships | Dynamic activity / evidence | Cross-cutting qualification | Optional aspects / specialization | Result |
| --- | --- | --- | --- | --- | --- | --- |
| **Atomic BME280** | One product/System works without separate component resources | Host/application can remain external | measurement/status/configuration changes fit | product/model/calibration/time qualify facts | power/interface/configuration can stay lightweight | **PASS** — proves optional decomposition |
| **Radiation portal** | Whole instrument supports multiple detectors/components | site/lane/host vehicle remain contextual | spectra/counts/status/analysis/alarm separate | detector/calibration/time/source traceability fits | radiation vocabulary remains specialization | **PASS** |
| **Open Group SOSA** | Whole Sensor + Components + products fit | Host Platform separate | mission data, management state, BIT/fault fit | multiple identity/topology roles need qualification | management/comms/power/software are rich overlays | **PASS WITH REFINEMENT** — add function-realization relationship |
| **UGS TRSS/OmniSense** | persistent device + optional detector/transducer works | emplacement/network/cue relations stay outside part-of | status/detection/image/command/config history fit | field-level source/time/authority essential | vendor states/config remain specialization | **PASS WITH REFINEMENT** — configuration authority/state needs explicit separation |
| **OPC/PA-DIM/AAS** | Device/Asset + model/type + component structure fits | network/manager/site stay relational | process signals/health/conditions/actions fit | semantic dictionaries/IDs/version fit | functional groups/submodels behave as aspects/views | **PASS WITH REFINEMENT** — aspect overlays should not be peer layer |
| **ISA/SAPIENT/WoT/LwM2M** | physical subject can remain separate from interface participant | mediation/gateway/network/virtual representation fit typed relations | status/events/tasks/resources/interactions fit | protocol/resource IDs separated from physical identity | native protocol hierarchies remain specializations | **PASS** |
| **OMS/SOSA/I-ADOPT** | equipment spine is external but compatible | Host/Deployment/FOI relationships fit | observation/execution/result patterns fit | property/variable/time/provenance semantics fit | observation semantics remain cross-cutting | **PASS WITH REFINEMENT** — product model vs Procedure must not be conflated |
| **MIMOSA** | Asset/model/component fits | Segment/Site/owner context fits | measurement→assessment→recommendation→work fits | source/time/agent/quality fits | lifecycle/maintenance rich aspect extends events | **PASS** |
| **OSUS** | whole Asset + type + internal sensor identity fits | platform pose/context fits | observation/status/BIT/command response fit | automatic source identity fits | operational management is optional rich aspect | **PASS** |
| **CSAPI/SensorML** | System + typeOf/systemKind + composition fits | Deployment/Platform/FOI fit | streams/observations/commands/events fit | semantic properties/time/UID fit | SensorML description/config/history can realize common semantics | **PASS WITH REFINEMENT** — distinguish model/kind from Procedure/method |
| **IETF topology/EMAN** | no need to become whole-system root | network and power relationships fit | counters/power/energy/state fit | measurement method/accuracy/identity fit | communications and power clearly cross-stratum aspects | **PASS WITH REFINEMENT** |
| **PROV** | domain subject remains external | Agent/responsibility relationships fit | provenance Activities/history/derivation fit | provenance is inherently cross-cutting | derived-information relationship is sufficient without universal assessment class | **PASS** |

**Overall result:** no challenge case falsifies the candidate anatomy. Several cases require refinement of the Phase C organizational wording and relationship taxonomy.

---

# 3. Refinement D1 — four core structural strata plus aspect overlays

## Finding

Phase C described five structural kinds, including Optional Technical / Management Aspects as the fifth kind.

The stress tests show that this is misleading.

Power, communications, condition/health, software and maintenance can each contain:

- persistent description;
- contextual relationships;
- dynamic information/events;
- provenance/qualification.

They therefore **cross the other structural strata** rather than sit beside them as a fifth peer layer.

## Validated organization

The candidate is refined to:

### Core structural stratum A — Persistent Subject Spine

What the System is, its reusable descriptions, enduring structure, functions/capabilities and configuration semantics.

### Core structural stratum B — Context and Typed Relationships

How the System is hosted, deployed, located, connected, powered, managed, grouped or otherwise situated relative to external subjects.

### Core structural stratum C — Dynamic Activity and Evidence

Observations, telemetry/state reports, commands/actions, events/history and derived information over time.

### Core structural stratum D — Cross-Cutting Qualification

Identity/reference, semantic definitions, time/validity, provenance/responsibility, units/quality, version/revision and bounded security/access metadata.

### Aspect overlays

Optional rich structures such as:

- condition/health/diagnostics;
- communications/network;
- power/energy;
- software/firmware/computational participation;
- maintenance/service/lifecycle.

An aspect can contribute content to more than one core stratum.

### Disposition

**REFINE / PASS.**

This organization survives all stress cases better than a five-peer-layer model.

---

# 4. Refinement D2 — Product/Model/Kind must be separated from Procedure/Method

## Finding

Phase C grouped "kind/model/procedure association" too loosely.

The formal semantic sources show that these are not universally equivalent:

- MIMOSA Model/Revision/Variant describes product/model identity.
- SAREF DeviceKind is an archetype of Devices.
- WoT Thing Model describes common interface metadata/capabilities.
- SensorML typeOf can relate a specific process to a general process.
- SOSA/OMS Procedure describes how an execution/observation is carried out.
- CSAPI systemKind uses Procedure as the reusable description of a system kind, creating a binding-specific relationship that must be mapped carefully.

## Validated distinction

The Persistent Subject Spine should support **two different reusable-description roles**:

### A. Product/model/kind relationship

Describes what reusable equipment/product/system kind the instance belongs to.

### B. Procedure/method relationship

Describes how a function/observation/process is carried out.

Some standards may encode these through one source construct or link one to the other, but V2 must not assume they are semantically identical.

### Disposition

**REFINE / PASS.**

---

# 5. Refinement D3 — Function, Capability, Procedure and Command are separate

## Finding

No challenge supports one universal Capability object that absorbs all behavior semantics.

Cross-source evidence instead supports four distinct meanings:

1. **Function** — what role/behavior is performed.
2. **Capability** — potential/performance/conditions under which something can be performed or produced.
3. **Procedure/Method** — how the behavior/observation is implemented/carried out.
4. **Command/Action definition** — externally requestable behavior.

## Validated candidate structure

Common anatomy should provide:

- functional description of the System;
- typed capability/performance relationships where applicable;
- Procedure/Method association;
- action/command description separate from actual execution.

Source-owned capability models can remain specializations.

## New relationship need

Phase D adds a candidate relationship role:

> **function/capability realized or implemented by component/System**

Evidence:
- SNRA physical ↔ functional entity mapping;
- AAS Capability ↔ Skill;
- Open Group SOSA functional Component ↔ Product/Module realization;
- SAREF FunctionOfInterest ↔ Device;
- SensorML ProcessMethod/process/components.

### Disposition

**REFINE / PASS.**

---

# 6. Refinement D4 — Configuration has design-time, requested and effective forms

## Finding

UGS, ISA, SensorML and OPC demonstrate that "configuration" is not one state.

The following can differ:

- allowed configuration space;
- stored/engineering configuration;
- requested/queued configuration;
- current/effective configuration;
- device-reported/applied configuration;
- historical configuration event.

## Validated candidate structure

### Persistent Subject Spine

Contains:
- configuration schema/allowed options;
- named modes;
- relatively stable instance settings where appropriate.

### Dynamic Activity/Evidence

Contains:
- requested/staged change;
- execution/application status;
- reported/effective configuration;
- change event/history.

### Cross-Cutting

Contains:
- source/authority;
- time;
- version.

### Disposition

**REFINE / PASS.**

This is required to avoid the exact false equivalence exposed by OmniSense/TRSS.

---

# 7. Refinement D5 — Common reported-state pattern, not common universal status enum

## Finding

State/condition survives every equipment stress case, but source dimensions conflict.

Examples include:

- operating state;
- mode;
- health;
- condition;
- fault;
- availability;
- alarm;
- BIT result;
- configuration state;
- power state;
- security state;
- lifecycle status.

## Validated common minimum

V2 should support a **typed reported-state fact pattern** with at least:

- affected subject;
- state/condition semantic definition;
- value/status;
- time/validity;
- source/provenance;
- quality/confidence where applicable.

Richer aspects can then standardize:
- health;
- diagnostics;
- BIT;
- faults;
- power;
- communications;
- cybersecurity.

## Explicit rejection

Do **not** create one universal:
- Status enum;
- Health enum;
- Readiness score.

### Disposition

**REFINE / PASS.**

---

# 8. Refinement D6 — Event/history backbone survives, but event type must stay open

## Finding

A common Event/history structure successfully accommodates:

- configuration change;
- calibration;
- software/firmware update;
- part replacement;
- deployment/relocation;
- maintenance/service;
- operator handoff;
- fault occurrence/clear;
- work action.

It does not need to absorb:
- LwM2M registration state machine;
- ISA/SAPIENT connection lifecycle;
- command execution status;
- observation/sampling events

as one universal lifecycle.

## Validated minimum Event semantics

- event identity/type;
- affected subject(s);
- event time/interval;
- responsible/source actor;
- related Deployment/configuration when relevant;
- related evidence/artifact;
- before/after or changed values where available.

Specialized event taxonomies remain source/profile owned.

### Disposition

**PASS.**

---

# 9. Refinement D7 — communications and power are common relations plus aspect overlays

## Communications

Stress testing confirms that:

- interface identity;
- connection point;
- network/link;
- gateway/controller/manager;
- communication state/metrics

should not become the physical component tree.

### Validated standing

- common typed connectivity/interface relationships;
- optional rich communications aspect.

## Power

Stress testing confirms that:

- power source;
- consumer;
- power interface;
- design/nameplate characteristics;
- live measurements;
- battery state/history

cross persistent/context/dynamic structures.

### Validated standing

- common power-source/consumer relationship;
- optional rich power/energy aspect.

### Disposition

**PASS with D1 structural refinement.**

---

# 10. Refinement D8 — Derived information needs common provenance support, not a universal Assessment class

## Finding

Derived/fused/assessed information is real across:

- MIMOSA;
- radiation;
- SAPIENT;
- PROV;
- UGS;
- sensing analytics.

But forcing every System to implement a common Assessment hierarchy would over-generalize.

## Validated common pattern

The common DIM should permit a typed **derived information/product** to retain:

- product/result identity;
- producing System/Activity/Procedure;
- source evidence;
- derivation relationship;
- time;
- responsible actor;
- domain-specific type.

Specializations may define:
- health assessment;
- prognosis;
- track;
- classification;
- alarm;
- recommendation;
- report.

### Disposition

**REFINE / PASS.**

No universal mandatory Assessment class is adopted.

---

# 11. Refinement D9 — minimum security/access semantics remain cross-cutting

## Finding

Security is structurally present in NIST, ISA, WoT, LwM2M, IEEE, NIEM and defense contexts, but the common DIM should not become an authorization system.

## Validated common boundary

The common DIM may carry or reference:

- classification/marking;
- access/handling constraints;
- interface security characteristics;
- security-state facts;
- relevant policy/profile reference.

Outside common DIM:

- credentials;
- keys;
- authentication sessions;
- enterprise IAM;
- enforcement implementation.

### Disposition

**PASS with bounded scope.**

---

# 12. Refinement D10 — location must be role/time/source qualified

## Finding

Location cannot be forced entirely into Deployment.

Examples:

- fixed equipment may have intrinsic/installation location;
- mobile equipment has changing current location;
- SensorML has local/external reference frames;
- UGS can have entered location and device GPS with different authority;
- detection/target location is distinct from sensor location;
- MIMOSA functional location is distinct from Asset identity;
- Deployment can have its own area/location.

## Validated rule

A location/pose fact must identify:

- what subject it describes;
- semantic role;
- time/validity where relevant;
- source/provenance;
- reference frame/CRS.

Deployment is one contextual owner of location, not the universal owner of every location fact.

### Disposition

**REFINE / PASS.**

---

# 13. Refinement D11 — internal components can remain non-resource-like until meaningful

## Finding

BME280 proves that real internal functions/components need not all deserve independent managed identity.

SOSA, OPC, radiation and UGS prove that some components absolutely do.

## Validated representation rule

Represent an internal element as an independently identified Component/System when one or more of the following materially matters:

- independent identity;
- independent configuration;
- independent state/health;
- independent calibration;
- independent output/action;
- independently replaceable/serviceable role;
- meaningful relationship to other elements.

Otherwise, source-defined structured description can remain embedded under the whole System.

### Disposition

**PASS.**

This prevents fabricated component trees while supporting rich systems.

---

# 14. Refinement D12 — relationship taxonomy expanded and validated

The Phase C relationship taxonomy survives with one important addition and one qualification.

## Validated common relationship roles

1. reusable product/model/kind relationship;
2. Procedure/Method relationship;
3. enduring part/subsystem;
4. hosted/carried by;
5. deployed/assigned in;
6. connected via / connected to;
7. supplied by / power relation;
8. managed by;
9. represented/exposed by;
10. mediated by;
11. observes / controls / targets;
12. produced/generated by;
13. derived from / supported by evidence;
14. responsible/attributed to;
15. **function/capability realized/implemented by**.

## Specialization-level relationship

- triggered/cued by.

This remains valuable for UGS and some sensing networks but is not yet strong enough to require common-core standing.

### Disposition

**REFINE / PASS.**

---

# 15. Formal-semantic mapping validation

The refined anatomy can map to the intended semantic/binding families without requiring identity between their classes.

## SOSA/SSN

Supports:
- System;
- Sensor role;
- Procedure;
- Execution;
- Observation;
- Platform;
- Deployment;
- FeatureOfInterest;
- Property.

Does **not** by itself supply:
- physical equipment identity/nameplate;
- rich configuration;
- condition/health;
- power;
- communications.

The V2 anatomy can reuse SOSA/SSN semantics without requiring every V2 System to be asserted directly as sosa:Sensor.

## OMS

Supports:
- Observation;
- Observer;
- Host;
- Deployment;
- ObservingProcedure;
- ObservableProperty;
- Result;
- capability;
- sampling chain.

Fits the Dynamic Evidence and Context strata without replacing the equipment spine.

## I-ADOPT

Supports semantic decomposition of Variables within cross-cutting qualification.

## SAREF

Validates:
- DeviceKind vs Device;
- Function/Command/Execution;
- Service/Operation separation;
- Property/State/value separation.

## PROV

Validates cross-cutting provenance and derived-information relationships.

### Result

**PASS.**

No ontology requires the V2 DIM to collapse into that ontology's class hierarchy.

---

# 16. OGC binding validation

The refined anatomy maps cleanly to CSAPI/SensorML without treating API carriers as domain truth.

## Persistent subject

- CSAPI System;
- SensorML DescribedObject/AbstractProcess/physical process encodings as appropriate.

## Reusable kind/model/procedure

- CSAPI systemKind / Procedure;
- SensorML typeOf/general process;
- additional model/product semantics may require a profile mapping distinct from Procedure.

## Composition

- CSAPI subsystem/Composition for enduring subordinate Systems;
- SensorML components for richer process/system decomposition.

## Context

- CSAPI Deployment;
- Platform;
- SensorML Deployment/DeployedSystem;
- feature/target links.

## Dynamic evidence

- DataStream/Observation;
- ControlStream/Command/Status/Result;
- SystemEvent.

## Cross-cutting

- Property semantics;
- identifiers;
- time/validity;
- provenance/profile conventions.

## Important binding caution

The refined distinction between **product model/kind** and **Procedure/method** means CSAPI systemKind alone may not carry every product-model use case. That must be handled explicitly in the later profile/binding design rather than by overloading Procedure.

### Result

**PASS WITH BINDING NOTE.**

---

# 17. Version 1 regression test

The candidate does **not** reproduce the Version 1 eight subjects.

Why:

- organization begins from semantic strata and relationship types, not eight inherited headings;
- communications, power, condition and maintenance are aspect overlays rather than predetermined peer modules;
- observation/action/event are dynamic structures, not forced into a single operational module;
- provenance/identity/time/semantics are cross-cutting rather than separate silos;
- deployment/host/network relations are typed context rather than one catch-all operational group;
- component depth is optional and scale-sensitive;
- specialization hooks remain external to the common core.

### Result

**PASS.**

---

# 18. Phase D answers to the twelve required questions

| Question | Result | Refinement |
| --- | --- | --- |
| 1. Is the organizational shape stable? | **PASS WITH REFINEMENT** | four core strata + aspect overlays, not five peer layers |
| 2. Common Function/Capability? | **PASS WITH REFINEMENT** | separate Function, Capability, Procedure/Method and Command; source-owned detail allowed |
| 3. Common state/condition depth? | **PASS WITH REFINEMENT** | typed reported-state fact pattern; no universal status enum |
| 4. Event/history backbone sufficient? | **PASS** | common event minimum + specialized process lifecycles |
| 5. Communications/power placement correct? | **PASS** | common relationship hooks + optional rich overlays |
| 6. Common derived information needed? | **PASS WITH REFINEMENT** | common derived-product provenance pattern; no universal Assessment class |
| 7. Minimum security/access semantics? | **PASS** | bounded cross-cutting metadata/reference only |
| 8. Relationship taxonomy covers stress cases? | **PASS WITH REFINEMENT** | add function/capability realization relation; cue/trigger stays specialization |
| 9. Components may remain non-resource-like? | **PASS** | represent separately only when independent semantics matter |
| 10. OGC/SOSA/OMS mapping without conflation? | **PASS WITH NOTE** | product model/kind vs Procedure requires explicit binding treatment |
| 11. Specializations can extend common structure? | **PASS** | no chassis fork required |
| 12. Version 1 structure recreated? | **PASS** | candidate organization is materially different |

---

# 19. Validated candidate V2 anatomy

After Phase D, the candidate anatomy is refined to:

## A. Persistent Subject Spine

Common:
- persistent System identity;
- product/model/kind association;
- Procedure/Method associations where applicable;
- optional enduring decomposition;
- Function/Capability description;
- configuration schema/modes and effective settings.

## B. Context and Typed Relationships

Common relationship capacity for:
- Deployment/emplacement;
- Host/Platform;
- location/pose with role/time/source;
- communications/connectivity;
- power-source;
- manager/responsibility;
- representation/mediation;
- target/FeatureOfInterest.

## C. Dynamic Activity and Evidence

Common:
- Observation/measurement/detection;
- typed reported-state facts;
- Command/action/task request, execution status and result;
- Event/history;
- optional derived information/products with provenance.

## D. Cross-Cutting Qualification

Common:
- scoped identity/reference;
- semantic definitions / Property / Variable meaning;
- units/constraints/quality;
- time/validity;
- provenance/source/responsibility;
- version/revision;
- bounded security/access metadata.

## Aspect overlays

Optional rich reusable aspects:
- condition/health/diagnostics;
- communications/network;
- power/energy;
- software/firmware/computational participation;
- maintenance/service/asset lifecycle.

## Specialization hooks

Domain/profile-specific:
- radiation;
- UGS;
- scientific instrument classes;
- IEEE smart-transducer structures;
- industrial automation;
- protocol/device-ecosystem-specific structures;
- other future sensing modalities.

---

# 20. Phase D disposition

**Disposition: PHASE D PASSED WITH REFINEMENTS.**

No stress case falsified the candidate anatomy.

The refinements are substantive but controlled:

1. optional aspects are overlays across four core strata;
2. product/model/kind is separated from Procedure/Method;
3. Function, Capability, Procedure and Command are kept distinct;
4. configuration is split into allowed/stored/requested/effective/history semantics;
5. reported state uses typed/source-qualified facts rather than one status enum;
6. function/capability realization is added to relationship taxonomy;
7. location is role/time/source qualified;
8. derived information uses common provenance support without a universal Assessment class.

The validated anatomy is now eligible for **working-decision promotion** into the maintained clean V2 artifact.

No machine-readable profile/binding/conformance design is authorized by this decision.
