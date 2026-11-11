# SOSA G3-N1 — C239/S251 artifact edition and native-original access (11 November 2026)

**G3-N1 is complete as a bounded access-and-lineage inventory only.** The twelve original registered The Open Group SOSA artifacts were checked by identifier, edition and source access, and all eight printed C239 Appendix B normative native filenames have explicit unresolved access standings. This packet did **not** read a native Domain-Specific Data Model (DSDM), Interface Definition Language (IDL), or OpenAPI schema; no equivalence, field, cardinality or runtime test was invented. [Machine-readable full item/hold/access ledger](SOSA_G3_N1_Source_Access_Ledger_11NOV2026.json).

## Primary originals and edition boundary

The original indexed `c239_5.pdf` (Project/Library file `file_00000000af4081f58c4bac329f85c58f`) was reread at its original cover and Appendix B/C pointers: PDF pages **1–2 and 390–392 of 403**. It identifies the The Open Group **C239 Edition 1.1, published June 2023**, with a **September 2023 erratum** to Rule 6.4.2-22. Appendix B is *Normative*, but identifies attached filenames only; its eight actual model/IDL/OpenAPI contents were not available in the indexed text. Attempting to materialize the original PDF binary failed because that Project file lacks an authorized raw-byte path, so **the PDF embedded-attachment manifest cannot be verified**.

