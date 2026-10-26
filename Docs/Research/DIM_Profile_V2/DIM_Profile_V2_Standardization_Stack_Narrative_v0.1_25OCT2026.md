# DIM/Profile V2 Standardization Stack Narrative

**Working draft v0.1 — 25 October 2026**  
**Standing:** Standalone research interpretation of the frozen 182-source V2 corpus. This document does not define the V2 DIM, profile, modules, or donor rankings.

## 1. Purpose

The V2 donor corpus contains many different kinds of standards artifacts. They are not interchangeable, and they should not be evaluated as though every source were competing to define the same thing. An ontology, an information model, a reference architecture, a data schema, an API, a profile, and a conformance specification standardize different aspects of information technology. Their value emerges partly from the distinctions among those roles and partly from the way those roles can be composed into a coherent interoperability framework.

The purpose of this narrative is to explain that standardization stack before substantive donor comparison begins. The analysis starts from the source types represented in the frozen 182-source bibliography rather than from the Version 1 DIM structure. The presence of a source type establishes that the V2 evidence base is capable of informing that kind of standardization problem; it does **not** establish that V2 must produce a corresponding artifact. The stack therefore describes a possibility envelope for the resulting work, not a predetermined product list.

## 2. Why information-technology standards occur at different layers

Information technology is too complex to standardize effectively through one artifact type. Different standards communities therefore separate concerns by abstraction level and purpose. RFC 3444 makes one of the clearest distinctions: an information model describes managed concepts and relationships at a conceptual and protocol-independent level, while lower-level data models add representation and implementation detail; multiple data models can derive from one information model (Pras and Schoenwaelder 2003). This distinction is representative of a broader pattern visible throughout the V2 corpus: standards stabilize meaning first, then progressively constrain organization, representation, interaction, and verification.

The layers are not a strict waterfall. A reference architecture may expose concepts that influence an information model; an API standard may identify a semantic distinction that the conceptual model should preserve; an ontology may formalize concepts that originally appeared in an information model; a profile may reveal that the base model lacks a distinction required by a real interoperability use case. The important point is not that one layer always precedes another, but that each type of artifact has a different primary authority. V2 should reuse that authority rather than ask every donor to answer every question.

## 3. Semantic foundation: ontologies, vocabularies, terminology, units, and registries

Ontologies and formal semantic models standardize machine-interpretable meaning. They define classes, properties, relationships, and, where appropriate, axioms that allow concepts to be interpreted consistently and related formally. The SOSA/SSN ontology, for example, defines a semantic model for systems, sensors, actuators, samplers, procedures, observations, actuations, sampling, properties, deployments, and associated relationships (World Wide Web Consortium and Open Geospatial Consortium 2026). Formal semantic sources can therefore contribute more than terminology: they can establish distinctions, inheritance, property domains and ranges, and explicit alignments to other models.

Terminologies, controlled vocabularies, units systems, code lists, and registries perform a different but complementary job. They stabilize the values and identifiers used within models. QUDT separates schema graphs from vocabulary graphs for units, quantity kinds, dimension vectors, and related concepts, illustrating how a shared semantic framework can standardize both the structure of quantitative information and the controlled identifiers used to express it (QUDT.org 2026). UCUM, VIM, IANA registries, NIEM code lists, and similar sources likewise reduce ambiguity without necessarily defining the entire domain model in which those terms are used.

Together, these source types can support a semantic foundation for V2: authoritative definitions, identifiers, quantities, units, code spaces, and machine-recognizable relationships. Their presence does not require V2 to publish a new ontology or vocabulary. They give V2 the option to reuse existing semantic assets, map to them explicitly, and author new semantic identifiers only where a genuine gap remains.

## 4. Conceptual foundation: information, domain, and conceptual models

Conceptual, information, and domain models answer a different question: **what things and relationships matter in the problem domain?** Their primary job is to organize concepts at an implementation-independent level. RFC 3444 emphasizes that information models are protocol-neutral and relationship-oriented, providing a conceptual basis from which one or more implementation-oriented data models may be derived (Pras and Schoenwaelder 2003).

This source type is the most direct evidence base for the V2 Domain Information Model. It can contribute candidate entities, distinctions, relationships, identity rules, state concepts, temporal relationships, intrinsic constraints, and domain boundaries. However, V2 should not simply select one donor information model and rename it. The corpus contains multiple information and domain models created for different communities and scopes. Their value lies in comparison: recurring concepts may reveal stable domain structure, incompatible distinctions may expose genuine alternative views, and gaps across all models may identify the limited areas where V2 must author new semantics.

