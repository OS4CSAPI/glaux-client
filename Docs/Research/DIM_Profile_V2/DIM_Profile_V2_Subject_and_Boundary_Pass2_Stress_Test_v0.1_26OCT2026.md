# Domain Information Model (DIM)/Profile Version 2 (V2) — Subject-and-Boundary Pass 2: Stress Test and Donor-Accommodation Envelope

**Version:** 0.1  
**Date:** 26 October 2026  
**Standing:** Focused boundary stress test; not a final scope name, root-class decision, module architecture, or application-profile binding  
**Controlling continuity:** `PITON_DIM_Profile_V2_Continuity_v1.3_26OCT2026.md`  
**Primary prior findings:** Post-Audit Discovery Pass 1; Emerging Subject-and-Boundary Pedigree v0.2; Phase A Bulk Trust Triage  
**Excluded from input:** quarantined Phase B/C/D artifacts and their promoted anatomy decisions

## 1. Purpose

Pass 1 produced the following evidence-backed hypothesis:

> **The DIM appears to be converging on an individually identifiable, persistently describable sensing-oriented technical subject that may be atomic or composite, whose enduring equipment boundary can be distinguished from its host, deployment, network, management and target context, and whose kind/model, capabilities, configuration, state, interactions, outputs/actions, history and provenance can be understood without conflating those with the subject itself.**

Pass 2 does not try to elaborate this into a model. It tries to **break it**.

Two complementary tests are applied:

1. **Outside-in boundary test:** find legitimate donor-backed cases that would not fit the hypothesis without distortion.
2. **Inside-out accommodation test:** ask what scope is implied if the DIM faithfully accommodates the strongest *relevant* semantic contributions from the donor pool.

The test uses donor-native evidence rather than the quarantined post-Phase-A synthesis artifacts.

## 2. Governing clarification — donor accommodation is per contribution, not per donor universe

A critical distinction emerged during this pass.

The project's interoperability goal should **not** be interpreted as:

> If a system conforms to any donor standard, the DIM must model the entire native universe of that donor.

That would make the domain unbounded. Open Platform Communications Unified Architecture (OPC UA) Devices covers transmitters, valve controllers, drives, programmable logic controllers and gateways; Web of Things (WoT) Things can represent physical devices, virtual entities, collections and services; Asset Administration Shell (AAS) can represent many industrial assets; Sensing for Asset Protection with Integrated Electronic Networked Technology (SAPIENT) includes sensors, effectors, fusion nodes and hierarchical system instantiations (OPC Foundation n.d.; World Wide Web Consortium 2023; Defence Science and Technology Laboratory 2026).

The more defensible rule is:

> **When V2 adopts, maps, or deliberately accommodates a donor concept that is relevant to an in-scope CSAPI-integrated subject, the DIM should be capable of preserving the material meaning and distinctions of that contribution without forcing native donor carrier mechanics into the common model.**

Therefore donor standards contribute **semantics**, not automatic jurisdiction over DIM scope.

This distinction is essential to the inside-out test.

---

# 3. Stress test 1 — Does mixed sensing and actuation break “sensing-oriented”?

## Challenge

Several important donors do not stop at sensing.

- Institute of Electrical and Electronics Engineers (IEEE) 1451.0 explicitly standardizes smart transducer interfaces for **sensors and actuators**; National Institute of Standards and Technology (NIST) describes a smart transducer as a smart sensor and/or actuator (IEEE 2024; NIST 2024).
- SAPIENT deliberately integrates both sensors and effectors, including soft-kill effectors, and tightly couples fused sensing with automated sensor/effector tasking (Defence Science and Technology Laboratory 2026).
- OPC UA defines a Device broadly enough to provide sensing, actuating, communication and/or control functionality (OPC Foundation n.d.).
- Sensor Model Language (SensorML) explicitly says that a sensor system whose overall application is sensing can contain sensing, actuating and computational subprocesses (Open Geospatial Consortium 2025b).

At first glance, these sources could imply that “sensing-oriented” is too narrow.

## Result — hypothesis survives, but “sensing-oriented” must mean defining orientation, not exclusive function

SensorML provides the decisive distinction: the **whole system's overall application** can remain sensing even when internal components perform actuation or computation (Open Geospatial Consortium 2025b).

This is compatible with the Connected Systems classification model, where `systemType` identifies the System's **primary activity**, not every activity it can perform. CSAPI also explicitly notes that all System types can generate datastreams and receive commands, so commandability does not make a Sensor an Actuator (Open Geospatial Consortium 2025a).

Therefore:

> **Actuation/effecting inside or alongside a sensing subject does not by itself invalidate a sensing-oriented top-level identity.**

