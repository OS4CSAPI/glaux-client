# Evaluating Sensor Information Preservation Through OGC Integration

*A Smart Citizen experiment with the MERLIN domain information model and managed physical sensing systems profile*

MERLIN Project

Working paper version 0.2 | 24 October 2026 | Study protocol and preliminary source assessment

## Abstract

Integrating a sensing system requires preserving the meaning of its information as well as transporting its measurements. An operator may need to distinguish a product model from an installed unit, a producing sensor from the subject it observes, and a reported condition from an interpretation of that condition. This paper defines a proposed experiment using public Smart Citizen data, an authored adapter, an OGC API Connected Systems service, and the Glaux client to evaluate the MERLIN domain information model and Managed Physical Sensing Systems profile. The study will combine published source definitions with captured responses, document each consequential transformation, and compare competent generic and profile-aware presentations of the same standardized resources. Each mapping will explain both its standard representation and its relationship to the underlying domain model and individually identified donor concepts.

Preliminary access checks establish that selected public measurements and aggregate history were retrievable; they do not establish a running adapter, a loaded CSAPI dataset, or a presentation benefit. The evaluation will report semantic preservation, domain coverage, and operator-facing utility separately. Initial diagrams and code fragments explain the proposed method. Paired source-interface and Glaux screenshots, executed mappings, and measured results will be added as evidence becomes available. The expected contribution is a reproducible account of which meanings survive integration, which require explicit enrichment, and which remain unsupported by the source.

**Keywords:** sensor integration; domain information model; SensorML; SWE Common; OGC API Connected Systems; semantic preservation; resource details.

## 1 Introduction

The MERLIN Resource Details effort began with the problem of presenting information from heterogeneous sensing systems in a consistent, useful view. TRSS and McQ OmniSense II remain motivating cases. The subsequent domain-model work expanded the inquiry from individual manufacturer screens to the physical sensing system in employment: its identity, equipment, functions, deployment, configuration, communications, power, and lifecycle. The retained MPSS draft organizes these concerns through eight information subjects and twenty relationship identifiers, R01–R20 (MERLIN Project 2026a, secs. 4–5).

The present question is whether this organization helps a client reconstruct useful meaning after integration. Receiving a temperature value demonstrates access to a measurement. It does not establish that the client can identify its producer, distinguish the sampled environment from the equipment, interpret its time, or explain how the information reached the application. Likewise, a populated battery field does not establish an identified power source or its relationship to the operating system. A useful experiment must make such distinctions inspectable rather than treating successful transport as sufficient evidence of semantic preservation.

Smart Citizen was selected as the first candidate because the preliminary study found accessible current and historical responses, informative channel metadata, official model documentation, and a plausible route to an owned physical kit. This is a purposive selection for an integration case study, not the outcome of an exhaustive device survey or a measured ranking of product quality. AirGradient was identified as a later independent comparison, while networking, acoustic, seismic, and radiation sources remain complementary candidates for other questions (MERLIN Project 2026c).

This paper is being written before execution of the proposed integration. Its purpose is to state what will be built, why the experiment is needed, how evidence will be collected and interpreted, and what would justify a conclusion. The initial staged plan is refined here by placing public-data integration before hardware acquisition (MERLIN Project 2026e). An owned kit is a later means of obtaining physical installation and lifecycle evidence. Deterministic captures will accompany live access so that the same observations can be examined throughout the integration chain.

## 2 Background and technical baseline

### Domain concepts and standards bindings

The study distinguishes domain concepts, standards mechanisms, and presentation decisions. The domain model identifies meaningful subjects and relationships. The MPSS working profile selects or authors bindings for those meanings. The client applies documented presentation rules to the resulting information. The profile does not prescribe a universal tab arrangement or require every device to populate every information subject (MERLIN Project 2026a, secs. 5.1, 7).

OGC API Connected Systems Part 1 supplies feature-resource mechanisms for systems, procedures, deployments, and related subjects. Part 2 addresses dynamic resources, including datastreams, observation schemas, observations, and control-related resources. These are approved standards in the inspected version 1.0 editions; a specific server must still be checked for the classes and operations it actually implements (Open Geospatial Consortium 2025a, secs. 7–15; 2025b, secs. 9–12).

SensorML 3.0 provides rich descriptions of processes and physical systems, including outputs, configurations, and related descriptive content. SWE Common 3.0 provides typed components, semantic definitions, units, structured values, and encoding mechanisms. Their official JSON schemas provide machine-readable structural constraints. These standards supply representation mechanisms; a structurally valid document can still identify the wrong subject or misinterpret a source field (Open Geospatial Consortium 2025c, secs. 8–9; 2025d, secs. 7–10; n.d.-a; n.d.-b).

