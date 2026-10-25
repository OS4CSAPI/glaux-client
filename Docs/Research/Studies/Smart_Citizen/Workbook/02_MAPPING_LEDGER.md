# 02 — Mapping ledger

**Status:** Phase 3 started. Three mappings have been formalized from the frozen 25 October specimen for resource-graph review. They are not yet executable adapter mappings and do not amend MPSS v0.3.5.

## Required chain

**native source assertion → underlying DIM concept → individual donor concept(s) → MPSS rule/binding → CSAPI resource/relationship → SensorML/SWE carrier → transformation → presentation implication → review outcome.**

A source vocabulary carried by Smart Citizen is recorded separately from a historical/model donor. An OGC encoding mechanism is recorded as a standard carrier even when its conceptual lineage also traces to SOSA/SSN. MERLIN-authored bindings and experiment-authored identity or naming choices remain explicitly ours.

## Mapping register

| Mapping ID | Source inventory | Status | Short description | Main unresolved issue |
| --- | --- | --- | --- | --- |
| SC-ID-01 | device top-level metadata | **proposed for resource-graph review** | Registered sensing-system identity and reusable SCK2.3 model description | exact CSAPI System UID policy and physical continuity beyond the source registration |
| SC-TEMP-01 | SC-SRC-019 | **proposed with temporal/subject qualification** | Current source-reported air-temperature observation | source supplies no separately identified feature of interest or result-time timestamp |
| SC-PM25-01 | SC-SRC-010 | **proposed with temporal/subject qualification** | Current source-reported PM2.5 observation | same subject/result-time issue; channel cadence differs from device-level latest time |
| SC-HUM-01 | SC-SRC-018 | **proposed with temporal/subject qualification** | Current relative-humidity observation | environmental feature of interest and resultTime remain unresolved |
| SC-PRESS-01 | SC-SRC-005 | **proposed with temporal/subject qualification** | Current barometric-pressure observation | environmental feature of interest and resultTime remain unresolved |
| SC-NOISE-01 | SC-SRC-020 | **proposed with processing qualification** | Current A-weighted sound-pressure-level observation | source documents custom audio processing but not a complete processing procedure |
| SC-BATT-01 | SC-SRC-004 | **proposed as System status measurement** | SCK remaining battery level percentage | no identified battery, supply topology, charging state, voltage or runtime |
| SC-RSSI-01 | SC-SRC-021 | **proposed as System/subsystem status measurement** | Wi-Fi received signal-strength indication | no separately modeled communications interface; RSSI is not interface oper-status |
| SC-SD-01 | SC-SRC-007 | **proposed as categorical System status** | SD-card presence/source status code | source code 0 conflates absent and corrupted; must not become Boolean health |
| SC-TEMP-AGG-01 | temperature history | **deferred** | Smart Citizen 1-hour average temperature history | source-platform aggregation provenance must not be misattributed to the physical kit |
| SC-PM25-AGG-01 | PM2.5 history | **deferred** | Smart Citizen 1-hour average PM2.5 history | source-platform aggregation provenance must not be misattributed to the physical kit |

---

# SC-ID-01 — Registered sensing system and reusable model

## Native source assertion

Frozen evidence: [device.json](../../../Evidence/Smart_Citizen/Captures/20261025T024348Z/device.json).

The source asserts a Smart Citizen Platform Device record with platform Device ID 19639, platform UUID 02612831-3387-4cb2-8bed-cf87670ca1e5, a user-facing name, and reported hardware SmartCitizen Kit 2.3 / SCK / version 2.3. The Smart Citizen Device ID and UUID identify the **platform registration**. They are not established manufacturer serial numbers and do not prove that a future re-registration could be reconciled automatically to the same enduring physical item.

The public response does not expose a physical serial or unfiltered hardware status message.

## Underlying DIM concept

The mapping invokes the DIM distinction between:
1. a **particular sensing-system instance**;
2. the **reusable description of its product/model kind**; and
3. the **source registration and representation provenance** through which information about the instance was obtained.

The experiment will represent the sensing-system instance known through registration 19639 as a CSAPI System while preserving the source registration identifiers as source identifiers/provenance. A reusable SCK2.3 model/datasheet description is a separate Procedure/model resource. This prevents the source registration ID, human-readable device name and product-model name from collapsing into one identifier.

## Individual donor concepts

