# Current Profile Rewrite checkpoint

Updated 17 November 2026, America/New_York, Profile Rewrite 60. Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`. Verify live HEAD. Read [AGENTS.md](../AGENTS.md) once.

## Active scope and evidence

The owner’s Profile Rewrite 57 and 58 Proceeds cover Step 2 of the [Devices and PA-DIM corrective plan](PLAN_OPC_UA_Devices_PADIM_Corrective_Assessment_17NOV2026.md); Profile Rewrite 59 authorized its publication receipt. Profile Rewrite 60 explicitly authorizes investigating and fixing chat-length disruption. The [PA-DIM source ledger](OPC_UA_PADIM_Source_Coverage.json), under `corrective_review`, records dispositions for all 477 starting cells, 40 native finding groups, 142 supporting definition groups and 22 prior additions. Step 2 corrected 29 existing PA-DIM cells, expanded two candidate definitions and added one provisional row for a signal’s compensation method and reference conditions. The [comparison narrative](Donor_Native_High_Level_Information_Groupings_Comparison.md) explains the source meanings and distinctions.

## Master and workbook

The [editable workbook](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) contains 478 information rows. All 8,619 comparison-grid values agree with the master JSON, both CSV files and both readable comparisons. PA-DIM has 68 blue common candidates, 12 amber specialized candidates and 398 white cells with explicit statuses. The master records 788 colored comparisons and 108 earlier held classifications. Workbook SHA-256 is `d3882d2f0db02ea829e07f59c849b785184dbed211635258c31165479f282dce`.

## Verified checkpoint

The [integrated candidate](https://github.com/OS4CSAPI/glaux-client/commit/ea119fa73e95c2c5cd08637572255e67541746cc) preserves the recovered local tree at `c4d8390`. Excel for the web opened its exact workbook without a repair notice. G507 showed the blue compensation candidate, its Devices counterpart was readable in F507, and G82 showed the narrower method-result mapping in white. Headers stayed visible while scrolling. The saved-file checks cover the full grid and preservation across 26 sheets. Desktop Excel and runtime behavior were outside this check. [Compensation row](Workbook_Verification/Excel_Web_PADIM_Step2_Compensation_17NOV2026.jpg) · [Method-result cell](Workbook_Verification/Excel_Web_PADIM_Step2_Result_17NOV2026.jpg).

## Holds and owner decisions

PA-DIM declares Devices 1.04. Two name-change comparisons and one recovery-advice comparison retain holds under PA-C2-Q015 and Q016 because the inspected legacy links returned Devices 1.05. All 14 prior PA-DIM questions, 12 Devices source limits, earlier ISA/SOSA/SAPIENT/AAS/case holds and SAPIENT bounded-PARTIAL standing carry forward. The historical model inventory marked 952 of 1,059 entries unread. Targeted reads and semantic cross-references are recorded at their actual depth. The owner retains decisions on source limits, model adoption, Step 24, Steps 35–39 and named-version Step 40. M00/M01 are preserved.

## History

Step 1’s published [baseline and archive](https://github.com/OS4CSAPI/glaux-client/tree/archive/pre-padim-correction-17nov2026) is `7d2593a4be7150a487e3960cad532ee970e60a67`. Its publication, workbook repair and two passing checks are recorded in the Devices ledger. The [Step 2 assessment backup](https://github.com/OS4CSAPI/glaux-client/tree/checkpoint/padim-corrective-assessment-17nov2026) at `76120bf` precedes the integrated candidate.

## Interrupted work

Profile Rewrite 58 published the workbook at `2fde004`. Profile Rewrite 59's receipt survived locally at `16b098d7e6c0cc6d3db26381010e89cb834aba39` in `/workspace/scratch/055f432dd14f/receipt`; it had not reached GitHub when Profile Rewrite 60 verified the branch. Its master/ledger receipt changes are carried forward here with the updated PITON. This is previously authorized delivery, with no workbook or donor-assessment change; confirm this commit is live before treating the receipt as published.

## Verification and publication

Profile Rewrite 59’s Proceed authorized this receipt. The [published Step 2 commit](https://github.com/OS4CSAPI/glaux-client/commit/2fde004c0819b0faad536d889e24e0942721411d) has tree `5da290b4ece8521f1086a61e2bf746b21f63fcef`, identical to the Excel-verified local commit `4626a88`. A fresh 501,831-byte workbook download matched the SHA-256 above. Both GitHub checks passed. [Master verification](https://github.com/OS4CSAPI/glaux-client/actions/runs/44152080376) · [Workbook publication](https://github.com/OS4CSAPI/glaux-client/actions/runs/44152080510). The PA-DIM ledger records the receipt under `corrective_review.publication` and the master under `workbookSnapshot.PADIM_corrective_2_publication`.

Profile Rewrite 60 found that existing recovery checks enforce document sizes only; output limits were behavioral instructions. The reusable [output guard](../../../../scripts/dim_context.py) now bounds command output and selected file reads; complete command logs stay on disk, oversized evidence requires a narrower selection, and original-source exceptions remain explicit. Live master/PA-DIM files measured 7,121,177/2,534,639 bytes; their size alone does not establish that they entered the failed conversation. The screenshot establishes a cutoff during the first authorized step, but no exact prior execution transcript or backend cutoff accounting was available. This safeguard does not establish a platform root cause or guarantee future conversation length.

The guard passed 23 focused checks plus a refusal/selection check against the actual master. The active CI verification commands, `check_dim_crosswalk_step06.py --recovery-only` and `integrate_sosa_opportunity_checkpoint.py --verify`, pass; use that route for this checkpoint, because the former's default legacy path expects an earlier 329-row master. Both recovered JSON receipts match `16b098d` exactly and the workbook hash is unchanged. The broader `verify-artifacts.py` check still reports the same five pre-existing document-register/link issues reproduced in the preserved receipt checkout; they are outside this repair.

## Next action and stop

Step 2 is complete. On one new Proceed, carry out Step 3, the final corrective-plan step. Reconcile the concrete differences between Devices and PA-DIM and explain in plain English what each contributes, what changed and which questions remain. Stop after joint closeout for the owner’s decision.
