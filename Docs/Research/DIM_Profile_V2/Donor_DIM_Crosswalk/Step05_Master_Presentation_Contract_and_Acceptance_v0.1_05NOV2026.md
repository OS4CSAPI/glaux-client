# Step 05 — Approved master-table presentation and acceptance contract

**5 November 2026 · ORIGINAL STEP05 ONLY · DISPLAY/BUILD SPECIFICATION, NOT A NEW XLSX OR DONOR MAPPING.** The owner accepted the **format** of the [seven-donor, 22-element, five-divider sample](../Deliverables/DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026.md). This step makes that format reproducible and testable; the actual working XLSX is scheduled for **Step06**, followed by an owner review at **Step08**.

**This is the agreed visual logic, not a new DIM design.** The donor concept is in the donor's column, and the rightmost column is the proposed DIM information element. A row can contain a direct correspondence, a qualified/partial correspondence, an unrelated source term recorded only in the evidence, or no established correspondence. A whole-width divider row introduces each group of meanings. The owner should be able to scan **across** to compare source concepts and **down** the DIM column to understand what the proposed model contains.

**Machine-readable control:** [Step05 presentation contract JSON](Step05_Approved_Master_Table_Presentation_Contract_v0.1_05NOV2026.json). **Read-only validation code:** [`scripts/check_dim_crosswalk_presentation.py`](../../../../scripts/check_dim_crosswalk_presentation.py). Step03's [row/cell/source-qualification contract](Step03_Row_Cell_Evidence_Contract_v0.1_05NOV2026.schema.json) remains independent of these display rules. Step04's [46 *possible* donor-column roster](Step04_Provisional_Donor_Column_Roster_v0.1_05NOV2026.md) does **not** authorize inserting all 46 columns.

## 1. One master table — no extra navigation/ID columns in front

| Required feature | Exact implementation rule | Why |
| --- | --- | --- |
| **Header** | **Row 1**, the donor names in their current approved order, followed by **PROPOSED DIM ELEMENT** as the **final rightmost column**. | The entire table can be read horizontally. |
| **Initial width** | Use the **seven approved sample donors + one DIM column** until a separately reviewed roster change. | The 17 provisional and 29 conditional donor *candidates* were not yet selected or ranked. |
| **No hidden first-class display field** | Stable row IDs and technical relationship bookkeeping remain in data/evidence, **not as visible leftmost master columns**. | A person should not need to know historical “R24” codes to read the model. |
| **Concept rows** | One proposed information meaning per row, in the sample's original sequence. Keep original native donor strings and qualifiers. | Prevents generated table from silently inventing alignments or changing the accepted example. |
| **Group divider rows** | Full-width **merged across all donor + DIM columns** with descriptive label; five in baseline. | Makes the sheet navigable like a System description, not a flat encyclopedia of fields. |
| **Direct comparisons** | Show the source-native donor name without an additional symbol (still **PROPOSED** until verified). | Short and legible; does **not** imply formal published equivalence. |
| **Partial/related/conditional comparisons** | Prefix **`≈`** and retain the exact caveat in the evidence record. | Shows that related meaning is not interchangeable. |
| **No match established** | Actual **blank cell**, never a forced hyphen/`N/A`/`None` meaning “donor lacks it.” | No proof of universal absence is implied. |
| **Rejected/held mappings** | Preserve negative source-evidence decision **off the main table**; do not fill a false equivalence. | Rejection is still useful research, but shouldn't masquerade as an aligned donor field. |
| **Rightmost DIM** | Display the proposed plain-English DIM label in a distinct but subdued column. | This is the proposed synthesis, not a claimed adopted ontology. |

**How the CSV mirror differs from the XLSX:** CSV cannot merge cells or preserve colors. For a group divider it contains the title in its first column and seven empty cells; the generated XLSX **must** merge the divider across the full range. The GitHub-readable Markdown mirror may use a native HTML table row with a full-width `colspan`, as in the approved sample. All three outputs must have exactly the same native terms and row order.

**Column order:** Retain the approved **IEEE 1451 → OMS 3.0 → OPC UA Devices → W3C SOSA/SSN → SensorML 3.0 → SAPIENT v2 → CSAPI Parts 1–2 → DIM** sample order for the first working edition. This is **sample usage order only**; it counted direct, partial and related entries equally. Final donor ordering remains **UNDETERMINED** until later original-source review and evidence-based contribution counts. If later work justifies new eligible columns, change the roster and review it explicitly before a display reorder.

## 2. What Step06 should actually generate

**Planned working XLSX — not yet created by Step05:** `Master_Donor_Concept_to_DIM_Crosswalk.xlsx`. It should have one **primary** owner-facing sheet named **Master Crosswalk**, plus the following supporting tabs:

| Sheet | Purpose | Filter? |
| --- | --- | --- |
| **Master Crosswalk** | Horizontal donors-to-DIM comparison, original sample headings, divider rows, plain labels | **No**, because the full-width merged divider rows do not form an ordinary rectangular Excel table |
| **Evidence** | One row per populated source claim and additional held/rejected mappings: original source URL, exact edition and clause, referent, mapping type, review status and non-equivalence warning | Yes |
| **DIM Definitions** | Internal stable row key, proposed term, working definition, element kind, tentative/held standing | Yes |
| **Donor Sources** | Candidate standard name and edition, publisher, scope, eligibility and later substantive contribution counts | Yes |
| **Holds & Decisions** | Unsupported mappings, source-access problems, conflicts, rejected equivalences and open reviewer questions | Yes |
| **Read Me** | A short owner-readable explanation, `≈`/blank legend, version, source limitations, how to trace a cell | No |

**Keep the master visible and readable.** Suggested restrained styling is a dark-navy header; light-blue full-width divider rows; lightly tinted **DIM** column; white or subtle alternating data-row background; legible 10–11pt text; ~22–40 character-width donor columns and ~32–44 for DIM, with wrapped text. Cap oversized rows rather than autofitting them infinitely. Avoid status badges, scores or decorative charts that obscure the comparison.

**Freeze the header row**, not the DIM at the far right: Excel does **not** support pinning just the final/rightmost column while allowing arbitrary earlier donor columns to scroll. This is a real limitation of the requested geometry, not a reason to rearrange the owner-approved design. The spreadsheet may require horizontal scrolling. Any later view/navigation alternative would be supplemental and would require approval; do not quietly duplicate the DIM as an extra left column.

**Evidence references:** Each populated master cell must have a matching donor+row evidence record, with original issuer, **native term kind** (class/attribute/channel/resource/etc.), edition, section/table/schema locator, original URL where available, mapping relation and what **not** to infer. Source links can be followed in the filterable Evidence tab; optional internal hyperlinks/comments in the master may supplement this, but must not replace it.

**Important:** The original sample's `SOURCE-VERIFIED SAMPLE` label is overconfident. Per [Step02 audit](Step02_Starting_Evidence_and_Coverage_Audit_v0.1_05NOV2026.md), all 51 historical sample correspondences have **prior source pointers**, not automatically a new original-clause readback. Step06 must present them as **WORKING / PRIOR_SOURCE_EXTRACT_ONLY** unless an actual original source review has occurred. No visible source term should magically gain the stronger `ORIGINAL_CHECKED` label because a table was formatted or exported.

## 3. Testable acceptance checks for the owner-approved fixture

The committed [read-only checker](../../../../scripts/check_dim_crosswalk_presentation.py) compares actual GitHub-source JSON, flat CSV, evidence CSV and Step04 roster against the [structured contract](Step05_Approved_Master_Table_Presentation_Contract_v0.1_05NOV2026.json). It refuses to silently ignore missing or changed baseline source files and checks the original **Git blob SHA** of each pinned input.

| Check | What would fail it |
| --- | --- |
| **Exact donor order and DIM last** | An added first ID column, donor reordering, DIM in the middle or incorrect donor names |
| **Five dividers and 22 rows** | Deleted or altered section, duplicated/missing DIM term, changed row sequence |
| **51 claims + literal cells** | An unexplained new/nonempty donor cell, a removed original entry, lost `≈` or changed published term |
| **Source/ledger parity** | One donor concept without a matching evidence row, broken term/fit, missing source locator/URL/non-equivalence explanation |
| **No false verification** | Treating the historical sample label as a source-checked or formally adopted model |
| **No unapproved 46-column expansion/ranking** | Forcing all Step04 candidates into the approved sample or pretending their `rank:null` is settled |
| **Divider + Excel functionality** | Trying to put one structured Excel table filter around merged heading rows, or claiming to freeze an individual far-right DIM column |
| **No premature binary deliverable** | Generating/publishing a first master XLSX during Step05 rather than separately authorized Step06 |

**One limit:** The checker tests **structure and consistency of already recorded source claims**. It does **not** independently inspect the actual IEEE/SAPIENT/OGC/OPC publisher clauses, validate ontology equivalence, prove 182 sources were all read, or certify the pending XLSX render. Step06 must separately test the actual generated XLSX and its GitHub byte/visual integrity. These are two different achievements.

## 4. Step05 disposition and next action

The owner-approved **format** has now been translated into a written technical contract and a read-only checker. No new donor, cell, DIM concept, original-source verification, UML change or source interpretation is authorized in this Step05.

**NEXT one owner “proceed”: STEP06 ONLY.** Generate a **first working real XLSX**, alongside matching GitHub-readable Markdown/CSV, seeded with the **unaltered 7-donor/22-row sample** and transparent prior-source evidence standing. Publish the **actual files to GitHub**, read them back, check layout and source-cell preservation, then show the links for owner inspection. **Step07/08** are separately authorized later steps; Step08 owner review is mandatory before donor expansion.
