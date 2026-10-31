# PITON v2.0 — Whole-System DIM/Profile V2 course correction and delivery roadmap

**31 October 2026 · America/New_York**  
**Standing:** **Current recovery authority and step-plan pointer**, NOT a new Domain Information Model (DIM), adopted application Profile, architecture decision, OGC requirements document, or declaration that implementation is complete.

**Repository:** [OS4CSAPI/glaux-client](https://github.com/OS4CSAPI/glaux-client)  
**Research branch:** `research/dim-profile-v2` · **live application branch:** `work/details-view-20261023`  
**Home:** `Docs/Research/DIM_Profile_V2/`  
**New controlling work plan:** [Whole-System Recovery-to-Delivery Plan v0.1 — 43 prompt-sized steps](PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md)  
**Earlier complete history:** [PITON v1.9](PITON_DIM_Profile_V2_Continuity_v1.9_31OCT2026.md), [v1.8](PITON_DIM_Profile_V2_Continuity_v1.8_30OCT2026.md), the [original problem and outcome baseline](DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md) and [drift/hallucination correction](DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md). These documents remain unchanged; v2.0 supersedes only their *current priority/next-step instructions*, not their evidence or history. The PITON version is not the DIM/Profile specification version.

## 0. The next assistant should understand this before doing anything

**The owner wants a sound, donor-grounded way to represent entire sensing Systems and to let one CSAPI client render different vendor systems in a consistent but meaningful Resource Details experience.** The aim is an implementation-independent **DIM**, a separate, evidence-based **OGC API – Connected Systems (CSAPI) application Profile**, and a **reusable Profile-aware Glaux client**, not a collection of handcrafted product pages.

We made genuine progress in research and code, but our experiments were beginning to serve their own narrow technical questions instead of advancing that whole-System goal. In particular, the Bennett’s Point probe-swap example successfully tested real historical identity/attribution and live server round trips, then consumed more work solving one 52°North observation-encoding limitation. The last proposed SWE JSON codec/contract test was *not* an owner-selected strategic priority.

**The owner asked for a comprehensive, human-readable reassessment** after saying “idk man, this stinks.” The subsequent assessment concluded that the research and implementation should **not** be thrown away, but that the method should change: stop treating the next discovered server defect as the next work assignment; use several different equipment arrangements, donor-native meanings and source-fidelity tests to build a coherent whole-System DIM and justified Profile first.

**The owner then explicitly requested a start-to-finish, safely sized step plan in GitHub and an updated PITON.** That request authorized the **plan and this documentation update**, not immediate execution of all steps, server writes, UI deployment, adoption of final classes, or an unbounded new donor survey.

The new [43-step controlling plan](PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md) is **0/43 executed**. On the next **“proceed”**, execute **Step 01 only**: re-anchor purpose, branches, evidence standing and success criteria, and establish the first human-readable cumulative workbook. At the end of that step, explain what changed and state Step 02. Do not run subsequent steps without another “proceed,” and do not automatically resume the old SWE JSON recommendation.

## 1. Why the direction changed — a genuinely important assessment

The core concern is **not** that our results are imaginary. The problem is that progress on narrow technical mechanisms is easier to measure than progress on a connected, general information model, and we had begun pursuing the former automatically.

The [original problem baseline](DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md) asks how a common client can preserve source-vendor differences in identity, detector/transducer arrangements, configuration, condition, communications, capability, operational actions, source records and context. A **DIM** must describe the subjects/relationships; the **Profile** must make those meanings reliably communicable using existing OGC standards; the **client** must recover them without a separate author-coded interpretation for each vendor. Generic CSAPI resource retrieval alone is not success.

**What we genuinely learned from earlier donor research:**

- An identified physical unit is not its product model, manufacturer label or digital record.
- A physical part is not automatically a logical function, an addressed transducer channel, a field or a DataStream; one sensor can supply several properties.
- A documented capability is not a selected setting; a requested command is not an acknowledged/completed action or observed effect.
- An observation's subject/observer, the equipment that logs/reports it, its time, quality, source and calculated interpretation can be different roles.
- A source definition, published message, synthetic fixture and actual historical record have different evidentiary standing.

These are **useful candidate distinctions**, not a coherent whole-System DIM yet. The five F-01–F-05 research headings have *not* been adopted as five obligatory classes; the right domain boundary/chassis/name remains to be discovered through fair donor and equipment comparisons.

**What the review found deficient:**

1. **Fragmentation:** Many individual “do not conflate” rules and example sections, but no sufficiently connected model/architecture of the whole sensing System.
2. **Donor fairness:** A 182-artifact source corpus has been collected, but that is not 182 independent standards and not equal-depth original-source study. The earlier five distinctions influenced later comparisons. ISA, SOSA, IEEE 1451, SAPIENT, AAS, PA-DIM, OPC UA Devices, OMS, WoT and others may require a revised structure—not merely fit existing headings.
3. **Weak whole-System empirical breadth:** AirGradient, Dragino and Campbell are qualified **manufacturer reference/example** arrangements, not independently authenticated operating installations. Bennett’s Point is **actual historical measurement+equipment-history evidence**, but limited, not a complete station operational dataset.
4. **Prototype-specific interpretation:** The [candidate term rulebook](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/src/profile/resource-details-proof.ts) uses authored semantic terms in fixtures, and the [live Bennett page](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/src/presentation/resource-details-live-bennett.ts) fetches preselected server IDs. These illustrate the idea but are **not** a truly source-independent, machine-readable Profile interpreter.
5. **Question drift:** The real issue “how do whole station/logger/probe/reporting relations survive?” gave way to “how can this particular 52°North server store the original QA token and 15-minute window?” The latter was technically worthwhile but insufficiently central to the DIM's current maturity.
6. **Duplicate representation risk:** Two NOAA measurements currently appear in two *original scalar* and two *archival-report* server Observation resources; the latter are representations of the same measurements, **not two more measurements**. The offline station-led stream and live probe-led streams reflect **different unresolved reporting-system assumptions**.
7. **UI as test, not authority:** Codex's Map renderer and the Resource Details placement matrix are helpful, but choosing tabs or making a polished page does not justify DIM classes or Profile requirements.

**Course correction:** Use real source-native equipment arrangements to test a proposed common meaning, challenge it with donor-native standards, derive only the justified DIM relationships, define a scoped CSAPI Profile and then prove whether the **same client interpretation** can correctly handle different vendors. The objective is not to reproduce proprietary screens exactly, assume complete proprietary source access, or invent universal coverage.

## 2. The outcomes that count — and those that do not

| Project layer | Current, source-supported state | What completion must actually demonstrate |
| --- | --- | --- |
| Standards/donor research | Strong partial source pedigree and documented gaps; candidate foundation v0.2, newer worked sections and donor side-by-side terms. | A **fair, targeted, original-source-supported** choice of whole-System meanings, with rejected alternatives and unexamined donor contributions visible. |
| DIM | Five candidate research distinctions and partial whole-system relationship text, but no mature integrated normative/conceptual architecture. | A **connected**, implementation-independent model with understandable relationships, constraints, justified specializations and scoped coverage, challenged against multiple different system arrangements. |
| CSAPI Profile | Many source-based proposed bindings and examples; no complete adopted implementation contract. | A **separate, testable and qualified** selection of CSAPI/SensorML/SWE Common carriers and conventions with examples, conformance scenarios and explicit unsupported requirements. |
| Source evidence | AirGradient, Dragino, Campbell documentary/reference cases; two historical Bennett measurements with separate equipment-history attribution. | Clear scope and provenance for every case. Never declare model examples to be live physical installations or treat missing source data as a zero. |
| Glaux | Live 52°North GETs, a case-specific Bennett page, prepared cross-vendor fixtures, a reusable Map, and qualified QA/interval display. | A **shared semantic interpreter** using the same Profile meanings for different cases, with a transparent source→DIM→Profile→client fidelity scorecard. |
| Final review/publication | Research and implementation artifacts, but no final publication gate. | Publication-ready **candidate** DIM and Profile, reproducible tests and a human-readable result/limitations statement. External standards adoption is not promised. |

**The most important new technical question:** In Bennett’s Point, who is the *observing probe*, who is the *station/logger that aggregates and reports an average*, who is the *host/whole System*, and who is the CSAPI DataStream's producing System? Our **offline station-oriented stream** and **live probe-owned streams** made different choices. This needs an equipment/donor/semantic decision **before** treating an encoding workaround as a final Profile rule.

## 3. Reuse the evidence we already have

The plan uses four deliberately different examples, but **does not call them four equivalent fielded systems**:

| Case | Source-grounded job | Limitation |
| --- | --- | --- |
| [Dragino S31-LB](Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md) | One external temperature/humidity probe, node, radio/battery/commands and documented outputs | Manufacturer reference/message examples; no authenticated installed unit |
| [AirGradient Open Air Max](Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md) | Multi-board/multi-sensor assembly, functions, measurements, communications and power | Product/reference and cloud examples; no joined operating individual verified |
| [Campbell CR1000X + first-generation ClimaVue 50](Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md) | Separate sensing assembly and logging/reporting/controller role | Reference arrangement; don't join unrelated status/firmware/program examples as one deployed installation |
| [Bennett’s Point, ACE Basin](Candidate_Specification/examples/bennetts-point-ee181.json) | True historical measurements around an EE181 probe replacement, operator source QA, time and distinct physical serials | Only a bounded real historical observation/equipment-history case, not the full station and no verified Deployment resources |

The earlier **TRSS/OmniSense** cases remain the reason the project was started, not compulsory experimental anchors. The **Smart Citizen Kit 2.3** design case remains informative, not a fielded authenticated individual. The owner had previously identified source-breadth gaps; Step 04 provides a narrow opportunity to check obtainable, better-linked actual operating evidence **without restarting the eight-step qualification plan or promising that a full packet exists**.

**Retain old results rather than replacing them:**

- [Original whole-System objective](DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md); [existing donor alignment comparison](Concept_Donor_Comparison/README.md); [donor-native terms](Concept_Donor_Comparison/Donor_Terms_Side_by_Side.md); [drift correction](DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md).
- [Candidate DIM foundation v0.2](Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md), [candidate DIM additions](Candidate_Specification/DIM.md) and [candidate CSAPI Profile](Candidate_Specification/CSAPI_Profile.md). These may change through justified work, not overwrite source claims.
- [Bennett offline evidence and reader](Candidate_Specification/examples/bennetts-point-wire/README.md), [actual live-server bridge report](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/BENNETT_OBSERVATION_CONTEXT_BRIDGE.md), [Codex Map reuse](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/BENNETT_LIVE_MAP_INTEGRATION.md), and [observation encoding options](Candidate_Specification/Observation_Encoding_Decision_31OCT2026.md).
- **The complete original OMS 3.0 standard is preserved**. [Source/recovery index](Primary_Sources/OGC_20-082r4_OMS_3.0.0.md): original 198-page PDF in connected Google Drive file ID `1QNBXosCb_TcSP96tppQAyLv42WdnU7G2`, page-marked extracted text ID `10B6djSL1kCDFSZ_vJipx5h_kpNZ8wSPW`. Recover from Drive through the connected tool before claiming normative source access is missing.
- Public IEEE 1451/NIST Playground resources, original ISA and SOSA PDFs, the pinned SAPIENT v2 document and companion code, and other donor editions have source registers. Original texts and exact edition limits control claims; a file list is not normative proof.

## 4. The controlling 43-step plan and how to run it

[**Read the complete staged plan and per-step acceptance tests**](PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md).

| Phase | Prompt steps | Why it exists | Gate |
| --- | --- | --- | --- |
| **A — Purpose/evidence and success test** | 01–04 | Re-anchor the objective, evidence levels and feasible case packets | Exact scope/evidence adequacy, not imagined datasets |
| **B — Four source-native arrangements** | 05–09 | Understand source equipment/roles before imposing a DIM | Human-readable cross-case differences/unknowns |
| **C — Fair donor/chassis review** | 10–15 | Explore competing whole-System frames on original standards evidence | Defensible provisional scope or explicit unresolved alternative |
| **D — Connected DIM** | 16–24 | Establish coherent physical, functional, operational, temporal and provenance roles | Draft and falsification across four cases, not five immutable slots |
| **E — CSAPI Profile** | 25–31 | Separate conceptual meaning from actual testable standard bindings | Scope-qualified Profile draft and counterexample tests |
| **F — Shared client interpreter** | 32–39 | Replace handcrafted case-specific meaning with reusable Profile-driven reading | Same interpretation across different source cases and qualified live CSAPI path |
| **G — Fidelity/publication review** | 40–43 | Compare original source to user-facing result, repair/block and prepare candidates | Publication-ready **candidate** outputs or explicit limited/not-ready outcome |

**All 43 numbered steps are PENDING; Step 01 is NEXT.** Each step's table in the plan names a bounded task and **observable completion condition**. The current instruction is to do **one numbered step per owner “proceed.”** Do not conflate a phase-gate review with a request for repetitive permission inside an already authorized prompt. A later blocker can lead to a small explicitly numbered repair step in the same tracker; never hide scope growth or mark an unresolved technical problem as complete.

### Iteration response rule

At the end of each completed prompt, explain in normal language:

1. **What did we learn or actually change?** (one real example)
2. **What is better understood about the whole System?**
3. **What does this imply, if anything, for the DIM, Profile and common client?**
4. **What remains unknown, unsupported or contradicted?**
5. **What exactly will the *next* “proceed” do?**

Prefer short paragraphs, clearly defined terminology, accurate standard editions and ordinary links to GitHub. Avoid lengthy internals, status recitations and “AI for AI” research reports. Use a small number of **cumulative evidence/decision documents**, not a new report per small prompt. Preserve PITON/recovery markers at completed phase boundaries or before chat resets.

## 5. Branch discipline and live resources

- **Research/specifications and plan:** `research/dim-profile-v2`; read and update files under `Docs/Research/DIM_Profile_V2/`. Never assume GitHub default-branch code search includes these documents.
- **Client and deployed code:** `work/details-view-20261023`; be deliberate about cross-branch documentation links and earlier independent Bennett renderer on research branch. Do not blindly merge.
- **Published running service:** [52°North/pygeoapi CSAPI on Oracle](https://129-80-248-53.sslip.io/csapi-pygeoapi/) — real server, but not proof of live sensor telemetry or complete standards conformance.
- **Current live demonstration:** [Bennett’s Point CSAPI](https://glaux-client.pages.dev/?page=resource-details-live-bennett), [generic live CSAPI browser](https://glaux-client.pages.dev/?page=resource-details-live-csapi), [Codex live Map](https://glaux-client.pages.dev/?page=resource-details-live-map), [prepared historical Bennett fixture](https://glaux-client.pages.dev/?page=resource-details-profile-test&case=bennetts-point).
- **Verified historical checkpoints:** [load/read-back run 41248245591](https://github.com/OS4CSAPI/glaux-client/actions/runs/41248245591) and [latest Glaux deploy run 41248473107](https://github.com/OS4CSAPI/glaux-client/actions/runs/41248473107), source revision `54b4e576472d89d4dbb3e67fdce0733c8bb84926`. These were checked on 31 October, **not** a promise about all future server/app states. New README/PITON commits do **not** deploy Glaux.
- **Exact server IDs, source rows and QA tokens:** retained in [PITON v1.9 §§3–6](PITON_DIM_Profile_V2_Continuity_v1.9_31OCT2026.md) and the [archival bridge report](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/BENNETT_OBSERVATION_CONTEXT_BRIDGE.md). Avoid repeating and accidentally altering them.

This PITON/plan update makes **no code, production site or server-data change**. No steps have been performed as part of writing it.

## 6. Recovery process for another chat

1. **Read PITON v2.0** and [the 43-step plan](PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md), especially the top contract, current step statuses and phase gates.
2. Read [PITON v1.9](PITON_DIM_Profile_V2_Continuity_v1.9_31OCT2026.md) for exact October 31 server/app and source evidence, then [v1.8](PITON_DIM_Profile_V2_Continuity_v1.8_30OCT2026.md) as needed for earlier donor and equipment history; the [AI drift study](DIM_Profile_V2_AI_Hallucination_and_Drift_Case_Study_v0.1_30OCT2026.md) is essential before choosing any new modeling priority.
3. Verify **both** branch heads and the real committed plan state using the GitHub connector; do not assume any future work not recorded there is complete.
4. Unless the user expressly requests a status explanation or plan revision, when they say **“proceed”**, execute only the next **PENDING** plan step. Step 01 begins with a human-readable baseline and the cumulative work area, *not* a SWE JSON codec, a 182-source survey or a new UI route.
5. Do not promote a past assistant recommendation, a completed plan, an experiment's `PASS`, an HTTP 200, a working map or a DataRecord carrying time into adopted model authority. For original standards claims, read the actual clauses and note which statements are project interpretation.
6. Respect explicit user instruction to preserve old pages and work, keep one step per prompt, explain outcomes naturally, and end each authorized iteration with the next step spelled out.

### Ready-to-paste next-chat opening

> Recover the whole-System DIM / OGC API – Connected Systems Profile V2 effort from **PITON v2.0** on `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, at `Docs/Research/DIM_Profile_V2/PITON_DIM_Profile_V2_Continuity_v2.0_31OCT2026.md`. Read the new 43-step `PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md`, then the detailed prior PITON v1.9 and original problem baseline as needed. The owner approved planning a strategic return to the whole sensing System and shared client meaning; Step 01 is NEXT and 0/43 have been executed. Do **not** automatically resume the isolated SWE JSON work, force the old five concepts or V1 power chassis, combine research and live app branches, or pretend published manufacturer reference examples are live systems. Explain our state in normal language and execute only the next explicitly requested “proceed” step, with source-grounded output and a clear next-step statement.

## 7. Current next action

**On the user's next “proceed”: Step 01 only** — confirm current research/app state against this PITON, create the cumulative human-readable workbook, and state the actual whole-System problem and evidence limits. **Then stop. Step 02 will define the success/fidelity test.**

If the owner changes the goal or a gate reveals that a release claim cannot be supported, update the tracked plan and this PITON as needed rather than silently continuing or reporting fictitious completion. The end-state is **defensible publication-ready candidates and a scoped reusable client proof**, or an explicitly limited outcome with release blockers—not adoption of an external standard.
