# 01 — Source specimen and native inventory

**Status:** Phase 1 complete for the frozen specimen; Phase 2 source characterization is substantially populated. Formal target mapping has not started.

## 1. Frozen specimen control record

| Field | Value |
| --- | --- |
| Candidate / selected registration | `19639` |
| Capture time UTC | `2026-10-25T02:43:48Z` |
| Device endpoint | `https://api.smartcitizen.me/v0/devices/19639` |
| History range | `2026-10-24T00:00:00Z` through `2026-10-25T00:00:00Z` |
| Temperature history | Sensor `55`; `rollup=1h`; `function=avg`; `all_intervals=true` |
| PM2.5 history | Sensor `194`; `rollup=1h`; `function=avg`; `all_intervals=true` |
| HTTP result | All three GET requests returned HTTP 200 |
| Complete raw evidence | [`Docs/Research/Evidence/Smart_Citizen/Captures/20261025T024348Z`](../../../Evidence/Smart_Citizen/Captures/20261025T024348Z/) |
| Device body SHA-256 | `9fc7abbb34c596f4185054cfc416335062601d158a2666ca8a106389e40cfb8d` |
| Temperature-history SHA-256 | `8024d8116799bdf75d58e30b4f097e644492e235907cec4d2b0e7b46b0e53b73` |
| PM2.5-history SHA-256 | `972c8e564f7265aa5cde6f006298771714056acd0852096d4e6b9431b9a62361` |
| Capture workflow | `.github/workflows/smart-citizen-freeze.yml`; GitHub Actions run `40155554453` |
| Frozen-evidence commit | `9c184d9270bf3a2baba73ea6e9410fd9bfd53fda` |

The frozen response identifies registration 19639 as `has_published`, tagged `online` and `outdoor`, and reported the latest device-level reading at `2026-10-25T02:40:21Z`. The formal capture began at `02:43:48Z`, so the source's most recent reported reading was approximately 3 minutes 27 seconds older than the capture time. This difference is source evidence, not a staleness determination; the expected cadence and acceptable age still require interpretation.

## 2. Source documentation set

| ID | Source | Access/revision | Exact locator | What it establishes | Limits |
| --- | --- | --- | --- | --- | --- |
| SC-DOC-001 | SmartCitizen API Reference | Accessed 25 Oct 2026 UTC | `Devices`, `Sensors`, `Readings`, `Measurements`, `Components` | Device IDs/state/last-reading meaning; sensors and parent concept; reading/history response; measurement vocabulary links; components join Devices to Sensors | Human-readable API reference; does not fully explain every field returned by the current deployment |
| SC-DOC-002 | Smart Citizen Kit documentation | Current public docs checked 24–25 Oct 2026 | `Smart Citizen Kit`; component/measurement descriptions | Product-family modularity, Data Board/Urban Board, sensing capabilities and hardware context | Model-level documentation does not prove this unit's exact installed inventory |
| SC-DOC-003 | Smart Citizen Data Platform documentation | Current public docs checked 24–25 Oct 2026 | `Data Platform`, API/front-end sections | Platform roles for ingestion, storage, API access and front-end applications | Platform architecture is distinct from physical-device facts |
| SC-DOC-004 | Smart Citizen vendor-presentation baseline | Repository record dated 24 Oct 2026 | Figures 6–7 source evidence | Historical first-party presentation patterns for device context, values/units, definitions and history | Not a matched view of registration 19639 |

Relevant API semantics already established by the source documentation include: device `id` is an incremental unique platform device ID; `state` is an automatic device state; `last_reading_at` is the last reading from any sensor; sensor `id`/`uuid` identify Smart Citizen sensor-catalogue records; a sensor with a parent is a sub-sensor; and a `Component` joins a Device to a Sensor. Historical readings return `[recorded_at, value]` tuples, while `sample_size` is the count of readings examined to build the response.

## 3. Native resource and identity inventory

