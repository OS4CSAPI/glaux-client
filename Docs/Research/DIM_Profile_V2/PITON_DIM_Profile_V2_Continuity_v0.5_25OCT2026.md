# PITON — DIM/Profile V2 Research Continuity

**Version:** 0.5  
**Date:** 25 October 2026  
**Standing:** Continuity checkpoint immediately after chassis validation and promotion  
**Repository:** OS4CSAPI/glaux-client  
**Branch:** research/dim-profile-v2  
**Workspace:** Docs/Research/DIM_Profile_V2/

> **IMMEDIATE RESTART INSTRUCTION:** The V2 chassis study is complete. Do **not** rerun the 14-source chassis extraction, reopen the Sensor + Equipment boundary as a mere candidate, invent a new umbrella class, or treat the chassis-validation passes as complete donor reviews. Resume with the **DIM anatomy / module-discovery study** in Sections 13–16 of this PITON: recover each Conceptual / Information / Domain Model source’s own internal organization and semantic partitions, then compare those source-native structures to discover candidate V2 conceptual modules or subject areas. Do not use the Version 1 eight subjects as bins.

---

## 1. Purpose of this PITON

This PITON supersedes v0.4 as the active continuity checkpoint.

Version 0.4 stopped immediately before the first chassis-finding donor analysis. That research sequence has now been completed through all of its required gates:

1. independent chassis extraction of all fourteen Conceptual / Information / Domain Model artifacts;
2. cross-source comparison;
3. source standing within the group;
4. candidate chassis synthesis;
5. Ontology / Formal Semantic Model validation;
6. Reference Architecture / Architectural Framework validation;
7. Requirements / Capability / Operational Specification validation;
8. cross-group decision record; and
9. promotion of the earned chassis decision into the maintained clean V2 artifact.

The next research problem is therefore **not** “what kind of thing is the DIM about?” That question now has a working answer. The next problem is:

> **How do mature donor models internally organize the information needed to describe that bounded kind of sensing System, and what recurring semantic structures—if any—earn standing as V2 modules, subject areas, or cross-cutting concepts?**

The goal is to discover the DIM’s internal anatomy from source evidence without silently rebuilding Version 1.

---

## 2. Governing V2 mission and method remain unchanged

Version 2 remains a clean-slate re-examination of the sensing-system Domain Information Model and eventual CSAPI application profile.

Version 1 remains predecessor evidence, not design authority. Its goals, examples, research, failures, and useful principles may be recovered deliberately. Its names, eight information subjects, R01–R20 relationships, donor choices, profile-owned terms, and structural partitions are not inherited automatically.

The governing semantic rule remains:

> **Use established source concepts as primitives and do not invent a new name merely because a combination makes sense.**

Multiple sourced concepts may be used together descriptively without creating a new class. New V2-owned semantics require demonstrated need after donor evidence has been examined.

The research remains evidence-first:

- donor investigation is not adoption;
- conceptual reuse is not donor-standard implementation;
- semantic mapping is not conformance;
- profile specialization is not the same as native donor implementation;
- an OGC binding is a realization of selected meanings, not domain truth; and
- individual donor reviews do not directly edit the clean DIM.

Evidence is extracted first and synthesized only at explicit gates.

---

## 3. Chassis study — completed working decision

The completed study establishes the following working domain boundary:

> **Version 2 concerns physically realized equipment Systems whose defining operational role is sensing/observing, modeled as complete operational subjects.**

This is a **boundary statement**, not a new V2-owned class.

In the intended CSAPI environment, the most direct current characterization is:

- `systemType = Sensor`
- `assetType = Equipment`

This combination is no longer merely the comparison baseline from early V2 work. It has survived independent challenge across the required source groups and is now the **working V2 chassis characterization**.

Do not regress it to “candidate” unless later evidence actually contradicts it.

---

## 4. No new chassis class or umbrella term was earned

The study did not identify one donor term that more faithfully captures both the sensing role and the physical realization.

Rejected as universal chassis terms:

- **Asset** — too semantically variable across donor communities.
- **Device** — strong physical-equipment concept but functionally neutral and too narrow for some composite installations.
- **Thing** — deliberately physical-or-virtual and domain-neutral in WoT.
- **Sensor Network** — legitimate larger aggregate, not the ordinary individual V2 System boundary.
- **Observation / Observer** — observation-process semantics do not replace the complete enduring equipment subject.
- **Managed Physical Sensing System** or similar compound terms — no source evidence justifies reviving or inventing such a V2 class merely for tidiness.

