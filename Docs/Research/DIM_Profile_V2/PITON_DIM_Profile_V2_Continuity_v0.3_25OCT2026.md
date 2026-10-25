# PITON — DIM/Profile V2 Research Continuity

**Version:** 0.3  
**Date:** 25 October 2026  
**Standing:** Continuity checkpoint after DIM-method grounding and visualization test drive  
**Repository:** `OS4CSAPI/glaux-client`  
**Branch:** `research/dim-profile-v2`  
**Workspace:** `Docs/Research/DIM_Profile_V2/`

> **CONTROLLING SEQUENCE:** Workstream 1 is complete. Workstream 2 is substantially drafted but not yet closed. The immediate next task is to **test the visualization convention against the actual V1 DIM using reproducible, source-controlled diagrams**, correct the guide if needed, and only then close Workstream 2. Do not begin donor grouping/review protocol (Workstream 3) until that test is complete.

## 1. Purpose of this PITON

This PITON supersedes v0.2 as the active continuity checkpoint for DIM/Profile V2. It captures the work completed after the methodological sequencing plan was established: grounding the term and role of the Domain Information Model, starting the clean V2 artifact, defining a practical modeling/visualization convention, creating reproducible diagram templates, and performing the first visual test drive against the V1 model. It is intended to let a successor chat resume without repeating research or accidentally treating an illustrative diagram as authoritative model content.

## 2. V2 objective and research discipline

V2 remains a clean-slate re-examination of the sensing-system domain information model and eventual application profile. V1 is predecessor evidence, not design authority. Established source concepts remain the preferred primitives; V2 should not invent umbrella terms, classes, relationships, or modules simply because a combination appears useful. Multiple sourced concepts may be used together descriptively without being promoted into a new named class.

The V2 research remains evidence-first. Donor investigation is not adoption, and standards-based translation, conceptual reuse, profile specialization, concrete OGC binding, and native implementation/conformance must remain explicitly distinct. Individual donor reviews must not modify the DIM directly. Evidence is accumulated first and synthesized only at an explicit synthesis gate after the agreed comparison population has been examined under common rules.

## 3. Concept baseline retained

The existing concept baseline remains valid. “Whole system” means informational completeness about the deployed sensor system: the user should be able to understand the system’s identity, technical description, components, configuration, capabilities, telemetry, deployment context, communications, power, condition, management interactions, lifecycle/history, provenance, observations, products, and supported actions as one coherent operational subject. It does **not** mean system-of-systems or architectural enlargement merely because the model contains more than observations.

The strongest current sourced characterization of the motivating hardware systems remains `systemType = Sensor` plus `assetType = Equipment` in CSAPI. This remains a candidate characterization, not a final scope boundary and not a newly named class. SOSA/SSN remains the conceptual source for Asset/System/Sensor/Actuator/Sampler/Platform relationships; CSAPI provides practical System classification and asset realization facets; SensorML supports rich system/process/hardware description. The search remains open for an established boundary-defining concept that may more naturally describe the family represented today by the combination of System, Sensor, and Equipment.

## 4. Workstream 1 completed — Domain Information Model grounding

Workstream 1 asked whether “Domain Information Model” was an invented project phrase or an established industry/standards practice appropriate to V2. The result is sufficiently strong to close that question unless later evidence requires revision. “Domain Information Model” is retained as the methodological anchor.

The working V2 definition is: **a Domain Information Model is an implementation- and protocol-independent model of the common concepts, entities, relationships, and intrinsic semantic constraints needed to describe and understand a defined problem domain**. The project-specific purpose is to model the information needed to understand a deployed sensor system as a complete operational subject, independently of the API, encoding, schema, implementation, or UI used to represent that information.

The principal governing rule is **purpose-driven but binding-independent**, summarized as **model for the profile, not to the profile**. The intended CSAPI application profile is a legitimate requirements lens: it may determine which domain questions V2 must be able to answer and which distinctions matter operationally. It must not, however, turn CSAPI paths, JSON properties, encoding structures, implementation convenience, or profile-only obligations into intrinsic domain semantics.

