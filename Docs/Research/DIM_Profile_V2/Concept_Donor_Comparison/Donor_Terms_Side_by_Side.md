# Donor terms, side by side

**What do different standards call the same thing?** Read across a row. The bold first column gives a working meaning for our Domain Information Model (DIM); the other columns use the donors’ own names. The short notes tell you when a translation needs more than the name. These are working mappings, not a requirement that every system supply every value.

[Equipment identity](#equipment-identity) · [Components and channels](#components-and-channels) · [Observations and samples](#observations-and-samples) · [Task responses](#task-responses) · [Donors and original diagrams](#donors-and-original-diagrams)

**Working specification:** [Read the proposed DIM relationships](../Candidate_Specification/DIM.md#components-and-channels) or [see how the Profile carries them](../Candidate_Specification/CSAPI_Profile.md#components-and-channels).

## Equipment identity

| Working DIM meaning | SAPIENT v2 | OPC UA Devices | PA-DIM | ETSI SAREF Core |
|---|---|---|---|---|
| **Manufacturer name** | `manufacturer` | `Manufacturer` | `2:Manufacturer` | `hasManufacturer` |
| **Product model designation** | `model` | `Model` | `2:Model` | `hasModel` |
| **Serial number of a hardware unit** | `serial_number` when it identifies hardware | `SerialNumber` | `2:SerialNumber` | `hasIdentifier` is broader; needs an explicit serial-number meaning |
| **Hardware revision** | `hardware_version` | `HardwareRevision` | `2:HardwareRevision` | No hardware-specific field established here |
| **Software revision** | `software_version` | `SoftwareRevision` | `2:SoftwareRevision` | No software-specific field established here |

**What maps directly?** When the fields describe the same item, the first two rows carry the same basic facts: who made it and what the product is called. PA-DIM explicitly inherits the Devices nameplate properties; Table 110 even links them to dictionary entries. That is documented reuse, not two independent inventions. The SAPIENT and SAREF pairings are our comparison of their definitions. Keep the original text and its language when supplied.

**Where does the match stop?** SAPIENT permits a software-only node to use `serial_number` for a product or license number. That value does **not** belong in a hardware serial-number field. Keep the component a revision applies to; OPC UA’s `SoftwareRevision` can describe firmware. SAREF’s general identifier and revision properties do not, by themselves, tell us which sort we have. `DeviceType` is an OPC UA type, **not** an alternative spelling of `Model`.

**One equipment check:** [Dragino sheet, C-I01, C-I15 and C-I16](../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md) gives the product designation **S31-LB**. We can populate the product-model row from the reference description. We cannot populate an individual unit’s serial number or installed firmware from that fact. The decoder version is not the unit’s software revision. This uses the sheet as documented evidence; it does not assert Dragino implements any of these donors.

*Definitions behind the cells:* [BSI Flex 335 v2.0:2024-03, §6.2.5.15, Table 32, printed p. 36][bsi-name] (fields on `ConfigurationData`); [OPC UA Devices v1.05.0, §4.5.2, VendorNameplate][di] and [§4.7, Table 35][device]; [OPC 30081 PA-DIM v1.02.0, §7.2, Tables 109–110][pa]; [ETSI SAREF Core v4.1.1, Device kinds and devices and Data Properties][saref]. `2:` is the namespace prefix as printed in PA-DIM’s table, not a fixed runtime namespace index. `has…` names in the SAREF column use the `saref:` prefix.

## Components and channels

**Question:** Is the source telling us what is physically there, what function it performs, how to address it, or what data it reports? Start with the [one-probe, two-quantity example](../Candidate_Specification/CSAPI_Profile.md#worked-result-s31-lb). The cells are our working correspondences, not donor-declared equivalences. **—** means no direct counterpart established in the material checked for that cell, not a finding that the donor lacks the idea.

| What we want to represent | IEEE 1451 public technical evidence | Integrated Sensor Architecture (ISA) 6.0 | The Open Group Sensor Open Systems Architecture (SOSA) | Connected Systems / SensorML / SWE Common |
|---|---|---|---|---|
| **A physical constituent** | `Transducer Interface Module` (TIM) when identified as hardware; membership needs evidence | A composition member *may* represent hardware; membership alone does not establish that | `Sensor Hardware Element`, e.g. a plug-in card | A physical `components` entry in SensorML; a CSAPI subsystem only when separately represented as a System |
| **A function implemented by hardware or software** | — | Component Capability Description declares capabilities; it does not identify their hardware implementation | `SOSA module` (functional building block); `ProductInstance` relates a manufactured product to `Component_` in the separate data model | SensorML `SimpleProcess` / `AggregateProcess` for nonphysical processes, not names for a circuit board |
| **An addressed transducer channel** | `TransducerChannel`; its Transducer Channel TEDS describes that channel | —; a visible member's identity addresses a participant, not necessarily a channel | — | A named output can carry the data; a `DataStream` is **not** the native channel address |
| **An interface exposes a member's capability** | Network Capable Application Processor (NCAP) mediates access to TIM services; related role, not ISA visibility semantics | Composition member can be visible or opaque; the composition can expose an opaque member's capabilities as its own | — | SensorML `connections` can trace a known member output to an aggregate output; this does not encode ISA taskability |
| **A quantity represented in an output** | Channel TEDS physical units qualify a channel's data; unit alone does not identify the property | `Observables` in capability definitions; declaration, not a reading | — | SWE `Quantity` within a `DataRecord`; CSAPI `DataStream` groups observations for an output. OMS `ObservableProperty` is what is observed, not the field or device |

**How these donors changed the design.** SOSA makes it possible to say *what implements a function*. ISA explains why *who exposes it* can be different. IEEE makes it worthwhile to retain the address of a channel even when there is no separately identified hardware part. SensorML and SWE supply concrete encodings for the part, its output and the output's fields. These are complementary contributions, not votes to make every column mean “subsystem.”

**Read the definitions:** ISA *Software Design Document* 6.0r5 §§4.2.2, 5.1.1 and *Data Model Specification* 6.0r12 §2. Open Group *SOSA Reference Architecture* ed. 1.1 §5.1, Fig. 5.1-1 and *Domain-Specific Data Model* ed. 1.0 §§1.1.3.15, .82–83 ([original-document locators](../Donor_Challenge/04_Other_Structural_Challenges.md)). IEEE: [2024-linked Playground tutorial](https://iml.ubi.pt/playground/docs/ieee1451/intro/), [NIST Channel TEDS example](https://www.nist.gov/el/intelligent-systems-division-73500/channel-teds), [authors’ historical P1451 service example, Tables 1 and 3](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=927142), and [edition/access notes](../Donor_Challenge/03_IEEE1451_Challenge.md). Actual OGC texts: [SensorML §§8.4–8.6, 9.5.2](https://docs.ogc.org/is/23-000/23-000.html), [CSAPI Part 1 §§10, 13](https://docs.ogc.org/is/23-001/23-001.html), [Part 2 §§9.1–9.2, 16.1.4](https://docs.ogc.org/is/23-002/23-002.html) and [OMS §§8.3, 8.6][oms]. The IEEE material is technical evidence, not a new inspection of licensed 2024 normative clauses.

[**Resulting DIM definitions**](../Candidate_Specification/DIM.md#components-and-channels) · [**Candidate Profile rules, example and check**](../Candidate_Specification/CSAPI_Profile.md#components-and-channels)

## Observations and samples

| Working DIM meaning | OMS 3.0 | Earlier O&M (2011) | SOSA/SSN (2017) | Connected Systems API 1.0 |
|---|---|---|---|---|
| **Act of observing** | `Observation` | `OM_Observation` | `sosa:Observation` | `Observation` |
| **Property being observed** | `ObservableProperty` | `GFI_PropertyType` | `sosa:ObservableProperty` | `Property` (observable use) |
| **Entity doing the observing** | `Observer` | `OM_Process`¹ | `sosa:Sensor` | `System` typed `sosa:Sensor` |
| **Method used to observe** | `ObservingProcedure` | `OM_Process`¹ | `sosa:Procedure` used for observation; `sosa-om:ObservationProcedure` in the O&M alignment | `Procedure` typed `sosa-oms:ObservingProcedure` |
| **Hosting platform** | `Host`² | No entry in C.3 | `sosa:Platform` | `System` typed `sosa:Platform` | **Sample** | `Sample` | `SF_SamplingFeature` | `sosa:Sample` | `SamplingFeature` |

**Who says these match?** The OMS, O&M and API columns follow the [published Connected Systems Part 1, informative Annex C.3][c3] shown in the owner’s screenshot. [W3C/OGC’s 2017 O&M alignment, §§6.3.4–6.3.5][ssn], explicitly calls `OM_Observation` and `sosa:Observation` equivalent classes, and likewise `SF_SamplingFeature` and `sosa:Sample`. Those are **published equivalents for the named pair and editions**. They do not declare every cell across the row equivalent. The extension prefixes `sosa-om:` (2017 alignment) and `sosa-oms:` (as printed in CSAPI) intentionally differ.

¹ The older `OM_Process` can refer to the observer **or** its method. A converter cannot decide which row to use from the class name alone. The 2017 alignment actually gives a union of the Sensor and ObservationProcedure classes, not two one-to-one synonyms. In [OMS §§8.5–8.6][oms], the corresponding distinction is explicit: the observer performs the method; it is not the method.

² This row covers a platform that hosts observing equipment. OMS `Host` is broader: §8.7 also allows an organizational grouping. Do not translate a survey campaign into a physical platform. The API column names the resource/role in C.3, not a literal JSON `type` field to copy.

**What our model gains:** the equipment that made a reading, the method it followed, the act of observing and the resulting value remain distinct. In the [OMS standard’s own worked example, §7.3.1, Figures 4–5][oms], the **pallet** is what is observed, **mass** is the property, and **25 kg** is the result. The scale is not the pallet, and 25 kg is not the observation itself.

## Task responses

This is a *project-proposed* mapping between two independently published code lists. The destination in Connected Systems is the command’s **`CommandStatus.statusCode`**, not a diagnosis of the equipment. Read it in the direction **SAPIENT report → candidate DIM meaning → CSAPI report**.

| Working DIM meaning | SAPIENT `TaskAck.task_status` | CSAPI `CommandStatus.statusCode` | Translation note |
|---|---|---|---|
| **Request accepted** | `ACCEPTED` | `ACCEPTED` | Both distinguish acceptance from completion. CSAPI explicitly allows later rejection or failure. |
| **Request rejected** | `REJECTED` | `REJECTED` | Match for a refused request. Preserve any supplied reason; CSAPI treats this state as final. |
| **Execution completed successfully** | `COMPLETED` | `COMPLETED` | Match the reported outcome. CSAPI also calls for actual execution time; the status code alone does not supply it. |
| **Execution failed** | `FAILED` | `FAILED` | Match when the failure was during execution. Do not invent an execution phase from a general inability to finish. |
| **Status unspecified** | `UNSPECIFIED` | No corresponding code in Table 14 | Do not translate to `PENDING`: unknown status does not mean a decision is pending. |

*Definitions:* [BSI Flex 335 v2.0, §6.5.9, Tables 86–87, printed p. 72][bsi-task]; [CSAPI Part 2 v1.0, §10.11, Tables 13–15][cs2]. **Proposed Profile check:** a SAPIENT `ACCEPTED` report alone must never generate a CSAPI `COMPLETED` report. Link status to the same requested operation; check report time, execution time and required information separately before emitting a resource. The table maps status meanings, not whole messages; no live transform is claimed.

## Donors and original diagrams

| Donor and edition | Find these concepts | Open the publisher’s diagram |
|---|---|---|
| **OPC UA Devices 1.05.0** — OPC Unified Architecture, Part 100 | Manufacturer, model, serial, revisions, device structure | [Figure 5: vendor nameplate][di] · [Figure 10: DeviceType][device] (OPC information model diagrams) |
| **PA-DIM 1.02.0** — Process Automation Device Information Model | Device base, inherited nameplate, signals, condition and subdevices | [§6.1, Figure 7: PA-DIM device model][pafig] |
| **SAPIENT v2.0** — BSI Flex 335 | Nodes, component configuration, task, acknowledgement | [Figure 1: architecture, PDF p. 11][bsifig]. An illustrative architecture drawing, not a UML class diagram. The field and code definitions are Tables 32 and 86–87. |
| **SAREF Core 4.1.1** — Smart Applications REFerence ontology | Device, device kind, property, state, function, command | [Figure 6: devices][sarefimg] · [text and caption][saref] (ontology diagram) |
| **OMS 3.0.0** — Observations, measurements and samples | Observer, observing procedure, observation, property, host, deployment, sample | [Figure 9: conceptual Observation schema, §8.1.1][omsfig] (UML, printed p. 46); [preserved original PDF and retrieval details](../Primary_Sources/OGC_20-082r4_OMS_3.0.0.md). For a concrete instance, see Figure 5, p. 42. |
| **O&M 2.0** — Observations and Measurements, ISO 19156:2011 | Earlier observation, process and sampling feature | [OMS Annex C.5.1 and C.5.2][migration] compare the old and revised observation models. This is the successor standard’s account. |
| **SOSA/SSN (2017)** — Sensor, Observation, Sample and Actuator / Semantic Sensor Network | Sensor, observation, observable property, procedure, platform, sampler, sample | [Figure 3: observations][ssnimg] · [figures and text in §4][ssn] (ontology diagrams, not UML) |
| **OGC API – Connected Systems 1.0** — Parts 1–2 | System, Procedure, Deployment, SamplingFeature, Observation, Command and CommandStatus | [Part 1, Figure 1: API resource UML, PDF p. 40][csfig] · [Part 2, §10.11, Figure 6: command status][cs2] |
| **SensorML 3.0** | Components and connections of a physical system | [§8.6, Fig. 18: physical processing system; §9.5.2: worked datasheet](https://docs.ogc.org/is/23-000/23-000.html) |
| **Integrated Sensor Architecture 6.0** | Visible and opaque composition members | Software Design Document 6.0r5, §4.2.2, Fig. 2, printed p. 12 ([source locator](../Donor_Challenge/04_Other_Structural_Challenges.md)); original supplied PDF, not rehosted here |
| **The Open Group SOSA ed. 1.1** | Logical modules versus supporting infrastructure | Reference Architecture §5.1, Fig. 5.1-1, printed p. 29 ([source locator](../Donor_Challenge/04_Other_Structural_Challenges.md)); distinct from W3C/OGC SOSA above |
| **IEEE 1451 public sources** | Module, access services, and transducer channel | [NIST-hosted authors’ Fig. 3 and Table 1, PDF p. 2](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=927142#page=2); historical implementation illustration, not 2024 normative UML |

<details>
<summary>Show original ontology diagrams: SAREF devices and SOSA observations</summary>

**ETSI SAREF Core v4.1.1, Figure 6.** Publisher’s image; [read with its definitions][saref].

![ETSI diagram of devices and kinds of device][sarefimg]

**W3C/OGC, Semantic Sensor Network Ontology (2017), Figure 3.** Publisher’s image; [read with the other perspectives][ssn].

![W3C and OGC diagram of the SOSA observation perspective][ssnimg]

</details>

**Maintaining this page:** add a row for a new meaning or a column for another donor where the original definition supports it. Keep published equivalences distinct from our proposed translations. A missing cell means “not established here,” not “the donor cannot express it.” These tables cover selected concepts from the listed editions, not the entire donor corpus. [Other donor families and earlier research](Donor_Contributions.md) · [Candidate DIM foundation v0.2](../Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md) · [Working DIM text](../Candidate_Specification/DIM.md) · [Working Profile text](../Candidate_Specification/CSAPI_Profile.md).

[bsi-name]: https://www.bsigroup.com/siteassets/pdf/en/insights-and-media/insights/brochures/bsi-flex-335.pdf#page=48
[bsi-task]: https://www.bsigroup.com/siteassets/pdf/en/insights-and-media/insights/brochures/bsi-flex-335.pdf#page=84
[bsifig]: https://www.bsigroup.com/siteassets/pdf/en/insights-and-media/insights/brochures/bsi-flex-335.pdf#page=11
[di]: https://reference.opcfoundation.org/DI/v105/docs/4.5.2
[device]: https://reference.opcfoundation.org/DI/v105/docs/4.7
[pa]: https://reference.opcfoundation.org/specs/OPC-30081/7.2
[pafig]: https://reference.opcfoundation.org/specs/OPC-30081/6.1
[saref]: https://saref.etsi.org/core/v4.1.1/
[sarefimg]: https://saref.etsi.org/core/v4.1.1/diagrams/Devices.png
[c3]: https://docs.ogc.org/is/23-001/23-001.pdf#page=224
[csfig]: https://docs.ogc.org/is/23-001/23-001.pdf#page=40
[cs2]: https://docs.ogc.org/is/23-002/23-002.html#:~:text=Command%20Status%20Codes
[ssn]: https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/
[ssnimg]: https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/images/SOSA-OntStructure-Observation.png
[oms]: https://docs.ogc.org/as/20-082r4/20-082r4.html
[omsfig]: https://docs.ogc.org/as/20-082r4/20-082r4.html#:~:text=Figure%209.%20Conceptual%20Observation%20schema%20overview
[migration]: https://docs.ogc.org/as/20-082r4/20-082r4.html#:~:text=OM_Observation%20in%20ISO
