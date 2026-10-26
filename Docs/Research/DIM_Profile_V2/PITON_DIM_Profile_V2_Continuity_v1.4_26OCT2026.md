# PITON — DIM/Profile V2 Research Continuity: Post-Audit Discovery and Concept Consolidation

**Version:** 1.4  
**Date:** 26 October 2026  
**Standing:** Current authoritative **research recovery and sequencing handoff**; not a DIM specification, adopted model architecture, or profile requirements.  
**Repository:** [`OS4CSAPI/glaux-client`](https://github.com/OS4CSAPI/glaux-client)  
**Branch:** `research/dim-profile-v2` — **do not default to `main`**  
**Workspace:** `Docs/Research/DIM_Profile_V2/`  
**Supersedes:** The **restart/status instructions** in [PITON v1.3](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/PITON_DIM_Profile_V2_Continuity_v1.3_26OCT2026.md), while preserving its foundational semantics, quarantine, and evidence-integrity safeguards.

> **RESTART INSTRUCTION — READ, DO NOT JUST SUMMARIZE FROM MEMORY:** On entering a new chat, first open this PITON and **read the linked repository documents in §2 in the prescribed order**, using the actual `research/dim-profile-v2` branch. The two original concept baselines remain mandatory. The Pass 1 concept note and current consolidation plan govern the next work. The old v1.3 statement that work must stop before post-audit synthesis is **outdated**, because the project owner has since authorized and completed specific corrective triage and subject/boundary discovery. The **old, quarantined Phase B/C/D anatomy outputs are still not authorized as factual/model authority**. **Do not start a new pass merely because you have read this PITON; follow the user's new instruction.**

## 1. Executive recovery: where we actually are

The project is developing **Version 2 of a Domain Information Model (DIM) and an eventual OGC API – Connected Systems (CSAPI) application profile** for the information needed to understand and interoperate with real sensing systems as complete operational subjects. V2 is **not named for MERLIN** as its formal identity; MERLIN and MPSS are predecessor/implementation evidence.

**What is established enough to guide research:** the relevant native CSAPI framing distinguishes a **`System` subject**, a **`systemType = Sensor`** characterization of its primary sensing/observing role, and a separate **`assetType = Equipment`** characterization of its hardware realization. These are **not three peer classes, nor one invented compound class**. The precise final DIM domain name, root-class architecture, full concept set and profile contents **are not frozen**.

**Current evidence-backed working hypothesis, not an adopted class or final scope:**

> **The DIM appears to be converging on an individually identifiable, persistently describable, equipment-realized System whose defining operational orientation is sensing/observing, but which may contain or perform non-sensing functions. The subject may be atomic or composite; its enduring composition can be distinguished from hosting, deployment, network, management, target, and digital-representation context; and its kind/model, capabilities, configuration, state, interactions, outputs/actions, history, and provenance can be represented without conflating those concerns with the subject itself.**

That statement is a **project synthesis with a sourced pedigree**, not verbatim normative language from a donor. Its equipment/sensing focus is a **current working boundary** and is open to material counterevidence. SAPIENT, IEEE 1451, WoT, OPC UA and other broad donors can support the DIM without forcing all their devices, pure effectors, virtual Things or networks into its top-level scope.

**Current work stage:** **Canonical Concept Consolidation** has begun **sequentially**. **Pass 1: Individual System Identity** is researched and documented **as a candidate for human review**, with a small **illustrative UML instance-view pilot**. **Passes 2–5 have NOT begun.** The pilot did not create an authoritative class diagram or demonstrate meaningful interoperability; it verified a narrow notation/instance distinction. The owner explicitly found the pilot visually underwhelming. **Do not oversell it or treat the pilot as the main accomplishment.**

**Exact next substantive research task, when the owner asks to continue:** **Pass 2 — Product / Model / Kind only**. Do not batch Passes 2–5, design a full anatomy, build JSON schemas, or begin formal profile conformance writing.

## 2. Required repository reading — explicit new-chat recovery sequence

**Follow the links and inspect their actual content before proposing, editing, or conducting further DIM research.** All links resolve to the working branch. Do not mistake old restarts or high-confidence-looking documents for current authority.

### A. Foundational semantic and methodological grounding — mandatory

1. **[Concept Baseline (25 October)](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DRAFT_Concept_Baseline_v0.1_25OCT2026.md)** — original native CSAPI and SOSA/SSN `System` / `Sensor` / `Equipment` reasoning, whole-system scope, Composition/Aggregation. **Must read in full.**
2. **[DIM Concept and Method Basis](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md)** — implementation-independent DIM, profile versus binding, domain boundary versus root class, reuse/modularity discipline. **Must read in full.**
3. **[C08 CSAPI validation audit](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Anatomy_PhaseA_Validation_Audit_v0.1_26OCT2026.md)** — three indispensable corrections (see §4). **Must read.**
4. **[30-lineage trust triage](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Anatomy_PhaseA_Bulk_Trust_Triage_v0.1_26OCT2026.md)** — GREEN/YELLOW evidence ceilings and synthesis controls. **Must read.**

### B. The tested working subject/boundary — mandatory

5. **[Post-audit discovery Pass 1](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Post_Audit_Discovery_Pass1_Subject_and_Boundary_v0.1_26OCT2026.md)** — why the subject centers on an identifiable individual rather than a feed or API representation. **Read its findings.**
6. **[Subject-and-Boundary Pass 2 stress test](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Subject_and_Boundary_Pass2_Stress_Test_v0.1_26OCT2026.md)** — mixed-function Sensors; Equipment scope; host and digital-representation distinctions; SAPIENT counterexamples; donor-accommodation test. **Read in full.**
7. **[Refined subject-and-boundary pedigree paper](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Refined_Subject_Boundary_Pedigree_v0.1_26OCT2026.md)** — **21 semantic bricks plus non-conflation synthesis**, donor-native definitions, limits, Chicago author-date evidence, and counterexamples. **Read its abstract, cited synthesis, brick map, synthesis rule, conclusion, and the brick sections pertinent to the next task.** Consult additional bricks when material; do not pretend to have checked any unread brick.

### C. What we are doing next and the methodological rules — mandatory

8. **[Incremental canonical concept plan](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md)** — **controlling five-pass order**, one-concept-per-pass delivery, first-use sourced synthesis with immediate donor pedagogy, **donor-language-first rule**, and checkpoint. **Must read in full.**
9. **[Pass 1: Individual System Identity](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Canonical_Concept_Pass1_Individual_System_Identity_v0.1_26OCT2026.md)** — current first completed research note. **Must read the cited candidate meaning and all nine source-pedigree subsections**, including the revision away from the invented phrase “remains the referent.” **Do not convert it into a new `IndividualSystem` class.**
10. **[DIM Modeling Convention](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Modeling_Convention_v0.1_26OCT2026.md)** — documented OMG/OGC/ISO-informed model form, semantic/notation boundaries, class/instance distinction, no premature cardinalities/modules. **Must read.**
11. **[Modeling and Visualization Guide](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md)** — actual UML and diagram mechanics, status annotations, source preservation, anti-patterns and **one figure = one canonical source**. **Read relevant sections when modeling/diagramming; do not bypass for figures.**
12. **[Provisional DIM/Profile outlines](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Provisional_Document_Outlines_v0.1_26OCT2026.md)** — distinct destinations for the DIM and future normative profile; OGC ModSpec 1.1 profile structure; **outlines are not model content or conformance requirements**. **Must read for publication/profile questions.**
13. **[Pass 1 modeling pilot](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Pass1_Modeling_Pilot_v0.1_26OCT2026.md)** — exact narrow visual test, outcome and limits. **Read before referencing its result or deciding that a formal class model already exists.**

### D. Supporting records — consult specifically when the next claim needs them

- [Prior recovery PITON v1.3](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/PITON_DIM_Profile_V2_Continuity_v1.3_26OCT2026.md) — **historical basis** for the two mandatory baseline reads, post-glitch recovery and quarantine. **Do not execute its older §14–15 safe-state/restart instructions.**
- [CSAPI anchor standards environment](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DRAFT_CSAPI_Anchor_Standards_Environment_v0.1_25OCT2026.md) — useful when claiming CSAPI / SOSA/SSN / SensorML / OGC normative relationships.
- [Original subject/boundary pedigree v0.2](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Emerging_Subject_Boundary_Pedigree_v0.2_26OCT2026.md) — predecessor to the **refined** pedigree; use for historical derivation or source detail.
- [Phase A 30-lineage source extractions](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DRAFT_DIM_Profile_V2_Anatomy_PhaseA_Independent_Extractions_v0.1_26OCT2026.md) — **candidate donor evidence**, not an adopted V2 model. For Pass 2 read the **applicable** donor sections, not the entire extraction indiscriminately.
- [182-source candidate ledger](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Anatomy_Phase0_182_Source_Ledger_v0.1_26OCT2026.csv) and [source-type donor bibliography](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Candidate_Donor_Bibliography_Source_Type_Grouped_v0.5_25OCT2026.md) — source provenance and coverage when a claim or donor is unclear.
- [Pass 1 diagram editable DOT source](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Visualization/source/Pass1_Individual_System_Instances.dot) and [Pass 1 illustrative SVG](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Figures/Pass1_Individual_System_Instances.svg) — **only if inspecting or changing that pilot**; it is an example, not an authoritative DIM class model.
- [Earlier combined V2 working draft](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Sensor_Systems_DIM_and_Profile_V2_Working_Draft_v0.1_25OCT2026.md) — **historical/noncontrolling**; contains over-promoted chassis and anatomy conclusions. Use only with the quarantine warning below.

**Access rule:** These are live repository sources. Read them through the GitHub connection at the exact branch; do not rely on summaries or the filename alone. If a critical linked file is unavailable, state the precise gap rather than guessing its contents.

## 3. Chronology, trust, and why the recovery changed

1. The original project had an independently derived CSAPI/SOSA/SSN **System/Sensor/Equipment** baseline; Version 1 whole-system categories were predecessor requirements evidence, **not** V2 module definitions.
2. A 182-artifact candidate donor population was frozen for this research increment; **30 semantic lineages** were extracted using a common 15-field Phase A worksheet. **30/30 mechanically complete does not mean 30/30 independently verified.**
3. Earlier AI continuation over-promoted the extraction into Phase B/C/D anatomy/model decisions. The owner stopped that work; **those Phase B/C/D artifacts remain quarantined**. PITON v1.3 restored the semantic baseline.
4. Subsequently, an owner-authorized **C08 calibration audit** corrected material CSAPI distinctions. A **bulk trust triage** then found **22 GREEN, 8 YELLOW, 0 RED**, providing evidence ceilings and reopening bounded discovery. GREEN does not mean that every line was independently rechecked.
5. An explicitly separate, owner-authorized **post-audit Subject-and-Boundary Pass 1** and **Pass 2 stress test** examined outside-in donor boundaries and the inside-out **donor-accommodation envelope**. They generated the **refined hypothesis**, followed by a detailed donor-pedigree paper. **This work does not retroactively validate or authorize the old Phase B/C/D outputs.**
6. The owner approved an **incremental five-pass concept-consolidation plan** and standards-informed modeling/documentation conventions, plus **provisional** separate DIM and CSAPI profile document outlines.
7. **Pass 1 (Individual System Identity)** produced a donor-grounded, Chicago 18 author-date cited **candidate meaning and nine-part narrative provenance**. The owner challenged coined terminology; the note was revised to use donor-native `individual System` / `System instance` wording. The terminology rule was added to the plan.
8. One **tiny UML object/instance pilot** illustrated `exampleA : System` and `exampleB : System` without new relationships or attributes. The owner did not find the result impressive. That is understandable: the pilot is **not a design breakthrough**, just a small check that UML class/instance notation does not introduce unsupported structure. This is the **present stopping point**.

## 4. Safeguards: donor semantics must not turn into invented V2 meaning

**Critical CSAPI C08 audit corrections (do not regress):**

- CSAPI `systemKind` points to **one Procedure resource describing the kind/model of System** (e.g., datasheet), while `procedures` points to **Procedures the System can implement**. **Product kind ≠ implemented method**, even though one CSAPI resource type can carry both kinds of description.
- **Sampling Feature** is a CSAPI resource type; **Feature of Interest** is not simply its peer CSAPI resource type. Preserve the distinction between the Sampling Feature and linked ultimate feature(s) of interest.
- Details of a deployed System's **configuration** may be expressible in a **SensorML representation of Deployment**; they are **not thereby native properties of base CSAPI Deployment**.

**Other required precision:**

- CSAPI requires a System `uniqueIdentifier` but describes its persistence/independence from the resource URL with **SHOULD**, not an unconditional lifetime persistence **SHALL**. Identifiers refer to a System; they do not constitute the equipment.
- A CSAPI `systemType = Sensor` tag is **not automatically equivalent to an RDF/OWL type assertion** of `sosa:Sensor`; classification carries semantic meaning without automatically implying extra API capabilities.
- **SOSA is ambiguous**: W3C/OGC **Sensor, Observation, Sample, and Actuator** versus The Open Group **Sensor Open Systems Architecture**. Never conflate the two.
- The **21 October 2026 SOSA/SSN “2023 Edition” Working Draft** is current research evidence but is **not** the earlier normative ontology edition referenced by published CSAPI v1.0. Make edition/dependency distinctions explicit.
- CSAPI **Composition** (integral/enduring components) and **Aggregation** (non-permanent, Deployment-scoped attachment) differ, and **neither label automatically authorizes UML diamond semantics**.
- Hosting, Deployment, network participation, management, sensed targets, and digital proxies/representations are not automatically intrinsic composition. A host-like item can be integral in one model and contextual in another; decide by the **meaning of its relationship**, not its English name.
- A sensing-oriented whole may contain actuation, computation, power, communications and management functions. **Pure non-sensing effectors** are **not automatically in the present target boundary**, even when a donor covers them.
- The goal of donor compatibility is **faithful accommodation of *relevant adopted/mapped donor semantics* for in-scope CSAPI-integrated Systems**. It is **not** a promise that V2 implements every donor standard or that native donor conformance automatically implies V2 conformance.
- Distinguish **donor-standard implementation and exact conformance**, **semantic mapping/translation**, **a V2/OGC profile or binding**, and **borrowing design ideas**. Never call reuse of an idea implementation of that standard.
- The old Phase A **YELLOW** ceiling applies to C03 IEEE 1451/ISO 2145x, C05 ISO/IEC 29182, C06 Matter 1.3, C07 MIMOSA, X05 MIP/JC3IEDM, X06 NIEM, S02 radiation, S04 UGS operations. Check a specific unverified proposition rather than reopen everything.

## 5. What has and has not been decided

| Area | Current standing |
| --- | --- |
| Name/method “Domain Information Model” | Retained as the established **working methodological term** |
| DIM method | Purpose-driven, implementation- and binding-independent; source-aware; **model for the profile, not to the profile** |
| Bounded real-world focus | **Working hypothesis:** identifiable sensing-oriented equipment Systems that may be atomic/composite and have rich but distinguishable contexts |
| Final domain name and model root class | **Open**; no invented `SensorEquipmentSystem` or `IndividualSystem` class |
| 182 sources / 30 lineage extractions | Research infrastructure; donor evidence **subject to triage/source limits** |
| Old anatomy Phase B/C/D and promoted decisions | **Quarantined**, **not** current model authority |
| Subject-and-boundary Pass 1, Pass 2, pedigree | **Documented research evidence**, not formal DIM adoption |
| Canonical Concept Pass 1: identity | **Researched, cited candidate**, open on replacement identity/reconciliation/component granularity |
| UML instance pilot | **Illustrative notation check only**; no conformance, formal UML metamodel, new class, or substantive interoperability proof |
| Passes 2–5 | **Not started** |
| DIM conventions | Working standards-informed modeling/visualization method documented; UML class diagrams favored **when they add value** |
| DIM and profile provisional outlines | **Document destinations**, not frozen concepts, module structure, or normative profile content |
| Actual DIM UML class model, logical schema, finalized modules | **Not created/adopted** |
| V2 CSAPI normative profile, requirements/conformance classes, test suite | **Not created/adopted**; predecessor MERLIN MPSS v0.3.5 remains separate historical baseline |

## 6. How to carry out the next incremental concept pass

**Next pass:** **Product / Model / Kind**. Work on this **one** problem rather than a combined identity/kind/procedure/composition/representation package.

**The conceptual problem:** Compare what donors mean by a **particular System instance** versus a **reusable kind, product model, device type, datasheet, or type-level description**. The known question is whether one or more existing source concepts can express the distinction and any mapping needed for V2, **without a new V2-authored concept**.

**Core donors and cautions to examine:**

- **CSAPI `systemKind`**, and its linked Procedure resource **as kind/model description**, compared carefully with separately implemented `procedures` (read C08 audit).
- **SAREF** `DeviceKind` versus `Device`.
- **AAS** Type versus Instance Asset, `AssetInformation`, and referenced type descriptions.
- **W3C Web of Things** `Thing Model` versus instance `Thing Description`.
- **OPC UA** `DeviceType`/product Model/part or instance identification where relevant.
- **Matter Device Type** (corroboration only **within its YELLOW evidence ceiling**); SensorML and SOSA/SSN § 8.16 for native comparison as needed.

**Required product, in one bounded concept note:** Begin with **one clear, Chicago Manual of Style 18 author-date cited candidate meaning** (citations next to the propositions they support). **Immediately follow with readable narrative** explaining *each building block*, its meaning to each donor, how it contributes to V2, material differences/partial mappings, and exactly what remains V2 inference. End with only open questions capable of changing the meaning. One or two readable pages is the aspiration; don't force an underdeveloped or overly bloated paper to meet a page count.

**Donor-language-first rule:** Use established donor terms if suitable. A synthesized *relationship* is not a license to coin an impressive-sounding V2 class or name. New V2-owned semantics require an evidenced gap, documented necessity, citation, and explicit labeling as proposed.

**Stop after Pass 2.** Do not automatically perform Pass 3, create DIM modules/class models, write profile `SHALL` requirements, or begin another broad review. Return a clear finding and a direct GitHub document link.

## 7. Five-pass path beyond the immediate step

1. **Individual System Identity** — completed **as research candidate**, not formally adopted.
2. **Product / Model / Kind** — **next**.
3. **Procedure / Method** — distinguish what the System implements from what kind of System it is.
4. **Composition and component standing** — intrinsic/enduring part, deployment aggregation, host/context, independent component identity.
5. **Digital representation / proxy** — real equipment versus AAS Shell, WoT Thing Description, OPC UA node/service, CSAPI resource, OSUS proxy.

After all five, hold **one short human checkpoint**, then decide whether the evidence now supports a small **UML class view** and whether subsequent capability, configuration, state, interactions, outputs/actions, history, and provenance investigation is warranted. The figure should represent justified semantics; it must **not** invent them.

## 8. Standards-informed document and diagram conventions already in force

- The DIM **defines concepts/relationships and justified domain-level constraints**; the eventual CSAPI application profile **selects and constrains DIM meanings**; an OGC binding **describes their representations and API obligations**. Implementation and UI behavior are later concerns.
- Prefer **OMG UML 2.5.1** class diagrams for *established structural meaning*, explanatory instance views for examples, and prose/tables where diagrams do not add explanatory value.
- **ISO 19103:2024** and **ISO 19109:2025** can inform **geographic conceptual/application-schema portions**; they are not automatically requirements for the entire DIM. The **OGC Testbed-17 UML Best Practice Engineering Report** is **informative**, not a normative standard.
- The intended normative profile should be structured with regard to **OGC ModSpec 1.1** requirements/conformance-class/testing discipline, but **no ModSpec conformity claim** has been earned; ModSpec Part 2 UML is optional. The profile's conformance target(s) and selected exact CSAPI classes remain **open**.
- Maintain exact-source **source files for diagrams** (e.g., DOT/PlantUML) with matching renders. Do not treat a generated image as a formal machine-readable UML metamodel. No diagram should conceal “candidate” status or silently add associations, multiplicities, classes, or modules.
- Preserve **Chicago 18 author-date** citations and reference entries where factual claims are made, including the synthesized candidate and the immediate donor-native meaning narrative. Expand acronyms on first use. The source of each borrowed or mapped meaning matters.

## 9. New-chat response discipline — protect the work without grinding it to a halt

Once the mandatory documents are actually read, begin the next response with a **concise recovered-state summary** (what is established, what is only candidate, what is quarantined, and the exact next pass). Do not demand that the user restate the project, replay already answered decisions, or approve a series of tiny steps. Follow the owner's current request.

The owner wants **high research value**, not voluminous “AI slop.” A tiny diagram with two underlined object names was acknowledged as technically valid but **not an impressive deliverable**; do not pretend it validates the future DIM. Prefer meaningful source-grounded explanations of donor semantics and evidence over repeated self-congratulatory paperwork or decorative diagrams. When a figure is valuable, ensure it shows the *actual* substantive relationship and has a retained editable source.

**No project work has been carried out beyond the Pass 1 pilot at the time of this PITON.** This handoff is the place to pick up the next chat without repeating earlier recovery failures.
