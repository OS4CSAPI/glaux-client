# DIM/Profile V2 Anatomy — Phase C Candidate Structure

**Working draft v0.1 — 26 October 2026**  
**Status:** Candidate V2 anatomy proposed from completed Phase A/B evidence. **Not yet validated or promoted into the clean DIM.**  
**Controlling continuity:** PITON_DIM_Profile_V2_Continuity_v1.0_26OCT2026.md  
**Evidence basis:** 30-lineage Phase A extraction + Phase B cross-source comparison.

## 1. Purpose

Phase C asks which of the sixteen Phase B propositions justify:

- common concepts and relationships;
- cross-cutting semantic structures;
- optional/aspect structures;
- specialization hooks; or
- concerns that should remain outside the common DIM.

The candidate below deliberately avoids copying one donor's package/module tree and does not resurrect the Version 1 eight-subject structure.

The working chassis remains:

> **physically realized equipment Systems whose defining operational role is sensing/observing, modeled as complete operational subjects.**

The candidate anatomy is therefore an organization **around that persistent System**, not a replacement chassis.

---

# 2. Candidate organizational shape

The evidence does not support one flat list of peer modules. It supports a **layered/aspect-oriented organization** with five kinds of structure:

1. **Persistent Subject Spine**
2. **Context and Relationship Structure**
3. **Dynamic Activity and Evidence Structure**
4. **Cross-Cutting Qualification Structure**
5. **Optional Technical / Management Aspects**

These are working organizational labels only. They are **not new domain classes** and are not final publication/module names.

Specializations then extend the common anatomy without requiring every System to support every domain-specific structure.

---

# 3. Candidate Persistent Subject Spine

The Persistent Subject Spine describes what the sensing System **is**, what reusable model/kind it follows, what it is durably made of when decomposition is meaningful, what it is capable of, and how it is configured.

## 3.1 Persistent System identity

### Candidate content

- persistent System identifier;
- human-readable name/description;
- classification as sensing-role physical Equipment through the chassis;
- product/manufacturer/model/serial/revision identifiers when applicable;
- distinction among domain identity, binding/resource ID and externally assigned identifiers.

### Evidence basis

Phase B:
- P01, P11, P12.

Representative lineages:
- CSAPI;
- AAS;
- MIMOSA;
- OPC/PA-DIM;
- Redfish/CIM;
- OSUS;
- SAREF;
- SensorML;
- LwM2M;
- WoT;
- UGS.

### Candidate disposition

**Common/core.**

Every represented System needs a stable subject identity even if it has no rich component tree or management interface.

---

## 3.2 Reusable kind / model / procedure association

### Candidate content

A System can relate to a reusable description of what kind/model/procedure it implements, without copying all model-level information into the instance.

Potential source-owned forms include:
- Procedure/systemKind;
- SensorML typeOf/general process;
- DeviceKind;
- product Model/Revision/Variant;
- Thing Model;
- AAS type/instance structures.

### Evidence basis

Phase B:
- P01, P16.

Representative lineages:
- CSAPI;
- SensorML;
- MIMOSA;
- SAREF;
- WoT;
- AAS;
- OPC;
- JC3IEDM.

### Candidate disposition

**Common/core relationship.**

The exact reusable-description representation remains open to Phase D/binding selection.

---

## 3.3 Enduring internal structure

### Candidate content

Support explicit representation of internal elements when they are meaningful to users/integration, while not requiring every internal function/block to become an independently addressable resource.

The candidate distinguishes:

- **subordinate Systems** that merit full System identity; and
- **non-System components/elements/channels** whose information may be represented more locally.

The relationship must express **enduring/intrinsic composition**, not temporary attachment, network connectivity, host placement or cueing.

### Evidence basis

Phase B:
- P02, P03.

Representative lineages:
- CSAPI;
- SensorML;
- OPC;
- AAS;
- Open Group SOSA;
- RFC 8348;
- IEEE 1451;
- OSUS;
- radiation;
- UGS;
- BME280.

### Candidate disposition

**Common/core relationship with optional decomposition depth.**

Atomic equipment may legitimately have no separately represented component resources.

---

## 3.4 Functional / capability description

### Candidate content

The System needs a way to describe **what it can do**, but Phase B does not justify one universal capability payload.

Candidate common semantics should support:

- one or more functions/roles performed by the System;
- supported observable/controllable properties or outputs/actions;
- performance/capability descriptions where applicable;
- constraints/conditions;
- relationships to the components/elements that realize a function when known.

