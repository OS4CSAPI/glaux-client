# Current Profile Rewrite checkpoint

23 November 2026. Branch `research/dim-profile-v2`. [Execution protocol](../AGENTS.md).

## Active scope and evidence

The owner requested a joint reassessment of the I-ADOPT and MIMOSA CCOM columns using the prior RFC 8348/N42.42 approach. The original baseline is [2f39e20, pre-review workbook and checkpoint](https://github.com/OS4CSAPI/glaux-client/tree/2f39e2071f705a9012f24425bc4699e440c3250b/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk). See the [comparison and findings](Donor_Native_High_Level_Information_Groupings_Comparison.md#reassessment-of-i-adopt-and-mimosa-ccom).

## Master and workbook

`IADOPT_CCOM_CORRECTIVE_64`. [Editable master](Master_Donor_Concept_to_DIM_Crosswalk.xlsx). The 26-sheet workbook has 620 information rows and 25 columns. I-ADOPT remains in R and CCOM in S. Rows 655–660 contain six new candidates. The respective [I-ADOPT ledger](I_ADOPT_Source_Coverage.json) and [CCOM ledger](CCOM_Source_Coverage.json) record the baseline, source checks, additions and previous/revised decisions under `corrective_review_64`. They account for all 620 decisions per donor and all 19 receiving donors on each of the 12 origin rows.

## Verified checkpoint

Both original 614-row columns were reassessed. I-ADOPT has 93 revised existing decisions and CCOM has 208. The four previous CCOM contributions have clearer definitions. Prior evidence, including the earlier I-ADOPT acceptance, retains its published scope.

## Verification and publication

Run `python -B scripts/check_dim_crosswalk_step06.py` for the paired source/row and receiving-donor decisions, classification colors, workbook package, preserved cells and four text mirrors. The [workbook delivery](https://github.com/OS4CSAPI/glaux-client/commit/4a977173305f4b7d856bac11b801d79537e72560) was read back on the live branch. An independent download matched SHA-256 `d0d24b2df3e25182e97fcf383a80715fdfc74494485101430d3d94a533c951a2` and passed package integrity checks. The [master verification](https://github.com/OS4CSAPI/glaux-client/actions/runs/45234676194) and [workbook publication](https://github.com/OS4CSAPI/glaux-client/actions/runs/45234675929) runs both passed. All 16,500 grid values matched the four text mirrors. A spreadsheet reader reopened the workbook and rendered sample ranges. Desktop Microsoft Excel was not run.

## Holds and owner decisions

IADOPT-Q1–Q3 and CCOM-Q1–Q3 remain bounded as updated. The comparison tested selected final-edition declarations and reference-data entries. Nine case-specific decisions in each column and 38 receiving-donor source holds remain explicit. Step 24, Steps 35–39, named-version Step 40 and manual M00/M01 retain their recorded scope.

## Interrupted work

The source-ledger, workbook and mirror changes form one delivery.

## History

[Pre-correction checkpoint](https://github.com/OS4CSAPI/glaux-client/blob/2f39e2071f705a9012f24425bc4699e440c3250b/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md).

## Next action and stop

Owner assessment of both corrected comparisons. A single Proceed records acceptance of both as bounded partial, with holds retained. Research on the World Wide Web Consortium Provenance Data Model, ranked ninth, requires its own authorization.
