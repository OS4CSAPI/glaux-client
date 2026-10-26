# Sensor Systems Domain Information Model and Application Profile

## Version 2 Working Draft

**Working draft v0.1 — 25 October 2026**  
**Working title:** “Sensor Systems” is descriptive working wording; no additional boundary-defining model class/name is currently required.  
**Standing:** Clean V2 artifact; contains only established working decisions and explicitly identified candidates/open items.

## 1. Purpose and standing

This document is the clean Version 2 working artifact for the Domain Information Model (DIM) and the application profile that will ultimately use it. It is intended to become the self-describing statement of what Version 2 is, what problem it addresses, what concepts it adopts, how those concepts are organized, and how the resulting model is later selected and realized through the application profile and OGC binding. This first draft contains only conclusions that have been sufficiently established by the Version 2 research to date. It deliberately does not fill unresolved sections with provisional design simply to make the document appear complete.

The working title uses the plain-language phrase “Sensor Systems” to identify the subject matter; it does not introduce a new compound class. The completed Version 2 chassis study has now established the working domain boundary without finding a superior single umbrella term: Version 2 concerns **physically realized equipment Systems whose defining operational role is sensing/observing, modeled as complete operational subjects**. In the intended CSAPI environment, the most direct present characterization is `systemType = Sensor` together with `assetType = Equipment` (Open Geospatial Consortium 2025a, sec. 9.2.2). This two-facet characterization is now a working boundary decision rather than merely a pre-study candidate. The eventual formal ontology mapping remains a separate question; a CSAPI Sensor classification must not be treated automatically as an OWL class assertion.

Version 2 is not coupled to MERLIN as a formal model or profile identity. MERLIN-era artifacts remain predecessor evidence because they record the original problem, donor research, implementation experience, and Version 1 design choices. They do not automatically determine Version 2 terminology, scope, relationships, modular structure, namespace, or profile obligations.

## 2. Objectives and design principles

The Version 2 effort adopts outcome-oriented objectives that can be used to judge the quality of whatever DIM/Profile structure ultimately emerges. These objectives deliberately do **not** carry forward the Version 1 eight information subjects, R01–R20 relationships, donor preferences, or former domain name as design requirements. They preserve the generally applicable interoperability principles demonstrated by the predecessor work while allowing the Version 2 model to be derived independently from the source evidence.

**Overarching objective.** Develop a standards-grounded Domain Information Model and CSAPI application profile that enable heterogeneous sensing systems to be represented, integrated, discovered, understood, and used through a common OGC framework while preserving the meaning, provenance, and distinctions of their source information.

### 2.1 Model the system as a complete operational subject

Version 2 should represent enough information to understand the sensing system itself rather than only the observations that it produces. The required information structure must emerge from the source evidence; this objective does not prescribe the eight Version 1 information subjects or any other predetermined partition.

### 2.2 Preserve donor semantics through integration

When Version 2 adopts, aligns with, or deliberately reuses a concept, relationship, vocabulary, or constraint from a documented donor source, an implementation conforming to that donor should be able to map the corresponding native information into the Version 2 representation without semantic reinvention. Any transformation, qualification, partial correspondence, information loss, unavailable content, or source-specific extension must remain explicit rather than being hidden by normalization.

Donor conformance does **not** imply conformance to the Version 2 profile as a whole, and Version 2 does not require implementations to natively implement every donor standard.

### 2.3 Enable cross-source interoperability and common interpretation

Where heterogeneous source systems express overlapping meaning, Version 2 should enable that meaning to converge on common OGC representations that can be discovered and interpreted consistently by a common client. Consistency does not require every source datum to become identical or every source-specific distinction to disappear.

### 2.4 Reuse established semantics before authoring new ones

Version 2 should prefer applicable authoritative concepts, relationships, vocabularies, and native OGC mechanisms before creating project-owned alternatives. New Version 2 semantics or constraints should be introduced only when the research demonstrates a real interoperability gap and the proposed addition has a clear, proportionate purpose.

### 2.5 Preserve provenance and semantic fidelity

Reused or translated information should remain traceable to its source standard or model, relevant edition, native identity where applicable, and consequential transformations. Normalization must not hide distinctions in subject, context, time, reference frame, cardinality, qualification, or meaning that are material to correct interpretation.

### 2.6 Keep the DIM purpose-driven but binding-independent

The known goal of producing a CSAPI application profile may determine which interoperability questions the DIM must answer, but CSAPI field placement, encoding mechanics, software architecture, and implementation convenience must not define domain truth. The DIM establishes meaning; the profile selects and constrains that meaning for a particular interoperability purpose; the OGC binding specifies its representation.

