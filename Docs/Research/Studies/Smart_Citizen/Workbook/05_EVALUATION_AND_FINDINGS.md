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

## Artifact feedback

| Finding | DIM action | Profile action | PBI/wireframe action | Code action | Paper treatment |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Completion gate

Material findings have an evidence-backed classification and destination rather than being fixed silently in code or presentation.
