# PITON — DIM/Profile V2 Research Continuity

**Version:** 0.1  
**Date:** 25 October 2026  
**Repository:** `OS4CSAPI/glaux-client`  
**Branch:** `research/dim-profile-v2`  
**Workspace:** `Docs/Research/DIM_Profile_V2/`

## 1. Mission

This PITON exists so the DIM/Profile V2 research can be resumed in a new chat without reconstructing the conceptual history from memory or accidentally reverting to version 1 assumptions. The effort is exploring a new version of the domain information model and application profile from the ground up, using the version 1 work as predecessor evidence rather than as an unquestioned design authority. The immediate objective is to establish the sourced conceptual taxonomy and scope boundary before reopening the broader donor/community research program. Do not jump ahead into profile redesign, conformance clauses, donor reconciliation, or implementation work until the current taxonomy question has been deliberately advanced.

The V2 work must not be coupled to MERLIN as a program or product identity. Existing MERLIN-era bibliography, profile, source register, research papers, examples, and continuity records remain valuable evidence because they document the original problem, investigated donors, and prior design decisions. They may be cited as predecessor artifacts but should not determine the title, formal identity, namespace, or conceptual scope of V2 merely through historical inertia. The new work should be capable of standing independently of MERLIN and should remain suitable for later external/community use if the research supports that direction.

## 2. Research discipline

Use established source concepts as primitives and resist inventing new names, classes, or umbrella categories simply because a combination sounds useful. Multiple sourced concepts may be applied together descriptively, but the sum of those concepts should remain the sourced parts gathered together unless later research proves that a new named concept is actually necessary. When a new term is considered, first determine whether an existing source concept, a combination of existing concepts, or an existing sourced relationship already expresses the required meaning. Always distinguish sourced terminology, project interpretation, mapping, proposed specialization, and genuinely project-authored semantics.

Do not treat every researched donor as implemented or adopted. A source can confirm a concept, expose a gap, provide a mapping, supply an interpretive constraint, or remain irrelevant to the final model without becoming a conformance obligation. Preserve the earlier research discipline that standards implementation means identifiable normative obligations and testable conformance, while design inspiration or translation remains explicitly different. The V2 effort should prefer reuse of mature concepts where they fit, but it should not distort the intended domain merely to maximize reuse.

## 3. Meaning of “whole system”

For this effort, “whole system” has a specific working meaning supplied by the project owner. It means that the user should be able to access, understand, and explore a deployed sensor system as a complete operational subject rather than merely retrieve the observations it produces. The intended information includes the system’s description, identity, components, configuration, capabilities, telemetry, deployment context, communications, power, condition, management interactions, service/lifecycle history, provenance, and other supported information. Do not reinterpret “whole system” as an automatic claim that the top-level subject is a system-of-systems, enterprise system, sensor network, or larger aggregate.

This meaning is consistent with SensorML 3.0, which allows a sensor system whose overall application is sensing to contain sensing, actuation, and computational subprocesses (Open Geospatial Consortium 2025b, sec. 8.6). A weather station or digital camera can therefore remain a sensor system even though its complete description contains components with different functional roles. The V2 model can describe those internal and contextual concerns without changing the top-level subject merely because more than observations are represented. This distinction is important when later donor models introduce architectures that use broader system or system-of-systems terminology.

## 4. Current sourced conceptual baseline

The strongest conceptual root currently comes from the SOSA/SSN 2023 Edition Working Draft dated October 21, 2026. In that model, `Asset` generalizes `System` and `Platform`, while `System` is an Asset that implements a Procedure in the context of an Execution and may have subsystems that are themselves Systems (World Wide Web Consortium and Open Geospatial Consortium 2026, sec. 5.3.5). `Sensor`, `Actuator`, and `Sampler` are specializations of System associated respectively with observing, actuating, and sampling procedures. `Platform` is separately an Asset that hosts other Assets and should not be casually inserted into the same inheritance branch even though a real individual can satisfy more than one role.

The phrase “sensing system” is presently being used as informal domain wording rather than as a literal CSAPI value or a newly defined class. Its principal sourced semantic referent is a System characterized as `sosa:Sensor`, meaning a System that implements an ObservingProcedure to determine the value of an observable Property (World Wide Web Consortium and Open Geospatial Consortium 2026, sec. 5.5.2.4). SOSA/SSN expressly allows a Sensor to be a device, infrastructure, human agent, or software-based system, so sensing alone does not establish hardware or physical embodiment. Do not silently equate Sensor with Equipment, device, or “physical sensor.”

## 5. CSAPI classification facets

