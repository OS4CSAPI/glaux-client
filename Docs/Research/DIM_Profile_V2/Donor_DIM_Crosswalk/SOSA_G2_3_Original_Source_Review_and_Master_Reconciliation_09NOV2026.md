# SOSA-G2-3 — Original C239 §§6.3–6.5: out-of-band hardware and operational/security state audit

**9 November 2026 · G2-3 original C239 INLINE source review complete; full The Open Group SOSA donor review OPEN.** Original `c239_5.pdf`, The Open Group 2023 *Technical Standard for SOSA Reference Architecture*, Edition1.1, Project Library ID `file_00000000af4081f58c4bac329f85c58f`. Inspected all C239 PDF pp119–140, original printed pp93–114, through the end of §6.5.4.4 before §7 begins. Source figures' visible parsed text/captions were reviewed; attempted original diagram page-image retrieval was not consistently available, so exact plotted arrow/geometry coverage is not falsely certified. ANSI/VITA46.11/65.0, HOST, IPMI, native C239 DSDM/IDL/OpenAPI external files were not read.

## 1. Original source-item and standing ledger

[Stable C239 original source census](SOSA_G2_3_Original_Source_Item_Census_09NOV2026.json) catalogs 119 enumerated original native items (not DIM fields):

| Inspected item kind | Count | Source standing |
| --- | ---: | --- |
| Original printed Rule labels | 49 | 48 `shall` obligations; **one incomplete** source-labeled Rule6.4.2-20 lacking a grammatical `shall` |
| Recommendations | 8 | Source `should`, not generic `shall`; includes conditional PSC analog voltage/current sensor recommendations |
| Observations | 11 | Explanatory/interpretive, not source requirements |
| Permissions | 8 | Source `may`; Permission6.4.2-2/-3 duplicate wording |
| Defined operational states | 20 | Sensor S0–S5, PIC P0–P6, Module M0–M6, System Manager viewpoint |
| Defined security states | 12 | System integrity (4), PIC trust (3), software authentication (3), IMI security (2) |
| Architecture/context entries | 11 | Source design/meaning and edition qualification, not separate normative obligations |
| **Total enumerated** | **119** | One source item is neither one canonical DIM field nor proof of deployed behavior |

**C239 source text explicitly distinguishes descriptive state transitions from established command policy.** At §6.5 (PDF128/printed102), it says specific policies with normative language about taking particular operational state transitions are planned for a future edition. However, **§6.5.4 secure start-up has explicit C239 SHALL Rules** on hardware configuration authentication, software-package authentication, security state assignment, PIC version and MAC/IP port reporting, and secured/unsecured inter-module interface designations. Those are edition/role-conditional SOSA obligations, NOT newly adopted CSAPI Profile SHALLs.

## 2. Key differences that must survive crosswalk reconciliation

**Out-of-band hardware management (§6.3):** In a SOSA chassis, management-power IPMC/Intelligent Platform Management Bus (IPMB) may remain reachable with payload processor down. Chassis Manager may be a physical card, nonstandard element, or distributed function and can mediate inventory, diagnostics, recovery and power/thermal management. The source distinguishes *physical FRUs/Power Supply Cards, logical management functions, software payloads, communication transports and management vs payload power domains*; none automatically establishes physical assemblies in our four observed/reference case columns. Original descriptions of manufacturer, model, serial and revision information are capabilities of FRU inventory, not observed installed identities.

**Native hardware Rules (§6.4):** 49 source-labeled Rules include backplane IPMB, Tier-2/Tier-3 IPMC requirements, Non-Volatile Memory Read Only (NVMRO) write-inhibit/latching, SYSRESET*, GDiscrete1, Power Supply Card (PSC) control and source-specific slot addressing. Eight Recommendations include PSC analog input/output voltage/current sensors. **NVMRO inhibits certain nonvolatile writes to the extent declared by a vendor Certificate of Volatility**; it is NOT equivalent to sanitization, a physical sensor command, a guaranteed wipe, or permanent equipment disablement.

**Operational state (§6.5.1–6.5.3):** Sensor S0 Off is generally **unreported** because a System Manager may not be available. PIC P6 and Module M6 **Lost Communication** concern management-agent reachability, and both may remain otherwise physically operational; they are distinct from known P5/M5 Faulted conditions. S2/P2/M2 Operational indicates healthy/configured from the System Manager viewpoint and does NOT equal successfully performing a mission task. Cleansing and shutdown states describe intended transitions, not evidence of completed actions. PIC hardware and software Module state families are scoped separately.

