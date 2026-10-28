# Donor Alignment — Step 02: Minimal Register Method, Evidence Rules, and Worked Example

**Version:** 0.1 · **28 October 2026**  
**Execution:** Step 02 of the [12-step controlled plan](../PLAN_DIM_Profile_V2_Donor_Alignment_and_Foundation_v0.1_28OCT2026.md)  
**Standing:** **METHOD AND RECORD FORMAT — NOT A POPULATED DONOR REGISTER, ACCEPTED DIM, OR CSAPI PROFILE.** The one worked example is deliberately illustrative and cannot be counted as the Step 04–08 concept-alignment deliverables.  
**Location:** `OS4CSAPI/glaux-client`, **`research/dim-profile-v2`**; do not move this work to `main` or modify the deployed Glaux client.  
**Source baseline:** [Step 01 verified 182-record identity ledger and seven exceptions](01_Corpus_Baseline_and_Exceptions.md).  
**Project purpose:** [Original TRSS/OmniSense-to-CSAPI-to-UI problem](../DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md) and [provisional DIM blueprint](../DIM_Profile_V2_Provisional_Architecture_Blueprint_v0.1_28OCT2026.md).

## 1. The problem the register solves

We need to answer **which existing donor meanings the candidate DIM reuses, qualifies, specializes, or rejects**, in a way an integrator or client developer can eventually test. The register is **not** a second bibliography; every source artifact already has a stable ID. It is also **not** a matrix of all 182 × 182 possible donor pairs, and not a mechanism for declaring all donors equivalent to our DIM.

The specific engineering chain is:

**Original donor concept (exact edition/clause)** → **source-native meaning and relationships** → **qualified candidate V2 meaning** → **possible later CSAPI Profile/representation consequences** → **client information-fidelity question and eventual evidence**.

The **same source artifact may support several conceptual topics**, and **several sources may inform one candidate**. Companions or duplicate editions do not become independent votes. A source may contribute to model semantics, encoding, a controlled vocabulary, an API, conformance methods or empirical validation **without defining a DIM class or module**.

**Purpose test for each future detailed entry:** Can the record explain what would be preserved, misunderstood or lost when a different vendor's source meaning becomes a CSAPI System description and is interpreted by a common Details UI? If no such benefit has been demonstrated yet, say `UI_BENEFIT_UNESTABLISHED`, rather than invent an example.

## 2. Keep three kinds of records apart

| Kind of record | Stable identifier / granularity | Where it lives and when populated | What it does *not* mean |
| --- | --- | --- | --- |
| **A. Source artifact accountability** | Frozen `artifact_id` = integer **1–182**, exactly **one row per existing artifact** | The existing [source-type CSV](../DIM_Profile_V2_Source_Type_Assessment_v0.1_25OCT2026.csv), [Phase 0 lineage CSV](../DIM_Profile_V2_Anatomy_Phase0_182_Source_Ledger_v0.1_26OCT2026.csv), and [chassis audit CSV](../DIM_Profile_V2_Chassis_Capability_Audit_182_Source_Ledger_v0.1_25OCT2026.csv). Step 03 creates a **derived** 182-row accountability view, joining these inputs without changing them. | No finding that an artifact provides an independently verified DIM concept or conforms to V2. |
| **B. Source-concept → candidate-V2 alignment** | Unique **analytical** `alignment_id`, one record for **one source-native concept/relationship assessed against one candidate V2 meaning**; link `artifact_id` and research `topic_id` | Steps 04–08: **one concept-centered Markdown evidence file per already researched topic**, with repeatable structured records and exact source locators. No new source-concept alignments are created in Step 03. | No newly adopted UML class, universal equivalent concept, lossless transformation, or mandatory Profile requirement. |
| **C. Donor-declared inter-source relationship/dependency** | Unique analytical `declaration_id` for an **explicit source statement**, keyed to the **declaring** artifact ID and exact clause, and target artifact ID or URI/edition if demonstrable | Record alongside relevant concept notes, then consolidate in **Step 09**. If source text does not state the relationship, leave unasserted. | Our inference that two standards “must” be compatible; automatic conformance, inheritance, or normative dependency. |

