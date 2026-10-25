# PITON — DIM/Profile V2 Research Continuity

**Version:** 0.2  
**Date:** 25 October 2026  
**Standing:** Method and sequencing checkpoint  
**Repository:** `OS4CSAPI/glaux-client`  
**Branch:** `research/dim-profile-v2`  
**Workspace:** `Docs/Research/DIM_Profile_V2/`

> **CONTROLLING SEQUENCE: 1 → 2 → 3, ONE AT A TIME.** Do not begin a later workstream until the current workstream has been completed, packaged, reviewed, and explicitly closed. The immediate next task is Workstream 1 only: ground the term and method **Domain Information Model**.

## 1. Purpose of this PITON

This PITON supersedes PITON v0.1 as the continuity checkpoint for the DIM/Profile V2 research effort. It captures the conceptual progress, source-population reset, NIEM expansion, and methodological decisions made after v0.1 so that a successor chat can resume without reconstructing the work or accidentally reverting to V1 habits. It does not revise the technical model, approve a profile, or adopt any donor source. Its main function is to preserve research discipline and enforce the next three workstreams in the agreed serial order.

## 2. Governing objective and standing

V2 is a clean-slate re-examination of the sensing-system domain information model and eventual application profile. V1 remains predecessor evidence: it records the problem, prior donor research, examples, design choices, and lessons learned, but its terminology, relationships, profile-owned vocabulary, and scope are not automatically carried forward. V2 is not coupled to MERLIN as a product or program identity and should be capable of standing independently if the research supports that outcome. The present effort remains pre-modeling research: no new V2 DIM has yet been synthesized.

## 3. Core research discipline retained from v0.1

- Use established source concepts as primitives. Do not coin umbrella categories, classes, or relationship names merely because a combination seems intuitive.
- When multiple sourced concepts describe one case, keep them as sourced concepts applied together unless research demonstrates that an existing term is insufficient and a genuinely new term is necessary.
- Distinguish source meaning, project interpretation, mapping/translation, profile constraint, newly authored semantics, and native standards implementation/conformance.
- Do not equate investigation with adoption. A source may confirm, challenge, contextualize, specialize, or prove irrelevant without becoming a dependency.
- Prefer evidence-first synthesis. Later sources must have the same opportunity to challenge earlier assumptions as earlier sources had to shape them.

## 4. Conceptual baseline preserved

The working meaning of **whole system** is informational, not architectural enlargement. It means that a user should be able to access, understand, and manage the deployed sensor system as a complete operational subject—not merely retrieve the observations it produces. Description, identity, configuration, components, capabilities, telemetry, deployment context, communications, power, condition, commands/management, service and lifecycle history, provenance, and related information may all belong to that complete description. Do not reinterpret whole system as a system-of-systems, enterprise system, sensor network, or larger aggregate unless a source and use case independently require that conclusion.

The strongest current sourced characterization of the top-level hardware sensing subjects that motivated V1 remains CSAPI `systemType = Sensor` together with `assetType = Equipment`. This is a candidate characterization, not a final V2 scope boundary and not a newly named class. SOSA/SSN supplies the conceptual System/Sensor/Actuator/Sampler/Platform distinctions, while CSAPI supplies the practical System-resource classifications and asset-type facet. SensorML provides complementary physical-system/process structure and supports complex sensor systems whose internal parts can perform sensing, actuation, computation, and other functions.

## 5. Subsystem relationship nuance that must be preserved

CSAPI Part 1 distinguishes **Composition** from **Aggregation** for subsystem relationships. Composition is used when a subsystem is an integral or ordinarily enduring part of the parent; Aggregation applies when a subsystem is not permanently attached and can be associated with different parents at different times, with Deployment carrying that time-scoped relationship. The physical connector is not the criterion: a cable-connected item may still be Composition if it ordinarily remains integral, while a mechanically mounted payload may be Aggregation if it is routinely reconfigured. Any future V2 component/equipment relationship must be checked against these native semantics before a new relationship is proposed.

## 6. Source-population reset completed after v0.1

After v0.1, the V1 donor population was re-audited because the first neutral V2 bibliography was too narrow and omitted important sources, including the full Army Integrated Sensor Architecture corpus. The corrected process stopped using summarized donor-family lists as a proxy for the actual source population and reconstructed the corpus from the maintained V1 bibliography/register and later research workstreams. The result was a neutral, non-annotated bibliography intended to remove V1-era judgments, rankings, dispositions, and “why it mattered” language from the V2 starting population. Alphabetical order is used to avoid implying priority.

- **v0.2 neutral bibliography:** 153 external candidate references reconstructed from the V1 population and later V1 workstreams.
- All **eleven supplied ISA 6.0 documents** are carried as distinct references rather than collapsed to one family citation.
- V1 project-authored analyses and device-specific test evidence are not treated as external donor standards, while distinct editions and machine-readable companion artifacts are preserved when they were independently researched.
- The incomplete 46-entry bibliography v0.1 was removed from the V2 branch.

## 7. NIEM donor-family expansion completed

