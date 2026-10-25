# Draft Concept Baseline for DIM/Profile V2: System, Sensor, Equipment, and Whole-System Scope

**Working draft v0.1 — 25 October 2026**  
**Status:** Research checkpoint; not a normative model, profile, or scope decision.

## 1. Purpose and standing

This document captures the conceptual checkpoint reached before beginning a renewed survey of external communities and donor models for version 2 of the domain information model and application profile. Its purpose is to preserve what has been established from the standards already closest to the work, distinguish sourced concepts from project interpretation, and prevent later research from silently rebuilding on assumptions inherited from version 1. The checkpoint deliberately stops before deciding whether the current `Sensor + Equipment` characterization is the complete scope of version 2. It therefore records a disciplined starting point rather than a finished taxonomy.

The version 2 effort is intentionally not coupled to MERLIN as a product or program identity. Existing MERLIN-era artifacts remain predecessor evidence because they record the problem that version 1 attempted to solve, but they do not define the identity or final scope of version 2. The working domain concern remains the class of sensor systems that motivated version 1, while the terminology and taxonomy are being rebuilt from sourced concepts rather than retained labels. No new umbrella term or compound class is introduced by this checkpoint.

## 2. The problem being carried forward from version 1

Version 1 used the idea of the “whole system” to communicate that the user should be able to understand and explore a deployed sensor system as a complete operational subject rather than merely consume the observations it produces. In this usage, “whole system” does not mean a system-of-systems, enterprise architecture, or larger aggregate beyond the sensor system itself. It means that the system’s identity, technical description, configuration, components, capabilities, telemetry, deployment context, communications, power, condition, management interactions, service history, and other supported information should remain accessible alongside its observations. That working meaning is adopted for version 2 unless later evidence requires revision.

This framing matters because a sensor system can remain a sensor system even when its complete description includes supporting functions that are not themselves sensing functions. SensorML 3.0 explicitly describes sensor systems whose overall application is sensing while their internal composition includes sensing, actuation, and computational subprocesses (Open Geospatial Consortium 2025b, sec. 8.6). The standard uses weather stations and digital cameras as examples of physical sensor systems whose internal components perform different roles while contributing to the system’s overall sensing purpose. The version 2 effort should therefore avoid treating “sensor” as equivalent to “a single detector that only emits observations.”

## 3. Sourced conceptual foundation in SOSA/SSN

The current SOSA/SSN model provides the cleanest sourced conceptual foundation for identifying the kind of thing being modeled. In the October 21, 2026 Working Draft of the 2023 Edition, `sosa:Asset` generalizes `sosa:System` and `sosa:Platform`, while `sosa:System` is an Asset that implements a Procedure in the context of an Execution (World Wide Web Consortium and Open Geospatial Consortium 2026, secs. 5.3.5.2.1, 5.3.5.2.4). A System may be a device, infrastructure, human agent, or software system and may contain subsystems that are themselves Systems. SOSA/SSN further states that System generalizes the Actuator, Sensor, and Sampler classes.

Within that model, `sosa:Sensor` is a System that implements an ObservingProcedure to determine the value of an observable Property (World Wide Web Consortium and Open Geospatial Consortium 2026, sec. 5.5.2.4). A Sensor may be implemented by a device, infrastructure, human agent, or software-based system, including a simulation, so sensing does not by itself imply hardware. `sosa:Actuator` and `sosa:Sampler` are sibling specializations of System associated with actuation and sampling rather than observation (World Wide Web Consortium and Open Geospatial Consortium 2026, secs. 5.4.2.4, 5.6.2.6). `sosa:Platform` is separately an Asset that hosts other Assets, particularly Systems and other Platforms, and therefore should not be casually treated as another subclass of System in the SOSA/SSN hierarchy (World Wide Web Consortium and Open Geospatial Consortium 2026, sec. 5.3.5.2.3).

