# PITON — DIM/Profile V2 Research Continuity

**Version:** 0.6  
**Date:** 25 October 2026  
**Standing:** Post-reconciliation continuity checkpoint  
**Repository:** OS4CSAPI/glaux-client  
**Branch:** research/dim-profile-v2  
**Workspace:** Docs/Research/DIM_Profile_V2/

> **RESTART INSTRUCTION:** The V2 chassis is a working decision after a complete 182-source capability audit. Do not rerun the chassis study or regress the boundary to an untested candidate unless genuinely contradictory evidence appears. The immediate next gate is to establish the DIM-anatomy evidence population by **structural semantic capability**, not by primary source type.

## 1. Why this supersedes v0.5

PITON v0.5 was written after the original chassis study. A later methodological review found that primary document classification had been used too strongly as an eligibility gate. Some artifacts whose main purpose is interface, schema, management, or representation also contain substantive domain boundaries and structural models.

The correction is permanent:

> **Source type determines how a source should first be understood; it does not determine whether that source is allowed to challenge a domain boundary or structural proposition.**

A bounded audit was then performed across the complete frozen corpus.

## 2. Corpus audit standing

The frozen corpus remains **182 sources**.

Authoritative ledger:

`DIM_Profile_V2_Chassis_Capability_Audit_182_Source_Ledger_v0.1_25OCT2026.csv`

Authoritative reconciliation narrative:

`DIM_Profile_V2_Chassis_Corpus_Wide_Reconciliation_v0.1_25OCT2026.md`

Accounting:

- 38 already explicitly chassis-tested;
- 13 previously under-contested artifacts explicitly reconciled;
- 101 lineage/companion/specialized artifacts retained without independent conceptual weight;
- 24 artifacts with no credible chassis potential;
- 6 operational/reference falsifiers.

**Control total: 182.**

## 3. Reconciled chassis decision

The full-corpus reconciliation did not overturn the boundary.

The V2 DIM remains bounded around:

> **physically realized equipment Systems whose defining operational role is sensing/observing, modeled as complete operational subjects.**

For the intended CSAPI application profile, the working characterization remains:

- `systemType = Sensor`
- `assetType = Equipment`

No new umbrella/root class is adopted.

## 4. Guardrails added by reconciliation

1. Source type is never an eligibility gate for a domain-boundary challenge.
2. `Equipment` is intentionally broader than any one donor's device/node/container/concrete physical-process class.
3. Network-visible or registered identity can differ from physical System identity.
4. Physical composition and domain membership are separate questions.
5. Concrete SensorML class selection is a later binding/model decision, not the chassis.
6. Internal members may be exposed, hidden, aggregated, or represented through another participant; representation visibility is not identical to physical composition.
7. Domain-specific device/instrument classes remain specializations unless cross-domain evidence supports promotion.
8. Companion schemas, APIs, tests, and guidance do not count as independent conceptual agreement.
9. Do not automatically equate CSAPI `systemType = Sensor` with RDF/OWL type `sosa:Sensor`.

## 5. Maintained clean V2 artifact

Current clean artifact:

`Sensor_Systems_DIM_and_Profile_V2_Working_Draft_v0.1_25OCT2026.md`

It now records that the chassis is **corpus-wide reconciled**.

The clean artifact contains the promoted decision only. Detailed evidence remains in the research records.

## 6. Authoritative chassis chain

1. `DRAFT_DIM_Profile_V2_Chassis_Study_Phase_A_v0.1_25OCT2026.md`
2. `DRAFT_DIM_Profile_V2_Chassis_Study_Phases_B-D_v0.1_25OCT2026.md`
3. `DRAFT_DIM_Profile_V2_Chassis_Validation_Ontologies_v0.1_25OCT2026.md`
4. `DRAFT_DIM_Profile_V2_Chassis_Validation_Architectures_v0.1_25OCT2026.md`
5. `DRAFT_DIM_Profile_V2_Chassis_Validation_Requirements_v0.1_25OCT2026.md`
6. `DIM_Profile_V2_Chassis_Cross_Group_Validation_and_Decision_v0.1_25OCT2026.md`
7. `DIM_Profile_V2_Chassis_Capability_Audit_182_Source_Ledger_v0.1_25OCT2026.csv`
8. `DIM_Profile_V2_Chassis_Corpus_Wide_Reconciliation_v0.1_25OCT2026.md`