The DIM is therefore the conceptual center of the potential V2 stack, but it is not the entire stack. It gives meaning to later profile and binding work while remaining independent of any one serialization, API endpoint, programming language, or implementation.

## 5. System context: reference architectures and requirements specifications

Reference architectures standardize the organization and context of systems. They typically define roles, components, viewpoints, responsibilities, boundaries, interfaces, and relationships among architectural elements. W3C's Web of Things Architecture illustrates the role clearly: it derives an abstract architecture from cross-domain requirements, identifies modular building blocks, and describes how those building blocks relate while allowing multiple concrete deployment scenarios (World Wide Web Consortium 2023). The V2 corpus contains several architecture families that can similarly expose distinctions that a pure domain model may overlook.

Requirements, capability, and operational specifications focus on expected behavior, performance, functions, or obligations. They can reveal what information must be representable because a system is expected to declare a capability, accept a control, report status, meet a performance bound, or participate in a defined operational pattern. These requirements should not automatically become DIM semantics. They are evidence about the operational questions the DIM and profile may need to answer.

Architectures and requirements therefore act as scope and completeness checks. They can challenge the DIM by asking whether the conceptual model can describe the roles, capabilities, states, and relationships that real systems and interoperability environments require. They also help separate domain truth from profile obligation: a requirement may become a profile rule even when it is not an intrinsic fact about the domain.

## 6. Specialization: profiles and application models

Profiles and specialization standards define how broader standards are selected, narrowed, combined, or constrained for a particular community or interoperability purpose. They are intentionally downstream from a broader base: a profile does not need to redefine every concept it uses. Instead, it identifies the subset, options, constraints, identifiers, and additional obligations needed to make implementations sufficiently predictable for a specific use case.

This source type is directly relevant to the eventual V2 application profile. Its value is methodological as well as technical. Existing profiles show how standards communities handle optionality, specialization, declaration of support, compatibility with a base standard, and community-specific semantics without unnecessarily forking the underlying standard. The V2 profile can therefore be understood as a purpose-specific contract over the DIM and OGC standards environment rather than as a second domain model.

## 7. Concrete representation: data models, schemas, encodings, and exchange formats

Data models, schemas, encodings, and exchange formats standardize how information is represented concretely. They answer questions such as which fields or structures exist, how values are serialized, how records are nested or referenced, how content is validated, and how data can be exchanged between implementations. They operate at a lower level of abstraction than the DIM and are closer to implementation, although some sophisticated schemas also carry substantial semantic structure.

The OGC SWE Common Data Model illustrates this layer by defining ways to package data so it is self-describing and semantically enabled, with the goal of interoperability at both syntactic and semantic levels (Open Geospatial Consortium 2025c). SensorML similarly supplies concrete structures for describing processes, physical systems, inputs, outputs, parameters, configurations, and related metadata (Open Geospatial Consortium 2025b). NIEM schemas, IEEE 1451 TEDS formats, Protobuf definitions, JSON schemas, UML-derived exchange models, and other corpus artifacts play comparable representational roles in their own communities.

For V2, these sources can inform the binding from DIM meaning into machine-readable structures. Their presence also gives the project a way to test donor accommodation: if V2 claims to reuse a donor concept, the donor's concrete representation can be compared with the V2 representation to determine whether the mapping is direct, transformed, partial, lossy, or intentionally unsupported.

## 8. Interaction: APIs, interfaces, protocols, and service specifications

APIs, interfaces, protocols, and service specifications standardize interaction. They define contracts between participants: resources, operations, messages, request/response patterns, streaming behavior, commands, queries, state transitions, transport bindings, or other exchanges. OGC API – Connected Systems exemplifies this layer. Part 1 defines Web API resources for systems and related feature resources; Part 2 defines dynamic resources and protocols for observations, commands, command status, results, and system events (Open Geospatial Consortium 2025a, 2025d).

This layer is where conceptual meaning becomes actionable interoperability. A DIM can establish what a Deployment or Sensor means, while an API determines how an implementation exposes, discovers, queries, creates, updates, or interacts with the corresponding representation. The profile can then constrain the applicable API behavior for the target community. Keeping these responsibilities separate prevents an API path or message structure from silently becoming the definition of the domain concept itself.

The API/interface population in the corpus is therefore especially useful for the eventual OGC binding and for donor-integration analysis. A donor may define a capability or relationship in a non-OGC protocol; V2 can preserve the donor meaning in the DIM while mapping the interaction contract into the selected CSAPI mechanism where an appropriate mapping exists.

## 9. Construction and assurance: modeling, packaging, versioning, conformance, policy, and governance

