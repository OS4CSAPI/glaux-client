# DIM/Profile V2 — Anatomy Phase 0 Structural Evidence Population

**Decision record v0.1 — 26 October 2026**  
**Status:** Phase 0 complete; anatomy evidence population frozen for Phase A extraction.  
**Controlling continuity:** `PITON_DIM_Profile_V2_Continuity_v0.6_25OCT2026.md`  
**Source accounting:** `DIM_Profile_V2_Anatomy_Phase0_182_Source_Ledger_v0.1_26OCT2026.csv`

## 1. Purpose

This record answers the Phase 0 question required by PITON v0.6:

> Which semantic lineages in the frozen 182-source corpus define enough internal organization to participate in discovering the anatomy of the V2 DIM, regardless of their primary document type?

The selection is based on **structural semantic capability**, not document classification. A source is admitted when it organizes the modeled subject, a major intrinsic concern, a contextual relationship set, or a domain specialization strongly enough to expose concepts, relationships, partitions, dependencies, or invariants that could shape the V2 DIM.

The selection does **not** imply adoption, normative dependency, conformance, equal evidentiary weight, or a future V2 module with the same name.

## 2. Complete corpus accounting

All 182 frozen sources are assigned exactly once.

| Source-level disposition | Count |
| --- | ---: |
| Primary evidence in admitted core structural lineages | 29 |
| Primary evidence in admitted cross-cutting structural lineages | 29 |
| Primary evidence in admitted specialization lineages | 14 |
| Companion evidence attached to admitted lineages | 83 |
| Excluded as non-structural for the DIM-anatomy question | 27 |
| **Total** | **182** |

The admitted population contains **30 semantic lineages**:

- **15 core structural donors**
- **11 cross-cutting structural donors**
- **4 specialization / operational donors**

Companion artifacts remain available within their lineage but do not receive independent conceptual weight.

## 3. Admission classes

### 3.1 Core structural donor

A lineage receives this standing when it supplies a substantial source-native organization of the whole subject, device/system/asset/node, or its primary internal organization.

A core donor does **not** need to share V2's chassis or terminology. It only needs enough internal structure to test the anatomy of the bounded V2 System.

### 3.2 Cross-cutting structural donor

A lineage receives this standing when it organizes one major semantic concern that can span the whole System or relate it to its context—for example observations, provenance, operational context, energy, hardware topology, network topology, or variable semantics.

A cross-cutting donor must not be mistaken for a candidate whole-System root merely because its concepts are broad.

### 3.3 Specialization donor

A lineage receives this standing when it provides a mature domain specialization or real-system organization useful for testing whether proposed V2 structures survive concrete modalities and equipment forms.

Specialization evidence can refine or falsify a candidate structure but cannot automatically become a universal V2 abstraction.

### 3.4 Companion / representation evidence

A companion artifact may provide schema details, implementation evidence, guidance, profile rules, APIs, historical versions, code lists, or executable validation. It is read with its parent lineage where needed but is not independently counted.

### 3.5 Non-structural for anatomy

These sources may still be valuable later for units, governance, linking, conformance, publication, transport, policy, or implementation, but they do not organize the bounded sensing System's domain anatomy strongly enough to enter Phase A.

---

# 4. Frozen core structural donor population

