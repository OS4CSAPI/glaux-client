import dragino from './examples/s31-lb-design.sml.json';
import campbell from './examples/campbell-temperature-roles.json';

// The JSON inputs are snapshots of Candidate_Specification/examples at this research commit.
export const researchRoot = 'https://github.com/OS4CSAPI/glaux-client/blob/aa655461ac949648f32398291f7e00e77532e9c1/Docs/Research/DIM_Profile_V2/';
export const caseKey = 'temperature';
interface Field { name: string; definition: string; label: string; uom: {code: string} }
interface Output { name: string; fields: readonly Field[] }
export interface Description { context: string; output: Output }
export interface PublishedValue { context: string; output: string; values: Readonly<Record<string,number>> }
export interface MeasurementRow { context: string; output: string; field: Field; value: number | undefined }

/** An output from one source cannot lend a number to another source, even for the same property. */
export function measurementRows(descriptions: readonly Description[], examples: readonly PublishedValue[]): MeasurementRow[] {
  const indexed = new Map<string, MeasurementRow>();
  const key = (context: string, output: string, field: string) => JSON.stringify([context,output,field]);
  for (const {context,output} of descriptions) for (const field of output.fields) {
    const id = key(context,output.name,field.name);
    if (indexed.has(id)) throw new Error('Duplicate measurement definition: '+id);
    indexed.set(id, {context,output:output.name,field,value:undefined});
  }
  for (const item of examples) for (const [name,value] of Object.entries(item.values)) {
    const id = key(item.context,item.output,name);
    const row = indexed.get(id);
    if (!row || row.value !== undefined || !Number.isFinite(value)) throw new Error('Unmatched, repeated or invalid reading: '+id);
    row.value = value;
  }
  return [...indexed.values()];
}

const probe = dragino.components[0];
const probeContext = 'S31-LB probe example';
export const descriptions: Description[] = [{context:probeContext,output:probe.outputs[0]}, ...campbell.descriptions];
// Dragino historical-message entry C-E01, NOT its FPort 2 instantaneous sample layout.
const e01 = new DataView(Uint8Array.from([0x00,0x00,0x02,0x36,0x01,0x10,0x40,0x64,0x6d,0x84,0xe1]).buffer);
export const examples: PublishedValue[] = [{context:probeContext,output:probe.outputs[0].name,values:{temperature:e01.getInt16(4,false)/10,relativeHumidity:e01.getUint16(2,false)/10}}, ...campbell.examples];
export const measures = measurementRows(descriptions, examples);
export const sourceGroups = [
  {context:probeContext, title:'Dragino S31-LB', detail:'One external SHT31 probe', source:'Dragino published history example · C-E01', url:researchRoot+'Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md#4-every-record-in-the-original-published-history-example', raw:{temperature:'FPort 3 · bytes 4–5',relativeHumidity:'FPort 3 · bytes 2–3'}},
  {context:campbell.descriptions[0].context, title:'Campbell CR1000X', detail:'Datalogger wiring panel',source:'Campbell published logger status example · PanelTemp',url:campbell.descriptions[0].source,raw:{PanelTemp:'PanelTemp'}},
  {context:campbell.descriptions[1].context, title:'Campbell ClimaVue 50',detail:'First-generation weather instrument',source:'ClimaVue 50 manual · Table 8-1, p. 21',url:campbell.descriptions[1].source,raw:{airTemperature:'aR7! · position 8',humiditySensorTemperature:'aR7! · position 12'}},
] satisfies {context:string;title:string;detail:string;source:string;url:string;raw:Record<string,string>}[];

export function readingText(row: MeasurementRow): string {
  if (row.value === undefined) return 'No reading supplied';
  const u = row.field.uom.code;
  return String(row.value)+' '+(u==='Cel'?'°C':u);
}
