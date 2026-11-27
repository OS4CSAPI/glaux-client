# Lightweight Machine to Machine comparison checkpoint

The [review plan](PLAN_LWM2M_Source_First_Donor_Review.md) pins the 621-row baseline and original sources. The following registry XML definitions were inspected at the pinned revision. LwM2M applicability as declared in the XML is distinct from the object version.

| Object ID | Definition | LwM2M version | Object version | Instances |
|---|---|---|---|---|
| 1 | Server | 1.2 | 1.2 | Multiple |
| 2 | Access Control | 1.0 | 1.1 | Multiple |
| 3 | Device | 1.1 | 1.3 | Single |
| 4 | Connectivity Monitoring | 1.1 | 1.3 | Single |
| 5 | Firmware Update | 1.1 | 1.2 | Single |

| Existing worksheet row | Finding |
|---|---|
| 4 | Direct. Device resource 0 represents Manufacturer. |
| 5 | Direct. Device resource 1 represents Model Number. |
| 6 | Direct. Device resource 2 represents Serial Number. |
| 260 | Partial. Device resource 3 describes firmware version. Broader software inventory needs additional evidence. |
| 306 | Direct for the address field. Connectivity Monitoring resource 4 exposes IP Addresses. The field alone does not establish a separate interface identity for each address. |
| 505 | Partial. Access Control resources 0–3 tie permissions and ownership to a target object and instance and distinguish servers. This is not a general current-user permission model. |
| 475 | Partial. Firmware Update resources 2, 3 and 5 distinguish the update operation, state and result. Proof that the new image is active depends on observed reporting and device-specific evidence. |
| 495 | Related. Firmware Update resource 12 represents the update state-change time, a narrower subject than a general device parameter change. |

## Candidate to test

The Core Discover operation returns resource links and applicable attributes scoped to the requesting server. It does not return the resource value as a Read does. Test whether the master already captures the distinction between a declared resource in the object definition, an instantiated path returned in discovery, and a value readable by the requesting server. Compare against rows 505 and 529 and the existing device and Thing affordance findings before adding any row.

Eight initial dispositions are recorded. Additional dispositions and the first candidate comparison follow below.

## Management operations and reporting

| Worksheet row | Finding | Source |
|---|---|---|
| 81 | Partial. Execute arguments can carry operation-specific inputs. An executable resource does not establish a general reusable parameter schema. | Core §6.3, Execute |
| 88 | Partial. Object definitions declare resource operations. Access control and the runtime operation determine whether a particular server can write. | Core §§6.3, 8.2 |
| 89 | Partial. Greater Than and Less Than thresholds can control notifications. They are notification attributes, with applicability rules for the target resource. | Core §§6.3.4, 7.3 |
| 90 | Related. Step is a threshold for change in the resource value. It does not establish a percentage change or a relative reference basis. | Core §7.3 |
| 91 | Partial. Notification attributes express periods and qualifying value changes. An actual notification also depends on an observation and its runtime conditions. | Core §§6.4, 7.3 |
| 95 | Partial. Execute initiates an action on an executable resource. A management request in the master may also include domain-specific intent or parameters. | Core §6.3, Execute |
| 96 | Partial. An operation response reports its outcome at the protocol boundary. Object-specific state and result fields supply separate evidence of asynchronous work. | Core §6.3 and Firmware Update object 5, resources 3 and 5 |
| 165 | Related. Discover enumerates management resources and attributes at the targeted path. That enumeration concerns resources rather than the set of component messages. | Core §6.3.2 |
| 184 | Direct for the operation distinction. Read at a resource path requests the current value subject to applicable access and operation rules. | Core §§6.3, 8.2 |
| 187 | Partial. Observe establishes notifications for targeted data. Observe-Composite addresses multiple targets. This does not establish the semantics of arbitrary future-message subscriptions. | Core §6.4 |
| 192 | Partial. Cancel Observation ends the specified observation. The master’s general subscription row may cover other subscription types. | Core §6.4 |
| 209 | Partial. An observation targets management paths. Attributes govern notification behavior. This does not define a general query language or transferable subscription identifier. | Core §§6.4, 7.3 |
| 210 | Related. The Observe response and subsequent notifications are separate protocol events. No general initial-cache selection follows from this distinction. | Core §6.4 |
| 520 | Partial. Registration lifetime and refresh govern a server's registration of a client. Applicability to a general directory or Thing Description requires a separate mapping. | Core §6.2 |
| 574 | Related. Server object resource 6 and the observation rules qualify storing notifications while offline or disabled. They do not establish metric-report wrap or append behavior. | Server object 1 resource 6, Core §6.4 |
| 592 | Related. Server object notification storage and periodic reporting concern individual servers and observations. They do not establish the specified backup destinations or retry policy. | Server object 1 resources 2, 3 and 6, Core §§6.4, 7.3 |