Source-owned capability models may remain specialized.

### Evidence basis

Phase B:
- P04, P06, P16.

Representative lineages:
- AAS;
- ISA;
- SAPIENT;
- SensorML;
- SAREF;
- SNRA;
- Open Group SOSA;
- IEEE 1451;
- OSUS;
- Matter.

### Candidate disposition

**Common/core relationship and concept family; payload semantics remain partially source-owned.**

### Explicit non-decision

Phase C does **not** adopt one universal Capability class or assert that all AAS/ISA/SAPIENT/SAREF capability terms are equivalent.

---

## 3.5 Configuration, operating modes and selected settings

### Candidate content

Distinguish:

- supported configuration space;
- named modes/options;
- selected/current settings;
- requested/staged settings;
- applied/reported settings where those states are available;
- configuration validity/version.

### Evidence basis

Phase B:
- P04, P05, P09, P14.

Representative lineages:
- SensorML;
- ISA;
- SAPIENT;
- Matter;
- OPC;
- Redfish;
- BME280;
- UGS;
- LwM2M.

### Candidate disposition

**Common structural concern; optional depth.**

A simple sensor may expose only a few settings. Complex equipment may expose structured modes/configurations.

---

# 4. Candidate Context and Relationship Structure

This structure describes **how the persistent System is situated, hosted, connected, employed or related**, without rewriting context as intrinsic composition.

## 4.1 Deployment / emplacement / operational use

### Candidate content

Relate the System to:

- Deployment/emplacement;
- time period;
- location/area/pose appropriate to the deployment;
- purpose/role/mission context where sourced;
- deployment-specific configuration;
- participating/associated Systems.

### Evidence basis

Phase B:
- P03, P09, P13.

Representative lineages:
- CSAPI;
- SensorML;
- SOSA/SSN;
- OMS;
- MIMOSA;
- Open Group SOSA;
- UGS;
- radiation.

### Candidate disposition

**Common contextual structure.**

Deployment is not part of persistent physical composition by default.

---

## 4.2 Host / Platform relationship

### Candidate content

Represent the entity that hosts/carries/mounts the sensing System when applicable.

Host/Platform remains distinct from:
- the Sensor/System;
- an internal component;
- the Deployment relationship.

### Evidence basis

Phase B:
- P03, P13.

Representative lineages:
- SOSA/SSN;
- Open Group SOSA;
- OMS;
- SensorML;
- SAPIENT;
- CSAPI;
- UGS;
- radiation.

### Candidate disposition

**Common typed relationship.**

---

## 4.3 Communications / connectivity relationship

### Candidate content

Common anatomy should be able to relate:

- System/component;
- communication interface/connection point;
- network/link/peer;
- manager/controller/gateway where applicable.

The common DIM should not absorb a full network-management topology unless needed by the application/profile.

### Evidence basis

Phase B:
- P03, P12, P14, P16.

Representative lineages:
- OPC;
- IETF interfaces/topology;
- Redfish;
- IEEE 1451;
- SNRA;
- SAPIENT;
- LwM2M;
- UGS.

### Candidate disposition

**Common relationship hooks + optional rich communications aspect.**

---

## 4.4 Power-source / energy relationship

### Candidate content

Support typed relationships between:

- consuming System/component;
- internal or external power source;
- relevant power interface;
- source-specific/static characteristics;
- dynamic measurements/state where available.

### Evidence basis

Phase B:
- P03, P14, P16.

Representative lineages:
- EMAN;
- Redfish;
- Open Group SOSA;
- SNRA;
- BME280;
- UGS;
- OPC.

### Candidate disposition

**Common relationship hook + optional rich power/energy aspect.**

A complete EMAN-style energy model is not mandatory for every sensor.

---

## 4.5 Organization / responsibility / management relationships

### Candidate content

Relate the System or event/fact to:

- owner;
- operator;
- responsible organization/person/agent;
- manager/controller;
- support contact;
- information source.

### Evidence basis

Phase B:
- P10, P11, P13.

Representative lineages:
- PROV;
- MIMOSA;
- ISA;
- Redfish;
- NIEM;
- JC3IEDM;
- SensorML;
- UGS.

### Candidate disposition

**Common relationship semantics, largely cross-cutting rather than a peer equipment module.**

---

# 5. Candidate Dynamic Activity and Evidence Structure

