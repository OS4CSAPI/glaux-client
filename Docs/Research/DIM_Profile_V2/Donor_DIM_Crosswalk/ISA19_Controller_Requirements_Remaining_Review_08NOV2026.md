# ISA Controller Requirements — remaining-area original-source review (Delivery 19)

**8 November 2026 · Original ISA Step 11 / accelerated delivery 19 · original-source review completed.** Reviewed the original *ISA Controller Requirements*, release 6.0, revision 4, 31 October 2023, Distribution Statement A (Project source `ISA_Controller_Requirements-6.0r4.pdf`, file ID `file_00000000e00082109d88d0119f744880`, 74 pages). Delivery 19 covers **PDF pages 43–74 (printed pages 36–67)**, exactly the remaining **eight registered sections**: `CNTR-6.0`, `CNTR-7.0`, `CNTR-7.1`, `CNTR-7.2`, `CNTR-7.3`, `CNTR-8.0`, `CNTR-AppendixA`, `CNTR-AppendixB`. All assigned source text and Appendix A/B tables were examined; the verification-method and acronym tables also received targeted page-image inspection. This is **documentary review, not executed conformance testing**. Earlier Controller §§1–5.12 are preserved rather than rereviewed.

## Source-native requirement inventory

| Assigned section | Original PDF pages | Unique new normative requirements | Original IDs |
| --- | --- | ---: | --- |
| §6.0 — Authorization Service | 43–45 | **10** (1H/2M/7L) | AZSV-H-0001, M-0001–0002, L-0001–0007 |
| §7.0 — Live Data parent | 46–56 | **0 separately** | Context and nested §§7.1–7.3 only; no duplicate credit |
| §7.1 — Component Discovery | 46–49 | **13** (1H/3M/9L) | LDSV-H-0001, M-0001–0003, L-0001–0009 |
| §7.2 — Subscription | 49–53 | **17** (1H/4M/12L) | LDSV-H-0002, M-0004–0007, L-0010–0021 |
| §7.3 — Subscribed-to Data Delivery | 53–56 | **15** (1H/3M/11L) | LDSV-H-0003, M-0008–0010, L-0022–0032 |
| §8.0 — Further Resources | 57 | **0** | Help Desk instructions and Figure 1, not normative requirements |
| Appendix A — Requirement Verification | 58–73 | **0 new definitions** | Table 4 maps all 101 already defined low-level IDs to recommended methods |
| Appendix B — Acronyms | 74 | **0** | Table 5 has 18 source acronyms, not model fields |
| **Delivery 19 new source definitions** | | **55** (4H/12M/39L) | 55 unique requirements, all normative `shall` |

The full *Controller Requirements* source across **deliveries 18 and 19** therefore contains **163** distinct native requirements: **17 high-level, 45 mid-level, and 101 low-level**; **162 shall, zero should, and one may**. The sole earlier `may` is CMSV-L-0019 from delivery18. These counts refer to requirement **definitions**, not to physical objects, DIM attributes or executed tests.

## Authorization Service — §6

The Authorization Service is a distinct core service responsible for determining authorization of the request contained in an **Authorize Request** message, applying authorization rules (AZSV-L-0001/0002), and evaluating the contents of Registration REQUEST ADD and command Request messages (AZSV-L-0003/0004). Authorization *checking* is distinct from the Communication Service's registration, brokering and the actual execution of any requested command.

**Source distinction that must survive:** AZSV-L-0005 specifies **authorized = Yes** and Response **SUCCESS** when authorized; AZSV-L-0006 specifies **authorized = No** and the *same* Response **SUCCESS** when denied. A successful *authorization determination* must not be mistaken for authorization granted or for a successful command. AZSV-L-0007 separately covers inability to perform authorization: it refers to values under the policy in effect and illustrates an inaccessible authorization database. A note states that policy may permit none or all requests under those circumstances; **neither fail-open nor fail-closed is made universal by this passage**.

## Live Data discovery and state retention — §7.1

