# 06 — Model currency and experiment audit

**Status:** corrective audit completed before Phase 5. The Smart Citizen source specimen remains valid, but the Phase 3/4 semantic design has been rechecked against the **actual MPSS v0.3.5 technical baseline** and the later research corpus rather than against the older v0.3-era source-selection summary. Phase 5 remains blocked until the corrections identified here are reflected in the mapping ledger, resource graph, paper, and decision log.

## 1. Why this audit exists

The experiment was intentionally designed to test the MERLIN domain information model (DIM) and Managed Physical Sensing Systems (MPSS) profile against a real source. During the paper v0.9 architecture rewrite, an earlier source-selection table was mistakenly summarized as though it represented the complete current research program. That summary omitted or flattened later bounded donor studies including Army ISA, SAPIENT v2, The Open Group SOSA, IEEE 1451/TEDS, OMS 3.0, SOSA/SSN, I-ADOPT, QUDT, SWEET, and later OSCAR stress-test work.

That paper defect raised a legitimate experiment-control question: **were Phases 1–4 themselves based on obsolete research, or was the error mainly in the paper's description of the model?** This audit answers that question by tracing the experiment to the current accepted technical baseline and then separately checking later research that was not automatically incorporated into the profile.

## 2. Authority and currency model

The experiment now distinguishes three different kinds of authority.

| Layer | Controlling material | What it controls | What it does not control |
| --- | --- | --- | --- |
| Native Smart Citizen evidence | Frozen specimen `20261025T024348Z`, source documentation, inspected Smart Citizen API implementation | What the source actually reports; source identifiers, values, units, times, aggregation behavior and limitations | MERLIN domain semantics or target-server representation |
| Accepted MPSS technical baseline | `MERLIN_Managed_Physical_Sensing_Systems_Profile_Integrated_Binding_Draft_v0.3.5_17OCT2026.docx` plus its accepted catalogue/example | Current owner-approved R01-R20 meanings and OGC/SensorML/SWE binding rules used by this experiment | Every later research recommendation or unresolved donor question |
| Wider research corpus | Current DIM bibliography/source register; Power, ISA, SAPIENT, The Open Group SOSA, IEEE 1451/TEDS, foundational semantics/OMS/I-ADOPT/QUDT/SWEET, OSCAR and related studies | Evidence that can reinforce, challenge, refine or expose gaps in the accepted profile | A technical profile change unless the change was explicitly dispositioned and accepted |

The current technical baseline is **not** the original v0.3 profile. MPSS v0.3.5 states that it incorporates **four owner-approved bounded increments** and that its accepted guidance draws on completed Power, ISA, SAPIENT and OMS findings. Its changed R01/R02/R04/R09-R12/R15-R17/R20 text also explicitly contains later-donor distinctions, including SAPIENT sender versus physical identity, ISA mediation versus composition, The Open Group SOSA physical/logical scope, SAPIENT mode-scoped capability, RFC 7326 energy relationships, OMS observational-versus-administrative distinctions, and refined subject/lineage handling.

The wider research corpus remains larger than v0.3.5. In particular, exact IEEE 1451 normative obligations remain access-gated; some cross-donor lineage and prospective-capability questions remain residual; and the 22 October OSCAR stress test identified candidate common-model improvements around artifacts, processing execution/derivation provenance and operational context. Those findings are **research evidence**, not silently accepted v0.3.5 rules.

## 3. Phase-by-phase audit

### Phase 1 — frozen source specimen

**Disposition: RETAIN.**

Phase 1 is source acquisition, not a DIM/profile interpretation. The exact public Device response, history responses, request metadata and hashes remain valid evidence regardless of later model refinement. No donor/model revision changes what Smart Citizen returned on 25 October 2026.

### Phase 2 — native source characterization

**Disposition: RETAIN.**

Phase 2 distinguishes source identifiers, catalogue relationships, current values, source times, notification preferences, location precision, source processing and history-query semantics. Those are source-characterization findings. Later donor research can affect how those facts are represented, but does not invalidate the characterization itself.

The Phase 2 corrections are also consistent with later accepted MPSS guidance: source registration/sender identity is not automatically physical identity; logical/catalogue dependency is not automatically physical composition; declared/status fields cannot be promoted to readiness; and source-processing provenance must remain distinguishable.

### Phase 3 — mapping ledger

**Disposition: RETAIN CORE SEMANTICS; REPAIR CURRENT-DONOR TRACEABILITY AND SELECTED CARRIERS.**

The Phase 3 mappings used MPSS v0.3.5 as their stated technical baseline, so they were not designed against the original v0.3 rules. However, several mapping narratives explain their lineage mainly through the older donor set and therefore under-document later accepted/research influences. That documentation gap is real even where the mapping result itself remains correct.

The mapping-specific dispositions are below.

