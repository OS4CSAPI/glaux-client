# Step 06 — First real editable donor-to-DIM master workbook

**6 November 2026 · STEP06 ONLY · WORKING-SAMPLE BUILD, NOT NEW DIM RESEARCH.**

The source-backed sample is now supplied as one actual **Excel .xlsx workbook**, a directly readable **GitHub Markdown table**, **CSV** and a **structured JSON file**. This is the first editable workbook following the owner's accepted table geometry; there is no claim of original standards equivalence or 182-source mapping completion.

## Owner-facing result

Open [**Master_Donor_Concept_to_DIM_Crosswalk.xlsx**](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) and select the first tab **Master Crosswalk**. It displays the **same seven donors in the same original order**, with the proposed DIM information element **far right**. Five merged topic-divider rows separate the 22 proposed information elements. Fifty-one existing donor cells contain their original literal donor terms and `≈` qualifiers; blank cells are intentionally blank.

GitHub preview: [**read the master table**](Master_Donor_Concept_to_DIM_Crosswalk.md) without installing Excel. A corresponding [**flat CSV**](Master_Donor_Concept_to_DIM_Crosswalk.csv) follows the same row and donor order, and [**structured source**](Master_Donor_Concept_to_DIM_Crosswalk.json) retains every source/evidence decision.

## Six worksheets (first master tab is not replaced)

| Tab | Contents and limitation |
| --- | --- |
| **Master Crosswalk** | Donors in columns, DIM last, 5 merged headings; header frozen. No AutoFilter over merged rows. |
| **Evidence** | One row for each of the **51 existing source claims**: stable internal key, edition, original native term and kind standing, relation, original locator, clickable source URL and explicit non-equivalence warning. Filterable. |
| **DIM Definitions** | 22 **proposed information elements** with working rationale, internal trace key and unresolved element kind. Filterable. |
| **Donor Sources** | The seven current sample donors, original edition/source information, sample counts and **undetermined final contribution rank**. Filterable. |
| **Holds & Decisions** | Selected **previously documented** rejected/held mappings and source-standing gaps, not invented new donor rows. Filterable. |
| **Read Me** | Plain-language instructions, `≈` legend, source-standing limits and owner-review gate. |

## Actual construction and acceptance scope

The generated workbook, Markdown, CSV and JSON all derive from the **same historical sample JSON plus its original 51-row evidence CSV**; the CSV matches the original sample's saved field strings. This step validates **presentation/source-pointer parity**, not the semantic validity of each original publisher clause. The original sample JSON, CSV and evidence files remain unchanged and pinned at these Git blobs:

- Sample JSON: `44b9298e91f6ea454c786534c6447c8833cccc99`.
- Sample CSV: `82ab142114e42831c6b9575fbb57d73a325ee89e`.
- Evidence ledger: `976fef4958f2a8a7f4bff26bbf1ac4ca79bc9904`.

**No new original-publisher clause review was performed.** All 51 active source claims are shown as `PRIOR_SOURCE_EXTRACT_ONLY`, never automatically `ORIGINAL_CHECKED`. Historical sample's `SOURCE-VERIFIED SAMPLE` label was overconfident; we did not rewrite that original. The 17 provisional and 29 conditional donor candidate columns remain **candidates** and were not silently inserted. No DIM concept, UML, CSAPI Profile, app, 52°North/Oracle server or Cloudflare deployment was changed.

**Packaging note:** The XLSX is an Office Open XML ZIP package with six editable worksheets, styled headers, merged headings, frozen header panes and external source hyperlinks in supporting tabs. It is deliberately **uncompressed ZIP storage** for transparent byte-level checking. The workbook must still be opened for the owner's substantive readability review at Step08; structural integrity cannot replace human assessment.

**Next one authorized `proceed`: Step07 ONLY** — review the existing group order and proposed row definitions against Dragino, AirGradient, Campbell and Bennett source distinctions, recording candidate splits/uniques without adding unverified donor mappings. **Step08 is the mandatory first formal owner checkpoint** before broader donor intake.

## Independent committed-byte verification after workbook layout refinement

The final XLSX Git blob is `0370723675697b6fb87836c41b8783d31403aa13`. An independently executed [**GitHub Actions validation run 42297230272**](https://github.com/OS4CSAPI/glaux-client/actions/runs/42297230272) completed **SUCCESS** on the final workbook commit. Its read-only Python verifier opened the committed ZIP, checked member CRCs and XML parsing, all six sheet identities, **seven donor headers and final DIM column**, original 22 element rows, **five merged section bands**, **51 source citations/verification states**, evidence hyperlinks and the exact CSV/JSON mirrors. Source-semantic equivalence, live Excel visual rendering and final owner acceptance are **not** inferred from this structural PASS.