The retained project baseline is MPSS v0.3.5, dated 17 October 2026. The first presentation comparison will use the recovered 560 × 440 CSS-pixel Resource Details frame. That frame is an existing review baseline with provisional layout choices; it is not evidence that the proposed Smart Citizen interface already exists or that the final PBI is complete (MERLIN Project 2026a; 2026d).

### Power as a discriminating example

Power illustrates why mapping requires more than matching labels. RFC 7326 distinguishes power-source, metering, and aggregation relationships. RFC 7577 defines battery-monitoring objects. MERLIN's selected OGC bindings remain project-authored uses of those donor meanings; neither RFC establishes a MERLIN screen layout or an automatic equivalence with a supplier's battery percentage (Parello et al. 2014, secs. 6.6, 8; Quittek et al. 2015, sec. 4; MERLIN Project 2026a, sec. 5.10).

The public Smart Citizen specimen reports remaining battery level as a percentage. That is useful measurement evidence, but it does not identify the installed battery, establish which source powers which equipment, or supply replacement history. The experiment will therefore distinguish successful preservation of the percentage from coverage of the wider power-arrangement model (MERLIN Project 2026b, record “smart-citizen-current-19639”).

## 3 Research questions and study design

The study proposes a traceable integration case. A controlled comparison of information presentation will follow that integration. Together, these stages address three research questions.

1. **Semantic preservation.** Which source-supported meanings survive acquisition, adaptation, CSAPI publication, retrieval, and presentation, and where does meaning become ambiguous or lost?
2. **Profile contribution.** Which operator questions become easier to answer through the DIM and MPSS when compared with competent presentation of the same standard resources without profile-specific organization?
3. **Coverage and transfer.** Which information subjects and relationships are exercised, and which mappings remain reusable when a second producer is introduced?

The unit of technical analysis is a traceable assertion: a value, identity, relationship, or contextual statement with an identified source and interpretation. A sample may contain several such assertions. The evaluation will avoid equating the number of observations with domain coverage or treating R01–R20 as twenty interchangeable checklist points. Findings about transport, interpretation, and presentation will be reported separately.

The immediate proposed path is public Smart Citizen acquisition through a documented adapter into an identified CSAPI test service, followed by Glaux retrieval. The exact server, write interfaces, version, adapter revision, and execution environment will be recorded before the first run. They are not selected by implication in this protocol. An owned kit is a later extension for facts that a public feed does not establish.

![Proposed architecture connecting source evidence, explicit mapping, a CSAPI service, and separate generic and profile-aware client inspection](figures/figure_01_architecture.svg)

**Figure 1. Proposed experiment architecture.** Source definitions and captured responses jointly inform the mapping. The two client conditions use the same standardized evidence, while the provider interface supplies a separate presentation reference. All adapter and service connections shown here are proposed. The architecture is authored for this study using the resource distinctions in the selected OGC standards and MPSS baseline (Open Geospatial Consortium 2025a; 2025b; MERLIN Project 2026a).

## 4 Source selection and preliminary observations

### Published definitions and observed responses

Smart Citizen publishes a human-readable schema description, endpoint tables, field meanings, and examples. Its sensor and measurement records also carry descriptive metadata and, where supplied, vocabulary and unit-definition links. The study has verified those resources and actual responses; a complete machine-readable OpenAPI or JSON Schema contract for the exact deployed source API has not yet been verified (Smart Citizen n.d.-d, “Schema,” “Sensors,” and “Measurements”).

Official kit documentation describes modular equipment and sensing functions, and the platform documentation describes data access and front-end applications. The project publishes separate hardware, firmware/tooling, and platform licensing information. Openness helps inspection but does not remove the need to examine data and media reuse terms separately (Smart Citizen n.d.-a; n.d.-b; n.d.-c).

Model documentation must remain distinct from unit-specific evidence. For example, the supplier states that kits shipped from July 2026 omit the UV sensor, while older public records may expose UV channels. A model designation alone therefore does not establish an exact installed inventory (Seeed Studio n.d.; MERLIN Project 2026c).

### Existing feasibility evidence

**Table 1. Selected observations from the preliminary public capture.** The preliminary study retrieved public registration 19639 on 24 October 2026 at 5:57:35 p.m. EDT, equivalent to 21:57:35 UTC. Selected measurements and their individual source timestamps are preserved in the evidence record. The table summarizes a subset; it is not a new live measurement or an executed adapter result (MERLIN Project 2026b). Source timestamps are on 24 October 2026 and are shown in UTC to preserve their original time basis.

