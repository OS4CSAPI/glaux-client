# Step 07 — Controlled-Corpus Qualification Decision

**Version:** 0.1 · 30 October 2026 (America/New_York)  
**Standing:** **STEP 07 COMPLETE — THREE PRIMARY REFERENCE/EXAMPLE CASES SELECTED; STEP 08 FREEZE NOT STARTED.** AirGradient (A), Dragino (C) and Campbell (D) qualify only within the documentary/example scopes below. Raspberry Shake & Boom (B) remains **CONDITIONAL / NOT A QUALIFIED PRIMARY CASE**. **No qualified actual-operating-history dataset or end-to-end interoperability evidence has been established.**  
**Workspace:** `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, `Docs/Research/DIM_Profile_V2/Controlled_Corpus/`.  
**Authority:** [Eight-step plan](../PLAN_DIM_Profile_V2_Controlled_Sensing_Equipment_Corpus_Qualification_v0.1_29OCT2026.md), Step 07 only; unchanged [Step 01 eligibility gates](01_Eligibility_and_Evidence_Gates.md), especially §§2, 5–6. The owner's separate “proceed” authorized comparison and selection, not the evidence freeze or additional audits.  
**Purpose:** Evidence for the implementation-independent Domain Information Model (DIM), separate OGC API – Connected Systems (CSAPI) application Profile and common System Resource Details experience in the [original problem/outcome baseline](../DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md).  
**Pre-step repository revision:** `4d832aac11597bb0bbaed7578a35fa17e575d679`.

## 1. Decision in ordinary language

**Choose AirGradient Open Air Max, Dragino S31-LB and Campbell CR1000X with first-generation ClimaVue 50 as the three primary cases for bounded source-based research.** Each has a documented sensing configuration and an inspected original message/example relevant to the declared case or an explicitly identified component. Together they provide different equipment arrangements and different interpretation problems. We do not need to pretend they are three authenticated field installations to use that evidence. [A, C, D, §C]

**This is a qualified reference/example set, not the comprehensive operating dataset we hoped might also be obtainable.** None of the four audits acquired qualifying actual observations/history. The selected examples cannot establish installed configuration, real equipment health, successful commands, calibrated measurement accuracy or live source-to-client fidelity. The documentary progress is useful, but that operational-evidence objective remains unmet. [A–D, §G]

The distinction is already in the approved research method: Step 01 allows documented reference configurations and original published examples, including a case with zero actual-history coverage, provided its permitted uses are bounded. This decision does not relax a gate, invent a compensating score or reinterpret synthetic tests as original evidence. The selected membership is now decided for this plan; exact evidence preservation and its reproducibility limits remain Step 08. [Step 01, §§2, 5–6]

## 2. Basis of this comparison

This is a synthesis of the **four completed audits**, not another manufacturer investigation. The records below were checked at the pre-step revision. The mounted audit copies have the same computed Git blob identifiers as the repository files. Source IDs such as A02 or D07 retain their meaning inside their own audit; they are not new entries in the frozen 182-artifact donor inventory.

| Reference | Controlling audit and passages | Verified Git blob |
| --- | --- | --- |
| **A** | [AirGradient audit](03_Candidate_A_Evidence_Audit.md), §§A, C–H; source register §B | `02f103cd3832e9317fd5d5e05126cb64e7692578` |
| **B** | [RS&BOOM audit](04_Candidate_B_Evidence_Audit.md), §§A, C–H; source register §B | `8f8b90b4ce9163a058a656e3ba590e8e45d27c04` |
| **C** | [Dragino audit](05_Candidate_C_Evidence_Audit.md), §§A, C–H; source register §B | `8b90e7d436516541845ac533ad7204c2a168210b` |
| **D** | [Campbell audit](06_Candidate_D_Evidence_Audit.md), §§A, C–H; source register §B | `287c2b81c49ccd59c79ae5f7b4d31068e81f4ef6` |

**Fixed comparison snapshot:** [Controlled_Corpus at the pre-step commit](https://github.com/OS4CSAPI/glaux-client/tree/4d832aac11597bb0bbaed7578a35fa17e575d679/Docs/Research/DIM_Profile_V2/Controlled_Corpus). Criteria blob: `7592bc828a11977e6e308b929d9081da68bac416`. The audit reports retain original publisher links, editions, access attempts, examples and limitations. This document relies on their findings and does not claim independent rechecking of every primary source or rerunning their checkers in Step 07.

## 3. Gate findings and exact membership

| Case | G1: bounded configuration | G2: whole-System account | G3: inspected record/example | G4: traceability | Existing verdict and Step 07 disposition |
| --- | --- | --- | --- | --- | --- |
| **A — Open Air Max O-M-1PPSTON-CE gas-equipped assembly** | MET | MET | MET by original examples | MET for declared reference/example scope | **PASS; SELECTED primary reference/example case.** Not all commercial `-CE-S` variants or an installed release pair. |
| **B — Raspberry Shake & Boom V3 reference; separate AM.R9D92.00 historical lead** | MET at reference scope | MET | **UNVERIFIED** | MET for documentary review only | **CONDITIONAL; NOT SELECTED as a primary case.** Retain as a limited documentary comparator and unresolved data lead, not a passing benchmark. |
| **C — S31-LB external-probe, primary-battery node** | MET | MET | MET by original historical-message example | MET for stated scope | **PASS; SELECTED primary reference/example case.** No imported S31B/LS construction or authenticated region/firmware. |
| **D — CR1000X + one first-generation ClimaVue 50 assembly and cable** | MET at reference scope | MET | MET with **logger-component** example scope | MET for declared documentary scope | **PASS; SELECTED primary reference/example case.** Not a complete installed station dataset, CR1000Xe or ClimaVue 50 G2. |

These are the existing gate findings, not new scores or upgraded verdicts. D's supporting power, housing, wiring and mounting roles are documented, but no specific battery, enclosure SKU, modem or site is invented. Its original CR1000X status example is useful for the named logger component; it is **not** a ClimaVue observation or output from the historical pairing-specific program. B's potentially obtainable files remain uninspected, and another case's examples cannot satisfy B's G3. [A–D, §§A, C]

METER ZL6 + ATMOS 41 and AudioMoth remain the **unaudited reserves** recorded in [Step 02](02_Discovery_and_Four_Audit_Slots.md); they are neither promoted into this set nor declared failed. Surveyor and McQ RANGER did not receive audit slots because the discovery review did not locate sufficiently defined public native examples. Their absence from this set is not evidence of product inferiority or universal source unavailability. No new candidate or fifth audit is introduced.

## 4. Comparison on the unchanged common questions

The columns describe **available evidence**, not four operating devices. Every cell inherits the corresponding audit's §§A, C–F and cited primary sources.

| Step 01 question | A — AirGradient | B — RS&BOOM, not selected | C — Dragino | D — Campbell |
| --- | --- | --- | --- | --- |
| **Q1 — What exactly is this case?** | Named gas-equipped assembly; hardware and firmware descriptions independently pinned. | Combined V3 reference and separately attributed historical station; no inspected file join. | External-probe/battery reference product; deployed region/firmware unknown. | Named logger/sensor pairing; no authenticated installation or tested release combination. |
| **Q2 — What is included?** | Documented modules, two particulate sensors, main board, enclosure and solar/battery roles; alternatives not assumed fitted. | Two sensing functions with shared support; actual station inventory/filter choice unknown. | One cabled probe supporting two quantities, node electronics, radio, enclosure and battery; gateway is external context. | Logger, sensor assembly and cable with support roles; multiple response quantities are not a physical inventory. |
| **Q3 — What can be configured or commanded?** | Portal choices and parsed command/configuration keys; no actual configuration or completion sequence. | Setup/forwarding choices; no applicable configuration export or executed command. | Command documentation and decoder branches; synthetic setting/status probes are not device state. | Historical pairing-specific program and separate later download description; no compiled/running program or applied settings. |
| **Q4 — How is operation or condition described?** | Voltage examples, power paths and local diagnostic/mode documentation; no current health record. | Local diagnostic mechanisms and power-input context; no acquired status, unresolved consumption inconsistency. | Voltage/flag definitions and battery caveats; no diagnostic history or remaining-capacity measurement. | Detailed **logger** status example; sensor verification is documented separately, not acquired. |
| **Q5 — What records/examples were actually inspected?** | Original cellular, annotated Wi-Fi and separate cloud examples; no real history. | No usable candidate-specific record/example obtained; other-model packets excluded. | Original eight-entry history-message example plus a pinned decoder; additional probes explicitly synthetic. | Original 31-field logger-status example and historical program text; no attributable weather series. |
| **Q6 — Do records and documentation describe the same scope?** | Product-level links support attribution; not one deployed release or synchronized readings. | Provider attribution is recorded; headers, response epochs and contents not verified. | Manual covers product; example does not authenticate a particular unit, firmware or region. | Pairing is documented; independent program/manual/API editions and component sample are not one operational stack. |
| **Q7 — Can the evidence be reproduced?** | Pinned repositories and example checker; mutable pages, failed live retrieval and disputed PDF excluded. | Exact leads and failed attempts retained; no acquired waveform/response and reuse restrictions remain. | Pinned decoder and offline harness; manual mutable, source permissions and version gaps retained. | Source editions and checker; transcribed JSON is not original bytes, current program package uninspected. |
| **Q8 — What useful differences should survive?** | Physical module versus quantities; raw versus calculated values; communication-path distinctions. | Equipment/channel/response identity; public data availability versus local management. | Timezone, absence markers, physical probe versus output fields and misleading convenience labels. | Logger versus sensor status; Boolean output state versus voltage; processing and carried-forward values. |

**Configuration, condition and measurement are not interchangeable coverage.** A mainly supplies measurement/power examples. C supplies an original historical-message example and documented controls, not actual status/configuration snapshots. D supplies a logger-status example, not a joined weather/configuration/status history. Their complementarity helps compare meaning, but cannot be combined into a fictitious fully evidenced operating System. [A–D, §D]

### Evidence-depth scores retained without aggregation

| Existing dimension (0 absent, 1 thin, 2 useful, 3 strong) | A | B | C | D |
| --- | ---: | ---: | ---: | --- |
| Whole-System component/architecture | 3 | 2 | 2 | 2 |
| Capability/configuration | 2 | 2 | 2 | 2 |
| Operational condition/power/diagnostics | 2 | 2 | 2 | **3 at logger-component scope only** |
| Machine-readable source/communication | 2 | 1 | 2 | 2 |
| Actual attributed observations/history | **0** | **0** | **0** | **0** |
| Reproducibility/version/rights | 2 | 2 | 2 | 2 |

Source: each audit §G. No sum, average, weighting or performance ranking is calculated. Zero history means no qualifying real records acquired in those bounded audits, not proof that real data does not exist. D's condition score cannot be applied to the ClimaVue or whole station, and no score compensates for B's unverified G3.

## 5. Why select all three passing cases rather than only two?

**A provides the integrated multi-sensor equipment case.** Its assembly description and independently attributed representations let a later study ask whether one physical module, several outputs, alternative communication paths and source-specific power quantities remain distinguishable. Gas calibration, the unresolved AFE unit, timing differences and suffix/release uncertainty stay outside unsupported quantitative or runtime assertions. [A, §§A, D–F]

**C adds a simpler external-probe wireless node and executable message-interpretation evidence.** Its original example and offline decoder checks make time interpretation, no-data handling and convenience labels concrete rather than hypothetical. This is a different research contribution from another integrated monitor; the synthetic branch probes remain separately labeled and cannot provide missing device observations. [C, §§D–F]

**D adds an explicitly separate logger and sensing assembly, richer component diagnostics and documented processing.** The source-described pressure adjustment and wind-value carry-forward expose questions about reported versus directly measured values. Its status example distinguishes supply voltage, internal battery voltage, panel temperature and switched-output state. Those are logger meanings, not evidence about the sensor's current condition. [D, §§D–F]

This is an analyst selection judgment based on the completed evidence, not a claim that three products represent the full intended domain. All three contribute something the other two do not cover in the same way. The set therefore has three manufacturers and structural variation, but its accepted sensing cases remain environmental-monitoring examples with overlapping quantities. **The desired qualified seismic/acoustic or surveillance case is missing.** B preserves a route back to that comparison only at documentary level; it does not fill the gap by being listed beside the selected cases. [A–D, §A; Step 02]

## 6. What the selected set can and cannot support

**Supported as inputs to later, separately authorized work:** source-based comparison of equipment/component roles, source-native quantities and types, documented configuration possibilities, component-scoped condition information, interpretation hazards, and traceable worked examples. The set can challenge a proposed representation: would it confuse a module with an output, a voltage with capacity, no data with zero, or a carried-forward value with a fresh measurement? These are prospective uses of the inspected evidence, not tests performed in Step 07 or adopted DIM/Profile rules. [A, §§D–F; C, §§D–F; D, §§D–F]

**Not supported:** verification of individual installed identities or inventories; a coherent deployed hardware/firmware/configuration combination; actual operational history; calibrated performance; successful command lifecycles; comprehensive whole-System health; military sensing equivalence; lossless transformation of a real station into CSAPI; or an end-to-end interoperable client. No qualifying actual-history set exists among the material acquired. An original example with a date remains an example. [A–D, §§F–H]

**Completeness is bounded, not universal.** These cases satisfy the research method's reference-configuration minimum, not every whole-System information need. None supplies a complete joined configuration/condition/measurement record. The eventual DIM must not be restricted to whatever these three products happen to publish, and their field names do not automatically become common model terms or user-interface categories. Source omissions are research limits, not negative facts about the equipment or reasons to delete information needs from the project's goal. [Step 01, §§2, 4, 6; original problem/outcome baseline, §§1–3]

### Limits that remain attached to the selection

| Case | Evidence retained for its selected use | Exclusions and unresolved issues carried forward |
| --- | --- | --- |
| **A** | Source-described `O-M-1PPSTON-CE` assembly, pinned firmware documentation, defined example fields and separate cloud examples. | No blanket `-CE-S` equivalence or matched deployment; no normalized Celsius value for unresolved `measure4`; no validated gas-concentration truth; no silently unified timing or synchronized examples; failed lab retrieval and conflicting PDF renderings are not positive evidence. [A, §§A, F] |
| **C** | External-probe/primary-battery reference, original eight-entry example, exact decoder and documented check methods. | No installed firmware/region inferred from a filename or synthetic status bytes; no LS/S31B features; preserve raw epoch and no-data context; no invented door hardware or real telemetry; upstream decoder unchanged. [C, §§A, E–F] |
| **D** | Documented CR1000X/first-generation ClimaVue pairing; historical program context; complete **logger-component** status example and field definitions. | No joined station history or proof sample came from that program; no verified runnable program/current download; retain extraction anomaly and independent editions; no invented support inventory, sensor-local voltage, ambient temperature or whole-station condition. [D, §§A, C, E–F] |
| **B — outside primary set** | Documentary V3 context, attributed historical lead and exact access/inspection limits. | G3 remains unverified; no automatic retry, response/record substitution or permission to rehost waveform data. [B, §§C, E–H] |

## 7. Preservation and reuse boundaries for the remaining step

**Step 08 still has to establish exactly what is preserved and reproducible.** An audit link, pinned repository identifier, local transcription, source byte capture and executed check are different artifacts. The existing checkers are research aids, not proof that every input is already bundled or that a corpus-wide byte-level freeze exists. Their input and license dependencies must remain explicit. [A, §E; C, §§B, E; D, §§B, E]

A's checker includes attributed README examples and a labeled comment-stripped derivative under the reported source license. C's harness requires the separately obtained pinned manufacturer decoder; its public availability does not establish unrestricted redistribution. D's checker requires a separately supplied original example or identified transcription, and its recorded transcription/normalization hashes do not identify downloaded publisher bytes. These are preservation facts to carry forward, not new legal conclusions. [A, §B and linked checker; C, §B and linked checker; D, §§B, E and linked checker]

**Do not fill the gaps while freezing.** Retain exact source locations, editions/commits, claim labels, allowed-use limits, known access/reuse conditions and small permitted artifacts where genuinely available. Any retained byte checksum must say precisely what bytes it covers. If a mutable or restricted source cannot be preserved lawfully or retrieved reliably, record that limitation rather than calling it frozen or upgrading an audit's evidence. No private device data, licensed manual archive, new station search or substitute candidate is authorized by this selection.

## 8. Completion and next one-prompt contract

**Step 07 is complete:** four audits compared under unchanged criteria; **A, C and D selected for documentary/reference-example uses**; B retained as CONDITIONAL and excluded from the primary set; source scopes, diversity shortfall, evidence scores and zero actual-history coverage preserved. No primary product re-audit, new dataset acquisition, Step 08 freeze, model adoption, Profile authoring or application change was performed. The original audits, checkers and donor corpus remain unchanged.

**Next separate “proceed”: Step 08 only — freeze the exact available evidence and write the handoff, then close this eight-step plan and STOP.** Produce `08_Frozen_Corpus_Manifest_and_Handoff.md` for the selected A/C/D set, retaining B's conditional finding and all preservation/access limits. Link exact sources and versions, distinguish originals/examples/transcriptions/derivatives/synthetic checks, inventory dependencies, and provide matched shared questions plus intentional source-specific differences. Preserve small files only when actually obtained and permitted. Do not claim unavailable bytes are archived, revive audits or begin another DIM subject. After Step 08, any use of this material for a new model or implementation task requires a separate owner decision.
