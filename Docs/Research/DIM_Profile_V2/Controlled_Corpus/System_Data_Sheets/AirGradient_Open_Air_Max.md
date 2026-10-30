# System Data Sheet A — AirGradient Open Air Max

**Version 0.1 · 30 October 2026 · America/New_York**  
**Reference case:** gas-equipped `O-M-1PPSTON-CE` assembly. **Not an installed unit.**  
**Purpose:** Itemized working information for later Domain Information Model (DIM) / OGC API – Connected Systems (CSAPI) work. This is a research data sheet, not a manufacturer-issued datasheet or adopted model.  
**Basis:** [A audit](../03_Candidate_A_Evidence_Audit.md), [selection](../07_Corpus_Qualification_Decision.md), [frozen handoff](../08_Frozen_Corpus_Manifest_and_Handoff.md), at repository revision `315034c25326dc4a08ecc0629f8bf3a933abe092`. Existing audit findings are unchanged.

## How to use this sheet

**Design** = `PRIMARY_DESIGN_OR_SPEC`; **Example** = `PRIMARY_PUBLISHED_EXAMPLE`; **Derived** = `SYNTHETIC_OR_DERIVED`; **Unknown** = `UNAVAILABLE_OR_UNVERIFIED`. These expand the existing evidence labels, not new confidence scores. All numbers below are design statements, published examples, or explicitly identified arithmetic; **none is acquired real telemetry**. Each row is a separately referenceable input; source IDs resolve in §8.

The sheet consolidates the audited equipment facts and enumerates every field of the pinned device examples and the two manufacturer cloud examples. It does not assert exhaustive extraction of firmware, schematics, dashboard exports or every manual paragraph. Sources A02/A06/A07/A08/A09 were reread for this itemization; new extraction detail is not retroactively attributed to the earlier audit. Fields with uncertain meaning are retained but withheld from quantitative interpretation.

## 1. Identity, physical arrangement and capabilities

| ID | Native item / subject | Information available | Evidence / exact source | Limit |
| --- | --- | --- | --- | --- |
| A-I01 | Model | O-M-1PPSTON-CE; gas-equipped assembled reference | Design; A01 Overview | Commercial -CE-S suffix is not declared equivalent. |
| A-I02 | Commercial model spelling | O-M-1PPSTON-CE-S | Design; A audit §A / A04 | Separate product-level spelling; no meaning assigned to -S. |
| A-I03 | Hardware description version | 89aacf5013fc0ffe4b988a2e3c5a227bce3c4983 | Design; A01 | Source revision, not installed hardware revision. |
| A-I04 | Firmware source version | 84e479a415d81151e7a81aea9a2f7449a15e98cc | Design; A02 | Independent snapshot; not a verified hardware/firmware release pair. |
| A-I05 | Main board | ESP32-C6; sensing, power and communication interfaces | Design; A01 Design structure / Key components | Description only; full schematic not independently audited. |
| A-I06 | Particulate sensors | 2 × Plantower PMS5003; PM1 / PM2 connections | Design; A01 Plug-in modules | Two physical units, not one unit for every output quantity. |
| A-I07 | CO2 module | SenseAir Sunlight; SUNX board; UART; documented range 0–5,000 ppm | Design; A01 Overview / Plug-in modules | Capability, not a measurement or calibration record. |
| A-I08 | TVOC / NOx module | Sensirion SGP41; I²C | Design; A01 Plug-in modules | Outputs are not separate physical module identities. |
| A-I09 | Temperature / humidity module | Sensirion SHT40 / SHT4x; I²C | Design; A01 Plug-in modules | No individual sensor serial or installed alternative established. |
| A-I10 | NO2 / O3 assembly | AlphaSense ADC module; NO2 A43F and O3 A431 as named in README | Design; A01 Overview / Plug-in modules | Manufacturer naming retained; no calibration validation. |
| A-I11 | Cellular card | CE card; LTE Cat 1; CE1 connection | Design; A01 Plug-in modules | Not a demonstrated cellular session. |
| A-I12 | Wi-Fi | 2.4 GHz IEEE 802.11 b/g/n | Design; A01 Overview | Supported connection, not selected mode. |
| A-I13 | Housing / mounting | Weatherproof UV-resistant ASA enclosure; wall or pole mounting | Design; A01 Overview | No site or installed mount identified. |
| A-I14 | Expansion | I2C3 and IO1 spare connectors | Design; A01 Plug-in modules | Spare ports do not establish attached equipment. |
| A-I15 | External services | Carrier, cloud and dashboard are reporting dependencies | A audit §A; research boundary | Not asserted physical constituents. |
| A-I16 | Installed identity | Not obtained | Unknown; A audit §§A/D | No authenticated serial-to-hardware link or deployed revision. |