| Mapping(s) | Current accepted-profile check | Later-research check | Audit disposition |
| --- | --- | --- | --- |
| SC-ID-01 | R01 distinguishes System instance from reusable model; v0.3.5 adds SAPIENT/ISA-informed rule that native sender/registration identity is not automatically physical System identity; R15 defines optional representation-source provenance | The Open Group SOSA and ISA reinforce physical/logical/mediation distinctions | **RETAIN semantic decision; REFINE mapping and Phase 4 carrier to use R15 representation-source provenance** |
| SC-TEMP-01, SC-PM25-01, SC-HUM-01, SC-PRESS-01, SC-NOISE-01 | R10 keeps declared products distinct from exposed streams; R11 preserves producer, observed subject and observation context and forbids inventing a SamplingFeature | SOSA/SSN, OMS and foundational-semantics work reinforce System/Procedure/Feature/Property/Result distinctions; I-ADOPT/QUDT/SWEET are optional semantic resources, not mandatory runtimes | **RETAIN**; source-provided property/unit definitions remain valid where sufficiently precise |
| SC-BATT-01 | R17 requires explicit subject/property/unit/time and forbids inferring battery identity/topology; R16 requires evidence for power relationships | Power research and foundational semantics reinforce the decision; SAPIENT was explicitly rejected as whole-system power model | **RETAIN**; no battery System or R16 edge without source evidence |
| SC-RSSI-01 | R13 requires an identified communications interface before interface state can be asserted; R11 requires the true observed subject | Later research does not establish an interface from Smart Citizen RSSI alone | **RETAIN** untyped DataStream/no invented interface or link |
| SC-SD-01 | R11 subject discipline and R20 observational-versus-administrative discipline prevent a source code from becoming generic health/readiness | OMS/foundational semantics reinforce the restriction | **RETAIN** categorical source status; do not manufacture Boolean health |
| SC-TEMP-AGG-01, SC-PM25-AGG-01 | CSAPI permits a System with assetType=Process; Part 2 defines Sensor broadly enough to include software responding to prior observation results; a reusable Procedure is distinct from the System that implements it | OSCAR later research correctly warns that reusable Procedure, persistent software/process implementation and one execution/derivation activity are different concepts | **RETAIN 2-System/2-Procedure design WITH CLARIFICATION:** SC-SYS-PROC-001 is the persistent study representation of the data-transforming source-platform process, **not one query execution**; SC-PROC-AGG-001 is the reusable method; the frozen HTTP query/response is retained as execution/provenance evidence and no common ProcessingExecution resource is invented |
| Aggregate derived-property definitions | v0.3.5 permits qualified Property/DerivedProperty semantics and SWE definition URIs; current target need not materialize a Property resource | I-ADOPT/QUDT foundational work supports qualified reusable variable definitions when a generic base property is insufficient, without requiring an ontology runtime | **RETAIN WITH CLARIFICATION:** authored aggregate definitions explicitly mean one-hour mean of the named base property under the documented procedure; they are MERLIN experiment definitions, not I-ADOPT/QUDT conformance claims |
| Current/aggregate time policies | CSAPI requires phenomenonTime and resultTime; source supplies fewer distinctions than the target model | Later donor work does not provide missing Smart Citizen timestamps | **RETAIN AS EXPLICIT EXPERIMENT-AUTHORED PROJECTIONS**, never source-native facts |

## 4. Phase 4 resource-graph audit

### 4.1 Resource count

**Disposition: RETAIN after corrections below.**

The reviewed first-load graph remains defensible as:

- 2 Systems;
- 2 Procedures;
- 10 DataStreams;
- 10 observation schemas; and
- 56 Observations.

No later accepted/current research establishes a missing Smart Citizen Deployment, SamplingFeature, battery System, Wi-Fi interface System, SD-card System or installed transducer component identity from the frozen evidence. The negative-resource decisions therefore remain important evidence-backed outcomes.

### 4.2 Required correction: representation-source provenance on SC-SYS-001

The current Phase 4 graph says the Smart Citizen Device ID/UUID remain source identifiers/provenance but does not actually invoke the v0.3.5 R15 **representation-source** mechanism. That is a carrier-level omission.

**Corrective design:** SC-SYS-001 shall include the applicable MPSS representation-source group identifying the Smart Citizen source entity/specification and the MERLIN adapter that produces the OGC representation. The group is provenance about where the representation came from; it does not change physical System identity, create a gateway, or imply native Smart Citizen conformance.

Exact source fields and code-space values must come from the v0.3.5 catalogue and the frozen/source evidence. Phase 5 may not invent new representation-source terms.

### 4.3 Required clarification: aggregate process versus execution

SC-SYS-PROC-001 is retained, but its meaning is narrowed.

