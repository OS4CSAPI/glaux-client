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

## Expanded comparison

The [row ledger](PROV_Row_Review.csv) now indexes all 620 stable identifiers and contains 40 source-located adjudications. The expansion covers activity, plan, agency, time, digital representation and input/output examples across the other donors. The pending rows have explicit review stages. The nine unresolved case rows retain their holds.

The strongest remaining candidate is a named **provenance bundle with its own attribution and generation history** (PROV-DM §5.4). Rows 220, 230 and 375 concern a claim, a source message and a package of records respectively. Review each donor's native coverage of the bundle distinction before adding a row. Qualified derivation also needs an overlap decision against rows 221, 629 and 630, specifically whether the current rows preserve the particular usage and generation events for a derivation.

## Bundle candidate decision

Retain a distinct candidate for **provenance of a named set of provenance assertions**. Its identifier denotes the assertion set. Its own attribution, generation time or lineage describes that set and can differ from the provenance of every subject described inside it. PROV-DM §5.4.2 treats a bundle as an entity and defines no bundle-specific attributes. PROV-O Examples 3–4 illustrate attribution and derivation of bundles. Candidate status does not imply a mandatory bundle, a particular serialization, a signature, or confidence in any assertion.

Compared against rows 220 (source-qualified assertion), 230 (source-message reference), 375 (exchange package), 629 (measurement lineage) and 653 (event evidence). The first two qualify a claim or message. The exchange package comes closest because it can have both identity and creator metadata. Its existing row addresses a container for digital records rather than the identity and provenance of the assertion set. Measurement lineage and event evidence describe the content of assertions, while the bundle identifies who assembled or published a particular view of that evidence.

The table records the cross-check of existing crosswalk evidence. A hold means that evidence did not support a decision on donor coverage. This is a comparison of existing evidence, with original-source confirmation for PROV itself.

| Donor | Nearest evidence and finding |
|---|---|
| IEEE 1451 | Hold. Existing comparisons at rows 220, 230 and 375 do not settle coverage of named provenance assertion sets. |
| OPC UA Devices | Related, rows 220 and 375. Declaration source and deployment packages have different subjects. |
| OPC UA PA-DIM | Hold. Rows 220, 230 and 375 record no established correspondence for the closest topics. |
| Asset Administration Shell | Partial, rows 220 and 375. Package identity, metadata and associations support provenance of an identifiable container. Coverage of a named set of provenance descriptions remains unsettled. |
| SAPIENT | Related, rows 220 and 230. Report assertions and mediated messages are distinct from a set of provenance statements with its own history. |
| Integrated Sensor Architecture | Related, row 230. A source message can retain originator, time, type and identifier. Its references are not an assertion set with independent provenance. |
| The Open Group SOSA | Related with source hold, rows 220 and 230. Vendor and audit-event context are relevant. The bounded audit evidence does not settle assertion-set provenance. |
| SAREF Core | Related, row 629. Inputs and outputs relate to an execution, which can be described by statements inside a bundle. |
| W3C Web of Things | Related, row 653. Exposure of an event and its payload does not establish independent provenance for a set of statements. |
| OSUS-R | Related, rows 220 and 230. Record identity and links relate individual observations. |
| Redfish | Related, rows 220 and 230. Resource origins qualify events and metrics. The reviewed mappings concern individual records or properties. |
| RFC 8348 | Related, row 220. Module revision identifies vocabulary provenance. |
| ANSI N42.42 | Related, rows 220, 375 and 629. Document identity, producing organization and raw-input references are close building blocks. The crosswalk evidence ties them to instrument data and analyses. |
| I-ADOPT | Scope distinction, rows 375 and 629. A VariableSet groups descriptions of variables, a different subject from provenance assertions about executions and results. |
| MIMOSA CCOM | Related, rows 220, 230, 375 and 653. Document identity, source context and evidence relationships describe distinct entities or records. The existing evidence does not establish metadata scoped to provenance assertions as a set. |
| W3C SOSA/SSN | Related, rows 629 and 653. The 2017 and 2026 alignment sections address observation and execution relationships. Credit for the bundle construct rests on PROV-DM §5.4. |
| Observations, Measurements and Samples | Related, rows 629 and 653. Observation collections and references concern observations, their results or interpretations. |
| SWE Common | Hold. Existing matches on record content and structures do not establish the bundle distinction. |
| SensorML | Related, row 629. A process description and its input connections can provide material for provenance assertions. |
| OGC API – Connected Systems | Related, row 629. Observation collections can group records. The scoped comparison does not establish a group of provenance assertions with separate attribution. |

Proposed optional row wording: **Named provenance assertion set and its own origin**. Preserve the identity, attribution and generation history of a named set of provenance assertions independently of the entities that set describes. Publish it with the finished provenance column, retaining unresolved donor comparisons as holds.

## 24 November assessment pass

The [assessments awaiting integration](PROV_Row_Assessments_Pending_Integration.csv) record 165 additional decisions by stable row ID. Related rows share a source-based rationale where they ask for the same kind of information. This pass distinguishes domain fields from the history of the entities that carry those fields. It also identifies partial correspondence for processing and substitution, verification, and timed equipment activities.

The working total is 205 assessed rows, nine existing case holds and 406 rows awaiting assessment. The published workbook still reflects the earlier 40 assessments. Integrate the saved decisions together with the remaining assessments and the proposed bundle candidate.
