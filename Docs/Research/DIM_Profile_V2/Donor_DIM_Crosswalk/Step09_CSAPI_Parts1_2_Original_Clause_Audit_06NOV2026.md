# Step09 — OGC API – Connected Systems Parts 1 & 2: original-clause mapping review

**6 November 2026 · source-driven technical iteration · 12/12 earlier CSAPI cells checked against the actual published OGC Parts 1 and 2. This is term/meaning qualification, NOT an adopted DIM or an OGC compliance test.** First owner-accepted horizontal format is retained: four source cases left → other donors → five grouped foundational standards → proposed DIM right.

## 1. What this means in plain English

The standard already draws several lines that our example table must respect. **System versus Procedure** distinguishes an individual API-described system from a type or datasheet; **subsystem and Deployment** support different relationships for built-in and temporarily deployed equipment. **DataStream** names an identified producer and observation/result schema; an underlying physical probe may still require separate source evidence. **Observation** and **Command** are time-varying resources, not proof that a manufacturer example happened. **CommandStatus** records execution progress, not independent physical outcome measurements.

The biggest genuinely useful addition for the whole-System objective is **Part 2 `SystemEvent`**: it already defines types for calibration, configuration changes, software updates, part replacement, relocation, deployment and decommissioning. That matters for Bennett's Point's probe-service history. **Part 1 `Deployment`** separately carries the validity period and deployed System/platform links. Neither fact licenses us to invent the exact EE181 swap minute, a verified completed Deployment graph or a 2026 operating condition.

## 2. Twelve existing CSAPI rows: what the original standard actually says

The **native source term** was checked against an original OGC section/table/requirement and explicitly qualified against our proposed DIM row; the proposed DIM row itself remains **not adopted**. `DIRECT` means a native field aligns with the narrowly worded row, `PARTIAL` and `RELATED` preserve semantic limitations. All 12 are written into the **CSAPI column and Donor Evidence sheet**, not simply documented in prose.

