# PITON — DIM/Profile V2 Research Continuity

**Version:** 0.4  
**Date:** 25 October 2026  
**Standing:** Continuity checkpoint immediately before first chassis-finding donor analysis  
**Repository:** `OS4CSAPI/glaux-client`  
**Branch:** `research/dim-profile-v2`  
**Workspace:** `Docs/Research/DIM_Profile_V2/`

> **IMMEDIATE RESTART INSTRUCTION:** Resume with the **Conceptual / Information / Domain Model chassis study** described in Sections 13–16 of this PITON. Do **not** reopen the DIM-method question, do **not** rebuild V1’s eight information subjects, do **not** expand the frozen 182-source corpus, do **not** rank donors before independent extraction, and do **not** resume figure-work unless the project owner explicitly asks for it.

## 1. Purpose of this PITON

This PITON supersedes v0.3 as the active continuity checkpoint for DIM/Profile V2. It captures the major methodological corrections, corpus organization, clean-artifact work, predecessor-goal recovery, standardization-stack analysis, and chassis-finding direction established after v0.3. Its purpose is to let a new chat continue the research without reconstructing the reasoning or accidentally reintroducing Version 1 structure as a hidden assumption.

The current phase is no longer about deciding whether a Domain Information Model is legitimate, nor about designing diagrams, nor about categorizing donors by Version 1 subject areas. The immediate research problem is now narrower and more consequential: **identify the strongest existing conceptual basis for the class of real-world thing the V2 DIM is actually about**. The project owner has called this the DIM’s **“chassis.”** “Chassis” is research shorthand only; it is not a proposed class, namespace term, or formal model element.

## 2. Governing V2 mission and discipline

V2 is a clean-slate re-examination of the sensing-system Domain Information Model and eventual CSAPI application profile. Version 1 remains predecessor evidence, not design authority. Its research, goals, examples, failures, and useful principles may be recovered deliberately, but its names, eight information subjects, R01–R20 relationships, donor choices, profile-owned terms, and structural partitions are not inherited automatically.

The project’s governing semantic rule remains: **use established source concepts as primitives and do not invent a new name merely because a combination makes sense**. Multiple sourced concepts may be used together descriptively without creating a new class. New V2-owned semantics require demonstrated need after the source evidence has been examined.

The research remains evidence-first. Donor investigation is not adoption. Conceptual reuse, standards-based translation, profile specialization, concrete OGC binding, native donor implementation, and conformance claims must remain distinct. Individual donor reviews do **not** edit the DIM directly. Evidence is extracted first and synthesized only at an explicit synthesis gate.

## 3. Settled conceptual baseline from the early V2 work

The early V2 concept baseline remains the comparison point, not the final answer. “Whole system” means **informational completeness about the sensor system**: the user should be able to understand the system as a complete operational subject rather than merely retrieve its observations. That may include identity, configuration, components, capability, deployment, communications, power, condition, management, history, provenance, observations, products, and actions, but this list does not establish future V2 modules.

“Whole system” does **not** mean system-of-systems, enterprise system, or aggregate simply because more than observations are represented. SensorML 3.0 supports the idea that a system whose overall application is sensing may include sensing, actuation, and computational subprocesses while remaining a sensor system at the top level.

The strongest current CSAPI characterization of the hardware systems that motivated the work remains:

- `systemType = Sensor`
- `assetType = Equipment`

This is a **candidate characterization**, not a final domain boundary and not a new class. SOSA/SSN provides the Asset/System/Sensor/Actuator/Sampler/Platform conceptual foundation; CSAPI supplies the system-role and asset-realization facets; SensorML provides detailed process/system representation. Version 2 remains open to discovering an established boundary-defining concept that describes the intended family more naturally than the current `System + Sensor + Equipment` combination.

CSAPI’s distinction between enduring subsystem **Composition** and deployment-scoped **Aggregation** also remains an important sourced distinction. Physical attachment alone is not decisive. An enduring integral subsystem and a field-reconfigurable or interchangeable attachment have different semantics. Do not automatically translate CSAPI’s use of the words Composition/Aggregation into strict UML diamond semantics.