| Reported channel | Source value and unit | Source time UTC | Question exposed |
| --- | --- | --- | --- |
| Temperature | 19.82 ºC | 21:55:12 | Are quantity, unit, subject, and time preserved? |
| Battery level | 99.0 % | 21:55:12 | Is percentage kept separate from runtime or supply topology? |
| PM2.5 | 10.6 ug/m3 | 21:46:09 | Does the older channel time remain visible? |
| Wi-Fi RSSI | −45 dBm | 21:55:12 | Is a radio measurement distinguished from end-to-end availability? |
| SD-card indicator | 1 | 21:55:12 | Is the source's coded meaning retained? |

The historical temperature request returned 24 groups with one-hour average aggregation and a response-wide sample size of 1,439. The returned timestamps are not all exact hour boundaries. The original exact retrieval time for this request was not retained. These limits remain part of the evidence; this paper does not reconstruct an acquisition time or invent averaging intervals (MERLIN Project 2026b, record “smart-citizen-history-19639-temperature”).

**Listing 1. Selected native temperature fields.** These members are reproduced from one channel in the captured response. Other members are omitted. The excerpt is not a complete API response or a formal source schema (MERLIN Project 2026b, record “smart-citizen-current-19639”).

```json
{
  "id": 55,
  "name": "Sensirion SHT31 - Temperature",
  "unit": "ºC",
  "unit_definition": "https://qudt.org/vocab/unit/DEG_C",
  "value": 19.82,
  "last_reading_at": "2026-10-24T21:55:12Z"
}
```

The source meaning of a field will not be inferred from this example alone. The value, unit definition, channel description, timestamp documentation, and observation context must be considered together. Definitions and actual samples can reveal different problems: documentation may describe a field that a public response filters, while a sample may expose a value whose broader meaning is underspecified.

## 5 Proposed dataset and mapping method

### Evidence collection and scope

The first dataset will include source registration and model metadata, channel inventory, definitions, units, individual timestamps, current readings, and bounded history. It will cover varied supported meanings: environmental temperature and humidity, particulate mass and particle-number concentration, light or pressure, noise level, battery percentage, radio signal strength, and storage indication. Selecting these different cases is intended to exercise semantic distinctions rather than maximize record count.

Each formal acquisition will retain the endpoint and query, acquisition time in UTC, HTTP outcome, available source-version information, original-response fingerprint, and review/transformation revision. Published excerpts will identify their omissions and relationship to the captured body. A fingerprint alone is not an archive. The earlier evidence record preserves excerpts and available fingerprints rather than every complete response, and formal experiment captures will not be retroactively attributed to those feasibility checks (MERLIN Project 2026b).

Source-reported facts, documentary model information, integration-created facts, and unresolved assertions will remain distinguishable. A model guide can support a description of available interfaces without proving the current peer or configuration of a selected unit. Similarly, an adapter's version and acquisition history are real integration facts, but an adapter restart is not a physical sensor service event.

### Identity and subject relationships

The represented physical system, a platform registration, a sensor catalogue entry, and the adapter have different identity scopes. The source API allows multiple registrations of one physical device and documents components as device-to-sensor associations. Their identifiers cannot silently become physical serials (Smart Citizen n.d.-d, “Schema” and “Components”). Any integration-assigned resource identity will state what it identifies and the evidence linking it to the source.

Environmental measurements must retain their observed environmental subject rather than become measurements of the kit merely because the kit produced them. Equipment-related readings need their appropriate subject as well. Where that subject cannot yet be identified precisely, the mapping will preserve the source assertion and its uncertainty rather than invent a battery resource or redirect historical observations to a later component (MERLIN Project 2026a, R01–R02, R11, R17).

![Proposed conceptual relationships separating model description, represented system, source registration, observations, observed subjects, and integration provenance](figures/figure_02_model.svg)

**Figure 2. Proposed conceptual distinctions for the mapped specimen.** This is a model explanation, not a diagram of resources already created on a server. The physical producer, observed subject, model, source registration, and representing software remain distinct. Missing power endpoints or deployment intervals are unresolved evidence requirements, not implicit relationships. Native carrier choices will be fixed in the mapping record (MERLIN Project 2026a, R01, R11, R15–R17; Open Geospatial Consortium 2025a; 2025b).

### Mapping records and concept lineage

For every consequential field, the mapping record will identify its source location, definition, identity scope, subject, quantity, unit, time meaning, aggregation, missing-value treatment, target resource/property, applicable MPSS rule, and presentation decision. Each transformation will have a rationale and an evidence locator. Conflicts between documentation and observed payloads will be recorded and resolved for the affected mapping. Consulting implementation code may help, but its exact revision does not automatically identify the revision deployed by the public service.

