# PITON — DIM/Profile V2 Research Continuity

**Version:** 0.9  
**Date:** 26 October 2026  
**Standing:** Anatomy Phase A complete; Phase B comparison ready  
**Repository:** OS4CSAPI/glaux-client  
**Branch:** research/dim-profile-v2  
**Workspace:** Docs/Research/DIM_Profile_V2/

> **RESTART INSTRUCTION:** DIM Anatomy Phase A is COMPLETE. All 30 frozen semantic lineages have been independently extracted under the common 15-field template. Do not redo Phase A unless a documented source error is found. The next permitted task is **Phase B — cross-source structural comparison**. Phase B may compare evidence but must not yet promote candidate V2 modules into the clean DIM.

## 1. Phase A completion state

Controlling extraction artifact:

`DRAFT_DIM_Profile_V2_Anatomy_PhaseA_Independent_Extractions_v0.1_26OCT2026.md`

Completion integrity check:

- 30 unique lineage sections;
- 30 explicit COMPLETE markers;
- all 15 required extraction fields present in every lineage;
- no duplicate lineage IDs;
- no missing numbered fields;
- no Phase B synthesis embedded in the Phase A artifact.

Observed content SHA before the final status-header edit:

`0147dd36fb0e03f58e4063b460d771e765d461a5`

Final status-header update commit:

`075f03b85c95ba65261c16fc3ed0d5cf4b5e454d`

The SHA is only a recovery locator; legitimate future edits will change it.

## 2. Completed frozen lineage population

### Core structural donors — 15/15 complete

C01 Asset Administration Shell  
C02 DMTF Redfish / CIM device management  
C03 IEEE 1451 / ISO 2145x  
C04 Integrated Sensor Architecture  
C05 ISO/IEC 29182 SNRA  
C06 Matter 1.3  
C07 MIMOSA  
C08 OGC API – Connected Systems  
C09 OGC SensorML 3.0  
C10 OPC UA Devices / PA-DIM  
C11 OSUS / OSUS-R  
C12 SAPIENT / BSI Flex 335  
C13 SAREF Core 4.1.1  
C14 SOSA/SSN  
C15 The Open Group SOSA

### Cross-cutting structural donors — 11/11 complete

X01 I-ADOPT Framework Ontology  
X02 IETF Energy Management (EMAN)  
X03 IETF Hardware Management  
X04 IETF Interfaces / Network Topology  
X05 MIP / JC3IEDM  
X06 NIEM 6.0  
X07 NISTIR 8259A IoT Device Cybersecurity Baseline  
X08 OGC Observations, Measurements and Samples  
X09 OMA Lightweight M2M  
X10 W3C PROV  
X11 W3C Web of Things

### Specialization / operational donors — 4/4 complete

S01 Bosch BME280 atomic sensor product evidence  
S02 Radiation detection / instrument family  
S03 SWEET instrument ontology  
S04 UGS operational / reference systems

## 3. Phase 0 controls remain binding

Frozen source universe: **182 artifacts**

Frozen anatomy lineage population: **30 semantic lineages**

Authoritative Phase 0 artifacts:

- `DIM_Profile_V2_Anatomy_Phase0_182_Source_Ledger_v0.1_26OCT2026.csv`
- `DIM_Profile_V2_Anatomy_Phase0_Population_Decision_v0.1_26OCT2026.md`

The unit of evidence is the semantic lineage, not the number of publications in that lineage.

## 4. Chassis remains unchanged

The corpus-wide reconciled chassis remains:

> **physically realized equipment Systems whose defining operational role is sensing/observing, modeled as complete operational subjects**

Intended CSAPI characterization:

- `systemType = Sensor`
- `assetType = Equipment`

No new root/umbrella class has been adopted.

Anatomy research occurs **inside this boundary** and must not silently reopen the chassis merely because donors use different nouns.

## 5. Permanent methodology

> **Source type determines how a source should first be understood; it does not determine whether that source may contribute domain structure.**

Additional controls:

- source-native structure first;
- no Version 1 eight-subject bins;
- companion documents do not create independent votes;
- interface/resource hierarchy is not automatically domain hierarchy;
- physical composition, functional grouping, network topology, deployment association and presentation grouping must remain distinguishable when sources distinguish them;
- conceptual reuse does not equal donor-standard implementation or conformance.

## 6. Phase B purpose

Phase B answers:

> **Across the 30 independently extracted lineages, what structural distinctions recur, which are genuinely equivalent, which are overloaded/conflicting, which concerns appear intrinsic to the bounded sensing System, which are contextual or cross-cutting, and which structures remain specialization-only?**

Phase B is comparison, not architecture selection.

## 7. Required Phase B comparison dimensions

At minimum compare:

1. whole-subject identity / model-instance structure;
2. physical composition and component identity;
3. functional grouping / capability / behavior;
4. configuration / modes / settings;
5. deployment / host / location / operational context;
6. communications / interfaces / network topology;
7. power / energy;
8. current state / health / condition / diagnostics;
9. observation / measurement / sensing outputs;
10. commands / actions / tasking;
11. events / history / lifecycle;
12. provenance / source / responsibility;
13. property / variable / semantic-definition structure;
14. information products / analysis / derived results;
15. management / maintenance / service;
16. security / authorization where structurally present;
17. type/model vs instance vs runtime representation;
18. persistent structure vs time-scoped association;
19. physical vs logical/virtual representation;
20. specialization boundaries and optionality.

Also compare source-native relationship distinctions such as:

- composition vs aggregation;
- part-of vs host/deployment;
- component vs functional group;
- physical topology vs network topology;
- capability vs current state;
- capability vs execution;
- property definition vs property value;
- observation act vs result;
- system/asset identity vs representation/resource identity;
- model/type vs instance;
- current state vs event/history;
- raw evidence vs assessment/analysis;
- request/command vs status/result;
- source equipment vs internal sensor/channel.

## 8. Phase B stop rules

Do not:

- create final V2 module names;
- force every recurring topic to become a module;
- count number of documents instead of independent lineages;
- treat common API/UI groupings as semantic equivalence;
- merge concepts solely because they have similar labels;
- promote specialization-only terminology into the common core;
- change the clean DIM;
- begin machine-readable schema/profile design;
- resolve conflicts by preference without tracing source semantics;
- use Version 1 subjects as the comparison frame.

## 9. Phase B deliverable expectation

Create a dedicated comparison artifact, separate from the Phase A extraction record.

It should contain:

- neutral structural comparison matrix;
- recurring semantic patterns;
- overloaded/conflicting terminology;
- source-lineage convergence/dependency notes;
- intrinsic vs contextual findings;
- cross-cutting findings;
- specialization-only findings;
- unresolved contradictions/gaps;
- explicit list of structural propositions that are **eligible for Phase C consideration**, without yet naming/adopting final V2 modules.

## 10. Exact restart point

**Phase A is closed.**

Next permitted task:

> **Begin Phase B — cross-source structural comparison across the 30 completed lineage extractions.**