Items 7–8 correct the source-type eligibility blind spot and control the current standing.

## 7. Next research problem: DIM anatomy

The chassis answers what kind of thing the DIM is about.

The next problem is:

> **How should information about that bounded System be conceptually organized?**

The v0.5 instruction to use only the original fourteen Conceptual / Information / Domain Model artifacts as the anatomy population is superseded.

The anatomy population must be selected by **structural semantic capability across the frozen corpus**.

The fourteen CIDM artifacts remain a high-value core population, but they are not an exclusive gate.

## 8. Anatomy Phase 0 — freeze the structural evidence population

Before detailed anatomy extraction:

1. Start from the 182-source audit ledger.
2. Identify semantic lineages that define meaningful internal organization of the bounded System or a closely related domain subject.
3. Group companion artifacts under one semantic lineage.
4. Classify candidate lineages as:
   - core structural donor;
   - cross-cutting structural donor;
   - specialization donor;
   - representation-only companion;
   - non-structural.
5. Freeze the anatomy evidence population before source-by-source extraction.

The reconciliation report identifies the cross-type lineages that must at minimum be considered during this gate.

## 9. Anatomy Phase A — source-native extraction

For every lineage admitted to the frozen anatomy population, extract independently:

1. source-native structural organization;
2. purpose of each partition;
3. central concepts per partition;
4. primary relationships;
5. dependency boundaries;
6. intrinsic vs contextual standing;
7. cross-cutting concepts;
8. state/temporal organization;
9. composition/topology organization;
10. capability/function/behavior organization;
11. information/output organization;
12. management/condition organization where source-native;
13. provenance/identity/reference organization where source-native;
14. semantic invariants that would be damaged by collapsing distinctions;
15. potential V2 structural contribution.

Do not update the clean DIM during individual extraction.

## 10. Synthesis gates

### Phase B — cross-source comparison

Compare only after every lineage in the frozen anatomy population has been independently extracted.

### Phase C — candidate V2 anatomy

Only then propose candidate core concepts, modules/subdomains, cross-cutting semantics, contextual relationships, or specializations.

Every candidate must identify the semantic cohesion and supporting sources.

### Phase D — validation

Challenge every proposed structure across relevant source types. Primary type may organize the order but may not exclude a challenger.

Only after validation may structure be promoted into the clean V2 artifact.

## 11. Stop rules

Do not:

- reopen the chassis merely because a donor uses a different noun;
- regress `Sensor + Equipment` to an untested candidate;
- invent a new umbrella/root class without contradictory evidence;
- narrow Equipment to one donor's concrete class;
- assume network/interface identity equals physical System identity;
- use source type as an eligibility gate;
- use the Version 1 eight subjects as anatomy bins;
- begin anatomy extraction before the structural population is frozen;
- count companion documents as independent conceptual agreement;
- update the clean DIM during individual source extraction;
- infer donor conformance from reuse or mapping; or
- resume visualization unless explicitly required.

## 12. Status matrix

| Topic | Standing |
| --- | --- |
| Frozen corpus | 182 sources |
| Chassis capability audit | **Complete: 182/182** |
| Source-type eligibility gap | **Reconciled** |
| V2 chassis | **Working decision, corpus-wide reconciled** |
| CSAPI characterization | `Sensor + Equipment` |
| New umbrella/root class | Not adopted |
| Formal ontology mapping | Open |
| DIM anatomy evidence population | **Open / immediate next gate** |
| DIM modules/subdomains | Open |
| V1 eight subjects | Predecessor evidence only |
| Visualization | Paused / non-gating |

## 13. Exact restart sequence

1. Read this PITON first.
2. Treat the chassis as corpus-wide reconciled.
3. Read the audit ledger/reconciliation record if source coverage is questioned.
4. Do not return automatically to the original fourteen-source anatomy population.
5. Perform Anatomy Phase 0 and freeze the structural evidence population across the 182-source corpus.
6. Preserve semantic lineages and avoid double-counting companions.
7. Perform source-native anatomy extraction only after the population is frozen.
8. Synthesize only after all admitted lineages are extracted.
9. Validate before clean-DIM promotion.

The first substantive question on restart is:

> **Which semantic lineages in the frozen 182-source corpus actually define enough internal organization to participate in discovering the anatomy of the V2 DIM, regardless of their primary document type?**
