# SOSA-G1 — comprehensive donor-source and C239 section coverage baseline

**9 November 2026 · SOSA-G1 SOURCE CENSUS COMPLETE; comprehensive original The Open Group SOSA donor assessment remains INCOMPLETE.** This delivery implements G1 from [the owner-corrected SOSA coverage plan](PLAN_SOSA_Source_Coverage_Correction_v0.1_09NOV2026.md). The complete, machine-checkable [12-artifact source and access register](SOSA_G1_Source_Artifact_Census_09NOV2026.json) and [192-heading C239 section coverage register](SOSA_G1_C239_Section_Coverage_09NOV2026.json) are the new evidence. Earlier [SOSA-A](Step17_SOSA_A_C239_Architecture_Roles_Review_09NOV2026.md), [SOSA-B](Step17_SOSA_B_C239_Management_Operational_Review_09NOV2026.md), [SOSA-C](Step17_SOSA_C_C239_DSDM_Interfaces_Edition_Review_09NOV2026.md) and [SOSA-D](Step17_SOSA_D_Crosswalk_Integration_Closeout_09NOV2026.md) remain verified **intermediate** research, not a complete original-source census. The original Step18 SAPIENT donor review remains **blocked**.

## 1. Source corpus and actual access

The unchanged [182-artifact accountability register](../Donor_Alignment/03_Source_Accountability_Register.csv) contains **12 The Open Group SOSA lineage records**, IDs **47–58**: C212 Edition1.0 (2021); an Edition1.0 DSDM (2022); C239 Edition1.1 (2023); its listed IDL and six management OpenAPI companions; and S251 2025 Edition2.0 Snapshot3 plus its ZIP bundle. This is one donor lineage with 12 source artifacts, **not twelve independent standards or model votes**.

**One original readable primary text** was available: the **403-page C239 Edition1.1 PDF** `c239_5.pdf`, project Library file `file_00000000af4081f58c4bac329f85c58f`. Earlier A/B/C research read selected native clauses and pictures. The original contents PDF pp.3–7 and G1 representative physical/operational pages were read successfully before subsequent attempts to re-access the Project Library PDF returned source-service errors. Raw source bytes for attachments were not materializable in the available runtime. We therefore **cannot attest C239 PDF embedded attachment absence or content hashes**.

The original C239 **Appendix B.1** references a **separately identified C239-native `SOSA_TechStd_v1_DSDM`**, but the 12-item register only registers a different *Edition1.0 DSDM* and the C239 IDL; edition/byte identity has **not** been established. Along with `SOSA_TechStd_v1_DSDM_IDL` and six C239 Appendix B.2–B.7 SysMan OpenAPI JSONs, that leaves **eight separately named native C239 model/API files unread**, not merely unverified by summary prose. All are explicitly listed in the source-access ledger, including the unregistered C239 DSDM as provisional dependency `SOSA-G1-X01`.

The original C239 **Appendix C**, printed p.366 / PDF p.392, references *Security Attributes SOSA Security Module Overlay for Specialty Signals* at `https://restricted.vdl.afrl.af.mil/xythoswfs/webview/_xy-7055996_1`. This is a separate **restricted VDL security overlay** `SOSA-G1-X02`, not inline Appendix C schema content or a thirteenth independent standard. It remains **INACCESSIBLE** to this review; authorized program access and relevant distribution rights must be considered before retrieval. It is source-relevant to security posture and authorization, but we cannot call it normatively reviewed.

