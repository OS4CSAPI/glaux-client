# DIM/Profile V2 Chassis Study — Phase A Independent Extractions

**Working draft v0.1 — 25 October 2026**  
**Status:** Research artifact; Phase A complete. No donor ranking, chassis selection, or clean-DIM edit is made in this document.  
**Controlling continuity:** `PITON_DIM_Profile_V2_Continuity_v0.4_25OCT2026` §§13–17.  
**Corpus:** Frozen 182-source V2 corpus; this study covers the 14 artifacts classified as Conceptual / Information / Domain Models in the source-type audit.

## 1. Purpose and method

This document executes Phase A of the chassis study defined by the active PITON. “Chassis” remains research shorthand for the bounded conceptual frame that identifies the class of real-world thing the DIM is about and establishes the high-level conceptual basis by which that thing is understood. It is not a proposed class or profile term.

Each of the fourteen sources is characterized independently under the same fifteen questions. Source-derived facts are stated first. V2 comparison statements are explicitly labeled as **V2 inference** so that project interpretation is not confused with donor semantics. The order remains neutral. The categories in field 15 are descriptive evidence labels only; they are not rankings.

### Evidence-depth notation

- **Full / source-native:** the complete or directly inspectable source artifact, official HTML specification, source code, or full project-provided artifact was inspected.
- **Official scope + sample:** official metadata/abstract plus an official preview/sample was available, but the complete normative source was not.
- **Official scope only:** official public abstract/metadata was available but the complete normative source was not.
- **Exact-version public overview + official metadata:** an exact-version overview was publicly inspectable through a mirror while official/NATO metadata established identity and scope; conclusions are limited accordingly.

---

## 2. Industrial Digital Twin Association — AAS Part 1: Metamodel v3.2

**Source:** Industrial Digital Twin Association. 2026. *Specification of the Asset Administration Shell Part 1: Metamodel*. IDTA 01001, version 3.2.  
**Evidence depth:** Full / source-native. Official HTML and the corresponding open-source metamodel documentation were inspected.  
**Primary locator:** https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/index.html

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | The core metamodel of the Asset Administration Shell (AAS): a standardized digital representation of an asset, with metadata, submodels, and model elements used to represent aspects of that asset. |
| 2 | Primary modeled subject | The organizing subject is an **asset as digitally represented by an AAS**, not a sensor or sensing system specifically. |
| 3 | Central / top-level concepts | Asset Administration Shell, AssetInformation, Asset, Submodel, SubmodelElement, Entity, Referable/Identifiable concepts, and type/instance/batch/role asset distinctions. A Submodel represents an aspect of an asset. |
| 4 | Membership / boundary criteria | The AAS boundary is representation-centered: an AAS represents an asset. The Entity concept further distinguishes **self-managed entities** (with their own AAS) from **co-managed entities** (without a separate AAS and represented as part of another self-managed entity). |
| 5 | System / asset / device / equipment / platform / component distinctions | **Asset** is intentionally broad and may be a single entity, collection, assembly, or composition; examples include physical equipment, parts, software, and intangible assets. The terminology section also defines System and Component, but these do not narrow Asset to sensing equipment. |
| 6 | Relationship to sensing | Sensing is not a membership criterion or organizing purpose. A sensor can be represented as an asset or part of one, but the metamodel is domain-neutral. |
| 7 | Relationship to equipment / physical realization | Strong but non-exclusive. Instance assets may be devices, machines, control systems, production systems, etc.; however, assets can also be digital or intangible. AssetKind and asset identifiers distinguish kinds/instances rather than equating Asset with equipment. |
| 8 | Physical / logical / functional / operational / informational character | Primarily an **informational/digital-representation** model anchored to a real or conceptual asset. It can carry physical, functional, operational, commercial, and other viewpoints through submodels. |
| 9 | Inside vs outside boundary | Inside the AAS are identifying metadata and submodels/aspects of the represented asset. The asset itself is the represented subject rather than a data structure contained inside the AAS. External assets/entities can be related or represented separately. |
| 10 | Composition / hosting / deployment / environment | Entity modeling and the self-managed/co-managed distinction support nested parts and assemblies. Submodels can describe structure and other aspects, but deployment is not the primary organizing boundary in Part 1. |
| 11 | Established names | **Asset**, **Asset Administration Shell**, and **digital representation** are established concepts. “Asset” is a plausible upper abstraction but not inherently a sensing-equipment family term. |
| 12 | Abstraction breadth | Very broad: physical, digital, and intangible assets. It can encompass all motivating equipment but also far more than the intended V2 family. |
| 13 | Known lineage / alignments | The specification explicitly draws terminology from IEC 63278 and is part of the aligned AAS specification series (API, data specifications, security, AASX). |
| 14 | Comparison to current V2 baseline | **V2 inference:** broader than `System + Sensor + Equipment` on the asset axis and orthogonal on sensing role. It supplies a strong asset/digital-representation frame but does not itself identify hardware sensing systems. |
| 15 | Chassis relevance | **V2 inference:** potentially supplemental and potentially central on the asset/equipment-realization axis; too broad by itself to establish the sensing-family boundary. No ranking is implied. |

---

## 3. IEEE — IEEE 1451.1-1999 NCAP Information Model

