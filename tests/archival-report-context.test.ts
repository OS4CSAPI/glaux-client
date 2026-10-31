import { describe, expect, it } from 'vitest';
import { decodeArchivedObservation, describeReserveTemperatureFlag } from '../src/profile/archival-report-context';

const archiveStream = {
  schema: {
    obsFormat: 'application/json',
    resultSchema: {
      type: 'DataRecord',
      fields: [
        { name: 'measurement', type: 'Quantity', definition: 'https://vocab.nerc.ac.uk/standard_name/air_temperature/', uom: {code:'Cel'} },
        { name: 'originalFlag', type: 'Text', definition: 'urn:merlin:dim-v2:bennetts:source-F_ATemp' },
        { name: 'averagingPeriod', type: 'TimeRange', definition: 'urn:merlin:dim-v2:bennetts:nominal-averaging-window' },
        { name: 'sourceTime', type: 'Time', definition: 'http://www.opengis.net/def/property/OGC/0/SamplingTime' },
        { name: 'instrument', type: 'Text', definition: 'urn:merlin:dim-v2:bennetts:attributed-sensing-unit-uid' },
      ]
    }
  }
};
const observer = 'urn:merlin:v2:bennetts:ee181:probe4';
const source = {
  result: {
    measurement: 29.1,
    originalFlag: '<0> ',
    averagingPeriod: ['2024-04-15T16:45:00Z','2024-04-15T17:00:00Z'],
    sourceTime: '2024-04-15T17:00:00Z',
    instrument: observer,
  }
};
describe('Live Bennett archival-report context decoder',()=>{
  it('recovers values using typed definitions, not field names or date/serial rules',()=>{
    const decoded=decodeArchivedObservation(archiveStream,source,observer);
    expect(decoded).toEqual({
      air:29.1,unit:'Cel',sourceStamp:'2024-04-15T17:00:00Z',
      averagingWindow:['2024-04-15T16:45:00Z','2024-04-15T17:00:00Z'],
      sourceQualityFlag:'<0> ',attributedSystemUid:observer,issues:[],
    });
    expect(describeReserveTemperatureFlag(decoded.sourceQualityFlag)).toContain('passed initial');
  });
  it('retains a rejected operator flag and does not call it passing',()=>{
    const other={result:{...source.result,originalFlag:'<-3> [GPR] (CSM)'}};
    const decoded=decodeArchivedObservation(archiveStream,other,observer);
    expect(decoded.sourceQualityFlag).toBe('<-3> [GPR] (CSM)');
    expect(describeReserveTemperatureFlag(decoded.sourceQualityFlag)).not.toContain('passed initial');
  });
  it('does not infer a passing flag when source quality is absent',()=>{
    const {originalFlag, ...rest}=source.result;
    const decoded=decodeArchivedObservation(archiveStream,{result:rest},observer);
    expect(decoded.sourceQualityFlag).toBeNull();
    expect(decoded.issues.join(' ')).toContain('Missing qc');
    expect(describeReserveTemperatureFlag(decoded.sourceQualityFlag)).toContain('No source');
  });
  it('reports an observer/identity mismatch instead of rewriting attribution',()=>{
    const decoded=decodeArchivedObservation(archiveStream,{result:{...source.result,instrument:'urn:other:probe'}},observer);
    expect(decoded.attributedSystemUid).toBe('urn:other:probe');
    expect(decoded.issues.join(' ')).toContain('does not match');
  });
  it('does not silently interpret a malformed or non-15-minute period',()=>{
    const decoded=decodeArchivedObservation(archiveStream,{result:{...source.result,averagingPeriod:['2024-04-15T16:55:00Z','2024-04-15T17:00:00Z']}},observer);
    expect(decoded.issues.join(' ')).toContain('not 15 minutes');
  });
  it('does not mistake unlabeled data for qualified record fields',()=>{
    const decoded=decodeArchivedObservation({schema:{resultSchema:{type:'DataRecord',fields:[]}}},source,observer);
    expect(decoded.air).toBeNull();
    expect(decoded.sourceQualityFlag).toBeNull();
    expect(decoded.issues).toHaveLength(1);
  });
});
