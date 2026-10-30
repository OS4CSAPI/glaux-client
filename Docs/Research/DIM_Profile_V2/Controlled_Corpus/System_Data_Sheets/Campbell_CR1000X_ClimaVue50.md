# System Data Sheet D — Campbell CR1000X + First-Generation ClimaVue 50

**Version 0.1 · 30 October 2026 · America/New_York**  
**Reference case:** CR1000X logger, one first-generation ClimaVue 50 sensing assembly and cable, with documented support roles. **Not an authenticated installed station, CR1000Xe or ClimaVue 50 G2.**  
**Purpose:** Itemized inputs for later Domain Information Model (DIM) / OGC API – Connected Systems (CSAPI) work; research data sheet, not a manufacturer-issued datasheet.  
**Basis:** [D audit](../06_Candidate_D_Evidence_Audit.md), [selection](../07_Corpus_Qualification_Decision.md), [handoff](../08_Frozen_Corpus_Manifest_and_Handoff.md), repository revision `315034c25326dc4a08ecc0629f8bf3a933abe092`. Verdict and frozen records remain unchanged.

## How to use this sheet

**Design** = `PRIMARY_DESIGN_OR_SPEC`; **Example** = `PRIMARY_PUBLISHED_EXAMPLE`; **Derived** = `SYNTHETIC_OR_DERIVED`; **Unknown** = `UNAVAILABLE_OR_UNVERIFIED`. These are the prior evidence labels in readable form. All settings/values retain their source scope; **none is an acquired actual station record**. Source IDs resolve in §9.

Three evidence groups remain distinct: the documented logger/sensor arrangement; sensor interface definitions; and the separate logger-status example. This sheet lists all 31 status-example fields and all 14 sensor `aR7!` response positions. D02/D06/D07 were reread for extraction; that detail extends the input inventory, not the earlier qualification verdict. The sensor tables were visually checked in the 08/2024 PDF. No assumption joins the 2019 program, 2021 download, 2024 manual and 2026 interface example into one working release.

## 1. Equipment, power, connection and configuration

| ID | Subject / native item | Information available | Evidence / locator | Limit |
| --- | --- | --- | --- | --- |
| D-I01 | Logger | CR1000X measurement/control datalogger | Design; D audit §A; D05 | Not CR1000Xe; no installed serial. |
| D-I02 | Attached sensing assembly | One first-generation ClimaVue 50 plus cable | Design; D audit §A; D03/D04 | Multiple quantities are not multiple independent physical Systems. |
| D-I03 | Support arrangement | Protected logger/power housing and appropriate sensor mounting | Design; D audit §A; D02/D05 | No chosen enclosure SKU, mast or deployment. |
| D-I04 | External logger supply | Nominal 12 Vdc | Design; D audit §A / D05 | No installed battery/charger/solar configuration. |
| D-I05 | Sensor supply | Continuous power; brown lead to 12V | Design; D02 §7.1 Table 7-1 | Not a measured sensor-local voltage. |
| D-I06 | Sensor signal | White lead: SDI-12 to configured C/U terminal | Design; D02 §7.1 Table 7-1 | Interface connection, not evidence a command ran. |
| D-I07 | Shield / power return | Clear shield to G; black power ground to G | Design; D02 §7.1 Table 7-1 | No physical wiring inspection. |
| D-I08 | Sensor address | Factory default 0; shared bus requires distinct addresses | Design; D02 §7.1 | Default is not discovered active address. |
| D-I09 | Historical program terminal | C1 | Example; D audit §A / D03 Appendix B | Specific example choice, not required universal port. |
| D-I10 | Historical program address | 0 | Example; D audit §A / D03 | Not an installed setting. |
| D-I11 | Historical program scan | 60 seconds | Example; D audit §A / D03 | No running program verified. |
| D-I12 | Manual scan guidance | 60 seconds recommended; scan longer than 10 seconds | Design; D02 QuickStart / §8.1 | Do not confuse scan interval with every sensor internal sample interval. |
| D-I13 | Programming | CRBasic; Short Cut / CRBasic Editor context | Design; D02 §7.2; D03 | No compilation/execution performed. |
| D-I14 | 2021 package | Example Program v1; July 8, 2021; 3 KB; login required | Design; D audit §B / D04 | Package not obtained; not declared identical to D03. |
| D-I15 | Siting / orientation | Level and correctly oriented mounting required | Design; D02 installation context | No site, orientation or accurate coordinate record. |
| D-I16 | Reporting path | MQTT status topic / dedicated logger example | Design/Example; D07/D08/D09 | External broker/service not a selected station component. |
| D-I17 | Installed versions | Logger OS, sensor hardware/firmware and active program unknown | Unknown; D audit §§A/F | Source publication dates are not deployed versions. |

