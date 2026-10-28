import {readFileSync} from 'node:fs';
import {expect,test} from 'vitest';
import {
  candidateRules, inputFixtures, mappedFieldCount, mappingsForView,
  projectSourceFixture, smartCitizenDesign, unmappedFields,
} from '../src/profile/resource-details-proof';

function fixture(name:string):Parameters<typeof projectSourceFixture>[0]{
  return JSON.parse(readFileSync(new URL('../public/fixtures/'+name,import.meta.url),'utf8')) as Parameters<typeof projectSourceFixture>[0];
}
test('manufacturer design maps to UI without inventing a physical System, readings or current condition',()=>{
  const s=smartCitizenDesign;
  expect(s.resourceStanding).toMatch(/product-kind/);
  expect(s.identifier).toMatch(/No verified/);
  expect(mappedFieldCount(s)).toBe(s.fields.length);
  expect(mappingsForView(s,'operational/Equipment').filter(x=>x.groupId==='urban-sht31'&&x.term==='supported-measurement').map(x=>x.value))
    .toEqual(['Temperature','Relative humidity']);
  expect(mappingsForView(s,'operational/Equipment').filter(x=>x.groupId==='urban-as7331'&&x.term==='supported-measurement').map(x=>x.value))
    .toEqual(['UV-A','UV-B','UV-C']);
  expect(mappingsForView(s,'activity/Table')).toHaveLength(0);
  expect(mappingsForView(s,'operational/Map')).toHaveLength(0);
  expect(mappingsForView(s,'management/Record').find(x=>x.term==='digital-association')?.caution)
    .toMatch(/Not a physical subsystem/);
});
test('TRSS fixture detector slots and estimated battery remain distinct',()=>{
  const trss=projectSourceFixture(fixture('trss-etu-ii.json'),'trss');
  const selected=mappingsForView(trss,'operational/Equipment').filter(f=>f.term==='selected-detector-type');
  expect(selected).toHaveLength(2);
  expect(selected.map(f=>f.groupId)).toEqual(['configured-detector-1','configured-detector-2']);
  expect(selected.map(f=>f.value)).toEqual(['SEISMIC/ACOUSTIC','IRID-II']);
  const estimate=mappingsForView(trss,'operational/Condition').find(f=>f.term==='estimated-capacity-remaining');
  expect(estimate?.value).toBe('100');
  expect(estimate?.unit).toBe('%');
  expect(estimate?.meaning).toMatch(/estimate/);
  expect(mappingsForView(trss,'activity/Table')).toHaveLength(0);
});
test('OmniSense transducers remain five labels rather than invented individual Systems',()=>{
  const source=projectSourceFixture(fixture('omnisense-core2.json'),'core2');
  const list=mappingsForView(source,'operational/Equipment').filter(f=>f.term==='reported-transducer-label');
  expect(list).toHaveLength(5);
  expect(list.map(f=>f.value)).toContain('Control Switch');
  expect(list[0].caution).toMatch(/not an individually identified/i);
});
test('separate OmniSense voltage example is not conflated with capacity or Core2 equipment',()=>{
  const source=projectSourceFixture(fixture('omnisense-core5ads.json'),'core5');
  const fields=mappingsForView(source,'operational/Condition');
  expect(fields.find(f=>f.term==='reported-battery-voltage')?.value).toBe('15.43');
  expect(fields.find(f=>f.term==='reported-battery-voltage')?.unit).toBe('V');
  expect(fields.some(f=>f.term==='estimated-capacity-remaining')).toBe(false);
  expect(fields.some(f=>f.term==='reported-transducer-label')).toBe(false);
  expect(fields.some(f=>f.term==='unverified-source-clock')).toBe(true);
});
test('unrecognized fields remain inspectable rather than being assigned guessed meanings',()=>{
  const doc:Parameters<typeof projectSourceFixture>[0]={
    characteristics:[{id:'unrecognized',label:'Native vendor',characteristics:[
      {name:'vendor_extension_1',label:'Vendor-only control',definition:'https://example.invalid/term/future-unknown-thing',value:'retain me'},
    ]}],
  };
  const source=projectSourceFixture(doc,'trss');
  expect(unmappedFields(source)).toHaveLength(1);
  expect(unmappedFields(source)[0].value).toBe('retain me');
  expect(mappedFieldCount(source)).toBe(0);
  expect(candidateRules['future-unknown-thing']).toBeUndefined();
});
test('all four source choices have distinct, truthful record standing',()=>{
  expect(inputFixtures.map(f=>f.key)).toEqual(['trss','core2','core5']);
  expect(smartCitizenDesign.evidence).toBe('manufacturer-design');
  for(const desc of inputFixtures)expect(desc.identifier).toMatch(/synthetic/);
});