| Donor / standard lineage | Exact concept | Edition / locator | Contribution invoked here | Reuse status |
| --- | --- | --- | --- | --- |
| SOSA/SSN | sosa:Sensor / ssn:System | W3C Recommendation 2017, §4.3.2.5 and System semantics | A sensing device is a System whose role is sensing/observing | conceptual lineage through CSAPI |
| RFC 8348 | model-name | RFC 8348 (2018), §7.1 ietf-hardware module | Separates vendor/model designation from serial/instance identity | donor concept adapted by MPSS technical description |
| RFC 8348 | hardware-rev | RFC 8348 (2018), §7.1 | Supports treating hardware/model revision separately from model name | donor concept adapted by MPSS technical description |
| RFC 8348 | mfg-name | RFC 8348 (2018), §7.1 | Constrains interpretation: manufacturer is a separate field and should be absent when not established | interpretive constraint; **not populated from the frozen source** |

Smart Citizen hardware.name, hardware.version and registration identifiers are **source vocabulary/data**, not historical DIM donors. The OGC System/Procedure and SensorML typeOf mechanisms below are target-standard carriers.

## MPSS binding

- **R01 — A System uses a reusable model description.**
- System.typeOf / CSAPI systemKind links the particular System to a reusable model description.
- P/group/technical-description carries selected model/technical Text properties using existing profile definitions.
- The mapping uses source-reported model designation SmartCitizen Kit 2.3 and revision/version 2.3.
- It does **not** populate manufacturer, firmware revision, physical serial, or asset ID from inference.
- R02/component modeling is not invoked merely because 21 channels are present; equipment composition is a separate mapping problem.

## OGC / SensorML representation

Proposed target structure:
- one CSAPI **System** with systemType = sosa:Sensor;
- one reusable CSAPI **Procedure** describing the SCK2.3 equipment kind/datasheet;
- System systemKind association → Procedure;
- SensorML System typeOf → Procedure;
- SensorML technical-description CharacteristicList using existing MPSS terms for model designation/revision;
- source Device ID and UUID retained as source identifiers/provenance, not silently promoted to manufacturer serial.

OGC API — Connected Systems Part 1 distinguishes System instances from Procedure/model descriptions and requires a URI-valued unique identifier for feature resources. The exact System and Procedure UIDs will be selected in the resource-graph phase. **The source registration UUID will not automatically become the CSAPI System UID**, because that would imply an enduring physical-identity assertion the source evidence does not establish.

## Transformation and presentation

No unit or value conversion occurs. Presentation may use the source name as a human-readable label while separately showing the reported product model and the Smart Citizen source registration. Operator presentation must not label the platform UUID as “serial number.”

Likely Resource Details use:
- persistent header: resource name / experiment-assigned System identity / source;
- Overview or Equipment: reported model SCK2.3 and source-registration identifiers;
- source disclosure: Smart Citizen Platform registration 19639.

## Review outcome

**Status: proposed for resource-graph review.**

Accepted semantic decisions:
- System instance and reusable model are distinct;
- source registration identifiers are not physical serials;
- product model/version can support technical-description content;
- manufacturer remains unpopulated unless independently evidenced.

Open decision:
- choose a stable CSAPI System UID representing the study's system identity while preserving the Smart Citizen registration UUID as a source identifier. The UID choice belongs in Phase 4 and must survive replay without claiming a manufacturer-issued identity.

---

# SC-TEMP-01 — Current air-temperature result

## Native source assertion

Frozen evidence: device.json → /data/sensors/18. Historical source series is retained separately and is **not** part of this current-reading mapping.

Source values:
- sensor catalogue ID 55;
- source label Sensirion SHT31 - Temperature;
- measurement Air Temperature;
- value 19.59;
- source unit ºC;
- unit definition https://qudt.org/vocab/unit/DEG_C;
- observable-property definition http://www.eionet.europa.eu/gemet/concept/281;
- channel last_reading_at = 2026-10-25T02:40:21Z;
- ancestry 54, indicating source catalogue hierarchy.

The inspected Smart Citizen API implementation indicates that the public Device value is a source-platform normalized/calibrated sensor result rather than proof of an untouched electrical/raw sample. That implementation evidence is not assumed to be the exact production revision, so the mapping describes the value as a **source-platform reported air-temperature result**.

## Underlying DIM concept

