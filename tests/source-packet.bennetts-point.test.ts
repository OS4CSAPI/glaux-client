import { readFileSync } from 'node:fs';
import { expect, test } from 'vitest';
import { interpretSourcePacket } from '../src/profile/source-packet';

/**
 * Step 37: ACTUAL HISTORICAL SOURCE CASE. The oracle below belongs ONLY IN TESTS.
 * One real ACE Basin/NERRS station, two original NOAA/CDMO source measurements,
 * two source-identified physical EE181 individuals, three date-qualified service
 * statements and four PREVIOUS PROJECT EXPERIMENTAL CSAPI representations.
 *
 * Research source-selection JSON Git blob:
 *   38d226842d1b88bda9940748ebb1763a34fa2376
 * Project Step 32 packet Git blob:
 *   83bd92f22b19a1f6a1f9a4c1e3444e64e546bf60
 *
 * NOT a new download of the full 2024 NOAA CSV, original PDF reinspection,
 * current live HTTP/52North read, OGC schema/format conformance test, or proof
 * of original result availability, exact probe swap, or active 2026 equipment.
 */
const directory = new URL('./fixtures/source-packets/', import.meta.url);
const fixture = (): any => JSON.parse(readFileSync(new URL('bennetts-point.historical.packet.json', directory), 'utf8'));
const frozen = (): any => JSON.parse(readFileSync(new URL('bennetts-point.source-selection.json', directory), 'utf8'));
const read = (input: unknown) => interpretSourcePacket(input);
const claim = (p: any, id: string): any => p.assertions.find((x: any) => x.id === id);
const subject = (p: any, id: string): any => p.subjects.find((x: any) => x.id === id);
const report = (p: any, id: string): any => p.originalEvents.find((x: any) => x.id === id);

const days = ['15','18'] as const;
// These old representation IDs were independently recorded in PITON v1.9;
// they are TEST ORACLES, never shared-client hard-coded interpretation keys.
const historicCopies: Record<string, [string, string]> = {
  'b-event15': ['4f3d3010-9e46-4227-9ba0-7d7014405efa', 'a742b704-c2cd-4c1d-970a-b97b5f628130'],
  'b-event18': ['33599d37-7992-4e14-a4c1-b0df85d62fc2', '50bf940e-55a0-45b6-9331-e6391704f6c7'],
};

/**
 * Independent original-source/frozen-selection oracle. It tests source truth,
 * while the GENERIC reader tests only packet consistency and references.
 * Source-specific station/serial/row identifiers are forbidden in src/profile.
 */
