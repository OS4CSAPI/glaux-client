# Step 8 — proposed layout revision: actual case columns and foundational block

**6 November 2026 · REVISED FILES PUBLISHED FOR OWNER REVIEW · OWNER HAS NOT ACCEPTED THIS FORMAT OR THE NEW REVIEW-HOLD ROWS.** The original Step06 workbook and its 51 proposed donor mappings are preserved unchanged. This revision changes presentation, adds four equipment-source columns and an empty SWE Common column, and displays source-native **case evidence** that had previously been out of sight.

## Why the geometry changed

The owner asked for the OGC-connected sensing/observation standards to appear together immediately before the far-right DIM, in right-to-left priority: **DIM ← CSAPI ← SensorML ← SWE Common ← OMS 3.0 ← W3C SOSA/SSN**, then the other donors, with **four experiment case columns at the far left**. This is accomplished in the revised [Excel workbook](Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026.xlsx) and [GitHub-readable master](Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026.md). W3C SOSA/SSN is **W3C**, not OGC; it is positioned with foundational observation/sensor concepts because the owner explicitly wants adjacent related standards. Remaining donor order (IEEE, OPC UA Devices, SAPIENT) is **provisional sample population order**, not original-source-verified substantive strength.

## Exactly what is new

The first sheet contains **13 columns**: 4 case columns, 3 other-donor columns, 5 foundational-standards columns (including SWE Common), and **1 final DIM** column. It contains the original **22 proposed information rows and five original section dividers**, plus one clearly separate **case terms awaiting DIM disposition** divider and **nine case-only REVIEW HOLD rows**, where original case fields could not responsibly be forced into an existing DIM row. All **51 older donor cells/relations are unchanged**, and the entire SWE Common donor column is left blank until checked against OGC 24-014. No adopted DIM/CSAPI Profile requirements or UML changes have been made.

The new source-case columns contain **73 recorded nonempty case cells**, each with source IDs, documentary/example/historical standing and caution in the [Case Evidence CSV](Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026_Case_Evidence.csv) and the Excel **Case Evidence** worksheet. The 51 legacy donor evidence records have their own **Donor Evidence** sheet. These case entries are a selection from the four maintained research sheets—not every vendor data field and not a new original publisher reading. **Dragino, AirGradient and Campbell** are reference/example evidence, not authenticated installed individual systems. **Bennett's Point** has actual source-reported 2024 station/equipment records and two original NOAA means; four older project API records remain *digital representations of those two events*.

## Key illustrative examples

- **Reported output field:** Dragino `TempC_SHT31; Hum_SHT31`, AirGradient `pm01; pm25; pm10`, Campbell ClimaVue `aR7!` positions 1–14 with a separately published logger `PanelTemp` example, Bennett `ATemp; F_ATemp; F_Record`. These are not four interchangeable semantics, and the evidence tab records that.
- **Performed Observation:** the three reference cases are blank because no qualified real performed source observation has been acquired. Bennett has the two original historical NOAA air-temperature mean values, not four observations.
- **Source role:** AirGradient PM1/PM2 sockets identify physical connectors, not the three particulate properties. Campbell 14 response field positions are not 14 physical sensors. The station coordinate from Bennett belongs to the station site, not to an individually surveyed EE181 probe.
- **Review-only topics:** dated equipment service, mounting/location, reporting paths, power, diagnostics, default versus applied configuration, processing, QA/time, and documented controls versus actual execution. These may lead to DIM rows, subelements or exclusions **only after review**.

## File integrity / source standing

- [New editable workbook](Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026.xlsx) · [direct full-table Markdown mirror](Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026.md) · [CSV](Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026.csv) · [complete structured JSON](Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026.json) · [case-evidence CSV](Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026_Case_Evidence.csv).
- Original v0.1 sample: [editable workbook](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) and [Markdown](Master_Donor_Concept_to_DIM_Crosswalk.md). **Neither has been overwritten.**
- No new donor native clauses, no confirmed equivalences, no final donor contribution ranking, no changes to the existing research DIM, OGC API – Connected Systems (CSAPI) application Profile, Glaux application, server or deployment.
- The revised workbook contains no automated network connections/macros; source URLs are stored as citation pointers. The final owner judgment remains **PENDING**.

**What comes next:** Stay at **Step08 owner review**. Look at the revised table and its nine visibly held example rows, then choose what to accept/change. **Do not start Step09** until the user explicitly accepts the layout and proposed review outcomes.
