# SOSA G2-7T — original C239 Appendix A glossary and normative Appendix B pointer audit

**11 November 2026. Original The Open Group SOSA C239 Edition1.1 (2023), Appendix A PDF384–389 and Appendix B PDF390–391; PDF392 Appendix C only restricted location pointer. STOP before native G3 file access.** The [typed source ledger](SOSA_G2_7T_Original_Source_Item_Coverage_11NOV2026.json) audits **77 distinct glossary definition rows, eight Appendix B filenames pointing to original normative files, nine source appendix headings and 12 source-semantic caveats**. No new numbered Rules occur in these appendices. The Appendix A terminology statement characterizes AV-2 as source of SOSA enterprise definitions but does not authorize generic DIM classes/fields.

**Core original meanings:** System/subsystem relation is context-dependent; Sensor is a device or system estimating external properties from one or more sensing elements; Module is a functional architectural role that can use hardware and/or software; Pod can contain elements from more than one sensor. Platform means one of device, host vehicle or computing infrastructure and requires contextual qualification. Health (status, faults, warnings), Status (performance/health), State (lifecycle), Mode (finite discrete behavior), Configuration (setup), Capability (tasks possible given health/configuration) are distinct. Task originates externally; Assignment internally. Raw/minimally processed Data Products differ from processed/reduced Information Products. Detection, Audit Event, Notification, Heartbeat, Relay Event, Collector Module and Logging should not be silently merged. Conformance is complete adherence, whereas Compliance is graded adherence; no implementation conformance is established here.

## All 77 original glossary terms and locators

