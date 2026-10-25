# Development boundaries

- Use existing CSAPI, SensorML, and SWE Common mechanisms before custom conventions.
- Keep library behavior (`src/data`), profile interpretation (`src/profile`), and
  operator presentation (`src/presentation`) distinguishable. Do not modify the
  upstream library as part of application work.
- Retain original server bytes and relevant metadata independently of parsed or
  derived models. Preserve unknown content, source meaning, subject, time, units,
  provenance, and uncertainty.
- Do not manufacture device identities, readings, relationships, or operational
  readiness. Test examples must be explicitly synthetic, never operational claims.
- Do not infer meaning from manufacturer names, display labels, or identifier spelling.
- Generic mode must retain competent standard-property and relationship handling;
  never deliberately weaken it to make profile-aware interpretation look better.
- Record specific profile gaps rather than silently revising the MERLIN/MPSS profile.
- The current increment implements the existing Overview, Equipment, and Condition
  wireframes using the MPSS v0.3.5 source materials. Read the actual sources and
  the bounded view mapping; do not infer requirements from this brief.
- The user subsequently authorized a bounded power-arrangement demonstration using
  the existing MPSS v0.3.5 source A/B replacement example. Apply its accepted R16
  relationships and supplied observation/history context; do not extend the
  proposed battery/interface model. Read `Docs/Design/POWER_ARRANGEMENT.md`.
- Bounded profile interpretation and explicitly synthetic, source-grounded local
  fixtures are authorized for this increment. Keep standard access competent and
  expose unsupported or ambiguous mappings without inventing profile rules.
- Vendor adapters, device controls, generalized ontology engines, OSCAR workflows,
  and an Operational Episode model remain outside this increment.
- On 24 October 2026, the user explicitly authorized publishing the identified
  MERLIN DIM, MPSS, Details View, and continuity project artifacts in this
  repository. The selected originals are recorded in `Docs/ARTIFACT_REGISTER.md`
  and `Docs/ARTIFACTS.json`; preserve their bytes, versions, and authority labels.
  This supersedes the earlier blanket instruction keeping these identified
  project documents outside the repository. Do not bulk-import the surrounding
  archival bundles, third-party manuals, captured operational data, credentials,
  private endpoints, or unrelated workspace material.
- The user has authorized a Cloudflare Pages deployment of this static client
  directly from its latest GitHub implementation. Record the selected branch,
  build settings, deployed commit, verified URL, and actual result in the
  deployment note. This authorization does not extend to existing CSAPI server
  infrastructure, server writes, device controls, or profile changes. No DGIWG or
  other organizational adoption/endorsement is established.
- Install and validate using the [README](README.md); dependency changes must follow
  the deliberate update procedure in [DEPENDENCIES](Docs/DEPENDENCIES.md).

## Documentation convention

- The owner authorized a standalone Resource Details View template using the
  recovered 560 × 440 working frame. Keep its layout-only placeholders separate
  from data examples. Follow [the template source record](Docs/Design/RESOURCE_DETAILS_TEMPLATE.md);
  do not treat provisional tab labels, review resize limits, or current spacing
  as finalized PBI or Dockview requirements.

- Keep `src/experiments.ts` current when adding or changing an experiment page.
  It supplies the deployed homepage index and the example selector. Record the
  page's description, latest actual change, and timestamp with an explicit
  timezone. Do not replace page-change times with build/deployment times. Follow
  [page-index maintenance](Docs/Design/PAGE_INDEX.md).

- Use [Docs/README.md](Docs/README.md) as the documentation index and `Docs/` as
  the single project documentation root; do not create a parallel lowercase tree.
- Organize material under Governance, Plans, Research, Design, or Testing as
  described in the index. Keep the root README and this file in place.
- Keep current authoritative material easy to identify. Label proposals and
  superseded history explicitly, with links to their current replacements.
  A folder or recorded proposal does not approve a design change.
- Maintain the published artifact set under `Docs/` using
  `Docs/Governance/ARTIFACT_MAINTENANCE.md`. Update the register, manifest, source
  references, and continuity notes in the same change as an artifact revision.
  The existing authorization covers the identified project artifacts; do not
  invent an additional approval gate for their import or routine maintenance.
- Maintain the [Smart Citizen experiment paper](Docs/Research/Studies/Smart_Citizen/README.md)
  as the experiment advances; v0.4 is dated 24 October 2026. Keep its canonical
  manuscript, generated Word edition, CMOS 18 author-date references, figures,
  listings and separate
  publication manifest consistent. Preserve proposed-versus-executed standing;
  add screenshots and results only with actual source/run evidence. Do not
  fabricate outcomes or silently revise the retained MPSS v0.3.5 baseline.
- Preserve the paper's experimental-server section as well as its early system overview. Keep the upstream pygeoapi framework, 52°North Connected Systems implementation, OS4CSAPI Oracle deployment, and 52°North public demo distinct. Record exact tested revision/image and deployment adaptations; do not infer backend, persistence, proxy, or restart configuration from upstream examples.
- Preserve the paper's early system overview and authentic, attributed imagery.
  Distinguish the SCK 2.3 model reference photograph from selected public
  registration 19639; its actual physical installation is unverified. Do not
  present model imagery as evidence of the selected unit or its deployment. Public-feed
  integration remains the immediate proposal; owned hardware and AirGradient are
  later extensions.
- Every mapping in the paper must explain its CSAPI resource/association and
  SensorML/SWE carrier, underlying DIM concept and exact MPSS rule, and
  project-authored choices. Attribute each individual donor concept with its
  citation, edition and exact locator; state direct reuse, adaptation,
  interpretive constraint, or unestablished equivalence. Follow the paper guide's
  mapping explanation and concept-lineage requirements in subsequent editions.
- Keep paper narrative paragraphs, including the abstract and explanatory
  figure/table/listing captions, at three to five sentences. Headings, tables,
  code and bibliographic entries remain structural. Preserve evidence standing
  and meaningful prose rather than adding unsupported claims to meet the count;
  apply the paragraph-counting conventions in the paper maintenance guide.
- Keep executable tests and fixtures in code directories; link to them from
  documentation rather than maintaining competing copies.
- Keep `Docs/Plans/CURRENT_WORK.md` current with the last verified implementation
  checkpoint, completed checks, limitations, and the next concrete action. Save
  source changes on the working branch at meaningful increments; an in-chat
  progress report is not a source-code checkpoint.
- Read `Docs/Plans/CONTINUITY.md` before continuing the broader DIM/MPSS effort.
  It carries current status and work sequencing beyond the preserved 22 October
  PITON and plan; importing those older documents does not restart completed work
  or authorize a new profile revision. Run `python3 scripts/verify-artifacts.py`
  after changing registered files or documentation links.
