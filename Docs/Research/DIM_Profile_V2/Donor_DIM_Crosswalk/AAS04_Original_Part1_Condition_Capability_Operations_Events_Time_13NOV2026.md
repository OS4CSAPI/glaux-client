# AAS04 — Original Part 1 condition, capability, operations/events and time

13 November 2026 · Research branch `research/dim-profile-v2` · Preflight `9c2ee4a4417549add4b41b22e84fb93fcf07a84b`

**AAS04 is complete at the stated source scope; Asset Administration Shell (AAS) remains active and incomplete.** One owner “Proceed” authorized this step after AAS03. The [existing donor plan](PLAN_AAS_v3_2_Source_First_Donor_Review_13NOV2026.md) and [cumulative original-source ledger](AAS01_Original_Source_Corpus_Coverage_13NOV2026.json) govern the work. No Domain Information Model (DIM) classes, cardinalities, hierarchy, OGC API–Connected Systems (CSAPI) Profile requirements or runtime conformance were adopted.

## What this changes in our understanding

A capability describes what an asset has the potential to achieve. AAS can link that capability to a skill implemented through an operation, property or larger information structure, but the capability itself does not say whether equipment is ready now. An Operation describes its arguments and results; it does not establish that a request was issued, accepted or completed. The source deliberately points to Part 2 for invocation contracts, which remain outside this step (AAS04-N001–N004).

The event machinery has a different purpose from an equipment health report. BasicEventElement.state means that the event is on or off, while observed identifies a modeled object whose information is being monitored. The event discussion includes condition monitoring, execution monitoring and alarms as motivating uses; it does not define a common equipment-health vocabulary or all the required payloads. The entire event concept remains Experimental, with future backward compatibility explicitly uncertain (AAS04-N005–N017).

Time must retain its specific meaning. An event trigger time, its last send/receive time, and the creation/update time of the information record answer different questions. Administrative dates are business milestones and need not change with every transient status value, so they cannot establish live sensor freshness. The distinction also prevents a new digital representation from silently replacing the original time and provenance of the Bennett source observations (AAS04-N009, N013, N019–N024).

The original source has inconsistencies that a mapping must expose. Administration prose says version/revision are stored as integers, while the datatype tables and selected JSON definition specify digit strings. DateTimeUtc includes a nonzero-offset example even though the selected schema accepts zero-offset suffixes, and the local UML partial uses timeStamp where the native table uses timestamp. These are held source questions for AAS05, not permission to invent a corrected encoding (AAS04-N023, N024, N028).

Vendor-specific information can be retained through proprietary extensions and submodels. The source explicitly says proprietary extensions do not provide global interoperability; a name and value do not establish common meaning or an accepted standard extension. Value qualifiers can distinguish measured from substitute values, while static qualifiers can describe as-planned or as-maintained context. These mechanisms support careful preservation of differences without approving a universal condition, capability or extension model (AAS04-N018, N025–N027, N029).

## Four time meanings kept separate

| Native information | What it means | Comparison boundary |
| --- | --- | --- |
| EventPayload.timestamp | When the experimental event was triggered | Not automatically physical phenomenon, observation result or transmission time |
| BasicEventElement.lastUpdate | Last event received for input, or sent for output | Not a timestamp on every exchange and not general object modification time |
| AdministrativeInformation.createdAt | Initial creation of the identified information object | Not manufacture, installation or acquisition time |
| AdministrativeInformation.updatedAt | Relevant business modification of the information object | Not required to advance for every real-time value fluctuation |

The optional event intervals are similarly scoped. minInterval concerns maximum input-handling or output-sending frequency; maxInterval concerns output event-status update spacing and is inapplicable to input. Neither is automatically an equipment sampling period, a whole-component Status heartbeat or a command to change a rate. Their experimental standing and directional meaning remain in the master (AAS04-N010–N011).

## Exact inspected source coverage

