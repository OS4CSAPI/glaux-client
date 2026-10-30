# Step 06 — Candidate D Evidence Audit: CR1000X + First-Generation ClimaVue 50

**Version:** 0.1 · 30 October 2026 (America/New_York)  
**Standing:** **PASS for a bounded, manufacturer-documented reference measurement arrangement and published examples only; NOT SELECTED.** No installed station, weather-history dataset, working program or deployed firmware combination was verified.  
**Workspace:** `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`; pre-step HEAD `0a4230e3ab7397ea96bcaf823db5b4ff7f680db5`.  
**Authority:** [Controlled-corpus plan](../PLAN_DIM_Profile_V2_Controlled_Sensing_Equipment_Corpus_Qualification_v0.1_29OCT2026.md), Step 06 only; unchanged [Step 01 gates and template](01_Eligibility_and_Evidence_Gates.md), blob `7592bc828a11977e6e308b929d9081da68bac416`; [Step 02 assignments](02_Discovery_and_Four_Audit_Slots.md).  
**Purpose:** Evidence for the eventual Domain Information Model (DIM), separate OGC API – Connected Systems (CSAPI) Profile and common Details experience—not authoring or validating those products in this step.

## A. Case boundary and comparability

The case is the **CR1000X acquisition/processing/logger with one first-generation ClimaVue 50 weather-sensor assembly and its sensor cable**, not a bare logger, CR1000Xe, ClimaVue 50 G2, or an authenticated installed station. Campbell explicitly publishes a program for this pairing. Its historical example selects terminal C1, sensor address 0 and a 60-second scan. Those are example settings, not discovered operating state. [D03, D04]

The necessary support context is documented rather than invented: external nominal 12 Vdc power for the logger, continuous power to the sensor, signal/ground/shield connections, protected logger/power housing and a supported sensor mounting arrangement. The logger manufacturer describes external power and enclosure options; the sensor manual describes wiring and mounting. **No specific battery pack, charger, solar panel, enclosure SKU, cable length, site or remote modem has been selected or claimed installed.** The reference is sufficiently bounded for the Step 01 measurement-configuration question, not a turnkey field-station bill of materials or an autonomy calculation. [D01, D02, D05]

This offers a modular environmental-monitoring comparison to the original unattended ground sensing problem. It does not establish military equivalence or surveillance capability. The research advantage is separating the attached sensing assembly, logger processing and logger self-status without merging them into a single undifferentiated sensor.

## B. Source manifest and access standing

All sources below were inspected **30 October 2026, America/New_York**. Dates describe publications or access, not installed firmware. **PRIMARY_DESIGN_OR_SPEC** applies to documentation; **PRIMARY_PUBLISHED_EXAMPLE** applies to the explicit examples. Actual station state and uninspected release applicability remain **UNAVAILABLE_OR_UNVERIFIED**. No item is promoted to **REAL_RECORDED** merely because an example contains a timestamp.