Dynamic structures represent what the System **observes, reports, does, experiences, or produces over time**.

## 5.1 Observation / measurement / detection

### Candidate content

Preserve the distinction among:

- observable/variable/property meaning;
- observation/execution act where applicable;
- source System / internal channel;
- feature/subject of interest;
- procedure/method;
- time;
- result/value;
- result quality;
- stream/channel/grouping.

### Evidence basis

Phase B:
- P05, P06, P07, P10, P11.

Representative lineages:
- OMS;
- SOSA/SSN;
- CSAPI;
- SensorML/SWE;
- I-ADOPT;
- IEEE 1451;
- OSUS;
- radiation;
- UGS.

### Candidate disposition

**Common dynamic structure.**

The exact OGC realization is a later binding decision.

---

## 5.2 Current telemetry / reported state

### Candidate content

Allow time-varying reported facts about the System/components, while preserving typed dimensions such as:

- operating state;
- mode;
- health;
- condition/fault;
- availability;
- diagnostic/BIT state;
- power state;
- communications state;
- security state.

Do not force all source-specific state into one universal enum.

### Evidence basis

Phase B:
- P04, P05, P09, P14.

Representative lineages:
- Redfish;
- RFC 8348;
- OPC;
- Open Group SOSA;
- OSUS;
- ISA;
- SAPIENT;
- NIST;
- UGS;
- EMAN.

### Candidate disposition

**Common dynamic pattern with typed/source-owned dimensions.**

### Explicit non-decision

No universal readiness/health score is adopted.

---

## 5.3 Command / action / task interaction

### Candidate content

Preserve:

- available/supported action or command semantics;
- request/task instance;
- target;
- parameters;
- execution status/progress;
- result;
- failure/rejection reason;
- linkage to resulting observations/events where applicable.

### Evidence basis

Phase B:
- P04, P05, P08, P10.

Representative lineages:
- CSAPI;
- ISA;
- SAPIENT;
- OSUS;
- Matter;
- SAREF;
- WoT;
- AAS.

### Candidate disposition

**Common dynamic structure.**

---

## 5.4 Event / history

### Candidate content

Provide a general history/event backbone for significant changes/actions such as:

- configuration changes;
- calibration;
- maintenance/service;
- software/firmware update;
- part replacement;
- deployment/relocation;
- ownership/operator handoff;
- fault occurrence/clearing;
- other source-defined events.

Each event should retain:
- affected subject(s);
- time;
- responsible/source agent where known;
- related evidence;
- changed configuration/state where available.

### Evidence basis

Phase B:
- P09, P10, P15.

Representative lineages:
- CSAPI SystemEvent;
- SensorML Event;
- MIMOSA;
- PROV;
- Redfish;
- OPC;
- UGS.

### Candidate disposition

**Common history/event structure.**

### Important limit

Specialized process lifecycles such as LwM2M registration or SAPIENT connection lifecycle remain specialized; they may generate Events without redefining the common event taxonomy.

---

## 5.5 Derived information / analysis / assessment

### Candidate content

Support derived information that remains linked to source evidence, such as:

- assessment;
- classification;
- fused track/product;
- alarm;
- prognosis;
- recommendation;
- processed information artifact.

Common semantics should emphasize:
- provenance;
- source observations/products;
- procedure/activity;
- responsible agent/system;
- result/product identity;
- revision/derivation.

### Evidence basis

Phase B:
- P07, P10, P15, P16.

Representative lineages:
- MIMOSA;
- radiation;
- SAPIENT;
- PROV;
- SOSA/OMS;
- UGS.

### Candidate disposition

**Optional common pattern / specialization hook.**

### Explicit non-decision

No mandatory universal Analysis or Assessment module is adopted. Specific assessment/alarm/fusion semantics remain specialization-owned unless Phase D establishes broader need.

---

# 6. Candidate Cross-Cutting Qualification Structure

These semantics qualify multiple areas and should not be trapped inside a single peer module.

## 6.1 Identity and reference

Candidate semantics include scoped identity for:

- System/equipment;
- reusable model/kind;
- component/channel;
- binding/API resource;
- message/observation/command/event;
- target/feature;
- semantic term/property;
- external artifact.

**Evidence:** P01, P11, P12; nearly all lineages.

---

## 6.2 Provenance, source and responsibility

Candidate semantics include:

