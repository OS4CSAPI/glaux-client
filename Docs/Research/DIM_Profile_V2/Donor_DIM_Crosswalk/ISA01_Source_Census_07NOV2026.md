# ISA-01 — source census and coverage register

**7 November 2026 · ISA-01 technical work COMPLETE · one of twelve correction iterations. Next: ISA-02 only.**

## What was done

The original ISA Data Model Specification 6.0r12, dated 31 October 2023, has **480 named catalogue entries**. Their names were independently enumerated from its contents, located in body headings and reconciled against its final index. All 148 indexed PDF pages were recovered by overlapping text slices and checked for missing/duplicate page markers. No contents entry lacks a body/index location, and every entry has an assigned correction pass.

The categories are **6 services, 24 capability bins, 91 properties, 39 observables, 96 commands and 224 data-type entries**. These are distinct source entries by section and kind, not 480 new DIM rows or verified correspondences. A property and a data type sharing a name remain different entries. The source index labels both services and capability bins as modalities; the body sections disambiguate them.

The **eleven 2023 ISA 6.0 document covers, editions and contents were verified**, including all six companion guides. The previously catalogued **2015 paper is the twelfth source record**, retained as historical context; its full text was not located in this pass. That narrowly identified access item is assigned to ISA-11 and does not invalidate the available 2023 definition corpus.

The source-block register includes **279 assigned section/administrative/access blocks** across those documents. This is a structural queue, not a second count of unique concepts. Each DMS entry requires later review of its nested fields, parameters, results, enum values, constraints and referenced types; those children are not falsely counted as already reviewed.

## Why this fixes the earlier failure mode

Every one of the **22 existing DIM rows and nine case-review topics** now has an assigned pass. The **eleven previous ISA mappings and fourteen previous ISA findings** are individually registered for reconciliation. The prior native terms remain visible, but old empty cells explicitly say **Not reviewed** and give their assigned pass. No empty cell is evidence of a donor deficiency.

Manufacturer, Model and Serial Number are explicitly scheduled for ISA-02; the inventory is not permission to fill those cells before reading their exact definitions and subject scope. Other source concepts will be examined even when the current table has no row for them.

## Two corrected source boundaries

The property catalogue continues to **printed p.18 / PDF p.33** with **Zones** and **Zoom**. ISA-03 owns both. The observable catalogue continues to **printed p.22 / PDF p.37** with **Solar Radiation**, **Velocity**, and **Verified By**. ISA-04 owns all three. Shared-page section boundaries are now entry-based, not clipped by an approximate page range.

## Named-entry workload

| Pass | Assigned DMS entries |
|---|---:|
| ISA-02 | 49 |
| ISA-03 | 42 |
| ISA-04 | 39 |
| ISA-05 | 48 |
| ISA-06 | 50 |
| ISA-07 | 54 |
| ISA-08 | 25 |
| ISA-09 | 55 |
| ISA-10 | 88 |
| ISA-11 | 30 |

Model and Serial Number are included in ISA-02's 49 entries for immediate known-omission repair and are not double-counted in ISA-03. Companion sections have separately assigned owners. The estimate of twelve iterations is retained; a future genuinely oversized batch must be subdivided transparently rather than skipped.

## Checks performed

Contents/body/index: **480/480/480**. Unassigned named entries, source blocks, row targets and former ISA findings: **zero**. Baseline CSV Git blob was reproduced exactly as **fc271b757bcd094866f428bf7c3dc67bee7cc8eb** before generating the new view; all non-ISA and equipment-case display cells remain equal to that source. Semantic mappings added or revised in ISA-01: **zero**. The original census checks passed locally. Publication recovery repeats hash, census-accounting and workbook-preservation checks in GitHub; see the publication record.

## Publication and continuity

The completed ISA-01 checkpoint is published on `research/dim-profile-v2`, together with the [lessons record](LESSONS_Donor_Review_Process.md) and [publication verification](ISA01_Publication_Recovery_07NOV2026.json). The recovery restored the saved fourteen-file checkpoint; it did not repeat the source census. All saved file hashes were checked before publication metadata was updated. The current workbook differs only in four publication-label cells.

**Next owner “proceed”: ISA-02 only — identity and the first property block.**
