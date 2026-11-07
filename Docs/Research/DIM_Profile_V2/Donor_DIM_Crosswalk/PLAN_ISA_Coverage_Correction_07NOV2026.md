# ISA coverage correction — execution plan

**7 November 2026 · Sizing revision after ISA-02 · ISA-01 and ISA-02 COMPLETE. Next owner “proceed”: ISA-03A ONLY — four named properties.**

**The former twelve-prompt estimate is withdrawn.** ISA-01 through ISA-12 now identify the twelve existing work packages, not a promise that each package fits one prompt. Remaining packages execute through explicitly bounded child batches. No completed source work is reopened by this scheduling correction.

[Current PITON](PITON_ISA_Coverage_Correction_07NOV2026.md) · [Progress and next batch](ISA_Correction_Status_07NOV2026.json) · [Current workbook](ISA_Correction_Review_ISA02_07NOV2026.xlsx) · [Current comparison](ISA_Correction_Review_ISA02_07NOV2026.md) · [Source inventory](ISA_DMS_Entry_Inventory_07NOV2026.csv) · [Coverage register](ISA_Coverage_Register_07NOV2026.json) · [Lessons](LESSONS_Donor_Review_Process.md).

The [prior plan at the verified ISA-02 commit](https://github.com/OS4CSAPI/glaux-client/blob/34963db95c38c49c19683a80d97c146c7638fd60/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PLAN_ISA_Coverage_Correction_07NOV2026.md) preserves the original planning history. This revision changes execution sizing and progress reporting, not the source coverage or completion requirements.

## 1. What failed in sizing

ISA-02 combined 49 primary properties, 46 supporting definitions, 45 additional information/question rows, UCI reconciliation, workbook preparation, checking and publication. Its [published results](ISA02_Publication_Record_07NOV2026.json) remain complete, but that was too much work for a deliberately small one-prompt iteration. The original plan already permitted subdivision; it was not applied before starting the oversized batch.

A page block or number of headings is not the full workload. Size the complete task: source definitions, dependencies, semantic decisions, table edits, verification and actual GitHub publication. The platform failure's technical cause is not established by this workload observation. Do not invent a model/platform explanation or claim a particular item count guarantees reliability.

## 2. Binding one-prompt limits

These are conservative planning ceilings, **not completion quotas and not a license to skip source entries**.

- Start with **four to six straightforward primary definitions**, or **one to three dense commands, composite types or architectural questions**. The specifically listed child batch, not its entire parent work package, is authorized by “proceed.”
- Budget no more than **four newly inspected supporting definitions** and **six new or materially revised information rows** in a normal source batch. Reuse exact-edition previously verified supporting evidence where applicable; do not reread forty-six definitions to repair four rows. A dense definition with many independent nested fields must be divided into explicitly named field groups rather than counted as one trivial item.
- Before substantive review, identify the exact source IDs, likely dependencies, affected rows, source-access route and existing publication path. A short source scan may establish this workload; it must not silently become a full additional review. If the batch exceeds the budget, reduce it before starting and assign every remaining item to a named continuation. Do not enlarge a short batch merely to use the ceiling.
- Reserve workload for updating the existing review workbook/evidence, source checking, preservation checks, visual inspection of changed areas, GitHub commit and readback. Reuse the existing formats and working publication machinery. Do not combine semantic review with designing a new exporter, rewriting the workbook or building a new transfer architecture.
- If unexpected dependencies expand the task, finish only the supported named subset and publish that checkpoint; register the exact unresolved dependency and continuation. Never convert unread material into a false no-match or completed interpretation question.
- Permit one bounded publication repair attempt within the batch. If the established publication route still fails, stop adding semantic work, preserve the exact evidence through the smallest working GitHub write action, and identify publication repair as the sole next action. Do not lose completed research, claim an unverified publication, or enter an unbounded debug/rebuild cycle.

Every normal batch ends with a reviewable table delta and the actual repository checkpoint. A separately necessary publication repair is a named action, not a reason to redo semantic research. Sandbox files never substitute for the GitHub handoff.

## 3. Exact remaining-property batches

The inventory assigns 42 unreviewed properties to parent ISA-03. The table below partitions all 42 exactly once. Model (ISA-DMS-080) and Serial Number (ISA-DMS-105) are already reviewed in ISA-02 and excluded. Full definitions and relevant dependencies remain required; these groups express workload, not assumed semantic equivalence.

| Next batch | Named source entries | Inventory ID suffixes | Count |
| --- | --- | --- | ---: |
| **ISA-03A** | Maximum Status Interval; Minimum Status Interval; Name; Operating State | 078, 079, 081, 082 | **4** |
| ISA-03B | Owner; Parameter Version; Program of Record; Software Version; Specification Version; Support | 084, 085, 092, 108, 109, 110 | 6 |
| ISA-03C | Orientation; Perceived Position; Position; Position Override | 083, 086, 088, 089 | 4 |
| ISA-03D | Relationship; Visible | 099, 118 | 2 |
| ISA-03E | Power; Power State; Reserve Capacity; Time to Empty | 090, 091, 100, 113 | 4 |
| ISA-03F | Polarity; Pulse Interval; Quality; Radar Mode; Resolution; Zoom | 087, 093, 094, 095, 101, 121 | 6 |
| ISA-03G | Range; Scan Time; Wavelengths | 096, 104, 119 | 3 |
| ISA-03H | Velocity; View Area; Zones | 116, 117, 120 | 3 |
| ISA-03I | Receive Data Rate; Receive Power; Signal Strength Ratio; Transmit Data Rate; Transmit Power | 097, 098, 107, 114, 115 | 5 |
| ISA-03J | Resources; Satellites; Shots; Tamper State; Temperature | 102, 103, 106, 111, 112 | 5 |
| **Total** | **Every remaining ISA-03 property assigned; zero duplicates or omissions** | **All IDs 078–121 except 080 and 105** | **42** |

This is a ten-batch starting schedule for ISA-03, not ten newly completed tasks. Each batch still undergoes the dependency check above; a further split, if actually needed, is explicit and retains every named item. ISA-03 completes only after all child assignments have dispositions and the block is reconciled.

**ISA-03A scope:** read the four property definitions in DMS 6.0r12, printed p.14/PDF p.29, and only their necessary linked definitions/requirements. Check existing ISA-02 evidence for already verified Secs, String, General State and General Code before fetching unrelated definitions. Update the applicable current rows or justified candidate rows. Do not infer an operating mode from a general operating-state label. Publish and verify the four-entry result, then stop. No ISA-03B, new observables, or other-donor work in that prompt.

## 4. Remaining work packages are not single prompts

All entries retain their original parent owner in the coverage register; the progress record's child schedule determines the next actionable subset. A parent assignment such as ISA-09 is **not** authority to process its entire source block at once.

| Parent package | Retained scope | Required execution form |
| --- | --- | --- |
| ISA-01 | Source census and coverage baseline | COMPLETE; do not repeat. |
| ISA-02 | Identity and first property block | COMPLETE; preserve its 49 outcomes and UCI reconciliation. |
| ISA-03 | Remaining 42 properties, through Zones and Zoom on printed p.18 | Ten named child batches above, dependency-checked before each. |
| ISA-04 | All 39 observables, through Solar Radiation, Velocity and Verified By on printed p.22 | Small coherent subsets, usually 4–6 simple or 1–3 dense entries; publish their exact IDs before execution. |
| ISA-05 and ISA-06 | Entire command catalogue and commanding types, with relevant authorization/request/response requirements | Usually 1–3 commands per batch; meaningful parameters, results and dependencies count as work. No whole command-catalogue half in one prompt. |
| ISA-07 | Base types, identifiers, envelopes and message structures | Small atomic-type groups or one message/identifier question with its actual dependencies; never all envelopes/messages plus every base type in one turn. |
| ISA-08 | Capability declarations, constraints, readiness and reporting | Usually one to three closely related structures; split dense field/enum work explicitly. |
| ISA-09 and ISA-10 | Reporting types, remaining reporting types and filtering, with assigned Query Language/companion sections | Small type or named field groups; same dependency and output budget. Previously inspected supporting evidence is reused, not falsely counted twice. |
| ISA-11 | Services, bins, architecture, requirements, assigned companions and reconciliation | Separate bounded source-section batches from row/finding reconciliation. The 279 assigned blocks and 31 original row targets are not one final catch-all prompt. |
| ISA-12 | Fresh source-first audit, reusable-practice consolidation and closeout | Audit in named slices; perform final whole-register completeness/preservation checks after those slices. Final closeout cannot conceal a large new source-review campaign. |

The next child batch of a later package is listed during the preceding normal closeout. Do not consume a separate planning turn merely to divide work already understood. If an uninspected package needs real preliminary dependency work, identify it honestly as a small preparation task instead of inventing an exact total. There is no new promised total prompt count. Source coverage remains measurable; the original twelve work-package labels remain stable.

## 5. Source scope and preservation — unchanged

Use `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, under this crosswalk directory. Current technical checkpoint: [34963db](https://github.com/OS4CSAPI/glaux-client/commit/34963db95c38c49c19683a80d97c146c7638fd60). Current [ISA-02 workbook](ISA_Correction_Review_ISA02_07NOV2026.xlsx), [view](ISA_Correction_Review_ISA02_07NOV2026.md), [evidence](ISA02_Identity_and_Properties_Evidence_07NOV2026.json) and [publication record](ISA02_Publication_Record_07NOV2026.json) remain unchanged by this planning revision.

Review both directions: all existing DIM information elements against ISA, and relevant ISA source concepts that require additional or split rows. The inventory contains 480 named DMS entries, not 480 mandatory model rows; their fields, parameters, enumerations, constraints and referenced definitions are included in their parent reviews. The 279 source blocks, 31 original row/topic targets and 25 earlier findings remain assigned. Keep relevant unique concepts visible rather than hiding them in a general holds list.

Primary originals: DMS 6.0r12, SDD 6.0r5, ICD 6.0r5, Component and Controller Requirements 6.0r4, dated 31 October 2023. The corpus also includes Data Model Topics r2, Query Language Guide r4, Introductory Guide r2, White Paper r2, Certificate Guide r2 and IPL3 Guide r4. Their substantive assigned sections remain in scope. The historical 2015 paper is tracked as a specific context-access question, not a blocker for eleven readable originals. Use original Files text/images as available; failed raw export is not missing source text.

Preserve core versus Custom/Nominated/Accepted extension status from the source body, physical versus virtual/network roles, declarations versus current settings versus execution, and original events versus copies. Cite exact original title/revision/section/printed and PDF pages. Do not use earlier AI prose as original authority. Requirements, explanatory text and examples are distinguishable.

The four leftmost equipment examples, adjacent foundational standards and rightmost DIM remain. Existing non-ISA values, original 58 primary donor correspondences and 73 case facts remain unchanged. The current 76 information/review rows include candidates and questions, not automatic owner adoption. New ISA-derived rows do not authorize researching other donors. Leave their other-donor cells explicitly unassessed here. Keep historical v0.9/ISA-01/ISA-02 technical snapshots.

No other donor review, final ranking, CSAPI Profile/UML change, application/server/deployment work or physical command is authorized. Step16 owner review follows the ISA correction; Step17 remains separate.

## 6. Coverage, evidence and completion — unchanged

Every registered source entry receives a justified outcome: existing-row mapping, candidate new/split row, supporting definition, duplicate/alias with canonical entry, specifically reasoned exclusion, or a precise source/meaning question. Unreviewed work is not a no-correspondence finding. Keep review status, semantic relationship, model acceptance and publication status separate. A blank or unsuccessful keyword search cannot establish that ISA lacks a representation.

Source-backed cells preserve actual native terms, kind, scope, extension standing, source locator, meaning and relation reasoning. A field relying on another type must have sufficient inspected evidence before asserting its meaning. A specific question names the uncertainty and next action. Do not label a difficult unread dependency a completed interpretation question merely to stay within the budget.

The four cases challenge interpretations; they do not restrict the model to their observed features. Do not invent deployed settings, original result times, probe positions, equipment identities or control effects.

Batch completion means all **named batch assignments** have their justified outcomes, evidence and table changes published and checked. Reaching six records alone is not completion. Parent completion means all its child assignments and dependencies are reconciled. Record exact progress rather than converting completed child prompts into an invented percentage of the whole effort.

Final ISA completion still requires: (1) the agreed source inventory traversed and reconciled against original contents/body/index; (2) all original 22 DIM rows plus nine case topics, eleven mappings and fourteen holds accounted for; (3) unique relevant source contributions visible in traceable rows/decisions; (4) no unreviewed or unassigned work in agreed scope; (5) source-first semantic checking, coverage checks, workbook/evidence parity, visual inspection and actual GitHub readback. A well-defined interpretation question may remain local with evidence and alternatives; missing required inspection cannot be hidden that way.

Say **“ISA-03A COMPLETE”** when that batch passes, without implying the whole property package is done. Say **“ISA correction COMPLETE”** when the final tests pass. Owner model decisions remain separate. Do not attach blanket unfinished-project caveats or reopen completed work absent specific new evidence.

## 7. Documentation checkpoint and next action

This revision responds to the owner's instruction to resize work before proceeding. It changes scheduling and recovery documents only; no property, mapping, workbook or other donor was reviewed or modified here. ISA-01 and ISA-02 retain their completed status. The lessons record captures the observed workload-sizing failure without claiming to diagnose the platform error.

**Next “proceed”: ISA-03A ONLY — Maximum Status Interval, Minimum Status Interval, Name and Operating State, followed by the normal verified GitHub delivery.**
