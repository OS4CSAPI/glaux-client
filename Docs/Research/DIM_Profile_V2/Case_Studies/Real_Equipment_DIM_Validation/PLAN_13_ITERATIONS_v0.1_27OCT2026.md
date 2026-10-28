# Real Equipment DIM Validation — 13-Iteration Execution Plan

**Version:** 0.1  
**Date:** 27 October 2026  
**Repository/branch:** [OS4CSAPI/glaux-client](https://github.com/OS4CSAPI/glaux-client), `research/dim-profile-v2` (**not `main`**)  
**Location:** `Docs/Research/DIM_Profile_V2/Case_Studies/Real_Equipment_DIM_Validation/`  
**Status:** **I01–I03 completed (27 October 2026); I04 next.** 3/13 substantive iterations completed. [I01 selection](I01_Equipment_Selection_and_Qualification_v0.1_27OCT2026.md); [I02 frozen corpus](I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md); [I03 source-native facts](I03_Source_Native_Fact_Register_v0.1_27OCT2026.md).  
**Parent research:** [Five-Pass Synthesis Checkpoint](../../DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md) and [Canonical Concept Consolidation Plan](../../DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md)

## 1. Why we are doing this

We have completed five donor-grounded *candidate* concept studies—Individual System identity; Product/Model/Kind; Procedure/Method; Composition and Component Standing; and Digital Representation/Proxy Identity—plus a five-pass synthesis checkpoint. **They have not yet demonstrated a useful DIM slice on real equipment.** This effort tests that practical value.

**Research question:** Can real, verifiable information about one sensing system be organized using established donor semantics, expressed as a small implementation-independent **Domain Information Model (DIM)** slice where warranted, and mapped to the **Open Geospatial Consortium (OGC) Application Programming Interface (API) – Connected Systems (CSAPI)** and related standards **without semantic loss, false equivalences, invented source facts, or gratuitous new V2 vocabulary**?

**Target deliverable:** One source-traceable case study that moves from real equipment evidence → relevant donor meaning → working DIM interpretation/view → CSAPI accommodation analysis → critical evaluation. The output should let the owner judge **what the five-pass research actually contributes, what remains unsupported, and which domain questions warrant investigation next**.

**What this is not:** Not a new server/client development project, not a finished DIM, not a conformance-certified CSAPI profile, not a full survey of the 182-source corpus, and not an excuse to revisit quarantined earlier anatomy Phase B/C/D conclusions.

**I01 selection:** Smart Citizen Kit **2.3** (SCK2.3) was selected as the **source-supported equipment-product baseline** in [I01's qualification record](I01_Equipment_Selection_and_Qualification_v0.1_27OCT2026.md). Official hardware/firmware and technical documentation are available. **A particular physical unit and its readings remain unverified.** The pinned project's SCK2.3 enclosure-test notebook references four *platform device IDs* (18486–18489), not proven physical identifiers; I02 verified that **the notebook has no executed output** and was **unable to obtain readable live records or recordings** in this environment. The [I02 register](I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md) pins 25 exact file sources across four Git repositories. Preserve the **physical-unit evidence gap** and reconsider a stronger unit evidence source before Gate A if needed. A product datasheet **does not prove** deployment, firmware or actual unit behavior.

## 2. Execution policy

- **One substantive iteration per user `proceed`.** Perform its evidence gathering, interpretation, artifact creation, checks and commit in the same turn; **do not** silently advance to the next iteration.
- **No approval carousel.** The user already approved this bounded workflow. Do routine research, citations, formatting, and GitHub commits without asking for micro-approvals. Explain material source insufficiency or scope-changing decisions.
- **Use authoritative source evidence.** Prefer official manufacturer/product documents, verifiable repository commits, standards and real source data. Distinguish documentation, actual sample/instance, observation, and invented illustration. Version and timestamp evidence; preserve stable URLs, specific sections/pages, and retrieval dates where material.
- **Do not manufacture data.** No fictional serial number, device identifier, firmware version, operating state, calibration or observation presented as an actual fact. Label hypothetical illustrations plainly, and do not let them satisfy an empirical validation gate.
- **Donor-language-first, Chicago Manual of Style 18 author–date.** Show a cited meaning and, immediately thereafter, what each donor says natively, why it applies, and where our project inference begins. A mere citation matrix is not a substitute for the narrative pedigree where synthesis is substantial.
- **Respect donor authority and edition.** Published CSAPI, Sensor Model Language (SensorML), and other standards are different from a 21 October 2026 Sensor, Observation, Sample, and Actuator / Semantic Sensor Network (SOSA/SSN) Working Draft; a verified product datasheet is not a general standard; implementation code is not a normative ontology. A Phase A GREEN lineage is not blanket clause-by-clause verification; YELLOW evidence ceilings remain.
- **Keep boundaries separate.** Actual equipment evidence ≠ donor-native concept ≠ V2 interpretation ≠ a DIM model declaration ≠ CSAPI encoding/profile obligation ≠ demonstrated implementation/conformance.
- **Choose diagrams by value, not ceremony.** If UML earns a useful representation, apply the [modeling convention](../../DIM_Profile_V2_Modeling_Convention_v0.1_26OCT2026.md) and [visualization guide](../../DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md); preserve editable source and corresponding render, and label candidate/example standing. No invented root class, module, datatype, multiplicity, or UML composition diamond.
- **Keep outputs compact but complete.** One clearly named primary finding/record per iteration where practical. Create additional source registers, diagrams or PITONs only when their separate format materially aids verification or reuse. No decorative administrative document proliferation.
- **GitHub is continuity authority.** Work only on `research/dim-profile-v2`; fetch source files before relying on them, write and verify committed artifact paths, update the README/plan's progress status and direct links. Existing prior files remain unmodified except narrowly needed cross-references.

## 3. Thirteen iterations and exit criteria

### Phase A — Establish trustworthy real-equipment evidence (I01–I04)

| Iteration | Work to perform | Evidence-backed output / exit criterion |
| --- | --- | --- |
| **I01 — Select equipment** | Evaluate SCK against a small number of feasible alternatives only if needed. Confirm the intended hardware/revision, authoritative technical documentation, observable/component detail, and evidence for at least one actual individual unit if obtainable. | **Selection decision** with cited evidence and honest limitations. No assumed unit identity. If a real unit cannot be established, document whether to select an alternative or limit the test; do not mislabel product-level evidence as a unit. |
| **I02 — Freeze source corpus** | Gather exact official product documents, source data, relevant versioned hardware/software references and any necessary donor documents. Establish what is available and what is missing. | **Versioned source register** with link, source owner, revision, date, scope, reliability, and evidence gaps. A bounded, reproducible corpus for this exercise; freeze by recorded versions or snapshots rather than claim web pages will never change. |
| **I03 — Source-native fact extraction** | Extract manufacturer/instance facts without yet applying our proposed DIM taxonomy; distinguish model-level, individual-unit and observed information. | **Fact register** with stable evidence IDs, precise source/section, native term, proposition, evidence type, and unresolved ambiguity. No inferred field values. |
| **I04 — Independent evidence audit and PITON A** | Challenge unsupported or contradictory facts, inspect a targeted sample of critical claims, correct extraction and lock down its usable evidence scope. | **Evidence-audit verdict + PITON A** (verified reading order, source inventory, corrections, next step). Only supported facts pass to Phase B; explicit partial/no-evidence results where necessary. |

**Gate A:** No factual claim flows into conceptual modeling merely because the extractor repeated it. Version-specific source evidence, source scope, and fact register are inspectable. If the system was only documented at product level, actual-instance tests remain incomplete.

### Phase B — Apply the existing five candidate findings (I05–I08)

| Iteration | Work to perform | Evidence-backed output / exit criterion |
| --- | --- | --- |
| **I05 — Individual and kind/model** | Apply [Pass 1](../../DIM_Profile_V2_Canonical_Concept_Pass1_Individual_System_Identity_v0.1_26OCT2026.md) and [Pass 2](../../DIM_Profile_V2_Canonical_Concept_Pass2_Product_Model_Kind_v0.1_26OCT2026.md) to fact IDs. Distinguish fielded item, kind/specification, IDs, and manufacturer/product metadata. | **Traceable identity/kind mapping**; demonstrate what is known of a real instance and what is not. No fabricated identity joins. |
| **I06 — Procedure/method** | Apply [Pass 3](../../DIM_Profile_V2_Canonical_Concept_Pass3_Procedure_Method_v0.1_26OCT2026.md). Differentiate product capability, reusable method, the System's ability to implement it, and evidence of its actual use. | **Procedure/method mapping**, native terminology and source limits; no false claim of executed methods. |
| **I07 — Composition/component standing** | Apply [Pass 4](../../DIM_Profile_V2_Canonical_Concept_Pass4_Composition_and_Component_Standing_v0.1_26OCT2026.md). Distinguish integral parts, detachable equipment, hosting, connection/data flow, internal channels, and independently describable items. | **Component/context mapping** with provenance, conditional component standing, and missing evidence; no mandatory hierarchy or automatic CSAPI Subsystem for every part. |
| **I08 — Digital representation + reconcile; PITON B** | Apply [Pass 5](../../DIM_Profile_V2_Canonical_Concept_Pass5_Digital_Representation_and_Proxy_Identity_v0.1_26OCT2026.md). Establish which real services/resources/identifiers have evidence of referring to the selected equipment. Reconcile all five mappings for contradiction and information loss. | **Consolidated donor/equipment mapping + critical reconciliation + PITON B**. State whether five-pass distinctions proved useful, irrelevant, or insufficient. |

**Gate B:** Each materially mapped concept can be traced back to a source fact and a donor's native meaning. Differences such as CSAPI versus AAS `assetType`, `systemKind` versus implemented `procedures`, and equipment versus proxy/service identity stay distinct. **Passing Gate B does not yet imply a DIM class hierarchy.**

### Phase C — Express and challenge a real DIM slice (I09–I10)

| Iteration | Work to perform | Evidence-backed output / exit criterion |
| --- | --- | --- |
| **I09 — Candidate conceptual slice** | Identify only the smallest justified concepts, relationships, definitions, applicability and open constraints. Separate source-native constructs from genuine V2 synthesis. Choose a clear model boundary and acknowledge unsupported areas. | **Candidate DIM slice with textual definitions, grounded relationships and fact/donor pedigree**. No unsupported new vocabulary or implied full-DIM coverage. |
| **I10 — Model/view and critical check** | Decide whether UML class/instance diagrams add explanatory value; if yes, draw source-accurate model views with editable source, inspect them against text and evidence and challenge example-to-class confusion. If not, document why the prose/matrix is the more faithful representation. | **Validated conceptual representation and discrepancy log**—either verified UML source/render or a recorded no-diagram decision. No diagram-created semantics. |

**Gate C:** The slice is internally coherent at the described scope and supported by source-to-donor-to-DIM traceability. “Working model slice” does **not** mean final adoption, complete donor-model equivalence, or normative profile conformance.

### Phase D — Assess CSAPI accommodation and deliver the case study (I11–I13)

| Iteration | Work to perform | Evidence-backed output / exit criterion |
| --- | --- | --- |
| **I11 — CSAPI/OGC mapping** | Map the slice to selected exact clauses/semantics of CSAPI Parts 1–2, SensorML and relevant OGC resources/encodings. Distinguish directly expressible information, partial mappings, missing input data, legitimate donor specialization, and potentially missing profile semantics. | **Concept-to-OGC accommodation matrix and explanatory narrative**, referencing exact standards/editions. **Potential gaps are not automatically new SHALL requirements.** |
| **I12 — Critical interoperability challenge** | Revisit consequential mappings and counterexamples; test whether source meaning survives, what cannot be inferred, and whether one standards-native representation is mistaken for another. | **Independent critical assessment**: supported, conditional, failed, untestable, unknown. A mapping claim and a working example do **not** establish system interoperability or standards conformance without actual implementation tests. |
| **I13 — Final case study + PITON C** | Consolidate a readable beginning-to-end case study and concise evaluation of actual added value, evidence gaps, corrected assumptions, and recommended next research/model work. Record verified exact links and current state for a new chat. | **Integrated case study + PITON C**; complete trace path, conclusions and one clearly stated next step. Avoid assembling another sprawling paper with duplicated donor material. |

**Gate D / end:** The case study demonstrates exactly the support earned by evidence and explicitly states where empirical verification could not be completed. It must be possible for another researcher to follow each consequential conclusion back to the manufacturer/unit evidence, native donor semantics, candidate DIM description and CSAPI accommodation finding.

## 4. Controlled records and recovery

Use simple status labels in the evidence and mapping documents:

- **SOURCE-DIRECT** — explicitly stated/observed in a named version of source evidence.
- **DONOR-NATIVE** — explicitly defined in a donor's relevant edition.
- **V2-INFERENCE** — our synthesis or interpretation, with its argument and source pedigree.
- **MAPPED (full / partial / conditional / failed)** — what a proposed alignment preserves or loses and why.
- **OPEN / NOT AVAILABLE / NOT TESTED** — uncertainty, unprovided source information, or unevaluated behavior; do not silently change to “supported.”

At **I04**, **I08**, and **I13**, create **PITON A, B, C**, respectively. Every PITON must tell a new conversation to fetch the current README, this plan, the exact completed outputs and critical parent research sources from the **working GitHub branch**, then name the exact next iteration. A PITON snapshot is historical; its progress claims cannot override newer verified statuses. If a source is later corrected, record what changed rather than allowing the later concept note to silently overwrite the original fact.

**Required parent recovery pointers (not material to copy blindly):**

1. [Concept Baseline](../../DRAFT_Concept_Baseline_v0.1_25OCT2026.md) and [DIM Concept and Method Basis](../../DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md): what the bounded problem and method are.
2. [PITON v1.4](../../PITON_DIM_Profile_V2_Continuity_v1.4_26OCT2026.md): original recovery and quarantined-material safeguards. **Its progress position is stale**; use latest case-study tracker instead.
3. [Five-Pass Synthesis Checkpoint](../../DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md): summary of source-grounded distinctions and unresolved modeling choices. Consult [five original passes](../../DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md) individually when their findings are applied.
4. [Phase A audit](../../DIM_Profile_V2_Anatomy_PhaseA_Validation_Audit_v0.1_26OCT2026.md) and [bulk evidence triage](../../DIM_Profile_V2_Anatomy_PhaseA_Bulk_Trust_Triage_v0.1_26OCT2026.md): avoid material C08 errors and respect eight YELLOW evidence ceilings.
5. [DIM modeling convention](../../DIM_Profile_V2_Modeling_Convention_v0.1_26OCT2026.md), [visual guide](../../DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md), and [provisional DIM/profile outlines](../../DIM_Profile_V2_Provisional_Document_Outlines_v0.1_26OCT2026.md): model form, source preservation, and binding/profile separation.

## 5. Progress tracker and the `proceed` contract

**Current state: 3 / 13 substantive iterations completed.**

**Completed:** [I01 Equipment Selection](I01_Equipment_Selection_and_Qualification_v0.1_27OCT2026.md), [I02 Frozen Source Corpus](I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md), and [I03 Source-Native Fact Register](I03_Source_Native_Fact_Register_v0.1_27OCT2026.md) (27 October 2026). **I03 output:** 60 traceable **candidate** source statements from 17 directly pertinent pinned files, six flags for I04 audit, and six evidence gaps. **No verified individual physical unit or actual observation obtained. I04 next.**

| Phase | Iterations | Current state | Checkpoint |
| --- | --- | --- | --- |
| A — evidence | I01–I04 | **I01–I03 COMPLETE; I04 NEXT** | PITON A at I04 |
| B — five-finding application | I05–I08 | Not started | PITON B at I08 |
| C — working DIM slice | I09–I10 | Not started | Model/evidence review at I10 |
| D — CSAPI evaluation | I11–I13 | Not started | PITON C at I13 |

**At the end of every iteration, the assistant must clearly state, in conversational language:**

1. **What we actually accomplished**—not just document names.
2. **Why that result matters** to the end goal, including a limitation or failure if one appeared.
3. **The verified GitHub link(s)** and current Ixx status.
4. **The next exact iteration and its objective**, ending with a direct invitation: **“Next: Iteration Ixx — [specific task]. Say ‘proceed’ to begin.”**

A simple **“proceed”** authorizes that single next iteration; the assistant must re-read the current plan/tracker, necessary upstream artifacts and exact source evidence, complete the named work, commit and verify, then stop and name the following step. Do not require the user to repeat context or grant routine approvals. If evidence fails the current gate, document the precise correction/recheck needed as the next actionable iteration rather than quietly continuing with unsupported claims.

**Next action: Iteration I04 — audit [the I03 fact register](I03_Source_Native_Fact_Register_v0.1_27OCT2026.md) against the pinned sources, examine the six flagged discrepancies and identity/provenance limits, record an explicit **Gate A PASS/CONDITIONAL/FAIL** verdict, and create **PITON A** with exact GitHub recovery links. **I05–I13 have not started.**
