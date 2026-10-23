# Profile interpretation boundary

`interpret.ts` implements the bounded Details View mapping. Only the MPSS
technical-description group and its four Text terms are recognized from the
unpublished v0.3.5 catalogue. Device-specific examples use the distinct
`https://example.invalid/glaux-client/experiment/v1/` namespace; these are
application experiments, not additions to MPSS.

Interpretation must consume independently retained source representations from
the data-access boundary, not replace them. Preserve unknown content and record
specific profile gaps. Never infer semantics from manufacturer names, display
labels, or identifier spelling.

Read [the exact mapping and unresolved bindings](../../Docs/Design/DETAILS_VIEW_MAPPING.md)
before extending these rules. Tests exercise duplicate terms, unknown definitions,
incorrect carriers/types/units/code spaces, nil tokens, foreign subjects, literal
source clocks, and the separation of the three historical examples.