The original source is Industrial Digital Twin Association (IDTA), *Specification of the Asset Administration Shell, Part 1: Metamodel*, version 3.2.0, Release 26-01, pinned at [`ecd191273a28dd9c4e7bb75e923f0f0fe5da444e`](https://github.com/admin-shell-io/aas-specs-metamodel/tree/ecd191273a28dd9c4e7bb75e923f0f0fe5da444e). Every finding has publisher, edition, standing, original path, exact lines, Git blob and pinned URL in the cumulative ledger. Counts overlap and are not percentages of whole-donor coverage or counts of adopted DIM fields. The original AAS01 census and historical AAS02/AAS03 records retain their grades.

| Material | Actual AAS04 contact | Limit |
| --- | --- | --- |
| Included event discussion | All 153 lines, including its four use-case examples and direction/type/scope discussions | Informative context under the annex; not complete transport or domain payload contracts |
| BasicEventElement, Direction, StateOfEvent, EventPayload, Capability, EventElement, Operation and OperationVariable | Selected sections fully reread for meaning; 20 AAS03 attribute IDs reused | AAS03 had already read the complete structural page; rereads are not 20 newly discovered fields |
| Administrative information and extensions | Full selected sections, 11 additional native attribute entries | Six administration attributes, one HasExtensions relation and four Extension attributes |
| Qualifiers, datatype entries, terms and proprietary/template guidance | Exact selected ranges in the ledger | Other sections, external dictionaries and industrial template specifications retain their earlier grades |
| Native constraints | Nine individually anchored rules, with original AASd identifiers | Native rules are not runtime enforcement or adopted Profile requirements |
| JSON schema | One complete named AdministrativeInformation definition reread for the observed conflicts | No broad AAS05 schema pass; no new XML/RDF/OpenAPI, inherited-definition or exhaustive regex audit |
| Diagrams and illustrations | Eight pinned class partials, two wrapper source files and three original event JPEGs inspected | Mutable working-branch includes not followed; publisher-rendered UML equality remains unverified |
| Findings | 29 native meaning records | These overlap attribute/rule/source-section records; do not add them into a fabricated unique-clause denominator |

OperationVariable.default and optional/mandatory cardinality are future-extension examples in the source, not current fields. AASd-134 requires variable-value idShort uniqueness across all three direction lists, and AASd-138 supplies the singleton-list rule for templates/operation variables. AASd-005 makes revision conditional on version, and AASd-077 scopes extension-name uniqueness to its owner. Qualifier consistency and template/instance rules retain their exact exceptions and experimental attribute standing.

## Progressive master integration

**22 existing-row AAS cells changed: 21 newly populated and one extended, bringing the total to 44.** The same 337 information rows and 354×16 layout remain, with AAS in G and the proposed DIM in P. Existing AAS02 text and source IDs remain in the extended configuration-version comparison. All other donor, case and DIM cells are unchanged; AAS source classifications remain unassigned.

| Existing row | Relation | Source-qualified addition |
| --- | --- | --- |
| `ISA-K-CAPABILITIES` — Declared component capability catalogue | RELATED | Capability describes potential independently of implementation. Semantically linked skills may use operations or properties; this is not the ISA supported-property/command/observable/type catalogue or evidence of readiness. |
| `ISA-K-COMMAND-DECL` — Declared command interface | PARTIAL | Operation describes input, output and inoutput variables. It supports an interface comparison, while invocation, errors and execution contracts remain Part 2 work. |
| `ISA-K-PARAMETER-DECL` — Declared command parameter | PARTIAL | Input/inoutput OperationVariables describe arguments through SubmodelElements. Their required value wrapper is not required-argument semantics; default/optional cardinality fields are future examples, not implemented declarations. |
| `ISA-K-RESULT-DECL` — Declared command result | PARTIAL | Output/inoutput OperationVariables describe result values. This does not establish ISA result optionality/range rules or a particular completed response. |
| `S06-R019` — Issued control request | RELATED | Part 1 declares an Operation and points to Part 2 invocation. A declaration is not an issued request; request identity, authorization and execution remain unreviewed here. |
| `S06-R020` — Command acknowledgement / reported outcome | NO_ESTABLISHED | The inspected Operation definition and experimental execution-event motivation do not establish acknowledgement, completion or physical effect. Part 2 response contracts remain unreviewed. |
| `ISA-R-EXECUTION` — Current command execution record | RELATED | The experimental event use-case table mentions monitoring long-running operations. It does not define the ISA execution-record fields or prove that an operation ran. |
| `ISA-K-CAPABILITY-STATE` — Capability readiness and reporting selection | NO_ESTABLISHED | Capability describes potential; BasicEventElement.state means event on/off. Neither establishes ISA command/property/observable readiness and separate reporting selection. Domain/API semantics remain open. |
| `ISA-C-082` — Reported component operating condition | RELATED | A semantically defined Property and qualifiers can carry a condition assertion. Experimental event state on/off is not equipment operating condition; no common health vocabulary or actual reading is established. |
| `ISA-T-EVENT-ID` — Source-qualified event identity and reference | PARTIAL | Experimental EventPayload identifies its source EventElement, scope and trigger time. These references do not supply a dedicated occurrence ID or the ISA creator/id/time event-reference contract. |
| `ISA-T-EVENT-TIME` — Event occurrence time | RELATED | Experimental EventPayload.timestamp is UTC event-trigger time. It must not automatically replace physical occurrence, observation phenomenon or result time. |
| `ISA-T-EVENT-REASON` — Event creation category | RELATED | Experimental event types use semantic meaning and specialized/custom payloads. The event use-case table is not an ISA Event Type enumeration. |
| `ISA-T-EVENT-CONTEXT` — Detector property context at event occurrence | RELATED | Experimental EventPayload identifies a logical scope and can carry custom bytes. This is not a defined detector-property snapshot or delta from the last Status. |
| `ISA-T-SENT-TIME` — Exchange transmission time | PARTIAL | Experimental BasicEventElement.lastUpdate is the last sent event time for output, but last received time for input. It is not a per-exchange Header.time; trigger time is separate. |
| `ISA-A-TIME-BASIS` — Component time basis and synchronization | RELATED | Native event and administrative dates use DateTimeUtc. This does not specify clock synchronization or the ISA epoch contract; the nonzero-offset example conflicts with the selected zero-offset schema pattern. |
| `ISA-C-048` — Component configuration version | RELATED | Version/revision and creation/update dates mark business changes to the information element, not every live value change. Prose integer storage conflicts with datatype/schema digit strings; preserve that source issue. |
| `ISA-A-EXTENSION-STANDING` — Extension standing and standardization context | RELATED | Proprietary Extension and free submodels preserve vendor-specific information. Unique local extension names and typed values do not establish global interoperability or ISA nomination/acceptance standing. |
| `ISA-C-078` — Maximum interval between component Status reports | RELATED | Experimental maxInterval describes output-event status-update spacing; it is inapplicable to input. It is not automatically the component Status heartbeat or a command to change it. |
| `ISA-C-079` — Minimum interval between component Status reports | RELATED | Experimental minInterval constrains maximum input-handling or output-sending frequency. It is not automatically the minimum component Status interval or sensor sample period. |
| `S06-R022` — Original event and derived digital representation (proposed DIM) | NO_ESTABLISHED | Experimental EventPayload.source identifies an EventElement and observableReference its scope. These do not establish physical-event-to-derived-copy lineage or authenticate the Bennett experimental copies. |
| `S06-R015` — Performed Observation | NO_ESTABLISHED | An experimental AAS event message and its trigger timestamp do not prove a performed observation, physical phenomenon time or measured result. A domain-specific payload and source evidence are still required. |
| `S06-R021` — Source-qualified assertion (proposed DIM) | RELATED | Administrative creator and experimental event subjectId identify record-maker or initiator roles. They are not authenticated evidence provenance or the proposed issuer/edition/locator/standing record. |

These negative comparisons are bounded: NO_ESTABLISHED means the inspected native construct does not establish the proposed equivalence. It does not mean the entire AAS family lacks any solution, particularly where Part 2 or a domain template remains unreviewed. Empty cells elsewhere still mean unreviewed rather than absent. No native AAS label was converted into a new master row or adopted DIM class.

## Existing case checks

The four established source cases were reused as tests of meaning, without new measurements, native AAS instances or fresh vendor-source inspection. Dragino and AirGradient supported/default network information remains distinct from current mode and readiness. Campbell's documented logger Status example does not authenticate an installed CR1000X/ClimaVue pairing or prove current freshness. Bennett's existing original NOAA means and project-derived representations retain their times and provenance; event-element references or administrative timestamps cannot establish their physical-event/copy lineage. The case cells and original evidence records remain unchanged.

## Same workbook and verification

The same editable [master workbook](Master_Donor_Concept_to_DIM_Crosswalk.xlsx), canonical JSON, both CSV mirrors and both GitHub-readable comparisons were refreshed together. Reopening the saved file verified all 5,664 comparison values and the original 26-sheet order. All previous cell styles, source classification colors, 67 mixed holds and 21 unrelated historical sheet XMLs are preserved; only affected Master Crosswalk and DIM Register rows received the height needed to display their AAS text. The existing Summary, Validation, Legend and AAS evidence column in DIM Register were refreshed, including a stale pre-M01 notice.

Frozen M00 and M01 are unchanged, and no M02 was created. The existing two workbook-check entry points share the same read-only AAS preservation verifier instead of adding another script or workflow. The cumulative ledger records the saved hash, preserved-sheet checks and visual review. The repository-wide document check retains seven pre-existing register/path issues; these are separate from the source-specific workbook checks and are not represented as passing.

## Holds and stop boundary

- **AAS04-H01 — experimental events:** BasicEventElement/EventPayload and related event concepts remain Experimental; future compatibility is not ensured. No stable common-event or runtime claim.
- **AAS04-H02 — source inconsistencies:** Integer-storage prose versus digit-string datatype/JSON; DateTimeUtc nonzero-offset example versus UTC wording/selected schema; UML timeStamp versus native timestamp. Preserve all three for bounded AAS05 corroboration; no invented correction.
- **AAS04-H03 — operation and update contracts:** Part 2 invocation/results, errors, asynchronous lifecycle, cancellation and update behavior remain unreviewed. AAS03 empty-versus-omitted representation conflict remains open.
- **AAS04-H04 — domain semantics and dependencies:** Capability paper/ontologies, IEC/DIN qualifier dictionaries, industrial templates and NIST ABAC originals were referenced but not audited. No universal readiness, operating-state, alarm or observation payload semantics established.
- **AAS04-H05 — proprietary specialization:** Extension/free submodel mechanisms preserve vendor information but do not establish global interoperability or owner adoption. AAS individual classification colors remain unassigned.
- **AAS04-H06 — source coverage and operational evidence:** Only stated text, one targeted schema definition and specified figure sources reviewed. Full schema/companion/API review and runtime evidence remain separate; prior ISA/SOSA/SAPIENT and unresolved AAS holds persist.

AAS03-H06 is partially addressed for Part 1 operation/capability/event meanings, while its API and remaining schema limits stay open. Earlier semantic-wording, missing AASd-090, diagram-provenance, companion and empty/omitted-update holds remain recorded. ISA, The Open Group SOSA and SAPIENT source limitations and owner dispositions are unchanged. No donor closure or transition is authorized.

After three completed research increments since the accepted post-AAS01 estimate, the arithmetic working remainder is low 7 / most likely 11 / high 18. This is planning guidance, not a quota, scope increase or fresh whole-corpus estimate. AAS05 should reuse the exact inspected definitions and focus on the pending schema evidence and recorded mismatches.

**One next fresh “Proceed” = AAS05 only:** original schema corroboration for reviewed native constructs in pinned Part 1 JSON/XML/RDF and selected Part 2 shared schema material. Record exact inspected paths, definitions, constraints and unresolved mismatches; stop before AAS06, API service review, another donor, DIM/Profile adoption, client changes or deployment.

## References

Industrial Digital Twin Association. 2026. *Specification of the Asset Administration Shell. Part 1: Metamodel*. Version 3.2.0, Release 26-01. July. [Publisher edition](https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/index.html). Original source is licensed CC BY 4.0; the cumulative ledger contains the exact immutable source URLs and section/attribute locators.

The referenced 2020 capabilities paper, IEC/DIN qualifier material, IDTA template-writing guideline and NIST ABAC publication are dependency leads only. Their bibliographic entries were inspected, but their original contents were not audited or used as independently verified authority in this step.