Every mapping explanation will connect the native assertion to its underlying DIM concept, the applicable MPSS binding, and the selected CSAPI concepts and representation. It will identify the relevant System, DataStream, Observation, or other resource and explain why that resource has the intended role. Where SensorML or SWE supplies the representation, the explanation will name the actual member, component, semantic definition, and unit mechanism. A JSON destination alone is an incomplete account because it does not explain the meaning being preserved or the model decision behind it.

Each individual donor concept invoked by that explanation will have its own attribution, including its name or identifier, source edition, exact section or object, and inline author-date citation. The account will state whether the concept is directly reused, adapted through an identified binding, used to constrain interpretation, or considered without an established equivalence. A source may contribute both conceptual meaning and an encoding mechanism, but those contributions will be explained separately. Multiple donors supporting one mapping will remain individually visible, and similarity of terminology will not be treated as evidence of historical derivation.

The donor explanation will distinguish an established contribution to the retained model from a source vocabulary encountered in this experiment. It will also identify MERLIN-authored bindings and experiment-authored transformations rather than crediting them to an external standard. Where the donor relationship is unverified, the mapping will say that it is not established and identify the missing evidence. The following requirements apply to every mapping added to this paper, including metadata and relationships as well as numerical readings.

**Table 2. Required explanation for each mapping.** Each mapping receives a stable study-local identifier and a narrative covering these layers. Every invoked donor receives a separately attributable concept entry, even when several donors support the same mapping. Unresolved relationships remain visible until source evidence and review support a disposition.

| Layer | Required explanation | Evidence to identify |
| --- | --- | --- |
| Native assertion | What the source actually asserts, about which subject and time | Source path, definition, capture, and limitations |
| Underlying DIM concept | Entity, property, relationship, and distinctions the mapping preserves | Model concept and exact baseline locator |
| Individual donor concepts | The meaning contributed by each donor and how it is invoked | Concept identifier, edition, section or object, citation, and reuse status |
| MPSS binding | Existing rule applied and any project-authored specialization | Exact rule, rationale, and remaining gap |
| Standard representation | CSAPI resource/association and SensorML/SWE carrier | Standard clause, field/component, definition, and unit |
| Transformation and presentation | Authored conversion, enrichment, label, or grouping and its reason | Mapping revision, code/listing, and source-to-display trace |
| Review outcome | What was preserved, unsupported, changed, or left unresolved | Executed check, evidence, and explicit limits |

### Illustrative encoding

Listing 2 illustrates a proposed SensorML output containing a SWE Quantity. The source measurement-definition URI and unit-definition URI are retained, while the local output name is an authored mapping choice. SensorML's output mechanism and SWE's Quantity and UnitReference structures provide the carriers (Open Geospatial Consortium 2025c; 2025d; n.d.-a, “AbstractProcess.json”; n.d.-b, “Quantity.json” and “basicTypes.json”).

**Listing 2. Proposed SensorML output with a SWE quantity.** This JSON fragment is explanatory authored content. It is not a complete System or a served resource. It does not represent a completed adapter mapping or an executed conformance result.

```json
{
  "outputs": [
    {
      "name": "airTemperature",
      "type": "Quantity",
      "definition": "http://www.eionet.europa.eu/gemet/concept/281",
      "label": "Air temperature",
      "uom": {
        "href": "https://qudt.org/vocab/unit/DEG_C"
      }
    }
  ]
}
```

The fragment describes an output; it does not contain the observed value. The eventual CSAPI datastream, observation schema, and observation must preserve their own roles and associations. Selection of phenomenon time, result time, and any aggregation interval remains an explicit decision, not an inference from the spelling of a timestamp field. Complete request and response examples will be added after actual service publication and retrieval (Open Geospatial Consortium 2025b, secs. 9.2, 9.6–9.7).

### Temperature mapping SC TEMP 01

Mapping `SC-TEMP-01` links the captured temperature channel to the proposed output declaration in Listing 2. The source supplies channel identifier 55, the value 19.82, a Celsius unit reference, an air-temperature definition reference, and the channel's source timestamp (MERLIN Project 2026b, record “smart-citizen-current-19639”). In the underlying model, this is an observation of an environmental property produced by a sensing system, with a result that remains distinct from the system description. MPSS R11 requires the producer, observed subject, and temporal context to remain distinguishable, so the observation cannot become a measurement of the kit merely because the kit reported it (MERLIN Project 2026a, sec. 5.8, R11). R10 also keeps a declared output distinct from the availability of recorded data (MERLIN Project 2026a, sec. 5.8, R10).

