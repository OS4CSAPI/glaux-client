# Donor Contributions — Coverage Before Conclusions

**Version 0.1 · 30 October 2026 · America/New_York**  
**Iteration 1: coverage inventory and open contributions only.** Detailed integration across all candidate meanings is scheduled for Iteration 2.  
**Input snapshot:** `8a4a2a082d18b0806a5df85f4b387a8f9ed14a31` on `research/dim-profile-v2`.

[Main comparison and worked example](README.md) · [Equipment view — not started](Equipment_Evidence.md) · [Plan](../PLAN_DIM_Profile_V2_Concept_Donor_and_Equipment_Comparison_v0.1_30OCT2026.md) · [Drift correction](../DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md)

## 1. What this inventory tells us

**Being in our resource collection does not mean a donor received detailed comparison, and receiving detailed comparison does not mean every useful contribution was incorporated.** This page separates those states. It includes all 30 lineage keys in the existing coverage screen, including preliminary work and deferred contributions, rather than showing only sources that fit the first worked example.

The underlying [coverage screen, §2](../Donor_Challenge/01_Coverage_and_Challenge_Selection.md) reported nine lineages positively represented in the original detailed alignment records, one further lineage represented only by a deferred record, and twenty without that detailed coverage. Subsequent reports examined SAPIENT, IEEE 1451, Integrated Sensor Architecture and The Open Group SOSA. Reconciliation of those records gives **13 of the 30 lineages with some specific alignment or later-donor review, and 17 without such a detailed report in this sequence**. This is an accounting of the named research sequence, not equal-depth coverage or a claim that the seventeen have never been researched elsewhere.

The original [reconciliation, §1.1](../Donor_Alignment/09_Cross_Concept_Reconciliation.md) records 48 topic-scoped entries using 12 frozen artifact IDs, including a deferred entry. These counts do not mean 48 standards, 12 independent votes, or 13 completely assessed donor families. The wider inventory contains 182 artifacts; the 30-lineage screen is a previous research grouping, not a newly certified exhaustive taxonomy of those artifacts.

