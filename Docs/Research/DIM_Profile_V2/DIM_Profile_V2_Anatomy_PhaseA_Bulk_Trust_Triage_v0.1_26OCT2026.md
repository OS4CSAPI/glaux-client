# DIM/Profile V2 — Phase A Bulk Trust Triage

**Version:** 0.1  
**Date:** 26 October 2026  
**Standing:** Bulk triage following C08 calibration audit  
**Controlling recovery state:** PITON_DIM_Profile_V2_Continuity_v1.3_26OCT2026.md

## 1. Purpose

This is a **risk triage, not thirty full audits**.

Its purpose is to decide whether the Phase A lineage extractions are usable enough to support renewed cross-donor discovery without turning validation into a second research program.

Ratings mean:

- **GREEN** — structurally usable for later comparison at the level extracted. Normal source-role and interpretation caveats still apply.
- **YELLOW** — usable only within an explicit evidence ceiling or with a material carrier/authority caveat. Do not allow the lineage to carry a finer-grained conclusion than its source access supports.
- **RED** — not safe to use as affirmative structural evidence until targeted recheck.

A GREEN rating does **not** mean every sentence was independently re-verified. A YELLOW rating does **not** mean the extraction is wrong.

The C08 calibration audit established the recurring general issue across Phase A: source facts, project interpretation, and comparison abstractions were not always labeled distinctly. Therefore all Phase A Section 15 “potential contribution” language and analytical headings such as intrinsic/contextual/cross-cutting are treated as **project analysis**, not donor-native taxonomy, unless a source explicitly says otherwise.

## 2. Bulk triage

| ID | Lineage | Rating | Human reason / safe use |
| --- | --- | --- | --- |
| C01 | Asset Administration Shell | **GREEN** | Official AAS metamodel and frozen IDTA templates were directly inspected. Use source-native Asset/AAS/Submodel/type-instance/reference structures; do not turn AAS carrier hierarchy into V2 hierarchy automatically. |
| C02 | DMTF Redfish / CIM | **GREEN** | Official Redfish guides, normative schemas, and exact CIM/Battery/Power artifacts support the extracted management/equipment distinctions. Keep URI/resource hierarchy and Links as Redfish carriers. |
| C03 | IEEE 1451 / ISO 2145x | **YELLOW** | High-level smart-transducer/module/channel/self-description structure is useful, but exact IEEE 1451.0-2024 TEDS definitions, optionality, cardinalities and conformance obligations remained behind the normative-access ceiling. Use high-level structure only. |
| C04 | Integrated Sensor Architecture | **GREEN** | Complete Distribution A ISA 6.0 documents were available. Strong source basis; keep ISA messages/services/virtualization/interface behavior distinct from universal domain truth. |
| C05 | ISO/IEC 29182 SNRA | **YELLOW** | Exact high-level public overview/preview supports physical-vs-functional entity organization, but complete normative Parts 1/3/4 were unavailable. Do not use uninspected lower-level definitions. |
| C06 | Matter 1.3 | **YELLOW** | Exact Device Library structures were directly inspected, but direct Core 1.3 retrieval was limited. Node/Endpoint/Device Type/Cluster/composition findings are useful where directly supported; do not generalize protocol structure into physical composition. |
| C07 | MIMOSA | **YELLOW** | Useful asset/condition/maintenance architecture, but the frozen CCOM 4.1.0 material is Proposed/RC1 and OSA-CBM/OSA-EAI are separate specifications. Preserve their distinctions and avoid treating the combined family as one settled conceptual model. |
| C08 | OGC API – Connected Systems | **GREEN — corrected** | C08 calibration audit found the extraction substantially source-faithful. Correct the systemKind-vs-implemented-Procedure distinction; qualify Feature of Interest and SensorML-carried Deployment configuration. |
| C09 | OGC SensorML 3.0 | **GREEN** | Exact approved standard and conceptual UML/JSON model were directly available. Strong structural source; keep conceptual semantics separate from JSON/schema carrier details. |
| C10 | OPC UA Devices / PA-DIM | **GREEN** | Exact official Part 100 and PA-DIM publications support generic-device and process-automation specialization structure. PA-DIM is specialization, not an independent vote. |
| C11 | OSUS / OSUS-R | **GREEN** | Pinned source code/schema provides exact reference-architecture/implementation evidence for Asset/capability/observation/command structures. Its authority is implementation/reference-system evidence, not universal normative vocabulary. |
| C12 | SAPIENT / BSI Flex 335 | **GREEN** | Exact BSI Flex 335 v2.0 plus official companion implementation artifacts support the source-native network/interface structures. Treat interface-control constructs as SAPIENT semantics, not automatically generic DIM classes. |
| C13 | SAREF Core 4.1.1 | **GREEN** | Exact ETSI ontology was directly inspected. Strong semantic evidence; keep SAREF ontology hierarchy and SAREF4SYST relationships distinct from API/resource design. |
| C14 | SOSA/SSN | **GREEN** | Exact frozen 21 Oct 2026 Working Draft was inspected and its draft status was explicit. Use it as current semantic evidence, while preserving that published CSAPI 1.0 normatively references the earlier SOSA/SSN edition. |
| C15 | The Open Group SOSA | **GREEN** | Adopted Edition 1.1 architecture and Edition 1.0 DSDM were directly available. Later Edition 2 Snapshot material was not used for new clause-level claims. |
| X01 | I-ADOPT | **GREEN** | Exact ontology 1.1.0 supports variable-description semantics. Use only for its cross-cutting variable/property role; it is not a System/equipment anatomy model. |
| X02 | IETF Energy Management | **GREEN** | Exact RFC framework and MIBs support Energy Object, relationships, power state and battery semantics. Preserve framework-vs-MIB realization distinction. |
| X03 | IETF Hardware Management | **GREEN** | Exact RFC 8348 supports physical component identity/hierarchy. Narrow donor by design; do not treat server-hardware management as a whole sensing-system model. |
| X04 | IETF Interfaces / Network Topology | **GREEN** | Exact RFCs support mature interface/layer/topology distinctions. Network topology is not physical system composition. |
| X05 | MIP / JC3IEDM | **YELLOW** | Exact-version high-level overview supports Item/Type, Action, Location, Capability, Context and Reporting-Data distinctions, but complete 3.1.4 package was unavailable. Use high-level conceptual structure only. |
| X06 | NIEM 6.0 | **YELLOW** | Exact OASIS model/schema material is strong, but the lineage is extremely broad and combines core construction/exchange machinery with multiple domain schemas. Use explicit reusable concepts/methodology; do not let model breadth masquerade as one coherent chassis. |
| X07 | NISTIR 8259A | **GREEN** | Exact frozen baseline supports six cybersecurity capabilities. Specialization/cross-cutting evidence only, not general device anatomy. |
| X08 | OMS 3.0 | **GREEN** | Complete OGC 20-082r4 was available and directly used. Strong conceptual evidence for observation/observer/procedure/host/deployment/sample structures. |
| X09 | OMA LwM2M 1.2.2 | **GREEN** | Exact approved specification was directly inspected. Strong device-management evidence; Object/Instance/Resource URI hierarchy and management operations remain LwM2M carriers. |
| X10 | W3C PROV | **GREEN** | Exact Recommendations for PROV-DM/O support provenance/derivation/responsibility semantics. Cross-cutting donor, not equipment anatomy. |
| X11 | W3C Web of Things | **GREEN** | Exact W3C Recommendation supports Thing/Thing Description/Thing Model/Affordance/Servient distinctions. Strong representation/interaction evidence; not a replacement for physical equipment/System semantics. |
| S01 | Bosch BME280 | **GREEN** | Exact datasheet. Valid scale-down/atomic-sensor falsifier; not a standards authority or universal vocabulary source. |
| S02 | Radiation instrument family | **YELLOW** | Strong family-level evidence, but full normative text was unavailable for several IEEE/IEC/ISO sources and exact 2020 schema cardinalities were not established. Use instrument/detector/calibration/measurement/analysis patterns, not unverified field-level claims. |
| S03 | SWEET instrument ontology | **GREEN** | Exact ontology modules were directly inspected. Useful specialization/type semantics; intentionally narrow and not a lifecycle/management model. |
| S04 | UGS operational/reference systems | **YELLOW** | Strong real-system falsification evidence, but full native OmniSense/Sentinel manuals were not present in searchable form; extraction depends on previously reviewed excerpts/training/public papers. Use observed operational patterns, not claims of universal UGS semantics or complete product coverage. |

