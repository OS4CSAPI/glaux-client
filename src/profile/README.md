# Profile interpretation boundary

`interpret.ts` implements the original bounded Details View mapping. The MPSS
technical-description group and its four Text terms are recognized from the
unpublished v0.3.5 catalogue. Device-specific examples use the distinct
`https://example.invalid/glaux-client/experiment/v1/` namespace; these are
application experiments, not additions to MPSS.

`power.ts` separately interprets the existing synthetic connected example's R16
energy relationships, typed source replacement history, and exact external-source
voltage binding. It consumes independently captured resources and an explicit
catalogue association for the result schema. Relationships, reporting systems,
observed subjects and their times stay distinct. Unresolved or unsupported
content retains evidence and cannot become an accepted reading. See
[the power mapping and limits](../../Docs/Design/POWER_ARRANGEMENT.md).

Interpretation must consume independently retained source representations from
the data-access boundary, not replace them. Preserve unknown content and record
specific profile gaps. Never infer semantics from manufacturer names, display
labels, or identifier spelling.

Read [the exact mapping and unresolved bindings](../../Docs/Design/DETAILS_VIEW_MAPPING.md)
before extending these rules. Tests exercise duplicate terms, unknown definitions,
incorrect carriers/types/units/code spaces, nil tokens, foreign subjects, literal
source clocks, and the separation of the three historical examples.