**Security state and startup (§6.5.4):** The system's Evaluating/Protected/Degraded/Compromised integrity states differ from PIC Trust Pending/Trusted/Untrusted, software Authentication Pending/Authenticated/Unauthenticated, and an IMI's Secured/Unsecured state. A Root of Trust may be software/hardware, with implementation-specific credentials and policies. Untrusted PICs can possibly operate despite management perception; software should not execute when unauthenticated. These states and explicit startup SHALLs do not prove real equipment reports, deployed certificates, commands or DIM requirements.

## 3. Exact original-source holds, not silent repairs

- **SOSA-G2-3-H01 — NATIVE_REFERENCED_STANDARD_UNREAD:** ANSI/VITA 46.11/65.0, HOST Tier-2, IPMI normative command and signaling details are cited but not original-source audited; only C239 inline text inspected. Locator: §§6.3–6.4.
- **SOSA-G2-3-H02 — ORIGINAL_C239_INTERNAL_REFERENCE_MISMATCH:** Observation 6.4-2 cites 16.7-4/-5/-6; Rule 6.4-8 points to Recommendation16.7-1, even though current material is §6.4. Do not silently fix. Locator: C239 PDF123 printed97.
- **SOSA-G2-3-H03 — ORIGINAL_C239_TABLE_REFERENCE_MISMATCH:** Rule 6.4.2-6 cites Table17.5.1; Rule 6.4.2-11 cites Table7.15.2, while local selected VITA specification tables appear as 6.4.2-1/-2; meaning and external original source not reconciled. Locator: C239 PDF125/PDF127 printed99/101.
- **SOSA-G2-3-H04 — DUPLICATE_IDENTICAL_PERMISSION:** Permission 6.4.2-2 and -3 are identical about PIC hosting active Chassis Manager potentially sourcing GDiscrete1; two distinct source occurrences retained. Locator: C239 PDF126 printed100.
- **SOSA-G2-3-H05 — SOURCE_LABELED_RULE_INCOMPLETE:** Rule 6.4.2-20 lacks explicit SHALL/verb; do not infer exact obligation, retain as grammatically incomplete despite the Rule label. Locator: C239 PDF127 printed101.
- **SOSA-G2-3-H06 — DESCRIPTIVE_STATE_TRANSITION_POLICY_NOT_NORMATIVE:** C239 §6.5 explicitly says the specific normative policies for making a particular operational state transition are future work; diagram pathways not Profile SHALLs. Locator: C239 PDF128 printed102.
- **SOSA-G2-3-H07 — SOURCE_STATE_COPY_EDIT_CONFLICT:** PIC P5 discussion duplicates transition to P2 for different reasons; M5/M6 sections refer to PIC where the target is a Module. Preserve exact inconsistent prose, no repaired native state transition rule. Locator: C239 PDF132 and PDF135.
- **SOSA-G2-3-H08 — OFF_AND_LOST_COMMUNICATION_LIMIT:** S0 Off typically unreported and PIC/module P6/M6 manager-agent link unavailable, not proven actual hardware failure; no default 'faulted' display. Locator: C239 PDF129–135.
- **SOSA-G2-3-H09 — SOSA_EDITION_SCOPE:** 2015/2021 source imports, June2023 C239 plus Sep2023 erratum, 2025 S251 snapshot3 distinct; §6.4.2-22 eratta noted on original C239 cover, companion edition not interchanged. Locator: C239 cover and PDF128.
- **SOSA-G2-3-H10 — PHYSICAL_SOURCE_CASE_NONREPRESENTATIVENESS:** No observed four-case equipment data establishes that specific C239 chassis/PIC/IPMB, Root of Trust, voltage and current sensors, flags, or state machines exist in those systems; source only defines SOSA architecture. Locator: §§6.3–6.5.

The source has additional bounded copy-edit anomalies in the PIC/module state transition prose. The item ledger retains the native reference and exact section even when source language appears internally inconsistent. Do not use a generated interpretation to “fix” the original and then call it a C239 requirement.

## 4. Source-qualified correspondence to ONE canonical master

**28 existing The Open Group SOSA donor column-I cells** gained source-qualified original meaning with exact item IDs, edition and negative-equivalence boundary in the canonical JSON. No new DIM class, field, cardinality, universal chassis, Profile SHALL, or physical equipment event was adopted. The full 329 information rows, 15 topic dividers, 58 historical non-SOSA donor facts, 73 four-case evidence facts, previous ISA and G2-1/G2-2 findings are preserved; no other donor/case/DIM cell is rewritten.