The relationship among artifacts is now understood as follows:

1. **DIM:** establishes domain meaning.
2. **Application profile:** selects and constrains DIM content for a specific interoperability purpose and adds profile obligations.
3. **OGC binding:** specifies how selected meanings and obligations are represented using CSAPI, SensorML, SWE Common, and related mechanisms.
4. **Implementation:** realizes those representations in servers, adapters, clients, validators, storage, and UIs.

The profile supplies requirements to the DIM; the DIM supplies semantics to the profile. This does not require pretending the profile is unknown while the DIM is built.

## 5. Domain boundary, root concept, and modularity decisions

The domain boundary and the root/anchor concept of the model are separate questions. V2 must not invent a single umbrella class merely to give the model a tidy root. Research may discover a recognized family concept beyond System/Sensor/Equipment, or it may determine that no additional root class is necessary. Either outcome is acceptable.

Modularity is accepted as a design principle **only where semantic cohesion justifies it**. Industry information models commonly organize reusable core/common concepts, domain modules, extensions, packages, or subdomains, but V2 must derive its partitions from evidence rather than inherit document headings. A subject area should become a reusable module/subdomain only where it has coherent internal concepts/relationships, bounded dependencies, meaningful independent applicability, and supporting source lineage.

The reuse rule is: **reuse invariants; specialize variation**. Common concepts should be common only when their meaning genuinely survives across relevant system families. Realization-specific concepts should remain specific rather than being abstracted into vague universal semantics merely to maximize reuse. A hypothetical future Human Sensor profile is an architectural test of cleanliness, not a present requirement that should distort the Equipment-focused semantics currently under study.

## 6. Standing of the eight V1 information subjects

The eight V1 organizing areas remain valuable predecessor evidence but are **not** adopted as eight V2 subdomains, modules, or “sub-DIMs.” They are candidate subject areas to test:

1. identity / model / technical description;
2. equipment / composition / physical arrangement;
3. sensing capabilities / performance / outputs;
4. deployment / emplacement / location / responsibility;
5. operating configuration / modes / supported actions;
6. communications / connectivity / access;
7. power sources / operating arrangement;
8. condition / service / recovery / lifecycle.

Different subjects may ultimately resolve differently. Some may be cross-cutting core semantics; some may become reusable modules; some may split or merge; some may prove to be relationship patterns rather than domain partitions. The donor-review process should be allowed to reveal that structure rather than forcing the V1 organization into V2.

## 7. Clean V2 artifact started

A clean V2 working artifact has been started:

`Sensor_Systems_DIM_and_Profile_V2_Working_Draft_v0.1_25OCT2026.md`

The title intentionally uses “Sensor Systems” as descriptive working language only. The final domain-family name remains open. The document is intended to become the self-describing V2 artifact rather than another research memo about V2. It currently contains only earned material: purpose/standing; artifact architecture; DIM definition; relation to the CSAPI profile; domain boundary versus anchor concept; current System/Sensor/Equipment foundation; whole-system scope; Composition/Aggregation nuance; modularity/reuse; status of the eight V1 subjects; decisions/open questions; and development sequence.

This clean artifact should grow as decisions are earned. Research notes, PITONs, donor inventories, and methodological artifacts remain supporting evidence rather than substitutes for the clean V2 document.

## 8. Workstream 2 drafted — Modeling and Visualization Guide

A practical V2 modeling and visualization convention has been drafted:

`DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md`

The goal is deliberately modest: provide enough repeatable instruction that diagrams are accurate, consistent, professional, reproducible, and semantically honest every time they are created. The guide is not intended to turn the project into a UML or model-driven-engineering exercise.

The approved working repertoire is intentionally small:

- UML class diagram — conceptual structure;
- UML object/instance diagram — concrete examples/configurations;
- UML package diagram — actual model organization/modules;
- UML sequence diagram — ordered interactions;
- UML state-machine diagram — states/transitions;
- UML activity diagram — workflow/branching;
- controlled context/layer diagram — explanatory architecture/scope;
- matrix/table — many-to-many source, donor, coverage, and traceability evidence.