function sourceOracle(p: any, s: any): string[] {
  const errors: string[] = [];
  const expectedSerials = [...new Set(s.unit_use_history.map((x: any) => x.serial))].sort();
  const physical = p.subjects.filter((x: any) => x.standing === 'SOURCE_IDENTIFIED_EQUIPMENT' &&
    x.sourceIdentity?.scheme === 'EE181 serial number');
  const actualSerials = physical.map((x: any) => x.sourceIdentity.raw).sort();
  if (p.focus !== 'b-station' || p.subjects.length !== 5 ||
    subject(p,'b-station')?.standing !== 'SOURCE_IDENTIFIED_STATION' ||
    subject(p,'b-station')?.sourceIdentity?.raw !== s.station.station_code ||
    subject(p,'b-logger')?.sourceIdentity?.raw !== s.logger_context.documented_logger_serial)
    errors.push('B37-identity: one real continuing station and separate source-identified logger, not invented equipment');
  if (JSON.stringify(actualSerials) !== JSON.stringify(expectedSerials) || physical.length !== 2)
    errors.push('B37-probes: exactly two individually serial-numbered EE181 units, including the returning one');
  const serviceIds = ['b-service3-early','b-service4','b-service3-return'];
  const service = p.assertions.filter((x: any) => x.concept === 'equipment.role_service');
  if (service.length !== 3 || serviceIds.some(id => !claim(p,id)))
    errors.push('B37-service-count: exactly three dated service statements, not three physical instruments');
  const expectedSubjects = ['b-probe3','b-probe4','b-probe3'];
  for (let i=0;i<3;i++) {
    const a = claim(p,serviceIds[i]), original = s.unit_use_history[i];
    if (!a || a.about !== expectedSubjects[i] || a.target !== 'b-station' ||
      a.standing !== 'SOURCE_FACT' || a.time?.precision !== 'CALENDAR_DAY' ||
      a.time?.startDate !== original.first_date_of_use ||
      (original.last_date_of_use_listed !== undefined &&
        a.time?.endDateListed !== original.last_date_of_use_listed) ||
      (original.still_in_use_as_of !== undefined &&
        (a.time?.asOfDate !== original.still_in_use_as_of || a.time?.endDateListed !== undefined))) {
      errors.push('B37-service-precision: original calendar-day boundaries and 2024 as-of cannot become exact swap or removal');
      break;
    }
  }
  if (p.originalEvents.length !== 2 ||
    p.originalEvents.some((x: any) => x.subject !== 'b-station' || x.sourceId !== 'b-cdmo' || x.nativeField !== 'ATemp') ||
    !['b-event15','b-event18'].every(id => report(p,id)))
    errors.push('B37-event-count: exactly two ORIGINAL NOAA 15-minute mean air-temperature source records');
  if (p.representations.length !== 4 || p.representations.some((x: any) =>
      x.standing !== 'HISTORICAL_PROJECT_EXPERIMENT') ||
    !['b-event15','b-event18'].every(id => {
      const found = p.representations.filter((r: any) => r.originalEventId === id);
      const refs = historicCopies[id];
      return found.length === 2 && found.every((r: any) => refs.some(ref => r.resourceRef.endsWith(ref))) &&
        new Set(found.map((r: any) => r.resourceRef)).size === 2;
    }))
    errors.push('B37-representation: four specific historical experiment copies represent TWO original source events');
  if (p.sources.find((x: any) => x.id === 'b-cdmo')?.url !== s.measurement_file.csv ||
    !p.sources.find((x: any) => x.id === 'b-cdmo')?.edition.includes(s.measurement_file.sha256))
    errors.push('B37-source-edition: preserve original NOAA archive locator and recorded snapshot hash');
  for (let i=0;i<2;i++) {
    const d = days[i], obs = s.readings[i], fields = obs.source_fields, event = 'b-event'+d;
    const id = report(p,event);
    if (!id || !id.recordLocator.includes('CSV line '+obs.csv_line) ||
      claim(p,'b-mean'+d)?.value?.raw !== fields.ATemp ||
      claim(p,'b-mean'+d)?.standing !== 'SOURCE_FACT' ||
      claim(p,'b-stamp'+d)?.value?.raw !== fields.DatetimeStamp ||
      claim(p,'b-stamp'+d)?.time?.precision !== 'SOURCE_LOCAL_MINUTE' ||
      !claim(p,'b-stamp'+d)?.time?.basis.includes('Eastern Standard Time') ||
      claim(p,'b-station-token'+d)?.value?.raw !== fields.StationCode ||
      claim(p,'b-record-flag'+d)?.value?.raw !== fields.F_Record ||
      claim(p,'b-qc'+d)?.value?.raw !== fields.F_ATemp ||
      claim(p,'b-qc'+d)?.evidence[0]?.nativeToken !== fields.F_ATemp)
      errors.push('B37-original-row-'+d+': ATemp, station stamp, padded station code and exact raw F_ATemp/F_Record differ');
    const period = claim(p,'b-period'+d);
    const end = obs.normalized_timestamp_utc;
    const begin = new Date(Date.parse(end)-15*60*1000).toISOString().replace('.000Z','Z');
    if (period?.standing !== 'DERIVED' || period?.time?.precision !== 'DERIVED_UTC_INTERVAL' ||
      period?.time?.derivedStartUtc !== begin || period?.time?.derivedEndUtc !== end ||
      period?.value?.raw !== begin+'/'+end ||
      !period?.derivation?.inputs.includes('b-stamp'+d) ||
      !period?.derivation?.inputs.includes('b-method'))
      errors.push('B37-derived-period-'+d+': source EST stamp and 15-min window are separate from derived UTC period');
    const attr = claim(p,'b-attribution'+d);
    const targetSerial = subject(p,attr?.target)?.sourceIdentity?.raw;
    if (attr?.standing !== 'DERIVED' ||
      targetSerial !== obs.attribution_from_equipment_history.serial ||
      !attr?.derivation?.inputs.includes('b-period'+d) ||
      !attr?.derivation?.inputs.some((x: string) => x.startsWith('b-service')))
      errors.push('B37-derived-probe-'+d+': source-joined probe attribution must remain DERIVED, not NOAA-authored');
    for (const field of ['observation.result_time','observation.producing_system']) {
      const a = p.assertions.find((x: any) => x.about === event && x.concept === field);
      if (a?.standing !== 'UNKNOWN' || a.value !== undefined || a.target !== undefined)
        errors.push('B37-unknown-'+d+': source does not establish original resultTime or a single completed-mean producer');
    }
  }
  if (claim(p,'b-probe-position')?.standing !== 'UNKNOWN' ||
    claim(p,'b-probe-position')?.value !== undefined)
    errors.push('B37-location: station site point is NOT independent per-probe coordinates');
  if (s.excluded_example?.F_ATemp !== '<-3> [GPR] (CSM)' || p.originalEvents.some((x: any) =>
    x.recordLocator.includes('10322')))
    errors.push('B37-rejected-row: 17 Apr temperature is a rejected quality control, not a third accepted original');
  return errors;
}

