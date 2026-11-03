import { readFileSync } from 'node:fs';
import { test, expect } from 'vitest';
import { loadNativeSourceProfile } from '../src/profile/native-source-profile';

const base='http://127.0.0.1:8015/api';
const json=(file:string):any=>JSON.parse(readFileSync(
  new URL('../public/fixtures/source-packets/'+file,import.meta.url),'utf8'));

function sample(kind:'Procedure'|'System'){
  const packet=json(kind==='Procedure'?'dragino.coverage.packet.json':'bennetts-point.coverage.packet.json');
  const id=kind==='Procedure'?'unfamiliar-reference':'unfamiliar-historical';
  const url=base+'/'+(kind==='Procedure'?'procedures':'systems')+'/'+id;
  const profile=base+'/profiles/dim-csapi-source-evidence/v0.1';
  const evidence=base+'/evidence/'+id;
  const uid='urn:example:resource:'+id;
  const native={
    type:'Feature',id,geometry:kind==='Procedure'?null:{type:'Point',coordinates:[-80.45456,32.55934]},
    properties:{uid,name:'Generic outside producer',featureType:'http://www.w3.org/ns/sosa/'+kind},
    links:[{href:url,rel:'self'}, {href:profile,rel:'profile'}, {href:evidence,rel:'describedby'}],
  };
  const sidecar={
    format:'dim-csapi-evidence-sidecar.v0.1',profile,
    describes:{href:url,uid,kind,sourceStanding:kind==='Procedure'?'REFERENCE_ARRANGEMENT':'SOURCE_IDENTIFIED_STATION'},
    integratingProducer:{name:'Test integration',role:'INTEGRATING_PRODUCER_NOT_ORIGINAL_ISSUER',
      verification:'PRODUCER_ASSERTED_UNVERIFIED',reason:'not independently signed'},
    sourceEvidence:{projectPacketFormat:packet.format,packetId:packet.id,focus:packet.focus,
      sources:packet.sources,subjects:packet.subjects,assertions:packet.assertions,
      originalEvents:packet.originalEvents,representations:packet.representations,holds:packet.holds},
  };
  const description={id:profile,projectContract:'dim-csapi-evidence-sidecar.v0.1',
    standing:'PROPOSED_PROJECT_PROFILE_EXTENSION_NOT_OGC_STANDARD'};
  const link='<'+profile+'>; rel="profile"; type="application/json", <'+evidence+'>; rel="describedby"; type="application/json"';
  const requests:{url:string;method?:string;credentials?:string}[]=[];
  const fetcher:typeof fetch=async (input,init)=>{
    const dest=String(input);
    requests.push({url:dest,method:init?.method,credentials:init?.credentials});
    const result=dest===url?native:dest===profile?description:dest===evidence?sidecar:null;
    return new Response(JSON.stringify(result??{code:'NotFound'}),{status:result?200:404,headers:{
      'Content-Type':dest===url?'application/geo+json':'application/json',
      ...(dest===url?{Link:link}:{}),
    }});
  };
  return {url,profile,evidence,native,sidecar,requests,fetcher};
}