The authoritative visual view of DIM conceptual structure is expected to be the UML class diagram unless another approved view better answers the question. Every figure must have a defined purpose; if a diagram is not clearer than prose or a table, do not make one.

## 9. Visualization semantic rules established

The guide establishes the following standing rules:

- UML symbols carry their actual semantics and are never decorative.
- Generalization means genuine specialization/generalization.
- Multiplicity is shown only when supported by domain evidence.
- Associations should use meaningful names/roles rather than generic “relatedTo” or “has” where a more precise relationship exists.
- DIM concepts, profile rules, OGC binding mechanisms, and implementation artifacts must not be mixed invisibly.
- Concepts/examples/instances must not be mixed without explicit layer/view labels.
- Source provenance and research status are shown textually (for example `[source: CSAPI]`, `[V2 candidate]`, `[V2-authored]`) and never solely through color.
- Color may support readability but cannot carry unique semantic meaning.
- Complex models should be split into coherent views rather than shrunk into unreadable “everything diagrams.”
- Diagram source must be preserved so a figure can be regenerated rather than manually reconstructed.

A particularly important rule is that **CSAPI Composition/Aggregation must not automatically be rendered with UML filled/hollow diamonds simply because the same English words appear in both specifications**. CSAPI explicitly uses its own semantics and describes Composition more loosely than strict UML. A UML aggregation/composition symbol is used only if UML semantics are independently supported; otherwise the CSAPI relationship should be represented as a labeled association.

## 10. Reproducible diagram source and templates

PlantUML is the preferred working source mechanism for UML-like V2 diagrams because it is text-based, versionable, diffable, and reproducible. PlantUML is not the semantic authority; OMG UML and the V2 guide are. If another tool is required to represent a construct correctly, the editable model source must still be preserved.

Seven starter templates were committed under:

`Docs/Research/DIM_Profile_V2/Visualization/templates/`

They cover conceptual class, instance, module/package, sequence, state, activity, and context/layer views. These templates contain no substantive DIM decisions; they exist to stabilize metadata, reading direction, and diagram-source structure.

## 11. First visualization test drive — V1 DIM

A first visual test was performed by asking for a diagram of the V1 DIM. The generated figure demonstrated that the new visual direction can produce a substantially clearer, more professional, and more communicative figure than the ad hoc diagrams that caused problems in V1. It was useful as a **visual-quality and communication test**.

However, that generated image is **not an authoritative V1 DIM diagram and does not yet satisfy the V2 visualization guide**. It was generated as an illustrative image rather than from the maintained V1 model using the version-controlled PlantUML convention. It also introduced visual/model details that were not independently verified against the V1 source during generation. Therefore:

- do not treat the generated figure’s class names, attributes, stereotypes, cardinalities, aggregation/composition symbols, or exact groupings as V1 model truth;
- do not commit it as an authoritative model diagram;
- do not use it as evidence for V2 semantics;
- retain the result only as proof that the desired visual quality and clarity are achievable.

This distinction is essential: **a visually strong diagram can still be semantically wrong**. The whole purpose of Workstream 2 is to make both dimensions reliable.

## 12. Immediate next task — rigorous V1 test drive

Before Workstream 2 is closed, recreate a representative V1 DIM diagram using the actual V1 model/profile sources and the new guide. The immediate test should:

1. recover the V1 DIM concepts/relationships from the maintained V1 technical artifacts rather than from memory;
2. decide which single question the test figure answers (for example, an overview of the eight V1 information subjects and principal concept/relationship groups);
3. author the figure in version-controlled PlantUML or another approved reproducible format;
4. explicitly distinguish V1 domain concepts, OGC-native constructs, V1-authored/profile bindings, and information-subject groupings;
5. avoid unsupported multiplicities or UML aggregation/composition symbols;
6. render the figure at normal document size and evaluate clarity, crossing, typography, grouping, and source/status labels;
7. revise the guide/templates if the real V1 test exposes a recurring problem;
8. preserve both source and rendered output once the test is judged accurate and useful.

