import { readFileSync } from 'node:fs';
import { expect, test } from 'vitest';
import { interpretSourcePacket } from '../src/profile/source-packet';
import { buildPacketPresentation, packetClaimsForView } from '../src/profile/source-packet-presentation';

/**
 * 41R-03 bounded original-source COVERAGE tests. Source-specific oracles below
 * are TEST-SIDE ONLY; the same generic reader/projection is used for both
 * manufacturer references and the unchanged original Step 32 cases.
 * Fourteen / fifteen new claims are project-authored selections from the
 * original Dragino C / AirGradient A controlled evidence sheets, not actual
 * field data, complete vendor datasets or a native CSAPI Profile carrier.
 */
const read = (name: 'dragino' | 'airgradient'): any => JSON.parse(readFileSync(
  new URL('../public/fixtures/source-packets/' + name + '.coverage.packet.json', import.meta.url), 'utf8'));
const claim = (p: any, id: string): any => p.assertions.find((x: any) => x.id === id);
const model = (p: any) => interpretSourcePacket(p);
const view = (p: any, key: Parameters<typeof packetClaimsForView>[1]) =>
  packetClaimsForView(buildPacketPresentation(p), key);
const clean = (p: any) => {
  const m = model(p);
  expect(m.accepted).toBe(true);
  expect(m.issues).toEqual([]);
  expect(m.claims.every(c => c.recognized)).toBe(true);
  expect(m.raw).toBe(p);
  expect(buildPacketPresentation(p).sourceAuthenticated).toBe(false);
  expect(buildPacketPresentation(p).nativeCsapiCarrier).toBe(false);
  expect(p.originalEvents).toEqual([]);
  expect(p.representations).toEqual([]);
  expect(p.subjects.every((s: any) => s.standing.startsWith('REFERENCE_'))).toBe(true);
};

/** Source sheet C / original Dragino manual + pinned decoder: not the Glaux interpreter. */
const draginoSourceOracle = (p: any) => {
  const issues: string[] = [];
  if (p.subjects.length !== 2 || p.subjects[0]?.standing !== 'REFERENCE_ARRANGEMENT' ||
      p.subjects[1]?.standing !== 'REFERENCE_COMPONENT') issues.push('C-I01/02 reference identity');
  if (claim(p, 'c41-default')?.value?.raw !== '20' ||
      claim(p, 'c41-default')?.value?.unit !== 'min' ||
      claim(p, 'c41-default')?.standing !== 'SOURCE_FACT') issues.push('C-O03 documented default');
  if (claim(p, 'c41-command-example')?.standing !== 'SOURCE_EXAMPLE' ||
      claim(p, 'c41-command-example')?.value?.raw !== '60000' ||
      claim(p, 'c41-command-example')?.value?.unit !== 'ms') issues.push('C-C01 printed AT command example');
  if (claim(p, 'c-effective')?.standing !== 'UNKNOWN' ||
      claim(p, 'c41-installed-firmware')?.standing !== 'UNKNOWN')
    issues.push('C-I16/C-O03 actual setting and firmware remain unknown');
  for (const [id, expected] of [
    ['c41-fport2', 'FPort 2'], ['c41-fport3', 'FPort 3'], ['c41-fport5', 'FPort 5'],
  ]) if (claim(p, id)?.value?.raw !== expected) issues.push('C-FPort message kind ' + expected);
  if (claim(p, 'c41-status-bat')?.value?.raw !== 'BAT' ||
      claim(p, 'c41-status-firmware')?.value?.raw !== 'FIRMWARE_VERSION')
    issues.push('C-S02/S05 source-defined status field');
  if (p.originalEvents.length !== 0 || p.representations.length !== 0)
    issues.push('C-G03 unsupported performed event');
  return issues;
};