The Live Data Service maintains Config and Status information for discovery; native lower-level LDSV-L-0001/0002 explicitly qualify this obligation **if sufficient computing resources exist**, unlike the broader high/mid-level wording. Upon receiving DEVICE REMOVED, LDSV-L-0003/0004 require removing the maintained **Config and Status** message information for the cited component. This is cache/service state cleanup, **not deletion of original historical Event/Observation records**, and not proof of physical equipment disappearance.

LDSV-L-0005 matches available components against **maintained Config/Status** using the criteria in an **authorized and valid Discover Request**. LDSV-L-0006 responds FAILED when matching cannot be performed. LDSV-L-0007 instead returns SUCCESS with matching UCIs when matching can be performed, **even if zero UCIs match** (explicit source Note). LDSV-L-0008/0009 conditionally deliver the stored matching Config/Status information when that information is requested. Returned cached source-state information is neither a performed Observation nor actual external equipment command success.

## Subscriptions — §7.2

LDSV-L-0010 creates an authorized subscription using its **consumer identity** and filtering criteria. L-0011/0012 return FAILED or SUCCESS with a unique subscription identifier, respectively. L-0013 notifies the subscribing component using SUBSCRIPTION ADDED if the subscription was created at another component's request. Thus requester/creator and consumer are not automatically the same participant.

LDSV-L-0014 says the service maintains unremoved subscriptions **created by a component while that component is registered**. In contrast, L-0021 removes subscriptions whose **consumer** is the component named in a DEVICE REMOVED notice. These are different printed scopes. Preserve both rather than inventing one universal creator-versus-consumer lifecycle rule. L-0017–0020 separately cover Remove Subscription and responses or notification for removal by another component.

LDSV-L-0015/0016 require sending currently maintained matching **Config and Status** messages upon subscription creation. This does not turn original Events into a cached history. The Guide's previously reviewed optional initial-cache query behavior remains separately attributed; this specific Controller Requirements wording does not silently resolve any cross-document difference.

## Message matching and forwarding — §7.3

Received Config, Status, Event and Administrative messages can match subscriptions under LDSV-L-0022/0023/0030/0031. LDSV-L-0032 requires forwarding matching received messages to the **consumer**. The service does not become the original observation performer, and a forwarding requirement does not itself prove delivery or original issuer authenticity.

LDSV-L-0024/0027 describe entry/exit of subscription match upon a changed Status property; L-0025/0028 cover the analogous change with **Event detector properties**. L-0026 describes an Administrative **START FOLLOWING** notice, while L-0029 contains the **STOP FOLLOWING** code. A detector property inside an Event does **not** become a Status update, physical failure, original observation or persistent equipment attribute merely because it affects filtering.

### Literal source discrepancies — preserve rather than fix

1. **LDSV-H-0002** prints a **“Parent Requirements”** label before the four M-level requirements that it actually decomposes. Treat this as a source labeling discrepancy, not a redefined direction of inheritance.
2. **LDSV-L-0028** (Stop Matching Subscriptions Based on Event) prints parent **LDSV-M-0010, Forward Matched Messages**, while the surrounding matching-change clauses are under M-0009. Do not silently reassign its parent.
3. **LDSV-L-0029** is titled **“Notify Subscribers of Start Matching Subscriptions”**, uses the condition **“now matched”**, but explicitly sends **STOP FOLLOWING**. All three native statements persist in the original body and Appendix A; do not silently correct the heading, conditional text or code.
4. **Authorization service non-performance** remains policy-dependent; no single fail-open/fail-closed behavior, concrete error code or actual access-control implementation is established by the source.
5. **Resource-conditional cache duties** and differently stated creator/consumer subscription lifetime rules remain visible source-specific qualifications; they are not promoted into new primary DMS questions or additional research prompts without subsequent source-first reconciliation.

## Appendix A: exact verification census