### 2.7 Support progressive compatibility

Version 2 should preserve useful access at multiple levels where the underlying standards permit it. Generic OGC/feature clients should retain the base-standard access they support, CSAPI/SensorML-aware clients should be able to use richer native content, and profile-aware clients should be able to recognize and apply the additional Version 2 contract. Profile awareness should add capability without unnecessarily breaking base-standard interoperability.

### 2.8 Make conformance claims precise and testable

Version 2 must distinguish conceptual reuse, semantic mapping or translation, application-profile conformance, OGC-standard conformance, and native implementation of an external donor standard. Every normative Version 2 obligation should have an identifiable conformance target, clear requirements or constraints, and an assessable means of determining compliance.

### 2.9 Remain reusable, extensible, and grounded in real systems

Genuinely common semantics should be structured so they can be reused by future specializations without weakening the needs of the present domain. Version 2 should be challenged against real systems and realistic integration cases so that theoretical elegance does not outrun operational usefulness. Reuse should follow the principle **reuse invariants; specialize variation**.

Two synthesis rules apply across these objectives:

- **Every donor is allowed to challenge the emerging Version 2 model.** Donor review must not be performed merely to validate choices already made.
- **Version 2 should own only the semantics and constraints that no suitable adopted source already owns.** Local authorship must be visible and justified.

A recurring acceptance question for donor-derived content is therefore: **If a conforming implementation of the donor standard arrived with the corresponding native information, could Version 2 map that information faithfully and recognizably?** A negative answer requires the project to explain whether the problem lies in the donor mapping, the Version 2 abstraction, the binding, or an intentional and documented difference.

## 3. What this document contains

Version 2 separates four related but distinct artifacts: the Domain Information Model, the application profile, the OGC binding, and software implementations. Keeping these responsibilities separate is necessary to prevent domain meaning from being confused with a particular API field, encoding, or user interface. The separation follows established information-modeling practice in which conceptual information models are independent of lower-level data models and protocol realizations (Pras and Schoenwaelder 2003, secs. 2–4).

| Artifact | Question answered | Current standing |
| --- | --- | --- |
| Domain Information Model | What concepts and relationships exist in the domain, and what do they mean? | This draft begins that artifact. |
| Application profile | Which DIM content and additional interoperability obligations apply for this purpose? | Intended; substantive obligations not yet defined. |
| OGC binding | How are selected DIM/profile meanings represented in CSAPI, SensorML, SWE Common, and related standards? | Intended; concrete binding rules not yet defined. |
| Implementation | How do servers, adapters, clients, validators, and UIs produce, consume, validate, and present the representations? | Outside the DIM; not specified here. |

Figure 1 summarizes the relationship among these artifacts, including the intentional feedback from profile requirements into the domain questions that the DIM must answer.

![Figure 1. V2 Artifact Architecture](Figures/Figure_1_V2_Artifact_Architecture.svg)

**Figure 1. V2 Artifact Architecture.** The DIM establishes domain meaning and supplies semantics to the application profile. Profile requirements identify the domain questions the DIM must be able to answer, while the profile selects and constrains DIM content for a specific interoperability purpose. The OGC binding expresses those selected meanings using CSAPI, SensorML, SWE Common, and related mechanisms, and implementations realize the binding in concrete software.

## 4. Domain Information Model

For Version 2, a Domain Information Model is an implementation- and protocol-independent model of the common concepts, entities, relationships, and intrinsic semantic constraints needed to describe and understand a defined problem domain. This use of DIM is not project-invented terminology. ISO/IEEE 11073-10201 defines a Domain Information Model for a bounded medical-device interoperability domain, while RFC 3444 distinguishes an implementation-independent information model from the lower-level data models and protocol details that realize it (ISO and IEEE 2020; Pras and Schoenwaelder 2003). OGC similarly treats a conceptual model as an implementation-independent representation of the important concepts of a domain and recommends platform-independent conceptual modeling (Open Geospatial Consortium 2021).

The Version 2 DIM therefore exists to establish domain meaning before implementation representation. It may contain concepts, definitions, generalization and specialization, relationships and relationship roles, identity distinctions, states, lifecycle concepts, activities, temporal or spatial relationships, and intrinsic semantic constraints where the evidence supports them. It does not contain CSAPI endpoint paths, JSON member placement, SensorML or SWE encoding choices, HTTP behavior, software architecture, or user-interface behavior merely because those mechanisms may later carry or present the model.