OGC API – Connected Systems Part 1 requires a `systemType` on every System resource and defines Sensor, Actuator, Sampler, Platform, and System as the standard values (Open Geospatial Consortium 2025a, sec. 9.2.2). Sensor is used when the System’s primary activity is sensing or observing; Actuator, Sampler, and Platform correspond to actuating, sampling, and carrying other systems; generic System covers other types. CSAPI explicitly states that this tagging carries semantic meaning and does not itself imply particular API functionality. Treat these as sourced classifications and not as a complete V2 domain taxonomy.

CSAPI separately defines optional `assetType` values Equipment, Human, LivingThing, Simulation, Process, Group, and Other (Open Geospatial Consortium 2025a, sec. 9.2.2). Equipment means that the System is composed of one or more hardware devices or pieces of equipment that interact directly with the real world, while the other values distinguish different kinds of realization. CSAPI demonstrates the independence of the two facets with examples such as Sensor + Equipment, Sensor + Simulation, Sensor + Human, Platform + Equipment, and System + Group. Do not turn the Cartesian product of these facets into named classes unless an external source already provides the name or a later V2 requirement proves that a new one is necessary.

## 6. Current candidate characterization

The strongest current characterization of the top-level systems that motivated V1 is `systemType = Sensor` together with `assetType = Equipment`. This is not yet the final V2 scope boundary and must not be promoted into a newly named class. It simply says, using two existing CSAPI classifications, that the System’s primary activity is sensing or observing and that the System is realized as hardware equipment interacting directly with the real world. CSAPI itself uses this combination for digital temperature probes, GPS receivers, and video cameras (Open Geospatial Consortium 2025a, sec. 9.1).

Equipment is sufficient to identify hardware embodiment in CSAPI, but it is not equivalent to the broader English adjective “physical.” Humans are physically embodied yet have a separate Human asset type, and a Group may represent multiple hardware systems without itself being Equipment. SensorML provides explicit PhysicalComponent and PhysicalSystem constructs for hardware devices when physical location and composition matter, which reinforces the importance of hardware embodiment without making it intrinsic to Sensor (Open Geospatial Consortium 2025b, secs. 8.5–8.6). Do not reintroduce “physical” as a taxonomic primitive unless later research demonstrates exactly what sourced concept it should denote.

## 7. Subsystems and the Composition/Aggregation distinction

CSAPI has a specific distinction that is likely to become important early in V2. Composition means that a subsystem is an integral part of its parent and cannot or is not usually taken apart during its lifetime except for maintenance, while Aggregation means that a subsystem is not permanently attached and can be associated with different parent Systems at different times (Open Geospatial Consortium 2025a, sec. 10.2). Composition is implemented through nested subsystem resources, whereas Aggregation uses Deployment resources to record what subsystem is mounted to what parent during a given period. CSAPI intentionally allows a looser Composition than strict UML, so an independently removable component can still be Composition if it is rarely separated from its parent.

The project owner highlighted the practical importance of this nuance using sensor assemblies that may contain either enduringly integrated sensing elements or field-reconfigurable sensors attached as needed. Do not hard-code that example into the model, but retain the conceptual distinction because V1 equipment/composition work may need to be re-evaluated against it. A cable, plug, or mechanical mounting method is not by itself the deciding criterion; the enduring versus deployment-scoped relationship is the meaningful distinction. Any future V2 equipment/component relationship should be checked against CSAPI Composition and Aggregation before a new relationship is introduced.

## 8. Profile-aware and domain-aware client hypothesis

The project owner raised an important possibility that native CSAPI classifications could help a client adjust its presentation without relying entirely on project-specific signaling. A generic client that sees Sensor + Equipment can legitimately know that it is dealing with a hardware System whose primary activity is sensing or observing, which may justify sensor-oriented presentation behavior. CSAPI nevertheless states that system typing is semantic and does not imply additional API functionality, so classification alone cannot prove that a richer V2 profile has been implemented (Open Geospatial Consortium 2025a, sec. 9.2.2). Treat classification-driven presentation as a promising standards-based behavior to investigate, not as an adopted V2 design.

RFC 6906 defines the `profile` link relation so a representation can signal an additional profile without changing its base media-type semantics (Wilde 2013, secs. 1, 3). It explicitly anticipates clients recognizing a profile URI and invoking specialized behavior, including specialized presentation. A future V2 design may therefore be able to combine native CSAPI System classification with an explicit profile identifier, allowing generic CSAPI clients to understand the base System and profile-aware clients to apply richer semantics. This mechanism remains a hypothesis to verify against the eventual V2 profile architecture rather than a requirement already adopted.

## 9. What is settled for the next step