- generated/provided by;
- derived from;
- used as evidence/input;
- responsible agent/organization;
- source authority;
- method/procedure;
- revision/alternate representation where relevant.

**Evidence:** P10, P15; PROV, MIMOSA, OMS/SOSA, OSUS, ISA, UGS, radiation.

---

## 6.3 Time and validity

Candidate semantics distinguish where applicable:

- description validity;
- phenomenon/observation time;
- result time;
- event time;
- execution start/end;
- deployment interval;
- configuration effective time;
- retrieval/report time.

**Evidence:** OMS, SOSA, SensorML, CSAPI, MIMOSA, PROV, ISA, UGS.

---

## 6.4 Semantic definitions, units, constraints and quality

Candidate semantics include:

- Property / Variable / ObservableProperty meaning;
- feature/object/context qualifiers;
- units;
- ranges;
- constraints;
- quality/uncertainty;
- statistical modifier where applicable;
- semantic identifiers/dictionary references.

**Evidence:** P06, P07; I-ADOPT, OMS, SOSA/SSN, SAREF, CSAPI, AAS, OPC, IEEE 1451, radiation.

---

## 6.5 Version / revision

Candidate semantics should preserve version/revision for:

- model/kind;
- System description;
- firmware/software;
- configuration;
- external artifacts;
- source standard/profile where relevant.

**Evidence:** AAS, MIMOSA, OPC, Redfish, SensorML, IEEE, LwM2M, NIEM.

---

## 6.6 Security / access qualification

Candidate common semantics may identify:

- security classification/marking where applicable;
- interface security characteristics;
- access/authorization constraints;
- security state references.

Credentials, keys and enterprise authorization infrastructure remain outside common DIM content.

**Evidence:** P14, P16; NIST, ISA, LwM2M, WoT, IEEE, NIEM/JC3IEDM.

### Candidate disposition

**Cross-cutting, bounded common metadata; depth to validate in Phase D.**

---

# 7. Candidate Optional Technical / Management Aspects

These concerns recur enough to justify common extension points/aspect structures, but the evidence does not support requiring rich content for every System.

## 7.1 Condition / health / diagnostics

May include source-supported dimensions such as:

- operating state;
- health;
- fault/condition;
- diagnostics;
- BIT/self-test;
- availability;
- alarms;
- source-specific status.

**Candidate standing:** optional reusable aspect with typed/source-owned semantics.

**Do not:** collapse all dimensions into a universal status enum or readiness score.

---

## 7.2 Communications / network

May include:

- interfaces/connection points;
- protocol/communication profile;
- network/link relationships;
- peer/gateway/controller relationships;
- addresses/settings;
- communication condition/metrics.

**Candidate standing:** optional rich aspect; common relationship hooks are more fundamental than the full topology.

---

## 7.3 Power / energy

May include:

- source identity/type;
- internal/external/shared supply relationship;
- design/static characteristics;
- current voltage/current/power/energy;
- charge/capacity/state;
- source/metering provenance.

**Candidate standing:** optional rich aspect; common supplied-by/consumes-from relationships are more fundamental.

---

## 7.4 Software / firmware / computational participation

May include:

- software/firmware identity/version;
- hosted software/component relationship;
- algorithm/process identity where operationally relevant;
- current/pending/fallback version;
- update history.

**Candidate standing:** optional reusable aspect.

**Do not:** treat every algorithm implementation as an independently managed physical Component.

---

## 7.5 Maintenance / service / asset lifecycle

May include:

- inspection;
- calibration action;
- repair;
- replacement;
- service;
- work request/work result;
- decommission/recovery;
- lifecycle status.

**Candidate standing:** optional rich aspect built over the common Event/history spine.

MIMOSA-style enterprise maintenance depth is not mandatory for every V2 implementation.

---

# 8. Candidate Specialization Hooks

The common anatomy should allow specializations to add governed structures without altering the chassis.

Examples:

### Radiation specialization

- radiation quantities;
- detector response/calibration;
- spectra;
- alarms;
- radionuclide analysis;
- screening workflow.

### UGS specialization

- detector-slot semantics;
- cue/trigger relations;
- vendor operating states;
- sleep/tamper/recovery functions.

### Instrument/science specialization

- SWEET instrument classes;
- discipline-specific measured properties.

### IEEE smart-transducer specialization

- TIM/channel/TEDS structures;
- family-specific interface/service metadata.

### Protocol/device ecosystem specializations

