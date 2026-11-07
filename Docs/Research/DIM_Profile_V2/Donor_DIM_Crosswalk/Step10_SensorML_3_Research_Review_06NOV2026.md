# Step10 — SensorML 3.0 original clauses and JSON schema donor review

**6 November 2026 · STEP10 source-driven iteration · Original clause review, not DIM adoption or OGC compliance testing.** Published original: [OGC SensorML Encoding Standard 23-000, v3.0](https://docs.ogc.org/is/23-000/23-000.html), publication 16 July 2025; official [normative JSON schemas](https://schemas.opengis.net/sensorML/3.0/json/).

## 1. What we actually learned

SensorML 3.0 gives us a mature way to describe sensing and computational processes, their parts, information flow, methods, settings and deployment context. A **PhysicalComponent** is a physical process not further subdivided by the description. A **PhysicalSystem** is an aggregate whose components and their data connections are described. Those are useful but cannot automatically be equated with our entire DIM, a physical bill of materials, or a CSAPI System resource.

Two source-native correspondences were absent from the old SensorML sample and now belong in existing provisional rows: **ObservableProperty** on the observed/observable-property row, and **Deployment.platform/location/deployedSystem** on the station/hosting-context row. Eight older SensorML matches were rechecked and refined. These are improvements to the crosswalk, not ten approved DIM requirements.

An important distinction is that **SensorML 3.0 defines normative JSON, not the XML syntax of earlier versions**. Source data sheets, vendor manuals and anecdotal XML from other assistants cannot be treated as valid SensorML 3.0 JSON without a schema-based encoding and a source-backed translation.

## 2. Ten source-checked SensorML mappings

Each entry below is tied to an exact OGC clause and the relevant official JSON schema. **DIRECT** refers to a narrowly matching native term, not an assertion that our DIM element is adopted or that a deployed sensor conforms.

| Proposed DIM element | Exact SensorML term / relation | Original standard + schema | Non-equivalence to preserve |
| --- | --- | --- | --- |
| S06-R002 — Product model designation | AbstractProcess.typeOf → general process/model — **PARTIAL** | [OGC §8.2.9.3 / Requirements 13–15; §9.1.5.1](https://docs.ogc.org/is/23-000/23-000.html) · [JSON schema](https://schemas.opengis.net/sensorML/3.0/json/AbstractProcess.json) | A model designation is not automatically the general process URI, nor proof of an individually installed unit. |
| S06-R004 — Persistent System identifier | DescribedObject.uniqueId — **PARTIAL** | [OGC §8.2.2 Requirement 8; §9.1.1 JSON description](https://docs.ogc.org/is/23-000/23-000.html) · [JSON schema](https://schemas.opengis.net/sensorML/3.0/json/DescribedObject.json) | A SensorML process ID does not automatically establish a physical manufacturer's serial number or a CSAPI System resource ID. |
| S06-R005 — Described sensing System / arrangement | PhysicalSystem (aggregate physical process) — **PARTIAL** | [OGC §8.6 Requirement 33; §9.5.2 Requirement 50](https://docs.ogc.org/is/23-000/23-000.html) · [JSON schema](https://schemas.opengis.net/sensorML/3.0/json/PhysicalSystem.json) | Not every referenced arrangement is a verified deployed, permanently assembled individual; the standard also represents reusable datasheets. |
| S06-R007 — Physical constituent | PhysicalComponent + PhysicalSystem.components — **PARTIAL** | [OGC §8.5.2 Requirement 31; §8.6 Requirement 33; §9.5.2](https://docs.ogc.org/is/23-000/23-000.html) · [JSON schema](https://schemas.opengis.net/sensorML/3.0/json/PhysicalSystem.json) | A SensorML process component is not automatically a separate manufactured module, a replaceable part or an installed constituent. |
| S06-R008 — Connected external equipment | AggregateProcess.connections (Link source/destination) — **RELATED** | [OGC §8.4.1 Requirement 24; §9.3.4](https://docs.ogc.org/is/23-000/23-000.html) · [JSON schema](https://schemas.opengis.net/sensorML/3.0/json/AggregateProcess.json) | A process/data-flow connection does not prove a physical cable, an electrical bus or externally connected hardware. |
| S06-R009 — Hosting platform / station context | Deployment.platform / location / deployedSystem — **PARTIAL** (new) | [OGC §8.9.2–8.9.3 Tables 2–3; §9.6 Deployment Schema](https://docs.ogc.org/is/23-000/23-000.html) · [JSON schema](https://schemas.opengis.net/sensorML/3.0/json/Deployment.json) | A station or platform location is not automatically an individual probe survey; no exact historical service interval can be invented. |
| S06-R010 — Observing procedure / method | ProcessMethod (methodology) — **PARTIAL** | [OGC §8.3.2; Requirement 20 in §8.3](https://docs.ogc.org/is/23-000/23-000.html) · [JSON schema](https://schemas.opengis.net/sensorML/3.0/json/SimpleProcess.json) | An algorithmic process description is not an actual performed observation, a verified running program, or automatically an OMS observing Procedure. |
| S06-R012 — Reported output field | AbstractProcess.outputs (SWE DataComponent) — **PARTIAL** | [OGC §8.2.9.1 Requirement 11; §9.1.5 / AbstractProcess.json](https://docs.ogc.org/is/23-000/23-000.html) · [JSON schema](https://schemas.opengis.net/sensorML/3.0/json/AbstractProcess.json) | A process output declaration is not necessarily a transmitted native field, physical channel, SWE record value or CSAPI DataStream schema. |
| S06-R013 — Observed / observable property | ObservableProperty (physical stimulus/property) — **DIRECT** (new) | [OGC §8.2.1; §8.2.9.1; AbstractProcess.json $defs/IOComponentChoice](https://docs.ogc.org/is/23-000/23-000.html) · [JSON schema](https://schemas.opengis.net/sensorML/3.0/json/AbstractProcess.json) | ObservableProperty is not itself a measured Quantity or a performed Observation; SWE field types and numerical results remain distinct. |
| S06-R016 — Supported operating mode | AbstractProcess.modes / Mode.configuration — **PARTIAL** | [OGC §8.8.1 Requirement 39; §8.8.2 Requirement 40; Mode.json / Settings.json](https://docs.ogc.org/is/23-000/23-000.html) · [JSON schema](https://schemas.opengis.net/sensorML/3.0/json/Mode.json) | A declared capability/mode list is not a source-observed active mode or actual applied settings from a fielded individual. |

## 3. Nine native-source leads kept on hold

These source facts are relevant but do not justify inserting a new DIM row or claiming an installed device has the corresponding information. Each remains a qualified *lead*, not an approved model commitment.

| Lead | Related current row / hold | Original SensorML concept | Why not yet a confirmed DIM match |
| --- | --- | --- | --- |
| SML-H01 | S06-R001 | [Manufacturer / contact responsible party](https://docs.ogc.org/is/23-000/23-000.html) — §8.2.6; DescribedObject.json | Contacts can include manufacturers, owners or maintenance staff but have distinct responsibility roles. A contact is not a guaranteed manufacturer-name field. |
| SML-H02 | S06-R003 | [Serial number in instance-specific identification metadata](https://docs.ogc.org/is/23-000/23-000.html) — §8.2.9.3.1; §8.2.2 | The standard's OEM instance example lists serial as possible additional information; no universal dedicated numeric hardware serial attribute was established by this review. |
| SML-H03 | CASE-H01 | [DescribedObject.history / EventList](https://docs.ogc.org/is/23-000/23-000.html) — §8.2.8; Event.json | History events can describe calibration, maintenance and deployment; they do not by themselves prove exact equipment role intervals, exact swap time or hardware serial join. |
| SML-H04 | CASE-H02 | [Deployment.location / platform / deployedSystems](https://docs.ogc.org/is/23-000/23-000.html) — §8.9 Tables 2–3; Deployment.json | Source supports deployment spatial/mounting context, not an individually surveyed probe point or an authenticated as-operated station graph. |
| SML-H05 | CASE-H04 | [DescribedObject.characteristics / capabilities](https://docs.ogc.org/is/23-000/23-000.html) — §8.2.4–8.2.5; DescribedObject.json | Performance/energy design properties may be described but do not establish actual battery charge, health, or observed runtime. |
| SML-H06 | CASE-H03 | [DataInterface + AggregateProcess connections](https://docs.ogc.org/is/23-000/23-000.html) — §8.2.9.1; §8.4.1; §9.3.4 | A data/process interface and connected process flow are not automatically a LoRaWAN port, SDI-12 wire, physical bus or verified active reporting path. |
| SML-H07 | CASE-H06 | [AbstractProcess.configuration / Settings.setValues, setModes](https://docs.ogc.org/is/23-000/23-000.html) — §8.2.9.3.2 Requirement 15; §8.8.2; Settings.json | Specific configured descriptions are source-representable, but a manufacturer's design setting is not evidence of the currently effective setting. |
| SML-H08 | CASE-H07 | [ProcessMethod / process chain components](https://docs.ogc.org/is/23-000/23-000.html) — §8.3.2; §8.4.1 | Process/transform lineage may be documented, but the source does not prove a Campbell program executed or an AirGradient correction method is validated. |
| SML-H09 | CASE-H08 | [DerivedProperty.baseProperty / statistic / qualifier](https://docs.ogc.org/is/23-000/23-000.html) — §8.10.2 Table 4; DerivedProperty.json | A statistical/qualified property supports mean-temperature semantics; it does not assert original event time, derived contributor identity or performed observations. |

## 4. Four examples that guard against a false match

**Dragino S31-LB.** The manufacturer description includes one external SHT31 probe and separate temperature and humidity report fields. SensorML can model a physical process and output descriptions, but the source does not prove a real deployed unit, a physical identity for each output, or performed field Observations.

**AirGradient Open Air Max.** Two actual *design modules* at PM1/PM2 connectors differ from the three particulate-size properties represented by pm01/pm25/pm10. A SensorML process component is not one output field. A SensorML connection is process data flow, **not** automatically a PCB connection or network cable.

**Campbell CR1000X / first-generation ClimaVue 50.** The source shows a candidate externally connected logger and sensing assembly, plus fourteen ordered ClimaVue response fields and a separately published logger-only Status example. SensorML processes and outputs can retain these roles, but none of this proves one running installation or a valid actual API observation.

**Bennett's Point.** The station has genuine historical equipment-service statements, station location and two NOAA 15-minute mean air-temperature events. SensorML Deployment can describe location/platform/deployed systems; DerivedProperty supports statistic/qualifier semantics. But the station site coordinate is not an individually surveyed EE181 probe coordinate; original NOAA resultTime and exact probe handoff time remain unavailable.

## 5. Technical source boundaries

- **Model versus device:** Original SensorML 3.0 §8.2.9.3 uses a manufacturer model referenced through typeOf, with optional instance-only serial, calibration and location information. A referenced model does not authenticate a deployed item.
- **Metadata:** DescribedObject.uniqueId is required, but identifiers can name either a process type or particular described object; it does not independently supply an authentic hardware serial number.
- **Observable property versus result:** ObservableProperty describes an observable phenomenon/property; a SWE Common Quantity is a representation of a measured value. Neither establishes an actual performed event.
- **Component and connection:** PhysicalComponent/PhysicalSystem model physically situated processes and component lists; AggregateProcess.connections defines source-to-destination **data links**, not physical cabling by default.
- **Modes and configuration:** Modes enumerate selectable collections of settings; configuration denotes documented configured values. A declaration is not evidence of currently applied settings or actual Commands. Requirement 39 states that a declared mode list includes at least two modes.
- **Deployment and history:** Metadata and event classes can describe location, platform, service and changes when source evidence is available. No Bennett exact serial replacement instant or present-day operational state is inferred.
- **Version discipline:** SensorML v3.0 normative JSON schemas checked; no v2.x XML element was taken as a source-native v3.0 JSON term; SWE Common 3.0 donor mapping is Step11 and remains empty.

## 6. What changed and what did not

**Source-checked:** eight historical SensorML correspondences and two newly mapped existing proposed rows (ten total), nine native concepts separately held. The donor correspondence register rises from 51 to **53** records. There are **10 SensorML and 12 CSAPI source-checked entries**, and **31** mappings in other donor columns remain earlier historical extracts.

**Unchanged:** the owner-accepted 13 columns, 22 proposed DIM information rows, nine review-only case rows, 73 source-case records, 12 previous CSAPI original-clause mappings and all original non-SensorML donor text. The v0.3 working edition is preserved.

**Not accomplished:** a full SensorML 3.0 profile, live JSON schema validation of actual devices, authenticated physical sensing or control, original-issuer provenance or production CSAPI interoperability. No DIM/UML, application Profile, Glaux client, server or Cloudflare change was made.

**NEXT single owner 'proceed': Step11 — OGC SWE Common 3.0 original-source donor review only.**
