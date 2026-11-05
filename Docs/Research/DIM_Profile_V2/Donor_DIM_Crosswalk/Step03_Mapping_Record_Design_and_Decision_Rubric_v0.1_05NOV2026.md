# Step 03 — A real row-and-cell evidence record and mapping-decision rubric

**5 November 2026 · Step 03 of the new donor-concept-to-DIM crosswalk effort · RECORD DESIGN ONLY; NO NEW MAPPINGS / NO ORIGINAL-SOURCE CLAIMS NEWLY CHECKED.**

**In ordinary language:** The [approved comparison table](../Deliverables/DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026.md) is still what the owner sees: **donors across columns; proposed DIM at far right; meaningful row groups separated by full-width dividers**. This step specifies the *information behind each cell*, so an unfamiliar researcher can determine exactly what native source term it came from, whether it actually means the same thing, what it definitely **does not mean**, and whether we have checked the original standard. The internal IDs and ratings live on the supporting side, not in the user's main table.

**Committed technical artifacts:**
1. [Step03_Row_Cell_Evidence_Contract_v0.1_05NOV2026.schema.json](Step03_Row_Cell_Evidence_Contract_v0.1_05NOV2026.schema.json) — *JSON Schema Draft 2020-12* for the proposed structured bundle with **donor columns**, **group dividers**, **DIM information-element rows** and **donor↔row cell decisions**. This is a **project work-file schema**, not a published DIM ontology, OGC Profile, or normative device data format.
2. [Step03_Row_Cell_Evidence_Examples_v0.1_05NOV2026.json](Step03_Row_Cell_Evidence_Examples_v0.1_05NOV2026.json) — **two schematic mapping decisions based entirely on already recorded project research**, deliberately labelled `EXAMPLE_ONLY_NOT_SOURCE_RECHECKED`, with no false `ORIGINAL_CHECKED` states.
3. [Step02 original starting-evidence audit](Step02_Starting_Evidence_and_Coverage_Audit_v0.1_05NOV2026.md) and [frozen record/blob register](Step02_Starting_Data_Inventory_v0.1_05NOV2026.json) — baseline of **22 proposed rows, 5 group dividers, 51 prior source claims, 7 donors and 182 individually unassessed artifacts**. The current Step03 schema is prospective. **It is not a silent migration or approval of those 51 existing cells.**

## 1. Four record types, not four new DIM classes

| Record | Plain meaning | Key fields | Owner-facing consequence |
| --- | --- | --- | --- |
| **Donor column** | Which actual standard or source edition a column represents | Stable donorKey; human-readable donor; **issuer, edition, scope, original publication URL**; whether the column bundles multiple standards; provisional display order; source review depth | Source names across the top, fixed after roster review. Does **not** rank donors by number of artifacts. |
| **Group divider** | Where a block of related DIM rows begins | Stable sectionKey; title, order, plain-language purpose; standing `SPREADSHEET_NAVIGATION_ONLY_NOT_DIM_PACKAGE` | Full-width labeled row. **Does not** silently create UML inheritance/package semantics. |
| **Proposed DIM row** | One distinct information meaning the DIM may need | Stable, non-display rowKey; label; **working definition, kind, referent scope, proposed/held standing**, group and notes | Label in the far-right DIM column. The ID stays stable when row order or section changes. Does **not** mean a finalized class or an enacted R24 rule. |
| **Cell decision** | Why a specific donor's native term **does or does not** correspond to a proposed DIM row | Stable decisionKey; rowKey + donorKey; **native term exactly as published, element kind, authoritative source, original clause/table/schema locator, comparison relation, evidence status, decision, explanation and rejected implication** | The donor cell shows a short native term only **when eligible for display**. A rejected/unsupported mapping remains documented in evidence but does **not** fill a misleading cell. |

**One row is a meaning, not necessarily one JSON field.** Source terms can be native classes, properties, associations, process roles, channels, API resources, commands or code values; `nativeElementKind` explicitly says which. One donor term may contribute to more than one DIM row, and one row may have more than one original donor source term: store a separate mapping decision for each genuine semantic claim, do not stuff unrelated statements into a cell or count the same original edition twice as independent confirmation.