This is an **Observation result of an environmental property**, produced/reported by the sensing system. The observed property is air temperature; the kit is the producer, not automatically the thing whose temperature is being measured. The observed subject/feature of interest is therefore distinct from the System and remains only generically supported as the surrounding/ambient air environment by the source meaning.

The current mapping deliberately does not manufacture a physical SamplingFeature identifier or reinterpret the System itself as the FeatureOfInterest.

## Individual donor concepts

| Donor / source vocabulary | Exact concept | Edition / locator | Contribution invoked here | Standing |
| --- | --- | --- | --- | --- |
| SOSA/SSN | sosa:Sensor | W3C 2017, §4.3.2.5 | Producer role: a Sensor generates observation results | conceptual donor through CSAPI |
| SOSA/SSN | sosa:Observation | W3C 2017, §4.3.2.2 | Distinguishes observation from System and result | conceptual donor through CSAPI |
| SOSA/SSN | sosa:ObservableProperty / sosa:observedProperty | W3C 2017, §4.3.2.1 and §4.3.2.3 | Property remains distinct from value and subject | conceptual donor through CSAPI |
| SOSA/SSN | sosa:FeatureOfInterest | W3C 2017 observation model | The property belongs to a subject distinct from the producer | conceptual constraint; actual target feature not yet identified |
| SOSA/SSN | sosa:Result / sosa:hasResult | W3C 2017 observation model | Separates result from property and observation | conceptual donor through CSAPI |
| SOSA/SSN | sosa:phenomenonTime / sosa:resultTime | W3C 2017, §4.3.2.4 and observation constraints | Applicability time remains distinct from result availability time | conceptual constraint; source supplies only one reading timestamp |
| GEMET | concept 281 Air Temperature | source-provided URI | Identifies native observable property | **source vocabulary**, not established DIM donor |
| QUDT | unit:DEG_C | source-provided URI | Identifies degree Celsius | **source vocabulary**, not established DIM donor |

## MPSS binding

- **R10**: declared output ↔ DataStream product correspondence.
- **R11**: producer, observed subject and temporal context remain distinguishable.
- MPSS v0.3.5 §5.8 is the current paper's locator for R10/R11.
- Full R09/R10 profile-aware function binding is **not yet complete**, because the experiment has not selected a sensing-function vocabulary/identifier for this source. Base OGC output/DataStream representation can proceed without inventing that profile term.

## OGC / SensorML / SWE representation

Proposed current-result carrier:
- System SensorML outputs[] contains a SWE **Quantity** for local output name airTemperature;
- Quantity definition = http://www.eionet.europa.eu/gemet/concept/281;
- Quantity uom.href = https://qudt.org/vocab/unit/DEG_C;
- one CSAPI **DataStream** associated with the System, type=observation, resultType=measure, outputName=airTemperature;
- one CSAPI **Observation** result carries numeric 19.59.

Target subject handling:
- do **not** set the System as the observation's feature of interest;
- do **not** invent a SamplingFeature merely to populate the association;
- CSAPI permits the sampling-feature association to be absent, so an initial target representation may preserve the subject as unresolved while retaining property/result correctly.

Target time handling:
- channel last_reading_at is the best available **source-recorded observation time** and is a strong candidate for phenomenonTime;
- CSAPI also requires resultTime, but Smart Citizen provides no separate result-availability timestamp in the frozen response;
- capture/retrieval time 02:43:48Z is **not** a substitute for source result time because it describes our acquisition;
- Phase 4 must choose/document a result-time fallback or obtain an additional source timestamp before executable Observation requests are finalized.

## Transformation and presentation

No numerical/unit conversion is required. Local output name airTemperature and display label are experiment-authored. Source channel ID, catalogue UUID, source label, property URI, unit URI and timestamp remain traceable.

Operator presentation should be able to answer:
- current reported air temperature;
- unit and semantic property;
- source observation time;
- reporting System;
- observed subject is not independently identified.

The client must not show the value as “device temperature.”

## Aggregate-history boundary

The 24 one-hour averages in temperature_history.json are **not folded into SC-TEMP-01**. They are source-platform aggregate products created by the Smart Citizen/Kairos processing path and require their own provenance/procedure decision (SC-TEMP-AGG-01) before CSAPI ingestion. This avoids misrepresenting a platform-derived hourly average as a direct physical-sensor observation.

## Review outcome

**Status: proposed with temporal/subject qualification.**

Semantically accepted:
- property URI;
- unit URI;
- scalar result;
- producer System;
- source observation timestamp must be preserved;
- System must not silently become the observed subject.

