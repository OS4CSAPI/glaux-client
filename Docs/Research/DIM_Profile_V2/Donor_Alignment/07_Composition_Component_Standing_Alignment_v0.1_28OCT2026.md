# Donor Alignment — Step 07: Composition / Component Standing

**Version:** 0.1 · **28 October 2026**  
**Plan:** [12-step Donor Alignment and Foundational DIM Construction](../PLAN_DIM_Profile_V2_Donor_Alignment_and_Foundation_v0.1_28OCT2026.md), **Step 07 ONLY**.  
**Standing:** **COMPLETE as bounded, source-qualified semantic comparison**, NOT an adopted DIM class/component hierarchy, publication-level mapping, application Profile, requirement, real physical-instance inventory or empirical interoperability result.  
**Branch:** `OS4CSAPI/glaux-client` / `research/dim-profile-v2`; no application/UI/fixture/deployment changes and no edits to the 182-source frozen corpus.  
**Prior evidence:** [Pass 4 — Composition/Standing](../DIM_Profile_V2_Canonical_Concept_Pass4_Composition_and_Component_Standing_v0.1_26OCT2026.md); [Step 02 alignment method](02_Register_Method_and_Schema.md); [Step 03 source register](03_Source_Accountability_Register.csv); [Steps 04–06](06_Procedure_Method_Alignment_v0.1_28OCT2026.md); [Smart Citizen I07](../Case_Studies/Real_Equipment_DIM_Validation/I07_Composition_and_Component_Standing_Mapping_v0.1_28OCT2026.md), [I10 critical review](../Case_Studies/Real_Equipment_DIM_Validation/I10_Model_View_Critical_Check_and_Gate_C_v0.1_28OCT2026.md), and [I12 challenged transforms](../Case_Studies/Real_Equipment_DIM_Validation/I12_Critical_Interoperability_Challenge_v0.1_28OCT2026.md).

## 1. Finding: relationship type and description granularity are **independent questions**

For a sensing-oriented equipment System, we must separately ask **(A) how a constituent or related element is associated with the whole** and **(B) what independently describable standing the source truly establishes for it**. A documented board, sensor chip, PM module, battery, channel, software association, Platform or external service may have an important relationship to the whole, **without** all becoming peer physical CSAPI `System` instances.

The donor corpus offers qualified, non-interchangeable mechanisms: CSAPI regular System-subsystems and a **Composition versus Aggregation/Deployment** lifecycle distinction; SensorML physical-process description with or without component dataflow; 2017 SSN and the 2026 SOSA/SSN Working Draft's edition-specific System-subsystem predicates, separate from hosting; OPC UA device/subdevice topology, which includes hardware and software; and SAREF's broad semantic composites. **None provides a universal rule to create a separate System for each named part, cable, measured channel, software record or source-defined “component.”**

**Candidate semantic statement, NOT an adopted class/relation:** *A sensing-equipment System can be understood as a whole and through source-supported constituents. Those constituents may have different relationship roles (integral, non-permanent, hosted/deployed, functional/dataflow, digital association) and different levels of description (unmodeled detail, separately characterized physical part, measurement channel, managed System). Distinct source facts must not be collapsed into one mandatory component hierarchy or a uniform lifetime assertion.*

**A useful design heuristic, explicitly OUR inference:** describe a constituent independently when its source-supported **identity, configuration, calibration, output, state, serviceability, replaceability or external relationship** would otherwise be lost or misattributed. **That is not a donor-prescribed threshold** for turning the element into a System. Each case still needs source evidence for the relevant viewpoint and proposed CSAPI/SensorML/other binding.

**Register scope:** **13** directional donor-alignment records below from **seven frozen artifact IDs: 10, 11, 13, 19, 20, 104, 144**. These represent **five lineages**, NOT seven independent donor votes (CSAPI Parts 1 and 2 together; 2017 and draft 2026 SOSA/SSN together). All seven IDs exist in the [frozen-derived 182-row source register](03_Source_Accountability_Register.csv); that snapshot intentionally retains its initial per-artifact `NOT_ASSESSED` field, while each later topic file controls its **topic-specific** review. The Smart Citizen I07/I10/I12 evidence is a **case-study test, not another frozen standards artifact or an eighth standard**.

**Evidence standing:** The **named** sections of the original CSAPI Parts 1–2, SensorML 3.0, 2017 SSN, dated 21 October 2026 SSN Working Draft, OPC UA Part 100 **v1.05.0** and ETSI SAREF **v4.1.1** were rechecked directly. The manufacturer assembly, Urban/Data Board source and Rails Component model were read at their **previously pinned commits**. This is **not** a full normative edition/conformance audit of those standards or actual fielded hardware. The 2026 draft alignment sections (§§7.2/7.3) are expressly non-normative and **not** formal proof of cross-standard equivalence.

## 2. Source-native concept-to-candidate-meaning alignments

