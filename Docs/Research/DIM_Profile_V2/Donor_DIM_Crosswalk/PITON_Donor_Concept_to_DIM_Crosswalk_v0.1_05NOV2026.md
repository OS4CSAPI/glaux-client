# Current Profile Rewrite checkpoint

Updated 17 November 2026, America/New_York, Profile Rewrite 57. Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`; verify live HEAD. Read [AGENTS.md](../AGENTS.md) once. This is the sole current status and next-action record.

## Active scope and evidence

The owner's latest **Profile Rewrite 57 Proceed authorizes Step 2 PA-DIM assessment and delivery** under the [three-step corrective plan](PLAN_OPC_UA_Devices_PADIM_Corrective_Assessment_17NOV2026.md). Step 1 Devices is complete and published. Step 2 assesses all 477 current PA-DIM cells, the 40 native finding groups and 22 prior additions against the fixed original corpus, integrating warranted corrections and new meanings. Its working baseline is `7d2593a4be7150a487e3960cad532ee970e60a67`, preserved by [archive/pre-padim-correction-17nov2026](https://github.com/OS4CSAPI/glaux-client/tree/archive/pre-padim-correction-17nov2026).

Step 2 assessment is complete and saved in the existing [PA-DIM ledger](OPC_UA_PADIM_Source_Coverage.json), `corrective_review`, with integration pending. All 477 starting cells have dispositions; 29 existing cell changes, two definition enrichments and one signal-compensation candidate are approved for integration. The 40 earlier native findings, 142 supporting-definition groups and 22 prior additions are reconciled; inventory entries without original examination remain explicitly unread. No Step 2 master/workbook correction is delivered yet. Reuse adequate original evidence, inspect disputed/omitted meanings and retain actual source-contact limits. PA-DIM's declared Devices 1.04 dependency must not be replaced with the separate Devices 1.05 assessment. Step 3 joint closeout remains a subsequent bounded step. No new donor, source-limit acceptance, model adoption, client or deployment work follows automatically.

## Verified checkpoint

**Published Step 1 delivery: `b8d585054f55fc6477dc7bd1e08b667047b7da8e`, tree `73a92299addf02430ba3c1a227631c74c4af46a6`.** The fetched remote tree exactly matches the saved local delivery (`0b34260`); all 13 changed file blobs match. A fresh download of the published workbook matches the SHA256 below. [Crosswalk check PASS](https://github.com/OS4CSAPI/glaux-client/actions/runs/44124001352); [same-workbook publisher PASS](https://github.com/OS4CSAPI/glaux-client/actions/runs/44124001318). The verified Step 1 receipt is `7d2593a4be7150a487e3960cad532ee970e60a67`; this Step 2 startup checkpoint changes only the PITON. Verify live HEAD.

Planning baseline `07704a67a2405eaccc055f5ceb3ddac3adeb63cb` is preserved by [archive/pre-devices-correction-17nov2026](https://github.com/OS4CSAPI/glaux-client/tree/archive/pre-devices-correction-17nov2026). Assessment checkpoint `958cd3a` and integration checkpoint `d2c876dd` remain locally preserved.
Earlier workbook repair: `866cc39efaab24b7130af97710f00f17779871ee`, receipt `6cd94b3d4016af8a3807ca7aba1e1dc68152ae99`. It corrected 102 out-of-order rows, removed three orphan table definitions/relationships, and unfroze the first four columns. All original 30,863 cells/styles survived that repair. The new research corrections intentionally change the recorded cells after that preserved baseline. [Pre-repair archive](https://github.com/OS4CSAPI/glaux-client/tree/archive/pre-opc-workbook-repair-17nov2026) and M00/M01 remain.

## Master and workbook

[Same editable Excel](Master_Donor_Concept_to_DIM_Crosswalk.xlsx): **477 information rows; 506×17=8,602 comparison cells; 876 classifications (768 colored/108 prior held)**. One new specialized update-key row; 39 existing Devices text/status changes, including all 22 later PA-DIM rows. The other donor columns are preserved; the new PA-DIM position explicitly awaits Step 2. Canonical JSON, both CSV mirrors and both readable comparisons match saved values. The 336 corrected internal row locators reflect the existing grid; no rows were reordered.

Current saved SHA256: **40231f8eb3335aa2f7066cfd978d66d3506d34d46e1c71c82d345f4c95063fe3**. Prior repaired baseline SHA256: `50690f1a6af7d0604de0d93f8b61aae9c2433d3e99c885d918567b2ceaca1341`. Same 26 sheets; first four columns scroll and two header rows remain frozen. Historical source-specific snapshots remain historical rather than silently overwritten.

## Verification and publication

`python -B scripts/integrate_sosa_opportunity_checkpoint.py --verify` passes ordered/unique cells, style validity and table relationships; exact recorded changes and unaffected-content preservation; all saved grid values/fills and both CSV/readable mirrors; prior source evidence and M00/M01. The existing workflow routes the new checkpoint to this verifier. No new script or workflow is added to the repository.

Fresh Microsoft Excel for the web verification PASS on the exact 477-row file: it reopened without WORKBOOK REPAIRED; F506 shows the amber new candidate, F468 the corrected blue target mode, and G506 its explicit Step 2 pending status. Horizontal scrolling places F at the left while A-D move off screen and header rows 1-2 stay fixed. Saved evidence: [new row and scrolling](Workbook_Verification/Excel_Web_Devices_Step1_New_Row_17NOV2026.jpg), [target mode](Workbook_Verification/Excel_Web_Devices_Step1_Mode_17NOV2026.jpg). The Devices ledger `corrective_review.verification.application_evidence` records the candidate and exact file hashes. Desktop Excel and runtime conformance are not claimed. Canonical publication/readback is complete; the Devices ledger `corrective_review.publication` records the receipt and checks.

## Holds and owner decisions

All twelve Devices source limits and fourteen prior PA-DIM questions remain. New PA-C2-Q015 (two name-change cells) and PA-C2-Q016 (recovery-advice cell) retain source-detail holds because the inspected legacy routes redirect to Devices 1.05; pinned 1.04 declarations do not establish those details. Preserve PA-DIM's Devices 1.04 dependency and source limits, ISA/SOSA/SAPIENT/AAS/case holds, prior accepted work, and SAPIENT bounded-PARTIAL standing. Step24, Steps35–39 and named-version Step40 remain gated. No automatic M02; no donor-exclusive contribution claim or ranking by counts.

## Interrupted work

Checkout: `/workspace/scratch/acb9b2ea127e/glaux-client`, local branch `codex/profile-rewrite-57-padim`. PA-DIM cache: `/workspace/scratch/705ccec1d857/padim`; Devices cache: `/workspace/scratch/eb7bba69536f/opc-di`. Step 2 baseline copies and temporary assessment records are under `/tmp/profile57-padim`: `baseline.json`, `baseline.xlsx`, and the developing `native_review.json`, `positive_review.json`, `negative_review.json`. Native review owns source/opportunity reconciliation; positive review owns 72 positive/related/origin cells; negative review owns the other 405 cells. The combined approved assessment is `/tmp/profile57-padim/approved-review.json` and is saved in the PA-DIM ledger overlay. This assessment-only checkpoint is intended for `checkpoint/padim-corrective-assessment-17nov2026`; remote save is not yet verified. It is incomplete backup, not canonical delivery. Integrate the approved changes, verify and publish within the existing Step 2 authorization.

No Step 1 delivery remains interrupted. Its comparison explanation labels the earlier 476-row PA-DIM results as historical. The old `codex/profile-rewrite-56` remote candidate contains only a workbook increment and is not the coherent delivery.

## Next action and stop

Complete the already authorized Step 2 assessment, integration, verification, canonical publication/readback and explanation, then stop for Proceed. The subsequent bounded action is Step 3 joint closeout under the same corrective plan. Do not begin Step 3 on Step 2 authorization or schedule another general donor review.

## History

Exact originals and previous statuses remain in Git and named archives. Retrieve only for a concrete evidence question.