Open before executable request:
1. CSAPI resultTime policy for a source that supplies only one reading timestamp;
2. whether to omit samplingFeature or create an explicitly integration-authored ambient-air SamplingFeature in Phase 4;
3. sensing-function/function-binding vocabulary if full MPSS R09/R10 interpretation is desired.

---

# SC-PM25-01 — Current PM2.5 mass-concentration result

## Native source assertion

Frozen evidence: device.json → /data/sensors/9.

Source values:
- sensor catalogue ID 194;
- source label Sensirion SEN5X - PM2.5;
- measurement PM2.5;
- description identifies particulate matter below 2.5 µm;
- value 9.3;
- unit ug/m3;
- unit definition http://dd.eionet.europa.eu/vocabulary/uom/concentration/ug.m-3;
- property definition http://dd.eionet.europa.eu/vocabulary/aq/pollutant/6001;
- channel last_reading_at = 2026-10-25T02:36:21Z;
- ancestry 192, indicating SEN5X catalogue hierarchy.

The device-level last_reading_at is 02:40:21Z, four minutes later. The PM2.5 mapping therefore uses the **channel timestamp**, not the Device record's latest-reading time.

## Underlying DIM concept

This is an Observation result of an environmental particulate-matter property, produced/reported by the sensing System. As with temperature, the ambient/environmental subject is not the kit itself. The mapping preserves the distinction among producer, particulate property, source-platform reported result, and unresolved feature of interest.

## Individual donor concepts

| Donor / source vocabulary | Exact concept | Contribution invoked here | Standing |
| --- | --- | --- | --- |
| SOSA/SSN | Sensor, Observation, ObservableProperty, FeatureOfInterest, Result, phenomenonTime, resultTime | Same producer/property/subject/result/time distinctions as SC-TEMP-01 | conceptual donor through CSAPI |
| Eionet AQ vocabulary | pollutant 6001 | Source-provided definition of PM2.5 property | **source vocabulary**, not established DIM donor |
| Eionet UOM vocabulary | concentration ug.m-3 | Source-provided unit definition | **source vocabulary**, not established DIM donor |

The source's SEN5X sensor name and ancestry are source catalogue/equipment metadata. They are not, by themselves, an MPSS equipment-role mapping.

## MPSS binding

- **R10**: output/DataStream correspondence.
- **R11**: producer, subject and time remain distinct.
- Full R09/R10 sensing-function binding is deferred until a reviewed function vocabulary is selected.
- No R20 health/assessment interpretation arises from a PM concentration value.

## OGC / SensorML / SWE representation

Proposed current-result carrier:
- SensorML output name pm25 (experiment-authored local name);
- SWE Quantity definition = http://dd.eionet.europa.eu/vocabulary/aq/pollutant/6001;
- uom.href = http://dd.eionet.europa.eu/vocabulary/uom/concentration/ug.m-3;
- CSAPI DataStream associated with the System, type=observation, resultType=measure, outputName=pm25;
- Observation result 9.3.

Subject handling follows SC-TEMP-01: the System is not substituted for ambient air, and a SamplingFeature is not invented simply to complete the graph.

Time handling follows the **channel-specific** 2026-10-25T02:36:21Z. Device-level 02:40:21Z and adapter capture time are different facts and remain separate. The same unresolved CSAPI resultTime policy applies.

## Transformation and presentation

No numerical conversion is proposed. The source property/unit URIs are retained even though the lexical unit label (ug/m3) may later be rendered typographically as µg/m³ for humans. Such display normalization must not change the underlying source URI/value relationship.

Operator presentation should expose PM2.5 value, unit, channel timestamp and property meaning. The four-minute difference from newer source channels is information; it is **not** automatically a stale-data alarm because an expected cadence/freshness rule has not been established.

## Aggregate-history boundary

The 24 one-hour PM2.5 averages in pm25_history.json are a separate source-platform aggregate product with sample_size=288. They require their own mapping (SC-PM25-AGG-01) so that source-side aggregation/provenance is not misattributed to the physical Sensor.

## Review outcome

**Status: proposed with temporal/subject qualification.**

Semantically accepted:
- property and unit definition URIs;
- scalar current result;
- producer System;
- channel-specific timestamp;
- explicit separation from device-level latest time.