**One concept-centered record file per topic, not an enterprise database.** A compact heading/field-table per assessed source concept, plus a separate donor-declaration table, is initially sufficient and keeps quotations/qualifications readable. If repeated machine extraction later becomes necessary, serialize these exact fields; do not invent a competing schema or parallel master registry merely to use a tool.

## 3. Source accountability view — Step 03 field contract

The mechanical Step 03 register is a **derived CSV with 182 rows**, **no assessments implied**. Preserve strings verbatim and use quoted CSV where fields contain commas, quotes or newlines.

| Field | Type and source | Rule |
| --- | --- | --- |
| `artifact_id` | Integer 1–182 from original `id` | **Required, unique, immutable**; exact cross-ledger join key, not a donor-standard or equipment identifier. |
| `citation` | Original frozen text from [Source-Type Assessment](../DIM_Profile_V2_Source_Type_Assessment_v0.1_25OCT2026.csv) | Required; **no automatic renaming or editorial correction**. |
| `primary_type`, `secondary_type`, `previous_provenance_group` | Existing source-type CSV | Carry verbatim; secondary may legitimately be blank. Type is **not an eligibility or ranking gate**. |
| `anatomy_lineage`, `lineage_role`, `source_role`, `anatomy_disposition` | Existing Phase 0 CSV | Carry verbatim as **historical research classifications**, not accepted future model architecture; blank lineage is valid for prior non-structural exclusions. |
| `challenger_lineage`, `chassis_disposition` | Existing chassis CSV `challenger_lineage`, `audit_disposition` | Carry verbatim, **separately** from anatomy values. Chassis-relevance status does not exclude a source from a future concept. |
| `bibliography_section` | Exact section title in [grouped bibliography v0.5](../DIM_Profile_V2_Candidate_Donor_Bibliography_Source_Type_Grouped_v0.5_25OCT2026.md) | Retain alongside `primary_type`; preserve **seven known placement differences** listed in Step 01. No auto-reconciliation. |
| `metadata_exception` | Step 01 report cross-reference or blank | For IDs **4, 42, 50, 73, 89, 157, 158**, set an **editorial/classification discrepancy** marker and link Step 01; not a standards conflict. |
| `concept_review_status` | **`NOT_ASSESSED`** initially for **all 182 rows** | This tracks whether a source has a *new register-level concept examination*, **not** whether it had ever been researched. Older Phase 0/GREEN/Chassis work remains referenced rather than silently promoted. |

**Only the frozen baseline supplies artifact identities and citations.** Do not create provisional IDs for sources not in the 182 artifact corpus in this step series. A relevant external source discovered later can be named by URI and noted as `OUTSIDE_FROZEN_CORPUS`, pending an explicit later corpus-governance decision; never silently insert it or reuse an ID.

### Source-accountability coverage statuses

| `concept_review_status` | Exact meaning |
| --- | --- |
| `NOT_ASSESSED` | No detailed new donor-to-candidate alignment record has been completed within this plan. **Step 03 must use this for every row**, even if older research exists. |
| `IN_REVIEW` | At least one relevant source-native concept is under assessment but its exact evidence/meaning has not passed the corresponding step's checks. |
| `ALIGNMENT_RECORDED` | A source has at least one complete concept-specific record with verified links and explicit qualifications. **Does not mean every concept in that source has been reviewed.** |
| `REVIEWED_NO_CURRENT_ALIGNMENT` | A specified **topic** was considered with evidence, without a justified alignment; **not global exclusion**. Use with explicit topic scope. |
| `SOURCE_ACCESS_BLOCKED` | Precise source text needed for a claimed alignment was unavailable; retain only appropriately qualified prior evidence. |

