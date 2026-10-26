# PITON — DIM/Profile V2 Research Continuity

**Version:** 1.3  
**Date:** 26 October 2026  
**Standing:** Recovery correction; Phase A extraction complete, validation/audit required before any cross-source synthesis  
**Repository:** OS4CSAPI/glaux-client  
**Branch:** research/dim-profile-v2  
**Workspace:** Docs/Research/DIM_Profile_V2/

> **RESTART INSTRUCTION:** This PITON supersedes v1.2 and all earlier restart instructions. Do not treat the later anatomy synthesis artifacts as accepted V2 decisions. Phase A reached mechanical extraction completion across 30 frozen semantic lineages, but that work has not been accepted as epistemically validated. **Phase B is NOT STARTED and is NOT AUTHORIZED.** Before substantive work resumes after a new-chat recovery, first reread the mandatory baseline documents in Section 2, restore the exact CSAPI-derived System/Sensor/Equipment reasoning, and then continue only with the owner-directed Phase A validation/audit work described here.

## 1. Why v1.3 exists

A chat/UI failure occurred after the Phase A extraction sequence, and subsequent AI execution overreached. Later artifacts promoted cross-source comparison, candidate anatomy, validation, and chassis/anatomy decisions farther than the project owner accepts as trustworthy.

The correction is not that Phase A produced no useful work. The correction is that **Phase A completion was mistaken for Phase A validation**, and later synthesis risked turning AI interpretation into apparently corroborated donor evidence.

This PITON therefore restores the safe research state:

- the early CSAPI-derived conceptual baseline remains the comparison baseline;
- the 182-source donor corpus and the 30-lineage Phase A population remain useful research infrastructure;
- the 30 Phase A worksheets remain candidate evidence;
- **Phase A findings are not presumed correct merely because all worksheets were completed;**
- Phase B/C/D outputs generated after that point are quarantined until deliberately revalidated;
- no final high-level DIM anatomy or final bounded domain name is accepted from those later outputs.

## 2. MANDATORY RECOVERY READ — standing rule for every new chat

Before resuming substantive DIM/Profile V2 research after a new-chat handoff, timeout, context loss, or PITON-based recovery, **reread these two documents in the repository**:

1. `DRAFT_Concept_Baseline_v0.1_25OCT2026.md`
2. `DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md`

Repository paths:

- `Docs/Research/DIM_Profile_V2/DRAFT_Concept_Baseline_v0.1_25OCT2026.md`
- `Docs/Research/DIM_Profile_V2/DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md`

These are required recovery refreshers because they preserve the careful reasoning that is easy to flatten or misremember as merely “system + sensor + equipment.”

When the immediate task concerns the native OGC/CSAPI standards environment, also reread as supporting context:

- `Docs/Research/DIM_Profile_V2/DRAFT_CSAPI_Anchor_Standards_Environment_v0.1_25OCT2026.md`

**Recovery rule:** do not rely on a compressed memory summary when these documents are available. Read them before making scope, naming, chassis, root-concept, donor-role, or profile/DIM relationship claims.

## 3. Exact meaning of the current System / Sensor / Equipment baseline

The current baseline is **not** three peer nouns casually combined into a domain label.

The sourced reasoning is layered:

- **System** is the represented subject/resource in the relevant SOSA/SSN and CSAPI conceptual environment.
- **Sensor** expresses the System's principal sensing/observing role. In CSAPI this is represented through the `systemType` facet.
- **Equipment** expresses the hardware/equipment realization of that System. In CSAPI this is represented through the separate `assetType` facet.

The present CSAPI characterization of the hardware sensing cases that motivated the work is therefore:

- `systemType = Sensor`
- `assetType = Equipment`

CSAPI deliberately permits other combinations such as Sensor + Simulation, Sensor + Human, and Platform + Equipment. The two classifications are independent semantic facets.

Accordingly:

- do **not** invent a compound class merely because `Sensor + Equipment` is meaningful;
- do **not** treat “System,” “Sensor,” and “Equipment” as three equivalent categories;
- do **not** assume that CSAPI `systemType = Sensor` is automatically identical to asserting RDF/OWL type `sosa:Sensor`;
- do **not** use “physical” as an unsourced synonym for Equipment;
- do **not** treat the current characterization as proof of the final V2 domain boundary.