| Native term | PDF | Source-native meaning (concise paraphrase) |
|---|---:|---|
| Analysis | 384 | Engineering or mathematical verification using accepted methods |
| Architecture | 384 | System organization embodied by components, relations and guiding principles |
| Assignment | 384 | Mission-related request originated within sensor system to module |
| Audit Event | 384 | Event produced by module that may be logged |
| Behavior | 384 | Responses and output interactions under stimuli |
| Capability | 384 | Tasks and assignments possible given current health/configuration |
| Closed Interface | 384 | Privately controlled or vendor-unique nondisclosed interface |
| Cohesion | 384 | How hardware/software support the same abstraction |
| Collector Module | 384 | Module receives audit events for analysis or storage |
| Compatibility | 384 | Ability to coexist or integrate without impairment |
| Compliance | 384 | Degree of adherence to standard or architecture |
| Configuration | 384 | How sensor system or module is set up |
| Conformance | 385 | Complete adherence to standard or architecture, 100-percent compliance limit |
| Coupling | 385 | Strength of logical interconnection and effect of changes |
| Cross-Sensor Cueing | 385 | Using one sensor's data to direct another's target search |
| Data Model | 385 | Format, structure and relationships documented as DIV-1, DIV-2 and DIV-3 |
| Data Products | 385 | Raw or minimally processed reusable digital sensor output |
| Data Rights | 385 | License rights to technical data and software IP |
| Demonstration | 385 | Qualitative exhibition of function, generally without measurements |
| Deprecation | 385 | Legacy profile equipment submitted after profile removed |
| Detection | 385 | Observation distinguished from ambient background |
| Element | 385 | Hardware, software or logical constituent of System or Subsystem |
| Hardware Element | 385 | Any hardware incorporated in a SOSA sensor |
| Health | 385 | Status, faults and warnings about module or sensor condition |
| Heartbeat | 385 | Periodic normal/abnormal operation signal between modules |
| Information Products | 385 | Processed/reduced reusable mission or exploitation digital output |
| Inspection | 385 | Examining device or controlled design drawing to check compliance |
| Interaction | 386 | Exchange of data/signal and behavioral response between modules/elements |
| Interface | 386 | Region of interaction between systems or elements |
| Interoperability | 386 | Effective exchange and use of information among elements |
| Legacy | 386 | Items intended for removal in later version |
| Logging | 386 | Persistent capture of sensor health, status, mode, state for retrieval |
| Metadata | 386 | Context of data such as position, orientation, timing, area of regard |
| Mode | 386 | Finite discrete condition with known expected behavior |
| Model | 386 | Representation of System, element or interface by drawing/text/notation |
| Modular Open Systems Approach (MOSA) | 386 | DoD modular open systems architecture principles and verification |
| Modularity | 386 | Distinct loosely coupled physical/functional elements with interfaces |
| Module | 386 | Architectural functional entity implemented in hardware and/or software |
| Notification | 386 | Interaction reporting occurrence of event |
| Open Architecture | 386 | Stakeholder-governed architecture with verification |
| Open Business Model | 386 | Transparent collaboration and reusable asset innovation |
| Open Interface | 387 | Interface conforming to open architecture or standard |
| Open Source | 387 | Software whose source may be used, copied, modified or distributed |
| Open Standard | 387 | Published consensus-governed and maintained standard |
| Open Systems Architecture | 387 | Accessible governed modules and interfaces subject to conformance checks |
| Platform | 387 | Context-dependent sensor/support device, host vehicle or computing infrastructure; qualify intended meaning |
| Plug-and-Play | 387 | Use newly introduced component without manual configuration |
| Plug-In Card | 387 | Circuit card mating with backplane; SOSA PIC conforms to slot profile |
| Pod | 387 | Integral sensor part with elements from one or more SOSA sensors mounted on/in it |
| Portable | 387 | Reuse a hardware/software item in different environment |
| Published Architecture (or Standard) | 387 | Interfaces and interchange protocols known/available to intended users |
| Publish-Subscribe | 387 | Publishers share data with zero or more subscribers |
| Quality of Service | 387 | Producer-consumer shared characterization of data flow behavior |
| Real-time | 387 | Meets specified time-critical or deterministic constraints |
| Reconfigure | 387 | Reversibly alter hardware/software/system for mission need |
| Relay Event | 388 | Audit-event filter forwarding to relay/collector or dropping by policy |
| Request-Response | 388 | Client sends request to service module, which acts and replies |
| Resilience | 388 | Continue or restore function under disruption with detectable graceful degradation |
| Reuse | 388 | Use standard hardware/software again in another system or function |
| Safety-critical | 388 | Failure may harm life, vehicle, system or mission |
| Scalable | 388 | Architecture usable with few/many elements or small/large platforms |
| Secure | 388 | Designed to resist impairment and unauthorized data access |
| Security Risk | 388 | Threat extent evaluated by likelihood and adverse impact |
| Sensor | 388 | Device or system estimating external entity properties with one or more host-mounted sensor elements, producing quantitative data |
| Sensor Management | 388 | Tasks accomplished via System Manager and Task Manager module functions/interfaces |
| Software Applications | 388 | Executables intended for users to accomplish tasks |
| Software Component | 388 | Software unit incorporated in SOSA sensor |
| Standardized Interfaces | 388 | Physical/electrical/logical interfaces codified in SOSA products |
| State | 388 | Top-level operational lifecycle condition of System or module |
| Status | 389 | Condition concerning performance or health |
| Subsystem | 389 | See System, context-relative hierarchical notion |
| SYSLOG | 389 | Event-logging standard IETF RFC5424 |
| System | 389 | Collection of elements constituting useful capability; may be subsystem in another context |
| Target | 389 | Entity of interest possibly resulting from detection |
| Task | 389 | Mission-related request originating outside sensor System |
| Test | 389 | Controlled quantitative verification with instrumented results and analysis |
| Verification | 389 | Measuring or assessing conformity to requirements |

## Eight native files referenced by normative Appendix B

| Original section | Filename as printed | Stated interface or model | File actually inspected? |
|---|---|---|---|
| B.1 | SOSA_TechStd_v1_DSDM | DIV-1/DIV-2/DIV-3 native data model | **No; original unread** |
| B.1 | SOSA_TechStd_v1_DSDM_IDL | Original data-model Interface Definition Language | **No; original unread** |
| B.2 | System Manager-SysMan-API.json | System Manager in-band system management API | **No; original unread** |
| B.3 | Module-SysMan-API.json | Generic Module in-band system management API | **No; original unread** |
| B.4 | Security Services-SysMan-API.json | Security Services in-band system management API | **No; original unread** |
| B.5 | Chassis Manager-SysMan-API.json | Chassis Manager in-band system management API | **No; original unread** |
| B.6 | PIC-SysMan-API.json | Plug-In Card in-band system management API | **No; original unread** |
| B.7 | PIC with SW RTE-SysMan-API.json | PIC with software RTE in-band management API | **No; original unread** |

