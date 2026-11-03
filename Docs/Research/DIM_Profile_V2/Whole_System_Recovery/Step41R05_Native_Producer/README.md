# Step 41R-05 — Isolated read-only native CSAPI Part 1 test producer

**3 November 2026 · TEST PRODUCER, NOT A PRODUCTION SERVER OR CERTIFIED OGC API.** This directory is a reproducible read-only Python 3.12 experiment for two **unlike original-source standings**, with genuine OGC API – Connected Systems Part 1 GeoJSON feature bodies and a separate **PROJECT-authored** linked source-evidence sidecar. **No** Oracle, 52°North, Cloudflare, deployed firmware, actual observations, exact historical Deployments or physical Command writes are touched.

## Executed evidence

- **CI:** [GitHub Actions run 41652689569](https://github.com/OS4CSAPI/glaux-client/actions/runs/41652689569), research branch, pinned original schema/actual HTTP test, **12/12 tests PASS**, plus [Step41R02 producer original-source oracle](../step41r02-source-oracles.cjs) **4/4 original packet source-ledger positives, 23/23 deliberately false original-source packets detected, 4/4 additional false source issuer/authority labels detected**. The previous run [41652011442](https://github.com/OS4CSAPI/glaux-client/actions/runs/41652011442) failed on an **offline JSON Schema test resolver bug**: after dereferencing external GeoJSON schema \`$id\`, its resolver treated an OGC local relative reference as \`https://geojson.org/common/links.json\`. The fixed test normalizes relative references **in memory only**; the checked-in OGC/GeoJSON upstream source JSON files remain unmodified. All actual native schema checks then passed.
- **Native producer:** [server.py](server.py) uses Python standard-library \`http.server\` and accepts only a **loopback bind**. It serves \`GET /api/procedures/dragino-s31-lb\` as **GeoJSON Procedure** with \`geometry:null\` (manufacturer reference design, **not installed**), and \`GET /api/systems/bennetts-point-acebpmet\` as **GeoJSON System** with the original *station-site* position (not a probe coordinate). It also serves read-only \`/api/procedures\`, \`/api/systems\`, matching \`/api/collections/{id}/items\`, \`/api/collections\`, \`/api/conformance\`, a minimal \`/api/api\` description, profile and evidence documents.
- **Profile/evidence:** Each canonical native resource has a real HTTP \`Link\` header **and matching body links** with registered \`rel="profile"\` and \`rel="describedby"\`. The second resolves to a source-evidence document with an explicit **resource URI + integrating-producer UID** binding, source issuer/edition/locator, all retained project source claims, exact \`SOURCE_FACT / SOURCE_EXAMPLE / DERIVED / UNKNOWN\` standing, originalEvent/copy relationships and honest \`PRODUCER_ASSERTED_UNVERIFIED\` producer trust. The evidence JSON validates against [source-evidence.schema.json](source-evidence.schema.json), a *project JSON Schema*, not OGC/SensorML/SWE Common.
- **HTTP tests:** [test_http.py](test_http.py) launches the **actual** Python subprocess on an ephemeral 127.0.0.1 port; checks landing, collections, native \`application/geo+json\` bodies and conformance response; validates **actual GET bodies against the pinned original OGC 23-001 v1.0.0 source schemas** \`geojson/procedure.json\`, \`system.json\` and their \`FeatureCollection\` counterparts (plus original external \`https://geojson.org/schema/Feature.json\` and \`FeatureCollection.json\`); checks source-standing/canonical URI/UID binding, read-only \`405\`/unsupported URL rejection, CORS header exposure, untrusted Host handling, and exact Bennett **2 original NOAA source mean events / 4 earlier experimental API representations**, \`F_ATemp="<0> "\` including whitespace and independent blank \`F_Record\`, with original resultTime/mean producer UNKNOWN. **No real browser or non-local network was tested**.

## Reproduce from the research branch

Run from repository root, Python 3.12 and Node 22+ available; **no Glaux npm production dependencies are changed**:

\`\`\`sh
python3 -m pip install -r Docs/Research/DIM_Profile_V2/Whole_System_Recovery/Step41R05_Native_Producer/requirements-test.txt
python3 Docs/Research/DIM_Profile_V2/Whole_System_Recovery/Step41R05_Native_Producer/test_http.py
node Docs/Research/DIM_Profile_V2/Whole_System_Recovery/step41r02-source-oracles.cjs
\`\`\`

To inspect manually, in another shell:

\`\`\`sh
python3 Docs/Research/DIM_Profile_V2/Whole_System_Recovery/Step41R05_Native_Producer/server.py --host 127.0.0.1 --port 8015
curl -i -H 'Accept: application/geo+json' http://127.0.0.1:8015/api/procedures/dragino-s31-lb
curl -i -H 'Accept: application/geo+json' http://127.0.0.1:8015/api/systems/bennetts-point-acebpmet
curl http://127.0.0.1:8015/api/evidence/bennetts-point-acebpmet
\`\`\`

**Read-only safety:** Server binds only to localhost/127.0.0.1; supports GET, HEAD, OPTIONS and rejects POST/PUT/PATCH/DELETE. There are NO routes for /observations, /deployments, /commands, /controlstreams or writes. The procedure type is not fabricated into an actual System, and the Bennett source means remain in a provenance description **only**, not exported as false native CSAPI Observations.

## Original standard clauses and pinned schemas (NOT generated project syntax)

- [OGC 23-001, Part 1 v1.0.0](https://docs.ogc.org/is/23-001/23-001.html), §§9 and 13, procedure/system canonical endpoints and collections, and §19.1 GeoJSON **Req 77** (\`application/geo+json\`), **Req 81** (System GeoJSON schema), **Req 82** (System mappings), **Req 85** (Procedure GeoJSON schema), **Req 86** (Procedure mappings), and the prerequisite OGC API Features/Common requirements classes.
- [OGC API Common Part 1 v1.0.0](https://docs.ogc.org/is/19-072/19-072.html), §§6.3–6.4 (typed links and relations), §9 (landing page and conformance declaration). [RFC 8288](https://www.rfc-editor.org/rfc/rfc8288) and [RFC 6906](https://www.rfc-editor.org/rfc/rfc6906) define Web Linking and the informational \`profile\` relation.
- Pinned original official JSON Schema **unmodified** from \`opengeospatial/ogcapi-connected-systems\` tag [v1.0.0](https://github.com/opengeospatial/ogcapi-connected-systems/releases/tag/v1.0.0), under [schema-vendor/ogc](schema-vendor/ogc). Examples of source Git blobs: \`geojson/procedure.json\` **a554bbba667db0332f739f56e336644be96ff9c5**; \`geojson/system.json\` **3849e83b73f2c37f490721b8829d42fe2213fcf5**; \`geojson/feature.json\` **dba7c00cc41cc237b79a69a2ead0e582d36c8351**; \`common/uris.json\` **b28eb225d16c0869f8dbccbfca19df1f8827c69e**.
- Original GeoJSON schema files \`Feature.json\` Git blob **30151f53a97b779ef873ff837c80aec2cd0a9e93** and \`FeatureCollection.json\` Git blob **c8d4e1b3bbacd0b6824f466b624710bb26ae6a51**, checked out from [geojson/schema gh-pages](https://github.com/geojson/schema/tree/gh-pages) under [schema-vendor/geojson](schema-vendor/geojson). Source repository license MIT; upstream OGC schemas governed by OGC's published license. These are included only to make source-exact offline schema validation reproducible.

## Critical release-limit findings

**The 41R-05 service is not a standards-conformance certificate.** Its \`/api/conformance\` exposes \`conformsTo: []\`, plus a separately identified set of **candidate** OGC class URIs. The full requirements-class prerequisite and OGC Abstract Test Suite (ATS) was **not** executed; the server's minimal \`/api/api\` is an OpenAPI discovery stub, not a complete certified OAPI specification. Declaring full \`/conf/geojson\`, \`/conf/procedure\`, \`/conf/system-features\` or \`/conf/api-common\` as passed would overstate the evidence. What **is** verified is an isolated pair of real native GeoJSON **singletons and collections** validated against original selected OGC schema, plus real tested link/sidecar HTTP behavior. Gate E/F remain OPEN for portable authenticated Profile claims until full class/producer/consumer tests and independent client evidence.

**The temporary Profile URI is loopback test context** (versioned \`/api/profiles/dim-csapi-source-evidence/v0.1\`); it is not a globally published or OGC-adopted Profile identifier. A stable versioned, independently reachable Profile URI and verified producer trust model are still required for external interoperability. One isolated publisher and one in-house client would not establish third-party implementation interoperability.

**Next separate “proceed”: Step 41R-06 ONLY.** Connect the **existing Glaux Resource Details** semantic reader to **this producer's actual native CSAPI resource, resource-specific links and project sidecar** through **one vendor/ID-independent discovery path** and run real browser/source-oracle negative tests; separately assess Gates E/F and preserve full conformance/issuer/independent-client limitations. **Do not implement 41R-06 within 41R-05**, and do not change Oracle/52°North, issue physical commands, deploy Cloudflare or advance original Steps 42–43.