## 4. Domain boundary and final name remain deliberately open

The project has intentionally resisted inventing an overarching domain name before the donor evidence earns one.

The current `System + Sensor + Equipment` shorthand is a **provisional evidence-based envelope**, not a final name and not necessarily the final scope description.

A standing research hypothesis is that the eventual accurate scoped focus may be narrower, more specific, or more conceptually coherent than that shorthand, even if the resulting DIM/Profile can accommodate many or all real systems falling under the broad words system, sensor, and equipment.

The eventual bounded subject should be discovered academically and naturally from:

- what the donor sources themselves model or standardize;
- the real-world subjects they assume;
- the structural boundaries they establish;
- the information and relationships they treat as intrinsic, contextual, dynamic, cross-cutting, or external;
- how their concepts can be reused or mapped without semantic distortion;
- what the combined donor evidence enables the resulting DIM/Profile to represent faithfully;
- and what real target systems the model can actually accommodate.

**Do not turn this hypothesis into a forced naming exercise.**

The standing question is:

> **What bounded real-world domain is increasingly revealed by the donor corpus, and what sourced concept or description—if any—best characterizes it?**

That question should remain visible during research, but the answer must emerge from evidence. It is acceptable if the eventual evidence confirms the current characterization rather than replacing it.

Also preserve the distinction:

> **What real-world problem space belongs inside the DIM?**

is not necessarily the same question as:

> **What sourced concept, if any, should serve as a central/root/anchor concept in the model?**

A coherent domain boundary does not require an invented root class.

## 5. “Whole system” is informational scope, not automatic taxonomic enlargement

The carried-forward “whole system” objective means that a user should be able to understand the sensing System as a complete operational subject rather than merely retrieve its observations.

Depending on evidence, that may include information about:

- identity and description;
- technical/product information;
- components and internal arrangement;
- capability and performance;
- configuration and modes;
- telemetry and reported state;
- deployment/emplacement;
- communications;
- power;
- condition/health;
- management interactions;
- maintenance/service/history;
- observations and derived products;
- commands/actions;
- provenance and responsibility.

This list is not a predetermined V2 module taxonomy.

SensorML supports the underlying point that a system whose overall application is sensing may contain sensing, actuation, computation, and other subprocesses while remaining a sensor system at the top level.

Therefore richer information about the subject does not by itself require a broader invented parent category.

## 6. Composition, aggregation, hosting, and context remain important sourced distinctions

CSAPI's Composition versus Aggregation distinction remains part of the early sourced baseline:

- enduring/integral subsystem relationships differ from deployment-scoped or interchangeable attachments;
- physical attachment alone is not enough to decide which relationship applies;
- a host Platform, vehicle, structure, network, or deployment context does not automatically become intrinsic composition merely because it carries, powers, connects to, or employs the sensing System.

These distinctions may help reveal the eventual domain boundary, but they should not be converted into new V2 semantics without controlled source analysis.

## 7. What Phase A actually is

Phase A was intended as a **broad structured hypothesis-generation and evidence-extraction exercise**.

Its purpose was to inspect selected donor traditions independently through a common structural lens before performing cross-source synthesis.

The controlling Phase A artifact is:

`DRAFT_DIM_Profile_V2_Anatomy_PhaseA_Independent_Extractions_v0.1_26OCT2026.md`

The frozen Phase A population contains 30 semantic lineages:

### Core structural donors — 15

C01 Asset Administration Shell  
C02 DMTF Redfish / CIM device management  
C03 IEEE 1451 / ISO 2145x  
C04 Integrated Sensor Architecture  
C05 ISO/IEC 29182 SNRA  
C06 Matter 1.3  
C07 MIMOSA  
C08 OGC API – Connected Systems  
C09 OGC SensorML 3.0  
C10 OPC UA Devices / PA-DIM  
C11 OSUS / OSUS-R  
C12 SAPIENT / BSI Flex 335  
C13 SAREF Core 4.1.1  
C14 SOSA/SSN  
C15 The Open Group SOSA

### Cross-cutting structural donors — 11