## 3. Triage result

**GREEN:** 22  
**YELLOW:** 8  
**RED:** 0

YELLOW set:

- C03 IEEE 1451 / ISO 2145x
- C05 ISO/IEC 29182 SNRA
- C06 Matter 1.3
- C07 MIMOSA
- X05 MIP / JC3IEDM
- X06 NIEM 6.0
- S02 Radiation instrument family
- S04 UGS operational/reference systems

## 4. What this means operationally

The Phase A population is **usable enough to stop making validation the main project**.

No lineage presently requires wholesale rejection.

The eight YELLOW lineages do not need full re-research before comparison. Instead, they carry explicit ceilings:

- C03, C05, X05 and S02 may support only the high-level structures actually established from accessible evidence.
- C06 may support directly inspected Matter structural patterns but not unsupported Core-level detail.
- C07 must keep CCOM, OSA-CBM and OSA-EAI distinct and acknowledge RC/proposed status.
- X06 must separate NIEM's exchange/model-construction machinery from actual domain semantics.
- S04 may falsify/test the emerging model against observed UGS reality but must not define universal UGS vocabulary from incomplete historical manuals.

If later synthesis depends critically on a fine-grained proposition from one of these YELLOW lineages, perform a **targeted check of that proposition only**.

## 5. Reopened synthesis gate

The validation exercise has now bought enough confidence to resume the actual research question.

Cross-donor discovery may proceed under these controls:

1. treat GREEN/YELLOW as confidence/evidence-ceiling metadata, not votes;
2. do not count companion documents as independent corroboration;
3. distinguish common inheritance/dependency from independent convergence;
4. preserve donor role: a provenance ontology, network model or cybersecurity baseline is not expected to define the whole subject;
5. keep donor-native claims separate from project interpretation;
6. do not let Phase A Section 15 “potential contribution” labels become evidence by repetition;
7. do not use the quarantined Phase B/C/D artifacts as input;
8. allow the bounded subject/name of the DIM to emerge from the validated donor evidence rather than forcing one.

The next discovery question is deliberately human:

> **What are the donor communities collectively telling us about the kind of real-world subject we are trying to describe, its natural boundaries, and the information that must remain understandable about it?**
