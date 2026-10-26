# Draft — CSAPI Anchor Standards Environment for DIM/Profile V2

**Version:** 0.1  
**Date:** 25 October 2026  
**Standing:** Workstream 3 source-organization checkpoint; not a donor disposition or model decision.

## 1. Purpose

This document establishes the first organizational group **within the existing 182-source V2 corpus**: the CSAPI-native/anchor sources already present in that corpus. The purpose is to separate those sources from the remaining external candidate donors before comparison begins. This exercise does **not** expand the corpus and does not attempt to inventory every normative dependency, related OGC standard, transport protocol, encoding, or interoperability target mentioned by CSAPI.

The 182-source bibliography is therefore frozen for this organizational stage. A standard that is not already in that corpus does not become a donor merely because CSAPI references, links to, or interoperates with it. Such sources may be recorded later as implementation or standards-pedigree context if needed, but they remain outside the donor-grouping exercise unless a separate research decision explicitly reopens corpus scope.

## 2. Native semantic and functional core

The following standards constitute the current native semantic/functional core for V2.

### OGC API – Connected Systems – Part 1: Feature Resources

Open Geospatial Consortium. 2025. *OGC API – Connected Systems – Part 1: Feature Resources*. OGC 23-001, version 1.0.

**Anchor role:** Primary feature-resource standard for Systems, subsystems, Deployments, Procedures, Sampling Features, and Property Definitions. Part 1 states that CSAPI extends OGC API – Features, complies with OGC API – Common, implements selected SOSA/SSN concepts, and defines advanced SensorML representations.

### OGC API – Connected Systems – Part 2: Dynamic Data

Open Geospatial Consortium. 2025. *OGC API – Connected Systems – Part 2: Dynamic Data*. OGC 23-002, version 1.0.

**Anchor role:** Primary dynamic-data standard for DataStreams, Observations, ControlStreams, Commands, command status/results, feasibility, and SystemEvents. Part 2 builds on Part 1, remains aligned with SOSA/SSN, and uses SWE Common for several observation and command encodings.

### OGC SensorML Encoding Standard

Open Geospatial Consortium. 2025. *OGC SensorML Encoding Standard*. OGC 23-000, version 3.0.

**Anchor role:** Native detailed system/process description model and JSON implementation used by CSAPI. SensorML 3.0 includes PhysicalComponent, PhysicalSystem, Deployment, configurable processes, derived properties, and other constructs relevant to complete system descriptions.

### OGC SWE Common Data Model Encoding Standard

Open Geospatial Consortium. 2025. *OGC SWE Common Data Model Encoding Standard*. OGC 24-014, version 3.0.0.

**Anchor role:** Native structured data-component and encoding model used by CSAPI Part 2 for observation and command schemas and JSON/text/binary data encodings, and normatively referenced by SensorML 3.0.

### OGC API – Features – Part 1: Core

Open Geospatial Consortium. 2022. *OGC API – Features – Part 1: Core corrigendum*. OGC 17-069r4, version 1.0.1.

**Anchor role:** Base feature API extended by CSAPI Parts 1 and 2.

### OGC API – Common – Part 1: Core

Open Geospatial Consortium. 2023. *OGC API – Common – Part 1: Core*. OGC 19-072, version 1.0.

**Anchor role:** Common OGC API behavior with which CSAPI states compliance.

### W3C/OGC Semantic Sensor Network Ontology (SOSA/SSN) — 2017 Recommendation

World Wide Web Consortium. 2017. *Semantic Sensor Network Ontology*. W3C Recommendation, October 19.

**Anchor role:** Normative semantic reference cited by published CSAPI Parts 1 and 2. CSAPI Part 1 states that its resource model is derived from SOSA/SSN.

### OGC/ISO Observations, Measurements and Samples (OMS) 3.0

Open Geospatial Consortium and International Organization for Standardization. 2023. *Observations, Measurements and Samples*. OGC Abstract Specification Topic 20, OGC 20-082r4 / ISO 19156:2023.

**Anchor role:** Foundational conceptual standard for observations, observable properties, procedures, observers, hosts, deployments, samples, sampling procedures, and samplers. CSAPI Part 1 Annex C.3 explicitly identifies OMS as “one of the foundational building blocks” of CSAPI through SOSA/SSN and provides direct mappings from OMS classes to CSAPI resources. OMS therefore belongs in the native semantic core rather than in the external donor corpus.

### W3C/OGC Semantic Sensor Network Ontology — current 2023 Edition work

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology – 2023 Edition*. W3C Working Draft / OGC 25-022.

**Anchor role:** Current evolution of the conceptual vocabulary already underlying CSAPI and the source used in the V2 concept-baseline research. It is **not** the normative SOSA/SSN edition referenced by published CSAPI 1.0.

## 3. Supporting normative infrastructure

