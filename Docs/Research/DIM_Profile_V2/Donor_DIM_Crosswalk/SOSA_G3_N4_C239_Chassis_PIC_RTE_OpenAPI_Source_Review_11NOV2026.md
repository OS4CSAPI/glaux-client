# SOSA G3-N4 — C239 Chassis Manager, PIC and PIC-with-RTE management OpenAPI source-access review

**Date: 11 November 2026. One owner-authorized G3-N4 packet, STOP before G4-F. Grade: BOUNDED PARTIAL.** The original The Open Group SOSA *Technical Standard for SOSA Reference Architecture*, C239 Edition1.1 (2023), **normative Appendix B.5–B.7** names three native management OpenAPI JSON files. The exact original filenames were visually checked in the uploaded **c239_5(1).pdf** (PDF pages 390–391; printed pp364–365); the file contains zero embedded attachments. **None of the three original 2023 native JSON files was authenticated, obtained or audited.** The original file contents, not necessarily their existence, remain **UNREVIEWED**. [Complete stable-ID source access ledger, metadata, routes and holds](SOSA_G3_N4_C239_Remaining_OpenAPI_Source_Access_11NOV2026.json).

## Source identity: original C239 versus separate later S251

| C239 Appendix | Original C239 (2023) printed filename | Original 2023 native coverage | S251 2025 Appendix B printed filename | S251 2025 uploaded ZIP actual member |
|---|---|---|---|---|
| B.5 | `Chassis Manager-SysMan-API.json` | REFERENCE FULLY READ NATIVE FILE UNREVIEWED | `ChassisManager-SysMan-API.json` | `Chassis Manager-SysMan-API.json` |
| B.6 | `PIC-SysMan-API.json` | REFERENCE FULLY READ NATIVE FILE UNREVIEWED | `PIC-SysMan-API.json` | `PIC-SysMan-API.json` |
| B.7 | `PIC with SW RTE-SysMan-API.json` | REFERENCE FULLY READ NATIVE FILE UNREVIEWED | `SW RTE-SysMan-API.json` | `SW RTE-SysMan-API.json` |

The authentic uploaded **S251 Edition2.0 Snapshot3 (2025)** PDF was inspected *only for its corresponding Appendix B reference names* on PDF page 567 (printed536). The separately bundled JSON members were inspected for **identity metadata only**: `openapi = 3.0.0`, `info.version = 2.0.0-snapshot.3`, SHA256, byte sizes and path/schema counts. The **2025 filenames, path counts, schemas and security scheme identifiers do not establish the original C239 content**. None of those 2025 JSON operations, payloads, fields, HTTP methods, rules or runtime behavior was substantively audited at this step.

**Two specific naming mismatches are now directly verified:** C239 Appendix B.7 names `PIC with SW RTE-SysMan-API.json`, whereas S251 Appendix B.7 names and its ZIP contains `SW RTE-SysMan-API.json`. Further, S251 Appendix B.5 prints `ChassisManager-SysMan-API.json` (without a space) but the actual 2025 ZIP contains `Chassis Manager-SysMan-API.json` (with a space). The latter is a **within-S251 document-versus-bundle mismatch**, not evidence that the earlier 2023 and later 2025 chassis APIs are identical. These exact discrepancies must survive donor reconciliation; do not silently fix an original source.

## Access work and source-coverage grade

C239's original Appendix B.5–B.7 **pointer text** was fully read. A direct 2023 PDF attachment check found **zero embedded native files**; targeted web and GitHub source searches found no authentic 2023 JSON original; earlier G3-N1/G3-N3 access routes were reused without unnecessary repetition. The public result surfaced an earlier **2022 S221** snapshot containing filename references, not the desired original JSON bytes. Publisher/catalog access holds from earlier steps remain; an unavailable URL or search non-hit does **not** establish the standard publisher lacks the source.

**Source coverage:** 3/3 original C239 native-file *references* read; **0/3 2023 native files obtained; 0/3 original native API schemas audited**. Compared with C239, two 2025 ZIP member basenames are identical and the third is different; **neither filename equality nor a similar role is semantic equivalence**. No C239 management API endpoints, request/response objects, authentication, error codes, cardinalities, hardware command mappings, or deployed source-case behavior has been verified from these original native files.

