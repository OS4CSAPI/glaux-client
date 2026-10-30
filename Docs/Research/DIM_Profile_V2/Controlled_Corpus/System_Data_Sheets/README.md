# Selected System Data Sheets — Working Information Inventory

**Version 0.1 · 30 October 2026 · America/New_York**  
**Workspace:** `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, `Docs/Research/DIM_Profile_V2/Controlled_Corpus/System_Data_Sheets/`.

## Start with the system, not the audit trail

These three sheets answer: **What information do we have about each reference system, what exact fields/examples are available for later work, and where did each item come from?** They consolidate equipment facts, physical arrangements, capabilities, power, communications, configuration, diagnostics, native messages and explicit gaps. They are working research inventories, not manufacturer-issued datasheets, installed-device records or an adopted Domain Information Model (DIM).

| Sheet | Itemized coverage | Important boundary |
| --- | --- | --- |
| [AirGradient Open Air Max](AirGradient_Open_Air_Max.md) | Gas-equipped assembly, power/configuration, local indicators, all 17 device-example fields and all three cellular groups; 28 world-endpoint and 36 location-endpoint cloud keys, 43 distinct keys across those two examples. | Independently attributed examples are not one synchronized installed system; ambiguous AFE units, gas validity and version/suffix relationships remain explicit. |
| [Dragino S31-LB](Dragino_S31_LB.md) | External-probe/battery construction, power/operation, measurement/settings/history/status message fields, all eight entries of the original 88-byte history example, and 18 commands/settings. | FPort-2/FPort-5 full original packets were not acquired; earlier synthetic branch probes are not actual configuration/status. No S31B or LS construction is borrowed. |
| [Campbell CR1000X + first-generation ClimaVue 50](Campbell_CR1000X_ClimaVue50.md) | Documented arrangement, all 14 aR7! sensor response positions, sensor verification/control definitions, program context, all 31 logger-status example fields and 29 additional source-defined logger fields without example values. | Logger status, sensor interface and historical program remain distinct. Thirteen example-field interpretations are held where definitions/units were not established. No actual weather series is invented. |

Each sheet includes a small **power/condition navigation section**, but the inventory covers the whole reference system. That section identifies relevant source rows for the proposed first discussion; it does not authorize a modeling campaign or remove the other information from scope.

## Reading a row

Stable IDs such as `A-F11`, `C-H05` and `D-S03` let later work refer to a precise input. A row retains the native name or byte position, fact or literal example value, type/unit where established, equipment/component subject, exact source heading/field, and interpretation limits. These IDs are editorial references, not model classes, vocabulary identifiers or Profile requirements.

The existing evidence labels are abbreviated within the sheets as **Design**, **Example**, **Derived** and **Unknown**, with their full labels defined there. Missing fields, explicit nulls, unknown meanings and no-data markers remain different. Blank or absent operating information is not supplied from general knowledge or inferred from a convenient field name.

**Completeness is tied to named inventories.** Every field in the specified device/cloud/status examples and every listed sensor-response position is itemized. This is not an assertion that every manufacturer manual paragraph, firmware member, schematic component, possible interface or lifecycle attribute has been extracted. Each sheet names remaining extraction or definition gaps, including information withheld from stronger interpretation.

## Provenance and relationship to the completed work

The baseline is research commit `315034c25326dc4a08ecc0629f8bf3a933abe092`, following the closed eight-step equipment qualification plan. The owner separately requested these data sheets after asking whether complete per-system information inventories existed. This is that explicitly authorized consolidation, **not Step 09 of the closed plan**.

The sheets draw from the existing [AirGradient audit](../03_Candidate_A_Evidence_Audit.md), [Dragino audit](../05_Candidate_C_Evidence_Audit.md), [Campbell audit](../06_Candidate_D_Evidence_Audit.md), [selection decision](../07_Corpus_Qualification_Decision.md) and [preservation handoff](../08_Frozen_Corpus_Manifest_and_Handoff.md). Already-selected original sources were reread where needed to expand selective audit tables into itemized inputs. Newly extracted detail is identified in each sheet; no prior report is silently rewritten or upgraded.

**Raspberry Shake & Boom remains outside the three primary sheets.** Its [conditional audit](../04_Candidate_B_Evidence_Audit.md) remains available as documentary context and an unresolved data lead. Actual observations/history coverage remains zero across the four original audits. These sheets do not turn examples into telemetry, validate a deployed firmware combination, or claim live interoperability.

## Checks and preservation

The three committed sheet contents were checked against their local Git blob identities. Local checks enumerated the AirGradient example keys, expanded the retained Dragino bytes without changing them, and checked Campbell's 31 positional values/types against the separately transcribed publisher example. The Campbell canonical JSON hash matches the earlier audit: `ef93d1fc12a09fe04a4d06da743b07a8694cd6bc74af3ce612110a8d4e15c8a8`. These are extraction/content checks, not hardware tests.

The prior frozen audits, checkers, decision and preservation record remain unchanged. The new sheets are additional project artifacts, not retroactive members of the earlier eight-file freeze. Manufacturer manuals, vendor decoder source, full raw API transcriptions and firmware packages are not bundled with these sheets. Source links and access/reuse boundaries remain inside the individual sheets.

**Next use:** review or cite the itemized rows as inputs to separately authorized modeling work. No new DIM structure, CSAPI application Profile, client behavior, deployment or successor plan is adopted here.
