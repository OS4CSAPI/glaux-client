# Candidate Profile → Resource Details placement matrix

**Working design record · 31 October 2026**

## Purpose

This page answers one bounded question:

> Given the current DIM/Profile meanings, where should each kind of information appear in the existing Resource Details navigation?

It does **not** change the Glaux UI, invent new tabs, or declare the current navigation final.

The recovered navigation baseline is:

- **Operational** → Overview, Map, Equipment, Communications, Condition
- **Activity** → Table, Charts
- **Commands** → Available, Requests
- **Management** → Record, Configuration, Sources

The recovered UI documentation establishes these labels and the compact frame, but explicitly does **not** establish a complete universal semantic taxonomy. Therefore each placement is classified as **Supported**, **Candidate**, or **Unresolved**.

## Placement principles

1. **Overview summarizes; it does not own every fact.**
2. **Meaning determines placement.** Labels, paths, manufacturers, or data types do not choose tabs by themselves.
3. **Model/type and individual-unit information remain distinguishable.**
4. **Historical observations/events are not current condition.**
5. **Requested/accepted commands are not resulting equipment state.**
6. **Source provenance and interpretation evidence remain inspectable under Management → Sources.**
7. **Unknown meanings remain unassigned rather than being forced into Overview.**

## Core placement matrix

| DIM/Profile meaning | Primary destination | Overview treatment | Standing | Rationale / guardrail |
|---|---|---|---|---|
| Resource identity — name, resource type, local ID, source | **Fixed identity frame** | Echo only if useful | **Supported** | Existing Resource Details requirements keep these values visible while tab content changes. |
| Individual physical System / equipment instance | **Operational → Equipment** | May summarize principal equipment | **Supported** | The Profile distinguishes the identified unit from its model. |
| Product model / system kind / datasheet Procedure | **Operational → Equipment** | Manufacturer/model may be summarized | **Supported / Candidate detail** | Model/type is equipment information but is not the individual unit. |
| Manufacturer, model designation, serial / unit identifiers | **Operational → Equipment** | Manufacturer/model may summarize; serial only when useful | **Supported** | These are equipment identity/nameplate facts, not deployment/location. |
| Physical components / subsystems | **Operational → Equipment** | Major composition may summarize | **Candidate** | Physical parts must stay distinct from outputs, channels and fields. |
| Product-design components in a datasheet | **Operational → Equipment**, marked as **model design** | Optional summary | **Candidate** | A design component does not prove an individually identified installed component. |
| Deployment / installation / assignment | **Operational → Equipment** for relationship/time; **Operational → Map** for supported spatial placement | Current/evidenced placement may summarize | **Candidate, split presentation** | Deployment contains more than coordinates. |
| Geometry / position | **Operational → Map** | Optional short location summary | **Supported** | Only evidenced spatial information belongs here. |
| Outputs / observable properties / what equipment can measure | **Operational → Equipment** as capability | Key capabilities may summarize | **Candidate** | Capability is not historical observation evidence. |
| DataStream / reporting output identity and schema | **Unresolved**; possibly Communications when it truly describes outward interface | Usually omit | **Unresolved / Candidate** | A DataStream is not automatically a communications channel. |
| Native channel / interface address | **Operational → Communications** | Usually omit | **Candidate** | Address/interface facts are not physical inventory. |
| Network / transport / endpoint / radio interface facts | **Operational → Communications** | Connectivity may summarize | **Supported in UI concept; Profile coverage incomplete** | Placement is clearer than the current V2 binding coverage. |
| Current/recent reported condition — voltage, diagnostics, health | **Operational → Condition** | Important condition may summarize | **Supported** | Historical values do not become current condition merely because they exist. |
| Current/effective configuration value | **Management → Configuration** | Only critical settings may summarize | **Candidate, strong** | Configuration is distinct from health/condition. |
| Model-supported parameter / manufacturer default | **Management → Configuration**, explicitly qualified as model/default | Usually omit | **Candidate, strong** | A default is not the current setting of an individual unit. |
| Historical configuration change | **Activity → Table** for event; **Management → Configuration** for effective setting if separately evidenced | Optional recent-change summary | **Candidate** | Event and resulting state are different facts. |
| Observation / measurement record | **Activity → Table** | Latest/important observation may summarize | **Supported / Candidate detail** | Observations are time-bounded activity, not equipment identity. |
| Observation time series | **Activity → Charts** | Compact latest/trend summary may appear | **Supported / Candidate detail** | Chart is a presentation of activity/history. |
| Observation quality / QA flag | **Activity → Table/Charts** beside the observation | Surface only when needed to interpret summary | **Candidate, strong** | Quality belongs with the result it qualifies. |
| Observer / sensing-unit attribution for an observation | **Activity → Table/Charts** with the observation; unit details remain in **Equipment** | May summarize when attribution is the point | **Candidate, strong** | This is a cross-link, not duplicate semantic ownership. |
| Task / command request | **Commands → Requests** | Do not imply execution in Overview | **Supported** | A requested value/action is not equipment state. |
| Available command/control capability | **Commands → Available** | “Control available” may summarize | **Supported** | Capability is distinct from executed command history. |
| Command acknowledgement / accepted / completed / failed | **Commands → Requests**; possibly **Activity → Table** in an audit/history view | Only important active/recent command state | **Candidate** | Task outcome and equipment state stay distinct. |
| Reported operating mode / state | **Condition** when treated as operational state; **Configuration** when treated as configured mode | Current mode may summarize | **Unresolved boundary** | Current evidence does not justify a universal rule yet. |
| Mission / sensor-string / assignment labels | **Operational → Overview** as concise operational context | Primary summary location | **Supported by prior Details View work** | A label does not itself establish Deployment. |
| Raw selected resource / standard representation | **Management → Record** | No | **Supported** | Complete representation and unfamiliar fields belong here. |
| Source documents, native paths, provenance, mapping evidence | **Management → Sources** | Only concise warnings in Overview | **Supported** | Users need to inspect why the client interpreted a fact a certain way. |
| Unmapped / ambiguous donor-native fact | **Management → Sources** until resolved | No unsupported summary | **Candidate, strong guardrail** | Preserve without inventing a semantic home. |

