# SOSA-G2-1 — C239 §§6.2.3–6.2.5 original-inline-source review and master correspondence

**Bounded result: G2-1 COMPLETE; full The Open Group SOSA donor review remains OPEN.** Original C239 Edition 1.1 (2023), `c239_5.pdf`, project Library ID `file_00000000af4081f58c4bac329f85c58f`, was read at PDF pp.73–90 (printed pp.47–64), continuing to the very end of §6.2.5.3. The referenced GENERAL PROFILE clauses (§6.2.1, PDF70–71) and native file names in Appendix B (PDF390–391) were checked for context, not claimed as complete source audits. Original C239 DSDM/IDL and six referenced OpenAPI files remain unread.

## Original entries, support grades and explicit Rules

| C239 original table / subclause | Native table entries | V1.0 | Future | Explicit Rules |
| --- | ---: | ---: | ---: | ---: |
| §6.2.4.1 System Manager functions (PDF74–82) | 98 | 60 | 38 | — |
| §6.2.4.2 System Manager interactions (PDF82–85) | 57 | 36 | 21 | — |
| §6.2.4.3 System Manager bindings (PDF86) | — | — | — | 4 |
| §6.2.5.1 Generic-module functions (PDF87–89) | 26 | 22 | 4 | — |
| §6.2.5.2 Generic-module interactions (PDF89–90) | 14 | 11 | 3 | — |
| §6.2.5.3 Generic-module bindings (PDF90) | — | — | — | 2 |
| **Totals** | **195** | **129** | **66** | **6** |

[The complete 201-original-item ledger](SOSA_G2_1_Original_Item_Inventory_09NOV2026.json) retains stable item IDs, table, page, native names, support labels, interaction input/output labels and explicit D/T conformance-method Rule IDs. These are 201 **table items and Rules**, not 201 distinct DIM concepts or independently inspected API endpoints. §6.2.3 explicitly defines `V1.0` as endpoints defined by this version and `Future` as endpoints planned for later; neither support label verifies the inaccessible native API's paths, types, cardinalities, behavior or an actual installed System.

The System Manager gives outside management functionality and supports the Task Manager; its four conditional `shall` Rules distinguish a System Manager implemented with operating-system/transport APIs from an alternative where interaction infrastructure takes technology-binding responsibility. The generic-module definitions apply by default **only where more specialized interaction definitions do not apply**, explicitly excluding the System Manager. Health, Fault, State, Mode, Configuration, logging, BIT, firmware, resource and security functions have distinct names, standing and return objects; do not merge them into generic command or status fields merely because labels look similar.

## Source-specific holds and negative equivalence

**SOSA-G2-1-Q01 — internal source citation conflict:** System Manager Rules **6.2.4.3-2 and -4** literally point to §B.3. Original Appendix **B.2** lists `System Manager-SysMan-API.json`; **B.3** lists `Module-SysMan-API.json` for the generic module (PDF390, printed364). Do not silently change the Rule citation or claim which file governs without native model/source resolution.

**SOSA-G2-1-Q02 — native OpenAPI unread:** Neither B.2 nor B.3 file contents was available for inspection. The published interaction tables list request-response names/objects but do not independently establish final endpoint URI templates, body schema, HTTP behavior, error status or runtime conformance.

**SOSA-G2-1-Q03 — native function/interaction correspondence source absent:** Both §§6.2.4.2 and 6.2.5.2 say their mapping to the function tables was not printed and is tracked in source material; the narrative refers back to its interaction table. Do not invent one-to-one source join or infer it from a name.

**Operations are NOT operational proof:** `getSensorMode/getMode` read ComponentMode, while `getSensorState/getState` read ComponentState. Listed sensor/component state-update functions are Future, whereas mode updates, selected restart/shutdown, zeroize/sanitize and BIT requests are V1.0. Many system-security monitoring/attestation and inventory functions are Future. None of these C239 table descriptions establishes that any of the four documentary equipment cases supports, accepts or executed such commands.

## Progressive canonical crosswalk update

Exactly **12 existing donor cells** in the *The Open Group SOSA* column were source-qualified without inserting rows, changing other standards/case cells or accepting DIM architecture. Existing SOSA-D text was retained where present. The [master JSON](Master_Donor_Concept_to_DIM_Crosswalk.json), [CSV](Master_Donor_Concept_to_DIM_Crosswalk.csv) and [GitHub-readable comparison](Master_Donor_Concept_to_DIM_Crosswalk.md) contain stable source item IDs, relation/caveat and explicit non-adoption for each row.

