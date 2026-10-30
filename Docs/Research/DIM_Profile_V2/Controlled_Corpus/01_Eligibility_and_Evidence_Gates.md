# Step 01 — Controlled-Corpus Eligibility and Evidence Gates

**Version:** 0.1 · 29 October 2026 (US Eastern)  
**Standing:** **STEP 01 CRITERIA COMPLETE; NO CANDIDATES ASSESSED OR SELECTED.** The owner's “proceed” in Profile Rewrite 6 authorized this step only. Product discovery, equipment audits and data acquisition have not started.  
**Workspace:** `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, `Docs/Research/DIM_Profile_V2/Controlled_Corpus/`.  
**Governing plan:** [Controlled Sensing-Equipment Corpus Qualification Plan](../PLAN_DIM_Profile_V2_Controlled_Sensing_Equipment_Corpus_Qualification_v0.1_29OCT2026.md), Step 01 and §§2, 5–7.  
**Purpose:** Support the implementation-independent Domain Information Model (DIM), separate OGC API – Connected Systems (CSAPI) application Profile and shared System Resource Details experience described in the [Original Problem and Outcome Baseline](../DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md), §§1–3. The [Research Story](../DIM_Profile_V2_Research_Story_and_Current_Position_v0.1_29OCT2026.md), §§8–12, explains why source completeness and faithful interpretation matter.

## 1. What this step establishes

We need a small set of equipment cases whose public evidence is rich enough to test meaningful whole-System questions later. A collection of attractive datasheets is not that set. Nor is an observation feed with no defensible connection to the equipment, configuration or documentation being studied. The gate asks whether we can explain the equipment and inspect usable source information without filling the gaps ourselves.

This document makes the plan's four minimum eligibility conditions, six evidence categories and six comparison dimensions operational. **The decision rules and scoring anchors below are project research-method choices, not requirements taken from a donor standard or facts about any candidate product.** No new donor review, adopted DIM concept, final domain name, Profile requirement or application change is introduced. The pre-step repository baseline was `cc16cb751dbcf860319d029cb5b64ac1d98b4311`.

A **documented complete reference configuration** can qualify without an authenticated installed unit. Its evidence must remain design/example evidence. A case with attributable real records may support additional temporal or operational questions, but those records do not automatically verify every installed part, calibration claim or firmware version. Qualification states **what the case can support**, not that every fact about a deployed System is known.

## 2. Four eligibility gates — check before comparing scores

Each gate receives **MET**, **UNVERIFIED** or **NOT MET**, with source locators and a short explanation. A missing source is not evidence that the equipment lacks the feature. These gates determine eligibility as a **primary whole-System case**; a failed candidate may still supply useful limited or controller-level reference material.

| Gate | Evidence needed to mark MET | What prevents a primary-case pass |
| --- | --- | --- |
| **G1 — A bounded, identifiable sensing configuration** | Identify an exact product/variant or documented reference build capable of unattended or remote sensing. State the case boundary, sensing elements and necessary supporting equipment. Distinguish a product design/reference build from an installed individual. For a modular logger, identify the documented logger-plus-sensor arrangement rather than inventing a station from supported ports. | Bare chip, controller alone, generic tutorial, ambiguous product family or a supposed complete configuration assembled from unrelated variants without source support. Unknown installed identity is not a failure when the declared case is a documented reference build. |
| **G2 — Meaningful first-party whole-System documentation** | Inspected manufacturer/developer material explains sensing composition, power, communications, normal operation and configurable or explicitly fixed behavior for the case. It distinguishes supplied/required elements from optional ones and explains the source meanings relevant to the records used. Record the depth and gaps in capability, condition and diagnostics separately. | Only marketing claims or an option list; no supported account of the equipment boundary or essential power/communications/sensing arrangement. A fixed-function device need not have remote commands, and mains-powered equipment need not have a battery. Do not invent either. |
| **G3 — At least one usable, attributable machine-readable record or original example** | Actually retrieve and inspect at least one source-native observation, status or configuration record, or an explicit original manufacturer/developer example of one. Locate field-level definitions and establish the supported relationship to the stated product/configuration. Preserve native keys, units/codes, subject and time context where supplied; document absent context. Check configuration, status and measurement availability separately. | An API advertised but not accessible, schema declarations alone, screenshots alone, a private endpoint with no usable public alternative, or assistant-authored payloads. A retrievable original published example can meet this gate; it does not prove a deployed unit or current state. Missing one of the three record categories is a recorded limitation, not automatic failure if the minimum is otherwise met. |
| **G4 — Traceable, reproducible and honestly bounded evidence** | Each material claim has an owner, title/file, original locator, edition/release or capture date, applicability, evidence label and known access/reuse conditions. Documentation and records can be related without silently joining incompatible variants. Provide reproducible access instructions and an explicit gap ledger. Copy only material whose redistribution is permitted. | Material assertions depend on uninspected sources, irreconcilable versions, an unproven device/document join, invented values, or inaccessible evidence with no public substitute. An unstated firmware version must stay unknown; it blocks version-dependent claims, not necessarily unrelated documented design facts. A capture date is not a firmware version or a guarantee of permanent availability. |

**Interpretation of “complete”:** enough evidence to describe the particular sensing configuration as a whole, not exhaustive knowledge of all lifecycle, security, calibration or proprietary functions. G2 does not require every possible diagnostic. G3 does not require every record category, a live feed, an account, or physical possession. Conversely, plentiful measurements do not excuse a failed whole-System boundary or missing equipment documentation.

**Scope rule:** A record may be attributable to a product-level example without being attributable to an individual installation. State that narrower scope. A station ID, software device ID or channel ID alone does not prove a hardware identity or component inventory. Related documents may be used together only to the extent their applicability is supported; unsupported joins remain gaps.

## 3. Evidence labels — retain the plan's vocabulary

Labels apply to the **specific claim, excerpt or record**, not indiscriminately to every assertion in a source. One manual can contain both design specifications and an explicitly illustrative payload. These labels identify evidence kinds; they are not interchangeable confidence scores.

| Label | Permitted interpretation | Limit to preserve |
| --- | --- | --- |
| **REAL_RECORDED** | Retrievable, attributable observations/telemetry from a real device or station, with available time, subject and source context. Record original publisher/operator and reporting path when known. | Not automatically current, calibrated, manufacturer-owned, or proof of a complete installed inventory. Public historical records remain historical. |
| **PRIMARY_PUBLISHED_EXAMPLE** | An original manufacturer/developer's explicitly published sample payload or example configuration. | Demonstrates a format or example behavior, not measured values or an actual deployment unless separately established. |
| **PRIMARY_DESIGN_OR_SPEC** | Manufacturer/developer datasheet, manual, hardware/firmware reference, interface/schema or versioned original source. | Describes design, allowed configuration or capabilities; does not establish what is installed, selected or occurring in an individual unit. |
| **SECONDARY_TECHNICAL** | Credible external research, implementation or field notes, with their own attribution. | Useful context; not silently promoted to first-party design authority. Attribute independently verifiable real records to their actual origin. |
| **SYNTHETIC_OR_DERIVED** | Authored fixtures, reconstructions or transformations, with input and method identified. | Cannot replace original evidence for G3. A transformation of genuine recorded data retains a link to that original; the transformation itself is not an original device record. |
| **UNAVAILABLE_OR_UNVERIFIED** | Access-gated, missing, uninspected or insufficiently attributable material/claims, including unknown version applicability. | Not evidence of coverage. Distinguish “not retrieved” from “product does not support.” |

**For every material claim, retain:** case/variant; source owner and title/file; stable original URL; release, edition, commit or capture date; exact page/section/line/key when obtainable; evidence label; what it establishes; what it does not establish; and access/redistribution limits. Add access date and timezone. Record checksums only for bytes actually obtained; a checksum verifies those bytes, not the truth of their contents.

## 4. Ask the same questions of every case

These are comparison questions, **not DIM modules, mandatory product features or a predetermined user-interface layout**. Answer from sources, and retain native terminology before proposing any later common interpretation.

| Question | What the audit should distinguish | Why it matters to the eventual Details view |
| --- | --- | --- |
| **Q1 — What exactly is this case?** | Product family versus precise model/variant; reference build versus installed individual; hardware, station, channel and software identities. | Prevents displaying a model's capabilities as facts about an authenticated unit. |
| **Q2 — What is physically or functionally included?** | Documented assembly, required peripherals and options; installed evidence where present; physical transducer versus output/channel; enclosure, controller and host relationships. | Prevents turning an options catalogue or multiple output channels into a fabricated hardware inventory. |
| **Q3 — What can be configured or commanded?** | Supported choices versus example settings versus actual selected state; fixed behavior where documented; request, acknowledgement and outcome where available. | Prevents “supports” becoming “is using,” or a command description becoming proof of successful execution. |
| **Q4 — How does it operate and report condition?** | Power source and reported quantities, diagnostics, errors, modes and reporting intervals; measured, estimated, calculated or categorical values; units, subject and validity/time when supplied. | Prevents equating voltage, estimated capacity, a diagnostic result and overall readiness. No missing status is invented. |
| **Q5 — What information can we actually inspect?** | Configuration, status and observation artifacts separately; protocol/interface, native fields and definitions; examples versus real records; source producer and intermediary where known. | Establishes usable inputs for a later experiment rather than a list of advertised integrations. |
| **Q6 — Do records and documentation describe the same scope?** | Model/firmware applicability, station or device linkage, sensor configuration, source timestamp and known transformation history. | Prevents combining one variant's manual with another device's telemetry to fabricate a complete case. |
| **Q7 — Can another researcher retrieve and understand it?** | Exact locators, releases/captures, reproducible small retrieval, access restrictions, reuse permissions and unresolved provenance. | Makes later source-to-representation fidelity checks repeatable and accountable. |
| **Q8 — Which useful similarities and differences should survive?** | Supported shared whole-System questions, legitimate modality-specific details, absent/unknown information, and comparability limits relative to the original unattended ground sensing use case. | Keeps the common Details experience useful without requiring identical fields or vendor-specific invention. No rendering or mapping is implemented in this step. |

**Availability is not absence:** Record “retrieved,” “located but not retrieved,” “not found in this bounded review,” or “source explicitly states unsupported/not applicable,” with a locator for the last. Do not label a feature unsupported merely because its documentation was not found.

## 5. Transparent comparison — six dimensions, no compensating total

Use the plan's scale: **0 absent, 1 thin, 2 useful, 3 strong**. Here “absent” means no qualifying evidence obtained in the bounded audit, not proof of an absent equipment feature. Each score needs concrete source support and a limit. Scores summarize evidence depth; **do not sum, average or weight them into an eligibility decision**. An optional feature legitimately not applicable is explained within the relevant dimension, not converted into imaginary evidence or an automatic maximum.

| Evidence dimension | 0 — absent | 1 — thin | 2 — useful | 3 — strong |
| --- | --- | --- | --- | --- |
| **Whole-System component/architecture depth** | No attributable arrangement. | Product overview or options only. | Bounded sensing configuration and documented power/communications/component roles. | Version-applicable assembly/architecture detail with clear constituent, peripheral and optional-element distinctions. |
| **Capability/configuration depth** | No usable description. | Capability list without setting/fixed-behavior detail. | Native limits, modes or settings/fixed behavior explained for the case. | Detailed configuration/program/interface material and an attributable actual or original example configuration; supported and selected states distinguished. |
| **Operational condition/power/diagnostic depth** | No usable evidence. | General “health” or power claims. | Specific condition/power/diagnostic meanings, units/codes and limitations documented. | Rich documented meanings plus retrievable actual or original example status evidence with subject and time semantics where applicable. Label examples explicitly. |
| **Machine-readable source/communication depth** | No retrievable record/example. | Located interface/schema, but no inspected usable record/example or unclear fields. | One attributable usable native record/example plus field definitions and communication context. | Coherent versioned interface with complementary inspected record types and explicit field/subject/time meanings. |
| **Actual attributed observations/history** | No qualifying real records; examples do not count here. | Actual records exist but attribution/time/configuration linkage is too weak for the intended use. | Small attributable real observation/telemetry extract with subject and time context and explicit linkage limits. | Reproducible temporal series with well-supported instrument/configuration association and documented quality/time limits. This is not proof of calibration. |
| **Reproducibility/version/rights** | Sources not reproducibly locatable or essential applicability/access unresolved. | Mutable/partial references with material provenance gaps. | Specific locators and applicable versions/captures, retrieval procedure, declared rights/access and explicit unknowns. | Stable versioned sources, reproducible permitted small examples and coherent applicability trail; checksums for any retained evidence bytes. Permission to redistribute every manual is not required. |

A case may pass the four gates while scoring **0 for actual history**, because the plan explicitly admits original published examples. Its permitted uses are then limited accordingly. Rich condition documentation is still valuable when real condition telemetry is unavailable; the audit must not claim to have obtained that telemetry. Likewise, a high history score cannot repair an undefined station configuration.

## 6. Verdicts, hard failures and selection discipline

**PASS:** All four gates are MET, the evidence permits a bounded whole-System case, and limitations and six scores are documented. State whether the usable records are real, examples, or a mixture. PASS means eligible for Step 07 comparison, **not selected**, fully characterized, interoperable or conformant to any donor standard.

**CONDITIONAL:** No established hard failure, but at least one gate is UNVERIFIED. Name the specific missing evidence and what would resolve it; a precise access/applicability problem is different from general hope that more data exists. Conditional cases are **not admitted as qualified primary cases**. They remain reserve/limited-use evidence unless the missing gate is affirmatively resolved within the authorized work; this status does not authorize another audit or indefinite retries.

**FAIL:** At least one gate is NOT MET within the bounded audit: for example, controller-only evidence presented as a station, no adequate first-party System account, no usable native record or original example, or claims that require fabricated/incompatible joins. Explain the decisive gap and any narrower legitimate value. Failure concerns **evidence suitability for this exercise**, not product quality or universal impossibility of obtaining more information.

In Step 07, seek **2–3 passing systems** and compare their coverage and differences. Prefer different manufacturers, modalities and structural arrangements as the plan directs; explicitly disclose any unmet diversity objective rather than imposing identical fields. Check at least one serious seismic/acoustic or other field-surveillance comparator during Step 02. No individual source's evidence can repair another case's failed gate. With fewer than two passing cases, record **NO QUALIFIED SET** rather than relaxing the gate.

A set supported only by design and published samples can be qualified **only for those evidence-supported uses**; it cannot support claims about actual operating-state fidelity or fielded interoperability. Record whether actual temporal records are available for any selected case and which future tests remain blocked. Criteria changes require an explicit dated correction with its reason and effects on earlier verdicts, never a silent change to help a preferred product pass.

## 7. Reusable one-case audit template

Copy the template below into the appropriate Step 03–06 artifact. It is a reporting aid, not additional steps. Fill only sourced findings; use explicit unknowns, keep native field names, and do not create synthetic operating values to fill the table. The eight questions in §4 and six dimensions in §5 apply unchanged to each case.

```markdown
# Step 0N — Candidate [A/B/C/D] Evidence Audit: [precise case]
Date/timezone: [actual audit date]
Criteria: 01_Eligibility_and_Evidence_Gates.md v0.1 [commit/ref]
Standing: [PASS / CONDITIONAL / FAIL] for evidence eligibility only; not selected.