| Existing original row | Source-qualified relation | New original evidence | Non-equivalence / boundary |
| --- | --- | --- | --- |
| S06-R001 | RELATED | SOSA-C239-G2-3-CONTEXT-FRU-IDENTITY | Architecture inventory capability, not a validated manufacturer of each installed System |
| S06-R002 | RELATED | SOSA-C239-G2-3-CONTEXT-FRU-IDENTITY | A subsystem FRU model does not equal an aggregate sensing System's model |
| S06-R003 | RELATED | SOSA-C239-G2-3-CONTEXT-FRU-IDENTITY | An architectural source inventory claim does not give serial number of any case hardware |
| S06-R007 | PARTIAL | SOSA-C239-G2-3-CONTEXT-MANAGEMENT-TIERS, SOSA-C239-G2-3-CONTEXT-CHASSIS-MGR-PLACEMENT | Management hierarchy and function hosting cannot establish universal physical containment or DIM chassis |
| ISA-E-COMPONENT-CATEGORY | RELATED | SOSA-C239-G2-3-CONTEXT-MANAGEMENT-TIERS, SOSA-C239-G2-3-CONTEXT-POWER-DOMAINS | SOSA hardware names are not the ISA human-facing component category enumeration |
| ISA-A-CERTIFICATE-TRUST | RELATED | SOSA-C239-G2-3-CONTEXT-ROOT-OF-TRUST, SOSA-C239-G2-3-RULE-6_5_4_1_4 … | No mandatory certificate Common Name, trust anchor schema or owner identity inferred |
| ISA-K-COMMAND-DECL | RELATED | SOSA-C239-G2-3-RULE-6_4_4, SOSA-C239-G2-3-RULE-6_4_5 … | External command table bytes not audited; not ISA command catalogue nor generic CSAPI control |
| ISA-A-BASELINE-CAPABILITIES | RELATED | SOSA-C239-G2-3-RULE-6_4_4, SOSA-C239-G2-3-RULE-6_4_6 … | Tier-specific hardware requirements are not ISA required/recommended capability support across systems |
| ISA-K-CAPABILITY-STATE | RELATED | SOSA-C239-G2-3-STATE-PIC-P6, SOSA-C239-G2-3-STATE-MODULE-M6 … | Management reachability is not actual equipment capability or arbitrary physical fault |
| ISA-C-082 | PARTIAL | SOSA-C239-G2-3-STATE-SENSOR-S2, SOSA-C239-G2-3-STATE-PIC-P5 … | State is source System Manager perspective; P6/M6 communication loss not confirmed fault |
| ISA-C-091 | RELATED | SOSA-C239-G2-3-CONTEXT-POWER-DOMAINS, SOSA-C239-G2-3-CONTEXT-OOB-LIGHTS-OUT | Separate power domains are not an observed component power condition |
| CASE-H04 | RELATED | SOSA-C239-G2-3-CONTEXT-POWER-DOMAINS, SOSA-C239-G2-3-STATE-PIC-P0 | Case-specific power source, charge, voltage and active equipment state remain unverified |
| CASE-H05 | RELATED | SOSA-C239-G2-3-STATE-PIC-P6, SOSA-C239-G2-3-STATE-MODULE-M6 … | No case-specific diagnostic or fault assertion established |
| ISA-C-052 | RELATED | SOSA-C239-G2-3-RECOMMENDATION-6_4_2_4 | SHOULD instrument PSC input current; no actual quantity, direct ISA component consumption or measurement |
| ISA-C-053 | RELATED | SOSA-C239-G2-3-RECOMMENDATION-6_4_2_2 | SHOULD instrument PSC output current; does not establish emitted device reading |
| ISA-C-054 | RELATED | SOSA-C239-G2-3-RECOMMENDATION-6_4_2_1, SOSA-C239-G2-3-RECOMMENDATION-6_4_2_7 | Output rail recommendation is not observed load-side DC voltage or adopted DIM field |
| ISA-C-055 | RELATED | SOSA-C239-G2-3-RECOMMENDATION-6_4_2_3 | Input rail recommendation is not observed DC source-side reading |
| ISA-C-072 | RELATED | SOSA-C239-G2-3-RULE-6_5_4_2_9, SOSA-C239-G2-3-RULE-6_5_4_2_10 | Network port status of directly managed SOSA PIC is not general ISA interface status of any component |
| ISA-C-108 | RELATED | SOSA-C239-G2-3-RULE-6_5_4_2_8, SOSA-C239-G2-3-CONTEXT-FRU-IDENTITY | PIC version information need not equal version of executing ISA software |
| ISA-C-066 | RELATED | SOSA-C239-G2-3-CONTEXT-FRU-IDENTITY | Hardware revision inventory possibility is not an observed hardware version |
| ISA-C-175 | RELATED | SOSA-C239-G2-3-CONTEXT-SECURE-STARTUP, SOSA-C239-G2-3-RULE-6_5_4_1_1 … | Architecture start-up sequence is not an ISA requested initialization command or proof of execution |
| ISA-C-223 | RELATED | SOSA-C239-G2-3-STATE-PIC-P6, SOSA-C239-G2-3-STATE-MODULE-M6 | Management connectivity loss does not equal ISA communication acknowledgement or device failure |
| ISA-C-232 | RELATED | SOSA-C239-G2-3-STATE-SENSOR-S3, SOSA-C239-G2-3-STATE-PIC-P3 … | Transition narrative is not a completed wipe, and specific transition policies not normative in Edition1.1 |
| ISA-C-235 | RELATED | SOSA-C239-G2-3-CONTEXT-OOB-LIGHTS-OUT, SOSA-C239-G2-3-CONTEXT-HARDWARE-MANAGEMENT-INTERFACES | Diagnostic architecture is not evidence of a performed diagnostic or ISA command |
| ISA-C-244 | RELATED | SOSA-C239-G2-3-STATE-SENSOR-S4, SOSA-C239-G2-3-STATE-PIC-P4 … | Neither stated transition policy nor actual hardware completion is established |
| ISA-T-STATUS | RELATED | SOSA-C239-G2-3-CONTEXT-MANAGER-VIEWPOINT, SOSA-C239-G2-3-STATE-PIC-P6 … | No ISA Status message correspondence, source time stamp or device telemetry value |
| ISA-A-SERVICE-ROLE | RELATED | SOSA-C239-G2-3-CONTEXT-MANAGEMENT-TIERS, SOSA-C239-G2-3-RULE-6_4_1_1 | Not one universal Controller role, physical chassis or mandated DIM ownership chain |
| S06-R018 | RELATED | SOSA-C239-G2-3-STATE-SENSOR-S2, SOSA-C239-G2-3-STATE-PIC-P6 … | A defined state machine is not a reported operating mode of an installed System |