**Keys are not model commitments:** Schema examples use `DEMO-ROW-MANUFACTURER`, `DEMO-OPC`, and `DEMO-MAP-...`, purely **internal stable keys**. They are not R24, normative class names, an equipment serial, or the user-facing DIM labels. The first working master may assign its own stable IDs only under the already planned steps; **Step03 did not mint IDs for all existing 22 rows or change the sample**.

## 2. Source standing is independent of concept correspondence

A cell needs **two different judgments** and a separate owner/research decision, not one misleading “verified” checkbox:

| Original-source review standing | Minimum meaning |
| --- | --- |
| `ORIGINAL_CHECKED` | An actual identified version/edition of the original authoritative publisher's text/schema was independently inspected, with a precise native term/locator, factual scope and date/reviewer. The schema requires `originalCheckedAt` and `originalCheckedBy` and a reference to the text; **a copied URL is not sufficient**. |
| `PRIOR_SOURCE_EXTRACT_ONLY` | A previous research document recorded this term, interpretation or citation, but this new crosswalk workflow **has not yet performed its own original-clause check**. This is the **honest default for the 51 sample cells**, regardless of whether their earlier `fit` says `DIRECT`. |
| `SOURCE_UNAVAILABLE` | The original referenced edition or needed section was not accessible to this evaluation. Related technical articles may be useful, but **cannot fabricate normative SHALLs**; record the exact missing original text and alternative source basis. |
| `NEEDS_REVIEW` | Unknown or unresolved source-text/edition details, ambiguous original term, or an unconfirmed source locator. Not evidence that the donor lacks the concept. |

Separate `sourcePointer.sourceKind` says whether the URL points to a publisher original, public technical companion, project prior extraction, public summary or other unverified resource. **Pointing at the publisher website is not synonymous with having opened and verified the publication.** Each cell also has actual `edition`, `standardIdentifier`, `exactLocator`, and optional artifact ID (only when the source genuinely matches the historic 182-register entry). For a column that groups multiple editions/standards, the **per-cell original source** always decides which one applies.

`recordedAt` / `recordedBy` indicate **when someone stored a proposed comparison**, not when its original publisher clause was inspected. Non-checked records must keep `originalCheckedAt:null` and `originalCheckedBy:null`. In contrast, `ORIGINAL_CHECKED` requires actual nonempty reviewer/date. Even this status validates only the checked original claim; it does **not** automatically validate its suggested equivalence to our DIM, or the whole donor standard.

**This corrects Step02 discrepancy D02-01 without retroactively editing the approved sample:** the sample JSON's `SOURCE-VERIFIED SAMPLE` status is an overly broad historical label. In our new supporting record interpretation **all 51 source-cited old proposals are `PRIOR_SOURCE_EXTRACT_ONLY` until separately evaluated**. Their literal values and approved layout remain unchanged.

## 3. Exactly how to describe the relationship

These are **project analytical relation labels, not automatically asserted equivalence axioms from the original standards**.

| Relation label | Meaning | Main-table behavior |
| --- | --- | --- |
| `DIRECT` | The native donor term corresponds to the proposed DIM element **in a stated, compatible scope**. Exact standard-to-standard equivalence remains unclaimed unless expressly published. | Short native term, qualified in evidence (possibly displayed provisionally before fresh primary review). |
| `BROADER` | Source concept includes the proposed DIM concept **and additional meanings**. | `≈` + native term; evidence names the overreach. |
| `NARROWER` | Source concept describes **only a subset** of the DIM element. | `≈` + native term; evidence names the missing coverage. |
| `PARTIAL_OVERLAP` | Concepts share meaningful content but each has non-overlapping meaning. | `≈` + native term; explanation is essential. |
| `RELATED_BUT_DIFFERENT` | Concept is adjacent/useful evidence but **not a substitute** for the DIM element. | **Normally blank** in the purported-equivalence row if the proposal is rejected; document in the evidence ledger or its **own rightful row**. |
| `CONFLICT` | Meanings/invariants conflict in the stated scope. | No unqualified mapping; hold/reject and explain the incompatible meanings. |
| `NO_ESTABLISHED_MAPPING` | No defensible relation from the source material reviewed. | Blank; **not** “the donor definitely has no such concept.” |
| `UNRESOLVED` | Relevant source passage, context, edition or relationship is insufficient to decide. | Blank or explicit withheld marker according to later owner-approved view policy; no invented equivalence. |

