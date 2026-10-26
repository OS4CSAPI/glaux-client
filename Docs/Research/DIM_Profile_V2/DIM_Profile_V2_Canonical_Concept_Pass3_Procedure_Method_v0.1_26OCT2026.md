# Domain Information Model (DIM) / Application Profile Version 2 (V2)
## Canonical Concept Consolidation — Pass 3: Procedure / Method

**Date:** 26 October 2026  
**Standing:** Evidence-backed **candidate meaning for human review**; not an adopted DIM class, new relationship, schema, or profile requirement.  
**Continuity:** [Pass 1 — Individual System Identity](DIM_Profile_V2_Canonical_Concept_Pass1_Individual_System_Identity_v0.1_26OCT2026.md); [Pass 2 — Product / Model / Kind](DIM_Profile_V2_Canonical_Concept_Pass2_Product_Model_Kind_v0.1_26OCT2026.md); [C08 validation correction](DIM_Profile_V2_Anatomy_PhaseA_Validation_Audit_v0.1_26OCT2026.md); [incremental consolidation plan](DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md).  
**Evidence standing:** This pass compares the published 2025 Connected Systems and Sensor Model Language standards, *Observations, Measurements, and Samples* (2023), and the World Wide Web Consortium/Open Geospatial Consortium SOSA/SSN **21 October 2026 Working Draft**. The draft is research evidence, **not** the older ontology edition referenced normatively by published Connected Systems 1.0.

## 1. The question

**What does it mean to describe how a System performs a sensing or other task, rather than what product/model the System is, what the System is configured to do, or what it actually did on one occasion?**

The preceding passes distinguish the **individual System** and its **reusable product/kind description**. This pass determines what the donors mean by **Procedure** and **Method**, and which relationships to the System and its executions they support. It does **not** attempt a general capability model, configuration model, or dynamic-data architecture.

## 2. Synthesized candidate meaning — with source pedigree

> **For V2, a Procedure or Method is a reusable description of how a task is carried out, such as an observing workflow, measurement protocol, algorithm, or processing method; it is distinct from the individual System that can perform it** (World Wide Web Consortium and Open Geospatial Consortium 2026, §§ 5.3.3.2.1, 5.3.5.2.11; Open Geospatial Consortium and International Organization for Standardization 2023, §§ 8.4–8.6; Open Geospatial Consortium 2025b, § 8.3.2). **A System may be described as capable of implementing a Procedure, while an actual Observation or other Execution is a separate occurrence that uses a Procedure and may produce a result** (World Wide Web Consortium and Open Geospatial Consortium 2026, §§ 5.3.3.2.5, 5.3.4.2.1, 5.3.4.2.11, 5.3.4.2.16; Open Geospatial Consortium and International Organization for Standardization 2023, §§ 8.2.2, 8.2.9, 8.5–8.6). **The Procedure description and its use must not be conflated with the System's product kind/model, even though existing standards may reuse one descriptive resource or include type-level information in a Procedure description** (Open Geospatial Consortium 2025a, §§ 9.2.2, 13.1–13.2; Open Geospatial Consortium and International Organization for Standardization 2023, § 8.5.2). **A method's detailed steps, parameterization, processing structure, and implementation references can be expressed at different levels of detail depending on the donor standard and the actual source evidence** (Open Geospatial Consortium 2025b, §§ 7.1–7.2, 8.3.2, 8.4.1; World Wide Web Consortium and Open Geospatial Consortium 2026, § 5.3.3.2.1).

**Synthesis status:** These are **relationships among existing source-native concepts**, not a proposal to create a V2 `SystemMethod`, `ProcedureExecution`, or other novel umbrella class. “Procedure or Method” is explanatory prose: the donors' definitions and classes are **not automatically equivalent**. In particular, “may be described as capable” does **not** assert that each System has a published Procedure description or that its claimed support proves a recorded execution.

## 3. Where the building blocks come from

### 3.1 A reusable description of how a task is carried out

**Meaning in the donor.** The current **Sensor, Observation, Sample, and Actuator (SOSA) / Semantic Sensor Network (SSN)** ontology, developed by the **World Wide Web Consortium (W3C)** and **Open Geospatial Consortium (OGC)**, defines `sosa:Procedure` as a reusable workflow, protocol, plan, algorithm, program, or computational method for making an `Execution`. It covers Observation, Actuation, and Sampling; its `hasInput` and `hasOutput` concepts concern inputs and outputs associated with the procedure, not one measurement record. The ontology explicitly leaves a comprehensive formal model for the internal description of Procedures to other standards (World Wide Web Consortium and Open Geospatial Consortium 2026, § 5.3.3.2.1–3).