- Matter Device Types/Clusters;
- LwM2M Objects;
- Redfish schema resources;
- PA-DIM device classes.

**Candidate rule:** specialization may refine/add domain semantics but should not require the common DIM to mirror its native transport/schema hierarchy.

---

# 9. Candidate Relationship Taxonomy

The strongest donor consensus is not on one class hierarchy but on keeping different relationship meanings distinct.

The following **relationship roles** are candidates for Phase D validation. Names are descriptive placeholders, not final property names.

| Candidate relationship role | Meaning to preserve | Principal evidence |
| --- | --- | --- |
| **kind/model relationship** | specific System → reusable model/kind/procedure | CSAPI, SensorML, MIMOSA, SAREF, WoT, AAS |
| **enduring part / subsystem** | intrinsic persistent composition | CSAPI, SensorML, OPC, AAS, Open Group SOSA, RFC8348 |
| **hosted/carried by** | physical hosting without asserting composition | SOSA/SSN, Open Group SOSA, OMS |
| **deployed/assigned in** | time/context-scoped operational association | CSAPI, SensorML, SOSA/SSN, MIMOSA, UGS |
| **connected via / connected to** | communications/interface/network relation | OPC, IETF topology, Redfish, IEEE, UGS |
| **supplied by / power relation** | power-source/consumer relation | EMAN, Redfish, Open Group SOSA, UGS |
| **managed by** | manager/controller responsibility | Redfish, OPC, ISA, UGS |
| **represented/exposed by** | logical/API/virtual representation of physical subject | AAS, WoT, ISA, LwM2M, Redfish |
| **mediated by** | intermediary/CIC/gateway/proxy relation | ISA, WoT, LwM2M |
| **observes / controls / targets** | relationship among System/function/action and target Property/Feature | SOSA/SSN, SAREF, OMS, CSAPI |
| **produced/generated by** | result/product/fact → source execution/System | OMS, SOSA, PROV, OSUS |
| **derived from / supported by evidence** | analysis/product/assessment → source evidence | PROV, MIMOSA, radiation |
| **responsible/attributed to** | fact/event/activity → Agent/organization | PROV, MIMOSA, NIEM |
| **triggered/cued by** | operational dependency between peer systems | UGS, SAPIENT | 

### Candidate disposition

The first twelve roles have strong common evidence.

Triggered/cued-by may remain a specialization relationship unless Phase D finds broader cross-domain need.

---

# 10. Candidate semantic invariants for the V2 anatomy

Any Phase D-validated anatomy should preserve these invariants:

1. The physical sensing System is not the same thing as its API/resource/digital representation.
2. A reusable model/kind is not the same thing as an individual System.
3. An internal sensing element/channel is not automatically a peer whole System.
4. Enduring physical composition is not the same as hosting, deployment, network connectivity, functional grouping or virtual mediation.
5. Supported capability is not current configuration.
6. Configuration is not current state/condition.
7. Current state is not event/history.
8. Action/command definition is not one execution/request.
9. Request is not execution status and not result.
10. Observable/property/variable meaning is not a particular value/result.
11. Observation/execution is not the same thing as its result.
12. Measurement/evidence is not the same thing as derived analysis/assessment.
13. Deployment/host/location context does not redefine persistent System identity.
14. Information provenance/source authority must remain explicit where facts can come from different sources.
15. Model/type IDs, equipment IDs, component IDs, resource IDs and data-item IDs must retain scope.
16. Atomic equipment must remain representable without fabricated component trees.
17. Composite equipment must allow rich decomposition without turning network/deployment peers into physical parts.
18. Specialization semantics must remain optional outside the specialization.
19. Security/transport/UI/storage implementation details must not silently become domain concepts.
20. Current CSAPI classification remains distinct from formal OWL class assertion unless explicitly mapped.

---

# 11. Concerns kept outside the common DIM

The following should remain outside common DIM semantics except for typed links/references where needed:

- HTTP/MQTT/SNMP/protobuf/native transport details;
- HLS/media transport mechanics;
- database tables/object-store paths;
- UI tab/layout/navigation behavior;
- browser caching/reconnect behavior;
- enterprise credential/key storage;
- authorization infrastructure implementation;
- proprietary analytics/algorithm internals;
- workflow engine implementation;
- report rendering;
- file-storage implementation;
- native vendor command wire formats;
- complete network-management topology where not required by the sensing-system use case.

