# Current Profile Rewrite checkpoint

22 November 2026, owner local date. Branch `research/dim-profile-v2`. [Execution protocol](../AGENTS.md).

## Active scope and evidence

Profile Rewrite 64. Following N42.42 delivery, the owner explicitly requested a joint reassessment of RFC 8348 and N42.42 using the previous two-donor review. The [findings and row guide](Donor_Native_High_Level_Information_Groupings_Comparison.md#rfc-8348-and-n4242-corrective-review) explain the changes. Both [RFC](RFC_8348_Source_Coverage.json) and [N42](N42_42_Source_Coverage.json) ledgers store the baseline comparisons, corrected evidence and native source checks under `corrective_review_64`.

## Verified checkpoint

`RFC8348_N4242_CORRECTIVE_64`. All 601 original information rows were reconciled for both columns. The review revised 135 RFC decisions and 59 N42 decisions on those rows. The 19 RFC decisions for N42-origin rows now also appear in the RFC ledger. Existing candidate definitions and eight source-supported earlier-donor comparisons were corrected. The review added 7 rows and compared every earlier donor on each addition.

## Master and workbook

[Updated editable master](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) · [Pre-review workbook](https://github.com/OS4CSAPI/glaux-client/blob/65be224dc1068827e99f6e94eeaa80c2b0120b4c/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/Master_Donor_Concept_to_DIM_Crosswalk.xlsx). Columns P and Q contain 608 decisions each. New rows begin at 639 and end at 645. The layout has 23 columns and 26 worksheets. SHA-256 `4cccfe4fd3a95948c2bd68cc80e23ce0ccc1eba396168d33cff244d8ef190520`. Canonical JSON, both CSVs, both readable comparisons and saved workbook reflect the same grid.

## Verification and publication

The verification checks cover stable IDs, old and revised cells, evidence and colors, mirrors, package structure and row-only freeze. The [delivery commit](https://github.com/OS4CSAPI/glaux-client/commit/8f97de4bd0f89d7a4604cc7408d5a36a0a3d1563) matched the local tree. The downloaded workbook matched the stated SHA-256 byte for byte. Both [master verification](https://github.com/OS4CSAPI/glaux-client/actions/runs/45114123073) and [workbook publication](https://github.com/OS4CSAPI/glaux-client/actions/runs/45114123007) passed.

## Holds and owner decisions

The owner's previous RFC bounded partial acceptance applies to [the baseline](https://github.com/OS4CSAPI/glaux-client/blob/65be224dc1068827e99f6e94eeaa80c2b0120b4c/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md). The corrected RFC and N42 assessments both await owner disposition. Preserve RFC8348-Q1–Q3 and N42-Q1–Q3. N42-Q1 covers unretrieved operative prose, N42-Q2 installed case evidence, and N42-Q3 extension, validation and illustrative standing. Project case holds remain. Earlier OSUS-R, Redfish, SAREF and WoT decisions stand. Final ranking, Step 24 adoption, Steps 35–39, named-version Step 40 and manual M00/M01 retain their standing.

## Interrupted work

The comparison and workbook integration are complete. The [interim checkpoint](https://github.com/OS4CSAPI/glaux-client/commit/7a03408ec988d126224328ca355b2a8959ee81db) preserves the early native review.

## History

[Exact previous checkpoint](https://github.com/OS4CSAPI/glaux-client/blob/65be224dc1068827e99f6e94eeaa80c2b0120b4c/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md).

## Next action and stop

Owner assessment of both revised columns. Recommend accepting both as bounded partial with their recorded source and case holds. No subsequent donor is authorized.