**Separate disposition:** `PROPOSED` = project working comparison, not accepted; `ACCEPTED_FOR_RESEARCH_REVIEW` = passed source validation for inclusion in the **candidate crosswalk**, **NOT** adopted in a final DIM (the JSON Schema requires `ORIGINAL_CHECKED` for this stronger state); `REJECTED` = do not display as a crosswalk match, but preserve the negative finding; `HELD` = preserve the question without filling a fictitious match. Neither accepted comparison nor a fully checked original standard makes a source equivalent to CSAPI or certifies the target DIM.

**When to split or add a row:** If one term addresses a hardware channel and another a reporting stream, those are **different DIM meanings**, even if both use the English word “channel.” An unmatched donor-original term can motivate a **separate provisional DIM row** after later source review; a source term may warrant multiple row decisions. Keep the counterexample and source note with the evidence, rather than filling all neighboring donor cells. Blanks, unique rows and conditionally populated cells are part of the design.

## 4. Positive example — an already documented plausible correspondence

| OPC UA Devices 1.05 | CSAPI Part 2 | **Proposed DIM** |
| --- | --- | --- |
| `Manufacturer` | *(no comparison attempted in this schematic example)* | **Manufacturer name** |

The [original owner-approved sample](../Deliverables/DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026.json) records OPC UA Devices' **`Manufacturer`**, `§4.5.2 VendorNameplate; §4.7 Table 35`, as `DIRECT` for **Manufacturer name**. This Step03 illustration copies that existing comparison into the new format with source issuer **OPC Foundation**, original document **OPC 10000-100**, edition **1.05.0 (2025)**, [publisher original source URL](https://reference.opcfoundation.org/specs/OPC-10000-100/) and historical register artifact **104**. It is deliberately `sourceVerification: PRIOR_SOURCE_EXTRACT_ONLY`, `originalCheckedAt: null`, `disposition: PROPOSED` because Step03 **did not newly inspect or re-validate those exact normative sections**.

This mapping can make sense **if the referent is the same identified product/equipment subject**. It does **not** establish that the manufacturer equals the system operator, station owner, data-service publisher, or the physical unit's serial number. The original-source clause and any finer distinctions still need to be checked when OPC UA Devices is reviewed in its planned donor iteration.

**What the example proves:** the new schema can record a promising *working comparison* with an exact cited source pointer **without lying that the original standard was freshly verified**. It does not prove formal correspondence, standard adoption or new mapping content.

## 5. Negative example — preserve an attractive but false equivalence

| OPC UA Devices 1.05 | CSAPI Part 2 | **Proposed DIM** |
| --- | --- | --- |
| *(not examined here)* | **[BLANK — deliberately rejected `DataStream` equivalence]** | **Addressed transducer channel** |