Only after this real-source test succeeds should Workstream 2 be considered closed.

## 13. Workstream 3 remains blocked

Do not begin donor grouping/review protocol yet. Once Workstream 2 is closed, Workstream 3 will:

1. separate the native/anchor CSAPI standards environment from the external candidate donor corpus;
2. group external sources neutrally by their native subject/community rather than by hoped-for contribution;
3. keep entries alphabetical within groups where practical;
4. distinguish **source family**, **potential contribution type**, and **eventual disposition** as separate classification axes;
5. define a common donor-extraction template;
6. prevent individual donor reviews from directly editing the DIM;
7. synthesize only at an explicit later gate.

The neutral candidate bibliography currently contains **182 external references**, including the 29-source NIEM increment. NIEM has been added to the source population but has not yet been substantively analyzed for V2 adoption.

## 14. Current V2 workspace artifacts

| Artifact | Role |
| --- | --- |
| `DRAFT_Concept_Baseline_v0.1_25OCT2026.md` | Sourced conceptual checkpoint: System/Sensor/Equipment, whole-system meaning, Composition/Aggregation. |
| `DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md` | Workstream 1 findings: DIM method, purpose, modularity, reuse, relationship to profile/binding. |
| `Sensor_Systems_DIM_and_Profile_V2_Working_Draft_v0.1_25OCT2026.md` | Clean V2 artifact to grow as decisions are earned. |
| `DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md` | Working diagram/visualization convention. |
| `Visualization/templates/*.puml` | Reproducible starter sources for approved diagram types. |
| `DIM_Profile_V2_Candidate_Donor_Bibliography_v0.3_25OCT2026.docx` | Neutral source population, 182 external candidate references. |
| `NIEM_Candidate_Donor_Source_Additions_v0.1_25OCT2026.md` | Auditable 29-source NIEM increment. |
| `PITON_DIM_Profile_V2_Continuity_v0.2_25OCT2026.md` | Superseded continuity checkpoint retained for history. |
| `PITON_DIM_Profile_V2_Continuity_v0.3_25OCT2026.md` | This active continuity checkpoint. |

## 15. Compact status matrix

| Topic | Standing | Meaning |
| --- | --- | --- |
| V2 identity | Working decision | Not coupled to MERLIN as formal model/profile identity. |
| DIM terminology/method | **Closed / working decision** | Domain Information Model is an appropriate, established methodological anchor. |
| DIM relation to profile | **Closed / working decision** | Purpose-driven but binding-independent; model for the profile, not to the profile. |
| Whole-system meaning | Working decision | Informational completeness about the sensor system. |
| Top-level candidate characterization | Candidate | Sensor + Equipment; final domain boundary/name remains open. |
| Domain boundary vs root concept | Working decision | Separate questions; no umbrella class invented for diagram neatness. |
| Modularity/reuse | Working decision | Reuse invariants; specialize variation; modules only where evidence supports cohesion. |
| V1 eight subjects | Candidate evidence | Subject areas to test, not inherited V2 modules/subdomains. |
| Clean V2 artifact | Started | Grow only with earned decisions. |
| Visualization convention | **Active / nearly complete** | Guide and templates drafted; requires rigorous real-source V1 test. |
| First generated V1 figure | Illustrative only | Good visual-quality proof; not authoritative or guide-compliant model source. |
| Donor grouping/review protocol | Blocked / next after visualization | Workstream 3. |
| V2 DIM synthesis | Blocked by design | Begins only after donor extraction and explicit synthesis gate. |

## 16. Restart instruction

When work resumes, **do not re-open the DIM-method question and do not begin donor grouping**. Resume Workstream 2 by building a guide-compliant, source-controlled V1 DIM test figure from the actual V1 artifacts. Use that test to determine whether the visualization guide is sufficient in practice. If the result is semantically accurate, readable, reproducible, and consistent with the guide, close Workstream 2 and proceed to Workstream 3. If the test reveals a weakness, correct the guide/templates first and repeat the test.