For Step 03, **do not prepopulate any `ALIGNMENT_RECORDED` values from older work**. The one worked example in §6 is a *schema illustration*, not a completed register entry. When later topics are reviewed, the detailed topic notes control their scoped status, rather than a misleading single "fully mapped" Boolean for an entire donor.

## 4. Minimal detailed alignment-record format — Steps 04–08

Each concept-centered Markdown file should contain repeatable entries with the following **required fields**. Use a label/value table (easier to read than a 16-column CSV row), one table per mapping. Only state a positive claim when supported.

| Field | Required content / format |
| --- | --- |
| `alignment_id` | Analytical local key, e.g. `ALN-T02-A010-01`, used only for this register. **Not a DIM class/property URI or published code list**. |
| `topic_id` and `candidate_meaning` | Named investigated semantic *question*, e.g. `TOPIC-02-KIND-INDIVIDUAL`, plus concise candidate sentence **and its prior five-pass research document**. Do not create a class just to have a key. |
| `artifact_id` / `lineage` / `source_role` | Exact numeric source ID and the frozen historical lineage/role for that row; independent vs companion count maintained. |
| `source_ed` / `source_concept` / `source_locator` | **Exact source edition**, native term or source-defined relation (including direction/participants) and directly inspectable clause/table/URI. A bibliographic title alone is not a sufficient semantic locator. |
| `source_native_meaning` | Narrow source-faithful paraphrase or brief attributed quotation, with any relevant permitted values, scope, cardinality, condition, or limitations. Distinguish a donor statement from our explanatory abstraction. |
| `mapping_direction` / `relation_kind` | What is being mapped **from → to**, and one value from §5. For `SOURCE_BROADER` / `SOURCE_NARROWER`, direction is **relative to the candidate V2 meaning**, not implied by an ambiguous arrow. |
| `reused_role` / `qualification_or_loss` | Which semantic feature would be retained or reused; where the candidate differs, what is unknown, and what cannot be concluded. Include source-specific constraints that must not be generalized blindly. |
| `evidence_status` / `source_claim_standing` | Controlled evidence status from §5 and one of `DONOR_TEXT`, `PRIOR_RESEARCH_PARAPHRASE`, `V2_ANALYST_INFERENCE`. Label the *individual claim*, not a whole document as universally proven. |
| `mapping_review_status` / `adoption_status` | Controlled values from §5, **independent** of evidence. No contributor is "adopted" merely because a source was cited. |
| `validation_evidence` / `compatibility_limit` | Exact reviewed test/trace link if any; otherwise `NO_TRANSFORMATION_TEST`. State whether we have only *conceptual* fit or actual supported translation/interoperation. **Never infer full donor conformance**. |
| `donor_declarations` | One or more `DECL-...` links if a donor explicitly cites another source/standard; otherwise `NOT_ASSESSED` or `NONE_FOUND_IN_CHECKED_CLAUSE` with exact review scope. |
| `source_to_client_consequence` / `open_question` | A specific possible benefit or prevented failure in a faithful CSAPI System Details view, plus the concrete missing Profile/encoding/source evidence. Use `UI_BENEFIT_UNESTABLISHED` where appropriate. |
| `record_provenance` | Date, authoring/review evidence, source document revision and register record version. Never quietly rewrite a prior decision; preserve a dated correction. |

**Cardinality of mapping records:** one source concept can have multiple honest mappings to **different** V2 candidate meanings, and one V2 candidate can have several donor contributors. This is *many-to-many with explicit qualified edges* rather than a donor-ranking vote. Do not collapse similar labels into one row or assume every source has a relevant mapping.

### Inter-donor declarations: a separate, strict evidence format

Use a small table alongside a concept note. Each verified declaration needs:

`declaration_id` · `declaring_artifact_id` · `declaring_source_exact_clause` · `source_declared_relation` · `target_artifact_id_or_external_uri_and_edition` · `normative/informative/unspecified_as_source_says` · `evidence_status` · `interpretive_limits`.