The observation-concept lineage runs through CSAPI to W3C SOSA/SSN: CSAPI explicitly identifies that semantic foundation, while documenting its own adaptations and allowing representations other than RDF (Open Geospatial Consortium 2025a, annex C.1). The individual contributing concepts are `sosa:Sensor`, `sosa:Observation`, `sosa:ObservableProperty`, `sosa:FeatureOfInterest`, and `sosa:Result`, which distinguish producer, observation activity, observed property, subject, and outcome (World Wide Web Consortium 2017, secs. 4.3.2, 4.6.2, 4.7.2). CSAPI supplies the DataStream and Observation resources and their associations; its observation `result` corresponds to `sosa:hasResult`, and `samplingFeature` corresponds to `sosa:hasFeatureOfInterest` (Open Geospatial Consortium 2025b, secs. 9.2, 9.7). This is an identified conceptual contribution through the standard, rather than an assertion that every SOSA/SSN term or constraint is adopted by the experiment.

Two further source contributions explain the property and unit: GEMET concept 281 identifies air temperature, and QUDT `unit:DEG_C` identifies degree Celsius (European Environment Agency 2021; QUDT.org n.d.). These are the vocabulary references carried by the native specimen; retaining them does not establish that they were historical donors to every part of the DIM. SWE's Quantity, semantic `definition`, and unit-reference mechanisms provide the typed representation, while SensorML's `outputs` member declares the output (Open Geospatial Consortium 2025c, secs. 8.2, 9.1; 2025d, secs. 7.3, 8.2, 9.1). The local name `airTemperature` and display label remain authored choices, while the final producer identity, sampling subject, observation-time interpretation, and executed CSAPI publication remain to be resolved and tested.

### Battery mapping SC BATT 01

Mapping `SC-BATT-01` concerns the source-reported remaining battery level of 99 percent, not a demonstrated physical power arrangement (MERLIN Project 2026b, record “smart-citizen-current-19639”). The underlying model distinguishes a reported property from an identified power-source entity and from a relationship describing which equipment it supplies. MPSS R17 preserves the quantity, subject, measurement point, time, and reading-versus-estimate meaning, while R11 preserves producer-versus-subject context (MERLIN Project 2026a, secs. 5.8, 5.10). Its Sensor, Observation, ObservableProperty, FeatureOfInterest, and Result distinctions follow the same SOSA/SSN lineage explained for `SC-TEMP-01` (World Wide Web Consortium 2017, secs. 4.3.2, 4.6.2, 4.7.2; Open Geospatial Consortium 2025a, annex C.1). A percent-scaled SWE Quantity within a CSAPI stream/observation representation is a proposed carrier, but the exact property definition and observation contract still require a completed mapping record (Open Geospatial Consortium 2025b, secs. 9.2, 9.6–9.7; 2025d, secs. 8.2.8, 9.1.9).

RFC 7326 contributes distinct power-source, metering, and aggregation relationship concepts; its Power Source Relationship concerns the energy-supply interconnection (Parello et al. 2014, secs. 6.6, 8.1–8.3). In this mapping, those concepts constrain interpretation by explaining why a battery percentage does not itself establish a supply edge. R16's OGC relationship binding is authored by MERLIN, so any later topology mapping must identify the reused RFC meaning and assess the binding's adaptations separately (MERLIN Project 2026a, sec. 5.10, R16). The present percentage mapping does not instantiate any of these three relationship concepts, and the paper will report that absence explicitly.

RFC 7577 supplies separate battery-monitoring concepts, including `batteryActualCharge` in milliampere hours and `batteryActualVoltage` in millivolts (Quittek et al. 2015, sec. 4). Neither quantity is established by a percentage alone, so this mapping has no demonstrated equivalence to either individual MIB object. The RFC is used here to test and reject unsupported substitutions, rather than to claim a directly reused battery-field definition. The proposed display therefore retains the supplier's percentage and its evidence limits without adding charge in milliampere hours, voltage, runtime, battery identity, or charging state.

### Expected domain coverage

**Table 3. Expected coverage and remaining evidence needs.** The starting material comes from inspected public evidence and proposed documentary enrichment. These are assessment expectations, not completed implementation results. The profile's inclusion of a subject does not require an unsupported source assertion (MERLIN Project 2026a, secs. 4, 5.1; 2026b; 2026c).

| Information subject | Supported starting material | Principal remaining need |
| --- | --- | --- |
| Identity and description | Registration and reported model | Physical identity and verified firmware |
| Equipment and arrangement | Channel inventory and model documentation | Installed components, support, and attachments |
| Functions and products | Varied readings, definitions, and history | Active-mode and parameter context |
| Deployment and responsibility | Source location and exposure metadata | Employment interval, purpose, and responsible roles |
| Configuration and actions | Documented supported settings | Actual settings and physical command evidence |
| Communications and access | RSSI and source/integration access | Physical peers, interfaces, and directed links |
| Power arrangement | Battery percentage | Identified supplies, power relationships, and changes |
| Condition and lifecycle | Literal status-related indicators | Qualified assessments and physical service history |