A standards family also needs rules for how it is constructed and how claims about it are assessed. Modeling, packaging, versioning, and conformance specifications standardize those meta-level processes. NIEM's Naming and Design Rules, for example, define separate conformance targets for namespaces, schema documents, models, and messages and make clear that different artifacts can carry different conformance claims (Cabral, Carlson, and Renner 2025). OGC's Modular Specification model similarly organizes standards into requirements and conformance classes so that obligations can be expressed and tested in modular form (Open Geospatial Consortium 2009).

Policy, registry, strategy, and governance sources operate at an adjacent institutional level. They address ownership, adoption, standards status, publication, lifecycle, and authoritative decision processes. These sources do not usually supply domain semantics, but they influence how a model or profile can be maintained responsibly over time.

For V2, this layer can support explicit extension rules, modularization, versioning, source provenance, conformance targets, machine-testable requirements, and governance boundaries. It is the layer that turns a useful model into a sustainable interoperability specification rather than a one-time research artifact.

## 10. Realization and evidence: implementations, tests, guidance, and operational systems

Implementation, test, and executable companion artifacts provide executable evidence. They can show whether a specification is implementable, how schemas or interfaces are used in practice, whether two systems interoperate, and where ambiguities appear. They are particularly valuable for validating mappings and conformance rules, but they do not define normative meaning merely by existing.

Guidance, research, engineering reports, and explanatory material provide rationale and interpretation. They often explain why a standard made a particular design choice, document mappings between standards, describe implementation experience, or expose limitations that are not obvious from normative clauses alone. Their authority differs from normative specifications, but they are useful for understanding context and avoiding superficial comparisons.

Reference systems, products, and operational evidence provide the reality check. Manuals, device specifications, actual sensor systems, and implementation examples can reveal information that abstract standards ignore or simplify. These sources allow V2 to test whether the emerging model/profile can describe real systems without forcing them into artificial abstractions. In the V2 method, they should validate and challenge the model rather than define it by anecdote.

## 11. How the source types fit together

The source types represented in the corpus can be understood as a layered but iterative standardization stack:

| Stack role | Primary source types | Principal contribution |
| --- | --- | --- |
| **Governance and construction** | Policy/strategy/governance; modeling, packaging, versioning, conformance methods | How the standards family is organized, extended, versioned, governed, and tested. |
| **Semantic foundation** | Ontologies; vocabularies; terminology; units; registries | Stable machine meaning, definitions, identifiers, quantity semantics, controlled values, and formal alignments. |
| **Conceptual/domain definition** | Conceptual, information, and domain models | Domain concepts, relationships, distinctions, intrinsic constraints, and abstraction boundaries. |
| **Architecture and requirements** | Reference architectures; requirements and capability specifications | Roles, system context, operational expectations, capabilities, completeness checks, and constraints that may drive profile obligations. |
| **Specialization** | Profiles and application models | Selection, narrowing, combination, optionality management, and community-specific obligations. |
| **Concrete representation** | Data models, schemas, encodings, exchange formats | Machine-readable structures and mappings from conceptual meaning into exchangeable data. |
| **Interaction and service behavior** | APIs, interfaces, protocols, services | Discoverable resources, operations, messages, commands, queries, and interaction contracts. |
| **Verification and realization** | Implementation/test artifacts | Executable validation, interoperability tests, reference behavior, and feasibility evidence. |
| **Interpretation and operational validation** | Guidance/research; reference systems/products/evidence | Rationale, implementation experience, real-system constraints, stress tests, and empirical challenge to the model. |

These layers reinforce one another. Semantics without representation cannot be exchanged; schemas without semantic grounding may be syntactically interoperable while remaining ambiguous; APIs without a stable model can expose inconsistent concepts; profiles without conformance rules may not produce predictable implementations; tests without clear normative targets can only test examples. Conversely, implementation experience may expose weaknesses in a conceptual model, and domain modeling may reveal that an existing API needs a more precise profile constraint. The stack should therefore be treated as a feedback system rather than a one-direction production line.

## 12. What the stack makes possible for V2

Removing the identity of individual donors and considering only the source types shows that the corpus is broad enough to support investigation of an end-to-end standards family. At its center could be a Domain Information Model establishing common domain meaning. That model could draw on existing ontologies, vocabularies, units systems, and information models rather than inventing equivalent semantics locally. Reference architectures and requirements could challenge its scope and completeness. An application profile could then select and constrain the model for the intended interoperability purpose. Schemas, encodings, and API specifications could realize those semantics in the CSAPI/SensorML/SWE environment. Conformance and governance methods could make the resulting obligations testable and maintainable, while implementations and real systems could validate whether the model actually works.