A distinct [public original 2022 S221 snapshot](https://www.vdl.afrl.af.mil/programs/arsenl/files/SOSA%20Technical%20Standard%20Edition%202.0.pdf) is readable: its title identifies **Edition 2.0 Snapshot 1, document S221, August 2022**, valid as a draft snapshot through 1 March 2023. S221 Appendix B prints `SOSA_TechStd_V2_SS1_DSDM`, `SecurityServices-SysMan-API.json` and `ChassisManager-SysMan-API.json`; original C239 instead prints `SOSA_TechStd_v1_DSDM`, `Security Services-SysMan-API.json` and `Chassis Manager-SysMan-API.json`. These are printed edition-specific identity differences, **not** proof of renamed/equivalent schema contents. The publicly announced **2025 S251 Edition 2.0 Snapshot 3** is later and different again; neither it nor its original registered ZIP was retrieved. [Dated 2025 release account](https://www.eejournal.com/industry_news/the-open-group-sensor-open-systems-architecture-or-sosa-consortium-releases-the-technical-standard-for-sosa-reference-architecture-edition-2-0-snapshot-3/).

## Twelve registered lineage sources — G3-N1 status

| Register ID | Exact source family / filename | Access conclusion |
| ---: | --- | --- |
| 47 | C212 Ed1.0 | Original native/earlier edition not obtained |
| 48 | Edition1.0 DSDM | Original native/earlier edition not obtained |
| 49 | C239 Ed1.1 original | PDF indexed text accessible; embedded bytes unknown |
| 50 | SOSA_TechStd_v1_DSDM_IDL | Original native/earlier edition not obtained |
| 51 | System Manager-SysMan-API.json | Original native/earlier edition not obtained |
| 52 | Module-SysMan-API.json | Original native/earlier edition not obtained |
| 53 | Security Services-SysMan-API.json | Original native/earlier edition not obtained |
| 54 | Chassis Manager-SysMan-API.json | Original native/earlier edition not obtained |
| 55 | PIC-SysMan-API.json | Original native/earlier edition not obtained |
| 56 | PIC with SW RTE-SysMan-API.json | Original native/earlier edition not obtained |
| 57 | S251 Ed2 Snapshot3 original | 2025 release known; original not obtained |
| 58 | 2025 S251 bundle ZIP | ZIP registered; archive not obtained |

The C239 model `SOSA_TechStd_v1_DSDM` is an **additional original normative dependency** identified by C239 B.1 but not a separate row in the twelve-item G1 register; do not swap in the Edition 1.0 predecessor model. Restricted C239 Appendix C is another separate dependency, not an inspected Appendix B attachment. The existing stable source IDs `SOSA-G1-X01` and `SOSA-G1-X02` remain active for these two exceptions.

## Eight specific C239 files still needing original inspection

| Original section | Printed original filename | Role | Source-byte access |
| --- | --- | --- | --- |
| B.1 | `SOSA_TechStd_v1_DSDM` | DSDM | **Not obtained** |
| B.1 | `SOSA_TechStd_v1_DSDM_IDL` | IDL | **Not obtained** |
| B.2 | `System Manager-SysMan-API.json` | OpenAPI | **Not obtained** |
| B.3 | `Module-SysMan-API.json` | OpenAPI | **Not obtained** |
| B.4 | `Security Services-SysMan-API.json` | OpenAPI | **Not obtained** |
| B.5 | `Chassis Manager-SysMan-API.json` | OpenAPI | **Not obtained** |
| B.6 | `PIC-SysMan-API.json` | OpenAPI | **Not obtained** |
| B.7 | `PIC with SW RTE-SysMan-API.json` | OpenAPI | **Not obtained** |

All eight original names were verified in actual indexed C239 Appendix B text, **none of their native bytes was obtained**. Thus model entity definitions, API fields, rules, interactions, service security, cardinalities, and edition fingerprints remain unreviewed. The apparently old `TechStd_v1` name within C239 Edition1.1 also does not independently establish the native file version.

## Exact access limitations

Source routes checked: original Project/Library PDF text; Library title/file searches; raw PDF materialization (authorization failure); The Open Group [C239](https://publications.opengroup.org/standards/sosa/c239) and [S251](https://publications.opengroup.org/standards/sosa/s251) publication pages (not accessible through the research browser); exact public/code filename searches (no genuine originals returned); original public S221 snapshot cover/Appendix B; and 2025 release metadata. **A failed search or browser access is not proof that the publisher lacks these files.** No public S221 model/API contents, original S251 ZIP contents or C239 embedded-file manifest were audited.

- **SOSA-G3-N1-H01:** C239 searchable original PDF cannot be materialized as raw bytes; embedded-file manifest unexamined.
- **SOSA-G3-N1-H02:** C239 DSDM original SOSA_TechStd_v1_DSDM unexamined, separately not registered within 12.
- **SOSA-G3-N1-H03:** C239 IDL original SOSA_TechStd_v1_DSDM_IDL unexamined.
- **SOSA-G3-N1-H04:** System Manager native OpenAPI original unexamined.
- **SOSA-G3-N1-H05:** Generic Module native OpenAPI original unexamined.
- **SOSA-G3-N1-H06:** Security Services native OpenAPI original unexamined.
- **SOSA-G3-N1-H07:** Chassis Manager native OpenAPI original unexamined.
- **SOSA-G3-N1-H08:** PIC native OpenAPI original unexamined.
- **SOSA-G3-N1-H09:** PIC with SW RTE native OpenAPI original unexamined.
- **SOSA-G3-N1-H10:** Original 2025 S251 Snapshot3 and sosa_ts_ed.2_v.3_bundle.zip unexamined; publisher page inaccessible in research tool.
- **SOSA-G3-N1-H11:** Original 2021 C212 and predecessor Edition1.0 DSDM not obtained.
- **SOSA-G3-N1-H12:** 2022 S221 and 2023 C239 different edition filenames and unknown native content; no verified structural or semantic equivalence.
- **SOSA-G3-N1-H13:** C239 Appendix C restricted overlay unexamined; source pointer only.

## Master, completeness, and owner boundary

**No source-qualified native model/API facts were earned, so no master or Excel changes were warranted.** The canonical JSON, **both CSV mirrors, both Markdown comparisons and same editable 26-sheet Excel** remain at the independently verified **G2-7T** checkpoint: **346×15 saved cells**, 22 preserved historical sheets, zero Excel lag and SHA-256 `46d12624bcdf23c017421ad84262c5bb4761bba4b47181f6ac874f38d60ec9f0`. This is *inherited* validation, not a newly run G3-N1 workbook publication or independent verifier. No historical cases, ISA findings, donor columns or provisional DIM proposals were modified.

The original C239 192-heading register remains **189 at least sampled/inline-reviewed, two substantively unread, one restricted**—not 189 complete clause audits. **SOSA remains ACTIVE/OPEN** and Step18 SAPIENT remains BLOCKED, with no adopted Domain Information Model (DIM) class/chassis/cardinality, OGC API – Connected Systems Profile SHALL, native API command or real hardware conformance.

**Next separate owner Proceed: G3-N2 ONLY.** Inspect authentic **C239-specific DSDM and IDL** native originals if obtainable, otherwise record the exact bounded **PARTIAL/inaccessible** disposition without fictional definitions and stop. Do not run G3-N3/N4 or the final G4/G5 gate, change donor, or adopt a DIM/Profile. Five conditional plan steps remain, and this number is not a source-completion guarantee.