X01 I-ADOPT Framework Ontology  
X02 IETF Energy Management (EMAN)  
X03 IETF Hardware Management  
X04 IETF Interfaces / Network Topology  
X05 MIP / JC3IEDM  
X06 NIEM 6.0  
X07 NISTIR 8259A IoT Device Cybersecurity Baseline  
X08 OGC Observations, Measurements and Samples  
X09 OMA Lightweight M2M  
X10 W3C PROV  
X11 W3C Web of Things

### Specialization / operational donors — 4

S01 Bosch BME280 atomic sensor product evidence  
S02 Radiation detection / instrument family  
S03 SWEET instrument ontology  
S04 UGS operational / reference systems

All 30 extraction worksheets were mechanically completed using the common 15-field template.

**Important:** “semantic lineage” is an analytical lane. It does not automatically mean a historically proven standards lineage, direct influence chain, recognized ontology family, or independent vote.

## 8. Phase A completion does NOT mean Phase A validation

The facts carried forward from PITON v0.9 are mechanical:

- 30 unique lineage sections exist;
- 30 explicit COMPLETE markers exist;
- all required extraction fields were populated;
- no duplicate lineage IDs were present;
- the Phase A artifact reached the planned extraction coverage.

Those facts mean:

> **30/30 extraction records were completed.**

They do **not** mean:

> **30/30 extraction records are correct, validated, equally reliable, or safe to synthesize.**

The Phase A records may contain a mixture of:

1. **SOURCE-DIRECT** — statements demonstrably supported by a source;
2. **INTERPRETATION** — reasonable analytical reading of what the source is structurally doing;
3. **ABSTRACTION** — neutral terminology or framework created by the research to permit comparison;
4. **NEEDS CHECK / UNSUPPORTED** — claims that cannot presently be established from the cited evidence;
5. **WRONG / OVERREACH** — claims that go beyond, distort, or misstate the source.

During the original execution these epistemic layers were not kept sufficiently distinct. That is the principal risk that must be corrected before synthesis.

## 9. Required pre-Phase-B validation/audit gate

**Phase B must not begin until the project owner explicitly authorizes it after the Phase A validation/audit is satisfactory.**

The pre-B audit should, at minimum:

- distinguish source-direct statements from interpretation and researcher-created abstraction;
- verify material source claims against the actual donor evidence where needed;
- identify unsupported or overconfident claims;
- identify terminology invented for comparison and prevent it from being attributed back to donors;
- check whether supposedly independent convergence is actually repeated AI interpretation;
- distinguish genuine donor-to-donor alignment from common inheritance or dependency;
- identify where a “lineage” is only a convenient analytical grouping rather than a demonstrated lineage;
- preserve useful interpretations while labeling them honestly as interpretation;
- correct or quarantine errors without forcing every donor into one shared structure.

Interpretation is not forbidden. Interpretation is necessary to build a DIM. The control is:

> **Interpretation must not masquerade as source fact.**

A useful audit vocabulary is:

- SOURCE-DIRECT
- INTERPRETATION
- ABSTRACTION
- NEEDS CHECK / UNSUPPORTED
- WRONG / OVERREACH

The project owner may revise this audit method before execution.

## 10. Quarantined later artifacts

The following artifacts exist in the branch but are **not controlling V2 decisions** at this recovery point:

- `DIM_Profile_V2_Anatomy_PhaseB_Cross_Source_Comparison_v0.1_26OCT2026.md`
- `DIM_Profile_V2_Anatomy_PhaseC_Candidate_Structure_v0.1_26OCT2026.md`
- `DIM_Profile_V2_Anatomy_PhaseD_Validation_v0.1_26OCT2026.md`
- `DIM_Profile_V2_Anatomy_Validation_and_Decision_v0.1_26OCT2026.md`
- any clean-draft changes that depend on those unaccepted anatomy conclusions;
- PITON v1.0, v1.1, and v1.2 restart instructions and promoted anatomy/chassis conclusions.

Do **not** delete these artifacts. They may contain useful candidate analysis and can later be mined or compared during controlled validation.

But they are quarantined because using them as accepted truth would risk circular validation of AI-generated synthesis.

PITON v0.9 remains useful only as evidence of **mechanical Phase A completion**. Its instruction that Phase B is the next permitted task is superseded by this PITON.

