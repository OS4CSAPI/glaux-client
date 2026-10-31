/**
 * Decode a source-qualified SWE DataRecord carried as an archival-report result.
 * This is NOT a decoder for native interval-valued CSAPI phenomenonTime or a
 * generic result-quality standard. It follows definitions in the live schema.
 */
export interface ArchivedObservationContext {
  air: number | null;
  unit: string | null;
  sourceStamp: string | null;
  averagingWindow: [string, string] | null;
  sourceQualityFlag: string | null;
  attributedSystemUid: string | null;
  issues: string[];
}

type Dict = Record<string, unknown>;
const isDict = (v: unknown): v is Dict => Boolean(v) && typeof v === 'object' && !Array.isArray(v);
const definition = {
  air: 'https://vocab.nerc.ac.uk/standard_name/air_temperature/',
  stamp: 'http://www.opengis.net/def/property/OGC/0/SamplingTime',
  window: 'urn:merlin:dim-v2:bennetts:nominal-averaging-window',
  qc: 'urn:merlin:dim-v2:bennetts:source-F_ATemp',
  probe: 'urn:merlin:dim-v2:bennetts:attributed-sensing-unit-uid',
} as const;

export function decodeArchivedObservation(stream: unknown, observation: unknown, systemUid: string): ArchivedObservationContext {
  const result: ArchivedObservationContext = {
    air: null, unit: null, sourceStamp: null, averagingWindow: null,
    sourceQualityFlag: null, attributedSystemUid: null, issues: [],
  };
  const fail = (message: string): void => { result.issues.push(message); };
  if (!isDict(stream) || !isDict(observation) || !isDict(observation.result)) {
    fail('The stream or its observation report is unavailable.');
    return result;
  }
  const schema = stream.schema;
  if (!isDict(schema) || schema.obsFormat !== 'application/json') {
    fail('The stream did not supply the expected application/json observation schema.');
    return result;
  }
  const record = schema.resultSchema;
  if (!isDict(record) || record.type !== 'DataRecord' || !Array.isArray(record.fields)) {
    fail('The observation result is not declared as a SWE DataRecord.');
    return result;
  }
  const fields = record.fields.filter(isDict);
  const getField = (key: keyof typeof definition, expectedType: string): [Dict, unknown] | null => {
    const matches = fields.filter(f=>f.definition===definition[key] && f.type===expectedType && typeof f.name==='string');
    if (matches.length !== 1) { fail('Missing or ambiguous '+key+' field definition.'); return null; }
    const f=matches[0];
    const v=observation.result as Dict;
    if (!Object.prototype.hasOwnProperty.call(v,f.name as string)) {fail('Missing '+key+' value.');return null;}
    return [f,v[f.name as string]];
  };
  const temp = getField('air','Quantity');
  if(temp) {
    if(typeof temp[1] === 'number' && Number.isFinite(temp[1])) result.air=temp[1];
    else fail('Temperature value is not a finite number.');
    if(isDict(temp[0].uom) && typeof temp[0].uom.code==='string')result.unit=temp[0].uom.code;
    else fail('The result schema does not state a temperature unit.');
  }
  const stamp=getField('stamp','Time');
  if(stamp) {
    if(typeof stamp[1]==='string' && !Number.isNaN(Date.parse(stamp[1])))result.sourceStamp=stamp[1];
    else fail('Source stamp is not a valid ISO time.');
  }
  const window=getField('window','TimeRange');
  if(window){
    if(Array.isArray(window[1]) && window[1].length===2 &&
       window[1].every(x=>typeof x==='string' && !Number.isNaN(Date.parse(x))) &&
       Date.parse(window[1][0]) < Date.parse(window[1][1])){
      result.averagingWindow=[window[1][0],window[1][1]];
      if(Date.parse(window[1][1])-Date.parse(window[1][0])!==900000)fail('The recorded nominal averaging window is not 15 minutes.');
    } else fail('The nominal averaging interval is not a valid TimeRange.');
  }
  const qc=getField('qc','Text');
  if(qc) {
    if(typeof qc[1]==='string')result.sourceQualityFlag=qc[1];
    else fail('Original operator QA flag is not text.');
  }
  const probe=getField('probe','Text');
  if(probe) {
    if(typeof probe[1]==='string'){
      result.attributedSystemUid=probe[1];
      if(probe[1]!==systemUid)fail('The report attribution does not match the selected physical System.');
    } else fail('Attributed System UID is not text.');
  }
  if(result.sourceStamp && result.averagingWindow &&
    Date.parse(result.sourceStamp)!==Date.parse(result.averagingWindow[1])) {
    fail('The record timestamp does not equal the nominal averaging window end.');
  }
  return result;
}

/** Interpret only the original reserve QA code; retain the token separately. */
export function describeReserveTemperatureFlag(raw: string | null): string {
  if(raw===null)return 'No source quality flag was recovered.';
  return raw.trim()==='<0>' ? '0 — passed initial QA/QC checks (not a calibration certificate)' :
    'Source flag retained; no passing-quality interpretation inferred.';
}