## 2. Power, operation and configuration

All settings are **supported choices or documentation defaults**, not a captured current configuration. No command was sent. Pin references to the named source; the README and later guide do not form a verified runtime contract.

| ID | Item | Fact / supported setting | Evidence / source | Interpretation boundary |
| --- | --- | --- | --- | --- |
| A-P01 | Solar panel | 10 W, 18 V included panel | Design; A01 Overview; A06 Solar Power | Rated design, not measured output. |
| A-P02 | Battery arrangement | Three 3,500 mAh 18650 Li-ion cells in series (3S) | Design; A01 Overview | Per-cell ratings; do not sum into an invented pack-capacity value. |
| A-P03 | USB-C supply | Can operate device with battery switch OFF | Design; A06 USB-C Power | No observed switch position. |
| A-P04 | Charging / backup | Battery switch ON is required for recharge and battery backup | Design; A06 USB-C Power / Battery Backup | No observed charging state. |
| A-P05 | Solar operation | Included panel connects to solar input; battery switch ON | Design; A06 Solar Power | No actual deployment or irradiance record. |
| A-P06 | Battery servicing | Replaceable cells; unprotected 18650 format specified | Design; A06 Batteries | No individual maintenance event. |
| A-P07 | Power electronics | Hardware README: BQ25798; inspected firmware class: BQ25672 | Design; A01 Key components; A audit §A/A03 | No assumed chip equivalence or demonstrated incompatibility. |
| A-C01 | System Settings Portal | Boot-button hold ≥5 s at first boot; settings interface | Design; A02 System Settings Portal | Not an executed session. |
| A-C02 | Network choice | Cellular or Wi-Fi; README default Cellular | Design; A02 Transmission | Default is not active mode. |
| A-C03 | Cellular APN | Configurable in portal | Design; A02 System Settings Portal | No APN value supplied. |
| A-C04 | Wi-Fi credentials | Configurable in portal | Design; A02 System Settings Portal | No credentials collected or published. |
| A-C05 | HTTP destination | Domain / URL configurable in portal | Design; A02 System Settings Portal | No selected destination captured. |
| A-C06 | co2CalibrationRequested | Boolean parsed by configuration implementation | Design; A03 Configuration.cpp lines 95–135 | Request support ≠ completed calibration. |
| A-C07 | abcDays | Integer configuration field parsed by implementation | Design; A03 Configuration.cpp lines 95–135 | No actual setting; no invented default. |
| A-C08 | ledBarTestRequested | Boolean parsed by configuration implementation | Design; A03 Configuration.cpp lines 95–135 | Not evidence a test was performed. |
| A-C09 | Configuration / firmware checks | README says every hour; configuration applied next wake cycle | Design; A02 Fetch Configuration / FOTA | A07 instead gives 90-minute/daily checks; preserve distinction. |
| A-C10 | Cellular transmission | Comma-separated samples over HTTP or MQTT; nominal 3-minute samples / 9-minute batches | Design; A02 Cellular | Timing is source-specific; not an observed schedule. |
| A-C11 | Cellular caching | Failed batches retained until a later transmission; volatile across power loss | Design; A02 Handling Data Loss | Not a delivery guarantee or measured retention depth. |
| A-C12 | Wi-Fi transmission | HTTP JSON; nominal one sample each 3 minutes; README says no retry cache | Design; A02 WiFi | Do not import cellular caching into Wi-Fi. |
| A-C13 | PM firmware alternatives | Each UART probes PMS5003 then SPS30; mixed pair supported in code description | Design; A02 Sensor Support | Reference assembly still uses A01 PMS5003 pair; alternatives not installed facts. |