/** Source sheet A / two independent pinned hardware & firmware READMEs: test-only oracle. */
const airgradientSourceOracle = (p: any) => {
  const issues: string[] = [];
  const byId = (id: string) => p.subjects.find((s: any) => s.id === id);
  const ids = ['a-main', 'a-co2', 'a-sgp41', 'a-sht40', 'a-gas', 'a-ce'];
  if (p.subjects.length !== 9 || byId('a-max')?.standing !== 'REFERENCE_ARRANGEMENT' ||
      ids.some(id => byId(id)?.standing !== 'REFERENCE_COMPONENT') ||
      byId('a-pm1')?.sourceIdentity?.raw !== 'PM1' ||
      byId('a-pm2')?.sourceIdentity?.raw !== 'PM2') issues.push('A-I01/06–12 reference physical modules');
  if (p.assertions.filter((x: any) => x.concept === 'equipment.reference_component').length !== 8)
    issues.push('A-I06 reference component count');
  if (p.assertions.filter((x: any) => x.concept === 'output.native_field').length !== 3)
    issues.push('A-F04/05/06 PM fields are not hardware sockets');
  if (claim(p, 'a41-solar')?.value?.raw !== '10' ||
      claim(p, 'a41-solar')?.value?.unit !== 'W' ||
      !claim(p, 'a41-battery')?.value?.raw?.includes('three 3,500 mAh'))
    issues.push('A-P01/P02 design panel/cell topology, not measured pack capacity');
  if (claim(p, 'a41-network-default')?.concept !== 'configuration.documented_default' ||
      claim(p, 'a41-network-default')?.value?.raw !== 'Cellular' ||
      claim(p, 'a41-network-default')?.standing !== 'SOURCE_FACT' ||
      claim(p, 'a41-firmware-revision')?.standing !== 'SOURCE_FACT' ||
      claim(p, 'a41-installed-firmware')?.standing !== 'UNKNOWN')
    issues.push('A-I04/A-C02 reference default/firmware versus actual');
  if (claim(p, 'a41-cell-report')?.value?.raw !== 'Cellular: nominal 3-minute samples; payload every 9 minutes (HTTP/MQTT), failed batches cached temporarily' ||
      claim(p, 'a41-wifi-report')?.value?.raw !== 'Wi-Fi: HTTP JSON one sample every 3 minutes; no retransmission cache')
    issues.push('A-C10/12 separate network reporting');
  if (claim(p, 'a-example')?.standing !== 'SOURCE_EXAMPLE' ||
      claim(p, 'a-installed')?.standing !== 'UNKNOWN' ||
      p.originalEvents.length !== 0 || p.representations.length !== 0)
    issues.push('A-F05/A-G01/G03 no fielded readings/serial');
  return issues;
};

test('Dragino enlarged source packet retains exactly one reference SHT31 and no performed observations', () => {
  const p = read('dragino'); clean(p);
  expect(model(p).claims).toHaveLength(21);
  expect(model(p).subjects).toHaveLength(2);
  expect(draginoSourceOracle(p)).toEqual([]);
});

test('Dragino design default is not a printed AT example or effective configuration', () => {
  const p = read('dragino'); clean(p);
  expect([claim(p, 'c41-default').value.raw, claim(p, 'c41-command-example').value.raw])
    .toEqual(['20', '60000']);
  expect(claim(p, 'c41-command-example').standing).toBe('SOURCE_EXAMPLE');
  expect(claim(p, 'c-effective').standing).toBe('UNKNOWN');
  expect(view(p, 'management/Configuration').some(x => x.id === 'c41-default')).toBe(true);
  expect(view(p, 'management/Configuration').some(x => x.id === 'c41-command-example')).toBe(true);
});

test('Dragino current/history/status FPorts are distinct documented messages, not new observations', () => {
  const p = read('dragino'); clean(p);
  expect(['FPort 2','FPort 3','FPort 5'].every(
    raw => view(p, 'operational/Communications').some(x => x.value?.raw === raw))).toBe(true);
  expect(['BAT','FIRMWARE_VERSION'].every(raw =>
    view(p, 'operational/Communications').some(x => x.value?.raw === raw))).toBe(true);
  expect(model(p).events).toEqual([]);
});

test('Dragino approved source-oracle negative: falsified default remains structurally accepted', () => {
  const p=read('dragino');claim(p,'c41-default').value.raw='1';
  expect(model(p).accepted).toBe(true);
  expect(draginoSourceOracle(p)).toContain('C-O03 documented default');
});

test('Dragino source-oracle negative: published example promoted to fact fails source truth', () => {
  const p=read('dragino');claim(p,'c41-command-example').standing='SOURCE_FACT';
  expect(model(p).accepted).toBe(true);
  expect(draginoSourceOracle(p)).toContain('C-C01 printed AT command example');
});

test('Dragino structural negative: inventing an installed firmware value in UNKNOWN is rejected', () => {
  const p=read('dragino');claim(p,'c41-installed-firmware').value={raw:'1.3'};
  expect(model(p).accepted).toBe(false);
});

test('AirGradient enlarged design includes distinct modules without duplicating PM outputs', () => {
  const p=read('airgradient'); clean(p);
  expect(model(p).subjects).toHaveLength(9);
  expect(model(p).claims).toHaveLength(22);
  expect(airgradientSourceOracle(p)).toEqual([]);
  expect(view(p, 'operational/Equipment').filter(x=>x.concept==='equipment.reference_component')).toHaveLength(8);
  expect(view(p,'operational/Communications').filter(x=>x.concept==='output.native_field')).toHaveLength(3);
});