## 4. Workstream 1 closed — what a DIM is and how it relates to the profile

The term **Domain Information Model (DIM)** survived the clean-slate test. It is an established standards term and sits within the broader industry practice of implementation-independent information modeling. The working V2 definition is:

> **A Domain Information Model is an implementation- and protocol-independent model of the common concepts, entities, relationships, and intrinsic semantic constraints needed to describe and understand a defined problem domain.**

The project-specific purpose is to model the information needed to understand a deployed sensing system as a complete operational subject independently of the API, encoding, schema, implementation, or user interface used to represent it.

The key architectural principle is **purpose-driven but binding-independent**, summarized as **model for the profile, not to the profile**. The intended CSAPI application profile is allowed to identify which interoperability questions the DIM must answer. It is not allowed to turn CSAPI resource paths, JSON member placement, encoding choices, UI needs, or implementation convenience into intrinsic domain truth.

The current artifact relationship is:

1. **DIM** — establishes domain meaning.
2. **Application Profile** — selects and constrains DIM content and states additional interoperability obligations for a purpose.
3. **OGC Binding** — specifies how those meanings/obligations are represented using CSAPI, SensorML, SWE Common, and related mechanisms.
4. **Implementation** — realizes the binding in servers, adapters, clients, validators, storage, and UIs.

The profile supplies requirements to the DIM; the DIM supplies semantics to the profile.

## 5. Modularity and reuse decisions

V2 may be modular, but modularity must be earned from semantic cohesion rather than inherited from V1 headings. A candidate subject area should become a reusable module or subdomain only if the source evidence shows coherent internal concepts and relationships, bounded dependencies, meaningful independent applicability, and sufficient source lineage.

The governing reuse rule is **reuse invariants; specialize variation**. Common concepts should be shared only when their meaning genuinely survives across relevant system families. Realization-specific concepts should remain specific rather than being weakened into vague abstractions merely to maximize future reuse.

A possible future Human Sensor profile is a useful architecture test, not a present requirement that should distort the Equipment-oriented problem. Reuse should follow semantic truth, not hypothetical future convenience.

## 6. Version 1 structure is explicitly not the V2 classification scheme

Version 1 organized its DIM around eight information subjects. Those subjects remain predecessor evidence only. They are **not** the bins for V2 donor analysis and are not assumed to be the eventual V2 structure:

1. identity / model / technical description;
2. equipment / composition / physical arrangement;
3. sensing capabilities / performance / outputs;
4. deployment / emplacement / location / responsibility;
5. operating configuration / modes / supported actions;
6. communications / connectivity / access;
7. power sources / operating arrangement;
8. condition / service / recovery / lifecycle.

The project owner explicitly corrected an attempted return to these categories during Workstream 3. The V2 structure must emerge from the source evidence. Do not ask donors how they fit the eight V1 subjects. Ask first what the donor itself standardizes and how it conceptualizes its own domain.

## 7. V2 objectives and design principles added to the clean working artifact

The clean V2 artifact now contains an early **Objectives and Design Principles** section. These are outcome-oriented goals, not inherited structure.

**Overarching objective:** develop a standards-grounded DIM and CSAPI application profile that enable heterogeneous sensing systems to be represented, integrated, discovered, understood, and used through a common OGC framework while preserving the meaning, provenance, and distinctions of their source information.

The nine supporting goals are:

1. **Model the system as a complete operational subject.**
2. **Preserve donor semantics through integration.**
3. **Enable cross-source interoperability and common interpretation.**
4. **Reuse established semantics before authoring new ones.**
5. **Preserve provenance and semantic fidelity.**
6. **Keep the DIM purpose-driven but binding-independent.**
7. **Support progressive compatibility.**
8. **Make conformance claims precise and testable.**
9. **Remain reusable, extensible, and grounded in real systems.**

Two synthesis rules apply across all nine:

- **Every donor is allowed to challenge the emerging V2 model.** Donor review must not merely validate choices already made.
- **V2 should own only semantics and constraints that no suitable adopted source already owns.** Local authorship must remain visible and justified.

A recurring acceptance question for donor-derived content is:

> **If a conforming implementation of the donor standard arrived with the corresponding native information, could V2 map that information faithfully and recognizably?**

A negative answer requires an explicit explanation: donor misunderstanding, intentional abstraction, binding loss, incomplete mapping, or another documented reason.

## 8. V1 integration goal recovered and deliberately retained as a V2 principle

The predecessor work contained a strong integration acceptance lens called **U-INT-01**. Its substance was that a source-specific adapter should be able to map available authenticated native information from a system using a documented donor standard into the common CSAPI/SensorML/SWE representation so a common client can interpret the corresponding meaning. Important distinctions and source provenance should be preserved; unavailable or unrepresentable information should be identified; native records should remain linkable when translation is insufficient.

V1 explicitly did **not** claim lossless conversion of every donor element, implementation of every donor protocol, or automatic full-profile conformance. Mapping outcomes included direct/equivalent, partial, native-linked, unavailable, and not appropriate. This principle is retained in V2 because it judges the honesty of reuse without prescribing the DIM’s structure.

V1 also supplied several generally applicable principles that have been carried forward into the V2 objectives:

- semantic fidelity over superficial normalization;
- explicit source provenance;
- donor comparison in both directions;
- native standards mechanisms before local invention;
- progressive compatibility for generic, standards-aware, and profile-aware clients;
- precise conformance boundaries;
- common-client interpretation across heterogeneous sources; and
- usefulness to real operators without sacrificing technical fidelity.

V1’s **solutions** are not thereby retained. Only these architecture-neutral goals and quality tests are carried forward.

## 9. Frozen source corpus and bibliography state

The current V2 source population is **frozen at 182 external candidate sources** for the present research stage. Do not add sources merely because CSAPI mentions another dependency or because a related standard appears useful. The project owner explicitly rejected dilution of the corpus through automatic dependency expansion.

The source population developed as follows:

- initial incomplete V2 bibliography v0.1: 46 sources — rejected;
- corrected neutral bibliography v0.2: 153 sources, including all eleven ISA 6.0 documents;
- NIEM expansion: +29 sources;
- neutral bibliography v0.3: **182 sources**;
- provenance/community-grouped bibliography v0.4: retained as a potentially useful alternate organization, but **not** the controlling organization for the present analysis;
- source-type grouped bibliography v0.5: current neutral organizational bibliography for Workstream 3.

Control rule: **182 sources in → 182 sources out, exactly once each** in the bibliography. Individual artifacts are the unit of placement. A standards family may therefore be represented in multiple groups through different documents, but the same bibliography entry is not duplicated across groups.

Within each group, sources remain alphabetized in CMOS 18 author-date style. Alphabetical order is deliberate: no source is visually ranked as more foundational, supplementary, or valuable until the group has been independently analyzed under common criteria.

## 10. Source type, source family, and contribution are separate axes

The corpus organization was corrected several times before the current method was established. The controlling distinction is now:

- **Source family / provenance:** who produced the source and what standards community it belongs to. Useful for lineage, but not the current comparison axis.
- **Primary source/artifact type:** what the individual source actually standardizes or provides. This is the current neutral grouping axis.
- **Technical/domain subject matter:** what concepts or problem areas the source actually describes. This must be extracted later from the sources themselves and must not be preloaded from V1.
- **Contribution/disposition:** what V2 eventually decides to reuse, map, supplement, defer, reject, or leave informative. This comes only after evidence review and synthesis.

A donor family is **not** forced into one group. Its individual documents are classified according to their own primary standardization target. For example, ISA requirements documents may sit with requirements, its Interface Control Document with interface specifications, its Data Model Specification with data/model artifacts, and its Software Design Document with architecture. NIEM, IEEE 1451, SOSA, MIMOSA, and other families distribute similarly where their individual artifacts perform different standardization jobs.

