# Step 17 / SOSA-C — C239 data model, interfaces, companions and edition boundary

**9 November 2026 · SOSA-C BOUNDED SOURCE REVIEW COMPLETE WITH EXACT NATIVE-FILE ACCESS HOLDS; full The Open Group SOSA Step17 still IN PROGRESS.** This is the third controlled increment of [the original Step17 donor assessment](Step17_SOSA_Source_Intake_and_Bounded_Assessment_09NOV2026.md), following [SOSA-A](Step17_SOSA_A_C239_Architecture_Roles_Review_09NOV2026.md) and [SOSA-B](Step17_SOSA_B_C239_Management_Operational_Review_09NOV2026.md). The **[structured evidence ledger](Step17_SOSA_C_C239_DSDM_Interfaces_Edition_Evidence_09NOV2026.json)** contains **23 original-C239 source concept/pointer statements, 17 qualified/negative correspondences to 15 existing master rows, eight precisely named source/edition/semantic holds and eight referenced but uninspected normative companion files**. The canonical master and physical cases remain unchanged; source integration is reserved to the separately authorized SOSA-D.

## 1. Exact original source and access standing

The primary original is The Open Group, *Technical Standard for SOSA Reference Architecture, Edition 1.1*, **C239**, June 2023 with September 2023 erratum. The project Library exposes the **403-page** original indexed `c239_5.pdf` (file `file_00000000af4081f58c4bac329f85c58f`). I directly read original C239 printed pp.35–37,335–357 and364–365 (PDF pages61–63,361–383,390–391), focusing on §5.7, §§14–15 and Appendix B. These named sections were examined within this scope, **not** the 403-page standard in its entirety or every original diagram/technical clause of the standard.

I searched the project-accessible repository and Library by exact filenames and checked current public discovery. The Library's PDF indexed text and selected original images are readable, but a requested raw-byte copy could not be materialized into the execution container, so **embedded attachment extraction could not be attempted on actual PDF bytes**. No separate, verified native `SOSA_TechStd_v1_DSDM`, `DSDM_IDL`, or any of the six exact OpenAPI JSON files was found in the accessible source results. The publisher publications URLs `https://publications.opengroup.org/standards/sosa/c239` and `.../s251` were not accessible through the available browsing route. **This is a bounded source-access HOLD, not a claim that the publisher does not distribute the files, or that the C239 PDF contains no attachments.** No native file hash, schema fields, UML entities or API endpoints can be authenticated from names alone.

## 2. What C239 itself establishes: conceptual/logical/physical data and transport

| Original source term | Source and precise meaning | Critical non-equivalence |
| --- | --- | --- |
| **DIV-1, conceptual** | §5.7.1, printed p.36 / PDF62: relationships and types of information, with distinct **mission** and **system-management** information domains | The PDF narrative alone does not disclose DSDM-native entity classes, associations or cardinalities |
| **DIV-2, logical** | §5.7.2, p.36 / PDF62: further logical information including measurements, units and coordinate systems | Not an actual reported measurement, sensor position, wire schema or universally adopted DIM data type |
| **DIV-3, physical representation** | §5.7.3 and §5.7, pp.35–36 / PDF61–62: intended physical representation, formats, bounds and structures | Here *physical* means data manifestation, **not** physical sensing-equipment hardware or installation |
| **Transport-independent data meaning** | §5.7, pp.35–36 / PDF61–62: the definition and carrying transport are separate concerns | Cannot infer SOSA DIV-2 = SWE Common or SOSA DIV-3 = CSAPI/ISA wire structure merely by similar wording |

**Important original-text discrepancy:** C239 §5.7 says normative material is in **Appendix B.2** (printed p.35 / PDF61), but Appendix **B.1** (printed p.364 / PDF390) actually identifies the SOSA data model; B.2 identifies the System Manager OpenAPI. We preserve both printed references and follow the actual B.1 contents for source identification without silently amending the original normative claim.

## 3. Eight separate authoritative-file references: verified pointers, not reviewed native content

