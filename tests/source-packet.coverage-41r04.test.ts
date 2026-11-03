import { readFileSync } from 'node:fs';
import { expect, test } from 'vitest';
import { interpretSourcePacket } from '../src/profile/source-packet';
import { buildPacketPresentation, packetClaimsForView } from '../src/profile/source-packet-presentation';

/**
 * Step 41R-04 source-ledger oracles, SEPARATE from the unchanged generic
 * meaning/relationship reader. These constants are transcribed from the
 * pinned original Campbell ClimaVue 50 manual D02 Table 8-1 and its
 * separately published CR1000X MQTT Status D07 example, via D source inventory.
 * Bennett expectations use actual 2024 ACE Basin operator metadata + the
 * frozen NOAA original source selection. All are SOURCE-SCOPED:
 * no deployed Campbell, no source-available Bennett resultTime.
 * Not an OGC CSAPI validator, native producer, manufacturer signature or
 * complete portable application Profile conformance test.
 */
const cases = {
  campbell: 'campbell.coverage.packet.json',
  bennett: 'bennetts-point.coverage.packet.json',
} as const;
const packet = (name: keyof typeof cases): any => JSON.parse(readFileSync(
  new URL('../public/fixtures/source-packets/' + cases[name], import.meta.url), 'utf8'));
const claim = (p: any, id: string): any => p.assertions.find((a: any)=>a.id===id);
const subject = (p: any, id: string): any => p.subjects.find((s: any)=>s.id===id);
const model = (p: any) => interpretSourcePacket(p);
const view = (p: any, key: Parameters<typeof packetClaimsForView>[1]) =>
  packetClaimsForView(buildPacketPresentation(p), key);

// These expected original field names, units, types and raw example literals are
// SOURCE-ORACLE constants in TESTS only, not runtime Glaux vendor branches.
const sourceClimaResponse = [{"index":1,"label":"Solar flux density","unit":"W/m²"},{"index":2,"label":"Precipitation","unit":"mm"},{"index":3,"label":"Lightning strike count","unit":"count"},{"index":4,"label":"Strike distance","unit":"km"},{"index":5,"label":"Wind speed","unit":"m/s"},{"index":6,"label":"Wind direction","unit":"°"},{"index":7,"label":"Wind speed max. — 10 s gust","unit":"m/s"},{"index":8,"label":"Air temperature","unit":"°C"},{"index":9,"label":"Vapor pressure","unit":"kPa"},{"index":10,"label":"Barometric pressure, absolute","unit":"kPa"},{"index":11,"label":"Relative humidity","unit":"fraction 0–1"},{"index":12,"label":"Humidity sensor temperature","unit":"°C"},{"index":13,"label":"Tilt North(+)/South(−) orientation","unit":"°"},{"index":14,"label":"Tilt West(+)/East(−) orientation","unit":"°"}];
const sourceLoggerStatus = [{"index":1,"name":"WatchdogErrors","raw":"0","kind":"number","unresolved":false},{"index":2,"name":"PanelTemp","raw":"25.91098","kind":"number","unresolved":false},{"index":3,"name":"Battery","raw":"13.2368","kind":"number","unresolved":false},{"index":4,"name":"LithiumBattery","raw":"3.70477","kind":"number","unresolved":false},{"index":5,"name":"Low12VCount","raw":"0","kind":"number","unresolved":true},{"index":6,"name":"CompileResults","raw":"cpu:main.crb -- Compiled in PipelineMode.\r\n","kind":"string","unresolved":false},{"index":7,"name":"SkippedScan","raw":"0","kind":"number","unresolved":false},{"index":8,"name":"SkippedSystemScan","raw":"0","kind":"number","unresolved":true},{"index":9,"name":"SkippedSlowScan(1)","raw":"0","kind":"number","unresolved":true},{"index":10,"name":"SkippedSlowScan(2)","raw":"0","kind":"number","unresolved":true},{"index":11,"name":"SkippedSlowScan(3)","raw":"0","kind":"number","unresolved":true},{"index":12,"name":"SkippedSlowScan(4)","raw":"0","kind":"number","unresolved":true},{"index":13,"name":"CommsMemFree","raw":"614\r\n147(146),328(283),445(434),226(106),114(107),91(86),78(76),53(51),2(2),0(0)","kind":"string","unresolved":false},{"index":14,"name":"CardStatus","raw":"Card OK.","kind":"string","unresolved":true},{"index":15,"name":"MaxProcTime","raw":"81240","kind":"number","unresolved":false},{"index":16,"name":"MaxBuffDepth","raw":"0","kind":"number","unresolved":true},{"index":17,"name":"MaxSystemProcTime","raw":"788","kind":"number","unresolved":true},{"index":18,"name":"MaxSlowProcTime(1)","raw":"10350364","kind":"number","unresolved":true},{"index":19,"name":"MaxSlowProcTime(2)","raw":"8703216","kind":"number","unresolved":true},{"index":20,"name":"MaxSlowProcTime(3)","raw":"2531229","kind":"number","unresolved":true},{"index":21,"name":"MaxSlowProcTime(4)","raw":"0","kind":"number","unresolved":true},{"index":22,"name":"PortStatus(1)","raw":"false","kind":"Boolean","unresolved":false},{"index":23,"name":"PortStatus(2)","raw":"false","kind":"Boolean","unresolved":false},{"index":24,"name":"PortStatus(3)","raw":"false","kind":"Boolean","unresolved":false},{"index":25,"name":"PortStatus(4)","raw":"true","kind":"Boolean","unresolved":false},{"index":26,"name":"PortStatus(5)","raw":"true","kind":"Boolean","unresolved":false},{"index":27,"name":"PortStatus(6)","raw":"true","kind":"Boolean","unresolved":false},{"index":28,"name":"PortStatus(7)","raw":"true","kind":"Boolean","unresolved":false},{"index":29,"name":"PortStatus(8)","raw":"true","kind":"Boolean","unresolved":false},{"index":30,"name":"SW12Volts(1)","raw":"true","kind":"Boolean","unresolved":false},{"index":31,"name":"SW12Volts(2)","raw":"true","kind":"Boolean","unresolved":false}];
const dfield = (p: any, n: number): any => n===8
  ? claim(p,'d-ambient-field') : claim(p,'d41r04-response-'+n);