## A. Case and comparability
Manufacturer/developer; product/model/variant; hardware/firmware scope.
Case basis: [documented reference configuration / attributable installed case].
System boundary and sensing/peripheral/power/communications arrangement.
Installed identity/configuration evidence, or explicit absence of that evidence.
Relation and limits relative to TRSS/OmniSense; no military-equivalence claim.

## B. Source manifest and access
| Source ID | Owner; title/file | Original URL and exact locator | Version/release/capture and applicability | Access date/timezone; retrieval result | Evidence label(s) for used claims | Access/reuse limits |
| --- | --- | --- | --- | --- | --- | --- |
| [S01] | [...] | [...] | [...] | [...] | [...] | [...] |
For each material claim, say what the cited source proves and cannot prove.
Do not invent a checksum or treat public access as redistribution permission.

## C. Eligibility gates
| Gate | MET / UNVERIFIED / NOT MET | Evidence locator | Gap and consequence |
| --- | --- | --- | --- |
| G1 | [...] | [...] | [...] |
| G2 | [...] | [...] | [...] |
| G3 | [...] | [...] | [...] |
| G4 | [...] | [...] | [...] |

## D. Shared questions and evidence coverage
Answer Q1–Q8 with source IDs, native distinctions, and unresolved questions.
| Evidence area | Retrieved design/spec evidence | Retrieved actual record or original example, with label | Missing/unverified material and consequence |
| --- | --- | --- | --- |
| Whole-System/component context | [...] | [...] | [...] |
| Kind/version/capability | [...] | [...] | [...] |
| Configuration/commands | [...] | [...] | [...] |
| Condition/power/diagnostics | [...] | [...] | [...] |
| Communications/machine data | [...] | [...] | [...] |
| Records/reproducibility | [...] | [...] | [...] |
Explicitly distinguish configuration, status and measurement record availability.