The OGC and **International Organization for Standardization (ISO)** standard *Observations, Measurements, and Samples* (**OMS**) defines `Procedure` as a **description of steps performed**, and `ObservingProcedure` as steps an Observer performs to determine an observable-property value. It explains that a procedure can be a measuring protocol, workflow, checklist, or algorithm, and different Observers can follow the same reusable procedure (Open Geospatial Consortium and International Organization for Standardization 2023, §§ 8.4.2, 8.5.2, 8.6.2).

**What V2 takes from these donors.** Procedure/Method concerns **the manner or method of performance**, not the identity of the performer. The same description may be relevant to different individual instruments or performances. This is directly sourced meaning, **not** a reason to design a new V2 class when `Procedure` is already a suitable candidate in the OGC/SOSA environment.

### 3.2 “The System can implement it” — capability to execute is a relationship, not an execution record

**Meaning in the donor.** In SOSA/SSN, `sosa:implements` explicitly relates a **System** to a **Procedure that it is capable of executing**; `sosa:implementedBy` is the inverse (World Wide Web Consortium and Open Geospatial Consortium 2026, §§ 5.3.5.2.11, 5.3.3.2.5). OGC **Application Programming Interface (API) – Connected Systems (CSAPI)** Part 1 reflects this by providing a System association named `procedures` for descriptions the System *can implement*; that association is optional in the CSAPI System resource model (Open Geospatial Consortium 2025a, § 9.2.2, table 5).

**What V2 takes from these donors.** A declared or known implemented Procedure is **information about what a System can do by following a method**. It need not be treated as a record proving the System performed that method on a specific occasion. Nor should an unpopulated CSAPI `procedures` association be interpreted as proof of *no method capability*. The logical distinction is important even though its final V2 cardinalities and required profile behavior remain open.

### 3.3 “An actual Execution used it” — the method, performer, and event have separate meanings

**Meaning in the donor.** The SOSA/SSN draft distinguishes `sosa:Execution` (the act of carrying out a Procedure using a System) from the reusable `Procedure` and from the executing `System`. Its relationships `sosa:usedProcedure` and `sosa:madeBySystem` identify the method used and who/what performed the act. Concrete execution kinds include `Observation`, `Actuation`, and `Sampling` (World Wide Web Consortium and Open Geospatial Consortium 2026, §§ 5.3.4.2.1, 5.3.4.2.11, 5.3.4.2.16). The newer `ObservingProcedure` specialization introduced in this 2023-edition draft is **marked non-normative/pending implementation experience**; use that draft status explicitly if citing the specialization (World Wide Web Consortium and Open Geospatial Consortium 2026, § 5.5.2.3).

OMS makes the same distinction especially explicit for observations: the *Observer* executes an *ObservingProcedure* to make an *Observation* and generate its result. Its conceptual schema requires exactly one associated observing procedure **for an Observation within that source model** (Open Geospatial Consortium and International Organization for Standardization 2023, §§ 8.2.2, 8.2.9, 8.5–8.6).

**What V2 takes from these donors.** **“System can implement Procedure” ≠ “this particular Observation used Procedure.”** Both relationships matter for interpreting sensor information and its provenance, but they are not interchangeable. The OMS observation-level cardinality is **OMS's normative constraint for its model**, not a newly established DIM-wide or CSAPI-profile rule. Describing a method is also distinct from initiating a command or recording the result of an execution; the latter details remain for later passes.

### 3.4 “Methodology can be detailed” — SensorML's process perspective

**Meaning in the donor.** **Sensor Model Language (SensorML) 3.0** describes processes using inputs, outputs, parameters, and methodology. Its `ProcessMethod` describes how a **SimpleProcess** converts input/parameter values into outputs, optionally with a machine-readable algorithm and references to executable implementations (Open Geospatial Consortium 2025b, §§ 7.1–7.2, 8.3.1–8.3.2). For **AggregateProcess** or a physical system, **connected component processes and their data-flow structure** may themselves provide the methodology; a single separate `ProcessMethod` object is **not required for every kind of SensorML process** (Open Geospatial Consortium 2025b, §§ 7.1–7.2, 8.4.1).

**What V2 takes from this donor.** SensorML offers the more detailed OGC **process-description** patterns that SOSA/SSN intentionally does not prescribe. It is therefore a strong potential way to **represent** detailed methods later, without making all SensorML process elements mandatory DIM concepts. Its *description of a process* does not by itself constitute an assertion that some identified System performed one historical Observation.

### 3.5 Why the kind/model and method meanings may overlap in the same donor resource

