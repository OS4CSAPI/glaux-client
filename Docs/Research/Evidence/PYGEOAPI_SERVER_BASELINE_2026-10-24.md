# 52°North connected-systems-pygeoapi experimental server baseline

Prepared 24 October 2026. This record consolidates the server facts used by the Smart Citizen integration study. It distinguishes upstream implementation facts, the tested OS4CSAPI deployment, bounded preservation evidence, and configuration details that remain unverified. It is an evidence record, not a new conformance verdict.

## Upstream lineage

The upstream implementation is [52North/connected-systems-pygeoapi](https://github.com/52North/connected-systems-pygeoapi), which describes itself as a proof of concept of OGC API – Connected Systems based on pygeoapi. The repository is maintained by 52°North Spatial Information Research GmbH and is licensed under Apache License 2.0. The tested upstream revision was `6ad75aa7fbfc76517c8a24c21446471845007855`.

At that revision, `pyproject.toml` identifies project version `0.6.0`, requires Python 3.12.12, and obtains pygeoapi from the 52°North pygeoapi fork at `ec1eb38d9a64d93ec9a2e1b9db6fea6dc05f194a`. The upstream Dockerfile runs the application with Hypercorn and includes native geospatial dependencies such as GDAL, PROJ, GEOS, NumPy, and Shapely. The repository provides example setups for multiple backends; those upstream choices do not establish which backend our deployed instance uses.

52°North reports that a first draft of the Connected Systems API based on pygeoapi was designed and prototypically implemented through KI:STE in synergy with MINKE and EMODnet Ingestion III. Its later open-source reporting describes continued pygeoapi-community work and Connected Systems prototype development. These project-history sources explain where the implementation came from; they do not establish the configuration of the OS4CSAPI deployment.

## OS4CSAPI Oracle deployment

The deployment used for the October 2026 MERLIN preservation experiments is the Oracle-hosted endpoint `https://129-80-248-53.sslip.io/csapi-pygeoapi`. The tested running build corresponded to upstream commit `6ad75aa7fbfc76517c8a24c21446471845007855` plus documented deployment adaptations, with container image ID `sha256:15e6991a3697e5f7130ed50bbb958720f2ffa7954f114a70be66cc93c0c489da`. Project inventory recorded this endpoint as unauthenticated for the test environment; that access posture must be reverified before the Smart Citizen run.

The retained deployment adaptations are a public-URL correction, an asynchronous full-scan/bootstrap-ID patch, and ARM64/native-dependency adaptations. The exact local patch diff is not reproduced in this record, so the implementation must not be described as byte-identical to upstream commit `6ad75aa7...`. The public-URL correction is relevant because the service is exposed below the reverse-proxy path `/csapi-pygeoapi`, and externally resolvable links are part of the behavior a client evaluates.

The recovered evidence does **not** establish the exact storage/backend selected by the running instance, its persistent-volume layout, database schema, reverse-proxy configuration, restart policy, or complete Docker Compose topology. Upstream supports multiple backend examples, and its dependency set includes more than one potential storage technology. The paper and experiment must therefore record those deployment details from the running environment before relying on them for reproducibility or durability claims.

A separate 52°North public demonstration exists at `https://csa.demo.52north.org/`. That service is operated by 52°North and is not the Oracle-hosted OS4CSAPI deployment. Prior verification work explicitly corrected an earlier package that targeted the public demo when the intended primary comparison was our Oracle instance.

## Why this server is the initial Smart Citizen target

The glaux-client bootstrap already identified the existing pygeoapi CSAPI test server as the intended server for the later prototype. The stronger experimental rationale came from the bounded 19 October 2026 write-read-compare test across the three running Oracle deployments. The same profile-style SensorML fixture was submitted without removing the fields MERLIN needed to test.

CS-GO rejected the fixture with HTTP 400 on `characteristics`, so preservation of that fixture could not be tested there. OpenSensorHub accepted it with HTTP 201 but the retrieved SensorML omitted the characteristic-group ID and conditions and the capability-group ID. The 52°North/pygeoapi deployment accepted the fixture with HTTP 201 and returned all submitted fields under the stated comparator rules.

This result is why pygeoapi is the initial server for the Smart Citizen experiment: it is the tested implementation that preserved the particular MPSS-relevant metadata already exercised. The result is **not** evidence that pygeoapi is universally more conformant, more complete, or better for every CSAPI capability. It is a bounded preservation result aligned with the semantic-preservation question this study is designed to extend.

## Observed behavior and limits

For the pygeoapi preservation sample, creation returned HTTP 201 and an explicit UUID JSON body but no `Location` header. The harness used that returned UUID as a retrieval candidate only after requiring the generated `uniqueId` to match, and it did not repeat the POST. Retrieval showed no submitted fields missing or altered under the comparison rules.

The returned response passed the supplemental schema validation used for that sample, and cleanup returned HTTP 200 followed by GET 404 for the created resource. Those results do not prove physical erasure from underlying storage or transaction history. They also do not prove preservation across restart, complete time-bearing representation support, observation or datastream writes, commands, access control, or whole-CSAPI conformance.

The direct comparison used one temporary synthetic System and deliberately avoided PUT, PATCH, datastream, observation, command, cascade, or existing-resource writes. Earlier time-bearing validation remained blocked by an official-schema dependency issue. The Smart Citizen experiment must therefore verify the publication operations it actually needs instead of assuming that the previous System test covers them.

## Deployment information to capture before the Smart Citizen run

Before live Smart Citizen publication, record the running endpoint, upstream revision, local patch revision or diff, container/image identity, host architecture, and reverse-proxy/public-base-URL configuration. Also record the active backend/provider, database or storage service, volume/persistence configuration, restart policy, authentication/access controls, and relevant runtime environment variables. These facts should be captured from the running deployment rather than inferred from upstream examples.

The execution record must distinguish source-data acquisition, adapter behavior, server behavior, and client behavior. A successful POST is evidence of server acceptance, not proof that the mapping was semantically correct. Restart durability, relationship traversal, observation history, and any other capability used by the study require their own executed checks.

## Source provenance

This record consolidates facts from the retained October 19 direct write-read-compare report and the earlier deployment/verification planning record, plus primary public sources for the upstream implementation. The original test report records the exact endpoint, upstream commit, image digest, deployment adaptations, request outcomes, and comparison limits. The earlier project record identifies the Oracle deployment as the intended prototype server and distinguishes it from 52°North's public demo.