“Sensor Systems” may continue as descriptive working wording. It is not a newly authored class.

---

## 5. Earned chassis-level boundary rules

The cross-group study established the following working rules.

### 5.1 Complete operational subject

The subject is the enduring sensing System/equipment itself, not merely an Observation, transducer, API endpoint, deployment record, software service, interface participant, or digital representation.

### 5.2 Composite physical realization

One sensing System need not equal one box or one Device.

The Open Group SOSA Edition 1.1 explicitly permits one Sensor to contain multiple hardware elements and allows those elements to be grouped or distributed at different locations on/in one Host Platform.

The realization facet therefore remains **Equipment**, potentially composite equipment.

### 5.3 Heterogeneous internal components

A sensing System may contain sensing elements plus processors, software, firmware, communications, storage, power, apertures, chassis, run-time infrastructure, actuators/effectors, management functions, BIT/diagnostics, and other supporting components.

Internal heterogeneity does not destroy the sensing identity of the whole.

### 5.4 Sensing need not be exclusive

The System may execute commands, actuate/effect, process, communicate, identify/classify, configure itself, report status, or perform other functions.

Membership depends on the **defining operational role of the whole System**, not functional purity.

### 5.5 Host Platform is distinct from intrinsic composition

A vehicle, building, pod, structure, mast, or other Host Platform does not become part of the Sensor merely because it carries, powers, connects to, or deploys it.

A tighter relationship requires evidence of enduring composition.

### 5.6 Network/aggregation is a distinct larger level

A sensor network, deployment grouping, or collection of cooperating Systems is not automatically one sensing System.

Evidence of one enduring System identity/composition boundary is required before collapsing multiple Systems into one.

### 5.7 Form factor does not define membership

The operational evidence includes handheld, portable, mobile, mounted, fixed, installed, and multi-element systems.

### 5.8 Virtual/interface identity does not prove physical realization

ISA permits virtual components with configuration, state, observations, and commands. Network-visible behavior alone cannot satisfy the V2 Equipment boundary.

---

## 6. Critical formal-semantic caution

The working chassis decision does **not** mean that CSAPI classification and OWL typing are automatically equivalent.

Current SOSA/SSN permits:

- broad `sosa:System`;
- `sosa:Sensor` as a System implementing an ObservingProcedure; and
- complex packages represented as an overall System containing Sensor subsystems.

CSAPI `systemType = Sensor`, by contrast, classifies a represented System by its principal activity.

Therefore:

> **Do not automatically translate `systemType = Sensor` into RDF type `sosa:Sensor`.**

The eventual ontology alignment/binding must make that mapping explicit and defensible.

This caution does not reopen the chassis boundary.

---

## 7. Chassis source standing

The chassis study produced the following relative standing only after all fourteen CIDM artifacts had been independently characterized.

### Foundational chassis evidence

- **The Open Group SOSA DSDM / Technical Standard** — strongest evidence for Sensor as the complete operational subject with Components, state, configuration, management, and distinct Host Platform.
- **OPC UA Part 100: Devices** — strongest generic physical Device/equipment frame.
- **MIMOSA CCOM** — strongest whole physical-asset lifecycle frame.
- **OSUS-R Asset model** — strongest motivating-domain whole physical-device corroboration.

### Supplemental chassis evidence

- AAS Part 1.
- ISO/IEC 29182-4 SNRA Entity Models.
- PA-DIM.

### Specialized/gap-filling chassis evidence

- IEEE 1451.1-1999 / ISO/IEC/IEEE 21451-1:2010 — one NCAP conceptual lineage.
- RFC 7326.

### Cross-cutting/non-chassis within this question

- OGC OMS 3.0.
- NIEM 6.0.
- W3C PROV-DM.
- JC3IEDM 3.1.4 as broad operational context rather than chassis.

These standings are **only for the chassis question**. A source that was cross-cutting for chassis may become highly important to a later DIM subject such as provenance, observation, operational context, or exchange semantics.

---

## 8. Cross-group validation results

### Ontology / Formal Semantic Model validation

The candidate survived.

Key result: donor ontologies encode the sensing-role/physical-realization intersection in different legitimate ways.

- SOSA/SSN keeps Sensor broad enough for non-physical realizations.
- SAREF makes Sensor a tangible Device.
- SWEET makes Sensor both a SOSA Sensor and an Instrument under Equipment.

This diversity supports keeping the two dimensions explicit rather than inventing one V2 class.

### Reference Architecture validation

The candidate survived and was strengthened.

Key results:

- SOSA explicitly bounds the whole Sensor.
- One Sensor may contain multiple/distributed hardware elements.
- Host Platform is separate.
- Internal hardware/software/firmware/infrastructure may be heterogeneous.
- SNRA confirms the sensor network as a distinct larger architectural level.
- WoT Thing is too generic and intentionally leaves domain vocabularies external.
- OSA-CBM is a functional maintenance architecture, not a chassis.
- NCDF is a metadata framework and was non-applicable to the chassis despite its source-type placement.

### Requirements / Capability / Operational validation

The candidate survived.

Key results:

- ISA components can expose observables, properties, and commands and can be virtual.
- Interface/component identity is not physical-realization identity.
- NIST IoT device semantics corroborate whole-device identity but are functionally too broad because sensor or actuator can satisfy the transducer criterion.
- Radiation operational standards/guidance confirm fixed, portable, mobile, installed, and multi-element detection equipment as coherent whole subjects.

---

## 9. Frozen corpus and source-type stack remain unchanged

The external candidate corpus remains frozen at **182 sources**.

Control rule remains:

> **182 sources in → 182 sources out, exactly once each in the neutral bibliography.**

Do not expand the corpus merely because a reviewed source cites another dependency.

The established source/artifact-type stack remains a **comparison/analysis aid**, not a predetermined DIM structure:

1. governance and construction;
2. semantic foundation;
3. conceptual/domain definition;
4. architecture and requirements;
5. specialization;
6. concrete representation;
7. interaction/service behavior;
8. executable verification/realization;
9. interpretation/reality check.

The chassis study used multiple stack layers narrowly to test one boundary decision. Those passes did **not** exhaust the donors’ possible contributions to later DIM content.

---

## 10. Maintained clean V2 artifact — current state

The maintained clean artifact remains:

`Docs/Research/DIM_Profile_V2/Sensor_Systems_DIM_and_Profile_V2_Working_Draft_v0.1_25OCT2026.md`

It has now been updated with the earned chassis decision.

The clean artifact now records:

- the DIM definition and methodological basis;
- purpose-driven but binding-independent relationship to the profile;
- nine V2 objectives/design principles;
- the working chassis boundary;
- `Sensor + Equipment` as the working CSAPI chassis characterization;
- no new umbrella/root class;
- composite-equipment realization;
- heterogeneous internal components;
- non-exclusive sensing role;
- Host Platform separation;
- network/aggregation distinction;
- CSAPI classification vs OWL assertion caution;
- enduring Composition vs deployment-scoped Aggregation;
- modularity/reuse rules;
- V1 eight subjects as predecessor evidence only;
- updated decision/open-question table; and
- a post-chassis development sequence.

Do not rewrite the clean artifact with the full research narrative. The evidence belongs in the dedicated research records.

---

## 11. Chassis research artifact chain

The authoritative research chain for the chassis decision is:

1. `DRAFT_DIM_Profile_V2_Chassis_Study_Phase_A_v0.1_25OCT2026.md`
   - independent extraction of all fourteen CIDM artifacts;
   - same 15-field template;
   - no ranking.

2. `DRAFT_DIM_Profile_V2_Chassis_Study_Phases_B-D_v0.1_25OCT2026.md`
   - cross-source comparison;
   - relative standing;
   - initial candidate synthesis.

3. `DRAFT_DIM_Profile_V2_Chassis_Validation_Ontologies_v0.1_25OCT2026.md`
   - ontology/formal-semantic validation;
   - role/realization intersection;
   - CSAPI-vs-OWL caution.

4. `DRAFT_DIM_Profile_V2_Chassis_Validation_Architectures_v0.1_25OCT2026.md`
   - composite/distributed hardware;
   - Host Platform boundary;
   - sensor-network distinction.

5. `DRAFT_DIM_Profile_V2_Chassis_Validation_Requirements_v0.1_25OCT2026.md`
   - real-system operational stress test;
   - virtual/interface vs physical identity;
   - fixed/mobile/portable equipment.

6. `DIM_Profile_V2_Chassis_Cross_Group_Validation_and_Decision_v0.1_25OCT2026.md`
   - integrated decision;
   - promotion gate;
   - explicit non-decisions.

Do not reconstruct the chassis conclusion from memory when these records are available.

---

## 12. Important provenance/evidence notes carried forward

### OSUS-R pinned revision

The frozen bibliography cites the OSUS-R artifact as 2026, but pinned revision `d09088fbe56d4b64f0544d72e98c3cb70fa941f6` resolves to a **22 February 2023** commit.