**Source:** IEEE. 1999. *IEEE Standard for a Smart Transducer Interface for Sensors and Actuators—Network Capable Application Processor (NCAP) Information Model*. IEEE 1451.1-1999.  
**Evidence depth:** Official scope only, supplemented by the ANSI catalog description of the object-model blocks. The complete normative text was not available to this Phase A review.  
**Primary locators:** https://standards.ieee.org/ieee/1451.1/2164/ ; https://webstore.ansi.org/standards/ieee/14511999

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | A network-neutral object model for connecting processors to communication networks, sensors, and actuators. |
| 2 | Primary modeled subject | The **Network Capable Application Processor (NCAP) information/object model**, not an arbitrary physical sensing system as a whole. |
| 3 | Central / top-level concepts | Public descriptions identify the transducer block, function block, physical block, and network block, together with services/components and their interactions. |
| 4 | Membership / boundary criteria | The modeled boundary is the NCAP-side software/object environment that mediates processor, network, and transducer interactions. |
| 5 | System / asset / device / equipment / platform / component distinctions | The public scope does not establish a generic Asset/Equipment/Platform taxonomy. It distinguishes processor/network/transducer functions through the object blocks. |
| 6 | Relationship to sensing | Central, but paired with actuation: the model explicitly serves **sensors and actuators**. |
| 7 | Relationship to equipment / physical realization | Physical transducers and processor/network interfaces motivate the model, but the standardized subject is an object/information model rather than a general equipment model. |
| 8 | Physical / logical / functional / operational / informational character | Predominantly logical, functional, and informational, with a “physical block” representing physical-device concerns within the object model. |
| 9 | Inside vs outside boundary | Blocks, services, components, and sensor/actuator interactions are in scope. The project description explicitly excludes defining individual device algorithms and implementation specifics. |
| 10 | Composition / hosting / deployment / environment | Block composition and interfaces are central; deployment/environment semantics are not established by the public scope material reviewed. |
| 11 | Established names | **NCAP** is a recognized standardized concept, but it names the network-capable processor role rather than the general V2 family. |
| 12 | Abstraction breadth | Narrower than V2 in whole-system scope and tied to smart-transducer network architecture. |
| 13 | Known lineage / alignments | Direct predecessor of ISO/IEC/IEEE 21451-1:2010, which IEEE identifies as an adoption of IEEE 1451.1-1999. |
| 14 | Comparison to current V2 baseline | **V2 inference:** narrower/partial. It strongly addresses the processor/network/transducer boundary but does not establish `Equipment` as the whole operational sensing subject. |
| 15 | Chassis relevance | **V2 inference:** potentially supplemental or too narrow as a whole-system chassis; valuable as a smart-transducer architectural boundary. Evidence ceiling is limited by lack of full normative text. |

---

## 4. ISO/IEC — ISO/IEC 29182-4:2013 SNRA Part 4: Entity Models

**Source:** ISO/IEC. 2013. *Information Technology—Sensor Networks: Sensor Network Reference Architecture (SNRA)—Part 4: Entity Models*. ISO/IEC 29182-4.  
**Evidence depth:** Official scope + official sample/preview.  
**Primary locator:** https://www.iso.org/standard/57094.html

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | Entity models for entities that enable **sensor network applications and services** under the Sensor Network Reference Architecture. The series aims to facilitate sensor-network design, improve interoperability, and support plug-and-play components. |
| 2 | Primary modeled subject | The **sensor network** and the physical/functional entities that realize its applications and services. |
| 3 | Central / top-level concepts | The sample divides entities into **physical entities** and **functional entities**. Examples include sensor nodes, gateways, sensors, actuators, data acquisition, processing, routing, authentication, self-localization, group management, collaborative processing, and device management. |
| 4 | Membership / boundary criteria | An entity belongs when it enables sensor-network applications/services within the SNRA. Physical and functional entities are both first-class views of the architecture. |
| 5 | System / asset / device / equipment / platform / component distinctions | The reviewed material uses physical entity, hardware/device/component, sensor node, gateway, sensor, and actuator concepts rather than a generic Asset/Equipment hierarchy. Sensors within a node are also physical entities. |
| 6 | Relationship to sensing | Central and defining: the source is expressly a sensor-network entity model. |
| 7 | Relationship to equipment / physical realization | Explicit. Physical entities are the hardware/devices/components forming the network; sensors and actuators are physical entities, with functional entities implemented on one or more physical entity types. |
| 8 | Physical / logical / functional / operational / informational character | Deliberately hybrid: the model separates **physical** entities from **functional** entities and relates functions to the physical entities that perform them. |
| 9 | Inside vs outside boundary | Sensor nodes, gateways, sensors, actuators, and network-specific functions are intrinsic to the sensor-network frame. The larger operational environment is context rather than the modeled subject. |
| 10 | Composition / hosting / deployment / environment | The sample explicitly recognizes sensors within nodes and functions carried out on physical entity types. It therefore supplies hosting/realization semantics even though deployment lifecycle is not the primary subject. |
| 11 | Established names | **Sensor network**, **sensor node**, **gateway**, **physical entity**, and **functional entity** are recognized concepts. “Sensor network” names a larger aggregate than many motivating V2 equipment instances. |
| 12 | Abstraction breadth | Broad across a whole network and its functions; potentially wider than a single deployed sensing equipment/system but narrower than generic IoT or enterprise architecture. |
| 13 | Known lineage / alignments | Part of the ISO/IEC 29182 SNRA series; terminology and architectural views are distributed across companion parts. |
| 14 | Comparison to current V2 baseline | **V2 inference:** broader in aggregate/network boundary, but directly relevant to sensing and physical realization. It provides a physical-versus-functional distinction not present in the simple `Sensor + Equipment` pair. |
| 15 | Chassis relevance | **V2 inference:** potentially central as a sensor-network frame and potentially supplemental for physical/functional distinctions; may be too broad if the V2 subject remains one equipment/system rather than the network. |