## 2. Every ClimaVue `aR7!` response position

**Source: D02 Table 8-1, printed p.21 (PDF page 25, 1-based). Evidence: Design/interface definition. Subject: the ClimaVue sensing assembly's response, not logger diagnostics.** All positions are numeric quantities, but the exact wire grammar is not redefined here. **No original numerical weather response was acquired; value is unknown for every row.** The source notation `a` denotes the SDI-12 address.

| ID / position | Source quantity | Native unit | Value available | Meaning boundary |
| --- | --- | --- | --- | --- |
| D-R01 / 1 | Solar flux density | W/m² | None; definition only | Reported quantity; not a physical component identity. |
| D-R02 / 2 | Precipitation | mm | None; definition only | Reported quantity; not a physical component identity. |
| D-R03 / 3 | Lightning strike count | count | None; definition only | Reported quantity; not a physical component identity. |
| D-R04 / 4 | Strike distance | km | None; definition only | Reported quantity; not a physical component identity. |
| D-R05 / 5 | Wind speed | m/s | None; definition only | Reported quantity; not a physical component identity. |
| D-R06 / 6 | Wind direction | ° | None; definition only | Reported quantity; not a physical component identity. |
| D-R07 / 7 | Wind speed max. — 10 s gust | m/s | None; definition only | Reported quantity; not a physical component identity. |
| D-R08 / 8 | Air temperature | °C | None; definition only | Not logger PanelTemp. |
| D-R09 / 9 | Vapor pressure | kPa | None; definition only | Reported quantity; not a physical component identity. |
| D-R10 / 10 | Barometric pressure, absolute | kPa | None; definition only | Absolute, not sea-level-adjusted pressure. |
| D-R11 / 11 | Relative humidity | fraction 0–1 | None; definition only | Not a percentage without an explicit conversion. |
| D-R12 / 12 | Humidity sensor temperature | °C | None; definition only | Not logger PanelTemp. |
| D-R13 / 13 | Tilt North(+)/South(−) orientation | ° | None; definition only | Reported quantity; not a physical component identity. |
| D-R14 / 14 | Tilt West(+)/East(−) orientation | ° | None; definition only | Reported quantity; not a physical component identity. |

D02's footnotes say `aR7!` resets averaging/totalizing/maximizing and can return a previously reported value when a new measurement has not been taken; lightning strike count is treated differently. Thus receipt is not proof of freshness. The `aC!` table also lists north/east wind speed (m/s) and a disabled compass-heading output; these are additional interface definitions, not extra acquired observations or a fitted active compass. D02 prints both “Maximum wind speed” and “Wind speed max. — 10 s gust” in the `aC!` list; this sheet does not silently collapse them.

## 3. Sensor identity, verification and controls

**Source: D02 Table 8-1, printed pp.22–23 (PDF pages 26–27).** Values remain absent; these are Design/interface definitions, separate from the logger example in §5.

| ID | Native command / response item | Type / unit | Information / value standing |
| --- | --- | --- | --- |
| D-V01 | aI! / a13CAMPBELLCLIM50SN-yyyyyyyy | identification string pattern | Address, SDI-12 version 13, model Clim50, serial placeholder; no actual response obtained. |
| D-V02 | aV! / operating system version | version value; encoding not expanded here | Sensor OS version definition; actual value unknown. |
| D-V03 | aV! / hardware version | version value; encoding not expanded here | Sensor hardware version definition; actual value unknown. |
| D-V04 | aV! / watchdog errors | count | Sensor diagnostic definition; not logger WatchdogErrors. |
| D-V05 | aV! / uptime | seconds | Sensor uptime definition; actual value unknown. |
| D-V06 | aAb! | address command; b is new address | Supported address change; no command sent or acknowledgement captured. |
| D-V07 | ?! | address query | Supported query; actual address not obtained. |
| D-V08 | aM!, aM1!, aM3!, aC! | measurement commands | Alternative response groupings documented; no actual command session. |

