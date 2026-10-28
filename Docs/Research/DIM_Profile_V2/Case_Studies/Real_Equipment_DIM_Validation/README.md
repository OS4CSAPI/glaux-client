# Real Equipment DIM Validation — Case Study 01

**Date opened:** 27 October 2026  
**Branch:** `research/dim-profile-v2` in [OS4CSAPI/glaux-client](https://github.com/OS4CSAPI/glaux-client)  
**Status:** **I01–I06 COMPLETE — 6/13 substantive iterations complete.** **Gate A remains CONDITIONAL** for product/design evidence; individual physical-unit identity and actual observations NOT VERIFIED.  
**Current next action:** **I07 — apply Composition and Component Standing to documented physical assemblies and interfaces, without asserting a fielded unit.**  
**Equipment selection:** **Smart Citizen Kit 2.3 selected as the documented product baseline.** Physical-unit identity, installed configuration, and actual recordings are **not yet verified**; see [I01 decision](I01_Equipment_Selection_and_Qualification_v0.1_27OCT2026.md).

## Why this folder exists

The earlier DIM/Profile V2 research produced five **evidence-backed candidate meanings** about an individual sensing System, its kind/model, implemented Procedures, composition/component standing, and digital representations. The [five-pass synthesis checkpoint](../../DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md) compared them but intentionally did **not** claim a completed DIM or demonstrate their value on actual equipment.

This case study tests whether those findings let us describe a **real sensing system** faithfully, organize a small **working Domain Information Model (DIM)** slice where supported, and assess how that meaning can be accommodated by **Open Geospatial Consortium (OGC) Application Programming Interface (API) – Connected Systems (CSAPI)**. Evidence and demonstrable semantic preservation matter more than pretty diagrams, paper volume, or invented taxonomy.

## Start here

**[13-Iteration Execution Plan — Version 0.1](PLAN_13_ITERATIONS_v0.1_27OCT2026.md)**

The plan is the authoritative **work sequence, status tracker, evidence policy, gate definitions, deliverable list, PITON schedule, and instruction for ending each iteration**. This README is the stable landing page. Its status should be updated alongside the plan after each completed iteration.

**Completed iterations (27 October 2026):** [I01 — Equipment Selection](I01_Equipment_Selection_and_Qualification_v0.1_27OCT2026.md): SCK2.3 product/design baseline. [I02 — Frozen Source Corpus](I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md): 25 pinned files across four official repository commits. [I03 — Source-Native Fact Register](I03_Source_Native_Fact_Register_v0.1_27OCT2026.md): 60 stable F### statements and explicit gaps. [I04 — Independent Evidence Audit and Gate A](I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md): **34/60 facts directly sampled**, false part-number discrepancy retracted, 8 MB design-backed flash clarified, and **CONDITIONAL PASS** recorded. [**PITON A — Evidence Gate Recovery**](PITON_A_Real_Equipment_DIM_Validation_v0.1_27OCT2026.md) is the authoritative new-chat handoff for this case study. **[I05 — Individual System and Product/Model/Kind Mapping](I05_Individual_System_and_Product_Kind_Mapping_v0.1_27OCT2026.md) COMPLETE:** the product generation/design is demonstrably distinct from an unidentified physical individual; existing donor kind/instance roles align but no real physical-unit-to-kind link is verified. **[I06 — Procedure / Method Mapping](I06_Procedure_and_Method_Mapping_v0.1_28OCT2026.md) COMPLETE (28 October):** nine evidence-traceable method/stage findings, including firmware SHT31, SEN5X and AS7331 acquisition routines and separate advanced air-quality postprocessing; supported method detail is **not proof of a fielded unit's execution or observations**. **I07–I13 have not started.**

**Continuity checkpoints:** **I04 + PITON A COMPLETE**; I08 (five-finding reconciliation + PITON B) and I13 (final case study + PITON C) are planned. The I04 audit's corrections govern older I02/I03 statements; product design evidence does not establish serial-number identity or real field observations. Any additional files created during I01–I13 should be linked from this page as they become real; do **not** create empty “completed” artifacts or assert future evidence now.

## Key parent research — read rather than reconstructing

The [Concept Baseline](../../DRAFT_Concept_Baseline_v0.1_25OCT2026.md) and [DIM Concept and Method Basis](../../DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md) establish the real-world and methodological scope. The [five-pass checkpoint](../../DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md) states the five actual candidate distinctions and open questions. The [canonical concept plan](../../DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md) links to the underlying individual passes; consult the actual Pass 1–5 notes as each is applied.

The [prior continuity PITON v1.4](../../PITON_DIM_Profile_V2_Continuity_v1.4_26OCT2026.md) preserves source-reading and quarantined-material safeguards, **but its progress checkpoint is historical**. Neither the earlier anatomy Phase B/C/D artifacts nor their promoted structures are authorized as the basis of this case study. Always use the current plan/README and latest verified case-study artifacts for progress.

## The “proceed” handoff

When the user says **“proceed,”** carry out the **one next iteration** identified in the plan. Read the relevant GitHub sources on this exact branch, do the work, record verified artifacts, update the tracker, and then stop.

Every iteration must finish with **what was accomplished**, **why it matters**, **the exact working GitHub document link(s)**, and **one clear next action** that the user can start with a plain **“proceed.”** Avoid requesting repeated approvals for routine execution. If material evidence is unavailable, explain the precise blocker and document the bounded recovery step rather than fabricate an answer.

**Next: Iteration I07 — Composition and Component Standing. Use our fourth existing concept pass to examine the SCK2.3 Data Board, Urban Board, onboard sensors, cabled PM module, power parts, and optional attachments; preserve the difference between real physical assembly, replaceability, temporary connection and separately described components. Say “proceed” to begin.**
