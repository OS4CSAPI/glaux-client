# Current ISA PITON — base types and messages reconciled

**8 November 2026 · Original ISA Step 7 / accelerated delivery 8 COMPLETE. Next “proceed”: original ISA Step 8 / accelerated delivery 9, `ISA-TYPES-CAPABILITY`, the 25 exact assignments in the progress JSON.** Four original work areas remain closed; broader Step 5/6/7 requirements retain their existing later document-review slots.

Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk`. GitHub is authoritative.
[Current readable master](Master_Donor_Concept_to_DIM_Crosswalk.md) · [Current structured master](Master_Donor_Concept_to_DIM_Crosswalk.json) · [Excel snapshot](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) · [Type evidence](ISA_Type_Catalogue_Evidence_08NOV2026.json) · [Coverage](ISA_Coverage_Register_07NOV2026.json) · [Progress/exact IDs](ISA_Correction_Status_07NOV2026.json) · [Plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Master/adoption PITON](PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md).

## Earned completion and counts

All 91 properties, 39 observables and 96 commands and their completed workbook/master integration remain COMPLETE. This pass fully reconciled all 54 DMS entries257–310 in sections4.1,4.2,5.1,6.1,6.2, with no omissions or duplicates. 45 reused earlier dependency inspections; nine were first primary inspections. All native scalar forms/ranges/units and message fields/variants/defaults are recorded. The primary count is now280/480, with274 source-supported dispositions and the same six prior primary questions. Type catalogue54/224,170 remaining.

The readable canonical master has270 information/review rows:253 preserved and17 coherent new metadata/message patterns. Supporting definitions and reserved Alarm ID were not mechanically converted into new rows. The support-use roster is168 (167 prior plus Admin Code); across primary and supporting type evidence177 unique definitions have been examined. These counts overlap and must not be added. Fifty-four are fully reconciled;123 others remain dependency inspections with later assignments.

Accelerated slots1–8 complete without subdivision; technical iterations27; original work areas closed4/12. **Remaining forecast14 central deliveries, range12–16.** No extra prompt is created for the wording notes. Next scope is the25 capability/constraint entries, not another planning or recovery pass.

## Important meanings and local source notes

Sender/recipients and Header.time concern transmission; message source and Event.time have different roles. Event ID is only component/time-context unique, unlike a universal permanent identifier. Request.identifier and request id remain separate; Response.reference is recorded exactly as a request-message identifier, without inventing equality to either field. Registration source has a distinct announcement role. Config's optional ccd and state lists do not become Status property values or Event observables. Required empty-capable collections remain required collections, not mandatory nonempty measurements.

Retain literal scalar constraints: Percent allows values beyond100; Kg excludes zero in its printed range; Amps is nonnegative while Volts/Watts/Joules/Newtons have signed ranges; blank ranges are not fabricated bounds. The unusual native Integer interval is not silently made int32. SIDC retains15 characters and the source's2525C reference. URL retains the edition's RFC1738 citation, not a claim of current-web best practice. Alarm ID is explicitly Reserved for Future Use.

Q001–Q006 remain unchanged. Additional wording records retain the previously recorded incomplete Wpm2 units label, Event.type Required1 plus an omission default Other, and the Request/Response reference wording. Together with the existing Observable State.reporting note there are four source notes, not four new primary questions or new work packages. Resolve the exact issues only in already scheduled interface/requirements/semantic reconciliation. Do not interpret them as a blanket reopening.

## Source inspection and preservation

Original DMS6.0r12,31 October2023, source ID `file_00000000ca1c81f48a3ccd49273425f8`. Complete original text65–76 and Admin Code90–91 inspected; images71–76 and108 inspected. Images65,70,90 were unavailable in new retrieval; no new visual claim for those. Scalar manifests reuse45 earlier exact-edition inspections, and Event Reference/UTC/state/declaration/query records are reused. All cross-page message definitions are complete. Admin Code's12 variants include undocumented OTHER without a fabricated definition; its later full-catalogue assignment remains open.

All480 entries,279 source blocks,31 original row targets,25 earlier findings,58 other-donor records,73 case statements,all earlier source files and253 prior table rows are preserved. No new DIM content is adopted. Bennett's original resultTime remains unknown. No other-donor research, Profile/UML, app/server/deployment or physical/network action occurred.

## Workbook snapshot and next action

The canonical XLSX remains the verified26-sheet master-integration snapshot with253 rows,226 primary reviews and SHA256 `4a660bc7f4640850fdc3215d3ea3686155ce8d1f0f05c07ca29b27b6078c3806`. Text/CSV/JSON are one source checkpoint newer:270 rows/280 primary dispositions. Refresh the canonical XLSX at substantial-section checkpoints, not each source pass; do not restart a standalone ISA overlay.

Next `ISA-TYPES-CAPABILITY`:25 DMS7.1–7.3 assignments311–335. Reuse existing manifests; inspect actual missing fields, constraints, type declarations, cardinalities, defaults and thresholds. Update the canonical master text, evidence, coverage and concise recovery through the same publication workflow. Stop after that group. Broader donor Step16 follows the ISA correction; adoption review remains broader Step24 and consolidated version approval Step40.
