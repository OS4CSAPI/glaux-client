# Current ISA PITON — reporting composites reconciled

**8 November 2026 · Original ISA Steps9/10 / accelerated delivery11 COMPLETE. Next “proceed”: original ISA Step10 / accelerated delivery12, `ISA-TYPES-FILTERING`:24 datatype assignments plus31 registered Data Query Language Guide blocks.** Four original work areas remain closed; requirements retain their existing document-review assignments.

Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk`. GitHub is authoritative.
[Working master](Master_Donor_Concept_to_DIM_Crosswalk.md) · [Structured master](Master_Donor_Concept_to_DIM_Crosswalk.json) · [Excel snapshot](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) · [Type evidence](ISA_Type_Catalogue_Evidence_08NOV2026.json) · [Coverage](ISA_Coverage_Register_07NOV2026.json) · [Progress/exact IDs](ISA_Correction_Status_07NOV2026.json) · [Plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Master/adoption PITON](PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md).

## Earned progress — do not repeat

All91 properties,39 observables,96 commands and their workbook/master integration remain COMPLETE. All93 section8.3 composites362–454 are now fully reconciled:80 prior supporting inspections reused,13 first primary inspections;309 exact native fields. Source standing is74 core,18 Accepted extensions and one Nominated extension. Primary reviews426/480 (420 supported and six unchanged primary questions); types200/224,24 remaining. No omissions or duplicate primary IDs.

The canonical readable master has304 information/review rows:292 preserved plus12 source-backed patterns. They distinguish execution records, nominated component/contact identity, detection/identification limits, reported values/error, message pedigree, typed collections/custom structures/trees, and video detections/tracks. Supporting definitions do not automatically become DIM classes. Existing displayed cells and meanings are unchanged; type-evidence references are additive.

Support-use roster171 is unchanged. Union of primary/supporting evidence223 unique types:200 fully reconciled and23 inspected only as dependencies. These counts overlap and must not be added. No new supporting dependency was needed. Accelerated deliveries1–11 COMPLETE without subdivision; technical iterations30; original work areas closed4/12. **Remaining forecast11 central deliveries, range9–13.** No additional source group, checklist or publication prompt was added.

## Source meanings and exceptions

Command Execution identifies a command currently executing using name,request id,issuer,start time; Command State only reports readiness. Detection Range requires maximum detection distance, with effective identification distance defaulting to maximum and minimum defaulting0.0. Preserve the simpler Range property separately.

Each of31 Measured composites has required value and optional error. Thirty state plus/minus one-standard-deviation error; Measured Psecpm3 does not. Count,Humidity,UTC also do not state that convention. Do not infer zero error from omission, normal distribution, physical concentrations from arbitrary levels or statistical confidence from a default. Measured Ohms and Measured Psecpm3 are Accepted extensions using Float; do not invent an Ohms/Psecpm3 base scalar.

Component Identity is Nominated, not a core identity mandate; it combines UCI with an empty-capable POC list. POC is Accepted and requires organization, not individual name. Keep native email/vCard wording. Message Reference carries originator,identifier,message type,time for pedigree, distinct from Event Reference and proof of authenticity.

Name Value Pair has name and Wildcard value, not an invented type field. Associative Array,List,Custom Type and Tree retain their different instance containers; type/declaration metadata supplies context. Tree nodes share a datatype; this is not physical composition. Video detections use pixel rectangles and optional0–1 confidence; is selected does not establish executed slewing. Video Track is ID plus optional location, not a full time-series trajectory.

All earlier geometry,resource,reading,state and route meanings remain. Geographic Position retains lat/long and At Ground Level omission semantics despite the source's introductory ECEF wording. Radiation Reading Level.channel literally mentions biological detectors; the field text is retained without changing the radiation role. Rotation Rate retains Q006 and no axis swap. UNKNOWN AOI default and observable reporting wording remain unresolved locally, not blanket re-openings.

Six primary questions Q001–Q006 and eight earlier wording notes are unchanged. Two additional local notes: Standard Identity.symbol/Tree.children required/default wording; Measured Kgsecpm3 prose contrasts with the base concentration-times-exposure definition. Preserve declared types and text; resolve only through already scheduled interface/requirements/semantic work. No new prompt or primary-question inflation.

## Source inspection and preservation

Original ISA DMS6.0r12,31 October2023, Files ID `file_00000000ca1c81f48a3ccd49273425f8`. Complete indexed spans for all93 definitions were matched to immutable census SHA256 and reconciled field-by-field; exact source text is retained in each manifest. New page-image inspection covered100–120 and128–129. Earlier recorded inspections for121–127/130–131 were reused; do not claim fresh images for those pages. Cross-page continuations and all309 field rows were followed. No OCR was used.

Preserve480 inventory entries,279 source blocks,31 original row targets,25 earlier findings,58 non-ISA donor records,73 case statements and all prior research. Supporting source blocks and owner work packages are not falsely closed by type review. Bennett original resultTime remains unknown. No DIM adoption,other-donor review,Profile/UML,app/server/deployment or physical/network action.

## Workbook snapshot and next scope

Canonical XLSX remains the verified26-sheet253-row/226-primary master integration, SHA256 `4a660bc7f4640850fdc3215d3ea3686155ce8d1f0f05c07ca29b27b6078c3806`. Markdown/CSV/JSON are four datatype checkpoints newer:304 rows/426 primary reviews,200 type outcomes and51 additional rows beyond Excel. Refresh at a substantial-section checkpoint; do not reinstate the isolated ISA workbook as current master or repeat completed publication.

**Next `ISA-TYPES-FILTERING`: all24 DMS10.1–10.3 entries457–480 plus all31 registered DQL source blocks, accelerated delivery12/original ISA-10.** Exact IDs are in progress. Reuse saved query/subscription/command evidence, inspect missing definitions and guide rules, preserve known limits. Update canonical master/evidence/coverage/PITON via the existing publisher. No automatic advance to services/architecture. Broader donor Step16 follows ISA correction; focused adoption remains broader24 and consolidated approval40.
