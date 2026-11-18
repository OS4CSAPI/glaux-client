# Current Profile Rewrite checkpoint

18 November 2026, America/New_York. Branch `research/dim-profile-v2`, [execution protocol](../AGENTS.md).

## Active scope and evidence

Profile Rewrite 63. The owner authorized the two-column correction and then replied “Proceed” to record acceptance of the corrected Web of Things 1.1 assessment. The [SAREF](SAREF_Core_Source_Coverage.json) and [Web of Things](WoT_1_1_Source_Coverage.json) ledgers record current decisions and affected cells under `correction_63`. [Plain-English findings](Donor_Native_High_Level_Information_Groupings_Comparison.md#how-the-donor-order-affected-saref-and-web-of-things). The [WoT plan](PLAN_W3C_WoT_1_1_Source_First_Donor_Review.md) retains the source limits.

## Master and workbook

[Editable workbook](Master_Donor_Concept_to_DIM_Crosswalk.xlsx). 493 information rows, 524 grid rows, 19 columns and 26 worksheets. On the existing rows 12 SAREF cells and 16 Web of Things cells changed, including five previously unassessed SAREF positions. Two additional Web of Things rows cover request-time address variables and directory record change notifications. Both donors have an explicit disposition on every information row. Other donors have explicit pending comparisons on the two new rows.

## Verified checkpoint

SAREF_WOT_63_SAVED_VERIFIED. The saved grid matches the canonical JSON, both CSVs and both readable tables. Both columns’ classifications match their fills. Earlier cell contents and styles outside the corrected positions, other worksheet parts and row-only freezing were checked. Artifact Tool reopened the saved workbook. [Saved correction render](Workbook_Verification/SAREF_WoT_63_New_Rows.png). Native Microsoft Excel was not exercised for this revision.

## Holds and owner decisions

SAREF Core acceptance at fe598e0 and SRF-Q1–Q3 stand. On 18 November 2026 the owner accepted the corrected Web of Things review as bounded partial. The ledger records the decision under `owner_decision`. WOT-Q1 retains selective passage and schema depth, WOT-Q2 retains companion and implementation limits, and WOT-Q3 retains installation and runtime holds. Prior donor and case holds, manual M00/M01, Step 24, Steps 35–39 and named-version Step 40 retain their standing. Final column order runs from least contributing at left toward largest foundational contribution at right. Ordering awaits comparative judgment.

## Interrupted work

The corrected comparison and both ledgers were published at 6f8d318. The downloaded workbook matched the verified copy and both publication workflows passed.

## History

The Web of Things inventory was checkpointed at 44428bc and the original assessment was delivered at 54fbc09.

## Verification and publication

The pre-correction publication was 54fbc09. [Pre-correction master workbook](https://github.com/OS4CSAPI/glaux-client/blob/54fbc09aef66562c7558e32d4411fbf026f7c17f/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/Master_Donor_Concept_to_DIM_Crosswalk.xlsx). [Pre-WoT workbook](https://github.com/OS4CSAPI/glaux-client/blob/751f4bccdec751fe8db90fdcf701c1409f755027/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/Master_Donor_Concept_to_DIM_Crosswalk.xlsx). The accepted workbook is pinned to [the verified correction](https://github.com/OS4CSAPI/glaux-client/commit/6f8d318072e2c97e938949b911128b691ae43550). The subsequent acceptance updates decision records only.

## Next action and stop

Owner selection of the next donor research priority. A further Proceed requests a read-only comparison and ranking of the remaining options for that decision. The seven Web of Things-origin rows remain pending separate Domain Information Model adoption decisions.
