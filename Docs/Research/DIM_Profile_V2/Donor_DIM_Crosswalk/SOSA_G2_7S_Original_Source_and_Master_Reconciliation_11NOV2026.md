**G2-7S SAME original Excel exit VERIFIED:** 41 source-qualified SOSA I-column cells, canonical JSON, both CSV and both readable Markdown comparisons, original 26-sheet saved Excel matching **346×15** source cells; 22 previous source-history worksheets preserved, zero lag. [Saved binary verification](SOSA_G2_7S_Workbook_Validation_11NOV2026.json) · [publisher](https://github.com/OS4CSAPI/glaux-client/actions/runs/43106976494) · [independent verification](https://github.com/OS4CSAPI/glaux-client/actions/runs/43107171060); SHA256 `89d80712b59c1018eb3c59da1eaa2a518c9d83a6a5f317faf74c60bfd8194a9a`. Original 113 typed source records, 31 precise holds, 189 at least sampled/inline heading coverage of 192, two unread and one restricted; no DIM/Profile adoption. **STOP before Appendix A; only distinct owner Proceed starts G2-7T original Appendix A/B through PDF392.**

---

# SOSA G2-7S — original Chapter15 inter-module interaction source audit

**The Open Group SOSA C239 Edition1.1 (2023), original §§15–15.7 PDF372–383, STOP before Appendix A at PDF384.** Original full inline source reviewed: **five numbered SHALL Rules, one Observation, one Permission, 12 native sections, four original tables with eight interaction types, twelve QoS policy rows, three protocol-binding stacks/five layers each, eight endpoint role rows**. [Original 113-record typed source ledger](SOSA_G2_7S_Original_Source_Item_Coverage_11NOV2026.json) preserves source IDs, semantics, normative standing and original holds. Figure-like interaction symbol artwork and external normative companions remain unreviewed.

**Native meaning:** Eight distinct interaction types map by default to analog media, SOSA Wideband Low-Latency Interconnect or SOSA Message Interconnect. QoS consists of six possible attributes (Reliability, Deadline, Durability, Liveliness, Ownership, Priority), but uniform implementation is explicitly future; X in priority [0,X] is unspecified, SHARED_EXCLUSIVE prose incomplete, source Durability spelling inconsistent. Interaction roles differ by type (sender, receiver, controller, subordinate, writer, reader, publisher, subscriber, client, server); the roles do not imply global DIM classes. Rule15.2-1 mandates FACE TSS capabilities conditionally when module software uses Transport API on Message Interconnect; Observation15.2-2 cites unrelated Rule14.2-1 and is held.

**Three native transport alternatives:** OMG DDS/RTPS v1.4+ over UDP, Protocol Buffers v3 + AMQP1.0 over TCP, Protocol Buffers v3 + ZMTP3.0 over TCP, using IPv4/IPv6; no mandatory CSAPI JSON encoding. Rule15.4-1 makes standard interaction infrastructure responsible if present, while Rule15.4-2 makes module responsible otherwise. REST, SOAP and SNMP are illustrative only, not mandatory. Publish-subscribe and general request-response implementation not fully specified, alternative-interconnect conformance TBD and §15.7 Services–Services Matrix future, not existing.

**Security:** TCP/IP when data-in-transit protection required must have configurable TLS1.2+, UDP/IP configurable DTLS1.2+. Permission15.6.1-1 allows implementing enable/disable via alternate firmware/software loads. This is not always-enabled transport security, endpoint certificate inventory, tasking authorization or an authenticated CSAPI Command. Physical discrete safety fallback remains possible.

## 41 source-qualified existing master comparisons

| Existing master label | Source match | Non-equivalence |
|---|---|---|
| Network participation role and responsibilities | RELATED: Endpoint roles depend on interaction type | Not permanent whole-System service provider class |
| Network instance and connection context | RELATED: Alternative on-wire binding stacks described | No actual network connection or CSAPI encoding |
| Network-visible participant | RELATED: Module and hardware element endpoints can act as interaction participants | Not publicly discoverable CSAPI resource identity |
| Composition member exposure and source attribution | RELATED: Multiple endpoints can exchange streams/messages | No public component members or reported observations |
| Declared component capability catalogue | RELATED: Interaction types describe design capabilities | No actual client-discoverable capability catalogue |
| Declared command interface | RELATED: Management request-response and conditional FACE Transport API are native | Not a CSAPI Command schema or endpoint |
| Declared command parameter | RELATED: Operation parameters represent inputs/outputs | No specific Command schema fields |
| Declared command result | RELATED: Responder returns parameters after operation | No actual command-result resource |
| Issued control request | RELATED: Management operations differ from low-latency signal control | No issued client command or safe execution |
| Command acknowledgement / reported outcome | RELATED: Responses exist and events can sometimes be acknowledged | Not universal command acknowledgement |
| Reported output field | RELATED: Structured data and signal samples may be transported | Not established observed-property field |
| Source-qualified event identity and reference | NO_ESTABLISHED: Event Notification defines event-triggered interaction | No unique event identifier |
| Event occurrence time | NO_ESTABLISHED: Notifications sent when event occurs | No timestamp value or time source |
| Requested named-observable Event reporting | RELATED: Event notifications include mode/fault changes | No named event subscription command |
| Requested named-property Status reporting | RELATED: Structured status data can follow publish-subscribe | No required CSAPI Status service |
| Message-matching criteria | RELATED: Topic identifies a structured message stream | No generalized ISA message filter expression |
| Subscription identity and query definition | RELATED: Publisher/subscriber roles and topics described | No subscription ID or lifecycle API |
| Current command execution record | NO_ESTABLISHED: Request-response can carry set operations | No queued/executing command record |
| Service role and required command support | RELATED: Requestor/responder role explicit for interaction | No global CSAPI service registry or commands |
| Message priority | RELATED: QoS writer priority default0 [0,X] X unspecified | Not ISA message priority |
| Message-data validity expiry | NO_ESTABLISHED: QoS deadline is expected update interval | Not expiration of a payload |
| Exchange transmission time | NO_ESTABLISHED: Deadline is contract on update interval | Not actual send timestamp |
| Message author or registration announcer | RELATED: Publisher role identifies message source | No cryptographically verified author |
| Source-message reference for provenance | NO_ESTABLISHED: Context metadata may accompany digital signals | No stable message provenance reference |
| Conversation-scoped message identifier | NO_ESTABLISHED: Intermodule operations have parameters | No conversation correlation ID |
| Negotiated message encoding and model version | RELATED: OMG DDS RTPS or Protobuf AMQP ZMTP stacks | Not an OGC JSON/SensorML encoding negotiation |
| Network-interface IP addresses | NO_ESTABLISHED: IPv4/IPv6 source network binding choices | No source-case assigned addresses |
| Network-interface up/down state | NO_ESTABLISHED: Interaction implies some transport capability | No observed live interface |
| Reported component receive data rate | NO_ESTABLISHED: High volume data stream source type | Not actual measured bandwidth |
| Reported component transmit data rate | NO_ESTABLISHED: Signal stream can carry high data rate | No current transmit throughput measurement |
| Component capability and readiness report | RELATED: Health data and fault events can be published | No actual readiness report |
| Reported component operating condition | RELATED: Fault warning state changes may generate notifications | No measured current state |
| REVIEW HOLD — reporting path | RELATED: SOSA message and wideband transports are distinguished | No observed CSAPI DataStream service |
| REVIEW HOLD — control execution | RELATED: Two distinct control interaction types | No authorized executed software/device control |
| REVIEW HOLD — processing | NO_ESTABLISHED: High-rate low-latency stream is native category | No actual source processing telemetry |
| REVIEW HOLD — time / QA | RELATED: QoS durations and liveliness lease in microseconds | Not UTC or quality assurance |
| REVIEW HOLD — service history | RELATED: Late joining reader durability and event notices described | Not ISA archive/history service |
| Component configuration version | NO_ESTABLISHED: TLS configuration may differ by software load | No current revision identifier |
| Certificate identity and trust context | RELATED: Conditional TLS/DTLS protection for intermodule traffic | No certificate identity or universal TLS |
| Request access-control metadata | NO_ESTABLISHED: Source permits conditional transport security configuration | No tasking permission policy |
| Administrative network and service notification | RELATED: Events can notify faults and modes | No standardized admin notification schema |

## 31 original source holds

- SOSA-G2-7S-Q01: §15.7 Services-Services Matrix explicitly future, no table rows exist.
- SOSA-G2-7S-Q02: Alternative nondefault interconnects have conformance TBD.
- SOSA-G2-7S-Q03: Conditional FACE Transport API Rule does not apply to every module, original FACE3.1 unread.
- SOSA-G2-7S-Q04: Observation15.2-2 cites Rule14.2-1 although it is an RTE file rule.
- SOSA-G2-7S-Q05: QoS implementation postponed, source policy taxonomy not live behavior.
- SOSA-G2-7S-Q06: Sensor-to-sensor QoS explicitly outside scope.
- SOSA-G2-7S-Q07: QoS Priority upper X undefined.
- SOSA-G2-7S-Q08: QoS Deadline and Liveliness intervals not message expiry or UTC.
- SOSA-G2-7S-Q09: Durability source prose typo PERSITENT vs table PERSISTENT.
- SOSA-G2-7S-Q10: SHARED_EXCLUSIVE ownership original description incomplete.
- SOSA-G2-7S-Q11: Three protocol bindings are alternatives only under stated conditions.
- SOSA-G2-7S-Q12: OMG DDS/RTPS Protobuf AMQP ZMTP native normative files unexamined.
- SOSA-G2-7S-Q13: FACE3.1 TSS original standard text not independently audited.
- SOSA-G2-7S-Q14: Rule15.4-1 infrastructure vs Rule15.4-2 module binding responsibility distinct.
- SOSA-G2-7S-Q15: Interaction roles depend on type; not global model classes.
- SOSA-G2-7S-Q16: Wideband signal/context/control/discrete differ from SOSA message transport.
- SOSA-G2-7S-Q17: Network virtual discrete restricted by performance/safety, physical discrete may remain.
- SOSA-G2-7S-Q18: VITA49.2 digital signal context original source unread.
- SOSA-G2-7S-Q19: Publish-subscribe implementation not fully determined by C239.
- SOSA-G2-7S-Q20: Request-response implementation not fully specified; REST/SOAP/SNMP examples not mandatory CSAPI.
- SOSA-G2-7S-Q21: Event acknowledgement possible not universally required.
- SOSA-G2-7S-Q22: Conditional TCP TLS1.2+ and UDP DTLS1.2+ enable-disable do not mandate universal always-on encryption.
- SOSA-G2-7S-Q23: TLS DTLS native cryptographic standards and actual deployment not examined.
- SOSA-G2-7S-Q24: Permission for alternate software/firmware load does not mandate live TLS setting.
- SOSA-G2-7S-Q25: Confidentiality integrity authenticity descriptions do not yield CSAPI certificate/authorization schema.
- SOSA-G2-7S-Q26: Endpoint-role diagram symbols not fully visually verified.
- SOSA-G2-7S-Q27: No empirical source-case protocol QoS TLS or message delivery test.
- SOSA-G2-7S-Q28: Eight original native C239 files, later S251, restricted Appendix C held.
- SOSA-G2-7S-Q29: External FACE MORA VICTORY OMG and other protocols still unread.
- SOSA-G2-7S-Q30: Future Services Matrix and unresolved source omissions prevent donor closure.
- SOSA-G2-7S-Q31: No adopted DIM classes Profile SHALLs or independent system conformance.

**Heading coverage:** 189 of192 at least sampled/inline reviewed, two unread, one restricted. §15.7 was source-reviewed as future placeholder only; actual matrix has no content to audit. Source-native protocol companions, figure symbols and distinct 2025 edition remain incomplete. No model/Profile adoption. **Mandatory publication:** same canonical JSON/two CSV/two readable Markdown, SAME editable 26-sheet Excel, verify actual saved cells and historical prior donor/case evidence. Distinct next Proceed G2-7T original Appendix A/B through PDF392 only.
