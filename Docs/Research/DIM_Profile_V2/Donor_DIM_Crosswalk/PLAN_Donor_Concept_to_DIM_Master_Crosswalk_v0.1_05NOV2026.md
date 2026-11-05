# Plan — Donor Concept → DIM Master Crosswalk (v0.1)

**5 November 2026 · Owner-directed new effort · Planning iteration 01/40 COMPLETE · Next: iteration 02, one prompt at a time.** This plan replaces **neither** the prior completed, qualified 43-step DIM/Profile research record nor its unresolved external interoperability limitations. It begins a **different, concrete work product** after the owner approved the visual **donors-as-columns → proposed DIM at far right** comparison template on 5 November. The 40 steps below are **a proposed, revisable work breakdown**, not proof that full source coverage can be accomplished in exactly 40 turns. The owner authorizes **one explicitly requested step at a time**, normally by “proceed.”

**Critical success definition:** One genuinely useful, readable, source-traceable **master donor-to-DIM concept crosswalk**: donor standards as fixed columns, provisional least-used on the left and most-used immediately before the DIM (final rank **derived from evidence**), **far-right DIM column** with plain-language proposed information elements, and full-width topic dividers so the reader can understand the sensing System from its identity and equipment to behavior, information, management and history. **A companion UML model must ultimately correspond to the accepted rows.** This is **not** another R24-versus-donor matrix, not a donor bibliography disguised as an alignment, not proof of formal standards equivalence, and not a repeat of the prior research plan.

**First owner review must occur after step 08**. There are further reviews after steps 16, 24, 34 and 40. If the working crosswalk is not useful to the owner, **STOP and repair the form/model before processing more donors**. Each step must leave a reviewable GitHub checkpoint, not merely a narrative of AI activity.

## 1. Control documents and scope