An owned or cooperating operator's kit can later supply a verified installation, actual configuration, power connections, and documented physical change. AirGradient will instead test transfer across producers. A second observation feed should not be assumed to solve the same missing physical-context questions automatically.

## 6 Integration and evaluation protocol

### Acquisition and publication

Before execution, the team will identify a public registration with sufficiently recent data and record the evidence used to assess freshness. Polling, caching, and retry behavior will follow the source's documented and observed behavior. Repeated retrieval of the same old observation will not make it new. The adapter will preserve acquisition time separately from source time and will document its duplicate-handling policy.

The selected CSAPI service will be checked for the required resource creation and retrieval capabilities. Only the chosen supported interfaces will be used, and the actual endpoint and version will be recorded in the execution record. A source sample will then be followed through capture, normalized representation, service response, and client display. Server acceptance establishes one part of that chain; it does not establish full semantic correctness (Open Geospatial Consortium 2025a; 2025b).

### Validation and reportable outcomes

**Table 4. Proposed evaluation criteria.** Structural checks will use the applicable target schemas, parsers, reference-resolution rules, and actual service responses. Semantic checks will compare the source meaning with the meaning represented and displayed. Each executed check will record the input revision, tool/version, scope, outcome, and evidence location. Illustrative code in this draft remains separate from executed evidence.

| Criterion | Evidence to collect |
| --- | --- |
| Traceability | Counts of traced, unresolved, and unsupported displayed assertions, with a stated denominator |
| Concept lineage | Individual donor concepts, exact citations, model/binding connections, reuse or adaptation decisions, and unestablished links |
| Semantic preservation | Field-level comparison of identity, producer, subject, property, unit, value, time, aggregation, and absence |
| Temporal integrity | Channel times retained; historical grouping preserved; refresh time kept separate |
| Qualified absence | Null, filtered, absent, unsupported, zero, and coded states interpreted explicitly |
| Resource consistency | Intended references and stream/schema/observation associations survive publication and retrieval |
| Presentation utility | Answer correctness, access to evidence, navigation steps, and overflow or keyboard obstacles |

Coverage will be reported independently for the eight information subjects and relevant R01–R20 relationships. The record will distinguish supported and exercised content, supported but unimplemented content, source-limited content, and content outside the case. A correctly preserved partial source is a valid result, but it cannot be reported as a complete-domain example.

Discrepancies will be classified as source omission, mapping defect, profile gap, or presentation issue. Uncertain classifications will remain open. A missing battery serial is initially a source limitation; overwriting a channel timestamp is a mapping defect; difficulty finding a preserved timestamp can be a presentation issue. Changes to the profile will require a separately supported disposition rather than being hidden inside the adapter.

## 7 Interface comparison and figure protocol

The planned comparison has three conditions: the actual Smart Citizen interface, a competent generic OGC presentation, and a profile-aware Glaux presentation. The source platform documents front-end access to its data, but no matched screenshot comparison is reported in this draft (Smart Citizen n.d.-a). Generic handling will retain useful labels, types, units, timestamps, relationships, and inspection access. It will not be reduced to a deliberately inconvenient JSON dump.

The generic and profile-aware conditions will use the same captured standardized resources. Differences will be attributed to documented presentation rules. Proposed operator tasks will ask a reader to identify the represented resource, distinguish newer readings from older channels, explain an aggregate, locate source evidence, and recognize what remains unknown. Initial evaluation will be investigator inspection, without claims about representative users. A later participant study would require its own recruitment, procedure, and analysis plan.

Each screenshot will record the registration, channel, observation or interval, aggregation, units, capture time, application revision where available, browser, zoom, viewport, and relevant controls. Glaux will be evaluated at the recovered 560 × 440 module size; other sizes will be reported explicitly. The source interface will retain its actual viewport and layout. Where it cannot replay the same sample or interval, images will be described as illustrative interface evidence rather than a matched comparison (MERLIN Project 2026d).

**Table 5. Planned figures and evidence status.** Figures 1 and 2 are authored diagrams of the proposed experiment. Figures 3–5 are reserved evidence slots. No substitute or simulated screenshots are presented.

| Figure | Intended content | Status in version 0.2 |
| --- | --- | --- |
| 1 | Proposed acquisition, mapping, service, and comparison architecture | Included as an authored diagram |
| 2 | Proposed model and subject distinctions | Included as an authored diagram |
| 3 | Actual Smart Citizen interface showing the selected channels and interval | Awaiting documented capture |
| 4 | Matched generic and profile-aware Glaux views of the integrated evidence | Awaiting implementation and capture |
| 5 | Actual implemented resource relationships and a traced source-to-display example | Awaiting server records and mapping results |