test('both unlike native kinds use one generic discovery and shared source interpreter',async()=>{
  for(const kind of ['Procedure','System'] as const){
    const p=sample(kind), r=await loadNativeSourceProfile(p.url,p.fetcher);
    expect(r.kind).toBe('profile');
    expect(r.source?.kind).toBe(kind);
    expect(r.presentation?.model.accepted).toBe(true);
    expect(r.presentation?.nativeCsapiCarrier).toBe(true);
    expect(r.presentation?.sourceAuthenticated).toBe(false);
    expect(p.requests.map(x=>x.url)).toEqual([p.url,p.profile,p.evidence]);
    expect(p.requests.every(x=>x.method==='GET'&&x.credentials==='omit')).toBe(true);
  }
});
test('reference examples and original historical NOAA event/copy identities remain distinct',async()=>{
  const a=sample('Procedure'), b=sample('System');
  const p=await loadNativeSourceProfile(a.url,a.fetcher);
  const h=await loadNativeSourceProfile(b.url,b.fetcher);
  expect(p.presentation?.model.claims).toHaveLength(21);
  expect(p.presentation?.originalEventCount).toBe(0);
  expect(p.presentation?.model.claims.find(x=>x.id==='c41-command-example')?.standing).toBe('SOURCE_EXAMPLE');
  expect(p.presentation?.model.claims.find(x=>x.id==='c-effective')?.standing).toBe('UNKNOWN');
  expect(h.presentation?.originalEventCount).toBe(2);
  expect(h.presentation?.experimentalRepresentationCount).toBe(4);
  expect(h.presentation?.model.claims.find(x=>x.id==='b-qc15')?.value?.raw).toBe('<0> ');
  expect(h.presentation?.model.claims.find(x=>x.id==='b-result-time15')?.standing).toBe('UNKNOWN');
  expect(h.presentation?.model.claims.find(x=>x.id==='b41r04-site-point')?.about).toBe('b-station');
});
test('mismatched sidecar native UID is a raw-only fallback',async()=>{
  const p=sample('System');p.sidecar.describes.uid='urn:example:other';
  const result=await loadNativeSourceProfile(p.url,p.fetcher);
  expect(result.kind).toBe('raw');
  expect(result.presentation).toBeUndefined();
  expect(result.reason).toMatch(/identity/);
});
test('sidecar describing a different resource is not interpreted',async()=>{
  const p=sample('System');p.sidecar.describes.href=base+'/systems/other';
  const result=await loadNativeSourceProfile(p.url,p.fetcher);
  expect(result.kind).toBe('raw');
  expect(result.presentation).toBeUndefined();
});
test('absent HTTP Profile Link does not activate source claims',async()=>{
  const p=sample('Procedure');
  const fetcher:typeof fetch=async (input,init)=>{
    const response=await p.fetcher(input,init);
    if(String(input)!==p.url)return response;
    return new Response(await response.text(),{headers:{'Content-Type':'application/geo+json'}});
  };
  const result=await loadNativeSourceProfile(p.url,fetcher);
  expect(result.kind).toBe('raw');
  expect(p.requests).toHaveLength(1);
});
test('unsupported Profile version cannot silently activate project standing',async()=>{
  const p=sample('Procedure');
  p.native.links.find(x=>x.rel==='profile')!.href=base+'/profiles/unsupported/v2';
  const result=await loadNativeSourceProfile(p.url,p.fetcher);
  expect(result.kind).toBe('raw');
});
test('missing assertion original-source locator is rejected',async()=>{
  const p=sample('Procedure');p.sidecar.sourceEvidence.assertions[0].evidence[0].sourceId='unregistered';
  const result=await loadNativeSourceProfile(p.url,p.fetcher);
  expect(result.kind).toBe('raw');
  expect(result.reason).toMatch(/source locator/);
});
test('false but well formed source claim remains explicitly PRODUCER_ASSERTED_UNVERIFIED',async()=>{
  const p=sample('Procedure');p.sidecar.sourceEvidence.assertions.find((x:any)=>x.id==='c-example').standing='SOURCE_FACT';
  const result=await loadNativeSourceProfile(p.url,p.fetcher);
  expect(result.kind).toBe('profile');
  expect(result.presentation?.sourceAuthenticated).toBe(false);
  expect(result.source?.verification).toBe('PRODUCER_ASSERTED_UNVERIFIED');
});
test('reference Procedure geometry cannot be a fabricated installed position',async()=>{
  const p=sample('Procedure');p.native.geometry={type:'Point',coordinates:[0,0]} as any;
  const result=await loadNativeSourceProfile(p.url,p.fetcher);
  expect(result.kind).toBe('raw');
});
test('source reference cannot be mislabeled as an actual recorded event',async()=>{
  const p=sample('Procedure');p.sidecar.sourceEvidence.originalEvents.push({id:'new-event'});
  const result=await loadNativeSourceProfile(p.url,p.fetcher);
  expect(result.kind).toBe('raw');
});
test('off-origin evidence link is refused to raw-only, not fetched',async()=>{
  const p=sample('System');
  p.native.links.find(x=>x.rel==='describedby')!.href='https://other.example/evidence';
  const result=await loadNativeSourceProfile(p.url,p.fetcher);
  expect(result.kind).toBe('raw');
  expect(result.reason).toMatch(/cross-origin/i);
  expect(p.requests.map(x=>x.url)).toEqual([p.url]);
});
test('nonloopback insecure HTTP source is refused before a request',async()=>{
  const p=sample('Procedure');
  await expect(loadNativeSourceProfile('http://example.org/api/procedures/unknown',p.fetcher))
    .rejects.toThrow(/HTTPS or explicit local loopback/i);
  expect(p.requests).toHaveLength(0);
});
