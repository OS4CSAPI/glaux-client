# PITON v1.8 — Recovering after Profile Rewrite 6

**30 October 2026 · America/New_York**  
**Purpose:** Continue the DIM/Profile V2 effort without losing the work, repeating corrected mistakes, or treating a recommendation as authorization. This is a recovery document, not a new research plan or model revision.  
**Repository:** `OS4CSAPI/glaux-client` · **Research branch:** `research/dim-profile-v2` · **Documentation:** `Docs/Research/DIM_Profile_V2/`  
**Pre-handoff revision:** `25ba081e862184b642aac03b34499ce27552712c`. Check the live branch and [README](README.md) for later owner-authorized changes.  
**Supersedes:** v1.7 and earlier PITONs for current status and restart instructions; those documents remain historical evidence. The version of this PITON is not the version of the DIM manuscript.

## 1. Read this first

**We have a researched starting framework, three detailed equipment information sheets, and connected comparison tables. We do not have a finished Domain Information Model (DIM), a finished OGC API – Connected Systems (CSAPI) application Profile, or the robust, connected real-equipment datasets the owner wanted.** Completed research steps are not the same as those completed products.

The latest four-iteration comparison plan is **4/4 complete and closed**. The earlier eight-step equipment qualification plan is **8/8 complete and closed**. Its selected cases qualify for documented reference arrangements and published examples, not complete operating installations. No new acquisition campaign, model subject, or implementation has been authorized at this handoff.

The owner rejected the assistant's repeated promotion of **“operational condition/status,” narrowed to power**, as the natural next subject. It was an internal proposed research heading, not a sixth donor-derived concept comparable to the five researched meanings. Read the [standalone hallucination and drift case study](DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md); do not revive the power-first recommendation.

The owner then challenged whether the research used actual standards rather than summaries, metadata, or implementations. The answer is **mixed, not “all except IEEE.”** Relevant original clauses were used for many major donors; other contributions have different limits. Section 5 below preserves that distinction.

**The owner supplied the complete OMS 3.0.0 standard, and it is now preserved.** Its actual PDF is in connected Google Drive; the [GitHub source/recovery record](Primary_Sources/OGC_20-082r4_OMS_3.0.0.md) contains its stable identifiers and checksums. Do not repeat the old HTML-reader failure as a current absence of the standard, and do not ask for another upload before trying the saved copy.

**Latest owner instruction:** make this PITON. Preserve and explain the state; do not use that instruction to begin a successor project.

## 2. The goal, without the research bookkeeping

The intended result is a common way to describe different sensing systems while preserving what makes each one different and useful. A client should understand the equipment, its components, capabilities, settings, reports, and available operations from communicated meaning—not from a separate hard-coded screen for every manufacturer.

The **DIM** should define those meanings and relationships independently of a particular encoding. The **Profile** should specify how justified meanings are communicated using CSAPI and related standards. Integrations should publish faithful source information, and the client should interpret it into a useful shared Details experience. The [purpose baseline](DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md) explains this division, but its older TRSS/OmniSense emphasis must be read with the owner's later correction.

The final domain name, scope boundary, organizing framework or “chassis,” and complete structure remain open. Keep the owner's provisional “system and sensor and equipment” scope question open; do not promote a convenient working description into an adopted domain. Do not reintroduce MERLIN-specific coupling simply because the surrounding ChatGPT project carries that name.

TRSS and OmniSense explain the original problem. They are **not compulsory experimental anchors**: the owner wants better-supported comparable systems because adequate full representations of those two products are unlikely to be available. Reusing V1 insights is allowed when their origin and current justification are explicit; inheriting V1's priorities is not.

## 3. What exists, and what each result actually means