test('unchanged shared reader accepts real historical source packet with five declared subjects and 23 evidence claims', () => {
  const p=fixture(), original=JSON.stringify(p), model=read(p);
  expect(model.accepted).toBe(true);
  expect(model.issues).toEqual([]);
  expect(model.focus?.standing).toBe('SOURCE_IDENTIFIED_STATION');
  expect(model.focus?.sourceIdentity?.raw).toBe('acebpmet');
  expect(model.subjects).toHaveLength(5);
  expect(model.claims).toHaveLength(23);
  expect(sourceOracle(p,frozen())).toEqual([]);
  expect(model.raw).toBe(p);
  expect(JSON.stringify(p)).toBe(original);
});

test('two actual EE181 serial-numbered individuals carry THREE day-only service statements, one returning', () => {
  const p=fixture(), m=read(p);
  const probeSerials=m.subjects.filter(s=>s.sourceIdentity?.scheme==='EE181 serial number')
    .map(s=>s.sourceIdentity?.raw).sort();
  expect(probeSerials).toEqual(['21281600077814','222016000109CE'].sort());
  const dates=m.claims.filter(a=>a.concept==='equipment.role_service');
  expect(dates).toHaveLength(3);
  expect(dates.map(a=>a.about)).toEqual(['b-probe3','b-probe4','b-probe3']);
  expect(dates.every(a=>(a.time as any)?.precision==='CALENDAR_DAY')).toBe(true);
  expect((dates[2].time as any).asOfDate).toBe('2024-12-31');
  expect((dates[2].time as any).endDateListed).toBeUndefined();
});

test('two original NOAA mean air temperature events are NOT four observations from experimental API copies', () => {
  const m=read(fixture());
  expect(m.events).toHaveLength(2);
  expect(m.events.map(e=>e.id)).toEqual(['b-event15','b-event18']);
  expect(m.events.map(e=>e.copies.length)).toEqual([2,2]);
  expect(m.events.every(e=>e.copies.every(c=>c.standing==='HISTORICAL_PROJECT_EXPERIMENT'))).toBe(true);
});

