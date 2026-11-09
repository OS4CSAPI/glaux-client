# Step 17 SOSA-D — bounded source-first integration and verification closeout

**9 November 2026 · COMPLETE at the authorized scope, with explicit native-source holds.** The Open Group SOSA C239 Edition 1.1 (June 2023, September erratum) now has a **distinct** donor column in the [source-backed horizontal master](Master_Donor_Concept_to_DIM_Crosswalk.md), [structured JSON](Master_Donor_Concept_to_DIM_Crosswalk.json), [CSV](Master_Donor_Concept_to_DIM_Crosswalk.csv), and [verified canonical Excel workbook](Master_Donor_Concept_to_DIM_Crosswalk.xlsx). W3C SOSA/SSN remains a separate column, and the five foundational sensing/observation columns stay together to its right. The proposed DIM is still rightmost.

## Exactly what changed

- One donor column added after ISA: **The Open Group SOSA Reference Architecture Edition 1.1 (C239)**; total now **15 columns**, consisting of four source cases, ten donor standards and the proposed DIM.
- The original **329 information/review rows** and 15 group-divider rows are retained, producing a **346×15 source presentation grid**. No rows or DIM design elements were added, merged, deleted or adopted.
- Original source-first [SOSA-A architecture roles](Step17_SOSA_A_C239_Architecture_Roles_Evidence_09NOV2026.json), [SOSA-B management/status/tasking](Step17_SOSA_B_C239_Management_Operational_Evidence_09NOV2026.json), and [SOSA-C data-model/interface pointers](Step17_SOSA_C_C239_DSDM_Interfaces_Edition_Evidence_09NOV2026.json) are reconciled into a [complete **57-decision** integration ledger](Step17_SOSA_D_Source_First_Integration_09NOV2026.json), covering **76** C239 original native concept/pointer records and **38** distinct current master rows with qualified, related, partial, narrower, negative or held comparisons. The remaining 291 SOSA cells say *Not assessed here*, not *no equivalent exists*.
- All **58** previous donor evidence records, **73** four-case evidence facts, 480 ISA DMS entries (474 supported, six original questions open) and original case/design holds survive. No donor names, case fields or other donor comparisons were rewritten.

Examples: C239 **SOSA Sensor** partially supports the proposed described sensing System, **SOSA Hardware Element** is a specialized physical constituent, and **SOSA Host Platform** is a qualified physical hosting context. C239 **SOSA Module** is a logical role, not automatically a physical device; a C239 Request/Response or Task status does not prove performed physical control; and a native C239 data-product publisher is not automatically an OGC observation performer. Original C239 Power and Task Management completeness are edition-qualified: several functions are descriptive or preliminary rather than complete Edition 1.1 obligations.

## Crucial retained source limitations

C239 Appendix **B.1** names **`SOSA_TechStd_v1_DSDM`** and its **`SOSA_TechStd_v1_DSDM_IDL`** companion. Appendix **B.2–B.7** names six management OpenAPI files. These **eight native files were referenced in the original C239 PDF but were not obtained, opened or parsed**. C239 §5.7 refers to **B.2** as its data-model location, whereas the actual Appendix uses **B.1**; both original references were preserved without fabricated reconciliation. C212 Edition 1.0, C239 Edition 1.1, 2022 S221 Snapshot 1 and 2025 S251 Snapshot 3 retain their distinct edition/source standing. None of the 12 registered SOSA lineage artifacts is represented as independently audited merely from the C239 review.

Accordingly, this is **bounded original-C239 architecture/source evidence**, not field-by-field native DSDM coverage, native OpenAPI endpoint verification, SOSA standards conformance or evidence of hardware/platform operations. Related source concepts and case-only holds do not automatically become DIM classes or Profile obligations.

## Actual file publication and verified checks

The final [one-time source-to-workbook publication run](https://github.com/OS4CSAPI/glaux-client/actions/runs/42708698659) **PASSED**, and the updated [read-only current master verification run](https://github.com/OS4CSAPI/glaux-client/actions/runs/42709075807) **PASSED**. [Machine-readable validation record](Step17_SOSA_D_Workbook_Validation_09NOV2026.json) contains the exact binary checks, and the [preview from actual saved XLSX cells](Step17_SOSA_D_Workbook_Preview_09NOV2026.png) was retrieved and visually inspected.

**Current workbook SHA-256:** `531451e4b43b0502e9e90b62972a7398be048ceb3987eb24ef4963e3f0fb1fba`.

The canonical workbook retains all **26 original sheet names/order**. Four live review tabs were refreshed (Master Crosswalk, DIM Register, Summary, Validation); the XML contents of **22 historical tabs** are byte-for-byte unchanged. Every **346×15** saved workbook cell was compared against JSON/CSV source values. Both GitHub-readable comparison tables match, and ZIP CRC, XML parsing, 15 full-width group dividers, donor groups, frozen cases/header, unique row IDs and absence of Excel error-type cells were verified. The preview is a Python image from the **actual saved workbook cells**, not a Microsoft Excel-native layout/print rendering.

## Owner-controlled continuation

**Step17/SOSA-D complete at the bounded reviewed scope, with native DSDM/IDL/OpenAPI source gaps held.** The next step in the established 40-step cross-donor plan is **Step18: SAPIENT v2 source identity, registration, ModeDefinition, status and equipment reporting**, only on the user's **next separate “Proceed.”** Reassess the original BSI Flex 335 edition and nine historical source-extract-only mappings before calling SAPIENT fully reviewed; right-size any necessary donor-specific follow-up. Step19 remains SAPIENT task/acknowledgement follow-up, and Step24/35–40 retain explicit cross-donor reconciliation and model-adoption controls.