---

## 5. ISO/IEC/IEEE — 21451-1:2010 NCAP Information Model

**Source:** ISO/IEC/IEEE. 2010. *Information Technology—Smart Transducer Interface for Sensors and Actuators—Part 1: Network Capable Application Processor (NCAP) Information Model*. ISO/IEC/IEEE 21451-1:2010.  
**Evidence depth:** Official scope only. ISO reports that the edition was confirmed in 2025.  
**Primary locator:** https://www.iso.org/standard/54357.html

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | An object model with a network-neutral interface connecting processors to communication networks, sensors, and actuators. |
| 2 | Primary modeled subject | The **NCAP information model** and its interactions with sensors/actuators. |
| 3 | Central / top-level concepts | The official abstract identifies blocks, services, and components. IEEE identifies the publication as an adoption of IEEE 1451.1-1999. |
| 4 | Membership / boundary criteria | Information belongs insofar as it participates in the NCAP object model and processor/network/transducer interactions. |
| 5 | System / asset / device / equipment / platform / component distinctions | No generic Asset/Equipment/Platform taxonomy is established in the public abstract. The block/service/component object model is the organizing structure. |
| 6 | Relationship to sensing | Central, alongside actuation. |
| 7 | Relationship to equipment / physical realization | Smart transducers and network-capable processors are the physical context, but the standardized model is not a general equipment lifecycle model. |
| 8 | Physical / logical / functional / operational / informational character | Predominantly logical/functional/informational. |
| 9 | Inside vs outside boundary | NCAP blocks/services/components and interactions are in scope; implementation-specific algorithms are not established as model semantics in the public material. |
| 10 | Composition / hosting / deployment / environment | Object-block composition and interface relationships are central; deployment/environment is not established as a chassis boundary. |
| 11 | Established names | **NCAP** is established but names a processor role, not the whole V2 sensing-equipment family. |
| 12 | Abstraction breadth | Narrow/specialized to smart-transducer network architecture. |
| 13 | Known lineage / alignments | IEEE explicitly identifies this standard as the adoption of IEEE 1451.1-1999. This is therefore not independent conceptual lineage from source 2 even though it is a separate artifact in the corpus. |
| 14 | Comparison to current V2 baseline | **V2 inference:** narrower/partial for the same reason as IEEE 1451.1-1999; useful for a processor/transducer boundary but not a complete `Sensor + Equipment` subject. |
| 15 | Chassis relevance | **V2 inference:** potentially supplemental or too narrow. Its conceptual evidence should not later be double-counted as two independent donor lineages. |

---

## 6. OASIS NIEMOpen — NIEM Model Version 6.0

**Source:** Medlin, Christina, ed. 2025. *NIEM Model Version 6.0*. OASIS Standard.  
**Evidence depth:** Full / source-native official HTML.  
**Primary locator:** https://docs.oasis-open.org/niemopen/niem-model/v6.0/niem-model-v6.0.html

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | A multi-domain data model made of reusable properties and types organized by namespaces/governance authority, intended to support consistent information exchange semantics among exchange partners. |
| 2 | Primary modeled subject | **Information exchange semantics**, not one class of real-world system. |
| 3 | Central / top-level concepts | Model components (properties and types), NIEM Core, Domains, Codes, Adapters, Auxiliary, External, Utility, plus associations/augmentations/roles/representations/references governed by the NDR. |
| 4 | Membership / boundary criteria | Model content is organized by governance source and business semantics. Implementations select the model components needed for a business exchange. |
| 5 | System / asset / device / equipment / platform / component distinctions | Any such distinctions are domain-content choices, not the organizing chassis of NIEM itself. |
| 6 | Relationship to sensing | Sensing is not central to the NIEM Model specification. Sensor/equipment semantics may occur in particular domain schemas but do not define the model. |
| 7 | Relationship to equipment / physical realization | Incidental/domain-specific rather than foundational. |
| 8 | Physical / logical / functional / operational / informational character | Primarily informational and exchange-oriented. |
| 9 | Inside vs outside boundary | Inside are standardized reusable properties/types and related model constructs. Real-world domain boundaries are supplied by the business information being exchanged, not by a single NIEM real-world subject. |
| 10 | Composition / hosting / deployment / environment | Associations, adapters, augmentations, roles, representations, and references support information modeling, but no sensor-equipment deployment boundary is intrinsic. |
| 11 | Established names | NIEM provides many domain concepts, but the top-level **NIEM Model** is not a recognized name for the V2 sensing family. |
| 12 | Abstraction breadth | Intentionally very broad/multi-domain. |
| 13 | Known lineage / alignments | Architecture governed by the NIEM Naming and Design Rules; adapters explicitly support external standards, and domains are managed by authoritative communities. |
| 14 | Comparison to current V2 baseline | **V2 inference:** orthogonal and much broader. NIEM can contribute semantics or mapping patterns but does not answer what `Sensor + Equipment` is as a bounded family. |
| 15 | Chassis relevance | **V2 inference:** cross-cutting / too broad for the chassis question; potentially important later for semantic reuse and exchange mappings. |