test('exact original NOAA values, fixed-EST source stamps and parameter-specific QA whitespace are unmodified', () => {
  const m=read(fixture()), src=frozen();
  for(let i=0;i<2;i++){
    const d=days[i], fields=src.readings[i].source_fields;
    expect(m.claims.find(c=>c.id==='b-mean'+d)?.value?.raw).toBe(fields.ATemp);
    expect(m.claims.find(c=>c.id==='b-stamp'+d)?.value?.raw).toBe(fields.DatetimeStamp);
    expect(m.claims.find(c=>c.id==='b-qc'+d)?.value?.raw).toBe('<0> ');
    expect(m.claims.find(c=>c.id==='b-station-token'+d)?.value?.raw).toBe('acebpmet  ');
    expect(m.claims.find(c=>c.id==='b-record-flag'+d)?.value?.raw).toBe('');
  }
  expect(m.events).toHaveLength(2);
});

test('15-minute UTC intervals are DERIVED, and cannot become original phenomenon/result-time facts', () => {
  const m=read(fixture());
  const intervals=m.claims.filter(c=>c.concept==='observation.nominal_period');
  expect(intervals).toHaveLength(2);
  expect(intervals.every(c=>c.standing==='DERIVED')).toBe(true);
  expect(intervals.map(c=>(c.time as any).derivedStartUtc)).toEqual([
    '2024-04-15T16:45:00Z','2024-04-18T16:45:00Z',
  ]);
  expect(intervals.map(c=>(c.time as any).derivedEndUtc)).toEqual([
    '2024-04-15T17:00:00Z','2024-04-18T17:00:00Z',
  ]);
  expect(intervals.every(c=>c.derivation?.inputs.includes('b-method'))).toBe(true);
});

test('probe attribution for both NOAA means is a DERIVED join to separate equipment history', () => {
  const m=read(fixture()), mappings=m.claims.filter(c=>c.concept==='observation.contributing_equipment');
  expect(mappings).toHaveLength(2);
  expect(mappings.map(c=>[c.about,c.target,c.standing])).toEqual([
    ['b-event15','b-probe4','DERIVED'], ['b-event18','b-probe3','DERIVED'],
  ]);
  expect(mappings.every(c=>c.derivation?.inputs.some(i=>i.startsWith('b-service')))).toBe(true);
});

test('historical original resultTime and producing System are UNKNOWN, and probe coordinates unproven', () => {
  const m=read(fixture());
  const unresolved=m.claims.filter(c=>c.standing==='UNKNOWN');
  expect(unresolved).toHaveLength(5);
  expect(unresolved.every(c=>c.kind==='unknown'&&c.value===undefined&&c.target===undefined)).toBe(true);
  for(const d of days){
    expect(m.claims.find(c=>c.id==='b-result-time'+d)?.standing).toBe('UNKNOWN');
    expect(m.claims.find(c=>c.id==='b-producing-system'+d)?.standing).toBe('UNKNOWN');
  }
  expect(m.claims.find(c=>c.id==='b-probe-position')?.standing).toBe('UNKNOWN');
});

test('four source history limitations remain visible in packet HOLDs, not solved by reader acceptance', () => {
  const p=fixture();
  expect(p.holds).toHaveLength(9);
  expect(p.holds.some((h:any)=>h.gap==='G30-01')).toBe(true);
  expect(p.holds.some((h:any)=>h.gap==='G30-04')).toBe(true);
  expect(p.holds.some((h:any)=>h.gap==='G30-05')).toBe(true);
  expect(p.holds.some((h:any)=>h.gap==='G30-06')).toBe(true);
  expect(read(p).accepted).toBe(true);
});

