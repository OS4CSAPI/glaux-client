# Donor Alignment — Step 06: Procedure / Method

**Version:** 0.1 · **28 October 2026**  
**Plan:** [Controlled Donor Alignment and Foundational DIM Construction](../PLAN_DIM_Profile_V2_Donor_Alignment_and_Foundation_v0.1_28OCT2026.md), **Step 06 only**.  
**Status:** **COMPLETE as an evidence-qualified, bounded semantic alignment exercise**. **NOT** an adopted DIM class, final model anatomy, normative CSAPI application Profile, conformance result, or operational data transformation.  
**Research branch:** `OS4CSAPI/glaux-client` / `research/dim-profile-v2`. No site, app code, synthetic fixtures or original 182-source ledgers changed.
**Controlling input:** [Pass 3 — Procedure/Method](../DIM_Profile_V2_Canonical_Concept_Pass3_Procedure_Method_v0.1_26OCT2026.md), [C08 CSAPI correction](../DIM_Profile_V2_Anatomy_PhaseA_Validation_Audit_v0.1_26OCT2026.md), [Step 02 alignment method](02_Register_Method_and_Schema.md), [Step 03 source snapshot](03_Source_Accountability_Register.csv), [Step 04 identity](04_Individual_System_Identity_Alignment_v0.1_28OCT2026.md) and [Step 05 product/kind](05_Product_Model_Kind_Alignment_v0.1_28OCT2026.md).

## 1. Bounded finding in plain language

**Which method can a particular sensing System perform, and which method did a particular event actually use?** These are *separate questions* from what the System's **manufacturer model/kind** is, and from the **result** of an occurrence. Original sources support distinct meanings for:

1. **Reusable System kind/datasheet**: what kind of System a particular unit is, not automatically an algorithm the unit performed.
2. **Reusable Procedure/Method**: a specification or protocol describing *how* something is done, sometimes with input/output/algorithm/configuration detail, possibly reusable across individual Systems.
3. **System implements / is capable of Procedure**: a supported method or implementable behavior, **not proof of performance**.
4. **Actual Observation/Execution used Procedure**: a claim about a *particular occurrence*, distinct from the producer and its general capabilities.
5. **Result and execution-specific settings**: values and parameters associated with that occurrence; a Procedure description does not itself generate evidence of the occurrence or a valid result.

**Key C08 correction:** Published CSAPI Part 1 can encode both kind/datasheet and method in a `Procedure` feature, but it distinguishes `System.systemKind` from `System.procedures` **by association meaning**. CSAPI Part 2 further distinguishes `DataStream.procedure` from `Observation.procedure` and provides observation-level `parameters` and `result`. This is **one carrier used for different information roles**, not a license to equate every source's concept named "Procedure" or invent separate mandatory DIM classes.

**Candidate meaning, not adopted class text:** *A System can be associated with descriptions of reusable methods it can perform. If source evidence supports a particular Observation or other act, the method actually used, the executing System, any context-specific parameters and the result must remain semantically distinguishable. The method can be represented at different levels of detail and in different donor-native forms; a kind/model description is not automatically that method.* This is V2 analyst synthesis supported only within the cited donor clauses; it is not a universal cardinality, mandatory property, ontology axiom, completed transformation or new `SystemMethod`/`ProcedureExecution` class.

**Scope and counts:** **10 alignment records** (below) from **six frozen artifact IDs: 8, 10, 11, 13, 19, 20**. These represent **four research lineages** (OMS, Connected Systems, SensorML, SOSA/SSN), **not six independent standards/votes**: ID 11 is a CSAPI companion part and ID 20 the published 2017 SOSA/SSN lineage companion to the 2026 Working Draft ID 19. All six IDs were checked against the frozen [182-source accountability register](03_Source_Accountability_Register.csv); no new artifact ID is assigned or prior register row edited. The new detailed notes, rather than the still-frozen Step 03 snapshot's initial `NOT_ASSESSED` column, control these **topic-specific** review standings.

**Source ceiling:** Direct primary HTML checked for CSAPI Parts 1–2, SensorML 3.0 and fixed 2017 and 21 October 2026 SOSA/SSN editions. The official OMS 3.0 web document's complete HTML was too large for the research reader; exact official indexed subsections and requirement text were inspectable. The OMS record is expressly `SOURCE_ACCESS_LIMITED`/`CANDIDATE_RECORDED`, **not** a claim of full-document examination. No other topic or donor source is declared assessed by these ten records.

## 2. Source-concept → candidate-meaning alignment records