---

## 7. MIMOSA — CCOM UML Class Model 4.1.0-RC1 package

**Source:** MIMOSA. *CCOM UML Class Model*. Version 4.1.0 / 4.1.0-RC1 package.  
**Evidence depth:** Full / source-native public release PDF inspected. The official MIMOSA release page identifies 4.1.0-RC1 as a Release Candidate dated 20 March 2020; the V2 bibliography retains its inherited 2018 citation.  
**Primary locator:** https://www.mimosa.org/mimosa-ccom/

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | CCOM is an information model for exchange of **asset lifecycle information** and standards-based interoperability between systems. |
| 2 | Primary modeled subject | Assets and their lifecycle/operational information across registration, configuration, measurement, events, health, work, and related contexts. |
| 3 | Central / top-level concepts | The UML model includes Entity, Asset, AssetType, Model, Segment, Site, Organization, Manufacturer, AssetComponent, SegmentComponent, lifecycle/event classes, measurements/tests/events, and health/prognostic assessments. |
| 4 | Membership / boundary criteria | The modeled frame centers on an identifiable asset and the information required to describe its type/model, composition, placement/segment/site relationships, state, history, assessments, and lifecycle interactions. |
| 5 | System / asset / device / equipment / platform / component distinctions | **Asset** and **AssetType** are explicit. AssetComponent provides parent/child asset composition; Segment/Site provide functional/location context. The model is not sensor-specific. |
| 6 | Relationship to sensing | Sensing is one possible use context. Measurements, tests, events, and assessments are substantial parts of the model, but “being a sensor” is not the defining membership criterion. |
| 7 | Relationship to equipment / physical realization | Strong. The model is explicitly presented by MIMOSA as “Open Standards for Physical Asset Management,” and the registry/configuration model treats assets as lifecycle-managed real-world subjects. |
| 8 | Physical / logical / functional / operational / informational character | Asset/lifecycle information model with strong physical and operational grounding. |
| 9 | Inside vs outside boundary | Asset identity, type/model, composition, configuration/history, measurements, condition/health, and work-related information are modeled. Site/segment/organization supply context around the asset. |
| 10 | Composition / hosting / deployment / environment | AssetComponent and SegmentComponent express composition; Site/Segment and configuration/event structures provide installation/operational context. |
| 11 | Established names | **Asset** is the central recognized term. It is broader than sensing equipment but semantically close to a managed physical-equipment subject. |
| 12 | Abstraction breadth | Broad across physical asset classes and lifecycle concerns; wide enough for motivating systems without being tied to one sensing modality, but broader than sensing. |
| 13 | Known lineage / alignments | CCOM succeeds earlier MIMOSA CRIS/OSA-EAI exchange modeling and is designed for enterprise application integration/asset lifecycle interoperability. |
| 14 | Comparison to current V2 baseline | **V2 inference:** broader than `Sensor` in role but direct on the `Equipment`/whole-lifecycle axis. It carries much more of the “complete operational subject” concern than observation-centric models. |
| 15 | Chassis relevance | **V2 inference:** potentially central and/or supplemental as an asset-lifecycle frame; sensing role would still require another sourced distinction. No relative standing is assigned here. |

---

## 8. Multilateral Interoperability Programme — JC3IEDM Baseline 3.1.4

**Source:** Multilateral Interoperability Programme. 2012. *Joint C3 Information Exchange Data Model (JC3IEDM)*. Baseline 3.1.4.  
**Evidence depth:** Exact-version public overview + official/NATO metadata. The NISP record establishes identity, date, scope, and STANAG adoption. Exact model-structure details below were checked against a public transcription of the v3.1.4 overview; the primary MIP package was not independently obtained in this Phase A pass.  
**Primary locator:** https://nisp.nw3.dk/standard/nato-jc3iedm-3.1.4.html

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | A corporate view of multinational military information exchange for multiple echelons in joint/combined wartime and crisis-response operations, supporting situational awareness, planning, execution, and reporting. |
| 2 | Primary modeled subject | The operational C2 information environment, not sensing equipment specifically. |
| 3 | Central / top-level concepts | The v3.1.4 overview identifies OBJECT-TYPE, OBJECT-ITEM, ACTION, LOCATION, CAPABILITY, CONTEXT, REPORTING-DATA, and related structures. |
| 4 | Membership / boundary criteria | A thing belongs when it is information needed for the C2 exchange model. OBJECT-ITEM/OBJECT-TYPE provide very broad “thing/type” abstractions used across the operational domain. |
| 5 | System / asset / device / equipment / platform / component distinctions | First-level item/type categories include Facility, Feature, Materiel, Organisation, and Person. Equipment appears below Materiel-Type (for example aircraft/electronic/engineering/maritime equipment types), rather than serving as the universal root. |
| 6 | Relationship to sensing | Not defining. Surveillance capability can be represented, but sensing is one operational capability among many. |
| 7 | Relationship to equipment / physical realization | Explicit through Materiel/Equipment and item/type classification, but equipment is one branch of a much larger operational object universe. |
| 8 | Physical / logical / functional / operational / informational character | Strongly operational and informational, with real-world objects, types, actions, locations, capabilities, and statuses represented for C2 exchange. |
| 9 | Inside vs outside boundary | The model intentionally includes a very large portion of the operational battlespace/C2 information domain. A sensing system is one possible OBJECT-ITEM/MATERIEL instance, not the model’s boundary. |
| 10 | Composition / hosting / deployment / environment | Type composition/establishment, item/type classification, location, status, capability, action, and organization structures provide rich operational context. |
| 11 | Established names | OBJECT-ITEM, OBJECT-TYPE, MATERIEL, and EQUIPMENT-TYPE are established within JC3IEDM. The first two are far too generic to name the intended V2 family. |
| 12 | Abstraction breadth | Much broader than V2: people, organizations, facilities, features, materiel, actions, locations, and other C2 information. |
| 13 | Known lineage / alignments | Adopted by NATO STANAG 5525 Edition 1 and used as the data-model core of the MIP interoperability solution. |
| 14 | Comparison to current V2 baseline | **V2 inference:** broader/orthogonal. It can contextualize equipment as an operational object but does not narrow the subject to `Sensor + Equipment`. |
| 15 | Chassis relevance | **V2 inference:** cross-cutting / too broad for the chassis; potentially useful later for operational role, location, capability, and mission context. Evidence ceiling noted above. |