## 11. Source-type assessment and the standardization stack

A corpus-wide source-type assessment classified all 182 sources exactly once by primary artifact type. Hybrid sources may carry a secondary type in the audit CSV, but each receives one primary placement for counting and neutral organization.

The 182-source assessment found these artifact types:

| Source/artifact type | Count |
| --- | ---: |
| Data model / schema / encoding / exchange format | 38 |
| Guidance / explanatory / research / training | 30 |
| API / interface / protocol / service specification | 29 |
| Modeling / packaging / versioning / conformance methodology | 15 |
| Conceptual / information / domain model | 14 |
| Vocabulary / terminology / units / code list / registry | 13 |
| Ontology / formal semantic model | 9 |
| Reference architecture / architectural framework | 8 |
| Implementation / test / executable companion artifact | 6 |
| Requirements / capability / operational specification | 6 |
| Policy / standards registry / strategy / governance | 5 |
| Reference system / product / operational evidence | 5 |
| Profile / specialization / application model | 4 |
| **Total** | **182** |

“CSAPI foundational” is **not** one of these artifact types. It is an orthogonal role. A foundational source may itself be an API, ontology, information model, encoding standard, etc.

When source identities are removed, the corpus supports a potential standardization stack with these roles:

1. **Governance and construction** — policy, modeling rules, modularization, packaging, versioning, conformance.
2. **Semantic foundation** — ontologies, vocabularies, terminology, quantities, units, identifiers.
3. **Conceptual/domain definition** — information/domain models defining concepts, entities, relationships, and intrinsic constraints.
4. **Architecture and requirements** — roles, boundaries, viewpoints, capabilities, operational expectations.
5. **Specialization** — profiles and application models.
6. **Concrete representation** — schemas, encodings, data/exchange models.
7. **Interaction and service behavior** — APIs, interfaces, protocols, service contracts.
8. **Executable verification and realization** — implementations, middleware, test harnesses, machine-readable companions.
9. **Interpretation and reality check** — research, guidance, manuals, products, operational systems, and stress-test evidence.

This stack describes the **possibility envelope** of what the corpus can support. It does **not** establish that V2 must create one artifact per stack layer.

## 12. Potential whole of the V2 effort inferred from the source-type stack

The source-type stack shows that the evidence base is broad enough to support investigation of a coherent chain from domain meaning to interoperable implementation. Potential V2 artifacts include:

- a Domain Information Model;
- semantic mappings or ontology alignments;
- controlled definitions, vocabularies, quantities, units, or code identifiers;
- an application profile;
- an OGC/CSAPI binding;
- machine-readable schemas or constraint artifacts where justified;
- donor-to-V2 mapping crosswalks documenting fidelity;
- conformance targets, requirements, and validation tests;
- extension, versioning, and governance rules;
- canonical examples, test vectors, adapters, or reference implementations; and
- informative design rationale and implementation guidance.

These are **possible**, not committed. Each artifact must later earn its existence through interoperability need, reuse value, implementation benefit, and proportionate stewardship cost.

The stack also changes how donor comparison should be performed. Ontologies should first be understood as ontologies, information models as information models, architectures as architectures, schemas as schemas, APIs as interfaces, and conformance specifications as assurance mechanisms. A source should not be penalized because it does not solve a problem outside its standardization role.

## 13. The next question: identify the DIM “chassis”

The project owner asked which source-type group has the best chance to define the **chassis** of the V2 DIM. The recommended answer is:

> **Conceptual / Information / Domain Models**

This is the group whose primary job is closest to the chassis question: **What kind of thing is being modeled? What concepts define it? What belongs inside its boundary? What relationships characterize it?**

“Chassis” is shorthand for:

> **the bounded conceptual frame that identifies the class of real-world thing the DIM is about and establishes the high-level conceptual basis by which that thing is understood.**

The chassis is not necessarily one root class, and the domain boundary is not the same question as the root/anchor concept. Research may discover an established concept that more naturally gathers the intended sensing-system concerns, or it may show that the correct result remains a combination of existing concepts such as Sensor and Equipment without a new named class.