A fresh NIEM research pass identified NIEM as a material donor family that V1 had not adequately represented. The search deliberately separated NIEM’s governing architecture and modeling methodology from its substantive machine-readable domain content. Twenty-nine NIEM-family sources were added, expanding the neutral V2 candidate bibliography from 153 to **182 external references**. Inclusion is still neutral: no NIEM concept, method, namespace, or schema has yet been accepted into V2.

The NIEM increment includes current NIEM 6.0 architecture and Naming and Design Rules, model and conformance material, still-relevant exchange/package and JSON/UML resources, and machine-readable NIEM 6 model artifacts such as Core, CBRN, CBRN code lists, Cyber, Intelligence, Military Operations, USMTF, Screening, CUI, GML adapter, and JSON-LD context. The CBRN material is notable because it contains substantive operational-sensing concepts such as radiation instruments, measurements, detection events, occupancy sensing, positioning, and N42-related data, but that observation does not constitute a donor disposition. The separate file `NIEM_Candidate_Donor_Source_Additions_v0.1_25OCT2026.md` records exactly which 29 sources were added. Do not begin NIEM concept extraction before the ordered workstreams below reach the donor-review stage.

## 8. New methodological problem statement

The next phase must establish the intellectual machinery for V2 before model synthesis begins. Three separate problems have been identified: **what kind of artifact we are actually building**, **how that artifact and its evidence will be represented visually and repeatably**, and **how a large donor population will be organized and reviewed without recreating V1 sequencing bias**. These problems are related but must not be solved simultaneously because each can silently bias the others. The project owner has directed that they be completed one at a time in the order below.

## 9. Workstream 1 — Ground “Domain Information Model”

This is the **immediate next task and the only workstream authorized to begin** when this PITON is resumed. The objective is to determine from authoritative industry and standards practice what *domain*, *information model*, *domain model*, *conceptual model*, and *domain information model* mean; how those terms relate; and which term most accurately describes the artifact V2 intends to build. The research must not search merely for citations that validate the project’s current wording. It must be allowed to conclude that another established term is more precise if the evidence warrants that result.

Required outcomes:

- Establish a source-citable definition and characteristics of an information model and a domain-focused information model.
- Distinguish the artifact from ontology, conceptual model, logical/data model, schema, API binding, application profile, implementation, and user-interface representation.
- Identify established standards or industry examples that use the same or closely related approach.
- Determine what the selected term implies about entities/concepts, relationships, constraints, behavior, technology independence, and governance.
- Produce a compact **Concept and Method Basis** artifact and update this PITON or a successor only after the result is reviewed.

**STOP GATE:** Do not begin Workstream 2 until Workstream 1 is complete, packaged, and reviewed. Do not use Workstream 1 to start designing the sensing-domain model itself. The desired output is methodological grounding, not a new DIM.

## 10. Workstream 2 — Establish a visualization and modeling convention

Workstream 2 begins only after Workstream 1 is closed. Its purpose is to establish a small, standards-practiced, repeatable visual language for the entire V2 effort so diagrams are analytical artifacts rather than ad hoc illustrations. The research should evaluate UML and other appropriate conventions by viewpoint and purpose, not select one universal diagram for every question. The output should define which diagram or matrix type is used for conceptual structure, instances/examples, behavior/time, scope/context, source traceability, and any other recurring need.

Required rules include:

- Every diagram must declare the question/viewpoint it answers.
- Graphical symbols and relationship lines must have defined semantics; proximity and decorative layout must not imply meaning.
- No critical semantic distinction may depend solely on color.
- Cardinality, specialization, composition, aggregation, hosting, deployment, and other relationships must use their established notation only when their formal meaning applies.
- Conceptual classes, instances/examples, external-source concepts, and V2-authored concepts must not be mixed invisibly.
- Prefer a text-based, version-controlled, reproducible source format where practical so diagrams can be diffed and regenerated consistently.
- Use matrices/tables instead of diagrams when many-to-many evidence or source mappings are clearer that way.

**STOP GATE:** Do not begin Workstream 3 until the visualization/modeling convention is documented and demonstrated on a trivial or non-domain-distorting example. The purpose is to prove that the notation can be produced consistently before it becomes the visual record of substantive donor research.

## 11. Workstream 3 — Organize donors and define the donor-review protocol

Workstream 3 begins only after Workstreams 1 and 2 are closed. The first task is to separate the **native/anchor standards environment** from the **external candidate donor corpus**, rather than treating every source as the same kind of donor. CSAPI, SensorML, SWE Common, and their actual normative or conceptual dependencies should be derived from the standards themselves and established as the anchor environment. External sources should then be grouped by the source community’s own native subject matter, with entries kept alphabetically within each group to avoid implied ranking.

Three independent classification axes must be kept separate:

| Axis | Question | When assigned |
|---|---|---|
| Source family | Where does the source natively belong, and what problem does it claim to address? | During neutral organization |
| Contribution type | What kind of contribution could the source potentially make? | During source extraction |
| Disposition | What does V2 ultimately decide to do with that contribution? | Only after evidence review/synthesis |

