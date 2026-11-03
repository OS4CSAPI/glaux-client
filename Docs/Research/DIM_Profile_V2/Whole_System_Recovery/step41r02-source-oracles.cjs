'use strict';
/*
 * Step 41R-02: bounded research SOURCE-ORACLE tests.
 * This is NOT the generic Glaux reader, a native CSAPI validator, or proof of
 * manufacturer/NOAA cryptographic authenticity.
 * Oracle constants are source-scoped and derived from controlled original
 * evidence inventories plus the preserved Bennett selection. NO client use.
 * Run from repository root:
 * node Docs/Research/DIM_Profile_V2/Whole_System_Recovery/step41r02-source-oracles.cjs
 */
function verifyCase(name, packet, preservedBennett) {
  const problems = [];
  const bad = (id, condition) => { if (condition) problems.push(id); };
  const sub = id => packet.subjects.find(s => s.id === id);
  const claim = id => packet.assertions.find(a => a.id === id);
  const original = preservedBennett;
  const same = (x, y) => JSON.stringify(x) === JSON.stringify(y);
  const rel = concept => packet.assertions.filter(a => a.concept === concept);
  const source = id => packet.sources.find(s => s.id === id);
  const reference = name !== 'bennett';
  bad('COMMON-SOURCES', !Array.isArray(packet.sources) || packet.sources.some(s =>
    !s.issuer || !s.url || !s.edition || !s.researchTrace || !s.authority));
  bad('COMMON-EVIDENCE', packet.assertions.some(a =>
    !Array.isArray(a.evidence) || a.evidence.length === 0 ||
    a.evidence.some(e => !source(e.sourceId) || !e.locator)));
  if (reference) bad('COMMON-REFERENCE-EVENTS', packet.originalEvents.length !== 0 ||
    packet.representations.length !== 0);
  if (name === 'dragino') {
    bad('D-IDENTITY', packet.focus !== 'c-s31' || packet.subjects.length !== 2 ||
      sub('c-s31')?.standing !== 'REFERENCE_ARRANGEMENT' ||
      sub('c-s31')?.sourceIdentity?.raw !== 'S31-LB' ||
      sub('c-s31')?.sourceIdentity?.scheme !== 'model' ||
      sub('c-sht31')?.standing !== 'REFERENCE_COMPONENT');
    bad('D-PROBE', packet.subjects.filter(s => s.standing === 'REFERENCE_COMPONENT').length !== 1 ||
      rel('equipment.external_probe').length !== 1 ||
      claim('c-external')?.target !== 'c-sht31');
    bad('D-FIELDS', rel('output.native_field').length !== 2 ||
      claim('c-temperature-field')?.value?.raw !== 'TempC_SHT31' ||
      claim('c-humidity-field')?.value?.raw !== 'Hum_SHT31' ||
      claim('c-temperature-field')?.value?.unit !== '°C' ||
      claim('c-humidity-field')?.value?.unit !== '% RH' ||
      claim('c-temperature-field')?.about !== 'c-sht31' ||
      claim('c-humidity-field')?.about !== 'c-sht31');
    bad('D-EXAMPLE', claim('c-example')?.standing !== 'SOURCE_EXAMPLE' ||
      claim('c-example')?.value?.raw !== '26.1' ||
      claim('c-example')?.value?.nativeField !== 'TempC_SHT31');
    bad('D-BATTERY', claim('c-battery')?.standing !== 'SOURCE_FACT' ||
      claim('c-battery')?.value?.raw !== '8500' ||
      claim('c-battery')?.value?.unit !== 'mAh');
    bad('D-UNKNOWN', claim('c-installed')?.standing !== 'UNKNOWN' ||
      claim('c-effective')?.standing !== 'UNKNOWN' ||
      claim('c-installed')?.value !== undefined ||
      claim('c-effective')?.value !== undefined);
    bad('D-SOURCE-EDITION', source('c02')?.url !==
      'https://wiki.dragino.com/docs/LoRaWAN-End-Node/temperature-humidity-sensors/s31-lb/' ||
      !source('c03')?.url?.includes('635417693adb215b32ac367c8e8909d9d609a120'));
  } else if (name === 'airgradient') {
    bad('A-IDENTITY', packet.focus !== 'a-max' || packet.subjects.length !== 3 ||
      sub('a-max')?.standing !== 'REFERENCE_ARRANGEMENT' ||
      sub('a-max')?.sourceIdentity?.raw !== 'O-M-1PPSTON-CE');
    bad('A-PHYSICAL', packet.subjects.filter(s => s.standing === 'REFERENCE_COMPONENT').length !== 2 ||
      !sub('a-pm1')?.label?.includes('PMS5003') ||
      !sub('a-pm2')?.label?.includes('PMS5003') ||
      sub('a-pm1')?.sourceIdentity?.raw !== 'PM1' ||
      sub('a-pm2')?.sourceIdentity?.raw !== 'PM2' ||
      rel('equipment.reference_component').length !== 2 ||
      claim('a-socket1')?.target !== 'a-pm1' ||
      claim('a-socket2')?.target !== 'a-pm2');
    bad('A-OUTPUT', rel('output.native_field').length !== 3 ||
      ['pm01','pm25','pm10'].some(field =>
        !rel('output.native_field').some(a => a.about === 'a-max' &&
          a.value?.raw === field && a.value?.nativeField === field &&
          a.value?.unit === 'µg/m³' && a.standing === 'SOURCE_FACT')));
    bad('A-EXAMPLE', claim('a-example')?.standing !== 'SOURCE_EXAMPLE' ||
      claim('a-example')?.value?.raw !== '27.7' ||
      claim('a-example')?.value?.nativeField !== 'pm25');
    bad('A-UNKNOWN', claim('a-installed')?.standing !== 'UNKNOWN');
    bad('A-SOURCE-EDITION', !source('a01')?.url?.includes('89aacf5013fc0ffe4b988a2e3c5a227bce3c4983') ||
      !source('a02')?.url?.includes('84e479a415d81151e7a81aea9a2f7449a15e98cc'));
  } else if (name === 'campbell') {
    bad('C-IDENTITY', packet.focus !== 'd-pair' || packet.subjects.length !== 3 ||
      sub('d-pair')?.standing !== 'REFERENCE_ARRANGEMENT' ||
      sub('d-logger')?.standing !== 'REFERENCE_COMPONENT' ||
      sub('d-climavue')?.standing !== 'REFERENCE_COMPONENT' ||
      sub('d-logger')?.sourceIdentity?.raw !== 'CR1000X' ||
      sub('d-climavue')?.sourceIdentity?.raw !== 'ClimaVue 50');
    bad('C-CONNECTION', claim('d-connection')?.concept !== 'equipment.design_connection' ||
      claim('d-connection')?.about !== 'd-logger' ||
      claim('d-connection')?.target !== 'd-climavue' ||
      claim('d-connection')?.evidence?.[0]?.nativeToken !== 'SDI-12' ||
      rel('equipment.reference_component').length !== 2);
    bad('C-FIELD-COUNT', claim('d-field-count')?.value?.raw !== '14' ||
      claim('d-field-count')?.value?.nativeField !== 'aR7!' ||
      claim('d-ambient-field')?.about !== 'd-climavue' ||
      claim('d-ambient-field')?.value?.raw !== '8' ||
      claim('d-ambient-field')?.value?.nativeField !== 'aR7! position 8' ||
      rel('output.native_field').length !== 2);
    bad('C-PANEL', claim('d-panel-field')?.about !== 'd-logger' ||
      claim('d-panel-field')?.value?.nativeField !== 'PanelTemp' ||
      claim('d-panel-field')?.value?.unit !== '°C');
    bad('C-EXAMPLE', claim('d-panel-example')?.about !== 'd-logger' ||
      claim('d-panel-example')?.standing !== 'SOURCE_EXAMPLE' ||
      claim('d-panel-example')?.value?.raw !== '25.91098' ||
      claim('d-panel-example')?.evidence?.[0]?.sourceId !== 'd07');
    bad('C-UNKNOWN', claim('d-installed')?.standing !== 'UNKNOWN');
    bad('C-SOURCE-EDITION', !source('d02')?.url?.endsWith('/climavue50.pdf') ||
      !source('d02')?.edition?.includes('08/2024') ||
      !source('d07')?.url?.includes('/mqtt/status.html'));
  } else if (name === 'bennett') {
    const expectedProbes = [...new Set(original.unit_use_history.map(u => u.serial))].sort();
    const actualProbes = packet.subjects.filter(s => s.sourceIdentity?.scheme ===
      'EE181 serial number').map(s => s.sourceIdentity.raw).sort();
    bad('B-IDENTITY', packet.focus !== 'b-station' || packet.subjects.length !== 5 ||
      sub('b-station')?.standing !== 'SOURCE_IDENTIFIED_STATION' ||
      sub('b-station')?.sourceIdentity?.raw !== original.station.station_code ||
      sub('b-logger')?.sourceIdentity?.raw !== original.logger_context.documented_logger_serial ||
      sub('b-transmitter')?.sourceIdentity?.raw !== '2335');
    bad('B-PROBES', actualProbes.length !== 2 || !same(actualProbes, expectedProbes));
    const sid = ['b-service3-early','b-service4','b-service3-return'];
    const ssub = ['b-probe3','b-probe4','b-probe3'];
    bad('B-SERVICE-COUNT', rel('equipment.role_service').length !== 3);
    const badService = sid.some((id,i) => {
      const a = claim(id), u = original.unit_use_history[i];
      return !a || a.about !== ssub[i] || a.target !== 'b-station' ||
        a.standing !== 'SOURCE_FACT' || a.time?.precision !== 'CALENDAR_DAY' ||
        a.time?.startDate !== u.first_date_of_use ||
        a.time?.endDateListed !== u.last_date_of_use_listed ||
        a.time?.asOfDate !== u.still_in_use_as_of ||
        a.time?.sourceStamp !== undefined;
    });
    bad('B-SERVICE', badService);
    bad('B-ARCHIVE-ID', source('b-cdmo')?.url !== original.measurement_file.csv ||
      !source('b-cdmo')?.edition?.includes(original.measurement_file.sha256));
    bad('B-EVENTS', packet.originalEvents.length !== 2 ||
      original.readings.some((row,i) => {
        const event = packet.originalEvents.find(e => e.id === ['b-event15','b-event18'][i]);
        return !event || event.subject !== 'b-station' ||
          event.sourceId !== 'b-cdmo' || event.nativeField !== 'ATemp' ||
          !event.recordLocator.includes('CSV line '+row.csv_line);
      }));
    const copyIds = {
      'b-event15':['4f3d3010-9e46-4227-9ba0-7d7014405efa','a742b704-c2cd-4c1d-970a-b97b5f628130'],
      'b-event18':['33599d37-7992-4e14-a4c1-b0df85d62fc2','50bf940e-55a0-45b6-9331-e6391704f6c7'],
    };
    bad('B-REPRESENTATIONS', packet.representations.length !== 4 ||
      Object.entries(copyIds).some(([originalId,ids]) => {
        const copies = packet.representations.filter(r => r.originalEventId === originalId);
        return copies.length !== 2 || copies.some(c => c.standing !==
          'HISTORICAL_PROJECT_EXPERIMENT' ||
          !ids.some(id => c.resourceRef?.endsWith(id))) ||
          new Set(copies.map(c => c.resourceRef)).size !== 2;
      }));
    let lexicalFailure=false, periodFailure=false, attributionFailure=false, unknownFailure=false;
    for (const [i,row] of original.readings.entries()) {
      const d = i === 0 ? '15' : '18';
      const f = row.source_fields;
      const named = [ ['b-mean'+d, f.ATemp], ['b-stamp'+d, f.DatetimeStamp],
        ['b-qc'+d, f.F_ATemp], ['b-station-token'+d, f.StationCode],
        ['b-record-flag'+d, f.F_Record] ];
      if (named.some(([id,v]) => claim(id)?.value?.raw !== v) ||
          claim('b-qc'+d)?.evidence?.[0]?.nativeToken !== f.F_ATemp ||
          claim('b-mean'+d)?.standing !== 'SOURCE_FACT' ||
          claim('b-stamp'+d)?.standing !== 'SOURCE_FACT') lexicalFailure=true;
      const end=row.normalized_timestamp_utc;
      const start = new Date(Date.parse(end)-15*60*1000).toISOString().replace('.000Z','Z');
      const period = claim('b-period'+d);
      if (period?.standing !== 'DERIVED' ||
        period?.time?.precision !== 'DERIVED_UTC_INTERVAL' ||
        period?.time?.derivedStartUtc !== start ||
        period?.time?.derivedEndUtc !== end ||
        period?.value?.raw !== start+'/'+end ||
        !period?.derivation?.inputs?.includes('b-stamp'+d) ||
        !period?.derivation?.inputs?.includes('b-method')) periodFailure=true;
      const attr = claim('b-attribution'+d);
      if (attr?.standing !== 'DERIVED' ||
        sub(attr?.target)?.sourceIdentity?.raw !==
          row.attribution_from_equipment_history.serial ||
        !attr?.derivation?.inputs?.includes('b-period'+d) ||
        !attr?.derivation?.inputs?.some(id => id.startsWith('b-service'))) attributionFailure=true;
      for (const c of ['observation.result_time','observation.producing_system']) {
        const a=packet.assertions.find(x => x.about==='b-event'+d && x.concept===c);
        if (!a || a.standing !== 'UNKNOWN' || a.value !== undefined || a.target !== undefined)
          unknownFailure=true;
      }
    }
    bad('B-LEXICAL', lexicalFailure);
    bad('B-PERIOD', periodFailure);
    bad('B-ATTRIBUTION', attributionFailure);
    bad('B-UNKNOWN', unknownFailure);
    bad('B-LOCATION', claim('b-probe-position')?.standing !== 'UNKNOWN' ||
      claim('b-probe-position')?.value !== undefined);
    bad('B-REJECTED', original.excluded_example.F_ATemp !== '<-3> [GPR] (CSM)' ||
      packet.originalEvents.some(e => e.recordLocator.includes('10322')));
  } else {
    bad('UNKNOWN-CASE',true);
  }
  return problems;
}