The V2 effort is currently grounded in sourced concepts rather than in the V1 phrase “Managed Physical Sensing Systems.” The working subject is a sensor system considered comprehensively, with the strongest present top-level characterization being Sensor + Equipment, while the complete domain boundary remains open. “Whole system” means complete operational understanding of that Sensor System and does not enlarge the subject into a system-of-systems by itself. No new compound category name has been adopted.

The current taxonomy must remain faceted rather than being flattened into one invented inheritance tree. SOSA/SSN supplies the Asset, System, Sensor, Actuator, Sampler, Platform, Procedure, Deployment, and subsystem foundations, while CSAPI adds operational System-resource classification and asset-type characterization. SensorML adds detailed process and hardware-system modeling constructs that can represent complete sensor systems and their internal physical and computational structure. These three source families are the immediate baseline to test before the V2 effort turns outward to the broader donor corpus.

## 10. What is explicitly not settled

Do not assume that Sensor + Equipment is the final V2 scope simply because it fits the motivating examples examined so far. The next investigation must determine whether the intended top-level target systems are consistently characterized this way or whether legitimate cases require other sourced System, Platform, assetType, Deployment, or subsystem patterns. Do not invent names for those possible patterns while testing them. Record the sourced classification and relationship first, then determine whether any existing recognized term already describes the combination.

Do not yet decide which V1 information subjects, R01–R20 relationships, profile-owned definitions, power model, communications model, lifecycle model, or other detailed semantics survive into V2. The present checkpoint is about identifying the kind of thing being modeled and the sourced classification framework around it. Broader research into ISA, SAPIENT, OSUS, The Open Group SOSA, OMS, IEEE 1451/TEDS, I-ADOPT, QUDT, SWEET, MIMOSA, and other donors should resume only after this baseline is treated as the comparison point. Later research should be allowed to challenge the baseline rather than being used merely to justify it.

## 11. Immediate next task when work resumes

Resume by testing the current Sensor + Equipment characterization against representative top-level systems of the kind V1 intended to support. The purpose is not yet to design the DIM or to survey every donor, but to determine whether these targets are naturally represented by the sourced classifications and relationships already available in SOSA/SSN, CSAPI, and SensorML. Pay special attention to cases containing integrated versus interchangeable sensor components, platforms, embedded processing, communications, power, and management functions while preserving the owner’s meaning of “whole system.” Stop and record any target that cannot be described honestly with the existing sourced building blocks.

If the Sensor + Equipment characterization survives representative testing, the next major stage is the broader donor/community review that V1 previously entered. That review should ask what other communities call and model comparable systems, which distinctions they add, and whether those distinctions expose gaps in the current baseline. Do not start that stage by importing donor taxonomies wholesale or by renaming the target concept to match one donor. The objective is to compare evidence against the baseline and make explicit dispositions.

## 12. Repository artifacts and predecessor sources

Start V2 work in `Docs/Research/DIM_Profile_V2/` on branch `research/dim-profile-v2`. The companion checkpoint document is `DRAFT_Concept_Baseline_v0.1_25OCT2026.md` in that directory and should be read before continuing this PITON. The maintained predecessor bibliography is `Docs/Research/Bibliography/MERLIN_Domain_Information_Models_Annotated_Bibliography_v0.10_22OCT2026.docx`, with the matching source register in the same directory. These predecessor files are evidence and research inventory, not V2 authority by default.

The principal V1 technical baseline is `Docs/Design/MPSS/MERLIN_Managed_Physical_Sensing_Systems_Profile_Integrated_Binding_Draft_v0.3.5_17OCT2026.docx`, accompanied by the connected examples and standards-pedigree primer in `Docs/Design/MPSS/`. The current repository continuity checkpoint is `Docs/Plans/CONTINUITY.md`, and the current Smart Citizen manuscript contains a useful corrected explanation of the V1 DIM/profile architecture and donor reconciliation history. Use those artifacts to recover what V1 attempted and why, while preserving the V2 rule that predecessor design is subject to re-evaluation. Do not silently copy V1 names, R-number relationships, or profile-owned vocabulary into V2.

## References

Open Geospatial Consortium. 2025a. *OGC API – Connected Systems – Part 1: Feature Resources*. OGC 23-001, version 1.0. Published July 16, 2025. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC SensorML Encoding Standard*. OGC 23-000, version 3.0. Published July 16, 2025. https://docs.ogc.org/is/23-000/23-000.html.

Wilde, Erik. 2013. “The ‘profile’ Link Relation Type.” RFC 6906. March 2013. https://www.rfc-editor.org/rfc/rfc6906.html.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology – 2023 Edition*. W3C Working Draft, October 21, 2026. OGC 25-022. https://www.w3.org/TR/vocab-ssn-2023/.