| Native item | Frozen value | Source scope | Supported meaning | Does not establish |
| --- | --- | --- | --- | --- |
| Device registration ID | `19639` | Smart Citizen Platform | Incremental unique platform Device ID | Manufacturer serial or enduring physical asset ID |
| Device registration UUID | `02612831-3387-4cb2-8bed-cf87670ca1e5` | Smart Citizen Platform | UUID for the platform Device record | Manufacturer serial or proof that no other registration represents the same physical unit |
| Device name | `Web2learn - nautical club of Thessaloniki` | Platform Device record | User/platform name of this registration | Standardized equipment type or official product designation |
| Device state | `has_published` | Platform Device record | Automatic source-platform state | MERLIN readiness/health state |
| System tags | `online, outdoor` | Platform Device record | Source tags; includes online/outdoor | Independently verified connectivity or physical deployment condition |
| Reported hardware | `SmartCitizen Kit 2.3` / `SCK` / `2.3` / `sck:2,3` | Platform hardware metadata | Source-reported product model information | Verified serial, firmware, exact shipping variant, or installed component inventory |
| Source location | `Panorama`, `Greece`; exposure `outdoor` | Platform Device location record | Source-platform location/exposure metadata | Surveyed emplacement accuracy, deployment interval, or GPS-derived position |
| Owner record | Present in raw public response | Smart Citizen Platform account | Source account/ownership metadata | Responsible party for MERLIN operations or equipment custody |
| Component IDs in history | `4039417141` (temperature), `4039430900` (PM2.5) | Smart Citizen Device↔Sensor association | Platform component/association joining this Device to a Sensor | Physical component serial or connector identity |

The source response includes 21 channel records but this is not evidence of 21 separately identified physical sensor devices. Smart Citizen's own API model allows a sensor to be a sub-sensor of another catalogue sensor, and the history endpoint exposes component IDs that represent the Device-to-Sensor association. Those identifiers must remain distinct during mapping.

## 4. Frozen channel inventory

The table below records all 21 channels returned in the frozen device body. `—` means the source response supplied no URI for that column; it does not mean the concept itself is absent from all Smart Citizen documentation.

