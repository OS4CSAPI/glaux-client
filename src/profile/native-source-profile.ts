import { buildPacketPresentation, type PacketPresentation } from './source-packet-presentation';

/**
 * Step 41R-06: one read-only producer-independent CSAPI Part 1 GeoJSON →
 * registered HTTP/body profile/describedby links → project-only evidence →
 * existing source-packet interpreter. Does not confer original issuer trust,
 * full OGC class conformance, or arbitrary vendor-extension interoperability.
 */
export interface NativeSourceRecord {
  url: string;
  uid: string;
  name: string;
  kind: 'Procedure' | 'System';
  profileUrl: string;
  evidenceUrl: string;
  nativeRaw: unknown;
  evidenceRaw: unknown;
  verification: string;
}
export interface NativeSourceLoad {
  kind: 'profile' | 'raw';
  nativeUrl: string;
  nativeRaw: unknown;
  source?: NativeSourceRecord;
  presentation?: PacketPresentation;
  reason?: string;
}

const evidenceFormat = 'dim-csapi-evidence-sidecar.v0.1';
const projectFormat = new Set([
  'dim-csapi-source-packet.s41r03.v0.1',
  'dim-csapi-source-packet.s41r04.v0.1',
]);
const object = (x: unknown): x is Record<string, unknown> =>
  !!x && typeof x === 'object' && !Array.isArray(x);
const text = (x: unknown): string => typeof x === 'string' ? x : '';
const sourceHold = (nativeUrl: string, nativeRaw: unknown, reason: string): NativeSourceLoad =>
  ({ kind: 'raw', nativeUrl, nativeRaw, reason });

