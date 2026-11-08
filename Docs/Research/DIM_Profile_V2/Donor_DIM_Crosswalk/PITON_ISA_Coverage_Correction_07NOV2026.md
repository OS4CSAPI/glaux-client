# Current PITON — spatial control and acquisition complete

**8 November 2026 · Original ISA Step5 of12;four original steps COMPLETE. Accelerated delivery3 COMPLETE. Commands66/96 reviewed;30 remain. Next “proceed”: ISA-COMMANDS-COMMUNICATION-SERVICES —16 assigned definitions only.**

Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. GitHub is authoritative.
[Plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Progress/exact queue](ISA_Correction_Status_07NOV2026.json) · [Comparison](ISA_Correction_Review_07NOV2026.md) · [Command evidence](ISA_Command_Catalogue_Evidence_07NOV2026.json) · [Coverage](ISA_Coverage_Register_07NOV2026.json) · [Workbook snapshot](ISA_Correction_Review_Observables_07NOV2026.xlsx) · [Workbook publication](ISA_Observables_Publication_Record_07NOV2026.json) · [Lessons](LESSONS_Donor_Review_Process.md).

## Earned progress and remaining schedule

All91 properties,39 observables,their consolidated12-sheet workbook and54 prior commands remain COMPLETE. All12 spatial/acquisition commands now have recorded source outcomes:11 supported and one exact axis question. **Totals196 primary reviews/190 supported/six local questions;223 information/review rows;129 unique supporting definitions.** Original command owners ISA-05/06 have42/24 reviewed entries respectively. Neither whole command/type/requirement package is falsely closed.

**Remaining forecast:19 central prompted deliveries, working range17–21.** Accelerated slot3 completed without subdivision. Three command-source passes plus one command-workbook checkpoint remain inside that forecast. ISA-Q006 joins existing type/companion reconciliation, not an extra prompt. Technical iterations complete22;original work areas complete4/12. Keep original step numbers,earned catalogue increment and remaining forecast visible.

## Source findings and exact inspection

Add Zone requires a nonempty associative array of Area of Interest values and replaces existing same-name zones. Remove Zone uses an existing zone name; anonymous-area restrictions and source shape/AOI defaults remain distinct. No new nested name field, polygon-only constraint or zone-ordering rule is invented.

Move's defined success criterion is arrival at its destination. Point Position instead requests pointing toward an absolute position. Point Orientation uses a Rotation: attached components use offset from home in their own frame; unattached ones use the source's absolute Earth-Centered Earth-Fixed wording. Do not silently close existing Orientation Q003 or invent numerical transforms. Observe may start late and continue after its requested UTC end time; its required zero-or-more components result can change over time.

Scan Area takes one closed Geographic Polygon (at least3 ordered positions) and UTC stop. Scan Points takes one Geographic Polyline (at least2 ordered positions) and UTC stop; scan order matters. Slew Percent's orientation parameter contains three Percent rates, not target angles. Slew Velocity uses three Measured Degpsec rates. Both require duration and have source-described zero-rate stopping; do not import Adjust's omitted-duration/default behavior.

**ISA-Q006 — Slew Velocity / Rotation Rate:** the Rotation Rate table describes pitch rate about x and roll rate about y, while Rotation describes pitch about y-prime and roll about x-double-prime. The reason for this difference is not established. Preserve native names,types,required duration and printed axes; do not swap fields, invent a transform or classify the supported command role as absent. Resolve or retain the local discrepancy in the already planned type/companion/semantic reconciliation.

Take Picture requests an image of the current view but declares no command-specific parameters or Results table; no payload/URL/timestamp/format is invented. Take Range declares required range:Measured Meters and recommends availability only when Armed is true (should,not shall). Range result differs from expected usable Range capability; optional measurement error is not perfect accuracy. No operation or equipment measurement is asserted.

Original DMS6.0r12 §3.3 text and page images38,55–58,61–63 inspected. Scan Area57–58 and Slew Percent61–62 continuations checked. Supporting page images100,109–110,113,126–127 inspected; Degpsec67 read as text. Four new dependencies:Rotation Percent Rate,Rotation Rate,Measured Degpsec,Degpsec. Prior exact-edition geometry,measurement,identity and scalar manifests reused. Original source ID `file_00000000ca1c81f48a3ccd49273425f8`; recover by exact title/revision. All locators,source hashes,parameter/result manifests and boundaries are in cumulative evidence. Dependency inspection does not falsely complete later full-catalogue assignments.

## Next single group — accelerated slot4

**ISA-COMMANDS-COMMUNICATION-SERVICES:** Add IP Address; Discover; Ping; Recommend Video Stream; Remove IP Address; Service Notify; Service Provider For Component; Set Authorization Service; Set Communication Service; Set Live Data Service; Sibling Service Providers; Start Data Input; Start Data Output; Stop Data Input; Stop Data Output; Trace Route.

IDs161,210,223,226,227,236,237,238,239,240,245,248,249,250,251,254. These16 remain unreviewed assignments. Review complete original definitions,parameters/results and necessary types; preserve optional fields,defaults,service recommendations,transfer-state meanings and routing cardinalities. Publish cumulative evidence,coverage,comparison and concise routing using the same assembler/workflow. No new exporter,per-group report,workflow or Excel release. Stop after the named16;no automatic advance to group5.

## Preservation

Current Excel remains the completed130-primary/157-row property/observable snapshot (SHA256 `68deb7b41c2fcfbf3350f7260929c560cfb81963246acaa0d3f134f1281b27a6`) with its original four questions. Current text is newer and includes Q005 and Q006; scheduled refresh is not failed publication. Preserve58 non-ISA donor records,73 case facts,480 source entries,279 blocks,31 original row targets,25 earlier findings and all earlier comparison cells. New source candidates are for owner review,not automatically adopted DIM classes.

Existing Level Q001,Link Loss Q002,Orientation frame Q003,Signal Strength Ratio Q004 and Adjust Power rate Q005 remain unchanged. Q006 concerns only the new Rotation Rate axis correspondence. Bennett retains two NOAA means/four representations and unknown original resultTime. No other donor,model adoption,Profile/UML,client/server/deployment or equipment operation. Broader donor-review Step16 follows this correction.

[Prior lifecycle checkpoint](https://github.com/OS4CSAPI/glaux-client/blob/0c4252323ad8467f7c206628e7474aff1c4a445c/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_ISA_Coverage_Correction_07NOV2026.md) retains history; its group3-next instruction is superseded here.
