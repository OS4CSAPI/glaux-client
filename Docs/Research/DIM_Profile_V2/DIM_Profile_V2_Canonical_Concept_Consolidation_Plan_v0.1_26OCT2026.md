# Domain Information Model (DIM) / Application Profile Version 2 (V2) — Incremental Canonical Concept Consolidation Plan

**Date:** 26 October 2026  
**Version:** 0.1  
**Method refinement (26 October 2026):** Donor-language-first terminology rule added; cited-synthesis and source-pedigree expectations clarified.  
**Status:** Active sequential plan. Pass 1 drafted for review; Passes 2–5 have not begun.  
**Location:** Research workspace, `Docs/Research/DIM_Profile_V2/`

## Purpose

The subject-and-boundary research now supports a **working hypothesis**: the DIM concerns an identifiable, equipment-realized System whose defining orientation is sensing/observing, potentially including non-sensing functions, with its enduring parts distinguished from surrounding context. This is **not** a final domain name, root class, or approved model.

The next task is to identify the **exact common concepts and relationships** needed to describe that subject, one at a time. We are not yet choosing modules or designing an application-profile binding.

**Modeling form:** Follow the [V2 Modeling Convention](DIM_Profile_V2_Modeling_Convention_v0.1_26OCT2026.md) for the eventual DIM's content and professional representation; use the existing [Modeling and Visualization Guide](DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md) for diagram mechanics. Neither guide authorizes premature class, module, schema, or binding decisions.

**Document destinations:** The [provisional DIM and application-profile outlines](DIM_Profile_V2_Provisional_Document_Outlines_v0.1_26OCT2026.md) show where future results belong. They do not approve model sections as modules or create profile requirements.

## Sequence

For reference, the main donor abbreviations used below are Open Geospatial Consortium (OGC) Application Programming Interface (API) – Connected Systems (CSAPI); Sensor, Observation, Sample, and Actuator (SOSA) / Semantic Sensor Network (SSN); Smart Applications REFerence (SAREF); Open Platform Communications Unified Architecture (OPC UA); and Sensor Model Language (SensorML). **The Open Group Sensor Open Systems Architecture is a different SOSA.**

Work through these five passes **in order**, completing and explaining each before taking up the next.

| Pass | Concept to investigate | Question to settle | Principal evidence to compare |
| --- | --- | --- | --- |
| **1** | **Individual System identity** | What is the enduring individual subject, as distinct from its identifiers, kinds, observations, and representations? | CSAPI; SOSA/SSN; SAREF; OPC UA Devices; Asset Administration Shell (AAS); Open Group SOSA |
| **2** | **Product / model / kind** | What reusable description identifies what kind of equipment this individual is? How does it differ from the individual itself? | CSAPI `systemKind`; SAREF `DeviceKind`; AAS type/instance; Web of Things (WoT) Thing Model; Matter (within its evidence limits) |
| **3** | **Procedure / method** | What describes how the System performs a function, rather than what product/model it is? | CSAPI `procedures` **versus** `systemKind`; SOSA/SSN Procedure; SensorML ProcessMethod; Observations, Measurements and Samples (OMS) |
| **4** | **Composition and component standing** | What is an enduring part of the System? When is an element independently meaningful? What is merely hosted, attached, networked, or deployed with it? | CSAPI Composition/Aggregation; SOSA/SSN; SensorML; OPC UA Devices; BME280; unattended ground sensor (UGS) examples |
| **5** | **Digital representation / proxy identity** | How does a digital description, API resource, adapter, proxy, or twin represent the subject without becoming the subject? | AAS; WoT; CSAPI; OPC UA Devices; Open Standard for Unattended Sensors (OSUS) |

**Pass 3 must explicitly preserve the C08 audit correction:** a `systemKind` link to a kind/model/datasheet description is not the same relationship as links to procedures that the System implements.

## Method for each pass

Each pass produces **one human-readable concept note**, organized around:

