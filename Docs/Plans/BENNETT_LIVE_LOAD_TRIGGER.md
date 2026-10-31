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
