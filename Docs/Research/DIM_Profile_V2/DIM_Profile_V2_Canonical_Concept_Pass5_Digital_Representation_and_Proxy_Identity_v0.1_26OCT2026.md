# Domain Information Model (DIM) / Application Profile Version 2 (V2)
## Canonical Concept Consolidation — Pass 5: Digital Representation / Proxy Identity

**Date:** 26 October 2026  
**Standing:** Evidence-backed **candidate meaning**, not an adopted DIM class, universal digital-twin architecture, identifier policy, or application-profile requirement.  
**Continuity:** [Incremental plan](DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md); [Pass 1 — Individual System](DIM_Profile_V2_Canonical_Concept_Pass1_Individual_System_Identity_v0.1_26OCT2026.md); [Pass 2 — Kind/Model](DIM_Profile_V2_Canonical_Concept_Pass2_Product_Model_Kind_v0.1_26OCT2026.md); [Pass 3 — Procedure/Method](DIM_Profile_V2_Canonical_Concept_Pass3_Procedure_Method_v0.1_26OCT2026.md); [Pass 4 — Composition](DIM_Profile_V2_Canonical_Concept_Pass4_Composition_and_Component_Standing_v0.1_26OCT2026.md).  
**Evidence scope:** Official published Connected Systems, Asset Administration Shell, Web of Things, OPC UA Devices, and SAREF sources; plus **pinned executable source evidence**, rather than normative claims, from Open Standard for Unattended Sensors reference implementation (OSUS-R), revision `d09088fbe56d4b64f0544d72e98c3cb70fa941f6`.

## 1. The question

**How should an individually identifiable sensing-equipment System relate to its API resource, digital description, server/device representation, proxy, adapter, virtual Thing, or digital twin—without confusing those with the actual subject or falsely equating the donor models?**

The question is **not** how to implement a proxy, choose universal identifiers, or construct a digital twin. It is whether existing donors make meaningful distinctions that the DIM should preserve when one real sensing System is integrated and exposed through different information systems.

## 2. Synthesized candidate meaning, with source pedigree

> **For the present V2 investigation, the individual equipment-realized System is distinct from the digital resources and descriptions through which information about it is published or accessed** (Open Geospatial Consortium 2025, §§ 8.5 and 9.2.2; Industrial Digital Twin Association 2026, “Overview,” “Asset Administration Shell Attributes”; World Wide Web Consortium 2023b, abstract and § 5.3.1.1). **A digital description may describe a particular System or Thing, while a service, server representation, intermediary, or adapter may provide access to, represent, or mediate selected information and functions without thereby becoming the same equipment System** (OPC Foundation n.d., §§ 1, 6.1, 6.3; World Wide Web Consortium 2023a, §§ 3, 6.10.2, 9.2.2; European Telecommunications Standards Institute 2024, “Services and Operations”; OSUS-R Contributors 2023, `Asset.java`, `AssetProxy.java`). **Several digital representations may concern one individual System, but their identifiers, versions, and relationships must be interpreted according to the source standard and actual evidence rather than assumed equal** (Open Geospatial Consortium 2025, § 8.5; OPC Foundation n.d., § 6.3; World Wide Web Consortium 2023a, § 9.2.2; World Wide Web Consortium 2023b, §§ 5.3.1.1, 11.2, 11.5). **In particular, a virtual Thing or digital twin may be a distinct software entity with additional functionality or may aggregate several Things; it must not be treated automatically as another physical sensing System or as a one-to-one copy of one** (World Wide Web Consortium 2023a, §§ 3, 5.7, 5.9, 9.2.2.2).

**Synthesis standing:** The *distinctions* have strong donor provenance. The combined statement is **V2 synthesis**. It introduces no new `DigitalSystem`, `RepresentationProxy`, `DigitalTwin`, or `representedBy` class/property and makes **no requirement for an identifier to be shared by all representations**.

## 3. Where each building block came from, and how it contributes

### 3.1 CSAPI: one real-world System can have several service representations

**What the donor means.** The **Open Geospatial Consortium (OGC) Application Programming Interface (API) – Connected Systems (CSAPI)** Part 1 separates a resource's server-local identity and URL from a `uniqueIdentifier` intended to identify the **real-world object represented across services**. Section 8.5 explains why multiple services may host different descriptions of one object. A System has a required `uniqueIdentifier`; the standard says that identifier **should** be persistent and independent of the resource URL—not an unconditional guarantee that every identifier persists for its entire physical lifetime (Open Geospatial Consortium 2025, §§ 8.4–8.5, 9.2.2).