### Power-mode guide (A07; explicitly firmware 0.7.0 onward)

| ID | Source scenario | Source condition | Link | Measure / transmit / config-update check |
| --- | --- | --- | --- | --- |
| A-M01 | Standard | USB or >10 V | Cellular | 3 min / 9 min / 90 min |
| A-M02 | Standard | USB or >10 V | Wi-Fi | 3 min / 3 min / 90 min |
| A-M03 | Power saving | Battery 9.5–9.9 V | Cellular | 30 min / 90 min / daily |
| A-M04 | Deep power saving | Battery <9.5 V | Cellular | 60 min / 180 min / daily |

These are Design inputs, not evidence of the example's firmware or active mode. No missing boundary rule, Wi-Fi saving mode or tie at 10 V is invented. The one-hour README check interval remains separate.

### Local indicator meanings (complete A02 first-boot list)

| ID | Pattern | Source meaning (paraphrased) | Evidence |
| --- | --- | --- | --- |
| A-L01 | On immediately | Power-on indication | Design; A02 Led indicator item 1 |
| A-L02 | Fast ×2 | CE-card initialization / network attempt | Design; A02 item 2 |
| A-L03 | Fast ×3 | Network connection succeeded | Design; A02 item 3 |
| A-L04 | Fast ×4 | First measurement post succeeded | Design; A02 item 4 |
| A-L05 | Slow ×2 | At least one sensor initialization failed | Design; A02 item 5 |
| A-L06 | Slow ×3 | Post failed | Design; A02 item 6 |
| A-L07 | Slow ×4 | Post failed due to server issue | Design; A02 item 7 |
| A-L08 | Slow ×5 | Connection check failed after unsuccessful post | Design; A02 item 8 |
| A-L09 | Slow ×6 | Stopped after three network-related post attempts | Design; A02 item 9 |
| A-L10 | Slow ×10 | Connection failed before retry | Design; A02 item 10 |
| A-L11 | Fast ×5 | Settings-portal start/stop trigger | Design; A02 item 11 |
| A-L12 | Continuous fast blinking | Settings portal active | Design; A02 item 12 |
| A-L13 | Wake cycle: off / slow ×2 / slow ×3 | No error indication / sensor init failure / post failure | Design; A02 Every wake-up cycle |

No LED observation or remote diagnostic history was acquired. A07's shorter guide uses solid blue at startup and LED-off for its normal phase; its summaries do not replace A02's versioned list or establish overall readiness.

## 3. Complete device-example field inventory

**Source: A02, both Example Payload Breakdown sections; evidence: Example.** The Wi-Fi values are numeric literals in an annotated JSON example, not telemetry. Cellular columns preserve raw integers for all three published groups. The scaling is documented arithmetic (**Derived** when applied). The source's quantity labels describe the reported signal; they do not authenticate a particular physical subcomponent or prove the values are ambient/calibrated.

