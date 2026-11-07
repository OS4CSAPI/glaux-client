# Current PITON — ISA property catalogue source review complete

**7 November 2026 · All 91 property entries reviewed and current in GitHub. Next: ISA-PROPERTIES-PUBLISH, the consolidated workbook checkpoint ONLY.** The Excel workbook remains the accurately labeled ISA-03D snapshot until that action.

## Current authority and actual completed work
Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. GitHub is authoritative.
[Plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Progress](ISA_Correction_Status_07NOV2026.json) · [Current comparison](ISA_Correction_Review_07NOV2026.md) · [Cumulative evidence](ISA_Property_Catalogue_Evidence_07NOV2026.json) · [Coverage](ISA_Coverage_Register_07NOV2026.json) · [Excel snapshot](ISA_Correction_Review_ISA03D_07NOV2026.xlsx) · [Lessons](LESSONS_Donor_Review_Process.md).

The three regrouped source passes are COMPLETE: eight power/condition, nine sensing settings and nine motion/data properties. The original49 ISA-02 outcomes plus all42 ISA-03 assignments account for91 properties: **87 supported, four precise questions; no unreviewed property remains**. Current comparison has118 information/review rows: original31 plus83 supported candidates and four question rows. Unique inspected supporting definitions total62; their later full catalogue assignments remain separately tracked.

Do not restart the completed source passes, revert to ISA-03E–J micro-prompts, or claim the workbook already contains the newer rows. The next checkpoint was planned and is not a publication failure. Source review, model acceptance and workbook integration remain distinct.

## Final source pass: exact outcomes and boundaries
**ISA-PROPERTIES-MOTION-DATA COMPLETE:** Receive Data Rate097, Receive Power098, Resources102, Signal Strength Ratio107, Transmit Data Rate114, Transmit Power115, Velocity116, View Area117, Zones120. All nine are core. Eight support distinct narrow information roles; Signal Strength Ratio is recorded as **ISA-Q004** because its original entry explicitly states No Documentation and Db alone does not identify the ratio. No SNR/SINR, dBm, Link Loss or sign/reference convention was guessed.

Receive/Transmit Data Rate use decimal Mbpsec with optional measurement error; signal power uses Dbm (one-milliwatt reference), not Percent or stored energy. Resources is a list of media access descriptors with required type/URL and source metadata/time conventions, not an equipment inventory or a proven live transfer. Velocity preserves required heading/speed and optional pitch with its source default; no numeric frame conversion was invented. View Area is the currently viewed polygon (ordered3+ positions, closure last-to-first), not nominal coverage or device position. Zones is ordered typed inclusion/exclusion areas, not an unordered polygon list or proof of enforcement.

Original property text: DMS6.0r12 §3.1 printed pp.15–18/PDF30–33. Source page images100,109,125,126,129 were inspected for AOI/map, polygon, resource and velocity fields. New supporting definitions: Dbm, Mpsec, Measured Mpsec, Velocity, Geographic Polygon, Area of Interest, AOI Reason and Geographic Shape. Exact locators and reused definitions are in the cumulative evidence. Geographic Shape retains its listed union alternatives; no automatic GeoJSON or point-only conversion. No source-case measurements were invented.

## Next sole task — consolidate and verify the workbook
**Next owner “proceed” executes ISA-PROPERTIES-PUBLISH only.** Reconcile the91 saved source outcomes, all existing candidate/question rows and dependencies with the register; refresh the current review workbook once, inspect its changed areas, publish through the existing exact-file assembler, and verify actual committed workbook/evidence/readable-view parity and historical/non-ISA preservation. Do not repeat semantic property research. Do not start Observables or another donor. Reuse the existing generation and verification machinery; no new exporter project or new standalone reports per tiny group.

Workbook snapshot is still ISA-03D (65 primary entries,92 information rows; original SHA256 below). Current readable view and evidence are newer at91 reviewed/118 rows. Completed source work remains complete when workbook snapshot and current research differ under this schedule.

## Four record-local questions
Level ISA-Q001: precise Percent-property referent. Link Loss ISA-Q002: ratio/reference/sign convention. Orientation ISA-Q003: reconcile named frame and stated axes before numeric transformation. **Signal Strength Ratio ISA-Q004:** identify compared quantities/reference from authoritative communications guidance if available; original DMS occurrences do not define them. These questions stay visible, attached to exact sources and later resolution actions; none erases completed property reviews or blocks unrelated model work.

All58 original non-ISA donor records,73 source-case statements, previous table cells and identity/Camera Mode corrections are preserved. The property-catalogue completion is not the completion of the whole480-entry donor corpus; use actual coverage states, never a false global count. All later source blocks/row targets remain tracked.

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

**Next sole action: the property-catalogue workbook checkpoint; all91 property source reviews are complete.** No new scripts, workflows, separate narrative reports, other donors, Profile/UML, application/server/deployment work or physical commands.
