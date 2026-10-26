# PITON — DIM/Profile V2 Research Continuity

**Version:** 0.7  
**Date:** 26 October 2026  
**Standing:** Anatomy Phase 0 complete; Phase A extraction ready  
**Repository:** OS4CSAPI/glaux-client  
**Branch:** research/dim-profile-v2  
**Workspace:** Docs/Research/DIM_Profile_V2/

> **RESTART INSTRUCTION:** The chassis is corpus-wide reconciled and the DIM-anatomy evidence population is frozen. Do not reopen chassis discovery, rebuild the anatomy population, or use primary source type as an eligibility gate. Resume **Anatomy Phase A** at the first incomplete lineage in the frozen 30-lineage order. Extract each lineage independently under the common 15-field template. Do not synthesize candidate V2 modules or edit the clean DIM until all 30 lineages are complete.

## 1. Controlling decisions

The V2 chassis remains:

> **physically realized equipment Systems whose defining operational role is sensing/observing, modeled as complete operational subjects**

Intended CSAPI characterization:

- `systemType = Sensor`
- `assetType = Equipment`

No new umbrella/root class is adopted.

The chassis standing is controlled by the full 182-source reconciliation, not only by the original CIDM study.

## 2. Anatomy Phase 0 is complete

Authoritative Phase 0 artifacts:

- `DIM_Profile_V2_Anatomy_Phase0_182_Source_Ledger_v0.1_26OCT2026.csv`
- `DIM_Profile_V2_Anatomy_Phase0_Population_Decision_v0.1_26OCT2026.md`

All **182** frozen sources are accounted for exactly once:

- 29 primary evidence artifacts in core structural lineages;
- 29 primary evidence artifacts in cross-cutting structural lineages;
- 14 primary evidence artifacts in specialization/operational lineages;
- 83 companion artifacts attached to admitted lineages;
- 27 excluded from independent anatomy extraction as non-structural for this question.

The frozen Phase A population contains **30 semantic lineages**:

- 15 core structural donors;
- 11 cross-cutting structural donors;
- 4 specialization/operational donors.

The unit of analysis is the **semantic lineage**, not the document.

## 3. Permanent methodological correction

> **Source type determines how a source should first be understood; it does not determine whether that source may contribute domain structure.**

Companion artifacts may clarify their parent lineage but do not count as independent conceptual agreement.

The Version 1 eight information subjects remain predecessor evidence only. They are not extraction bins.

## 4. Phase A extraction template

Every admitted lineage is independently characterized under the same questions:

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

Field 15 is an evidence label only. No V2 modules are created during Phase A.

## 5. Frozen extraction order

### Core structural donors
C01 Asset Administration Shell  
C02 DMTF Redfish / CIM device management  
C03 IEEE 1451 / ISO 2145x  
C04 ISA  
C05 ISO/IEC 29182 SNRA  
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

The order has no evidentiary standing.

## 6. Phase A stop rules

Do not:

- compare or rank donors while extracting an individual lineage;
- rename donor partitions into V2 terminology during extraction;
- infer a V2 module from one donor;
- count companion documents as independent agreement;
- silently merge version/edition differences;
- fill access gaps with general knowledge;
- treat interface/schema placement as domain truth;
- update the clean DIM;
- revive the Version 1 eight-subject structure as an organizing frame.

If a lineage does not answer a field, record it as absent/non-applicable.

## 7. Synthesis gate

Only after all 30 lineages are complete may Phase B compare:

- recurring semantic clusters;
- intrinsic versus contextual partitions;
- cross-cutting structures;
- functional/physical/informational distinctions;
- composition/topology;
- capability/behavior;
- state/lifecycle;
- outputs/results;
- provenance/identity;
- dependencies;
- conflicting boundaries;
- specialization-only structures.

Only after Phase B may Phase C propose V2 anatomy. Candidate structures must then pass Phase D cross-type validation before promotion to the clean DIM.

## 8. Current restart point

**Begin C01 — Asset Administration Shell.**

Use source IDs 94–98 as the AAS structural lineage:

- IDTA AAS Part 1 Metamodel v3.2;
- Hierarchical Structures Enabling Bills of Material;
- Generic Frame for Technical Data for Industrial Equipment;
- IEC 81346 hierarchy extension;
- Capability Description.

The complete AAS lineage is to be understood source-natively before any comparison with other lineages.
