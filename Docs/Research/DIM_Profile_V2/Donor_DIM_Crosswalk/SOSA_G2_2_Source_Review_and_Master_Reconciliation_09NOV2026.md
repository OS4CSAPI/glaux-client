# G2-2 final Excel checkpoint addendum — 9 November 2026

**Saved workbook source parity is VERIFIED**, superseding the G2-2 prepublication lag described later in this report. The original-source findings (352 C239 entries/rule appearances) and the 22 existing-row qualified comparisons are unchanged; the SAME [26-sheet master Excel](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) now includes **all 22 column-I changes** and agrees cell-for-cell with JSON, both CSV mirrors and both readable comparisons across **346×15**. [Actual saved workbook checks](SOSA_G2_2_Workbook_Validation_09NOV2026.json) · [successful Actions run](https://github.com/OS4CSAPI/glaux-client/actions/runs/42753787384) · [workbook publication commit](https://github.com/OS4CSAPI/glaux-client/commit/6cbfcf46f5991ebf93b00083f112fd250e4609de). The Excel lag is **zero**, 22 historical sheets remain byte preserved; source completeness, native API/DSDM access, adoption and external conformance remain unproven. **NEXT only on separate owner Proceed: SOSA-G2-3 C239 §§6.3–6.5. SAPIENT blocked.**

## Original G2-2 source review and its historical prepublication Excel state

# SOSA-G2-2 — Original C239 §§6.2.6–6.2.9: native source census and master reconciliation

**Evidence status:** Bounded G2-2 ORIGINAL INLINE TEXT RESEARCH COMPLETE; wider The Open Group SOSA donor **STILL OPEN**. Original 2023 C239 Edition 1.1 (`c239_5.pdf`, Project Library ID `file_00000000af4081f58c4bac329f85c58f`) was examined across PDF pp90–118, original printed pp64–92, through the end of §6.2.9.3. This packet reviewed four specialized in-band management families (Security Services Module, Chassis Manager hardware element, SOSA Plug-In Card, Plug-In Card hosting Software Run-Time Environment), not the following §6.3 out-of-band requirements nor any separate native OpenAPI JSON files.

## Full original-native inventory (not DIM field count)

| Original source family | Functions | Interactions | V1.0 entries | Future entries | Source-labeled Rules |
| --- | ---: | ---: | ---: | ---: | ---: |
| Security Services (§6.2.6) | 65 | 32 | 56 | 41 | 2, both `shall` |
| Chassis Manager (§6.2.7) | 41 | 27 | 44 | 24 | 2, both `shall` |
| PIC (§6.2.8) | 50 | 36 | 54 | 32 | 6, four `shall` + two descriptive |
| PIC + SW RTE (§6.2.9) | 53 | 36 | 54 | 35 | 2, both `shall` |
| **Total** | **209** | **131** | **208** | **132** | **12 (10 `shall`, 2 descriptive)** |

The machine-readable [**352 original source-item occurrences with stable IDs**](SOSA_G2_2_Original_Item_Inventory_09NOV2026.json) captures all eight function/interaction native tables, support labels, edition, exact section and original page, and each appearance of the source-labeled Rules. These are not 352 unique DIM concepts or 352 independently verified interface endpoints. C239's `V1.0` means source-defined edition support; `Future` is planned later, not presently claimed implemented. Actual referenced native B.4–B.7 OpenAPI files and C239 DSDM/IDL were **NOT** opened or parsed.

## Source semantics and four important distinctions

1. **Security Services is not an observed security monitor.** Its system security status, many security alerts, attestation/verification and cryptographic resource functions are marked `Future`, while named security logging and several health management entries are `V1.0`. The owner cannot infer currently deployed security posture, trust, authentication or capabilities merely from source role names.
2. **Chassis Manager is a source-specific hardware element, not the DIM's universal chassis.** Its `executeCommand` interface (`LowLevelCommand` input, `LowLevelResult` output) is `V1.0`, described as a bridge to lower-level IPMI out-of-band management with possibly restricted access (Table 6.2.7.1-1, printed74 / PDF100 and interaction Table 6.2.7.2-1, PDF103). This does not establish unrestricted hardware command authorization, executed device control or an OGC API command.
3. **Physical PIC, its management representation, and hosted software runtime are distinguishable.** §6.2.8 says some PICs are unmanaged, and some managed PICs are indirectly represented by an interface implemented on another PIC. §6.2.9 defines PIC-with-SW-RTE as hardware that hosts one or more RTE instances; the application state interactions (load/unload/start/stop/pause/resume/reset) concern software lifecycle, not a one-to-one physical sensor subassembly or control of an observed deployed sensor.
4. **Do not collapse Source Mode, State, Health, BIT and Configuration.** ApplicationStateRequest/ApplicationState, ComponentMode, ComponentState, SecurityStatus (Future) and the different *SecurityServicesConfig*, *ChassisManagerConfig*, *PluginCardConfig* and *PluginCardSWRTEConfig* source types have different scopes. Many `get...Config` operations are `V1.0` while the associated `updateConfig` interactions remain `Future`; no per-property ISA mutability or generic DIM control contract follows.

## Original source questions/holds

- **SOSA-G2-2-Q01 (cross-reference conflicts):** All four specialized in-band interface `shall` rules refer literally to **Appendix B.3**, while original Appendix B.4–B.7 name the appropriate specialized OpenAPI files for Security Services, Chassis Manager, PIC and PIC-with-SW-RTE. B.3 is the generic-module file. Preserve **both** original labels and references, not an assistant correction.
- **SOSA-G2-2-Q02 (duplicate source rule IDs):** The two initial paragraphs labeled `Rule 6.2.8.3-1/-2` state descriptive scope and that not every PIC category is prescribed. The following normative `shall` Rules reuse the identical two numbers, then Rules -3/-4 follow. Evidence IDs preserve all six occurrences and distinguish description from obligations.
- **SOSA-G2-2-Q03 (PIC applicability):** A delegated interface is not a physically built-in device interface, and source does not require in-band support for all PICs.
- **SOSA-G2-2-Q04 (low-level IPMI boundary):** Potentially restricted Chassis Manager low-level command gateway is not carte blanche to operate hardware; the source explicitly describes the out-of-band bridge.
- **SOSA-G2-2-Q05 (unread original native files):** Native model/IDL and B.4–B.7 schemas remain unavailable for actual field, path, cardinality or interoperability verification.
- **SOSA-G2-2-Q06 (unpublished function–interaction join):** Do not invent exact mapping where source table notes omit original function-to-interaction crosswalk.

## Progressive integration into the ONE canonical master

**Exactly 22 existing The Open Group SOSA donor column-I cells** gained source-graded, caveated meaning. Each row points to stable original item IDs and records relation status and a negative-equivalence boundary in the canonical JSON. Earlier SOSA-D and G2-1 comparison text remains retained; all ISA, other-donor, case and DIM labels/values remain unchanged. Some original items contribute only supporting evidence or explicit negative correspondence (e.g., `Future` resource reservations do not establish ISA time-bounded exclusive command access), so no forced new DIM classes, fields or source-category fields were created.

| Existing canonical row | Qualified relation | Illustrative original source IDs | Meaning not established |
| --- | --- | --- | --- |
| S06-R007: Physical constituent | PARTIAL | SOSA-C239-G2-2-CMI-012, SOSA-C239-G2-2-RTEI-031 … | Physical PIC and logical RTE must not collapse into one physical constituent or imply this chassis exists in any source case. |
| ISA-E-COMPONENT-CATEGORY: Human-facing component category | RELATED | SOSA-C239-G2-2-SSI-019, SOSA-C239-G2-2-CMI-022 … | Architectural hardware/function category differs from ISA's human-facing component-category code and from real equipment observation. |
| ISA-A-MEMBER-EXPOSURE: Composition member exposure and source attribution | NO_ESTABLISHED | SOSA-C239-G2-2-RULE-07, SOSA-C239-G2-2-RULE-08 | Do not infer ISA composition or ownership from SOSA delegated management representation. |
| ISA-A-SERVICE-ROLE: Service role and required command support | RELATED | SOSA-C239-G2-2-RULE-01, SOSA-C239-G2-2-RULE-03 … | No universal DIM service class, mandatory chassis superclass or ISA Controller role implied. |
| ISA-A-BASELINE-CAPABILITIES: Required and recommended capability support | RELATED | SOSA-C239-G2-2-CMI-019, SOSA-C239-G2-2-PICI-024 … | Support label is an edition endpoint declaration, not evidence every PIC implements it or an ISA required capability. |
| ISA-K-CAPABILITY-STATE: Capability readiness and reporting selection | RELATED | SOSA-C239-G2-2-RULE-05, SOSA-C239-G2-2-RULE-06 … | Management representation is not ISA capability enablement nor measured runtime readiness. |
| ISA-K-COMMAND-DECL: Declared command interface | RELATED | SOSA-C239-G2-2-CMI-012, SOSA-C239-G2-2-CMF-018 | Not a generic ISA command declaration nor authorization to issue a physical control action. |
| ISA-K-RESULT-DECL: Declared command result | RELATED | SOSA-C239-G2-2-CMI-012 | Specified result object is not observed execution proof or CSAPI command-result schema. |
| ISA-K-MUTABILITY: Declared property mutability | RELATED | SOSA-C239-G2-2-SSI-019, SOSA-C239-G2-2-CMI-022 … | Future config update does not establish mutable deployment properties. |
| S06-R018: Source-reported operating mode | RELATED | SOSA-C239-G2-2-SSI-012, SOSA-C239-G2-2-CMI-013 … | Source-defined retrieval interface does not prove a mode value emitted by any of the four real-case sources. |
| S06-R019: Issued control request | RELATED | SOSA-C239-G2-2-PICI-012, SOSA-C239-G2-2-PICI-015 … | An application-lifecycle request is not a physical sensor actuation or observed issued CSAPI control. |
| S06-R020: Command acknowledgement / reported outcome | RELATED | SOSA-C239-G2-2-CMI-012, SOSA-C239-G2-2-PICI-014 | Object type in a source table does not prove completed command, fault-free response or ISA TaskAck equivalence. |
| ISA-C-177: Requested component active state | RELATED | SOSA-C239-G2-2-PICI-014, SOSA-C239-G2-2-PICI-015 … | Application state is distinct from whole component enabled/active state or physically operational status. |
| ISA-T-STATUS: Component property-value report | RELATED | SOSA-C239-G2-2-SSI-001, SOSA-C239-G2-2-SSI-022 … | Not one generic ISA Status object; Future security status is not source-supported current operational reporting. |
| ISA-T-ADMIN: Administrative network and service notification | RELATED | SOSA-C239-G2-2-SSI-013, SOSA-C239-G2-2-CMI-014 | No direct equivalence with ISA administrative network/service notifications or deployed event subscription. |
| ISA-T-ACCESS: Request access-control metadata | RELATED | SOSA-C239-G2-2-CMF-018, SOSA-C239-G2-2-CMI-012 | Possible restriction is not an observed authorization grant, credential field, or mandatory CSAPI security control. |
| ISA-C-046: Latest built-in-test reported result | RELATED | SOSA-C239-G2-2-SSI-008, SOSA-C239-G2-2-CMI-008 … | No source-native guarantee that a returned BIT result is the latest actual hardware test event. |
| ISA-C-235: Requested component diagnostic procedures | RELATED | SOSA-C239-G2-2-SSI-007, SOSA-C239-G2-2-CMI-007 … | Interface presence is not completed physical diagnostic or ISA command-definition equivalence. |
| ISA-C-244: Requested component shutdown sequence | RELATED | SOSA-C239-G2-2-SSI-011, SOSA-C239-G2-2-CMI-011 … | No observed component shutdown sequence or success implied. |
| ISA-C-232: Requested removal of security-relevant application data | RELATED | SOSA-C239-G2-2-SSI-015, SOSA-C239-G2-2-PICI-023 … | No proof of secure removal of specified ISA application data or a completed zeroization. |
| ISA-C-211: Requested current component configuration message | RELATED | SOSA-C239-G2-2-SSI-019, SOSA-C239-G2-2-CMI-022 … | Different native role-specific schema names are not one ISA Config message or observed installed configuration. |
| ISA-R-EXECUTION: Current command execution record | RELATED | SOSA-C239-G2-2-CMI-012, SOSA-C239-G2-2-PICI-012 | A declared output type is not a current command execution history record or proof of hardware control. |

## Corpus coverage and owner stop boundary

The G1 source corpus contains **192 C239 TOC headings**: 65 previously sampled, 126 substantively unread and one restricted. After G2-1, 67 were at least source-read and 124 remained unread. This G2-2 packet fully inspected **inline C239 original tables/Rules** for four heading families, of which **three** were previously unread: the coverage ledger therefore advances to **70 at least source-read, 121 substantively unread, one restricted**; the four families' separate native API model files are still not read. This is not a source-complete C239 or SOSA certification.

**The G2-2 text master is 329×15 with 22 qualified SOSA cells; the saved pre-publication XLSX remains the G2-1 checkpoint (SHA256 `6a22fb1d76be9decd11a0023136d55750971020c8c23d60dc4dbb57ab332ec9b`) until this SAME packet's mandatory L23 Excel publisher and actual saved-cell verification succeed.** The publisher must preserve all 26 original tabs and all case/ISA/other-donor cells. Neither a no-source-inventory ledger nor a workbook integrity check proves donor completeness, accepted DIM content, a CSAPI Profile `SHALL`, runtime conformance or an installed equipment operation.

**Owner stop:** G2-2 original-source packet only. Once its required Excel synchronization is verified, **the next separate user “Proceed” may authorize SOSA-G2-3 only (C239 §§6.3–6.5, out-of-band hardware management and component states)**; original Step18 SAPIENT remains BLOCKED until donor coverage gate and owner disposition.