## Candidate disposition against the closest rows

Recommend retaining **Declared resource, discovered instance and operation-specific access** as a provisional row. Row 165 concerns message discovery. Row 371 concerns finding a digital record and endpoint. Row 505 concerns a caller's permission. Row 529 concerns a subordinate sensor key and capture capability. A client needs all three facts about the same path: its definition declares available operations, discovery identifies what an endpoint exposes to the caller, and an attempted Read can separately establish a value or a failure. A path missing from one server's discovery does not prove that the equipment never implements it. Peer-donor comparisons remain open.

The ledger now contains 24 initial dispositions. The other 597 baseline rows, remaining peer comparisons and workbook integration are pending.

## Peer evidence for the discovery candidate

The existing crosswalk supports retaining this candidate. The closest overlap is OPC UA. Its address-space and session attributes cover much of the distinction, so represent this as a cross-donor information need rather than an LwM2M-specific feature. Here, a hold means the workbook evidence reviewed for this comparison does not settle the mapping.

| Peer | Existing evidence and disposition |
|---|---|
| OPC UA Devices | Substantial overlap. Rows 88, 371 and 505 cover general access, address-space discovery and session-level permissions. A successful read still supplies separate runtime evidence. |
| OPC UA PA-DIM | Partial. Rows 88 and 505 cover inherited access attributes and caller-specific permissions. The reviewed evidence does not settle discovery for a particular instance. |
| AAS | Partial. Rows 371 and 522 cover discovery of records or endpoints and template context. Caller-specific successful read requires additional evidence. |
| W3C Web of Things | Partial. Rows 88, 184, 371, 505 and 522 distinguish templates, descriptions and advertised read forms. An advertised operation alone does not establish permission or a successful read. |
| Redfish | Partial. Rows 88, 165, 184 and 371 distinguish schema access restrictions, instance affordances and resource retrieval. Caller-specific success remains runtime evidence. |
| ISA | Partial. Rows 88, 165 and 184 distinguish declared mutability, discovery of messages and named-property reads. Message discovery differs from discoverability of the exact resource path. |
| OSUS-R | Partial. Rows 371 and 529 distinguish directory lookup, subordinate identity and supported capture. These features do not establish a generic caller-specific read of an individual management resource. |
| RFC 8348 | Partial. Rows 88 and 184 distinguish configuration from state and permit retrieval at a hardware data path. Caller-specific discovery requires evidence from outside the hardware module. |
| SAREF Core | Related. Rows 184 and 371 cover meter-value retrieval and service exposure. Evidence for the three-way distinction remains open. |
| I-ADOPT | Scope distinction. Rows 88 and 505 concern management behavior. I-ADOPT describes variable meaning and applicability. |
| MIMOSA CCOM | Related. Rows 184, 371 and 522 cover record selection, source location and templates. These supply components of a representation without establishing the candidate as a whole. |
| W3C PROV | Related. Provenance can distinguish an operation and evidence of its result. Management discovery and read permissions require domain semantics. |
| IEEE 1451, SAPIENT, The Open Group SOSA, ANSI N42.42, W3C SOSA/SSN, Observations Measurements and Samples, SWE Common, SensorML, OGC API – Connected Systems | Evidence hold for each peer. The nearest crosswalk entries did not establish a complete same-subject discovery and caller-specific read comparison. |

Candidate wording: **Declared resource, discovered instance and caller-specific read outcome**. Preserve these three facts for an individually identified management path. Keep the read outcome explicit where a caller attempts the read. Advance this candidate with the workbook after the remaining baseline assessments.