The DIM is domain-scoped rather than universal. Its present purpose is to organize the information needed to understand a deployed sensing System as a complete operational subject. The chassis study described in Section 6 has now established the working domain boundary; detailed model structure, modules, donor ownership, formal ontology mappings, and application-profile obligations remain open research questions.

## 5. Relationship to the intended application profile

The DIM is being developed because Version 2 is intended to support a CSAPI application profile, and the research should not pretend otherwise. Established domain-modeling practice begins from real information requirements and use cases; NIEM, for example, directs modelers to map actual information requirements to existing concepts, identify gaps, and create new content only where existing content is insufficient (NIEM 2016). A concrete interoperability purpose may therefore determine which questions the DIM must be capable of answering.

The governing Version 2 principle is **purpose-driven but binding-independent: model for the profile, not to the profile**. The intended profile may reveal which domain distinctions matter and what information requires coherent meaning, but it must not turn CSAPI representation mechanics or implementation convenience into domain facts. The application profile will later select and constrain the DIM content that participating implementations agree to support for a specific interoperability purpose, while the OGC binding will specify how those selected meanings are represented through CSAPI, SensorML, SWE Common, and any other selected standards.

The relationship is therefore reciprocal but responsibility-preserving: profile requirements identify questions that the DIM must answer, while the DIM supplies the semantics that the profile selects and constrains. A concept may belong in the DIM even when a particular profile does not require it, and a profile obligation may exist even when it is not an intrinsic truth about the domain.

## 6. Domain boundary and anchor concepts

The boundary of the domain and the root or anchor concept of the model are separate questions. A domain is a bounded universe of discourse or problem space; it does not require the project to invent a single umbrella class merely to give the model a visually tidy root (Open Geospatial Consortium 2021).

The Version 2 chassis study independently characterized all fourteen Conceptual / Information / Domain Model artifacts in the frozen corpus, compared them only after independent extraction, and then tested the resulting candidate against the Ontology / Formal Semantic Model, Reference Architecture / Architectural Framework, and Requirements / Capability / Operational Specification groups. The candidate survived all required validation gates.

The resulting working boundary is:

> **Version 2 concerns physically realized equipment Systems whose defining operational role is sensing/observing, modeled as complete operational subjects.**

This is a boundary statement composed from established source concepts, not a new Version 2-owned class. The evidence did not identify a single donor noun that more faithfully captures both the functional role and the physical realization. **Asset** is too semantically variable across communities; **Device** is a strong physical-equipment concept but functionally neutral and can be too narrow for composite installations; **Thing** is deliberately physical-or-virtual and domain-neutral; **Sensor Network** names a larger aggregate; and observation-process concepts describe what sensing does rather than the enduring equipment subject.

The strongest recurring pattern is instead a separation between **what the System principally does** and **what kind of thing realizes that role**. The intended CSAPI representation expresses those dimensions directly as `systemType = Sensor` and `assetType = Equipment`. This combination is therefore the working V2 chassis characterization. No new compound/root class is adopted.

The realization facet is deliberately **Equipment**, not a requirement that one System equal one physical Device. The Open Group SOSA architecture provides direct precedent for one Sensor consisting of one or more hardware elements, including elements distributed at different locations on or in the same host platform (The Open Group 2023). Operational radiation-detection sources likewise include fixed and installed systems composed of multiple detector and supporting elements. A V2 sensing System may therefore be composite equipment while remaining one enduring operational subject.

The chassis is a bounding condition for later modeling, not a predetermined module taxonomy. It determines the kind of thing whose information Version 2 is organizing; it does not decide in advance how identity, capability, deployment, communications, power, condition, lifecycle, provenance, or other evidence-derived concerns will be partitioned.

## 7. Current sourced conceptual foundation

The sourced foundation comes principally from SOSA/SSN, OGC API – Connected Systems Part 1, SensorML 3.0, and the donor evidence examined through the chassis study. In the current SOSA/SSN 2023 Edition Working Draft, Asset generalizes System and Platform; Sensor, Actuator, and Sampler are specializations of System, while Platform is separately an Asset that hosts other Assets (World Wide Web Consortium and Open Geospatial Consortium 2026, secs. 5.3.5, 5.4–5.6). Sensor denotes a System that implements an ObservingProcedure and does not by itself imply hardware, because a Sensor may be realized by a device, infrastructure, human agent, software system, or simulation.