| Sourced concept | Sourced role at this checkpoint |
| --- | --- |
| `Asset` | Abstract SOSA/SSN resource involved in a Deployment; generalizes System and Platform. |
| `System` | Asset that implements a Procedure in the context of an Execution. |
| `Sensor` | System that implements an ObservingProcedure. |
| `Actuator` | System that implements an ActuatingProcedure. |
| `Sampler` | System that implements a SamplingProcedure. |
| `Platform` | Asset that hosts other Assets, particularly Systems and other Platforms. |

## 4. CSAPI system classification is faceted rather than a single tree

OGC API – Connected Systems Part 1 turns selected SOSA/SSN concepts into actionable API resources and requires each System resource to carry a `systemType` (Open Geospatial Consortium 2025a, sec. 9.2.2). Its standard values are Sensor when the System’s primary activity is sensing or observing, Actuator when its primary activity is actuating, Sampler when its primary activity is sampling, Platform when its primary activity is carrying other systems, and generic System for other system types. CSAPI explicitly notes that tagging a System resource with one of these types carries semantic meaning but does not itself imply particular API functionality. The classification therefore helps describe what kind of System is being represented without turning the classification into a separate service contract.

CSAPI also defines an independent optional `assetType`, with values Equipment, Human, LivingThing, Simulation, Process, Group, and Other (Open Geospatial Consortium 2025a, sec. 9.2.2). Equipment means that the System is composed of one or more hardware devices or pieces of equipment that interact directly with the real world, while Simulation and Process distinguish software-based and data-transforming realizations. The standard demonstrates that these are separate classification facets by combining them in examples such as `Sensor + Equipment` for a digital temperature probe, `Sensor + Simulation` for a weather forecasting system, `Sensor + Human` for a human bird watcher, and `Platform + Equipment` for an unmanned vehicle. Version 2 should therefore treat `systemType` and `assetType` as sourced building blocks rather than inventing a new named class for each possible combination.

| CSAPI facet | Sourced values most relevant to the present checkpoint | Question answered |
| --- | --- | --- |
| `systemType` | Sensor, Actuator, Sampler, Platform, System | What principally characterizes the System’s activity or role? |
| `assetType` | Equipment, Human, LivingThing, Simulation, Process, Group, Other | What kind of asset realization is involved in the System? |

## 5. Current candidate characterization: Sensor plus Equipment

The strongest current characterization of the top-level systems that motivated version 1 is the combination `systemType = Sensor` and `assetType = Equipment`. Both terms are native CSAPI concepts, and CSAPI expressly uses this combination for hardware sensing examples such as a digital temperature probe, GPS receiver, and video camera (Open Geospatial Consortium 2025a, sec. 9.1). This checkpoint does not convert that combination into a newly named class, nor does it assert that every possible version 2 case must use it. For now, it is simply the most direct sourced characterization of a hardware System whose primary activity is sensing or observing.

The Equipment classification is sufficient to establish hardware that interacts directly with the real world in the specific sense defined by CSAPI, but it is not synonymous with everything that can be described as physical. A human is physically embodied yet is classified separately as Human, and a Group may represent multiple physical systems while remaining a distinct asset type (Open Geospatial Consortium 2025a, sec. 9.2.2). SensorML likewise has explicit PhysicalComponent and PhysicalSystem constructs for hardware devices whose real-world location is important, showing that physical realization is meaningful without making “physical” intrinsic to the concept of Sensor (Open Geospatial Consortium 2025b, secs. 8.5–8.6). Version 2 should therefore retain Equipment as a sourced classification and avoid using “physical” as an unsourced taxonomic shortcut until the intended boundary is fully tested.

## 6. Whole-system information does not change the System’s primary classification