**Controlling approved layout (DO NOT REPLACE):**
- [Directly readable 22-row, 7-donor sample](../Deliverables/DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026.md), five section dividers; donor columns from lower to higher **sample** populated correspondence counts; DIM **far-right**. This sample's **layout**, not every proposed element, source equivalence or donor rank, was explicitly accepted.
- [Sample's structured source JSON](../Deliverables/DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026.json); [flat Excel-compatible CSV](../Deliverables/DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026.csv); [51-cell evidence ledger](../Deliverables/DIM_V2_Donor_Columns_Sample_v0.1_05NOV2026_Evidence.csv). The 51 rows are **historical claimed source locators**, not independent re-verification of every cited original clause in this planning iteration. Re-verify as donor reviews proceed.
- [Existing older workbook with *different/wrong main layout*](../Deliverables/DIM_V2_Donor_to_Model_Traceability.xlsx) and [182-artifact lineage-only CSV](../Donor_Alignment/05_Donor_to_R24_Artifact_Traceability_04NOV2026.csv): **REFERENCE/ACCOUNTABILITY ONLY**, never silently promote either to the approved master crosswalk.
- [The original 182-artifact citation/accountability register](../Donor_Alignment/03_Source_Accountability_Register.csv): exact source list, one artifact per row, **182/182** records marked `NOT_ASSESSED` for **individual artifact-level concept review** as of the starting checkpoint. This status does not mean the 13 family studies did not occur; it does **not** prove all 182 individual sources were reviewed.
- [Thirteen developed donor lineages; seventeen preliminary/deferred leads](../Concept_Donor_Comparison/Donor_Contributions.md) and [side-by-side donor native terminology and careful qualifications](../Concept_Donor_Comparison/Donor_Terms_Side_by_Side.md). “Family” is an organizing device, not proof that each associated artifact was independently evaluated.
- [Existing proposed DIM](../Candidate_Specification/DIM_Profile_V2_Proposed_Research_Candidate_DIM_v0.1_03NOV2026.md) and [R24 antecedent definitions](../Candidate_Specification/DIM.md). **R24** means a research-authored set of 15 relationship propositions drafted in a prior *Step 24*; it is **not** a donor-native field, a user-facing column name, or a settled UML class. Keep those codes only in internal evidence/trace links if useful.
- [Separate proposed CSAPI Profile](../Candidate_Specification/DIM_Profile_V2_Proposed_Research_Candidate_CSAPI_Profile_v0.1_03NOV2026.md). Do not change Profile requirements or claim native OGC adoption merely because the DIM alignment changes.
- [Prior 43-step final reproducibility and research-qualification report](../Whole_System_Recovery/Step43_Final_Reproducibility_Source_Fidelity_and_Release_Decision_03NOV2026.md) and [PITON v3.3 (historical completed campaign)](../PITON_DIM_Profile_V2_Continuity_v3.3_03NOV2026.md); retain the source and live-client qualification limits.
- **Working repository/branch:** `OS4CSAPI/glaux-client`, `research/dim-profile-v2`. **Do not** write a new model or mapping to `main` or `work/details-view-20261023` by accident. GitHub `blob/research/dim-profile-v2` URLs are human navigational refs; record actual commit/blob SHAs when publishing evidence snapshots.

**Proposed location for future master:** this folder, `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`, with `Master_Donor_Concept_to_DIM_Crosswalk.xlsx` (owner-facing), a **GitHub-browser-readable mirror** in Markdown/CSV, a separate row/cell evidence ledger, coverage/decision log, and later synchronized UML source plus SVG/PNG. The filenames are prospective; they **do not yet exist**. Source of truth must be a maintainable structured table; *generate* the workbook/mirrors to avoid hand-maintained drift. Preserve the 22-row sample unchanged as the historical layout baseline.

## 2. Exactly what the user approved

**Master table appearance, from left to right:** **Donor A | Donor B | … | Donor N | PROPOSED DIM ELEMENT**. No R24 or “research lineage score” as the main leftmost field. **Each horizontal row is a distinct meaningful candidate information element**. Columns contain the donor's **actual native class/attribute/relationship/property/event/operation/field name**, not a made-up paraphrase; include a short qualifier only where needed to prevent a false equivalence. A **merged/full-width divider row** begins each concept group. Topic headings are **navigation only** until independently justified as modules/packages in a model.

**What counts as a “field”:** the owner's useful informal shorthand. The technical source might actually declare a **concept/class**, **attribute/property**, **association**, **process role**, **code value**, **data field**, **reported state**, **service/operation**, or **exchange object**. Identify that actual source type in the *evidence ledger*, not by treating every cell as a literal JSON field. Preserve which element describes a **kind/model**, **individual asset**, **physical component**, **functional role**, **API resource**, **event**, or **digital copy**.

**Empty/filled cells:** Blank means **no verified candidate correspondence in the material assessed**, *NOT* “the donor has no such idea.” If a donor has a **unique concept**, give it its own appropriately grouped row; leave other donors blank and use a **provisional proposed DIM term** or explicit **UNRESOLVED / NOT ADOPTED** at far right. A donor's concept may map to **several** DIM rows, or several source fields may contribute to **one** row; use separate evidence-ledger mappings for each without inventing a one-to-one false identity.

**Relation qualification (in evidence ledger, not visually cluttering master):** `DIRECT` (same scoped meaning supported), `BROADER`, `NARROWER`, `OVERLAP/PARTIAL`, `RELATED_BUT_DIFFERENT`, `CONFLICT`, `NO_ESTABLISHED_MAPPING`, `UNRESOLVED`. Use an unobtrusive symbol such as `≈` in the main cell only for broader/narrower/partial/related matches. `DIRECT` is not equivalent to a published owl:equivalentClass or normative encoding constraint unless **the standard explicitly says so**. Disputes require notes and source comparison, not consensus by superficial similarity.

**Evidence ledger minimum for every populated donor cell:** stable row ID independent of display position; proposed DIM label/working definition; source owner/issuer, donor **standard vs version/edition**, original *exact* concept name, element kind, original **clause/table/figure/schema path**, public URL or precisely identified repository-local original, original meaning paraphrase with source fidelity, mapping relation and reasoning, **what the mapping must not imply**, field/evidence confidence and verification status (`ORIGINAL_CHECKED`, `PRIOR_SOURCE_EXTRACT_ONLY`, `SOURCE_UNAVAILABLE`, `NEEDS_REVIEW`), and reviewer/date. Distinguish an actual original source from a project paper citing it. A Markdown link working is not proof of semantic validation. **No phantom publisher requirements or fabricated SHALLs.**

**Donor-column eligibility:** one column per **coherently distinct donor standard/family meaning** after source-aware review, not one column for each of the 182 artifact titles and not necessarily exactly the previous 30 family labels. Consider when to **separate** apparently combined lineages (e.g., OPC UA Devices versus PA-DIM; CSAPI versus SensorML/SWE; The Open Group SOSA versus W3C SOSA/SSN; original edition versus draft). Maintain a column-roster metadata sheet so the source edition and source roles are inspectable. **Do not force eligibility or row names because the old R24 model needs them.**

**Column order:** provisional initially. The owner requests **least used → most used**; after concept alignment, rank by the **number of unique DIM rows with source-supported substantive contributions**, counted separately for direct and partial support. Do not count multiple documents within one lineage as multiple votes, and do not treat an unsupported “RELATED” mention as equal to a direct contribution. Display basis and ties transparently; ranking means **breadth of use in this crosswalk, not normative authority or donor quality**. The DIM remains the absolute rightmost column. The workbook may scroll horizontally; preserve column order and a useful frozen header. Do not replace the agreed horizontal layout with a vertical list of donors.

**Row order:** currently the five groups in the accepted sample (identity; system/equipment; channels/observations; configuration/control; provenance/evidence). Expansion may split or reorder groups when source evidence demands it, e.g., capabilities/functions, deployments, power, communications, lifecycle, security. A useful proposed traversal is identity → whole/parts/connections/hosting → functionality/interfaces → outputs/data → actual observations → configuration/state → management/actions → lifecycle/condition → source/provenance. **Do not canonize topic headings as DIM classes or assume every source describes each group.**

## 3. Explicit exclusions and anti-drift rules

1. **No new overarching domain label, compulsory “chassis,” universal inheritance tree, predetermined 8-module design or hidden reconciliation that changes the meaning of the user's target.** The DIM's actual content and name must emerge through evidenced donor comparisons. Legacy MPSS v0.3.5/V1 and proposed V2 candidates are context, not acceptance-by-default.
2. **No fabricated exact match.** Never infer physical containment from software hierarchy, two physical sensors from two reported values, a current installed setting from a manual default, or four original Observations from four API copies of two originals. Distinguish kind from individual, capability from execution, source-fact from derived/unknown, and host location from individual probe location.
3. **No “182 donors fully mapped” claim** until individually evaluated. Keep count of source artifacts, reviewed unique source titles, donor columns and mapped DIM rows separately. If the available source corpus lacks licensed text, record the gap and public source alternatives without inventing normative clause requirements.
4. **No silent new modeling commitments** during donor intake. A new donor finding can add a provisional DIM row, split a false alignment, or challenge the current model; adoption is an explicit subsequent synthesis/review decision. Use standards URLs, true editions, and Chicago Manual of Style 18 author–date in supporting narrative where appropriate; the master sheet must remain scannable.
5. **No AI-generated process as a substitute for the actual workbook.** Every mapping step must produce an actual GitHub table/workbook delta, with count of new/changed/rejected/held mapping cells and exact link(s). One narrow scope per prompt; don't draft multiple “justification papers” unless a specific unresolved disagreement demands one.
6. **No app deployment, Oracle/52°North server changes, physical Commands, changes to the older CSAPI Profile or merging branches** within this research crosswalk effort. Do not claim OGC full ATS, issuer authentication or independent interoperability based on workbook mappings.
7. **No automatic step advance.** End each iteration with the achieved concrete result, limitations, next single numbered task, and a simple “proceed” path. If a step cannot be evidenced at reasonable scope, record partial/held and choose the smallest correct continuation; do not mark an absent artifact COMPLETE.
8. **Preserve user control:** at checkpoints 08, 16, 24, 34 and 40, explain **in ordinary language** what the spreadsheet now shows, show a few representative cross-row comparisons and a direct GitHub link, and ask whether to accept the format/content before continuation. Not all such checkpoints necessarily add a full new version of PITON.

## 4. Required outputs and objective checks

| Deliverable | Minimum acceptance, not a completion prediction |
| --- | --- |
| **Master spreadsheet, source-maintained** | One **primary** donor-as-columns table; final DIM rightmost; frozen readable header, distinct full-width group-divider rows, consistent column order, human-readable content; each active donor column identified in a roster. |
| **Per-cell evidence ledger** | Every populated donor cell (including repeated and partial links) locatable to a real edition and clause/schema line; mappings classified and limitations explained. Each unmatched/unresolved concept explicitly tracked without auto adoption. |
| **Candidate DIM information-element register** | One stable row ID, plain-English label, working definition, concept type and proposed standing for each master row. Row IDs **not** technical model classes. Duplicates, splits, edits and renamed rows tracked. |
| **Contribution/coverage and audit view** | True donor column counts including direct/partial, reviewed original source IDs, 182-register NOT_ASSESSED exceptions; the final least-to-most ranking computed only when suitable evidence exists. |
| **Synchronized UML** | Human-readable structural and behavioral views based on the accepted information-element register; class vs property vs relationship accurately distinguished, no unsupported cardinalities or UML inheritance. Evidence trace for each nontrivial edge. |
| **GitHub publication** | XLSX **and** GitHub-readable Markdown/CSV and editable diagram source plus SVG/PNG, all actually committed and downloaded/read back. No ChatGPT-only temporary sandbox links. |
| **Owner readability** | Owner can pick a DIM element, scan **horizontally** across donors and inspect sources; scan **down** to understand a System. A source contributor or obvious unique concept cannot vanish due to grouping. |
| **Final bounded result** | Explicit `CANDIDATE` or `ACCEPTED FOR FURTHER REVIEW` status, coverage numbers, open disagreements, and evidence we **did not** establish. 40 completed iterations ≠ 182 assessed sources or model adoption. |

**Progress bookkeeping:** count **original-source terms/claims reviewed**, **rows added / split / merged**, **populated donor→row cells by relation standing**, **distinct donor standards/editions covered**, **source artifacts actually individually inspected**, **unresolved disputes**, **model features traceable to evidence**. A progress metric cannot substitute for opening the workbook.

## 5. Proposed 40 one-prompt iterations

**Rule for sizing:** A donor-intake step targets one named original donor standard/family and typically **no more than ~8–12 substantive new or corrected information-element decisions** (or ~15–25 evidence cells) in a single turn, dependent on source complexity. If original evidence is unavailable or the step is bigger than that, **STOP/record a partial hold** and request authorization for a smaller follow-on; do not rush, hallucinate or silently close it. A standard with multiple editions may require explicit subdivision. The 40 rows are **control points**, not a license to force coverage.

### Phase A — establish controls before touching the mapping (01–04)

| Step | One-iteration task and tangible output | Standing |
| --- | --- | --- |
| **01** | **Create this dedicated plan and robust recovery PITON, index them from research/Deliverables.** Preserve owner-accepted layout and clear evidence/stop rules. **Do not map new donor concepts or modify DIM.** | **CURRENT · COMPLETE once GitHub readback verified** |
| **02** | Audit the exact 7-column/22-row sample, 51 source-claim ledger, the 182-artifact register and distinct 13 developed/17 preliminary source groups; create a **frozen starting-data inventory and review-status discrepancy list**. No new mappings. | NEXT |
| **03** | Convert the evidence/relationship decision rubric above into a **single concrete row-and-cell record schema**, with positive/negative example and exact source/edition control. Do not adjudicate unseen sources. | PENDING |
| **04** | Assemble an **eligible donor-column roster**: distinguish unique standards, editions, companion sources and non-conceptual methods. One record per proposed column with original-source pointers and unverified standing, **no final ranking**. | PENDING |

### Phase B — make one genuinely usable editable working master (05–08)

| Step | One-iteration task and tangible output | Standing |
| --- | --- | --- |
| **05** | Establish the **approved visual/table contract** in code/structured format: donor header columns, far-right DIM, section divider, symbol legend, blanks, evidence links, owner-facing readability checks. Preserve the accepted sample unchanged. | PENDING |
| **06** | Generate the first **GitHub-stored XLSX master + readable Markdown/CSV mirrors from one structured source**, seeded with the 22-row sample, source-claim statuses and no new interpretation. Verify resulting actual file bytes. | PENDING |
| **07** | Review the preliminary group ordering and row definitions **against the four available real equipment case distinctions**, note necessary proposed splits/unique rows without declaring new donor mappings. | PENDING |
| **08** | **OWNER CHECKPOINT 1:** open the actual master in GitHub, compare layout to the accepted sample, show a few complete horizontal comparisons and decide whether the structure is useful. **Hard stop** if not approved. | PENDING |

### Phase C — source-focused developed donor reviews (09–24)

| Step | One-iteration donor scope; update workbook cells + evidence only | Standing |
| --- | --- | --- |
| **09** | **OGC API – Connected Systems Parts 1–2 (23-001/23-002):** native System, Procedure, subsystem, DataStream, Observation, status/control; avoid conflating resource vs physical part. | PENDING |
| **10** | **SensorML 3.0:** process/PhysicalComponent/PhysicalSystem, typeOf, components/connections, inputs/outputs and parameters. | PENDING |
| **11** | **SWE Common 3.0:** original data fields, Quantity, DataRecord/TimeRange and unit semantics, distinct from System identity or original event. | PENDING |
| **12** | **OMS 3.0:** Observer versus method, actual Observation, result, feature, phenomenonTime and resultTime, host; retain Bennett unknowns. | PENDING |
| **13** | **W3C SOSA/SSN:** initially anchor *2017 Recommendation*, identify 2026 draft discrepancies separately, never mix with Open Group SOSA. | PENDING |
| **14** | **IEEE 1451/TEDS:** work from accessible IEEE/NIST/Playground technical evidence, separate NCAP/TIM/TransducerChannel and actual TEDS fields; explicitly hold uninspected normative 2024 text. | PENDING |
| **15** | **Integrated Sensor Architecture (ISA) 6.0:** composition, visibility/roles, capability declarations, actual status/response; bounded cited source versions only. | PENDING |
| **16** | **OWNER CHECKPOINT 2:** audit and show the actual master after foundational sensor/observing-source reviews; correct false equivalences before more donor families. | PENDING |
| **17** | **The Open Group SOSA:** distinct whole Sensor / Host Platform / functional Component vs Module / implementation roles; preserve RA/DSDM edition boundaries. | PENDING |
| **18** | **SAPIENT v2:** source identity, registration, ModeDefinition, status and equipment reporting. Do **not** merge TaskAck with actual control effects here. | PENDING |
| **19** | **SAPIENT v2 action/status follow-up:** Task, TaskAck, outcomes and precise status-code alignment/challenge against CSAPI when original clauses warrant it. | PENDING |
| **20** | **Asset Administration Shell v3.2:** Asset vs Shell, type vs instance and contextual submodels/relationships without mandatory AAS multiplicity inheritance. | PENDING |
| **21** | **OPC UA Devices v1.05.0:** source-native DeviceType/Device, nameplate, connections, information and state. | PENDING |
| **22** | **OPC UA PA-DIM v1.02.0:** **separate** process-device model, inherited OPC names versus PA-DIM-only facts, source-tested distinctions; no automatic reuse count. | PENDING |
| **23** | **SAREF Core v4.1.1 and W3C WoT 1.1, bounded related source terms:** DeviceKind/Function/Service versus Thing Model/Thing Description, interactions, digital mediation. Mark distinct original issuers. | PENDING |
| **24** | **OSUS/OSUS-R and developed-donor checkpoint:** original Asset/AssetProxy implementation scope, mediator versus physical unit. Review 13 developed families’ contribution without calling unassessed artifacts verified. | PENDING |

### Phase D — fair examination of previously deferred or specialized lines (25–34)

These are bounded **challenge/coverage passes**, not a promise to read every line of 182 artifacts. A new donor can **change the row structure**, not merely occupy a slot inherited from earlier favorites.

| Step | One-iteration focus; source-verified row deltas or honest HOLD | Standing |
| --- | --- | --- |
| **25** | **NIEM:** types, association, augmentation, model/exchange versus physical identity; do not convert packaging tools into sensor hardware classes. | PENDING |
| **26** | **MIP/JC3IEDM:** model/item, location, state, event and capability distinctions where original edition available. | PENDING |
| **27** | **Redfish/Common Information Model:** Chassis, ComputerSystem, Manager, Battery/Power and Sensor versus managed hardware/system; identify physical vs monitoring roles. | PENDING |
| **28** | **Matter and OMA LwM2M:** node/endpoint/cluster/object/resource meaning versus hardware structure; selected original concepts only. | PENDING |
| **29** | **MIMOSA and IETF RFC 8348:** asset/event/service lifecycle versus hardware replaceability; source-bounded maintenance and component identity. | PENDING |
| **30** | **IETF interfaces/topology and energy management:** connection, interface/address hierarchy, energy object/power/battery evidence; no fake total battery state. | PENDING |
| **31** | **I-ADOPT, SWEET, QUDT and UCUM:** quantity/variable/property/matrix/instrument taxonomy and units; sample limited by concrete original terms, not exhaustive vocabularies. | PENDING |
| **32** | **NIST IoT cybersecurity baseline and W3C PROV:** required security capability versus actual authorization, source/agent/activity/derived information; do not turn W3C PROV into original issuer cryptographic proof. | PENDING |
| **33** | **ISO/IEC 29182 sensor-network architecture and radiation-instrument family:** specialized sensor/network/instrument/evidence distinctions; admit edition/text gaps. | PENDING |
| **34** | **BME280 product and TRSS/OmniSense historical/synthetic case leads; residual corpus triage; OWNER CHECKPOINT 3.** Record unique surviving elements, excluded methods, remaining unassessed sources. These are case evidence, not automatic normative donors. | PENDING |

### Phase E — reconcile, make diagram trustworthy and decide what truly exists (35–40)

| Step | One-iteration deliverable | Standing |
| --- | --- | --- |
| **35** | Reconcile **duplicate/split/overloaded DIM rows and divider groups** from verified donor material. Preserve changes as candidate decisions; don't silently adopt a final model. | PENDING |
| **36** | Compute **final evidence-based donor column ordering** from distinct supported row contributions with direct/partial counts and ties; apply fixed least-used→most-used order, DIM last. Do not use source count or subjective importance. | PENDING |
| **37** | Derive **readable UML-style views** from the crosswalk's candidate element **kinds and supported associations**; reject phantom classes, cardinalities and inheritance; preserve editable source and image outputs. | PENDING |
| **38** | Audit crosswalk against **Dragino, AirGradient, Campbell and Bennett** positive/negative source situations. Verify exemplar information survived; document source standing, 2→4 Bennett representations, unproved facts and incompatible concepts. | PENDING |
| **39** | Run **actual file/data/source quality checks**: all nonempty donor cells → original evidence locator/status, row IDs unique, stable donor order, literal DIM-last column, group separators, model↔table agreement, zero broken GitHub links, XLSX opens, diagrams render. Publish actual verified review files. | PENDING |
| **40** | **OWNER FINAL REVIEW / BOUNDED CLOSEOUT:** show the actual source-backed master and UML, quantify what was and wasn't audited, get owner substantive judgment, and update this plan/PITON. **No claim of complete 182-source adoption or external CSAPI Profile conformance.** | PENDING |

**Intentional flexibility:** If one donor needs 3 prompt iterations to do correctly, don't squeeze it into one. Record an authorized bounded inserted step, update next and counts, preserve the old plan for traceability. If owner rejects a checkpoint, fix before following phases. The “40” is **a credible work breakdown**, not a completion mandate. The owner may choose to stop early once the crosswalk is useful.

## 6. What each future “proceed” response must include

For a **mapping** step: *Donor and original edition reviewed; precise original sections/URLs; list of proposed DIM rows added/changed/split, with 3–6 representative horizontal comparisons; new/updated/held/rejected mapping-cell counts; any unavailable primary source; GitHub master/evidence links; next single numbered step.* No “success” if no actual workbook/deliverable was changed.

For a **setup/review** step: *exact decision/document needed for future trustworthy mapping; GitHub evidence/readback; anything still deferred; next single step*. Avoid sprawling future architectures or a new plan unless the owner changes the goal.

**Current after iteration 01:** This plan and [new PITON](PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md) exist. **No new donor concept mappings were added** and the previously approved layout sample remains unchanged. **NEXT when owner says “proceed”: Step 02 ONLY — verify source inventory, baseline sample and evidence/coverage status; create the bounded starting-data audit.** No row/column reordering, new donor mapping or UML change in Step 02.

## 7. Source provenance and citations

This work must be able to show **where an original standard actually defines a term**, not simply a prior AI-written summary. Start with documented original-source locators in the [source-side terminology sheet](../Concept_Donor_Comparison/Donor_Terms_Side_by_Side.md), [donor contribution research](../Concept_Donor_Comparison/Donor_Contributions.md), [direct source excerpts and challenges](../Donor_Challenge/), and source citation register. Then follow back to original OGC 23-001, 23-002, 23-000, 24-014, OMS 20-082r4, applicable manufacturer/operator, IEEE/ISA/SAPIENT/OPC/SOSA/AAS/WoT/W3C primary resources at the **actual reviewed editions**. Do **not** cite a project's own “R24” row as proof that a donor published the same relation. Nonpublic/licensed originals remain outside public GitHub; cite locator/extraction standing rather than dumping copyrighted text.

**Revision policy:** Candidate master rows and UML can and should change with better original evidence, but the owner-approved presentation geometry remains until the owner agrees otherwise. The evidence-ledger history explains **why**, preserving both donor-native semantics and original publication status.