**What V2 takes.** CSAPI offers the closest **binding-side anchor** for relating information about one individual equipment System across servers. A second resource URL does **not** inherently create a second System. But a matching label, vendor model, or URL pattern cannot prove that two resources describe the *same* equipment. V2 has not chosen identity reconciliation rules; its DIM-level requirement is to **avoid confusing equipment identity with a server resource address**.

### 3.2 AAS: the represented Asset and its digital shell are separately identifiable

**What the donor means.** The **Industrial Digital Twin Association (IDTA) Asset Administration Shell (AAS)** metamodel states that an `AssetAdministrationShell` **represents exactly one Asset**. The Shell is itself `Identifiable`, contains `AssetInformation` for the represented Asset, and references zero or more `Submodels` describing particular aspects of that Asset. Its own Shell identifier and the Asset identifiers held by `AssetInformation` have different roles; `globalAssetId` can be optional early in the lifecycle, subject to the metamodel's asset-identification constraint (Industrial Digital Twin Association 2026, “Overview,” “Asset Administration Shell Attributes,” “Asset Information Attributes”).

**What V2 takes.** This is independent, strongly explicit evidence that **identity of an equipment subject and identity of a digital shell are different**. The AAS one-Shell-to-one-Asset rule is **AAS-native**, however: it must **not** be made a universal rule for CSAPI servers, WoT proxies, or V2 representations. AAS Submodels are **aspect descriptions**, not new physical subsystems or V2 modules merely because they are separate digital documents.

### 3.3 WoT: a Thing, a Thing Description, and a Virtual Thing are different

**What the donor means.** The **World Wide Web Consortium (W3C) Web of Things (WoT)** Thing Description 1.1 defines a `Thing` as an abstraction of a **physical or virtual entity**. A `Thing Description` (TD) is a machine-readable description of that Thing's **metadata and interfaces**; it may be hosted on the Thing or externally—for example, to retrofit a legacy device (World Wide Web Consortium 2023b, abstract, § 5.3.1.1). WoT Architecture 1.1 also defines `Virtual Thing`, `Shadow`, and `Digital Twin` constructs, which can represent, mediate, enhance, simulate, or combine the behavior of underlying Things (World Wide Web Consortium 2023a, §§ 3, 5.7, 5.9).

**What V2 takes.** The distinction **Thing ≠ Thing Description** aligns with our equipment-versus-description question, although **not every WoT Thing denotes equipment**. A virtual Thing can itself be a software Service or an aggregation of several Things. We should **not** silently map its identity to the identity of one sensing-equipment System, nor absorb the complete WoT virtual-service domain into the DIM simply because it has applicable representation concepts.

### 3.4 WoT Intermediary: proxy identities can differ from originating Thing identities

**What the donor means.** A WoT `Intermediary` may consume a Thing and expose a proxy that changes protocol/security metadata, caches state, or adds functionality. The WoT Architecture expressly permits a proxy-generated TD to **reuse the original Thing identifier or receive a new identifier**, depending on the scenario (§ 6.10.2). Its proxy use case (§ 9.2.2.1) illustrates the new-identifier case. A digital twin can do more than proxy requests: it may cache state, queue work, predict behavior, or combine devices (World Wide Web Consortium 2023a, §§ 6.10.2, 9.2.2.1–9.2.2.2).

The Thing Description Recommendation also says its `id` property is **optional** and permits identifiers whose scope is contextual. Its security considerations advise that Thing IDs **should be mutable** when needed to reduce tracking risk (World Wide Web Consortium 2023b, §§ 5.3.1.1, 11.2, 11.5). **This is not the same identity policy as CSAPI's recommended persistent System UID**.

**What V2 takes.** It is **wrong to require all proxies to use the same URI** or to infer from different proxy IDs that they represent different equipment. A proxy may introduce a **separately identified exposed software Thing**. Whether an original and proxy representation refer to the same System, mirror its state, contain cached values, or represent a composite is **a relationship to establish from evidence**, not a consequence of using WoT. V2 is not deciding privacy/identifier conformance across those different standards.

### 3.5 OPC UA: server AddressSpace nodes, online/offline views, and the Device are different

