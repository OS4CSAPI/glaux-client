# Bennett's Point — preserving average-window and QA context on the live CSAPI test server

**Experiment, not an adopted Profile binding.** October 31, 2026. The original scalar Observations remain unchanged. This is a separate, explicitly qualified archival-report carrier tested against our actual Oracle-hosted 52°North/pygeoapi service.

## The facts we need to carry

| Operator row | Source clock (EST, UTC−05:00) | Nominal 15-minute window (UTC) | ATemp mean | Original F_ATemp |
|---|---|---|---:|---|
| CSV line 10130 | 2024-04-15 12:00 | 2024-04-15 16:45–17:00 | 29.1 °C | `"<0> "` |
| CSV line 10418 | 2024-04-18 12:00 | 2024-04-18 16:45–17:00 | 27.3 °C | `"<0> "` |

The [NOAA/CDMO meteorological parameter documentation](https://www.nerrsdata.org/data/parameters.cfm) explicitly says the average covers the interval *prior to* the timestamp. The [ACE Basin operator metadata](https://cdmo.baruch.sc.edu/waf/YearlyFiles/ACE%20Basin/meteorological/metadata/acemet01-12.24m.pdf) §4 describes 15-minute averages of 5-second samples and year-round Eastern Standard Time; §11 defines flag 0 as "Passed Initial QAQC Checks." The [original CSV](https://cdmo.baruch.sc.edu/waf/swmp_data_archives/acebpmet2024.csv) carries the source timestamp, ATemp and F_ATemp but no probe serial. These physical probe identities were attributed separately from operator equipment history; [read the controlled evidence](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Candidate_Specification/examples/bennetts-point-ee181.json).

The nominal window is a *calculation from the documented logging convention*, not two independent timestamps printed on each row. The raw F_ATemp token retains the original trailing space. Flag 0 does not mean calibration was independently verified.

## Two gaps that must remain visible

1. **Phenomenon period.** OGC *Observations, measurements and samples* 3.0 §8.2.3 Note 2 says the phenomenon time of an average is the time interval over which the input samples were taken. However, the [CSAPI Part 2 `application/json` observation schema](https://schemas.opengis.net/ogcapi/connected-systems/part2/1.0/openapi/schemas/json/observation.json) defines `phenomenonTime` as `TimeInstant`, not `TimeRange`. The deployed 52°North decoder also invokes `datetime.fromisoformat` and its database stores one timestamp for each of `phenomenontime` and `resulttime`. We therefore cannot claim native CSAPI JSON interval support on this path.
2. **Observation-specific source flag and true result time.** CSAPI Part 2 §16.1.4 permits a stream-specific optional `parametersSchema` and §16.1.5 lets an observation carry `parameters`. But the deployed `OMJsonSchemaParser.decode()` does not decode that field and its `encode()` does not return it. The operator CSV also contains no independently established result-generation time; the existing server's required `resultTime` has been populated with the published station stamp as an *explicit test surrogate*, not evidence that result generation occurred at that instant.

The decoder/database findings come from [52°North's exact tested baseline (`6ad75aa7fbfc76517c8a24c21446471845007855`), `om_json_scalar.py`](https://github.com/52North/connected-systems-pygeoapi/blob/6ad75aa7fbfc76517c8a24c21446471845007855/connected-systems-api/provider/part2/formats/om_json_scalar.py) and [`part2.py`](https://github.com/52North/connected-systems-pygeoapi/blob/6ad75aa7fbfc76517c8a24c21446471845007855/connected-systems-api/provider/part2/part2.py). We should not silently invent a field called `resultQuality` on CSAPI JSON Observations or imply it would survive this server.

## A bounded preservation bridge, not semantic equivalence

Because the existing scalar DataStreams already contain observations and their schemas cannot be safely changed in place, this experiment creates **one additional DataStream per physical probe**. It leaves each original System, scalar stream and observation intact.

The additional stream uses a SWE Common 3.0 `DataRecord` *result* schema with five typed fields: a `Time` source stamp (`stamp`), a `TimeRange` nominal mean window (`window`), a `Quantity` temperature in Cel (`air`), a `Text` original quality token (`qc`), and a `Text` attributed physical System UID (`probe`). The operator's source tokens and the calculated nominal window are placed in the recorded report result, and the client explicitly labels this as **preserved report context**, **not** a standard CSAPI `phenomenonTime` period or a normative quality property. SWE Common `DataRecord` and `TimeRange` supply typed encoding rules; using them here as a composite archival-report result is the project's adapter choice.

This bridge makes the specific fields recoverable on a live HTTP round trip while preventing a false claim of full Profile fidelity. A later server capability upgrade could permit a more appropriate standards-native representation; it would require its own versioned design and conformance check.

The [loader](../../scripts/load-bennett-archival-report-csapi.py) uses the existing two Systems by stable UID, discovers the local IDs assigned by pygeoapi, checks whether matching archival-report streams/observations exist before writing, and confirms the retrieved report fields match the source-derived expected values **exactly** (including `"<0> "` with whitespace). It fails closed rather than rewriting an existing resource or declaring acceptance sufficient.

## Application placement

- **Operational → Equipment:** two individual probe Systems and their shared model, unchanged.
- **Activity → Table:** the value, quality code (with its original spelling retained), nominal averaging interval, and attributed observer for each historical archived report; each must be identified as a *retrieved preservation carrier*, not native `phenomenonTime` or a result-time assertion.
- **Management → Record:** unaltered live API responses and schema.
- **Management → Sources:** source documents, verified scope and the outstanding semantic limits.
- **Operational → Condition:** unchanged. The QA flag describes a source observation, not the physical probe's health.

## Verification

The loader's live round-trip must demonstrate both correctly attributed rows; no duplication on rerun; unchanged original scalar streams; one additional report stream per probe; exact recovery of `air`, `qc`, `window`, `stamp`, `probe`; and retrieved SWE field definitions/types. Separate UI checks must demonstrate that the live Activity table presents the report context without labeling the outer server `phenomenonTime` as the full interval.

**Not established by this test:** native time-period observations on this JSON path; native `parameters` round trip; true result-generation times; source calibration; installation geometry; Deployment writes; or universal interoperability. These gaps stay open.

## Executed result — 31 October 2026

[Live server load/read-back verification, GitHub Actions run 41248245591](https://github.com/OS4CSAPI/glaux-client/actions/runs/41248245591) completed successfully. The earlier scalar streams and observations were found and left unchanged. The loader created one additional archival-report DataStream per identified EE181 probe, read back each stream's typed DataRecord schema, and verified the **exact** returned report values, including the trailing space in `"<0> "`.

| Attributed unit | Parallel archival-report DataStream ID | Returned Observation ID | Returned nominal window (UTC) | Temperature | Original flag |
|---|---|---|---|---:|---|
| Probe 4, `222016000109CE` | `c1870c01-4c61-43a2-ace5-14e86d317c36` | `a742b704-c2cd-4c1d-970a-b97b5f628130` | 2024-04-15 16:45–17:00 | 29.1 Cel | `"<0> "` |
| Probe 3, `21281600077814` | `8b8f9361-e2fa-4179-b1bb-947d3cd3d86d` | `50bf940e-55a0-45b6-9331-e6391704f6c7` | 2024-04-18 16:45–17:00 | 27.3 Cel | `"<0> "` |

[Verified production build and deployment, run 41248473107](https://github.com/OS4CSAPI/glaux-client/actions/runs/41248473107) passed TypeScript, unit tests, Vite build, and Cloudflare Pages deployment. Independent browser rendering of [the dedicated live Bennett’s Point page](https://glaux-client.pages.dev/?page=resource-details-live-bennett) under **Activity → Table** returned the two report cards, two temperatures, both exact quality tokens, both interval endpoints, matching physical probe IDs and serials, and no interpretation warnings. The existing historical Profile and separate live-map pages still return HTTP 200.

The [schema-driven Profile reader](../../src/profile/archival-report-context.ts) identifies fields through their SWE component types and semantic definitions. Its [offline tests](../../tests/archival-report-context.test.ts) verify source-token preservation, non-promotion of rejected/missing flags, a mismatched probe UID, and incorrect window duration.

**Result and scope:** The exact data and qualified context now survive a live 52°North CSAPI `application/json` **DataRecord result** round trip, with a client that exposes the distinction to the operator. The outer `Observation.phenomenonTime` is still instant-valued; `resultTime` is still a source-stamp surrogate, not independently evidenced; and `Observation.parameters` is not preserved by this deployed server. Do **not** describe this as full normative phenomenon-time/quality interoperability, a true result-generation timestamp, or a corrected 52°North implementation.
