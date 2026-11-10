# SOSA-G2-6A — Original C239 Hardware Element source audit and progressive donor-to-DIM integration

**Date:** 10 November 2026. **Source:** The Open Group SOSA Consortium, *Technical Standard for SOSA Reference Architecture*, Edition 1.1, C239 (2023), original project file `c239_5.pdf` (Library `file_00000000af4081f58c4bac329f85c58f`). **Owner-bounded source scope:** §§13.1–13.2.10, original PDF208–229 (printed182–203), with **only** the final sentence/line of the §13.2.10 CoV requirement read on PDF230. The separately headed §13.2.11 starts on PDF230 but was **not** audited or included. No other donor, model design, client/server code, deployment, device control or new DIM/Profile adoption.

## 1. Original-source coverage and individual item accounting

[Original source coverage and native-item ledger](SOSA_G2_6A_Original_Source_Item_Coverage_10NOV2026.json) has **13 registered original C239 table-of-contents headings**, **19 additional inline nested subsection headings**, **98 original Rule-labeled SHALL occurrences**, **eight Permissions**, **three Recommendations**, and **21 Observations**. Ten original tables and five figures were examined at published text, caption and numeric/row-label depth; source figure pixel/arrow/dimension geometry was not independently verified. **Eleven source-required Certificate of Volatility (CoV) documentation items** are individually identified; twelve project-written interpretive contexts are **not additional native requirements**. This is **156 native labeled/table/documentation records + 12 analytical summaries = 168 accountable records**, NOT 168 adopted DIM fields.

These 13 original headings were UNREAD in the prior G1 census, so the 192-heading C239 source-status baseline advances from **136 at least sampled/inline-read, 55 unread, one restricted** to **149 at least sampled/inline-read, 42 still substantively unread, one restricted**. Inline C239 text coverage is not original ANSI/VITA or DSDM/IDL/OpenAPI completion; zero original native-companion-complete section certifications are claimed.

## 2. Native meanings that must not be flattened

**Physical identity, form factor and host relations:** §13.1's hardware diagram is expressly illustrative; the PIC, PIC family/profile, physical chassis, backplane, host/platform interface, processing/payload/switch and separate Chassis Manager are not interchangeable identifiers. Rule13.2.1-1 specifically scopes OpenVPX PIC to ANSI/VITA 65.0 3U/6U form factors, not the only possible sensing System kind. Short **100mm 3U** conduction-cooled **1.2-inch-pitch** geometry and standard **160mm 3U** configurations have different fit; §13.2.4 warns the variants are generally not interchangeable. Backplane routing and limited front-panel exceptions do not establish a real external sensor cable, field mount or a universal physical DIM containment tree.

**Power vs battery vs management:** C239 §13.2.3 specifies conditional PIC VS1/VS2/VS3, 3.3V_AUX, **VBAT** and **ALT_VBAT** input/limits. A named rail or a 1mA/45mA current limit is **not evidence of an installed battery, charged flag, reserve, time-to-empty or current measurement**. §13.2.6 defines distinct 3U/6U **Power Supply Cards (PSCs)** with power input/output, return, remote-sense, geographical addressing, IPMC, current-sharing and ENABLE*/INHIBIT*/FAIL* signals. The original Table13.2.6.5-1 is a design state truth table, not recorded current device health or actual executed control.

**Cooling, modularity and maintenance:** §13.2.5 separates conduction, airflow-through and liquid cooling, with conditional host infrastructure and intermateability restrictions. §13.2.7 permits nonconformant mezzanine cards under specific rules, while §13.2.9 identifies XMC pin-overlay selections; source note points security overlays into **restricted Appendix C**, which was not read. §13.2.8 calls the Maintenance Console Port a **low-level UART board-maintenance/debug** interface, not an ordinary mission-operational interface or CSAPI ControlStream. Slot/profile compatibility, analog/optical connectors and pin overlays describe design, not user-visible network addresses or installed equipment.

**Certificate of Volatility:** §13.2.10 mandates a vendor CoV documentation package for conformable hardware and enumerates memory maker/type/function/size/write mechanism/protection and internal retention-supply disclosures. A source CoV requirement is not proof that any of the four source case vendors supplied or that this project inspected an original CoV. The source warns that some embedded/undocumented internal nonvolatile memory may be beyond a CoV's scope; no complete sanitization or manufacturer authentication is claimed.

