# G2-4A saved Excel and source-first bounded closeout (10 November 2026)

**G2-4A source semantics unchanged; Excel synchronization now VERIFIED.** The older “20 cells behind” statement further down in this research record described the intermediate prepublication checkpoint, now superseded. The SAME canonical 26-sheet workbook now contains all 20 G2-4A qualified SOSA column-I cells; [actual saved-cell verification](SOSA_G2_4A_Workbook_Validation_10NOV2026.json) and [GitHub check PASS](https://github.com/OS4CSAPI/glaux-client/actions/runs/42815270533) confirm 346×15 JSON/2CSV/2Markdown/XLSX parity and 22 unchanged historical sheets. SHA-256 `fe63866c0ac561e9efcb903f72c5b108814afd3b4f3ee3bd1973dd6d1b5c4a0e`. Original Chapters7–11 and native companions remain unread in this packet. No class/field/cardinality/Profile adoption or runtime test. **Next separate owner Proceed: G2-4B original Chapters7–11 only.**

## Earlier source report and superseded prepublication Excel status

# SOSA-G2-4A — Original C239 Chapters 1–5 original-source and master review (10 November 2026)

**Bounded G2-4 source packet, not completion of G2-4 or of the The Open Group SOSA donor.** Original publisher *The Open Group*, *Technical Standard for SOSA Reference Architecture*, Edition 1.1, C239 (2023), project Library `file_00000000af4081f58c4bac329f85c58f`, actual inline C239 PDF pp27–63 (printed1–37) reviewed. **All 42 originally registered TOC headings** across Chapters1–5 were read at original *inline text/table and figure-caption/label* depth: 27 previously UNREAD and 15 previously SOURCE_READ sampled. The source's RIG, certification policy, standalone DSDM/IDL/OpenAPI original files, detailed original figure pixels and external standards were not audited. Reading this prose is neither complete source corpus nor author-approved DIM/Profile adoption.

## Native-source evidence, not class proliferation

[One original source and coverage ledger](SOSA_G2_4A_Original_Source_Item_Coverage_10NOV2026.json) records each TOC heading's previous G1 standing, source edition and exact start page, all **95 inventoried named native terms/entries**, original type and standing:
| Native original item type | Item count | Interpretation |
|---|---:|---|
| quality attribute | 10 | Native label/context/quality or implementation design source item; **not** a DIM element or conformance SHALL |
| architecture principle | 15 | Native label/context/quality or implementation design source item; **not** a DIM element or conformance SHALL |
| module catalog | 27 | Native label/context/quality or implementation design source item; **not** a DIM element or conformance SHALL |
| physical context | 6 | Native label/context/quality or implementation design source item; **not** a DIM element or conformance SHALL |
| taxonomy term | 7 | Native label/context/quality or implementation design source item; **not** a DIM element or conformance SHALL |
| decomposition criterion | 7 | Native label/context/quality or implementation design source item; **not** a DIM element or conformance SHALL |
| implementation example | 5 | Native label/context/quality or implementation design source item; **not** a DIM element or conformance SHALL |
| data model level | 3 | Native label/context/quality or implementation design source item; **not** a DIM element or conformance SHALL |
| other native concept | 15 | Native label/context/quality or implementation design source item; **not** a DIM element or conformance SHALL |
| **Total original named source items** | **95** | NOT ninety-five adopted DIM classes or Profile fields |

The 10 Table3.1-1 quality attributes and 15 numbered architectural principles are source *drivers*, not a list of mandatory reportable equipment fields. Table4.2-1 defines **27 module catalogue positions (24 named, three Reserved)**; it explicitly says not every module is instantiated in a SOSA sensor, and §1.6 says not every desired module has requirements specified in the 2023 edition. Sources distinguish service functions such as System Manager, Task Manager, Reporter, Network Subsystem, power, calibration and processing without demanding one physical device per role.

**Physical vs logical (§§4.1,5.1–5.3):** A SOSA sensor is an aggregate of one/more sensor hardware elements; the host platform, optional integral Sensor Pod, physical aperture/card/enclosure, logical SOSA Module, software RTE, interaction infrastructure and procurable unit have different referents. The taxonomy explicitly stops short of implementation and procurement hierarchies; procurable units may implement several modules and vice versa. The five examples in §5.3 are **illustrative implementations**, not tested installations or products. Preserve separate identity, physical relationship, logical function, host relation and product instance; no universal chassis or approved model tree.

**Scope and source boundary (§§4.2,5.4):** System Manager performs housekeeping, discovery, health, configuration, security, while Task Manager handles mission-oriented tasking, resources and outputs. §5.4 says Task Manager modules are not ready for publication in this edition; do not treat a preliminary module description as a complete native command API. Reporting Services packages/disseminates reported data, and source service-flow illustrations are not installed equipment telemetry.

**Conformance/edition (§§1.3,2.1.2,5.7):** C239 gives source keywords Rule/Recommendation/Permission/Observation/Suggestion and says unlabeled narrative is descriptive. SOSA certification phases are a program description, not a certificate for our case products. §1.4 prints Normative References: None, while §5.7 points normative data-model text at Appendix B.2 although Appendix B.1 names original DSDM; original native files unread. DIV-1/2/3 are conceptual/logical/physical *data-model levels* and DO NOT prove fields/types/cardinalities in those unread schemas.

**Airworthiness/security (§5.5–5.6):** Aircraft mission equipment versus flight safety requirements and qualification are host/application-specific guidance, not a universal sensor mandate. Security Manager is a function of System Manager; its security primitives do not establish a certificate attribute or live verified authentication for any device.

## Source-qualified integration into the same master

Exactly **20 existing The Open Group SOSA (column I) cells** now contain source-qualified comparisons and caveats with stable source IDs. No rows added/renamed/reordered; all four source-case columns, other donor comparisons, ISA source evidence, previous SOSA-D/G2-1/2/3 contributions, provisional DIM and topic dividers remain intact. These donor mappings are neither accepted DIM model elements nor new CSAPI Profile SHALLs.

| Existing information row | Evidence and relation | Source item examples | Negative equivalence or hold |
| --- | --- | --- | --- |
| S06-R005 — Described sensing System / arrangement | PARTIAL | SOSA-C239-G2-4A-PHYSICAL_CONTEXT-001, SOSA-C239-G2-4A-TAXONOMY_TERM-001 | SOSA sensor scope is architecture- and modality-specific, not all real world sensing arrangements or a new universal DIM root |
| S06-R007 — Physical constituent | PARTIAL | SOSA-C239-G2-4A-PHYSICAL_CONTEXT-002, SOSA-C239-G2-4A-TAXONOMY_TERM-001 … | Logical module identity may map to hosted physical elements many-to-many; do not invent source hardware containment |
| S06-R008 — Connected external equipment | RELATED | SOSA-C239-G2-4A-PHYSICAL_CONTEXT-005, SOSA-C239-G2-4A-PHYSICAL_CONTEXT-006 | Sensor boundary or interface type is not identified external equipment or observed cable |
| S06-R009 — Hosting platform / station context | PARTIAL | SOSA-C239-G2-4A-PHYSICAL_CONTEXT-003, SOSA-C239-G2-4A-PHYSICAL_CONTEXT-004 … | A delivered integral sensor pod is not automatically an independent host; an RTE is software infrastructure, not physical hosting platform |
| S06-R006 — Network-visible participant | RELATED | SOSA-C239-G2-4A-TAXONOMY_TERM-005, SOSA-C239-G2-4A-OTHER_NATIVE_CONCEPT-011 | A module or interaction transport is not necessarily an independently network-addressable CSAPI/ISA participant |
| ISA-A-MEMBER-EXPOSURE — Composition member exposure and source attribution | NO_ESTABLISHED | SOSA-C239-G2-4A-TAXONOMY_TERM-006, SOSA-C239-G2-4A-TAXONOMY_TERM-001 | Module logical composition and vendor implementation patterns cannot infer a real member-exposure policy |
| ISA-A-SERVICE-ROLE — Service role and required command support | RELATED | SOSA-C239-G2-4A-MODULE_CATALOG-001, SOSA-C239-G2-4A-MODULE_CATALOG-002 … | SOSA management/mission service roles differ from ISA Controller roles and do not establish universal service obligations |
| ISA-A-CIC-MEDIATION — Composition interface task mediation role | RELATED | SOSA-C239-G2-4A-MODULE_CATALOG-001, SOSA-C239-G2-4A-MODULE_CATALOG-002 | No direct equivalence to ISA composition interface task mediation or observed host control path |
| S06-R019 — Issued control request | RELATED | SOSA-C239-G2-4A-MODULE_CATALOG-002, SOSA-C239-G2-4A-OTHER_NATIVE_CONCEPT-006 | Mission task requests and administrative control requests differ; neither proves executed task in a source case |
| ISA-K-CAPABILITIES — Declared component capability catalogue | RELATED | SOSA-C239-G2-4A-MODULE_CATALOG-001, SOSA-C239-G2-4A-MODULE_CATALOG-007 … | Design catalog is not ISA component-specific declared capability set, required membership or runtime support |
| ISA-K-TYPE-CHOICE — Declared built-in or custom value type | NO_ESTABLISHED | SOSA-C239-G2-4A-DATA_MODEL_LEVEL-001, SOSA-C239-G2-4A-DATA_MODEL_LEVEL-002 … | Cannot assert SOSA-to-ISA built-in/custom type, bounds, multiplicities or JSON encodings from prose |
| ISA-A-CONNECTION-PRESENTATION — Negotiated message encoding and model version | RELATED | SOSA-C239-G2-4A-OTHER_NATIVE_CONCEPT-001, SOSA-C239-G2-4A-OTHER_NATIVE_CONCEPT-002 | Not an ISA negotiated version/encoding, session handshake or concrete CSAPI binding |
| ISA-A-NETWORK-CONTEXT — Network instance and connection context | RELATED | SOSA-C239-G2-4A-OTHER_NATIVE_CONCEPT-001, SOSA-C239-G2-4A-OTHER_NATIVE_CONCEPT-002 | Defined interconnects are not ISA network instance identifier, live link or network topology observation |
| S06-R012 — Reported output field | RELATED | SOSA-C239-G2-4A-MODULE_CATALOG-017, SOSA-C239-G2-4A-MODULE_CATALOG-016 | Report packaging/archival roles do not establish an OGC observable/reported output field schema |
| CASE-H03 — REVIEW HOLD — reporting path | RELATED | SOSA-C239-G2-4A-OTHER_NATIVE_CONCEPT-005, SOSA-C239-G2-4A-MODULE_CATALOG-017 | Hypothetical SOSA flow and generic module service do not verify vendor equipment source reporting paths |
| CASE-H02 — REVIEW HOLD — site / mounting | RELATED | SOSA-C239-G2-4A-PHYSICAL_CONTEXT-003, SOSA-C239-G2-4A-PHYSICAL_CONTEXT-004 | Source example mounting/pod relationships are not measured sites, mounts, attachments or actual equipment placements |
| ISA-T-ACCESS — Request access-control metadata | RELATED | SOSA-C239-G2-4A-OTHER_NATIVE_CONCEPT-007, SOSA-C239-G2-4A-MODULE_CATALOG-018 | No source-native ISA request access-control metadata schema, authorization grant or deployed permission inferred |
| ISA-C-099 — Reported physical parent/child attachment relationships | RELATED | SOSA-C239-G2-4A-PHYSICAL_CONTEXT-002, SOSA-C239-G2-4A-PHYSICAL_CONTEXT-003 | Source physical architecture is not source-reported device attachment graph or cardinality |
| ISA-T-CONFIG — Component capability and readiness report | RELATED | SOSA-C239-G2-4A-DATA_MODEL_LEVEL-001, SOSA-C239-G2-4A-DATA_MODEL_LEVEL-003 | Data-model level is not an ISA telemetry/configuration message or observed readiness |
| ISA-A-CAPABILITY-GROUP — Capability group membership | RELATED | SOSA-C239-G2-4A-DECOMPOSITION_CRITERION-004, SOSA-C239-G2-4A-DECOMPOSITION_CRITERION-002 | Design grouping criteria are not membership/required-support fields in a device capability manifest |

## Exact source holds (not invented repairs)

- **SOSA-G2-4A-H01 — NATIVE_COMPANION_NOT_REVIEWED:** Reference Implementation Guide (RIG) three sensor-design examples are explicitly hypothetical; source file not inspected, do not treat as actual source equipment cases Original locator §1.2.4 p31.
- **SOSA-G2-4A-H02 — SOURCE_COMPANION_UNREVIEWED:** Conformance Verification/Certification Policy and Product Sets described but original policy and certification registers not inspected; cannot assert external product certification Original locator §1.3 pp31–32.
- **SOSA-G2-4A-H03 — SOURCE_INTERNAL_NORMATIVE_REFERENCE_CONFLICT:** §1.4 says Normative References None, while §5.7 states normative data model at B.2 and Appendix B.1 names DSDM; original DSDM/IDL and B.2 OpenAPI not inspected. Preserve exact source discrepancy and edition. Original locator §1.4 p32 vs §5.7 pp61–62, Appendix B.1/B.2 p390.
- **SOSA-G2-4A-H04 — NORMATIVITY_BOUNDARY:** Rule requires shall, Recommendation should, Permission may, Observation no requirement, unlabeled prose descriptive. Do not elevate module descriptions or possible future capabilities as normative Profile shall. Original locator §2.1.2 pp34–35.
- **SOSA-G2-4A-H05 — SOURCE_DESIGN_NOT_PRODUCT_CONFORMANCE:** Quality attributes and 15 source Architecture Principles are design drivers and broader objectives, not individually verified runtime behavior or universal information fields. Original locator §3.1–3.2 pp36–45.
- **SOSA-G2-4A-H06 — SOURCE_GRANULARITY_SEPARATION:** Sensor, external host, optional sensor pod, physical hardware, logical module, software runtime, interaction infrastructure, procurable unit are different referents; no universal chassis/class tree or ISA exact equivalence. Original locator §4.1 pp46–48, §5.1 pp55–56, §5.3 pp57–58.
- **SOSA-G2-4A-H07 — EDITION_AND_IMPLEMENTATION_COVERAGE:** Tables include reserved modules, incomplete edition-dependent functionality, Future EO/IR & Comms flow work; not all modules are instantiated or defined or usable by current hardware. Original locator §4.2–4.3 pp49–54 and §1.6 p33.
- **SOSA-G2-4A-H08 — HOST_CONTEXT_SPECIFIC:** Airworthiness/qualification discussion addresses aircraft mission/flight equipment; no universal requirement for all host environments and no proof of case equipment qualification. Original locator §5.5 pp58–60.
- **SOSA-G2-4A-H09 — NATIVE_SCHEMA_AND_FIGURE_NOT_FULLY_AUDITED:** Data-model DIV1/DIV2/DIV3 logical source roles and interconnect diagram inspected at text/label depth, but original C239 DSDM/IDL/native OpenAPI and exact figure pixel/edge geometry not verified. Original locator §5.7–5.8 pp61–63.
- **SOSA-G2-4A-H10 — NEXT_PACKET_WITHIN_ACTIVE_G2_4:** Explicit authorized G2-4 wider scope remains pending; 27 TOC headings are NOT comprehensively reviewed by the current source packet. Earlier sampled material remains only historical samples. Original locator C239 Chapters 7–11 original TOC starts p141; 27 headings.

## Corpus coverage and actual stopping rule

C239 original G1 TOC has 192 headings. Before this packet, G2-3 had at least 75 sampled/inline-read headings, 116 substantively unread, and one restricted. Reading 42 Chapter1–5 headings at inline text depth, of which **27 were previously unread**, advances the bounded count to **102 at least source-read, 89 substantively unread, one restricted**. That count is not a certification of full original normative source coverage; relevant native schemas and visual figure details remain unverified. **Chapters7–11 remain 27 registered headings pending review** (only earlier selected source samples exist for eight of them). This source packet is **G2-4A only**, not a donor-completion gate, no SAPIENT transition.

**L23 Excel publication:** Current JSON, both CSVs and both human-readable comparisons have 20 G2-4A SOSA-column changes. The SAME existing 26-sheet canonical XLSX remains the verified G2-3 snapshot SHA256 `8dab9447dd00ede955a1cdc36d48493d54726bf0d40c9b409b0da47801381750` until the mandatory same-packet publisher verifies all 346×15 saved XLSX cells and preserves historical sheets. Do not advance until that checkpoint succeeds.

**ONE next step on a separate owner Proceed after verified saved Excel:** **SOSA-G2-4B**, source-first C239 Chapters7–11 Transmission/Reception, task management, signal/target processing, analysis, convey/report native details, sized by original source complexity. No G2-4B review, hardware deployment, DIM/Profile adoption or donor transition authorized here.