Do not silently rewrite the frozen bibliography while researching. Preserve the discrepancy as provenance evidence to reconcile during bibliography maintenance.

### MIMOSA CCOM release metadata

The frozen bibliography carries inherited dating for the CCOM 4.1.0 / 4.1.0-RC1 package, while the official MIMOSA release page identifies 4.1.0-RC1 as a Release Candidate dated **20 March 2020**.

Again, preserve the frozen citation until bibliography reconciliation is explicitly undertaken.

### SOSA S251 evidence ceiling

The Edition 2.0 Snapshot 3 bundle exists in project history, but raw-byte retrieval was unavailable during the architecture validation pass. No new clause-level S251 claim was introduced. C239 Edition 1.1 supplied the fully inspectable architectural boundary evidence.

---

# 13. Next research problem — discover the DIM’s internal anatomy

The chassis answers **what kind of thing the DIM is about**. It does not answer **how the information about that thing should be conceptually organized**.

The immediate next question is:

> **How do the Conceptual / Information / Domain Model donors themselves partition and organize the information about their modeled subject, and what recurring semantic clusters or relationship structures emerge across those donors without imposing the Version 1 eight-subject scheme?**

This is a new extraction question. It must not be answered by reusing the chassis template or by converting V1 headings into donor bins.

The objective is to discover candidate semantic cohesion from donor-native structures.

“Module,” “subject area,” “subdomain,” “package,” and similar terms are not assumed to be interchangeable. The source’s own organization should be recorded first; V2 terminology comes only at synthesis.

---

# 14. DIM anatomy study — Phase A extraction method

Begin with the **same fourteen Conceptual / Information / Domain Model artifacts** because this source type is still the group most directly capable of revealing model structure. The chassis study already established relative chassis standing, so alphabetical neutrality is no longer required as a protection against premature chassis ranking; however, every artifact must still receive the same extraction before structural synthesis.

For each source, extract independently:

1. **Source-native structural organization**
   - What packages, modules, views, domains, aspects, classes of information, or major partitions does the source itself define?

2. **Purpose of each partition**
   - What semantic problem does each source-native partition solve?

3. **Central entities/concepts per partition**
   - Which concepts carry the partition?

4. **Primary relationships**
   - What relationships make the partition internally coherent?

5. **Dependency boundaries**
   - What other partitions/concepts must it depend on?
   - Can it be understood or reused independently?

6. **Intrinsic vs contextual standing**
   - Does the source treat the information as intrinsic to the modeled subject, as external context, as an interaction, as an output/result, or as cross-cutting metadata?

7. **Cross-cutting concepts**
   - Which concepts intentionally span multiple partitions rather than belonging to one?

8. **State / temporal / lifecycle organization**
   - How does the source organize change over time, if at all?
   - Record source-native structure; do not force a “lifecycle” category if the donor does not use one.

9. **Composition/topology organization**
   - How does the source organize constituents, hosting, grouping, hierarchy, or topology?

10. **Capability/function/behavior organization**
    - How does the source represent what the subject can do versus what it is?

11. **Information/output organization**
    - How does the source organize observations, measurements, products, events, messages, records, or other outputs when applicable?

12. **Management/condition organization**
    - Record only if the source itself establishes such a coherent area; do not preload Version 1 categories.

13. **Provenance/identity/reference organization**
    - Again, source-native only.

14. **Semantic invariants**
    - Which distinctions appear fundamental enough that collapsing them would damage the source’s meaning?

15. **Potential V2 structural contribution**
    - Evidence label only at first:
      - likely core/intrinsic;
      - likely reusable module;
      - likely contextual relationship;
      - likely cross-cutting;
      - specialization/domain-specific;
      - binding/representation concern rather than DIM structure;
      - not applicable.

Do **not** immediately name V2 modules from one donor.

---

# 15. DIM anatomy study — comparison and synthesis gates

## Phase A — independent source-native anatomy extraction

Review all fourteen CIDM artifacts under the Section 14 template.

Do not update the clean DIM during individual extractions.

## Phase B — cross-source structural comparison

Compare only after all fourteen are extracted:

- recurring semantic clusters;
- equivalent or conflicting partitions;
- recurring relationships;
- intrinsic vs contextual distinctions;
- cross-cutting concepts;
- functional vs physical vs informational partitions;
- common dependency patterns;
- lifecycle/state structures;
- source lineage that explains apparent convergence;
- specialized structures that should remain specializations; and
- gaps where no source provides a coherent organization.

## Phase C — candidate V2 structural propositions