1. **Cited candidate meaning first:** state the synthesized meaning clearly, using Chicago Manual of Style, 18th edition, author-date citations where the contributing source evidence enters the statement.
2. **Immediate narrative pedigree:** explain each substantive building block, what it means *in each relevant donor's own model*, why it contributes to our candidate meaning, and where a mapping is partial or only a resemblance. Cite sources reasonably throughout, with source locations where possible.
3. **Differences and limits:** distinguish donor-native facts, dependent sources, independent corroboration, and V2 interpretation; do not claim that similar donor classes are equivalent.
4. **Material unresolved points:** record only questions that could actually change the meaning or its use.

**Donor-language-first rule:** Use established donor terminology where it adequately expresses the meaning. For cross-donor conclusions, describe the relationships in ordinary language rather than coin new technical labels. Introduce any V2-owned term only when a material semantic need cannot be expressed accurately using existing terms; identify the gap, explain why the donor terms are insufficient, cite that evidence, and explicitly label the proposed term as V2-authored. **A synthesized meaning is permitted; invented terminology is not its default expression.**

Target **roughly one to two readable pages per pass**, not a new research volume or exhaustive standards-conformance audit. Do source checking only where a consequential claim needs it. Preserve donor-owned semantics; label our interpretations as our own. If evidence cannot settle a point, record it as open rather than inventing closure.

A candidate concept does **not** become a V2 standard, requirement, adopted class, or conformance claim by appearing in a note. Keep conceptual reuse, semantic mapping, profile specialization, actual donor-standard implementation, and OGC binding distinct.

## Human checkpoint after Pass 5

Bring the five findings together in **one brief synthesis**, showing:

- the individual subject and its relationships to kind/model, implemented procedure, enduring components, and digital representation;
- what meanings are supported, partial, or unresolved;
- whether these findings still fit the working subject-and-boundary hypothesis.

A **small conceptual diagram** may help here; no large model, modules, schemas, encoding designs, or conformance rules are authorized by this plan. Only after this checkpoint should we decide how to investigate capability, configuration, state, interactions, outputs/actions, history, and provenance.

## Standing guardrails

- **Do not invent an umbrella domain name** or force a single root class. The final bounded scope remains an evidence-led research question.
- **Do not inherit Version 1's eight subjects as the V2 module structure.**
- **Do not make 30 equal donor “votes.”** Use each source for the concepts it actually owns; respect known access limits and source dependencies.
- **Do not silently promote** any findings from the quarantined earlier anatomy Phase B/C/D artifacts.
- **Do not restart Phase A** or reopen the entire donor survey for routine questions.
- **Do not force full-standard compatibility.** Test faithful accommodation of *relevant adopted/mapped donor semantics for in-scope systems*, not every concept or obligation in each donor standard.
- **Do not hide uncertainty behind neat diagrams or terminology.** The human explanation is the primary deliverable.

## Recovery and starting point

Before resuming in a new chat, read the controlling [PITON v1.3](PITON_DIM_Profile_V2_Continuity_v1.3_26OCT2026.md) and its two mandatory baseline refreshers: [Concept Baseline](DRAFT_Concept_Baseline_v0.1_25OCT2026.md) and [DIM Concept and Method Basis](DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md). Then consult the [refined subject-and-boundary pedigree](DIM_Profile_V2_Refined_Subject_Boundary_Pedigree_v0.1_26OCT2026.md), the [Pass 2 stress test](DIM_Profile_V2_Subject_and_Boundary_Pass2_Stress_Test_v0.1_26OCT2026.md), and [C08 validation audit](DIM_Profile_V2_Anatomy_PhaseA_Validation_Audit_v0.1_26OCT2026.md) where relevant.

**Current checkpoint:** Review the [Pass 1 — Individual System Identity](DIM_Profile_V2_Canonical_Concept_Pass1_Individual_System_Identity_v0.1_26OCT2026.md) candidate. **Next new research pass when authorized: Pass 2 — Product / Model / Kind only.**