| # | Semantic lineage | Primary source IDs | Companion IDs | Why admitted |
| ---: | --- | --- | --- | --- |
| C01 | Asset Administration Shell | 94, 95, 96, 97, 98 | — | Asset-centered metamodel plus technical-data, hierarchy/BOM, and capability aspect models. |
| C02 | DMTF Redfish / CIM device management | 89 | 90–93 | Chassis, ComputerSystem, Manager, Sensor, power/battery and related resource organization. |
| C03 | IEEE 1451 / ISO 2145x | 110, 114, 124 | 109, 111–113, 115, 123, 125–131 | NCAP/TIM/transducer-channel/TEDS/service structure; current exact normative detail remains access-controlled where necessary. |
| C04 | ISA | 37, 42 | 28, 35, 36, 38–41, 43–45 | Component, Composition, virtual/visible member, network, deployment, capability/state and interface-mediated structure. |
| C05 | ISO/IEC 29182 SNRA | 116, 118, 120 | 117, 119, 121, 122 | Sensor-network physical/functional entity models and multi-view architecture. |
| C06 | Matter | 107 | — | Node/Endpoint/Device-Type and composed-device organization. |
| C07 | MIMOSA | 99, 100, 101 | 102 | Physical Asset lifecycle, CCOM, CBM functional architecture and integration information structures. |
| C08 | OGC Connected Systems | 10, 11 | 3, 9, 12, 17 | System/Deployment/Procedure/Property resource architecture plus observations, commands, streams and events. |
| C09 | OGC SensorML | 13 | 1, 2, 4, 6, 16 | Whole process/system description structure including components, capabilities, configuration, interfaces, modes and history. |
| C10 | OPC UA Devices / PA-DIM | 103, 104 | 105 | Device/component/topology/functional-group frame and a mature domain specialization. |
| C11 | OSUS / OSUS-R | 34 | 27, 59 | Physical Asset with sensors, capabilities, observations, commands, status and BIT. |
| C12 | SAPIENT | 21 | 22–25 | Node types, capabilities, modes, dependencies, platform/fusion hierarchy and recursive configuration. |
| C13 | SAREF | 144 | — | Device/System/Sensor, function, property, feature-of-interest and composition ontology structure. |
| C14 | SOSA/SSN | 19 | 18, 20 | Asset/System/Sensor/Platform/Procedure/Deployment and subsystem/hosting formal semantics. |
| C15 | The Open Group SOSA | 48, 49 | 47, 50–58 | Whole Sensor DSDM and architecture with modules, components, platform, configuration, state and management. |

The numerical order is a neutral extraction control, not a ranking.

---

# 5. Frozen cross-cutting structural donor population

| # | Semantic lineage | Primary source IDs | Companion IDs | Structural question it can inform |
| ---: | --- | --- | --- | --- |
| X01 | I-ADOPT | 145, 146 | 147, 150 | How an observed variable is compositionally qualified by property, object, matrix, context, constraints and modifiers. |
| X02 | IETF EMAN | 135, 139–141 | — | How equipment, components, power interfaces, energy relationships, measurements and battery state are organized. |
| X03 | IETF hardware management | 133 | — | Physical component hierarchy, containment, class, identity and state. |
| X04 | IETF interfaces / topology | 134, 136, 137 | — | Interface identity/layering and node/link/topology structures. |
| X05 | MIP / JC3IEDM | 29 | 26, 30, 46 | Operational objects/types, actions, locations, capabilities and context. |
| X06 | NIEM | 64, 75, 76, 78–86 | 60–63, 65–74, 77, 87, 88 | Cross-domain information organization, associations, roles, augmentations and domain/core boundaries. |
| X07 | NIST IoT cybersecurity baseline | 108 | — | Cross-cutting device capability organization for identity, configuration, protection, interfaces, update and security state. |
| X08 | OGC OMS | 8 | 15 | Observation/sampling acts, participants, procedure, feature/result, host/deployment and sampling distinctions. |
| X09 | OMA LwM2M | 129 | — | Device-management boundary and Object/Instance/Resource organization. |
| X10 | W3C PROV | 159, 160 | — | Entity/Activity/Agent provenance and derivation/association/attribution structure. |
| X11 | W3C Web of Things | 132 | — | Thing/Thing Model/Thing Description and interaction-affordance organization. |

The numerical order is a neutral extraction control, not a ranking.

---

# 6. Frozen specialization / operational population

| # | Semantic lineage | Primary source IDs | Why admitted |
| ---: | --- | --- | --- |
| S01 | Atomic sensor product evidence | 170 | Tests whether candidate anatomy scales down to a small, atomic sensing product rather than assuming a large composite system. |
| S02 | Radiation detection / instrument family | 163–168 | Mature modality-specific whole-instrument, detector, measurement, status and operational structures. |
| S03 | SWEET instrument ontology | 142, 143 | Scientific/instrument specialization with Equipment → Instrument and Sensor relationships plus discipline-specific instrument types. |
| S04 | UGS operational / reference systems | 169, 174–177 | Real deployed-system/manual organization used to falsify abstractions that fail actual UGS information needs. |

These sources do not receive universalizing authority merely because they are concrete.

---

# 7. Sources excluded from independent anatomy extraction

Twenty-seven artifacts are excluded from Phase A as independent structural donors. Their roles are methodology, standards policy, registries, units/quantity vocabulary, generic linking/profile mechanisms, unrelated modeling methods, media transport, or implementation-only evidence.

Important examples:

- OGC ModSpec;
- NATO/NISP/Data Strategy/NCDF where the available NCDF evidence is metadata-framework rather than sensor-system anatomy;
- RFC 7228 constrained-node terminology;
- HTTP Live Streaming;
- IANA link-relation registry;
- VIM, QUDT quantity/unit terms, and UCUM;
- profile/linking vocabularies;
- DCAT;
- OpenSensorHub implementation repositories;
- DISR/MOSA/DoD standards governance;
- CMMN;
- RFC 3444.

Exclusion from Phase A does **not** mean irrelevance to the overall profile. These sources can re-enter when a later question concerns terminology, units, governance, binding, conformance, implementation, or publication.

---

# 8. Why the population is not simply the original 14 plus the 13 chassis gaps

The anatomy problem is different from the chassis problem.

A source can be weak as a whole-System chassis but strong as an anatomy donor. Examples:

- OMS does not define the equipment chassis, but has a mature internal structure for observations and sampling.
- PROV does not define a sensor system, but gives a coherent provenance structure.
- RFC 8348 does not define sensing-domain membership, but gives a rigorous physical-component hierarchy.
- I-ADOPT does not define instruments, but gives a coherent structure for qualified observed variables.
- EMAN does not define the sensing System, but organizes power/energy relationships and state.
- JC3IEDM is much broader than the V2 domain but can contribute operational context distinctions.

Conversely, a source being classified as an architecture or ontology does not automatically earn Phase A standing if it lacks relevant internal organization for the bounded System.

---

# 9. Extraction-unit rule

**The unit of Phase A analysis is the semantic lineage, not the document.**

For each admitted lineage:

1. identify its controlling/current source(s);
2. use companion artifacts only where they clarify the lineage's source-native structure;
3. record edition/version differences when material;
4. do not count the same concept twice because it appears in a schema, API, implementation, guidance document, and test harness;
5. preserve genuine differences among editions rather than merging them silently.

Where a current source is access-limited, the extraction must state the evidence ceiling and may use authoritative older/public lineage evidence without inventing current normative detail.

---

# 10. Phase A extraction template

Each of the 30 admitted lineages will be characterized under the same questions:

1. source-native structural organization;
2. purpose of each partition;
3. central concepts per partition;
4. primary relationships;
5. dependency boundaries;
6. intrinsic vs contextual standing;
7. cross-cutting concepts;
8. state / temporal / lifecycle organization;
9. composition / topology organization;
10. capability / function / behavior organization;
11. information / output organization;
12. management / condition organization where source-native;
13. provenance / identity / reference organization where source-native;
14. semantic invariants that would be damaged by collapsing distinctions;
15. potential V2 structural contribution.

The final field remains an evidence label only during Phase A. No V2 modules are created during individual extraction.

---

# 11. Neutral Phase A extraction order

To make progress reproducible, Phase A will use the following order. The order has **no standing** and creates no preference.

### Core structural donors

C01 AAS  
C02 Redfish / CIM  
C03 IEEE 1451 / ISO 2145x  
C04 ISA  
C05 SNRA  
C06 Matter  
C07 MIMOSA  
C08 OGC Connected Systems  
C09 OGC SensorML  
C10 OPC UA Devices / PA-DIM  
C11 OSUS / OSUS-R  
C12 SAPIENT  
C13 SAREF  
C14 SOSA/SSN  
C15 The Open Group SOSA

### Cross-cutting structural donors

X01 I-ADOPT  
X02 IETF EMAN  
X03 IETF hardware management  
X04 IETF interfaces / topology  
X05 MIP / JC3IEDM  
X06 NIEM  
X07 NIST IoT cybersecurity baseline  
X08 OGC OMS  
X09 OMA LwM2M  
X10 W3C PROV  
X11 W3C Web of Things

### Specialization / operational donors

S01 Atomic sensor product evidence  
S02 Radiation detection / instrument family  
S03 SWEET instrument ontology  
S04 UGS operational / reference systems

---

# 12. Phase 0 decision

**Disposition: FREEZE THE 30-LINEAGE POPULATION ABOVE FOR ANATOMY PHASE A.**

No source may be added merely because it is discovered in a citation chain. The frozen 182-source corpus remains the universe.

A source/lineage already inside the 182 may be reclassified during Phase A only if direct inspection proves the Phase 0 structural-capability judgment materially wrong. Such a reclassification must be recorded explicitly rather than performed silently.

The clean V2 DIM remains unchanged during Phase A.

## Immediate next step

Begin **C01 — Asset Administration Shell** using the common 15-field anatomy template, then proceed through the frozen lineage order without cross-source synthesis until all 30 lineages have been independently extracted.
