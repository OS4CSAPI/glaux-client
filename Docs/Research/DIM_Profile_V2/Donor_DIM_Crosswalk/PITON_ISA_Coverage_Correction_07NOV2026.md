# Current PITON — ISA-only coverage correction

**7 November 2026 · CURRENT RECOVERY AUTHORITY FOR THE ISA CORRECTION.** Planning and continuity checkpoint complete. Twelve correction iterations are planned; none has yet been executed. **The next owner “proceed” executes ISA-01 only: source census and coverage register.**

[Controlling correction plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Current machine-readable progress](ISA_Correction_Status_07NOV2026.json) · [Crosswalk landing](README.md) · [Parent forty-step plan](PLAN_Donor_Concept_to_DIM_Master_Crosswalk_v0.1_05NOV2026.md).

## 1. Read this before older “next step” instructions

The owner stopped the transition from Step15 to Step16 after discovering blank ISA manufacturer/model/serial-number cells. Those concepts exist in the original ISA Data Model Specification. The assistant acknowledged that it had selected eleven concepts rather than systematically accounting for ISA's source contents and all current DIM rows. Spreadsheet parity tests had passed, but could not discover missing entries that were never put into the mapping ledger.

The owner now authorizes planning a **correction limited to ISA**, using bounded one-prompt iterations and an updated robust PITON. This plan is inserted between the delivered Step15 artifacts and Step16 owner review. Older “Step16 next” statements describe the pre-correction checkpoint. **They are superseded for execution by this PITON and the correction plan.** Other donor reviews, final ranking and Step17 remain unchanged and unstarted here.

Do not repeat the root-cause discussion as though the next action were still undecided. Do not ask the owner again whether to make a plan. The plan is now recorded. Do not execute all twelve passes from one “proceed.”

## 2. Owner intent and communication rules

The user wants a readable donor-to-DIM comparison that does not miss straightforward source content or invent analogies. The whole-system purpose remains: a defensible implementation-independent Domain Information Model (DIM), a separate Connected Systems API (CSAPI) Profile and eventually a generic, useful client interpretation of unlike equipment. This correction repairs ISA's contribution to that work; it does not reopen the entire research effort.

The current user specifically rejects blanket caveats that later chats treat as permanent reasons to call the effort unfinished. **Completion of a defined source-review task is a real completion.** A specific unresolved interpretation belongs to its exact row/question, not to an overarching declaration that the model or project is unusable. Source review, proposed model acceptance and deployed implementation are separate statuses. Lack of owner adoption of a proposed row does not reverse completed source work.

Examples: “ISA-03 complete: all entries in the assigned property block are dispositioned. Next ISA-04.” At final closeout: “ISA correction complete; the corrected table is ready for Step16 owner review.” Name any genuinely open design decisions separately. Never use this wording rule to conceal unread source sections or invented mappings.

Explain the human meaning and show the table delta after each pass. Preserve paragraphs of reasonable length and conclude with one clearly named next task so the owner only needs to say “proceed.”

## 3. Repository, starting assets and preservation