| ID | First-party source and locator | Version/access and evidence ceiling |
| --- | --- | --- |
| **D01** | Campbell Scientific. [“ClimaVue 50: Compact Digital Weather Sensor”](https://us.campbellsci.com/climavue-50), Overview, Detailed Description, Specifications, Downloads and FAQs. | Mutable HTML read. First-generation product identified; current retirement label is not a reason to substitute G2. Product claims, not installed equipment. |
| **D02** | Campbell Scientific. [*ClimaVue 50 Compact Digital Weather Sensor: Product Manual*](https://s.campbellsci.com/documents/us/manuals/climavue50.pdf), revision **08/2024**; §§5–8; Table 7-1, printed p.13; Table 8-1, pp.21–23. | Parsed text inspected. Cover and relevant tables visually checked on PDF pages **1, 17, 25 and 27** (1-based). Source specification only; not a live response or adopted model. |
| **D03** | Campbell Scientific. [*ClimaVUE 50 Compact Digital Weather Sensor*](https://s.campbellsci.com/documents/eu/manuals/climavue50.pdf), revision **9/19 as identified in extracted text**, Appendix B, **B-1–B-3**, “CR1000X Program Measuring the ClimaVUE 50.” | Complete three-page program text inspected through browser extraction. Cover/program screenshots failed with cache-miss errors; original bytes were not obtained. Historical published configuration/processing example, not a visually verified transcription, compiled program or the 2021 download. |
| **D04** | Campbell Scientific. [“ClimaVue 50 Example Program”](https://www.campbellsci.com/resources/software/climavue50-example-program), download description. | **v1, July 8, 2021, 3 KB**; page explicitly requires login. Description inspected; packaged program **not downloaded**. No credentials used or access restriction bypassed. Do not assert equality with D03. |
| **D05** | Campbell Scientific. [“CR1000X: Measurement and Control Datalogger”](https://us.campbellsci.com/cr1000x), Communications, Enclosures, Power and Specifications. | Mutable HTML read for the named logger. Supports power/storage/communication context, not a chosen field installation. No CR1000Xe-specific capability imported. |
| **D06** | Campbell Scientific. [“CR1000X Status Table”](https://help.campbellsci.com/crbasic/cr1000x/Content/Instructions/StatusTable.htm), Battery, LithiumBattery, PanelTemp, SW12Volts, CommsMemFree, WatchdogErrors and program/version entries. | Field definitions inspected. Describes meanings and update/reset conditions, not values from this reference station. |
| **D07** | Campbell Scientific. [“Status — MQTT API”](https://help.campbellsci.com/datalogger-api/mqtt/status.html), **CR1000X Example**. | Footer **2026-09-21 (ced60094)**, not asserted as a Git commit or firmware version. Entire example retrieved as browser text and locally transcribed for checking. Logger-level example, not ClimaVue weather data. |
| **D08** | Campbell Scientific. [“JSON Data Formats — MQTT API”](https://help.campbellsci.com/datalogger-api/mqtt/json_data_formats.html), GEOJSON Output Format. | Same displayed footer. Confirms positional correspondence of names and values. Its OS-version note concerns formatting; it does not identify D07's running firmware. |
| **D09** | Campbell Scientific. [“Data Logger MQTT API”](https://help.campbellsci.com/datalogger-api/mqtt/index.html), introduction and warning. | Same displayed footer. Publisher expressly requires validation against the specific firmware/environment. No production compatibility claim follows from this audit. |

**Acquisition limits:** Direct runtime requests for D02, D03 and D07 failed DNS resolution. Browser text remained available; D02 screenshots succeeded while D03 screenshots did not. No original-source byte checksum is claimed. Other regional manual editions were located but are not substituted into the selected evidence. This is not proof that source files are unavailable elsewhere.

**Rights:** Manuals carry publisher copyright. No redistribution license for the complete manuals, packaged program or status-example page was established in this bounded review. They are linked, not republished in the repository. The checked-in helper is original audit code and requires the example to be supplied separately; this report does not grant permission for later rehosting.

## C. Eligibility gates

| Gate | Result | Basis and retained limit |
| --- | --- | --- |
| **G1 — Bounded sensing configuration** | **MET** | Named logger-plus-sensor pairing and necessary power/connection/mounting context are manufacturer-described. This is not an arbitrary selection of supported peripherals. Individual identity and exact support-hardware SKUs are not asserted. [D01–D05; §A] |
| **G2 — Whole-System documentation** | **MET** | Sensing assembly, acquisition, processing, power and communication roles can be explained at reference-design level. Actual inventory, calibration, site configuration and total power consumption remain unknown. [D01–D06] |
| **G3 — Usable original example** | **MET, with subject scope explicit** | D07 is a complete original **CR1000X-component** status message, with field meanings from D06 and positional rules from D08. D03 additionally documents the named pairing's configuration/processing. Neither is asserted to be a record generated by the other. No actual ClimaVue measurement series was obtained. |
| **G4 — Traceable, reproducible boundaries** | **MET for the declared documentary scope** | Editions, exact locators, access failures, transcript method, helper and unresolved joins are recorded. Claims requiring the uninspected 2021 package or a particular deployed firmware are excluded. Original-byte freezing and production validation are not complete. |

**Why this is not a hidden station-data join:** The eligible case includes an explicitly identified logger component whose published status example is useful in its own right. The paired sensor is independently established by manufacturer documentation and a pairing-specific example—not inferred from that status message. Step 01 does not require every available example to describe the same authenticated installation. An experiment requiring simultaneous weather, status and configuration records would **not** be supported by this evidence.

## D. Shared questions and coverage

| Question | Finding and remaining gap |
| --- | --- |
| **Q1 — What is this?** | A documented reference arrangement. D07's illustrative logger identifier does not authenticate a unit; its coordinates do not establish a deployment. [D01, D03, D07] |
| **Q2 — What is included?** | One named attached weather assembly, cable and logger, with required support context in §A. The fourteen R7 response quantities are not fourteen independently identified physical child Systems. [D02, D03] |
| **Q3 — Configurable or commanded?** | Historical program/settings and current download description are available at different evidence levels. No command was sent, acknowledged or verified on equipment. [D03, D04] |
| **Q4 — Operation and condition?** | Logger voltage, backup battery, panel temperature, port states and diagnostic counters have distinct meanings. Sensor-level verification is documented separately. No actual condition history exists in this packet. [D02, D06] |
| **Q5 — Inspectable information?** | **Configuration:** historical program text, not the 2021 package. **Status:** complete original logger example. **Weather measurements:** field definitions, but no attributable station series. [D02–D04, D07] |
| **Q6 — Same scope?** | The pairing is established, but the 2019 program, 2024 manual and 2026 API documentation are not a verified release combination. D07 is not output from D03. [D03, D04, D07–D09] |
| **Q7 — Repeatable?** | Exact source sections and the local-check method are supplied. Repeatability of semantic checks is stronger than byte-level source preservation here; access and reuse limits remain. [§B, §E] |
| **Q8 — Differences to preserve?** | Logger versus sensor subject, reported versus transformed values, carried-forward versus newly measured values, and example versus installed state. These are research implications, not adopted DIM classes or Profile rules. |

## E. Small native-example check

D07's full JSON example was transcribed from inspected browser text with whitespace reformatted; names, ordering, JSON types and values were retained. **This is an example transcription, not a captured MQTT packet.** No raw manufacturer page/program is bundled. The original [offline checker](06_Campbell_Example_Check.py) accepts a separately supplied example file and makes no network or hardware calls.

**Executed results:** JSON parsed; **31 unique field names matched 31 values**, comprising **18 numbers, three strings and ten Booleans**. The example timestamp `2025-06-04T18:29:23.271Z` parsed with its explicit UTC suffix. These checks establish syntax, types and positional pairing only; neither event authenticity nor clock accuracy was tested.

The local transcription's SHA-256 was `69068d1a06c3f949788a3f69f9296d1999f31c4928370da1084905d0556dc878`. Its canonical JSON SHA-256 was `ef93d1fc12a09fe04a4d06da743b07a8694cd6bc74af3ce612110a8d4e15c8a8` using sorted keys, compact separators and UTF-8. **These identify the locally created transcript/normalization, not downloaded source bytes.**

| Native key / value kind | Source meaning and permitted interpretation | Do not infer |
| --- | --- | --- |
| `Battery` — illustrative **13.2368** | Logger system-supply voltage, Vdc. [D06, D07] | Remaining capacity, sensor-local voltage or installed battery model. |
| `LithiumBattery` — illustrative **3.70477** | Internal lithium-battery voltage. [D06, D07] | Same power source as the external supply. |
| `PanelTemp` — illustrative **25.91098** | Logger wiring-panel temperature, °C. [D06, D07] | ClimaVue air temperature. |
| `SW12Volts(1/2)` — Boolean | Switched-output state. [D06, D07] | Measured voltage merely because the key contains “Volts.” |
| `CommsMemFree` — string | Structured memory-allocation summary. [D06, D07] | One scalar free-memory measurement. |
| `WatchdogErrors` — counter | Resettable program-associated diagnostic count. [D06] | Lifetime absence of faults or whole-station readiness from zero. |

The helper was also checked against a deliberately shortened value array; it rejected the mismatch rather than silently truncating a positional pairing. That is an **analyst-created negative test**, not another manufacturer record. CRBasic was neither compiled nor executed, and no numerical weather conversion was run.

## F. Interpretation hazards and unresolved points

**Processing before transport matters.** D04 says its example adjusts pressure for an assumed site elevation and substitutes previous valid wind values for invalid ones. D03's extracted program text also exposes unit conversions and interval-based outputs. Thus a plausible-looking reported value can depend on a program, a site parameter or previous data. The future fidelity test must examine that history rather than presume all values are fresh, direct sensor readings. This is an inference from the documented processing, not a finding about a fielded station.

**Preserve source editions and extraction uncertainty.** D03 extraction contains the literal `Cont SeaLevelAdj=15.29091`. With screenshots and original bytes unavailable, this audit does not decide whether that is a publication typo or extraction defect, silently replace it, or call the program runnable. The 2021 download remains a separate, uninspected artifact. No logger operating-system or sensor hardware/firmware revision has been established for an installed pair.

**Sensor-level diagnostics are not logger-level diagnostics.** D02 Table 8-1 lists sensor verification outputs including version, watchdog errors and uptime. Those are not supplied by D07's logger status. Likewise, polling can return previously reported values; receipt time alone is insufficient evidence of a new physical measurement. No sensor verification response was acquired.

**No numerical completeness or availability inflation:** No authenticated ClimaVue weather record, joined configuration/status history, calibration result, field installation inventory or public station dataset was acquired. A website's examples are not a live service test. **Actual observations/history remains zero.** The availability of named configuration interfaces does not prove enabled or authorized control.

## G. Six evidence-depth scores — no aggregate

| Dimension | Score | Evidence and ceiling |
| --- | ---: | --- |
| Whole-System component/architecture depth | **2** | Documented measurement arrangement and support roles; no complete installed bill of materials or schematic audit. [D01–D05] |
| Capability/configuration depth | **2** | Historical program text and supported settings; current package uninspected, extraction anomaly unresolved and no compilation. [D02–D04] |
| Operational condition/power/diagnostic depth | **3 at logger-component scope** | Rich field definitions plus a complete original typed status example; sensor diagnostics and whole-station condition remain unmeasured. This score does not imply station-wide coverage. [D06, D07] |
| Machine-readable source/communication depth | **2** | Complete original message, field definitions and executed format check; no coherent tested end-to-end station interface. [D06–D09] |
| Actual attributed observations/history | **0** | No qualifying station observations or telemetry acquired. Original examples are excluded from this score. |
| Reproducibility/version/rights | **2** | Editions/locators, public example, helper and explicit access/rights limits. No original-byte freeze or deployed-version validation. [§B, §E] |

## H. Verdict and next step

**PASS for the bounded reference/example evidence case, not an accepted final-corpus member.** It supports later comparison of modular equipment, logger-versus-sensor status and documented processing. It cannot support a claim that a whole installed station has been faithfully transformed through CSAPI or that these source editions form a validated operational stack.

**Step 06 is complete.** Earlier audits and criteria are unchanged. No source-inventory ledger, candidate DIM v0.2, Profile rule, application code or deployment changed. Source preservation at final-corpus level remains Step 08.

**Next separate “proceed”: Step 07 only — compare the four completed audits and decide whether a defensible two-to-three-system controlled set exists.** Preserve each verdict, evidence scope and missing actual-data coverage. Do not reopen audits, silently relax gates, select a new candidate, begin a DIM subject or change Glaux automatically.
