# Current PITON — control and lifecycle commands complete

**8 November 2026 · Original ISA Step 5 of 12; four original steps COMPLETE. Accelerated delivery 2 COMPLETE. Commands 54/96 reviewed; 42 remain. Next “proceed”: ISA-COMMANDS-SPATIAL-ACQUISITION — 12 assigned definitions only.**

Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. GitHub is authoritative.
[Plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Progress/exact queue](ISA_Correction_Status_07NOV2026.json) · [Comparison](ISA_Correction_Review_07NOV2026.md) · [Command evidence](ISA_Command_Catalogue_Evidence_07NOV2026.json) · [Coverage](ISA_Coverage_Register_07NOV2026.json) · [Workbook snapshot](ISA_Correction_Review_Observables_07NOV2026.xlsx) · [Workbook publication](ISA_Observables_Publication_Record_07NOV2026.json) · [Lessons](LESSONS_Donor_Review_Process.md).

## Earned completion and remaining schedule

All 91 properties, 39 observables, their consolidated twelve-sheet workbook and all 36 prior command reviews remain COMPLETE. The 18 control/lifecycle entries are now reviewed: **17 supported outcomes and one precise rate-input question. Totals: 184 primary reviews / 179 supported / five local questions; 211 information/review rows; 125 unique supporting definitions.** Commands span original ISA-05/06 ownership (41 and 13 reviewed respectively); the broader command/type/requirement packages are not falsely closed.

**Remaining forecast: 20 central prompted deliveries, working range 18–22.** Accelerated slot 2 completed without subdivision. Four command-source passes plus one command-workbook checkpoint remain within that forecast. The rate discrepancy is assigned to existing reconciliation, not a new prompt. Keep original step numbers, actual catalogue increment and remaining forecast visible. Technical iterations completed: 21; original work areas complete: 4/12.

## Actual source findings and inspection

Adjust Level retains direction, optional rate default100% of maximum rate of change, and optional duration. Change Level and Change Power retain one required level:Percent target. Generic Level's physical referent remains the existing ISA-Q001; these commands add source-backed control contracts, not an invented quantity.

**ISA-Q005 — Adjust Power:** the complete original table lists required direction and optional duration but no rate parameter, although the prose refers to a specified relative rate. Do not repair that omission by copying rate:Percent or a100% default from neighboring Adjust commands. Preserve its direction and duration meanings while keeping this exact rate-contract question local. Omitted adjustment duration differs from zero; this is not a reason to reopen the18 completed reviews.

Set Property applies when the component cannot determine the value and takes a Name Value Pair with required name and typed value. Clear Property applies only to values previously supplied via Set Property; it sets the value null and ready false, not merely reporting false. Arm/Disarm concern commands that require pre-arming, not general authorization. Designate and Illuminate retain the source's availability recommendation (should, not shall), optional-duration semantics and lack of a declared mechanism. No physical commands are invoked.

Calibrate means the source's initialization routines, not an assumed metrological calibration. Initiate NUC means a component-specific Non-Uniformity Correction process. Self Test requests diagnostics. Reset returns to a component-defined original state; the home-pointing example is not universal. Shutdown, permanent non-functioning via Render Useless, security-relevant application-data removal via Sanitize, and accumulated unique application-data removal via Zeroize remain distinct. No technique, executed result or fielded capability is inferred. Entries without a Parameters/Results table do not imply absence of generic request or acknowledgement fields.

Original DMS6.0r12 §3.3 page text and images41–43,47–48,50–51,54,57–58,60–61,64 inspected; Adjust Power and Designate continuations included. Name Value Pair image120 rechecked. Exact-edition Linear Direction,Percent,Secs,Float,String,Wildcard and prior Armed evidence reused; **zero newly counted supporting types**. Per-entry hashes, locators, parameter manifests, restrictions and shared families are in cumulative evidence. Source ID `file_00000000ca1c81f48a3ccd49273425f8`; recover by exact title/revision if needed. Raw-byte export failure is not source-text absence.

## Next single source group — accelerated slot 3

**ISA-COMMANDS-SPATIAL-ACQUISITION:** Add Zone; Move; Observe; Point Orientation; Point Position; Remove Zone; Scan Area; Scan Points; Slew Percent; Slew Velocity; Take Picture; Take Range.

Exact IDs: ISA-DMS-163,221,222,224,225,229,233,234,246,247,252,253. All 12 remain unreviewed assignments. Inspect complete original parameters/results and necessary types; preserve source geometry, timing, optional/default fields, request-versus-outcome distinctions and genuine local questions. Publish cumulative evidence, coverage, readable comparison and concise routing using the existing assembler/workflow. No new exporter, per-group report, workflow or Excel release. Stop after the named12; do not advance to group4 automatically.

## Preservation

Workbook remains the completed130-primary/157-row property/observable snapshot, SHA256 `68deb7b41c2fcfbf3350f7260929c560cfb81963246acaa0d3f134f1281b27a6`, with its original four questions. Current GitHub text is newer and includes ISA-Q005; scheduled Excel refresh is not failed publication. Preserve58 non-ISA donor records,73 case facts,480 source entries,279 blocks,31 original row targets,25 earlier findings and all previous grid cells. Source entries/candidates are individually traceable, not automatically adopted independent DIM classes.

Existing Level Q001,Link Loss Q002,Orientation frame Q003 and Signal Strength Ratio Q004 are unchanged. New Adjust Power Q005 concerns only its missing rate contract. Bennett retains two NOAA means/four representations and unknown original resultTime. No other donor, model adoption, Profile/UML, client/server/deployment or actual equipment operation. Broader donor-review Step16 follows the ISA correction.

[Prior configuration checkpoint](https://github.com/OS4CSAPI/glaux-client/blob/6685f22e3444572a8966802e4c5059158dd519aa/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_ISA_Coverage_Correction_07NOV2026.md) retains history; its group2-next direction is superseded here.
