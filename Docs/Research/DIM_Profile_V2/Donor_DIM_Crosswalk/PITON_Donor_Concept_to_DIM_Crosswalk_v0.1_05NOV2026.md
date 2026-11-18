# Current Profile Rewrite checkpoint

18 November 2026. Branch `research/dim-profile-v2`. [Execution protocol](../AGENTS.md).

## Active scope and evidence

The owner requested the same corrective review for OSUS-R and Redfish that was used for SAREF Core and W3C Web of Things. The published [pre-change master](https://github.com/OS4CSAPI/glaux-client/blob/d423e3943b136a7317c401c22b1d79466a51d2a4/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/Master_Donor_Concept_to_DIM_Crosswalk.xlsx) has 568 information rows. The [interim checkpoint](https://github.com/OS4CSAPI/glaux-client/commit/a27e460f9da62fd6e5b6e46a7a3667800ab157b2) records the OSUS-R coverage gap and source checks. The joint delivery adds six rows and assesses both donors on all 574 rows. [Plain-English findings](Donor_Native_High_Level_Information_Groupings_Comparison.md#osus-r-and-redfish-corrective-review).

## Master and workbook

[Editable Excel master](Master_Donor_Concept_to_DIM_Crosswalk.xlsx). The canonical JSON, both CSVs, both readable comparisons and workbook cover a 608-by-21 grid. OSUS-R remains in column N and Redfish in O. The earlier donor ledger stopped at 521 rows. Its 47 missing formal decisions now include 11 partial matches, 19 related findings and 17 bounded no-match findings. The team also revised 16 earlier OSUS-R assessments and 19 earlier Redfish assessments. The evidence for each change, predecessor text, paired decisions on all six additions and nearest prior row are in `corrective_review_63` in the [OSUS-R ledger](OSUS_R_Source_Coverage.json) and [Redfish ledger](Redfish_Source_Coverage.json). Original `new_rows` arrays preserve the historical 28 and 47 candidates. Six joint-review candidates are recorded separately.

## Verified checkpoint

`OSUSR_REDFISH_63_SAVED_VERIFIED`. Workbook SHA-256 `0beec73db8fb23a8d9ea00c80814aa51dbf1d25c36656b0cc09f76ab3f907b1a`.

## Verification and publication

Saved values, source labels, classifications and fills were checked for both donors. Verification also checks the 26-sheet package and unchanged parts, old cells outside documented corrections, row-only freeze, both pairs of mirrors and the prior decision and holds. Artifact Tool reopened the workbook and matched all 608 positions in both N and O. [Rendered sample](Workbook_Verification/OSUSR_Redfish_63_Corrected.png). Native Microsoft Excel was not exercised. Publication includes readback and GitHub verification.

## History

[Prior recovery record](https://github.com/OS4CSAPI/glaux-client/blob/d423e3943b136a7317c401c22b1d79466a51d2a4/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md) · [Full interim recovery record](https://github.com/OS4CSAPI/glaux-client/blob/a27e460f9da62fd6e5b6e46a7a3667800ab157b2/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md).

## Interrupted work

The interim record preserves the initial discrepancy. The integrated correction supersedes it.

## Holds and owner decisions

SAREF Core and corrected Web of Things retain their earlier bounded acceptances. OSUS-R retains the earlier owner decision on its 521-row assessment and OSUS-Q1–Q3. Redfish retains RF-Q1–Q3. The joint corrections are ready for owner disposition. The evidence distinguishes schema declarations, implementation examples and installed-case records. Final ranking, Step 24 adoption, Steps 35–39, named-version Step 40 and manual M00/M01 retain their existing standing. The [research-priority order](Donor_Research_Priority_Order.md) is separate from eventual donor-column order.

## Next action and stop

 Owner disposition on the corrected OSUS-R and Redfish assessments with their existing source and deployment limits. Stop here.