The source-type search order for this question is:

1. **Conceptual / Information / Domain Models** — strongest chance to define the bounded thing.
2. **Ontologies / Formal Semantic Models** — sharpen and test what the thing means.
3. **Reference Architectures / Architectural Frameworks** — test boundaries, roles, context, and composition.
4. **Requirements / Capability / Operational Specifications** — test whether the chassis can describe what real systems are expected to be and do.

The current CSAPI/SOSA/SSN baseline remains a comparison baseline, not a conclusion.

## 14. Chassis-study evidence population

The source-type assessment identifies **14 Conceptual / Information / Domain Model artifacts** in the frozen 182-source corpus. Thirteen appear under that heading in the v0.5 bibliography; OMS 3.0 is placed once in the separate CSAPI foundational group but is still classified as a Conceptual / Information / Domain Model in the source-type audit. The chassis study must therefore use the source-type audit rather than rely only on bibliography headings.

The 14-source evidence population is:

1. Industrial Digital Twin Association. 2026. *Specification of the Asset Administration Shell Part 1: Metamodel*. IDTA 01001, version 3.2.
2. Institute of Electrical and Electronics Engineers. 1999. *IEEE Standard for a Smart Transducer Interface for Sensors and Actuators—Network Capable Application Processor (NCAP) Information Model*. IEEE 1451.1-1999.
3. International Organization for Standardization and International Electrotechnical Commission. 2013. *Information Technology—Sensor Networks: Sensor Network Reference Architecture (SNRA)—Part 4: Entity Models*. ISO/IEC 29182-4.
4. International Organization for Standardization. 2010. *Information Technology—Smart Transducer Interface for Sensors and Actuators—Part 1: Network Capable Application Processor (NCAP) Information Model*. ISO/IEC/IEEE 21451-1:2010.
5. Medlin, Christina, ed. 2025. *NIEM Model Version 6.0*. OASIS Standard.
6. MIMOSA. 2018. *CCOM UML Class Model*. Version 4.1.0, 4.1.0-RC1 package.
7. Multilateral Interoperability Programme. 2012. *Joint C3 Information Exchange Data Model (JC3IEDM)*. Baseline 3.1.4.
8. Open Geospatial Consortium. 2023. *Abstract Specification Topic 20—Observations, Measurements and Samples*. Version 3.0.0. OGC 20-082r4. **Foundational-role source; also a conceptual/information/domain model.**
9. OPC Foundation and FieldComm Group. 2025. *OPC UA for Process Automation Devices—PA-DIM*. Version 1.02.0. OPC 30081.
10. OPC Foundation. 2025. *OPC Unified Architecture Part 100: Devices*. Version 1.05.0. OPC 10000-100.
11. OSUS-R Contributors. 2026. *OSUS-R Asset Interface and Capability Model*. Pinned source revision d09088.
12. Parello, John, Benoît Claise, Brad Schoening, and Juergen Quittek. 2014. *Energy Management Framework*. RFC 7326.
13. The Open Group. 2022. *Technical Standard for SOSA Reference Architecture, Edition 1.0: SOSA Domain-Specific Data Model*.
14. World Wide Web Consortium. 2013. *PROV-DM: The PROV Data Model*.

Some of these may ultimately prove too narrow, cross-cutting, or specialized to supply the chassis. They remain in the study because the current task is to discover that through a common review rather than exclude them by intuition.

## 15. Chassis-study research question and extraction template

The immediate question for every source in the 14-artifact population is:

> **How does this source conceptualize and bound the kind of operational sensing system/equipment that V2 is attempting to describe, if it does so at all?**

Do **not** begin by asking which V1 information subjects the source covers. Do **not** start by asking what useful concepts can be imported. First recover the source’s own conceptual frame.

For each source, extract the following independently:

1. **Source scope / universe of discourse** — what problem domain does the source say it models?
2. **Primary modeled subject** — what is the source fundamentally about?
3. **Central/top-level concepts** — what concepts organize the source?
4. **Membership or boundary criteria** — what makes something belong inside the modeled subject?
5. **System / asset / device / equipment / platform / component distinctions** — which terms exist and how are they related?
6. **Relationship to sensing** — is sensing central, one capability among many, external, or absent?
7. **Relationship to equipment / physical realization** — how does the source represent hardware, physical assets, or realization?
8. **Physical, logical, functional, operational, or informational character** — what kind of boundary is being modeled?
9. **Inside vs outside the boundary** — what is intrinsic to the subject and what is contextual/external?
10. **Composition / hosting / deployment / environment** — how does the source express constituent parts and operational context?
11. **Established names** — does the source provide an existing recognized concept that could plausibly name the intended V2 family?
12. **Abstraction breadth** — is the concept broad enough to include the motivating systems without becoming meaningless?
13. **Known lineage or alignments** — does the source explicitly reuse or map to another donor?
14. **Comparison to the current V2 baseline** — direct, broader, narrower, orthogonal, partial, or not applicable relative to `System / Sensor / Equipment` and the current whole-system intent.
15. **Chassis relevance** — record evidence only at first: potentially central, potentially supplemental, cross-cutting, too narrow, too broad, or not applicable. Do not rank sources yet.

Each source should be reviewed under the same template, with exact source version and locators where available. Preserve uncertainty and evidence depth. A source that cannot answer the chassis question should be recorded honestly rather than forced into it.

## 16. Neutral comparison, synthesis, and ranking gate

The chassis-study sequence is deliberately staged:

### Phase A — independent extraction

Review all 14 artifacts independently using the template above. Keep the source order neutral/alphabetical. Do not edit the clean V2 DIM or select a winner during this phase.

### Phase B — cross-source comparison

After all 14 are characterized, compare:

- recurring central concepts;
- recurring boundary definitions;
- equivalent or conflicting terminology;
- explicit source lineage;
- concepts that are broader/narrower than `Sensor + Equipment`;
- sources that provide a complete conceptual frame versus only a specialized slice;
- gaps that no source addresses; and
- cases where no new chassis name is necessary because existing sourced concepts already suffice.

### Phase C — source standing within the group

Only after comparison may the project identify sources that appear to provide:

- a **foundational chassis candidate**;
- **supplemental conceptual coverage**;
- **gap-filling distinctions**;
- **cross-cutting semantics** that belong elsewhere;
- **specialized/domain-only contributions**; or
- **no useful chassis contribution**.

This is where donor ranking or relative standing becomes legitimate. Alphabetical neutrality is preserved until Phase C.

### Phase D — chassis synthesis gate

Only after the group analysis should the project propose a candidate V2 chassis, boundary, or family term. The result must then be tested against the ontology, architecture, and requirements groups before being promoted into the clean V2 artifact.

## 17. Explicit stop rules for the next chat

The next chat must **not**:

- rebuild the eight V1 information subjects as donor-analysis categories;
- expand the frozen 182-source corpus without an explicit owner decision;
- treat the v0.4 provenance/community grouping as the controlling comparison structure;
- equate a standards family with one artifact type;
- duplicate the same source across bibliography groups;
- rank chassis sources before all 14 receive independent extraction;
- make `Sensor + Equipment` the desired answer rather than the comparison baseline;
- create a new umbrella class merely because a neat hierarchy would be convenient;
- update the clean V2 DIM during individual donor review;
- infer donor conformance from conceptual reuse or mapping;
- resume visualization-pipeline remediation unless explicitly requested.

If a source does not fit the chassis question, record that result and continue. Do not broaden the question mid-review merely to make every donor relevant.

## 18. Visualization status — paused and non-gating

A V2 Modeling and Visualization Guide exists and contains useful rules about diagram types, UML semantics, source provenance, layer separation, and a canonical-figure workflow. The figure workflow encountered repeated synchronization/layout problems between independently recreated Word/GitHub figures. The project owner directed the effort to stop spending time on figures and return to substantive research.