**Do not assert `DONOR_DECLARED` based only on a reviewer comparing two donors.** A source's own statement that an association *maps to* an ontology relation is not automatically a normative import of that ontology's current working-draft class model, and is not evidence of semantic equivalence between two entire specifications. When the target document's edition is uncertain, preserve the literal target URI and mark its edition **NOT_VERIFIED**.

## 5. Controlled terminology: what each status means

### Mapping relationship — record `relation_kind`

| Value | Narrow definition and required caution |
| --- | --- |
| `EXACT_SEMANTIC_EQUIVALENCE` | **Strongest and exceptional**: same meaning/constraints in the *specified scope*, with both mapping directions examined and no meaningful loss. Requires direct original-source comparison; **not automatic cross-standard conformance**. No record may use this based solely on a similar term. |
| `CLOSE_ALIGNMENT_WITH_QUALIFICATION` | Same essential domain distinction, but one side adds implementation, scope, granularity, optionality or cardinality not yet justified for the other. **Default defensible outcome in the worked example.** |
| `SOURCE_BROADER` | The source-native concept covers *more* cases/meaning than the precise candidate V2 meaning; name the excluded source cases. |
| `SOURCE_NARROWER` | The source-native concept covers *less* than the candidate V2 meaning; name the uncovered V2 cases. |
| `PARTIAL_OVERLAP` | Meaningful shared part, **neither** clearly subsumes the other; identify intersection and each non-shared part. |
| `INCOMPATIBLE` | A direct proposed equivalence or mapping conflicts in the stated scope; give the precise conflict instead of forcing a match. |
| `DESIGN_INSPIRATION_ONLY` | Useful method or idea borrowed without adopting donor semantics or promising semantic/technical mapping. |
| `UNRESOLVED` | Relevant source concept and V2 question identified, but evidence or decision is inadequate to assert any mapping. |
| `NOT_APPLICABLE` | A *scoped and sourced* topic-level no-mapping decision. **Not** a blanket claim that a donor is irrelevant to V2. |

**Directional warning:** `SOURCE_BROADER` is not the same as a universal `subClassOf` relation. These are **textual comparison findings**, not necessarily ontology axioms, UML generalizations or data-conversion rules.

### Evidence vs decision vs validation — three independent axes

| Axis | Allowed status | Exact meaning |
| --- | --- | --- |
| **Evidence** `evidence_status` | `PRIMARY_TEXT_CHECKED` | Exact source edition/clause directly inspected for *this narrow claim*. **Not** an audit of the entire donor document. |
| | `PRIOR_CITED_RESEARCH` | A prior research note cites a precise source; the primary text **was not rechecked in this record**. |
| | `SOURCE_ACCESS_LIMITED` | Exact original source unavailable/partial; use only supported accessible claims. |
| | `NOT_VERIFIED` | Cannot presently ground the specific statement. Do not promote a positive semantic alignment. |
| **Review decision** `mapping_review_status` | `ILLUSTRATIVE_ONLY` | Example showing the format; **not counted** as a concept review completion. |
| | `CANDIDATE_RECORDED` | Meaning, source text, mapping limitations and use case documented; still subject to further review. |
| | `SUPPORTED_FOR_CANDIDATE_DIM` | Evidence supports using this *bounded meaning* in draft DIM text, but not unconditional adoption or normative Profile obligations. |
| | `REJECTED_MAPPING` | Named proposed mapping contradicted by the evidence; record reason and alternative. |
| | `DEFERRED_UNRESOLVED` | Retained without a positive or negative verdict because source, version or meaning remains unsettled. |
| **DIM adoption** `adoption_status` | `NOT_ADOPTED` | **Default for all entries** in this plan unless an explicit owner-approved model decision changes it. |
| | `OWNER_APPROVED_CANDIDATE_TEXT` | Owner explicitly approved candidate wording for ongoing DIM draft; **still not a published class or standard**. |
| | `ADOPTED_IN_DIM_VERSION` | Only when the owner records a specific DIM version and explicit adoption decision; do not infer from this plan's progress/completion. |
| **Technical proof** `validation_evidence` | `NO_TRANSFORMATION_TEST` | No executed source→profile-constrained CSAPI→client interchange/test for this semantic mapping. |
| | `STATIC_REPRESENTATION_CHECK` | Named static encoding checked for specified structural/semantic invariants; **not real runtime interoperability**. |
| | `TRANSFORMATION_TESTED` | Named source→target transform and test corpus reviewed; report what was preserved/lost, without claiming complete donor conformance. |
| | `END_TO_END_INTEROP_TESTED` | Named runtime CSAPI service/client interaction and test conditions verified; **does not imply conformance to any unrelated donor standard**. |

