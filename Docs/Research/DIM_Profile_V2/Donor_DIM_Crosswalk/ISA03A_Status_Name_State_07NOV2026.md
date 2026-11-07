# ISA-03A — Status intervals, Name and Operating State

**7 November 2026 · ISA-03A COMPLETE: four of four source reviews and workbook integration are complete.** The [current workbook](ISA_Correction_Review_ISA03A_07NOV2026.xlsx), [horizontal comparison](ISA_Correction_Review_ISA03A_07NOV2026.md) and coverage register now incorporate these exact decisions. Next owner “proceed”: **ISA-03B only**.

[Exact four-entry evidence](ISA03A_Status_Name_State_Evidence_07NOV2026.json) · [Current progress](ISA_Correction_Status_07NOV2026.json) · [Current PITON](PITON_ISA_Coverage_Correction_07NOV2026.md) · [Current integrated workbook](ISA_Correction_Review_ISA03A_07NOV2026.xlsx).

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

| Measure | Integrated result |
| --- | ---: |
| Saved ISA-03A primary decisions integrated | 4 of 4 |
| Additional candidate rows | 4 |
| Total reviewed primary catalogue entries | 53 |
| Source-supported primary outcomes | 51 |
| Existing source-definition questions | 2 |
| Unique supporting definitions recorded | 47 |
| Total information/review rows | 80 |
| Non-ISA donor/equipment values changed | 0 |
| New source reviews during integration | 0 |

The [current workbook](ISA_Correction_Review_ISA03A_07NOV2026.xlsx) and [full horizontal view](ISA_Correction_Review_ISA03A_07NOV2026.md) contain all four candidates under the existing Identity and contacts, Operating and readiness states, and Communications groups. All previous rows, the original 58 primary donor records and 73 equipment-evidence statements remain unchanged. The Camera Mode correspondence remains exactly as before; Operating State has its own candidate row.

The prior ISA-02 workbook is retained as history. The four source decisions were not re-researched. Supporting type reads do not complete their later full catalogue review. The publication record provides exact output hashes and the verification-run URL.

## Publication closeout and next exact action

**Integration and publication COMPLETE.** The original transfer issue has been resolved through a read-only GitHub Actions artifact of the exact repository inputs. The updated workbook was edited with the existing artifact_tool workflow, the changed summary and row areas were visually checked, and the source ledger/CSV/Markdown were synchronized.

[Publication record](ISA03A_Publication_Record_07NOV2026.json) records the actual files and read-only verification. No historical workbook, original evidence ledger, non-ISA source fact, Profile rule, runtime or equipment value was changed.

**Next owner “proceed”: ISA-03B only** — Owner, Parameter Version, Program of Record, Software Version, Specification Version and Support. No ISA-03B review was performed in this publication action.
