# Step15 — Integrated Sensor Architecture (ISA) 6.0 original-source audit

**7 November 2026.** Examined textual pages of five original October 2023 ISA 6.0 Distribution Statement A project-uploaded PDFs. Eleven source-native candidate correspondences are staged and fourteen native-source distinctions held. The original source PDFs are not republished on GitHub because raw materialization was unavailable.

## Primary source documents and editions

| ISA original | Exact source edition (31 October 2023) | Prior project file |
|---|---|---|
| ISA Software Design Document | Document 6.0 revision 5 | ISA_Software_Design_Document-6.0r5.pdf |
| ISA Data Model Specification | Release 6.0 document revision 12 | ISA_Data_Model_Specification-6.0r12.pdf |
| ISA Component Requirements | Document 6.0 revision 4 | ISA_Component_Requirements-6.0r4.pdf |
| ISA Controller Requirements | Document 6.0 revision 4 | ISA_Controller_Requirements-6.0r4.pdf |
| ISA Interface Control Document | Document 6.0 revision 5 | ISA_Interface_Control_Document-6.0r5(1).pdf |

**Important:** A current 2026 Army Summit report and earlier 2023 Army public overview support context only; these do NOT replace the original 6.0 text. The ISA documents have different revision suffixes within release 6.0.

## Eleven source-checked mappings to existing proposed DIM rows

| Proposed DIM information element | ISA original term | Fit | Original clause and printed/PDF page | Boundary |
|---|---|---|---|---|
| Persistent System identifier | UCI (Universal Component Identifier) | PARTIAL | DMS §4.0 UCI printed p.55, PDF p.70; ICD §6.1 printed p.19, PDF p.27; Component Requirements [CMPT-M-0001], PDF p.14 | Does not automatically identify a CSAPI System URI, physical station, individual probe serial or full sensing arrangement |
| Described sensing System / arrangement | ISA composition (via CIC) | PARTIAL | Software Design Document §4.2.2, printed pp.10–12, PDF pp.18–20 | Capability aggregation is not one physical housing or complete physical bill of materials |
| Network-visible participant | ISA component / ISA Controller | PARTIAL | Software Design Document §4.2.1, printed pp.9–10, PDF pp.17–18 | Network participant is not necessarily the physical sensing device or actual Observation performer |
| Physical constituent | composition member (visible / opaque) | RELATED | Software Design Document §4.2.2, printed pp.10–11, PDF pp.18–19 | Composition member may be software or non-ISA; visibility does not establish physical containment |
| Connected external equipment | CIC-to-member ISA/native interface | RELATED | Software Design Document §4.2.2, printed pp.10–11, PDF pp.18–19 | Does not prove a physical cable, externality, installed topology or exact connection scheme |
| Reported output field | Observable Declaration (CCD.observables) | PARTIAL | Data Model Specification §7.3 Observable Declaration, printed p.72, PDF p.87; §6.2 Config.ccd, printed p.58, PDF p.73 | Declared field is not a performed reading, physical channel or CSAPI DataStream result schema |
| Performed Observation | Event message (reported observables) | RELATED | Data Model Specification §6.2 Event, printed pp.58–59, PDF pp.73–74; ICD §6.6, printed pp.22–23, PDF pp.30–31 | The published Event message is not automatically identical to an underlying OMS/CSAPI observing act or its original resultTime |
| Supported operating mode | Capability Declaration (Config.ccd) | RELATED | Data Model Specification §7.3 Capability Declaration, printed p.70, PDF p.85; §6.2 Config.ccd, printed p.58, PDF p.73; ICD §6.4, printed p.20, PDF p.28 | Not a complete operating-mode register, the currently selected setting or proof of execution |
| Source-reported operating mode | Status.properties (current component values) | RELATED | Data Model Specification §6.2 Status, printed p.61, PDF p.76; ICD §6.5, printed pp.21–22, PDF pp.29–30 | Only a specifically declared mode property could convey a mode; Status does not itself establish a mode or independent health truth |
| Issued control request | Request message (command invocation) | PARTIAL | Data Model Specification §6.2 Request, printed pp.59–60, PDF pp.74–75; ICD §6.7, printed pp.23–25, PDF pp.31–33 | A message type or declared command does not establish a particular issued/authorized/executed real-world action |
| Command acknowledgement / reported outcome | Response message (command disposition) | PARTIAL | Data Model Specification §6.2 Response, printed p.60, PDF p.75; ICD §6.7.1 Table 23, printed pp.24–25, PDF pp.32–33 | Response Success is a reported disposition, not independently observed physical effect |

These are source-to-DIM research proposals, not ISA-authored equivalence declarations, adopted DIM elements or formal test results. Composition member and virtual/opaque/visible semantics must not be reduced to physical enclosure or individually installed hardware.