const dstatus = (p: any, n: number): any => n===2
  ? claim(p,'d-panel-example') : claim(p,'d41r04-status-'+n);

function campbellSourceOracle(p: any): string[] {
  const errs: string[]=[];
  if(p.subjects.length!==3 || p.subjects.some((s:any)=>!s.standing.startsWith('REFERENCE_')) ||
     p.originalEvents.length || p.representations.length) errs.push('D-REFERENCE-ONLY');
  if(p.assertions.filter((a:any)=>a.about==='d-climavue'&&a.concept==='output.native_field').length!==14)
    errs.push('D-AR7-FIELD-COUNT');
  for(const r of sourceClimaResponse){
    const a=dfield(p,r.index);
    if(a?.about!=='d-climavue' || a?.standing!=='SOURCE_FACT' ||
       a?.value?.nativeField!=='aR7! position '+r.index ||
       a?.value?.raw!==String(r.index) ||
       a?.value?.unit!==(r.index===8?'position (°C)':r.unit) ||
       (r.index!==8 && !a?.value?.interpretation?.includes(r.label)))
      errs.push('D-R'+String(r.index).padStart(2,'0'));
  }
  if(p.assertions.filter((a:any)=>a.about==='d-logger'&&a.concept==='output.example_value').length!==31)
    errs.push('D-LOGGER-STATUS-COUNT');
  for(const x of sourceLoggerStatus){
    const a=dstatus(p,x.index);
    if(a?.about!=='d-logger' || a?.standing!=='SOURCE_EXAMPLE' ||
       a?.concept!=='output.example_value' || a?.value?.raw!==x.raw ||
       a?.value?.nativeField!==x.name || (x.unresolved && !a?.value?.interpretation?.includes('UNRESOLVED')))
      errs.push('D-S'+String(x.index).padStart(2,'0'));
  }
  if(claim(p,'d-installed')?.standing!=='UNKNOWN' ||
     claim(p,'d-connection')?.concept!=='equipment.design_connection' ||
     claim(p,'d41r04-address')?.concept!=='configuration.documented_default' ||
     claim(p,'d41r04-action')?.concept!=='configuration.supported_action')
    errs.push('D-DESIGN-VS-INSTALLED');
  return errs;
}
function bennettSourceOracle(p: any): string[] {
  const errs: string[]=[];
  const eq=[
    ['b-baro2','R1510517'],
    ['b-wind2','WM166288'],
    ['b-par1','22346']
  ];
  if(p.subjects.length!==8||subject(p,'b-station')?.sourceIdentity?.raw!=='acebpmet' ||
     eq.some(([id,serial])=>subject(p,id)?.sourceIdentity?.raw!==serial ||
       subject(p,id)?.standing!=='SOURCE_IDENTIFIED_EQUIPMENT')) errs.push('B-OTHER-EQUIPMENT');
  if(p.assertions.filter((a:any)=>a.concept==='equipment.role_service').length!==6 ||
     eq.some(([id])=>{const a=claim(p,'b41r04-use-'+id.slice(2));
       return a?.about!==id||a?.target!=='b-station'||
         a?.time?.precision!=='CALENDAR_DAY'||a?.time?.startDate!=='2024-04-16'||
         a?.time?.asOfDate!=='2024-12-31'}))
     errs.push('B-DATE-QUALIFIED-ROLES');
  if(claim(p,'b41r04-site-point')?.about!=='b-station' ||
     claim(p,'b41r04-site-point')?.concept!=='location.station_position' ||
     claim(p,'b41r04-site-point')?.value?.raw!=='32.55934 N, -80.45456 W' ||
     claim(p,'b-probe-position')?.standing!=='UNKNOWN')
     errs.push('B-STATION-NOT-PROBE-GEO');
  if(claim(p,'b41r04-maint16')?.about!=='b-station' ||
     claim(p,'b41r04-maint16')?.concept!=='lifecycle.maintenance_note' ||
     claim(p,'b41r04-maint16')?.time?.sourceStamp!=='04/16/2024 09:45–13:30 EST')
     errs.push('B-APR16-STATION-MAINTENANCE');
  if(claim(p,'b41r04-maint17')?.about!=='b-logger' ||
     claim(p,'b41r04-maint17')?.time?.precision!=='CALENDAR_DAY' ||
     claim(p,'b41r04-maint17')?.time?.startDate!=='2024-04-17' ||
     claim(p,'b41r04-os-version')?.about!=='b-logger' ||
     claim(p,'b41r04-os-version')?.value?.raw!=='CR1000X.Std.07.02')
     errs.push('B-APR17-LOGGER-OS');
  if(p.originalEvents.length!==2 || p.representations.length!==4 ||
     p.assertions.filter((a:any)=>a.concept==='observation.result_time').some((a:any)=>a.standing!=='UNKNOWN') ||
     claim(p,'b-qc15')?.value?.raw!=='<0> '||claim(p,'b-qc18')?.value?.raw!=='<0> '||
     claim(p,'b-record-flag15')?.value?.raw!==''||claim(p,'b-record-flag18')?.value?.raw!=='')
     errs.push('B-TWO-ORIGINALS-RAW-QA-UNKNOWN');
  return errs;
}
function clean(p:any) {
  const m=model(p);
  expect(m.accepted).toBe(true);
  expect(m.issues).toEqual([]);
  expect(m.claims.every(c=>c.recognized)).toBe(true);
  expect(m.raw).toBe(p);
  const presentation=buildPacketPresentation(p);
  expect(presentation.nativeCsapiCarrier).toBe(false);
  expect(presentation.sourceAuthenticated).toBe(false);
  expect(presentation.mappablePosition).toBeNull();
}

