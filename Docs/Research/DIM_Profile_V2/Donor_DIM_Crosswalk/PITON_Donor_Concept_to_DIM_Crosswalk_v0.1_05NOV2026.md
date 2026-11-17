# Current Profile Rewrite checkpoint

Updated 17 November 2026, America/New_York, Profile Rewrite 58. Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`. Verify live HEAD. Read [AGENTS.md](../AGENTS.md) once.

## Active scope and evidence

The owner’s Profile Rewrite 57 and 58 Proceeds cover Step 2 of the [Devices and PA-DIM corrective plan](PLAN_OPC_UA_Devices_PADIM_Corrective_Assessment_17NOV2026.md). The [PA-DIM source ledger](OPC_UA_PADIM_Source_Coverage.json), under `corrective_review`, records dispositions for all 477 starting cells, 40 native finding groups, 142 supporting definition groups and 22 prior additions. Step 2 corrected 29 existing PA-DIM cells, expanded two candidate definitions and added one provisional row for a signal’s compensation method and reference conditions. The [comparison narrative](Donor_Native_High_Level_Information_Groupings_Comparison.md) explains the source meanings and distinctions.

## Master and workbook

The [editable workbook](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) contains 478 information rows. All 8,619 comparison-grid values agree with the master JSON, both CSV files and both readable comparisons. PA-DIM has 68 blue common candidates, 12 amber specialized candidates and 398 white cells with explicit statuses. The master records 788 colored comparisons and 108 earlier held classifications. Workbook SHA-256 is `d3882d2f0db02ea829e07f59c849b785184dbed211635258c31165479f282dce`.

## Verified checkpoint

The [integrated candidate](https://github.com/OS4CSAPI/glaux-client/commit/ea119fa73e95c2c5cd08637572255e67541746cc) preserves the recovered local tree at `c4d8390`. Excel for the web opened its exact workbook without a repair notice. G507 showed the blue compensation candidate, its Devices counterpart was readable in F507, and G82 showed the narrower method-result mapping in white. Headers stayed visible while scrolling. The saved-file checks cover the full grid and preservation across 26 sheets. Desktop Excel and runtime behavior were outside this check. [Compensation row](Workbook_Verification/Excel_Web_PADIM_Step2_Compensation_17NOV2026.jpg) · [Method-result cell](Workbook_Verification/Excel_Web_PADIM_Step2_Result_17NOV2026.jpg).

## Holds and owner decisions

PA-DIM declares Devices 1.04. Two name-change comparisons and one recovery-advice comparison retain holds under PA-C2-Q015 and Q016 because the inspected legacy links returned Devices 1.05. All 14 prior PA-DIM questions, 12 Devices source limits, earlier ISA/SOSA/SAPIENT/AAS/case holds and SAPIENT bounded-PARTIAL standing carry forward. The historical model inventory marked 952 of 1,059 entries unread. Targeted reads and semantic cross-references are recorded at their actual depth. The owner retains decisions on source limits, model adoption, Step 24, Steps 35–39 and named-version Step 40. M00/M01 are preserved.

## History

Step 1’s published [baseline and archive](https://github.com/OS4CSAPI/glaux-client/tree/archive/pre-padim-correction-17nov2026) is `7d2593a4be7150a487e3960cad532ee970e60a67`. Its publication, workbook repair and two passing checks are recorded in the Devices ledger. The [Step 2 assessment backup](https://github.com/OS4CSAPI/glaux-client/tree/checkpoint/padim-corrective-assessment-17nov2026) at `76120bf` precedes the integrated candidate.

## Interrupted work

The recovered checkout is `/workspace/scratch/acb9b2ea127e/glaux-client`.

## Verification and publication

Excel verification is complete. Read back the published content tree and a fresh workbook download, confirm the affected repository checks, and record the receipt here and in the PA-DIM ledger and master.

## Next action and stop

After the receipt, stop for Proceed. Step 3 is the one remaining corrective-plan step. It covers a finite comparison of the two donors and a plain-English joint explanation.