| Inv. ID | JSON path | Source channel | Sensor ID | Unit | Unit definition | Measurement | Measurement definition | Frozen value | Channel time UTC | Source description |
| --- | --- | --- | ---: | --- | --- | --- | --- | ---: | --- | --- |
| SC-SRC-001 | `/data/sensors/0` | AMS AS7731 - UVA | 214 | uW/cm2 | — | UVA | — | 0.08 | 2026-10-25T02:40:21Z | AMS AS7731 UVA Channel |
| SC-SRC-002 | `/data/sensors/1` | AMS AS7731 - UVB | 215 | uW/cm2 | — | UVB | — | 0.1 | 2026-10-25T02:40:21Z | AMS AS7731 UVB Channel |
| SC-SRC-003 | `/data/sensors/2` | AMS AS7731 - UVC | 216 | uW/cm2 | — | UVC | — | 0.0 | 2026-10-25T02:40:21Z | AMS AS7731 UVC Channel |
| SC-SRC-004 | `/data/sensors/3` | Battery SCK | 10 | % | — | battery | — | 99.0 | 2026-10-25T02:40:21Z | Custom Circuit |
| SC-SRC-005 | `/data/sensors/4` | NXP MPL3115A2 - Barometric Pressure | 58 | kPa | https://qudt.org/vocab/unit/KiloPA | Barometric Pressure | https://qudt.org/vocab/quantitykind/AtmosphericPressure | 101.69 | 2026-10-25T02:40:21Z | Digital Barometric Pressure Sensor |
| SC-SRC-006 | `/data/sensors/5` | ROHM - BH1730FVC | 14 | lux | https://qudt.org/vocab/unit/LUX | Light | — | 0.0 | 2026-10-25T02:40:21Z | Digital Ambient Light Sensor |
| SC-SRC-007 | `/data/sensors/6` | SD Card | 221 | — | — | SD-Card Presence | — | 1.0 | 2026-10-25T02:40:21Z | SD Card Presence |
| SC-SRC-008 | `/data/sensors/7` | Sensirion SEN5X - PM1 | 193 | ug/m3 | http://dd.eionet.europa.eu/vocabulary/uom/concentration/ug.m-3 | PM1 | http://dd.eionet.europa.eu/vocabulary/aq/pollutant/6002 | 8.8 | 2026-10-25T02:36:21Z | Particulate Matter PM1 |
| SC-SRC-009 | `/data/sensors/8` | Sensirion SEN5X - PM10 | 196 | ug/m3 | http://dd.eionet.europa.eu/vocabulary/uom/concentration/ug.m-3 | PM10 | http://dd.eionet.europa.eu/vocabulary/aq/pollutant/5 | 9.3 | 2026-10-25T02:36:21Z | Particulate Matter PM10 |
| SC-SRC-010 | `/data/sensors/9` | Sensirion SEN5X - PM2.5 | 194 | ug/m3 | http://dd.eionet.europa.eu/vocabulary/uom/concentration/ug.m-3 | PM2.5 | http://dd.eionet.europa.eu/vocabulary/aq/pollutant/6001 | 9.3 | 2026-10-25T02:36:21Z | Particulate Matter PM2.5 |
| SC-SRC-011 | `/data/sensors/10` | Sensirion SEN5X - PM4.0 | 195 | ug/m3 | http://dd.eionet.europa.eu/vocabulary/uom/concentration/ug.m-3 | PM4.0 | — | 9.3 | 2026-10-25T02:36:21Z | Particulate Matter PM4.0 |
| SC-SRC-012 | `/data/sensors/11` | Sensirion SEN5X - PN0.5 | 197 | #/0.1l | — | PN0.5 | — | 5960.0 | 2026-10-25T02:36:21Z | Particle Matter PN0.5 |
| SC-SRC-013 | `/data/sensors/12` | Sensirion SEN5X - PN1.0 | 198 | #/0.1l | — | PN1.0 | — | 6910.0 | 2026-10-25T02:36:21Z | Particle Matter PN1.0 |
| SC-SRC-014 | `/data/sensors/13` | Sensirion SEN5X - PN10.0 | 201 | #/0.1l | — | PN10.0 | — | 6950.0 | 2026-10-25T02:36:21Z | Particle Matter PN10.0 |
| SC-SRC-015 | `/data/sensors/14` | Sensirion SEN5X - PN2.5 | 199 | #/0.1l | — | PN2.5 | — | 6950.0 | 2026-10-25T02:36:21Z | Particle Matter PN2.5 |
| SC-SRC-016 | `/data/sensors/15` | Sensirion SEN5X - PN4.0 | 200 | #/0.1l | — | PN4.0 | — | 6950.0 | 2026-10-25T02:36:21Z | Particle Matter PN4.0 |
| SC-SRC-017 | `/data/sensors/16` | Sensirion SEN5X - TPS | 202 | um | — | Typical Particle Size | — | 43.1 | 2026-10-25T02:36:21Z | Particle Matter Typical Particle Size |
| SC-SRC-018 | `/data/sensors/17` | Sensirion SHT31 - Humidity | 56 | % | https://qudt.org/vocab/unit/PERCENT | Relative Humidity | https://qudt.org/vocab/quantitykind/RelativeHumidity | 65.54 | 2026-10-25T02:40:21Z | Humidity |
| SC-SRC-019 | `/data/sensors/18` | Sensirion SHT31 - Temperature | 55 | ºC | https://qudt.org/vocab/unit/DEG_C | Air Temperature | http://www.eionet.europa.eu/gemet/concept/281 | 19.59 | 2026-10-25T02:40:21Z | Temperature |
| SC-SRC-020 | `/data/sensors/19` | TDK ICS43432 - Noise Level A weighting | 53 | dBA | https://qudt.org/vocab/unit/DeciB_A | Noise Level | https://qudt.org/vocab/quantitykind/SoundPressureLevel | 31.28 | 2026-10-25T02:40:21Z | I2S Digital Mems Microphone with custom Audio Processing Algorithm |
| SC-SRC-021 | `/data/sensors/20` | Wi-Fi Antenna - RSSI | 220 | dBm | — | RSSI | — | -45.0 | 2026-10-25T02:40:21Z | RSSI from Wi-Fi antenna |

### Timing pattern in the frozen current response

Seventeen non-particulate channels in the frozen current response report `2026-10-25T02:40:21Z`. The ten SEN5X particulate mass/number/size channels report `2026-10-25T02:36:21Z`, four minutes earlier. Device-level `last_reading_at` is `02:40:21Z`, which confirms that the device-level latest time cannot be substituted for every channel's own time.

### Hardware-variant observation

The frozen registration reports three AMS AS7731 ultraviolet channels (UVA, UVB and UVC). Current Smart Citizen/retailer material previously reviewed for the project states that some SCK2.3 units shipped from July 2026 omit the UV sensor, while this registration was created in May 2026. The frozen source therefore provides a useful real case where reported model designation alone is insufficient to infer the exact channel inventory of every SCK2.3 unit.

## 5. Bounded historical series

### Temperature history

- Sensor ID: `55`; component ID: `4039417141`; sensor key: `t`.
- Range: `2026-10-24T00:00:00Z` through `2026-10-25T00:00:00Z`.
- Rollup/function: `1h` / `avg`.
- `sample_size`: `1439` readings examined to build the response.
- Returned aggregate tuples: `24`.
- Earliest returned tuple: `2026-10-24T00:00:05Z` → `19.627999999999993`.
- Latest returned tuple: `2026-10-24T23:00:12Z` → `19.75166666666667`.