## E. Small native record/example check
Original source locator; retrieval method/date; type/version; record evidence label.
Subject/model/station linkage and time meaning, or precise unknowns.
Retain a small permitted original excerpt/file where appropriate, otherwise link.
| Native field/key | Source-defined meaning and locator | Unit/code/type | Subject and time scope | What must not be inferred |
| --- | --- | --- | --- | --- |
| [verbatim source key] | [...] | [...] | [...] | [...] |
State whether any parse/format check was actually performed and what it proved.
No format check is a hardware, Profile or semantic-conformance test.

## F. Six evidence scores
Report the six dimensions from §5: score 0–3, source locator, reason and limit.
Do not calculate an aggregate score or hide a failed gate.

## G. Verdict and allowed uses
Explain PASS / CONDITIONAL / FAIL and the decisive gate findings.
State which questions the case supports now and which future tests it cannot support.
Separate real records, original examples and design facts in the conclusion.
List precise blockers, unresolved joins and narrower useful evidence.
No final selection; no additional audit automatically authorized.

## H. Owner-facing explanation and next step
What evidence was actually obtained? Why is it good enough or insufficient?
What remains missing? Name only the next unfinished step in the governing plan.
```

## 8. Step 01 completion and next action

**Completed:** defined four eligibility gates, preserved all six plan evidence labels, set eight shared questions, anchored the six 0–3 dimensions, defined PASS/CONDITIONAL/FAIL and supplied the reusable audit template. This is a completed research-method artifact, not a product finding. **No new equipment evidence was acquired; no candidate was assessed, scored or selected.** The candidate DIM v0.2, frozen donor inventory, closed donor plans and separate Glaux application branch remain unchanged.

The protection against invented vendor data is concrete: every claim must identify its source and scope; a record must actually be retrieved; an example cannot become a measured state; an option cannot become an installed part; and missing evidence prevents or limits qualification rather than being supplied by the analyst. We can accept useful bounded examples without pretending they are real operating telemetry.

**Next separate “proceed”: Step 02 only — bounded discovery of approximately 6–8 candidates and selection of exactly four audit slots**, using these criteria. The existing four suggestions remain hypotheses, not winners. Record provisional evidence availability and replacement reasons in `02_Discovery_and_Four_Audit_Slots.md`; do not conduct the four deep audits, select the final corpus, change the DIM/Profile or edit/deploy Glaux in that step.