## 11. Chassis/foundation research — standing meaning

“Chassis” is research shorthand, not a formal class or model element.

The chassis question was introduced to help discover:

- the bounded conceptual frame for the class of real-world thing the DIM is about;
- which donor sources are closest to defining that bounded subject;
- which donors provide broad structural foundations versus narrower semantic contributions;
- and whether the combined donor evidence reveals a more accurate domain description than the provisional System/Sensor/Equipment shorthand.

The source-type analysis suggested that **Conceptual / Information / Domain Models** deserve early attention for the chassis question because defining bounded concepts and relationships is their native job. Ontologies, reference architectures, and requirements/operational specifications then provide important semantic and boundary tests.

That search order is a research heuristic, not a conclusion.

No donor family is entitled to become the chassis merely because it is broad, familiar, normative, or already close to CSAPI.

SAPIENT, ISA, OSUS, SOSA, IEEE 1451/TEDS, OMS, SOSA/SSN, OPC UA/PA-DIM, W3C Web of Things, I-ADOPT, QUDT, SWEET, NIEM and other donor families must not silently disappear merely because they fit awkwardly into one grouping. Grouping is organizational, not evidentiary exclusion.

## 12. Governing V2 methodology that remains in force

The following controls survive this recovery correction:

- Version 1 is predecessor evidence, not design authority.
- Do not inherit the Version 1 eight information subjects as V2 modules or donor bins.
- Use established source concepts as primitives before authoring new V2-owned semantics.
- Combining sourced concepts descriptively does not create a new class.
- Donor investigation is not donor adoption.
- Conceptual reuse, semantic mapping/translation, profile specialization, concrete OGC binding, native donor implementation, and conformance claims are different things and must remain distinct.
- Individual donor reviews do not directly edit the DIM.
- Preserve source provenance and semantic ownership.
- Model for the profile, not to the profile: the intended CSAPI application profile may identify needed domain questions, but API paths, JSON layout, encoding choices, UI structure, and implementation convenience do not become intrinsic domain truth.
- Domain boundary and root/anchor concept are separate questions.
- Modularity must be earned from semantic cohesion; do not create modules merely because a topic exists.
- Reuse invariants; specialize variation.
- Every donor is allowed to challenge the emerging V2 model.
- New V2-owned semantics require demonstrated need after source evidence has been examined.

## 13. Frozen corpus / research infrastructure retained

The current V2 candidate source population remains frozen at **182 external candidate source artifacts** for the present research stage unless the project owner explicitly reopens corpus scope.

The 30-lineage anatomy population remains a useful controlled Phase A research population.

These controls remain:

- source family/provenance, primary artifact type, subject matter, and final contribution/disposition are separate axes;
- companion documents do not automatically create independent evidentiary votes;
- source type determines how a source should first be understood, not whether it may contribute useful domain structure;
- sources should first be understood on their own terms before comparison;
- document count is not the same as independent conceptual convergence.

## 14. Current safe state

The authoritative safe state is:

> **Early CSAPI/DIM conceptual baseline: retained.**  
> **Final bounded domain name/description: OPEN.**  
> **Final root/anchor concept: OPEN.**  
> **Chassis/foundation conclusion: NOT frozen as final.**  
> **Phase A extraction coverage: COMPLETE — 30/30.**  
> **Phase A epistemic/source validation: NOT COMPLETE.**  
> **Phase B cross-source synthesis: NOT STARTED / NOT AUTHORIZED.**  
> **Phase C/D and later anatomy decisions: QUARANTINED.**

## 15. Exact restart point

After recovering into a new chat:

1. read this PITON;
2. reread the two mandatory baseline documents in Section 2;
3. restore the exact System / Sensor / Equipment semantic reasoning;
4. remember that the final bounded domain focus/name must emerge from donor evidence rather than be invented;
5. inspect the Phase A extraction record only as candidate evidence;
6. continue with **Phase A validation/audit planning or execution only at the project owner's direction**;
7. do **not** begin Phase B until the owner explicitly authorizes it after the audit.

> **NEXT SAFE TASK:** validate the Phase A evidence before any cross-source comparison.

