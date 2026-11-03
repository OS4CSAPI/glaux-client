/**
 * Step 39 read-only native CSAPI endpoint reachability and source-fidelity probe.
 * No production write, login, cookie, POST, mutation, command, or deployment.
 * Network failures are BLOCKED (not a fabricated API success or a server outage).
 * A 200 JSON body is transport evidence, NOT OGC standards conformance.
 *
 * Usage: node scripts/verify-step39-csapi-readonly.mjs
 * Optional: GLAUX_STEP39_BASE=https://documented-host/csapi-pygeoapi
 * Output: artifacts/step39-csapi-readonly.json, concise JSON summary on stdout.
 */
import { createHash } from 'node:crypto';
import { mkdir, writeFile } from 'node:fs/promises';

const base = process.env.GLAUX_STEP39_BASE ??
  'https://129-80-248-53.sslip.io/csapi-pygeoapi';
const root = new URL(base.endsWith('/') ? base : base + '/');
if (root.protocol !== 'https:' || root.username || root.password) {
  throw new Error('Only an explicit HTTPS, credential-free CSAPI service base is allowed.');
}
const fixture = {
  probe4: {
    system: 'b171318e-8efe-550d-be99-bec5364984c0',
    stream: '351545ac-6ad6-418e-9688-7bba0329bb38',
    reportStream: 'c1870c01-4c61-43a2-ace5-14e86d317c36',
    originalCsvLine: 10130,
    originalSourceMean: '29.1',
  },
  probe3: {
    system: '378df868-d52f-4847-b783-865ec0c1df5e',
    stream: 'd97c6dcc-d09d-4c70-aae9-a1b63c29e4b9',
    reportStream: '8b8f9361-e2fa-4179-b1bb-947d3cd3d86d',
    originalCsvLine: 10418,
    originalSourceMean: '27.3',
  },
};
const plan = [
  { id:'landing', path:'', media:'application/json' },
  { id:'conformance', path:'conformance', media:'application/json' },
  { id:'systems-collection', path:'systems', media:'application/json', params:{limit:'2'} },
  ...Object.entries(fixture).flatMap(([key, source]) => [
    {id:key+'-system', path:'systems/'+source.system, media:'application/json'},
    {id:key+'-scalar-stream', path:'datastreams/'+source.stream, media:'application/json'},
    {id:key+'-scalar-observations', path:'datastreams/'+source.stream+'/observations', media:'application/json'},
    {id:key+'-report-stream', path:'datastreams/'+source.reportStream, media:'application/json'},
    {id:key+'-report-observations', path:'datastreams/'+source.reportStream+'/observations', media:'application/json'},
  ]),
  // A format request is only a transport probe. A JSON body with a SWE-looking
  // media type is NOT itself proof the native SWE encoding is valid.
  { id:'probe4-swe-request', path:'datastreams/'+fixture.probe4.reportStream+'/observations',
    media:'application/swe+json' },
];
const rows = [];
const now = new Date().toISOString();

