# Current PITON — ISA correction after ISA-03B

**7 November 2026 · ISA-01, ISA-02 and child batches ISA-03A/B COMPLETE. Next owner “proceed”: ISA-03C ONLY.**

## Current authority and exact next task

Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. GitHub is authoritative. [Current workbook](ISA_Correction_Review_ISA03B_07NOV2026.xlsx) · [Current horizontal view](ISA_Correction_Review_ISA03B_07NOV2026.md) · [ISA-03B report](ISA03B_Ownership_Versions_Support_07NOV2026.md) · [Exact source evidence](ISA03B_Ownership_Versions_Support_Evidence_07NOV2026.json) · [Coverage](ISA_Coverage_Register_07NOV2026.json) · [Progress](ISA_Correction_Status_07NOV2026.json) · [Publication](ISA03B_Publication_Record_07NOV2026.json) · [Plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Lessons](LESSONS_Donor_Review_Process.md).

ISA-03B reviewed Owner, Parameter Version, Program of Record, Software Version, Specification Version and Support. **Six of six supported**, with five Accepted extensions and one core entry (Specification Version). All six are separate candidate rows in Identity and contacts. Source support uses original DMS §3.1 pp.14–17/PDF29–32; POC text and original page121 image checked; String and Resource Descriptor/Resource Type dependencies reused from ISA-02. Unique supporting definitions remain47. No new source questions.

Current grid: **86 information/review rows**, original31 plus **53 supported candidates and two existing question rows**. **59 primary entries reviewed / 57 supported / two existing questions**. Earlier source rows and all non-ISA/equipment values are preserved. Parent ISA-03: ten of42 properties reviewed,32 remain; original ISA-02 Model/Serial Number are not counted twice. Later catalogue passes are not falsely marked complete by supporting-type reuse.

**Next ISA-03C only:** Orientation (ISA-DMS-083), Perceived Position (086), Position (088), Position Override (089). Read their original definitions and relevant existing spatial support. Preserve reference-frame and override distinctions; do not infer a physical probe coordinate from a station position. Do not execute ISA-03D or any other donor. Normal ceilings remain4–6 simple definitions,1–3 dense items, at most4 new support definitions and6 changed information rows, including verification/publication workload.

**Distinct ISA-03B meanings:** Owner is component-specific ownership contact information, not permission. Program of Record is represented through a POC list, not an acquisition ID or procurement status. Support excludes maintenance, which stays separate. Parameter Version reports the version of hardware/software parameters unavailable through ISA; not the parameter values and not an absolute immutability rule. Software Version identifies running software. Specification Version reports ISA compatibility, not an independent conformance certificate.

ISA-03A's transfer issue is resolved. The existing exact-input Actions artifact export and exact-file publication route work; reuse them instead of creating a new exporter. Current source decisions/workbook/progress are the ISA-03B checkpoint. Do not repeat completed ISA-01/02/03A reviews or use historical “pending integration” language below to reopen finished work.

