# 05 — Evaluation, PBI observations, and findings disposition

**Status:** Vendor presentation baseline exists; matched Glaux evaluation has not started.

## Operator-question evaluation

| Question/task | Vendor evidence | Generic OGC result | MPSS-aware Glaux result | Correct evidence | Finding |
| --- | --- | --- | --- | --- | --- |
| What resource is this? | | | | | |
| What can it report? | | | | | |
| What is the value/unit/time? | | | | | |
| What does the selected property mean? | | | | | |
| Which values are older/newer? | | | | | |
| What remains unknown? | | | | | |

## PBI observations

| ID | User need | Evidence | Proposed behavior | UI location | Acceptance example | Status |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Discrepancy register

| Finding ID | Description | Classification | Evidence | Impact | Proposed disposition | Status |
| --- | --- | --- | --- | --- | --- | --- |
| | | source limitation / documentation conflict / mapping defect / DIM gap / donor question / profile gap / server / client / presentation | | | | |
| SC-FIND-001 | Initial supplemental vocabulary workflow requested wrong Smart Citizen Measurement IDs for temperature, humidity, PM2.5 and pressure | experiment evidence-collection defect | workflow run `40156434639`; corrected run `40156565257`; corrected vocabulary capture `20261025T030010Z` | Could have contaminated semantic mapping if undetected; frozen device specimen itself unaffected | Preserve first capture as audit history; use corrected measurement IDs 1, 2, 14 and 25; require source-channel measurement IDs to drive future vocabulary capture | resolved |
| SC-FIND-002 | Phase 2 described `<sensor_id>_raw` as the original reading | source-characterization defect | Smart Citizen `RawStorer` at commit `25a524cb...` calls `normalized_value` before writing the `_raw` key, then calls the method named `calibrated_value` for the public sensor-ID value | Overstated rawness and could imply unsupported calibration provenance | Describe `_raw` as normalized/pre-calibration source-platform value; call public `value` a source-platform reported/processed result; do not claim formal VIM calibration | resolved |
| SC-FIND-003 | `notify.low_battery=false` and `notify.stopped_publishing=false` could be misread as live condition assertions | source-characterization / semantic false-friend | Smart Citizen API reference defines both as notification settings | Could create false “battery OK” or “publishing OK” condition facts | Explicitly classify as notification preferences and exclude from first condition/status mappings | resolved |
| SC-FIND-004 | Initial SC-RSSI-01 classified RSSI as a `status` DataStream solely because it is equipment/communications-related | mapping defect | Smart Citizen Measurement 78; OGC Part 2 DataStream type definitions; MPSS R13 constraints | Could make received-signal power appear to be a parent-System/subsystem status property without identifying the observed subject | Leave DataStream `type` unset until subject is established; preserve RSSI as source-reported communications telemetry and keep interface/link status inferences prohibited | resolved for Phase 3 |
| SC-FIND-005 | Paper v0.6 formal mapping prose still used the earlier 24 October feasibility values instead of the frozen 25 October specimen | research-documentation drift | preliminary evidence record versus frozen capture `20261025T024348Z` | Could blur preliminary and formal experiment provenance | Paper v0.7 uses the frozen specimen for formal mappings and retains earlier access only as feasibility history | resolved in v0.7 |
| SC-FIND-006 | Phase 2 timing paragraph said 17 non-particulate plus 10 SEN5X channels despite a 21-channel response | source-characterization arithmetic defect | frozen `device.json`: 11 channels at 02:40:21Z and 10 SEN5X channels at 02:36:21Z | Internal inconsistency could undermine timing analysis | Correct to 11 + 10 and retain the two-cohort conclusion | resolved |

## Artifact feedback

| Finding | DIM action | Profile action | PBI/wireframe action | Code action | Paper treatment |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Completion gate

Material findings have an evidence-backed classification and destination rather than being fixed silently in code or presentation.