**Meaning in the donor.** CSAPI is especially consequential here: its **same `Procedure` resource type** can carry both a **System kind/datasheet** description and a **methodology**. But CSAPI names **different relations**: `systemKind` targets one Procedure describing the *kind of System*, while `procedures` targets Procedures the System *can implement*. Its Procedure resource also carries a `procedureType` capable of identifying observing/sampling/actuating methodologies and sensor/actuator/other system datasheets (Open Geospatial Consortium 2025a, §§ 9.2.2, 13.1–13.2, tables 5 and 16). This dual use of one carrier must **not** collapse the distinct relation meanings recovered in the project's [C08 audit](DIM_Profile_V2_Anatomy_PhaseA_Validation_Audit_v0.1_26OCT2026.md).

OMS supplies a valuable counterweight to any absolute separation: its description of an `ObservingProcedure` says it **cannot describe an individual sensor instance but can describe a sensor type** (Open Geospatial Consortium and International Organization for Standardization 2023, § 8.5.2). Thus the word **Procedure** need not imply a technical document utterly divorced from model/type specifications.

**What V2 takes from these donors.** The safest rule is **distinguish what the information is used to say**: what kind of System an individual is, which procedures that System can implement, and which procedure a given execution actually used. **These semantic roles are distinct even where one source document or CSAPI resource contains overlapping specifications.** We should not invent disjoint V2 `ProductModel` and `ProcedureMethod` classes merely to force one particular packaging choice onto sources.

## 4. Contribution comparison and implications

| Donor | Source-native concept or relationship | What V2 should preserve | Caution |
| --- | --- | --- | --- |
| CSAPI Part 1 | `System.systemKind`, `System.procedures`, shared `Procedure` resource, `procedureType` | **Kind description vs implemented method as different association roles** | Same resource type does not make roles synonyms; API link mechanics are bindings |
| SOSA/SSN 2026 Working Draft | `Procedure`, `System implements Procedure`, `Execution usedProcedure` | **Reusable method, capable performer, occurrence of use** | Draft status; no automatic ontology class or profile obligations |
| SensorML 3.0 | `ProcessMethod`, `SimpleProcess`, `AggregateProcess`, inputs/outputs/parameters | **Method details may be explicit steps/algorithm or component/data flow** | Process/encoding structure is not automatically a DIM class hierarchy |
| OMS 3.0 | `Procedure`, `ObservingProcedure`, `Observer`, `Observation` | **Observation method separate from actual Observer and Observation; source result interpretation** | OMS cardinalities are source-scoped; procedure may also describe sensor type |

**Practical value:** Imagine two deployed probes of the same manufacturer model measuring groundwater level. One uses an automated sensing method, while a technician later measures the same property with a manual probe following another protocol. OMS explicitly uses an automated-versus-manual-probe comparison to distinguish observing procedures, even when the observed property is the same (Open Geospatial Consortium and International Organization for Standardization 2023, § 8.3.2). Knowing only the device model or the observation result does **not necessarily identify the method used**. The procedure can supply context relevant to result interpretation, quality and cross-source comparison.

## 5. What remains genuinely open

1. **Granularity and reuse.** When does a named method warrant a distinct, referenceable Procedure description rather than remaining a paragraph within a sensor datasheet? The sources support both; V2 has **not** chosen a universal rule.
2. **Method versions and settings.** When changed parameters, calibration, software revision or algorithm implementation changes the actual method—and how the method version is identified—depends on source semantics and evidence. No new identity/versioning rule is adopted here.
3. **Linking a method to a result.** SOSA/SSN and OMS offer precise execution–method relationships, but V2 has not selected what must be conveyed, at what granularity, or through which binding/profile constraints for every integrated sensor.

**Disposition:** The source evidence strongly supports **separate meanings** for *individual System*, *kind/model description*, *reusable Procedure/Method*, *System capable of implementing it*, and *particular execution using it*. **No new V2 class, universal cardinality, implementation binding, or normative profile requirement is justified by Pass 3 alone.**

**Next planned increment (only when directed): Pass 4 — Composition and Component Standing.** Do not start it automatically.

## References — Chicago Manual of Style, 18th edition, author–date

Open Geospatial Consortium. 2025a. *OGC API—Connected Systems—Part 1: Feature Resources*. OGC 23-001, version 1.0, July 16. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC SensorML Encoding Standard*. OGC 23-000, version 3.0, July 16. https://docs.ogc.org/is/23-000/23-000.html.

Open Geospatial Consortium and International Organization for Standardization. 2023. *Observations, Measurements and Samples*. OGC 20-082r4 / ISO 19156:2023. https://docs.ogc.org/as/20-082r4/20-082r4.html.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology—2023 Edition*. Working Draft, October 21. OGC 25-022. https://www.w3.org/TR/vocab-ssn-2023/.
