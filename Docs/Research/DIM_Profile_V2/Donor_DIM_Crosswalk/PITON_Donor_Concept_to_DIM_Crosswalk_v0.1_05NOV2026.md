# Current Profile Rewrite checkpoint

Updated 15 November 2026 (America/New_York), Profile Rewrite 45. Owner requested an efficient recovery repair. This document is the single current status; replace its sections in place. Read [the protocol](../AGENTS.md) first. The objective remains a whole-sensing-system Domain Information Model (DIM) and OGC API – Connected Systems (CSAPI) Profile supporting a useful common Details view without erasing vendor/equipment differences.

## Verified checkpoint

Repository `OS4CSAPI/glaux-client`; branch `research/dim-profile-v2`. Query its live HEAD. The last published **research** checkpoint is `e7628af544dd216e3171624ac51af032864d3748` (O2 delivery/status); subsequent protocol-only commits do not advance research. O2 data commit: [f6bbba4](https://github.com/OS4CSAPI/glaux-client/commit/f6bbba43169860350ee192d7026253552f905538). F3 is owner-accepted; O1 and O2 are delivered. Asset Administration Shell (AAS) remains active, bounded PARTIAL.

The **recovery protocol repair**, authorized in Profile Rewrite 45, is published as recorded below. It does not authorize O4, donor transition, model adoption, client work or deployment. The replacement protocol supersedes the prior full-history/all-links startup reread requirement; original-source and owner controls remain.

## Interrupted work

O3 survives as **local-only** commit `f9309f30f5daeaa55a1f6af9b829047ed60b6bfe`, parent `e7628af544dd216e3171624ac51af032864d3748`, in `/workspace/scratch/68383c030602/glaux-client`. This path is a recovery lead, not durable remote publication. Remote archiving of O3 was blocked by automatic approval review during the protocol repair; no remote O3 archive is asserted. Do not discard this checkout. If unavailable, report the missing commit; never infer O3 delivery from screenshots or status text.

O3 records 52 existing findings plus six O2 follow-ups and five provisional candidates: event declaration/state, event source/scope, routing, initiator and qualified context. Three are common and two specialized. Selected original passages and schema blocks were revisited; this is not full-corpus coverage. Its local verification passed on 15 November: prior 345 rows/624 classifications unchanged, all 5,904 saved comparison values and mirrors matched, 26 sheets and M00/M01 preserved. GitHub publication/checks remain pending.

**Do not blindly cherry-pick O3.** Its five routing documents restore historical bloat and prematurely offer O4. Review its data/evidence/publisher changes against the live branch; preserve this compact protocol, indexes, plans and recovery guard. Incorporate O3's checker dispatch without replacing the updated checker. Rewrite current status only after actual publication readback.

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

Protocol repair [feed486](https://github.com/OS4CSAPI/glaux-client/commit/feed4864359e3e57385730d521b0dedc38e27dde) was fetched back with the exact locally verified tree; its [existing verification workflow passed](https://github.com/OS4CSAPI/glaux-client/actions/runs/43718589967). The guard rejected the old oversized PITON, duplicate status headings and a missing stop section. Canonical data, mirrors, source ledger and workbook are byte-identical to O2. This handoff update records delivery, not new research. The ChatGPT Project settings field still needs the owner's replacement bootstrap if it retains the older protocol; repository instructions are updated.

O2 [publication check](https://github.com/OS4CSAPI/glaux-client/actions/runs/43674698614) and [saved-master check](https://github.com/OS4CSAPI/glaux-client/actions/runs/43674698581) were read back successful. These are integrity checks, not independent source audits. Local O3 saved-file verification passed; no O3 remote result is claimed. Protocol checks: `python -B scripts/check_dim_crosswalk_step06.py --recovery-only`; the normal command also runs saved-master verification. Verify actual live commit and changed blobs before claiming any new publication.

## Next action and stop

After this protocol repair, a separate **Proceed completes interrupted O3 delivery only**: recover the preserved changes, retain current protocol, verify affected files, publish/read back on the research branch, record actual checks, then STOP. O4 requires a subsequent Proceed. The O4–O7 research forecast remains 5–7 substantive steps, source-dependent, excluding the unfinished O3 delivery. No research is earned by this repair.

## History

Complete pre-repair published material is preserved in [the named archive](https://github.com/OS4CSAPI/glaux-client/tree/archive/dim-recovery-protocol-before-20261115) and [this immutable PITON snapshot](https://github.com/OS4CSAPI/glaux-client/blob/e7628af544dd216e3171624ac51af032864d3748/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md). Search historical sections only for a specific unresolved decision; old CURRENT/NEXT banners do not govern. All original research files and workbook versions remain in the repository.