for (const item of plan) {
  const url = new URL(item.path, root);
  url.searchParams.set('f', item.media);
  for (const [k,v] of Object.entries(item.params ?? {})) url.searchParams.set(k,v);
  // Restrict probes to this explicit base URL. Never follow cross-origin redirects.
  if (url.origin !== root.origin || !url.pathname.startsWith(root.pathname)) {
    throw new Error('Blocked unexpected endpoint outside configured CSAPI base.');
  }
  const entry = { id:item.id, path:url.pathname+url.search, requestedMedia:item.media };
  try {
    const response = await fetch(url, {
      method:'GET', redirect:'manual', credentials:'omit',
      headers: { Accept: item.media },
      signal: AbortSignal.timeout(12000),
    });
    const body = Buffer.from(await response.arrayBuffer());
    const text = body.toString('utf8');
    Object.assign(entry, {
      status:response.status,
      responseContentType:response.headers.get('content-type') ?? '',
      bytes:body.byteLength,
      sha256:createHash('sha256').update(body).digest('hex'),
    });
    let json;
    try { json = JSON.parse(text); } catch {}
    entry.statusClass = !response.ok
      ? (response.status>=500||response.status===401||response.status===403?'BLOCKED_HTTP':'HTTP_FAIL')
      : json===undefined ? 'NON_JSON' : 'JSON_RETRIEVED';
    if (json && typeof json==='object') {
      entry.jsonType = Array.isArray(json) ? 'array' : (json.type ?? 'object');
      const items = Array.isArray(json.features) ? json.features
        : Array.isArray(json.items) ? json.items
          : null;
      if (items) entry.collectionMembers = items.length;
      if (Array.isArray(json.links)) entry.linkCount = json.links.length;
      if (Array.isArray(json.conformsTo)) {
        entry.advertisedConformanceCount = json.conformsTo.length;
        entry.advertisedConformanceURIs = json.conformsTo.slice(0,50);
      }
      // A requested response type is distinct from the actually returned media type.
      if (item.media==='application/swe+json') {
        entry.mediaMismatch = !entry.responseContentType.toLowerCase()
          .startsWith('application/swe+json');
        entry.sweStructureConformant = 'NOT_TESTED';
      }
      if (item.id.includes('observations')) {
        entry.containsHistoricExpectedNumber =
          Object.values(fixture).some(x=>text.includes(x.originalSourceMean));
        entry.resultTimeIndependentlyEstablished = 'NOT_TESTED';
        entry.originalArchiveQAConformant = 'NOT_TESTED';
      }
    }
  } catch (error) {
    entry.statusClass = 'BLOCKED_TRANSPORT';
    entry.errorType = error instanceof Error ? error.name : 'UnknownError';
    entry.errorMessage = error instanceof Error ? error.message : String(error);
  }
  rows.push(entry);
  // Do not print source response bodies; retain only evidence metadata/hashes.
  console.log(item.id+': '+entry.statusClass+(entry.status ? ' HTTP '+entry.status : ''));
}

const outcome = {
  title:'Step 39 — bounded READ-ONLY CSAPI transport evidence, NOT standards certification',
  checkedAt:now,
  configuredBase:root.origin+root.pathname,
  requestMethod:'GET only',
  authentication:'none; credentials omitted',
  redirects:'manual (not followed)',
  stationContext:'Historical 2024 Bennett source cases, not current telemetry',
  sources:'Original NOAA 2024 selection and prior project experimental resource IDs (not newly verified originals)',
  count:rows.length,
  counts:{
    json:rows.filter(x=>x.statusClass==='JSON_RETRIEVED').length,
    blocked:rows.filter(x=>x.statusClass?.startsWith('BLOCKED')).length,
    httpFailure:rows.filter(x=>x.statusClass==='HTTP_FAIL').length,
    nonJSON:rows.filter(x=>x.statusClass==='NON_JSON').length,
  },
  limitations:[
    'A reachable JSON response does not establish CSAPI/SensorML/SWE/OMS requirements-class conformance.',
    'The source packet standing/DERIVED/UNKNOWN/original-event linkage carrier is not proven discoverable.',
    'No native resultTime, averaged phenomenonTime, resultQuality, exact Deployment or completed-mean producer mapping is invented.',
    'Network-blocked requests are NOT evidence the remote server is down.',
    'No original NOAA archive CSV was re-downloaded or independently rehashed by this script.',
    'No POST/PATCH/PUT/DELETE, credentials, device control or production deployment was performed.',
  ],
  rows,
};
const output = new URL('../artifacts/step39-csapi-readonly.json', import.meta.url);
await mkdir(new URL('./', output), { recursive:true });
await writeFile(output,JSON.stringify(outcome,null,2)+'\n');
console.log(JSON.stringify({file:'artifacts/step39-csapi-readonly.json',checkedAt:now,
  count:outcome.count,counts:outcome.counts,readOnly:true},null,2));