**What the donor means.** **Open Platform Communications Unified Architecture (OPC UA)** Part 100: Devices defines a **Device** as an independently delimited physical entity, and its **Device Integration Host** as a Server that exposes information about multiple Devices even when those data are stored elsewhere (OPC Foundation n.d., §§ 3.1.5–3.1.6, 6.1). The OPC UA AddressSpace has its own **NodeIds** for Node representations, distinct in purpose from Device nameplate identification such as `SerialNumber` and `ProductInstanceUri` (OPC Foundation n.d., §§ 3.3.2, 4.5.2). Section 6.3's optional **Online/Offline** model can expose schematically equivalent online and configured/offline instances, connected by `IsOnline`; their Parameter Nodes **must have different NodeIds** even while they relate to the same equipment topology (OPC Foundation n.d., § 6.3).

**What V2 takes.** A Server node or offline engineering representation is **not another real device simply because it has a different NodeId**. Nor does an online value necessarily mean the same thing as a configured/offline value. This is particularly relevant to sensing-equipment state/configuration integration, though **the actual OPC UA node topology, NodeIds, and online/offline implementation mechanics stay donor- and binding-specific**.

### 3.6 SAREF: a Service represents a function, not automatically a complete device

**What the donor means.** The **European Telecommunications Standards Institute (ETSI)** Smart Applications REFerence (**SAREF**) Core 4.1.1 distinguishes a tangible `saref:Device`, the functions it supports, and a `saref:Service`: the Service is a **digital representation of a function in a network**. The `saref:represents` relation links a Service to its `Function` or `FunctionOfInterest`; `saref:offers` links a Device to the Service it offers. An `Operation` exposes a Command over the network (European Telecommunications Standards Institute 2024, “Services and Operations”).

**What V2 takes.** Not every digital representation corresponds to a whole physical System. Some represent **one function or command interface** of that System. Thus a service-to-Device mapping is not automatically a **device-identity equivalence**, and this narrower SAREF perspective is **not the same concept as an AAS Shell representing an Asset**. No separate V2 `Service` class is justified solely because SAREF uses one.

### 3.7 OSUS-R: a consumer-facing Asset interface and a hardware adapter differ

**What the source implements.** The **Open Standard for Unattended Sensors reference implementation (OSUS-R)** defines `Asset` as the **consumer-facing interface** for a physical device; consumers are explicitly instructed not to use the plug-in `AssetProxy` directly. Its `AssetProxy` interface is implemented by a **device-specific plug-in** that interacts with hardware, while the core automatically handles some information and provenance fields (OSUS-R Contributors 2023, `Asset.java` and `AssetProxy.java`, pinned revision noted above).

**What V2 takes.** This is direct **implementation-level evidence** for separating **an equipment subject, the common software interface presenting it, and a device-specific adapter implementing communication/behavior**. But its Java `Asset` interface is itself a **software abstraction of equipment**, not literally the physical object; the `AssetProxy` is an adapter interface, **not automatically a WoT Virtual Thing, AAS Shell, or digital twin**. The pattern informs integration architecture but does **not** justify transplanting OSUS-R's software classes into the conceptual DIM.

## 4. Alignment and semantic limits

| Donor | What it represents or mediates | Important distinction / mapping limit |
| --- | --- | --- |
| CSAPI `System` resource | A standards-defined feature-resource description of a System | Real-world System UID ≠ server resource URL/local ID; multiple descriptions may concern one System |
| AAS `AssetAdministrationShell` | An identified digital shell representing one Asset | Shell identity ≠ Asset identity; *AAS* one-Asset constraint is source-scoped |
| WoT `Thing Description` | Metadata/interfaces for one physical **or virtual** Thing | Thing ≠ TD; TD `id` is optional/contextual and may change |
| WoT Intermediary / Digital Twin | Protocol/behavior mediation, state caching, optional simulation or aggregation | Proxy may get a new ID; one digital twin may cover more than one Thing |
| OPC UA `AddressSpace` Device node | Server-visible model of Device data/topology | NodeId ≠ hardware identity; configured/online views may have different NodeIds |
| SAREF `Service` / `Operation` | Network representation of a Function / Command | Digital functional interface ≠ complete Device representation |
| OSUS-R `Asset` / `AssetProxy` | Common consumer interface / hardware-facing plug-in | Implementation boundary, **not** a general digital-twin ontology |

**Conclusion from donor comparison:** The donors converge on the value of preserving **subject versus digital description/exposure/mediation**, but do **not** define one interchangeable generic `DigitalRepresentation` class. Their representations have different **subjects**, scales, functions, cardinalities, and identity rules. The words *represents*, *describes*, *offers*, *mediates*, *hosts*, and *identifies* should remain different **where the source distinguishes them**—do not silently replace all with one V2 predicate.