Potential contribution types may include concepts/definitions, relationships, classifications/taxonomies, constraints/cardinalities, code lists/vocabularies, state/lifecycle semantics, behavior/process semantics, architecture/interface patterns, profiling/extension/governance methods, conformance/test methods, mapping/translation precedents, and implementation/stress-test evidence. This list is provisional and should be finalized as part of Workstream 3 rather than treated as an already-approved taxonomy. Likewise, future dispositions may include forms such as direct reuse, qualified reuse, mapping/translation, specialization-only use, methodological precedent, informative-only, defer, source-gated, out-of-scope, or reject/conflict, but the vocabulary must be defined before it is applied.

## 12. Anti-bias donor-review rule and synthesis gate

V2 must not repeat the V1 pattern in which early donors influenced an emerging model and later donors were primarily evaluated as improvements to that existing model. Individual donor reviews must extract source meaning independently using the same review template and **must not directly modify the DIM**. Findings from each source or source family accumulate into an evidence set. Model synthesis occurs only at an explicit synthesis gate after the agreed comparison population has been examined under common rules.

1. Review Source A independently and record its concepts, relationships, constraints, distinctions, evidence depth, and possible contribution types.
2. Repeat the same extraction protocol for Source B, Source C, and the remaining agreed sources without editing the DIM.
3. Compare extracted evidence across sources only after the relevant review set is complete.
4. At the synthesis gate, identify candidate common concepts and relationships, conflicts, specializations, gaps, and cases where no new concept is necessary.
5. Only then draft or revise V2 model content, with every adopted meaning traceable to its source or explicitly identified as project-authored.

## 13. Immediate restart instruction

When this work resumes, **begin with Workstream 1 only**. Research and ground the term *Domain Information Model* and the adjacent terms necessary to determine whether DIM is the correct methodological anchor for V2. Do not begin diagram-standard selection, donor grouping, donor extraction, donor disposition, or DIM construction in the same iteration. Package and review the Workstream 1 result before proceeding to Workstream 2.

## 14. Current V2 workspace artifacts

| Artifact | Role |
|---|---|
| `DRAFT_Concept_Baseline_v0.1_25OCT2026.md` | Conceptual checkpoint for System/Sensor/Equipment, whole-system meaning, and subsystem semantics. |
| `PITON_DIM_Profile_V2_Continuity_v0.1_25OCT2026.md` | Superseded continuity checkpoint retained for history. |
| `DIM_Profile_V2_Candidate_Donor_Bibliography_v0.3_25OCT2026.docx` | Current neutral non-annotated bibliography; 182 external candidate references after NIEM expansion. |
| `NIEM_Candidate_Donor_Source_Additions_v0.1_25OCT2026.md` | Auditable 29-source NIEM increment added during V2. |
| `PITON_DIM_Profile_V2_Continuity_v0.2_25OCT2026.md` / `.docx` | This checkpoint; controlling research sequence and restart instructions. |

## 15. Predecessor V1 materials to preserve but not inherit automatically

The maintained V1 annotated bibliography and source register remain the provenance record for the prior research, and the MPSS v0.3.5 profile and related examples/primer remain the strongest record of what V1 attempted to model. These artifacts are evidence, not authority for V2 terminology or structure. Use them to recover prior questions, sources, decisions, and test cases, but do not silently copy V1 names, R01–R20 relationships, local code lists, or profile-owned concepts into V2. Any V1 concept that survives must do so because the V2 research independently supports it.

## 16. Compact status matrix

| Topic | Standing | Meaning |
|---|---|---|
| V2 identity | Settled for now | Not coupled to MERLIN as formal model/profile identity. |
| “Whole system” meaning | Working conclusion | Complete operational understanding of the sensor system; not automatically a system-of-systems. |
| Top-level candidate characterization | Open candidate | CSAPI Sensor + Equipment; must still survive broader evidence. |
| New compound class name | Not adopted | No invented name for Sensor + Equipment or other combinations. |
| Composition vs Aggregation | Working conclusion | Preserve native CSAPI distinction for enduring vs deployment-scoped subsystem association. |
| Neutral donor population | Current | 182 external candidate references in bibliography v0.3. |
| NIEM | Added, not analyzed | 29 sources added as a first-class candidate donor family. |
| DIM terminology/method | Next / open | Workstream 1. |
| Visualization convention | Queued | Workstream 2; do not begin yet. |
| Donor grouping/review protocol | Queued | Workstream 3; do not begin yet. |
| V2 DIM synthesis | Blocked by design | Begins only after controlled donor extraction and explicit synthesis gate. |

## 17. References carried forward for the conceptual baseline

Open Geospatial Consortium. 2025a. *OGC API – Connected Systems – Part 1: Feature Resources*. OGC 23-001, version 1.0. July 16. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC SensorML Encoding Standard*. OGC 23-000, version 3.0. July 16. https://docs.ogc.org/is/23-000/23-000.html.

Wilde, Erik. 2013. “The ‘profile’ Link Relation Type.” RFC 6906. March. https://www.rfc-editor.org/rfc/rfc6906.html.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology – 2023 Edition*. W3C Working Draft, October 21. OGC 25-022. https://www.w3.org/TR/vocab-ssn-2023/.
