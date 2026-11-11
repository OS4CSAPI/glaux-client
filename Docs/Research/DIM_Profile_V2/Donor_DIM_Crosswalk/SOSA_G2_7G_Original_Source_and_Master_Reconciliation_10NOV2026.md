# SOSA-G2-7G — original C239 §13.3.8 analog/optical backplane apertures and source-to-master reconciliation

**Verified mandatory L23 SAME 26-sheet Excel packet exit:** Exactly **18** G2-7G source-qualified The Open Group SOSA donor-column cells are current in canonical JSON, BOTH CSV, BOTH readable Markdown and the **SAME original editable 26-sheet Excel**. All **346×15 actual saved cells match**, 22 historical worksheet XMLs untouched, original 329 information rows/15 columns and prior 58 donor/73 equipment-case/ISA480 outcomes with six original questions preserved, **Excel lag ZERO**. [Saved workbook validation](SOSA_G2_7G_Workbook_Validation_10NOV2026.json) · [source-cell preview](SOSA_G2_7G_Workbook_Preview_10NOV2026.png) · [publisher PASS](https://github.com/OS4CSAPI/glaux-client/actions/runs/42950283017) · [independent original-source/saved-XLSX verifier PASS](https://github.com/OS4CSAPI/glaux-client/actions/runs/42950474352); saved workbook SHA256 `adc2fde9ce66a0a64bbd4cb01964a24aab28a5907fae48c7263975496e8eb444`. Source remains PARTIAL for original pinout figure pixel geometry, ANSI/VITA and eight native C239 companions, unresolved SMPM14 table pointer conflict and 30 unread registered headings. No adopted DIM/CSAPI Profile or real installed PIC conformance; **SOSA remains OPEN and SAPIENT blocked**. **STOP — G2-7H original §13.4 requires a separate owner Proceed.**

**Original source:** The Open Group SOSA Consortium, *Technical Standard for SOSA Reference Architecture*, Edition 1.1 (2023), C239, project Library original `c239_5.pdf`, **§13.3.8 including §§13.3.8.1–13.3.8.2, original PDF266–268 (printed240–242)**; **STOP BEFORE §13.4 SOSA Plug-In Cards Using VNX**. [Stable source-item ledger](SOSA_G2_7G_Original_Source_Item_Coverage_10NOV2026.json) accounts for **30 original source-native entries (13 source contexts, two numbered Rules, three figures, ten extracted SMPM-10 pin-label rows, one Recommendation and one Observation)** plus **six analyst contexts**, with **19 exact holds**. This is a direct original INLINE-TEXT, figure-caption and extracted pin-label review; repeated attempts to retrieve original high-resolution page images failed, so **pin-contact positions, all SMPM-14 mapping geometry and referenced ANSI/VITA pinout tables are NOT independently visually verified**. It is source-PARTIAL at original figure and companion level.

## 1. Native physical scope, intent and current-versus-future limits

Original §13.3.8 distinguishes **ANSI/VITA 67.3 coaxial** backplane apertures from **VITA 66.5 fiber-optical** apertures in source VITA 65 Slot Profiles. The source says previously defined slot profiles describe the *physical aperture interface*, whereas §13.3.8 adds recommended uses of individual signal interfaces to reduce unnecessary recabling when capabilities are replaced. This purpose is a physical design/interchangeability rationale—not a blanket mandatory common DIM chassis, an observed installed cable, an API resource field or proof of existing multi-vendor interoperability.

**§13.3.8.1 explicitly restricts then-current regulations to coaxial pin designations for the named 3U Radial Clock slot profile** `SLT3x-TIM-2S1U22S1U2U1H-14.9.2-1`. An original Note says broader ANSI/VITA 67.3/66.5 slot-profile definitions are expected in a future edition; future text is NOT an Edition1.1 present requirement. The source defines *analog I/O* here to cover **radio-frequency (RF) and intermediate-frequency (IF)** signals, not just CSAPI Observations or an actual RF transmission.

## 2. SMPM-10 radial clock source Rule, figure and ten printed pin labels

**Rule 13.3.8.1-1** uses **SHALL**, requiring the SMPM-10 coax pin designations to follow **ANSI/VITA 65.1 Table 6.4.5.6.3-1**, portrayed in **Figure 13.3.8.1-1**. No `Conformance Methodology` code is printed adjacent to this Rule in the available original text; do not infer method T by analogy to the later SMPM-14 rule. The original external ANSI/VITA standard has not been read, and figure-pixel verification remains on hold.

The following **ten signal/pin labels were extracted directly from the original embedded Figure13.3.8.1-1 text**, but their exact graphical connector orientation and contact geometry are **not pixel-verified**:

| Pin | Printed direction | Source label | Related C239 context |
| --- | --- | --- | --- |
| A1 | OUT | `EXT_REF_CLK_Out` | §5.14.1 |
| A2 | OUT | `EXT_AUX_CLK_Out` | §5.14.2 |
| A3 | X | `RSVD` | Reserved |
| B1 | IN | `EXT_AUX_CLK_In` | §5.14.2 |
| B2 | IN | `EXT_REF_CLK_In` | §5.14.1 |
| B3 | X | `RSVD` | Reserved |
| B4 | X | `RSVD` | Reserved |
| C1 | X | `RSVD` | Reserved |
| C2 | IN | `GPS_Ant2_In` | §5.14.3 |
| C3 | IN | `GPS_Ant1_In` | §5.14.3 |

These printed directions and reference-clock/auxiliary-clock/GPS antenna signal names describe a particular physical coax allocation; they **do not establish actual time synchronization accuracy, GPS position measurement, antenna connection, active source power or installed device wiring**.

## 3. SMPM-14: binding Rule, different Recommendation and scoped Observation

Original §13.3.8.2 refers to **Figure13.3.8.2-1** for SMPM-14 ANSI/VITA67.3 aperture pin definitions and **Figure13.3.8.2-2** for contact designations viewed from **the front of the backplane**. The source **Figure13.3.8.2-1 caption refers to ANSI/VITA 65.1 Table `6.5.4.6.4-1` while Rule13.3.8.2-2 points to Table `6.4.5.6.4-1`**. Preserve this discrepancy exactly; without original ANSI/VITA table content and figure pixels, do NOT decide which pointer is correct. The directly available original clause prints **Rule13.3.8.2-2** but no Rule13.3.8.2-1; do not invent a missing Rule merely to normalize numbering.

**Rule 13.3.8.2-2 (SHALL; printed Conformance Methodology `(T)`)** requires a SOSA PIC with an ANSI/VITA67.3 SMPM-14 coax pin designation to follow the cited ANSI/VITA table as portrayed in Figure13.3.8.2-2. **Recommendation 13.3.8.2-1 (SHOULD; printed `(T)`)** separately recommends associating physical coax pins with internal channels following that figure; it is not a Rule or mandatory all-sensors requirement. No test (T) was performed on any real hardware.

**Observation 13.3.8.2-1** describes the first two analog-channel mappings explicitly: with one signal it uses **B1**; with two, Channel 1 uses **B1** and Channel 2 **B4**. The Observation mentions configurations for eight analog I/O contacts and interoperability of vendor cards plus chassis I/O association, but **it does not give a pixel-verified full eight-contact map** in the accessible text. An AMPS RF pinout protocol field indicates which physical pinout variant is used; this is **not** an observed analog value, a live RF receiver, a CSAPI DataStream field or evidence a source case has an SMPM-14 connector.

## 4. Qualified donor correspondence and master preservation

Only the **The Open Group SOSA donor column I** of the one horizontal source master can receive qualified source relationships. The original material can inform **physical constituent**, **physical interface or external equipment connection**, **hosting/chassis interconnection context**, **time/clock hardware context**, **design-time protocol/port declaration**, **source-grade Rule/Recommendation/Observation distinctions**, and **positive/negative equipment-case holds**. Use stable original source IDs, exact/partial/related/no-established meaning and negative equivalence; do **not** populate W3C SOSA/SSN, change case facts, invent full SMPM-14 connector assignments, or adopt a final DIM type because the source names a physical card/chassis.

The approved master must preserve **329 information rows ×15 columns, 15 topic dividers, four empirical source-case columns left, the grouped Open Geospatial Consortium (OGC) foundation and proposed DIM far right**. Preserve earlier 58 donor source facts, 73 empirical case facts, 480 Integrated Sensor Architecture (ISA) outcomes/six unresolved source questions, all prior The Open Group SOSA source data and **the earlier 19/17/16/17 precise G2-7C/D/E/F holds**. Incorporating donor comparisons is not accepting any DIM class, hardware chassis/cardinality, Connected Systems API (CSAPI) Profile SHALL or physical-device conformance.

## 5. Exact holds, source coverage and next owner boundary

The [19 local G2-7G holds](SOSA_G2_7G_Original_Source_Item_Coverage_10NOV2026.json) isolate unavailable source pixels, unopened original ANSI/VITA65.1/67.3/66.5, eight C239 native schema/API files, the SMPM-14 conflicting figure-vs-Rule table reference, missing inline Rule13.3.8.2-1, Rule13.3.8.1-1 with **no printed conformance code**, recommendation versus binding Rule, incomplete contact geometry, current-vs-future scope and lack of real equipment/case proof. One previously unread **registered TOC heading §13.3.8** is now original inline-reviewed, with both nested subsections accounted separately; cumulative C239 heading status **161/192 at least sampled/inline-reviewed, 30 substantively unread and one restricted**. This is **not** an exhaustive source/figure/companion audit.

**Mandatory existing L23 exit:** Any qualified source cells must appear in canonical JSON, BOTH CSV mirrors, BOTH GitHub-readable comparisons and the SAME original editable 26-sheet workbook before another packet. Verify **all 346×15 actual saved cells**, preservation of all historical worksheets, GitHub commit/readback and independent CI. No new source claims or adopted DIM/Profile conformance are proven by successful workbook integrity tests.

**STOP after G2-7G source-to-SAME Excel saved-cell verification.** Only a **separate owner “Proceed”** may begin **G2-7H, original §13.4 SOSA Plug-In Cards Using VNX**, sized by original source complexity. The Open Group SOSA donor remains **OPEN**, original crosswalk Step18 SAPIENT **BLOCKED**.