## 5. A practical integration test

Suppose the **same real-world temperature instrument** has a CSAPI System resource, an AAS Shell with technical information, an OPC UA online/offline pair, and a WoT proxy at a different network address. These descriptions could in principle all concern one equipment System, **but this is a hypothetical mapping example**; their identifiers are not guaranteed to match and their contents may describe different moments, functions, or scopes. To assert sameness, an integration needs actual asset identity evidence or explicit validated mappings. To avoid semantic loss, it must also retain distinctions such as current/online versus configured/offline values and Thing-versus-proxy identity (Open Geospatial Consortium 2025, § 8.5; Industrial Digital Twin Association 2026, “Asset Information Attributes”; OPC Foundation n.d., § 6.3; World Wide Web Consortium 2023a, § 6.10.2).

An interoperable DIM **need not itself expose five native protocols**; it should not conflate the described equipment with the information resources and software mechanisms through which that equipment is understood. The eventual profile/binding may need to communicate certain source relationships, but this pass does not decide their exact representation.

## 6. Material open questions and disposition

1. **Which relations really belong in the DIM?** Distinguishing a physical subject from its representations is essential. But is an explicit source-neutral **relationship to a digital representation** itself domain-semantic, or should some of those links remain profile/binding or provenance metadata? No common `representedBy` predicate is adopted here.
2. **How will identity reconciliation and provenance work?** Does V2 need to preserve source System identifiers, representation IDs, mediating agency, version/time and whether information was cached, translated or inferred? These are relevant requirements to examine later—not grounds for inventing one persistent global identifier or equivalence test now.
3. **What is a virtual subject versus a representation of equipment?** WoT admits virtual/software Things, composites and intermediaries. Our present `Sensor + Equipment` scope does not automatically admit those as *top-level equipment Systems*, though related digital resources may be indispensable to an integration. Exact selection remains open.
4. **Multiplicity and ownership of representations.** AAS requires one represented Asset per Shell; WoT can proxy or aggregate multiple Things; OPC UA can expose multiple Devices through a host. These **donor-local relationships must not produce one universal V2 cardinality**.

**Disposition:** **Strongly supported semantic distinction; no new DIM class or relationship mandated.** We now have candidate meanings for all **five** planned concept passes. **Stop here:** the **next planned task is the five-pass human synthesis checkpoint**, not an automatic model-building exercise, not a new identity schema, and not an application-profile draft.

## References — Chicago Manual of Style, 18th ed., author–date

European Telecommunications Standards Institute. 2024. *SAREF: Smart Applications REFerence Ontology—Core*. Version 4.1.1. https://saref.etsi.org/core/v4.1.1/.

Industrial Digital Twin Association. 2026. *Specification of the Asset Administration Shell, Part 1: Metamodel*. Version 3.2. https://industrialdigitaltwin.io/aas-specifications/IDTA-01001/v3.2/spec-metamodel/core.html.

Open Geospatial Consortium. 2025. *OGC API—Connected Systems—Part 1: Feature Resources*. OGC 23-001, version 1.0, July 16. https://docs.ogc.org/is/23-001/23-001.html.

OPC Foundation. n.d. *OPC Unified Architecture Part 100: Devices*. Version 1.05.0. https://reference.opcfoundation.org/specs/OPC-10000-100/full.

OSUS-R Contributors. 2023. `Asset.java` and `AssetProxy.java`. Open Standard for Unattended Sensors Reference Implementation. Frozen Git revision `d09088fbe56d4b64f0544d72e98c3cb70fa941f6` (22 February 2023). https://github.com/ssg-udri/OSUS-R/blob/d09088fbe56d4b64f0544d72e98c3cb70fa941f6/mil.dod.th.core/src/mil/dod/th/core/asset/Asset.java; https://github.com/ssg-udri/OSUS-R/blob/d09088fbe56d4b64f0544d72e98c3cb70fa941f6/mil.dod.th.core/src/mil/dod/th/core/asset/AssetProxy.java.

World Wide Web Consortium. 2023a. *Web of Things (WoT) Architecture 1.1*. W3C Recommendation, December 5. https://www.w3.org/TR/wot-architecture11/.

World Wide Web Consortium. 2023b. *Web of Things (WoT) Thing Description 1.1*. W3C Recommendation, December 5. https://www.w3.org/TR/wot-thing-description11/.
