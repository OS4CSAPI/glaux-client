# SOSA-G2-7D — original C239 §13.3.5 Switch AMPS source and qualified master correspondence (10 November 2026)

**Original:** The Open Group SOSA Consortium, *Technical Standard for SOSA Reference Architecture*, Edition 1.1, C239 (2023), original project Library `c239_5.pdf`, §13.3.5, PDF pp.263–264 (printed pp.237–238). This bounded original-source packet ends **BEFORE §13.3.6** and does not claim ANSI/VITA companion access or as-installed hardware conformance. [Stable source-item ledger](SOSA_G2_7D_Original_Source_Item_Coverage_10NOV2026.json) records **38 source-native evidence entries plus 6 analytical contexts**, including **17 local holds**. The dense **Table 13.3.5-1 pixel/column legal-port alignment has not been independently visually verified**; source audit is **PARTIAL** at that granularity.

## 1. Original source scope, named families and source status

C239 §13.3.5 names **four distinct Switch Plug-In Card Profile (PICP) families**, not four universal sensor-system kinds. The source has three **3U** options—**Data Plane (DP) Switch**, VITA slot `14.4.14` / Alternate Naming Structure (ANS) `16.4.15-1`; **Expansion Plane (EP) Switch**, slot `14.4.15` / ANS `16.4.16-1`; **DP Switch/V66**, slot `14.8.7` / ANS `16.8.7-1`—and one **6U DP Switch**, slot `10.8.1` / ANS `12.8.1-1`. These are different physical switching/port architectures, not equivalent to a software switching module, whole Sensor, generic chassis, or source case installed component.

Original Table 13.3.5-1 displays **16 depth/cooling/pitch protocol rows** across the four named families. The table prints **three named dash options** (`-0-`, `-4-`, `-5-`) for 3U DP Switch/V66 and **two** (`-0-`, `-3-`) for 6U DP Switch; the other two families have no such numbered dash alternatives in this section. Some rows use `X` for **Not Applicable**, so neither `X` nor all illustrated protocol combinations may be treated as a supported deployed configuration.

The source captions distinguish possible transport designs: 3U DP Switch data-plane Ethernet with control-plane Ethernet, 3U EP Switch PCI Express expansion plane with control plane, 3U DP Switch/V66 with an optical VITA 66 field, and a physically different 6U DP Switch. These terms describe physical port allocations and examples, not observed network routing, negotiated HTTP messages, live sensor measurements, or actual throughput. The original prose says the tables express legal protocols by port, but the **precise dense matrix column-to-cell alignment remains unverified** because the original source page-image route was unavailable; text access is not a full visual-port matrix audit.

## 2. Four actual example AMPS strings and original anomalies

Original Table 13.3.5-2 gives **four complete source examples**, not four tested or mandatory installed configurations:

| Source family | Original printed example (as source text) |
| --- | --- |
| 3U DP Switch | `MODA3-16.4.15-1-(5E8-4E7)(7E7)<3E19-N-E19-N>` |
| 3U EP Switch | `MODA3-16.4.16-1-(6P3F)(8E7-E3)` |
| 3U DP Switch/V66 | `MODA3-16.8.7-1-j-(3E8-4E7)(7E7)[E19]<3E19-N-E19-N>` |
| 6U DP Switch | `MODA6-10.8.1-j-(14E8-16E8-2E3)(15E7-E14)[E19]` |

The text distinguishes backplane copper fields `(...)`, VITA 66 optical backplane fields `[...]`, and SOSA-only **front-panel optical** switch fields `<...>`. This last meaning is **not** interchangeable with the Payload AMPS RF/XMC angle-bracket meaning reviewed in G2-7C, even though the same delimiters appear. The two example `-j-` forms are printed placeholders for slot-profile variants; no deployed dash selection or exact intermateability is inferred.

C239 contains **two original wording tensions** worth retaining verbatim as exceptions: the Switch section's introductory prose calls entries “Payload PICPs,” and the lead-in to Table 13.3.5-2 says its example strings are “from the PICPs of Table 13.3.4-3,” which is the preceding Payload AMPS example table. Neither source pointer is silently repaired or used to merge hardware roles. The note explicitly says the protocol values are *examples of format*; §13.3.7 normative Rule/SHALL material is **not part of this authorized packet**.

## 3. Crosswalk integration guardrails

Only the existing **The Open Group SOSA column I** of the single approved canonical crosswalk may receive qualified correspondence; W3C SOSA/SSN remains its distinct donor column. Candidate rows about physical constituents, hardware-profile roles, possible hosting/connection design, source-published protocol/switch choices and case evidence may receive PARTIAL/RELATED/NO_ESTABLISHED comparisons with native source IDs and an explicit boundary. A physical Switch PICP is not a CSAPI DataStream, ObservedProperty, network-addressed device, current applied configuration, or mandatory Domain Information Model class.

Preserve all **329 original information rows, 15 columns, 15 topic dividers, four case columns left, foundational OGC group and proposed DIM far right**. Earlier **58 donor-source facts, 73 empirical case facts, 480 ISA source outcomes/six open source questions, all previous SOSA source records and the 19 separate G2-7C holds** remain unaffected. Every substantive SOSA column update must appear in canonical JSON, both CSVs, both human-readable Markdown tables and the **SAME 26-sheet original editable Excel** with actual saved-grid parity before G2-7E can be started (mandatory lesson L23).

## 4. Explicit scope holds, corpus status and STOP

The [17 source-local holds](SOSA_G2_7D_Original_Source_Item_Coverage_10NOV2026.json) include original ANSI/VITA 65.0/65.1 and optical companion text, the eight unread C239 DSDM/IDL/OpenAPI originals, exact high-resolution matrix alignment, the two printed wording/pointer conflicts, the unselected `-j-` dash examples, and lack of actual installed-equipment facts. The new section adds **one** registered C239 heading at source inline text depth, bringing the cumulative status to **158 of 192 at least sampled/inline-read, 33 substantively unread, one restricted**. These are TOC-heading accounting totals, **not** a claim that every previously sampled section is thoroughly audited.

**Donor status: OPEN / source-PARTIAL**; no adopted DIM classes, cardinalities, CSAPI Profile SHALLs, real switch-card operations, manufacturer certification or independent runtime test. **STOP after G2-7D same-workbook validation and independent readback.** Only a **new owner “Proceed”** may start **G2-7E, original §13.3.6 Portion of the AMPS String for VITA 66 Connectors**, source-sized; the §13.3.4 and §13.3.5 matrix holds remain open and original Step18 SAPIENT stays blocked.