Screenshots document visible states. They cannot alone demonstrate semantic correctness or a profile benefit. A screenshot finding must be linked to the source records, mapping decisions, and task outcome. Cropping, annotation, or masking will be disclosed, and the original capture will be retained with its evidence record. Figure captions will identify the source, time basis, comparison limits, and any author-added marks.

## 8 Results to be reported

**The proposed adapter, CSAPI loading, live integration, and comparative evaluation have not been executed as part of this study.** No experimental success rate, task-time improvement, or user outcome is reported in version 0.2. The public access observations in section 4 establish limited feasibility and remain separate from experimental results.

The results section will be completed in three parts. First, acquisition and integration results will identify the actual versions, selected records, publication/retrieval outcomes, and failures. Second, semantic and coverage results will account for every selected assertion and relevant relationship, with source limitations distinguished from implementation defects. Third, presentation results will connect the matched figures to the predefined operator questions and document where profile-aware organization helped, made no difference, or introduced a problem.

The expected reporting structure does not presume a favorable outcome. An accurate generic presentation may answer a task as well as the profile-aware condition. A proposed binding may prove unnecessary or insufficient. Those findings would inform the model and PBI rather than invalidate the experiment's purpose.

## 9 Discussion and limitations

The immediate public-data case is strongest for measurements, descriptions, source context, and integration provenance. It is weaker for unit-specific physical composition, operating configuration, deployment history, power topology, and maintenance. More readings can enrich temporal evidence without filling those missing relationships. Documentary model enrichment must not be presented as observation of a particular installation (MERLIN Project 2026a; 2026b; Smart Citizen n.d.-c).

The selected source may change its fields, permissions, or availability. The research captures are limited in scope, and not every original response body was archived. Timestamp semantics and historical location applicability require verification. The example cannot establish general performance across all sensor families, operational conditions, or users. A later independent producer can test transfer, while an owned kit can address physical evidence gaps; these are different extensions.

No full OGC conformance, whole-profile implementation, or native Smart Citizen support for MPSS is claimed. Structural correctness, service interoperability, and operator benefit require different evidence. The study will also retain the distinction between native source meanings, selected standard mechanisms, MERLIN-authored bindings, and client choices throughout its reporting.

## 10 Reproducibility and document maintenance

The manuscript, figures, code listings, reference metadata, and publication manifest will be maintained together in the repository. Each paper revision will state its version, date, changed evidence, and execution status. The Word edition will be generated from the maintained manuscript and inspected after rendering. Source and output fingerprints will make a stale derived edition detectable.

Narrative paragraphs, including the abstract and explanatory figure, table, and listing captions, will contain three to five sentences. Headings, metadata, research-question items, table cells, code, and reference entries retain their respective structural formats. The publication check will enforce the paragraph rule, while editorial review will assess whether each paragraph develops a coherent point. Each mapping revision must also maintain the individual donor attributions and the explanation of its model and standard-representation roles.

References use the Chicago Manual of Style eighteenth-edition author-date system. Undated pages retain access dates; same-author/same-year suffixes are applied consistently; citations identify specific sections or evidence records when useful. “MERLIN Project” is an editorial corporate-author label for the cited project working documents, not a claim of individual authorship or outside institutional endorsement (University of Chicago Press n.d.).

The existing fourteen imported project artifacts retain their versions and bytes. This paper is a new research artifact. Its mapping choices and findings will be reconciled into the appropriate PBI, wireframe, profile, and DIM records when supported; publication of a research draft does not silently amend those baselines. The next paper revision should add the initial mapping record and actual execution evidence, including the first trace through the selected CSAPI service.

## 11 Conclusion

This protocol establishes a way to test whether a standards-grounded description of a sensing system remains useful after integration. The first case will combine public Smart Citizen readings with source definitions, documented model information, and explicit integration provenance. Its value will be assessed through traceable meaning, stated domain coverage, and observable operator tasks. The paper is prepared to accumulate both successful mappings and counterexamples as the experiment proceeds.

## References

European Environment Agency. 2021. “Air Temperature.” *GEMET*, version 4.2.3, December 6. Concept 281. Accessed October 24, 2026. https://www.eionet.europa.eu/gemet/en/concept/281.

MERLIN Project. 2026a. *Managed Physical Sensing Systems and Deployments: Profile Scope, Content Outline and Integrated Binding Draft*. Version 0.3.5. October 17. Project working draft. https://github.com/OS4CSAPI/glaux-client/blob/1a24fdff71ef801d9b326d2b42a63743db737a8e/Docs/Design/MPSS/MERLIN_Managed_Physical_Sensing_Systems_Profile_Integrated_Binding_Draft_v0.3.5_17OCT2026.docx.

