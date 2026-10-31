# Can we represent the Bennett’s Point observation period and quality through native CSAPI?

**Bounded standards/server review · v0.1 · 31 October 2026**

**Decision:** Keep the live archival-report preservation bridge as a *verified, explicitly limited experiment*. Do **not** adopt it as the final application Profile binding or claim an OMS-complete observation. The most promising next *implementation test* is a real OGC API – Connected Systems (CSAPI) Part 2 **SWE Common JSON observation read/write path** on an isolated 52°North/pygeoapi instance. First validate the existing offline record against the published schemas, and independently resolve whether CSAPI’s time mapping can identify an interval as the actual `phenomenonTime`. Do not edit or duplicate the existing live historical observations while investigating.

## What a reader must recover

The Bennett’s Point 2024 source supplies a station, air-temperature value, operator `F_ATemp` quality token and station timestamp. The separate dated equipment log supports physical-probe attribution. It does **not** supply the probe serial in the measurement row, an independently measured time when the result became available, or individual timestamps for the five-second samples.

| Selected NOAA/CDMO row | Published station stamp (fixed EST) | Source-derived *nominal* averaging period (UTC) | Mean air temperature | Original quality token | Unit attributed separately |
|---|---|---|---:|---|---|
| CSV line 10130 | 2024-04-15 12:00 | 2024-04-15 16:45–17:00 | 29.1 Cel | `"<0> "` | EE181 probe 4, serial `222016000109CE` |
| CSV line 10418 | 2024-04-18 12:00 | 2024-04-18 16:45–17:00 | 27.3 Cel | `"<0> "` | EE181 probe 3, serial `21281600077814` |

The 15-minute window is derived from the documented *prior-to-stamp averaging convention*, not from two independently recorded CSV endpoints. `<0>` means passed initial checks; the raw token also contains trailing whitespace. **Keep the exact token and its interpretation separate.**