CSAPI Part 1 provides two independent System-classification facets. `systemType` identifies the System’s principal role or activity using Sensor, Actuator, Sampler, Platform, or System, while optional `assetType` identifies the kind of realization using Equipment, Human, LivingThing, Simulation, Process, Group, or Other (Open Geospatial Consortium 2025a, sec. 9.2.2). CSAPI demonstrates that these facets are independent by combining them in examples such as Sensor + Equipment, Sensor + Human, Sensor + Simulation, and Platform + Equipment.

The completed chassis study independently corroborates the need to keep these dimensions distinguishable. The Open Group SOSA treats Sensor as a whole operational subject composed of heterogeneous components; OPC UA Devices, MIMOSA CCOM, OSUS-R, RFC 7326, NIST IoT guidance, and radiation-detection sources independently reinforce the physical device/equipment side; SAREF narrows Sensor to a tangible Device; and SWEET provides an explicit intersection pattern in which Sensor is both a SOSA Sensor and an Instrument under Equipment. No single donor encoding is therefore treated as the universal class structure.

A formal semantic caution follows from that result. In current SOSA/SSN, a complex package can be modeled as an overall `sosa:System` containing `sosa:Sensor` subsystems, whereas CSAPI `systemType = Sensor` classifies a represented System by its principal activity. **Version 2 must not automatically equate the CSAPI classification token with an RDF/OWL assertion that the resource is an instance of `sosa:Sensor`.** The eventual semantic alignment must state that mapping explicitly.

| Concept | Current V2 standing |
| --- | --- |
| System | Sourced conceptual foundation and top-level system abstraction. |
| Sensor | Sourced sensing/observing role; establishes the defining domain role but does not alone guarantee physical realization across donor communities. |
| Equipment | **Working V2 physical-realization boundary** for the present domain. May represent composite equipment rather than a single Device. |
| Sensor + Equipment | **Working V2 chassis characterization** in the intended CSAPI environment; not a newly named class. |
| Device | Important donor mapping/comparison concept for physical equipment; not adopted as the universal V2 root. |
| Asset | Useful sourced superconcept/mapping concept whose breadth varies by donor; not sufficient alone to define V2 membership. |
| Platform | Separate sourced host/context concept; physical hosting does not automatically make the Platform intrinsic to the Sensor/System. |
| Deployment | Sourced operational context for employment and for time-scoped aggregation/attachment. |
| Sensor Network / aggregation | Larger multi-system context; not automatically one V2 sensing System. |

## 8. Whole-system scope

Whole system is an informational scope statement, not a taxonomic enlargement. It means that a user should be able to access, understand, and manage the sensing System as a complete operational subject rather than only retrieve the observations that it produces. Identity, technical description, configuration, components, capabilities, telemetry, deployment context, communications, power, condition, management interactions, service and lifecycle history, provenance, observations, products, and related supported information may therefore belong to the model without changing the top-level subject into a system-of-systems or enterprise construct.

SensorML 3.0 supports this interpretation by describing physical sensor systems whose overall application is sensing even though their internal composition may contain sensing, actuation, computation, and other subprocesses (Open Geospatial Consortium 2025b, secs. 8.5–8.6). The Open Group SOSA architecture independently treats the Sensor as a whole subject containing hardware, firmware, software, processing, run-time, communications, power, management, and other supporting components (The Open Group 2023).

A whole sensing System does not have to be one box, one detector, or one Device. It may contain multiple sensing elements and heterogeneous non-sensing components, and its physical hardware may be distributed within an enduring System boundary. Nor must every capability be observational: commands, actuation/effecting, processing, configuration, communications, health monitoring, BIT, diagnostics, and management behavior can coexist with a sensing identity when sensing/observing remains the defining operational role of the whole System.

The model should therefore classify the System by the sourced semantics of the whole operational subject rather than infer a broader category merely because its internal functions are heterogeneous. Conversely, a set of cooperating sensing resources, a sensor network, or a deployment aggregation is not automatically one System; evidence of an enduring common System identity and composition boundary is required before those resources are collapsed into one subject.

## 9. Composition, hosting, and deployment-scoped attachment

Version 2 must preserve the distinction exposed by CSAPI between Composition and Aggregation. Composition applies when a subsystem is an integral or ordinarily enduring part of its parent, even if maintenance can physically remove it. Aggregation applies when a subsystem is not permanently attached and can be associated with different parent Systems at different times; CSAPI represents that relationship through Deployment (Open Geospatial Consortium 2025a, sec. 10.2). A cable, connector, mounting rail, or other physical attachment mechanism is not by itself the deciding criterion.

