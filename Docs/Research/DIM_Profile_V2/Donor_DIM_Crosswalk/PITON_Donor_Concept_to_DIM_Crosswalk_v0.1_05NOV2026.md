# Current Profile Rewrite checkpoint

Updated 17 November 2026, America/New_York, Profile Rewrite 57. Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`; verify live HEAD. Read [AGENTS.md](../AGENTS.md) once. This is the sole current status and next-action record.

## Active scope and evidence

The owner's Profile Rewrite 56 Proceed authorized Step 1 Devices assessment and delivery; Profile Rewrite 57 Proceed resumes its interrupted final verification/publication under the [three-step corrective plan](PLAN_OPC_UA_Devices_PADIM_Corrective_Assessment_17NOV2026.md). Complete integration, verification and publication within that authorization; no internal approval gates. Step 2 PA-DIM and Step 3 joint closeout remain subsequent bounded steps. No new donor, source-limit acceptance, model adoption, client or deployment work follows automatically.

The [Devices ledger](OPC_UA_Devices_Source_Coverage.json), key `corrective_review`, records all 476 starting cells, 39 corrected cells, the new `OPCDI-UPDATE-KEY` candidate, original-source locators, retained evidence and exact limits. [Comparison explanation](Donor_Native_High_Level_Information_Groupings_Comparison.md), opening section, explains what changed and why. Prior ledger entries remain historical evidence; the corrective overlay governs current Devices decisions.

## Verified checkpoint

Planning baseline: **07704a67a2405eaccc055f5ceb3ddac3adeb63cb**, preserved by [archive/pre-devices-correction-17nov2026](https://github.com/OS4CSAPI/glaux-client/tree/archive/pre-devices-correction-17nov2026). It contains the verified repaired workbook and published corrective plan. Local assessment checkpoint: `958cd3a`; integrated checkpoint: `d2c876dd185cef71c31a4deab46eae2323a652f0`. The exact workbook was staged at remote candidate `8118923152276187aa299b4108dadfaf4ef54441` on `codex/profile-rewrite-56`; that candidate contains only the workbook increment and is not the coherent canonical delivery. Canonical publication/readback is pending. Do not confuse local completion with canonical delivery.

Earlier workbook repair: `866cc39efaab24b7130af97710f00f17779871ee`, receipt `6cd94b3d4016af8a3807ca7aba1e1dc68152ae99`. It corrected 102 out-of-order rows, removed three orphan table definitions/relationships, and unfroze the first four columns. All original 30,863 cells/styles survived that repair. The new research corrections intentionally change the recorded cells after that preserved baseline. [Pre-repair archive](https://github.com/OS4CSAPI/glaux-client/tree/archive/pre-opc-workbook-repair-17nov2026) and M00/M01 remain.

## Master and workbook

[Same editable Excel](Master_Donor_Concept_to_DIM_Crosswalk.xlsx): **477 information rows; 506×17=8,602 comparison cells; 876 classifications (768 colored/108 prior held)**. One new specialized update-key row; 39 existing Devices text/status changes, including all 22 later PA-DIM rows. The other donor columns are preserved; the new PA-DIM position explicitly awaits Step 2. Canonical JSON, both CSV mirrors and both readable comparisons match saved values. The 336 corrected internal row locators reflect the existing grid; no rows were reordered.

Current saved SHA256: **40231f8eb3335aa2f7066cfd978d66d3506d34d46e1c71c82d345f4c95063fe3**. Prior repaired baseline SHA256: `50690f1a6af7d0604de0d93f8b61aae9c2433d3e99c885d918567b2ceaca1341`. Same 26 sheets; first four columns scroll and two header rows remain frozen. Historical source-specific snapshots remain historical rather than silently overwritten.

## Verification and publication

`python -B scripts/integrate_sosa_opportunity_checkpoint.py --verify` passes ordered/unique cells, style validity and table relationships; exact recorded changes and unaffected-content preservation; all saved grid values/fills and both CSV/readable mirrors; prior source evidence and M00/M01. The existing workflow routes the new checkpoint to this verifier. No new script or workflow is added to the repository.

Fresh Microsoft Excel for the web verification PASS on the exact 477-row file: it reopened without WORKBOOK REPAIRED; F506 shows the amber new candidate, F468 the corrected blue target mode, and G506 its explicit Step 2 pending status. Horizontal scrolling places F at the left while A-D move off screen and header rows 1-2 stay fixed. Saved evidence: [new row and scrolling](Workbook_Verification/Excel_Web_Devices_Step1_New_Row_17NOV2026.jpg), [target mode](Workbook_Verification/Excel_Web_Devices_Step1_Mode_17NOV2026.jpg). The Devices ledger `corrective_review.verification.application_evidence` records the candidate and exact file hashes. Desktop Excel and runtime conformance are not claimed. Canonical publication/readback is pending.

## Holds and owner decisions

All twelve Devices source limits remain. Publisher document197 was retried without successful retrieval. Preserve PA-DIM's Devices 1.04 dependency and source limits, ISA/SOSA/SAPIENT/AAS/case holds, prior accepted work, and SAPIENT bounded-PARTIAL standing. Step24, Steps35–39 and named-version Step40 remain gated. No automatic M02; no donor-exclusive contribution claim or ranking by counts.

## Interrupted work

Checkout: `/workspace/scratch/acb9b2ea127e/glaux-client`, local branch `codex/profile-rewrite-56`. Devices source cache: `/workspace/scratch/eb7bba69536f/opc-di`; PA-DIM cache: `/workspace/scratch/705ccec1d857/padim`. Step 1 research, integration and application verification are complete; the coherent delivery awaits canonical publication and readback. The comparison explanation now labels the earlier 476-row PA-DIM results as historical, preserving their substance. Temporary authored inputs and preservation builder: `/tmp/profile56-devices`. Original Profile Rewrite 55 checkout remains at `/workspace/scratch/9e6e4c6747b1/glaux-client`; do not use its obsolete workbook/guard as current.

## Next action and stop

Finish the already authorized Step 1 canonical publication/readback and explanation, then stop for Proceed. Next is Step 2 PA-DIM assessment and delivery, including the newly added update-key row, under the same corrective plan. Do not begin Step 2 on Step 1 authorization or create another general Devices review round.

## History

Exact originals and previous statuses remain in Git and named archives. Retrieve only for a concrete evidence question.
