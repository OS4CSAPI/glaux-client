# DIM/Profile V2 — Post-Audit Discovery Pass 1: Subject and Boundary

**Version:** 0.1  
**Date:** 26 October 2026  
**Standing:** Human-readable discovery finding; not a final DIM scope, name, chassis selection, or module architecture  
**Inputs:** early CSAPI/DIM concept baseline; Phase A independent lineage extractions; C08 calibration audit; Phase A bulk trust triage  
**Excluded from input:** quarantined Phase B/C/D artifacts and their promoted anatomy decisions

## 1. The question

This pass asks only:

> **What are the donor communities collectively telling us about the kind of real-world subject we are trying to describe, its natural boundaries, and the information that must remain understandable about it?**

It does **not** ask for a final umbrella name, root class, module taxonomy, JSON structure, or profile binding.

## 2. First major finding — the recurring center is a persistent identifiable technical subject, not an observation feed

Across otherwise different traditions, the recurring center is some persistent subject that can be identified and described independently of any one measurement, message, command, event, network session or API representation.

Different communities call that subject different things:

- AAS represents an **Asset** through an Asset Administration Shell.
- Redfish manages typed physical/logical **Resources**, including devices/chassis/components.
- ISA centers interoperating **Components** and Compositions.
- Matter centers a **Node** with Endpoints.
- CSAPI centers a **System**.
- OPC UA Part 100 centers a **Device** and its components/subdevices.
- OSUS-R centers an **Asset** as the consumer-facing whole device.
- SAREF distinguishes a tangible **Device** from its DeviceKind.
- SOSA/SSN centers **Assets/Systems** and their specializations.
- The Open Group SOSA explicitly treats the bounded **Sensor** as its main subject.
- LwM2M manages a device-side **Client** and its exposed Objects.
- WoT distinguishes a **Thing** from the Thing Description that represents it on the Web.
- real UGS evidence centers persistent deployed sensor/device instances.

These terms are not asserted to be equivalent classes.

The useful convergence is more basic:

> **The thing of interest persists while its state, configuration, deployment, observations, commands, events and representations can change.**

That is stronger evidence for the DIM's center than any API endpoint or observation schema.

## 3. Second major finding — instance, kind/model, and digital representation repeatedly separate

Several independent traditions resist collapsing “the thing” into “the description of the thing.”

Examples include:

- AAS: represented Asset vs its AAS/digital representation, with type/instance distinctions.
- CSAPI: System instance vs `systemKind` description, plus separately implemented Procedures.
- SAREF: Device vs DeviceKind.
- Matter: Node/Endpoint instance vs Device Type.
- OPC UA: Device instance/type structures.
- WoT: Thing vs Thing Description, and Thing Model vs concrete Thing Description.
- Redfish: managed resource instance vs manufacturer/model/product information.

The C08 audit sharpened an especially important distinction:

> **System instance ≠ product/model/kind/datasheet ≠ Procedure/Method implemented by the System.**

This is one of the first cross-donor distinctions that now looks structurally important enough to preserve during later modeling.

## 4. Third major finding — enduring composition is repeatedly separated from other relationships

This is the strongest boundary signal in the donor evidence so far.

Independent communities repeatedly distinguish “what is part of this subject” from other ways things can be related:

- CSAPI: enduring Composition vs Deployment-scoped Aggregation.
- SOSA/SSN: subsystem vs hosting Platform vs Deployment.
- Open Group SOSA: Sensor Component boundary vs external Host Platform and external interfaces.
- ISA: Composition topology vs network topology.
- OPC UA Devices: component/subdevice topology vs communication/integration-host topology.
- AAS: part/hierarchy structures vs installation/location/other viewpoints.
- EMAN: physical Device/Component hierarchy vs power-flow, metering and aggregation relationships.
- SAPIENT: recursive subcomponents vs platform dependency vs network relationships.
- Matter: endpoint/functional composition, with explicit warning that this is not automatically physical containment.
- UGS evidence: device/component relationships vs trigger/cue, communications and deployment relationships.

The recurring lesson is not that all donors use the same part-of relation.

It is:

> **A useful DIM cannot use one generic “connected to / belongs to / child of” relationship for everything.**

The boundary of the subject has to preserve the difference between enduring intrinsic composition and external/contextual association.

## 5. Fourth major finding — the subject may be atomic or composite

The donor set strongly argues against assuming either “one box = one System” or “every System needs a component tree.”

Examples span both ends:

- Bosch BME280: one small integrated sensing product with internal functional blocks that do not need to become separately managed domain resources.
- IEEE 1451: module/channel structures where internal transducer channels matter.
- OSUS/UGS: whole device with meaningful internal sensors/cameras/transducers.
- OPC UA/AAS: rich component and subdevice structures.
- radiation instruments: handheld atomic equipment through multi-detector portal systems.
- Open Group SOSA: a Sensor can contain substantial hardware/software/runtime infrastructure.

The emerging scale rule is therefore:

> **Represent internal elements independently when their identity, state, configuration, capability, output, serviceability or relationships matter; do not fabricate decomposition merely because internals physically exist.**

This remains an interpretation to test later, but it is strongly supported by the scale range in the donor evidence.

## 6. Fifth major finding — “whole system” breadth is real, but the information categories are not the subject itself

Across the corpus, useful understanding of the persistent subject extends far beyond its observation output.