test('AirGradient solar rating and three-cell 3S design do not create a measured charge or invented pack mAh', () => {
  const p=read('airgradient'); clean(p);
  expect(claim(p, 'a41-solar').value.raw).toBe('10');
  expect(claim(p, 'a41-solar').value.unit).toBe('W');
  expect(claim(p, 'a41-battery').value.raw).toContain('series (3S)');
  expect(p.assertions.some((x:any)=> x.concept==='power.remaining_charge')).toBe(false);
  expect(view(p,'operational/Condition').some(x=>x.id==='a41-battery')).toBe(true);
});

test('AirGradient distinct cellular and Wi-Fi documented behavior is generic communications, not telemetry', () => {
  const p=read('airgradient'); clean(p);
  const communications=view(p,'operational/Communications');
  expect(communications.filter(x=>x.concept==='communications.documented_reporting')).toHaveLength(2);
  expect(communications.some(x=>x.id==='a41-wifi')).toBe(true);
  expect(communications.some(x=>x.id==='a41-cellular')).toBe(true);
  expect(model(p).events).toHaveLength(0);
});

test('AirGradient firmware source snapshot is not installed firmware, and Cellular default is not selected mode', () => {
  const p=read('airgradient'); clean(p);
  expect(claim(p,'a41-network-default').value.raw).toBe('Cellular');
  expect(claim(p,'a41-firmware-revision').value.raw).toBe('84e479a415d81151e7a81aea9a2f7449a15e98cc');
  expect(claim(p,'a41-installed-firmware').standing).toBe('UNKNOWN');
  expect(view(p,'management/Configuration').some(x=>x.id==='a41-installed-firmware')).toBe(true);
  expect(p.assertions.some((x:any)=>x.concept==='configuration.effective_setting')).toBe(false);
});

test('AirGradient false hardware component inferred from pm25 is structurally accepted, rejected by source oracle', () => {
  const p=read('airgradient');p.subjects.push({id:'invented-pm3',label:'PMS5003 at PM3',standing:'REFERENCE_COMPONENT'});
  p.assertions.push({id:'fake-pm3',about:'a-max',concept:'equipment.reference_component',
    standing:'SOURCE_FACT',target:'invented-pm3',evidence:[{sourceId:'a01',locator:'PM3 not in original'}]});
  expect(model(p).accepted).toBe(true);
  expect(airgradientSourceOracle(p)).toContain('A-I01/06–12 reference physical modules');
});

test('AirGradient source false: published default relabeled as effective setting remains source false', () => {
  const p=read('airgradient');claim(p,'a41-network-default').concept='configuration.effective_setting';
  expect(model(p).accepted).toBe(true);
  expect(p.assertions.some((x:any)=>x.concept==='configuration.effective_setting')).toBe(true);
  expect(airgradientSourceOracle(p)).toContain('A-I04/A-C02 reference default/firmware versus actual');
});

test('AirGradient source false: 9-minute cellular report is not proof of effective 9-minute device setting', () => {
  const p=read('airgradient');claim(p,'a41-cell-report').value.raw='Cellular observed active transmit interval 9 minutes';
  expect(model(p).accepted).toBe(true);
  expect(airgradientSourceOracle(p)).toContain('A-C10/12 separate network reporting');
});

test('Both enlarged packets stay inspectable raw in Management/Sources, with unverified issuer standing', () => {
  for(const name of ['dragino','airgradient'] as const) {
    const p=read(name);clean(p);const projection=buildPacketPresentation(p);
    expect(packetClaimsForView(projection,'management/Sources')).toHaveLength(p.assertions.length);
    expect(projection.warnings.some(w=>w.includes('does not authenticate source issuer'))).toBe(true);
    expect(projection.mappablePosition).toBeNull();
    expect(model(p).events).toHaveLength(0);
  }
});

test('A reference-only originalEvent cannot be manufactured by either expanded packet', () => {
  for(const name of ['dragino','airgradient'] as const){
    const p=read(name);p.originalEvents.push({id:'fictional',subject:p.focus,
      sourceId:p.sources[0].id,recordLocator:'printed manual example',nativeField:'sample'});
    expect(model(p).accepted).toBe(false);
    expect(model(p).issues.some(x=>x.message.includes('reference-only'))).toBe(true);
  }
});
