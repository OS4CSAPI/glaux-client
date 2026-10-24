# Resource Details wireframe template

## Purpose and standing

The owner requested an initial Resource Details View canvas on 24 October 2026,
using the compact frame developed during the earlier PBI work. Open
`/?page=resource-details-template` from the experiment index. The page supports
joint layout review before adding the DIM/profile content selected in later work.

The default frame is **560 × 440 CSS pixels**. Requirements v0.8, §6.1.1,
explicitly retains that shared working size. It was acceptable as a starting
point for continued review; it is not a completed PBI or a final size validated
inside MERLIN's Dockview host. This page implements the owner's requested canvas
at that recovered size without promoting the earlier proposals to final rules.

## Source evidence

The originals remain byte-preserved at their registered repository paths:

- [Resource Details Requirements v0.8](Details_View/MERLIN_Resource_Details_Requirements_v0.8_08OCT2026.docx),
  dated 8 October and amended 9 October 2026.
- [System Details Working Views](Details_View/MERLIN_System_Details_Working_Views_10OCT2026.pdf),
  the 55-page review packet; page numbers below are PDF page numbers.
- [Semantic Presentation and Interaction Guide v0.5](Details_View/MERLIN_Semantic_Presentation_and_Interaction_Guide_v0.5.docx),
  retaining the fixed Resource Type, ID, Source, and classification frame.

| Framework element | Recovered evidence and scope |
| --- | --- |
| Default 560 × 440 frame | Requirements §6.1.1 retains this CSS-pixel working size. RD-C12 leaves final dimensions and host validation for the PBI review. |
| Compact use of space | RD-C06 prioritizes identity, markings, and useful content over oversized headers, padding, decorative badges, and empty panels. |
| Fixed identity | RD-C01 and §6.1.1.1 retain supplied name, Resource Type, local ID, and Source while content changes. PDF p. 35 retains that frame. |
| Top and bottom markings | RD-S01–03 and PDF p. 35 retain both banner locations. Template labels are placeholders, not a classification assigned to a resource. |
| Adjacent category rows | RD-C02 and §6.1.1.2 place a category's optional subdivisions directly below its top-level row. PDF p. 35 preserves the adjacent rows. |
| Content-area scrolling | Requirements §6.1.1.2 says to scroll content while identity, required banners, and navigation remain usable. |
| Keyboard operation | RD-C05 requires keyboard operation, visible focus, and selected/expanded states. |
| Current working category labels | PDF pp. 35–53 carry Operational, Activity, Commands, and Management. These remain review labels rather than a finished universal navigation specification. |

The later PDF review at **p. 34** uses a **640 CSS-pixel-wide**, content-height
prototype with **14 px body / 12 px supporting text**. That page explicitly leaves
final dimensions in the continuing PBI work and does not amend the requirements
baseline by implication. It therefore does not replace the recovered 560 × 440
default frame for this canvas. Its typography supplies a readable starting point.

## Navigation placeholders

The template uses the following previously illustrated labels to expose the
framework. Selecting any of them leaves the content canvas empty by default.

| Category | Subcategories | Working-view evidence |
| --- | --- | --- |
| Operational | Overview, Map, Equipment, Communications, Condition | PDF pp. 35–53 |
| Activity | Table, Charts | PDF p. 5 |
| Commands | Available, Requests | PDF p. 25 |
| Management | Record, Configuration, Sources | PDF p. 24 |

These labels do not establish required source data, supported commands, or a
final category taxonomy. Earlier requirement examples using Details and a wider
category inventory remain historical proposals. The page follows the later
working-view labels while retaining the earlier compact frame.

## Canvas behavior

The persistent frame contains a name placeholder, Resource Type / ID / Source
placeholders, top and bottom marking placeholders, and adjacent category and
subcategory rows. The content region owns its scrolling. A long body does not
push the surrounding frame out of the module or increase the default height.
Navigation is keyboard accessible and exposes the active category/subcategory.

External controls allow resizing and resetting the module to 560 × 440. Native
resize interaction and explicit width/height controls support the same review.
The default canvas is blank. Optional vertical, wide, and combined overflow
samples demonstrate the scrolling behavior using layout-only material. They are
not System records, observations, commands, DIM bindings, or profile examples.

This is a standalone template, not an actual Dockview-hosted integration. It makes
no resource or fixture request and offers no device operation or server write.

## Choices introduced for this review page

The following are implementation choices made for the requested canvas, not
recovered pixel requirements from the earlier PBI:

- Thin native scrollbars appear when their content overflows. No permanent gutter
  is reserved for an absent scrollbar. Browser and platform rendering can vary.
- Body and supporting text use the PDF p. 34 starting sizes of 14 px and 12 px;
  exact region spacing, control styling, and borders are current review choices.
- Resize controls permit **320–1200 px width** and **280–1000 px height** for
  experimentation. These are test-page limits, not MERLIN minimum/maximum bounds.
- The external size controls, reset, native resize affordance, and overflow
  samples exist to review the frame. They are not additional module capabilities.

The source documents do not settle scrollbar thickness, region-height budgets,
final spacing tokens, or production resize bounds. Subsequent review can change
these choices explicitly while keeping source-derived requirements traceable.

## Maintenance and verification

Maintain this page's description, actual update summary, and timestamp through
the shared [page catalogue](../../src/experiments.ts), following
[index maintenance](PAGE_INDEX.md). Later content work should identify the
specific DIM/profile decision it implements rather than treating this blank
framework as evidence that a binding is complete.

[Current work](../Plans/CURRENT_WORK.md) and the
[deployment record](../Plans/CLOUDFLARE_DEPLOYMENT.md) record implementation,
verification, and deployment outcomes. This design note alone makes no claim
that a build, browser check, or upload has passed.