Repository: `OS4CSAPI/glaux-client`. Research branch: `research/dim-profile-v2`. Work area: `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. Do not write to `main` or the separate application branch.

Pre-correction branch checkpoint: `2f298e00f12025d4be45d210546a71fc8eb12827`.

- [v0.9 editable workbook](Master_Donor_Concept_to_DIM_Crosswalk_v0.9_Step15_ISA_07NOV2026.xlsx), blob `bf87c64981bcab1bf0834b032a824fadf3b33783`, 465,506 bytes, fifteen worksheets.
- [v0.9 structured master](Master_Donor_Concept_to_DIM_Crosswalk_v0.9_Step15_ISA_07NOV2026.json), pre-correction blob `7f358d6a49ab1f9737e5ef60b731689d439b469b`.
- [Thirteen-column primary comparison](Master_Donor_Concept_to_DIM_Crosswalk_v0.9_Step15_ISA_07NOV2026.md) and [fourteen-column ISA proposal](Step15_ISA_6_Proposed_14_Column_Overlay_07NOV2026.md).
- [Original eleven-record ISA stage and fourteen holds](Step15_ISA6_Primary_Source_Staging_07NOV2026.json), blob `1f857915c2227e6dc0b071f7db1ded4d3fc09fb4`.
- [Prior ISA source report](Step15_ISA_6_Original_Source_Clause_Audit_07NOV2026.md) and [successful structural/parity check](https://github.com/OS4CSAPI/glaux-client/actions/runs/42342501927). That check did not establish complete source coverage; the known omissions are why this correction exists.

The primary baseline has 22 proposed DIM rows, nine case-only review topics, 73 equipment source statements and 58 non-ISA primary donor correspondences. The latter are 37 original-standard-reviewed OGC/W3C, six IEEE public-technical and fifteen OPC/SAPIENT historical records. ISA's eleven staged correspondences are separate from those 58. Preserve these distinctions, but do not treat eleven or fourteen as final limits on ISA's useful content.

Keep the v0.9 files as history. Build a versioned corrected ISA review view and its synchronized evidence from the existing sources. The owner-approved case-first format, adjacent foundational standards block and DIM rightmost remain. New ISA-supported information can become candidate additional/split rows in the review view. Do not fill other donor cells for new rows without their own review; mark them not assessed here. Step16 retains owner control of layout promotion and substantive adoption.

## 4. Source recovery — actual originals, not earlier AI summaries

The principal original documents are dated **31 October 2023**, with different revisions within ISA release 6.0. These previously working Files identifiers are recovery hints, not proof that access cannot change:

| Original title and revision | Known file identifier |
| --- | --- |
| ISA Data Model Specification 6.0r12 | `file_00000000ca1c81f48a3ccd49273425f8` |
| ISA Software Design Document 6.0r5 | `file_000000004c10824683c0a84b37f24a3b` |
| ISA Interface Control Document 6.0r5 | `file_000000008de0820e8e33af2cb096bb12` |
| ISA Component Requirements 6.0r4 | `file_00000000ed048210a141e046f2e93a17` |
| ISA Controller Requirements 6.0r4 | `file_00000000e00082109d88d0119f744880` |

Use Files search/find/read. If a handle fails, search exact filename and revision across Project/conversation and Library. Indexed original text was readable even when raw-byte materialization was unavailable. **Do not turn that export limitation into “ISA sources unavailable.”** Inspect page images when layout, tables, extension marks or diagrams determine meaning; do not claim an image was inspected from parsed text alone.

ISA-01 also accounts for the ISA companions in the existing donor register: Data Model Topics, Data Query Language User's Guide, Introductory Guide, White Paper, Certificate Usage Guide, IPL3 Usage Guide and the historical architecture paper. The correction plan tells how to allocate their substantive sections. Duplicate uploads are one source edition, not extra evidence votes.

Known omission locators in DMS 6.0r12: `Manufacturer` printed p.13/PDF p.28; `Model` printed p.14/PDF p.29; `Serial Number` printed p.16/PDF p.31. `Manufacturer POC` is a distinct extension entry; do not merge its standing into Manufacturer. Native `Operating State`, `Relationship` and `Reserve Capacity` are further known items requiring exact comparison, not automatic equivalents or final classifications.

Source entries must be found from the source's own contents/body/index, including named nested fields and meaningful constraints, not only by searching for existing DIM labels. Preserve the original distinction among core, Custom, Nominated and Accepted entries. Cite actual definitions and referenced types. No factory default becomes an installed setting, and no declared command becomes a physical action.

## 5. The twelve-pass sequence and next precise task

The controlling plan sets: **1** census/coverage; **2** identity plus first property block; **3** remaining properties; **4** observables; **5–6** commands in two blocks; **7** identifiers/envelopes/messages; **8** capability declarations/constraints; **9–10** reporting types in two blocks and filtering; **11** architectural/requirements/companion closure and full reconciliation; **12** fresh source-first audit, publication and completion.

Do not improvise this into another thirteen- or forty-step campaign. The source inventory, not an arbitrary number of populated cells, controls the work. If a real block needs subdivision, record its exact remaining entries and an explicit subpass before advancing. No silent scope shrink, unassigned backlog or end-of-plan dump of unexamined ideas into “holds.”

**ISA-01 only on the next prompt:** establish the ISA source inventory and entry/section owners for subsequent passes; reconcile the 22 existing DIM rows plus nine case topics; register the eleven old ISA mappings and fourteen old findings; initialize visible review-status distinctions and coverage tracking. Report what is now accounted for and which exact source block is next. It is a census task, not permission to invent mappings from titles.

## 6. Completion, evidence and local questions

Keep review state, mapping relation and owner/model decision separate. Use understandable labels for otherwise empty ISA cells: Not reviewed; Question [specific ID]; or No correspondence found in [named scope]. A blank or a failed keyword search is not “ISA has no representation.” Native terms remain in positive cells, with fit qualifications in the evidence.

All existing 22 plus nine review targets, every entry in the agreed ISA inventory, every former eleven mapping and fourteen hold, and every newly raised relevant concept must have a traceable disposition before final closure. Relevant unique concepts become candidate rows, supporting relationships or precisely identified design decisions. Unsupported matches are rejected with reasons. Source unreadness cannot be relabeled as a completed interpretation question.

Final review compares the original source inventory against the table, not merely one generated file against another. Mechanical checks verify coverage records, stable IDs, evidence parity and preserved non-ISA/case content; semantic checking uses original definitions; visual checking inspects the actual workbook/view. Describe each type of evidence accurately.

No source-review completion requires a live ISA controller, external CSAPI test suite, authenticated hardware operation, production client deployment, or resolution of unrelated historical programme gates. Those are different tasks, and none is authorized here.

## 7. Four case boundaries retained without expanding this correction

Dragino and AirGradient are documentary reference designs, and Campbell's logger/sensor pairing and printed logger status values are not a verified installed system. Bennett is historical: two EE181 serial identities across three dated service statements and two original NOAA mean events with four experimental digital representations. Keep the original quality token and time precision; unknown historical result availability, probe coordinates and exact replacement minute do not become invented ISA values.

These cases challenge an interpretation; their limited feature coverage is not a reason to ignore other relevant ISA concepts.

## 8. Recovery routing and earned progress

Current authority order: owner instructions in this chat → correction plan/progress → this recovery anchor → parent forty-step roadmap and historical source artifacts. Preserve valid earlier source work; reopen only a specific row or claim when new evidence warrants it. Historical source-selection delivery and successful workbook checks remain real accomplishments. The correction fixes source coverage and the meaning of blanks; it does not erase the existing project.

Today is the planning checkpoint. No workbook mappings changed and ISA-01 has not run. After the twelve correction passes satisfy their source-coverage tests, record **ISA correction COMPLETE** and return to Step16 owner review. A design choice awaiting that review does not turn the finished correction into an indefinite failure state.
