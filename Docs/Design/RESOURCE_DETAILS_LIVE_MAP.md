# Resource Details live map experiment

This separate page adapts the live CSAPI Resource Details view for a compact map
of the selected System's reported position. The MASBUS map chip supplied by the
owner inspired the framed imagery, prominent resource marker, zoom controls, and
basemap choice. The existing live page and other experiment routes remain available.
The project's [Resource Details research paper](../Research/Reports/MERLIN_Resource_Details_Research_Paper_v0.15_09OCT2026.docx),
Appendix J, section J2's “Location and map” row and section J3's “Physical
position and frames” row, inform the source and reference-frame boundaries.

The map displays a supported GeoJSON Point using longitude, latitude as specified
by [RFC 7946](https://www.rfc-editor.org/rfc/rfc7946#section-3.1.1). The source
coordinates remain visible, and an explicitly selected alternate interpretation is
available where its values are in range. This is an exploratory interpretation,
not evidence of producer intent or an automatic correction. Missing, unsupported,
or unresolved positions receive a text fallback; Web Mercator's polar limits are
not silently treated as actual location. A System position is not a Deployment
area, and neither descriptor validity nor retrieval time establishes position time.

The map is read-only and does not imply current tracking or known position
accuracy. It provides zoom, panning, recentering, a text coordinate summary, and
satellite or street basemap selection. A tile failure is reported separately from
the reported position. The default satellite layer is the historical 2016
Sentinel-2 cloudless mosaic, attributed to EOX and Copernicus; street tiles are
attributed to OpenStreetMap contributors. Requests to a basemap provider disclose
the viewed area and the browser's IP address, as stated in the interface.

Implementation references: [Leaflet accessibility guidance](https://leafletjs.com/examples/accessibility/),
[EOX licensing and fair-use guidance](https://cloudless.eox.at/documentation/faq),
and [OpenStreetMap tile usage policy](https://operations.osmfoundation.org/policies/tiles/).
Public tile services may be unavailable and the satellite layer is not live imagery.
