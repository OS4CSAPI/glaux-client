# Bennett's Point V2 live CSAPI load trigger

31 October 2026.

This file intentionally triggers the bounded loader in
`.github/workflows/load-bennett-v2-csapi.yml`.

The loader creates, only when absent, two identified Campbell Scientific EE181
probe Systems, one air-temperature DataStream for each, and one historical
Observation per DataStream. It verifies each created resource by reading it back
from the Oracle-hosted 52°North/pygeoapi Connected Systems API.

This is a controlled research load. It does not claim live physical-sensor
telemetry, a Deployment-resource write, or complete CSAPI conformance.

Retry note: loader now discovers resources by stable `uniqueId` and captures the local IDs assigned by this pygeoapi deployment.

Retry note 2: verifier now normalizes equivalent UTC lexical forms (`Z` and `+00:00`) returned by the server.

## 31 October 2026 — archival-report context bridge

Trigger the independently verified parallel DataRecord archival-report load. Preserve the nominal 15-minute window and exact operator F_ATemp token in typed SWE Common report fields returned by the live CSAPI server. Keep the original scalar DataStreams and their observations unchanged. Document the unresolved native CSAPI JSON phenomenonTime interval and dropped observation parameters separately in [the design record](../Design/BENNETT_OBSERVATION_CONTEXT_BRIDGE.md).