Only after comparison may V2 propose candidate:

- core concepts;
- modules/subdomains;
- cross-cutting semantics;
- contextual relationship sets;
- specializations; or
- concepts that should remain donor-specific.

Every candidate must state **why it is semantically cohesive** and **which source evidence owns/supports it**.

## Phase D — cross-group structural validation

Candidate V2 modules/partitions must then be challenged against:

1. Ontologies / Formal Semantic Models;
2. Reference Architectures / Architectural Frameworks;
3. Requirements / Capability / Operational Specifications;
4. relevant vocabularies/data models/interfaces as needed for the specific proposition.

These validation passes are **new structural reviews**, not a reuse of the narrow chassis conclusions.

Only after validation may a candidate module/subject structure be promoted into the clean V2 artifact.

---

# 16. Stop rules for the next chat

The next chat must **not**:

- rerun the chassis study as though it were incomplete;
- downgrade `Sensor + Equipment` back to a mere untested candidate;
- invent a new umbrella/root class without contradictory new evidence;
- equate CSAPI `systemType = Sensor` with OWL `sosa:Sensor` automatically;
- narrow Equipment to one Device or one enclosure;
- absorb Host Platform merely because it physically carries the Sensor;
- treat a sensor network or deployment grouping as one System by default;
- rebuild the Version 1 eight subjects as extraction categories;
- assume the chassis artifact-type reviews were complete donor reviews;
- expand the frozen 182-source corpus without explicit owner direction;
- update the clean DIM during individual anatomy extraction;
- convert source presentation headings into V2 modules without semantic-cohesion evidence;
- treat every recurring topic as a module;
- force every donor to contribute to every structural question;
- infer donor-standard conformance from conceptual reuse/mapping; or
- restart visualization remediation unless explicitly requested.

If a source has no meaningful internal organization relevant to the anatomy question, record that honestly and continue.

---

## 17. Current artifact status matrix

| Topic | Standing | Current result |
| --- | --- | --- |
| DIM terminology/method | Working decision | Domain Information Model; implementation- and protocol-independent. |
| DIM/profile relationship | Working decision | Purpose-driven but binding-independent; model for the profile, not to the profile. |
| Whole-system meaning | Working decision | Complete operational subject; internal heterogeneity allowed. |
| Chassis/domain boundary | **Working decision** | Physically realized equipment Systems whose defining role is sensing/observing. |
| CSAPI chassis characterization | **Working decision** | `systemType = Sensor` + `assetType = Equipment`. |
| New umbrella/root class | Not adopted | No source-supported need. |
| Equipment vs Device | Working decision | Equipment retained; may be composite/multi-element. |
| Host Platform boundary | Working decision | Host is external context unless enduring composition is established. |
| Network/aggregation boundary | Working decision | Not automatically one System. |
| CSAPI vs OWL Sensor mapping | Open | Explicit semantic mapping required later. |
| Chassis study | **Complete** | CIDM + ontology + architecture + requirements validation completed and promoted. |
| Final DIM modules/subdomains | **Open / immediate research target** | Discover through source-native anatomy extraction and synthesis. |
| V1 eight subjects | Predecessor evidence only | Not V2 structural bins. |
| Source corpus | Frozen | 182 external candidates. |
| Visualization | Paused / non-gating | Resume only if explicitly needed. |

---

## 18. Exact restart sequence

When this work resumes in a new chat:

1. Read this PITON first.
2. Treat the chassis decision as a current working decision, not an open starting question.
3. Read the clean V2 artifact only as needed to recover the promoted boundary and current open questions.
4. Read the chassis decision record if the evidence/rationale behind the boundary is needed.
5. Use the existing fourteen-source CIDM population from the source-type audit; do not reconstruct or expand it.
6. Begin **DIM anatomy Phase A** using the Section 14 source-native extraction template.
7. Preserve each donor’s own partitions/terms before translating anything into V2 language.
8. Do not use the Version 1 eight subjects as bins.
9. Do not modify the clean DIM during individual source extraction.
10. After all fourteen anatomy extractions are complete, perform the Phase B structural comparison.
11. Only then propose candidate V2 modules/subject areas/cross-cutting structures.
12. Validate any candidate structure across the relevant ontology, architecture, requirements, and other source groups before promotion.

The first substantive question in the next chat is therefore:

> **Across the fourteen Conceptual / Information / Domain Model artifacts, how does each source internally organize the information about its modeled subject, and what recurring source-native semantic structures—if any—should become candidates for the internal anatomy of the V2 DIM?**
