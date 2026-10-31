# Bennett’s Point live Map integration

**Status:** Experimental application integration, 31 October 2026. This record describes presentation behavior, **not** a new Domain Information Model (DIM) concept, Profile requirement, or new location fact.

## What this change does

The existing [live Bennett’s Point V2 case](https://glaux-client.pages.dev/?page=resource-details-live-bennett) now reuses the map renderer created for the independent [live resource map experiment](https://glaux-client.pages.dev/?page=resource-details-live-map). **No copy of the map implementation was created.**

- Shared renderer: [`src/presentation/resource-details-map.ts`](../../src/presentation/resource-details-map.ts), `renderResourceMap(content, position)`.
- Integration: [`src/presentation/resource-details-live-bennett.ts`](../../src/presentation/resource-details-live-bennett.ts), Map subtab only.
- Navigation source: [`RESOURCE_DETAILS_TEMPLATE.md`](RESOURCE_DETAILS_TEMPLATE.md), Operational → Map.
- Semantic placement proposal: [candidate Resource Details placement matrix](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Candidate_Specification/Resource_Details_Placement_Matrix.md).
- Existing map's own technical constraints: [`RESOURCE_DETAILS_LIVE_MAP.md`](RESOURCE_DETAILS_LIVE_MAP.md).

## Evidence and behavior

The controlled 52°North/pygeoapi service currently returns **two individually identified Campbell Scientific EE181 System descriptions**, corresponding to Bennett’s Point Probe 4 and Probe 3. Neither currently contains an attributable `position` geometry.

Within Operational → Map, the user can choose **one individual System**. The client passes that selected System’s actual `position` member, **if any**, unchanged to the existing map renderer. The renderer chooses whether it is a supported mappable GeoJSON Point and handles validation, basemap, coordinates, accessibility, and cleanup. The map selection is preserved within this page while changing tabs.

**Expected result with the current controlled data:** for both probes, show the selected unit and the renderer's missing-position fallback. No marker, site centroid, inferred coordinates, or satellite imagery is made to represent a probe location.

This preserves four distinct assertions:

1. **Individual System identity:** an identified physical probe (System), not the EE181 model or the station.
2. **System position:** only if the selected System description explicitly supplies a supported position.
3. **Deployment:** an evidenced time-scoped probe-to-site relationship; its spatial content cannot be fabricated by geocoding the station name.
4. **Observation:** the April 2024 historical air-temperature result; its time is not automatically a position time.

No `Deployment` resource was created or inferred in this integration. The shared map component and the separate independent map-experiment page are preserved.

## Acceptance check

- The dedicated live page retains Overview, Equipment, Communications, Activity, Record and Sources behavior.
- Operational → Map offers Probe 4 and Probe 3 separately.
- Each selection renders from **that selected System's** returned `position`, never the other System's geometry or a shared station location.
- With currently absent geometry, each produces the shared renderer's no-position fallback and **no marker**.
- Changing tabs or switching Systems disposes the previous map instance to avoid stale markers and rendering state.
- The existing `resource-details-live-map` route remains unchanged.
- This does not assert live physical tracking, positional accuracy, or the current installed position of either probe.

## Next bounded study

Resume the previously identified observation-semantic gap: preserve the historical **15-minute phenomenon interval** and the archive-specific **temperature QA flag** on the live CSAPI round trip, without turning the QA flag into equipment condition. Deployment publication requires separate research into the deployed server's supported operations.
