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

## Step 35 — AirGradient Open Air Max source-evidence challenge (3 November 2026)

The **unchanged** [shared source-packet reader](source-packet.ts), Git blob `346d682cbff6a2e97770feba088452df6a067c4e`, was exercised against the manufacturer/reference [AirGradient Open Air Max source packet](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Candidate_Specification/examples/step32-source-packets/airgradient.reference.packet.json). The [app-side pinned fixture](../../tests/fixtures/source-packets/airgradient.reference.packet.json) has the **same Git blob `f3684d6e1e8285f9f766420a379cef8c0dc60201`**. Original pinned A01 [hardware README](https://github.com/Open-Air-Foundation/pcb-openair-max-main/blob/89aacf5013fc0ffe4b988a2e3c5a227bce3c4983/README.md) and A02 [firmware README](https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/README.md) were checked against the maintained [research source sheet A](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md).

The reader recovered a **reference assembly** O-M-1PPSTON-CE and **two distinct PMS5003 design modules at PM1 and PM2 hardware sockets**, not two verified installed serial-numbered units. The packet reports separate **`pm01` / `pm25` / `pm10`** PM1.0/PM2.5/PM10 property fields, all scoped to the reference assembly; the packet does **not** prove which physical PMS5003 produced any particular actual result. The printed manufacturer **`pm25=27.7 µg/m³`** remains `SOURCE_EXAMPLE`, with zero genuine acquired Observation events; the installed unit remains `UNKNOWN`. No firmware version is treated as installed or any gas result as calibrated.

[The committed Step 35 source-case tests](../../tests/source-packet.airgradient.test.ts) contain **16 scenarios**. They passed **16/16 only when their exact logic was executed with the unchanged reader and fixture using a temporary V8 compatibility harness**, stripping TypeScript-only annotations and supplying lightweight assertions. **Not Vitest or full application test/build.** Five malformed packets were rejected by the generic reader. **Four additional source-false packets were accepted by the generic reader** yet rejected by the original-source test oracle: product-reference model promoted to actual unit; PM2.5 output field reclassified as PM2 hardware; printed value promoted to `SOURCE_FACT`; invented third physical PMS5003 reference module. These are actual **fidelity failures at original-source authority**, not four successes.

**Selected-packet coverage limits** remain explicit: manufacturer A01/A02 and other qualified sources describe CO₂, SGP41, SHT4x and gas modules; solar/battery/network options; different firmware/configuration/transport examples; and uncertain electrode calibration. The small packet captures none of those full descriptions, and is **not** a complete model of the manufacturer design. No unsupported original-stream link, live gas measurement, installed firmware pairing or physical-unit serial should be manufactured from them.

**Gate E remains NOT CLOSED (G30-01 source-authority/portable discovery).** No vendor-name condition was introduced into the shared interpreter, and no existing app route/UI, `src/data`, server, physical command or Cloudflare deployment was altered. The full case record and qualified, **informative-only** Resource Details preview are in [workbook §39](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Whole_System_Recovery/README.md#39-step-35--airgradient-open-air-max-source-packet-challenge-and-fidelity-limits).

**Next: Step 36 only**, using this same reader on the **Campbell CR1000X + first-generation ClimaVue 50** reference packet, separating logger status, sensing assembly, native SDI-12 response fields and source-example authority. Do not advance Bennett, UI integration, live API tests or release gates as part of Step 35.