/** Only https and explicit loopback http may be read; credentials are never sent. */
function safeUrl(value: string, origin?: string): URL {
  const url = new URL(value, origin);
  if (url.username || url.password || url.hash) throw new Error('Authenticated or fragment URLs are unsupported');
  const loopback = ['127.0.0.1', 'localhost', '[::1]'].includes(url.hostname);
  if (url.protocol !== 'https:' && !(url.protocol === 'http:' && loopback))
    throw new Error('Only HTTPS or explicit local loopback HTTP is supported');
  return url;
}
function boundLink(value: string, base: string): string {
  const target = safeUrl(value, base);
  const native = safeUrl(base);
  if (target.origin !== native.origin)
    throw new Error('Cross-origin Profile or evidence links are not trusted by this test contract');
  return target.href;
}
function bodyLink(feature: Record<string, unknown>, rel: string, base: string): string | null {
  const links = Array.isArray(feature.links) ? feature.links : [];
  const selected = links.filter(l => object(l) && l.rel === rel);
  if (selected.length !== 1 || !object(selected[0]) || !text(selected[0].href)) return null;
  return boundLink(text(selected[0].href), base);
}
/** Strict *supported subset* of RFC 8288 Link syntax. Never treats a missing header as advertised. */
function headerHasLink(header: string, href: string, rel: string): boolean {
  const tokens = header.match(/<[^>]+>\s*;\s*rel\s*=\s*"[^"]+"(?:\s*;\s*[^,]+)?/g) ?? [];
  return tokens.some(token => {
    const match = token.match(/^<([^>]+)>\s*;\s*rel\s*=\s*"([^"]+)"/);
    return match !== null && match[1] === href && match[2] === rel;
  });
}
function isNativeFeature(raw: unknown): raw is Record<string, unknown> {
  if (!object(raw) || raw.type !== 'Feature' || !object(raw.properties) ||
      !text(raw.properties.uid) || !text(raw.properties.name)) return false;
  const ft = raw.properties.featureType;
  const supported = ['http://www.w3.org/ns/sosa/Procedure', 'http://www.w3.org/ns/sosa/System',
    'sosa:Procedure', 'sosa:System'];
  return typeof ft === 'string' && supported.includes(ft) && ('geometry' in raw);
}
async function readJSON(fetcher: typeof fetch, url: string, accept: string): Promise<{body: unknown; response: Response}> {
  const response = await fetcher(url, {
    method: 'GET', headers: { Accept: accept }, mode: 'cors',
    credentials: 'omit', cache: 'no-store', redirect: 'error',
  });
  if (!response.ok) throw new Error('HTTP ' + response.status + ' for ' + url);
  const type = response.headers.get('content-type')?.split(';')[0]?.trim().toLowerCase();
  if (type !== accept) throw new Error('Unexpected media type ' + (type ?? 'missing') + ' for ' + url);
  return { body: await response.json() as unknown, response };
}
/** This is project-source-claim validation, not an OGC JSON Schema or manufacturer signature. */
function evidencePacket(doc: Record<string, unknown>, nativeUid: string, nativeUrl: string, nativeKind: 'Procedure'|'System', profile: string): unknown {
  if (doc.format !== evidenceFormat || doc.profile !== profile ||
      !object(doc.describes) || doc.describes.href !== nativeUrl ||
      doc.describes.uid !== nativeUid || doc.describes.kind !== nativeKind ||
      !object(doc.integratingProducer) ||
      doc.integratingProducer.role !== 'INTEGRATING_PRODUCER_NOT_ORIGINAL_ISSUER' ||
      doc.integratingProducer.verification !== 'PRODUCER_ASSERTED_UNVERIFIED' ||
      !object(doc.sourceEvidence)) throw new Error('Profile evidence version, identity, or producer standing does not match native resource');
  const e = doc.sourceEvidence;
  if (!projectFormat.has(text(e.projectPacketFormat)) || !text(e.packetId) || !text(e.focus) ||
      !Array.isArray(e.sources) || !Array.isArray(e.subjects) ||
      !Array.isArray(e.assertions) || !Array.isArray(e.originalEvents) ||
      !Array.isArray(e.representations) || !Array.isArray(e.holds))
    throw new Error('Project source evidence is missing required collections or packet version');
  const expected = nativeKind === 'Procedure' ? 'REFERENCE_ARRANGEMENT' : 'SOURCE_IDENTIFIED_STATION';
  if (doc.describes.sourceStanding !== expected) throw new Error('Source referent standing conflicts with native resource type');
  const packet = {
    format: e.projectPacketFormat, id: e.packetId, focus: e.focus, sources: e.sources,
    subjects: e.subjects, assertions: e.assertions, originalEvents: e.originalEvents,
    representations: e.representations, holds: e.holds,
  };
  if (nativeKind === 'Procedure' && (packet.originalEvents.length || packet.representations.length))
    throw new Error('A reference Procedure cannot assert performed original events or copies');
  const sourceIds = new Set<string>();
  for (const source of packet.sources) {
    if (!object(source) || !text(source.id) || !text(source.issuer) ||
        !text(source.edition) || !text(source.url) || !text(source.researchTrace))
      throw new Error('Missing original issuer, edition, URL or evidence locator');
    sourceIds.add(source.id as string);
  }
  for (const assertion of packet.assertions) {
    if (!object(assertion) || !Array.isArray(assertion.evidence) || !assertion.evidence.length ||
        assertion.evidence.some(ref => !object(ref) || !sourceIds.has(text(ref.sourceId)) || !text(ref.locator)))
      throw new Error('Evidence claim lacks resolvable original-source locator');
  }
  const focus = packet.subjects.find(subject => object(subject) && subject.id === packet.focus);
  if (!object(focus) || focus.standing !== expected)
    throw new Error('Profile focal referent is not consistent with native source standing');
  return packet;
}

/**
 * Load any user-supplied native *single resource* URL. No model names, known
 * manufacturer IDs, local fixture paths, or source specific parsing branches.
 * Failing/unknown Profile semantics return a native-raw-only result; only a
 * transport/invalid-URL failure throws. No unsupported claims are interpreted.
 */