| ID / position | Wi-Fi native key | Reported quantity / unit | Wi-Fi example | Cellular raw groups 1 / 2 / 3 | Cellular divisor |
| --- | --- | --- | --- | --- | --- |
| A-F01 / 1 | `rco2` | CO2 / ppm | 452 | 452 / 450 / 446 | 1 |
| A-F02 / 2 | `atmp` | Temperature / °C | 28.5 | 285 / 286 / 286 | 10 |
| A-F03 / 3 | `rhum` | Relative humidity / % | 75.1 | 751 / 751 / 753 | 10 |
| A-F04 / 4 | `pm01` | PM1.0 / µg/m³ | 16.3 | 163 / 170 / 167 | 10 |
| A-F05 / 5 | `pm25` | PM2.5 / µg/m³ | 27.7 | 277 / 283 / 287 | 10 |
| A-F06 / 6 | `pm10` | PM10 / µg/m³ | 29.5 | 295 / 300 / 302 | 10 |
| A-F07 / 7 | `tvocRaw` | TVOC raw / raw; not ppb/index | 34012 | 34012 / 34140 / 34139 | 1 |
| A-F08 / 8 | `noxRaw` | NOx raw / raw; not NO2 concentration | 20429 | 20429 / 20589 / 20577 | 1 |
| A-F09 / 9 | `pm003Count` | PM 0.3 particle count / volume basis not fixed here | 3225 | 3225 / 3272 / 3237 | 1 |
| A-F10 / 10 | `wifi` | Signal strength / dBm per cellular sequence | -69 | -69 / -69 / -69 | 1 |
| A-F11 / 11 | `volt` | Battery voltage / V | 11.24 | 1124 / 1124 / 1124 | 100 |
| A-F12 / 12 | `light` | Solar-panel voltage / V | 1.4 | 14 / 15 / 15 | 100 |
| A-F13 / 13 | `measure0` | O3 working electrode / mV | 580.981 | 580981 / 581000 / 581013 | 1000 |
| A-F14 / 14 | `measure1` | O3 auxiliary electrode / mV | 581.369 | 581369 / 581400 / 581438 | 1000 |
| A-F15 / 15 | `measure2` | NO2 working electrode / mV | 581.319 | 581319 / 581388 / 581350 | 1000 |
| A-F16 / 16 | `measure3` | NO2 auxiliary electrode / mV | 582.4 | 582400 / 582456 / 582494 | 1000 |
| A-F17 / 17 | `measure4` | AFE Temperature / source says mV; unresolved | 579.6 | 5796 / 5795 / 5796 | 10 |

**A-F18 — `interval`:** the leading cellular integer is `180` seconds, outside the repeated groups. The example has 52 integers total (1 + 3 × 17). It supplies no absolute timestamp or authenticated subject identifier in that body. Preserve the distinction between device Wi-Fi `pm25` and cloud `pm02`.

**Do not repair these values:** cellular panel `14 / 100 = 0.14 V`, while Wi-Fi `light = 1.4`; no synchronization is established. `measure4` is held from physical-temperature normalization because the source label and unit are unresolved. The Wi-Fi example is not strict JSON until its explanatory comments are removed; the existing checker labels that derivative. A sample-format check is not firmware execution.

## 4. Complete manufacturer cloud-example inventory

**Source: A09 reply #3, 15 September 2026; evidence: Example.** W = `/public/api/v1/world/locations/{locationId}/measures/current`; L = `/public/api/v1/locations/{locationId}/measures/current`. W and L are separate examples, not a joined record. `—` means the key is absent from that example; `null` is an explicitly present null. Quoted values remain strings. Displayed location/serial values are placeholders, not actual identities.