The owner-approved sample already associates the source-native IEEE 1451 **`TransducerChannel`** with the proposed DIM **Addressed transducer channel**, while separately recording CSAPI `DataStream resultSchema` under the **Reported output field** meaning. The old [source-native term comparison](../Concept_Donor_Comparison/Donor_Terms_Side_by_Side.md#components-and-channels) explicitly notes that CSAPI **DataStream is not a native IEEE transducer channel address**. For this deliberately rejected proposed match, the example retains original OGC source **OGC 23-002 Part 2 v1.0.0, §9.2**, [original OGC URL](https://docs.ogc.org/is/23-002/23-002.html), historical artifact **11**, `relation: RELATED_BUT_DIFFERENT`, `disposition: REJECTED`, and `sourceVerification: PRIOR_SOURCE_EXTRACT_ONLY`. This is a **negative example**, not a proposed new CSAPI-to-channel mapping and not a fresh normative finding.

A reporting DataStream may publish data that ultimately originated from an addressed physical channel; that **does not make the API resource itself the channel, its hardware identifier or its address**. The rejected comparison must remain auditable in the evidence record but must **not populate the CSAPI cell in that row**. That is why the schema records both **semantic relation** and **mapping disposition** instead of storing only a text string in the visible spreadsheet.

**What this example proves:** the record system can preserve a tempting source comparison **as a documented rejection**, not promote it to the model, and also preserve the source/edition and verification limits.

## 6. Exact display and integrity rules for future generation

1. **Keep the accepted master geometry:** fixed donor columns left→right, **proposed DIM far right**, full-width labeled group dividers. Internal row/cell/section IDs and long citations belong in a supporting sheet, not a new leftmost main column. The old 22-row sample and its CSV/JSON remain untouched as the baseline.
2. **Render a cell only when a working comparison is displayable:** a proposed/direct or proposed/partial mapping can be visible as a *working* hypothesis with explicit evidence limitations; `REJECTED` and `HELD` do **not** silently fill a false equivalence. `NO_ESTABLISHED_MAPPING` must not render as a false “absent” claim. Clearer visual styling is a future workbook-format decision in Steps05–06; no redesign occurred here.
3. **Do not count proposed/partial/related mappings equally in the final donor ranking.** The sample uses raw populated counts; the final least→most **breadth of supported contributions** needs distinct-row counts and source standing, separated by DIRECT vs BROADER/NARROWER/PARTIAL. No votes by 182 source-artifact filenames. Ranking remains provisional until synthesis.
4. **Enforce basic record integrity:** unique stable donor/row/decision/section keys; every row's section and every cell's row/donor foreign keys resolve; no duplicate acceptance of incompatible meanings without documented qualification; source issuer/edition/locator/URL nonempty; relation/disposition/verifier enumerations valid; original-check reviewer/date mandatory only when actually checked; no final owner approval inferred from a project mapping rating.
5. **Schema limits:** The committed Draft 2020-12 JSON Schema can validate structure, enumerations, key formats and conditional verification/disposition requirements, but **cannot by itself establish unique IDs, resolve foreign keys, confirm original URLs, validate citations or prove semantic correspondence**. Those require later deterministic checks plus primary-source review. A schema `PUBLISHER_ORIGINAL` pointer identifies an issuer URL, **not** proof it was actually retrieved.
6. **Do not backfill original baseline statuses or update the prior 182-artifact register here.** Step02 identified nine coverage/evidence issues D02-01–09; this Step03 *defines* a remedy for the schema/rubric portion, not evidence that any original donor source was newly reviewed or promoted to `ORIGINAL_CHECKED`.

**Why this is sized as one iteration:** one actual source-neutral schema, two already sourced illustration records and one human-readable decision rubric. **No new donor column roster, no new DIM concept, no new original-clause audit, no xlsx generation and no UML update**. The **primary observable product** is a trustworthy way to populate the owner-approved sheet, not another stand-alone information model or a premature conformance check.

### 6.1 Executed structural checks of the actual committed examples

The actual GitHub JSON Schema and two-record example JSON were read back after commit and parsed as JSON. A source-neutral local recursive structure/conditional checker found **zero violations** in the example and resolved **all donor/section/row foreign keys**. Deliberately false modifications were then tested: (1) assigning `ORIGINAL_CHECKED` without an actual original-source reviewer/date, (2) treating a prior-extract-only source claim as `ACCEPTED_FOR_RESEARCH_REVIEW`, and (3) marking a rejected DataStream-as-transducer-channel comparison `DIRECT`. All three **failed the relevant contract checks** as expected.

The source check in the revised schema also requires an `ORIGINAL_CHECKED` record to reference a `PUBLISHER_ORIGINAL` source, and an accepted-for-review relation to be `DIRECT`, `BROADER`, `NARROWER` or `PARTIAL_OVERLAP`. This is **a local structural/negative contract self-check**, not a fully executed third-party JSON Schema conformance suite, external source retrieval, semantic equivalence validation, or modification of the existing donor map.

## 7. Next single iteration — Step04 only

**NEXT owner “proceed”:** [Plan Step04](PLAN_Donor_Concept_to_DIM_Master_Crosswalk_v0.1_05NOV2026.md#phase-a--establish-controls-before-touching-the-mapping-0104) — identify an **eligible original donor-standard column roster** from the 13 developed/17 preliminary lineages plus actual 182-source context, distinguishing multiple editions, companion material, separate OPC UA Devices/PA-DIM and CSAPI/SensorML/SWE, and W3C SOSA/SSN vs Open Group SOSA. Record **eligible/companion/conditional/excluded/HOLD** and **provisional** display order only. Do **not** settle final least→most ranking, invent donor→DIM cells or rewrite the owner-approved 22-row sample.

**Step03 completion is the presence and verified readback of this rubric and both structured work files, not source agreement on any DIM concept.**