Different sources repeatedly expose some combination of:

- identity and product/model information;
- components/internal arrangement;
- functions/capabilities;
- configuration and modes;
- current state/condition/health;
- interfaces/connectivity;
- power/energy;
- deployment/location/host relationships;
- observations/measurements/detections;
- commands/actions/tasking;
- events/history/maintenance;
- provenance/responsibility;
- software/firmware and version information.

But those concerns occur in different structural roles.

For example:

- Observation is not the System.
- Command is not capability.
- Current state is not allowed configuration.
- Event/history is not current description.
- Network topology is not physical composition.
- Host Platform is not automatically part of the Sensor.
- Digital/API representation is not automatically the physical subject.
- Product/model information is not the individual instance.

This is the practical meaning of the earlier “whole system” objective: **retain enough information to understand the operational subject without turning every related fact into intrinsic composition or one monolithic record.**

## 7. What this says about the CSAPI System + Sensor + Equipment baseline

The donor research has **not yet produced evidence for a better final umbrella name**.

It has, however, clarified the role of the existing baseline.

The CSAPI framing remains valuable because it separates three ideas that other donors often combine differently:

- a persistent **System** subject;
- a sensing/observing **role** represented by `systemType = Sensor`;
- a hardware/equipment **realization** represented by `assetType = Equipment`.

External donors strongly reinforce the need for a persistent subject and a physical/equipment realization boundary.

They also show that the internal structure of that subject can range from atomic to highly composite and can include non-sensing support functions without necessarily changing the identity of the whole subject.

What they **do not yet independently establish** is that “Sensor + Equipment” is the complete final scope of every legitimate V2 target case.

That remains open, as intended.

## 8. Chassis result at this point

The evidence does **not** currently justify replacing the CSAPI/SOSA/SSN baseline with one external donor as “the chassis.”

Instead, several donors sharpen different parts of the boundary:

- **CSAPI + SOSA/SSN** — strongest native anchor for System/Sensor/Equipment-role context, subsystem/hosting/Deployment distinctions and the intended OGC environment.
- **SensorML 3.0** — strongest native OGC detail for physical systems/processes, components, configuration/capability and whole-system description.
- **Open Group SOSA** — unusually strong sensing-domain evidence for a bounded Sensor containing heterogeneous hardware/software/support components while remaining distinct from its Host Platform.
- **OPC UA Devices / PA-DIM** — strong generic device/equipment evidence for device identity, subdevices/components, functions, health and communications/integration boundaries.
- **AAS and SAREF** — strong independent evidence for represented asset/device, type/kind, semantic references, composition and reusable aspect/function structures.
- **ISA, SAPIENT, OSUS and UGS evidence** — strong operational stress tests showing what real managed/deployed sensing systems need to expose and where network/tasking/management structures can be mistaken for intrinsic equipment structure.
- **MIMOSA, EMAN, Redfish, LwM2M and other focused donors** — strong evidence for narrower management, condition, power, lifecycle, interface or device-management concerns without necessarily defining the whole sensing subject.

This suggests that **“chassis” may ultimately be a sourced conceptual foundation assembled from compatible donor strengths rather than a wholesale adoption of one donor model**.

That is a research observation, not yet a design decision.

## 9. A candidate description of the emerging subject — deliberately not a name

The evidence is now strong enough to state a provisional descriptive hypothesis without naming a new class:

> **The DIM appears to be converging on an individually identifiable, persistently describable sensing-oriented technical subject that may be atomic or composite, whose enduring equipment boundary can be distinguished from its host, deployment, network, management and target context, and whose kind/model, capabilities, configuration, state, interactions, outputs/actions, history and provenance can be understood without conflating those with the subject itself.**

This is **not** the final scope statement.

It is useful because it can now be tested against the remaining donor evidence and real systems without inventing a noun for it.

If later evidence shows that this description excludes legitimate intended cases, it must change.

## 10. What remains genuinely unresolved

The important open questions are now narrower and more meaningful:

1. **Sensing boundary:** must the top-level subject's defining role always be sensing/observing, or do legitimate profile cases require a broader system role while still belonging to the same domain?
2. **Sensor/effecter mixtures:** when a sensing system includes actuation/effecting, when is that simply internal capability and when does it change the subject classification?
3. **Kind/model semantics:** how should reusable product/model/kind information relate to reusable Procedure/Method definitions across donors?
4. **Component threshold:** when does an internal detector/channel/component become an independently represented subject?
5. **Host boundary:** when can a platform/vehicle/structure become enduring composition rather than contextual hosting?
6. **Digital representation:** which representation/proxy/digital-twin concepts belong in the DIM versus later profile/binding layers?
7. **Common vs specialized information:** which condition, power, communications, maintenance, security and modality-specific semantics are truly common?
8. **Final domain name/description:** does an established concept emerge that names this bounded subject more accurately than the current System/Sensor/Equipment shorthand?

## 11. Direction from here

The next useful discovery work is **not** another broad audit.

It is to test and refine the subject/boundary findings above against the donor corpus, especially the unresolved questions, while preserving the GREEN/YELLOW evidence ceilings.

Only after the bounded subject is stable enough should the project derive candidate DIM structural organization.

The research sequence is therefore back to:

> **understand the subject → settle its boundaries → then derive its information structure → then bind/profile it in CSAPI.**