**Source-text discrepancies retained:** Rule13.2.4.2-9 twice cites Table13.2.4.2-1 despite the distinct Table13.2.4.2-2. Rule13.2.3.2-5 spells ALT_VBATT where other text uses ALT_VBAT; the Figure13.2.4.2-2 caption prints `100m`; and Rule13.2.6.6-8 prints `–DC/CAN` where neighboring material uses `–DC/ACN`. No undocumented correction was asserted. Native ANSI/VITA 46/48/62/65/66/67 and restricted security sources remain independently unexamined.

## 3. Source-qualified integration into the SAME canonical master

Exactly **39 existing The Open Group SOSA donor column I** comparison cells have been qualified with original source IDs, relation and negative-equivalence boundaries. No rows, groups or column names were added/reordered. Original **329 information rows, 15 columns, 58 prior donor facts, 73 manufacturer/historical case facts**, ISA 480 outcomes/six questions and previous SOSA G2-1–G2-5 correspondence remain retained. [Canonical current horizontal comparison](Master_Donor_Concept_to_DIM_Crosswalk.md) and [source JSON](Master_Donor_Concept_to_DIM_Crosswalk.json) preserve the full row-level evidence, not a one-source-term/one-DIM-class proliferation.

| Existing row | Relation and inspected original evidence | Negative-equivalence boundary |
| --- | --- | --- |
| `S06-R007` — Physical constituent | PARTIAL; `SOSA-C239-G2-6A-RULE-13.2.1-1`, `SOSA-C239-G2-6A-RULE-13.2.4.4-1` | Logical modules do not equal one PIC each or one universal chassis |
| `S06-R008` — Connected external equipment | RELATED; `SOSA-C239-G2-6A-RULE-13.2.4.1-1`, `SOSA-C239-G2-6A-RULE-13.2.4.1-2` | Backplane routing does not prove an external cable or installed peripheral |
| `S06-R009` — Hosting platform / station context | RELATED; `SOSA-C239-G2-6A-RULE-13.2.4.2-9`, `SOSA-C239-G2-6A-ANALYTICAL_CONTEXT-004` | Slot fit is not an observed hosting platform or surveyed station |
| `ISA-E-COMPONENT-CATEGORY` — Human-facing component category | PARTIAL; `SOSA-C239-G2-6A-RULE-13.2.1-1`, `SOSA-C239-G2-6A-RULE-13.2.6-1` | Not ISA ComponentCategory enumeration or universal hierarchy |
| `ISA-E-POWER-SOURCE` — Power-source classification | NO_ESTABLISHED; `SOSA-C239-G2-6A-ANALYTICAL_CONTEXT-003`, `SOSA-C239-G2-6A-RULE-13.2.3.1-1` | No inferred solar, grid, external generator or installed battery |
| `ISA-C-052` — Consumed DC current | RELATED; `SOSA-C239-G2-6A-RULE-13.2.3.2-2`, `SOSA-C239-G2-6A-RULE-13.2.3.2-3` | Max electrical current limit is not reported consumed DC current |
| `ISA-C-054` — Load-side DC voltage | RELATED; `SOSA-C239-G2-6A-RULE-13.2.6.2-1`, `SOSA-C239-G2-6A-RULE-13.2.6.2-2` | Not measured load-side DC voltage |
| `ISA-C-091` — Reported condition of power to the component | RELATED; `SOSA-C239-G2-6A-RULE-13.2.6.6-4`, `SOSA-C239-G2-6A-TABLE-13.2.6.5-1` | Not active ISA power-condition telemetry |
| `ISA-A-TIME-BASIS` — Component time basis and synchronization | RELATED; `SOSA-C239-G2-6A-RULE-13.2.6.6-1`, `SOSA-C239-G2-6A-RULE-13.2.6.6-2` | No absolute UTC event time or proven synchronized installed clock |
| `ISA-K-COMMAND-DECL` — Declared command interface | NO_ESTABLISHED; `SOSA-C239-G2-6A-RULE-13.2.8.4-1`, `SOSA-C239-G2-6A-ANALYTICAL_CONTEXT-010` | Not normal operational command or CSAPI ControlStream |
| `S06-R021` — Source-qualified assertion (proposed DIM) | RELATED; `SOSA-C239-G2-6A-COV_FIELD-001`, `SOSA-C239-G2-6A-COV_FIELD-009` | No original case CoV inspected or manufacturer-authenticated project assertion |
| `CASE-H04` — REVIEW HOLD — power / state | RELATED; `SOSA-C239-G2-6A-RULE-13.2.3.1-5`, `SOSA-C239-G2-6A-TABLE-13.2.6.5-1` | No observed device power state or battery supply |