Evidence: [pinned source fields, CSV fingerprint and operator metadata](examples/bennetts-point-ee181.json); [original operator metadata (pp. 2, 6, 11–13)](https://cdmo.baruch.sc.edu/waf/YearlyFiles/ACE%20Basin/meteorological/metadata/acemet01-12.24m.pdf); [NOAA/CDMO archive](https://cdmo.baruch.sc.edu/waf/swmp_data_archives/acebpmet2024.csv); [CDMO parameter timing convention](https://www.nerrsdata.org/data/parameters.cfm).

## What the approved standards actually distinguish

**OMS 3.0 (OGC 20-082r4), §8.2.3 (printed p. 48):** `phenomenonTime` is the time for which the observed result applies; Note 2 specifically says the time of an average taken from samples at different times is the *interval* covering those samples. §8.2.4 (printed p. 49) instead defines `resultTime` as the instant when the result became available. Its two cardinality requirements call for one of each. These were checked against the [owner-preserved original 198-page OMS standard](../Primary_Sources/OGC_20-082r4_OMS_3.0.0.md), not inferred from an earlier summary. We lack the original observation’s actual result-availability instant.

**CSAPI Part 2 (OGC 23-002 v1.0), §§16.1.4–16.1.5, Requirements 96–98:** `application/json` supports a SWE `resultSchema` and optional SWE `parametersSchema`; `result` and `parameters` are to follow their corresponding schemas. The [published Observation JSON schema](https://schemas.opengis.net/ogcapi/connected-systems/part2/1.0/openapi/schemas/json/observation.json) maps both `phenomenonTime` and `resultTime` to a `TimeInstant` and requires `resultTime`. Thus **the source’s period cannot simply be placed in this JSON `phenomenonTime` member**, and assigning the station timestamp as `resultTime` is an acknowledged compatibility surrogate, not newly discovered evidence.

**CSAPI Part 2 §§16.2.2–16.2.4, Requirements 107–111:** The separate `application/swe+json` encoding has its own `recordSchema` and `JSONEncoding` object. Requirement 110 requires at least one `Time` component mapped to `phenomenonTime` or `resultTime`, identified by one of the specified standard definition URIs. Requirement 111 requires returned observations to follow that declared SWE Common structure. The text does **not** explicitly establish that an additional `TimeRange` field becomes the standard-level `phenomenonTime`; a record containing it may faithfully preserve the averaging window **without resolving that mapping**.

**SWE Common 3.0 (OGC 24-014), §7.4.1 and §§8.2.14–8.2.15, 10.2:** `TimeRange` is the standard type for a time extent, and a dynamically supplied `Text` component can convey source-specific quality information. A source-defined `Text` for `F_ATemp`, semantically tagged as the quality token for **air temperature only**, is justified; it is not equivalent to an OMS/CSAPI built-in `resultQuality` property, a quality assessment of other channels or the physical probe’s condition.

Primary references: [CSAPI Part 2](https://docs.ogc.org/is/23-002/23-002.html#_requirements_class_swe_common_json_encoding), [SWE Common 3.0](https://docs.ogc.org/is/24-014/24-014.html), [canonical CSAPI JSON observation/schema source](https://github.com/opengeospatial/ogcapi-connected-systems/blob/master/api/part2/openapi/schemas/json/observation.json). Published OGC text/schemas, rather than a later GitHub branch, govern normative requirements.

## What we actually observed on the running 52°North service

**Read-only probes, 31 October 2026.** Target: `https://129-80-248-53.sslip.io/csapi-pygeoapi`. Example existing *archival-report* DataStream: `c1870c01-4c61-43a2-ace5-14e86d317c36`. No writes, metadata changes or edits were performed in this review.

| GET probe | HTTP / returned content | What it establishes |
|---|---|---|
| `.../observations?f=application%2Fjson` | **200**, `application/json`; ordinary JSON Observation objects with outer `resultTime`, `phenomenonTime`, nested `result` | Current JSON observation path works for our preserved DataRecord result. |
| `.../observations?f=application%2Fswe%2Bjson` | **200**, header `application/swe+json`, **but** collection of conventional JSON Observation objects, not direct SWE fields matching a SWE `recordSchema` | Merely selecting/echoing the SWE media type does **not** demonstrate the distinct Part 2 SWE encoding. |
| `.../observations?f=swe%2Bjson` | **400** `InvalidMimetype` (expected formats include `application/json` and `application/om+json`) | The shorthand is not accepted; not a general conformance verdict. |
| `.../schema?obsFormat=application%2Fswe%2Bjson&f=json` | **200**, but response still says `"obsFormat":"application/json"` and contains `resultSchema`, **not** a SWE `recordSchema` + `JSONEncoding` | We cannot obtain a format-specific SWE observation schema through this tested route. |
| `.../schema?obsFormat=application%2Fjson&f=json` | **200**, the same JSON `resultSchema` | Baseline control: the schema endpoint returns the existing JSON schema. |
| `/conformance?f=json` | **200**, currently lists only OGC API Common core | The conformance advertisement does **not** establish that the Part 2 SWE JSON requirements class is supported. This alone does not prove every implementation feature is absent. |

The [tested 52°North baseline at `6ad75aa7...`](https://github.com/52North/connected-systems-pygeoapi/blob/6ad75aa7fbfc76517c8a24c21446471845007855/connected-systems-api/provider/part2/formats/om_json_scalar.py) instantiates `OMJsonSchemaParser`, decodes `resultTime` and `phenomenonTime` using `datetime.fromisoformat`, stores `result` as JSON and does not decode or emit observation `parameters`. The [provider](https://github.com/52North/connected-systems-pygeoapi/blob/6ad75aa7fbfc76517c8a24c21446471845007855/connected-systems-api/provider/part2/part2.py) stores single timestamp columns for both times, not an interval type. These source findings align with our live probes; the deployed instance includes documented local adaptations, so do not claim it is byte-identical to upstream.

## Options and decision

| Option | Preserves value, nominal window and original `F_ATemp`? | Native temporal semantics / source truth | Server impact | Decision |
|---|---|---|---|---|
| **A. Current scalar JSON** | Value only; other context absent from native observation | Uses source-stamp surrogate in `resultTime`; interval absent | Already live | Keep untouched as historical baseline. |
| **B. Parallel JSON `DataRecord` result** | **Yes — independently read back on 31 October** | Window is explicit **record context**, not outer `phenomenonTime`; source-stamp `resultTime` surrogate persists | Already live, extra DataStreams | Retain as proven preservation bridge; **not final Profile rule**. |
| **C. Scalar JSON result + `parametersSchema` (`qc`, window, unit attribution)** | Standards provide the field locations, but **our server does not preserve `parameters`** | Cleaner scalar `result`, but outer `phenomenonTime` still instant-only and `resultTime` still unknown | Would require 52°North parser/encoder/storage upgrade | Possible compatibility route after repair; **does not solve the period/result-time issue**. |
| **D. CSAPI Part 2 `application/swe+json` with SWE `DataRecord` fields** | Candidate can carry `Time` stamp, `TimeRange`, `Quantity` air, `Text` flag, and optional attributed unit | Avoids requiring a fabricated outer JSON `resultTime` in each serialized record, **but** does not by itself prove `TimeRange` maps to OMS `phenomenonTime` | Requires proper format-specific schema, SWE JSON encode/decode, retrieval and tests | **Preferred next isolated implementation experiment.** |
| **E. True interval-valued observation `phenomenonTime` and independently evidenced `resultTime`** | Would meet the conceptual distinctions if all facts available | **Cannot be fully established from the two CSV rows today**, and a native CSAPI encoding may need clarification/revision | Standards-level mapping review plus appropriate server support | Keep as explicit standards/data gap; do not claim or fake completion. |

The existing [offline SWE JSON candidate](examples/bennetts-point-wire/example.json) and [reader](examples/bennetts-point-wire/check.py) provide a small, testable starting point for **D**, not a certified conformance result. They already preserve `stamp`, `window`, `air`, `qc` and `probe` with declared SWE types. Reuse that work rather than inventing another representation. When moving to CSAPI resources, retain the distinction between the source’s period stamp, its nominal averaging window and the unavailable result-availability time.

**Implementation boundary:** Do not modify the live Oracle service during a preliminary standards review. An isolated 52°North test instance or reviewed patch must first demonstrate the correct `obsFormat`, `recordSchema` / `JSONEncoding`, and observation payload under real `application/swe+json` negotiation. Acceptance of a media type, or a JSON response with a mislabeled MIME type, is a failing control, not success.

## Recommended **one-prompt next step**

Create a **read-only, executable SWE JSON contract/conformance test** against the offline Bennett fixture and the target’s known format endpoints. The test should exercise:

1. **Positive schema/meaning checks** using the published observation schema and SWE Common types, including one mapped standard `Time` component, a separate clearly named `TimeRange`, original `F_ATemp` text and the physical-unit reference.
2. **Negative controls:** missing/wrong `Time` definition; malformed TimeRange; changed/missing QA token; unresolvable unit UID; a response that advertises `application/swe+json` while actually returning the old `application/json` Observation shape.
3. **Explicit result-time/phenomenon-time reporting:** distinguish what is source-known, what is computed, what the API maps, and what remains undefined. No test can manufacture a historical resultTime.

After this test, consider a small **isolated server-side SWE JSON implementation**, with tests demonstrating actual write/read conformance. Independently, bring the precise **TimeRange-to-`phenomenonTime` mapping question** to the OGC Connected Systems Standards Working Group for clarification; this review does not presume its resolution.

**Acceptance for this investigation:** exact standard clauses and API observations documented, alternatives compared, specific missing capabilities named, and one bounded next test selected. The existing production Glaux views and archival report data remain untouched.