---

## 9. OGC — Abstract Specification Topic 20: Observations, Measurements and Samples 3.0

**Source:** Open Geospatial Consortium. 2023. *Abstract Specification Topic 20—Observations, Measurements and Samples*. Version 3.0.0. OGC 20-082r4.  
**Evidence depth:** Full / source-native official OGC HTML.  
**Primary locator:** https://docs.ogc.org/as/20-082r4/20-082r4.html

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | Conceptual schemas for observations, features involved in the observation process, and features involved in sampling, supporting exchange of observation acts/results and related metadata. |
| 2 | Primary modeled subject | The **observation/sampling process and its information**, not the sensor equipment as a whole. |
| 3 | Central / top-level concepts | Observation, observable property, feature of interest, procedure/observing procedure, observer, result, sample/sampling feature, sampling procedure, sampler, host/deployment and related observation/sampling constructs. |
| 4 | Membership / boundary criteria | Information belongs when it participates in describing an observation or sampling act, its procedure, participants, observed property, target/feature, result, or sample. |
| 5 | System / asset / device / equipment / platform / component distinctions | OMS models Observer/Host/Sampler roles and related features but does not organize the domain around a generic Equipment lifecycle hierarchy. |
| 6 | Relationship to sensing | Central: observing is the core process. |
| 7 | Relationship to equipment / physical realization | Equipment is a possible realization of an observer/host/sampler, but physical realization is not the primary abstraction. |
| 8 | Physical / logical / functional / operational / informational character | Primarily conceptual/informational and functional around acts of observation/sampling. |
| 9 | Inside vs outside boundary | The observation act, its result, target, property, procedure, and participants are in scope. The full operational history/maintenance/configuration of the observing equipment is outside the core boundary unless relevant as observation metadata/context. |
| 10 | Composition / hosting / deployment / environment | Host/deployment and sampling relationships provide context, but equipment composition is not the organizing concern. |
| 11 | Established names | Observation, Observer, Sample, Sampler, Host, Deployment, etc. None alone names the V2 whole-equipment family. |
| 12 | Abstraction breadth | Broad across scientific/technical observation domains but narrow around observation/sampling semantics rather than whole-system information. |
| 13 | Known lineage / alignments | Joint OGC/ISO lineage (ISO 19156:2023) and explicit ongoing harmonization with SSN/SOSA. CSAPI maps OMS observer/host/sampler/procedure concepts into its resources. |
| 14 | Comparison to current V2 baseline | **V2 inference:** partial/orthogonal. It explains what a Sensor/observer does and how observations are structured, but not the whole `Equipment` subject. |
| 15 | Chassis relevance | **V2 inference:** potentially supplemental / cross-cutting, especially for sensing semantics; not a complete equipment chassis by itself. |

---

## 10. OPC Foundation / FieldComm Group — PA-DIM 1.02

**Source:** OPC Foundation and FieldComm Group. 2025. *OPC UA for Process Automation Devices—PA-DIM*. Version 1.02.0. OPC 30081.  
**Evidence depth:** Full / source-native official HTML.  
**Primary locator:** https://reference.opcfoundation.org/specs/OPC-30081/full

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | A protocol- and vendor-independent OPC UA information model for **Process Automation Devices**, supporting their lifecycle and a common information set for interoperability. |
| 2 | Primary modeled subject | The **Process Automation Device**. |
| 3 | Central / top-level concepts | PADIMType, device identity/nameplate data, DeviceHealth/conditions, process values, configuration, diagnostics, SubDevices, and specialized device types such as ProcessAnalyserType. |
| 4 | Membership / boundary criteria | A Process Automation Device is equipment used in industrial automation for measurement tasks (pressure, temperature, flow, level, etc.) or actuator/positioner functions. PA-DIM defines the common device information expected for these device classes. |
| 5 | System / asset / device / equipment / platform / component distinctions | Device is explicit; SubDevices are instances of PADIMType or subtypes. PADIMType specializes the OPC UA Devices model rather than inventing a separate generic asset root. |
| 6 | Relationship to sensing | Central for measurement devices, but sensing is not exclusive because control actuators/positioners are also in scope. |
| 7 | Relationship to equipment / physical realization | Strong and direct: the model concerns industrial automation devices and their product/device information. |
| 8 | Physical / logical / functional / operational / informational character | An information model grounded in physical industrial devices and their lifecycle/operational use. |
| 9 | Inside vs outside boundary | Identification, diagnostics, process values, configuration, conditions, and lifecycle-relevant device information are within the device model. Plant/control systems and cloud applications are external actors/context. |
| 10 | Composition / hosting / deployment / environment | Explicit SubDevices composition. The model sits within industrial automation systems but does not use deployment as the root boundary. |
| 11 | Established names | **Process Automation Device** is a recognized, well-bounded family name. |
| 12 | Abstraction breadth | Semantically strong but industry-specific. It includes both measurement and actuation devices and therefore does not equal the intended heterogeneous sensing family. |
| 13 | Known lineage / alignments | Built as a specialization of OPC UA Part 100 Devices; uses IEC 61987 and ECLASS dictionary identifiers. |
| 14 | Comparison to current V2 baseline | **V2 inference:** narrower by industrial domain, broader by functional role because actuators are peers. Strong direct evidence for how a standards community bounds and describes physical devices. |
| 15 | Chassis relevance | **V2 inference:** potentially central and/or supplemental; the **device** frame is highly relevant, while “Process Automation Device” is too domain-specific as a universal V2 family term. |