| ID | Native key | W example | L example | Meaning / use boundary |
| --- | --- | --- | --- | --- |
| A-API01 | `locationId` | 123456 | 123456 | Location identifier; not hardware ID |
| A-API02 | `locationName` | "Example Location" | "Example_Location" | Location label |
| A-API03 | `publicLocationName` | "Example Public Location" | — | Public location label |
| A-API04 | `latitude` | 0.0 | 0.0 | Coordinate placeholder; not an installation |
| A-API05 | `longitude` | 0.0 | 0.0 | Coordinate placeholder; not an installation |
| A-API06 | `offline` | false | — | Service Boolean; not whole-equipment health |
| A-API07 | `pm01` | 5.3 | 5.3 | PM1; A08 quantity context, µg/m³ |
| A-API08 | `pm02` | 7.3 | 7.4 | PM2.5; A08 quantity context, µg/m³ |
| A-API09 | `pm10` | 7.5 | 7.5 | PM10; A08 quantity context, µg/m³ |
| A-API10 | `pm003Count` | 983 | 1110 | Particle-count field; no cross-path conversion asserted |
| A-API11 | `atmp` | 14.8 | 15.1 | Temperature; A08 context °C |
| A-API12 | `rhum` | 87 | 87 | Relative humidity; A08 context % |
| A-API13 | `rco2` | 526 | 523 | CO2; A08 context ppm |
| A-API14 | `tvoc` | null | null | Null; no usable value |
| A-API15 | `wifi` | -49 | -48 | Signal field; not overall communications health |
| A-API16 | `timestamp` | "2026-09-15T05:49:58.000Z" | "2026-09-15T05:58:59.000Z" | Timestamp string with Z; no authenticated event |
| A-API17 | `tvocIndex` | 34295 | 34428 | Keep native key/value; no valid index-range mapping assumed |
| A-API18 | `noxIndex` | 18097 | 18379 | Keep native key/value; no valid index-range mapping assumed |
| A-API19 | `heatindex` | 15 | — | Meaning/unit not resolved by these excerpts: hold |
| A-API20 | `placeId` | 99999 | — | Place identifier, not hardware ID |
| A-API21 | `publicPlaceName` | null | — | Null public-place label |
| A-API22 | `publicPlaceUrl` | null | — | Null public-place URL |
| A-API23 | `publicContributorName` | "Example Contributor" | — | Contributor placeholder |
| A-API24 | `timezone` | "Asia/Bangkok" | "Asia/Bangkok" | Named zone; do not overwrite Z time |
| A-API25 | `model` | "O-M-1PPSTON-CE" | "O-M-1PPSTON-CE" | Model attribution in example only |
| A-API26 | `firmwareVersion` | null | null | Null; installed version unknown |
| A-API27 | `no2` | 17.7 | 27.909033 | ppb stated in A09 for W; gas-validity cautions apply |
| A-API28 | `o3` | -17.9 | -14.725 | ppb stated in A09 for W; excluded from validated concentration use |
| A-API29 | `locationType` | — | "outdoor" | Example location category |
| A-API30 | `pm01_corrected` | — | 5.3 | Corrected-named PM1; formula not established |
| A-API31 | `pm02_corrected` | — | 4.4 | Corrected-named PM2.5; chosen correction unknown |
| A-API32 | `pm10_corrected` | — | 7.5 | Corrected-named PM10; formula not established |
| A-API33 | `atmp_corrected` | — | 15.1 | Corrected-named temperature; algorithm not established |
| A-API34 | `rhum_corrected` | — | 87 | Corrected-named humidity; algorithm not established |
| A-API35 | `rco2_corrected` | — | 523 | Corrected-named CO2; algorithm not established |
| A-API36 | `serialno` | — | "00000example" | Placeholder, not authenticated unit identity |
| A-API37 | `batteryVoltage` | — | "12.25" | Battery-voltage string; preserve native type |
| A-API38 | `panelVoltage` | — | "17.18" | Panel-voltage string; preserve native type |
| A-API39 | `o3WorkingElectrode` | — | 383.7125 | Raw O3 working-electrode field; no concentration conversion |
| A-API40 | `o3AuxiliaryElectrode` | — | 398.4375 | Raw O3 auxiliary-electrode field; no concentration conversion |
| A-API41 | `no2WorkingElectrode` | — | 306.5125 | Raw NO2 working-electrode field; no concentration conversion |
| A-API42 | `no2AuxiliaryElectrode` | — | 300.525 | Raw NO2 auxiliary-electrode field; no concentration conversion |
| A-API43 | `afeTemp` | — | 316.3375 | AFE field; unit/physical interpretation unresolved: hold |

Coverage check: **28 W keys, 36 L keys, 43 distinct keys; all listed**. Native JSON types are apparent from the literals; no string-to-number or null-to-zero replacement was made. A08 is a separate CSV-export reference, not proof that these cloud values obey its schema. Its index discussion does not justify silently correcting A09's unusually large index-labeled values.

A09 replies #5–#6, dated 17 September 2026, give gas-calibration cautions and advise ignoring O3 at that time. Those cautions are retained as dated statements; no later resolution is asserted. Raw electrode values, processed gases, raw channel signals and indices are not equated. Other CSV-only fields have not been comprehensively extracted into this sheet.

## 5. Information suitable for the proposed first power/condition discussion

The immediately available references are **A-P01–P07**, **A-M01–M04**, **A-F11–F12**, the `batteryVoltage` / `panelVoltage` cloud rows, and **A-L01–L13**. These identify design power paths, voltage examples, timing rules and documented local diagnostic meanings. They do not supply remaining-capacity percentages, runtime readiness, observed switch state or successful control. This is a navigation aid, not approval of a model or a decision to discard the other rows.

