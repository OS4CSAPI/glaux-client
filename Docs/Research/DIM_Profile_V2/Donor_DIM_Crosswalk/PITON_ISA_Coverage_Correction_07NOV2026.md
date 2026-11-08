# Current PITON — readout, history and archive results complete

**8 November 2026 · Original ISA Step 5 of 12; four original steps COMPLETE. Accelerated delivery 5 COMPLETE. Commands 89/96 reviewed; seven remain. Next “proceed”: ISA-COMMANDS-AUTH-SUBSCRIPTIONS — the final seven assigned command definitions only.**

Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. GitHub is authoritative.
[Plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Progress/exact queue](ISA_Correction_Status_07NOV2026.json) · [Comparison](ISA_Correction_Review_07NOV2026.md) · [Command evidence](ISA_Command_Catalogue_Evidence_07NOV2026.json) · [Coverage](ISA_Coverage_Register_07NOV2026.json) · [Workbook snapshot](ISA_Correction_Review_Observables_07NOV2026.xlsx) · [Workbook publication](ISA_Observables_Publication_Record_07NOV2026.json) · [Lessons](LESSONS_Donor_Review_Process.md).

## Earned progress and remaining schedule
All 91 properties, 39 observables, their consolidated twelve-sheet workbook and 82 prior command reviews remain COMPLETE. All seven readout/history/archive entries are now reviewed: core, source-supported, no new primary interpretation question. **Totals: 219 primary reviews / 213 supported / six unchanged primary questions; 246 information/review rows; 162 unique supporting definitions.** Original command owners ISA-05/06 have 44/45 reviewed entries respectively; neither complete command/type/requirement work package is falsely closed.

**Remaining forecast: 17 central prompted deliveries, working range 15–19.** Accelerated slot 5 completed without subdivision. One command-source pass and one command-workbook checkpoint remain inside this forecast. Technical iterations complete: 24; original work areas complete: 4/12. Keep step numbers, actual catalogue increment, remaining forecast and workbook snapshot visible. No planning turn or source rereading is due.

## Source meanings retained
Create Zip Archive uses the Integer result key from a previous History query and returns archive:Resource, bytesize:Integer and optional stale:UTC. Resource allows Blob or Resource Descriptor; no URL-only assumption. Archive expiry requires a new archive request; expired underlying results require a new History first. Blob length is payload byte length, explicitly not uncompressed length.

Get Config returns one current Config message, with optional capability declaration and empty-capable state lists. Get Status returns one Status message with current values of declared properties whose ready state is true. Readiness differs from reporting; disabling property publication does not remove the explicit Get Property/Get Status retrieval route. Get Property takes name:String and returns property:Name Value Pair, preserving the typed value.

Get Last Operation State takes code:General Code; time:UTC and state:General State are individually optional results for the latest matching Operating State occurrence. Get Operation State History takes optional after:UTC and returns an empty-capable associative array keyed by time with full General State values. No missing-input defaults, lifetime-retention claim, paired-omission rule, sorted-list substitution or serialization of time keys is invented.

History queries messages published in the past. Its required query:Data Query reuses the saved selection/matching evidence; optional before/after concern publication time. It returns result key, matches and optional stale, not a messages payload. Matches means total in SUCCESS and so-far in IN PROGRESS. Repeating an expired query can return different results. Query-result expiry, archive expiry, envelope validity, occurrence times and Bennett's unknown resultTime remain distinct.

## Supporting source inspection and reuse
Original DMS6.0r12 §3.3 text and images50–54 were inspected, including Get Property52–53 and History53–54 and each following-heading boundary. Ten new supporting definitions were inspected: Config, Response, Status, Capability Declaration, Resource, Blob, Command State, Observable State, Property State and Bytestream. Images73,75–76,85–86,100,102,106,121,123 were inspected; Bytestream65 and the following section77 were checked as text. Resource99 text was complete but its image was unavailable; do not claim visual inspection of99.

The source Observable State.reporting description says status messages, while Set Observable Reporting explicitly says Event messages. The exact wording contrast is retained in `ISA-SOURCE-NOTE-OBSERVABLE-REPORTING` in the supporting evidence for the existing type reconciliation. This does not invalidate Get Config's supported result contract or add a prompt. Property State's introductory observable wording is also noted; its fields explicitly describe properties. Config's capability container was inspected, but nested declaration constraints retain their scheduled ISA-08 review.

Reuse the previously inspected Data Query/Response Code, General State/General Code, Name Value Pair, identity/scalar and resource-descriptor evidence. No old dependency is counted again and no full-type assignment is falsely closed. Original source file ID `file_00000000ca1c81f48a3ccd49273425f8`; recover by exact title/revision. Per-entry source hashes, locators and complete native manifests are in the cumulative evidence.

## Next single group — accelerated slot 6
**ISA-COMMANDS-AUTH-SUBSCRIPTIONS:** Add Subscription; Authorize Registration; Authorize Request; Cancel; Lock; Remove Subscription; Unlock.
IDs: ISA-DMS-162,173,174,176,219,228,255. These are the final seven unreviewed commands. Inspect complete original parameters/results, authorization subjects, subscription identity/defaults, cancellation references and lock semantics. Reuse saved query and Response evidence; inspect any necessary new Request/Registration/Subscription details. These are assignments, not pre-established conclusions.

Publish the same cumulative evidence, coverage, comparison and concise routing through the existing assembler/workflow. No new per-group report, exporter, workflow or Excel release. Stop after the seven; the separate command-workbook checkpoint follows. Do not silently change the remaining forecast or repeat completed research.

## Preservation
Excel remains the completed 130-primary/157-row property/observable snapshot, SHA256 `68deb7b41c2fcfbf3350f7260929c560cfb81963246acaa0d3f134f1281b27a6`, with its original four questions. Current text contains newer command reviews and Q005/Q006; scheduled refresh is not failed publication. Preserve 58 non-ISA records, 73 case facts, 480 source entries, 279 blocks, 31 original row targets, 25 earlier findings and every prior comparison value.

Existing questions Q001–Q006 remain unchanged. New candidates are for owner review, not automatically adopted DIM classes. Bennett retains two original NOAA means/four representations and unknown original resultTime. No actual query, archive, network/equipment operation, other-donor review, model adoption, Profile/UML or application/server change occurred. Broader donor-review Step16 follows this correction.

[Prior communication/service checkpoint](https://github.com/OS4CSAPI/glaux-client/blob/e50f836953117a2887fb44342abe3aa44edcfbce/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_ISA_Coverage_Correction_07NOV2026.md) preserves history; its slot5-next routing is superseded here.