## Bennett's Point allocation check

The current Bennett's Point demo puts the two records together in Overview because the narrow experiment visually demonstrates the probe swap. That is acceptable as an **experiment summary**, but it is not the desired full-resource allocation.

| Bennett's Point information | Detailed home |
|---|---|
| Station identity / selected resource identity | Fixed identity frame + concise **Operational → Overview** context |
| EE181 model / manufacturer | **Operational → Equipment** |
| Probe 3 and Probe 4 identities and serials | **Operational → Equipment** |
| Probe installation / return periods | **Operational → Equipment**; spatial placement, if supplied, may also appear in **Map** |
| 15 April and 18 April air-temperature observations | **Activity → Table** |
| Temperature trend across multiple records | **Activity → Charts** |
| Quality flags | Beside their observations in **Activity** |
| Which probe produced each observation | With the observation in **Activity**, linking back to **Equipment** |
| Original NOAA/ACE Basin records and attribution basis | **Management → Sources** |
| Raw encoded CSAPI/SWE representation | **Management → Record** |
| No current configuration evidence | **Management → Configuration** remains empty |
| No command evidence | **Commands** remains empty |
| No selected communications evidence | **Operational → Communications** remains empty |

## Important unresolved boundaries

1. **Condition vs Configuration for operating mode.** A reported mode can act like operational state; a configured mode can act like configuration.
2. **DataStream vs Communications.** A CSAPI DataStream is a data-delivery resource, but not every stream is a network/physical communications interface.
3. **Deployment across Equipment and Map.** One underlying Deployment may legitimately be viewed relationally in Equipment and spatially in Map.
4. **Overview content budget.** Overview should summarize useful facts from their real semantic homes, but the existing source documents do not yet define one universal inclusion rule.

## Acceptance rule for future Profile work

For each new DIM/Profile concept, update this matrix before placing the concept in the client.

A placement decision should state:

1. what the fact **means**;
2. its primary detailed destination;
3. whether Overview may summarize it;
4. which Profile/donor evidence supports that meaning;
5. what nearby concept it must **not** be confused with; and
6. whether the placement is **Supported, Candidate, or Unresolved**.

If meaning is not yet established, keep the source fact inspectable under **Management → Sources** rather than forcing it into a semantic view.

## Source basis

- [Resource Details wireframe template](../../../Design/RESOURCE_DETAILS_TEMPLATE.md) — recovered navigation and frame; explicitly says the labels are working-view labels, not a finished universal taxonomy.
- [Details View source and implementation mapping](../../../Design/DETAILS_VIEW_MAPPING.md) — prior Overview/Equipment/Condition choices and source-meaning guardrails.
- [Candidate DIM](DIM.md) — current identity, model/kind, components/channels, measurement-subject, and configuration distinctions.
- [Candidate CSAPI Profile](CSAPI_Profile.md) — current model/unit, Deployment, observation, quality, configuration, task-response, component and channel decisions.
- OGC Abstract Specification Topic 20 / ISO 19156:2023 — semantic separation of Observation, Observer, Host, Deployment, ObservableProperty, procedure, phenomenon time and result quality. **The UI placement decisions themselves are this project's application design, not OMS requirements.**
