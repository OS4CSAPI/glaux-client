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