**Negative/unmatched boundaries:** A source SHOULD recommending PSC analog sensors is not an observed measured voltage/current. Hardware commands defined by ANSI/VITA/HOST references are not an ISA command catalogue (those external originals were not inspected). NVMRO write inhibition is not requested permanent disablement. No `latest` or time-series state history is proven for ISA source rows, no claim a real case contains the SOSA PIC/chassis, and a known PIC/Module communications loss is not conclusive physical hardware fault.

## 5. Coverage count, mandatory Excel gate and next owner boundary

In the original 192-heading C239 G1 census, post-G2-2 the bounded standing was 70 at least sampled/inline-reviewed headings, 121 substantively unread and one restricted. This G2-3 packet reads nine TOC heading families, including five formerly UNREAD (§6.3, §6.4, §§6.4.1–6.4.2, §6.5) and four already sampled (§§6.5.1–6.5.4): the **new bounded heading standing is 75 source-read/sampled, 116 substantively unread, one restricted**. The original inline text of these families has been reviewed, but no relevant external ANSI/VITA/HOST or separate native SOSA companion source audits are certified complete. Unread does not mean no equivalent.

At this research publication instant, canonical JSON, both CSV mirrors and both Markdown comparison tables agree at **329×15 with 28 new SOSA cell qualifications**. The **SAME 26-sheet Excel is still the verified SOSA-G2-2 snapshot (SHA256 `35c36f7adfa47fed18b64a4cc2d4a7f3d40d24cf8ec683fdbbcdcdbd8ee5dfdb`)** until the required L23 saved-cell publisher/verification is executed; the difference is precisely 28 column-I cells. **Do not advance to another packet until its exact saved-XLSX source parity is verified.**

**Next only after successful packet publication and a separate owner “Proceed”: SOSA-G2-4 original C239 §§1–5 and 7–11 remaining architecture/mission/tasking source sections.** No automatic source packet, SAPIENT review, model adoption or conformance claim.