The reference model's functions include precipitation, solar, wind, humidity, thermistor, tilt, barometric-pressure and lightning sensing as described in D02 §5. Those function names are not asserted as an independently serial-numbered internal component inventory.

## 4. Program-mediated values and processing context

| ID | Information | Source / standing | What must survive |
| --- | --- | --- | --- |
| D-C01 | Sea-level pressure adjustment uses assumed site elevation | D04 description; Design; D audit §F | Adjusted pressure ≠ directly reported absolute pressure. |
| D-C02 | Invalid wind values may be replaced with previous valid values | D04 description; Design | Carried-forward value ≠ a new measurement. |
| D-C03 | Historical program contains conversions and interval outputs | D03 extracted program; Example; D audit §F | No executable weather transform verified; exact program applicability unresolved. |
| D-C04 | Literal extraction: Cont SeaLevelAdj=15.29091 | D03 extraction; Unknown transcription correctness | Do not fix syntax or claim runnable program without verifying source. |
| D-C05 | Example package vs historical program | 2019 text / separate 2021 package | Do not equate two editions without contents comparison. |
| D-C06 | Status publication interval | MQTTStatusInterval setting; D07 Design | No configured interval value obtained. |
| D-C07 | Status topic | `<baseTopic>/status/<deviceId>`; D07 Design | Transport address is not a physical sensor identity. |

## 5. Complete CR1000X status-example inventory

**Source: D07, “CR1000X Example,” footer 2026-09-21 (ced60094). Evidence: Example. Subject: logger component only.** The example is not output from D03 and does not establish an attached ClimaVue. The field names below pair positionally with the values, as D08 specifies. Literal numbers/strings/Booleans are preserved; no values are measurements obtained by this research.

### Envelope and time

| ID | Native member | Example value / type | Boundary |
| --- | --- | --- | --- |
| D-E01 | type | Feature / string | Message representation type, not equipment kind. |
| D-E02 | geometry.type | Point / string | Example geometry only. |
| D-E03 | geometry.coordinates | [0.0, 0.0, 0.0] / number array | Placeholders; no actual installation coordinates. |
| D-E04 | properties.loggerID | ABCD-EFGH-1234 / string | Illustrative logger identifier; no authenticated unit. |
| D-E05 | properties.observationNames | 31 strings in order | Do not sort names separately from the values. |
| D-E06 | properties.observations timestamp key | 2025-06-04T18:29:23.271Z / string | Explicit UTC example time; no verified event or clock accuracy. |

### All 31 status fields, in publisher order