### PM2.5 history

- Sensor ID: `194`; component ID: `4039430900`; sensor key: `pm_avg_2.5`.
- Range: `2026-10-24T00:00:00Z` through `2026-10-25T00:00:00Z`.
- Rollup/function: `1h` / `avg`.
- `sample_size`: `288` readings examined to build the response.
- Returned aggregate tuples: `24`.
- Earliest returned tuple: `2026-10-24T00:01:06Z` → `6.158333333333332`.
- Latest returned tuple: `2026-10-24T23:01:12Z` → `9.491666666666667`.

Both series return 24 hourly aggregate tuples, but the reported tuple timestamps are not exact clock-hour boundaries and the two channels differ by roughly one minute in many bins. The source documentation defines the tuple timestamp as `recorded_at` and the function as an average over the rollup period; it does not, by itself, justify inventing exact interval boundaries around each returned timestamp. Temperature and PM2.5 also have different `sample_size` values—1439 and 288—which reinforces that response-wide sample counts belong to each queried source series rather than to a universal per-bin count.

## 6. Representative first mapping set

| Proposed case | Inventory/evidence | Why it is useful |
| --- | --- | --- |
| Registration + reported model | Device top-level metadata | Exercises identity scope, model versus instance, and source-platform provenance |
| Air temperature | SC-SRC-019 + temperature history | Strong property/unit vocabulary support; current and aggregate temporal cases |
| PM2.5 | SC-SRC-010 + PM2.5 history | Different reporting cadence, Eionet property/unit vocabularies, particulate subject semantics |
| Relative humidity | SC-SRC-018 | QUDT unit/property definitions; same SHT31 physical package lineage as temperature |
| Barometric pressure | SC-SRC-005 | Different quantity and QUDT vocabulary; useful independent scalar case |
| Noise level | SC-SRC-020 | Processed acoustic metric with A-weighted unit; tests that a sound-level result is not an audio product |
| Battery percentage | SC-SRC-004 | Tests power-related measurement without inventing battery identity, charge, runtime or supply topology |
| Wi-Fi RSSI | SC-SRC-021 | Equipment/communications-related telemetry distinct from environmental observations |
| SD-card presence | SC-SRC-007 | Coded device-status indicator; source explicitly says `0` can mean absent **or corrupted** |

## 7. Resolved source-characterization questions and carried uncertainties

### Platform record times