export async function loadNativeSourceProfile(
  address: string, fetcher: typeof fetch = fetch,
): Promise<NativeSourceLoad> {
  const nativeUrl = safeUrl(address.trim()).href;
  const { body, response } = await readJSON(fetcher, nativeUrl, 'application/geo+json');
  if (!isNativeFeature(body)) return sourceHold(nativeUrl, body, 'Native JSON does not identify a supported Procedure or System Feature');
  const feature = body;
  let sourceUrl: string | null;
  let profile: string | null;
  let evidence: string | null;
  try {
    sourceUrl = bodyLink(feature, 'self', nativeUrl);
    profile = bodyLink(feature, 'profile', nativeUrl);
    evidence = bodyLink(feature, 'describedby', nativeUrl);
  } catch (error) {
    return sourceHold(nativeUrl, body, 'Unsafe or cross-origin linked evidence: ' +
      (error instanceof Error ? error.message : String(error)));
  }
  if (sourceUrl !== nativeUrl) return sourceHold(nativeUrl, body, 'Canonical native resource self link does not match requested URL');
  const featureType = text((feature.properties as Record<string, unknown>).featureType);
  const nativeKind: 'Procedure' | 'System' = featureType.endsWith('Procedure') ? 'Procedure' : 'System';
  if (nativeKind === 'Procedure' && feature.geometry !== null)
    return sourceHold(nativeUrl, body, 'Manufacturer reference Procedure must not assert deployed geometry');
  const header = response.headers.get('link') ?? '';
  if (!profile || !evidence || !headerHasLink(header, profile, 'profile') ||
      !headerHasLink(header, evidence, 'describedby'))
    return sourceHold(nativeUrl, body, 'Versioned Profile/evidence links are absent, conflicting or not exposed by HTTP');
  // Profile URI identifies this *project's* experimental contract, not an adopted OGC class.
  if (!profile.endsWith('/profiles/dim-csapi-source-evidence/v0.1'))
    return sourceHold(nativeUrl, body, 'Unrecognized or unsupported Profile version');
  try {
    const profileDoc = (await readJSON(fetcher, profile, 'application/json')).body;
    if (!object(profileDoc) || profileDoc.id !== profile ||
        profileDoc.projectContract !== evidenceFormat ||
        profileDoc.standing !== 'PROPOSED_PROJECT_PROFILE_EXTENSION_NOT_OGC_STANDARD')
      throw new Error('Profile identification document is incompatible with this client');
    const evidenceDoc = (await readJSON(fetcher, evidence, 'application/json')).body;
    if (!object(evidenceDoc)) throw new Error('Source evidence must be a JSON object');
    const packet = evidencePacket(evidenceDoc,
      text((feature.properties as Record<string, unknown>).uid), nativeUrl, nativeKind, profile);
    const presentation = buildPacketPresentation(packet);
    if (!presentation.model.accepted) throw new Error('Source claims or internal references failed shared reader validation');
    const source: NativeSourceRecord = {
      url: nativeUrl, uid: text((feature.properties as Record<string, unknown>).uid),
      name: text((feature.properties as Record<string, unknown>).name),
      kind: nativeKind, profileUrl: profile, evidenceUrl: evidence,
      nativeRaw: body, evidenceRaw: evidenceDoc, verification: 'PRODUCER_ASSERTED_UNVERIFIED',
    };
    // The native body has been fetched; its complete OGC ATS conformance and
    // original publisher signature remain OUT OF SCOPE for this UI check.
    return {kind:'profile',nativeUrl,nativeRaw:body,source,presentation:{
      ...presentation, nativeCsapiCarrier:true, nativeResource:source,
      warnings:[
        'Native CSAPI Part 1 GeoJSON resource; additional source evidence is a project Profile convention, NOT an OGC normative field.',
        'Source issuer and individual facts remain PRODUCER_ASSERTED_UNVERIFIED; independent publisher authentication was not performed.',
        'Producer full OGC requirements-class advertisement/ATS and all native observation or deployment semantics remain unverified.',
      ],
    }};
  } catch (error) {
    return sourceHold(nativeUrl, body, 'Profile evidence rejected: ' + (error instanceof Error ? error.message : String(error)));
  }
}