The last axis is **a future evidence classification**, not a requirement that Step 02–08 conduct runtime tests. When multiple statuses apply over time, preserve provenance and the exact test/review artifact rather than simply overwriting `NO_TRANSFORMATION_TEST` with an unsupported positive claim.

**Compatibility statements must name the scope.** “This source concept is closely aligned with a candidate distinction” is not “any implementation of this donor automatically satisfies our DIM,” and neither is “this client conforms to that donor.” Full donor-standard conformance, future CSAPI Profile conformance, and verified cross-schema transformation are **different claims**, each requiring its own requirements and test evidence.

## 6. Exactly one worked example — **format illustration**, not Step 05 execution

This example reuses **Pass 2: Product / Model / Kind**. The relevant original standard is **OGC API – Connected Systems Part 1, OGC 23-001, v1.0**, frozen corpus **artifact ID 10**. Its [§9.2.2 Table 5](https://docs.ogc.org/is/23-001/23-001.html) lists the `systemKind` association as **optional**, targeting a **single Procedure resource** describing the System's *kind*, such as a datasheet. The same table separately identifies `procedures` as Procedures that the System may implement; [§13.1](https://docs.ogc.org/is/23-001/23-001.html) distinguishes System instances, kind descriptions and methods. This precise OGC 23-001 source wording was checked for this example; broader donor equivalence and implementation tests were **not** performed. See the earlier [Pass 2 donor analysis](../DIM_Profile_V2_Canonical_Concept_Pass2_Product_Model_Kind_v0.1_26OCT2026.md), especially §§2–4, and the [C08 correction](../DIM_Profile_V2_Anatomy_PhaseA_Validation_Audit_v0.1_26OCT2026.md), §3.

| Field | Illustrative value |
| --- | --- |
| `alignment_id` | `ALN-T02-A010-01` — **ILLUSTRATIVE ONLY; not yet in the populated alignment register** |
| `topic_id` / `candidate_meaning` | `TOPIC-02-KIND-INDIVIDUAL`: an individual System may be described by a reusable kind/model description that differs from the individual and from an implementable Method. **Research candidate, not a newly coined ProductModel class.** |
| `artifact_id` / `lineage` / `source_role` | **10** / `OGC Connected Systems` / `primary anatomy evidence` (**historical Phase 0 classification**). |
| `source_ed` / `source_concept` / `source_locator` | **OGC 23-001 v1.0 (2025)**; `System.systemKind` association; §9.2.2, Table 5; §13.1 for contrast with implementable Procedures. |
| `source_native_meaning` | A `System` instance may link a **single `Procedure` resource describing its kind/datasheet**, distinct from its separate `procedures` association. Source-defined cardinality and carrier remain attached to the **CSAPI binding**. |
| `mapping_direction` / `relation_kind` | `CSAPI System.systemKind → candidate V2 reusable-kind/individual distinction`; `CLOSE_ALIGNMENT_WITH_QUALIFICATION`. This is a comparison **not** a proven two-way/complete conversion. |
| `reused_role` / `qualification_or_loss` | Reuse the **semantic separation of individual and reusable kind**, but **do not** carry “one Procedure target / optional” into a universal implementation-independent DIM multiplicity or assume all donors model kind that way. |
| `evidence_status` / `source_claim_standing` | `PRIMARY_TEXT_CHECKED` / `DONOR_TEXT` for the described CSAPI associations; `V2_ANALYST_INFERENCE` for their candidate DIM alignment. |
| `mapping_review_status` / `adoption_status` | `ILLUSTRATIVE_ONLY` / `NOT_ADOPTED`. **Not a completed Pass 2 donor-alignment step.** |
| `validation_evidence` / `compatibility_limit` | `NO_TRANSFORMATION_TEST`; **conceptual fit only**. No valid individual System response, vendor conversion, complete donor conformance, or profile-aware client behavior is proved by this table. |
| `donor_declarations` | **CSAPI §9.2.2 Table 5** explicitly displays `ssn:hasSystemKind` as its SOSA/SSN relationship correspondence. This is a **source-declared mapping**, not a newly tested claim of equivalence with the **2026 Working Draft** ontology. Preserve the exact target relation; authoritative target edition/dependency analysis **NOT_VERIFIED** in Step 02. |
| `source_to_client_consequence` | A future profile-aware System Details view could distinguish **manufacturer kind-level specifications** from the individual unit's identity, selected settings and actual reported state; no concrete UI runtime test is claimed. |
| `open_question` / `record_provenance` | Confirm any final DIM meaning/relationship and its cardinality before writing Profile constraints. Schema illustration dated **28 October 2026**; source text checked only for the stated CSAPI clauses. |

**Source-declared relationship illustration (not a full donor-to-donor reconciliation):** In its Table 5, OGC 23-001 identifies `ssn:hasSystemKind` as the semantic property corresponding to `systemKind`. We may record **that OGC declares that mapping**. We may **not** infer that every version of SOSA/SSN shares the same semantics or that an integration conforming to either standard automatically conforms to the other. If this declaration is promoted in Step 09, the target source edition and exact relationship should be separately checked.

**Why this example was chosen:** A superficial matcher would call a product model, a Procedure, and a supported observing method “the same concept” because they share a CSAPI resource type. This record makes the genuine distinction visible, preserves donor-specific mechanics, and identifies the later Profile/UI question **without writing any new requirement**.

## 7. Step 02 acceptance checks and limits

- [x] **Artifact vs lineage vs source-defined concept vs candidate DIM meaning** have separate record standing and identifiers.
- [x] **Frozen ID** 1–182 is the only join key for the 182-row future artifact view; edition/citation retained; all **seven** Step 01 classification discrepancies preserved without repair.
- [x] **One-to-many and many-to-one** concept mappings supported by repeatable records; no 182 × 182 pairwise matching and no ranking by bibliography group.
- [x] **Relation direction, scope, source-original meaning and semantic loss** must be explicit.
- [x] **Source-declared inter-donor relationships** separated from analyst-inferred alignments and unverified edition implications.
- [x] Mapping kinds, evidence ceilings, candidate decisions, adoption, and actual transformation/interoperability proof have **distinct meanings**; no automatic conformance.
- [x] **Exactly one existing Pass 2 example**, explicitly `ILLUSTRATIVE_ONLY` and `NOT_ADOPTED`, used to test the record fields.
- [x] **No 182-row derived register, detailed concept 1–5 alignment file, DIM classes, Profile SHALL, or UI edit** created here.

**Result:** This method is sufficient to begin **Step 03** without deciding a full model architecture. If source row parsing, mappings or field names change later, record the schema revision and reason alongside the derived register; do not silently alter frozen CSVs or retroactively rewrite past meaning without versioned correction.

**Next step, only on a new user `proceed`: Step 03 — mechanically create the 182-row source-accountability view with exact frozen IDs, citations and existing lineage/chassis metadata; mark new concept mappings `NOT_ASSESSED` and preserve the seven Step 01 editorial exceptions. Stop before any concept-level alignment assessment.**