Every record follows the [Step 02 controlled format](02_Register_Method_and_Schema.md#4-minimal-detailed-alignment-record-format--steps-0408). The source-native statements and the V2 researcher's directional comparisons are deliberately distinguished. Where a citation is a source declaration, it is numbered separately in §3. No alignment implies conformance to all six donors. All records are `NOT_ADOPTED` and `NO_TRANSFORMATION_TEST`.


### ALN-T03-A010-01 — CSAPI Part 1: System `procedures` is not `systemKind`

| Field | Evidence-qualified entry |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T03-A010-01 / TOPIC-03-PROCEDURE-METHOD / source-qualified reusable Method, capability relation, actual use and distinct result. |
| `artifact_id` / `lineage` / `source_role` | **10** / OGC Connected Systems Part 1 / core structural donor; primary anatomy evidence; API/resource model. |
| `source_ed` / `source_concept` / `source_locator` | [OGC 23-001, Part 1 v1.0](https://docs.ogc.org/is/23-001/23-001.html), §9.2.2 Table 5: `System.procedures` versus `System.systemKind`. |
| `source_native_meaning` | `procedures` optionally associates a System with a list of Procedure descriptions it can implement; `systemKind` optionally associates it with a single Procedure describing the *kind* of System (e.g., datasheet). The two association meanings and target cardinalities differ even though the carrier resource type is shared. |
| `mapping_direction` / `relation_kind` | Source's System–implementable-Procedure association → candidate role ‘individual System is capable of a described method’; `CLOSE_ALIGNMENT_WITH_QUALIFICATION`. Source's `systemKind` is a **different relationship**, preserved in Step 05 rather than recast as a method. |
| `reused_role` / `qualification_or_loss` | Preserve source-backed capability/method role, the optionality and the distinct kind-association. Do not read a populated `procedures` association as proof of any particular historical execution; absence is not proof of no capability. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for the cited table; source relation is `DONOR_TEXT`, comparison and fidelity implications `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for the distinction / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`. This is a qualified semantic comparison only; no live source→profile-constrained CSAPI→client transformation, functional interchange, complete donor-standard conformance or Profile conformance was tested. |
| `donor_declarations` | `DECL-T03-01`, `DECL-T03-02` (qualified standard references, not equation of individual terms). |
| `source_to_client_consequence` / `open_question` | Show ‘Procedures this System can implement’ separately from ‘Model/datasheet’ if the producer supplies evidence; do not label supported methods as performed. Open: will a future Profile specify preferred relations and fallback behavior for omitted `procedures`? |
| `record_provenance` | 28 October 2026; bounded Step 06 original-edition inspection and project Pass 3 comparison; record v0.1; analyst-written research, not owner approval. |


### ALN-T03-A010-02 — CSAPI Part 1: one `Procedure` resource carrier serves specifications and methodologies

| Field | Evidence-qualified entry |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T03-A010-02 / TOPIC-03-PROCEDURE-METHOD / source-qualified reusable Method, capability relation, actual use and distinct result. |
| `artifact_id` / `lineage` / `source_role` | **10** / OGC Connected Systems Part 1 / core structural donor; primary anatomy evidence; API/resource model. |
| `source_ed` / `source_concept` / `source_locator` | [OGC 23-001, Part 1 v1.0](https://docs.ogc.org/is/23-001/23-001.html), §§13.1–13.2, esp. Tables 14–16 (`procedureType`, `implementingSystems`, sensor datasheet versus observing/sampling/actuating methods). |
| `source_native_meaning` | A `Procedure` feature can provide a reusable system-type specification/datasheet **or** a methodology used by a System. `procedureType` is a required URI in the source's Procedure resource model; Table 16 includes both method-role and equipment-datasheet categories. `implementingSystems` links back to implementing Systems optionally. |
| `mapping_direction` / `relation_kind` | Source's broad, role-dependent `Procedure` carrier → candidate reusable method meaning; `PARTIAL_OVERLAP`. A method fits the carrier, but not every Procedure resource in this API represents a method. |
| `reused_role` / `qualification_or_loss` | Preserve actual *relation role* and `procedureType` rather than assume all Procedure resources are identical procedures. These are **CSAPI-specific API rules**, not mandatory DIM-wide structure or an accepted new `ProductModel`/`ProcedureMethod` split. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for §§13.1–13.2 and Tables 14–16; semantic content `DONOR_TEXT`, V2 comparison `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for the disambiguation / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`. This is a qualified semantic comparison only; no live source→profile-constrained CSAPI→client transformation, functional interchange, complete donor-standard conformance or Profile conformance was tested. |
| `donor_declarations` | `DECL-T03-01`, `DECL-T03-02`. |
| `source_to_client_consequence` / `open_question` | Treat kind/datasheet, observing methodology, sampling methodology and actuation methodology as *qualified presentations* instead of one generic ‘Procedures’ list. Open: when/how should producer descriptions expose overlapping documentation and stable method versions? |
| `record_provenance` | 28 October 2026; bounded Step 06 original-edition inspection and project Pass 3 comparison; record v0.1; analyst-written research, not owner approval. |


### ALN-T03-A011-01 — CSAPI Part 2: `DataStream.procedure` is a stream-level method association

| Field | Evidence-qualified entry |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T03-A011-01 / TOPIC-03-PROCEDURE-METHOD / source-qualified reusable Method, capability relation, actual use and distinct result. |
| `artifact_id` / `lineage` / `source_role` | **11** / OGC Connected Systems Part 2 / core structural donor; primary anatomy evidence; dynamic-data companion, not a separate chassis vote. |
| `source_ed` / `source_concept` / `source_locator` | [OGC 23-002, Part 2 v1.0](https://docs.ogc.org/is/23-002/23-002.html), §9.2.2 Table 5 (`DataStream.procedure`); see §9.7.1 for factoring common properties at stream level. |
| `source_native_meaning` | The optional `procedure` association of a DataStream identifies a single Procedure used to generate its observations. A DataStream groups related observations and shares information that need not be duplicated on every member Observation. |
| `mapping_direction` / `relation_kind` | Source's collection/stream-level *used Procedure* → candidate ‘method used in making observations’; `PARTIAL_OVERLAP` because this is a stream/collection-scoped association, not a one-to-one historical method-use event record. |
| `reused_role` / `qualification_or_loss` | Retain which resource **asserts** the used method; do not silently turn the stream association into evidence about an unrelated device, unlinked observation, detailed per-sample settings or an independent runtime trace. Do not infer an automatic precedence rule if an observation has its own Procedure. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for §9.2.2 Table 5 and §9.7.1; carrier semantics `DONOR_TEXT`, projection caution `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for source-scoped relationship distinction / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`. This is a qualified semantic comparison only; no live source→profile-constrained CSAPI→client transformation, functional interchange, complete donor-standard conformance or Profile conformance was tested. |
| `donor_declarations` | `DECL-T03-03` (draft SSN selected correspondence, not OWL equivalence). |
| `source_to_client_consequence` / `open_question` | If available, display ‘Method associated with this datastream’ with the source and scope labeled. Open: how should a client communicate any difference between stream-level and individual-observation procedure references? |
| `record_provenance` | 28 October 2026; bounded Step 06 original-edition inspection and project Pass 3 comparison; record v0.1; analyst-written research, not owner approval. |


### ALN-T03-A011-02 — CSAPI Part 2: an individual Observation may identify its used method and parameters

| Field | Evidence-qualified entry |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T03-A011-02 / TOPIC-03-PROCEDURE-METHOD / source-qualified reusable Method, capability relation, actual use and distinct result. |
| `artifact_id` / `lineage` / `source_role` | **11** / OGC Connected Systems Part 2 / core structural donor; primary anatomy evidence; dynamic-data companion, not a separate chassis vote. |
| `source_ed` / `source_concept` / `source_locator` | [OGC 23-002, Part 2 v1.0](https://docs.ogc.org/is/23-002/23-002.html), §§9.7.1–9.7.2, Tables 6–7: `Observation.procedure`, `Observation.parameters` and `Observation.result`. |
| `source_native_meaning` | For an individual Observation, the optional `procedure` association identifies the Procedure **used to make that observation**; optional `parameters` explain how it was used on this occasion. The Observation's `result` represents estimated observed-property values and is required in the source model. Observations belong to a DataStream. |
| `mapping_direction` / `relation_kind` | Source Observation's *actual method-use relation* → candidate ‘a particular execution used a reusable Procedure’; `CLOSE_ALIGNMENT_WITH_QUALIFICATION`. Source `Observation` is not a general-purpose execution record for all acts and Part 2's links are optional. |
| `reused_role` / `qualification_or_loss` | Separate documented method, occurrence-level parameters, and result. Neither a documented product method nor a bare observation value supplies an unsupported execution-method join. No new result class, event log or profile cardinality follows. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for §9.7.2 Tables 6–7; terms `DONOR_TEXT`, candidate comparison `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for method-use/result distinction / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`. This is a qualified semantic comparison only; no live source→profile-constrained CSAPI→client transformation, functional interchange, complete donor-standard conformance or Profile conformance was tested. |
| `donor_declarations` | `DECL-T03-03` applies only to the selected datastream/controlstream correspondences explicitly tabulated in the 2026 draft, **not** a blanket draft-backed assertion for every Observation record. |
| `source_to_client_consequence` / `open_question` | When actual observation resources expose source evidence, show ‘Method used’ and per-observation parameters alongside the corresponding result, not as the System's standing product capabilities. Open: what if method is present only at stream level or omitted entirely? |
| `record_provenance` | 28 October 2026; bounded Step 06 original-edition inspection and project Pass 3 comparison; record v0.1; analyst-written research, not owner approval. |


### ALN-T03-A013-01 — SensorML 3.0: `ProcessMethod` describes method for a `SimpleProcess`

| Field | Evidence-qualified entry |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T03-A013-01 / TOPIC-03-PROCEDURE-METHOD / source-qualified reusable Method, capability relation, actual use and distinct result. |
| `artifact_id` / `lineage` / `source_role` | **13** / OGC SensorML / core structural donor; primary anatomy evidence; process/information encoding. |
| `source_ed` / `source_concept` / `source_locator` | [OGC 23-000 SensorML 3.0](https://docs.ogc.org/is/23-000/23-000.html), §§8.3.1–8.3.2, Requirements 19–20; related core inputs/outputs/parameters in §§7.1–7.2. |
| `source_native_meaning` | A `SimpleProcess` is used when a defined input/output processing function is not to be further divided; the SimpleProcess model requires support for a method. `ProcessMethod` describes how inputs and parameters produce outputs, with textual methodology and optional algorithm/implementation references. Access to a full method can be legally or security restricted. |
| `mapping_direction` / `relation_kind` | Source's SimpleProcess/ProcessMethod detailed mechanism → candidate reusable methodology; `SOURCE_NARROWER`: it addresses a particular SensorML process pattern rather than all real-world procedures, including purely manual observing protocols. |
| `reused_role` / `qualification_or_loss` | Useful candidate representation for detailed processing, but do not require a `ProcessMethod` object for every hardware function, all types of SensorML process, or an ordinary CSAPI System. Information that is protected or unavailable stays unavailable. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for exact sections and requirements; native conditions `DONOR_TEXT`, generalization limit `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for qualified process-detail viewpoint / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`. This is a qualified semantic comparison only; no live source→profile-constrained CSAPI→client transformation, functional interchange, complete donor-standard conformance or Profile conformance was tested. |
| `donor_declarations` | `DECL-T03-02` for CSAPI's stated SensorML relationship; NOT an asserted one-to-one mapping of `ProcessMethod` to every CSAPI `Procedure`. |
| `source_to_client_consequence` / `open_question` | A client might display a known algorithm, explanatory method text and external method URI when actually exposed; absence of a published algorithm is not evidence the equipment has no method. Open: method confidentiality, links, revision and parameter provenance. |
| `record_provenance` | 28 October 2026; bounded Step 06 original-edition inspection and project Pass 3 comparison; record v0.1; analyst-written research, not owner approval. |


### ALN-T03-A013-02 — SensorML 3.0: aggregate processing/dataflow is another way to describe methodology

| Field | Evidence-qualified entry |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T03-A013-02 / TOPIC-03-PROCEDURE-METHOD / source-qualified reusable Method, capability relation, actual use and distinct result. |
| `artifact_id` / `lineage` / `source_role` | **13** / OGC SensorML / core structural donor; primary anatomy evidence; process/information encoding. |
| `source_ed` / `source_concept` / `source_locator` | [OGC 23-000 SensorML 3.0](https://docs.ogc.org/is/23-000/23-000.html), §§7.1–7.2, 8.4.1; AggregateProcess requirements and component/dataflow description. |
| `source_native_meaning` | An `AggregateProcess` is built from component processes with explicit mappings of dataflow between them. Components may be physical or nonphysical; its approach describes behavior through connected process structure, not necessarily through one stand-alone `ProcessMethod` block. |
| `mapping_direction` / `relation_kind` | Source's aggregate-processing structure → candidate meaning ‘methodology may be represented by a reproducible structure’; `PARTIAL_OVERLAP` because a process network is not interchangeable with a textual observing protocol or one isolated method resource. |
| `reused_role` / `qualification_or_loss` | This is a methodological representation option; preserve its topology, inputs and outputs if supported, but **composition/component standing is deliberately reserved for Step 07**. No source-supported claim that all components are separately managed Systems. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for §8.4.1; method/generalization comparison `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `CANDIDATE_RECORDED` / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`. This is a qualified semantic comparison only; no live source→profile-constrained CSAPI→client transformation, functional interchange, complete donor-standard conformance or Profile conformance was tested. |
| `donor_declarations` | `DECL-T03-02` is standard-family provenance only. |
| `source_to_client_consequence` / `open_question` | Prevent flattening a documented process chain into a made-up single algorithm. Open: could a later Profile link qualified aggregate SensorML descriptions in a way a client can navigate? No binding decided. |
| `record_provenance` | 28 October 2026; bounded Step 06 original-edition inspection and project Pass 3 comparison; record v0.1; analyst-written research, not owner approval. |


### ALN-T03-A008-01 — OMS 3.0: `Procedure`, `ObservingProcedure`, `Observer`, `Observation` and result

| Field | Evidence-qualified entry |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T03-A008-01 / TOPIC-03-PROCEDURE-METHOD / source-qualified reusable Method, capability relation, actual use and distinct result. |
| `artifact_id` / `lineage` / `source_role` | **8** / OGC OMS / cross-cutting structural donor; primary anatomy evidence; conceptual/domain model. |
| `source_ed` / `source_concept` / `source_locator` | [OGC 20-082r4 / ISO 19156:2023, OMS v3.0.0](https://docs.ogc.org/as/20-082r4/20-082r4.html), §§8.2.2, 8.2.9, 8.3.2, 8.4.2, 8.5.2, 8.6.2 and (for the migration warning) Annex C.5.3. Official indexed exact-section text inspected; full HTML retrieval exceeded the reader's content-size limit. |
| `source_native_meaning` | OMS `Procedure` denotes a description of steps; `ObservingProcedure` describes steps to determine the value of an observable property. The identifiable `Observer` can implement a reusable observing procedure and make an `Observation`, which provides a result. Within OMS's Conceptual Observation schema an Observation has **exactly one** observingProcedure. OMS says an observing procedure may describe a sensor *type*, **not** an individual sensor instance. Annex C.5.3 distinguishes old `OM_Process` uses that map to procedure versus observer according to meaning. |
| `mapping_direction` / `relation_kind` | OMS's *observing* method relation → candidate reusable method and actual observation-use distinction; `SOURCE_NARROWER` because the investigated candidate also includes other methods beyond observation and OMS describes its own abstract/concrete models. |
| `reused_role` / `qualification_or_loss` | Capture meaning and the **OMS-scoped** Observation cardinality without falsely imposing it on CSAPI Part 2 (whose Observation Procedure association is optional) or all DIM occurrences. Do not treat a historical `OM_Process` as proof of one specific individual's identity. |
| `evidence_status` / `source_claim_standing` | `SOURCE_ACCESS_LIMITED`: direct official indexed sections and exact requirement statements inspected, but the complete original HTML document could not be fetched due to size. This is a **retrieval ceiling**, not a claim that the reported OMS sections are unreliable. `DONOR_TEXT` for only the quoted/paraphrased sections, `V2_ANALYST_INFERENCE` for the mapping. |
| `mapping_review_status` / `adoption_status` | `CANDIDATE_RECORDED` pending full-text recheck of precisely bounded clauses if later needed / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`. This is a qualified semantic comparison only; no live source→profile-constrained CSAPI→client transformation, functional interchange, complete donor-standard conformance or Profile conformance was tested. |
| `donor_declarations` | `DECL-T03-02`: Part 1 explicitly describes OMS as a conceptual predecessor/foundation through SOSA/SSN, not a direct equivalent schema. |
| `source_to_client_consequence` / `open_question` | Different methods can create results about the same observed property; OMS's groundwater automated-probe versus manual-probe illustration is an honest comparison **as a standards example**, not a claim about TRSS/OmniSense. Open: profile target constraints and whether the source supplies observation-level method identity and quality context. |
| `record_provenance` | 28 October 2026; bounded Step 06 original-edition inspection and project Pass 3 comparison; record v0.1; analyst-written research, not owner approval. |


### ALN-T03-A020-01 — Published SOSA/SSN 2017: `sosa:Procedure`, `ssn:implements`, `sosa:usedProcedure`

| Field | Evidence-qualified entry |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T03-A020-01 / TOPIC-03-PROCEDURE-METHOD / source-qualified reusable Method, capability relation, actual use and distinct result. |
| `artifact_id` / `lineage` / `source_role` | **20** / SOSA/SSN (2017 Recommendation) / companion/lineage evidence for SOSA/SSN; not a separate independent vote. |
| `source_ed` / `source_concept` / `source_locator` | [W3C/OGC SOSA/SSN Recommendation, 19 October 2017](https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/), §§4.8.2.1–4.8.2.4, and referenced systems model §4.9. |
| `source_native_meaning` | The reusable `sosa:Procedure` can guide observations, sampling or actuation. `ssn:implements` relates an implementer to a Procedure; `sosa:usedProcedure` associates a specific observation/actuation/sampling activity to a reusable Procedure. The published 2017 class/property names here are **not** `sosa:implements` nor the 2026 draft's general `sosa:Execution`. |
| `mapping_direction` / `relation_kind` | Source's published capability-versus-occurrence relations → candidate distinction between implementable method and its actual use; `CLOSE_ALIGNMENT_WITH_QUALIFICATION`; ontology-specific classes/properties are not the same as CSAPI JSON relation names. |
| `reused_role` / `qualification_or_loss` | Hold published 2017 and draft 2026 namespaces/IRIs apart. In particular, `ssn:implements` (2017) must not be silently replaced by `sosa:implements` (2026) in citation of the published Recommendation. Published 2017 does **not** define the new draft `sosa:ObservingProcedure` specialization. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for §4.8.2; ontology evidence `DONOR_TEXT`, correspondence to V2 `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `SUPPORTED_FOR_CANDIDATE_DIM` for semantically stable relation *distinctions* / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`. This is a qualified semantic comparison only; no live source→profile-constrained CSAPI→client transformation, functional interchange, complete donor-standard conformance or Profile conformance was tested. |
| `donor_declarations` | `DECL-T03-01`: this is the edition explicitly cited in the published CSAPI Part 1 normative references; not an independent vote by addition to draft 2026. |
| `source_to_client_consequence` / `open_question` | Support/capability and performed method are different labels; a client must not use a source's 2026-draft property name while claiming it verified 2017 semantics. Open: if a future Profile uses RDF/JSON-LD, which edition and term mappings will it explicitly target? |
| `record_provenance` | 28 October 2026; bounded Step 06 original-edition inspection and project Pass 3 comparison; record v0.1; analyst-written research, not owner approval. |


### ALN-T03-A019-01 — 21 October 2026 SOSA/SSN Working Draft: `sosa:Procedure` and `sosa:implements`

| Field | Evidence-qualified entry |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T03-A019-01 / TOPIC-03-PROCEDURE-METHOD / source-qualified reusable Method, capability relation, actual use and distinct result. |
| `artifact_id` / `lineage` / `source_role` | **19** / SOSA/SSN (21 October 2026 draft) / core structural donor; primary anatomy evidence; draft ontology. |
| `source_ed` / `source_concept` / `source_locator` | [W3C/OGC 25-022, *Semantic Sensor Network Ontology—2023 Edition*, Working Draft 21 Oct 2026](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/), §§5.3.3.2.1–5.3.3.2.5, 5.3.5.2.11. |
| `source_native_meaning` | A reusable `sosa:Procedure` specifies how an `Execution` is made and may describe inputs/outputs. `sosa:implements` relates a `sosa:System` to a `sosa:Procedure` that it is **capable of executing**; inverse `sosa:implementedBy`. This draft does not prescribe a full internal method-description formalism. |
| `mapping_direction` / `relation_kind` | Draft's reusable method and capability-to-execute relation → candidate method support distinction; `CLOSE_ALIGNMENT_WITH_QUALIFICATION`, subject to **working-draft status**, edition and eventual scope constraints. |
| `reused_role` / `qualification_or_loss` | Useful semantics for a possible coherent explanation, **not** an authoritative retrofit of 2017 term IRIs, a required method object for each System, or automatic proof of execution. Do not use draft-only optional terms as published commitments. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` for the **dated Working Draft** only; `DONOR_TEXT` claims are draft-only; V2 correspondence `V2_ANALYST_INFERENCE`. |
| `mapping_review_status` / `adoption_status` | `CANDIDATE_RECORDED` because edition is an active Working Draft / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`. This is a qualified semantic comparison only; no live source→profile-constrained CSAPI→client transformation, functional interchange, complete donor-standard conformance or Profile conformance was tested. |
| `donor_declarations` | `DECL-T03-03`, the draft's *non-normative* selected CSAPI-to-SSN correspondence (not an OWL equivalence axiom). |
| `source_to_client_consequence` / `open_question` | Distinguish ‘method capable of being executed’ from ‘method recorded for an Observation’. Open: await final 2023-edition normative standing and exact profile targets; protect stable 2017 compatibility. |
| `record_provenance` | 28 October 2026; bounded Step 06 original-edition inspection and project Pass 3 comparison; record v0.1; analyst-written research, not owner approval. |


### ALN-T03-A019-02 — 21 October 2026 SOSA/SSN Working Draft: `Execution`, `usedProcedure`, performer and result

| Field | Evidence-qualified entry |
| --- | --- |
| `alignment_id` / `topic_id` / `candidate_meaning` | ALN-T03-A019-02 / TOPIC-03-PROCEDURE-METHOD / source-qualified reusable Method, capability relation, actual use and distinct result. |
| `artifact_id` / `lineage` / `source_role` | **19** / SOSA/SSN (21 October 2026 draft) / core structural donor; primary anatomy evidence; draft ontology. |
| `source_ed` / `source_concept` / `source_locator` | [W3C/OGC 25-022, Working Draft 21 Oct 2026](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/), §§5.3.4.2.1, 5.3.4.2.6–5.3.4.2.7, 5.3.4.2.11, 5.3.4.2.16 and 5.5.2.3. |
| `source_native_meaning` | `sosa:Execution` generalizes particular Observation, Actuation and Sampling activities. `sosa:usedProcedure` links an Execution/collection to the method actually used; `sosa:madeBySystem` identifies the performer; `sosa:hasResult` identifies the produced result. The draft's specific `sosa:ObservingProcedure` specialization is **explicitly non-normative/pending implementation experience**. |
| `mapping_direction` / `relation_kind` | Draft's actual occurrence–method–performer–result relations → candidate distinctions between doing, how, by whom and outcome; `CLOSE_ALIGNMENT_WITH_QUALIFICATION`, not one all-purpose event class for the new DIM. |
| `reused_role` / `qualification_or_loss` | Do not identify an Execution from a list of supported Procedures; do not promote a command request to a completed Actuation without status/effect evidence. Do not turn draft `ObservingProcedure` into a 2017 Recommendation term. Source result is related to but not identical to the method or the performer. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` on the dated WD; `DONOR_TEXT` for its relations, `V2_ANALYST_INFERENCE` for the V2 choice. |
| `mapping_review_status` / `adoption_status` | `CANDIDATE_RECORDED` for draft-only general execution-pattern framing / `NOT_ADOPTED`. |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`. This is a qualified semantic comparison only; no live source→profile-constrained CSAPI→client transformation, functional interchange, complete donor-standard conformance or Profile conformance was tested. |
| `donor_declarations` | `DECL-T03-03` applies to the draft's expressly *selected* CSAPI correspondences; no asserted universal equality of CSAPI command to completed `sosa:Actuation`. |
| `source_to_client_consequence` / `open_question` | If actual Observation evidence exists, a client can distinguish recorded procedure, performer, value and time. If all that exists is a capability or issued Command, do **not** display a completed method execution or result. Open: evidentiary status of commands, outcome provenance and profile bindings. |
| `record_provenance` | 28 October 2026; bounded Step 06 original-edition inspection and project Pass 3 comparison; record v0.1; analyst-written research, not owner approval. |

## 3. Explicit donor-declared relationships — not our inferred equivalences

The following are source-owned statements, cited with **declaring document and exact location**. They are evidence of a relationship **in that source's terms**, not approval of the draft ontology, equality between standards, or automatic conformance.

| Declaration | Declaring artifact / exact source | What the source itself states | Limit of the declaration |
| --- | --- | --- | --- |
| **`DECL-T03-01`** | **ID 10**, [CSAPI Part 1 v1.0 §3 Normative References](https://docs.ogc.org/is/23-001/23-001.html) | CSAPI cites the **19 October 2017 SSN Recommendation** (**ID 20**) and **SensorML 3.0** (**ID 13**) among its normative references. | A citation is not proof that a class, property, procedure subtype or OWL IRI in the **2026 Working Draft** existed in the 2017 Recommendation, nor that SensorML `ProcessMethod` and every CSAPI `Procedure` are one-to-one. |
| **`DECL-T03-02`** | **ID 10**, [CSAPI Part 1 v1.0 informative Annex C.1–C.3](https://docs.ogc.org/is/23-001/23-001.html) | CSAPI explains that its resource model draws on the published SOSA/SSN ontology, that SensorML is foundational for detailed descriptions/encoding, and that OMS contributes concepts through the SOSA/SSN lineage. | *Informative architectural provenance*, not a normative cross-standard identity, preservation proof or verified bidirectional transformation. OMS remains source-native for its §8 conceptual relations. |
| **`DECL-T03-03`** | **ID 19**, [SOSA/SSN **21 October 2026 Working Draft**, **non-normative §7.3.1**, Tables 14–15](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20261021/) | The draft explicitly gives **selected conceptual correspondences**: CSAPI `Procedure` ↔ `sosa:Procedure`, `System.procedures` → `sosa:implements`, and Part 2 `DataStream/ControlStream.procedure` → `sosa:usedProcedure`. It notes the tables are **not formal OWL equivalence axioms**. | Draft, non-normative, selected mappings only; it **does not** say that Part 1 `systemKind` is an implemented method, nor that a `Command` equals completed Actuation, nor retroactively define 2026 names in 2017. The observation-level `procedure` association in Part 2 is independently checked in **ID 11**, not falsely attributed to the draft's selected Table 15. |

**No general inter-donor equivalence established:** The fact that OMS, SensorML, SOSA/SSN and CSAPI all describe "procedures" does not establish lossless cross-conversion of method versions, algorithms, configuration, inputs/outputs, temporal provenance, security controls or individual event records. Other declared dependencies are for Step 09's cross-concept reconciliation only after specific source review.

## 4. Counterexamples, unresolved questions and compatibility limits

### ISSUE-T03-01 — CSAPI `Procedure` carrier versus relation role (prevent repetition of C08 error)

**Rejected shortcut:** `System.systemKind` = `System.procedures` = `Observation.procedure`. **Evidence contradicts this:** Part 1 Table 5 assigns the first to a System's kind/datasheet and the second to implementable Procedures. Part 2 Tables 5 and 7 assign a procedure to a stream and separately to an individual Observation. Part 2's optional `parameters` can specify how a method was used for **that observation**. One declared underlying resource type does not collapse these relations. See [C08 audit](../DIM_Profile_V2_Anatomy_PhaseA_Validation_Audit_v0.1_26OCT2026.md).

**Standpoint discipline:** A known catalogued detection algorithm or a product datasheet cannot, by itself, establish a historical signal detection, a particular algorithm/version actually used, a generated Observation, or a correctly observed result. The same applies to a supported command/actuation method versus a command request that is rejected or never executed; CSAPI Part 2 §10.7 differentiates received Command, status, execution time and result. No command operations or statuses are populated in this Step 06.

### ISSUE-T03-02 — Published 2017 versus October 2026 **working-draft** terminology

**Do not silently equate** 2017 `ssn:implements` (ID 20 §4.8.2.3) with 2026-draft `sosa:implements` (ID 19 §5.3.5.2.11), or treat the draft `sosa:Execution` generalization as a class defined in the 2017 edition. The 2026 draft's `sosa:ObservingProcedure` (§5.5.2.3) expressly says **non-normative, pending further implementation experience**. Published CSAPI Part 1 Table 16 lists that IRI as an observing Procedure type, but its §3 references 2017 SOSA/SSN: the Procedure-type vocabulary and its target ontology edition should be investigated before future formal conformance text, rather than silently reconciled.

The 2026 draft's §7.3.1 CSAPI alignment is **its own** source-declared **non-normative selected correspondence**, not an approved revision of 2025 CSAPI or a blanket equivalent RDF binding.

### ISSUE-T03-03 — OMS `Observation.observingProcedure [1]` versus CSAPI optional links

OMS §8.2.9 requires exactly one observing procedure in its own conceptual Observation model, while CSAPI Part 2 §9.7.2 Table 7 marks an Observation's `procedure` association **optional**, and §9.2.2 Table 5 supports method information at the DataStream level. These are **different source-model target constraints**, not an error to "repair" by inventing a mandatory DIM/Profile attribute. If the intended Profile ultimately selects a particular conformance target, only then should binding requirements and tests address this difference. Additionally OMS 3.0 explains that earlier `OM_Process` can encode either an observer or a procedure, requiring *meaning-based* migration; don't turn a historical process record into a fabricated individual sensor.

**OMS evidence ceiling:** This issue is supported by source-specific official indexed excerpts, not an unrestricted full-document reinspection. If any future normative Profile depends on the exact wording of OMS constraints, re-open that primary section in an accessible original edition before adopting obligations.

### ISSUE-T03-04 — Granularity, accessibility, settings and proof remain open

- **Method identity/versioning:** no rule yet for URI stability, method variants, firmware revision, calibration effects or parameter defaults versus actual settings.
- **Structure:** methodology can be text, algorithm, executable implementation reference, or SensorML aggregate dataflow. Its description may be subject to access control; no blanket disclosure requirement.
- **Observation/stream provenance:** presence of a DataStream-level method does not independently verify each raw vendor event or settle precedence when an Observation-level method differs. A missing optional relation does not prove the method didn't exist.
- **Result versus capability:** product options and theoretical supported method ≠ installed/current configuration ≠ specific execution ≠ result. A command issue/request ≠ successful actuation.
- **No adoption:** whether these should be classes, relations, encoding constraints, or merely existing donor-native roles is still a future DIM/Profile design judgment. **No invented class** called `ProcedureMethod`, `MethodExecution`, etc., and no new `SHALL`.

### Worked fidelity check — conceptual illustration only, NOT a device test

Suppose a future source-integrated System exposes a manufacturer kind, one reusable measurement method, a DataStream and a particular Observation. A defensible client would render **Model/kind** from kind evidence, **Supported method** from the individual System's implementable-method link, **Method associated with stream** from the stream link, and **Method used / parameters / result** only where the Observation or its documented context supplies evidence. It should visibly qualify omissions/conflicts and preserve the native source identifiers. These are **hypothetical labels**, not observations about an actual TRSS, OmniSense or SCK unit.

In the earlier [Glaux Profile-aware Details prototype](https://glaux-client.pages.dev/?page=resource-details-profile-test), documented model options and synthetic examples are informative only; the historical TRSS/OmniSense fixtures do **not** establish runtime CSAPI Observation-to-Procedure relationships. The [Smart Citizen case study](../Case_Studies/Real_Equipment_DIM_Validation/README.md) established a conditional research report, not a completed source→CSAPI→client exchange. **Do not** promote a fixture, published datasheet or assumed algorithm to an equipment-specific executed method or end-to-end compatibility result.

**Practical reason to preserve these meanings:** two observations of the same property may have used different protocols; knowing method and associated per-observation settings can inform interpretation/quality. OMS §8.3.2's automated and manual groundwater-level probe comparison shows this distinction without requiring a new universal class or attributing invented equipment values to our actual donor cases.

## 5. Step 06 acceptance, exclusions and next authorized action

| Exit check | Bounded result |
| --- | --- |
| One concept-family question | **PASS** — `TOPIC-03-PROCEDURE-METHOD` only; composition/component standing held for Step 07 |
| Frozen register IDs | **PASS** — IDs **8, 10, 11, 13, 19, 20** verified against exact 182-row derived corpus; **10** detailed mappings; no invented IDs, changed original ledgers or additional donor votes |
| Exact editions and links | **PASS WITH LIMIT** — original CSAPI Parts 1/2, SensorML, 2017 SSN and dated 2026 WD sections checked; OMS official indexed sections checked but complete large HTML unavailable (marked `SOURCE_ACCESS_LIMITED`) |
| Source-native versus V2 analyst meaning | **PASS** — distinct source roles, ontology/encoding scope, method use, result, cardinality and draft edition ceilings |
| Controlled alignment directions | **PASS** — `CLOSE_ALIGNMENT_WITH_QUALIFICATION`, `SOURCE_NARROWER`, `PARTIAL_OVERLAP`; no `EXACT_SEMANTIC_EQUIVALENCE` invented |
| Source-declared dependencies | **PASS** — **three** scoped declarations; citations and draft/annex standing named; no inferred equivalence |
| Adversarial corrections | **PASS** — CSAPI kind vs implementable method, stream vs actual Observation, OMS vs CSAPI cardinality, SensorML detail, 2017 vs 2026 working draft, unrealized commands |
| Technical proof | **NONE** — all ten `NO_TRANSFORMATION_TEST`; no source-to-Profile-to-client test, physical source attribution or complete donor conformance |
| New DIM class/module, Profile SHALL or UI deployment | **NONE** — every mapping `NOT_ADOPTED`; no app/site changes |

**Value for the future manuscript and Profile:** Preserve a source-qualified account of *reusable method*, *System's ability to implement it*, *actual occurrence using it*, and *its outcome*, while accommodating distinct donor granularity, reuse and encoding patterns. This is evidence for **candidate DIM prose**, not a publication-ready ontology, mandatory Procedure-per-function rule, complete donor conformance or end-to-end integration.

**Stop boundary:** Step 06 ends here. **Next only after the owner's new ‘proceed’: Step 07 — Composition / Component Standing donor alignment**. Reuse the completed Pass 4 and audited Smart Citizen I07/I10/I12 examples. Examine whole/part, managed subsystems, physical components, channels, temporary associations, platform/deployment and source software records; **do not** start Step 07 now or adopt a universal component class.
