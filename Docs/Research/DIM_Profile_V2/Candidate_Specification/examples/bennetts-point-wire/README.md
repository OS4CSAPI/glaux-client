# Can a client tell which probe measured the temperature?

**Yes, for these two records.** The same station and model appear on both days. A reader of the encoded observations recovered two different instrument serial numbers without looking up a date in the equipment log. The comparison against the source data used that log separately.

| Station timestamp (fixed EST, UTC−05:00) | Air temperature (15-minute mean) | Operator's temperature flag | Sensing probe recovered by the client |
|---|---:|---|---|
| 15 April 2024, noon | 29.1 °C | `<0>` — passed initial checks | EE181 sensor 4 · `222016000109CE` |
| 18 April 2024, noon | 27.3 °C | `<0>` — passed initial checks | EE181 sensor 3 · `21281600077814` |

[Open the two encoded observations and their descriptions](example.json) · [Read the Profile decision and physical swap history](../../CSAPI_Profile.md#which-probe-measured-the-air-temperature) · [Inspect the retained source fields and archive fingerprint](../bennetts-point-ee181.json).

## How to read the example

`responses[].body` is a single observation payload in the Connected Systems `application/swe+json` representation. `schema` is the corresponding stream schema. `systems` contains the two SensorML unit descriptions. **The surrounding JSON is a file cabinet for an offline test, not an API resource.** Paths and `urn:example:` identifiers belong to this fixture; the reserve did not issue them. The parent stream represents station air-temperature summaries, not the raw analogue outputs of either probe. The logger records the summaries; it is not the sensing probe.

| What has to survive | Where the client finds it | Who supplies the meaning |
|---|---|---|
| The value and unit | `air` in each body; its field definition and `uom.code = Cel` in the shared schema | Operator's `ATemp`; SWE Common `Quantity`; existing air-temperature property URI. The schema labels it as a mean of five-second samples. |
| Quality of **that temperature** | `qc` in the same body, described by a `Text` field specifically for `F_ATemp` | The operator's own flag, including its original trailing space. `<0>` is not a confidence percentage or proof of calibration. We use text so that a future flag with reason codes is not silently truncated. No row-wide flag substitutes for it. |
| The physical probe | `probe` in the body → matching `uniqueId` in a SensorML System → its typed serial-number identifier | Our Profile makes the contributing unit explicit **after** attribution by station, temperature role and deployment period. Neither original CSV row named the probe. It is a profile-defined reference, not a built-in CSAPI observation member. A missing attribution leaves the reported value and flag intact. |
| When and over what period | `stamp` (station stamp expressed in UTC) and `window` (a separate SWE `TimeRange`) | Both rows are stamped 17:00 UTC. The reserve documents 15-minute means, not sample-by-sample event times. The example uses 16:45–17:00 as the **nominal** window, treating the scan stamp as the closing stamp, consistent with the logger's documented interval-average convention. These bounds are calculated, not two timestamps printed in the CSV. Neither unit assignment depends on that choice: both dates lie well inside the respective deployments. |

## What the standards say, and what we chose

*Observations, measurements and samples* 3.0, §8.2.3 Note 2, treats the period of an average as its phenomenon time; §8.2.4 distinguishes this from when its result became available, and §8.6.2 Note 2 distinguishes the observer instance from its type. See the [preserved standard](../../../Primary_Sources/OGC_20-082r4_OMS_3.0.0.md). The physical medium assessed here is ambient air, not the logger or probe housing.

[OGC API – Connected Systems Part 2, §§16.2.3–4, requirements 109–111](https://docs.ogc.org/is/23-002/23-002.html) permits a SWE JSON record with a `Time` component for measurement time without serializing a separate result-time component. The schema uses the specified SamplingTime URI for the station stamp; the extra `TimeRange` carries the nominal averaging bounds rather than suggesting an instantaneous sample. [SWE Common 3.0 §§7.4.1, 9.1.10 and 10.2](https://docs.ogc.org/is/24-014/24-014.html) supplies field-specific dynamic quality, UTC time representation and record encoding. [SensorML §8.2.2.3](https://docs.ogc.org/is/23-000/23-000.html) supplies typed identifiers. Our three local field meanings, the decision to use one stream with a per-record probe reference, and the attribution procedure are project choices; they are not new donor classes.

The standard's ordinary [application/json Observation schema](https://schemas.opengis.net/ogcapi/connected-systems/part2/1.0/openapi/schemas/json/observation.json) requires `resultTime`. The source extract does not provide it independently. This example therefore **does not** generate that representation, use the file retrieval or revision date as a substitute, or claim the broader API information model's result-time obligation is resolved. The chosen representation has its own [SWE JSON schema](https://schemas.opengis.net/ogcapi/connected-systems/part2/1.0/openapi/schemas/json/observationSchemaSwe.json).

## Reproduce the check

Run `python3 Docs/Research/DIM_Profile_V2/Candidate_Specification/examples/bennetts-point-wire/check.py` from the repository root (Python 3.10+; no network or additional packages). The [reader](check.py) takes only a response body and cached resource context. It uses the shared field definitions to find the value and flag and resolves the unit reference; it does not know which serial goes with which date. A separate check calculates expected values from the retained source columns and looks up the unit in the equipment history, **without** reading the stored preassigned serial in the observations. Both original rows matched even when presented in reverse order.

Five deliberately altered inputs check that a swapped probe fails comparison with the log; a rejection flag stays a rejection flag; missing probe attribution preserves the measurement; a broken probe link is flagged; and an absent quality flag is not silently treated as passing. The rejection flag used for this control is from the separate April 17 record; neither selected reading was actually rejected. This is an executed offline consumer check, not a live Glaux/HTTP exchange, a full OGC schema or conformance test, or a calibration comparison.

**Primary data:** ACE Basin National Estuarine Research Reserve, South Carolina Department of Natural Resources; NOAA National Estuarine Research Reserve System, System-wide Monitoring Program, Centralized Data Management Office. [2024 station CSV](https://cdmo.baruch.sc.edu/waf/swmp_data_archives/acebpmet2024.csv), lines 10130 and 10418; [operator's meteorological record](https://cdmo.baruch.sc.edu/waf/YearlyFiles/ACE%20Basin/meteorological/metadata/acemet01-12.24m.pdf), §§4, 9, 11–13; [dataset DOI](https://doi.org/10.25921/vw8a-8031). [CR1000X interval-average timestamp example, Campbell Scientific](https://help.campbellsci.com/CR1000X/Content/shared/Details/Data/About_Data_Tables.htm).