The clean V2 working artifact was restored to **Figure 1 only**. Figure 2 and Figure 3 experiments are not approved maintained content. The current figure lesson is captured in the guide: one figure must have one canonical source and multiple mechanical renders; GitHub and Word/PDF must be visually checked against the same source before approval.

Visualization work is **paused**. It does not gate the chassis study or donor analysis. Do not restart it unless explicitly asked.

## 19. Current clean V2 working artifact

The maintained clean V2 artifact is:

`Docs/Research/DIM_Profile_V2/Sensor_Systems_DIM_and_Profile_V2_Working_Draft_v0.1_25OCT2026.md`

It currently contains:

- purpose and standing;
- V2 objectives and design principles;
- DIM / Profile / Binding / Implementation separation;
- the working DIM definition;
- purpose-driven but binding-independent principle;
- domain-boundary vs root-concept distinction;
- current CSAPI/SOSA/SSN conceptual baseline;
- whole-system meaning;
- CSAPI Composition/Aggregation nuance;
- modularity/reuse principles;
- explicit non-inheritance of the V1 eight subjects;
- decisions/open questions; and
- development sequencing.

The clean artifact should not be expanded with chassis conclusions until the 14-source chassis analysis and cross-group validation have earned them.

## 20. Current V2 research artifacts and their roles

| Artifact | Role / standing |
| --- | --- |
| `DRAFT_Concept_Baseline_v0.1_25OCT2026.md` | Early sourced baseline for System/Sensor/Equipment, whole-system scope, and Composition/Aggregation. |
| `DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md` | Workstream 1 methodological grounding for DIM, profile relationship, modularity, and reuse. |
| `Sensor_Systems_DIM_and_Profile_V2_Working_Draft_v0.1_25OCT2026.md` | Clean self-describing V2 artifact; grows only with earned decisions. |
| `DIM_Profile_V2_Candidate_Donor_Bibliography_v0.3_25OCT2026.docx` | Frozen flat neutral bibliography: 182 external sources. |
| `DIM_Profile_V2_Candidate_Donor_Bibliography_Grouped_v0.4_25OCT2026.*` | Provenance/community-grouped alternate organization; retained for possible later use, not current comparison method. |
| `DIM_Profile_V2_Candidate_Donor_Bibliography_Source_Type_Grouped_v0.5_25OCT2026.md` | Current neutral bibliography: foundational group first, then sources grouped by what each artifact primarily standardizes; alphabetical within groups. |
| `DIM_Profile_V2_Source_Type_Assessment_and_Stack_v0.1_25OCT2026.md` | Corpus-wide artifact-type assessment and identity-free potential standardization stack. |
| `DIM_Profile_V2_Source_Type_Assessment_v0.1_25OCT2026.csv` | Auditable source-by-source primary/secondary type classification for all 182 sources. |
| `DIM_Profile_V2_Standardization_Stack_Narrative_v0.1_25OCT2026.md` | Standalone narrative explaining how the artifact types fit together and what the corpus can potentially support. |
| `DRAFT_CSAPI_Anchor_Standards_Environment_v0.1_25OCT2026.md` | Working note for CSAPI-native/foundational subset; corpus is frozen and not expanded through dependency chasing. |
| `DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md` | Visualization convention; useful but figure work currently paused/non-gating. |
| `PITON_DIM_Profile_V2_Continuity_v0.3_25OCT2026.md` | Superseded continuity checkpoint. |
| `PITON_DIM_Profile_V2_Continuity_v0.4_25OCT2026.md` | This active checkpoint. |

## 21. V1 predecessor artifacts worth recovering only when needed

The V1 materials remain evidence and should be consulted deliberately, not allowed to define V2 silently. Particularly useful predecessor artifacts include:

- `MERLIN_Managed_Physical_Sensing_Systems_Profile_Integrated_Binding_Draft_v0.3.5_17OCT2026.docx` — strongest V1 technical profile baseline;
- maintained V1 annotated bibliography/source register — provenance of the original research corpus;
- `MERLIN_MPSS_Evidence_to_Design_Update_Plan_v1.0_15OCT2026.docx` — contains U-INT-01 and the two-direction donor-comparison method;
- `PITON_MERLIN_MPSS_Integration_Continuity_v4.0_15OCT2026.docx` — predecessor integration continuity and mapping discipline;
- `MERLIN_Profile_Standards_Pedigree_and_Design_Rationale_Primer_v0.1_14OCT2026.docx` — layered compatibility, profile-awareness, and conformance distinctions;
- `MERLIN_OSCAR_Standards_Architecture_Review_v1.1_2026-10-22.pdf` — later review of V1 architecture, donor reconciliation, and source-vs-binding discipline.

Use these to recover goals, evidence, and lessons only. Do not revive V1 structure merely because it was well documented.

## 22. Compact status matrix

| Topic | Standing | Current result |
| --- | --- | --- |
| V2 formal identity | Working decision | Not coupled to MERLIN as formal model/profile identity. |
| DIM terminology/method | Closed / working decision | Domain Information Model is appropriate and source-grounded. |
| DIM/profile relationship | Closed / working decision | Purpose-driven but binding-independent; model for the profile, not to the profile. |
| Whole-system meaning | Working decision | Informational completeness about the sensing system; not automatically system-of-systems. |
| Current top-level CSAPI characterization | Candidate baseline | `Sensor + Equipment`; comparison baseline only. |
| Final domain-family/chassis term | Open / immediate research target | Must emerge from donor evidence; no new term coined yet. |
| Modularity/reuse | Working decision | Reuse invariants; specialize variation; modules only when semantically earned. |
| V1 eight subjects | Predecessor evidence only | Explicitly not donor-analysis bins or V2 architecture. |
| V2 objectives | Added to clean artifact | Nine outcome-oriented goals plus donor-accommodation acceptance question. |
| Source corpus | Frozen | 182 external sources; no dependency-driven expansion. |
| Current donor grouping | Active | Individual artifacts grouped once by primary standardization/artifact type; alphabetical within groups. |
| Source-type stack | Established | Describes possibility envelope, not DIM structure. |
| Chassis source type | Immediate focus | Conceptual / Information / Domain Models. |
| Chassis evidence population | Established | 14 artifacts from source-type audit, including foundational OMS 3.0. |
| Donor ranking | Blocked until group extraction complete | Independent extraction first; rank only after common comparison. |
| Clean V2 DIM synthesis | Blocked by design | No DIM edits during individual donor review. |
| Visualization work | Paused | Figure 1 only in clean artifact; visual work is non-gating unless explicitly resumed. |

## 23. Exact restart sequence

When this work resumes in a new chat:

1. Read this PITON first.
2. Read `DRAFT_Concept_Baseline_v0.1_25OCT2026.md` and `DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md` only as needed to recover the current comparison baseline.
3. Read `DIM_Profile_V2_Source_Type_Assessment_v0.1_25OCT2026.csv` to recover the 14-source Conceptual / Information / Domain Model evidence population and artifact classifications.
4. Use `DIM_Profile_V2_Candidate_Donor_Bibliography_Source_Type_Grouped_v0.5_25OCT2026.md` for neutral CMOS-18 source order and citations.
5. Begin **Phase A independent chassis extraction** for the 14 sources using the Section 15 template.
6. Preserve alphabetical neutrality. Do not rank, synthesize, or edit the DIM until all 14 source characterizations are complete.
7. After Phase A, perform the cross-source comparison in Section 16.
8. Only then identify potential foundational chassis candidates, supplements, gap-fillers, cross-cutting sources, and non-applicable sources.
9. Any candidate chassis must subsequently be tested against the Ontology, Reference Architecture, and Requirements groups before being promoted into the clean V2 artifact.

The first substantive question in the new chat is therefore:

> **Across the 14 Conceptual / Information / Domain Model artifacts, how does each source conceptualize and bound the kind of operational sensing system/equipment V2 is trying to describe, and what existing recognized concept—if any—best serves as the chassis for the emerging DIM?**