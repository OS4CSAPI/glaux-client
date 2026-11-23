# PROV donor comparison checkpoint

Baseline dc97640. This records the first row adjudications against the [pinned provenance sources](PLAN_PROV_Source_First_Donor_Review.md). References to PROV-DM and PROV-O below refer to the 30 April 2013 Recommendations.

| Master row | Finding | Original source |
|---|---|---|
| 220 · S06-R021 | Partial. Attribution can identify an agent responsible for an entity. An edition and source locator can accompany an entity as attributes. Evidence standing and verification of an issuer require separate semantics. | PROV-DM §§5.3.2, 5.7 |
| 221 · S06-R022 | Direct for the stated distinction. Give the originating occurrence and each experimental representation distinct identifiers and kinds. Relate the generated representation to its generating activity. Use derivation between source and copy entities where the content lineage is asserted. | PROV-DM §§5.1.1–5.1.3, 5.2.1 |
| 230 · ISA-R-MESSAGE-REFERENCE | Partial. Entity identifiers and attribution support reference to a particular source message and author. Conversation scope and message types come from the messaging model. | PROV-DM §§5.1.1, 5.3.2, 5.7 |
| 357 · AAS-O2-RECORD-ADMIN | Partial. Explicit revision links can connect independently identified records and attribution can identify a responsible agent. A business revision label alone cannot establish whether substantial content came from a predecessor. | PROV-DM §§5.2.2, 5.3.2 |
| 372 · AAS-O4-RECORD-HISTORY | Related. Specialization can relate a time-scoped record to an entity with more general aspects. It does not define the repository operation, version selection or retention behavior. | PROV-DM §5.5.1 |
| 603 · JOINT-SAMPLE-RECORD-TIMES | Direct for time separation. The measuring activity can carry start/end times and the resulting record can carry its own generation time. Times for report creation require the report to be identified separately when appropriate. | PROV-DM §§5.1.2–5.1.3 |
| 629 · N4242-LINEAGE | Partial. Derivation relates derived and contributing raw entities. Generation and usage qualify the link when execution evidence is available. Collection membership supports grouping. Radiation types and the conditions on raw-reference placement remain N42.42 rules. | PROV-DM §§5.2.1, 5.6 |
| 630 · N4242-ALGORITHM | Partial. An activity can have start/end times and a qualified association with an agent and plan. Versioned algorithms, settings with units, reported status and confidence require domain semantics. | PROV-DM §§5.1.2, 5.3.3 and PROV-O §3.3 |
| 650 · CCOM-INSTALL-HISTORY | Partial. Activity and usage can describe an installation or removal with participating entities and timing. These general terms need an equipment-domain model for functional location and the type of transition. | PROV-DM §§5.1.1–5.1.4 and §5.3.3 |
| 651 · CCOM-MODEL-HISTORY | Related. Entity specialization or a record-derivation link can distinguish successive asset descriptions. The date of a record revision does not establish when the asset was assigned its product model. | PROV-DM §§5.2.2, 5.5.1 |
| 652 · CCOM-WORK-EXECUTION | Partial. A plan and performed activity are distinct, and an informing activity can be linked to the informed one. A maintenance order's request and completion states and specific cause/effect links need equipment-domain terms. | PROV-DM §§5.1.2, 5.1.5, 5.3.3 |
| 653 · CCOM-EVENT-EVIDENCE | Partial. A diagnostic activity can use measurements and generate a proposal entity. Derivation can record the source of that proposal. Whether a measurement supports a hypothesis, and with what likelihood, requires the event or evidence model. | PROV-DM §§5.1.3–5.1.4, 5.2.1 |

## Candidate distinctions to test

- Qualified derivation can describe the particular generating activity and usage/generation records associated with an output-to-input link. First test against 221, 629 and 630 to determine whether a dedicated row adds a distinct information need.
- Qualified association can record the role and plan within one activity-agent relationship. Test whether the existing procedure, participation and responsibility rows capture that detail.
- A provenance bundle is itself an entity whose provenance can be described. Compare with 220 and 230 before deciding whether provenance about an assertion set adds a distinct information need.
- Check the draft SOSA-PROV property chain in its documented direction. A qualified execution association with a procedure can imply usedProcedure. A usedProcedure statement alone does not supply a particular association or identify its responsible agent.

This checkpoint covers 12 original row IDs. Complete the remaining row dispositions, check candidate overlaps against the existing donors and integrate the verified set into the canonical workbook and mirrors.