The “whole system” objective is informational rather than taxonomic: it asks for a sufficiently complete representation of the Sensor System, not for a broader parent category merely because more than observations are represented. SensorML states that a physical sensor system may coordinate sensing components, actuators, and computational components while the system’s overall application remains sensing (Open Geospatial Consortium 2025b, sec. 8.6). That distinction allows version 2 to model the top-level System’s identity, specification, internal structure, telemetry, operating state, and management context without requiring every internal component to be a Sensor. The top-level classification should follow the sourced semantics of the System itself rather than the diversity of information exposed about it.

This point also guards against a recurring modeling error in which “system description” is reduced to the observation interface. CSAPI Part 1 explicitly provides System metadata, Procedures, Deployments, Sampling Features, Property Definitions, subsystem relationships, and advanced SensorML encodings for detailed system descriptions, while Part 2 adds observations, commands, and system events (Open Geospatial Consortium 2025a, secs. 1, 7). The standards stack therefore already anticipates access to substantially more than observations when describing a connected Sensor. Version 2 should use that breadth as the starting environment for a domain information model rather than create an artificial split between “sensor data” and “everything else about the sensor.”

## 7. Subsystems: composition and aggregation must remain distinct

CSAPI provides a particularly important distinction for System/subsystem relationships. Composition applies when a subsystem is an integral part of the parent and cannot or is not normally taken apart from the parent during its lifetime except for maintenance, while Aggregation applies when a subsystem is not permanently attached and may be attached to different parents at different times (Open Geospatial Consortium 2025a, sec. 10.2). Composition is represented by nested subsystem resources, whereas Aggregation is represented through Deployment resources that describe which subsystem is mounted on which parent during a given period. CSAPI intentionally uses a looser meaning of Composition than strict UML, allowing a component to be independently removable in principle while still being treated as Composition if it is rarely separated from the parent.

This distinction is likely to matter directly to the version 2 domain because sensing systems can combine permanently integrated and field-reconfigurable sensor components. CSAPI illustrates Composition with built-in UAV sensors and weather stations with built-in sensors, Aggregation with interchangeable weather-station sensors, and mixed cases with a UAV that has permanent flight equipment plus interchangeable sensor payloads (Open Geospatial Consortium 2025a, sec. 10.2). The presence of a cable, connector, or mounting mechanism is not itself the governing criterion; the semantic question is whether the component is an integral enduring part of the parent or a deployment-scoped, interchangeable attachment. Version 2 should preserve that sourced distinction rather than create a single generic “has component” relationship for both cases.

## 8. Implications for the version 2 domain information model

At this checkpoint, the domain information model should be understood as organizing information about a Sensor System comprehensively while retaining the distinctions already supplied by the underlying standards. The top-level subject can remain characterized as a Sensor even when the model also describes its specification, subsystems, deployed attachments, configuration, telemetry, communications, power, condition, commands, service history, and other supported information. Those concerns describe and contextualize the Sensor System; they do not automatically create a different top-level system category. The version 2 model should therefore build outward from sourced System, Sensor, asset, subsystem, deployment, procedure, observation, command, and event concepts before introducing any new vocabulary.

The current `Sensor + Equipment` characterization should be treated as a candidate boundary to be tested, not a conclusion to be defended. The next research stage must determine whether the kinds of hardware sensor systems version 1 intended to support are consistently characterized this way or whether legitimate target cases require other sourced `systemType`, `assetType`, Platform, Deployment, or subsystem patterns. That testing should occur before broader donor concepts are absorbed into the model so that later research can be evaluated against a clear baseline. Any future expansion should identify the exact sourced concept or relationship that requires the change rather than broadening the scope through informal analogy.

## 9. Machine-readable classification and profile-aware clients

The native CSAPI classifications may provide useful cues to clients even before a domain profile is recognized. A client that sees `systemType = Sensor` and `assetType = Equipment` can legitimately know that it is handling a hardware System whose primary activity is sensing or observing, which may support different generic presentation behavior than a Platform, Actuator, Simulation, or Human System (Open Geospatial Consortium 2025a, sec. 9.2.2). CSAPI cautions, however, that system typing carries semantic meaning and does not itself imply additional API functionality or conformance to an external profile. Version 2 should therefore investigate classification-driven presentation as a standards-based convenience without treating those classifications as proof that the richer domain contract is present.

