# PITON — DIM/Profile V2 Research Continuity

**Version:** 0.8  
**Date:** 26 October 2026  
**Standing:** Recovery/checkpoint after conversation-to-repository state desynchronization  
**Repository:** OS4CSAPI/glaux-client  
**Branch:** research/dim-profile-v2  
**Workspace:** Docs/Research/DIM_Profile_V2/

> **RESTART INSTRUCTION:** Anatomy Phase A is **22 of 30 semantic lineages complete**. Do not redo C01–C15 or X01–X07. The next incomplete frozen lineage is **X08 — OGC Observations, Measurements and Samples (OMS)**. Resume there only when explicitly instructed to continue.

## 1. Why v0.8 supersedes v0.7

During a long autonomous Phase A extraction sequence, the repository continued to receive valid lineage extractions while the conversational progress/checkpoint state fell behind. PITON v0.7 therefore became stale: it still named C01 as the restart point even though the working extraction artifact had advanced through X07.

A repository integrity audit on 26 October 2026 established that the Phase A working draft contains:

- all 15 core structural donors, C01–C15;
- cross-cutting donors X01–X07;
- one unique heading per completed lineage;
- all 15 required extraction fields in every completed lineage; and
- an explicit COMPLETE marker for every one of those 22 lineages.

No incomplete C14–X07 section, duplicate lineage section, or missing extraction field was detected.

This PITON corrects continuity control only. It does not alter the substantive research decisions already recorded.

## 2. Controlling Phase A artifact

`DRAFT_DIM_Profile_V2_Anatomy_PhaseA_Independent_Extractions_v0.1_26OCT2026.md`

Repository SHA observed during integrity audit:

`1c470fd8eb4d163cc227c30ade363a868e468b99`

Observed document length at audit:

`394145 characters`

The exact SHA is a recovery checkpoint, not a permanent content identifier; later legitimate edits will change it.

## 3. Frozen population remains unchanged

Phase 0 remains controlled by:

- `DIM_Profile_V2_Anatomy_Phase0_182_Source_Ledger_v0.1_26OCT2026.csv`
- `DIM_Profile_V2_Anatomy_Phase0_Population_Decision_v0.1_26OCT2026.md`

The population remains **30 semantic lineages**:

- 15 core structural donors;
- 11 cross-cutting structural donors;
- 4 specialization/operational donors.

The frozen 182-source universe and lineage assignments are unchanged.

## 4. Completed Phase A lineages — DO NOT REDO

### Core structural donors — 15/15 complete

- C01 Asset Administration Shell
- C02 DMTF Redfish / CIM device management
- C03 IEEE 1451 / ISO 2145x
- C04 Integrated Sensor Architecture
- C05 ISO/IEC 29182 SNRA
- C06 Matter 1.3
- C07 MIMOSA
- C08 OGC API – Connected Systems
- C09 OGC SensorML 3.0
- C10 OPC UA Devices / PA-DIM
- C11 OSUS / OSUS-R
- C12 SAPIENT / BSI Flex 335
- C13 SAREF Core 4.1.1
- C14 SOSA/SSN
- C15 The Open Group SOSA

### Cross-cutting donors — 7/11 complete

- X01 I-ADOPT Framework Ontology
- X02 IETF Energy Management (EMAN)
- X03 IETF Hardware Management (RFC 8348)
- X04 IETF Interfaces / Network Topology
- X05 MIP / JC3IEDM
- X06 NIEM 6.0
- X07 NISTIR 8259A IoT Device Cybersecurity Capability Core Baseline

## 5. Remaining Phase A lineages — 8

### Cross-cutting donors

1. **X08 — OGC Observations, Measurements and Samples (OMS)**
2. X09 — OMA Lightweight M2M
3. X10 — W3C PROV
4. X11 — W3C Web of Things

### Specialization / operational donors

5. S01 — Atomic sensor product evidence
6. S02 — Radiation detection / instrument family
7. S03 — SWEET instrument ontology
8. S04 — UGS operational / reference systems

## 6. Required extraction method remains unchanged

Every remaining lineage must use the same 15-field source-native template:

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
13. provenance / identity / reference organization;
14. semantic invariants that would be damaged by collapsing distinctions;
15. potential V2 structural contribution.

No cross-source synthesis is allowed until all 30 lineages are complete.

## 7. Methodological standing remains unchanged

The chassis remains corpus-wide reconciled:

> physically realized equipment Systems whose defining operational role is sensing/observing, modeled as complete operational subjects.

The intended CSAPI characterization remains:

- `systemType = Sensor`
- `assetType = Equipment`

The permanent methodological correction remains:

> Source type determines how a source should first be understood; it does not determine whether that source may contribute domain structure.

The Version 1 eight information subjects remain predecessor evidence only and are not extraction bins.

## 8. Recovery rules

If work resumes after another interruption:

1. read v0.8 before v0.7;
2. inspect the tail of the Phase A working draft;
3. identify the last lineage carrying an explicit COMPLETE marker;
4. verify that the completed lineage contains all 15 numbered fields;
5. resume only at the next frozen lineage;
6. do not infer progress from conversational updates alone;
7. do not overwrite or re-extract a completed lineage unless a documented source error is found;
8. do not begin Phase B synthesis until all 30 Phase A lineages are complete.

## 9. Exact current restart point

**STOPPED SAFELY AFTER X07.**

The next permitted Phase A research task is:

> **X08 — OGC Observations, Measurements and Samples (OMS)**

No X08 research is considered complete by this checkpoint.