Appendix A defines **four** methods: Analysis, Demonstration, Inspection and Test. Table 4 identifies a recommended method for **each of the 101 distinct low-level Controller Requirements** across service deployment, Communication, Authorization and Live Data. The 101 IDs reconcile with the source definition census of DPLY-L-0001–0004, CMSV-L-0001–0058, AZSV-L-0001–0007 and LDSV-L-0001–0032; **no ID was missing or duplicated**.

| Recommended method | Low-level entries |
| --- | ---: |
| Test | **95** |
| Inspection | **6** |
| Analysis | **0** |
| Demonstration | **0** |
| **Total** | **101** |

The **six Inspection** entries are DPLY-L-0004, CMSV-L-0002, CMSV-L-0005, CMSV-L-0006, CMSV-L-0040 and CMSV-L-0042. No original verification method is inferred, and these are **recommended methods, not tests we executed**. Appendix B contains **18 acronyms**, including CCD expanded as *Component Capability Description* (preserved alongside the earlier edition's Description/Declaration terminology boundary); it supplies context only.

## Existing master implications and source-fidelity limits

The material supports **existing** comparison candidates for authorization/permissions, registration, service roles, cached Config/Status, discovery, subscription identity and matching, Event context, Administrative START/STOP notifications, participation/departure and source attribution. A requirement to implement an ISA Live Data behavior does **not** automatically produce a new physical component, DIM class, original Observation, runtime result or verified equipment condition. Preserve all supported previous DMS catalogue outcomes, original donor/case cells and the separate future owner-adoption gate.

This source pass does not rerun runtime tests, deploy an ISA Controller, exercise device commands, revise another standard, adopt DIM/Profile content or rebuild the Excel workbook. **Source document review completion is distinct from the later source-first crosswalk audit.** Earlier full-Controller first-area definitions and the complete Component Requirements evidence are reused, not credited again.

**Next after cumulative publication:** accelerated Delivery 20 only — residual Data Model Topics source blocks, bounded 2015 access issue, and whole-ISA document/section reconciliation. Delivery21 then retains the original31 correspondence targets,25 earlier findings and six source-specific questions. Delivery22 retains final validation and canonical Excel refresh. No new plan/delivery is authorized by completing the Controller document.


## GitHub publication and readback closeout — 8 November 2026

**DELIVERY 19 PUBLISHED AND SOURCE-SCOPE VERIFIED.** The [structured native/verification evidence](ISA19_Controller_Requirements_Indexed_Evidence_08NOV2026.json), [current structured master](Master_Donor_Concept_to_DIM_Crosswalk.json), [readable master](Master_Donor_Concept_to_DIM_Crosswalk.md), [cumulative companion evidence](ISA_Service_and_Context_Evidence_08NOV2026.json), [279-block coverage register](ISA_Coverage_Register_07NOV2026.json), [exact status](ISA_Correction_Status_07NOV2026.json), [current ISA PITON](PITON_ISA_Coverage_Correction_07NOV2026.md) and [execution plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) were committed to `research/dim-profile-v2` and read back. Independent structural comparisons against the Delivery18 branch head found **329 original master row IDs and all displayed donor/ISA/case cells unchanged**, with58 earlier donor evidence records,73 case source facts and all prior holds retained. The 279-block register now marks Controller28/28 and Component34/34 reviewed, preserves480 DMS outcomes and six precise source questions, and contains170 cumulative source-boundary notes.

Scope precision: The evidence index records original native IDs/titles and exact original section locators; the authoritative complete requirement wording remains in the original project PDF. Only targeted appendix pages were visually inspected; the complete source was read as indexed text. Full native requirement titles were not separately independently revalidated word-for-word against the index after publication because the document-reading service became unavailable; the original source-text inventory and counts were completed before that interruption. The 101-row verification mapping and six non-Test IDs were checked against the source before publication. No actual ISA runtime conformance suite, whole-repository CI claim, external issuer authentication, model adoption or refreshed XLSX is asserted.

**Next separate “Proceed” = Delivery20 ONLY.** The Controller Requirements source review is closed. Reuse it, do not reopen it merely because earlier source-note wording remains literally discrepant.
