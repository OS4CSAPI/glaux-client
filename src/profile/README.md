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

## Step 34 — Dragino S31-LB reference-only source challenge (3 November 2026)

The **unchanged** [`source-packet.ts`](source-packet.ts) reader was exercised against the first *actual preserved manufacturer-reference research case*, [Dragino S31-LB](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md). The [Step 32 research packet](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Candidate_Specification/examples/step32-source-packets/dragino.reference.packet.json) was copied **without changing its Git blob bytes** into [the app-side test fixture](../../tests/fixtures/source-packets/dragino.reference.packet.json), matching source Git blob **`5d7931846ff88b0752dab81402a4df1703fa8077`**. Test-only source oracles and adversarial changes live in [`tests/source-packet.dragino.test.ts`](../../tests/source-packet.dragino.test.ts), **not** the generic interpreter.

The direct read preserves **one model/reference node**, **one externally cabled three-metre SHT31**, two native output fields `TempC_SHT31` and `Hum_SHT31` from the *same physical reference probe*, a `SOURCE_EXAMPLE` temperature of **26.1 °C** (not observed field telemetry), the **8,500 mAh manufacturer nameplate rating** (not remaining battery charge), and explicit **UNKNOWN** installed identity and effective reporting interval. It creates **no actual original Observation, physical installed serial, Deployment, or Command**. These are source/model semantics only; no native CSAPI source→wire mapping or Resource Details page was deployed.

**Bounded executed test:** 13/13 committed Dragino test cases passed when the **exact unchanged reader and test logic were executed via a temporary V8 compatibility harness after stripping TypeScript-only annotations**. Five structurally invalid mutations were rejected directly; **three additional source-false mutations were still accepted by the reader** (model designation promoted to actual unit, printed sample promoted to `SOURCE_FACT`, and a second reference SHT31 invented). The **source-specific test oracle** detected all three as contradictions to the original C-I01/C-I02/C-F05 evidence. This is *not* full Vitest/Node 24 build verification; the normal repository `npm test`, app-wide typecheck, browser tests, and full OGC conformance suite were not run.

**Documented source-to-packet omission:** the original source sheet **C-O03** gives a **20-minute design default uplink**, but this Step 32 packet has no assertion carrying that known default. The interpreter did not drop a value it received; the *source-to-packet coverage* is incomplete. Do not fill it with a fictitious effective setting or infer a current device mode. Carry the missing data and the non-authenticating evidence contract forward into the fidelity/blocker audit.

**Gate E remains NOT CLOSED:** locally accepted `standing` and reference IDs are author declarations, not proof of original-issuer authenticity or interoperable CSAPI discovery. A generic reader without source validation can accept coherent but false manufacturer claims. **No change to the reader's source-dependent behavior was made**, and no production UI, Oracle/52°North service, command, Cloudflare Pages trigger or deployment was touched. [Step 34 workbook results](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Whole_System_Recovery/README.md#38-step-34--dragino-s31-lb-source-packet-challenge-and-fidelity-limits) preserve the source-oracle outcomes and an **informative**, nondeployed Resource Details preview.

**Next: Step 35 only** — exercise the **same unchanged reader** on the separately documented AirGradient Open Air Max manufacturer reference, with equivalent source-bound falsification. Do not broaden Step 34 into live deployment or the later Campbell/Bennett cases.