---

## 11. OPC Foundation — OPC UA Part 100: Devices 1.05

**Source:** OPC Foundation. 2025. *OPC Unified Architecture Part 100: Devices*. Version 1.05.0. OPC 10000-100.  
**Evidence depth:** Full / source-native official HTML.  
**Primary locator:** https://reference.opcfoundation.org/specs/OPC-10000-100/full

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | A generic OPC UA information model for devices, their components, topology, interfaces, health, identity, functional organization, and companion-specification specialization. |
| 2 | Primary modeled subject | The **Device**, represented by concrete subtypes of the abstract DeviceType. |
| 3 | Central / top-level concepts | TopologyElementType, ComponentType, DeviceType, SoftwareType, ConnectionPoint, FunctionalGroupType, nameplate/support/health interfaces, and component relationships. |
| 4 | Membership / boundary criteria | A concrete DeviceType subtype represents a device. ComponentType is the more general abstract parent; DeviceType and SoftwareType are sibling specializations. |
| 5 | System / asset / device / equipment / platform / component distinctions | **Component** is the abstraction above Device and Software. Device is therefore explicitly distinguished from software while sharing common component semantics. |
| 6 | Relationship to sensing | Not defining. Sensors are represented through device/companion specifications, not by the base DeviceType itself. |
| 7 | Relationship to equipment / physical realization | Strong for DeviceType: the model is explicitly designed to structure device instances with manufacturer/model/serial/hardware revision/asset identifier, health, communication interfaces, etc. |
| 8 | Physical / logical / functional / operational / informational character | Device information model with physical-product grounding and logical/functional organization. |
| 9 | Inside vs outside boundary | Device identity, health, support information, functional groups, protocol support, connection points, and contained components can be inside. External networks are related through ConnectionPoints. |
| 10 | Composition / hosting / deployment / environment | HasComponent and functional grouping support device composition; ConnectionPoints model network interfaces. Deployment is not the fundamental root. |
| 11 | Established names | **Device** is an established generic equipment concept with strong cross-domain recognition. |
| 12 | Abstraction breadth | Broad across device types without becoming as unconstrained as Asset; however, it is not intrinsically limited to sensing. |
| 13 | Known lineage / alignments | Serves as a reusable base for OPC UA companion specifications including PA-DIM. |
| 14 | Comparison to current V2 baseline | **V2 inference:** broad on the `Equipment` axis and orthogonal on `Sensor` role. It may supply an equipment chassis while requiring a separate sensing-role specialization. |
| 15 | Chassis relevance | **V2 inference:** potentially central as a generic device/equipment frame and potentially supplemental for composition/connectivity/health. No ranking is made in Phase A. |

---

## 12. OSUS-R — Asset Interface and Capability Model, pinned revision d09088

**Source:** OSUS-R Contributors. *OSUS-R Asset Interface and Capability Model*. Pinned revision `d09088` as identified in the frozen V2 bibliography.  
**Evidence depth:** Full / source-native pinned source code.  
**Primary locator:** https://github.com/ssg-udri/OSUS-R/tree/d09088fbe56d4b64f0544d72e98c3cb70fa941f6