## Historical ISA-03A checkpoint and continuing source rules

Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`; directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. GitHub is the authoritative project home.

Read [current progress](ISA_Correction_Status_07NOV2026.json), [current workbook](ISA_Correction_Review_ISA03A_07NOV2026.xlsx), [horizontal comparison](ISA_Correction_Review_ISA03A_07NOV2026.md), [four exact source decisions](ISA03A_Status_Name_State_Evidence_07NOV2026.json), [closeout](ISA03A_Status_Name_State_07NOV2026.md), [coverage register](ISA_Coverage_Register_07NOV2026.json), and [publication verification](ISA03A_Publication_Record_07NOV2026.json). The [revised execution plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) and [living lessons](LESSONS_Donor_Review_Process.md) govern the small-batch process.

**ISA-03A source review and integration are complete.** Do not repeat either because an old checkpoint refers to a transfer failure. The ISA-02 workbook/evidence stay as immutable historical inputs; the active review is ISA-03A. Parent ISA-03 remains in progress, with 38 remaining properties assigned to ISA-03B–J. The twelve work-package labels are not a twelve-prompt estimate.

The integration added exactly four candidate rows, keeping all older rows and non-ISA/equipment values. The current workbook has twelve tabs and 80 information/review rows. Primary source coverage is 53 reviewed entries: 51 supported outcomes plus the same two Level/Link Loss questions. There are 49 additional candidate/question rows: 47 supported plus two questions. Forty-seven unique supporting type definitions are recorded; their later catalogue passes remain separate.

## New completed source work — exact four entries

The following were checked against original ISA DMS 6.0r12 §3.1, printed p.14 / PDF p.29. All four are core properties. Relevant ICD 6.0r5 §6.5, printed pp.21–22 / PDF pp.29–30, was read for Status publication behavior.

| ID | Native property | Candidate ID and proposed label | Crucial source boundary |
| --- | --- | --- | --- |
| ISA-DMS-078 | Maximum Status Interval | ISA-C-078 — Maximum interval between component Status reports | Status heartbeat upper bound, not sensor sampling or observation resultTime. No installed value or proof of liveness inferred. |
| ISA-DMS-079 | Minimum Status Interval | ISA-C-079 — Minimum interval between component Status reports | Lower spacing bound with cached changes; not a sample period or a guaranteed history of all transitions. |
| ISA-DMS-081 | Name | ISA-C-081 — Changeable component display name | Human-friendly and reassignable; not persistent UCI, manufacturer, model or serial identity. |
| ISA-DMS-082 | Operating State | ISA-C-082 — Reported component operating condition | Component state itself, not ISA lifecycle, selected mode, power state or capability readiness. Preserve Camera Mode separately. |

All four support these specific candidate information rows; there are no new source-definition questions in this batch. Candidate fit is direct to the narrowly worded proposed information element, not adopted model equivalence. No non-ISA donor, existing case value or prior identity mapping changed.

Four supporting definitions were inspected/reused: **Secs** (DMS §4.2 p.55/PDF70), **String** (§4.1 p.50/PDF65), **General State** (pp.93–94/PDF108–109) and **General Code** (p.79/PDF94). General State has required `code`, optional machine-readable `subcode` and optional human-readable `details`; its sealed code enumeration is FAILURE, FAULT, OK, UNINITIALIZED, WARNING. Do not count supporting-type checks as completion of their later catalogue passes or add them to unique dependency totals without checking existing IDs.

A source-page image request failed because raw-byte backing was unavailable. Original indexed text was readable and inspected; do not claim a visual PDF inspection or source absence.

## Completed ISA-03B assignment — retained scope

Review only these six ISA-03B entries: Owner (ISA-DMS-084), Parameter Version (085), Program of Record (092), Software Version (108), Specification Version (109), and Support (110). Follow the bounded batch policy: preflight relevant types and existing evidence, preserve source core/extension standing, integrate supported outcomes and verify the GitHub publication, then stop before ISA-03C.

Reuse the working GitHub Actions artifact download when a repository workbook is not already mounted. Read-only workflow artifacts can carry the exact committed input files; verify the workbook hash before editing. This resolves the earlier missing-local-copy problem without repeating source review.

ISA-03A's four saved properties and supporting Secs/String/General State/General Code evidence are already integrated. Operating condition remains distinct from a selected mode; the existing Camera Mode row is preserved. Do not fill new other-donor or equipment cells by inference.

## Workload limits retained

Normal source batches start with four to six simple primary definitions or one to three dense items, at most four newly inspected supporting definitions and six new/materially revised information rows. Count nested fields and dependencies as work. Reserve room for source checking, visual inspection, repository publication and readback. These are planning ceilings, not guarantees or quotas.

Preflight exact source IDs, likely dependencies, affected rows, source access and the existing publication route. Reuse verified same-edition supporting evidence. Do not combine semantic research with designing a new exporter/transport system. If scope grows, publish the supported named subset and assign its exact remainder; never invent a meaning to finish a batch.

The plan permits one bounded publication repair attempt, then preserving evidence through a working GitHub action and naming the specific repair as next. That was a historical intermediate checkpoint; ISA-03A and ISA-03B are now integrated. No unbounded debug loop, no sandbox-only handoff and no false binary-publication claim.

The original 42-property ISA-03 package is partitioned into ISA-03A–J with zero duplicated or unassigned IDs. Four are reviewed in this saved batch; 38 remain for later child batches. Model and Serial Number were already completed and remain excluded. Zones and Zoom on printed p.18/PDF33 remain assigned despite sharing the page with Observables. Later architecture and final-audit work also require bounded child batches.

## Earned earlier progress — preserved

ISA-01 inventoried **480 named DMS entries**, **279 source blocks**, **31 original row/topic targets** and **25 earlier ISA findings**. Eleven 2023 originals were identified. The historical 2015 paper is a local context-access item, not a blocker for readable primary sources. Inventory entry counts are not mapping counts.

ISA-02 completed **49 property reviews**: **47 supported outcomes and two precise definition questions**. The source-standing split was 46 core plus Hardware Version, Maintenance and Manufacturer POC as three accepted extensions. Manufacturer, Model and Serial Number are corrected; UCI's unsupported network-scope restriction was removed. Four identity row targets and old ISA-M01 were reconciled.

Camera Mode supplies a camera-specific current-mode correspondence. Forty-three supported candidate rows and two question rows expanded the original 31 review rows to 76. New non-ISA cells read Not assessed here and new equipment cells read Not linked here. The original 58 primary donor records, 73 case-evidence statements and earlier non-ISA values remain unchanged. Historical v0.9 and ISA-01 artifacts remain history.

Forty-six supporting definitions were inspected in ISA-02; their future full catalogue passes were not marked complete. The earlier ISA-02 technical checkpoint is [34963db](https://github.com/OS4CSAPI/glaux-client/commit/34963db95c38c49c19683a80d97c146c7638fd60), with [publication record](ISA02_Publication_Record_07NOV2026.json) and [read-only verification](https://github.com/OS4CSAPI/glaux-client/actions/runs/42392228728). The four-entry supplement is now integrated in the current ISA-03A workbook; [publication record](ISA03A_Publication_Record_07NOV2026.json) identifies the verified checkpoint.

## Source distinctions and specific questions retained

Manufacturer may mean producer or vendor; not every vendor is the fabricator. Model refers to the manufacturer's product line. Serial identity is component-scoped, with uniqueness expected from manufacturer/model/serial together. UCI can identify a virtual component and need not be a URI; syntax/certificate requirements do not authenticate our case examples.

Maintenance is a contact list, not maintenance history. Identity is tactical classification, not UCI/serial. Enabled is permission to become active; Active reports operation. Data Inputs/Outputs concern current transfers rather than available Resources or output schemas. Attached versus Local transforms have different frames and order. Field of Regard is scan-wide; Field of View instantaneous. AC/DC and source/load quantities stay separate. Camera Mode's source-specific representation rule is not a universal physical-component rule.

**ISA-Q001 Level:** Percent is declared without property-definition prose. Related level-control context was checked; the referent remains a precise ISA-05/06 or ISA-11 source question.
**ISA-Q002 Link Loss:** Db is declared without reference quantity/sign convention. Do not infer packet-loss percentage or a particular attenuation model; revisit an applicable ISA-09/11 child batch.
These questions do not reopen ISA-02 or prevent completing unrelated source reviews.

## Source recovery, checking and continuity

Original 31 October 2023 files: DMS 6.0r12 `file_00000000ca1c81f48a3ccd49273425f8`; SDD 6.0r5 `file_000000004c10824683c0a84b37f24a3b`; ICD 6.0r5 `file_000000008de0820e8e33af2cb096bb12`; Component Requirements 6.0r4 `file_00000000ed048210a141e046f2e93a17`; Controller Requirements 6.0r4 `file_00000000e00082109d88d0119f744880`. The source register carries companion titles. If an identifier fails, search by exact title/revision. Indexed text can remain readable when raw PDF/image export fails; do not manufacture an access gap.

Manufacturer is printed p.13/PDF28, Model p.14/PDF29, Serial Number p.16/PDF31. ISA-02's UCI reconciliation used DMS §4.2 p.55/PDF70, ICD §6.1 p.19/PDF27 and Component Requirements §4.1.1 pp.7–9/PDF14–16. Universal/Unique is a document naming distinction, not two identifiers.

Each delivery must be verified at its actual GitHub commit. Coverage and semantic checks differ from file/formula/hash checks. The ISA-02 twelve-tab workbook was visually inspected and corrected before its verified export; do not repeat its preparation solely because batch size changed. The four ISA-03A candidates are integrated; summary and changed row areas were visually inspected, with exported values/formula caches verified.

Maintain the living lessons record only when a new substantive observation warrants an entry. The current interruption is already covered by the publication and bounded-work rules; no additional research campaign is authorized. Preserve case precision: reference designs versus deployed units, two original NOAA means versus four API representations, and unknown historical result availability remain distinct.

**The historical instructions above do not override the current ISA-03C handoff at the top of this PITON.**
