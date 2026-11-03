import { readFileSync } from 'node:fs';
import { expect, test } from 'vitest';
import { buildPacketPresentation, packetClaimsForView } from '../src/profile/source-packet-presentation';

// Exact copies of Step 32 research packets, now also served locally by Vite.
// Test includes real source-qualified historical/descriptive claims, not live API.
const base = new URL('../public/fixtures/source-packets/', import.meta.url);
function packet(name:string): any {
  return JSON.parse(readFileSync(new URL(name+'.json',base),'utf8'));
}
const names=[
  'dragino.reference.packet','airgradient.reference.packet',
  'campbell.reference.packet','bennetts-point.historical.packet',
] as const;
const view=(raw:unknown)=>buildPacketPresentation(raw);

test('all four source cases use the identical Step 33 reader and one bounded presentation model',()=>{
  const results=names.map(n=>view(packet(n)));
  expect(results.every(p=>p.model.accepted)).toBe(true);
  expect(results.map(p=>p.originalEventCount)).toEqual([0,0,0,2]);
  expect(results.map(p=>p.experimentalRepresentationCount)).toEqual([0,0,0,4]);
  expect(results.every(p=>p.nativeCsapiCarrier===false&&p.sourceAuthenticated===false)).toBe(true);
  expect(results.every(p=>p.mappablePosition===null)).toBe(true);
});

test('manufacturer reference subjects do not create an installed physical sensor or performed event',()=>{
  for(const name of names.slice(0,3)){
    const p=view(packet(name));
    expect(p.model.focus?.standing).toBe('REFERENCE_ARRANGEMENT');
    expect(p.model.subjects.every(s=>s.standing.startsWith('REFERENCE_'))).toBe(true);
    expect(p.originalEventCount).toBe(0);
    expect(packetClaimsForView(p,'activity/Table').every(x=>x.standing==='SOURCE_EXAMPLE')).toBe(true);
  }
});

test('equipment includes source-defined components/relations, not property-field counts as physical units',()=>{
  const a=view(packet('airgradient.reference.packet'));
  const equipment=packetClaimsForView(a,'operational/Equipment');
  expect(equipment.filter(x=>x.concept==='equipment.reference_component')).toHaveLength(2);
  expect(equipment.every(x=>x.concept!=='output.native_field')).toBe(true);
  const outputs=packetClaimsForView(a,'operational/Communications').filter(x=>x.concept==='output.native_field');
  expect(outputs.map(x=>x.value?.raw)).toEqual(['pm01','pm25','pm10']);
});

test('ClimaVue ambient field and logger PanelTemp remain scoped to different source subjects',()=>{
  const c=view(packet('campbell.reference.packet'));
  const fields=packetClaimsForView(c,'operational/Communications').filter(x=>x.concept==='output.native_field');
  expect(fields).toHaveLength(2);
  expect(fields.map(x=>x.about)).toEqual(['d-climavue','d-logger']);
  expect(fields.map(x=>x.value?.nativeField)).toEqual(['aR7! position 8','PanelTemp']);
});

test('Bennett original-event count is TWO even with four historical representation copies',()=>{
  const p=view(packet('bennetts-point.historical.packet'));
  expect(p.model.focus?.standing).toBe('SOURCE_IDENTIFIED_STATION');
  expect(p.model.events).toHaveLength(2);
  expect(p.model.events.map(x=>x.copies.length)).toEqual([2,2]);
  expect(p.experimentalRepresentationCount).toBe(4);
  expect(p.model.subjects.filter(x=>x.sourceIdentity?.scheme==='EE181 serial number')).toHaveLength(2);
});

test('source QA preserves the exact trailing space and an independently empty record flag in original raw',()=>{
  const raw=packet('bennetts-point.historical.packet'), p=view(raw);
  const activity=packetClaimsForView(p,'activity/Table');
  const qa=activity.find(x=>x.id==='b-qc15');
  const recordFlag=activity.find(x=>x.id==='b-record-flag15');
  expect(qa?.value?.raw).toBe('<0> ');
  expect(qa?.evidence[0]?.nativeToken).toBe('<0> ');
  expect(recordFlag?.value?.raw).toBe('');
  expect(p.model.raw).toBe(raw);
  expect(JSON.stringify(p.model.raw)).toContain('\\u003c0> '.replace('\\u003c','<'));
});

test('Bennett temporal and instrument attribution stay DERIVED; original resultTime stays UNKNOWN',()=>{
  const p=view(packet('bennetts-point.historical.packet'));
  const activity=packetClaimsForView(p,'activity/Table');
  expect(activity.filter(x=>x.concept==='observation.nominal_period').map(x=>x.standing))
    .toEqual(['DERIVED','DERIVED']);
  expect(activity.filter(x=>x.concept==='observation.contributing_equipment').map(x=>x.standing))
    .toEqual(['DERIVED','DERIVED']);
  expect(activity.filter(x=>x.concept==='observation.result_time').map(x=>x.standing))
    .toEqual(['UNKNOWN','UNKNOWN']);
  expect(activity.find(x=>x.id==='b-result-time15')?.value).toBeUndefined();
});

test('condition does not turn source initial QA into instrument health or model battery into live charge',()=>{
  const d=view(packet('dragino.reference.packet'));
  expect(packetClaimsForView(d,'operational/Condition').some(x=>x.id==='c-battery'&&x.standing==='SOURCE_FACT')).toBe(true);
  expect(packetClaimsForView(d,'operational/Condition').some(x=>x.value?.raw==='100')).toBe(false);
  const b=view(packet('bennetts-point.historical.packet'));
  expect(packetClaimsForView(b,'operational/Condition').some(x=>x.concept==='observation.raw_quality_token')).toBe(false);
});

test('a well-shaped but source-false packet is NEVER claimed authenticated by the UI projection',()=>{
  const raw=packet('airgradient.reference.packet');
  raw.subjects[0].standing='SOURCE_IDENTIFIED_EQUIPMENT';
  const p=view(raw);
  expect(p.model.accepted).toBe(true); // important parser/source-truth distinction
  expect(p.sourceAuthenticated).toBe(false);
  expect(p.nativeCsapiCarrier).toBe(false);
  expect(p.warnings.join(' ')).toContain('does not authenticate');
});

test('invalid packet remains inspectable, and does not receive normalized production meaning',()=>{
  const raw=packet('dragino.reference.packet');
  raw.assertions[0].target='missing-physical-component';
  const p=view(raw);
  expect(p.model.accepted).toBe(false);
  expect(p.model.issues.length).toBeGreaterThan(0);
  expect(p.model.raw).toBe(raw);
  expect(p.nativeCsapiCarrier).toBe(false);
});

test('future fields/unknown concepts remain in the raw record rather than being assigned invented meanings',()=>{
  const raw=packet('dragino.reference.packet');
  raw.unknownSourceExtension={registered:false,blank:'',zero:0};
  raw.assertions.push({id:'foreign',about:'c-s31',standing:'SOURCE_FACT',
    concept:'third-party.unrecognized-property',value:{raw:'<0> '},
    evidence:[{sourceId:'c02',locator:'unverified test extension'}]});
  const p=view(raw);
  expect(p.model.accepted).toBe(true);
  const foreign=packetClaimsForView(p,'management/Sources').find(x=>x.id==='foreign');
  expect(foreign?.recognized).toBe(false);
  expect((p.model.raw as any).unknownSourceExtension).toEqual({registered:false,blank:'',zero:0});
});

test('no evidence packet may turn station-site geometry into an EE181-specific Map pin',()=>{
  for(const name of names){
    const p=view(packet(name));
    expect(p.mappablePosition).toBe(null);
  }
});