Open before executable request:
1. result-time fallback;
2. feature-of-interest/SamplingFeature policy;
3. full function-binding vocabulary;
4. whether the source catalogue parent SEN5X should later be represented as an embedded component/model after its parent record is frozen and reviewed.

---

# SC-HUM-01 — Current relative-humidity result

## Native source assertion

Frozen evidence: device.json → /data/sensors/17. The source reports sensor catalogue ID 56, label Sensirion SHT31 - Humidity, value 65.54, unit %, unit definition https://qudt.org/vocab/unit/PERCENT, property definition https://qudt.org/vocab/quantitykind/RelativeHumidity, and channel time 2026-10-25T02:40:21Z. Its ancestry points to catalogue parent 54, whose separately frozen record describes Sensirion SHT31 as a digital relative-humidity and air-temperature sensor.

## DIM / donor / MPSS interpretation

This is an environmental Observation result produced by the sensing System, not a humidity property of the kit itself. It reuses the same SOSA/SSN Sensor, Observation, ObservableProperty, FeatureOfInterest, Result and temporal distinctions as SC-TEMP-01. QUDT RelativeHumidity and PERCENT are source-carried vocabulary references, not newly claimed historical DIM donors. MPSS R10/R11 apply; R02 component modeling remains a separate question because the source catalogue parent does not identify a unique physical SHT31 instance in registration 19639.

## Proposed OGC representation

- SensorML output local name relativeHumidity.
- SWE Quantity definition = https://qudt.org/vocab/quantitykind/RelativeHumidity.
- SWE unit href = https://qudt.org/vocab/unit/PERCENT.
- CSAPI DataStream type observation, resultType measure, produced by the System.
- Observation result = 65.54 and channel source time = 2026-10-25T02:40:21Z.
- Feature of interest and separate resultTime remain unresolved under the same policy as SC-TEMP-01.

**Status:** proposed with temporal/subject qualification.

---

# SC-PRESS-01 — Current barometric-pressure result

## Native source assertion

Frozen evidence: device.json → /data/sensors/4. The source reports sensor catalogue ID 58, label NXP MPL3115A2 - Barometric Pressure, value 101.69 kPa, QUDT unit KiloPA, QUDT AtmosphericPressure property definition, and source time 2026-10-25T02:40:21Z. Its ancestry points to catalogue parent 57, MPL3115A2, described by Smart Citizen as a digital barometric-pressure sensor.

## DIM / donor / MPSS interpretation

This is an environmental atmospheric-pressure Observation, with the System as producer and an environmental feature of interest distinct from the producer. SOSA/SSN supplies the observation-role distinctions; QUDT property/unit URIs are source-carried vocabulary. MPSS R10/R11 apply. The catalogue parent is useful model/equipment evidence but does not establish an independently identified installed component.

## Proposed OGC representation

- SensorML output local name barometricPressure.
- SWE Quantity definition = https://qudt.org/vocab/quantitykind/AtmosphericPressure.
- SWE unit href = https://qudt.org/vocab/unit/KiloPA.
- CSAPI DataStream type observation, resultType measure.
- Observation result = 101.69 at source channel time 2026-10-25T02:40:21Z.
- Environmental feature of interest and separate resultTime remain unresolved.

**Status:** proposed with temporal/subject qualification.

---

# SC-NOISE-01 — Current A-weighted sound-pressure-level result

## Native source assertion

Frozen evidence: device.json → /data/sensors/19. The source reports sensor catalogue ID 53, label TDK ICS43432 - Noise Level A weighting, value 31.28 dBA, unit URI https://qudt.org/vocab/unit/DeciB_A, property URI https://qudt.org/vocab/quantitykind/SoundPressureLevel, and source time 2026-10-25T02:40:21Z. The frozen parent Sensor catalogue record 52 describes ICS43432 as an I2S digital MEMS microphone with a custom audio-processing algorithm.

## DIM / donor / MPSS interpretation

The mapped product is a scalar sound-pressure-level result, **not an audio waveform, recording, detection, classification, or media product**. SOSA/SSN supplies producer/property/subject/result distinctions; QUDT supplies source-carried property and unit references. MPSS R10/R11 apply. The source documents that processing occurs, but it does not provide enough information here to model a complete processing Procedure or claim that the value is raw microphone output.

## Proposed OGC representation