The following kinds of sources may support implementation, serialization, Web behavior, geometry, time, or protocol mechanics, but they are **not part of the donor-grouping exercise unless they already occur in the frozen 182-source corpus**. They should not be added merely because they appear in CSAPI normative references.

### OGC standards and policy dependencies

- OGC 08-131r3, *The Specification Model – A Standard for Modular Specifications*.
- OGC API – Features – Part 2: *Coordinate Reference Systems by Reference*.
- OGC API – Features – Part 4: *Create, Replace, Update and Delete* (edition/status as cited by CSAPI).
- OGC Simple Feature Access – Part 1: Common Architecture.
- OGC GeoPose 1.0, where required through SensorML.

### General Web, serialization, and schema dependencies

- RFC 8259, *The JavaScript Object Notation (JSON) Data Interchange Format*.
- RFC 7946, *The GeoJSON Format*.
- RFC 8288, *Web Linking*.
- JSON Schema Validation, Draft 2020-12.
- RFC 6455, *The WebSocket Protocol*, for applicable CSAPI Part 2 functionality.
- MQTT Version 5.0, for applicable CSAPI Part 2 functionality.

### Temporal, spatial, metadata, and units dependencies

- ISO 8601-1:2019 and ISO 8601-2:2019.
- ISO 19103, ISO 19107, ISO 19108, ISO 19111, and ISO 19115 editions normatively referenced by SensorML 3.0.
- UCUM, version 2.1, as normatively referenced by SensorML 3.0.

These dependencies affect conformance and representation but should not receive the same donor-review treatment as sources that may contribute domain concepts, relationships, or modeling structure.

## 4. Machine-readable companion artifacts

Machine-readable schemas and examples belonging to the native stack should remain associated with their parent standards rather than becoming separate conceptual donor families. Current examples already present in the V2 source population include the SensorML 3.0 JSON Schema Collection and CSAPI Part 2 `systemEvent.json`.

## 5. Important distinction from the external donor corpus

The external candidate donor corpus begins **outside** this native anchor environment. Sources such as ISA, SAPIENT, OSUS, The Open Group SOSA, NIEM, IEEE 1451/TEDS, MIMOSA, I-ADOPT, QUDT, SWEET, Redfish, OPC UA/PA-DIM, AAS, and similar models may contribute concepts, distinctions, governance methods, mappings, stress-test evidence, or nothing at all. They will be grouped neutrally by their own native subject/community in the next stage.

Several sources are close to the OGC/semantic ecosystem without being native CSAPI semantic-core dependencies. OGC API – Processes belongs to the related OGC interoperability ecosystem because CSAPI explicitly supports linking to it. I-ADOPT, QUDT, SWEET, PROV, RFC 6906, and W3C Profiles Vocabulary remain outside the native core and must be classified according to their actual role rather than placed there merely because they are familiar or potentially useful.

## 6. Consequence for the 182-source neutral bibliography

The existing 182-entry bibliography is the **frozen candidate source population for Workstream 3 organization**. The fact that CSAPI has additional normative or interoperability dependencies that are not listed there is not a reason to enlarge this corpus.

For the present exercise, V2 maintains one neutral source population and organizes it internally:

1. **CSAPI-native/anchor subset** — only sources already present in the 182-source corpus that belong to the immediate CSAPI conceptual/standards environment.
2. **Remaining external candidate donors** — all other sources in the same frozen corpus, to be grouped neutrally by their own native subject/community.

Generic implementation dependencies or adjacent interoperability standards that are absent from the 182-source corpus remain outside this organizational exercise.

## 7. Standing decision

For Workstream 3, the first source group is the **CSAPI-native/anchor subset of the frozen 182-source corpus**. OMS 3.0 belongs in that subset because CSAPI explicitly treats it as foundational. No source is added to the corpus simply because it appears in a CSAPI dependency list or related-standards annex.

This classification is organizational only. It does not imply that every concept in the anchor subset must appear in the V2 DIM, nor that external donors have subordinate evidentiary value.

## References

Open Geospatial Consortium. 2025. *OGC API – Connected Systems – Part 1: Feature Resources*. OGC 23-001. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025. *OGC API – Connected Systems – Part 2: Dynamic Data*. OGC 23-002. https://docs.ogc.org/is/23-002/23-002.html.

Open Geospatial Consortium. 2025. *OGC SensorML Encoding Standard*. OGC 23-000. https://docs.ogc.org/is/23-000/23-000.html.

Open Geospatial Consortium. 2025. *OGC SWE Common Data Model Encoding Standard*. OGC 24-014. https://docs.ogc.org/is/24-014/24-014.html.

World Wide Web Consortium. 2017. *Semantic Sensor Network Ontology*. https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology – 2023 Edition*. https://www.w3.org/TR/vocab-ssn-2023/.
