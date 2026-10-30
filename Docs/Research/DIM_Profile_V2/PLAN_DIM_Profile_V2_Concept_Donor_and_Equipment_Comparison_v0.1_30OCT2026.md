# DIM / CSAPI Profile V2 — Concept, Donor and Equipment Comparison Plan

**Version:** 0.1 · 30 October 2026 (America/New_York)  
**Standing:** **IN PROGRESS — ITERATION 1 COMPLETE (1/4); ITERATIONS 2–4 NOT STARTED.** Updated 30 October 2026. The owner separately authorized Iteration 1 after plan preparation. Each subsequent “proceed” authorizes exactly the next named unfinished iteration, not the whole plan.  
**Workspace:** `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, `Docs/Research/DIM_Profile_V2/`.  
**Pre-plan repository revision:** `8c8bd730fc0222794f3fcd25e5518c9c2250e82d`.  
**Governing correction:** [AI Hallucination and Research Drift Case Study](DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md), especially §§6–8.  
**Purpose authority:** [Original Problem and Outcome Baseline](DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md), read with the owner's later correction above.

## 1. What this work should give us

Produce one readable, connected account of **what the candidate Domain Information Model (DIM) currently proposes, which donors contribute which meanings, what the synthesis does and does not establish, and which equipment information can exercise it**. Tables are the central presentation, supported by short definitions, explanations, alternatives and precise source links. They are not a replacement for model reasoning or a completed OGC API – Connected Systems (CSAPI) application Profile.

This is consolidation and verification of existing V2 research, not a predetermined next domain study. The five researched meanings are the starting record, not five immutable slots. Additional donor contributions must remain visible even when they have no current destination; earlier and later findings receive the same evidentiary treatment. Power, “operational condition,” V1 architecture, and TRSS/OmniSense do not determine the outcome or work order.

## 2. Inputs and small cumulative work product

Use the [candidate DIM v0.2](Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md), the [original alignment method](Donor_Alignment/02_Register_Method_and_Schema.md), [cross-concept reconciliation](Donor_Alignment/09_Cross_Concept_Reconciliation.md) and their linked topic records. Include the [later-donor coverage record](Donor_Challenge/01_Coverage_and_Challenge_Selection.md), [later reconciliation](Donor_Challenge/05_Challenge_Reconciliation.md) and its linked source-specific findings. Their historical “challenge” titles do not make incumbent concepts privileged in this comparison.

The [System Data Sheets index](Controlled_Corpus/System_Data_Sheets/README.md) supplies the three itemized reference cases. The [selection](Controlled_Corpus/07_Corpus_Qualification_Decision.md) and [preservation handoff](Controlled_Corpus/08_Frozen_Corpus_Manifest_and_Handoff.md) govern their evidence limits. Reuse existing source IDs and exact donor editions; do not create a parallel bibliography or reinterpret a historical review-status snapshot as current comprehensive coverage.

Create **three linked Markdown pages** under `Concept_Donor_Comparison/` during execution, not during this planning turn:

| Planned page | Reader's question |
| --- | --- |
| `README.md` — main conceptual comparison | What meanings and relationships are proposed, why, with which donor correspondences and unresolved alternatives? Includes the final verification and next-step recommendation. |
| `Donor_Contributions.md` | What does each relevant donor contribute on its own terms, how deeply was it reviewed, and what remains unrepresented or deferred? |
| `Equipment_Evidence.md` | Which exact data-sheet facts/records relate to the candidate meanings, under what qualifications, and which model, donor-review or dataset gaps block stronger claims? |

Each iteration improves these same pages. This plan is the tracker; no separate narrative report per iteration, new database, giant donor-column matrix or duplicate evidence ledger is required. The earlier closed plans, reports and frozen records remain intact.

## 3. Four working iterations — one per “proceed”

| Iteration | Work and scope | Completion condition | State |
| --- | --- | --- | --- |
| **1 — Establish coverage and show one working example** | Inventory the existing V2 records to consolidate, including original alignments, later donor findings and known unrepresented/deferred contributions. Use the existing donor-family coverage record to explain selection and review depth, without claiming a fresh audit of every artifact. Create the documentation home and a substantive representative comparison; the already researched product/model/kind distinctions are a suitable presentation trial, not a selected root or new priority. | A readable home, visible coverage/omissions, and one populated comparison with native terms, candidate meaning, directional fit, synthesis rationale, source links and uncertainties. The owner can inspect the format before it is used throughout. Other views are clearly marked unstarted. | **COMPLETE** — [worked comparison](Concept_Donor_Comparison/README.md) and [coverage inventory](Concept_Donor_Comparison/Donor_Contributions.md); one model/kind example, all 30 previously screened lineage keys visible; no equipment mappings |
| **2 — Populate the concept-and-relationship comparison** | Consolidate the five existing candidate meanings, their recorded relationships, and additional distinctions/questions already identified around them. Present early and later donor contributions together. Keep unmapped contributions and alternatives visible rather than forcing them into the five. | Main comparison and donor view cover the agreed existing record, with readable definitions, relationships, donor provenance, rejected shortcuts and open alternatives. Any potential retain/revise/split/merge/replace outcome is an evidence-linked proposal, not a silent rewrite of v0.2 or adoption. | **NOT STARTED** |
| **3 — Connect equipment evidence and distinguish gaps** | Link applicable meanings to exact rows in all three system data sheets. Separate already-supported links from proposed, untested mappings. Account for coverage at sheet-section level; do not imply that selected row examples exhaust every field or constitute a complete conversion. Keep unexamined/unmapped material locatable. | Equipment view shows source subject, native type/unit/time where supplied, evidence kind, relevant meaning, correspondence conditions and test standing. Gaps distinguish missing model meaning, insufficient donor review and missing equipment evidence. No complete operating dataset is claimed. | **NOT STARTED** |
| **4 — Verify the comparison and recommend the next substantive task** | Check the populated views against underlying records: definitions, source editions/clauses, direction, qualifications, omissions, links and claim status. Review readability and donor fairness. Compare plausible next actions from the exposed gaps by model impact, cross-source relevance, equipment-test value and evidence feasibility. | Correct material consolidation errors or explicitly hold unsupported claims; record what was checked and what was not in the main page. Explain the current model in ordinary language and give a justified, non-automatic next-task recommendation, or the specific evidence needed to choose one. Update recovery links, close this plan and stop. | **NOT STARTED** |

## 4. What must remain visible in the tables

| View | Minimum information; short linked detail can keep tables readable |
| --- | --- |
| **Candidate meaning / relationship** | Plain-language definition and role; donor-native counterparts; exact edition/clause and existing evidence record; scope/direction of correspondence; source-declared relationship versus analyst inference; synthesis rationale, qualifications and alternatives; current candidate/adoption standing. |
| **Donor contribution / coverage** | Native concept and scope; existing review depth; relevant candidate destination or “no destination yet”; reason for inclusion/deferral; distinguish not examined, no direct counterpart and rejected equivalence. Count source families/editions honestly, not artifacts as independent votes. |
| **Equipment evidence / gaps** | Data-sheet row and underlying source; subject/component, value/type/unit/time when available; design/example/derived/actual-record standing; supported or proposed correspondence; what is preserved, qualified, unresolved or unrepresented; what was tested, if anything. |

A claim is not established by a matching label or checkmark. Source cardinalities and obligations remain source-specific unless an explicit candidate rationale supports broader use. Existing correspondence statements must retain their limitations; an unexamined relationship stays unexamined. “Preserved” in a documentary comparison is not an executed transformation result. Proposed CSAPI/Profile carriers may be referenced where already researched, but new binding requirements are outside this plan.

Use full names before acronyms, short explanations beside the tables, and human-readable labels alongside existing IDs. Prefer several focused tables over a single excessively wide table. The owner should be able to understand a synthesis decision without decoding identifiers or reading the entire execution history.

## 5. Evidence and scope controls

Use existing V2 material first. Targeted read-backs may resolve an existing citation or transcription, but unresolved source questions become explicit gaps rather than an unannounced donor research campaign. Do not silently correct conflicting sources, upgrade draft/source-local claims, or invent mappings to complete cells. Original report findings and proposed corrections remain distinguishable.

The selected equipment cases currently support documentary/reference-example work, not complete joined operating histories. The richer comparable-dataset objective remains unmet; this plan makes that shortfall visible rather than lowering it. TRSS/OmniSense can explain the historical motivation, but are not compulsory experimental anchors. V1 insights need explicit inherited provenance and current V2 justification, not automatic authority.

**Not authorized by this plan:** reopen earlier plans or candidate audits; add equipment candidates or acquire new datasets; redo all 182 source artifacts; adopt/rewrite the DIM manuscript or final domain/chassis; define a new condition/power module; write normative Profile requirements; implement mappings, edit/deploy Glaux, merge branches or change application code. The tables may reveal reasons for later work; they do not authorize it.

## 6. Execution, verification and recovery

At each execution turn, read this tracker and the drift correction, complete only the next named iteration, update the cumulative pages and status, commit, read back the changed content, and check the file diff. End with what became clearer, what remains unresolved and the next named action. No extra approval loop is required inside an authorized iteration; the next owner “proceed” advances one iteration. If a material blocker prevents completion, record the partial result and exact blocker rather than mark the step complete or silently expand it.

Completion of Iteration 4 means a checked presentation of the current V2 synthesis and gaps, **not a completed DIM, equal-depth review of every potential donor, robust operational dataset, or interoperability proof**. Close the plan after the evidence-based recommendation. No fifth iteration, new domain study or implementation follows automatically.

**Iteration 1 result — 30 October 2026:** The [main comparison](Concept_Donor_Comparison/README.md) presents the existing kind/model distinction and REL-01 with source-native meanings, directional fit, rejected equivalence, source editions/clauses, synthesis rationale and unresolved alternatives. It covers eight original topic records and four later donor contributions without adopting new model structure. The [donor page](Concept_Donor_Comparison/Donor_Contributions.md) accounts for all 30 prior lineage keys: 13 with some specific comparison or later review, 17 preliminary/deferred in that sequence, with partial-family and beyond-screen limits explicit. Five previously recorded open contribution questions remain without a developed model destination. The [equipment page](Concept_Donor_Comparison/Equipment_Evidence.md) is navigation only and expressly NOT STARTED. Input snapshot: `8a4a2a082d18b0806a5df85f4b387a8f9ed14a31`; page creation commits: `4b16b63388c3c2fba1f3121cd729546d604df045`, `2904f22f3aa31edc7074cdfad3fbbe1864f73fd9`, `6413a9d1631776add1066d8b1603ff2e4450a7cc`. No original source audit, candidate manuscript or application was changed.

**Current restart contract: 1/4 complete. The next separate “proceed” authorizes Iteration 2 only — populate the broader concept-and-relationship comparison and donor-contribution view from existing V2 records.** Keep early and later contributions on the same footing, retain alternatives and unrepresented material, and leave equipment mapping to Iteration 3. Do not adopt/rewrite the DIM, begin a new domain study or change the application. Future PITONs should link this plan, the comparison pages and the drift correction; older “next proceed” instructions remain historical.