## 6. Explicit gaps / items withheld from stronger use

| Gap ID | Missing or unresolved information | Treatment |
| --- | --- | --- |
| A-G01 | Installed identity, component serials, active hardware/firmware pair | Unknown; no fabricated individual System. |
| A-G02 | Actual configuration, command acknowledgement and execution outcomes | Definitions only; no applied-state record. |
| A-G03 | Actual current/history measurements and health | None obtained; earlier lab endpoint failure remains an access finding. |
| A-G04 | `measure4` / `afeTemp` physical unit and conversion | Keep native label/value; no Celsius normalization. |
| A-G05 | Gas-calibration validity; index-key interpretation | Preserve examples/cautions; no calibrated environmental truth. |
| A-G06 | README-versus-guide timing and model-suffix relationship | Separate source contexts; no reconciliation by assumption. |
| A-G07 | Full firmware schema, CSV-only fields, module schematics and lifecycle/security details | Not fully extracted; this sheet does not claim completeness beyond its named inventories. |
| A-G08 | Conflicting PDF edition/renderings in earlier audit | Excluded from positive evidence; do not repair the audit silently. |

## 7. Preservation and repeatability

The unchanged [AirGradient checker](../03_AirGradient_Example_Check.py) retains the A02 cellular and annotated Wi-Fi examples with attribution. Its embedded examples support all §3 values. This sheet's cloud table is a factual itemization of the two A09 examples, not a captured API response or a full website archive. No new sensor request, hardware test or source-to-CSAPI transformation occurred. Prior hashes and qualification verdicts remain unchanged.

A02 excerpt attribution: AirGradient / Open Air Foundation; CC BY-SA 4.0 for the licensed README-derived device table; table rearrangement and arithmetic are identified above. Do not extend that license to unrelated website/forum material. All manufacturer documents are referenced, not republished in full.

## 8. Source key and exact locators

Source IDs retain their meanings in the A audit. Access for this consolidation: **30 October 2026, America/New_York**. Pinned commit dates are not deployed firmware dates. Table references to source headings/keys are the claim locators.

- **A01:** AirGradient hardware team, *Open Air Max — Hardware*, [README at 89aacf5](https://github.com/Open-Air-Foundation/pcb-openair-max-main/blob/89aacf5013fc0ffe4b988a2e3c5a227bce3c4983/README.md), Overview / Key components / Plug-in modules. Audited design facts retained; not a new schematic audit.
- **A02:** AirGradient, *Firmware for the AirGradient Open Air Max*, [README at 84e479a](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/README.md), exact sections named above; blob `1322b58c7ed70ec0f4900bd557ec09fa65e03732`. Pinned text reread.
- **A03:** [Configuration.cpp at the same firmware commit](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/main/Configuration.cpp), audited lines 95–135; Sensor.cpp / MaxConfig.h coverage remains as recorded in A audit §B.
- **A04:** [Open Air Max product page](https://www.airgradient.com/professional/products/open-air-max/), commercial spelling retained through A audit §A; not a new variant determination.
- **A06:** [Power, Battery Backup, and Solar](https://www.airgradient.com/documentation/kb/airgradient-open-air-max-power-battery-backup-and-solar), USB-C Power / Battery Backup / Solar Power / Batteries; mutable HTML reread.
- **A07:** [Status LED and Reporting Intervals](https://www.airgradient.com/documentation/kb/airgradient-open-air-max-status-led-and-reporting-intervals), Power Modes and LED table; mutable HTML reread.
- **A08:** [Dashboard CSV Export field reference](https://www.airgradient.com/documentation/kb/kb-diy-air-quality-parameters), General Parameters; context only, not an API schema.
- **A09:** Tai_AirGradient, [*Max API — Working example with O3 and NO2 data*](https://forum.airgradient.com/t/max-api-working-example-with-o-and-no-data/7345), reply #3 (15 September 2026) examples; replies #5–#6 (17 September 2026) caveats. Only the manufacturer's posts are used.

**Finished product:** source-qualified working inventory, with all named example fields enumerated. No model terminology, Profile rules, live integration or audit upgrade is adopted by this sheet.