- **SC-SYS-PROC-001:** persistent study representation of the Smart Citizen data-transforming aggregation process/service; CSAPI System with assetType=Process. A Sensor semantic role is defensible because CSAPI's Sensor definition includes software that responds to input data composed from prior Observation results and generates a Result.
- **SC-PROC-AGG-001:** reusable one-hour-average computational/observing Procedure.
- **One frozen history request/response:** evidence of a particular integration acquisition/execution context, not a newly minted common model resource.

This resolves the later OSCAR processing-execution warning without pretending that MPSS v0.3.5 already defines a universal execution/derivation resource. If later common-model work adopts a formal ProcessingExecution concept, that can be tested in a future revision without rewriting the source evidence.

### 4.4 Required clarification: authored aggregate property definitions

The aggregate-property definitions remain local authored semantic identifiers for:
- one-hour mean air temperature; and
- one-hour mean PM2.5 mass concentration.

Each definition must state:
- its base observed property;
- the statistical/aggregation qualification;
- the source aggregation procedure;
- the unit; and
- its MERLIN experiment authorship.

The definitions may be carried through SWE without claiming implementation of I-ADOPT, QUDT ontology reasoning, or a local CSAPI Property resource. If the server later supports Property creation correctly, the same semantic definitions can be materialized as Property/DerivedProperty resources.

## 5. Later research not automatically promoted into this experiment

The following work remains relevant but does not automatically change the first Smart Citizen load.

| Research area | Current standing for this experiment |
| --- | --- |
| Army ISA | Accepted identity/mediation/configuration/action clarifications are already reflected in v0.3.5. ISA is not a required runtime or bridge. |
| SAPIENT v2 | Accepted sender-identity, mode/state, task acknowledgement and selected lineage distinctions are reflected in v0.3.5. Native SAPIENT protocol implementation is not required. |
| The Open Group SOSA | Physical/logical composition and hardware/module/host distinctions informed accepted v0.3.5 rules. Modular hardware constraints are not a universal MERLIN equipment hierarchy. |
| OMS 3.0 | Accepted observational-versus-administrative and declared-product/current-data distinctions affect v0.3.5. No parallel OMS service is required. |
| SOSA/SSN | Conceptual foundation/alignment informs CSAPI and the profile; draft alignments are not formal equivalence or mandatory RDF runtime. |
| I-ADOPT / QUDT / UCUM / SWEET | Useful for precise property/quantity/unit semantics when needed. Citation or definition URI use is not ontology implementation. Smart Citizen source-provided definitions remain preferred when they are sufficient. |
| IEEE 1451 / TEDS | Exact normative transducer/channel obligations remain gated by normative-source access. The first public Smart Citizen load does not claim IEEE/TEDS implementation. Revisit for owned hardware/channel metadata when the source evidence supports it. |
| OSCAR stress test | Post-v0.3.5 research identifies residual common-model questions around artifacts, processing execution/derivation and operational episodes. For this experiment, only the processing-execution distinction is immediately exercised; it is addressed by the clarification above without inventing a new resource class. |

## 6. What this audit proves — and what it does not

This audit supports the following conclusion:

> **The Smart Citizen experiment was not wholly built on the obsolete pre-ISA/pre-SAPIENT model.** Its stated technical baseline, MPSS v0.3.5, already incorporates later owner-approved findings from Power, ISA, SAPIENT, OMS and related research, and several Smart Citizen decisions directly match those accepted rules.

The audit also establishes that the experiment was **not fully current in its traceability and explanatory documentation**. The Phase 3 donor narratives did not expose enough of the later research lineage, the Phase 4 graph omitted the accepted R15 representation-source carrier, and the process/execution distinction needed to be reconciled explicitly with later OSCAR research.

This audit does **not** claim that every item in the 109-source research corpus has been accepted into MPSS v0.3.5. The project's controlled-reconciliation method intentionally retains rejected, deferred, conditional and evidence-gated findings. A research source becomes a technical obligation only through an explicit disposition and, where needed, owner approval.

## 7. Phase 5 gate

Phase 5 deterministic adapter implementation remains blocked until all of the following are true:

1. this audit is linked from the workbook index and current-work record;
2. SC-ID-01 and the Phase 4 graph use the current R15 representation-source rule;
3. aggregate-process wording distinguishes persistent process System, reusable Procedure and acquisition/execution provenance;
4. authored aggregate-property definitions state base property, statistical qualification, procedure and authorship;
5. the research paper is rebuilt from the current research architecture, not the earlier donor table;
6. the paper contains a readable model diagram based on R01-R20 and a separate evidence-to-design/disposition diagram;
7. the paper's acronyms and terms/definitions are moved out of the opening narrative so they no longer interrupt the argument;
8. the standalone “power as a discriminating example” framing is removed; power is treated as one information subject among the eight and battery appears where the Smart Citizen mapping actually exercises it; and
9. repository and paper verification pass.

Only after these corrections are complete should Phase 5 resume.