RFC 6906 provides a separate Web mechanism for signaling that a representation follows an additional profile, and it explicitly allows a client to invoke specialized behavior when it recognizes a profile URI (Wilde 2013, secs. 1, 3). The RFC also requires the profile not to alter the base representation semantics, which aligns with the desired progressive behavior of generic and profile-aware clients. A future version 2 profile may therefore be able to use native CSAPI classifications to tell a client what kind of System it is seeing while using an explicit profile identifier to tell the client which additional semantic contract applies. This is a promising design direction rather than an adopted version 2 requirement at this checkpoint.

## 10. Working conclusions and unresolved questions

The table below records the standing of conclusions at this checkpoint. “Working conclusion” means the statement is sufficiently supported to guide the next research step but remains subject to revision if stronger source evidence requires it. “Open” means the question must not be silently resolved by implementation convenience or by reusing a version 1 term. These standings are intended to keep the next phase of research honest.

| Topic | Standing | Checkpoint result |
| --- | --- | --- |
| Program identity | Working conclusion | Version 2 is not coupled to MERLIN; MERLIN-era materials are predecessor evidence. |
| “Whole system” | Working conclusion | Means complete operational understanding of the sensor system, not a larger system-of-systems construct. |
| Sourced conceptual root | Working conclusion | SOSA/SSN Asset → System, with Sensor, Actuator, and Sampler as System specializations; Platform is separately an Asset. |
| “Sensing system” wording | Working conclusion | Informal domain wording principally corresponding to a System characterized as Sensor; it is not a literal CSAPI value. |
| Hardware target characterization | Candidate | `systemType = Sensor` + `assetType = Equipment`. |
| New compound class name | Not adopted | Do not coin a new name for the combination at this stage. |
| Equipment and physicality | Working conclusion | Equipment establishes real-world hardware in CSAPI, but “physical” is broader than Equipment and should not be used as an equivalent taxonomic primitive. |
| Subsystem semantics | Working conclusion | Preserve CSAPI Composition versus Aggregation and their different API/Deployment realizations. |
| Final V2 domain boundary | Open | Test whether Sensor + Equipment covers all intended top-level target systems. |
| Additional system/asset patterns | Open | Identify only where real target cases require them. |
| Profile-aware client signaling | Open design direction | Investigate native classifications plus an explicit RFC 6906 profile identifier; do not treat classification alone as profile conformance. |
| Broader donor/community research | Deliberately deferred | Begin only after this checkpoint is preserved and used as the baseline for comparison. |

## 11. Research gate

This document marks the deliberate stopping point before version 2 re-enters the broader standards and community landscape that informed version 1. The next phase should test this sourced baseline against representative target sensor systems and then against external donor communities, asking whether those sources confirm, refine, or expose gaps in the present concepts. Later work must preserve the distinction between adopting a source concept, combining existing source concepts descriptively, mapping between sources, and authoring a genuinely new concept. The default should remain reuse and explicit composition of sourced concepts, with new vocabulary considered only when existing concepts demonstrably cannot express a required meaning.

## References

Open Geospatial Consortium. 2025a. *OGC API – Connected Systems – Part 1: Feature Resources*. OGC 23-001, version 1.0. Published July 16, 2025. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC SensorML Encoding Standard*. OGC 23-000, version 3.0. Published July 16, 2025. https://docs.ogc.org/is/23-000/23-000.html.

Wilde, Erik. 2013. “The ‘profile’ Link Relation Type.” RFC 6906. March 2013. https://www.rfc-editor.org/rfc/rfc6906.html.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology – 2023 Edition*. W3C Working Draft, October 21, 2026. OGC 25-022. https://www.w3.org/TR/vocab-ssn-2023/.