**Read the tables as a coverage report, not a work queue.** Earlier “Later: power/condition” and similar routing labels are historical recommendations. Here they identify unfinished comparisons only. The [owner's correction](../DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md) prevents those labels, preliminary traffic-light ratings or incumbent F-01–F-05 headings from determining current priority.

## 2. Thirteen lineages with some specific comparison or later-donor review

Within this section, rows are alphabetical by displayed family name, not ranked by preference. Topic labels are the historical five researched meanings: individual identity; kind/model; method/execution; composition; and digital representation. Source-edition detail remains in the linked topic or source-specific report. A reviewed claim is not an adopted model term.

| Donor lineage / retained key | Specific work already recorded | What remains open or underrepresented |
| --- | --- | --- |
| **Asset Administration Shell — C01** | Identity, kind/model and digital representation in the original alignments; asset versus Shell and Type/Instance distinctions. | Entity/Relationship forms and component/aspect treatment were flagged for further comparison. Inclusion of AAS does not mean those aspects are complete. |
| **IEEE 1451 / ISO 2145x — C03** | [Corrected IEEE report](../Donor_Challenge/03_IEEE1451_Challenge.md): interface/channel/self-description roles, including substantial public Playground and NIST technical evidence. | Addressed channel versus physical transducer, applicability of detailed descriptions, and exact uninspected normative requirements remain separate questions. Do not restore the superseded implication that the donor is technically unavailable. |
| **Integrated Sensor Architecture — C04** | [ISA source-specific findings](../Donor_Challenge/04_Other_Structural_Challenges.md): participant/composition, mediated visibility, capability declarations and communication roles. | Physical membership, exposure and taskability are not one topology; complete runtime/configuration semantics are not developed. |
| **Observations, Measurements and Samples — X08** | Original method/execution alignment: Observer, Procedure, Observation and result distinctions. | The screen records source-access limits for some cardinality work and fuller observation coverage still to develop. No universal multiplicity is inferred. |
| **OGC API – Connected Systems Parts 1–2 — C08** | Original records across all five topics; kind/method, subsystem/discovery and producer/resource distinctions. | Source vocabulary/edition issues and many actual bindings remain open. Intended binding does not make CSAPI the sole conceptual donor or a demonstrated source conversion. |
| **OPC UA Devices / PA-DIM — C10** | Original identity, kind/model, composition and representation work via **Devices Part 100, artifact 104**. | **PA-DIM artifact 103 did not receive that same separate detailed mapping.** Its signals/health material is a coverage gap, not covered merely because the family name appears here. |
| **OSUS-R — C11** | Original digital-representation comparison of pinned `Asset`/`AssetProxy` implementation code. | Wider capability/status/observation/command content remains unintegrated; implementation evidence is not a universal ontology. |
| **SAPIENT v2 — C12** | [SAPIENT source-specific report](../Donor_Challenge/02_SAPIENT_Challenge.md): Node identity, kind/role, declarations, modes, status, tasks and dependencies. | Declared versus actual roles and request/acknowledgement/outcome remain incompletely modeled; published-specification/protobuf discrepancies remain open. |
| **SAREF — C13** | Original identity, kind/model, composition and digital-representation records. | Execution/state meanings were flagged for topic-specific work. DeviceKind/Service comparisons do not complete them. |
| **SensorML 3.0 — C09** | Original kind/model, method/execution and composition records. | Physical assembly, process decomposition and inheritance/configuration differ; no universal component hierarchy follows. |
| **The Open Group SOSA — C15** | An original identity comparison was deferred; a [later source-specific review](../Donor_Challenge/04_Other_Structural_Challenges.md) examined whole Sensor, functional/manufactured/host roles and management. | Edition 1.0 data model and Edition 1.1 architecture must remain distinct. Broader product/realization/topology and management questions are not settled by their inclusion. |
| **W3C/OGC SOSA/SSN — C14** | Original identity, kind/model, method/execution and composition records using explicitly distinguished published/draft editions. | Edition/namespace correspondence remains open. This lineage is not The Open Group SOSA. |
| **W3C Web of Things — X11** | Original kind/model and digital-representation records: Thing Model, Thing Description and intermediary roles. | Broader interaction semantics are not fully compared; Thing Description 1.1 is a recorded companion outside the frozen artifact roster. |

**Evidence basis:** [prior screen §2](../Donor_Challenge/01_Coverage_and_Challenge_Selection.md), [original reconciliation §§1–3](../Donor_Alignment/09_Cross_Concept_Reconciliation.md), and [later reconciliation §§1–5](../Donor_Challenge/05_Challenge_Reconciliation.md). These tables reconcile their coverage claims; they do not independently certify every original source statement. The product/model/kind subset is illustrated on the [main page](README.md#3-worked-comparison--what-does-model-or-kind-describe).

## 3. Seventeen lineages retained as preliminary or deferred in this sequence

All rows below come from the earlier screen, not a new primary-source review. The contribution column states **the lead recorded there**, not a newly established DIM mapping. “No detailed report in this sequence” is not rejection, proof of irrelevance, or proof that no V1/preliminary work exists. The source screen links each retained key to the underlying prior extraction and its access limitations.

| Lineage / retained key | Contribution lead already recorded | Coverage limit retained here |
| --- | --- | --- |
| **Bosch BME280 — S01** | One chip versus multiple measured quantities; technical product evidence. | No detailed five-topic alignment; product datasheet is not a domain standard. |
| **I-ADOPT — X01** | Variable, property, matrix and statistical-modifier distinctions. | Preliminary extraction; measured-property contribution is not yet a developed candidate-model destination. |
| **IETF Energy Management — X02** | EnergyObject, source/battery roles and electrical quantity distinctions. | Preliminary V2 comparison in this sequence; V1 work does not grant current priority or adoption. |
| **IETF Hardware, RFC 8348 — X03** | Component class, parent position, replaceability and inventory/measurement detail. | Preliminary extraction; no detailed donor-to-candidate treatment here. |
| **IETF Interfaces / Topology — X04** | Interface/network links and layered connectivity versus mechanical membership. | Preliminary extraction; no developed comparison of these relationship meanings. |
| **ISO/IEC 29182 Sensor Network Reference Architecture — C05** | Sensor node/network and physical/functional views. | Screen records original-part access limitations; no detailed comparison in this sequence. |
| **Lightweight Machine-to-Machine — X09** | Client/Object/Instance/Resource structure and management. | Preliminary extraction; digital hierarchy must not be assumed to be physical composition. |
| **Matter 1.3 — C06** | Node, Endpoint, Device Type and Cluster as functional organization. | Preliminary extraction with recorded authority/access limits; no new edition or hardware equivalence assumed. |
| **MIMOSA — C07** | Asset/type, events, condition and maintenance roles. | Preliminary work; Common Conceptual Object Model release-candidate material and other MIMOSA specifications have distinct standing. |
| **MIP / JC3IEDM — X05** | Type/item, action, status, location, capability and report concepts. | Preliminary extraction; exact deeper-edition access limited in the screen. |
| **NIEM — X06** | Type, Association, Augmentation and exchange/modeling techniques. | Preliminary extraction; no generic sensor class or source-to-DIM mapping established here. |
| **NISTIR 8259A — X07** | Device identity, access, secure configuration and events. | Preliminary coverage lead; not a physical-anatomy or full security model for this DIM. |
| **Radiation instruments — S02** | Instrument/detector, calibration and modality-specific distinctions. | Several normative details were inaccessible; a family lead, not a qualified equipment dataset. |
| **Redfish / Common Information Model — C02** | Chassis, ComputerSystem, Manager, Sensor and Battery distinctions. | Preliminary extraction; no detailed comparison in the referenced alignment/review sequence. |
| **SWEET ontology — S03** | Sensor/Instrument/Equipment taxonomy. | Preliminary extraction; not a completed domain-boundary or lifecycle synthesis. |
| **Unattended ground sensing cases — S04** | Historical TRSS/OmniSense contrasts. | Limited historical/synthetic case material, not a normative donor or compulsory new experiment. The owner's later correction supersedes the old emphasis. |
| **W3C PROV — X10** | Entity/Activity/Agent, sources and derivation. | Preliminary extraction; provenance relevance does not establish a completed cross-cutting DIM model. |

IETF denotes the Internet Engineering Task Force; RFC denotes Request for Comments. Other family names and historical keys are retained as labels from the source screen; they are not new concept names. The original [screen §2](../Donor_Challenge/01_Coverage_and_Challenge_Selection.md) gives the frozen artifact IDs, extraction locations and source-specific access context for all rows. No preliminary rating is promoted into verified equivalence or conformance.

### Material beyond the 30-lineage screen

The [182-artifact accountability snapshot](../Donor_Alignment/03_Source_Accountability_Register.csv) remains the wider inventory. **This iteration does not establish complete coverage outside the 30 named prior extractions, or a new all-artifact-to-family reconciliation.** Unlisted artifacts and companion sources cannot be treated as irrelevant or fully assessed. That coverage boundary remains visible instead of being hidden by an apparently complete donor table.

## 4. Contributions with no developed model destination yet

The later reconciliation records seven source-specific issue flags grouped into five open questions. The grouping is editorial, not five new classes. The table below carries those questions forward **without adopting their earlier suggested homes in F-01–F-05**. A future proposal may place them elsewhere, divide them, combine them or demonstrate that another structure is preferable.

| Open contribution from the existing record | Source findings to follow | What still has to be explained |
| --- | --- | --- |
| **Declared capabilities, allowed behavior and actual selected/reported state** | `DC05-G01`: SAPIENT `SAP-NC-01`; structural-donor `DC04-NC-03`. | A declaration and a current report are different claims; there is no complete common treatment yet. “Operational condition” is not a defined destination. |
| **Requests, acknowledgements, outcomes and test results** | `DC05-G02`: `SAP-NC-02`; `DC04-NC-03`. | Acceptance, completion and a resulting observation/test finding cannot imply one another without source evidence. No universal lifecycle has been selected. |
| **Addressed channels and technical self-description** | `DC05-G03`: IEEE `IE03-NC-01/02`, including the corrected Playground evidence. | How channel address, physical element, described property, units, range, calibration and timing relate at their actual scopes. |
| **Physical, functional, manufactured and hosted arrangements** | `DC05-G04`: `DC04-NC-02`. | Multiple legitimate relationship structures may describe the same subject; a single component tree is not established. |
| **Outward visibility, taskability and intermediary authority** | `DC05-G05`: `DC04-NC-01`. | Which subject exists, which representation is exposed, what can be tasked, and whose information is being published. |

Source: [later reconciliation §5](../Donor_Challenge/05_Challenge_Reconciliation.md). These are already-recorded gaps, not a new donor survey or a ranked next-subject recommendation. The further leads in §3 remain outside even these five clusters; a table of recorded gaps cannot claim to exhaust all potential donor contributions.

## 5. What is and is not complete in this view

**Complete for Iteration 1:** all 30 prior lineage keys are visible once in §§2–3; the original/later coverage distinction is reconciled; partial coverage within families is explicit; known unrepresented questions remain locatable; and the worked example links source meanings to the existing candidate interpretation.

**Still to do:** populate the broader meaning-and-relationship comparison in Iteration 2, connect equipment records in Iteration 3, and verify the consolidated claims and alternative next actions in Iteration 4. No claim of equal-depth donor review, full-corpus completeness or neutral re-synthesis is made merely because this inventory is now readable. Historical findings remain unchanged; proposed future changes must have their own evidence and rationale.