- SensorML output local name noiseLevelA.
- SWE Quantity definition = https://qudt.org/vocab/quantitykind/SoundPressureLevel.
- SWE unit href = https://qudt.org/vocab/unit/DeciB_A.
- CSAPI DataStream type observation, resultType measure.
- Observation result = 31.28 at source channel time 2026-10-25T02:40:21Z.
- Environmental acoustic feature of interest and separate resultTime remain unresolved.

**Status:** proposed with processing, temporal and subject qualification.

---

# SC-BATT-01 — SCK remaining battery-level status

## Native source assertion

Frozen evidence: device.json → /data/sensors/3, plus Smart Citizen Sensor catalogue record 10 and Measurement record 7. The source reports 99% at 2026-10-25T02:40:21Z. Sensor 10 is Battery SCK, has no parent catalogue sensor, and Measurement 7 defines the property as “The SCK remaining battery level in percentage.” Neither source record supplies an external semantic-definition URI.

## Underlying DIM concept and donor constraints

This is changing **System power/status information**, not evidence of a separately identified battery object. MPSS R17 says changing power information belongs in DataStream/Observation representations with producer and observed subject kept correct; R16 supply topology is not invoked because the source supplies no battery identity, interface, supply edge, or replacement event. RFC 7326 power-source/metering concepts therefore constrain against inventing topology. RFC 7577 batteryActualCharge and batteryActualVoltage are not equivalent to this percentage and are not mapped.

## Proposed OGC / SWE representation

- CSAPI DataStream type status, because the source property is explicitly the SCK's remaining battery level.
- resultType measure.
- SensorML/SWE output local name batteryLevel, represented as Quantity.
- Quantity definition = https://api.smartcitizen.me/v0/measurements/7, an experiment-selected resolvable URI for the source Measurement concept because Smart Citizen supplies no external definition URI.
- uom code = %; no external unit URI is invented.
- Observation result = 99 and phenomenon/source time = 2026-10-25T02:40:21Z.
- The parent System is the intended status subject; no battery SamplingFeature/System is created.

Using the Smart Citizen Measurement resource URL as the SWE/CSAPI property definition is an **experiment-authored preservation choice**, not a claim that Smart Citizen publishes an ontology. It keeps the source concept dereferenceable without inventing a MERLIN battery ontology term.

## Presentation constraints

Display may say source-reported battery level 99%. It must not add charge in mAh, voltage, charging state, runtime, battery identity, full-charge assessment, or supply topology. A later owned-kit experiment can add physical battery/supply evidence separately.

**Status:** proposed as System status measurement; separate CSAPI resultTime policy remains open.

---

# SC-RSSI-01 — Wi-Fi received-signal-strength status

## Native source assertion

Frozen evidence: device.json → /data/sensors/20, plus Sensor catalogue record 220 and Measurement record 78. The source reports -45 dBm at 2026-10-25T02:40:21Z. Sensor 220 is named Wi-Fi Antenna - RSSI, carries source tags system and raw, has no parent catalogue sensor, and Measurement 78 defines RSSI as a measurement of power present in a received radio signal.

## Underlying DIM concept and donor constraints

This is equipment/communications-related telemetry, not an environmental observation. CSAPI status streams are intended for observations of the parent System or its subsystems, so a status DataStream is the best base carrier while the Wi-Fi antenna/interface is not independently modeled. MPSS R13 and its RFC 8343/RFC 2863 donors constrain interpretation: RSSI is **not** interface-enabled, interface type, interface operational status, link availability, or network reachability. The source does not supply enough interface identity/type information to instantiate the full R13 communications-interface group.

## Proposed OGC / SWE representation

- CSAPI DataStream type status, resultType measure.
- SensorML/SWE output local name wifiRssi represented as Quantity.
- Quantity definition = https://api.smartcitizen.me/v0/measurements/78.
- uom code = dBm; the source does not provide a unit-definition URI.
- Observation result = -45 at source time 2026-10-25T02:40:21Z.
- The source's Wi-Fi-antenna qualification is retained in description/provenance; no interface System/component or communication link is invented.

## Presentation constraints

Display as source-reported Wi-Fi RSSI, not “Wi-Fi health,” “connected,” “link up,” or “signal quality” unless a separately supported interpretation threshold is adopted. The source's system tag online is a separate 60-minute platform heuristic and is not derived from this -45 dBm result.

**Status:** proposed as System/subsystem status measurement; full MPSS R13 interface mapping remains incomplete by source limitation.

---

# SC-SD-01 — SD-card presence/status code

## Native source assertion