The Smart Citizen API documentation defines `created_at` as the date/time the Device record was created and `updated_at` as the date/time the Device information was last updated. The current API source at commit [`25a524cbfb036f8950c247b847d8884a4e776297`](https://github.com/fablabbcn/smartcitizen-api/tree/25a524cbfb036f8950c247b847d8884a4e776297) updates `last_reading_at`, current data and `state` with `update_columns` when readings arrive; `raw_storer.rb` explicitly notes that this occurs “without touching updated_at.” These fields are therefore platform-record metadata and must not be mapped as physical installation, commissioning, service, or latest-observation times.

### Sensor ancestry and Device-to-Sensor association

The API documentation describes parent/sub-sensor relationships, while the v0 Device response exposes the underlying `ancestry` field. The current [Sensor model](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/app/models/sensor.rb) uses Rails `has_ancestry`; therefore values such as temperature/humidity ancestry `54` and SEN5X particulate ancestry `192` are source catalogue hierarchy, not physical component serials. Historical `component_id` values remain a separate Device-to-Sensor association identity. Parent catalogue records should be retained as supplementary source evidence when their descriptions are used in equipment/model mapping, but the child channel hierarchy is already sufficient to prevent treating every returned channel as a separate physical device.

### Location standing

Smart Citizen documentation identifies Device location as platform location metadata and allows user-selected precision; the current [Device model](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/app/models/device.rb) can fuzz latitude/longitude when precise location is not enabled. The public response filters the `precise_location` policy value, so the study cannot establish whether the returned coordinates are exact or fuzzed. The frozen location is therefore retained as **source-platform location/exposure context**. It is not yet promoted to an MPSS Deployment/emplacement assertion because source method, accuracy and applicability interval are not established.

### Source platform state and online tag

Smart Citizen `state=has_published` means the Device has stored/published data; it is not a MERLIN equipment-health assessment. The current Device model computes the `online` system tag from `last_reading_at` being within the preceding 60 minutes, and otherwise emits `offline`. Both values are therefore source-platform status semantics. The experiment may preserve them as source facts but must not translate them into mission readiness, communications-link state, or physical-operating condition without a separately supported mapping.

### Public current-value processing provenance

The inspected Smart Citizen API source indicates that ingestion can preserve a raw reading separately while storing a normalized/calibrated value under the sensor ID used by the public Device response. The Device model's public `formatted_data` uses the stored sensor-ID value for `value`, while `raw_storer.rb` places the original reading in a distinct `<sensor_id>_raw` entry and the calibrated result in the sensor-ID entry. Therefore, the frozen `value` fields are treated as **Smart Citizen source-platform reported results**, not asserted to be untouched electrical/raw sensor output. The inspected source commit is implementation evidence only; its exact equivalence to the production deployment has not been independently established.

### Historical aggregation and tuple time

The Smart Citizen implementation sends the requested aggregation function and rollup to KairosDB with `align_sampling: true`, then returns Kairos result timestamps as UTC `recorded_at` values. When `all_intervals=true` and the rollup is at least ten minutes, its code also generates expected interval times and merges close real/empty entries using a tolerance of ten percent of the rollup period. This implementation evidence explains why the frozen 1-hour histories can contain timestamps slightly offset from exact hour boundaries. For the experiment, preserve the returned tuple time exactly and the explicit `rollup=1h` / `function=avg`; do **not** manufacture exact phenomenon-time interval boundaries until the target time model and source aggregation semantics are reviewed together.

### Deferred nonselected-channel unit normalization

The current representative mapping set does not require normalization of `#/0.1l` particle-number units, `um` typical-particle-size units, or `uW/cm2` ultraviolet units. Those source strings and their missing unit-definition URIs are preserved in the native inventory. Unit normalization for those channels is explicitly deferred rather than silently guessed.

### Remaining mapping-level uncertainties

The source characterization is sufficient to begin formal mapping, but several questions properly move into the mapping ledger rather than blocking Phase 2:

1. whether the OGC System identity should use the Smart Citizen registration UUID directly, preserve it only as a source identifier, or use an integration-local identity while keeping the source UUID as an external identifier;
2. how to represent the environmental feature of interest for air temperature, humidity, pressure and particulate observations without inventing a physical SamplingFeature from a display label;
3. whether and how parent Smart Citizen Sensor catalogue records should become SensorML components or reusable Procedure/model descriptions;
4. whether source-platform location should remain metadata only or can support a bounded Deployment/SamplingFeature after its spatial meaning and applicability are established.

## 8. Supplemental source-vocabulary evidence

A corrected supplemental capture was completed at `2026-10-25T03:00:10Z` and is retained at [`Docs/Research/Evidence/Smart_Citizen/Vocabulary/20261025T030010Z`](../../../Evidence/Smart_Citizen/Vocabulary/20261025T030010Z/). It freezes the Smart Citizen Measurement records actually referenced by the representative mapping set—Air Temperature `1`, Relative Humidity `2`, Noise Level `4`, battery `7`, PM2.5 `14`, Barometric Pressure `25`, RSSI `78`, and SD-Card Presence `79`—plus parent Sensor catalogue records `52`, `54`, `57`, and `192`.

The corrected source vocabulary establishes several useful native meanings. Battery is defined by Smart Citizen as the SCK remaining battery level in percentage; RSSI is the received signal-strength indication measuring power present in a received radio signal; and SD-card presence uses `1` for inserted while `0` means either absent **or corrupted**. The SHT31 parent record describes a digital relative-humidity and air-temperature sensor, the SEN5X parent describes a light-scattering particulate sensor with additional NOx/VOC indexes, and the ICS43432 parent describes a digital MEMS microphone with custom audio processing.

The first supplemental capture at `2026-10-25T02:57:59Z` requested incorrect Measurement IDs for four intended concepts because the workflow lookup list was authored incorrectly. The frozen device specimen was unaffected; the error was limited to the supplemental vocabulary lookup. The incorrect capture is retained as audit history, the workflow was corrected, and the corrected vocabulary set above is the authoritative supplemental source for mapping.

## 9. Phase gates


**Phase 1 — Freeze specimen: complete.** The exact current device body, response headers, two bounded history responses, request URLs, sizes and SHA-256 values are retained under the frozen-evidence commit.

**Phase 2 — Characterize native source: complete for the representative first mapping set.** The channel inventory, identity scopes, platform-state semantics, location standing, temporal differences, source aggregation implementation and deferred nonselected-channel questions are recorded. Remaining identity/feature-of-interest/component questions are now formal mapping questions and are carried into Phase 3 rather than being resolved implicitly in code.
