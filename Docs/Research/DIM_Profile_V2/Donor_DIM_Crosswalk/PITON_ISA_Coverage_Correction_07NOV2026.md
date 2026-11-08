# Current ISA PITON — capability declarations and constraints reconciled

**8 November 2026 · Original ISA Step8 / accelerated delivery9 COMPLETE. Next “proceed”: original ISA-06/09 / accelerated delivery10, `ISA-TYPES-REPORTING-ENUMS`,28 exact IDs in progress.** Four original work areas remain closed; scheduled requirements/companion work is unchanged.

Repository `OS4CSAPI/glaux-client`,branch `research/dim-profile-v2`,directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk`. GitHub is authoritative.
[Working master](Master_Donor_Concept_to_DIM_Crosswalk.md) · [Structured master](Master_Donor_Concept_to_DIM_Crosswalk.json) · [Excel snapshot](Master_Donor_Concept_to_DIM_Crosswalk.xlsx) · [Type evidence](ISA_Type_Catalogue_Evidence_08NOV2026.json) · [Coverage](ISA_Coverage_Register_07NOV2026.json) · [Progress/exact IDs](ISA_Correction_Status_07NOV2026.json) · [Plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Master/adoption PITON](PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md).

## Earned progress

All91 properties,39 observables,96 commands and their workbook/master integration remain COMPLETE. This pass reconciled exactly25 core capability types311–335 (DMS7.1–7.3):3 earlier supporting inspections reused and22 first primary inspections. All native fields, variants, cardinalities, defaults and source bounds are recorded. Full Type Name has201 literal codes. Primary reviews305/480 (299 source-supported dispositions and six unchanged primary questions); types79/224,145 remaining.

Fifteen declaration/constraint patterns were added to the canonical master in Configuration & Control;285 information/review rows now preserve every previous270-row value and order. No type becomes a compulsory adopted model class. Capability Declaration, Custom Type Declaration and Field Declaration reuse their earlier evidence while adding the assigned full constraints. Comparator and scalar/state definitions were reused. Custom Type Name was newly inspected as the Type union dependency; its later full filtering assignment remains open.

Support-use roster169; union of primary/supporting type evidence200 unique definitions;79 fully reconciled,121 other definitions inspected as dependencies. These overlapping counts must not be added. Accelerated slots1–9 COMPLETE without subdivision; technical iterations28. **Remaining forecast13 central deliveries, range11–15.** No new source pass, checklist prompt or publication step was added.

## Meanings and local notes

Declarations describe support/interfaces, not current values, readiness, authorization or execution. Command args/results are declaration lists, not the actual Request.parameters/Response.values. Observable Declaration explicitly says declared observables need not occur in every Event and reported observables should be declared. Do not strengthen should to shall.

Mutability retains PERMANENT,READ ONLY,READ WRITE,WRITE ONLY and source wording; no user policy is inferred. Range Declaration can describe permitted/excluded values; Bounded Range has independent endpoint-inclusion flags; Discrete Range.inclusive defaults true. No precedence among conflicting ranges is invented. Result Declaration.range is **Range**, unlike Parameter/Property/Observable range:**Range Declaration**.

Single Structure has no fields; not a null value. List/associative-array min length and tree min depth are required; maxima are optional and unbounded when omitted. A value tree is not a hardware composition. Property thresholds trigger Status publication independently of status interval. Relative extent is last measured, last reported, or component uptime; do not conflate them. No AND/OR threshold-combination rule is supplied here.

Six primary questions Q001–Q006 and four earlier source notes are unchanged. Two new local notes retain Field Declaration.optional and Range/Threshold Declaration required/default wording, and Type Name descriptive mismatches. No alias or wire omission rule was invented. The earlier Observable State.reporting note gains corroboration from Observable Declaration's Event wording, but its source text is not silently corrected or marked resolved. Resolution stays in existing interface/requirements/semantic review, not an extra prompt.

## Source inspection and preservation

Original DMS6.0r12 (31 October2023),Files ID `file_00000000ca1c81f48a3ccd49273425f8`. Complete original text77–89 and Custom Type Name/Comparator133 read. Page images85–89 inspected; images77 and84 unavailable, no visual claim for them. Type Name77–84, Absolute Threshold84–85 and Field Declaration86–87 continuations followed. All25 indexed text spans match their existing census SHA256 hashes. Preserve native Type Name codes and printed descriptions even when descriptive names differ.

All480 entries,279 blocks,31 original row targets,25 earlier findings,58 non-ISA records,73 cases,270 prior table rows and original source/evidence files are preserved. Unknown Bennett resultTime remains unknown. No other donor,model adoption,Profile/UML,client/server/deployment or operational command.

## Workbook and exact next group

Canonical XLSX remains the verified26-sheet253-row/226-primary master integration, SHA256 `4a660bc7f4640850fdc3215d3ea3686155ce8d1f0f05c07ca29b27b6078c3806`. Text/CSV/JSON are two type checkpoints newer:285 rows/305 primary dispositions. Refresh at a substantial-section checkpoint; do not restart an isolated ISA overlay or repeat completed integration.

Next `ISA-TYPES-REPORTING-ENUMS`:28 exact assignments in sections8.1,8.2,9.1, as listed in progress. Reuse existing enum/union/command dependencies, inspect genuine gaps and native values, preserve qualifications. Update canonical master text/evidence/coverage/PITON through the existing publication path. Stop after this group. Broader Step16 follows ISA correction; focused adoption remains broader24, consolidated named version40.