| Work | Durable starting point | Actual standing |
| --- | --- | --- |
| Original donor alignment | [Twelve-step plan](PLAN_DIM_Profile_V2_Donor_Alignment_and_Foundation_v0.1_28OCT2026.md) and [cross-concept reconciliation](Donor_Alignment/09_Cross_Concept_Reconciliation.md) | **12/12 closed.** Five candidate meanings, topic-level donor records and qualified relationships; not a complete model or exhaustive donor comparison. |
| Additional-donor review | [Six-step plan](PLAN_DIM_Profile_V2_Donor_Challenge_v0.1_28OCT2026.md), [reconciliation](Donor_Challenge/05_Challenge_Reconciliation.md), and [candidate manuscript v0.2](Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md) | **6/6 closed.** SAPIENT, IEEE 1451, Integrated Sensor Architecture and The Open Group SOSA added important distinctions. The owner did not endorse framing late donors merely as challengers to an incumbent model. |
| Equipment qualification | [Eight-step plan](PLAN_DIM_Profile_V2_Controlled_Sensing_Equipment_Corpus_Qualification_v0.1_29OCT2026.md), [selection](Controlled_Corpus/07_Corpus_Qualification_Decision.md), and [handoff](Controlled_Corpus/08_Frozen_Corpus_Manifest_and_Handoff.md) | **8/8 closed.** Three reference/example cases selected; no qualifying actual operating history acquired. The richer dataset objective remains unmet. |
| Itemized system information | [System Data Sheets index](Controlled_Corpus/System_Data_Sheets/README.md) | Three GitHub documentation pages with stable row identifiers, native fields, values where available, sources and gaps. Complete named inventories are not complete installation datasets. |
| Concept, donor and equipment comparison | [Four-iteration plan](PLAN_DIM_Profile_V2_Concept_Donor_and_Equipment_Comparison_v0.1_30OCT2026.md) and [comparison home](Concept_Donor_Comparison/README.md) | **4/4 closed.** Connected presentation of existing findings and selected equipment correspondences; not a model rewrite or tested transformation. |
| Source preservation | [OMS original-document record](Primary_Sources/OGC_20-082r4_OMS_3.0.0.md) | Complete original PDF and searchable derivative saved in Drive. Availability is resolved; earlier interpretations are not automatically revalidated. |

The five researched meanings distinguish **the individual System; reusable model/kind descriptions; methods and capabilities versus actual activities/results; composition and component standing; and equipment versus digital representations/proxies**. They are candidate distinctions, not five immutable classes or five slots into which every donor must fit. Ten relationship passages and further unresolved questions are also recorded in the manuscript/comparison.

The latest tables provide three routes: [concept → donor rationale](Concept_Donor_Comparison/README.md), [donor → contribution or unrepresented material](Concept_Donor_Comparison/Donor_Contributions.md), and [equipment information → candidate meaning or unresolved question](Concept_Donor_Comparison/Equipment_Evidence.md). The equipment view has 27 grouped comparisons, not an exhaustive mapping of every field. It separates missing model meaning, insufficient donor review, and missing or unclear equipment evidence.

Coverage counts are navigation aids, not proof of fairness: 182 source artifacts are not 182 independent standards; 48 original alignment records are not 48 successful mappings. The retained 30-family screen has 13 families with some specific review and 17 without that detailed treatment in the referenced sequence. Partial treatment of a family does not establish adequate treatment of every companion—especially OPC UA Devices versus PA-DIM.

