# Current PITON — ISA correction with catalogue-level workbook publication

**7 November 2026 · Power/condition and Sensing-settings source passes COMPLETE. Next: nine Motion, viewed area, resources and data links properties. Excel remains the ISA-03D snapshot.**

## Current authority and read-first artifacts
Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. GitHub is authoritative.
[Plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Progress](ISA_Correction_Status_07NOV2026.json) · [Current comparison](ISA_Correction_Review_07NOV2026.md) · [Cumulative evidence](ISA_Property_Catalogue_Evidence_07NOV2026.json) · [Coverage](ISA_Coverage_Register_07NOV2026.json) · [Excel snapshot](ISA_Correction_Review_ISA03D_07NOV2026.xlsx) · [Lessons](LESSONS_Donor_Review_Process.md).

The owner replaced repeated mini-batch releases with three coherent source-and-readable-table passes followed by one consolidated workbook checkpoint. Two of these source passes are now complete. **Do not restart completed work or revert to ISA-03E–J micro-prompts.** No new publication script/workflow or standalone report per pass. Reuse the established text assembler; publish current evidence, table, coverage and concise progress directly to GitHub.

## Newly completed nine-property pass
**ISA-PROPERTIES-SENSING COMPLETE:** Polarity087; Pulse Interval093; Quality094; Radar Mode095; Range096; Resolution101; Scan Time104; Wavelengths119; Zoom121. All nine are core source properties, with supported candidate information roles and zero new questions. Exact meanings and locators are in the cumulative evidence. Core property text was read at DMS6.0r12 printed pp.15–18/PDF30–33, including Zoom on the page shared with Observables.

Himelo and Polarity are two newly inspected supporting definitions; their enum meanings were read across printed pp.79–80/PDF94–95. Neither is marked sealed. Measured Meters printed p.101/PDF116 was checked in original text and page image. Same-edition Measured Secs, Secs, Meters, Percent, String and Float evidence reused. Unique supporting definitions are54; their later full catalogue passes remain uncompleted until reviewed there. Requested PDF94–95 images were unavailable; full indexed text was read and no visual inspection of those pages is claimed.

**Current research:**82 reviewed properties/79 supported/three existing questions;109 information/review rows;78 candidate/question rows (75 supported,three questions). Original480-entry inventory,279 source blocks,31 row targets,25 legacy records,58 non-ISA primary donor mappings and73 case statements are preserved. Parent ISA-03 has33/42 assignments complete; with49 from ISA-02 this is82/91 properties. Nine remain.

**Important meanings:** Quality and Resolution share Himelo but rate distinct output characteristics, with no numeric thresholds, QA flag conversion or pixels inferred. Pulse Interval is laser inter-pulse time; Scan Time covers one whole scan area. Range is expected usable range, not target distance. Polarity is thermal palette, not electrical/polarization. Wavelengths is a laser-specific list. Zoom is camera percentage of maximum, not magnification or an optical/digital distinction. Radar Mode is a radar-specific String related to the existing source-reported-mode row; Camera Mode remains intact. Nine narrow source roles are visible for later model reconciliation, not nine automatically required final DIM fields.

## Next exact source pass and snapshot cadence
**ISA-PROPERTIES-MOTION-DATA only:** Receive Data Rate097; Receive Power098; Resources102; Signal Strength Ratio107; Transmit Data Rate114; Transmit Power115; Velocity116; View Area117; Zones120. Read their exact definitions/types and preserve scope; do not infer signal semantics from a label or convert unavailable documentation into a guessed quantity. Update the same evidence, coverage, comparison and progress; stop before the workbook checkpoint.

The current readable view/CSV includes both recent source passes. Excel remains the accurately labeled ISA-03D snapshot (65 reviewed,92 rows), unchanged by either. Once the last nine properties are reviewed, reconcile the91-entry catalogue and update/export/inspect/publish the workbook once with the existing machinery. This cadence is planned and does not reopen completed source reviews. Unknowns remain attached to individual records, not the whole effort.

## Historical integrated-workbook starting point and preservation

Last fully integrated checkpoint: [c34f7b1](https://github.com/OS4CSAPI/glaux-client/commit/c34f7b1560a920a85c9061deec63c6dd6ab49e4b). Workbook `ISA_Correction_Review_ISA03D_07NOV2026.xlsx`, SHA256 `c569018ee166940d205a007da53486492e47e96e3a5bc042ee0e62d463627404`, 94,332 bytes, twelve worksheets. [Separate post-publication verification](https://github.com/OS4CSAPI/glaux-client/actions/runs/42410293370) succeeded.

Coverage: **65 reviewed primary properties /62 supported/three local questions;92 information/review rows;61 additional candidate/question rows;47 unique supporting definitions**. Parent ISA-03 has16 of42 reviewed; with the49 ISA-02 properties this leaves26 of91 properties. No completed work was reopened by this procedural change.

Preserve all existing non-ISA/equipment values,58 original primary donor mappings,73 case statements, prior identity corrections and Camera Mode. Keep fourteen review columns with four cases left, established donor order and foundational standards adjacent, DIM rightmost. Candidate additions are not automatically adopted DIM requirements. A source entry need not become a unique model row: supporting types, grouped source concepts and specific justified exclusions still need individual evidence traceability. Do not retroactively delete or collapse published rows without a semantic decision.

## Source recovery and meaning boundaries

Original ISA DMS6.0r12: `file_00000000ca1c81f48a3ccd49273425f8`. Companions: SDD6.0r5 `file_000000004c10824683c0a84b37f24a3b`; ICD6.0r5 `file_000000008de0820e8e33af2cb096bb12`; Component Requirements6.0r4 `file_00000000ed048210a141e046f2e93a17`; Controller Requirements6.0r4 `file_00000000e00082109d88d0119f744880`. Exact titles/editions in the source register govern recovery if handles change. Primary originals dated31 October2023; eleven originals/companions registered. Failed raw export does not make indexed source text unavailable. Do not claim an image was inspected when only text was available.

Manufacturer/Model/Serial Number corrections remain. UCI identifies a component, potentially virtual; it is not automatically a URI or physical probe. Maintenance is a contact role, Identity is tactical classification, Visible is laser-spectrum information, and Relationship is physical attachment with source parent/child/link cardinalities. Owner/Support/Program of Record contact roles and source Accepted-extension status remain distinct. Position/Perceived Position/Override are different reported roles; site coordinates do not establish an individual probe point.

**ISA-Q001 Level:** sparse Percent property definition; do not invent its referent. **ISA-Q002 Link Loss:** missing reference quantity/sign convention; do not infer packet-loss percentage. **ISA-Q003 Orientation:** preserve the source's frame label and axis wording without a guessed numeric transformation. These record-local questions do not undo the completed source reviews or hold the whole project hostage.

Source coverage remains480 named entries,279 blocks,31 original row/topic targets and25 earlier findings. Those populations are not additive counts of required model fields. The four equipment examples challenge interpretations; they do not limit relevant source discovery. Preserve reference-design versus installed-system status and Bennett's two original NOAA means versus four experimental representations; no fabricated historical resultTime, device state or exact probe location.

## Completion and scope
Completed source reviews remain complete; three local questions retain their exact follow-up scope. Owner model adoption and catalogue-level workbook publication are distinct statuses. The current source/readable-view checkpoint is the Sensing pass, not the older workbook. No source-catalogue task is marked complete by reusing a supporting type.

**Next substantive work: the nine Motion/viewed-area/resource/data-link properties only, then the property-catalogue workbook checkpoint.** No new scripts, workflows, separate narrative reports, other donors, Profile/UML, application/server/deployment work or physical commands.