The Appendix B heading is **Normative**, but the source consists of *pointers to original files*, not the original model, IDL or OpenAPI contents. Those eight files are a material independent G3 source-access and clause-coverage obligation. Appendix C's restricted Air Force original was not examined; only its source location pointer appears at PDF392.

## 50 source-qualified comparisons to existing master rows

| Existing approved master information row | Source-native relation | Negative-equivalence boundary |
|---|---|---|
| Described sensing System / arrangement | RELATED: Source System is elements forming useful capability and can be a Subsystem depending on context; Sensor may be device or System | No universal chassis, one hierarchy or adopted DIM superclass |
| Observer / observing System | RELATED: Sensor estimates properties of another entity and produces quantitative data | Not every installed source constituent is an observing system |
| Physical constituent | RELATED: Element can be hardware/software/logical while Hardware Element is physical hardware incorporated in sensor | No automatic individually identified System or mixing software with equipment |
| Hosting platform / station context | RELATED: Platform can mean supported sensing device, vehicle host or computing infrastructure; Pod may carry components of multiple sensors | Platform role must be qualified, no generic chassis |
| Connected external equipment | RELATED: Platform can mean vehicle host or computing infrastructure; Interface defines interaction boundary | No actual named/connected external hardware |
| Composition member exposure and source attribution | RELATED: Module is functional architectural entity realizable in hardware and/or software elements | Not automatically a discoverable child resource or observation attribution |
| Reported physical parent/child attachment relationships | RELATED: System may be nested and Pod may hold elements from several SOSA sensors | No measured installation or fixed cardinality |
| Persistent System identifier | NO_ESTABLISHED: Native System is defined by capability and contextual composition | No persistent unique System ID established by native definition |
| Declared component capability catalogue | RELATED: Capability represents tasks or assignments possible given current health/configuration | Not a reported machine-readable capabilities catalogue |
| Component capability and readiness report | RELATED: Capabilities depend on current condition, Health comprises status faults and warnings | No actual status or readiness message |
| Required and recommended capability support | RELATED: Conformance means complete adherence whereas Compliance means degree and verification checks adherence | Glossary does not impose DIM Profile SHALLs or certify equipment |
| Supported operating mode | RELATED: Mode is finite discrete condition with expected behavior for system module or equipment | No identified set of modes on source-case equipment |
| Declared default mode | NO_ESTABLISHED: Source Mode definition says discrete finite behavior | Does not define default mode |
| Source-reported operating mode | RELATED: Mode is behavioral condition separate from Status performance and health | No reported current operating mode |
| Reported component operating condition | RELATED: Health aggregates status/faults/warnings; Status is performance/health condition; State top-level lifecycle | These distinct concepts must not be collapsed into one status field |
| Component property-value report | RELATED: Status is condition, Configuration is operational setup | No specific observed property-value message |
| Four-valued evaluation state | NO_ESTABLISHED: State is top-level lifecycle condition | No native four-value ISA state enumeration |
| Requested latest occurrence of an operating-state code | NO_ESTABLISHED: Logging persistently captures lifecycle state | No latest-occurrence query or time-keyed request |
| Requested time-keyed operating-state history | RELATED: Logging stores modes and states for later retrieval | No standardized history query or timestamp key |
| Component configuration version | NO_ESTABLISHED: Configuration describes how sensor/module is set up | No revision field or current version identified |
| Requested current component configuration message | NO_ESTABLISHED: Glossary defines operational setup | No network-accessible query/request API |
| Declared command interface | RELATED: Task comes from outside sensor; Assignment is internal; management and request-response support functions | No approved CSAPI Command endpoint/schema |
| Issued control request | RELATED: Origin distinguishes external Task from internal Assignment | No actual issued request or tasking authorization |
| Command acknowledgement / reported outcome | RELATED: Service acts on client request then responds | No async acknowledgement or current execution evidence |
| Declared command parameter | NO_ESTABLISHED: Source describes request-response interaction pattern | No typed command parameters or source schema |
| Declared command result | RELATED: Source describes response message after service acts | No accepted common result schema |
| Service role and required command support | RELATED: Sensor Management functions implemented by System Manager and Task Manager modules/interfaces | No universal common CSAPI command role or service set |
| Reported output field | RELATED: Raw/minimal Data Products differ from processed/reduced Information Products | Neither guarantees digital ObservedProperty or named output field |
| Observed / observable property | RELATED: Sensor estimates properties of external entities and generates quantitative data | No exact OGC ObservedProperty identity or vocabulary |
| Performed Observation | RELATED: Sensor estimates properties and Detection is observation distinguished from background | No current observed event or time-stamped result |
| Reported value and associated uncertainty | NO_ESTABLISHED: Native Sensor produces quantitative data | No uncertainty quantity/unit in this definition |
| Original event and derived digital representation (proposed DIM) | RELATED: Detection and raw/processed outputs reflect different native phenomena and processing stages | No owner approval to merge event with derived representation |
| Source-qualified event identity and reference | NO_ESTABLISHED: Audit Event is module-produced loggable event while Notification reports occurrence | No event ID URI or source reference |
| Event occurrence time | NO_ESTABLISHED: Native Notification reports event at occurrence | No timestamp/clock basis in definition |
| Event creation category | RELATED: Detection and Audit Event are semantically different event types | No accepted common category enumeration |
| Reported primary event-generation method | NO_ESTABLISHED: Detection is an observation differentiated from background | No defined triggering algorithm/method |
| REVIEW HOLD — reporting path | RELATED: Notifications report events; audit events can be filtered relayed collected for storage | No live CSAPI DataStream/event endpoint |
| REVIEW HOLD — service history | RELATED: Logging is persistent, Collector receives audit events, Heartbeat periodically indicates operation | No queryable archive schema or retention guarantee |
| Message author or registration announcer | NO_ESTABLISHED: Audit Event is generated by module | No identified authenticated author or registered message source |
| Administrative network and service notification | RELATED: Event notification and periodic heartbeat are distinct mechanisms | No administrative network notification schema |
| Network participation role and responsibilities | RELATED: Interaction exchanges signal/data/behavior at interfaces among module and hardware elements | Not permanent whole-System service/provider role |
| REVIEW HOLD — time / QA | RELATED: Metadata can include timing, Heartbeat periodic, Real-time means deadlines | No UTC/clock synchronization or event-time accuracy |
| Orientation relative to attached parent | RELATED: Metadata may include orientation context | No observed parent-frame orientation |
| Position relative to attached parent | RELATED: Metadata may include position context | No measured parent-frame coordinates |
| Latest built-in-test reported result | NO_ESTABLISHED: Health concerns faults/warnings; Test is controlled quantitative verification | No built-in-test result or diagnostic report |
| Requested component diagnostic procedures | NO_ESTABLISHED: Glossary describes health and evidence of conformance | No diagnostic Command defined |
| Reported activity flag | NO_ESTABLISHED: Lifecycle State is a defined notion | No current boolean active-state flag |
| REVIEW HOLD — processing | RELATED: Native raw/minimally processed output differs from reduced/processed output | No actual processing utilization/status measurement |
| REVIEW HOLD — control execution | RELATED: External task internal assignment and service request are source-distinct | No authorized or witnessed CSAPI command execution |
| REVIEW HOLD — power / state | NO_ESTABLISHED: State and Status describe lifecycle versus performance | No current power state or electrical measurement |

