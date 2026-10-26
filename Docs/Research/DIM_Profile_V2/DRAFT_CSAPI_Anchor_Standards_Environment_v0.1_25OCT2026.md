# Draft — CSAPI Anchor Standards Environment for DIM/Profile V2

**Version:** 0.1  
**Date:** 25 October 2026  
**Standing:** Workstream 3 source-organization checkpoint; not a donor disposition or model decision.

## 1. Purpose

This document establishes the first source group for DIM/Profile V2: the native standards environment in which the eventual profile is intended to operate. The purpose is to separate that environment from the external candidate donor corpus before donor comparison begins. Inclusion in this anchor group is factual rather than evaluative: it identifies standards that define, directly underpin, or normatively support OGC API – Connected Systems (CSAPI), not sources judged to be more useful or authoritative than external donors for every modeling question.

The anchor environment is intentionally divided into two layers. The first contains the semantic and functional standards that directly define the CSAPI resource model, its principal encodings, and its conceptual basis. The second contains supporting normative infrastructure used by CSAPI or those standards. This prevents generic Web, temporal, spatial, and transport dependencies from being confused with domain-information donors.

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

### W3C/OGC Semantic Sensor Network Ontology — current 2023 Edition work

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology – 2023 Edition*. W3C Working Draft / OGC 25-022.

**Anchor role:** Current evolution of the conceptual vocabulary already underlying CSAPI and the source used in the V2 concept-baseline research. It is **not** the normative SOSA/SSN edition referenced by published CSAPI 1.0.

## 3. Supporting normative infrastructure

These sources support implementation, serialization, Web behavior, geometry, time, or protocol mechanics. They are part of the CSAPI standards environment where applicable but should **not** be treated as external domain donors merely because they appear in normative references.

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

Several sources are close to the OGC/semantic ecosystem without being native CSAPI dependencies. OGC OMS 3.0, OGC API – Processes, I-ADOPT, QUDT, SWEET, PROV, RFC 6906, and W3C Profiles Vocabulary are examples that must be classified according to their actual role rather than placed into the native anchor group merely because they are familiar or potentially useful.

## 6. Consequence for the 182-source neutral bibliography

The existing 182-entry bibliography was built as a **candidate donor population**, not as a complete inventory of every normative dependency of the CSAPI stack. The present anchor review reveals that several generic normative dependencies of CSAPI are not represented there. That is not necessarily a defect in the donor bibliography.

V2 should therefore maintain two related inventories:

1. **Anchor standards environment** — native CSAPI/SensorML/SWE/SOSA-SSN standards and supporting normative dependencies.
2. **External candidate donor corpus** — the neutral population to be grouped and reviewed for possible contributions.

This separation avoids bloating the donor corpus with generic implementation dependencies while preserving the standards pedigree needed for the eventual profile and conformance work.

## 7. Standing decision

For Workstream 3, the first source group is established as the **CSAPI anchor standards environment**, divided into:

- **Native semantic and functional core**, and
- **Supporting normative infrastructure**.

This classification is organizational only. It does not imply that every concept in the native stack must appear in the V2 DIM, nor that external donors have subordinate evidentiary value.

## References

Open Geospatial Consortium. 2025. *OGC API – Connected Systems – Part 1: Feature Resources*. OGC 23-001. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025. *OGC API – Connected Systems – Part 2: Dynamic Data*. OGC 23-002. https://docs.ogc.org/is/23-002/23-002.html.

Open Geospatial Consortium. 2025. *OGC SensorML Encoding Standard*. OGC 23-000. https://docs.ogc.org/is/23-000/23-000.html.

Open Geospatial Consortium. 2025. *OGC SWE Common Data Model Encoding Standard*. OGC 24-014. https://docs.ogc.org/is/24-014/24-014.html.

World Wide Web Consortium. 2017. *Semantic Sensor Network Ontology*. https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology – 2023 Edition*. https://www.w3.org/TR/vocab-ssn-2023/.
