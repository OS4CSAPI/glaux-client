# Step 03 — Candidate A Evidence Audit: AirGradient Open Air Max

**Version:** 0.1 · 29 October 2026 (America/New_York)  
**Verdict:** **PASS — documented reference configuration and original published examples only; NOT SELECTED for the final corpus.** No real station record was retrieved. This verdict does not qualify a verified installation, matched hardware/firmware deployment, calibrated gas dataset or executable integration.  
**Authority:** [Controlled-corpus plan](../PLAN_DIM_Profile_V2_Controlled_Sensing_Equipment_Corpus_Qualification_v0.1_29OCT2026.md), Step 03 only; [unchanged Step 01 criteria](01_Eligibility_and_Evidence_Gates.md), blob `7592bc828a11977e6e308b929d9081da68bac416`; [Step 02 assignments](02_Discovery_and_Four_Audit_Slots.md).  
**Workspace:** `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`; pre-step commit `3e1b3710bc42bfb9a9c7a8a0dbb74015f386ee8b`.  
**Purpose:** Obtain defensible equipment evidence for the eventual Domain Information Model (DIM), OGC API – Connected Systems (CSAPI) Profile and common Resource Details experience. No model, Profile or application changes are made here.

## 1. What the audit established

We have a usable whole-equipment reference case, not just a brochure. The hardware project's description identifies the assembled gas-equipped **O-M-1PPSTON-CE**, its sensor modules, main board, cellular card, enclosure and solar/battery arrangement; it explicitly links the firmware project. The pinned firmware README supplies original cellular and Wi-Fi payload examples. Additional manufacturer documentation explains configuration, power behavior and reporting, and dated manufacturer support posts provide separate cloud-response examples. These are attributable sources about design and example representations, not proof that one fielded unit has every described property. [A01–A09]

The important gains are concrete: several reported quantities can come from one physical module; battery voltage is not remaining-capacity percentage; raw gas-electrode signals are not calculated gas concentrations; and reporting time can differ from measurement timing. Source labels and versions matter because the documents contain differences that cannot safely be flattened. The audit preserves those differences rather than repairing the manufacturer's text or inventing missing device state.

## A. Case boundary, applicability and comparability

**Qualifying case:** the manufacturer-documented, assembled **Open Air Max O-M-1PPSTON-CE gas-equipped reference configuration**, with its included solar supply and internal batteries. A01 describes two PMS5003 particulate sensors, Sunlight carbon-dioxide module, SGP41 volatile-organic-compound/nitrogen-oxide module, SHT40 temperature/humidity module, AlphaSense gas/analogue-to-digital module, cellular card, ESP32-C6 main board and enclosure. It distinguishes plug-in modules, directly attached particulate sensors and spare expansion connectors. The cloud, cellular carrier and dashboard are external information/communications services, not asserted physical constituents of the monitor. This is a documented assembly, not an installed inventory. [A01]

**The product suffix issue is bounded, not silently solved.** The current commercial page A04 names **O-M-1PPSTON-CE-S**. A01 names **O-M-1PPSTON-CE**, explicitly links that product page, describes the solar-equipped assembly and links the firmware repository. That supports a product-level relationship; it does not prove every suffix, board revision and firmware build is interchangeable. This audit therefore qualifies the explicitly documented `...-CE` reference assembly and its attributable examples. It does **not** certify a particular `...-CE-S` unit or invent a meaning for `-S`. The non-gas `O-M-1PPST-CE`, AirGradient ONE and ordinary Open Air are excluded as substitute evidence. [A01, A02, A04, A08]

**Version boundary:** hardware-description snapshot **89aacf5013fc0ffe4b988a2e3c5a227bce3c4983** and firmware-source snapshot **84e479a415d81151e7a81aea9a2f7449a15e98cc** are independently pinned. These are repository commits, not an asserted matched release pair or installed versions. The physical board revision and deployed firmware are unknown. The hardware README's BQ25798 charger name and the inspected firmware's BQ25672 class are not evidence of chip-level equivalence or incompatibility; no driver/schematic compatibility test was performed. [A01–A03]

**Comparability:** this is unattended environmental equipment with multiple sensing functions, power management, communications, configuration and remote reporting. Those are useful whole-System comparison questions. It is not a tactical seismic/acoustic detection system, and no military performance or tasking equivalence to TRSS/OmniSense is claimed.

## B. Source manifest and access standing

All sources were inspected on **29 October 2026, America/New_York**. Website dates below are capture dates unless a publication date is stated. Repository locators pin the inspected text; mutable pages remain mutable. The source IDs below are local to this audit, not additions to the frozen donor inventory.