| ID | Native field | Exact example value | Type / unit | Definition or explicit gap (D06) |
| --- | --- | --- | --- | --- |
| D-S01 | `WatchdogErrors` | 0 | number / count | Program-associated watchdog count; reset on compile or explicit reset. Zero is not lifetime fault-free. |
| D-S02 | `PanelTemp` | 25.91098 | number / °C | Logger wiring-panel temperature; not outside air or ClimaVue temperature. |
| D-S03 | `Battery` | 13.2368 | number / Vdc | System-supply voltage at logger; not capacity or sensor-local voltage. |
| D-S04 | `LithiumBattery` | 3.70477 | number / V | Internal lithium-battery voltage; separate supply subject. |
| D-S05 | `Low12VCount` | 0 | number / UNRESOLVED | Field/value retained; definition, unit or reset semantics not established by inspected D06. HOLD interpretation. |
| D-S06 | `CompileResults` | "cpu:main.crb -- Compiled in PipelineMode.\r\n" | string / text | Compilation/runtime diagnostic string; not hardware readiness. |
| D-S07 | `SkippedScan` | 0 | number / count | Skipped program scans; excludes intentionally skipped scans. |
| D-S08 | `SkippedSystemScan` | 0 | number / UNRESOLVED | Field/value retained; definition, unit or reset semantics not established by inspected D06. HOLD interpretation. |
| D-S09 | `SkippedSlowScan(1)` | 0 | number / UNRESOLVED | Field/value retained; definition, unit or reset semantics not established by inspected D06. HOLD interpretation. |
| D-S10 | `SkippedSlowScan(2)` | 0 | number / UNRESOLVED | Field/value retained; definition, unit or reset semantics not established by inspected D06. HOLD interpretation. |
| D-S11 | `SkippedSlowScan(3)` | 0 | number / UNRESOLVED | Field/value retained; definition, unit or reset semantics not established by inspected D06. HOLD interpretation. |
| D-S12 | `SkippedSlowScan(4)` | 0 | number / UNRESOLVED | Field/value retained; definition, unit or reset semantics not established by inspected D06. HOLD interpretation. |
| D-S13 | `CommsMemFree` | "614\r\n147(146),328(283),445(434),226(106),114(107),91(86),78(76),53(51),2(2),0(0)" | string / structured text | Communication-memory allocations; parentheses indicate low-water sizes. |
| D-S14 | `CardStatus` | "Card OK." | string / UNRESOLVED | Field/value retained; definition, unit or reset semantics not established by inspected D06. HOLD interpretation. |
| D-S15 | `MaxProcTime` | 81240 | number / µs | Maximum processing time for current scan; reset/update semantics matter. |
| D-S16 | `MaxBuffDepth` | 0 | number / UNRESOLVED | Field/value retained; definition, unit or reset semantics not established by inspected D06. HOLD interpretation. |
| D-S17 | `MaxSystemProcTime` | 788 | number / UNRESOLVED | Field/value retained; definition, unit or reset semantics not established by inspected D06. HOLD interpretation. |
| D-S18 | `MaxSlowProcTime(1)` | 10350364 | number / UNRESOLVED | Field/value retained; definition, unit or reset semantics not established by inspected D06. HOLD interpretation. |
| D-S19 | `MaxSlowProcTime(2)` | 8703216 | number / UNRESOLVED | Field/value retained; definition, unit or reset semantics not established by inspected D06. HOLD interpretation. |
| D-S20 | `MaxSlowProcTime(3)` | 2531229 | number / UNRESOLVED | Field/value retained; definition, unit or reset semantics not established by inspected D06. HOLD interpretation. |
| D-S21 | `MaxSlowProcTime(4)` | 0 | number / UNRESOLVED | Field/value retained; definition, unit or reset semantics not established by inspected D06. HOLD interpretation. |
| D-S22 | `PortStatus(1)` | false | Boolean / on/off | C-terminal control state; True on/high, False off/low; not measured voltage. |
| D-S23 | `PortStatus(2)` | false | Boolean / on/off | C-terminal control state; True on/high, False off/low; not measured voltage. |
| D-S24 | `PortStatus(3)` | false | Boolean / on/off | C-terminal control state; True on/high, False off/low; not measured voltage. |
| D-S25 | `PortStatus(4)` | true | Boolean / on/off | C-terminal control state; True on/high, False off/low; not measured voltage. |
| D-S26 | `PortStatus(5)` | true | Boolean / on/off | C-terminal control state; True on/high, False off/low; not measured voltage. |
| D-S27 | `PortStatus(6)` | true | Boolean / on/off | C-terminal control state; True on/high, False off/low; not measured voltage. |
| D-S28 | `PortStatus(7)` | true | Boolean / on/off | C-terminal control state; True on/high, False off/low; not measured voltage. |
| D-S29 | `PortStatus(8)` | true | Boolean / on/off | C-terminal control state; True on/high, False off/low; not measured voltage. |
| D-S30 | `SW12Volts(1)` | true | Boolean / on/off | Switched 12-V terminal state; True on; not numeric voltage. |
| D-S31 | `SW12Volts(2)` | true | Boolean / on/off | Switched 12-V terminal state; True on; not numeric voltage. |

