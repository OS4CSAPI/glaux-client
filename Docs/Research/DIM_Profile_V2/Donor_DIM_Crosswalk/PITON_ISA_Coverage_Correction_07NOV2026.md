# Current PITON — ISA correction after the ISA-03A source review

**7 November 2026 · ISA-01 and ISA-02 COMPLETE. ISA-03A: four of four source reviews COMPLETE and committed. Current workbook/register integration is pending. Next owner “proceed”: ISA-03A-PUBLISH ONLY.**

## Current authority and durable handoff

Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`; directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. GitHub is the authoritative project home. The completed ISA-01 census and ISA-02 results remain valid. Do not redo completed work because an old checkpoint or a separate publication action is pending.

**Read first:** [current progress and precise next action](ISA_Correction_Status_07NOV2026.json), [ISA-03A four-entry report](ISA03A_Status_Name_State_07NOV2026.md), and [exact saved source evidence](ISA03A_Status_Name_State_Evidence_07NOV2026.json). These four decisions are saved in GitHub, not only in a sandbox. Source evidence commit: `e1e0272ff6416484a095a1c6ea855e361e13afd4`; readable delta commit: `a5519ad371ad1d60e20e84c7c761dc9db9a4a0a7`.

The last integrated artifacts are still the [ISA-02 workbook](ISA_Correction_Review_ISA02_07NOV2026.xlsx), [horizontal view](ISA_Correction_Review_ISA02_07NOV2026.md), [ISA-02 evidence](ISA02_Identity_and_Properties_Evidence_07NOV2026.json), [coverage register](ISA_Coverage_Register_07NOV2026.json), and [validation](ISA02_Validation_07NOV2026.json). They were not overwritten during ISA-03A. The [revised execution plan](PLAN_ISA_Coverage_Correction_07NOV2026.md), [ISA-01 boundary amendment](ISA01_Plan_Amendment_07NOV2026.md) and [living lessons](LESSONS_Donor_Review_Process.md) remain in force.

**Execution precedence:** current progress and this PITON specify the publication/integration part of ISA-03A, not permission to repeat its source reading or begin ISA-03B. The owner's post-ISA-02 sizing instruction still overrides all older full-block instructions. ISA-01 through ISA-12 are work-package labels, not a twelve-prompt estimate.

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

## Next exact task: ISA-03A-PUBLISH — no further source-property review

**Apply the four saved decisions to the actual current workbook, current readable review and coverage register, then verify the committed output.** Reuse the existing workbook and publication machinery. Confirm the four candidate IDs do not duplicate current candidate rows, preserve the fourteen-column case-first/standards-adjacent/DIM-right format, and carry the precise source meanings and extensions into the evidence sheet.

Before integration the current register reports 49 reviewed primary entries. These four separately saved reviews make **53 completed source reviews in total**. When integrating, update the register once: 51 supported outcomes and the two existing record-local questions. Do not count the four again. The current 76 information/review rows would become 80 if all four candidates are added after duplicate-ID checking. This is an anticipated integration delta, not a claim that the current workbook already contains them.

The actual obstacle in this turn was transfer of the current workbook binary into the workspace. Direct runtime download failed on DNS resolution and the separate public raw-file download route did not resolve the file. GitHub text fetch/create/update actions worked and saved the evidence. **This is not evidence that the workbook is missing or that all GitHub binary access is impossible.** Do not attribute it to a model switch. Do not rebuild the workbook from an older ISA-01 snapshot, erase ISA-02 work, or repeat these four source reviews.

No workbook export, formula/visual check, or GitHub Actions pass occurred for ISA-03A in this text-only checkpoint. Once integration and readback pass, mark ISA-03A delivered and name ISA-03B next. Until then, the current action is publication/integration only. This narrow pending action does not turn completed source work into a generic unfinished-project warning.

## Workload limits retained

Normal source batches start with four to six simple primary definitions or one to three dense items, at most four newly inspected supporting definitions and six new/materially revised information rows. Count nested fields and dependencies as work. Reserve room for source checking, visual inspection, repository publication and readback. These are planning ceilings, not guarantees or quotas.

Preflight exact source IDs, likely dependencies, affected rows, source access and the existing publication route. Reuse verified same-edition supporting evidence. Do not combine semantic research with designing a new exporter/transport system. If scope grows, publish the supported named subset and assign its exact remainder; never invent a meaning to finish a batch.

The plan permits one bounded publication repair attempt, then preserving evidence through a working GitHub action and naming the specific repair as next. That is the state now: four source decisions saved, current workbook untouched, one integration action next. No unbounded debug loop, no sandbox-only handoff and no false binary-publication claim.

The original 42-property ISA-03 package is partitioned into ISA-03A–J with zero duplicated or unassigned IDs. Four are reviewed in this saved batch; 38 remain for later child batches. Model and Serial Number were already completed and remain excluded. Zones and Zoom on printed p.18/PDF33 remain assigned despite sharing the page with Observables. Later architecture and final-audit work also require bounded child batches.

## Earned earlier progress — preserved

ISA-01 inventoried **480 named DMS entries**, **279 source blocks**, **31 original row/topic targets** and **25 earlier ISA findings**. Eleven 2023 originals were identified. The historical 2015 paper is a local context-access item, not a blocker for readable primary sources. Inventory entry counts are not mapping counts.

ISA-02 completed **49 property reviews**: **47 supported outcomes and two precise definition questions**. The source-standing split was 46 core plus Hardware Version, Maintenance and Manufacturer POC as three accepted extensions. Manufacturer, Model and Serial Number are corrected; UCI's unsupported network-scope restriction was removed. Four identity row targets and old ISA-M01 were reconciled.

Camera Mode supplies a camera-specific current-mode correspondence. Forty-three supported candidate rows and two question rows expanded the original 31 review rows to 76. New non-ISA cells read Not assessed here and new equipment cells read Not linked here. The original 58 primary donor records, 73 case-evidence statements and earlier non-ISA values remain unchanged. Historical v0.9 and ISA-01 artifacts remain history.

Forty-six supporting definitions were inspected in ISA-02; their future full catalogue passes were not marked complete. The last integrated technical checkpoint is [34963db](https://github.com/OS4CSAPI/glaux-client/commit/34963db95c38c49c19683a80d97c146c7638fd60), with [publication record](ISA02_Publication_Record_07NOV2026.json) and [read-only verification](https://github.com/OS4CSAPI/glaux-client/actions/runs/42392228728). Current four-entry text evidence is a supplement pending integration, not a replacement for that checkpoint.

## Source distinctions and specific questions retained

Manufacturer may mean producer or vendor; not every vendor is the fabricator. Model refers to the manufacturer's product line. Serial identity is component-scoped, with uniqueness expected from manufacturer/model/serial together. UCI can identify a virtual component and need not be a URI; syntax/certificate requirements do not authenticate our case examples.

Maintenance is a contact list, not maintenance history. Identity is tactical classification, not UCI/serial. Enabled is permission to become active; Active reports operation. Data Inputs/Outputs concern current transfers rather than available Resources or output schemas. Attached versus Local transforms have different frames and order. Field of Regard is scan-wide; Field of View instantaneous. AC/DC and source/load quantities stay separate. Camera Mode's source-specific representation rule is not a universal physical-component rule.

**ISA-Q001 Level:** Percent is declared without property-definition prose. Related level-control context was checked; the referent remains a precise ISA-05/06 or ISA-11 source question.
**ISA-Q002 Link Loss:** Db is declared without reference quantity/sign convention. Do not infer packet-loss percentage or a particular attenuation model; revisit an applicable ISA-09/11 child batch.
These questions do not reopen ISA-02 or prevent completing unrelated source reviews.

## Source recovery, checking and continuity

Original 31 October 2023 files: DMS 6.0r12 `file_00000000ca1c81f48a3ccd49273425f8`; SDD 6.0r5 `file_000000004c10824683c0a84b37f24a3b`; ICD 6.0r5 `file_000000008de0820e8e33af2cb096bb12`; Component Requirements 6.0r4 `file_00000000ed048210a141e046f2e93a17`; Controller Requirements 6.0r4 `file_00000000e00082109d88d0119f744880`. The source register carries companion titles. If an identifier fails, search by exact title/revision. Indexed text can remain readable when raw PDF/image export fails; do not manufacture an access gap.

Manufacturer is printed p.13/PDF28, Model p.14/PDF29, Serial Number p.16/PDF31. ISA-02's UCI reconciliation used DMS §4.2 p.55/PDF70, ICD §6.1 p.19/PDF27 and Component Requirements §4.1.1 pp.7–9/PDF14–16. Universal/Unique is a document naming distinction, not two identifiers.

Each delivery must be verified at its actual GitHub commit. Coverage and semantic checks differ from file/formula/hash checks. The ISA-02 twelve-tab workbook was visually inspected and corrected before its verified export; do not repeat its preparation solely because batch size changed. The four ISA-03A candidates still need their own integration and changed-area inspection.

Maintain the living lessons record only when a new substantive observation warrants an entry. The current interruption is already covered by the publication and bounded-work rules; no additional research campaign is authorized. Preserve case precision: reference designs versus deployed units, two original NOAA means versus four API representations, and unknown historical result availability remain distinct.

**Next “proceed” = ISA-03A-PUBLISH only. Preserve the completed four-entry source review; finish its current-workbook integration; do not start ISA-03B.**