However, SAPIENT and IEEE 1451 reveal a genuine boundary condition:

> **A pure effector/actuator whose defining role is not sensing is not automatically covered merely because one of our donors also standardizes it.**

If V2 later intends pure effectors as first-class top-level subjects, the current scope would need deliberate expansion.

### Pass 2 standing

**PASS WITH QUALIFICATION.**

“Sensing-oriented” remains viable if interpreted as:

> **sensing/observing is the defining or primary operational orientation of the top-level subject, not its only function.**

Pure-effector inclusion remains an explicit future scope decision, not an automatic consequence of donor reuse.

---

# 4. Stress test 2 — Does the donor pool force a scope broader than Equipment?

## Challenge

Several donors are intentionally broader than physical equipment.

- CSAPI distinguishes Equipment from Human, LivingThing, Simulation, Process, Group and Other asset realizations (Open Geospatial Consortium 2025a).
- WoT Thing is an abstraction of either a physical or virtual entity, and Virtual Things can represent or compose other Things (World Wide Web Consortium 2023).
- SOSA/SSN System may include software systems and agents where relevant (World Wide Web Consortium and Open Geospatial Consortium 2026).
- AAS Asset is deliberately broad across industrial asset use cases.

If V2 wants semantic compatibility with contributions from these donors, one might conclude that the DIM must also cover humans, simulations, pure software and virtual services.

## Result — no; broad donor applicability does not require broad V2 realization scope

The donor-accommodation rule resolves this.

A broad donor may contribute a distinction that is valid inside the V2 domain without importing every realization the donor permits.

Examples:

- WoT contributes **Thing vs Thing Description vs Thing Model** and representation/interaction separation. V2 can use those distinctions when describing equipment without making Virtual Thing or cloud Service a new top-level equipment realization.
- AAS contributes **Asset vs digital shell**, type/instance, composition, capabilities and semantic references. V2 can use those distinctions for equipment assets without becoming a universal industrial-asset model.
- OPC UA contributes Device/component, communication and integration-host distinctions. V2 can use those semantics for sensing equipment without promising to model every PLC, drive or valve controller.
- SOSA/SSN contributes System, Platform, Deployment, Procedure, FeatureOfInterest and Execution distinctions without forcing V2 to adopt every possible software/agent System realization.

CSAPI itself gives the cleanest implementation-side expression of this selective boundary through `assetType = Equipment`.

### Pass 2 standing

**PASS.**

The evidence still supports an **equipment-realized** target boundary for the present V2 effort.

This does not preclude future Human, Simulation, Process or other profiles. It means those are not silently imported merely because a reusable donor concept also applies to them.

---

# 5. Stress test 3 — Is the Host/Platform always outside the subject?

## Challenge

Pass 1 said the enduring equipment boundary can be distinguished from its host/platform context. That is correct as a distinction, but an overly literal reading would make every support structure external.

That would fail real systems.

A camera includes housing, processing electronics and possibly actuators as part of the camera. A weather station can be modeled as a whole sensing system containing several sensing and computational components. Conversely, a sensor payload mounted on a reusable aircraft or vehicle may clearly be hosted by a separate Platform (Open Geospatial Consortium 2025a, 2025b).

## Result — “host is external” is not the rule; relationship meaning is the rule

CSAPI's Composition/Aggregation distinction is more useful than a fixed noun-based rule:

- an integral subsystem that is not normally separated during the parent's lifetime is Composition;
- a non-permanent/interchangeable subsystem is Aggregation represented through Deployment (Open Geospatial Consortium 2025a).

SOSA/SSN separately provides subsystem, Platform hosting and Deployment relationships, confirming that these are distinct semantic roles (World Wide Web Consortium and Open Geospatial Consortium 2026).

The Open Group Sensor Open Systems Architecture (SOSA) independently places the Host Platform outside its Sensor boundary in its architecture, providing strong evidence for the hosted-payload case.

The correct emerging rule is therefore:

> **Do not classify something as intrinsic or contextual merely because it is called a platform, mount, chassis, vehicle, housing or host. Determine whether it belongs to the enduring identity/composition of the sensing subject or is an external hosting/deployment relationship.**

A dedicated weather-station structure may belong to the sensing System. A reusable vehicle carrying interchangeable payloads normally remains host context. A purpose-built integral support structure could be composition if the evidence establishes that boundary.

### Pass 2 standing

**PASS WITH REFINEMENT.**

The hypothesis should preserve **distinguishability from host context**, not assert that every possible host-like structure is external.

---

# 6. Stress test 4 — When does an internal detector/channel/component become its own modeled subject?