test('opaque packet-local IDs and labels do not decide the generic source-reader meanings', () => {
  const p=fixture(), q=structuredClone(p);
  const rename=(v:string)=>'opaque-'+v;
  q.id='another-source-packet';q.focus=rename(q.focus);
  q.subjects.forEach((x:any)=>{x.id=rename(x.id); x.label='Unrelated title';});
  q.originalEvents.forEach((x:any)=>{x.id=rename(x.id);x.subject=rename(x.subject);});
  q.representations.forEach((x:any)=>{x.originalEventId=rename(x.originalEventId);});
  q.assertions.forEach((x:any)=>{
    x.id=rename(x.id); x.about=rename(x.about);
    if(x.target)x.target=rename(x.target);
    if(x.derivation)x.derivation.inputs=x.derivation.inputs.map(rename);
  });
  const before=read(p),after=read(q);
  expect(after.accepted).toBe(true);
  expect(after.claims.map(x=>[x.concept,x.kind,x.standing,x.value?.raw]))
    .toEqual(before.claims.map(x=>[x.concept,x.kind,x.standing,x.value?.raw]));
  expect(after.events.map(x=>x.copies.length)).toEqual([2,2]);
});

test('broken evidence link to nonexistent original archive source is REJECTED', () => {
  const p=fixture();claim(p,'b-qc15').evidence[0].sourceId='not-source';
  const result=read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x=>x.message.includes('Evidence must resolve'))).toBe(true);
});

test('a source-identified serial association pointing to missing probe is REJECTED', () => {
  const p=fixture();claim(p,'b-attribution15').target='nonexistent-probe';
  const result=read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x=>x.message.includes('Relationship target'))).toBe(true);
});

test('an invented literal resultTime attached to an explicitly UNKNOWN claim is REJECTED', () => {
  const p=fixture();claim(p,'b-result-time15').value={raw:'2024-04-15T17:00:00Z'};
  const result=read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x=>x.message.includes('UNKNOWN'))).toBe(true);
});

test('source-event representation whose originalEventId does not resolve is REJECTED', () => {
  const p=fixture();p.representations[0].originalEventId='nonexistent-source-event';
  const result=read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x=>x.message.includes('Copy does not resolve'))).toBe(true);
});

test('same original source report copied into a second event with identical row/field is REJECTED', () => {
  const p=fixture();p.originalEvents.push({...structuredClone(p.originalEvents[0]),id:'duplicate-source-event'});
  const result=read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x=>x.message.includes('same original source record/field'))).toBe(true);
});

test('DERIVED probe attribution referencing a nonexistent input assertion is REJECTED', () => {
  const p=fixture();claim(p,'b-attribution15').derivation.inputs.push('fictional-source-input');
  const result=read(p);
  expect(result.accepted).toBe(false);
  expect(result.issues.some(x=>x.message.includes('Input assertion ID does not resolve'))).toBe(true);
});

test('source-FALSE third EE181 physical instrument is accepted structurally but rejected against original history', () => {
  const p=fixture();p.subjects.push({id:'invented-probe',label:'third probe',
    standing:'SOURCE_IDENTIFIED_EQUIPMENT',
    sourceIdentity:{issuer:'ACE Basin operator metadata',scheme:'EE181 serial number',raw:'NOT-IN-OPERATOR-HISTORY'}});
  expect(read(p).accepted).toBe(true);
  expect(sourceOracle(p,frozen())).toContain('B37-probes: exactly two individually serial-numbered EE181 units, including the returning one');
});

test('source-FALSE original 2024 as-of changed into a removal date is accepted structurally but rejected', () => {
  const p=fixture();claim(p,'b-service3-return').time.endDateListed='2024-12-31';
  expect(read(p).accepted).toBe(true);
  expect(sourceOracle(p,frozen())).toContain('B37-service-precision: original calendar-day boundaries and 2024 as-of cannot become exact swap or removal');
});

test('source-FALSE calendar-day service upgraded to exact time is accepted structurally but rejected', () => {
  const p=fixture();const a=claim(p,'b-service4');
  a.time.precision='SOURCE_LOCAL_MINUTE';a.time.sourceStamp='2024-04-16T09:45:00-05:00';
  expect(read(p).accepted).toBe(true);
  expect(sourceOracle(p,frozen())).toContain('B37-service-precision: original calendar-day boundaries and 2024 as-of cannot become exact swap or removal');
});

