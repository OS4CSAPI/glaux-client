# Step 08 — Owner checkpoint CLOSED: revised crosswalk layout accepted

**6 November 2026 · STEP08 COMPLETE (8/40) · NEXT STEP09 NOT STARTED.**

## What you approved — and what you did not

You viewed the revised 13-column crosswalk and responded **“yes, that's better.”** You then explicitly authorized this Step08 closeout. That means the [revised v0.2 editable master](Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026.xlsx) is our **accepted working presentation layout**. It is **not** blanket approval of its information-element meanings, donor equivalences, source interpretations, row names, case-only review entries, final ranking or the Domain Information Model (DIM) / OGC API – Connected Systems (CSAPI) Profile.

**Accepted columns, left → right:** Dragino S31-LB · AirGradient Open Air Max · Campbell CR1000X + ClimaVue 50 · Bennett's Point (ACE Basin) · IEEE 1451 · OPC UA Devices · SAPIENT v2 · W3C SOSA/SSN · OGC OMS 3.0 · OGC SWE Common 3.0 · SensorML 3.0 · CSAPI Parts 1–2 · **PROPOSED DIM ELEMENT**. W3C SOSA/SSN was put beside the related foundational sensing/observation standards for comparison; that does **not** mean it was published by OGC. The three other donor columns remain in **provisional sample order**, not proven order of contribution.

The [GitHub-readable full comparison](Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026.md) and [actual Excel workbook](Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026.xlsx) are the current **layout baseline**. The earlier [v0.1 workbook](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) is preserved, unchanged, for history. The current workbook's readme/source JSON still records **PENDING** because it was created *before* you approved the format. **This later signed-off owner decision controls execution status**; that old metadata is a record of the earlier snapshot, not permission to revisit Step08.

## Holds, in normal terms

| Area | Step08 decision |
| --- | --- |
| **22 previously proposed DIM rows** | Retained as **proposals**, not technically adopted. Their names/groupings can change when actual source evidence warrants. |
| **Nine case-derived extra rows** | Remain **review holds** `CASE-H01` through `CASE-H09`. Do not silently adopt them as DIM requirements or equate them to donor concepts. |
| **51 historical donor comparisons** | Retained literally with **`PRIOR_SOURCE_EXTRACT_ONLY`** standing; none was newly verified against original clauses here. |
| **73 case-example entries** | Remain qualified manufacturer reference/published examples (Dragino, AirGradient, Campbell) or genuine historical-source statements (Bennett). **Not vendor compliance claims.** |
| **SWE Common 3.0 column** | Now positioned immediately beside other foundational standards, but blank pending actual source review. |
| **Other donor ordering / additional sources** | Final evidence-based ranking is unresolved. The 17 provisional and 29 conditional *candidate* column roster does not automatically enter this workbook. |

The original earlier DIM, candidate Profile, UML, source packets, Glaux app, native server and deployment were **not changed** in this step. The existing [independent workbook validation](https://github.com/OS4CSAPI/glaux-client/actions/runs/42314409072) checked actual file structure and mirror consistency **before the owner decision**, not the semantic correctness of donor mappings. The complete precise decision is also stored in [structured JSON](Step08_Owner_Review_Disposition_06NOV2026.json).

## Current status and next step

**Steps 01–08 COMPLETE (8/40). Step09 PENDING — not started.** The plan, recovery PITON and README point to this recorded acceptance. No additional donor source clauses were checked and no new mappings were made during the Step08 closeout.

**NEXT one owner “proceed” executes STEP09 ONLY:** take **OGC API – Connected Systems Parts 1 and 2**, consult their original published definitions and clauses, and make a small number of defensible donor-to-information-element comparisons with evidence in the **accepted horizontal master**. Keep a CSAPI resource distinct from a physical part and preserve unresolved source/model distinctions. Show real technical results and stop; **do not automatically continue to Step10**.