## Challenge

The donor pool spans:

- the Bosch BME280, whose internal sensing elements and electronics are real but not separately managed equipment subjects;
- IEEE 1451 TransducerChannels;
- Open Standard for Unattended Sensors (OSUS) internal sensors/cameras;
- unattended ground sensor (UGS) detector slots/transducers;
- OPC UA modular Devices/subdevices;
- SensorML PhysicalComponents and PhysicalSystems;
- complex radiation instruments with multiple detector elements.

A simplistic “everything physical is a component resource” rule would badly over-model atomic sensors. A simplistic “one box is one subject” rule would badly under-model complex systems.

## Result — independent representational standing is earned by semantic significance, not physical existence

No single donor gives V2 one universal threshold, but the corpus supports a practical common test.

An internal element increasingly merits independent DIM representation when one or more of the following materially matter to interoperability:

- persistent or source-recognized identity;
- independent type/model/kind;
- independently meaningful capability or performance;
- separate configuration or operating mode;
- separate current state/health/condition;
- separate calibration or quality semantics;
- distinct observations, outputs, commands or actions;
- independent replaceability/serviceability;
- meaningful relationships to other components, hosts, targets or sources;
- independent addressability/management in the source standard.

The BME280 supplies the negative control: internal functional blocks can be real and semantically different without being independently addressable subjects (Bosch Sensortec 2024).

SensorML supplies the conceptual scale control through PhysicalComponent versus PhysicalSystem (Open Geospatial Consortium 2025b).

### Pass 2 standing

**PASS.**

The current atomic/composite hypothesis survives.

The threshold above is a **V2 synthesis rule to test during concept consolidation**, not a donor-owned normative rule.

---

# 7. Stress test 5 — Do digital twins, proxies and API/runtime representations belong inside the subject?

## Challenge

AAS, WoT, OPC UA, OSUS and CSAPI all expose digital or software representations of real equipment. If all donor contributions are accumulated naively, V2 could collapse the physical subject and its digital representations into one concept.

## Result — representation relationship matters; representation identity must not replace subject identity

The separation is strong across independent donors:

- AAS distinguishes Asset from Asset Administration Shell.
- WoT distinguishes Thing from Thing Description and Thing Model; a Thing Description may even be hosted externally. WoT also defines Virtual Things, Shadows and Digital Twins as software/service constructs that can represent or mediate other Things (World Wide Web Consortium 2023).
- CSAPI requires a persistent System identifier independent of the API resource URL (Open Geospatial Consortium 2025a).
- OPC UA distinguishes real Device semantics from the Server/AddressSpace representation and from Device Integration Host behavior.
- OSUS separates the consumer-facing Asset abstraction from source-specific AssetProxy/adapter realization.

The DIM may need a semantic relationship such as **represented/exposed/mediated by** because the distinction itself is part of interoperability.

But the web resource, proxy, digital twin, API endpoint or server object should not silently become the same concept as the equipment subject.

### Pass 2 standing

**PASS.**

Digital representation is best treated as a **distinct but related concern**. Exact representation mechanics belong primarily to the later profile/binding/implementation layers.

---

# 8. Stress test 6 — Does SAPIENT force the DIM to become a system-of-systems/fusion model?

## Challenge

SAPIENT is one of the strongest potential counterexamples.

It is explicitly a modular sensor/effector system architecture. A SAPIENT instantiation includes sensors/effectors and a fusion node; version 2 permits hierarchical SAPIENT instantiations to appear as one sensor or effector to a higher-level fusion node (Defence Science and Technology Laboratory 2026).

This creates a danger: if every useful SAPIENT contribution is absorbed into the common DIM, fusion nodes, hierarchical system-of-systems structure, fused tracks, task allocation and system-level coverage could become intrinsic to the sensing-equipment subject.

## Result — SAPIENT is evidence for both reusable semantics and a boundary beyond the common subject

SAPIENT contributes highly relevant semantics:

- self-description/registration;
- capabilities and modes;
- state/status;
- detections/alerts;
- tasks/task acknowledgements;
- subcomponent metadata;
- source and message identity;
- platform/dependency relationships.

But its fusion architecture also contains semantics at a **larger operational-system level** than one persistent equipment subject.

The fact that an entire local SAPIENT instantiation can be abstracted upward as one sensor/effector is especially informative:

> **representation at one integration boundary does not prove that the represented aggregate is one enduring equipment subject at another modeling level.**

Therefore SAPIENT should challenge and enrich the common model without forcing its fusion-system architecture into the intrinsic equipment chassis.

### Pass 2 standing

**PASS WITH STRONG SCOPE GUARDRAIL.**