**Coverage check:** 31 unique fields / 31 values: **18 numbers, 3 strings, 10 Booleans**. Every field is listed, including the fields whose interpretation remains on hold. For `Low12VCount`, `SkippedSystemScan`, `SkippedSlowScan(1–4)`, `CardStatus`, `MaxBuffDepth`, `MaxSystemProcTime` and `MaxSlowProcTime(1–4)`, the value's presence/type is established by D07, but this extraction does not invent the missing detailed definition or units from the field name. `Card OK.` is source text, not a verified condition.

The transcript's canonical JSON SHA-256 is `ef93d1fc12a09fe04a4d06da743b07a8694cd6bc74af3ce612110a8d4e15c8a8`, matching the earlier audit/handoff. The full raw publisher JSON is not added as an alleged device record; this table is a factual inventory of its fields/values. The locally reconstructed JSON was parsed and checked against all 31 rows during consolidation.

## 6. Additional D06 fields — definitions, no example values

These published field definitions are useful identity/configuration/diagnostic context but are **not present in the 31-field example**. Evidence is Design; subject is the CR1000X logger. An absent example value is not evidence of an unsupported feature. Names, native types and units are retained where D06 supplies them.

| ID | Native field | Native type / unit | Documented meaning and absence |
| --- | --- | --- | --- |
| D-X01 | `CalCurrent()` | numeric | Factory correction factors; no values. |
| D-X02 | `CalGain()` | numeric | Factory correction factors; no values. |
| D-X03 | `CalOffSet` | numeric | Offset calibration factor; no value. |
| D-X04 | `CalRefOffSet()` | numeric | Offset calibration factor; no values. |
| D-X05 | `CalRefSlope()` | numeric | Factory correction factors; no values. |
| D-X06 | `CalVolts()` | numeric | Factory correction factors; no values. |
| D-X07 | `CardBytesFree` | bytes; type not stated in excerpt | Free card bytes; no value. |
| D-X08 | `FullMemReset` | numeric | 98765 is a documented reset-control input, not current state; not invoked. |
| D-X09 | `MeasureTime` | numeric / µs | Compile-time measurement-duration calculation, not observed duration. |
| D-X10 | `MemoryFree` | numeric / bytes | Unallocated final-storage memory; availability qualifications apply. |
| D-X11 | `MemorySize` | numeric / bytes | Total final-storage memory size; no value. |
| D-X12 | `OSDate` | string / mm/dd/yyyy | OS build date; no actual value. |
| D-X13 | `OSSignature` | numeric | OS signature; no actual value. |
| D-X14 | `OSVersion` | string | OS version; no actual value. |
| D-X15 | `PakBusRoutes` | structured string | Port, via-neighbour, address and response-time tuples; no routes acquired. |
| D-X16 | `PortConfig` | string | C-terminal function configuration; no selected configuration. |
| D-X17 | `ProcessTime` | numeric / µs | Last-scan processing time; no actual value. |
| D-X18 | `ProgErrors` | numeric / count | Compile/runtime error count; no value. |
| D-X19 | `ProgName` | string | Running program name; not supplied for this reference installation. |
| D-X20 | `ProgSignature` | numeric | Source-program signature including comments; no value. |
| D-X21 | `Record` | Long; range 0 to 2^32 as printed | Increments when support software requests record; no value. |
| D-X22 | `RevBoard` | string xxx.yyy | Hardware/clock-chip software revision; no value. |
| D-X23 | `RunSignature` | numeric | Compiled-program signature; independent of comments; no value. |
| D-X24 | `SerialNumber` | numeric | Factory-assigned serial; no value. |
| D-X25 | `StartTime` | NSEC | Program start-time field; no value. |
| D-X26 | `StartUpCode` | numeric code | 0 normal; −1 power-loss restart; −2 watchdog restart; no event acquired. |
| D-X27 | `StationName` | string | Logger station-name field; not automatically support-software name or data-file header. |
| D-X28 | `TimeStamp` | NSEC | Record-generation scan time; no value. |
| D-X29 | `VarOutOfBound` | numeric / count | Out-of-bounds array-write attempts; no value. |