A companion standard/contract may define these responsibilities.

---

# 12. Traceability from candidate structure to Phase B propositions

| Candidate structure | Phase B propositions | Representative supporting lineages |
| --- | --- | --- |
| Persistent System identity | P01, P11, P12 | CSAPI, AAS, MIMOSA, OPC, Redfish, SAREF, SensorML |
| Model/kind/procedure association | P01, P16 | CSAPI, SensorML, SAREF, MIMOSA, WoT, AAS |
| Optional enduring decomposition | P02, P03 | SensorML, OPC, AAS, CSAPI, SOSA, RFC8348, BME280 |
| Functional/capability description | P04, P06, P16 | AAS, ISA, SAPIENT, SensorML, SAREF, SNRA, IEEE |
| Configuration/modes/settings | P04, P05, P09, P14 | SensorML, ISA, SAPIENT, OPC, Matter, UGS |
| Deployment/context | P03, P09, P13 | CSAPI, SensorML, SOSA/SSN, OMS, MIMOSA, UGS |
| Host/Platform relation | P03, P13 | SOSA/SSN, Open Group SOSA, OMS, SAPIENT |
| Communications relationship/aspect | P03, P12, P14, P16 | OPC, IETF, Redfish, IEEE, SNRA, UGS |
| Power relationship/aspect | P03, P14, P16 | EMAN, Redfish, SOSA, SNRA, UGS |
| Observation/measurement | P05, P06, P07, P10 | OMS, SOSA, CSAPI, I-ADOPT, IEEE, radiation |
| Reported state/telemetry | P04, P05, P09, P14 | Redfish, OPC, RFC8348, OSUS, ISA, UGS |
| Command/action/task | P04, P05, P08, P10 | CSAPI, ISA, SAPIENT, OSUS, SAREF |
| Event/history | P09, P10, P15 | CSAPI, SensorML, MIMOSA, PROV |
| Derived information | P07, P10, P15, P16 | MIMOSA, radiation, SAPIENT, PROV |
| Provenance/responsibility | P10, P11, P15 | PROV, MIMOSA, OMS/SOSA, UGS, ISA |
| Property/variable semantics | P06, P07 | I-ADOPT, OMS, SOSA, SAREF, CSAPI |
| Optional/aspect mechanism | P02, P14, P16 | AAS, NIEM, OPC, SensorML, BME280, radiation, UGS |

---

# 13. Phase C unresolved decisions for Phase D challenge

Phase D must attempt to falsify/refine at least these candidate choices:

1. **Is the five-kind organizational shape genuinely stable** across atomic, composite, distributed and virtualized cases, or does it hide an important source-native boundary?
2. **Should Function and Capability be common concepts**, or only a common relationship hook to source-owned functional/capability descriptions?
3. **How much reported-state structure belongs in the common DIM** without inventing a universal status model?
4. **Is a common Event/history backbone sufficient** for configuration/service/deployment history, with specialized lifecycle semantics layered above it?
5. **Are communications and power correctly placed as common relationship hooks plus optional rich aspects?**
6. **Does Derived Information need a common concept**, or is provenance linking among source-owned products sufficient?
7. **Is common security/access metadata necessary in the DIM**, and if so what is the minimum boundary?
8. **Does the proposed relationship taxonomy cover real UGS, radiation, SOSA, industrial and atomic-device cases without overgeneralization?**
9. **Can internal components remain optionally non-resource-like** while still supporting source identity/calibration/status when those details matter?
10. **Can the candidate map cleanly to CSAPI/SensorML/SOSA/OMS without equating binding constructs with domain concepts?**
11. **Can specializations add modality/workflow semantics without forking common identity/composition/deployment semantics?**
12. **Does any candidate accidentally recreate the Version 1 eight-subject structure by another name?**

---

# 14. Phase C disposition

**Disposition: PHASE C CANDIDATE ANATOMY ESTABLISHED — VALIDATION REQUIRED.**

The evidence supports a candidate V2 anatomy organized as:

- persistent subject spine;
- context and typed relationships;
- dynamic activity/evidence;
- cross-cutting qualification;
- optional technical/management aspects;
- specialization hooks.

This is materially different from both:

- a monolithic equipment record; and
- a flat list of peer information modules.

No final V2 module names/classes have been adopted.

The clean V2 DIM remains unchanged.

**Next gate: Phase D — cross-source validation/falsification of the candidate anatomy.**
