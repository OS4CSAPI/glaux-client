# Current Details View work

Updated 23 October 2026. Status: implementation reconstruction in progress.

## Objective

Implement the first compact System Details View with Overview, Equipment, and
Condition. Compare standard CSAPI/SensorML/SWE access and MPSS v0.3.5
interpretation using the same retrieved records. Preserve the distinct meanings
of TRSS configuration, OmniSense reported transducers, and condition observations.

## Verified starting point

- Application baseline: `d2386062871ff8caaa7021d38f39f1af7c74dd12`.
- Working branch: `work/details-view-20261023`.
- Library: `OS4CSAPI/ogc-client-CSAPI_2`, pinned to
  `4ca1d7db9b1ccdf545adbef42ef941139fe11977` (phase-10 provenance).
- The earlier local implementation is unavailable. Recovered screen images are
  design evidence, not recovered source code or evidence of passing tests.
- This branch reconstructs that authorized increment from the actual source
  documents. Bootstrap-only exclusions are superseded only for these views,
  bounded interpretation, and explicitly synthetic local evaluation records.

## Implementation scope

Keep standard data retrieval and original response capture, profile
interpretation, and presentation separate. Display the source, subject, meaning,
units, and time associated with each fact. Preserve unknown data and allow
inspection in standard mode. Keep TRSS ETU-II, OmniSense Core 2 Equipment, and
OmniSense Core 5 ADS Condition as distinct examples.

No deployment, infrastructure change, live device commands, server writes,
upstream-library modifications, or MPSS profile changes are included. Do not
copy private source documents, manuals, operational data, or chat transcripts
into this public repository.

## Current verification

The baseline and pinned submodule have been retrieved. No new implementation
checks are yet reported as passing. This note will be updated with actual
results as the source code is completed.

## Next action

Finish the source-to-view mapping, reconstruct the read-only data path and three
views, add focused preservation/interpretation tests, and verify the rendered
client. Check in each coherent implementation increment and update this note.