| Existing master row | Source relation | Original source support | Critical limit |
| --- | --- | --- | --- |
| ISA-A-SERVICE-ROLE — Service role and required command support | RELATED | SOSA-C239-G2-1-SMR-01, SOSA-C239-G2-1-SMR-02, SOSA-C239-G2-1-SMR-03 and more | C239 system management service roles are not automatically ISA Controller network roles or new DIM classes. |
| ISA-A-BASELINE-CAPABILITIES — Required and recommended capability support | RELATED | SOSA-C239-G2-1-SMF-001, SOSA-C239-G2-1-SMF-081, SOSA-C239-G2-1-GMF-021 | C239 support grades identify edition endpoints, not ISA core/extension requirements or actual equipment support. |
| ISA-K-COMMAND-DECL — Declared command interface | RELATED | SOSA-C239-G2-1-SMI-028, SOSA-C239-G2-1-GMI-009, SOSA-C239-G2-1-GMI-007 | Interface operation names do not establish ISA command schema or CSAPI command endpoints. |
| S06-R018 — Source-reported operating mode | PARTIAL | SOSA-C239-G2-1-SMI-031, SOSA-C239-G2-1-SMI-032, SOSA-C239-G2-1-GMI-008 | C239 interface return type is not evidence that an installed source system reports that mode. |
| S06-R019 — Issued control request | RELATED | SOSA-C239-G2-1-SMI-033, SOSA-C239-G2-1-SMI-029 | Do not equate mission Task Manager, in-band management request and observed physical control. |
| ISA-T-STATUS — Component property-value report | RELATED | SOSA-C239-G2-1-SMI-001, SOSA-C239-G2-1-GMI-005, SOSA-C239-G2-1-GMI-008 | Health, State and Mode are different SOSA native typed representations; no ISA Status message equivalence. |
| ISA-C-046 — Latest built-in-test reported result | RELATED | SOSA-C239-G2-1-SMI-015, SOSA-C239-G2-1-SMI-016 | No native latest-value temporal guarantee, device observation or ISA result-schema equivalence. |
| ISA-C-235 — Requested component diagnostic procedures | RELATED | SOSA-C239-G2-1-SMI-013, SOSA-C239-G2-1-SMI-014 | Request interface is not evidence of actual sensor BIT execution or ISA diagnostic procedure. |
| ISA-C-244 — Requested component shutdown sequence | RELATED | SOSA-C239-G2-1-SMI-030, SOSA-C239-G2-1-GMI-007 | Request-response support does not prove successful physical shutdown or universal deployed availability. |
| ISA-C-232 — Requested removal of security-relevant application data | RELATED | SOSA-C239-G2-1-SMI-036, SOSA-C239-G2-1-SMI-038, SOSA-C239-G2-1-GMI-010 and more | Security operations and their payloads do not prove source-specific ISA application-data wipe or actual execution. |
| ISA-C-211 — Requested current component configuration message | RELATED | SOSA-C239-G2-1-SMI-046, SOSA-C239-G2-1-SMI-047, SOSA-C239-G2-1-GMI-012 | Sensor aggregate, System Manager and Generic Module configurations are distinct source contexts. |
| ISA-K-MUTABILITY — Declared property mutability | RELATED | SOSA-C239-G2-1-SMI-046, SOSA-C239-G2-1-SMI-048, SOSA-C239-G2-1-GMI-012 and more | Future management update endpoints do not establish property-level ISA access semantics or mutable actual equipment. |

G2-1 has **not** changed the 329 existing DIM/review topics, 15-column arrangement, original 58 donor records, 73 four-case facts, prior ISA evidence or source holds. The new inventory records additional native source entries, not 201 master fields or 201 Profile requirements.

## Source coverage and Excel standing

The original SOSA-G1 census recorded 192 C239 TOC headings: 65 with selected passages sampled, 126 without substantive review and one restricted Appendix C. This packet newly audits two previously UNREAD headings (§§6.2.3 and 6.2.4) and deepens the already sampled §6.2.5: heading-level at-least-sampled becomes **67**, remaining UNREAD **124**, inaccessible **one**. All nine in-body sections/subsections in scope have their entire *C239 inline* tables/Rules read, but no C239 section is certified native OpenAPI/DSDM dependent completeness. Historical G1 section statuses stay a dated baseline, not retroactively overwritten.

The **26-sheet canonical editable XLSX is still the pre-G2-1 SOSA-D checkpoint** (SHA-256 `531451e4b43b0502e9e90b62972a7398be048ceb3987eb24ef4963e3f0fb1fba`, earlier 346×15 parity PASS). The source-advanced JSON/CSV/Markdown differ from its saved cells in **exactly 12 The Open Group SOSA cells**; current Excel parity is **NOT** claimed. Refresh and inspect the same workbook at a subsequent substantive checkpoint, retaining all 26 sheets and all legacy evidence.

**Stop:** G2-1 is complete **at its bounded C239 inline text review scope**, The Open Group SOSA remains the active donor, and original Step18 SAPIENT remains BLOCKED. **ONE next owner-authorized “Proceed”: SOSA-G2-2 only — original C239 §§6.2.6–6.2.9 Security Services, Chassis Manager, PIC and PIC with Software RTE in-band interfaces.**