MERLIN Project. 2026b. “Open Sensor Candidate Access Observations.” October 24. Research evidence record, schema version 1. https://github.com/OS4CSAPI/glaux-client/blob/1a24fdff71ef801d9b326d2b42a63743db737a8e/Docs/Research/Evidence/OPEN_SENSOR_ACCESS_2026-10-24.json.

MERLIN Project. 2026c. “Open Sensor Candidates for MERLIN DIM and MPSS Experiments.” October 24. Research report. https://github.com/OS4CSAPI/glaux-client/blob/1a24fdff71ef801d9b326d2b42a63743db737a8e/Docs/Research/Reports/OPEN_SENSOR_CANDIDATES_2026-10-24.md.

MERLIN Project. 2026d. “Resource Details Wireframe Template.” October 24. Design and implementation record. https://github.com/OS4CSAPI/glaux-client/blob/1a24fdff71ef801d9b326d2b42a63743db737a8e/Docs/Design/RESOURCE_DETAILS_TEMPLATE.md.

MERLIN Project. 2026e. “Smart Citizen Experiment Plan.” October 24. Proposed experiment plan. https://github.com/OS4CSAPI/glaux-client/blob/1a24fdff71ef801d9b326d2b42a63743db737a8e/Docs/Plans/SMART_CITIZEN_EXPERIMENT_PLAN.md.

Open Geospatial Consortium. 2025a. *OGC API—Connected Systems—Part 1: Feature Resources*. Version 1.0. OGC 23-001. Edited by Alexandre Robin. July 16. https://docs.ogc.org/is/23-001/23-001.html.

Open Geospatial Consortium. 2025b. *OGC API—Connected Systems—Part 2: Dynamic Data*. Version 1.0. OGC 23-002. Edited by Alexandre Robin. July 16. https://docs.ogc.org/is/23-002/23-002.html.

Open Geospatial Consortium. 2025c. *OGC SensorML Encoding Standard*. Version 3.0. OGC 23-000. Edited by Alexandre Robin. July 16. https://docs.ogc.org/is/23-000/23-000.html.

Open Geospatial Consortium. 2025d. *OGC SWE Common Data Model Encoding Standard*. Version 3.0.0. OGC 24-014. Edited by Alexandre Robin. July 16. https://docs.ogc.org/is/24-014/24-014.html.

Open Geospatial Consortium. n.d.-a. “Index of /sensorML/3.0/json.” Official SensorML 3.0 JSON schema repository. Accessed October 24, 2026. https://schemas.opengis.net/sensorML/3.0/json/.

Open Geospatial Consortium. n.d.-b. “Index of /sweCommon/3.0/json.” Official SWE Common 3.0 JSON schema repository. Accessed October 24, 2026. https://schemas.opengis.net/sweCommon/3.0/json/.

Parello, John, Benoit Claise, Brad Schoening, and Juergen Quittek. 2014. *Energy Management Framework*. RFC 7326. Informational. September. https://doi.org/10.17487/RFC7326.

QUDT.org. n.d. “Degree Celsius.” *QUDT Units Vocabulary*, version 3.5.3. Unit DEG_C. Accessed October 24, 2026. https://qudt.org/vocab/unit/DEG_C.

Quittek, Juergen, Rolf Winter, and Thomas Dietz. 2015. *Definition of Managed Objects for Battery Monitoring*. RFC 7577. Standards Track. July. https://doi.org/10.17487/RFC7577.

Seeed Studio. n.d. “Smart Citizen Kit 2.3—Open Source Environmental Monitoring Kit.” SKU 114993536. Accessed October 24, 2026. https://www.seeedstudio.com/Smart-Citizen2-3-p-6327.html.

Smart Citizen. n.d.-a. “Data Platform.” *Smart Citizen Docs*. Accessed October 24, 2026. https://docs.smartcitizen.me/data/data-platform/.

Smart Citizen. n.d.-b. “Open Source.” *Smart Citizen Docs*. Accessed October 24, 2026. https://docs.smartcitizen.me/about/open-source/.

Smart Citizen. n.d.-c. “Smart Citizen Kit.” *Smart Citizen Docs*. Accessed October 24, 2026. https://docs.smartcitizen.me/hardware/kit/.

Smart Citizen. n.d.-d. “SmartCitizen API Reference.” Accessed October 24, 2026. https://developer.smartcitizen.me/.

University of Chicago Press. n.d. “Author-Date: Sample Citations.” *The Chicago Manual of Style Online*. Accessed October 24, 2026. https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-2.html.

World Wide Web Consortium. 2017. *Semantic Sensor Network Ontology*. W3C Recommendation, October 19. https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/.
