# Current Profile Rewrite checkpoint

Updated 17 November 2026, America/New_York, Profile Rewrite 60, corrective Step 3. Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`. Verify live HEAD; follow [AGENTS.md](../AGENTS.md).

## Active scope and evidence

The owner's Proceed after `d4a40e4` authorizes Step 3, the final step of the [Devices and PA-DIM corrective plan](PLAN_OPC_UA_Devices_PADIM_Corrective_Assessment_17NOV2026.md). The finite joint comparison accounts for 478 current cells per donor (956 positions), four correction dispositions and five retention/count-scope dispositions. It adds no rows or definitions. The [comparison narrative](Donor_Native_High_Level_Information_Groupings_Comparison.md#devices-and-pa-dim-joint-corrective-closeout--17-november-2026) gives the complete plain-English explanation, rationale, source references and recommendation.

The master and both source ledgers record the identical `joint_corrective_closeout`: exact old/new texts, source locators, frozen discrepancies, original-source contact, classification intersections, saved checks and publication state. [Devices ledger](OPC_UA_Devices_Source_Coverage.json) · [PA-DIM ledger](OPC_UA_PADIM_Source_Coverage.json).

## Master and workbook

The [same editable workbook](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) has 478 information rows, 507 grid rows, 17 columns, 8,619 grid values and 26 sheets. Devices has 97 common/5 specialized/376 explicit white cells; PA-DIM has 71/12/395. There are 792 colored comparisons; the 108 prior held classifications remain. Both CSV mirrors and both readable comparisons agree with the master and saved worksheet.

Current workbook SHA-256: `1eaba51990e7cd8df28f0c9fb1d4fd707e5d9e740ddb1762b9208d822a0d5f30` (502,268 bytes). Only F190 (Devices cancellation), G82 (inherited typed result), G95 (declared request) and G96 (declared invocation outcome) changed text/fill, all to qualified common candidates. Current PA-DIM snapshot counts were repaired to 83 colored and 478 explicit cells; historical assessment counts remain scoped to their original checkpoints.

## Verified checkpoint

The saved joint delivery passed the current verifier. Exactly four values/fills changed; all other cells/styles/package parts, row order, row-only freezing, 26 sheet identities and M00/M01 bytes are preserved. Only `xl/worksheets/sheet2.xml` changed inside the workbook. The actual saved workbook's four changed ranges rendered with complete wrapped text and correct blue fills: [F190](Workbook_Verification/Artifact_Render_Devices_PADIM_Joint_F190_17NOV2026.png), [G82](Workbook_Verification/Artifact_Render_Devices_PADIM_Joint_G82_17NOV2026.png), [G95](Workbook_Verification/Artifact_Render_Devices_PADIM_Joint_G95_17NOV2026.png), [G96](Workbook_Verification/Artifact_Render_Devices_PADIM_Joint_G96_17NOV2026.png).

Earlier Excel-for-web evidence is reused for unchanged structure. These new images are Artifact Tool renders of the actual workbook, not a new native Excel application check. Automated checks do not establish source completeness, adoption or runtime behavior.

## Holds and owner decisions

PA-DIM 1.02.0 declares Devices 1.04.0; the independent Devices donor is 1.05.0. PA-C2-Q015/Q016 retain three white source-detail holds on changeable/requested names and recovery advice. All 12 Devices limits, all 14 earlier PA-DIM questions, the two later questions, DI-Q005's state contradiction and earlier ISA/SOSA/SAPIENT/AAS/case holds remain. PA-DIM's historical inventory still marks 952 of 1,059 model entries unread; targeted reads do not establish a full recursive audit. Owner acceptance of bounded source coverage, model adoption, Step 24, Steps 35–39 and named-version Step 40 remain separate decisions.

## History

The exact [pre-joint checkpoint](https://github.com/OS4CSAPI/glaux-client/blob/d4a40e4c58fe355f4b14d80b807522341e5e8065/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md) preserves Step 2's publication receipt and the chat-length investigation. `d4a40e4` is the joint baseline; its workbook hash is `d3882d2f0db02ea829e07f59c849b785184dbed211635258c31165479f282dce`. Step 1 changed 39 cells and added one row; Step 2 changed 29 cells, clarified two definitions and added one row. These per-step counts are not a distinct-cell total.

## Interrupted work

Local Step 3 implementation is complete in `/workspace/scratch/8d381dcd4fda/glaux-step3`; canonical publication is pending. Resume the existing delivery if interrupted; do not restart either donor or create another audit.

## Verification and publication

Current evidence checkpoint: `DEVICES_PADIM_JOINT_3_SAVED_VERIFIED`. Run `python -B scripts/check_dim_crosswalk_step06.py --recovery-only` and `python -B scripts/integrate_sosa_opportunity_checkpoint.py --verify` through the output guard. The updated current-checkpoint workflow uses that route; prior Step 1/2 verifier bodies are unchanged. The joint publication receipt is explicitly pending until remote files, workbook bytes and affected checks are verified. Unrelated pre-existing document-register issues remain recorded in the pre-joint checkpoint.

## Next action and stop

Finish and verify the already-authorized Step 3 publication, then stop for the owner's decision on the completed joint closeout with retained source limits. No automatic fourth review round, next donor or DIM/Profile authoring is authorized. Continue to use the enforced output guard; it reduces avoidable output but does not diagnose or fix ChatGPT's platform limit.
