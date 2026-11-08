# Current PITON — Image-adjustment command review COMPLETE

**7 November 2026 · ISA-COMMANDS-IMAGE-ADJUSTMENTS COMPLETE. Next owner “proceed”: ISA-COMMANDS-IMAGE-SETTINGS only — the six Change commands named below.**

Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. GitHub is authoritative.
[Comparison](ISA_Correction_Review_07NOV2026.md) · [Command evidence](ISA_Command_Catalogue_Evidence_07NOV2026.json) · [Coverage](ISA_Coverage_Register_07NOV2026.json) · [Progress](ISA_Correction_Status_07NOV2026.json) · [Plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Completed workbook snapshot](ISA_Correction_Review_Observables_07NOV2026.xlsx) · [Workbook publication record](ISA_Observables_Publication_Record_07NOV2026.json) · [Lessons](LESSONS_Donor_Review_Process.md).

## Completed checkpoint and preservation
All 91 property and 39 observable reviews and their consolidated workbook remain COMPLETE. **Six command entries 164–168,171 are now source-reviewed and published: all core, all supported, no new question.** Command coverage6/96;90 remain in the existing inventory. Current totals136 reviewed/132 supported/four unchanged property questions;163 information/review rows (original31 +128 supported candidates +four questions);124 unique supporting definitions.

The current Excel is the completed property/observable snapshot, not a failed publication:130 reviewed primary entries,157 information/review rows,SHA256 `68deb7b41c2fcfbf3350f7260929c560cfb81963246acaa0d3f134f1281b27a6`. New command decisions are in the current GitHub comparison and command evidence; update Excel at the next catalogue/substantial-section checkpoint. Preserve all prior grid values,58 non-ISA donor records,73 case statements,480 source entries,279 blocks,31 original targets and25 findings. No completed source review or workbook task is to be repeated.

## Six commands and their exact semantics
Adjust Brightness/Contrast/Gain increase or decrease their named settings. Adjust Focus narrows or widens focus in the source wording; do not convert this to near/far distance or field-of-view. Adjust Iris Size increases/decreases iris size without an invented f-number. Adjust Zoom zooms in/out without an inferred magnification or optical/digital distinction.

Each has required direction:Linear Direction, optional rate:Percent default100% of maximum adjustment speed, and optional duration:Secs. **Omitted duration means continue until a limit unless superseded; explicit zero means immediately stop adjusting.** The source's 0%/100% setting endpoints are not the rate parameter. Percent's generic definition does not impose a hard0–100 validation bound. Secs requires millisecond resolution. No unsupported negative-duration behavior is added.

Linear Direction is a sealed NEGATIVE/NONE/POSITIVE enum. Its global NONE value is retained, but these command paragraphs give POSITIVE/NEGATIVE behavior; do not invent NONE as an alternate guaranteed stop contract. None of the six entries declares a command-specific Results table; do not turn that into a claim that there is no protocol acknowledgement. Command definition, issued request, actual execution and reported result remain distinct. General Request/Response aggregate-row review is still assigned, not completed by these six definitions.

Original DMS6.0r12 §3.3 printed23–27/PDF38–42 was read and page images inspected, including Focus and Iris cross-page continuations. Following heading on43 and Linear Direction on95 were read as text; Percent69 and Secs70 checked. One new supporting definition:Linear Direction. Prior exact-edition Percent/Secs/Float evidence reused. Only the six assigned primary entries advance; nearby Adjust Level/Power and the generic Level question remain untouched. Source ID `file_00000000ca1c81f48a3ccd49273425f8`; recover by exact registered title/revision. A failed raw export is not absent source text.

## Next six only and same delivery
**Next “proceed” = ISA-COMMANDS-IMAGE-SETTINGS: Change Brightness184, Change Contrast186, Change Focus190, Change Gain192, Change Iris Size193, Change Zoom205.** These are unreviewed inventory assignments, not conclusions about their parameters. Read complete source definitions and required dependencies, compare with saved Adjust semantics, update cumulative command evidence/coverage/readable comparison and concise current routing, then verify the actual GitHub output. Do not run the whole remaining90 commands or export a workbook per group.

No new per-group report, publisher or workflow. No other donor, model adoption, Profile/UML, server/client/deployment or physical command changes. Existing four questions (Level Q001,Link Loss Q002,Orientation frame Q003,Signal Strength Ratio Q004) remain local and unchanged. All case examples retain documentary/historical standing; no native ISA control capability or measured new state is asserted.

[Previous completed workbook checkpoint](https://github.com/OS4CSAPI/glaux-client/blob/7cf47c489dec32464c95c97a795468726592e7b2/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_ISA_Coverage_Correction_07NOV2026.md) preserves history; its older next-step direction is superseded here.
