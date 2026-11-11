# SOSA-G2-7H — original C239 §13.4 VNX source and master correspondence

**SOURCE REVIEW COMPLETED; SAME Excel packet exit pending.** Original The Open Group SOSA C239 Edition1.1 (2023) **§13.4, PDF268–273 / printed242–247** was read through source text, four tables, two figure captions and two numbered Observations, ending BEFORE §13.5. [Original 57-item source ledger](SOSA_G2_7H_Original_Source_Item_Coverage_11NOV2026.json) includes 9 registered headings and 17 nested source sections, 18 explicit standalone TBD section-body records, 17 local holds and 16 qualified existing master-target proposals. **No source-numbered SHALL Rule or SHOULD Recommendation occurs in §13.4**; future and TBD content are NOT adopted specifications.

## Edition-specific source meaning

The original says VNX small-form-factor Plug-In Card work is **in process**, gives the committee's general direction and plans detailed requirements for a *future edition*. It lists **19, 32.5 and 39 mm** cards, connector S0/S1/S2 physical signal paths and potential optical MT/coax apertures. ANSI/VITA 74.0, VITA74.5 and developing VITA74.x source originals were not reviewed; this is not a conformance audit of VITA or installed equipment.

## Source-native connector configuration table transcription

| PIC | Combination | Pins | Config class | Aperture fill | Image text |
| --- | --- | ---: | --- | --- | --- |
| 19mm | Connector Only | 400 | 1 | None | BLANK |
| 19mm | Small Aperture | 320 | TBD | TBD | TBD |
| 19mm | Large Aperture | 240 | TBD | TBD | TBD |
| 32.5mm | Connector Only | 400 | TBD | TBD | TBD |
| 32.5mm | Small Aperture | 320 | TBD | TBD | TBD |
| 32.5mm | Large Aperture | 240 | TBD | TBD | TBD |
| 39mm | Connector Only | 400 | TBD | TBD | TBD |
| 39mm | Small Aperture | 320 | TBD | TBD | TBD |
| 39mm | Large Aperture | 240 | TBD | TBD | TBD |

The only fully stated configuration-class/aperture-fill pair is **19 mm connector-only: Class 1; 400-pin; fill None**. Its **image cell is blank in parsed source**, not asserted as a figure of 'None'. The other eight classes are TBD, and no page-image verification of table figure cells or connector geometry was possible.

## Observations, thermal source and placeholders

**Observation 13.4.4.2-1** explains module size instead of slot pitch when cards may be adjacent or differently oriented. **Observation 13.4.4.3-1** points unresolved RF/optical work to VITA 74.5 §TBD and SOSA §TBD. Neither is a binding Rule. §13.4.5 describes compressible Thermal Interface Material (TIM) on two side faces and a handle-face with a heat-transfer mechanism by ANSI/VITA74.0 reference; Table13.4.5-1 lists **compressible TIM to heat exchanger, wedge locks, single-module deployment** with TBD figures. Figure13.4-1 and13.4.5-1 actual pixels were not accessible.

The **18 explicit TBD bodies** include VNX clock, utility/power/geographic addressing/console/NVMRO, portions of mechanics/front panel/keying, RF/optical apertures, PSC/ESC and PSC input/outputs/SYNC, and security. No installed clock, power supply or applied operating setting is established.

## Crosswalk and source coverage

**16** original-source-qualified potential existing-row comparisons are documented with IDs, source meaning, relation and negative-equivalence caveat. Only The Open Group SOSA donor column I is eligible for updating; four source-case facts, other donor cells and candidate DIM adoption must remain unchanged. Original 192 registered C239 headings are now **170 at least sampled/inline-reviewed, 21 substantively unread and one restricted**, *not 170 fully audited headings*; native companion/figure and later S251 holds remain.

**Mandatory L23:** synchronize canonical JSON, BOTH CSV, BOTH readable Markdown and the SAME 26-sheet editable Excel, then independently compare all 346×15 saved cells. Do not advance to §13.5/SAPIENT on source-only success. STOP after verified G2-7H; only a separate owner Proceed can authorize **G2-7I beginning §13.5**.
