# Current PITON — all96 command definitions reviewed; workbook checkpoint next

**8 November 2026 · Original ISA Step5 of12; four original work areas COMPLETE. Accelerated delivery6 COMPLETE. Commands96/96 reviewed; zero remaining. Next “proceed”: ISA-COMMANDS-PUBLISH — one consolidated workbook checkpoint, with no new source research.**

Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. GitHub is authoritative.
[Plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Progress](ISA_Correction_Status_07NOV2026.json) · [Comparison](ISA_Correction_Review_07NOV2026.md) · [Command evidence](ISA_Command_Catalogue_Evidence_07NOV2026.json) · [Coverage](ISA_Coverage_Register_07NOV2026.json) · [Workbook snapshot](ISA_Correction_Review_Observables_07NOV2026.xlsx) · [Prior workbook publication](ISA_Observables_Publication_Record_07NOV2026.json) · [Lessons](LESSONS_Donor_Review_Process.md).

## Earned progress and next delivery
All91 properties,39 observables,their twelve-sheet workbook and89 earlier command reviews remain COMPLETE. The final seven commands are now reviewed, all core and supported. **The command-definition catalogue is COMPLETE:96 unique inventory entries match96 unique evidence records,94 supported interpretations and two local command questions (Q005,Q006), zero omissions or duplicates.** Original ISA-05 and ISA-06 each own48 reviewed commands; their broader type/requirement reconciliation remains in the existing schedule, not newly added work.

Current totals: **226 primary reviews /220 supported /six unchanged primary questions;253 information/review rows;167 unique supporting definitions.** Technical iterations25; original work areas closed4/12. Accelerated slots1–6 complete without subdivision. **Remaining forecast16 central prompted deliveries, working range14–18.** This includes the next workbook checkpoint; no command-source pass remains. Report these separately from original step numbers and owner model adoption.

## Final seven findings
Add Subscription creates or updates future-message delivery, unlike History retrieval. Same-name use replaces an existing subscription; multiple subscriptions with one provider need unique names. Omitted consumer defaults to the requester. The required returned Subscription ID contains creator,consumer,name; no omitted-name generation rule is invented. Remove Subscription takes that structured identifier, not a bare label; removal does not imply recall/deletion of previously delivered messages.

Authorize Registration preserves client/server identities and optional Registration input. Authorize Request.subject is the component being tasked, not the requester; the embedded Request carries source, command, distinct request id and access-control data. Both return required authorized:Boolean, with explicit true/false permission outcomes. Permission is not proof of registration or execution and is not identical to readiness or a control lock.

Cancel identifies the original Request.source plus Request.request id, not its separate identifier. SUCCESS means the cancellation succeeded; FAILED means unable to cancel, not that the original action failed. Lock reserves time-bounded exclusive command use; requester is automatically a holder, lock holders and commands are required empty-capable lists, empty commands means all supported commands, and lock time is Integer seconds. Unlock takes the target component and returns release approval. No renewal, rollback, policy rule or equipment interlock is invented.

## Source inspection and reuse
Original DMS6.0r12 §3.3 text/page images37–38,43–44,54–55,57,64 inspected, including both subscription and lock continuations. Five new supporting definitions:Registration,Request,Registration Operation,Subscription,Subscription ID. Images74–75 and138 inspected; Registration Operation97 was read completely as text after its image request failed. Subscription ID is complete on138; the next heading on139 is known from prior original text, and new139 retrieval was unavailable. No visual claim for97 or139. Exact-edition Data Query,Response/Response Code,identity/scalar and Name Value Pair evidence was reused. Supporting inspection does not advance later primary type-catalogue status.

Source file ID `file_00000000ca1c81f48a3ccd49273425f8`; recover by exact title/revision. Field/variant manifests, source locators and inventory source-span hashes remain in cumulative command evidence. Primary question recordsQ001–Q006 and `ISA-SOURCE-NOTE-OBSERVABLE-REPORTING` remain unchanged. No unread definition is counted as a question or exclusion.

## Next “proceed” — command workbook only
Integrate all96 saved command outcomes and the cumulative supporting evidence into the workbook once. Check register/table/evidence parity, all253 current information rows, all six primary questions and the supporting wording note. Preserve the completed91-property/39-observable evidence, original31 rows,58 non-ISA donor records,73 case facts and all prior equipment/donor values. Reuse the existing workbook-authoring and publication machinery, inspect changed layout and formulas, publish and verify actual committed output. Do not repeat command research or start the next datatype review.

The current workbook remains the130-primary/157-row property/observable snapshot, SHA256 `68deb7b41c2fcfbf3350f7260929c560cfb81963246acaa0d3f134f1281b27a6`, with its original four questions. The current GitHub text is newer. Scheduled workbook integration is not a failed publication or a restart of completed science. The next checkpoint is slot7 of the existing22-slot forecast; no new planning turn is due.

## Boundaries and recovery
Preserve the480-entry source inventory,279 blocks,31 original row targets,25 earlier findings and all prior meanings. New candidates remain for owner review, not automatically adopted DIM classes. Bennett retains two NOAA means/four representations and unknown original resultTime. No physical/network commands,other-donor work,Profile/UML,application/server/deployment change or owner model adoption. Broader donor-review Step16 follows this ISA correction.

[Previous readout/history checkpoint](https://github.com/OS4CSAPI/glaux-client/blob/db2d7a6275fba2d01e2c30af3d4915fc0bd4d9e0/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_ISA_Coverage_Correction_07NOV2026.md) retains history; its final-seven review instruction is superseded by this completed source checkpoint.