## Eight exact source holds

- **SOSA-G3-N4-H01 (2023_C239_NATIVE_FILE_NOT_OBTAINED):** C239 Appendix B.5 Chassis Manager-SysMan-API.json. Original 2023 Chassis Manager API operations, schema semantics, requests, responses and requirements remain unreviewed.
- **SOSA-G3-N4-H02 (2023_C239_NATIVE_FILE_NOT_OBTAINED):** C239 Appendix B.6 PIC-SysMan-API.json. Original 2023 PIC API operations, schema semantics, requests, responses and requirements remain unreviewed.
- **SOSA-G3-N4-H03 (2023_C239_NATIVE_FILE_NOT_OBTAINED):** C239 Appendix B.7 PIC with SW RTE-SysMan-API.json. Original 2023 combined PIC with SW RTE API structures and constraints remain unreviewed.
- **SOSA-G3-N4-H04 (DISTINCT_EDITION_NO_2023_EQUIVALENCE):** Three 2025 S251 API members. S251 version 2.0.0-snapshot.3 metadata cannot be projected onto C239 Edition1.1 or adopted CSAPI Profile requirements.
- **SOSA-G3-N4-H05 (PRINTED_FILENAME_AND_ROLE_LINEAGE_CHANGED_EQUIVALENCE_UNKNOWN):** C239 B.7 PIC with SW RTE vs S251 B.7 SW RTE. The 2025 original and archive use SW RTE-SysMan-API.json, not the 2023 PIC with SW RTE-SysMan-API.json; do not assume one replaces or preserves the other.
- **SOSA-G3-N4-H06 (S251_PDF_ZIP_FILENAME_DISCREPANCY):** S251 Appendix B.5 name vs same edition ZIP member. 2025 S251 PDF prints ChassisManager-SysMan-API.json, whereas its uploaded archive contains Chassis Manager-SysMan-API.json; treat it as a source naming mismatch, not a verified alias.
- **SOSA-G3-N4-H07 (ACCESS_UNRESOLVED_NOT_SOURCE_ABSENCE):** 2023 publisher/native-source access channels. C239 PDF has no embedded attachments; targeted searches located no authentic C239 native JSON; cannot infer publisher lacks files.
- **SOSA-G3-N4-H08 (NATIVE_SEMANTIC_COVERAGE_BOUNDED_PARTIAL):** Original 2023 API meaning and modeled system runtime. No source-qualified new native mappings, adopted model requirements, API conformance, hardware commands, or source-case telemetry established.

## Canonical comparison and Excel standing

There are **zero new source-qualified native semantic mappings**, so the ONE canonical donor-to-DIM master JSON, **BOTH CSV mirrors, BOTH GitHub-readable Markdown comparisons and the SAME original editable 26-sheet Excel** remain **unchanged**, as required for an access-only packet. The last actual saved-cell verification is the **G3-N2** checkpoint, XLSX SHA256 `47c9df11ef64e112c8892e87c749930f08552c43a0e8e06508bb34ef8a04903c`, with matching 346×15 cells and preservation of 22 historical sheets. This is inherited verification, **not** a newly performed G3-N4 binary-workbook check; **Excel lag ZERO** because comparison content did not change.

The C239 text-heading register remains **189 of 192 at least sampled or inline-read, two substantively unread and one restricted**; this is not 189 completely audited headings, nor does it include the eight unreviewed native files. The separate original 2022 v1 DSDM/IDL source findings and later 2025 S251 edition remain lineage-qualified, not adopted as C239 2023 equivalents. **The Open Group SOSA donor stays ACTIVE/OPEN; Step18 SAPIENT remains BLOCKED**, with no accepted generic chassis, Domain Information Model classes or cardinalities, Connected Systems API Profile SHALLs, implementation conformity or actual equipment commands.

**ONE next separate owner Proceed: G4-F only** — reconcile the cumulative original SOSA source/heading/companion coverage and the existing donor-to-DIM master, distinguish actually complete evidence from partial/unavailable original material, and prepare the exact evidence-based donor closure assessment. **STOP before G5-D owner decision, SAPIENT Step18, model/Profile adoption, client/UI or deployment.** **Two planned gates remain**, conditional on source evidence and the owner's decision, not a guarantee of comprehensive source completion.
