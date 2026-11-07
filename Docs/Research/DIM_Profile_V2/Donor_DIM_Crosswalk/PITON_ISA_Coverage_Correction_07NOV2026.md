# Current PITON — ISA correction after ISA-02

**7 November 2026 · ISA-02 COMPLETE · correction progress 2/12 · next owner “proceed”: ISA-03 ONLY.**

## Current authority and durable handoff

Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`; working directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. GitHub is the authoritative project home. The former ISA-01 publication failure was repaired; do not redo its completed census or use an old “0/12,” “1/12” or sandbox-only label to reverse current progress.

Read [progress](ISA_Correction_Status_07NOV2026.json), [current workbook](ISA_Correction_Review_ISA02_07NOV2026.xlsx), [horizontal view](ISA_Correction_Review_ISA02_07NOV2026.md), [ISA-02 closeout](ISA02_Identity_and_Properties_07NOV2026.md), [exact evidence](ISA02_Identity_and_Properties_Evidence_07NOV2026.json), [coverage](ISA_Coverage_Register_07NOV2026.json), [validation](ISA02_Validation_07NOV2026.json), and [lessons](LESSONS_Donor_Review_Process.md). The [twelve-pass plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) and [ISA-01 boundary amendment](ISA01_Plan_Amendment_07NOV2026.md) still govern. The publication record stores the actual committed checkpoint and workflow verification.

## Earned progress

ISA-01 inventoried **480 named DMS entries**, **279 source blocks**, **31 original row/topic targets** and **25 earlier ISA findings**. Eleven 2023 originals were identified; the 2015 historical paper remains a specific context-access item, not a blocker for the available primary corpus. The inventory count is not a mapping count.

ISA-02 reviewed **all 49 assigned properties**: **47 source-supported correspondences** and **two exact source-definition questions**. The core/extension split is **46 core + three accepted extensions** (Hardware Version, Maintenance, Manufacturer POC). Manufacturer, Model and Serial Number now appear in the identity rows. UCI's earlier “network-scoped” gloss was removed because the original source defines component uniqueness, with lexical and virtual-identifier rules. Four identity row targets and the old ISA-M01 are reconciled.

Camera Mode adds a camera-specific current-mode correspondence; the broader operating-mode row still has its assigned ISA-03 reconciliation. The remaining property contributions are visible as **43 source-supported candidate rows plus two question rows**. The corrected review has 76 information/review rows: original 31 + new 45, in grouped fourteen-column form. Other donor cells in newly added rows say “Not assessed here”; equipment cells say “Not linked here.” Existing non-ISA/equipment cells, original 58 primary donor records and 73 case evidence statements are unchanged. Historic v0.9 and ISA-01 files remain history, not overwritten technical baselines.

Forty-six referenced type definitions were inspected to support the 49 property decisions. Their later full catalogue passes are not falsely marked complete or counted twice. Source entry review, mapping fit, candidate-row acceptance and publication are separate fields.

## Actual source distinctions to retain

Manufacturer is a component manufacturer/producer/vendor String: do not turn every vendor label into the actual fabricator. Model describes the manufacturer's product line. Serial Number is component-scoped, with uniqueness expected from manufacturer/model/serial together; physical hardware interpretation requires the component context. UCI need not be a URI and can identify a virtual component; syntax and certificate-binding requirements do not authenticate our examples.

Maintenance is a POC list, not maintenance history. Identity is tactical classification via Standard Identity, not UCI or a serial. Enabled is permission to become active; Active reports operation. Data Inputs/Outputs describe current transfers, distinct from available Resources and output-field schemas. Attached transforms and own-frame Local transforms have different reference frames and order. Field of Regard is scan-wide while Field of View is instantaneous. AC/DC and source/load quantities remain separate. Do not promote a source-specific Camera Mode component-representation rule to a universal physical-component rule.

**ISA-Q001 Level:** Percent declared but no property-description prose. Related level-control commands and Auto Level context were checked; exact referent is not forced. Revisit in ISA-05/06 command context and ISA-11 guidance.
**ISA-Q002 Link Loss:** Db declared but no reference quantity/sign convention. Do not infer packet-loss percentage or a specific propagation attenuation definition; revisit applicable ISA-09/11 source guidance.
Both entries have complete source-review outcomes with precise questions. They do not cancel ISA-02 completion or hold unrelated rows hostage.

## Source recovery and method

Original 31 October 2023 files: DMS 6.0r12 `file_00000000ca1c81f48a3ccd49273425f8`; SDD 6.0r5 `file_000000004c10824683c0a84b37f24a3b`; ICD 6.0r5 `file_000000008de0820e8e33af2cb096bb12`; Component Requirements 6.0r4 `file_00000000ed048210a141e046f2e93a17`; Controller Requirements 6.0r4 `file_00000000e00082109d88d0119f744880`. The source register carries all eleven original titles and companions. Use Files search/find/read by exact edition when a prior identifier fails.

Raw PDF/image export can fail while original indexed text remains readable. Do not declare those sources unavailable. In ISA-02, requested DMS images failed; full original text, body extension markings, cross-page continuations and referenced definitions were inspected. Do not claim unavailable source pictures were seen. Source text slices have leading/trailing whitespace quirks: join using verified page/overlap evidence rather than assuming every materialized slice has precisely the requested line count.

Manufacturer is p.13/PDF28, Model p.14/PDF29, Serial Number p.16/PDF31. The completed ISA-02 block is 47 first-block properties plus Model and Serial Number, exactly 49 primary entries. UCI reconciliation used DMS §4.2 p.55/PDF70, ICD §6.1 p.19/PDF27, Component Requirements §4.1.1 pp.7–9/PDF14–16. Universal/Unique is a source-document spelling distinction, not two invented identifiers.

## Next exact task: ISA-03

Review the **42 remaining DMS §3.1 properties** assigned ISA-03, from printed p.14 through p.18, excluding already-assigned Model and Serial Number. Include **Zones and Zoom on p.18/PDF33** even though that page also begins Observables. Follow each definition to completion, inspect its referenced types, verify core/extension standing from the body, and assign a supported existing/new candidate row or exact source question.

Use the current row and evidence ledger, not only the initial 22-row proposal. Reconcile state/mode and applicable case topics without inventing deployed values. Do not conflate Operating State with the ISA connection lifecycle. Preserve existing non-ISA cells, original case precision, the four leftmost examples, adjacent foundational standards, and DIM at far right. ISA-04 observables, Step16 owner adoption, Profile/UML, runtime and deployment remain separate.

## Publication, checking and lessons

Every delivery goes to GitHub on the research branch and is read back from the actual commit. The workbook, source registers, readable view, status and this PITON must agree. Verify the current source record set and original-cell preservation separately from file hashes and formulas. One generated ledger matching another does not establish source coverage.

The current workbook has twelve tabs, including ISA Evidence, Dependencies and Questions. Summary, identity rows and added rows were visually inspected; exported values and formula caches were checked. A summary merge-layout issue found in rendering was corrected before export. The final workbook has no formula-error values. No original case/non-ISA fact changed.

Maintain one [living lessons record](LESSONS_Donor_Review_Process.md); add a lesson only when actual review supplies new evidence. At ISA-12 consolidate demonstrated practices, not the arbitrary number of passes, for reuse with other donors. Completed work remains complete. Reopen a particular claim only for specific new evidence, not a generic “unfinished model” caveat.

**Next “proceed” = ISA-03 only.** ISA-02 source review and GitHub delivery are the checkpoint; there is no census restart.


## Repository verification

[Publication record](ISA02_Publication_Record_07NOV2026.json) · [Read-only verification of the published commit](https://github.com/OS4CSAPI/glaux-client/actions/runs/42392228728). The correction remains 2/12; next ISA-03 only.