SAPIENT is a key donor and stress test, but it also demonstrates why donor compatibility cannot mean wholesale donor-model absorption.

---

# 9. Inside-out test — what scope is implied by the best relevant donor contributions?

The inside-out test begins with the strongest useful contributions identified across the donor pool, then asks what kind of subject would coherently need all of them.

## 9.1 Contributions that cluster around the persistent subject

Across independent donors, the strongest recurring subject-centered contributions include:

- durable identity and source-recognized identifiers;
- individual instance versus reusable type/model/kind;
- enduring composition and component identity;
- function/capability/performance;
- configuration, modes and allowed settings;
- current state/condition/health;
- calibration/quality/characteristics;
- interfaces and communications participation;
- power/energy characteristics and state;
- software/firmware/version information;
- observations/measurements/detections and other outputs;
- commands/actions/tasking and execution/result distinctions;
- events/history/service changes;
- semantic definitions, quantities and properties;
- provenance/source/responsibility.

These contributions are coherent around a technical subject that is **operated, configured, observed, tasked, maintained and interpreted over time**.

## 9.2 Contributions that consistently sit around the subject rather than define it

Other strong donor contributions repeatedly appear as typed context:

- Host/Platform;
- Deployment/emplacement;
- network topology;
- management/controller/server relationships;
- FeatureOfInterest/target;
- external operators/organizations;
- mission/activity/fusion context;
- digital representation/proxy/service;
- product/model/datasheet;
- source documents and provenance agents.

These are important to understanding the subject, but the donor evidence repeatedly warns against making them intrinsic composition by default.

## 9.3 Contributions that are specialization-level rather than universal

Several donor families contribute rich semantics that are useful only when applicable:

- radiation spectra, isotope identification and alarms;
- unattended-ground-sensor detector/cue semantics;
- detailed power/energy management;
- cybersecurity capability baselines;
- industrial automation specializations;
- maintenance/reliability/prognostics;
- sensor-network clustering/fusion;
- domain-specific instrument taxonomies.

A coherent DIM should be able to accommodate these without forcing every System to carry them.

## 9.4 Resulting semantic accommodation envelope

When the best **relevant** donor contributions are combined, the natural scope does **not** look like:

> all concepts present in all donor standards.

It looks like:

> **the common semantics needed to identify and understand an equipment-realized, sensing-oriented technical System as a persistent operational subject, including its meaningful internal structure and behavior, while preserving explicit relationships to the contexts, representations, evidence and specializations that surround it.**

This is compatible with the Pass 1 hypothesis.

More importantly, the inside-out test and the outside-in boundary test are now converging on substantially the same subject.

---

# 10. Counterexample matrix

| Counterexample | Would it fit the current hypothesis? | Pass 2 interpretation |
| --- | --- | --- |
| atomic BME280 sensor | **Yes** | equipment-realized, sensing-oriented, atomic; optional rich structures remain absent |
| composite weather station | **Yes** | whole remains sensing-oriented despite multiple sensors/computation |
| camera with internal actuator/computation | **Yes** | internal non-sensing functions do not defeat sensing orientation |
| multi-detector radiation portal | **Yes** | composite sensing equipment with meaningful detector decomposition |
| UGS sensor with cued external imager | **Yes, with typed relationship** | cueing does not automatically make the imager intrinsic composition |
| sensor mounted on reusable UAV | **Yes, with host separation** | sensor and host Platform may remain distinct; deployment/hosting expresses relationship |
| pure actuator/valve controller | **Not automatically** | donor semantics may be reusable, but current sensing-oriented boundary excludes it unless scope is deliberately expanded |
| SAPIENT soft-kill effector | **Not automatically** | same boundary issue as pure actuator |
| SAPIENT fusion node/system hierarchy | **Not as one intrinsic equipment subject by default** | operational/fusion context may relate multiple in-scope subjects |
| WoT Virtual Thing/cloud service | **Not as equipment realization** | may represent/mediate an in-scope subject without becoming that subject |
| human observer | **Not under present Equipment boundary** | CSAPI/SOSA can model it, but current V2 does not automatically include it |
| simulation/prediction System | **Not under present Equipment boundary** | possible future realization/profile; not forced by donor reuse |
| generic OPC UA drive/PLC/gateway | **Not automatically** | OPC contributes reusable device semantics; donor conformity alone does not put every device in V2 scope |

---

# 11. Pass 2 verdict on the current synthesized hypothesis

The hypothesis **survives the stress test**.

No reviewed counterexample currently requires abandoning the core idea of:

- an individual persistent subject;
- equipment realization;
- sensing/observing as its defining orientation;
- atomic-to-composite scale;
- enduring composition distinct from host/deployment/network/management/target context;
- explicit separation of kind/model, capability, configuration, state, interactions, outputs/actions, history and provenance.

However, Pass 2 makes three refinements important enough to carry forward.

## Refinement 1 — sensing-oriented means primary/defining orientation

The subject may perform or contain actuation, computation, communication, management and other functions.

The present boundary excludes **pure non-sensing top-level subjects** unless the project later chooses to broaden it.

## Refinement 2 — the equipment boundary is relational, not noun-based

A host-like structure can be intrinsic if it is genuinely part of the enduring sensing System. A thing called a Platform can be contextual in one case and integral in another only if the source semantics support that relationship.

The DIM must preserve the relationship meaning rather than classify by label.

## Refinement 3 — donor compatibility is contribution-scoped

V2 should preserve the meaning of adopted/mapped donor contributions for in-scope systems.

It should **not** promise whole-standard compatibility merely because a donor contributed one useful semantic pattern.

---

# 12. Refined hypothesis after Pass 2

Pass 2 supports a slightly more precise version of the working hypothesis:

> **The DIM appears to be converging on an individually identifiable, persistently describable, equipment-realized System whose defining operational orientation is sensing/observing, but which may contain or perform non-sensing functions. The subject may be atomic or composite; its enduring composition can be distinguished from hosting, deployment, network, management, target, and digital-representation context; and its kind/model, capabilities, configuration, state, interactions, outputs/actions, history, and provenance can be represented without conflating those concerns with the subject itself.**

This is still a **research hypothesis**, not the final formal scope definition or a proposed new class name.

The main change from Pass 1 is not a broader scope. It is a more precise interpretation of **sensing-oriented** and a clearer statement that digital representation is another relationship/context distinction.

---

# 13. Implication for the eventual scope definition

The outside-in and inside-out methods now converge on a useful scope test.

A candidate V2 scope is defensible if it can answer both questions:

1. **Boundary test:** Does this concept describe or materially contextualize the persistent equipment-realized sensing subject?
2. **Accommodation test:** If an in-scope CSAPI-integrated system carries an adopted donor semantic, can V2 preserve that meaning recognizably without importing unrelated donor-domain machinery?

For each donor concept that fails one of these tests, V2 should decide explicitly whether it is:

- outside scope;
- contextual;
- specialization-only;
- profile/binding-level;
- implementation-only; or
- evidence that the current domain boundary is genuinely too narrow.

This is a more empirical route to scope than either inventing a name first or accumulating every donor field.

---

# 14. Recommended next step

Pass 2 has reduced the boundary problem enough that the next useful work should move from **what the subject is** to **the exact concepts needed to describe it**.

The recommended next phase is **canonical concept consolidation**, beginning with the distinctions that now have the strongest pedigree and greatest structural leverage:

1. individual System identity;
2. product/model/kind;
3. Procedure/Method;
4. physical/equipment composition and component standing;
5. representation/proxy/digital identity.

These concepts should be consolidated before capability, configuration, state and dynamic interactions because mistakes in identity/type/composition would contaminate everything downstream.

The objective is not to design modules yet. It is to determine:

> **what each common concept means, which donor owns the strongest semantics, how other donors map to it, and where mappings must remain partial or specialized.**

## References

Bosch Sensortec. 2024. *BME280 Combined Humidity and Pressure Sensor: Data Sheet*. Revision 1.24. February.

Defence Science and Technology Laboratory. 2026. “SAPIENT: How It Works.” GOV.UK. Published October 14.

IEEE. 2024. *IEEE Standard for a Smart Transducer Interface for Sensors and Actuators—Common Functions, Communication Protocols, and Transducer Electronic Data Sheet (TEDS) Formats*. IEEE 1451.0-2024.

National Institute of Standards and Technology. 2024. “IEEE 1451.0-2024 Standard Published Under Leadership of NIST Researchers.” July 1.

Open Geospatial Consortium. 2025a. *OGC API—Connected Systems—Part 1: Feature Resources*. OGC 23-001, version 1.0. July 16.

Open Geospatial Consortium. 2025b. *OGC SensorML Encoding Standard*. OGC 23-000, version 3.0. July 16.

OPC Foundation. n.d. *OPC Unified Architecture Part 100: Devices*. Version 1.05.0.

World Wide Web Consortium. 2023. *Web of Things (WoT) Architecture 1.1*. W3C Recommendation. December 5.

World Wide Web Consortium and Open Geospatial Consortium. 2026. *Semantic Sensor Network Ontology—2023 Edition*. Working Draft, October 21. OGC 25-022.