The Open Group publication endpoints for `c239` and `s251` returned inaccessible responses in the browsing environment. That does not establish that the publisher does not distribute these materials. Contemporary [S251 Snapshot3 release coverage](https://militaryembedded.com/radar-ew/sensors/sosa-consortium-releases-the-technical-standard-for-sosa-reference-architecture-edition-20-snapshot-3) and [U.S. DoD SOSA-ED.2.0-SNAP3 adoption metadata](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=287032) independently confirm edition/adoption identity **without supplying the native S251 text**. The publicly viewable [AFRL file named Edition2.0](https://www.vdl.afrl.af.mil/programs/arsenl/files/SOSA%20Technical%20Standard%20Edition%202.0.pdf) is **S221 August2022 Snapshot1**, confirmed from its original cover and document-number page, **NOT S251 June2025 Snapshot3**. No snapshot edition is silently mapped into the C239 donor column.

## 2. C239 original table-of-contents coverage: quantified without overstating completeness

The existing primary PDF's original contents (PDF pp.3–7) was indexed into **192 stable chapter/section/appendix headings**, including **41 parent headings and 151 leaf headings**. All 192 IDs are unique. Printed page starts and corresponding PDF page numbers are recorded in the machine-readable section ledger, together with a review status, reason, priority family, and existing original-source locator IDs.

| G1 status on the 192 TOC headings | Count | What it actually establishes |
| --- | ---: | --- |
| **SOURCE_READ** | **65** | One or more selected original passages or pointers in that heading were previously examined by SOSA-A/B/C. **It does not mean the entire section or all native Rules were audited.** |
| **UNREAD** | **126** | The heading is known from the original TOC (some had G1 page spotchecks), but a substantive complete original clause review is not established. |
| **INACCESSIBLE** | **1** | Appendix C's restricted-security-overlay content is unread although its in-PDF reference pointer was read. |
| **Full-section exhaustive source-coverage certifications** | **0** | Conservative evidence standing: no section is claimed complete across every applicable native Rule/Recommendation/Observation and companion dependency merely from sampled paragraphs. |

**All 76 previously committed individual A/B/C source-native record IDs** were reconciled with this original TOC, retaining their original locators; they reference **60 distinct TOC headings**. Those 60 include overlapping sections and subheadings. The earlier 76 source findings are **not** 76 audited chapters, and the 65 sampled-heading count is not a percentage of original requirements addressed. These are navigation/review-depth measurements, not coverage-by-requirement percentages.

### Where the largest risks are

| C239 source family | TOC entries | Currently evidenced position and risk |
| --- | ---: | --- |
| §§1–3: context, definitions, quality attributes, architecture principles | 19 | Only selected source normativity definitions were earlier reviewed. Whole-system quality attributes and engineering principles deserve applicability screening, not assumed irrelevance |
| §§4–5: physical sensor, host, function taxonomy, system and data context | 23 | Useful selected evidence already included, but airworthiness, security and interconnect subsections remain insufficiently traced |
| **§6: System Management** | **23** | Selected rules on notifications and states read; **6.2.3–6.2.9**, out-of-band management and many native interface schemas require systematic coverage |
| §§7–11: tasking, RF/signal processing, storage, reporting | 27 | Preliminary/future definitions found, but scope and original detailed interaction and Rule inventories are not complete |
| **§12: Supporting system operation** | **23** | Security, audit, key/authorization functions, host interface, navigation/time, calibration and power require a complete relevant-clause check |
| **§13: Hardware Element** | **40** | **Printed pp.182–334 (~153 pages)** of physical hardware and interfaces. Previous targeted sampling (e.g. power distribution, VNX, external battery connector) is not a systematic evidence inventory |
| §§14–15: run-time and interaction interfaces | 27 | Several selected rules reviewed; full profile, interaction, QoS and implementation constraints remain incompletely inventoried |
| Appendices A/B/C | 10 | Original glossary and Appendix B file **pointers** inspected; eight native companions and restricted Appendix C overlay **not read** |

**Important physical-equipment screening:** C239 Chapter13 contains explicit original Power Supply Card, Energy Storage Card, utility power distribution, connector and external battery interface discussions. Those are potentially relevant to the DIM's power/equipment and physical-interface work even when pin assignment specifics may ultimately remain implementation detail. **No Chapter13 subsection is declared irrelevant solely because it is an electrical or mechanical clause.** G1 representative spotchecks also found some VNX fields marked `TBD`; these cannot be promoted to edition-wide normative DIM requirements.

## 3. Systematic reconciliation method and source limitation controls

The new [section ledger](SOSA_G1_C239_Section_Coverage_09NOV2026.json) records original heading IDs, start pages, major source-content family, priority, whether earlier source records refer to that heading, and the **exact 76 earlier record-to-TOC associations**. **Every record retains its native locator**, but the automatic association to a contents heading is only a navigation aid: it **cannot certify all subclauses or attachments have been inspected**. Missing headings remain flagged as unread rather than silently checked off.

In the next substantive source review, original statements must be inventoried as *Rule, Recommendation, Permission, Observation, source definition, example, future placeholder,* or *unresolved*. Each potential DIM relation must have a native locator, source-standing grade, evidence/negative-equivalence limit, and explicit non-adoption. **Update the existing 329-row master JSON, both CSV mirrors and GitHub-readable tables progressively** when a source finding changes comparison meaning. Use the same canonical 26-sheet workbook at substantive checkpoints; if it lags, label the lag plainly. G1 itself only classifies **coverage**, so it does **not** create unsupported new semantic mappings or force an Excel rebuild. The **existing 15-column JSON/CSV/Markdown/XLSX content remains synchronized**, aside from adding G1 source-census metadata.

## 4. Work remaining: bounded review families, not a predetermined finish line

Original relevant C239 source review is expected to require **multiple controlled source packets**. These are an evidence-driven grouping proposal, **not an assertion that eight future prompts will complete the donor**:

1. **G2-1 (next single authorized packet):** C239 §§**6.2.3–6.2.5**, System Manager and generic Module in-band definitions, printed pp.47–63. Inventory exact original functions, representations, message/RFC/OpenAPI dependencies and requirement standing. Compare with existing system/management/control rows, preserve native-access caveats, and progressively update the canonical master/mirrors if source-qualified changes arise.
2. **G2-2:** §§6.2.6–6.2.9, Security Services, Chassis Manager, PIC and PIC/RTE in-band interfaces (printed pp.64–92).
3. **G2-3:** §§6.3–6.5, out-of-band hardware management, complete state/security transitions and the difference between controlled and merely reported state.
4. **G2-4:** §§1–5 and 7–11 outstanding architectural principles, sensor/task/observation and mission/reporting source clauses.
5. **G2-5:** §12 full supporting-operation source (security/audit/authorization, calibration, navigation/time, host/power), not just top-level descriptive summaries.
6. **G2-6:** §13 physical PIC, power/energy-storage, coolant, equipment/assembly and interface family. Split by exact original Rule density if required; do not turn every pinout into a top-level DIM field.
7. **G2-7:** §§14–15 remaining runtime, protocols, QoS and data/interaction/metadata relationships.
8. **G3/G4/G5:** actual native model/API sources where accessible, cross-donor master reconciliation and workbook checkpoints, independent source-coverage review and explicit owner completion disposition.

A defensible prompt-count forecast is **not yet available**: 126 headings remain without verified substantive source review, and native-companion access may change the work materially. The review packets above are candidate groupings, not hard delivery-count ceilings. Reestimate after the first two actual G2 source packets, when full Rule/element density and original-source access have been observed. This avoids prematurely repeating the four-iteration SOSA closure mistake.

**Completion standard:** A donor cannot be called equivalent to the ISA coverage correction until the applicable C239 and companion sources have evidence-graded, justified coverage, or the owner explicitly accepts a *bounded source-limited partial result* with transparent exclusions. Passing a 26-sheet workbook integrity check is **not** a substitute for original-source completeness or independent sensor-system conformance.

## 5. G1 exact handoff

**SOSA-G1: COMPLETE AT SOURCE-CENSUS / TOC CLASSIFICATION DEPTH. SOSA full donor assessment: OPEN. Original Step18 SAPIENT: BLOCKED.** Preserve all prior original source and case evidence. **Next user “Proceed”: G2-1 only — systematic C239 §§6.2.3–6.2.5 in-band System Manager/Generic Module original-source audit, source-native concept-to-master comparison, and progressive canonical master updates as justified.** Do not execute G2-2, G3, a new source edition, or SAPIENT automatically.
