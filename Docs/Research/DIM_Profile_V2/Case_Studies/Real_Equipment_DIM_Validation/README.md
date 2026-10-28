# Real Equipment DIM Validation — Case Study 01

**Date opened:** 27 October 2026  
**Branch:** `research/dim-profile-v2` in [OS4CSAPI/glaux-client](https://github.com/OS4CSAPI/glaux-client)  
**Status:** **I01–I08 COMPLETE — 8/13 substantive iterations complete.** **Gate A + Gate B CONDITIONAL** for documented product/design and source-grounded semantic alignment. Individual physical-unit identity, actual observations and empirical interoperability NOT VERIFIED.  
**Current next action:** **I09 — consolidate the smallest defensible candidate DIM conceptual slice, preserving every evidence limitation.**  
**Equipment selection:** **Smart Citizen Kit 2.3 selected as the documented product baseline.** Physical-unit identity, installed configuration, and actual recordings are **not yet verified**; see [I01 decision](I01_Equipment_Selection_and_Qualification_v0.1_27OCT2026.md).

## Why this folder exists

The earlier DIM/Profile V2 research produced five **evidence-backed candidate meanings** about an individual sensing System, its kind/model, implemented Procedures, composition/component standing, and digital representations. The [five-pass synthesis checkpoint](../../DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md) compared them but intentionally did **not** claim a completed DIM or demonstrate their value on actual equipment.

This case study tests whether those findings let us describe a **real sensing system** faithfully, organize a small **working Domain Information Model (DIM)** slice where supported, and assess how that meaning can be accommodated by **Open Geospatial Consortium (OGC) Application Programming Interface (API) – Connected Systems (CSAPI)**. Evidence and demonstrable semantic preservation matter more than pretty diagrams, paper volume, or invented taxonomy.

## Start here

**[13-Iteration Execution Plan — Version 0.1](PLAN_13_ITERATIONS_v0.1_27OCT2026.md)**

The plan is the authoritative **work sequence, status tracker, evidence policy, gate definitions, deliverable list, PITON schedule, and instruction for ending each iteration**. This README is the stable landing page. Its status should be updated alongside the plan after each completed iteration.

**Completed research (27–28 October 2026):** [I01 equipment selection](I01_Equipment_Selection_and_Qualification_v0.1_27OCT2026.md) established the SCK2.3 product baseline; [I02 pinned source corpus](I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md) fixed 25 initial source files in four immutable upstream repositories; [I03 60 source-native facts](I03_Source_Native_Fact_Register_v0.1_27OCT2026.md) recorded traceable statements and missing real-unit evidence; [I04 independent audit/Gate A](I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md) corrected source errors and conditionally cleared product/design evidence; [PITON A](PITON_A_Real_Equipment_DIM_Validation_v0.1_27OCT2026.md) preserves that evidence checkpoint. Then [I05 individual System/kind](I05_Individual_System_and_Product_Kind_Mapping_v0.1_27OCT2026.md), [I06 procedure/method](I06_Procedure_and_Method_Mapping_v0.1_28OCT2026.md), and [I07 composition/component standing](I07_Composition_and_Component_Standing_Mapping_v0.1_28OCT2026.md) applied the first four findings to vendor evidence. **[I08 digital representation and five-finding reconciliation](I08_Digital_Representation_and_Five_Pass_Reconciliation_v0.1_28OCT2026.md) COMPLETE:** 8 direct digital findings, a five-pass crosswalk, and **Gate B CONDITIONAL PASS for conceptual/source consistency only**—including a verified software-`Component` versus physical-component mismatch. [**PITON B — Phase B recovery**](PITON_B_Real_Equipment_DIM_Validation_v0.1_28OCT2026.md) is the current new-chat checkpoint; PITON A is historical for progress. **I09–I13 not started.**

**Continuity checkpoints:** **I04/PITON A and I08/PITON B COMPLETE**; I13/PITON C remains planned. I04's corrected source evidence and I08's documented source/digital name collisions govern later modeling; the two conditional gates prohibit false claims of a verified physical device or empirical observations. Any additional files created during I01–I13 should be linked from this page as they become real; do **not** create empty “completed” artifacts or assert future evidence now.

## Key parent research — read rather than reconstructing

The [Concept Baseline](../../DRAFT_Concept_Baseline_v0.1_25OCT2026.md) and [DIM Concept and Method Basis](../../DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md) establish the real-world and methodological scope. The [five-pass checkpoint](../../DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md) states the five actual candidate distinctions and open questions. The [canonical concept plan](../../DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md) links to the underlying individual passes; consult the actual Pass 1–5 notes as each is applied.

The [prior continuity PITON v1.4](../../PITON_DIM_Profile_V2_Continuity_v1.4_26OCT2026.md) preserves source-reading and quarantined-material safeguards, **but its progress checkpoint is historical**. Neither the earlier anatomy Phase B/C/D artifacts nor their promoted structures are authorized as the basis of this case study. Always use the current plan/README and latest verified case-study artifacts for progress.

## The “proceed” handoff

When the user says **“proceed,”** carry out the **one next iteration** identified in the plan. Read the relevant GitHub sources on this exact branch, do the work, record verified artifacts, update the tracker, and then stop.

Every iteration must finish with **what was accomplished**, **why it matters**, **the exact working GitHub document link(s)**, and **one clear next action** that the user can start with a plain **“proceed.”** Avoid requesting repeated approvals for routine execution. If material evidence is unavailable, explain the precise blocker and document the bounded recovery step rather than fabricate an answer.

**Next: Iteration I09 — Candidate DIM Conceptual Slice. Derive only the smallest warranted, implementation-independent concepts and relationships from the I05–I08 case-study findings under both conditional gates; explicitly mark the real-equipment identity and observation information we lack. Create a cited candidate slice, not a final DIM, diagram-driven class hierarchy or profile requirement. Say “proceed” to begin.**