test('source-FALSE probe attribution swapped across NOAA rows is accepted structurally but rejected', () => {
  const p=fixture();claim(p,'b-attribution15').target='b-probe3';
  expect(read(p).accepted).toBe(true);
  expect(sourceOracle(p,frozen())).toContain('B37-derived-probe-15: source-joined probe attribution must remain DERIVED, not NOAA-authored');
});

test('source-FALSE inferred probe attribution relabeled NOAA SOURCE_FACT is accepted structurally but rejected', () => {
  const p=fixture();const a=claim(p,'b-attribution18');
  a.standing='SOURCE_FACT';delete a.derivation;
  expect(read(p).accepted).toBe(true);
  expect(sourceOracle(p,frozen())).toContain('B37-derived-probe-18: source-joined probe attribution must remain DERIVED, not NOAA-authored');
});

test('source-FALSE raw QA token trimmed and original F_Record merged is accepted structurally but rejected', () => {
  const p=fixture();claim(p,'b-qc15').value.raw='<0>';claim(p,'b-record-flag18').value.raw='<0> ';
  expect(read(p).accepted).toBe(true);
  expect(sourceOracle(p,frozen())).toContain('B37-original-row-15: ATemp, station stamp, padded station code and exact raw F_ATemp/F_Record differ');
  expect(sourceOracle(p,frozen())).toContain('B37-original-row-18: ATemp, station stamp, padded station code and exact raw F_ATemp/F_Record differ');
});

test('source-FALSE original resultTime fabricated from station stamp with changed standing is accepted structurally', () => {
  const p=fixture();const a=claim(p,'b-result-time15');
  a.standing='SOURCE_FACT';a.value={raw:'2024-04-15T17:00:00Z'};
  expect(read(p).accepted).toBe(true);
  expect(sourceOracle(p,frozen())).toContain('B37-unknown-15: source does not establish original resultTime or a single completed-mean producer');
});

test('source-FALSE project-derived interval shifted one minute is accepted structurally but rejected', () => {
  const p=fixture();claim(p,'b-period15').time.derivedStartUtc='2024-04-15T16:44:00Z';
  expect(read(p).accepted).toBe(true);
  expect(sourceOracle(p,frozen())).toContain('B37-derived-period-15: source EST stamp and 15-min window are separate from derived UTC period');
});

test('source-FALSE third original NOAA event with new row locator is accepted structurally but rejected', () => {
  const p=fixture();p.originalEvents.push({id:'fictional-third',subject:'b-station',
    sourceId:'b-cdmo',recordLocator:'CSV line 10419 (fictional)',nativeField:'ATemp'});
  expect(read(p).accepted).toBe(true);
  expect(sourceOracle(p,frozen())).toContain('B37-event-count: exactly two ORIGINAL NOAA 15-minute mean air-temperature source records');
});

test('source-FALSE experimental copy silently joined to wrong original event is accepted structurally but rejected', () => {
  const p=fixture();p.representations.find((r:any)=>r.id==='b-r18-report').originalEventId='b-event15';
  expect(read(p).accepted).toBe(true);
  expect(sourceOracle(p,frozen())).toContain('B37-representation: four specific historical experiment copies represent TWO original source events');
});

test('source-FALSE independent original producer invented is accepted structurally but rejected', () => {
  const p=fixture();const a=claim(p,'b-producing-system18');
  a.standing='SOURCE_FACT';a.target='b-probe3';
  expect(read(p).accepted).toBe(true);
  expect(sourceOracle(p,frozen())).toContain('B37-unknown-18: source does not establish original resultTime or a single completed-mean producer');
});

test('no simulated current operation or rejected 17 April NOAA value is installed as a real third result', () => {
  const p=fixture(),s=frozen();
  expect(s.excluded_example.F_ATemp).toBe('<-3> [GPR] (CSM)');
  expect(p.originalEvents.every((x:any)=>!x.recordLocator.includes('10322'))).toBe(true);
  expect(sourceOracle(p,s)).toEqual([]);
  expect(p.assertions.some((x:any)=>x.concept==='configuration.effective_setting')).toBe(false);
  // The selected source lacks original result availability and per-probe surveyed coordinates.
});