| Original Appendix | C239 native file reference | What is currently established |
| --- | --- | --- |
| B.1 | `SOSA_TechStd_v1_DSDM` | Exact file *named* as the native DIV-1/DIV-2/DIV-3 DSDM; file contents unavailable |
| B.1 | `SOSA_TechStd_v1_DSDM_IDL` | Exact original IDL companion *named*; bytes unavailable |
| B.2 | `System Manager-SysMan-API.json` | System Manager in-band OpenAPI *named*; endpoints, parameters and schemas unreviewed |
| B.3 | `Module-SysMan-API.json` | Generic SOSA Module management OpenAPI *named*; contents unreviewed |
| B.4 | `Security Services-SysMan-API.json` | Security Services management OpenAPI *named*; contents unreviewed |
| B.5 | `Chassis Manager-SysMan-API.json` | Chassis Manager management OpenAPI *named*; contents unreviewed |
| B.6 | `PIC-SysMan-API.json` | Plug-In Card management OpenAPI *named*; contents unreviewed |
| B.7 | `PIC with SW RTE-SysMan-API.json` | PIC/software Run-Time Environment management OpenAPI *named*; contents unreviewed |

These **eight references are one SOSA donor lineage**, not eight independent standards. The earlier 182-artifact index identifies DSDM Edition1.0 separately and the Edition1.1 IDL/API companions; those older source-ledger entries **do not prove the C239-referenced native DSDM's exact bytes or edition**. The SOSA-C evidence register keeps its source pointer as a separate unresolved native-file identity.

## 4. C239 §§14–15: source-supported implementation and interaction structure

**Run-Time Environment (RTE), §14.1 (printed pp.335–337 / PDF361–363).** C239 identifies three distinct software execution profiles: Future Airborne Capability Environment (FACE) Operating System Segment, Container and Virtual Machine. Conditional Rules 14.1-1–4 concern which profile is used according to the implementation form. Multiple executables/containers can realize one logical SOSA Module; execution containment is **not** identical to a physical Hardware Element, Host Platform, Sensor or original measurement source.

**RTE configuration, §14.2 (printed pp.337–338 / PDF363–364).** Rules 14.2-1–6 address configuration per RTE, `ProfileType`, `ImageLoad`, `Resources`, and conditional `FileSystem` and `StartOrder` data. Observation 14.2-1 says the original edition specifies minimum configuration content rather than a complete file format, and Recommendation 14.2-1 suggests human-readable XML, JSON or YAML. These C239 configuration fields are real, source-verified original terms—not an equivalent of an ISA `Config` message or a mandate that all DIM elements implement these configuration fields.

**Interaction roles and families, §15.1 (printed pp.346–347 / PDF372–373).** The source defines analog distribution, digital signal streams, associated signal context, low-latency signal-layer control, discrete interactions, publish-subscribe, request-response and event notification. It distinguishes a general-purpose SOSA Message Interconnect from a Wideband Low-Latency Interconnect. **Digital sender, requester, responder, publisher, subscriber and message producer do not by themselves identify an original physical observing sensor**, a CSAPI System URI or a source-authenticated Observation.

**Interface and QoS, §§15.2–15.3 (printed pp.348–351 / PDF374–377).** Conditional Rule 15.2-1 concerns portable SOSA module software and FACE 3.1 transport capabilities, while Quality of Service (QoS) is a producer/consumer data-flow compatibility arrangement. This is an implementation/interface dimension, not a new physical sensing class or performed Observation.

**Wire interaction-binding stack, §15.4 (printed pp.351–352 / PDF377–378).** The five explicit categories are *Data Definition, Data Encoding, Encapsulation, Transport and Network*. Table15.4-1 lists three source choices for relevant interactions: **OMG DDS/RTPS v1.4+**, **Protobuf v3 + AMQP v1.0**, and **Protobuf v3 + ZMTP v3.0**. Rules 15.4-1–2 are conditional on the specified Message Interconnect/implementation circumstances and absence of contrary sections; they do **not** impose those technologies on CSAPI or disclose the uninspected DSDM entity list.