test('Campbell extended reference packet preserves first-generation ClimaVue and separate CR1000X',()=>{
  const p=packet('campbell');clean(p);
  expect([p.subjects.length,p.assertions.length,p.originalEvents.length]).toEqual([3,56,0]);
  expect(campbellSourceOracle(p)).toEqual([]);
});
test('All fourteen aR7 response-position names, units, order and original sensor scope survive',()=>{
  const p=packet('campbell');clean(p);
  expect(sourceClimaResponse).toHaveLength(14);
  expect(sourceClimaResponse.map(x=>dfield(p,x.index).value.nativeField))
    .toEqual(sourceClimaResponse.map(x=>'aR7! position '+x.index));
  expect(dfield(p,11).value.unit).toBe('fraction 0–1');
  expect(dfield(p,10).value.unit).toBe('kPa');
  expect(dfield(p,8).value.unit).toBe('position (°C)'); // original old packet retained verbatim
  expect(campbellSourceOracle(p)).toEqual([]);
});
test('All thirty-one logger Status example values are separate and preserve raw field lexical types',()=>{
  const p=packet('campbell');clean(p);
  expect(sourceLoggerStatus).toHaveLength(31);
  expect(sourceLoggerStatus.map(x=>dstatus(p,x.index).value.nativeField))
    .toEqual(sourceLoggerStatus.map(x=>x.name));
  expect(sourceLoggerStatus.map(x=>dstatus(p,x.index).value.raw))
    .toEqual(sourceLoggerStatus.map(x=>x.raw));
  expect(sourceLoggerStatus.filter(x=>x.kind==='number')).toHaveLength(18);
  expect(sourceLoggerStatus.filter(x=>x.kind==='string')).toHaveLength(3);
  expect(sourceLoggerStatus.filter(x=>x.kind==='Boolean')).toHaveLength(10);
});
test('Campbell unknown Status field semantics stay explicitly unresolved, not healthy or measured',()=>{
  const p=packet('campbell');clean(p);
  expect(sourceLoggerStatus.filter(x=>x.unresolved)).toHaveLength(13);
  expect(sourceLoggerStatus.filter(x=>x.unresolved).every(x=>
    dstatus(p,x.index).value.interpretation.includes('UNRESOLVED'))).toBe(true);
  expect(dstatus(p,14).value.raw).toBe('Card OK.');
  expect(dstatus(p,3).value.raw).toBe('13.2368');
  expect(dstatus(p,25).value.raw).toBe('true');
});
test('Campbell source documented SDI-12 command/address/supply does not imply executed actions or actual unit',()=>{
  const p=packet('campbell');clean(p);
  expect(claim(p,'d41r04-address').value.raw).toBe('0');
  expect(claim(p,'d41r04-action').value.raw).toBe('aAb!');
  expect(claim(p,'d-installed').standing).toBe('UNKNOWN');
  expect(model(p).events).toHaveLength(0);
});
test('Published logger Status example cannot be promoted to real instrument measurement',()=>{
  const p=packet('campbell');claim(p,'d41r04-status-3').about='d-climavue';
  expect(model(p).accepted).toBe(true); // shape cannot authenticate source
  expect(campbellSourceOracle(p)).toContain('D-S03');
});
test('Logger published Card OK string cannot become independently proven physical health',()=>{
  const p=packet('campbell');claim(p,'d41r04-status-14').standing='SOURCE_FACT';
  expect(model(p).accepted).toBe(true);
  expect(campbellSourceOracle(p)).toContain('D-S14');
});
test('Humidity source fraction cannot be silently relabeled percentage',()=>{
  const p=packet('campbell');claim(p,'d41r04-response-11').value.unit='%';
  expect(model(p).accepted).toBe(true);
  expect(campbellSourceOracle(p)).toContain('D-R11');
});
test('Bennett historical reference remains a source-identified continuing station with 3 more actual instruments',()=>{
  const p=packet('bennett');clean(p);
  expect([p.subjects.length,p.assertions.length,p.originalEvents.length,p.representations.length])
    .toEqual([8,37,2,4]);
  expect(bennettSourceOracle(p)).toEqual([]);
  expect(p.subjects.filter((x:any)=>x.standing==='SOURCE_IDENTIFIED_EQUIPMENT')).toHaveLength(7);
});
test('Bennett original two EE181s and three use statements are preserved; additional roles are date-only',()=>{
  const p=packet('bennett');clean(p);
  expect(['21281600077814','222016000109CE'].every(s=>
     p.subjects.some((x:any)=>x.sourceIdentity?.raw===s))).toBe(true);
  expect(p.assertions.filter((x:any)=>x.concept==='equipment.role_service')).toHaveLength(6);
  expect(bennettSourceOracle(p)).toEqual([]);
});
test('Bennett has two original NOAA means, four old experimental copies and original QA whitespace',()=>{
  const p=packet('bennett');clean(p);
  const m=model(p); expect(m.events).toHaveLength(2);
  expect(m.events.map(x=>x.copies.length)).toEqual([2,2]);
  expect(claim(p,'b-qc15').value.raw).toBe('<0> ');
  expect(claim(p,'b-qc18').value.raw).toBe('<0> ');
  expect(claim(p,'b-record-flag15').value.raw).toBe('');
  expect(claim(p,'b-result-time15').standing).toBe('UNKNOWN');
  expect(claim(p,'b-producing-system18').standing).toBe('UNKNOWN');
});
test('Station coordinates remain station-specific text; original per-probe geometry is unknown and Map unfilled',()=>{
  const p=packet('bennett');clean(p);
  expect(claim(p,'b41r04-site-point').about).toBe('b-station');
  expect(claim(p,'b-probe-position').standing).toBe('UNKNOWN');
  expect(view(p,'operational/Equipment').some(x=>x.id==='b41r04-site-point')).toBe(true);
  expect(buildPacketPresentation(p).mappablePosition).toBeNull();
});
test('Station 16 April multi-instrument service is not an exact EE181 exchange; 17 April logger OS is separate',()=>{
  const p=packet('bennett');clean(p);
  expect(claim(p,'b41r04-maint16').about).toBe('b-station');
  expect(claim(p,'b41r04-maint17').about).toBe('b-logger');
  expect(claim(p,'b41r04-maint17').time.precision).toBe('CALENDAR_DAY');
  expect(view(p,'activity/Table').filter(x=>x.concept==='lifecycle.maintenance_note')).toHaveLength(2);
});
test('Bennett actual OS version reported as of 2024 is not an installed future version of a probe',()=>{
  const p=packet('bennett');clean(p);
  expect(claim(p,'b41r04-os-version').value.raw).toBe('CR1000X.Std.07.02');
  expect(claim(p,'b41r04-os-version').about).toBe('b-logger');
  expect(view(p,'management/Configuration').some(x=>x.id==='b41r04-os-version')).toBe(true);
});
test('Campbell and Bennett pass same project reader without manufacturer-name or event-count special cases',()=>{
 for(const name of ['campbell','bennett'] as const){
   const p=packet(name);clean(p);
   expect(packetClaimsForView(buildPacketPresentation(p),'management/Sources')).toHaveLength(p.assertions.length);
 }
});
test('Mutating station point into per-probe location is still structurally possible but source-oracle-false',()=>{
  const p=packet('bennett');claim(p,'b41r04-site-point').about='b-probe3';
  expect(model(p).accepted).toBe(true);
  expect(bennettSourceOracle(p)).toContain('B-STATION-NOT-PROBE-GEO');
});
test('Mutating the maintenance window into exact probe swap is source-oracle-false',()=>{
  const p=packet('bennett');claim(p,'b41r04-maint16').about='b-probe4';
  expect(model(p).accepted).toBe(true);
  expect(bennettSourceOracle(p)).toContain('B-APR16-STATION-MAINTENANCE');
});
test('A changed as-of date on another sensor is rejected by the historical source oracle',()=>{
  const p=packet('bennett');claim(p,'b41r04-use-baro2').time.asOfDate='2026-11-03';
  expect(model(p).accepted).toBe(true);
  expect(bennettSourceOracle(p)).toContain('B-DATE-QUALIFIED-ROLES');
});
test('41R-04 packet version keeps known older concepts and guards only newly introduced meanings',()=>{
  for(const name of ['campbell','bennett'] as const){
    const p=packet(name);clean(p);
    expect(p.format).toBe('dim-csapi-source-packet.s41r04.v0.1');
    p.format='dim-csapi-source-packet.s41r03.v0.1';
    expect(model(p).accepted).toBe(true);
    // Campbell's new field/example claims reuse supported 41R-03 concept meanings.
    // Bennett adds station-position, mounting, historical-maintenance, dated OS terms.
    expect(model(p).claims.some(x=>x.recognized===false)).toBe(name==='bennett');
    expect(model(p).raw).toBe(p);
  }
});
test('Unsupported format cannot be mislabeled as a supported native CSAPI Profile',()=>{
 const p=packet('campbell');p.format='application/sml+json';
 expect(model(p).accepted).toBe(false);
 expect(model(p).issues.some(x=>x.path==='/format')).toBe(true);
});
test('Reference examples cannot become original performed observations through a fake logger sample event',()=>{
 const p=packet('campbell');
 p.originalEvents.push({id:'false-event',subject:'d-logger',sourceId:'d07',
   recordLocator:'publisher example',nativeField:'Battery'});
 expect(model(p).accepted).toBe(false);
 expect(model(p).issues.some(x=>x.message.includes('reference-only'))).toBe(true);
});
