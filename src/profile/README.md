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

## Step 33 research-packet reader — 3 November 2026

[`source-packet.ts`](source-packet.ts) adds the **first pure, typed, source-independent reader** of the versioned [Step 32 research source-packet contract](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Candidate_Specification/Step32_Source_Packet_Contract.md). It declares reference/actual subject standing, keeps source evidence and raw lexical values, distinguishes original facts, printed examples, project derivations and explicit UNKNOWNs, follows source/subject/derivation pointers, and groups historical experiment copies under source original-event IDs. It does **not** choose CSAPI observation ownership, discover a Profile from a server, authenticate source assertions, encode native SWE JSON, or populate Resource Details views.

The reader **does not inspect manufacturer names, model names, file names or known Bennett IDs** to choose its interpretation. Unknown/future concepts remain marked as unrecognized and available through each unmodified raw assertion; the complete input remains available through `raw`. Even when `accepted=true`, that means only **bounded declared packet-shape and relationship-link consistency**, not independent fact verification or JSON Schema/OGC conformance. Do not promote a model's original identifier into a serial-numbered installed unit without original identity evidence.

[`tests/source-packet.test.ts`](../../tests/source-packet.test.ts) contains **11 source-neutral synthetic positive/negative unit tests**; these do not yet exercise the four real research packets (reserved for Steps 34–37). Exact committed source/test files passed **11/11 isolated Node built-in test checks** in the assistant's temporary local harness after a strict TypeScript check. **The repository's Vitest, full `npm run typecheck`, `npm test`, production build and browser tests were not run in that offline environment** because the app's dependencies/Node 24 installation were unavailable there. No active app route, server, Cloudflare trigger or application deployment changed.

**Next plan step: 34 only** — use the unchanged reader on the **Dragino S31-LB reference packet**, with explicit evidence-scope positive/negative checks. Keep later AirGradient/Campbell/Bennett case coverage, UI integration, server validation and publication separate.