## Device telemetry and management resources

Object and resource numbers below refer to the pinned [OMA XML registry](https://github.com/OpenMobileAlliance/lwm2m-registry/tree/a763bb5414099844fadf0797b2c8223d169d0c7e). Reassessing row 260 with Device resource 19 confirms additional coverage for a software version, while the partial disposition remains appropriate for broader inventories.

| Worksheet row | Finding |
|---|---|
| 239 | Partial. Device 3/13–15 describes current time, UTC offset and timezone. These fields do not establish time synchronization or timing accuracy. |
| 252 | Direct for the field. Device 3/18 carries a hardware version. Support for the resource depends on implementation. |
| 261 | Related. Server 1/25 advertises supported server protocol versions. This is distinct from the ISA specification version reported by a component. |
| 289 | Related. Device 3/8 reports power-source current but does not identify it as consumed AC current. |
| 293 | Related. Device 3/8 reports source current without establishing the consumed DC measurement basis. |
| 299 | Partial. Device 3/9 reports a battery-level percentage. It does not identify absolute remaining energy or define all power-source reserve measurements. |
| 301 | Partial. Device 3/6 enumerates available power sources. The native enumeration should be compared with the master’s classification before aligning individual categories. |
| 307 | Related. Connectivity Monitoring 4/0–1 identifies the current and available network bearers. Those fields do not report a generic per-interface administrative and operational state. |
| 308 | Partial. Server 1/3 supplies a default maximum notification period. That period concerns observations for the server rather than an ISA Status message as such. |
| 309 | Partial. Server 1/2 supplies a default minimum notification period. Its scope and attribute overrides differ from a component-wide Status period. |
| 311 | Partial. Connectivity Monitoring 4/2 reports radio signal strength. Its bearer-specific rules do not cover every received signal measurement. |
| 345 | Related. Device 3/11 reports device error codes. An error code does not establish the execution and outcome of the latest built-in test. |
| 445 | Partial. Connectivity Monitoring 4/11 reports signal-to-noise ratio. The resource does not establish the referenced signal bandwidth required by this row. |
| 462 | Partial. Device 3/18 and 3/19 distinguish hardware and software version. Neither establishes a single combined revision identifier. |
| 472 | Partial. Device 3/3 and Firmware Update 5/7 distinguish running firmware and the firmware package version where reported. They do not establish a fallback-image version. |
| 478 | Related. Firmware Update 5/8 and 5/9 identify supported transfer protocols and delivery methods. They do not establish image compatibility with specific equipment or software versions. |
| 499 | Partial. Device 3/10 and 3/21 describe free and total memory available for data storage in the device. Preserve the native units and scope before comparing a particular storage partition. |
| 509 | Partial. Device 3/17 can report Device Type. Identity of a managed endpoint and its device type are distinct, and the object supplies no general cross-donor type hierarchy. |
| 532 | Related. Server 1/1–3 describes registration lifetime and default notification periods. These values alone do not identify the next expected status-report deadline. |
| 608 | Related. Device 3/4 initiates a reboot and 3/11 can expose errors. These resources do not supply the last reset time and attributable cause as a pair. |

This adds 20 baseline dispositions, for 44 recorded assessments. The other 577 baseline rows and workbook integration remain pending.

## Registration, addressing and exchange behavior

| Worksheet row | Finding | Source |
|---|---|---|
| 7 | Partial. The client endpoint name identifies the registration subject. Equipment persistence and equivalence between registrations need separate evidence. | Core §§6.2, 7.1 |
| 11 | Partial. A server has a registration for the named client. Registration is scoped to that server and does not prove current reachability. | Core §6.2 |
| 13 | Related. An Object Instance is an instance of a logical management object. Its path does not identify a physical constituent merely by having a parent segment. | Core §§7.1–7.2 |
| 20 | Related. Registration advertises supported object or instance links and Discover exposes management resources. Neither operation is a general account of physical composition or source attribution. | Core §§6.2, 6.3.2, 7 |
| 21 | Partial. Register, Update and Deregister track a client’s participation per server. Network attachment and physical connectivity are separate facts. | Core §6.2 |
| 23 | Related. Object, Object Instance, Resource and Resource Instance identifiers can address a value. A management path does not in itself identify a transducer channel. | Core §7.1 |
| 24 | Partial. Resource definitions describe fields and types while Read returns current values. The protocol does not give every reported field an observation-specific meaning. | Core §§6.3, 7 |
| 76 | Partial. Registration and discovery describe supported object instances and resources within the protocol. A general catalogue of component capabilities requires another abstraction. | Core §§6.2, 6.3.2 |
| 78 | Partial. Resource definitions identify data types, operations and instance constraints. Domain-specific property semantics depend on the applicable definition. | Core §7 and pinned registry |
| 80 | Partial. Execute addresses a resource declared executable. Applicability and input semantics follow the individual object definition. | Core §§6.3, 7 |
| 85 | Partial. Core defines resource data types. Complex types in donor-specific payloads require their own definitions. | Core §7 |
| 86 | Partial. Single and multiple constraints apply to objects and resources. These do not establish arbitrary nested collection bounds. | Core §7 and pinned registry |
| 180 | Scope negative. The reviewed Core operations do not define creation of a ZIP archive of a historical query result. | Core §6 |
| 185 | Partial. Read-Composite accepts several selected paths. A donor-specific readiness rule for including properties is separate from path selection. | Core §§6.3, 7.5.6 |
| 186 | Related. Composite retrieval selects multiple paths. It does not by itself issue an archive query or create a reusable result identifier. | Core §§6.3, 7.5.6 |
| 188 | Partial. Register has server-side acceptance and protocol results. Registration acceptance is distinct from authorization for later management operations on individual object instances. | Core §§6.2, 8.2 |
| 194 | Partial. Registration inventory and the Device object expose supported resources and device information. They do not provide the master’s readiness semantics. | Core §6.2 and Device object 3 |
| 198 | Related. Management requests and responses are paired through the selected protocol binding. This is separate from a portable identifier for the command and its result. | Core §6.3 and Transport binding companion |
| 203 | Related. Composite retrieval selects paths to resource values. It does not define arbitrary selection by management message kind. | Core §§6.3, 7.5.6 |
| 204 | Scope negative. Addressing and notification conditions do not supply a generic message-matching query language. | Core §§6.3–6.4, 7.3 |
| 205 | Related. Path segments navigate object instances and resources. Other field traversal and filtering require separate evidence. | Core §§6.3, 7.1 |
| 223 | Related. Protocol binding can correlate a request and response. LwM2M address identifiers identify resources, rather than generic messages in a conversation. | Core §7.1 and Transport binding companion |
| 225 | Related. Registration lifetime limits registration validity. It does not establish general message-data expiry. | Core §6.2 |
| 231 | Partial. SenML composite responses can carry path names and typed values. A general named-value payload need not use those management paths. | Core §7.5.6 |
| 237 | Partial. Version and supported representation information are scoped to the protocol and its resources. Other message contract negotiation requires another mapping. | Core §§6.2, 7.5 |
| 464 | Related. Object instances collect resources. Composite operations can target multiple paths without creating a persistent purpose-based group. | Core §§6.3, 7 |
| 521 | Partial. A selected operation and binding can return distinct success or error results. Operation-specific representations and domain failure reasons need their own evidence. | Core §6 and Transport binding companion |
| 523 | Partial. Model identifiers provide typed address segments for object and resource levels. They do not define a generic URI template parameter model. | Core §7.1 |

This adds 28 dispositions. The total is 72 of 621 baseline rows, with 549 still pending. The workbook and peer candidate remain pending integration.

## Partial workbook integration

Column U incorporates the 72 recorded assessments and explicitly marks the other 549 baseline rows as evidence holds. The discovery candidate is now on worksheet row 664. This delivery does not close the outstanding row reviews.

## Device and location resource follow-up

Applied 43 row dispositions from Device 1.3, Connectivity Monitoring 1.3 and Location 1.0 in the pinned registry. These are bounded to the three object definitions. Individual findings and locators are recorded in the [source coverage ledger](LWM2M_Source_Coverage.json). Column U now includes 115 baseline assessments, 506 evidence holds and the provisional candidate.

## Command and exchange comparison

The [command and exchange assessments](LWM2M_Command_And_Exchange_Assessments.csv) record 93 additional baseline dispositions. The comparison distinguishes a generic operation from a resource definition that supplies the intended device behavior. These are scoped findings. Other registry objects and vendor extensions may require separate evidence. The 93 decisions are integrated in column U. The working total is 208 assessed baseline rows, with 413 still held.

## Pinned sensor-object assessment

The following findings use object version 1.1 of the indicated definitions in the pinned OMA registry. A named reading matches the measured quantity only within the indicated subject and unit. A generic resource or application type cannot establish who or what was measured.

| Worksheet row | Disposition and evidence |
|---|---|
| 25 | Partial. Generic Sensor 3300/5700–5701 can report a value and units. A typed object or additional semantic context is needed to identify the observable. |
| 31 | Partial. Humidity 3304/5700–5701 represents relative humidity. The measured air volume and atmospheric observation context require additional evidence. |
| 33 | Partial. Barometer 3315/5700–5701 provides barometric pressure. Confirm location and correction basis separately. |
| 34 | Partial. Temperature 3303/5700–5701 provides temperature and units. Ambient-air scope is an instance-level assertion. |
| 39 | Partial. Distance 3330/5700–5701 reports distance. It does not establish the observer and observed entity endpoints. |
| 347 | Partial. Temperature 3303/5700 represents a temperature reading. Placement inside the named device requires instance evidence. |
| 446 | Partial. Accelerometer 3313/5702–5704 reports X, Y and Z. Platform or external reference frame and subject association require additional evidence. |
| 541 | Partial. Acidity 3326/5700 supplies a pH reading. Water as the measured medium requires instance evidence. |
| 542 | Related. Concentration 3325/5700–5701 gives concentration and units. The analyte and liquid medium must be established. |
| 543 | Partial. Conductivity 3327/5700–5701 covers conductivity and units. Water as the medium requires separate evidence. |
| 547 | Related. Concentration 3325/5700–5701 does not establish chlorine species or the sample medium. |
| 548 | Related. Concentration 3325/5700–5701 does not establish a total dissolved solids measurement or its calculation method. |
| 549 | Related. Conductivity 3327 and Concentration 3325 give possible input or reporting quantities. They do not specify a salinity scale or a conversion. |
| 551 | Partial. Pressure 3323/5700–5701 provides a pressure reading. The object does not identify the water circuit or measurement location. |
| 567 | Partial. Generic Sensor 3300/5603–5604 gives the range of values the sensor can measure. Equipment operating limits and environmental derating require separate evidence. |
| 568 | Partial. Generic Sensor 3300/5601–5602 reports observed extrema. These resources alone do not associate each extreme with its own timestamp. |
| 578 | Related. Energy 3331 provides an energy reading. That reading does not establish battery health or a discharge-cycle count. |
| 604 | Partial. Barometer 3315 can report a pressure reading. Its value and units do not distinguish local-elevation pressure from a sea-level correction. |

Eighteen additional baseline dispositions are integrated into column U. The working total is 226 assessed baseline rows, with 395 remaining.

## Notification, timing and measurement exchange

| Worksheet row | Finding | Source |
|---|---|---|
| 512 | Related. A composite operation can gather separate resource values. It does not assert that those values are constituents of one quality or quantity. | Core §§6.3, 7.5.6 |
| 514 | Partial. The resource definition determines whether Execute is supported. An addressed resource supplies the instance target, while a shared definition supplies the operation kind. This is not a portable command identity. | Core §§6.3.5, 7 |
| 518 | Related. The declared operation tells a caller what operation class is available. Successful execution and safety or retry characteristics need operation-specific evidence. | Core §§6.3.5, 7 |
| 519 | Partial. Observe and Cancel Observation have separate operation contracts. These do not define a general event-subscription schema for arbitrary payloads. | Core §6.4 |
| 522 | Partial. Object definitions describe instance multiplicity and mandatory or optional resources. They do not define Thing Model substitution behavior. | Core §7 and Device object 3 |
| 524 | Related. Registration Update can notify a server of changes to its client's advertised object inventory. It does not implement a general description-directory notification. | Core §6.2 |
| 530 | Partial. Notify can deliver an observation update after an observation is established without a new Read request. A notification is not necessarily a device response to a management command. | Core §6.4 |
| 563 | Partial. A management path identifies the resource instance and a typed object identifies the kind of value. Source excerpt lineage and the identity of separate equipment being measured require additional evidence. | Core §7 and Generic Sensor 3300 |
| 566 | Related. Evaluation periods delimit when reporting criteria are evaluated. Neither evaluation periods nor notification periods establish an averaging window or complete sample coverage. | Core §7.3 |
| 569 | Partial. SenML supports an integrated sum and time values. The start of the accumulation interval still needs explicit interpretation and supporting evidence. | Core §7.5.6 and RFC 8428 §§4.3–4.4 |
| 570 | Partial. Notification attributes can specify greater-than or less-than crossings and a step. These do not define a combined dwell-time and return-hysteresis rule. | Core §7.3 |
| 575 | Related. SenML represents a time associated with a record and the encoding distinguishes numeric data. The fields do not declare clock error and value accuracy as separate quality measures. | Core §7.5.6 and RFC 8428 §4.3 |
| 576 | Partial. A SenML entry can identify the resource associated with a value. Its object definition supplies the native field meaning. A separate metric-definition identity requires additional evidence. | Core §§7.1, 7.5.6 |
| 603 | Partial. A measurement record can carry a time value. That value does not separately establish when the server created or persisted the record. | Core §7.5.6 and RFC 8428 §4.3 |
| 607 | Related. Core operations distinguish errors from resource payloads, and numeric zero is a typed value. The full disabled, omitted and null combination requires application-specific evidence. | Core §§6.3, 7.5 |
| 611 | Partial. Evaluation and reporting periods control when the client evaluates criteria or reports. A SenML time does not establish a separate server acquisition time or refresh contract. | Core §§7.3, 7.5.6 |
| 612 | Partial. The object declares its type, and representations such as SenML encode typed values. Reserved-value interpretation comes from the resource definition or associated domain contract. | Core §7 and RFC 8428 §4 |
| 616 | Partial. Registration Update can advertise changes in object instances. It supplies neither a general hardware inventory event nor a timestamp of the physical change. | Core §6.2 |

The eighteen dispositions are integrated into column U. The workbook now contains 244 assessed baseline rows and 377 evidence holds.

## Software package and operational lifecycle

These decisions use the pinned registry's Firmware Update object 5 version 1.2 and Software Management object 9 version 1.1. In object 9, installation, activation and operational state have separate resources.

| Worksheet row | Finding | Source |
|---|---|---|
| 195 | Partial. Package Settings can link to application-specific configuration, and Start and Stop control operation. A portable hosted runtime deployment descriptor requires other evidence. | Software Management 9/13, 9/19–21 |
| 401 | Partial. A package or package URI addresses an installable artifact. Software Component Link identifies components installed in scope of the package. A physical target-component association needs separate evidence. | Firmware Update 5/0–1 and Software Management 9/2–3, 9/17 |
| 405 | Partial. Package name and version identify software. Installation, activation and operation have distinct states. The addressed client gives management context. Independent host relationships need other evidence. | Software Management 9/0–1, 9/7, 9/12, 9/21 |
| 469 | Related. A Package Settings link supplies an application-defined settings object. It does not specify paired offline plan and online applied configuration representations. | Software Management 9/13 |
| 470 | Related. Package Settings supplies a link and Update Result supplies a package-level result. Neither establishes per-parameter synchronization outcomes. | Software Management 9/9, 9/13 |
| 473 | Partial. Checkpoint can link to update conditions or dependencies, and Update Supported Objects can trigger advertisement of changed objects. Additional side effects require instance evidence. | Software Management 9/5, 9/8 |
| 474 | Related. Uninstall supports preparation for an update. Package Settings supports configuration modification. These fields do not specify which settings survive or are restored. | Software Management 9/6, 9/13 |
| 476 | Related. Installation and update results distinguish reported states and outcomes. Post-update connectivity confirmation and rollback remain separate evidence questions. | Firmware Update 5/3, 5/5 and Software Management 9/7, 9/9 |
| 477 | Partial. Checkpoint can refer to a target-system dependency. Package components can be linked. A reusable updater-to-target compatibility hierarchy is not defined by these links. | Software Management 9/5, 9/17 |
| 479 | Scope negative for the two reviewed objects. Package and result fields do not define signature provenance, signing authority or approval records. | Pinned objects 5 and 9 |
| 480 | Partial. Software Component Link represents components installed in scope of a software package. This link alone does not convey target-specific installation order. | Software Management 9/17–18 |
| 506 | Scope negative for the two reviewed objects. These update resources do not define a per-update unlocking key or its lifecycle. | Pinned objects 5 and 9 |
| 590 | Partial. Maximum Defer Period bounds deferral of firmware update. A general maintenance calendar or permitted settings schedule requires separate evidence. | Firmware Update 5/13 |

The thirteen dispositions are integrated into column U. The workbook now contains 257 assessed baseline rows and 364 evidence holds.

## Calibration, metering and device-state evidence

These dispositions use the pinned OMA registry. The objects cited below are version 1.1, except Device 3 version 1.3 and Firmware Update 5 version 1.2.

| Worksheet row | Finding | Source |
|---|---|---|
| 482 | Related. Cumulative energy and battery level represent different quantities. Neither establishes estimated component lifetime consumption and remaining design life. | Energy 3331/5700, Device 3/9 |
| 486 | Related. Current Calibration reports a calibration value. A separately reported sensor timestamp does not identify calibration time and purpose. | Voltage 3316/5821, 3316/5518 |
| 487 | Related. Current Calibration does not describe a series of known calibration inputs paired with the corresponding measured outputs. | Pressure 3323/5821 |
| 488 | Related. A calibration value does not establish the technique, environmental conditions or reference instrument. | Current 3317/5821 |
| 493 | Partial. Object and Resource identifiers identify the native definition. Unit fields and the native enumerations need a separate mapping before treating them as dictionary-qualified properties. | Generic Sensor 3300/5701, 3300/5751 and Device 3/20 |
| 496 | Related. An Object Instance and Resource path identifies a management value. Physical sensing or control-point identity requires a mapping beyond the path. | Generic Sensor 3300/5700 |
| 501 | Partial. Water Meter provides cumulative pulse value and pulse ratio. These fields do not establish individual pulse width. | Water Meter 3424/4, 3424/6 |
| 510 | Related. Application Type can describe an application of a sensor and Sensor Type can qualify the type. Neither proves the original equipment design purpose. | Generic Sensor 3300/5750–5751 |
| 531 | Related. Software Activation State and Operational State distinguish software states and operational failure. These states do not establish a physical asset's activation lifecycle. | Software Management 9/12, 9/21 |
| 546 | Partial. A Temperature object supplies a reading and units. The instance must establish water as the measured medium. | Temperature 3303/5700–5701 |
| 577 | Partial. Battery Level expresses a relative level. Voltage and current describe source electrical measurements. The object does not provide all three capacities and energy quantities as separate fields. | Device 3/7–9 |
| 588 | Partial. Water Meter represents suspected and detected leaks independently. Response severity and delay need separate evidence. | Water Meter 3424/9–10 |
| 596 | Related. Measurement Quality Indicator and Level carry quality metadata. They do not explicitly encode significant digits and percent versus absolute accuracy. | Generic Sensor 3300/6042, 3300/6049 |
| 615 | Related. Firmware Update exposes its last state change time. This applies to the update state machine and does not establish a hardware initialization or insertion fallback. | Firmware Update 5/12 |

The fourteen dispositions are integrated into column U. The workbook contains 271 assessed baseline rows and 350 evidence holds.

## Observation and radiation comparison

The [assessment ledger](LWM2M_Observation_And_Radiation_Assessments.csv) records 35 additional dispositions. The sources distinguish the managed endpoint and its resource values. A separately observed target, radiation spectrum and calibration evidence need domain semantics. Findings are limited to the pinned Core and reviewed objects. The working total is 306 assessed baseline rows, with 315 requiring review. Column U reflects 271 assessments pending integration of this pass.