Every row cites stable glossary source IDs in the original ledger, preserving prior donor and case data. No adoption of proposed DIM classes, fields, chassis or OGC API–Connected Systems Profile requirements follows.

## 30 exact source holds

- SOSA-G2-7T-Q01: Appendix A native AV-2 terms are definitions, not newly numbered mandatory requirements.
- SOSA-G2-7T-Q02: Appendix A printed glossary table ID 13.5.3.3.3-1 is unusual within Appendix A; preserve exact original citation.
- SOSA-G2-7T-Q03: Platform has device/host vehicle/computing infrastructure senses, not one unqualified class.
- SOSA-G2-7T-Q04: System and Subsystem depend on context; no universal immutable hierarchy.
- SOSA-G2-7T-Q05: Sensor estimates properties and generates quantitative data; whole-System DIM scope broader.
- SOSA-G2-7T-Q06: Module is functional architecture distinct from physical Hardware Element and software unit.
- SOSA-G2-7T-Q07: Pod may hold components of multiple sensors; not generic single-sensor chassis.
- SOSA-G2-7T-Q08: Health Status State Mode Capability and Configuration definitions remain distinct.
- SOSA-G2-7T-Q09: External Task vs internal Assignment cannot be silently merged.
- SOSA-G2-7T-Q10: Data Products raw/minimal and Information Products processed/reduced differ; not automatic OGC Observations.
- SOSA-G2-7T-Q11: Detection Audit Event Notification Heartbeat Relay Event and Logging have distinct semantics.
- SOSA-G2-7T-Q12: Conformance complete adherence versus Compliance degree, not evidence of actual product certification.
- SOSA-G2-7T-Q13: Inspection Test Demonstration Analysis and Verification are different source methods.
- SOSA-G2-7T-Q14: Glossary alone does not define current device telemetry or a network service.
- SOSA-G2-7T-Q15: Appendix B Normative DSDM reference is only filename; original DIV1/DIV2/DIV3 contents unread.
- SOSA-G2-7T-Q16: Appendix B DSDM IDL filename does not prove actual native schema was inspected.
- SOSA-G2-7T-Q17: System Manager-SysMan-API.json original interface contents unexamined.
- SOSA-G2-7T-Q18: Module-SysMan-API.json original interface contents unexamined.
- SOSA-G2-7T-Q19: Security Services-SysMan-API.json original interface contents unexamined.
- SOSA-G2-7T-Q20: Chassis Manager-SysMan-API.json original interface contents unexamined, no adopted DIM chassis.
- SOSA-G2-7T-Q21: PIC-SysMan-API.json original interface contents unexamined.
- SOSA-G2-7T-Q22: PIC with SW RTE-SysMan-API.json original interface contents unexamined.
- SOSA-G2-7T-Q23: Appendix B references attached files but does not establish retrieval/access of their actual bytes.
- SOSA-G2-7T-Q24: TechStd_v1 native filename within C239 Ed1.1 does not establish file revision or edition lineage.
- SOSA-G2-7T-Q25: Appendix C restricted Air Force overlay original unavailable; only pointer read.
- SOSA-G2-7T-Q26: AV-2 native meanings may be RELATED without adopting any mandatory DIM classes/cardinalities.
- SOSA-G2-7T-Q27: No real four empirical source-case device conformance established by glossary.
- SOSA-G2-7T-Q28: External SYSLOG RFC5424 original standard and implemented logs not inspected.
- SOSA-G2-7T-Q29: Distinct later 2025 The Open Group SOSA S251 edition original unreviewed.
- SOSA-G2-7T-Q30: No adopted common CSAPI Profile SHALL, chassis hierarchy, Command or runtime conformance.

**C239 registered heading standing remains 189/192 at least sampled/inline source-reviewed, two substantively unread, one restricted.** Original Appendix A/B registered headings already had SOURCE_READ credit from G1, so this more detailed glossary/table audit does not falsely increase the broad heading count. Eight normative original companions and later SOSA S251 remain unexamined; source completeness is bounded PARTIAL. **Required gate:** update canonical JSON, BOTH CSV, BOTH Markdown and same original editable 26-sheet Excel; independently verify actual saved cells and historical tabs. Next *distinct* owner Proceed only **G3-N1 edition/source-artifact identification and access investigation**, no native artifact clause reading yet.