| Existing proposed DIM row | Original CSAPI source term in working master | Relation | Original OGC clause | Critical boundary |
| --- | --- | --- | --- | --- |
| S06-R002 — Product model designation | `systemKind → Procedure (type/datasheet)` | Partially related, with conditions | [Part 1 §9.1 Note 1; §9.2 Table 5](https://docs.ogc.org/is/23-001/23-001.html) | A model is reusable; a System remains an instance. Keep model ID separate from physical serial and API URL. |
| S06-R004 — Persistent System identifier | `System.uniqueIdentifier (URI)` | Direct native term only | [Part 1 §9.2 Table 4; §9.3 Requirement 5](https://docs.ogc.org/is/23-001/23-001.html) | A persistent System ID is not necessarily the manufactured item's physical serial. |
| S06-R005 — Described sensing System / arrangement | `System resource (instance)` | Partially related, with conditions | [Part 1 §9.1; §9.2 Tables 4–7](https://docs.ogc.org/is/23-001/23-001.html) | A focal reference arrangement, a manufactured assembly, a physical constituent, and a whole deployed station need not share one System identity. |
| S06-R007 — Physical constituent | `System.subsystems / parentSystem (composition or aggregation)` | Related or carrier, not same concept | [Part 1 §9.2 Table 5; §§10.2–10.3 Table 8; Requirement 9](https://docs.ogc.org/is/23-001/23-001.html) | A linked System or nested resource does not, by itself, prove a physical constituent, manufactured chip, permanently installed part or inspected cable. |
| S06-R009 — Hosting platform / station context | `Deployment.platform; System.systemType=Platform` | Partially related, with conditions | [Part 1 §9.1 Notes 2–3; §11.2 Tables 10–11](https://docs.ogc.org/is/23-001/23-001.html) | Deployment location, station/site context, and the actual individual probe position are distinct; platform need not be a System. |
| S06-R010 — Observing procedure / method | `Procedure.procedureType=ObservingProcedure` | Partially related, with conditions | [Part 1 §13.2 Tables 14–16; §9.2 Table 5](https://docs.ogc.org/is/23-001/23-001.html) | The Procedure resource can be a method OR datasheet kind; do not collapse executed behavior or processing implementation into a type link. |
| S06-R012 — Reported output field | `DataStream /schema → resultSchema` | Related or carrier, not same concept | [Part 2 §9.6 Requirement 11; §16.1.4 resultSchema; §16.1.5 Requirement 98](https://docs.ogc.org/is/23-002/23-002.html) | A named result field is not automatically a physical transducer channel or IEEE 1451 channel. |
| S06-R013 — Observed / observable property | `DataStream.observedProperties (URI list)` | Partially related, with conditions | [Part 2 §9.2 Table 2; Part 1 §15.1–15.2 Table 19](https://docs.ogc.org/is/23-002/23-002.html) | A property URI is not a reported field name, raw output channel, physical sensor module or evidence of an actual measurement. |
| S06-R014 — Observer / observing System | `DataStream.system (identified producer)` | Partially related, with conditions | [Part 2 §9.2 Table 5; §9.2 DataStream constraints](https://docs.ogc.org/is/23-002/23-002.html) | The stream-producing System may be a station/logger/process; the physically sensing contributor and original event issuer require independent evidence. |
| S06-R015 — Performed Observation | `Observation (DataStream member)` | Partially related, with conditions | [Part 2 §9.7 Tables 6–7; §9.8 Requirement 12](https://docs.ogc.org/is/23-002/23-002.html) | A valid API Observation representation does not authenticate a manufacturer example or prove a new original measurement event. |
| S06-R019 — Issued control request | `Command (ControlStream member)` | Partially related, with conditions | [Part 2 §10.2; §10.7 Tables 11–12](https://docs.ogc.org/is/23-002/23-002.html) | Published syntax, available command definitions, or manufacturer request flags are not evidence an actual Command was issued. |
| S06-R020 — Command acknowledgement / reported outcome | `CommandStatus.reportTime / statusCode` | Partially related, with conditions | [Part 2 §10.11 Tables 13–15](https://docs.ogc.org/is/23-002/23-002.html) | ACCEPTED is not execution success; a reported COMPLETED status should not be treated as independently measured physical effect. |

## 3. Native CSAPI concepts deliberately NOT forced into the nine held case rows

These **eight original-source findings** could help resolve our unresolved examples. Their correct disposition here is **source-confirmed lead / unapproved candidate relationship**, not a new DIM row, inferred vendor conformance or another 8 populated master cells.

| Source lead | Review-hold context | Native source capability | Source | Why still held |
| --- | --- | --- | --- | --- |
| C09-H01-A | CASE-H01 | `Deployment.validTime + deployedSystems + platform` | [§11.2 Tables 10–11](https://docs.ogc.org/is/23-001/23-001.html) | A time-bounded deployment can associate a System with a platform. It is a candidate carrier for installed/service roles, not evidence of a particular Bennett's Point probe join or exact swap minute. |
| C09-H01-B | CASE-H01 | `SystemEvent(type=PartReplacement), eventTime, system` | [§12.1–12.2 Tables 19–21](https://docs.ogc.org/is/23-002/23-002.html) | Part replacement is an event category, but a generic event record does not by itself specify full old/new serial IDs or the exact time of the Bennett EE181 change. |
| C09-H02 | CASE-H02 | `System.location / Deployment.location / Deployment.platform` | [§9.2 Table 4; §11.2 Tables 10–11](https://docs.ogc.org/is/23-001/23-001.html) | Station point or deployment area does not become the individually surveyed position of every probe. |
| C09-H05 | CASE-H05 | `DataStream.type=status / DataStream.system` | [§9.2 Tables 3 and 5](https://docs.ogc.org/is/23-002/23-002.html) | Diagnostic/status datastreams are conceptually supported, but no actual Campbell Status event from an installed station has been obtained. |
| C09-H06 | CASE-H06 | `SystemEvent(type=ConfigurationChange or SoftwareUpdate)` | [§12.2 Table 20](https://docs.ogc.org/is/23-002/23-002.html) | A dated change event does not furnish full previous/next configuration values or prove present effective settings. |
| C09-H07 | CASE-H07 | `Property.baseProperty / objectType / statistic` | [§15.1–15.2 Table 19](https://docs.ogc.org/is/23-001/23-001.html) | Property definitions can distinguish an hourly mean from basic temperature, but do not prove the processing method executed or the source-to-result causal chain. |
| C09-H08 | CASE-H08 | `Observation.phenomenonTime / resultTime / result` | [§9.7 Tables 6–7](https://docs.ogc.org/is/23-002/23-002.html) | These temporal properties are required in CSAPI representation; historical source data may not furnish original resultTime, so do not invent it. |
| C09-H09 | CASE-H09 | `ControlStream.live / async / controlledProperties; CommandStatus` | [§10.2 Tables 8–10; §10.11 Tables 13–14](https://docs.ogc.org/is/23-002/23-002.html) | A declared live control channel and status vocabulary are not proof of authenticated command execution or observed physical effect. |

## 4. Four concrete equipment contrasts

**Dragino S31-LB.** A manufacturer-described SHT31 probe and LoRaWAN end node can motivate a System/Procedure/subsystem comparison; it does **not** prove a unique fielded System resource or that example `TempC_SHT31` values are authentic live Observations.

**AirGradient Open Air Max.** Two documented PMS5003 modules at hardware sockets `PM1` and `PM2` are not the same as `pm01`, `pm25` and `pm10` result fields. CSAPI DataStream resultSchema is an information schema; it is not a physical hardware interface or transducer identity.

**Campbell CR1000X + first-generation ClimaVue 50.** A documented SDI-12 connection between two distinct products, 14 ClimaVue response definitions and a separately published 31-field logger Status example must **not** be collapsed into one installed System and field history. A `DataStream.type=status` may carry diagnostics, but no verified actual logger Status event is available in this case.

**Bennett's Point.** The continuing station has genuine historical EE181 serials, date-limited service assertions and two original NOAA mean events (not four merely because there are four experiment API representations). A CSAPI Deployment and SystemEvent *could* represent relevant relationships/events, but the original operator evidence lacks the exact swap minute, original `resultTime` and a justified final DataStream producer identity. Those gaps remain held; no fabricated native server resource was generated.

## 5. Documentation and limits

**Primary publisher sources inspected directly:**
- [OGC API – Connected Systems Part 1: Feature Resources (23-001, 1.0, 2025)](https://docs.ogc.org/is/23-001/23-001.html): §9.1–9.2 System instance/identity/associations; §10.2–10.3 components and recursive Systems; §11.2 Deployment; §13.2 Procedure; §15.1–15.2 Property Definitions.
- [OGC API – Connected Systems Part 2: Dynamic Data (23-002, 1.0, 2025)](https://docs.ogc.org/is/23-002/23-002.html): §9.2/9.6–9.7 DataStream/schema/Observation; §10.2/10.7/10.11 ControlStream/Command/CommandStatus; §12.1–12.2 SystemEvent.

**Verification distinction:** Primary-source terms and locators were actually checked (unlike the earlier `PRIOR_SOURCE_EXTRACT_ONLY` standing). The **proposed match to the user's DIM row remains analytical** and unapproved; `DIRECT` is not a declaration of general semantic interoperability. Original source text was paraphrased rather than copied wholesale.

**Excluded in Step09:** other donor reviews, SWE Common mapping, IEEE 1451.4/Gemini crosswalk, DIM revisions, case-only row adoption, UML changes, CSAPI Profile changes, Glaux app/server/Cloudflare modifications, deployed observation/command executions, formal OGC ATS validation. This pass is bounded to **12 existing rows and eight separately held native leads**, not a claim that all clauses across two lengthy standards were exhaustively mapped.

**NEXT SINGLE OWNER “proceed”: Step10 — SensorML 3.0 original-source mapping only**. Step09 produces inspectable updated master XLSX/Markdown/CSV/JSON and source audit now; Step10 is not performed here.
