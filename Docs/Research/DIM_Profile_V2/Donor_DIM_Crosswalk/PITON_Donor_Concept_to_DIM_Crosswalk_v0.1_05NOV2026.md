# Current Profile Rewrite checkpoint

Updated 17 November 2026, America/New_York, Profile Rewrite 56. **Workbook repair is published and verified, including Microsoft Excel for the web.** Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`; verify live HEAD. Read [AGENTS.md](../AGENTS.md) once. This is the sole current status/next-action record.

## Active scope and evidence

The owner's Profile Rewrite 55 request authorized fixing Excel's repair warning and unfreezing the first four Master Crosswalk columns. **Profile Rewrite 56 Proceed** authorizes finishing the interrupted repair, preventive checks, Excel verification, canonical publication and this checkpoint. Preserve two frozen header rows and all research content/classifications. No donor transition, source-limit acceptance, model adoption, client or deployment work follows automatically.

The separate owner concerns about Devices and PA-DIM coverage, classification accuracy and fair opportunity remain open. The subsequent Profile Rewrite 56 Proceed authorized documenting/publishing the [finite corrective plan](PLAN_OPC_UA_Devices_PADIM_Corrective_Assessment_17NOV2026.md). Planning is complete; execution has not started. Three planned execution steps: Devices assessment/delivery, PA-DIM assessment/delivery, joint closeout/explanation. Each Proceed authorizes one step; internal checkpoints do not add gates. The repaired-file result does not establish research completeness.

## Verified checkpoint

**Published repair: `866cc39efaab24b7130af97710f00f17779871ee`, tree `08487eedf6b79d3f5a81a20a66d10b7648940621`.** All six affected remote blobs match the verified local artifacts, and a fresh download of the published workbook matches the recorded SHA256. [Crosswalk check PASS](https://github.com/OS4CSAPI/glaux-client/actions/runs/44101967322); [same-workbook publisher PASS](https://github.com/OS4CSAPI/glaux-client/actions/runs/44101967345). This receipt update changes metadata and the PITON only.

The pre-repair canonical HEAD is `8516d932bcc7e0284575176bdb2012038ef2b339`, preserved by [archive/pre-opc-workbook-repair-17nov2026](https://github.com/OS4CSAPI/glaux-client/tree/archive/pre-opc-workbook-repair-17nov2026). Earlier pre-Devices/pre-PA-DIM archives and manual M00/M01 remain; no automatic M02.

The initial order-only candidate `537671fa338298ae60e574e83280d3fb004adb34` still triggered Excel's repair warning. Verified candidate **`1b5cf34a7f01f0666c101ab86d5609080f4aa250`**, on `codex/profile-rewrite-56`, also removes three dangling table relationships and their already unreferenced definitions. Both active tables remain. It corrects cell order in 101 Master Crosswalk rows and one DIM Register row and changes Master Crosswalk to row-only freezing at A3.

**All 30,863 existing cell records and styles across all 26 sheets are preserved.** Only worksheet cell order, the requested pane, three orphan table definitions/relationships and their content-type entries change. ZIP recompression alters no contained part bytes. Source meanings, research decisions, cases, donor order, row identities, layouts and holds are unchanged. Current snapshot count labels are corrected to the already published 476-row/17-column PA-DIM result; no rows are added by this repair.

## Master and workbook

[Same editable Excel](Master_Donor_Concept_to_DIM_Crosswalk.xlsx): **476 information rows; 505×17=8,585 comparison cells; 870 unchanged classifications (762 colored/108 held).** All 476 Devices and PA-DIM information cells are explicit. Canonical JSON, both CSV and both readable mirrors match saved values; zero value/fill/mirror lag.

Repaired workbook SHA256: **50690f1a6af7d0604de0d93f8b61aae9c2433d3e99c885d918567b2ceaca1341**. The [PA-DIM ledger](OPC_UA_PADIM_Source_Coverage.json), key `integration.workbook_structure_repair`, owns exact repair scope, removed parts, checks, Excel observations and publication receipt.

## Verification and publication

`python -B scripts/integrate_sosa_opportunity_checkpoint.py --verify` passes structural checks, exact pre-repair cell/style preservation, existing source/preservation checks, mirror/fill parity and M00/M01 preservation. The strengthened check rejects both the original workbook's out-of-order F7 and the order-only candidate's dangling table relationship. Existing publisher/check workflows use this command; no extra workflow is introduced.

Microsoft Excel for the web opened the exact candidate without WORKBOOK REPAIRED. F8 shows its text and blue fill; F204 has its explicit status; G8's PA-DIM text is visible. Horizontal scrolling places G at the left with A-D off screen while rows 1-2 stay fixed. [Saved Excel evidence](Workbook_Verification/Excel_Web_Repaired_Workbook_17NOV2026.jpg). Desktop Excel is not tested; programmatic full-cell parity is distinct from sampled UI viewing.

## Holds and owner decisions

PA-DIM research/integration remains the previously delivered result: 40 finding dispositions, 22 additions (13 common/nine specialized), and 454 prior-row assessments. No source research is repeated. Preserve publisher-date, external-dictionary, unit-conversion, label/reference and overview-figure limits; Devices, ISA, SOSA, SAPIENT, AAS and case holds; previous SOSA/AAS acceptance and SAPIENT bounded-PARTIAL standing. Step24, Steps35–39 and named-version Step40 remain gated. Unrelated historical register/link errors are outside this repair.

## Interrupted work

No workbook or research delivery remains interrupted. Current checkout: `/workspace/scratch/acb9b2ea127e/glaux-client`, local branch `codex/profile-rewrite-56`. The repaired workbook remains the published verified artifact above. The planning follow-up changes only this PITON and the linked corrective plan; no workbook or research correction is performed. Its baseline is the verified repair receipt `6cd94b3d4016af8a3807ca7aba1e1dc68152ae99`; verify the live HEAD and both planning files on recovery. The original Profile Rewrite 55 checkout and order-only guard edit remain at `/workspace/scratch/9e6e4c6747b1/glaux-client` for preservation, not as the current deliverable. Source cache: `/workspace/scratch/705ccec1d857/padim`.

## Next action and stop

Workbook repair and corrective planning are complete. Stop for Proceed. The next bounded action is Step 1 of the [corrective plan](PLAN_OPC_UA_Devices_PADIM_Corrective_Assessment_17NOV2026.md): assess Devices native opportunity, all 476 current donor cells and classifications, preserve a pre-correction snapshot, integrate justified changes into every canonical format, verify/publish, and explain results. Do not start PA-DIM Step 2 in the same authorization.

## History

Earlier status and exact originals remain in Git and the named archives. Retrieve only for a concrete evidence need.