function mutations() {
  const claim = (p,id) => p.assertions.find(a => a.id === id);
  const subject = (p,id) => p.subjects.find(s => s.id === id);
  return [
    ['D01','dragino','D-IDENTITY',p => {subject(p,'c-s31').standing='SOURCE_IDENTIFIED_EQUIPMENT';}],
    ['D02','dragino','D-EXAMPLE',p => {claim(p,'c-example').standing='SOURCE_FACT';}],
    ['D03','dragino','D-PROBE',p => {p.subjects.push({id:'invented-probe',label:'Second SHT31',
      standing:'REFERENCE_COMPONENT'});p.assertions.push({id:'false-connection',about:'c-s31',
      concept:'equipment.external_probe',standing:'SOURCE_FACT',target:'invented-probe',
      evidence:[{sourceId:'c02',locator:'C-I02'}]});}],
    ['A01','airgradient','A-IDENTITY',p => {subject(p,'a-max').standing='SOURCE_IDENTIFIED_EQUIPMENT';}],
    ['A02','airgradient','A-OUTPUT',p => {const a=claim(p,'a-pm25');delete a.value;
      a.concept='equipment.reference_component';a.target='a-pm2';}],
    ['A03','airgradient','A-EXAMPLE',p => {claim(p,'a-example').standing='SOURCE_FACT';}],
    ['A04','airgradient','A-PHYSICAL',p => {p.subjects.push({id:'invented-pm3',
      label:'PMS5003 at PM3',standing:'REFERENCE_COMPONENT',
      sourceIdentity:{issuer:'AirGradient',scheme:'hardware socket in reference design',raw:'PM3'}});
      p.assertions.push({id:'fabricated-third',about:'a-max',concept:'equipment.reference_component',
      standing:'SOURCE_FACT',target:'invented-pm3',
      evidence:[{sourceId:'a01',locator:'plug-in modules',nativeToken:'PM3'}]});}],
    ['C01','campbell','C-IDENTITY',p => {subject(p,'d-logger').standing='SOURCE_IDENTIFIED_EQUIPMENT';}],
    ['C02','campbell','C-PANEL',p => {claim(p,'d-panel-field').about='d-climavue';}],
    ['C03','campbell','C-EXAMPLE',p => {claim(p,'d-panel-example').standing='SOURCE_FACT';}],
    ['C04','campbell','C-IDENTITY',p => {for(let i=1;i<=14;i++){
      const id='false-sensor-'+i;p.subjects.push({id,label:'Invented sensor '+i,
      standing:'REFERENCE_COMPONENT'});p.assertions.push({id:'false-link-'+i,
      about:'d-pair',concept:'equipment.reference_component',standing:'SOURCE_FACT',
      target:id,evidence:[{sourceId:'d02',locator:'Table 8-1, output position '+i}]});}}],
    ['C05','campbell','C-CONNECTION',p => {claim(p,'d-connection').concept='equipment.role_service';}],
    ['B01','bennett','B-PROBES',p => {p.subjects.push({id:'invented-probe',label:'third probe',
      standing:'SOURCE_IDENTIFIED_EQUIPMENT',sourceIdentity:{issuer:'ACE Basin operator metadata',
      scheme:'EE181 serial number',raw:'NOT-IN-OPERATOR-HISTORY'}});}],
    ['B02','bennett','B-SERVICE',p => {claim(p,'b-service3-return').time.endDateListed='2024-12-31';}],
    ['B03','bennett','B-SERVICE',p => {const t=claim(p,'b-service4').time;
      t.precision='SOURCE_LOCAL_MINUTE';t.sourceStamp='2024-04-16T09:45:00-05:00';}],
    ['B04','bennett','B-ATTRIBUTION',p => {claim(p,'b-attribution15').target='b-probe3';}],
    ['B05','bennett','B-ATTRIBUTION',p => {const a=claim(p,'b-attribution18');
      a.standing='SOURCE_FACT';delete a.derivation;}],
    ['B06','bennett','B-LEXICAL',p => {claim(p,'b-qc15').value.raw='<0>';
      claim(p,'b-record-flag18').value.raw='<0> ';}],
    ['B07','bennett','B-UNKNOWN',p => {const a=claim(p,'b-result-time15');
      a.standing='SOURCE_FACT';a.value={raw:'2024-04-15T17:00:00Z'};}],
    ['B08','bennett','B-PERIOD',p => {claim(p,'b-period15').time.derivedStartUtc=
      '2024-04-15T16:44:00Z';}],
    ['B09','bennett','B-EVENTS',p => {p.originalEvents.push({id:'fictional-third',
      subject:'b-station',sourceId:'b-cdmo',recordLocator:'CSV line 10419 (fictional)',
      nativeField:'ATemp'});}],
    ['B10','bennett','B-REPRESENTATIONS',p => {
      p.representations.find(r => r.id==='b-r18-report').originalEventId='b-event15';}],
    ['B11','bennett','B-UNKNOWN',p => {const a=claim(p,'b-producing-system18');
      a.standing='SOURCE_FACT';a.target='b-probe3';}],
  ];
}
function run(packets, frozen) {
  const clone=x=>JSON.parse(JSON.stringify(x));
  const cases=['dragino','airgradient','campbell','bennett'];
  const positives=cases.map(name=>({case:name,problems:verifyCase(name,packets[name],frozen)}));
  const negatives=mutations().map(([id,name,expected,mutate])=>{
    const p=clone(packets[name]);mutate(p);
    const problems=verifyCase(name,p,frozen);
    return {id,case:name,expected,detected:problems.includes(expected),problems};
  });
  const failures=[...positives.filter(x=>x.problems.length).map(x=>x.case+': positive failed: '+x.problems),
    ...negatives.filter(x=>!x.detected).map(x=>x.id+': missed '+x.expected)];
  return {standing:'controlled-source-ledger consistency; NOT issuer authentication',
    originalPacketPositive:positives.length,
    originalPacketPass:positives.filter(x=>x.problems.length===0).length,
    negativeOracleCases:negatives.length,
    negativeDetected:negatives.filter(x=>x.detected).length,
    byCase:Object.fromEntries(cases.map(name=>[name,negatives.filter(x=>x.case===name).length])),
    positives,negatives,failures};
}
module.exports={verifyCase,mutations,run};
if (typeof require==='function' && require.main===module) {
  const fs=require('node:fs'),path=require('node:path');
  const dir=path.resolve(__dirname,'../Candidate_Specification');
  const fixture=n=>JSON.parse(fs.readFileSync(path.join(dir,
    'examples/step32-source-packets/'+n+'.json'),'utf8'));
  const packets={
    dragino:fixture('dragino.reference.packet'),
    airgradient:fixture('airgradient.reference.packet'),
    campbell:fixture('campbell.reference.packet'),
    bennett:fixture('bennetts-point.historical.packet'),
  };
  const frozen=JSON.parse(fs.readFileSync(path.join(dir,'examples/bennetts-point-ee181.json'),'utf8'));
  const result=run(packets,frozen);
  console.log(JSON.stringify({standing:result.standing,
    originalPacketPass:result.originalPacketPass,originalPacketPositive:result.originalPacketPositive,
    negativeDetected:result.negativeDetected,negativeOracleCases:result.negativeOracleCases,
    byCase:result.byCase,failures:result.failures},null,2));
  if (result.failures.length) process.exitCode=1;
}