The chassis study adds a second boundary distinction: **host Platform is not the same as intrinsic composition**. The Open Group SOSA architecture explicitly separates the Sensor from the physical Host Platform to which it is mounted and provides a Host Platform Interface across that boundary (The Open Group 2023). A vehicle, structure, building, mast, pod, or other host therefore does not become part of the sensing System merely because it carries, powers, connects to, or deploys it. A particular implementation may establish a tighter enduring composition relationship, but that must be supported by source evidence rather than inferred from physical proximity.

These findings illustrate how binding and architecture standards can legitimately contribute semantics to an implementation-independent DIM. The enduring-versus-deployment-scoped distinction and the intrinsic-component-versus-host-context distinction may prove to be domain relationships worth preserving, while `/subsystems`, Deployment resources, concrete interface links, and other carriers remain binding mechanisms. Version 2 should preserve useful domain distinctions revealed by implementation standards without making their API or architecture carrier identical to the concept itself.

## 10. Model organization and modularity

Version 2 may be modular, and established information-modeling practice supports modular organization where semantic cohesion justifies it. DMTF’s Common Information Model separates core, common, and extension content; TM Forum partitions its information model into domains and Aggregate Business Entities; NIEM promotes reuse of existing components and creation of new content only where demonstrated requirements expose gaps (DMTF 2010; NIEM 2016; TM Forum 2026). These precedents support modularity as a design principle without prescribing a particular module taxonomy for this domain.

A candidate subject area should be promoted to a reusable module or subdomain only when the evidence shows strong internal semantic cohesion, meaningful concepts and relationships of its own, bounded dependencies, plausible applicability across more than one specialization, and a substantial source or standards lineage. A document heading does not create a module, and the word subdomain should not be applied merely because a topic is important. The architecture should be derived from semantic evidence rather than from the presentation structure of Version 1.

The governing reuse policy is **reuse invariants; specialize variation**. Concepts should be shared only when their meaning genuinely survives across the relevant system families. Realization-specific concepts should remain specific even when that reduces superficial reuse. Version 2 should optimize first for semantic correctness of the demonstrated sensor-system domain and preserve future reuse where the semantics themselves justify it.

## 11. Standing of the Version 1 information subjects

Version 1 organized its whole-system problem into eight recurring information subjects. They remain useful predecessor evidence because they record the clusters of information that emerged when Version 1 attempted to describe an employed sensing system comprehensively. Version 2 has not adopted them as eight subdomains, modules, or “sub-DIMs,” and their architectural status must be re-evaluated through the controlled donor-review process.

1. identity / model / technical description
2. equipment / composition / physical arrangement
3. sensing capabilities / performance / outputs
4. deployment / emplacement / location / responsibility
5. operating configuration / modes / actions
6. communications / connectivity / access
7. power sources / operating arrangement
8. condition / service / recovery / lifecycle

These are **candidate subject areas to test**, not inherited V2 modules. Different subjects may ultimately resolve to core semantics, reusable modules, cross-cutting relationships, specializations, or a different partition altogether.

## 12. Current decisions and open questions

The following table records the present standing of the Version 2 work. A working decision controls the methodology unless later evidence overturns it; a candidate is supported enough to test but is not final; and an open item must not be resolved silently by implementation convenience or by carrying forward a Version 1 term.

| Topic | Standing | Current result |
| --- | --- | --- |
| DIM terminology | Working decision | Retain Domain Information Model as the methodological anchor. |
| DIM abstraction level | Working decision | Domain-scoped, conceptual, implementation- and protocol-independent. |
| Relationship to CSAPI profile | Working decision | Purpose-driven but binding-independent; model for the profile, not to the profile. |
| Whole-system meaning | Working decision | Informational completeness about the sensing System; heterogeneous components/functions do not make it automatically a system-of-systems. |
| Domain boundary vs root concept | Working decision | Treat as separate questions. |
| Chassis / domain boundary | **Working decision** | Physically realized equipment Systems whose defining operational role is sensing/observing, modeled as complete operational subjects. |
| CSAPI chassis characterization | **Working decision** | `systemType = Sensor` + `assetType = Equipment` for the intended hardware sensing domain. |
| New compound/root class | **Working decision — not required** | Do not coin one; the two sourced dimensions are sufficient at the chassis level. |
| Equipment vs Device | **Working decision** | Retain Equipment as the realization facet; one System may be composite equipment spanning multiple hardware elements. |
| Host Platform boundary | **Working decision** | Hosting/mounting does not automatically make the Platform part of the Sensor/System. |
| Network/aggregation boundary | **Working decision** | Cooperating Systems or a sensor network are not automatically one sensing System. |
| CSAPI Sensor vs `sosa:Sensor` assertion | Open mapping question | Do not equate classification and OWL class assertion without an explicit semantic mapping. |
| Composition vs Aggregation | Working decision | Preserve enduring vs deployment-scoped relationship distinction. |
| Modularity | Working decision | Use where semantic cohesion and bounded reuse justify it. |
| V1 eight subjects | Candidate evidence | Treat as subject areas to test, not inherited modules/subdomains. |
| Boundary-defining family term | Working decision | No additional umbrella term/class is required; “Sensor Systems” remains descriptive wording rather than a new model class. |
| Final modules/subdomains | Open | Derive through broader donor review and synthesis under the earned chassis boundary. |
| Visualization work | Paused / non-gating | Figure work does not gate substantive research unless explicitly resumed. |
| Chassis study | Complete | CIDM extraction/synthesis plus ontology, architecture, and requirements validation completed. |