The [final review](Concept_Donor_Comparison/README.md#verification) was a separate pass by the same assistant against existing research and data sheets. It was **not independent human validation or a fresh audit of every original source**. The owner subsequently said the presentation was still overwhelming and “by AI for AI”; do not claim that the readability objective received owner acceptance.

### The equipment cases

| Case and sheet | What is retained | Boundary to preserve |
| --- | --- | --- |
| [AirGradient Open Air Max](Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md) | Gas-equipped `O-M-1PPSTON-CE` reference assembly; components, configuration/reporting descriptions and original published message examples. | Reference/example PASS, not a verified unit. Do not silently equate `-CE` and `-CE-S`, join unrelated cloud/device examples, or claim an authenticated firmware/configuration combination. |
| [Dragino S31-LB](Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md) | External-probe, primary-battery product; message and command definitions, an eight-entry manufacturer history example and decoder checks. | Reference/example PASS. Exclude integrated-probe S31B and solar LS construction. Published bytes, decoded derivatives and synthetic checks are not acquired real-node history or successful commands. |
| [Campbell CR1000X + first-generation ClimaVue 50](Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md) | Documented logger/sensor pairing, sensor-response definitions and a separate 31-field logger-status example. | Reference/example PASS. The logger example does not establish an attached ClimaVue or actual weather history; thirteen status-field meanings remain held. |
| [Raspberry Shake & Boom audit](Controlled_Corpus/04_Candidate_B_Evidence_Audit.md) | Instrument documentation and an attributed historical station/data lead. | **CONDITIONAL**, outside the primary set; applicable record inspection remained unsuccessful. Tool access failures were not proof the records do not exist. Rehosting permission was not established. |

The accepted cases are environmental-monitoring references; a qualified seismic/acoustic or surveillance primary case is still missing. METER ZL6/ATMOS 41 and AudioMoth remain recorded reserves, not rejected products. Do not select a new winner or retry sources merely by reading this PITON.

The [preservation record](Controlled_Corpus/08_Preservation_Record.json) and [manifest](Controlled_Corpus/08_Frozen_Corpus_Manifest_and_Handoff.md) distinguish retained files from external links. AirGradient's checker embeds its attributed examples; Dragino still needs its separately obtained pinned decoder; Campbell needs the separately supplied publisher example. The later data sheets and comparison pages are outside that earlier freeze. Do not describe the record as a full manufacturer-source archive.

## 4. Corrections that must survive the next chat

**Donor fairness.** The owner deemed V1 unrecoverable because early donors shaped the work and later sources could not receive a fair foundational role. V2 reused the resource body, not V1's architecture. Late sources must be allowed to revise, split, combine, replace or introduce meanings on the same evidence standard as early sources; they need not merely defeat or fit an existing proposal. The [drift case study](DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md) preserves the full explanation.

**No inherited power priority.** Relevant power and diagnostic evidence exists, but the repeated recommendation was not a demonstrated V2-wide priority decision. “Operational condition” was not independently defined with the same provenance treatment as the five meanings. Do not suppress useful electrical information; do not promote its familiar heading into a sixth concept, adopted module or automatic next task.

**No success by relabeling.** A closed plan, a PASS for published examples, a complete field list, a functioning decoder, and a complete operating dataset are different achievements. The owner's goal remains rich, reliable comparable system information for experiments. Do not quietly weaken that goal, and do not demand impossible knowledge of every proprietary detail either: completeness must be explicit for the experiment.

**Human explanation first.** Explain what a finding means through a concrete system example before giving record IDs, counts or filenames. Use short paragraphs, spell out acronyms on first use, and keep the main answer focused on what changed, why it matters, what remains missing and the next bounded action. Tables need readable definitions and synthesis explanations; more tables alone did not solve the owner's comprehension problem.

**GitHub is the documentation home.** The owner explicitly declined unsolicited ZIP/download bundles and repeatedly asked for GitHub documentation pages. Give GitHub links first; do not manufacture another bundle. Distinguish documents committed to GitHub, original files stored in connected Drive/Library, and temporary local copies. Do not claim every original donor document is archived in the repository.

**Preserve earlier corrections.** The rushed Anatomy Phase B/C/D material remains quarantined, not an adopted model. Earlier Smart Citizen acceptance concerned the written case study, not real interoperability. Older “next proceed” paragraphs and the previously rejected automatic checkpoint do not authorize work now. Historical prose that says TRSS/OmniSense remain essential is superseded as an experimental mandate by the owner's later clarification.

## 5. Actual standards, not evidence about their existence

The last substantive question before preservation was whether the assistant had used **the actual standards documents**. Do not answer with a blanket assurance based on bibliography entries or an earlier AI report. Availability, original-source inspection, depth of review, preserved copies, and correctness of interpretation are separate questions.

The following is a recovery summary of existing source records and the end-of-chat clarification, **not a new all-source audit performed for this PITON**. Open the named original clauses for substantive work; use the research reports to locate them, not replace them.

| Source group | Recorded basis and limit |
| --- | --- |
| CSAPI Parts 1–2, SensorML 3.0, W3C/OGC SOSA/SSN | Direct official specification text was used for relevant clauses. The published 2017 ontology and recorded 2026 Working Draft are separate editions with unresolved namespace/mapping questions; a draft is not an adopted final standard. See [method review](Donor_Alignment/06_Procedure_Method_Alignment_v0.1_28OCT2026.md) and [source trail](Concept_Donor_Comparison/README.md#source-trail). |
| Asset Administration Shell, OPC UA Devices, SAREF, Web of Things | Relevant official metamodel/specification/ontology content was inspected: AAS Part 1 v3.2, OPC UA Devices v1.05.0, SAREF Core v4.1.1, WoT Architecture/Thing Description 1.1. Official HTML can contain the original specification; do not imply a standalone PDF was separately read when it was not. The WoT TD companion is outside the frozen corpus. See [representation review](Donor_Alignment/08_Digital_Representation_Proxy_Identity_Alignment_v0.1_28OCT2026.md). |
| SAPIENT v2 | Actual BSI Flex 335 v2.0:2024-03 PDF plus pinned official protobuf companions. Their recorded field/tag and timestamp discrepancies remain unresolved; code does not automatically overrule the publication. See [source register](Donor_Challenge/02_SAPIENT_Challenge.md). |
| Integrated Sensor Architecture and The Open Group SOSA | Supplied original PDFs were inspected: `ISA_Software_Design_Document-6.0r5(1).pdf`, `ISA_Data_Model_Specification-6.0r12(1).pdf`, `c239_5.pdf`, and `sosa_techstd_v1_dsdm.pdf`. Recover through Project/Library files using exact titles; do not assume these originals were all committed to GitHub or copied into the OMS Drive location. Architecture Edition 1.1 and data-model Edition 1.0 are distinct. See [exact-source register](Donor_Challenge/04_Other_Structural_Challenges.md). |
| IEEE 1451 | Public Playground, NIST and other recorded technical material make detailed study useful now. Do not return to “IEEE is unavailable” or treat it as only metadata. Exact uninspected licensed normative obligations, cardinalities and edition deltas still need their own evidence. See the [corrected IEEE report, §0](Donor_Challenge/03_IEEE1451_Challenge.md). |
| OSUS-R | The cited contribution used pinned implementation code. This is primary evidence for that implementation, not a substitute for an authoritative OSUS standard or proof of standards-wide semantics. See [representation review](Donor_Alignment/08_Digital_Representation_Proxy_Identity_Alignment_v0.1_28OCT2026.md). |
| Other/deferred sources | Original-document coverage is not uniform. Recorded limits include ISO/IEC 29182 Sensor Network Reference Architecture parts, deeper MIP/JC3IEDM edition access, and some radiation-instrument normative details. PA-DIM did not receive the same separate detailed comparison as OPC UA Devices. Consult the [coverage record](Donor_Challenge/01_Coverage_and_Challenge_Selection.md) and [donor view](Concept_Donor_Comparison/Donor_Contributions.md); do not treat those historic limitations as permanent without trying available sources. |
| OMS 3.0 | Earlier research used limited official indexed text after a reader-size failure. The full original was subsequently supplied and saved. **Source availability is now resolved; prior interpretations have not all been rechecked against the saved PDF.** Use §6 below. |

Before promoting a source-dependent definition into the DIM, inspect the actual defining material and relevant context, constraints and figures. Keep source-native statements separate from our synthesis. Companion schemas, examples and implementation code can contribute, but their authority must be named accurately. Never call checking our own summaries an independent source validation.

## 6. Recover the complete OMS standard

**Original:** *OGC Abstract Specification Topic 20: Observations, measurements and samples*, OGC `20-082r4`, version `3.0.0`, publication date 26 May 2023. The owner supplied `20-082r4 (1).pdf`. The [preservation record](Primary_Sources/OGC_20-082r4_OMS_3.0.0.md) reports a successful download-back and byte-for-byte match to the upload.

| Preserved object | Stable retrieval details |
| --- | --- |
| [Original PDF in connected Drive](https://drive.google.com/file/d/1QNBXosCb_TcSP96tppQAyLv42WdnU7G2/view?usp=drivesdk) | File ID `1QNBXosCb_TcSP96tppQAyLv42WdnU7G2`; stored name `OGC_20-082r4_OMS_3.0.0_Original_Standard.pdf`; **198 pages; 11,049,351 bytes**. |
| PDF SHA-256 | `6eefa8dd843d5a8c2dc29e481bf693d1b6d83ee1f96e065db4c1eed204cabebf` |
| [Page-marked searchable text](https://drive.google.com/file/d/10B6djSL1kCDFSZ_vJipx5h_kpNZ8wSPW/view?usp=drivesdk) | File ID `10B6djSL1kCDFSZ_vJipx5h_kpNZ8wSPW`; 333,794 bytes; mechanical extraction, not an AI summary or replacement for diagrams/tables. |
| Text SHA-256 | `3a91bd5d46c5c8ec6285a594767a1d3766ee6926460a34a0102dbd0a103d53fc` |

The **actual PDF bytes are in Drive, not committed as a GitHub PDF**. GitHub holds the source index and recovery instructions. Sharing was not broadened; the saved copy requires the owner's authorized connection. Do not publish temporary signed download URLs or pretend a local `/mnt/data` path is the persistent location.

To recover, read Drive metadata by the recorded ID, then fetch the stored non-native PDF with raw download enabled. Use the returned file reference or mounted path; materialize only when needed. Verify its size and SHA-256. Use extracted text to locate passages, then the original PDF for substantive reading and layout-dependent interpretation. A fresh chat must try this saved copy before claiming it cannot access OMS or asking the owner to upload it again.

The source index points to Procedure §8.4, ObservingProcedure §8.5 and Observer §8.6. These are navigation leads, not a newly completed reassessment. **Saving the standard did not resolve every old OMS mapping question.** Do not silently erase or upgrade earlier limited-evidence findings, and do not start an OMS research campaign merely because the file is available.

## 7. Where we stopped and what was proposed next

The [final comparison recommendation](Concept_Donor_Comparison/README.md#next-task) was to obtain one coherent, attributable real-equipment case before selecting another model subject. In the subsequent plain-language explanation, the assistant described a **bounded attempt using existing leads**, aimed at retaining actual records together with applicable equipment/configuration context—not another general survey or report saying a download exists. One case would be a first step toward a comparable multi-system set, not replacement of that goal.

**That recommendation was not accepted as a new execution task before this handoff.** The conversation turned to source authenticity, then preserving the supplied OMS original, then requesting this PITON. No winning equipment source, new model subject, new plan, or source-to-CSAPI implementation was selected. The closed plans have no automatically authorized next iteration.

If the owner later authorizes the acquisition attempt, its result should be actual retained evidence where permitted and a short explanation of what belongs together and what does not—or the precise retrieval/association blocker. Historical recorded data may suffice; live hardware is not inherently necessary. Published examples remain useful for limited conceptual work, but cannot be relabeled as acquired operating records. Do not weaken the data objective or make perfect equipment knowledge a precondition for all further thinking.

The broader direction remains to use concrete information needs and a fair comparison of relevant donors to draft actual model definitions/relationships, try them against another system, and then justify Profile bindings and client behavior. That is an intended progression, not an approved multi-step campaign. Primary-source checking must accompany any donor-dependent work; a missing device record, an unexamined donor and a missing model meaning require different remedies.

## 8. Recovery procedure and ready-to-paste opening

A new assistant should read this PITON and the current [README](README.md), then the [drift correction](DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md) and [OMS recovery record](Primary_Sources/OGC_20-082r4_OMS_3.0.0.md). Read the comparison's [overview](Concept_Donor_Comparison/README.md), [review](Concept_Donor_Comparison/README.md#verification) and [recommendation](Concept_Donor_Comparison/README.md#next-task), following donor or equipment links only as needed for the requested task. Do not require the owner to reconstruct earlier chats or read the entire document collection before continuing.

Use connected GitHub reads with an explicit ref; default-branch code search can miss this research branch. Research edits belong on `research/dim-profile-v2`; application work is separately recorded on `work/details-view-20261023`. Do not merge, deploy or change application code during recovery. When writing documentation, read existing content, preserve unrelated work, commit, read back and check the changed-file scope.

The earlier client experiment remains a **fixture/design-based prototype**, not a validated integration using actual CSAPI System records and an adopted Profile. Its [design record](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/RESOURCE_DETAILS_PROFILE_TEST.md) and [deployment record](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Plans/CLOUDFLARE_DEPLOYMENT.md) are historical technical pointers; live status was not retested for this handoff. The [older research story](DIM_Profile_V2_Research_Story_and_Current_Position_v0.1_29OCT2026.md) explains the earlier work, but this PITON and the owner correction govern newer status and priorities.

For an authorized plan, execute one named prompt-sized step at a time, explain the substantive result and state the next step so “proceed” has a clear meaning. Do not insert redundant approval checkpoints inside an already authorized step. At this particular boundary, **recovery itself does not authorize a new research or acquisition step**.

**Opening message for the next chat:**

> Recover the DIM/Profile V2 work from PITON v1.8 dated 30 October 2026 in OS4CSAPI/glaux-client, branch research/dim-profile-v2, at Docs/Research/DIM_Profile_V2/PITON_DIM_Profile_V2_Continuity_v1.8_30OCT2026.md. Read its linked drift correction and OMS source-preservation record. Confirm where we stopped in ordinary language and stop before starting new work. Do not revive the power-first recommendation, restart closed plans, claim the rich datasets are complete, or repeat that the original OMS standard is unavailable. Use GitHub documentation links, not download bundles.

**Change boundary for this handoff:** this new PITON and its README recovery pointers only. Prior research, source sheets, comparison conclusions, frozen records, manuscript, Profile and application are not revised by creating the handoff.