## Fourteen source-native ISA concepts deliberately held

| ISA original concept | Original clause and page | Why held |
|---|---|---|
| Visible versus opaque composition member | SDD §4.2.2 printed p.11, PDF p.19 | Network-facing exposure does not prove the presence/absence of hidden physical hardware |
| Virtual component / CIC-scoped UCI | SDD §4.2.2 printed p.11, PDF p.19; Component Requirements [CMPT-L-0008], PDF p.16 | Virtual proxy identification is not an additional independent physical device |
| Transparent versus translucent member | SDD §4.2.2 printed p.11, PDF p.19 | Visible membership does not guarantee that the member can be tasked |
| CIC performer / broker / relay | SDD §4.2.2 printed p.11, PDF p.19 | Network endpoint receiving a request need not be the actual performer |
| CCD: properties / observables / commands / custom types | DMS §7.3 printed p.70, PDF p.85; ICD §6.4 printed pp.20–21 | Declarations of unlike capability kinds must not collapse into one operating mode |
| Capability readiness versus reporting | ICD §6.4 printed p.21, PDF p.29; Component Requirements [CMPT-M-0026/27] | Capability ready, reporting and actually executed are different states |
| PropertyDeclaration.mutability / range | DMS §7.3 printed p.73, PDF p.88 | Read-write support is not an installed default or current effective setting |
| Minimum and Maximum Status Interval | ICD §6.5 printed pp.21–22, PDF pp.29–30 | Heartbeat cadence does not establish measurement period or diagnostic state |
| Event.source + event time + eventID | ICD §6.6 printed p.22, PDF p.30; DMS §4.0 Event ID printed p.52 | An event-identity tuple does not determine the original NOAA averaged-result process |
| Event Reference corrections/updates | ICD §6.6 printed p.23, PDF p.31 | Correction/update reference is not a general original-to-API-copy provenance model |
| Response queued/in progress/final codes | ICD §6.7.1 Table 23 printed p.25, PDF p.33 | Reported success and measured physical effect differ; queued/in progress are nonfinal |
| Authorization before forwarding requests | ICD §6.7.1 printed p.24, PDF p.32; Controller Requirements [AZSV-M-0001], PDF p.44 | A successful authorization check is not itself a command execution |
| Controller deployment/communications topology | SDD §§4.2.1–4.3 printed pp.9–13, PDF pp.17–21 | A network/controller location is not a surveyed sensor point or dated physical deployment |
| Custom / Nominated / Accepted extensions | DMS preliminary Document Notes printed p.ii, PDF p.2 | Extension category does not mean a term is in the adopted ISA core model |

The Data Model Specification explicitly differentiates Custom, Nominated and Accepted nonstandard extension entries. A new data model extension is not necessarily a core adopted ISA data type.

## Four original case falsification checks

**Dragino:** one external SHT31 carrying temperature/humidity does not imply a particular ISA CIC or virtual component. **AirGradient:** two PMS5003 modules at PM1/PM2 sockets do not become three physical sensors because three particulate outputs exist. **Campbell:** fourteen ClimaVue response positions and thirty-one separate logger Status example fields do not prove an installed ISA Config/Status/Event producer. **Bennett:** the real historical station has two serial-numbered EE181 probes across three dated service-role statements and two original NOAA temperature means represented by four experimental API copies. The original resultTime is UNKNOWN, the source QA text including its trailing space remains intact, and a station site coordinate is not a surveyed probe point.

## Workbook disposition and Step16 owner checkpoint

The approved primary workbook remains 13 columns, 22 proposed DIM rows, nine case-only holds, 73 source-qualified cases, and 58 prior donor correspondence records (37 earlier original-standard-source-checked, 6 IEEE public-technical-only, 15 OPC/SAPIENT prior-only). The eleven ISA original-source-backed records are staged separately and do not inflate those primary totals.

The new v0.9 workbook includes both an ISA Original Clause Audit worksheet and the full 14-column ISA Proposed Overlay worksheet, in addition to all unchanged prior worksheets. A GitHub-readable 14-column overlay and CSV also exist. The candidate ISA column is not part of the accepted primary master until owner review.

**NEXT:** Step16 owner checkpoint only. Decide whether the ISA donor column and any previously held unique concepts should be promoted, adjusted or rejected. Step17 The Open Group SOSA is not started.

## Public contextual evidence (not the primary source PDFs)

U.S. Army, February 6, 2023: https://www.army.mil/article/263782/armys_interoperable_sensors_solution_keeps_military_modernization_efforts_on_track

U.S. Army / DVIDS, July 14, 2026: https://www.dvidshub.net/news/printable/569918
