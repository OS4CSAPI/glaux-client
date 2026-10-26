# Resource Details Activity table wireframe

## Purpose and scope

The owner requested a separate page that reuses the complete recovered Resource
Details template while leaving `/?page=resource-details-template` unchanged. Open
`/?page=resource-details-activity`, then select **Activity → Table**. Every other
category, subtab, placeholder, frame dimension, marking band, resize control and
layout sample remains the shared template behavior.

This is a presentation wireframe. It makes no resource request and uses bracketed
placeholders rather than operational records. It does not establish a universal
Activity endpoint or claim that an arbitrary server can supply the combined view.

## Explicit research basis

The controlling design is Appendix J/K of
[Resource Details Research Paper v0.15](../Research/Reports/MERLIN_Resource_Details_Research_Paper_v0.15_09OCT2026.docx):

- System-scoped Activity supports Table, Charts, and Feed when applicable.
- Activity co-displays **Observations, Commands, and System Events** with resource-
  type filters and explicit System/member scope.
- Type, origin, relevant time, and per-command progress remain recoverable.
- Activity is cross-type history; Commands remains the tasking home.
- Each resource comes from its actual CSAPI path; no universal Activity endpoint
  is implied.

The columns reuse the reviewed semantics in the
[Semantic Presentation and Interaction Guide v0.5](Details_View/MERLIN_Semantic_Presentation_and_Interaction_Guide_v0.5.docx)
and the Resource Discovery table requirements:

| Wireframe column | Resource-specific meaning |
| --- | --- |
| Resource Type | Observation, Command, or System Event |
| Start Time / End Time | Observation phenomenon time, Command execution time, or System Event event time |
| Result / Issue Time | Observation result time or Command issue time; not forced onto System Events |
| Result / Parameters / Message | Observation result, Command parameters, or directly supplied System Event message |
| Origin / scope | DataStream/producer, ControlStream/receiver, or System/event source context |
| Status | Command current status when supplied; not manufactured for other rows |

The shared labels are functional presentation analogies, not claims that their
source fields are synonymous. A future connected implementation must retain the
source resource, association role, time meaning, paging/completeness, and access
state for every row.

## Interaction

The Table view initially shows one placeholder row for each supported resource
type. **All**, **Observations**, **Commands**, and **System Events** buttons filter
the same table without changing the focal System. Charts remains the untouched
blank canvas because the source research requires suitable quantities before a
chart is justified.

The page catalogue and browser verification must be updated with this page. The
dedicated browser check confirms shared frame dimensions, original default state,
the three-resource table, each type filter, unchanged Charts content, and absence
of fixture or remote requests.