D06 itself directs readers to the logger manual for a complete Status-table list. This sheet does not claim that the 31 example fields plus these 29 additional definitions exhaust every firmware's Status table.

## 7. Starting references for power/condition work

Use **D-I04–I07**, **D-S01–S05**, **D-S07–S31**, and **D-V04–V05**, with the on-hold definitions above kept on hold. Especially useful are **D-S03 `Battery`**, **D-S04 `LithiumBattery`**, and **D-S30–S31 `SW12Volts`**: their different subjects/types are explicit. Do not transfer logger values to the attached weather sensor or infer whole-station health from any of them. Sensor verification has definitions only, not values.

## 8. Explicit gaps and withholding decisions

| ID | Gap | Treatment |
| --- | --- | --- |
| D-G01 | Installed identity, support-hardware inventory, site and active program/firmware combination | Unknown; no joined station is manufactured from separate sources. |
| D-G02 | Actual weather observations, condition history or configuration export | None obtained; actual-history coverage remains zero. |
| D-G03 | Detailed meanings/units for 13 of the 31 example fields | Native values/types retained in §5; interpretation held pending exact source definitions. |
| D-G04 | Executable 2021 program package and verified 2019 transcription | Not obtained/verified; no repairs or runnable-program assertion. |
| D-G05 | Numerical `aR7!`, `aI!`, `aV!` replies | Definitions only; no invented readings, serial or version. |
| D-G06 | Complete internal component inventory, all capabilities and all logger interfaces | Not exhaustively extracted; source references remain available. |
| D-G07 | Command authorization, acknowledgements and outcomes | No executed session; documented controls are not enabled user actions. |
| D-G08 | Original-byte archive and redistribution permission for full manuals/program | Not established; link to sources rather than republish entire works. |

## 9. Sources, editions and reproduction

IDs retain D audit §B meaning; accessed for consolidation **30 October 2026, America/New_York**. This is extraction from already selected sources, not a fresh candidate audit.

- **D01 / D05:** Campbell [ClimaVue 50](https://us.campbellsci.com/climavue-50) and [CR1000X](https://us.campbellsci.com/cr1000x) product information as qualified in the audit; no later product substituted.
- **D02:** Campbell, [*ClimaVue 50 Product Manual*, 08/2024](https://s.campbellsci.com/documents/us/manuals/climavue50.pdf), Table 7-1 printed p.13, Table 8-1 pp.21–23; PDF pages 17 and 25–27 visually inspected for this sheet. Short Cut scan guidance is in QuickStart. No manual redistributed.
- **D03:** [Historical European manual](https://s.campbellsci.com/documents/eu/manuals/climavue50.pdf), 9/19 as identified in the prior extraction, Appendix B. Only previously qualified program facts used; visual/transcription anomaly remains unresolved.
- **D04:** [ClimaVue 50 Example Program](https://www.campbellsci.com/resources/software/climavue50-example-program), v1 / July 8, 2021, as recorded in the audit. Download contents remain uninspected.
- **D06:** [CR1000X Status Table](https://help.campbellsci.com/crbasic/cr1000x/Content/Instructions/StatusTable.htm), exact native field entries; mutable HTML reread. Missing entries are not inferred from similarly named fields.
- **D07:** [Status — MQTT API](https://help.campbellsci.com/datalogger-api/mqtt/status.html), CR1000X Example, displayed footer 2026-09-21 (ced60094); reread and locally reconstructed for the content comparison.
- **D08 / D09:** [JSON Data Formats](https://help.campbellsci.com/datalogger-api/mqtt/json_data_formats.html) and [MQTT API introduction](https://help.campbellsci.com/datalogger-api/mqtt/index.html), positional and compatibility limits retained from D audit; no implementation test.

The unchanged [Campbell checker](../06_Campbell_Example_Check.py) accepts a separately supplied JSON example. The source example still has to be obtained/transcribed for an exact replay; the sheet does not convert the example into a device record. Existing frozen artifacts are unchanged. No DIM, Profile, producer or client modification is made here.