Each entry follows [Step 02's exact field contract](02_Register_Method_and_Schema.md#4-minimal-detailed-alignment-record-format--steps-0408). Original source roles/editions and the researcher's proposed meaning are separate; every record is `NOT_ADOPTED` and `NO_TRANSFORMATION_TEST`. Mapping direction is explicitly source concept → candidate V2 distinction, not an OWL axiom or an automatic donor-conformance claim.


### ALN-T04-A010-01 — CSAPI subsystem is itself a regular System resource, not every physical part

| Field | Source-qualified value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T04-A010-01 / TOPIC-04-COMPOSITION-COMPONENT-STANDING / *relation-to-whole, source-justified separately described standing, and non-equivalent representation/association roles*. This is a thematic research topic ID, **not** a DIM class. |
| `artifact_id` / `lineage` / `source_role` | **10** / OGC Connected Systems (Part 1) / primary anatomy evidence; core structural donor; target API feature model. |
| `source_ed` / `source_concept` / `source_locator` | **OGC 23-001 v1.0, 16 July 2025**. [OGC Part 1 §§10.1, 10.3.1–10.3.2, §9.2.2](https://docs.ogc.org/is/23-001/23-001.html): Subsystems requirements class and Table 8 `parentSystem` (required). |
| `source_native_meaning` | Under the optional *Subsystems* requirements class, hierarchically represented subsystems are regular CSAPI `System` features, possibly nested without a fixed depth. A described child System has a `parentSystem` association and canonical resource URL. The requirement describes **API System-resource standing**, not every physically present resistor, IC, channel or database association. |
| `mapping_direction` / `relation_kind` | Source's *explicitly modeled sub-System* → V2 candidate distinction ‘some subordinate things are individually describable Systems’; `CLOSE_ALIGNMENT_WITH_QUALIFICATION`. This API-specific representational standing is a **narrower condition** than merely having a source-identifiable piece of equipment. |
| `reused_role` / `qualification_or_loss` | Preserve identification and genuine parent relation for a source-supported subsystem. Do **not** turn each mounted SHT31/AS7331 chip, sensor output or backend `Component` into a System based only on containment/naming. A subsystem may be a System, but a board-level separate description does not itself prove that standing. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` (§§10.1,10.3, Table 8); source resource requirements `DONOR_TEXT`, V2 candidate relation `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for the separation of parent relationship and resource standing. **`adoption_status=NOT_ADOPTED`**. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST` — only scoped primary-text review and hypothetical semantic-loss checks. No audited vendor→Profile-constrained CSAPI data transformation, real individual equipment identity, implemented conformance tests or end-to-end client proof. |
| `donor_declarations` | `DECL-T04-01`, `DECL-T04-02`; see ontology-edition warning. |
| `source_to_client_consequence` / `open_question` | A later details UI may show validated subsystems as independent resource links, while showing non-System parts in qualified internal equipment detail. Open: which source identifier, descriptive life cycle and CSAPI representation justify each physical part as a System? |
| `record_provenance` | 28 October 2026; Step 07 direct source review, plus existing Pass 4 and I07/I10/I12 source-correction comparison. Research record v0.1; no owner model-adoption decision. |


### ALN-T04-A010-02 — CSAPI Composition versus Aggregation: **lifecycle/association**, not cable type

| Field | Source-qualified value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T04-A010-02 / TOPIC-04-COMPOSITION-COMPONENT-STANDING / *relation-to-whole, source-justified separately described standing, and non-equivalent representation/association roles*. This is a thematic research topic ID, **not** a DIM class. |
| `artifact_id` / `lineage` / `source_role` | **10** / OGC Connected Systems (Part 1) / primary anatomy evidence; core structural donor; target API feature model. |
| `source_ed` / `source_concept` / `source_locator` | **OGC 23-001 v1.0, 16 July 2025**. [OGC Part 1 §10.2](https://docs.ogc.org/is/23-001/23-001.html), ‘Types of System/Subsystem Associations,’ examples and note contrasting UML Composition. |
| `source_native_meaning` | CSAPI **Composition** means an integral part, not usually separated except maintenance; it may be used even if the part can theoretically exist independently. **Aggregation** describes non-permanent attachment, possibly moving between parents over time, represented by `Deployment` resources. The source contrasts built-in sensors with mission-swappable payloads, and explicitly cautions that its ‘Composition’ is looser than strict UML composite aggregation. |
| `mapping_direction` / `relation_kind` | CSAPI's permanence-sensitive part relation → candidate distinction of *enduring/integral versus non-permanent/interchangeable association*; `CLOSE_ALIGNMENT_WITH_QUALIFICATION` because the former uses CSAPI carrier choices and may lack verified source lifecycle history. |
| `reused_role` / `qualification_or_loss` | Retain **source-described expected assembly and actual history as separate assertions**. Being cabled/removable does not, by itself, imply temporal Aggregation. Do not draw UML filled diamonds, assign lifetime destruction behavior, or choose CSAPI Deployment for a PM module merely because there is a cable. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` (§10.2); native interpretation `DONOR_TEXT`, Smart Citizen application `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for qualified relation-type distinction. **`adoption_status=NOT_ADOPTED`**. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST` — only scoped primary-text review and hypothetical semantic-loss checks. No audited vendor→Profile-constrained CSAPI data transformation, real individual equipment identity, implemented conformance tests or end-to-end client proof. |
| `donor_declarations` | `DECL-T04-01` (standard pedigree) only; no donor-stated equivalence to OPC UA Modular Device ‘aggregated’ SubDevices. |
| `source_to_client_consequence` / `open_question` | Distinguish installed standard-assembly constituent from temporary payload where evidence permits. Open: is the actual identified component ordinarily integral over its operating lifetime, or really reattached between host Systems at dated deployments? |
| `record_provenance` | 28 October 2026; Step 07 direct source review, plus existing Pass 4 and I07/I10/I12 source-correction comparison. Research record v0.1; no owner model-adoption decision. |


### ALN-T04-A010-03 — CSAPI subsystem endpoint may list **currently deployed** children; nesting ≠ permanence

| Field | Source-qualified value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T04-A010-03 / TOPIC-04-COMPOSITION-COMPONENT-STANDING / *relation-to-whole, source-justified separately described standing, and non-equivalent representation/association roles*. This is a thematic research topic ID, **not** a DIM class. |
| `artifact_id` / `lineage` / `source_role` | **10** / OGC Connected Systems (Part 1) / primary anatomy evidence; core structural donor; target API feature model. |
| `source_ed` / `source_concept` / `source_locator` | **OGC 23-001 v1.0, 16 July 2025**. [OGC Part 1 §10.5, Requirement 9(C)](https://docs.ogc.org/is/23-001/23-001.html), plus §§10.2 and 10.3. |
| `source_native_meaning` | The `/systems/{parentId}/subsystems` endpoint SHALL include permanently attached System subsystems but CAN also expose **currently deployed** subsystems. The text recommends distinct Deployment descriptions when interchangeable payloads change. Therefore discovery through nesting alone does **not** assert Composition. |
| `mapping_direction` / `relation_kind` | CSAPI's source-owned *discovery rule* → candidate need to distinguish **resource discoverability** from **relationship permanence**; `PARTIAL_OVERLAP`. This is an API exposure rule, not an identity claim about any one physical assembly. |
| `reused_role` / `qualification_or_loss` | Retain the §10.5 permissions along with §10.2's substantive association types; do not infer the history of a part from an endpoint path. Specifically reproduces [I12 X03/C12-03](../Case_Studies/Real_Equipment_DIM_Validation/I12_Critical_Interoperability_Challenge_v0.1_28OCT2026.md). |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` (§10.5 Req 9(C)); exposure rule `DONOR_TEXT`, candidate negative inference `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for source/API-versus-domain disambiguation. **`adoption_status=NOT_ADOPTED`**. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST` — only scoped primary-text review and hypothetical semantic-loss checks. No audited vendor→Profile-constrained CSAPI data transformation, real individual equipment identity, implemented conformance tests or end-to-end client proof. |
| `donor_declarations` | No new inter-donor assertion; `DECL-T04-02` concerns the separate ontology-label correspondence. |
| `source_to_client_consequence` / `open_question` | A client should not label all visible ‘subsystems’ as permanently installed. Open: what Deployment/history source makes a claim of permanence or interchangeability testable? |
| `record_provenance` | 28 October 2026; Step 07 direct source review, plus existing Pass 4 and I07/I10/I12 source-correction comparison. Research record v0.1; no owner model-adoption decision. |


### ALN-T04-A010-04 — CSAPI parent recursively exposes child streams, not direct production by the parent

| Field | Source-qualified value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T04-A010-04 / TOPIC-04-COMPOSITION-COMPONENT-STANDING / *relation-to-whole, source-justified separately described standing, and non-equivalent representation/association roles*. This is a thematic research topic ID, **not** a DIM class. |
| `artifact_id` / `lineage` / `source_role` | **10** / OGC Connected Systems (Part 1) / primary anatomy evidence; core structural donor; target API feature model. |
| `source_ed` / `source_concept` / `source_locator` | **OGC 23-001 v1.0, 16 July 2025**. [OGC Part 1 §10.7, Requirement 13, Table 9](https://docs.ogc.org/is/23-001/23-001.html): recursive `samplingFeatures`, `datastreams` and `controlstreams`. |
| `source_native_meaning` | Where a parent CSAPI System has described subsystems, its `datastreams` association must include those generated by the parent **and all descendants**. The analogous requirement applies to sampling features and control streams. Thus a stream's appearance under a parent association is not sufficient to identify that parent as the measurement producer. |
| `mapping_direction` / `relation_kind` | API's recursive aggregation of resource associations → candidate distinction of *discovery context* versus *actual producing System*; `PARTIAL_OVERLAP`; this rule is about navigation/search, not a direct part-to-observation provenance relation. |
| `reused_role` / `qualification_or_loss` | Prevent the falsified [I12 X02/C12-02](../Case_Studies/Real_Equipment_DIM_Validation/I12_Critical_Interoperability_Challenge_v0.1_28OCT2026.md) mapping. Preserve the **explicit stream producer** (Part 2 ID 11) even when users navigate via the parent. No sensor-channel → child-System multiplication is implied. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` (§10.7 Table 9); recursive rule `DONOR_TEXT`, fidelity implication `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for discovery-versus-producer separation. **`adoption_status=NOT_ADOPTED`**. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST` — only scoped primary-text review and hypothetical semantic-loss checks. No audited vendor→Profile-constrained CSAPI data transformation, real individual equipment identity, implemented conformance tests or end-to-end client proof. |
| `donor_declarations` | The two CSAPI parts belong to the same published multipart standards family; this is a cross-part **analyst comparison** with ID 11 below, not a new external-donor consensus statement. |
| `source_to_client_consequence` / `open_question` | For child-produced readings discovered on a parent Details page, distinguish the context/host parent from the producer indicated by the DataStream. Open: which stream producer and measured-channel source references are actually present? |
| `record_provenance` | 28 October 2026; Step 07 direct source review, plus existing Pass 4 and I07/I10/I12 source-correction comparison. Research record v0.1; no owner model-adoption decision. |


### ALN-T04-A011-01 — CSAPI Part 2 DataStream producer is a source link independent of physical part count

| Field | Source-qualified value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T04-A011-01 / TOPIC-04-COMPOSITION-COMPONENT-STANDING / *relation-to-whole, source-justified separately described standing, and non-equivalent representation/association roles*. This is a thematic research topic ID, **not** a DIM class. |
| `artifact_id` / `lineage` / `source_role` | **11** / OGC Connected Systems (Part 2) / primary anatomy evidence; dynamic-data companion of the same CSAPI lineage (not an independent donor vote). |
| `source_ed` / `source_concept` / `source_locator` | **OGC 23-002 v1.0, 16 July 2025**. [OGC Part 2 §9.1–9.2.2, Table 5](https://docs.ogc.org/is/23-002/23-002.html): `DataStream.system` (required), observation/result schema and DataStream grouping. |
| `source_native_meaning` | Part 2's `DataStream.system` references the **System that produces the datastream**. The DataStream groups observations according to source/output, observed-property set and result-schema rules. One packaged physical chip can support multiple measured properties; the source standard does not require ‘one stream per chip,’ ‘one per backend Component’ or ‘one per individual measured property’ merely from physical layout. |
| `mapping_direction` / `relation_kind` | Source's datastream producer relation → candidate need for distinct *physical/subsystem source identity* versus *measurement output/stream semantics*; `CLOSE_ALIGNMENT_WITH_QUALIFICATION`. This is a data-resource binding, not evidence of a physical child System. |
| `reused_role` / `qualification_or_loss` | Retain the Part 2 producer association; avoid assigning each logical output its own System or mistakenly treating the parent recursive association as its unique producer. Actual correct stream count requires observed properties, schema and real vendor data—absent here. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` (§§9.1–9.2.2/Table 5); source relation `DONOR_TEXT`, mapping caveat `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for output/provenance distinction, not for a finalized stream-binding rule. **`adoption_status=NOT_ADOPTED`**. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST` — only scoped primary-text review and hypothetical semantic-loss checks. No audited vendor→Profile-constrained CSAPI data transformation, real individual equipment identity, implemented conformance tests or end-to-end client proof. |
| `donor_declarations` | Not an independent lineage: companion Part 2 to ID 10; 2026 draft §7.3.1 correspondence is separately declared in `DECL-T04-03` and non-normative. |
| `source_to_client_consequence` / `open_question` | Group temperature/humidity and UV outputs according to **actual stream schema and producer**, rather than rendering each UI row as a separate physical device. Open: no authenticated SCK2.3 producer/stream/Observation exists in the frozen case. |
| `record_provenance` | 28 October 2026; Step 07 direct source review, plus existing Pass 4 and I07/I10/I12 source-correction comparison. Research record v0.1; no owner model-adoption decision. |


### ALN-T04-A013-01 — SensorML PhysicalComponent: defined-process description without internal process decomposition

| Field | Source-qualified value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T04-A013-01 / TOPIC-04-COMPOSITION-COMPONENT-STANDING / *relation-to-whole, source-justified separately described standing, and non-equivalent representation/association roles*. This is a thematic research topic ID, **not** a DIM class. |
| `artifact_id` / `lineage` / `source_role` | **13** / OGC SensorML / primary anatomy evidence; core process/physical description and encoding donor. |
| `source_ed` / `source_concept` / `source_locator` | **OGC 23-000 SensorML 3.0, 16 July 2025**. [OGC SensorML 3.0 §8.5.2, Requirement 31](https://docs.ogc.org/is/23-000/23-000.html): `PhysicalComponent` definition. |
| `source_native_meaning` | SensorML uses `PhysicalComponent` for a physical process/device with defined inputs and outputs when the description is **not intended to be subdivided into component subprocesses**, and physical position matters. The source explicitly includes detector/electrical/computational examples. It does **not** claim that such a device has no physical constituents. |
| `mapping_direction` / `relation_kind` | Specific SensorML physical-process description pattern → V2 question ‘granularity of a description is not intrinsic physical divisibility’; `PARTIAL_OVERLAP`. PhysicalComponent is a **SensorML class/representation**, not the as-yet-unadopted universal Component of V2. |
| `reused_role` / `qualification_or_loss` | Allow a useful whole physical sensing device to be described without individual per-chip System resources; preserve detailed source parts where separately needed. Do not confuse SensorML PhysicalComponent with CSAPI System-subsystem resource standing or with Smart Citizen Rails `Component`. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` (§8.5.2/Req 31); formal source conditions `DONOR_TEXT`, mapping `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for source-qualified nonmandatory decomposition. **`adoption_status=NOT_ADOPTED`**. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST` — only scoped primary-text review and hypothetical semantic-loss checks. No audited vendor→Profile-constrained CSAPI data transformation, real individual equipment identity, implemented conformance tests or end-to-end client proof. |
| `donor_declarations` | `DECL-T04-01` is CSAPI's declared SensorML standard reference, **not** a 1:1 PhysicalComponent-to-System identity assertion. |
| `source_to_client_consequence` / `open_question` | One integrated sensing unit can have multiple meaningful outputs without requiring a hardware subtree. Open: source-specific granularity for actual hardware versus process substructure. |
| `record_provenance` | 28 October 2026; Step 07 direct source review, plus existing Pass 4 and I07/I10/I12 source-correction comparison. Research record v0.1; no owner model-adoption decision. |


### ALN-T04-A013-02 — SensorML PhysicalSystem/AggregateProcess: process topology need not be physical assembly

| Field | Source-qualified value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T04-A013-02 / TOPIC-04-COMPOSITION-COMPONENT-STANDING / *relation-to-whole, source-justified separately described standing, and non-equivalent representation/association roles*. This is a thematic research topic ID, **not** a DIM class. |
| `artifact_id` / `lineage` / `source_role` | **13** / OGC SensorML / primary anatomy evidence; core process/physical description and encoding donor. |
| `source_ed` / `source_concept` / `source_locator` | **OGC 23-000 SensorML 3.0, 16 July 2025**. [OGC SensorML 3.0 §§8.4.1, 8.6.2, Requirements 24 and 33](https://docs.ogc.org/is/23-000/23-000.html): `AggregateProcess` and `PhysicalSystem`. |
| `source_native_meaning` | `AggregateProcess` describes connected component processes, which may be physical or non-physical, with inputs/outputs and dataflow links. A `PhysicalSystem` describes hardware as an aggregate of one or more component processes, potentially combining sensors, actuators and computation. Connection of subprocesses describes **functional/process flow**, not automatically mechanical fastening, ownership or separate deployment. |
| `mapping_direction` / `relation_kind` | Source composite process and physical-process structure → candidate distinct *functional decomposition* from *physical/lifecycle part relation*; `PARTIAL_OVERLAP`. Process components may not be individually real hardware or CSAPI System features. |
| `reused_role` / `qualification_or_loss` | Preserve source's process wiring and computation when meaningful, while separately qualifying assembly membership, provenance and individual part identity. **Do not** use this report to model specific components or class hierarchy reserved outside Step 07. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` (SensorML §§8.4,8.6); source process/model meaning `DONOR_TEXT`, V2 separation `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for separation of dataflow and physical assembly. **`adoption_status=NOT_ADOPTED`**. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST` — only scoped primary-text review and hypothetical semantic-loss checks. No audited vendor→Profile-constrained CSAPI data transformation, real individual equipment identity, implemented conformance tests or end-to-end client proof. |
| `donor_declarations` | `DECL-T04-01`; no donor declaration that SensorML component connections encode CSAPI §10.2 Composition lifetime rules. |
| `source_to_client_consequence` / `open_question` | A future client may display a processing chain **if published**, without calling every stage a removable sensor. Open: what format/binding exposes process topology and its relation to specific equipment? |
| `record_provenance` | 28 October 2026; Step 07 direct source review, plus existing Pass 4 and I07/I10/I12 source-correction comparison. Research record v0.1; no owner model-adoption decision. |


### ALN-T04-A020-01 — 2017 SSN Recommendation has `ssn:hasSubSystem`, with hosting separate

| Field | Source-qualified value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T04-A020-01 / TOPIC-04-COMPOSITION-COMPONENT-STANDING / *relation-to-whole, source-justified separately described standing, and non-equivalent representation/association roles*. This is a thematic research topic ID, **not** a DIM class. |
| `artifact_id` / `lineage` / `source_role` | **20** / SOSA/SSN (2017 Recommendation) / companion/lineage evidence; published ontology edition cited by 2025 CSAPI; not a separate SOSA/SSN lineage vote. |
| `source_ed` / `source_concept` / `source_locator` | **W3C Recommendation, 19 October 2017**. [W3C SOSA/SSN Recommendation, 19 Oct 2017, §§4.9.2.2–4.9.2.6](https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/): `ssn:System`, `ssn:hasSubSystem`, `sosa:hosts`/`sosa:isHostedBy`, `ssn:Deployment`. |
| `source_native_meaning` | The 2017 Recommendation uses `ssn:System` for a unit of abstraction containing subordinate Systems and ***`ssn:hasSubSystem`*** for System-to-System component relations. It separately describes `sosa:hosts` / `sosa:isHostedBy` for a Platform hosting Sensors etc. The 2017 class/property names must not be rewritten as draft 2026 `sosa:System` / `sosa:hasSubSystem`. |
| `mapping_direction` / `relation_kind` | Published SSN subsystem predicate → candidate *some whole/part relations link System-level individuals*; `CLOSE_ALIGNMENT_WITH_QUALIFICATION`, edition-specific. CSAPI 2025's different ‘sosa:hasSubSystem’ Table 8 label is a **recorded edition/nomenclature mismatch**, not proof of formal published SSN axiom identity. |
| `reused_role` / `qualification_or_loss` | Preserve System-to-System relation and distinct Platform hosting. Do not treat every nested electronic/functional unit as `ssn:System` or infer permanence from hosting alone. 2017 and 2026 WD share a lineage, not two independent votes. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` (2017 §§4.9.2.2–4.9.2.6); class/predicate names `DONOR_TEXT`, edition comparison `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for stable conceptual distinction; not for cross-edition term substitution. **`adoption_status=NOT_ADOPTED`**. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST` — only scoped primary-text review and hypothetical semantic-loss checks. No audited vendor→Profile-constrained CSAPI data transformation, real individual equipment identity, implemented conformance tests or end-to-end client proof. |
| `donor_declarations` | `DECL-T04-01` & `DECL-T04-02` disclose the normative/reference and Table 8 naming issue. |
| `source_to_client_consequence` / `open_question` | An ontology-aware integration needs edition-aware predicates rather than assuming 2017 `ssn:hasSubSystem` and WD2026 `sosa:hasSubSystem` are literally the same published property. Open: eventual chosen semantic/URI binding edition. |
| `record_provenance` | 28 October 2026; Step 07 direct source review, plus existing Pass 4 and I07/I10/I12 source-correction comparison. Research record v0.1; no owner model-adoption decision. |


### ALN-T04-A019-01 — 2026 SOSA/SSN draft: subsystem System relation and optional complex-device viewpoint

| Field | Source-qualified value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T04-A019-01 / TOPIC-04-COMPOSITION-COMPONENT-STANDING / *relation-to-whole, source-justified separately described standing, and non-equivalent representation/association roles*. This is a thematic research topic ID, **not** a DIM class. |
| `artifact_id` / `lineage` / `source_role` | **19** / SOSA/SSN (2026 Working Draft) / primary anatomy evidence; current *draft* ontology edition, not the 2017 published dependency. |
| `source_ed` / `source_concept` / `source_locator` | **W3C/OGC OGC 25-022, Working Draft dated 21 October 2026**. [21 Oct 2026 Working Draft §§5.3.5.2.4, 5.3.5.2.9, 5.3.5.2.14, 8.15](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/). |
| `source_native_meaning` | Draft `sosa:hasSubSystem` links a `sosa:System` to component Systems, with `sosa:isSubSystemOf` inverse. Its §8.15 example models one packaged temperature/humidity device with **separately represented sensing Systems** for the functions. The example demonstrates a permitted semantic granularity, not a requirement that every multi-output IC become two independent managed physical devices. |
| `mapping_direction` / `relation_kind` | Draft's System-subsystem relation → candidate *explicit System-standing may be useful for meaningful functional internals*; `CLOSE_ALIGNMENT_WITH_QUALIFICATION` (source is a Working Draft, use-case decomposition is illustrative). |
| `reused_role` / `qualification_or_loss` | Keep class meaning distinct from CSAPI lifetime, sensor channel identity and source-authenticated equipment instances. A complex-device *illustration* cannot prove real SCK2.3 chip serials or mandate a CSAPI subsystem per measurable property. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` on dated **21 Oct 2026 Working Draft**; draft source predicates/examples `DONOR_TEXT`, mapping qualification `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `CANDIDATE_RECORDED` due to draft edition and nonmandatory example. **`adoption_status=NOT_ADOPTED`**. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST` — only scoped primary-text review and hypothetical semantic-loss checks. No audited vendor→Profile-constrained CSAPI data transformation, real individual equipment identity, implemented conformance tests or end-to-end client proof. |
| `donor_declarations` | `DECL-T04-03` for draft non-normative CSAPI mappings; `DECL-T04-04` for non-normative SAREF comparison. |
| `source_to_client_consequence` / `open_question` | Could render independently described subsystems when a producer actually asserts them; do not fabricate them from output channel labels. Open: intended 2026 draft final status and chosen resource/graph correspondence. |
| `record_provenance` | 28 October 2026; Step 07 direct source review, plus existing Pass 4 and I07/I10/I12 source-correction comparison. Research record v0.1; no owner model-adoption decision. |


### ALN-T04-A019-02 — 2026 SOSA/SSN draft: Platform hosting and Deployment are not ‘part of’ synonyms

| Field | Source-qualified value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T04-A019-02 / TOPIC-04-COMPOSITION-COMPONENT-STANDING / *relation-to-whole, source-justified separately described standing, and non-equivalent representation/association roles*. This is a thematic research topic ID, **not** a DIM class. |
| `artifact_id` / `lineage` / `source_role` | **19** / SOSA/SSN (2026 Working Draft) / primary anatomy evidence; current *draft* ontology edition, not the 2017 published dependency. |
| `source_ed` / `source_concept` / `source_locator` | **W3C/OGC OGC 25-022, Working Draft dated 21 October 2026**. [21 Oct 2026 Working Draft §§5.3.5.2.2–5.3.5.2.14](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/): `sosa:Deployment`, `sosa:hosts`, `sosa:isHostedBy`, `sosa:hasSubSystem`. |
| `source_native_meaning` | The draft distinguishes a System's constituent System relationship from **Platform hosting/mounting an Asset** and from a **Deployment** that describes operational arrangement. `sosa:hosts` and `sosa:isHostedBy` have Platform and hosted Asset participants, while `sosa:hasSubSystem` links Systems. None inherently asserts CSAPI's exact maintenance/interchange interval. |
| `mapping_direction` / `relation_kind` | Source's distinct hosting/deployment context → candidate independent *assembly vs operational hosting vs deployment* viewpoints; `PARTIAL_OVERLAP`. Hosting relation may coincide with assembly in a specific case but is not universally an enduring physical part-of predicate. |
| `reused_role` / `qualification_or_loss` | Retain contextual difference for an imager cueing a detector, a vehicle hosting a payload, or a Kit installed at a location; not every communication link, mount or accessory is a child System. **System/Platform can be multiple roles**, not mutually exclusive bins. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` on dated Working Draft §§5.3.5.2.2–14; source predicates `DONOR_TEXT`, example transfer `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `CANDIDATE_RECORDED`; no draft term required by the published 2025 CSAPI Profile. **`adoption_status=NOT_ADOPTED`**. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST` — only scoped primary-text review and hypothetical semantic-loss checks. No audited vendor→Profile-constrained CSAPI data transformation, real individual equipment identity, implemented conformance tests or end-to-end client proof. |
| `donor_declarations` | `DECL-T04-03` is a **selected non-normative correspondence** and does not collapse different source relationship roles. |
| `source_to_client_consequence` / `open_question` | Label hosting/deployment separately from built-in parts where known, and preserve uncertainty about fielded mounting. Open: temporal validity and real platform association evidence. |
| `record_provenance` | 28 October 2026; Step 07 direct source review, plus existing Pass 4 and I07/I10/I12 source-correction comparison. Research record v0.1; no owner model-adoption decision. |


### ALN-T04-A104-01 — OPC UA Devices: ComponentType spans physical Device and mechanical/software parts

| Field | Source-qualified value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T04-A104-01 / TOPIC-04-COMPOSITION-COMPONENT-STANDING / *relation-to-whole, source-justified separately described standing, and non-equivalent representation/association roles*. This is a thematic research topic ID, **not** a DIM class. |
| `artifact_id` / `lineage` / `source_role` | **104** / OPC UA Devices / primary anatomy evidence; device structure and industrial information-model viewpoint. |
| `source_ed` / `source_concept` / `source_locator` | **OPC 10000-100, release 1.05.0, published 15 November 2025**. [OPC UA Part 100 v1.05.0 §§1, 4.1, 4.6 and 4.9](https://reference.opcfoundation.org/specs/OPC-10000-100/full). |
| `source_native_meaning` | OPC UA Part 100 distinguishes **device information model**, **device communication model** and **device integration host model**. Abstract `ComponentType` supports Device or parts including mechanical **and software parts**. `DeviceSet` provides a root locating Devices; complex child Devices can be located via hierarchical references from the root. These are defined in the OPC UA AddressSpace, not a claim that every part is an independently maintained physical sensor. |
| `mapping_direction` / `relation_kind` | Source-native OPC component/device information-model structure → candidate ‘some separately representable constituent detail has source-specific kinds/identities’ with `PARTIAL_OVERLAP`; OPC AddressSpace ComponentType and physical equipment parts are **not coextensive**. |
| `reused_role` / `qualification_or_loss` | Keep device topology distinct from communication/network topology and management host. **OPC UA `ComponentType` ≠ Smart Citizen Rails `Component` ≠ physical IC ≠ CSAPI `System`**. The fact that a software part is a ComponentType in OPC cannot make it physical hardware. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` on official OPC UA Part 100 **release v1.05.0**; native structure `DONOR_TEXT`, cross-source caution `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for qualified structure/identity distinctions. **`adoption_status=NOT_ADOPTED`**. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST` — only scoped primary-text review and hypothetical semantic-loss checks. No audited vendor→Profile-constrained CSAPI data transformation, real individual equipment identity, implemented conformance tests or end-to-end client proof. |
| `donor_declarations` | No direct OPC→CSAPI semantic equivalence statement found in the **named inspected clauses**; `NONE_FOUND_IN_CHECKED_CLAUSE`. |
| `source_to_client_consequence` / `open_question` | Potentially show device, mechanical and software constituent views if original source distinguishes them; don't equate UA hierarchies or API named objects with verified physical assembly. Open: which hierarchies/NodeIds identify actual fielded hardware? |
| `record_provenance` | 28 October 2026; Step 07 direct source review, plus existing Pass 4 and I07/I10/I12 source-correction comparison. Research record v0.1; no owner model-adoption decision. |


### ALN-T04-A104-02 — OPC UA Modular Device top Device/SubDevices: ‘aggregation’ is not CSAPI Aggregation

| Field | Source-qualified value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T04-A104-02 / TOPIC-04-COMPOSITION-COMPONENT-STANDING / *relation-to-whole, source-justified separately described standing, and non-equivalent representation/association roles*. This is a thematic research topic ID, **not** a DIM class. |
| `artifact_id` / `lineage` / `source_role` | **104** / OPC UA Devices / primary anatomy evidence; device structure and industrial information-model viewpoint. |
| `source_ed` / `source_concept` / `source_locator` | **OPC 10000-100, release 1.05.0, published 15 November 2025**. [OPC UA Part 100 v1.05.0 §§9.2.1, 9.4](https://reference.opcfoundation.org/specs/OPC-10000-100/9.4): Modular Devices, `SubDevices` and `SupportedTypes`. |
| `source_native_meaning` | A Modular Device has a top-Device and configurable SubDevices/modules; a SupportedTypes collection describes permitted module types and some modules may be preconfigured/instantiated. SubDevices can themselves be modular. The source speaks of modules **‘aggregated’ under SubDevices**, as an OPC modeling/AddressSpace arrangement—not CSAPI §10.2's declared lifetime distinction. |
| `mapping_direction` / `relation_kind` | Source's configurable modular Device structure → candidate *documented interchangeable/supportable versus installed module standing*; `PARTIAL_OVERLAP`, not automatic CSAPI Composition/Aggregation equivalence. |
| `reused_role` / `qualification_or_loss` | Separate *supported module types* from a particular module's installed identity and temporally changing relationships. A configuration model does not establish that an identified PM module was actually swapped, nor that each submodule is a CSAPI System. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` (official Part 100 §§9.2.1,9.4); OPC terms `DONOR_TEXT`, CSAPI comparison `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for modularity-versus-instance qualification. **`adoption_status=NOT_ADOPTED`**. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST` — only scoped primary-text review and hypothetical semantic-loss checks. No audited vendor→Profile-constrained CSAPI data transformation, real individual equipment identity, implemented conformance tests or end-to-end client proof. |
| `donor_declarations` | `NONE_FOUND_IN_CHECKED_CLAUSE` for OPC-to-CSAPI semantic equality. |
| `source_to_client_consequence` / `open_question` | Display known supported module types separately from verified installed modules where evidence exists. Open: who identifies an installed module, its replacement lifecycle and mapping to independent Systems? |
| `record_provenance` | 28 October 2026; Step 07 direct source review, plus existing Pass 4 and I07/I10/I12 source-correction comparison. Research record v0.1; no owner model-adoption decision. |


### ALN-T04-A144-01 — SAREF `consistsOf` is a broad composite relation, not only hardware assembly

| Field | Source-qualified value |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T04-A144-01 / TOPIC-04-COMPOSITION-COMPONENT-STANDING / *relation-to-whole, source-justified separately described standing, and non-equivalent representation/association roles*. This is a thematic research topic ID, **not** a DIM class. |
| `artifact_id` / `lineage` / `source_role` | **144** / ETSI SAREF Core / primary anatomy evidence; device and composite semantic viewpoint. |
| `source_ed` / `source_concept` / `source_locator` | **ETSI SAREF Core v4.1.1 (ontology date 31 October 2024)**. [ETSI SAREF Core v4.1.1, ‘Composite Properties and Property Values’ and ‘saref:consistsOf’ definition](https://saref.etsi.org/core/v4.1.1/). |
| `source_native_meaning` | `saref:consistsOf` relates composite entities to constituents; its example includes a temperature/humidity device containing two sensing concepts. But the predicate also combines **feature types, properties, states, property values and state values** in other source sections. It does not by itself fix mechanical attachment, physical unit identity, maintenance lifetime or the CSAPI §10.2 Representation choice. |
| `mapping_direction` / `relation_kind` | SAREF's general composite relation → narrower candidate relation question ‘equipment contains physically meaningful constituents’; `SOURCE_BROADER` because the source predicate covers many non-equipment composites beyond our physical/lifecycle issue. |
| `reused_role` / `qualification_or_loss` | Inspect subject/object types before asserting equipment part-of. SAREF uses the same English property for semantic composites of outputs/values; not every `consistsOf` is a physical child System. Its compound temperature/humidity example cannot prove one physical transducer per named channel. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` in exact v4.1.1 official ontology; donor semantics `DONOR_TEXT`, directional source-broader comparison `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for typed-composition warning; not as universal physical assembly encoding. **`adoption_status=NOT_ADOPTED`**. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST` — only scoped primary-text review and hypothetical semantic-loss checks. No audited vendor→Profile-constrained CSAPI data transformation, real individual equipment identity, implemented conformance tests or end-to-end client proof. |
| `donor_declarations` | `DECL-T04-04` is the 2026 **draft's** one-way alignment toward `saref:consistsOf`; SAREF has **not** directly declared every `consistsOf` equivalent to `sosa:hasSubSystem`. |
| `source_to_client_consequence` / `open_question` | A SAREF-aware view should not label composite properties/measurement values as removable equipment components. Open: explicit equipment-subject typing and relation lifetime where needed. |
| `record_provenance` | 28 October 2026; Step 07 direct source review, plus existing Pass 4 and I07/I10/I12 source-correction comparison. Research record v0.1; no owner model-adoption decision. |

## 3. Explicit **source-declared** relationships (not assumed consensus)

These four statements were checked **in the declaring source**. They are not independent ‘votes’ or indications that whole standards are equivalent, and their **edition/authority** matters.

| Declaration ID | Declaring source and exact locator | Narrow source-owned statement | What it **does not** establish |
| --- | --- | --- | --- |
| **`DECL-T04-01`** | **ID 10**, [CSAPI Part 1 v1.0 §3 Normative References](https://docs.ogc.org/is/23-001/23-001.html) | Cites the **19 October 2017 SOSA/SSN Recommendation (ID 20)** and **SensorML 3.0 (ID 13)**. | A normative reference is **not** a claim of equal component semantics; does not adopt the October 2026 WD predicates into the published edition or identify every physical chip as System. |
| **`DECL-T04-02`** | **ID 10**, [CSAPI Part 1 §10.3.2 Table 8](https://docs.ogc.org/is/23-001/23-001.html) | The CSAPI `parentSystem` association's SOSA/SSN correspondence column gives ‘inverse Of `sosa:hasSubSystem`’. | **Edition-sensitive naming:** the independently inspected **2017 Recommendation ID 20** instead uses `ssn:hasSubSystem` and `ssn:System`. Preserve CSAPI's literal table and the original 2017 terms **without** asserting they are one identical published ontology IRI. |
| **`DECL-T04-03`** | **ID 19**, [21 October 2026 SSN Working Draft §7.3.1, Table 15 (non-normative)](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/) | Lists selected correspondences `System.subsystems` → `sosa:hasSubSystem` and subsystem `parentSystem` → `sosa:isSubSystemOf`, alongside other CSAPI associations. | Draft authors explicitly call these **selected conceptual correspondences, not formal OWL equivalence axioms**. No retroactive rewriting of CSAPI 2025 or published SSN 2017, and no rule that nested discovery proves permanence. |
| **`DECL-T04-04`** | **ID 19**, [21 October 2026 SSN Working Draft §7.2.1.2 within non-normative §7.2](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/) | Its **proposed one-way alignment** says `sosa:hasSubSystem ⊑ saref:consistsOf` and also references `s4syst:hasSubSystem`. | A draft author's **narrower-than** alignment does not make every SAREF `consistsOf` statement an SSN subsystem, does not establish the target SAREF/SAREF4SYST edition as independently reviewed, and is not normative mutual conformance. The SAREF version **actually** inspected in this step is v4.1.1 (ID 144). |

**Additional contrasts here are *our* comparisons:** OPC UA's ‘aggregated SubDevices’ versus CSAPI §10.2 Aggregation; SensorML component-process dataflow versus physical fastening; SAREF's composite property values versus hardware; software `Component` versus a CSAPI subsystem. None was found to be formally declared equivalent in the **named** relevant clauses. Lack of a declaration in a checked clause is not proof no such relationship exists anywhere in the 182-artifact corpus.

## 4. Adversarial Smart Citizen source-to-standard checks: product design ≠ physical instance

These are **negative semantic fidelity checks**, carried forward from I07, I10 and I12 and re-grounded in manufacturer/backend files pinned by the closed case study. They are **not** newly executed transformations and do not show a hardware unit exists or is installed.

| Check | Direct source evidence | Forbidden inference | Safe scoped result / future client implication |
| --- | --- | --- | --- |
| **C04-A — cabled PM module *inside* ordinary kit assembly** | [Pinned Smart Citizen Kit 2.3 assembly, PM inserted in clip and connected via cable, lines 121–147](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/guides/getting-started/kit-assembly.md#L121-L147), plus [Urban Board PM connector and sensor table](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/boards/urban-board.md#L31-L59). | Cable → *external / temporarily deployed* Sensor; or normal assembly → *provably lifetime-permanent* Composition. | **Product-design relationship supported:** distinct detachable module placed **inside normal Kit enclosure** in source assembly. **Real individual, installed SEN50/54/55 variant, permanence and prior swaps NOT VERIFIED.** Do not choose CSAPI Aggregation/Deployment merely because cabled. |
| **C04-B — two physical ICs expose multiple measurement channels** | [Pinned Urban Board 2.3 sensor table, lines 47–59](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/boards/urban-board.md#L47-L59): **SHT31 → temperature and relative humidity; AS7331 → UV-A/B/C**. | Every channel → separate mounted chip, independently identified sensor/System, or one required Datastream per channel. | **Multiple output roles per physical component design** supported. How to group or provenance-record outputs requires actual producer, observed properties and stream schema; no physical chip serial or runtime observation verified. |
| **C04-C — Data Board / Urban Board separately described, not established System children** | [Pinned Data Board modular Sensor Board connector/replacement, lines 58–64](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/boards/data-board.md#L58-L64); [I07 CMP02–CMP03](../Case_Studies/Real_Equipment_DIM_Validation/I07_Composition_and_Component_Standing_Mapping_v0.1_28OCT2026.md). | Replaceable board → temporary operational payload; separate design document → authenticated standalone physical System. | **Distinct board-level descriptive standing**; no demonstrated independently registered or managed CSAPI System for either board and no actual replacement event. |
| **C04-D — backend `Component` is a database association** | [Pinned Smart Citizen API `Component` model, lines 1–7](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/app/models/component.rb#L1-L7), [component presenter, lines 10–27](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/app/lib/presenters/component_presenter.rb#L10-L27); explicit correction [I10 D01](../Case_Studies/Real_Equipment_DIM_Validation/I10_Model_View_Critical_Check_and_Gate_C_v0.1_28OCT2026.md). | Each API `Component` → physical IC, replaceable mechanical part, one uniquely identified channel or CSAPI System. | **Directly rejected false mapping (I12 X04)**: Rails `Component` belongs to Device and Sensor definitions and exposes readings. **Do not** make one-to-one chip or one-channel assertions from the software object. |
| **C04-E — optional auxiliary connector is not installed payload** | [Pinned Data Board §Auxiliary connector, lines 58–64](https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/docs/hardware/boards/data-board.md#L58-L64); [I07 CMP09](../Case_Studies/Real_Equipment_DIM_Validation/I07_Composition_and_Component_Standing_Mapping_v0.1_28OCT2026.md). | Supported attachment port → already installed module, dated Deployment or distinct managed System. | **Product capability** supported; attached unit, relationship duration and unique device identity unknown. |
| **C04-F — nested discovery versus true datastream producer** | [CSAPI Part 1 §10.5 Req 9(C) and §10.7 Req 13](https://docs.ogc.org/is/23-001/23-001.html); [CSAPI Part 2 §9.2.2 Table 5](https://docs.ogc.org/is/23-002/23-002.html); [I12 X02–X03/C12-02–03](../Case_Studies/Real_Equipment_DIM_Validation/I12_Critical_Interoperability_Challenge_v0.1_28OCT2026.md). | Nested child visible → permanently integral; parent-linked datastream → parent actually measured each member observation. | Both shortcuts are **false** under published CSAPI. Resource discovery and producing-System provenance must remain distinct; this is a standards-level check, not a real populated CSAPI implementation. |

### What the cases **do not** establish

The closed Smart Citizen project has **product/design and pinned backend-code evidence**, but not a validated **individual SCK2.3** linked to an actual live platform record, physical module serials, real installed SEN5X type, lifecycle events, actual DataStreams or a source-to-CSAPI transform. Manufacturer design **alternatives** and software paths cannot substitute for actual inventory, location, state, readings or configuration. The case study's Gate D was **conditional acceptance of the written report only**. Nor has this step verified TRSS/OmniSense transducer identities; their archived source examples retain the S04 YELLOW ceiling.

The controlled output is thus a set of **candidate meaning and counterexamples** for a future Profile and UI, *not* a component hierarchy instantiated for a fielded Kit.

## 5. Open questions and next bounded handoff

1. **Identity/standing threshold:** what real source identifiers, operational roles, independently managed condition or lifecycle justify exposing a given physical part as a full CSAPI System, versus a source-qualified element in one SensorML equipment description? No universal policy adopted.
2. **Relation temporality:** how to represent an installed part that is normally integrated but serviceable/removable, or a temporarily attached payload, when replacement/deployment history is unavailable? CSAPI's permissive classification requires source-backed judgment.
3. **Functional channels:** how to distinguish measurement properties and logical/firmware processing from hardware topology in a vendor-independent presentation, while correctly honoring Part 2 stream grouping and producer associations?
4. **Source editions and explicit donor relationships:** the 2017 `ssn:hasSubSystem` versus CSAPI Table 8/draft 2026 `sosa:hasSubSystem` discrepancy is open for **future formal binding**; do not silently choose one URI. Draft §7.2's proposed subproperty-to-SAREF mapping is expressly non-normative and directional.
5. **Physical versus digital representations:** this step names one documented vendor software/physical ‘Component’ collision **only** to avoid false hardware mapping. **The full digital representation/proxy-identity research is Step 08**, not performed now.

### Step 07 exit checks

| Check | Evidence-grounded outcome |
| --- | --- |
| Single Step 07 scope | **PASS** — composition, component standing, hosting, functional channel and source-specific software Component counterexample; Step 08 held |
| Frozen source IDs | **PASS** — **7 distinct IDs** from existing 182 register: 10, 11, 13, 19, 20, 104, 144; **13** record IDs; five lineages, no independently invented source |
| Native source/edition and directional mapping | **PASS** — exact source sections/URI and qualified relation type; published 2017 ontology distinguished from 2026 WD, OPC Part 100 v1.05.0 and SAREF v4.1.1 pinned |
| Source-declared versus inferred | **PASS** — four exact declaration records; WD 2026 §7.2 & §7.3 non-normative and source-specific; semantic equality **not** established |
| Smart Citizen adversarial checks | **PASS for evidence-rejection of six misleading interpretations**, not actual device conversion; correct cabled PM, shared IC, backend `Component` and recursive parent stream traps retained |
| Standing and implementation proof | **All `NOT_ADOPTED`; all `NO_TRANSFORMATION_TEST`**. No DIM classes, universal Component superclass, UML mandatory diamonds, Profile SHALLs, site commits, end-to-end test or physical identity claims |
| Evidence limits and unresolved issues | **RECORDED** — documentation versus individual unit, future lifecycle granularity, equipment/dataflow/source-semantic mismatch and 2017/2026 ontology crosswalk disagreement |

**Value toward eventual DIM/Profile/client:** The source-qualified whole–part distinction can support truthful System Details organization *without* forcing a uniform physical component metamodel: show documented **internal parts and channels** with their genuine level of evidence, show **full child System resources only where justified**, and keep **hosted/deployed equipment**, **logical outputs**, **software records** and **true measurement producers** distinct. It does not yet demonstrate donor-wide interoperability or prove a finished universal model.

**STOP. Next, only after the user's next plain “proceed”: Step 08 — Digital Representation / Proxy Identity donor alignment.** Reuse Canonical Pass 5 and existing I08/I10 evidence; examine physical equipment versus resource, proxy, digital twin, service and software Device–Sensor association. Do **not** begin Step 08 within this iteration or adopt new model classes or Profile requirements.
