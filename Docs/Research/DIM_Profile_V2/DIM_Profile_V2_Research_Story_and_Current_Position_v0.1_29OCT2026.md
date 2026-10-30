# How We Got Here, What We Learned, and Where the DIM / CSAPI Profile Work Stands

**A plain-language research narrative and orientation for the DIM / CSAPI Profile V2 effort**

**Version:** 0.1 — 29 October 2026 (US Eastern)  
**Standing:** **Historical and explanatory orientation; current through completion of the original 12-step donor-alignment plan and the subsequent 6-step donor-neutrality challenge.** This is **not a PITON**, a normative DIM, a CSAPI Profile, a model adoption decision, an active plan, a new work authorization, or a substitute for source-specific research.  
**Home:** `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, folder `Docs/Research/DIM_Profile_V2/`.  
**For future PITONs:** Link this narrative as **the explanation of why the effort exists, how its research developed, what we actually accomplished, and what remains to be accomplished**. Use the [original problem/outcome baseline](DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md) for purpose and controlling scope, the [closed six-step tracker](PLAN_DIM_Profile_V2_Donor_Challenge_v0.1_28OCT2026.md) for plan status, the [candidate DIM v0.2](Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md) for latest candidate manuscript wording, and primary donor documents for exact definitions. If later work changes the situation, **version this narrative or explicitly date an addendum; do not quietly change the meaning of what was known on 29 October 2026**.

---

## 1. The one thing this project is ultimately trying to accomplish

We began with a simple but difficult interoperability problem: **how could one OGC API – Connected Systems (CSAPI) client present the important information about different manufacturers' sensing equipment in a useful, consistent Resource Details experience, without losing what makes each system distinctive?**

The original examples were the **TRSS** and **OmniSense II** unattended ground sensing (UGS) systems. Both describe real sensing equipment and many similar areas of concern: detector or transducer arrangements, manufacturer identity, capabilities, configuration, operating modes, power, communications, operational condition and management. But they use different source terminology, organizing structures, values and user interfaces. The original challenge was not to make the vendor screens look identical. It was to make a *common client* capable of interpreting the meaningful information from either source while preserving its actual differences. See the [project's controlling problem statement, §1](DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md#1-the-problem-in-the-owners-terms).

CSAPI already helps us integrate diverse systems behind common web resources. Sensor Model Language (SensorML) provides powerful descriptions of physical and functional sensing systems and processes. But **common technical access does not guarantee common semantic understanding**. A generic client may retrieve a correct property or a rich SensorML document without knowing whether it is looking at a manufacturer model, an installed detector, a supported option, a current operating mode, a measured voltage or an estimated remaining-capacity percentage. If the integrator throws away source meaning, the client cannot reconstruct it. Alternatively, the data may be present but a generic client may fail to recognize or organize it. **We have not shown that CSAPI or SensorML inherently destroys vendor information; the loss point must be tested rather than assumed.**

This is why the project needs more than a new UI layout. It needs an *agreed way to understand the information* and an *agreed way for implementations to communicate that meaning*.

## 2. The proposed solution, with the jobs of each part kept separate

We established a sequence of related but different deliverables:

1. **Investigate actual manufacturers and existing standardization sources.** Find what each source describes, the problem it solves, and its authoritative distinctions, rather than inventing a model from intuition.
2. **Develop an implementation-independent Domain Information Model (DIM).** Define the subject, relevant meanings, meaningful distinctions, relationships and justified specializations without tying their identity to a particular JSON field, API or UI tab.
3. **Develop a separate CSAPI Application Profile.** Select how appropriate DIM meanings are carried by the *existing* CSAPI, SensorML and related structures. Add only justified, testable conventions or requirements needed to make the communication predictable; do not casually copy donor-specific SHALLs.
4. **Build faithful source-to-CSAPI integrations and a profile-aware client.** The producer must preserve and publish sufficient information. The client must recognize the specified interpretation and present useful details without manufacturer-specific hard-coding or fabricated missing facts.

The intended conceptual path is **vendor/source information → donor-supported DIM meaning → selected CSAPI Profile convention → actual producer representation → common client interpretation → source-fidelity check**. The [original problem baseline §2 and §5](DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md#2-the-proposed-solution-chassis--dim--profile--client) explains the division. **The DIM is not the Profile; the Profile is not the UI; and a mock UI is not proof that a producer implements the Profile.**

A successful client would have recognizable organization—identity, equipment, capabilities, configurations, operating condition and so forth—while showing specialized source details only where they are actually supported. A client's job is to interpret the information with appropriate qualifications, not to turn everything into identical fields. Nor should the client simply duplicate the vendor's screen pixel for pixel. This is a **common understanding and presentation problem**.

## 3. Why the research grew into a large standards-donor corpus

When we considered writing a DIM, the user challenged the project to ask what standards organizations, commercial industries, government programs and technical communities had *already* solved. We did not want an impressive custom model that reinvented mature engineering work or picked arbitrary new classes simply because they sounded plausible.

The resulting research corpus grew to **182 frozen source artifacts**. An artifact is a traceable publication, standard edition, schema, research paper, official guidance, source repository or companion technical item. **It is not necessarily an independent standard.** For example, SAPIENT has a BSI primary specification and several Dstl companion sources, including official Protocol Buffers, middleware implementation and test-harness material. They belong to one donor lineage, not five separate votes for the same idea. The [frozen accountability register](Donor_Alignment/03_Source_Accountability_Register.csv) and the [earlier 30-lineage extraction](DRAFT_DIM_Profile_V2_Anatomy_PhaseA_Independent_Extractions_v0.1_26OCT2026.md) were created to make this explicit.

A *donor* is not an authority over our whole model simply because we included it. A donor contributes source-defined concepts, relationships, information structures or tested integration patterns **within its original scope**. Sometimes it supplies a potentially common domain meaning. Sometimes its useful contribution is a specialized data model or an architecture that warns us against making an unsafe equivalence. Sometimes an implementation example helps demonstrate what a standard can carry, without being independently normative.

Our research initially suffered from **selection bias**: the standards discovered early influenced our evolving descriptions more than later, potentially stronger contributors. The first twelve-step plan produced a disciplined starting point, but the later six-step challenge had to correct this imbalance. The important correction was **not to require a donor to define our entire DIM chassis before allowing it to contribute to a specific domain meaning**.

## 4. What we mean by the provisional “chassis” — and why it has not been chosen

The original chassis question was: *What kind of complete, bounded real-world thing are we trying to describe, how does the standardization world classify it, and what relationships organize its important parts and activities?*

For our first equipment cases, the working focus is **individually describable, equipment-realized Systems whose primary operational role is sensing or observing**. Such a System may also incorporate equipment and activities for power, communications, computation, recording, command, security, maintenance and deployment. CSAPI's source-native classifications `systemType = Sensor` and `assetType = Equipment` express two relevant facets; they do **not** establish a new universal compound class called SensorEquipment. See the [candidate foundation v0.2 §1.2](Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md#12-working-subject-boundarydescription-is-not-root-class-adoption).

A complete sensing System is not necessarily a single circuit board, a housing, a network Node, a digital twin, a transducer, or a manufacturer's product category. The word *chassis* is useful as a design/research metaphor, **not** an approved UML superclass, product taxonomy or the name of the DIM. Our exact future scope/name/root has deliberately been left **open to discovery from donor evidence**. The earlier artificially promoted *Anatomy Phase B/C/D* structure remains **quarantined** and is not the accepted foundation.

The key architectural insight is that **the donor best suited to the whole-System boundary need not be the donor best suited to everything inside the System**. One source can define its sensing functions, another its transducer calibration and channels, another its power or status, and another its physical and managed relationships. They may still disagree in important ways. Our work must make those differences explicit instead of forcing them into one broad but imprecise class tree.

## 5. The first twelve-step research plan: what it actually did

The [twelve-step plan](PLAN_DIM_Profile_V2_Donor_Alignment_and_Foundation_v0.1_28OCT2026.md) **completed all twelve authorized research/documentation tasks** on 28 October 2026. It did not complete the DIM itself. The [independent Step 12 audit](Donor_Alignment/12_Completion_Audit_and_Recommendations.md) supplies the exact validation and limits.

**Steps 1–3 organized the sources and method.** We checked the frozen artifact population and classifications, established how to distinguish native source meaning from our proposed mapping, and made it possible to trace particular conclusions to specific editions. This reduced the risk of silently changing donors or mistaking one author's implementation for a universal standard.

**Steps 4–8 asked five foundational domain questions**, rather than attempting an impossible source-by-source comparison of all 182 artifacts. The initial questions became **F-01 through F-05**: individual System subject; reusable product kind/model; Procedure/Method versus actual performance; composition/component standing; and real-world equipment versus digital representation/proxy identity. The detailed work yielded **48 unique source-concept alignment records from exactly 12 frozen source artifact IDs**, **one of those source comparisons explicitly deferred**. It did **not** examine all donors, nor did 48 records represent 48 independent standards.

**Steps 9–10 reconciled the source meanings and created the first candidate DIM prose.** We found, for example, that CSAPI may use a `Procedure` resource in both a kind/datasheet relationship and a supported method relationship, but those relationships don't mean the same thing. We also rejected easy but false substitutions, such as treating a vendor's product Model, OPC UA `DeviceType` and a WoT Thing Model as one generic class. The outcome was [Candidate DIM v0.1](Donor_Alignment/10_Candidate_DIM_Foundation.md): an actual, source-linked explanatory manuscript about *part* of the domain, **not** five approved classes or a complete model architecture.

**Steps 11–12 checked the value and integrity of that starting point.** We compared the meanings against TRSS, OmniSense and Smart Citizen source cases, inspected the separate Glaux interpretation experiment, and audited the references and research records. That exercise exposed missing whole-System subject matter, particularly operational condition, power, diagnostics and rich configuration. It also identified interpreter limitations. The twelve-step effort **passed as bounded research and documentation, not as proven source-to-CSAPI-to-client interoperability**.

The primary shortcoming we recognized afterward was that **SAPIENT and IEEE 1451**, although recognized in our broader corpus and earlier screening, had not been given the same detailed concept-by-concept challenge to the first five meanings. The donor choice was still narrower than the accumulated evidence justified.

## 6. The second six-step donor challenge: why it happened and what it accomplished

The [six-step challenge plan](PLAN_DIM_Profile_V2_Donor_Challenge_v0.1_28OCT2026.md) **finished all six authorized steps on 29 October 2026 and is CLOSED**. Its purpose was not to restart the original research, select a new chassis, or launch an unlimited survey. It was to ask whether previously underused donors could strengthen or overturn the *five* candidate meanings already in our manuscript.

**Step 1 compared our existing 30 donor lineages against F-01–F-05**, preserving which sources had already been deeply studied and which needed additional concept-level attention. That selected four substantive challenger families: SAPIENT v2, IEEE 1451, Integrated Sensor Architecture (ISA), and The Open Group SOSA. Other families, including PA-DIM, Redfish/CIM, MIMOSA, IETF hardware models, LwM2M and the rest, retained topic-specific future relevance rather than being declared irrelevant.

**Step 2 directly examined SAPIENT v2**, its BSI interface specification, official pinned Dstl schemas and bounded companion implementation evidence. It found important distinctions among identity, declared capability, supported mode, selected/current mode, status reporting, task request, acknowledgement and actual detection. The work also found a concrete **published BSI Registration field-number versus pinned protobuf discrepancy**, which remains unresolved. See the [SAPIENT challenge report](Donor_Challenge/02_SAPIENT_Challenge.md).

**Step 3 examined IEEE 1451 and ISO/IEC/IEEE 21451**, especially smart transducer, TIM/NCAP, addressable channel, and TEDS meanings. The first draft underused our extensive prior public-source research, and the user rightly challenged that. The [corrected IEEE report](Donor_Challenge/03_IEEE1451_Challenge.md#0-corrective-evidence-finding--ieee-1451-is-technically-usable-as-a-dim-donor-28-october-2026) expressly recovers the current **2024-linked IEEE 1451 Playground**, detailed Meta/Transducer Channel/Optional TEDS technical information, NIST research, 1451↔Web of Things research and historical IEEE↔OGC SWE prototype evidence. **IEEE 1451 is a substantial, usable conceptual and technical donor NOW.** What remains limited is verification of exact, uninspected full licensed 2024 normative requirements/cardinalities/conformance, not access to its useful technical ideas.

**Step 4 examined ISA and The Open Group SOSA from their supplied original sources.** ISA establishes that internal equipment may be visible, opaque, virtual, transparent or translucent through a Composition Interface Component; **external representation and taskability are not physical membership**. The Open Group SOSA provides particularly strong whole-Sensor organization: one bounded Sensor, multiple hardware elements, functional/software Components, manufactured Products and implementations, a distinct Host Platform, and separated system management and mission tasking. Its **Edition 1.0 DSDM and Edition 1.1 C239 architecture are distinct**, and The Open Group SOSA is **not** the W3C/OGC SOSA/SSN ontology. See the [ISA/SOSA challenge report](Donor_Challenge/04_Other_Structural_Challenges.md).

**Step 5 reconciled those four donor families against our original five meanings and 48 records.** The narrow five distinctions were still defensible; **none had to be discarded solely on the evidence reviewed**. But F-03 and F-04 were **materially incomplete** for rich whole-System operation and equipment structure. F-02 and F-05 needed much stronger source-scope qualifications, while F-01 needed a better account of the whole physical subject versus an interface participant. Seven source-derived gap flags were consolidated into five **overlapping research questions, not five new classes**. See the [Step 05 reconciliation](Donor_Challenge/05_Challenge_Reconciliation.md).

**Step 6 incorporated the earned improvements into a separate complete candidate manuscript**, [Candidate DIM v0.2](Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md). It retained the earlier F-01–F-05 distinctions and `REL-01`–`REL-10` candidate relations, made the stronger donor findings explicit, added source pedigree, and preserved unresolved questions. [The Step 06 change record](Donor_Challenge/06_Candidate_Foundation_Amendments.md) explains each edit. Original v0.1 remains byte-for-byte unchanged. **Step 6 did not decide any final classes/root, write normative Profile requirements, or touch the deployed client**.

In other words: **the first plan gave us our first defensible piece of DIM prose; the second tested its donor choices and turned it into better-informed candidate prose**. Neither plan built a finished model.

## 7. What the five candidate DIM meanings now say, in normal language

These are *connected distinctions*, **not five mandated classes**, five API resource types, five modules or a finished set of model definitions. The source-grounded details and original records are in [candidate v0.2 §4–5](Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md#4-candidate-concept-meanings-and-their-donor-native-boundaries).

### F-01 — Which real System is this information about?

A **particular equipment-realized sensing System** is not its manufacturer's product family, its resource URL, a serial number alone, or its software description. It may be a whole operational Sensor containing multiple hardware elements, as The Open Group SOSA illustrates. An ISA Component, SAPIENT Node, IEEE NCAP/TIM, or software proxy might participate in exposing information about that real System **without itself being that real whole**. We must have source-backed referent evidence before asserting that two identifiers describe the same physical individual. The final domain root and universal lifetime/replacement identity policy remain **OPEN**.

**Client consequence:** Do not mint fictitious physical Systems from every interface participant, virtual member or channel identifier. Show an individual unit's verified identity separately from network identifiers and manufacturer models.

### F-02 — What does a type, model, role or datasheet actually describe?

A **manufacturer product model** can characterize multiple actual units. But `type` might instead mean a sensing modality, a functional software role, a sensor design alternative, a standardized interaction template, or a channel-scoped electronic description. SAPIENT separates `NodeType` from reported manufacturer `model`; The Open Group SOSA separates Product/ProductInstance from functional Component_; IEEE TEDS supplies detailed module/channel/calibration-specific descriptions. These are not automatically one global `ProductModel` class.

**Client consequence:** “Seismic sensing role,” “TRSS manufacturer model,” “optional detector,” “IEEE channel physical units and uncertainty” and “installed detector configuration” should not be presented as five interchangeable kinds of product identification.

### F-03 — What can it do, what is it doing, and what actually happened?

The earlier distinction **reusable Procedure/Method ≠ executed event** remains valid but is **too coarse**. SAPIENT distinguishes declared abilities, supported modes, current mode/status, requested Tasks, acknowledgements and detections. ISA distinguishes declared Properties/Observables/Commands from Status/Event/Request/Response information. The Open Group SOSA separates keeping the Sensor functioning (System Manager) from executing mission tasks (Task Manager), and distinguishes test definition from performed built-in-test results. IEEE TEDS and available transducer services are not the same as actual measurements or calibration events.

**Client consequence:** “Supports mode X” is not “currently operating in mode X”; “Task accepted” is not “Task completed”; a successful communication or diagnostic is not necessarily evidence of a detection or completed observing procedure. This distinction is fundamental to operational usefulness.

### F-04 — What is a constituent, and what kind of relationship connects it?

Physical *part-of* is not the same as a functional module, manufactured-product realization, software interface, sensor channel, hosted-on platform, network dependency, or temporarily deployed subsystem. The Open Group SOSA differentiates `SensorComponent`, `ModuleImplementation`, `ProductInstance` and `HostPlatform`. ISA differentiates actual internal member, external visibility, virtualized identity and separate taskability. SAPIENT differentiates `sub_components` configuration descriptions from `dependent_nodes` operational effects. IEEE's TransducerChannel is distinct from the physical chip and the client-facing DataStream. We must also decide separately when an internal element warrants independent System description.

**Client consequence:** One SHT31 chip reporting temperature and humidity is not automatically two physical Systems; one source software `Component` is not automatically a board; five reported OmniSense transducer labels are not five authenticated unique hardware IDs; an ISA-hidden member has not ceased physically existing.

### F-05 — What representation or message is this, and how authoritative/current is it?

The equipment is distinct from the description, API resource, software association or proxy that talks about it. A mediator might publish information that originated elsewhere; a digital record can describe a product kind, whole System, part, channel, function or virtual actor. A stored status value might be historical, cached or derived rather than a new measurement. Its subject, original producer, time, value type, source edition and reporting path may matter. None of these facts can be reconstructed by assuming one resource ID means one unit of hardware.

**Client consequence:** A reported value must keep its units, source, subject and status as far as the source supports them; no old or estimated value should silently become current physical fact. A proxy's identity is not by default the actual sensor's identity.

### The underlying discovery

**All five are questions about what information is *really about*.** They are not yet full descriptions of physical inventory, electrical power, communications, security, lifecycle, diagnostics or observation/output schemas. Those are still major whole-System areas requiring work. The novel value of the first five is that they protect **semantics and reference relationships** so subsequent specialized descriptions can be organized honestly.

## 8. The equipment cases show why this is engineering rather than terminology

### TRSS and OmniSense — similar user questions, different facts

One historical TRSS ETU-II fixture describes detector configurations, including a specifically designated **Detector 1 SEISMIC/ACOUSTIC** and a **Detector 2 IRID-II** source case. It also contains an **estimated remaining battery capacity of 100%** along with estimator status and inputs. That **does not** prove 100% actual measured capacity, readiness or voltage. A separate OmniSense **Core2** case contains **five reported transducer labels** but not five proven independent physical identities. A different OmniSense **Core5ADS** source case has **15.43 V DC reported electrical information** and **six distinct diagnostic findings**, as well as a source clock whose validity/time zone was not established. **Core2 and Core5ADS are different fixture contexts and must not be blended into one invented installed device.**

A naive common UI might put all of these numbers under `Battery/Health` and normalize them into one percentage or a green `Healthy` status. That would discard their original meaning. Estimated capacity, reported voltage, a diagnostic `Pass` result, current operating mode and overall readiness are **different kinds of claims**. They need source-qualified descriptions and, ultimately, a more developed model of condition, measured/estimated quantities, diagnosis and time. See the [original Step 11 source-to-UI fidelity review](Donor_Alignment/11_Source_to_DIM_to_Profile_to_UI_Check.md) and the [twelve-step audit's explicitly unstarted condition/status recommendation](Donor_Alignment/12_Completion_Audit_and_Recommendations.md#7-one-bounded-next-subject-to-recommend--no-execution-authorized).

### Smart Citizen Kit 2.3 — manufacturer product design is not a verified physical installation

The independent Smart Citizen case gives us a commercial product stress test. Its source documentation describes Data and Urban Boards, an in-enclosure cabled particulate-matter module, an **SHT31** chip supporting temperature and relative humidity, and an **AS7331** chip associated with multiple ultraviolet outputs. A manufacturer may document supported sensor variants or functions without proving which variant is installed in a particular customer's unit. The Smart Citizen backend also uses `Component` for a **Device–Sensor-definition database association**, not necessarily a removable physical integrated circuit. Those distinctions exposed concrete false hypothetical mappings.

Nothing in that product documentation proves a particular authenticated Kit's actual identity, installed component list, IEEE 1451 compliance, live Observations or DataStreams. A candidate DIM must distinguish **design/specification evidence** from an **individual deployed System**, and **physical hardware** from **channels/software data objects**. See the [Smart Citizen I13 integrated case report](Case_Studies/Real_Equipment_DIM_Validation/I13_Integrated_Smart_Citizen_Case_Study_and_Gate_D_v0.1_28OCT2026.md) and [critical I12 mapping corrections](Case_Studies/Real_Equipment_DIM_Validation/I12_Critical_Interoperability_Challenge_v0.1_28OCT2026.md).

### Three different levels of possible information loss

A vendor's original system may have the right information. A source-to-CSAPI converter may **fail to publish it**. Or the converter may publish it correctly but a **generic client fails to interpret it**. Those are not equivalent defects. A rigorous future test must compare **original source fact → produced CSAPI representation → Profile expectations → actual client rendering** and identify precisely where a distinction was preserved or lost. Do not claim that CSAPI itself lacks a capability merely because one prototype renderer doesn't recognize a source field.

## 9. What the Glaux experiment proves—and what it does not

Our separate [Profile-aware Resource Details test](https://glaux-client.pages.dev/?page=resource-details-profile-test) was an early, deliberately controlled experiment on the independent app branch `work/details-view-20261023`. It compares a generic field-listing view and a candidate term-aware Details view in the same layout, with Smart Citizen **product-design facts** and synthetic/historical TRSS and OmniSense cases. The owner's feedback was **“janky but on the right path”** as a primitive exploration—not approval of a final user interface or Profile.

The [source-to-UI audit](Donor_Alignment/11_Source_to_DIM_to_Profile_to_UI_Check.md) inspected **76 source input fields across four cases**: **55 term-suffix rule matches**, **15 fixture provenance-only fields**, and **six Core5ADS diagnostic fields that remained in an unknown/raw fallback**, using **31 hand-authored rules**. These are code/fixture counts, **not** claims of 55 semantically correct standard mappings, 76 real CSAPI observations, interoperability coverage or successful live browser testing. In particular, matching only the suffix of a definition URI is not sufficiently rigorous to interpret an adopted Profile. The deployment had 80 offline tests, but the source-to-producer-to-client chain wasn't validated in a fielded-device integration.

The **direction of travel is promising**: a common interface could give richer equipment details when it recognizes meaningful information. But a useful prototype is **not** a complete DIM, a normative Profile, a valid producer translation, or proof that all vendor semantics survive the pipeline. We must not use the apparent success of a screen to claim those things.

## 10. What it means to use donors *compatibly*

We want the DIM to **respect and reuse** source-standard meanings, and ideally support a well-defined translation of relevant information from a system already using one of those standards. But **reusing a donor's domain concept is not the same as implementing or conforming to that donor's entire native interface**.

For example, IEEE 1451 might supply an authoritative technical understanding of TEDS and channel properties while the eventual Profile uses SensorML/SWE Common structures to represent *some* of that information through CSAPI. That would be **semantic reuse or a verified scoped translation**, not evidence that the CSAPI server itself is a 1451 NCAP. Likewise, faithfully mapping SAPIENT's TaskAck/Mode/Status differences doesn't automatically make the CSAPI Profile SAPIENT-conformant. Our interoperability claim must state **which source meanings and scenarios are supported, which are qualified/omitted, what code actually runs, and what was tested**.

One source's `Component` or `Type` may overlap another's but not be equal to it. Where a donor explicitly adopts or cites another standard, record the precise clause/edition and the nature of that relationship. Where we *propose* that concepts line up, call it **analyst inference** until actual mapping and tests justify a stronger claim. The earlier [Step 09 cross-concept reconciliation](Donor_Alignment/09_Cross_Concept_Reconciliation.md) and the [six-step Step 05 reconciliation](Donor_Challenge/05_Challenge_Reconciliation.md) deliberately preserve these distinctions.

This gives us a realistic goal: **source-qualified compatibility for defined scopes** instead of saying “our DIM complies with all 182 donor artifacts.” The latter is neither what was tested nor how the donor population is structured.

## 11. So where are we actually, and how much is left?

**We have completed two bounded plans: twelve steps and six steps.** Each plan is fully complete **as the specifically authorized research/documentation effort**. The first built a traceable candidate foundation and tested it against example-source/UI questions. The second fixed a source-selection blind spot, evaluated four significant challenger donor families, reconciled those findings and produced a stronger **candidate DIM v0.2**. The completed work is serious research progress; **it is not an 18-step completed DIM**.

We now have **(a)** a stable source-accountability structure; **(b)** a repeatable way of distinguishing source-owned facts and our proposed mappings; **(c)** an actual publication-oriented candidate manuscript for five meaningful concepts; **(d)** an enriched understanding of whole Systems, technical channel description, task/status roles, components and digital representation; and **(e)** explicit case-based evidence of how a common client could go wrong. These are useful outcomes.

**What remains incomplete is substantial.** The model still needs adequate whole-System coverage of power sources and quantities, operational condition/diagnostics and recovery, communications, configuration/control, measurement performance and outputs, actual Observations, deployment and hosting across time, security, software/firmware, maintenance and lifecycle. We have not chosen a defensible final domain name/root, accepted classes and associations, class/property cardinalities, cross-cutting source-value/provenance structures or formal module design. That work may require additional donor comparisons and equipment evidence. The eight V1 information subjects and provisional blueprint are **inputs to the question**, not eight approved future modules.

**The CSAPI Profile has not been authored as a completed normative specification.** Its eventual bindings, requirements, inheritance, versioning and conformance tests must follow justified DIM choices and an actual interoperability case. **The Glaux prototype has not demonstrated live source-to-profile-conforming-CSAPI-to-client behavior across authenticated vendor equipment.** No current percentage of overall project completion is justified; two completed research plans do not define the unknown total effort.

The old [Step 12 audit](Donor_Alignment/12_Completion_Audit_and_Recommendations.md#7-one-bounded-next-subject-to-recommend--no-execution-authorized) singled out **evidence-qualified operational condition and status** as a *promising possible next subject*, particularly because of the TRSS capacity estimate and OmniSense voltage/diagnostic contrast. Donors such as SAPIENT, ISA, The Open Group SOSA, PA-DIM, Redfish, MIMOSA, IETF Energy Management and IEEE 1451 could contribute different pieces. **This subject has not yet been initiated as a new campaign**, and no successor plan was authorized when the six-step challenge closed.

## 12. What was good about the work, what went wrong, and what future work should change

The strongest improvement was in **technical accountability**: stable source references, edition-aware mapping, explicit negative findings, and a willingness to retain unresolved questions rather than invent classes or requirements. We corrected real donor-selection bias, recovered detailed IEEE evidence that had been underweighted, preserved the original manuscript when producing v0.2, and kept the client and frozen source corpus separate from the research. These protections matter for a publishable model.

The biggest process failure was **communication with the owner**. Too many iterations reported documents, counts, commits and status labels while failing to explain in ordinary language what the source taught us or why it mattered to the original problem. A complete GitHub artifact is not sufficient if the owner cannot tell whether our conceptual understanding improved. A future iteration should lead with three ordinary explanations: **what we learned**, **what it changes or fails to change about our understanding/model**, and **how it could help a common CSAPI client preserve real equipment information**. The evidence record and repository references should *support* that explanation, not substitute for it.

Another lesson was that **limited access to the complete paid normative standard must not be confused with inability to study a donor seriously**. The corrected IEEE 1451 research explicitly demonstrates the difference. Publicly accessible technical forms, academic/research implementations, editor/sandbox tools and first-party explanations can be rich enough for **conceptual and field-level research** while still leaving exact normative SHALLs and compliance details unverified. This distinction should become a permanent habit across donor investigations.

A third lesson was to **make the actual interoperability problem visible during research**. The user's original concerns—detector choices, channels versus physical hardware, voltage versus battery estimates, operational state, command results, source attribution and common Resource Details—are not incidental illustrations. They are stress cases that can expose a bad model even when every definition sounds plausible. We should use them to challenge candidate meanings, but not fabricate an actual installed device or Observation when we have only a product manual or synthetic fixture.

## 13. How a future PITON or new chat should use this document

**This document is the human narrative, not an execution script.** It explains the project's *why*, the progression from original equipment problem to source donor investigation, what both completed plans achieved, and the meaning of the current limits. A PITON should link this narrative near its beginning so the next assistant can understand the work without simply re-running a status tracker or misreading “plan complete” as “DIM complete.”

Use sources for different purposes, in this order when resuming:

1. **[This research narrative](DIM_Profile_V2_Research_Story_and_Current_Position_v0.1_29OCT2026.md)** — understand the *story and purpose* in normal language.
2. **[Original problem/outcome baseline](DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md)** — authoritative definition of the user's objective and distinctions among DIM, Profile, producer and UI.
3. **[Candidate DIM foundation v0.2](Donor_Challenge/10_Candidate_DIM_Foundation_v0.2_Donor_Challenge.md)** with [Step 06 change record](Donor_Challenge/06_Candidate_Foundation_Amendments.md) — current source-qualified *candidate* manuscript and specific additions; preserve original [v0.1](Donor_Alignment/10_Candidate_DIM_Foundation.md) as historical predecessor.
4. **[Final six-step tracker](PLAN_DIM_Profile_V2_Donor_Challenge_v0.1_28OCT2026.md)** and [original twelve-step audit](Donor_Alignment/12_Completion_Audit_and_Recommendations.md) — exact *closed* statuses and test/evidence ceilings. The six-step plan is **6/6 COMPLETE**; the first twelve-step plan is **12/12 COMPLETE**. Both are **closed**.
5. **[Original 48-alignment reconciliation](Donor_Alignment/09_Cross_Concept_Reconciliation.md), [donor challenge Step 05](Donor_Challenge/05_Challenge_Reconciliation.md), and original source records** — inspect technical claims, donor native terms, frozen editions, original source-dependent requirements, negative mappings, and unresolved issues before proposing anything normative.

**What not to do:** A PITON must not restart either closed plan, silently treat an older README or historical PITON's “next Step 01/06/11” note as current authority, invent a successor plan, change the client branch or declare a final DIM root based on this explanatory text. The research branch is `research/dim-profile-v2`; the separate prototype code branch is `work/details-view-20261023`. Use explicit owner authorization for any *new* research plan, model design decision, Profile requirement or app action.

**A model of the user's desired progress report:** “We compared source X and source Y for [equipment meaning]. We found [specific agreement/difference, with original sources]. This changes our candidate understanding because [plain-language reason], but [source claim] is still unresolved. For TRSS/OmniSense/Smart Citizen this would prevent [a concrete false interpretation]. The GitHub evidence is [exact link]. The next bounded task would be [one understandable action]—**only after owner approval**.” The document explains the research so the owner never needs to take the latest “AI completed a report” message on faith.

---

## 14. End-of-chapter perspective

**The completed work is a significant improvement in the quality of our *foundation*, not the completion of the *building*.** We did not simply find four more donor standards. We found why the same physical System can legitimately have several kinds of descriptions and representations; why a system's kind differs from its installed state and allowed behaviors; why a physical component differs from an addressed channel, functional module and virtual interface; why the complete sensing System needs distinct mission and self-management meanings; and why source/temporal authority is crucial to a rich shared client.

A completed DIM and Profile still require much more work, especially whole-System information coverage, defensible conceptual structure, testable CSAPI representation choices and real producer/client validation. The virtue of the present candidate foundation is that it gives us **better questions and better-supported distinctions** for that work. The task going forward is not to generate more documentation because another plan can be imagined. It is to produce explained, source-backed improvements that can be traced from real equipment facts to a genuinely intelligible common interoperable Resource Details experience.

**As of 29 October 2026, both bounded plans are closed, candidate DIM v0.2 is the latest conceptual manuscript, no normative Profile or cross-vendor fielded integration is complete, and there is NO AUTOMATIC NEXT STEP.** The owner must explicitly decide the next bounded piece of work.

---

### Document provenance and limitations

This explanatory document was assembled from the user's original objective, the two completed repository research programs, direct source-challenge reports, case-study evidence and the candidate v0.2 manuscript. **It does not claim independent rechecking of every donor's primary standard.** If this narration conflicts with a verified source excerpt, exact edition, or a later dated model decision, **the source-specific evidence and approved later decision control**. Its references are links to authoritative internal research artifacts and a few external primary or implementation sources; no private attachments or copyrighted standards files are embedded here. This is designed to be **read, reviewed and referenced by future PITONs**, not to issue instructions or certify conformance.