No donor comparison alone approves DIM class, attribute, cardinality, hierarchy, Profile SHALL, actual equipment runtime claim or independent interoperability.

## 4. Exact unresolved source holds

- **SOSA-G2-6A-H01 — UNREAD_EXTERNAL_VITA:** ANSI/VITA 65.0/46.0/46.30/.31/48.2/.4/.8/62.0/66.x/67.x and companion originals referenced by C239 but not read in this packet
- **SOSA-G2-6A-H02 — UNVERIFIED_FIGURE_PIXEL_GEOMETRY:** Original hardware diagrams/cross-sectional/overlays read at caption and labels, not visually verified pixel geometry
- **SOSA-G2-6A-H03 — VOLTAGE_INPUT_NOT_BATTERY:** VBAT/ALT_VBAT pins and electrical limits do not prove a battery, source chemistry, current charge, current power path or manufacturer installation
- **SOSA-G2-6A-H04 — SHORT_VS_FULL_3U:** 100mm short 3U 1.2-in pitch and standard 160mm 1-in pitch differ; no universal intermateability or chassis
- **SOSA-G2-6A-H05 — COOLING_DEPENDENT:** Conduction, airflow and liquid cooling use different slot profiles; adapted installations conditional, not necessarily plug-compatible
- **SOSA-G2-6A-H06 — POWER_SUPPLY_CARD_SCOPE:** PSC has distinct input, output, return/sense/control, keying and management pins; table is electrical design, not field telemetry
- **SOSA-G2-6A-H07 — BACKPLANE_VS_EXTERNAL_CABLE:** Primary PIC signals traverse backplane except enumerated front-panel exceptions, not a general external sensor cable or DIM child graph
- **SOSA-G2-6A-H08 — MCP_NONOPERATIONAL:** Maintenance Console Port is service/debug UART, not normal sensing or CSAPI operational command channel
- **SOSA-G2-6A-H09 — COV_SOURCE_DOCUMENT_ONLY:** Certificate of Volatility describes vendor memories and protection, and CoV original remains absent for four cases
- **SOSA-G2-6A-H10 — COV_EMBEDDED_NVM:** Original §13.2.10 says embedded undocumented NVM may escape CoV inventory; cannot certify full memory sanitization
- **SOSA-G2-6A-H11 — SOURCE_TYPOS:** 13.2.4.2-9 repeats Table13.2.4.2-1; ALT_VBATT vs ALT_VBAT, 100m caption, –DC/CAN vs –DC/ACN inconsistent originals preserved
- **SOSA-G2-6A-H12 — RESTRICTED_APPENDIX_C:** Security overlay rules referenced in restricted Appendix C, not audited; no inferred high assurance certification
- **SOSA-G2-6A-H13 — SCOPE_STOP:** Only §13.2.10 CoV continuation on PDF230 source-read; next §13.2.11 not audited
- **SOSA-G2-6A-H14 — NO_MODEL_RELEASE:** No new domain name, hardware root, DIM class/cardinality, Profile SHALL, vendor conformance or device execution adopted

## 5. Mandatory saved-workbook L23 exit and STOP boundary

Current JSON, BOTH CSV and BOTH Markdown comparison tables contain all **39** original-source-qualified SOSA cells. **Intermediate publication state:** the SAME 26-sheet canonical workbook is the verified **G2-5** snapshot SHA256 `e793461d393bee743b8cf3464f2f6274244a0cbc4cb630a42b772f676615188a`; it is **39 newly qualified SOSA column-I cells behind** until the SAME-packet workbook publisher and independent saved 346×15 source-cell check succeed. Do **NOT** claim G2-6A complete or proceed to the next source packet while that lag remains; no owner-approved deferral exists.

After verified Excel closeout, **only a separate owner “Proceed”** may start **SOSA-G2-6B**, the next bounded original §13.2.11 hardware PICP evidence packet, not automatically all of remaining Chapter13, SAPIENT, DIM/Profile adoption or UI/deployment.