The source stack therefore makes the following kinds of V2 artifacts **possible**, subject to later evidence and need:

- a Domain Information Model;
- semantic mappings or ontology alignments;
- controlled definitions, vocabulary, units, and code identifiers;
- a modular application profile;
- an OGC/CSAPI binding;
- machine-readable schemas or constraint artifacts where necessary;
- donor-to-V2 mapping crosswalks that document mapping fidelity;
- explicit conformance targets, requirements, and validation tests;
- extension, versioning, and governance rules;
- canonical examples, test vectors, adapters, or reference implementations;
- informative design rationale and implementation guidance.

This list is deliberately broader than the committed V2 deliverables. **The presence of a source type means the corpus can inform that artifact class; it does not mean V2 should create it.** Each artifact must still justify itself through an actual interoperability need, reuse of existing standards, implementation value, and proportionate stewardship cost.

## 13. Implication for donor analysis

The stack changes how donor comparison should proceed. Sources should first be assessed according to the kind of authority they possess. Ontologies should be compared as semantic systems; information models as conceptual models; architectures as architectures; schemas as concrete representations; APIs as interaction contracts; conformance specifications as assurance methods. A donor should not be penalized because it does not solve a problem outside its standardization role.

Only after the groups have been understood on their own terms should V2 synthesize across them. At that stage, recurring concepts and relationships can be traced across ontology, information-model, architecture, schema, and interface layers. Where multiple sources describe the same underlying idea, their differences can be compared explicitly. Where a concrete schema contains a distinction absent from the information models, that distinction can be investigated rather than silently imported. Where no source type supplies a needed concept, the gap becomes visible and any V2-authored addition can be justified openly.

This approach allows the eventual DIM and profile to **emerge from the evidence**. It preserves the clean-slate intent of V2 while still taking advantage of the unusually broad standards corpus assembled for the effort.

## 14. Working conclusion

The 182-source corpus is not simply a large bibliography of competing sensor standards. It is a cross-section of the mechanisms by which information technology is standardized: semantic definition, conceptual modeling, architecture, requirements, specialization, representation, interaction, conformance, governance, implementation, and operational validation. Its principal value is therefore not that one donor will “win” globally. The corpus gives V2 the ability to select the strongest applicable source at each level, preserve mappings among levels, and identify where multiple standards are complementary rather than competitive.

The resulting V2 effort can consequently be more than a new data schema or API profile. If the evidence supports it, V2 can become a coherent standards-grounded chain from domain meaning to interoperable representation and testable implementation. The next research phase should determine which parts of that chain are actually necessary and which donor sources provide the strongest foundations or supplements within their respective standardization roles.

## References

Cabral, James, Tom Carlson, and Scott Renner, eds. 2025. *NIEM Naming and Design Rules (NDR) Version 6.0*. OASIS Standard. December 5. https://docs.oasis-open.org/niemopen/ndr/v6.0/ndr-v6.0.html.

Open Geospatial Consortium. 2009. *The Specification Model—A Standard for Modular Specifications*. OGC 08-131r3. October 19. https://docs.ogc.org/pol/08-131r3.pdf.

Open Geospatial Consortium. 2025a. *OGC API—Connected Systems—Part 1: Feature Resources*. OGC 23-001, version 1.0. July 16. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC SensorML Encoding Standard*. OGC 23-000, version 3.0. July 16. https://docs.ogc.org/is/23-000/23-000.html.

Open Geospatial Consortium. 2025c. *OGC SWE Common Data Model Encoding Standard*. OGC 24-014, version 3.0.0. July 16. https://docs.ogc.org/is/24-014/24-014.html.

Open Geospatial Consortium. 2025d. *OGC API—Connected Systems—Part 2: Dynamic Data*. OGC 23-002, version 1.0. July 16. https://docs.ogc.org/is/23-002/23-002.html.

Pras, Aiko, and Jürgen Schönwälder. 2003. “On the Difference between Information Models and Data Models.” RFC 3444. January. https://www.rfc-editor.org/rfc/rfc3444.html.

QUDT.org. 2026. *QUDT Catalog*. Accessed October 25, 2026. https://www.qudt.org/catalog/qudt-catalog.html.

World Wide Web Consortium. 2023. *Web of Things (WoT) Architecture 1.1*. W3C Recommendation. December 5. https://www.w3.org/TR/wot-architecture11/.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology—2023 Edition*. W3C Working Draft. https://www.w3.org/TR/vocab-ssn-2023/.