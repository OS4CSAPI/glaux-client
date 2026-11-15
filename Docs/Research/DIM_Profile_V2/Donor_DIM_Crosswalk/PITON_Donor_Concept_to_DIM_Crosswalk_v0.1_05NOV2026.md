# Current Profile Rewrite checkpoint

Updated 15 November 2026 (America/New_York), Profile Rewrite 45. Owner installed the replacement Project instructions and authorized completion of interrupted O3 delivery. This document is the single current status; replace its sections in place. Read [the protocol](../AGENTS.md) first. The objective remains a whole-sensing-system Domain Information Model (DIM) and OGC API – Connected Systems (CSAPI) Profile supporting a useful common Details view without erasing vendor/equipment differences.

## Verified checkpoint

Repository `OS4CSAPI/glaux-client`; branch `research/dim-profile-v2`. Query its live HEAD. The last published **research** checkpoint is `e7628af544dd216e3171624ac51af032864d3748` (O2 delivery/status); subsequent protocol-only commits do not advance research. O2 data commit: [f6bbba4](https://github.com/OS4CSAPI/glaux-client/commit/f6bbba43169860350ee192d7026253552f905538). F3 is owner-accepted; O1 and O2 are delivered. Asset Administration Shell (AAS) remains active, bounded PARTIAL.

The current **Proceed authorizes O3 delivery only** from research-branch preflight `f3d93d6fec5c5d385bfc9b832f6905c31f126d37`. The compact recovery protocol remains binding. Stop after O3 publication/readback; O4, donor transition, model adoption, client work and deployment are not authorized.

## Interrupted work

O3 was recovered from preserved local commit `f9309f30f5daeaa55a1f6af9b829047ed60b6bfe` (parent `e7628af544dd216e3171624ac51af032864d3748`) in `/workspace/scratch/68383c030602/glaux-client`. Its data, source notes and publisher were preserved exactly, while its checker dispatch was integrated into the current recovery guard. The current completion checkout is `/workspace/scratch/eb7ff8d5824b/glaux-o3`. Remote publication remains pending until verified below; local paths are recovery leads, not durable delivery.
O3 records 52 existing findings plus six O2 follow-ups and five provisional candidates: event declaration/state, event source/scope, routing, initiator and qualified context. Three are common and two specialized. Selected original passages and schema blocks were revisited; this is not full-corpus coverage. Its local verification passed on 15 November: prior 345 rows/624 classifications unchanged, all 5,904 saved comparison values and mirrors matched, 26 sheets and M00/M01 preserved. GitHub publication/checks remain pending.

The five obsolete O3 routing documents were not replayed. Compact protocol, indexes, plans and budget guard are retained. This is completion of prior source work, not a new source audit or renewed classification decision.

## Active scope and evidence

[AAS plan](PLAN_AAS_v3_2_Source_First_Donor_Review_13NOV2026.md): `O3 — interrupted delivery` and `Execution and coverage controls`; [broader plan](PLAN_Donor_Concept_to_DIM_Master_Crosswalk_v0.1_05NOV2026.md) preserves the 40-step sequence. Read those sections only as relevant.

Targeted structured evidence: `AAS01_Original_Source_Corpus_Coverage_13NOV2026.json` keys `F3_owner_acceptance`, `AAS_O1_source_opportunities`, `AAS_O2_native_review`; the local O3 copy additionally has `AAS_O3_native_review` with `records`, `targeted_original_contacts`, `holds_retained`, `publication`. Master JSON: `currentEvidenceCheckpoint`, `workbookSnapshot`, `nextOwnerAction`, `AAS_O2_native_review`; O3 additionally has `AAS_O3_native_review`. Use key extraction, not whole-file output.

O3 source notes are [AAS04](AAS04_Original_Part1_Condition_Capability_Operations_Events_Time_13NOV2026.md) and [AAS05](AAS05_Original_Schema_Corroboration_14NOV2026.md). Original editions/locators are in the ledger. Its 15 source contacts include sampled schema files; contact hashes do not establish fresh source reading.

## Master and workbook

One [canonical master](Master_Donor_Concept_to_DIM_Crosswalk.json) and [editable workbook](Master_Donor_Concept_to_DIM_Crosswalk.xlsx); both CSV mirrors and both readable comparisons remain required.

| Snapshot | Information rows | Source-bearing classifications | Saved comparison values | Workbook SHA-256 |
|---|---:|---:|---:|---|
| Published O2 | 345 | 624 (516 colored, 108 held) | 5,808 | `2618bb8a0d93004e22ba2ac0dcb018de88e7912516ea960a9d676af7cedf27a2` |
| Local O3 | 350 | 629 (521 colored, 108 held) | 5,904 | `2aa1791b4d91d12145e711cfe8f56011500a1638c2439aa0a553ac86052055d9` |

Each snapshot has internal JSON/CSV/readable/XLSX parity; GitHub is five candidate rows behind local O3. Both retain 26 sheets, the approved 16-column layout and M00/M01. No M02. Actual Microsoft Excel clean reopening remains unverified.

## Holds and owner decisions

Preserve AAS experimental-event/qualifier standing, timestamp/timeStamp, administrative integer/string and UTC example/pattern conflicts; encoding differences do not establish lossless conversion or supplied-empty/no-update equivalence. Companion, figure, external dictionary and API-profile coverage remains limited; 34 profiles/436 method incidences were inventoried, not exhaustively audited.

Retain six ISA questions, nine The Open Group SOSA hold families, 39 overlapping SAPIENT limitations, four-case ceilings, prior evidence and all DIM/Profile adoption gates. F3 acceptance is recorded in the [F3 plan](PLAN_F3_Cross_Donor_Classification_Fairness_14NOV2026.md#f3-owner-explanation-and-accepted-results). Step24, Steps35–39 and Step40 still require owner decisions. The broad artifact check now reports five pre-existing register/link errors; three obsolete README links left the active indexes with their history preserved. These errors do not prove source or workbook failure.

## Verification and publication

Protocol repair [feed486](https://github.com/OS4CSAPI/glaux-client/commit/feed4864359e3e57385730d521b0dedc38e27dde) was fetched back with the exact locally verified tree; its [existing verification workflow passed](https://github.com/OS4CSAPI/glaux-client/actions/runs/43718589967). The guard rejected the old oversized PITON, duplicate status headings and a missing stop section. That protocol-only checkpoint preserved O2 data. The owner has now supplied the replacement Project instructions, completing that setup step.

O2 [publication check](https://github.com/OS4CSAPI/glaux-client/actions/runs/43674698614) and [saved-master check](https://github.com/OS4CSAPI/glaux-client/actions/runs/43674698581) were read back successful. These are integrity checks, not independent source audits. Recovered O3 saved-file and mirror/preservation verification passed again with the recovery guard intact; no O3 remote result is claimed yet. The unchanged workbook retains its prior visual review; no new rendering or native Excel reopening is claimed. Protocol checks: `python -B scripts/check_dim_crosswalk_step06.py --recovery-only`; the normal command also runs saved-master verification. Verify actual live commit and changed blobs before claiming any new publication.

## Next action and stop

**Current action: finish O3 publication and verification, then STOP.** After verified delivery, the next separate owner Proceed authorizes **O4 only**: original discovery/service meanings from 38 AAS06 findings; stop before O5. O4 has not started. The O4–O7 research forecast remains 5–7 substantive steps, source-dependent. No new research is earned by this delivery recovery.

## History

Complete pre-repair published material is preserved in [the named archive](https://github.com/OS4CSAPI/glaux-client/tree/archive/dim-recovery-protocol-before-20261115) and [this immutable PITON snapshot](https://github.com/OS4CSAPI/glaux-client/blob/e7628af544dd216e3171624ac51af032864d3748/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md). Search historical sections only for a specific unresolved decision; old CURRENT/NEXT banners do not govern. All original research files and workbook versions remain in the repository.
