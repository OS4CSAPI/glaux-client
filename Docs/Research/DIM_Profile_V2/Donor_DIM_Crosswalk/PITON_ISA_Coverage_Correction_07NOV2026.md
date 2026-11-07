# Current PITON — ISA correction after ISA-03D

**7 November 2026 · ISA-01, ISA-02 and child batches ISA-03A/B/C/D COMPLETE. Next owner “proceed”: ISA-03E ONLY.**

## Authority and read-first artifacts
Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`; `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. GitHub remains authoritative.
[Workbook](ISA_Correction_Review_ISA03D_07NOV2026.xlsx) · [Horizontal view](ISA_Correction_Review_ISA03D_07NOV2026.md) · [ISA-03D report](ISA03D_Relationship_Visible_07NOV2026.md) · [Exact source evidence](ISA03D_Relationship_Visible_Evidence_07NOV2026.json) · [Coverage](ISA_Coverage_Register_07NOV2026.json) · [Progress](ISA_Correction_Status_07NOV2026.json) · [Publication](ISA03D_Publication_Record_07NOV2026.json) · [Plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Lessons](LESSONS_Donor_Review_Process.md).

ISA-03D reviewed only **Relationship (099) and Visible (118)**, both core properties, with two supported candidates and no new source questions. **65 primary entries reviewed/62 supported/three specific questions**; **92 information/review rows**, original31 plus58 supported candidates and three questions. The47 unique supporting definitions are unchanged; Relationship, Relation Link, Link, UCI and Boolean were already verified supporting entries, not new catalogue completions.

**Relationship** is physical parent/child attachment, not CIC visibility or network connectivity. Optional parent0–1 and required child list0+ use Relation Links with required UCI and Link fields. Link's sealed values ATTACHED/DETACHED concern physical attachment. Do not infer an installed child, complete parts list or spatial transform. **Visible** means the laser is in the visible spectrum; it does not mean a component is exposed to the ISA network, a GUI item is visible, or a laser is firing. Read original definitions, not similar words in architecture prose.

Original property text at DMS6.0r12 §3.1 printed pp.16–17/PDF31–32; Relation Link/Relationship printed p.110/PDF125 text and page image inspected; Link printed p.80/PDF95 and Boolean printed p.50/PDF65 checked. Existing UCI evidence reused. Two candidate rows are added within existing Position and orientation and Imaging and sensing settings groups. All prior rows, three local questions, non-ISA/equipment values and old source evidence are retained.

## Next exact task — ISA-03E
Only **Power (ISA-DMS-090), Power State (091), Reserve Capacity (100) and Time to Empty (113)**. Use original definitions and the already recorded types. Keep variable-power percentage, power condition, reserve energy percentage and estimated time remaining separate. No source review for these entries occurred in ISA-03D.

ISA-03 parent progress:16 of42 properties reviewed,26 remain in E–J. Model/Serial Number stay credited to ISA-02. Normal batch ceilings remain4–6 simple definitions or1–3 dense items, at most4 new supporting definitions and6 materially changed rows, including verification/publication. Reuse the exact-input artifact download, current workbook and checksummed publication assembler. No new transport/export infrastructure.

## Spatial meanings retained

Perceived Position reports hardware position while ordinary Position is overridden and is **optional**, not required whenever override is supported. Position reports the current position of its identified component. Position Override supplies an overriding position value; it does not itself establish active state, permissions, physical motion or improved accuracy.

Orientation has a world-space role distinct from prior Attached Orientation and Local Orientation. **ISA-Q003** preserves the source's ECEF label and true-north/right/gravity-down axis wording. Rotation has required yaw/pitch/roll with the defined sequential axes. No guessed frame identifier or numeric transformation was adopted. Reconcile exact numeric frame interpretation in the later Rotation/spatial-guidance subpass; do not repeat the finished four-entry review.

Geographic Position requires latitude/longitude and has optional altitude/error terms and source default conventions. Do not interpret default zeros as perfect measured accuracy or missing altitude as a supplied height. Component position does not establish the precise physical probe, feature-of-interest or observation location.

## Completed work and prior questions

ISA-01 census:480 named DMS entries,279 source blocks,31 original row/topic targets,25 prior ISA findings; eleven original2023 source titles verified. ISA-02:49 properties reviewed, Manufacturer/Model/Serial Number corrected, UCI's unsupported network-scope restriction removed. ISA-03A:four Status/name/state entries integrated. ISA-03B:six ownership/version/support entries integrated. None is reopened by a historical transfer error or an old “pending” label.

Level (ISA-Q001) and Link Loss (ISA-Q002) retain their precise definition questions; Orientation ISA-Q003 is additional and local. A completed source review with a recorded interpretation question remains completed. Owner model adoption and tested implementation are separate tasks, not reasons to label the correction indefinitely unfinished.

Original58 non-ISA primary donor records,73 equipment-source statements, prior case values, identity and Camera Mode matches are preserved. Current review remains14 columns: four cases left, established donor order, foundational standards adjacent, proposed DIM rightmost. New case cells say Not linked here; other donor cells Not assessed here.

## Source recovery and supporting evidence

Primary source: ISA DMS6.0r12 dated31 October2023, Files identifier `file_00000000ca1c81f48a3ccd49273425f8`; source register has companion editions/handles. Use Files by exact edition if a handle fails. Raw-byte export failure does not establish original text absence. ISA-03C read property text pp.14–15/PDF29–30, Geographic Position p.95/PDF110 and Rotation pp.111–112/PDF126–127. Geographic Position's original page image was inspected; property-page image access failed and is not claimed.

Reuse ISA-02 supporting evidence for Rotation, Geographic Position, Measured Degrees, Degrees and Meters. Their reuse does not add five unique definitions or complete their future full catalogue assignments. Full child-field/constraint checks remain tied to original source entries.

## Workload, publication and recovery

One “proceed” authorizes only the named child batch. Start with4–6 straightforward or1–3 dense entries, at most4 newly inspected support definitions and6 changed information rows. Include checking, visual inspection and actual GitHub publication in the workload. Split unexpected expansion with exact remaining IDs; do not omit entries or invent a match. Reuse the existing workbook/export and checksummed publication route; no new infrastructure campaign.

The Actions exact-input artifact export works when current repository files are not mounted. Verify the current workbook hash before editing. Publication uses the established exact-file assembler and a read-only postcommit check. Preserve prior snapshots; do not overwrite an old source-review workbook to erase its history.

Historical checkpoints: [ISA-02](ISA02_Publication_Record_07NOV2026.json), [ISA-03A](ISA03A_Publication_Record_07NOV2026.json), [ISA-03B](ISA03B_Publication_Record_07NOV2026.json). Their completed records are history; the current routing is this ISA-03D document and progress. Obsolete “ISA-03A integration pending” instructions were removed from active status during ISA-03C closeout.

**Next “proceed” = ISA-03E only. ISA-03D source review, workbook integration and GitHub delivery COMPLETE.**