**Provenance note:** the V2 bibliography cites this artifact as “OSUS-R Contributors. 2026.” The pinned revision itself resolves to commit `d09088fbe56d4b64f0544d72e98c3cb70fa941f6`, dated **22 February 2023**. This Phase A artifact does not rewrite the frozen bibliography citation; it records the source-revision date so later provenance is accurate.

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | A software/runtime model for interacting with OSUS assets, capabilities, observations, commands, status, and communications. |
| 2 | Primary modeled subject | The OSUS **Asset**: the core source code defines it as “a physical device that typically produces data or responds to a command.” |
| 3 | Central / top-level concepts | Asset, AssetProxy, AssetFactory, AssetCapabilities, Observation, Command/Response, activation/deactivation, status, BIT, captureData, sensor identifiers, and communications. |
| 4 | Membership / boundary criteria | The Asset boundary is explicitly a physical device exposed to the OSUS runtime. Examples include motion detector, camera, UAV, security gate, valve actuator, engine, and radio. |
| 5 | System / asset / device / equipment / platform / component distinctions | Asset is explicitly a physical device; one Asset may have multiple sensors. The model therefore distinguishes the whole Asset from sensors within it. |
| 6 | Relationship to sensing | Strong but not exclusive. Asset package documentation calls these assets “(sensors),” captureData returns Observations, and sensor IDs are supported; however, actuator/engine/radio examples show the Asset abstraction is broader than sensing alone. |
| 7 | Relationship to equipment / physical realization | Direct and defining: Asset is a physical device. |
| 8 | Physical / logical / functional / operational / informational character | Physical-device boundary realized through an operational software interface/contract. |
| 9 | Inside vs outside boundary | Activation state, data capture, status, BIT, commands/responses, capabilities, and device protocols are part of Asset behavior. The controller/runtime and communications network are surrounding context/services. |
| 10 | Composition / hosting / deployment / environment | One Asset may have multiple sensors; capture can be directed by sensor ID. Capabilities characterize supported behavior. The core Asset interface is not a generalized deployment model. |
| 11 | Established names | **Asset** is the OSUS-established name for the whole physical device. Its semantics are narrower than the generic AAS “Asset.” |
| 12 | Abstraction breadth | Broad enough for many unattended-sensor and related physical-device cases, yet it includes non-sensing devices and therefore needs role qualification for V2. |
| 13 | Known lineage / alignments | Source-native OSUS-R runtime/interface model. No external standards alignment is inferred from this Phase A review. |
| 14 | Comparison to current V2 baseline | **V2 inference:** direct/partial. Its whole **Asset** closely resembles `Equipment`, while the “may have multiple sensors” distinction demonstrates that the whole equipment can be a sensing subject without every internal element being the top-level Sensor. |
| 15 | Chassis relevance | **V2 inference:** potentially central due to its explicit physical-device boundary and whole-device operational behavior; OSUS-specific implementation semantics must not be mistaken for universal domain truth. |

---

## 13. IETF — RFC 7326 Energy Management Framework

**Source:** Parello, John, Benoît Claise, Brad Schoening, and Juergen Quittek. 2014. *Energy Management Framework*. RFC 7326.  
**Evidence depth:** Full / source-native RFC.  
**Primary locator:** https://www.rfc-editor.org/rfc/rfc7326.html

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | Energy management for devices/components within or connected to communication networks; defines a physical reference model and information model. |
| 2 | Primary modeled subject | The **Energy Object**, an abstract representation of equipment relevant to energy management. |
| 3 | Central / top-level concepts | Energy Object, Device, Component, Power Interface, Energy Management Domain, identity/context, power state, measurements, relationships. |
| 4 | Membership / boundary criteria | An Energy Object is equipment that is part of or attached to a communications network and is monitored/controlled, or aids management of another device, **for Energy Management**. |
| 5 | System / asset / device / equipment / platform / component distinctions | Explicit: Device is a physical piece of equipment; Component is part of a physical piece of equipment; Power Interface is a physical inlet/outlet. |
| 6 | Relationship to sensing | Incidental. Metering/measurement exists, but sensing is not the defining purpose. |
| 7 | Relationship to equipment / physical realization | Direct and explicit. The model distinguishes device, component, and physical power interface. |
| 8 | Physical / logical / functional / operational / informational character | Physical equipment reference model plus information model for energy-management state and measurements. |
| 9 | Inside vs outside boundary | Identity, business/site/organizational context, category, role, power/energy/demand, power states, batteries, and energy relationships are in scope; non-energy device semantics remain external. |
| 10 | Composition / hosting / deployment / environment | Device may contain components; Energy Object relationships include power source, metering, and aggregation; site/deployment context is explicitly represented. |
| 11 | Established names | **Energy Object**, **Device**, **Component**, **Power Interface**. Energy Object is purpose-specific and unsuitable as a general sensing-family name. |
| 12 | Abstraction breadth | Narrow by management purpose despite broad device applicability. |
| 13 | Known lineage / alignments | Part of the IETF EMAN framework and basis for related EMAN MIB work. |
| 14 | Comparison to current V2 baseline | **V2 inference:** partial. Very strong `Equipment`/Component semantics, but energy management rather than sensing defines membership. |
| 15 | Chassis relevance | **V2 inference:** potentially supplemental / too narrow as chassis; valuable for physical Device/Component distinctions and deployment context. |

---

## 14. The Open Group — SOSA Domain-Specific Data Model, Edition 1.0