Frozen evidence: device.json → /data/sensors/6, plus Sensor catalogue record 221 and Measurement record 79. The source reports numeric code 1 at 2026-10-25T02:40:21Z. Measurement 79 defines 1 as a microSD card inserted in the kit and 0 as either no card **or a corrupted card**. Sensor 221 carries source tags system and raw and has no parent catalogue sensor.

## Underlying DIM concept and negative constraints

This is a categorical System/subsystem status assertion. It is not a Boolean health property because code 0 deliberately conflates at least two source states. It is also not an MPSS R20 assessment result: the source supplies a device indicator, not an assessment procedure, assessor, evidence chain, or readiness judgment.

## Proposed OGC / SWE representation

- CSAPI DataStream type status.
- resultType record, using a one-field SWE DataRecord so the categorical field is not mislabeled as a unit-bearing measure.
- DataRecord field local name sdCardPresence, type Category.
- Category definition = https://api.smartcitizen.me/v0/measurements/79.
- Category constraint enumerates string tokens 0 and 1; no separate code-space vocabulary is claimed.
- The adapter converts native numeric 1/0 to categorical tokens "1"/"0" while preserving the original numeric source value in provenance.
- Observation current value = "1" at source time 2026-10-25T02:40:21Z.

SWE Common requires Category to define a code space or enumerated allowed tokens; using the two source-supported tokens preserves the native coding without inventing a third “corrupt” state that the source cannot distinguish.

## Presentation constraints

Code 1 may be explained as card inserted. Code 0 must be displayed as the source's combined “absent or corrupted” meaning, not as simply absent, false, failed, or unhealthy. No overall storage health/readiness value is inferred.

**Status:** proposed as categorical System status; separate CSAPI resultTime policy remains open.

---
## Deferred mappings and negative constraints

### SC-TEMP-AGG-01 / SC-PM25-AGG-01

These are intentionally deferred because the public history endpoint is a **platform aggregation service**. Treating aggregate values as if the physical kit itself produced hourly averages would erase processing provenance. Phase 4 must decide whether aggregation is modeled as a separate Procedure/processing System, Observation parameters, a distinct DataStream product, or remains outside the first CSAPI load.

### SC-BATT-01

The paper's battery example remains illustrative until reworked against the frozen specimen. The frozen source confirms 99% with the source definition “remaining battery level in percentage,” but supplies no identified battery, charge in mAh, voltage, charging state, runtime, supply relationship or replacement history. RFC 7326/RFC 7577 concepts continue to constrain unsupported substitutions.

## Phase 3 working rules

1. No adapter code is authoritative for a mapping absent from this ledger.
2. Source registration identifiers are not physical serials.
3. A producer is not automatically the feature of interest.
4. Device-level latest time cannot overwrite channel time.
5. Acquisition time is integration provenance, not source result time.
6. Source-platform aggregates require explicit processing provenance.
7. Source vocabulary references are preserved without retroactively claiming they were historical DIM donors.
8. A profile-aware mapping may remain incomplete while a base OGC representation is still valid; the gap remains visible.

## Principal evidence and standards consulted

- Frozen source evidence: [20261025T024348Z](../../../Evidence/Smart_Citizen/Captures/20261025T024348Z/).
- MPSS baseline: [v0.3.5 Integrated Binding Draft](../../../../Design/MPSS/MERLIN_Managed_Physical_Sensing_Systems_Profile_Integrated_Binding_Draft_v0.3.5_17OCT2026.docx).
- Smart Citizen API reference: <https://developer.smartcitizen.me/>.
- Smart Citizen API implementation evidence: <https://github.com/fablabbcn/smartcitizen-api/tree/25a524cbfb036f8950c247b847d8884a4e776297>.
- OGC API — Connected Systems Part 1, §§8.5, 9.2, 13.2, 19.2: <https://docs.ogc.org/is/23-001/23-001.html>.
- OGC API — Connected Systems Part 2, §§9.2, 9.6, 9.7: <https://docs.ogc.org/is/23-002/23-002.html>.
- SensorML 3.0: <https://docs.ogc.org/is/23-000/23-000.html>.
- SWE Common 3.0: <https://docs.ogc.org/is/24-014/24-014.html>.
- SOSA/SSN 2017, especially §4.3.2: <https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/>.
- RFC 8348 §7.1: <https://www.rfc-editor.org/rfc/rfc8348.html>.