**Endpoint interactions and security, §§15.6.1–15.6.4 (printed pp.353–357 / PDF379–383).** §15.6.2 distinguishes endpoint roles and directionality (publishers/subscribers, requester/responder, sender/receiver). Publish-subscribe topics identify structured information exchanges, **not sensors or observed properties**. Request-response operations do not prove a requested physical control was performed. Event notification is triggered reporting, not the original performed Observation. Where security is required and named transport conditions apply, Rules 15.6.1-1–2 specify TLS/DTLS configurability. That is not independent evidence of sensor-deployed security or source authenticity. The source's later §15.6.4 language that general publish-subscribe implementation is not yet determined must be read with the earlier specifically conditional §15.4 rules, rather than forced into a universal implementation claim.

## 5. Version control and 2025 snapshot limits

**C239** remains the source edition of this audit. The separate **S221** AFRL-hosted PDF often labeled generically *Edition 2.0* is explicitly a **2022 Snapshot1**, not the registered **S251 Edition2.0 Snapshot3** released June 2025. [Contemporary June 2025 announcement](https://militaryembedded.com/radar-ew/sensors/sosa-consortium-releases-the-technical-standard-for-sosa-reference-architecture-edition-20-snapshot-3) reports updates to the SOSA data model, hardware and communications, with Snapshot3 features intended for a future official Edition2.0. The [U.S. ASSIST adoption record](https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=287032) names `SOSA-ED.2.0-SNAP3`, with an adoption date of May19,2025; DoD adoption of a **snapshot identifier** must not be mistaken for the publication of the finished Edition2.0 standard. The exact S251 source and bundle were **not** inspected, so no source-native Edition2.0 semantic deltas are asserted.

## 6. Evidence-to-existing-master comparison — staged only

The JSON ledger records **17 bounded source-first comparisons touching 15 existing working-master rows**. Illustrative associations: DIV-2 quantity semantics with `ISA-R-MEASUREMENT`, RTE configuration with `ISA-T-CONFIG`, source-defined interaction binding with `ISA-A-CONNECTION-PRESENTATION`, request/response with `S06-R019`/`S06-R020`, message topics with `ISA-Q-SUBSCRIPTION`, and source-independent digital payloads with `S06-R012`. Relations are intentionally **RELATED**, **PARTIAL**, **CASE-RELEVANT**, or **NO ESTABLISHED EXACT EQUIVALENCE**. There is no source-supported exact original DSDM-to-DIM class mapping, no mandatory new DOM class, no API conformance claim, and no reinterpretation of four source cases.

**All existing 329 master information rows, 14 columns, 58 prior donor evidence records and 73 original case facts are preserved unchanged.** This source stage introduces zero master rows, zero cell edits, zero DIM approvals and zero verified native OpenAPI endpoints.

## 7. Completed scope, exact holds and next authorized action

SOSA-C's **bounded original-C239 architectural and interface review is COMPLETE WITH EIGHT SOURCE ACCESS/QUALIFICATION HOLDS**. That does **not** mean the SOSA DSDM or native management APIs have been reviewed; the crucial normative native evidence remains unavailable. The structured ledger identifies one native DSDM, its IDL, six management JSONs and eight outstanding question classes, so a later review cannot silently treat missing source content as completed.

**Next separate owner “Proceed” = SOSA-D only.** Use the original-source-verified SOSA-A/B/C evidence to integrate a distinct The Open Group SOSA donor column into the **single canonical crosswalk and synchronized workbook**, preserve the correct W3C SOSA/SSN distinction, and label unverified native DSDM/API concepts as held. Verify exact source/CSV/JSON/XLSX and historical donor/case preservation. If a native schema is indispensable for a proposed mapping, leave that mapping unestablished, not invented. The broader Step17 donor assessment **cannot be called an exhaustive normative DSDM/API audit** after SOSA-D unless those original files have actually been inspected. Step18 SAPIENT remains untouched.