**Source:** The Open Group. 2022. *Technical Standard for SOSA Reference Architecture, Edition 1.0: SOSA Domain-Specific Data Model*.  
**Evidence depth:** Full / source-native project-provided PDF.  
**Primary evidence locators:** DIV-1 Conceptual Data Model §§1.1.1–1.1.4; Sensor §1.1.3.89; Platform §1.1.3.78; Component_ §1.1.3.15; HostPlatform §1.1.3.54; SensorComponent §1.1.3.92.

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | A SOSA domain-specific data model with DIV-1 conceptual, DIV-2 logical, and DIV-3 physical data-model content. DIV-1 models entities, characteristics, and associations. |
| 2 | Primary modeled subject | The model is organized around the **SOSA Sensor and its supporting subsystem/component/platform environment**, rather than a generic asset universe. The entity-diagram set begins with “General Sensor/Subsystem Installed on a Platform.” |
| 3 | Central / top-level concepts | Sensor, Component_, Platform, HostPlatform, SensorComponent, Controller, Chassis, Product/ProductInstance, Antenna, power/network/configuration/test/fault/state entities and associations, among many others. |
| 4 | Membership / boundary criteria | The Sensor entity is “a SOSA sensor embodying one or more of the SOSA sensor types of radar, SIGINT, EW, communications, and EO/IR.” Components can be explicitly related as parts of a Sensor. |
| 5 | System / asset / device / equipment / platform / component distinctions | Sensor is distinct from **Component_** and **Platform**. Component_ is a physical or software unit with well-defined functional boundaries/purpose/interfaces and is made of hardware/software modules. Platform is a physical entity to which a Sensor is mounted. |
| 6 | Relationship to sensing | Defining and central. |
| 7 | Relationship to equipment / physical realization | Strong. The Sensor has components; Platform is explicitly physical; components may be physical or software; product/product-instance associations connect manufactured products to functional components. |
| 8 | Physical / logical / functional / operational / informational character | Hybrid conceptual model spanning physical, software, functional, operational-state, configuration, health, BIT/fault, network, power, and information concerns. |
| 9 | Inside vs outside boundary | Sensor state/configuration/health and its SensorComponents are intrinsic to the Sensor frame. Platform is modeled as a distinct physical host related through HostPlatform rather than collapsed into the Sensor. |
| 10 | Composition / hosting / deployment / environment | SensorComponent explicitly says a component is part of a Sensor. HostPlatform associates a Sensor with a Platform. Chassis/slot/network/power relations provide additional physical hosting structure. |
| 11 | Established names | **Sensor** is the explicit whole modeled subject; **Platform** and **Component** are distinct supporting concepts. |
| 12 | Abstraction breadth | Strong for defense sensor systems but its enumerated SOSA sensor types (radar, SIGINT, EW, communications, EO/IR) make the source’s direct domain narrower than all heterogeneous sensing equipment. |
| 13 | Known lineage / alignments | Native data model of the SOSA Reference Architecture. This source is distinct from the W3C/OGC SOSA/SSN ontology despite the acronym overlap and must not be conflated with it. |
| 14 | Comparison to current V2 baseline | **V2 inference:** direct on the `Sensor` axis and compatible with the whole-system intent because Sensor itself carries health, operational, and configuration state and can contain Components. It does not express the current CSAPI `assetType = Equipment` facet directly. |
| 15 | Chassis relevance | **V2 inference:** potentially central because it explicitly treats **Sensor** as the whole operational subject, with Components and a separate physical Platform; domain breadth must later be tested. No ranking is made in Phase A. |

---

## 15. W3C — PROV-DM

**Source:** World Wide Web Consortium. 2013. *PROV-DM: The PROV Data Model*. W3C Recommendation.  
**Evidence depth:** Full / source-native official W3C Recommendation.  
**Primary locator:** https://www.w3.org/TR/prov-dm/

| # | Extraction question | Independent extraction |
|---|---|---|
| 1 | Source scope / universe of discourse | A generic data model for provenance that allows domain/application-specific provenance to be translated and exchanged among heterogeneous systems. |
| 2 | Primary modeled subject | **Provenance**, not an equipment/system family. |
| 3 | Central / top-level concepts | Entity, Activity, Agent; generation/use; derivation; attribution/association/delegation; bundles; alternate/specialization; collections. |
| 4 | Membership / boundary criteria | Anything participates insofar as its provenance is being described. Entity is deliberately generic. |
| 5 | System / asset / device / equipment / platform / component distinctions | None are intrinsic to the PROV chassis; a system/device could be modeled as an Entity or Agent only in a provenance role. |
| 6 | Relationship to sensing | Absent as a domain-defining concern. |
| 7 | Relationship to equipment / physical realization | Not intrinsic. Physical equipment may be represented generically when provenance requires it. |
| 8 | Physical / logical / functional / operational / informational character | Purely cross-domain informational/provenance semantics. |
| 9 | Inside vs outside boundary | Provenance relations and the entities/activities/agents participating in them are in scope; the full intrinsic domain model of those things remains external. |
| 10 | Composition / hosting / deployment / environment | Bundles and collections structure provenance information, not physical equipment composition/deployment. |
| 11 | Established names | Entity/Activity/Agent are established provenance concepts but far too generic to name V2’s family. |
| 12 | Abstraction breadth | Deliberately universal. |
| 13 | Known lineage / alignments | Core member of the W3C PROV family, with companion ontology/constraints/notation specifications. |
| 14 | Comparison to current V2 baseline | **V2 inference:** orthogonal. PROV can describe provenance of `System/Sensor/Equipment` information but does not define those concepts. |
| 15 | Chassis relevance | **V2 inference:** cross-cutting / not applicable as a chassis source; potentially important later for the V2 provenance objective. |

---

## 16. Phase A completion gate

All fourteen Conceptual / Information / Domain Model artifacts in the frozen source-type audit have now received an independent extraction under the same fifteen questions. Phase A therefore satisfies the PITON gate for moving to cross-source comparison.

This document intentionally stops before:
- ranking any donor;
- selecting a chassis;
- creating a new umbrella class;
- changing the current `Sensor + Equipment` comparison baseline;
- editing the clean V2 DIM/Profile working artifact; or
- treating conceptual reuse as donor-standard conformance.

The next permitted step is **Phase B — cross-source comparison**, followed only then by Phase C source standing and the Phase D chassis synthesis gate.
