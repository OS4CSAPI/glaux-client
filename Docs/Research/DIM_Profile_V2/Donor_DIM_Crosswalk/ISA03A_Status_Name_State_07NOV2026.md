# ISA-03A — Status intervals, Name and Operating State

**7 November 2026 · Four of four assigned source reviews COMPLETE.** The evidence and this readable four-row delta are published in GitHub. **The current Excel workbook and main coverage register have not yet been updated.** The next action is **ISA-03A-PUBLISH only**, applying these saved decisions and verifying the integrated workbook/view. Do not repeat these four source reviews or begin ISA-03B.

[Exact four-entry evidence](ISA03A_Status_Name_State_Evidence_07NOV2026.json) · [Current progress](ISA_Correction_Status_07NOV2026.json) · [Current PITON](PITON_ISA_Coverage_Correction_07NOV2026.md) · [Last integrated workbook — ISA-02](ISA_Correction_Review_ISA02_07NOV2026.xlsx).

## Four source decisions

All four properties are in **ISA Data Model Specification, release 6.0 revision 12, 31 October 2023, §3.1, printed p.14 / PDF p.29**. They are core entries, not marked extensions. Each supports a specific candidate information row rather than an inappropriate substitute for an existing identifier, mode or observation-time row.

| Native ISA property | Candidate information element | Source-supported meaning | Essential distinction |
| --- | --- | --- | --- |
| Maximum Status Interval | Maximum interval between component Status reports | Upper bound on the interval between Status transmissions; the ICD relates the upper bound to heartbeat reporting. | Not the sensor sampling period, an observation resultTime, or proof of delivery/liveness. |
| Minimum Status Interval | Minimum interval between component Status reports | Lower bound on transmission spacing; changes occurring during the interval are cached for the next permitted Status send. | Not a measurement period or a guarantee that every intervening state transition is retained as a history. |
| Name | Changeable component display name | A human-friendly component name that may be reassigned or changed. | Not UCI, manufacturer, product model or serial number; no uniqueness requirement is inferred. |
| Operating State | Reported component operating condition | The current condition of the component itself, explicitly separate from its ISA lifecycle state. | Not automatically the selected operating mode, capability readiness or power state. Keep the earlier Camera Mode correspondence. |

Candidate IDs are **ISA-C-078, ISA-C-079, ISA-C-081 and ISA-C-082**. The fit is direct to these deliberately specific proposed information elements, not an ISA-authorized equivalence assertion or an adopted DIM requirement. No case data or non-ISA donor cell is filled by inference.

## Supporting definitions and behavior checked

`Secs` (DMS §4.2, printed p.55 / PDF p.70) is floating-point seconds for an interval, represented with millisecond resolution. `String` is defined in §4.1, printed p.50 / PDF p.65. These are source types, not source-supplied values for any of our equipment cases.

`General State` (printed pp.93–94 / PDF pp.108–109) contains required `code`, optional machine-readable component-specific `subcode`, and optional human-readable component-specific `details`. Its sealed `General Code` enumeration (printed p.79 / PDF p.94) contains **FAILURE, FAULT, OK, UNINITIALIZED and WARNING**. The source differentiates halted operation, limited operation, acceptable behavior, a non-error pre-operational condition, and a warning while operation can continue.

ISA Interface Control Document 6.0r5, §6.5, printed pp.21–22 / PDF pp.29–30, describes Status publication on significant changes and explains the lower and upper delivery-frequency bounds. These paragraphs were checked alongside the DMS definitions. Four supporting type definitions were inspected/reused for this batch; their later full catalogue review is not marked complete or counted as additional primary entries.

Original indexed source text was readable. A requested PDF page image could not be returned because its raw-byte backing path was unavailable; no visual source-page inspection is claimed. The meanings above are established by the original definitions, not by assumptions drawn from their names.

## Coverage and unchanged work

| Measure | Result |
| --- | ---: |
| Primary entries assigned to ISA-03A | 4 |
| Primary entries reviewed | 4 |
| Source-supported outcomes | 4 |
| New interpretation questions | 0 |
| Additional proposed information rows | 4 |
| Current integrated register, before applying this batch | 49 reviewed entries |
| Completed source reviews including this saved batch | 53 entries |
| New non-ISA donor or equipment changes | 0 |

The current integrated workbook remains the ISA-02 workbook. It has 76 information/review rows; these four candidates would make 80 after integration, provided the continuation confirms the IDs do not duplicate an existing candidate. The original 58 primary donor records, 73 equipment-evidence statements, identity corrections, Camera Mode comparison and the two previous record-local questions remain unchanged.

## Exact next action — integration/publication only

The current workbook is present in GitHub, but its binary did not reach the local workspace through the attempted download routes. Direct runtime access failed on DNS resolution; the separate download service did not resolve the public raw-file URL. This is a specific transfer/integration issue, not a finding that the workbook is missing, GitHub writing is unavailable, or ISA source review must restart.

**ISA-03A-PUBLISH** must reuse the current workbook and established publication path, incorporate the four decisions into the current fourteen-column review and coverage register, update evidence/summary counts without double-counting supporting types, inspect the changed workbook areas, publish, and read back the actual commit. No new source-property review is authorized during that action. The result must keep the four source examples left, the foundational standards together, and proposed DIM rightmost.

Once integration passes, mark ISA-03A fully delivered and identify ISA-03B as next. Until then, report the precise states: **source review complete; evidence published; workbook/register integration pending**. These states do not reopen ISA-01, ISA-02 or the four source decisions recorded here. No new GitHub Actions or workbook-validation PASS is claimed for this text-only checkpoint.