| ID | Original source and exact locator | Version and evidence standing | What it supports; limit |
| --- | --- | --- | --- |
| **A01** | AirGradient hardware team / Open Air Foundation. [Open Air Max hardware README](https://github.com/Open-Air-Foundation/pcb-openair-max-main/blob/89aacf5013fc0ffe4b988a2e3c5a227bce3c4983/README.md), Overview, Design structure, Key components, Plug-in modules, Related repositories. | Commit `89aacf5…` (30 September 2026); README blob `6a915a09e7d34bd11b6b0dbe6698898d36976466`. **PRIMARY_DESIGN_OR_SPEC**. | Named whole assembly, internal roles and source-declared firmware relationship. README inspected; complete KiCad schematics, manufacturing outputs and module repositories not independently audited. |
| **A02** | AirGradient / Open Air Foundation. [Firmware README](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/README.md), Sensor Support, System Settings Portal, Transmission and both Example Payload Breakdown sections. | Commit `84e479a…` (18 September 2026); README blob `1322b58c7ed70ec0f4900bd557ec09fa65e03732`. **PRIMARY_DESIGN_OR_SPEC + PRIMARY_PUBLISHED_EXAMPLE**. | Field meanings and original examples. Not a captured device message; README alone is not a version-specific runtime contract. |
| **A03** | Same firmware commit: [Configuration.cpp](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/main/Configuration.cpp#L95-L135), [Sensor.cpp](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/main/Sensor.cpp#L1-L215), [MaxConfig.h](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/main/MaxConfig.h). | **PRIMARY_DESIGN_OR_SPEC**, source implementation, not execution evidence. Configuration first 135 lines; Sensor first 215 lines; MaxConfig inspected. | Declared/parsed configuration keys, conditional gas-sensor initialization, invalid-value constants and acquisition logic. No build, full serializer audit or actual configuration response. |
| **A04** | AirGradient. [Open Air Max product page](https://www.airgradient.com/professional/products/open-air-max/), Technical Data. | Captured 29 October 2026; model `O-M-1PPSTON-CE-S`. **PRIMARY_DESIGN_OR_SPEC**. | Commercial variant, component and power claims; not installed configuration or independent performance validation. |
| **A05** | AirGradient. [Device Overview and First Test](https://www.airgradient.com/documentation/kb/airgradient-open-air-max-device-overview), Device Overview and Connect the monitor; [Adding to the Dashboard](https://www.airgradient.com/documentation/kb/airgradient-open-air-max-adding-to-the-dashboard), Add the Monitor and Viewing Battery and Solar Data. | Captured 29 October 2026. **PRIMARY_DESIGN_OR_SPEC**. | Controls, connectivity, gas/non-gas choice and serial-number onboarding; no account or actual device identity obtained. |
| **A06** | AirGradient. [Power, Battery Backup, and Solar](https://www.airgradient.com/documentation/kb/airgradient-open-air-max-power-battery-backup-and-solar), USB-C Power, Battery Backup and Solar Power. | Captured 29 October 2026. **PRIMARY_DESIGN_OR_SPEC**. | Power paths and switch dependence; not observed switch position, charge state or runtime endurance. |
| **A07** | AirGradient. [Status LED and Reporting Intervals](https://www.airgradient.com/documentation/kb/airgradient-open-air-max-status-led-and-reporting-intervals), Status LED behavior, Reporting Interval and Power Modes. | Captured 29 October 2026; power-mode section expressly says firmware **0.7.0 onward**. **PRIMARY_DESIGN_OR_SPEC**. | Local diagnostic indications and documented timing modes; no reported current mode or fault log. Keep differences from A02 explicit. |
| **A08** | AirGradient. [What Data Is Included in an AirGradient Dashboard CSV Export?](https://www.airgradient.com/documentation/kb/kb-diy-air-quality-parameters), General Parameters and Open Air Max with/without NO2/O3. | Captured 29 October 2026. **PRIMARY_DESIGN_OR_SPEC**. | Model-scoped columns, raw/corrected distinctions and channel context. This is an export reference, not proof that every device payload or API response uses the same keys. |
| **A09** | Tai_AirGradient. [Max API — Working example with O3 and NO2 data](https://forum.airgradient.com/t/max-api-working-example-with-o-and-no-data/7345), manufacturer replies **#3, #5 and #6**, 15–17 September 2026. | **PRIMARY_PUBLISHED_EXAMPLE** for the two explicit response examples; **PRIMARY_DESIGN_OR_SPEC** for dated manufacturer support statements. | Product-specific cloud examples and dated gas-value caveats. Community assertions elsewhere in the thread are not used as first-party evidence. Placeholder locations/serials and null firmware are not a real installation. |
| **A10** | [Public lab endpoint](https://api.airgradient.com/public/api/v1/world/locations/194928/measures/current), explicitly offered in A09 #6. | **UNAVAILABLE_OR_UNVERIFIED** in this audit. Web retrieval failed; local direct retrieval failed at DNS resolution. | Manufacturer-attributed real-data lead only. Neither failure proves the endpoint is down, private or permanently unavailable. No response body, HTTP status, measurement or source-file checksum is claimed. |
| **A11** | AirGradient. [Open Air Max manual PDF](https://www.airgradient.com/documents/manuals/Open_Air_Max_Manual.pdf). | **UNAVAILABLE_OR_UNVERIFIED for edition-specific use**. | Tool text identified Version 3 / 19 May 2026, while screenshots of pages 1 and 6 showed 15 May 2025 and different text. Local byte retrieval failed. Do not combine these renderings into a verified edition. Excluded from positive gate evidence; HTML sources support the limited findings independently. |
| **A12** | AirGradient. [Open-Source Files & Builds Overview](https://www.airgradient.com/documentation/kb/kb-diy-the-airgradient-builds-overview), Firmware Repositories and Open Air Max; [pinned firmware LICENSE](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/LICENSE). | Captured 29 October 2026; repository license heading inspected. | Manufacturer provenance for firmware and CC BY-SA 4.0 source standing. Do not extend that permission automatically to the forum, website, PDF or live service data. |

**Access and reuse:** No credentials, account creation, device commands, firmware flashing or non-public records were used. The small checker below attributes the licensed README examples and labels the comment-stripped derivative. Other sources are linked and paraphrased, not bulk-republished. No raw upstream file-byte checksum is supplied: the GitHub connector supplied decoded text and blob identifiers, while direct local downloads failed. A blob identifier is not an independently computed SHA-256 digest.

## C. Eligibility gates

The following are analyst decisions under the unchanged Step 01 rules, not manufacturer certifications.

| Gate | Finding | Supporting evidence and scope |
| --- | --- | --- |
| **G1 — Bounded identifiable configuration** | **MET** | A01 explicitly describes an assembled `O-M-1PPSTON-CE`, including sensing, support equipment and solar/battery supply. Not a bare main board promoted into an invented station. The qualifying subject is the documented assembly, not an authenticated individual or every `-S` revision. |
| **G2 — Whole-System documentation** | **MET** | A01–A07 provide composition, power, communications, normal operation and configurable behavior. Some diagnostics are local LED/code descriptions, not machine-readable records. No requirement for every possible diagnostic is added. |
| **G3 — Usable native record/original example** | **MET** | A02 contains an actually inspected delimited sample with a defined field sequence and scaling. Its Wi-Fi example and A09 cloud examples provide additional evidence. Ambiguous fields are excluded from normalized quantitative use; enough defined fields remain for bounded research. This gate is met by published examples, not A10 or invented operating values. |
| **G4 — Traceable and bounded evidence** | **MET for the declared reference/example scope** | A01/A02 snapshots and exact example sections are pinned; A09 examples name the gas-equipped model. Unknown installed versions, suffix equivalence, timing differences, gas/AFE limitations and the PDF retrieval discrepancy remain explicit. No hardware/firmware release pairing or source-to-device join is claimed. These exclusions block broader runtime claims rather than changing the gate. |

**Why PASS rather than CONDITIONAL:** Step 01 expressly admits a documented complete reference configuration with original examples and permits unknown deployed firmware when version-dependent claims are withheld. Those minimum conditions are met without the failed lab retrieval or disputed PDF. An actual installed-state or executable-integration case is **not** established and cannot inherit this PASS. The final corpus still depends on the other audits and Step 07.

## D. Common questions and actual coverage

| Question | Source-backed answer | Missing information / consequence |
| --- | --- | --- |
| **Q1 — What exactly is the case?** | Gas-equipped assembled reference model identified in A01/A02/A09; commercial `-S` spelling preserved separately in A04. | No authenticated unit, installed board revision, serial-to-hardware join or deployed firmware. |
| **Q2 — What is included?** | A01 names boards, physical modules, two particulate sensors, required power arrangement, enclosure and spare connectors. | A02 firmware support for alternative particulate sensors is not proof those alternatives are fitted to this reference build. No per-part serial inventory. |
| **Q3 — What can be configured/commanded?** | A02 describes selecting cellular/Wi-Fi, network settings and reporting destination. A03 parses such keys as `co2CalibrationRequested`, `abcDays` and `ledBarTestRequested`. | No original actual configuration snapshot, acknowledgement sequence or successful calibration/test execution was obtained. Code support is not active state. |
| **Q4 — How does it operate/report condition?** | A02 examples contain battery/panel voltages; A06 explains power-path/switch behavior; A07 describes diagnostics and power-dependent timing. | No verified charge percentage, current power mode, switch position, diagnostic history or comprehensive remotely reported health object. |
| **Q5 — What can be inspected?** | Device-side cellular and annotated Wi-Fi examples (A02), cloud-response examples (A09), source configuration definitions (A03), export definitions (A08). | Measurement examples: available. Power/status-related examples: voltages available, diagnostic records absent. Actual configuration records: absent. Actual observations/history: not obtained. |
| **Q6 — Do documents and records describe the same scope?** | A01 explicitly links the firmware repository; A02 gas fields and A09 model values explicitly identify `O-M-1PPSTON-CE`. | This supports product/example attribution, not simultaneous readings from a known installed assembly or one matched release. No silent cross-source state merge. |
| **Q7 — Is it reproducible?** | A01/A02 commits, exact sections and checker preserve the example provenance and local format exercise. | Websites and temporary lab access can change. No full archive, complete source packet or independent raw-file byte capture. |
| **Q8 — Which similarities/differences matter?** | Multiple quantities per component, alternative transports, design versus configuration, power signals and raw versus calculated values are inspectable. | Their usefulness for a future common Details view is an analyst inference, not a DIM adoption, CSAPI mapping or rendered-client test. |

## E. Small original example check

At **23:51 EDT on 29 October 2026**, Python checked the two A02 payload examples, transcribed from the inspected pinned README text. The adjacent [offline checker](03_AirGradient_Example_Check.py) preserves those example strings, source attribution and exact transformations. It does not access the network or execute manufacturer firmware.

| Check | Result | What it does not prove |
| --- | --- | --- |
| Cellular example token/shape check | **52 integer tokens:** one interval of **180 seconds**, then **three groups of 17 values** under A02's gas-equipped example sequence. | Not a complete decoder, current serializer contract, actual observation series or absolute time reconstruction. |
| First cellular group's documented arithmetic | Temperature `285 / 10 = 28.5`; battery `1124 / 100 = 11.24 V`; panel `14 / 100 = 0.14 V`. | These are calculations on illustrative values, not new measurements or verified sensor accuracy. |
| Wi-Fi example, unchanged | Strict JSON parser **rejects** the source's `//` explanatory comments. | Not evidence of faulty device output: this is an annotated documentation example. |
| Wi-Fi example, comments removed only | Derived string parses into **17 keys**, retaining `volt=11.24`, `light=1.4`, and all original values. | The derivative is **SYNTHETIC_OR_DERIVED**, not raw captured telemetry or silently repaired source evidence. |
| Cross-example comparison | Cellular panel arithmetic yields **0.14 V**, while Wi-Fi `light` is **1.4 V**. Both are retained. | The examples are not established as synchronized records; neither value is corrected or treated as proof the other is erroneous. |

**Selected field-level meanings:**

| Native field or position | Source-defined meaning | Interpretation limit |
| --- | --- | --- |
| Cellular `interval` | Seconds between the documented example measurement sets (A02). | No absolute timestamp or authenticated subject in this body; do not assign a date or identify a device from it. |
| `rco2`; `atmp`; `rhum` | Carbon dioxide in ppm, temperature in degrees Celsius and relative humidity in percent in A02's example context. | Supported example meanings, not active calibration, ambient representativeness or a device identity. |
| `pm25` in device example; `pm02` in cloud example | Respective source keys for the PM2.5 quantity (A02/A09). | Similar meaning does not establish a tested producer-to-cloud crosswalk or equal values; keep both native keys and source paths. |
| `volt`; `light` | Battery and solar-panel voltage in the Wi-Fi example (A02). | Voltage is not remaining energy, charge percentage, switch position or overall readiness. |
| `tvocRaw`; `noxRaw` | Raw channel signals under A02's labels. | Not interchangeable with processed indices or NO2 concentration. A08 is a separate export reference; no automatic API-type conversion. |
| `measure0`–`measure3` | O3/NO2 working and auxiliary electrode signals; millivolt descriptions in A02/A08. | Not calibrated concentration in ppb. |
| `measure4` | A02 calls it AFE temperature but labels the cellular unit **mV**; A08 calls it a monitor-reported value without resolving the unit. | Preserve native label/value; **do not normalize to degrees Celsius** or claim a temperature conversion. |
| `batteryVoltage`; `panelVoltage` | Separately named power fields in A09's cloud example, with quoted numeric strings. | Preserve source types; these are not the same sampled values as A02. |
| `model`; `firmwareVersion`; `timestamp` | A09 includes model attribution, null firmware and illustrative timestamps. | Example metadata is not actual hardware identification, installed firmware or evidence of an operational event. |

## F. Open issues and deliberate exclusions

| Issue | Evidence | Constraint on later use |
| --- | --- | --- |
| **Version-dependent timing** | A02 says hourly configuration/update checks; A07 says 90 minutes in standard mode from 0.7.0 and daily in saving modes. A03 has constants and comments, not an executed schedule test. | Preserve source-specific claims. No universal interval or active-mode claim; no silent reconciliation of code, README and guide. |
| **Gas-value validity** | In dated A09 replies, the manufacturer warned about gas values without calibration and advised ignoring O3 at that time. | Do not use the illustrative gas concentrations as validated environmental truth. No later resolution was established in this bounded audit. This does not remove the usefulness of raw/derived meaning distinctions. |
| **AFE unit and transport distinctions** | A02/A08 leave `measure4` unit interpretation unresolved; the two A02 examples differ in panel value and A09 uses different keys/types. | No guessed conversion, synchronized join or universal schema. Defined unaffected fields remain usable. |
| **Hardware/firmware and model suffix** | Independent source snapshots, `...-CE` versus `...-CE-S`, and untested implementation details. | No release compatibility, exact chip equivalence, installed-module inventory or `-S` identity policy. |
| **Actual record availability** | A10 retrieval failed in this environment. | History score stays zero; do not say the API requires authentication, the device is offline or public data does not exist. |
| **Manual edition provenance** | A11 parsed text and screenshots disagree; direct download failed. | PDF excluded from positive evidence until a single byte-identifiable edition can be verified. Do not quietly substitute its newer parsed text for older rendered pages. |

## G. Six evidence scores — no aggregate

These rate the evidence **obtained in this audit**, not the product or its performance. Their meaning is fixed by Step 01.

| Dimension | Score | Evidence and reason | Ceiling |
| --- | ---: | --- | --- |
| Whole-System component/architecture depth | **3** | A01 supplies a pinned, assembly-level description and explicit constituent/module/power relationships. | Source-described design, not an independently inspected physical build or complete schematic audit. |
| Capability/configuration depth | **2** | A02/A03 explain supported controls and source configuration fields. | No actual or complete original configuration-response record obtained. |
| Operational condition/power/diagnostic depth | **2** | A02/A06/A07 explain voltage fields, power paths, local diagnostic codes and modes. | Missing actual diagnostic/status history and current operating-state evidence. |
| Machine-readable source/communication depth | **2** | A02's usable delimited example and documented fields; A09 provides complementary original cloud examples. | No proven coherent, versioned end-to-end interface; field/version differences remain. |
| Actual attributed observations/history | **0** | No real device record was obtained; A10 is only a lead. | Manufacturer examples are not counted as real history. |
| Reproducibility/version/rights | **2** | Pinned source snapshots, exact locators, dated support examples and a reproducible licensed small check. | Mutable web documentation, unknown deployed versions and no full byte-level evidence freeze. |

## H. Verdict, allowed uses and next step

**PASS, with scope stated rather than hidden.** The reference assembly and original examples meet the four minimum gates. They can support later source-based comparison of equipment structure, source-qualified quantities, power reporting, possible configuration and different representation paths. They cannot establish actual installed state, live health, calibration accuracy, successful commands, a validated decoder, standards conformance or cross-vendor interoperability. Candidate A is eligible for Step 07 comparison, **not selected now**.

The most useful new lesson is that a future common Details view must preserve **which component or description a value concerns, whether it is raw or calculated, which representation supplied it, and what its version/time evidence permits**. AirGradient gives us concrete material with which to challenge those questions. That is research value, not a newly adopted DIM rule.

**Step 03 is complete.** No other candidate was audited; no criteria were relaxed; the original donor inventory, closed donor plans, candidate DIM v0.2 and separate Glaux application branch remain untouched. The small example check is research evidence, not client implementation or the Step 08 frozen corpus.

**Next separate “proceed”: Step 04 only — Raspberry Shake & Boom evidence audit**, using the same gates, questions, scoring anchors and honest access limits. Do not repeat Candidate A indefinitely, select the corpus, begin a new DIM subject or change Glaux automatically.
