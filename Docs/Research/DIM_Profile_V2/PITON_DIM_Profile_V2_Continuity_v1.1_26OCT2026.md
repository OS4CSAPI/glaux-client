# PITON — DIM/Profile V2 Research Continuity

**Version:** 1.1  
**Date:** 26 October 2026  
**Standing:** Anatomy Phase C candidate established; Phase D validation required  
**Repository:** OS4CSAPI/glaux-client  
**Branch:** research/dim-profile-v2  
**Workspace:** Docs/Research/DIM_Profile_V2/

> **RESTART INSTRUCTION:** Phase 0, Phase A, Phase B and Phase C are complete. Do not redo population selection, the 30 lineage extractions or the cross-source comparison. The next task is **Phase D — validation/falsification of the candidate anatomy** in DIM_Profile_V2_Anatomy_PhaseC_Candidate_Structure_v0.1_26OCT2026.md. Do not edit the clean V2 DIM unless Phase D confirms/refines the candidate sufficiently for promotion.

## 1. Completed anatomy chain

Phase 0:
- DIM_Profile_V2_Anatomy_Phase0_182_Source_Ledger_v0.1_26OCT2026.csv
- DIM_Profile_V2_Anatomy_Phase0_Population_Decision_v0.1_26OCT2026.md

Phase A:
- DRAFT_DIM_Profile_V2_Anatomy_PhaseA_Independent_Extractions_v0.1_26OCT2026.md
- 30/30 lineages complete, all 15 fields present.

Phase B:
- DIM_Profile_V2_Anatomy_PhaseB_Cross_Source_Comparison_v0.1_26OCT2026.md
- commit da54dd70949a61d63ff6d3998ee97df9d8c44a31
- 16 propositions eligible for Phase C.

Phase C:
- DIM_Profile_V2_Anatomy_PhaseC_Candidate_Structure_v0.1_26OCT2026.md
- commit e92877b85bba0b2be4c03cb39ec474a9fdb15c3e

## 2. Candidate organizational shape under validation

The Phase C candidate is organized as five structural kinds:

1. Persistent Subject Spine
2. Context and Relationship Structure
3. Dynamic Activity and Evidence Structure
4. Cross-Cutting Qualification Structure
5. Optional Technical / Management Aspects

Specializations extend the common structure.

These are organizational labels, not adopted domain classes/module names.

## 3. Candidate Persistent Subject Spine

Candidate common elements/relations include:

- persistent System identity;
- reusable kind/model/procedure association;
- optional enduring decomposition into subordinate Systems or meaningful components;
- functional/capability description;
- configuration/modes/settings.

## 4. Candidate Context / Relationship Structure

Candidate relationships include:

- Deployment/emplacement;
- Host/Platform;
- communications/connectivity;
- power-source/energy;
- organization/responsibility/manager relationships.

## 5. Candidate Dynamic Activity / Evidence Structure

Candidate structures include:

- Observation/measurement/detection;
- reported state/telemetry;
- Command/action/task interaction;
- Event/history;
- optional derived information/analysis/assessment.

## 6. Candidate cross-cutting semantics

- identity/reference;
- provenance/source/responsibility;
- time/validity;
- semantic property/variable definitions;
- units/constraints/quality;
- version/revision;
- bounded security/access metadata.

## 7. Candidate optional aspects

- condition/health/diagnostics;
- communications/network;
- power/energy;
- software/firmware/computational participation;
- maintenance/service/asset lifecycle.

## 8. Phase D required challenge cases

At minimum validate against:

1. atomic sensing product — BME280;
2. composite installed system — radiation portal;
3. complex modular sensor — Open Group SOSA;
4. distributed/remote UGS — TRSS/OmniSense;
5. industrial device family — OPC UA Devices/PA-DIM/AAS;
6. virtual/mediated participants — ISA/SAPIENT/WoT/LwM2M;
7. formal observation semantics — OMS/SOSA/SSN/I-ADOPT;
8. lifecycle/assessment-heavy asset model — MIMOSA;
9. whole-device operational implementation — OSUS;
10. current OGC binding environment — CSAPI/SensorML;
11. network/power cross-cutting models — IETF topology/EMAN;
12. provenance/derived-information model — PROV.

## 9. Phase D questions to falsify/refine

1. Is the five-kind organizational shape stable?
2. Should Function/Capability be common concepts or only common hooks to source-owned descriptions?
3. How much state/condition belongs in the common DIM?
4. Is a common Event/history backbone sufficient?
5. Are communications and power correctly modeled as common relation hooks + optional rich aspects?
6. Is common support for derived information needed?
7. What minimum security/access semantics belong in the DIM?
8. Does the relationship taxonomy cover the stress cases?
9. Can internal components remain optional/non-resource-like?
10. Can the anatomy map to CSAPI/SensorML/SOSA/OMS without binding/domain conflation?
11. Can specializations extend common structures without forking identity/composition/deployment?
12. Does the candidate accidentally reproduce Version 1 structure?

## 10. Promotion rule

Only after Phase D:

- record PASS / REFINE / FAIL per candidate element;
- incorporate required refinements into a final anatomy decision record;
- then promote only validated anatomy decisions into the clean V2 working draft.

Do not promote unresolved candidate labels or native donor carriers.

## 11. Current restart point

**Begin Phase D validation/falsification.**