## 13. Development sequence

The chassis question is now closed as a working Version 2 decision. The dedicated evidence chain consists of the fourteen-source independent extraction, cross-source comparison and synthesis, ontology validation, architecture validation, requirements/operational validation, and the cross-group chassis decision record. Those research artifacts preserve the full evidence and cautions; this clean artifact retains only the earned result.

The next substantive workstream returns from the narrow chassis study to the broader frozen donor corpus. The earned chassis is a **bounding condition**, not a module taxonomy: donor analysis must now determine what recurring concepts, relationships, constraints, and semantically cohesive subject areas are actually needed to describe that bounded class of sensing Systems. Sources should continue to be understood first according to what they themselves standardize—ontology, information model, architecture, vocabulary, schema, API, requirements, conformance method, or operational evidence—rather than being forced into Version 1 headings.

Individual donor reviews still do not edit the DIM directly. Evidence is extracted independently, compared under common criteria, and promoted only at explicit synthesis gates. The Version 1 eight information subjects remain predecessor evidence and useful challenge material, not bins into which new evidence is sorted by default.

Visualization work remains paused and non-gating. It should resume only when a substantive modeling decision requires a maintained diagram and a canonical rendering source can be used consistently across GitHub and publication formats.

As later modeling proceeds, every proposed concept should be tested against the chassis boundary: **Is this information intrinsic to understanding the complete physically realized sensing System, a relationship to its context, an interaction/output, or a concern that belongs outside the DIM or only in a specialization/profile?** This keeps the newly established boundary from becoming an excuse for indiscriminate whole-world modeling.

## 14. References

DMTF (Distributed Management Task Force). 2010. *Common Information Model (CIM) Infrastructure*. DSP0004, version 2.6. https://www.dmtf.org/sites/default/files/standards/documents/DSP0004_2.6.pdf.

ISO and IEEE. 2020. *Health Informatics—Device Interoperability—Part 10201: Point-of-Care Medical Device Communication—Domain Information Model*. ISO/IEEE 11073-10201:2020. https://www.iso.org/standard/77339.html.

NIEM. 2016. *Introduction to Domain Modeling*. August 24. https://reference.niem.gov/niem/guidance/dmg/technical/domain-modeling-guide/content.html.

Open Geospatial Consortium. 2021. *OGC Testbed-17: UML Modeling Best Practice Engineering Report*. OGC 21-031. https://docs.ogc.org/per/21-031.html.

Open Geospatial Consortium. 2025a. *OGC API – Connected Systems – Part 1: Feature Resources*. OGC 23-001, version 1.0. July 16. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC SensorML Encoding Standard*. OGC 23-000, version 3.0. July 16. https://docs.ogc.org/is/23-000/23-000.html.

Pras, Aiko, and Jürgen Schönwälder. 2003. “On the Difference between Information Models and Data Models.” RFC 3444. January. https://www.rfc-editor.org/rfc/rfc3444.html.

TM Forum. 2026. “Information Framework (SID).” Accessed October 25, 2026. https://www.tmforum.org/oda/information-systems/information-framework-%28sid%29/.

The Open Group. 2023. *Technical Standard for SOSA™ Reference Architecture, Edition 1.1*. C239. June 28. https://publications.opengroup.org/c239.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology – 2023 Edition*. W3C Working Draft, October 21. OGC 25-022. https://www.w3.org/TR/vocab-ssn-2023/.
