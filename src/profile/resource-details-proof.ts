/** Provisional presentation experiment, NOT the published DIM or an OGC application profile.
 * A generic renderer consumes the same source facts as a candidate meaning-aware renderer.
 * No physical Smart Citizen Kit, TRSS or OmniSense unit is authenticated by these fixtures. */
export type EvidenceBasis = 'manufacturer-design' | 'synthetic-source-replay';
export type ViewKey =
  | 'operational/Overview' | 'operational/Equipment' | 'operational/Condition'
  | 'operational/Communications' | 'operational/Map'
  | 'activity/Table' | 'activity/Charts'
  | 'commands/Available' | 'commands/Requests'
  | 'management/Record' | 'management/Configuration' | 'management/Sources';

export interface SourceField {
  groupId: string;
  groupLabel: string;
  term: string;
  sourceLabel: string;
  value: string;
  unit?: string;
  sourceUrl?: string;
  sourceKind: 'characteristic' | 'capability';
}
export interface SourceCase {
  key: string;
  title: string;
  resourceStanding: string;
  identifier: string;
  source: string;
  evidence: EvidenceBasis;
  warning: string;
  fields: SourceField[];
  links: ReadonlyArray<{ label: string; url: string }>;
}
export interface MappedField extends SourceField {
  view: ViewKey;
  section: string;
  displayLabel: string;
  meaning: string;
  caution?: string;
}
interface Rule {
  view: ViewKey;
  section: string;
  meaning: string;
  label?: string;
  caution?: string;
}

/** This is a *candidate client vocabulary*, NOT OGC or published-profile authority.
 * Rules are keyed by declared source term, never by manufacturer name or page type. */
export const candidateRules: Readonly<Record<string, Rule>> = {
  'product-generation': { view:'management/Record', section:'Product kind', meaning:'reusable product kind' },
  'physical-assembly': { view:'operational/Equipment', section:'Physical assembly', meaning:'product-design constituent', caution:'Described hardware, not an independently identified CSAPI System.' },
  'sensing-component': { view:'operational/Equipment', section:'Sensing components and outputs', meaning:'physical sensing component (design)', caution:'Model of an IC, not a separate verified hardware instance.' },
  'supported-measurement': { view:'operational/Equipment', section:'Sensing components and outputs', meaning:'supported measurement output', caution:'Product capability, not a measured Observation or separate physical System.' },
  'power-design': { view:'operational/Condition', section:'Power arrangement', meaning:'power-system design', caution:'Manufacturer description, not present battery condition.' },
  'storage-design': { view:'operational/Equipment', section:'Data handling and storage', meaning:'physical storage design' },
  'communications-path': { view:'operational/Communications', section:'Communication and publishing', meaning:'documented communication capability' },
  'firmware-method': { view:'management/Configuration', section:'Documented measurement methods', meaning:'described reusable method', caution:'Source code is not evidence of an executed observation or installed firmware.' },
  'product-option': { view:'management/Configuration', section:'Supported design options', meaning:'kind-level option', caution:'Exact option selected on a physical Kit is unverified.' },
  'digital-association': { view:'management/Record', section:'Digital representation', meaning:'software record relationship', caution:'Not a physical subsystem.' },
  'sensor-string-label': { view:'management/Record', section:'Source identifiers and labels', meaning:'source system-string designation', caution:'Not a certified physical serial number.' },
  'detector-position': { view:'operational/Equipment', section:'Detector positions', meaning:'configured detector slot' },
  'selected-detector-type': { view:'operational/Equipment', section:'Detector positions', meaning:'source-described detector selection', caution:'A selected type is not an authenticated hardware inventory.' },
  'detector-orientation': { view:'operational/Equipment', section:'Detector positions', meaning:'configured orientation' },
  'supported-detector-type': { view:'management/Configuration', section:'Supported detector choices', meaning:'available device option', caution:'Availability is not a statement that the option is installed.' },
  'orientation-constraint': { view:'management/Configuration', section:'Supported detector choices', meaning:'configuration constraint' },
  'estimated-capacity-remaining': { view:'operational/Condition', section:'Battery estimate', meaning:'source application estimate', caution:'Estimated percentage, not measured battery voltage or measured state-of-charge.' },
  'estimate-status': { view:'operational/Condition', section:'Battery estimate', meaning:'source estimate status' },
  'estimator-internal-battery-count': { view:'operational/Condition', section:'Estimator inputs', meaning:'battery-estimator input' },
  'estimator-battery-nominal-voltage': { view:'operational/Condition', section:'Estimator inputs', meaning:'nominal estimator input', caution:'Not a live battery-voltage reading.' },
  'estimator-external-battery-count': { view:'operational/Condition', section:'Estimator inputs', meaning:'battery-estimator input' },
  'estimator-temperature-input': { view:'operational/Condition', section:'Estimator inputs', meaning:'temperature used by estimator', caution:'Not an ambient-temperature observation.' },
  'reported-message-count': { view:'operational/Condition', section:'Estimator inputs', meaning:'source application count' },
  'reported-time-on': { view:'operational/Condition', section:'Estimator inputs', meaning:'source duration label' },
  'reported-transducer-label': { view:'operational/Equipment', section:'Reported transducers', meaning:'reported transducer label', caution:'Not an individually identified physical component.' },
  'reported-battery-voltage': { view:'operational/Condition', section:'Historically reported electrical condition', meaning:'source-reported voltage', caution:'Not estimated capacity, remaining lifetime or current readiness.' },
  'voltage-kind': { view:'operational/Condition', section:'Historically reported electrical condition', meaning:'voltage qualifier' },
  'unverified-source-clock': { view:'operational/Condition', section:'Source time information', meaning:'unverified literal source time', caution:'Clock and timezone unverified; not a current Observation timestamp.' },
  'source-mode': { view:'operational/Condition', section:'Reported operating information', meaning:'reported source mode', caution:'Historical synthetic replay, not live state.' },
  'source-report-interval': { view:'operational/Communications', section:'Reported communications configuration', meaning:'literal reported interval' },
  'source-on-time': { view:'operational/Condition', section:'Reported operating information', meaning:'literal uptime field' },
};
export const termsRetainedAsProvenance: ReadonlySet<string> = new Set([
  'source-document', 'source-locator', 'assertion-basis', 'source-time-status', 'fixture-note',
]);

const docBase = 'https://github.com/fablabbcn/smartcitizen-docs/blob/0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f/';
const fwBase = 'https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/';
const product = docBase+'docs/hardware/kit/index.md#L59-L123';
const board = docBase+'docs/hardware/boards/urban-board.md#L47-L59';
const assembly = docBase+'docs/guides/getting-started/kit-assembly.md#L114-L149';
const sckFw = fwBase+'sam/src/SckUrban.cpp';
const dataBoard = docBase+'docs/hardware/boards/data-board.md#L22-L40';
function claim(groupId: string, groupLabel: string, term: string, sourceLabel: string, value: string, sourceUrl: string, sourceKind:'characteristic'|'capability'='characteristic'):SourceField {
  return { groupId,groupLabel,term,sourceLabel,value,sourceUrl,sourceKind };
}

/** Product-kind facts sourced from the completed I01-I13 study; NOT a CSAPI System instance. */
export const smartCitizenDesign: SourceCase = {
  key: 'sck23',
  title: 'Smart Citizen Kit 2.3',
  resourceStanding: 'Manufacturer product-kind description',
  identifier: 'No verified physical-unit identifier',
  source: 'Fab Lab Barcelona · pinned SCK2.3 design',
  evidence: 'manufacturer-design',
  warning: 'This is a description of a documented model, NOT a retrieved physical System. No installed configuration, actual observation or live status has been verified.',
  links: [
    { label:'Product and sensor table',url:product },
    { label:'Assembly instructions',url:assembly },
    { label:'Pinned firmware',url:sckFw+'#L842-L895' },
    { label:'13-step integrated case study',url:'https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Case_Studies/Real_Equipment_DIM_Validation/I13_Integrated_Smart_Citizen_Case_Study_and_Gate_D_v0.1_28OCT2026.md' }
  ],
  fields: [
    claim('kind','Kind / generation','product-generation','Product generation','Smart Citizen Kit 2.3',product),
    claim('assembly','Normal enclosure assembly','physical-assembly','Assembly','Data Board + Urban Board',assembly),
    claim('assembly','Normal enclosure assembly','physical-assembly','Particulate module','Cabled SEN5X family PM sensor, secured inside the enclosure',assembly),
    claim('urban-sht31','SHT31 · temperature / humidity','sensing-component','IC model','SHT31',board),
    claim('urban-sht31','SHT31 · temperature / humidity','supported-measurement','Supports','Temperature',product,'capability'),
    claim('urban-sht31','SHT31 · temperature / humidity','supported-measurement','Supports','Relative humidity',product,'capability'),
    claim('urban-as7331','AS7331 · ultraviolet','sensing-component','IC model','AS7331',board),
    claim('urban-as7331','AS7331 · ultraviolet','supported-measurement','Supports','UV-A',product,'capability'),
    claim('urban-as7331','AS7331 · ultraviolet','supported-measurement','Supports','UV-B',product,'capability'),
    claim('urban-as7331','AS7331 · ultraviolet','supported-measurement','Supports','UV-C',product,'capability'),
    claim('pm-options','Particulate-module variants','product-option','Supported models','SEN50 · SEN54 · SEN55',product,'capability'),
    claim('power','Power design','power-design','Power source','Internal battery, charged/managed on Data Board',dataBoard),
    claim('storage','Data storage','storage-design','Recording','microSD card',assembly),
    claim('storage','Data storage','storage-design','Buffering','Data Board flash memory',dataBoard),
    claim('comms','Manufacturer communications','communications-path','Connectivity','Wi-Fi on Data Board',dataBoard),
    claim('comms','Manufacturer communications','communications-path','Platform transport','MQTT publication path',docBase+'docs/data/data-platform.md#L30-L35'),
    claim('method-sht31','Documented acquisition methods','firmware-method','SHT31 readout','Single-shot command → 6-byte response → CRC validation → temperature/humidity conversion',sckFw+'#L842-L895'),
    claim('method-as7331','Documented acquisition methods','firmware-method','AS7331 readout','Read UV channels with device-ready checks and gain/integration scaling',sckFw+'#L2760-L2815'),
    claim('method-sen5x','Documented acquisition methods','firmware-method','SEN5X readout','State-dependent initiation, warm-up and fresh-reading checks',sckFw+'#L2022-L2100'),
    claim('digital','Vendor digital representation','digital-association','Backend Component','Association of a Device record and a Sensor definition (not a physical part)','https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/app/models/component.rb#L1-L7'),
  ]
};
export const inputFixtures = [
  { key:'trss',path:'/fixtures/trss-etu-ii.json',title:'TRSS ETU-II',resourceStanding:'Synthetic System description',identifier:'urn:example:glaux-client:trss-etu-ii-synthetic',source:'Pinned historical fixture · TRSS',warning:'Synthetic historical replay. Detector selections and a battery estimator are not authenticated installed hardware or current device state.' },
  { key:'core2',path:'/fixtures/omnisense-core2.json',title:'OmniSense Core2',resourceStanding:'Synthetic System description',identifier:'urn:example:glaux-client:omnisense-core2-synthetic',source:'Pinned historical fixture · OmniSense',warning:'Five source-reported transducer labels. No independent physical-part identities or detection-time measurements.' },
  { key:'core5',path:'/fixtures/omnisense-core5ads.json',title:'OmniSense Core5ADS',resourceStanding:'Synthetic System description',identifier:'urn:example:glaux-client:omnisense-core5ads-synthetic',source:'Pinned historical fixture · OmniSense',warning:'Separate historical example from Core2; 15.43 V DC is reported voltage, NOT battery percentage or current operational condition.' },
] as const;
type FixtureKey = typeof inputFixtures[number]['key'];
interface FixtureField {
  name?:unknown;
  label?:unknown;
  definition?:unknown;
  value?:unknown;
  uom?:{code?:unknown};
}
interface FixtureGroup {
  id?:unknown;
  label?:unknown;
  characteristics?:FixtureField[];
  capabilities?:FixtureField[];
}
interface FixtureDocument {
  label?:unknown;
  id?:unknown;
  uniqueId?:unknown;
  characteristics?:FixtureGroup[];
  capabilities?:FixtureGroup[];
}
export function projectSourceFixture(document:FixtureDocument,key:FixtureKey):SourceCase {
  const descriptor=inputFixtures.find(item=>item.key===key);
  if(!descriptor)throw new Error('Unknown fixture source');
  if(typeof document!=='object'||!document)throw new Error('Missing source fixture');
  const fields:SourceField[]=[];
  for(const [section,groups] of [['characteristic',document.characteristics],['capability',document.capabilities]] as const){
    for(const group of groups??[]){
      if(!group||typeof group!=='object')continue;
      const groupId=String(group.id??'unnamed');
      const groupLabel=String(group.label??groupId);
      const items=section==='characteristic'?group.characteristics:group.capabilities;
      for(const item of items??[]){
        if(!item||typeof item!=='object')continue;
        const url=String(item.definition??'');
        // The term URI is the hypothetical profile binding. Unknown URIs remain visible in raw Sources.
        const term=url.split('/').pop()||String(item.name??'undefined');
        const value=typeof item.value==='number'||typeof item.value==='boolean'||typeof item.value==='string'
          ? String(item.value):'(not supplied)';
        fields.push({groupId,groupLabel,term,sourceLabel:String(item.label??item.name??term),value,
          unit:typeof item.uom?.code==='string'?item.uom.code:undefined,
          sourceKind:section});
      }
    }
  }
  if(fields.length===0)throw new Error('Selected fixture has no source fields');
  return {key,title:descriptor.title,resourceStanding:descriptor.resourceStanding,
    identifier:descriptor.identifier,source:descriptor.source,evidence:'synthetic-source-replay',
    warning:descriptor.warning,fields,links:[{
      label:'Synthetic source fixture',
      url:'https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/public'+descriptor.path,
    }]};
}
export function mappedFieldCount(example:SourceCase):number {
  return example.fields.filter(f=>Boolean(candidateRules[f.term])).length;
}
export function mappingsForView(example:SourceCase,view:ViewKey):MappedField[] {
  const mapped=example.fields.flatMap((field):MappedField[]=>{
    const rule=candidateRules[field.term]; if(!rule||termsRetainedAsProvenance.has(field.term))return [];
    return [{...field,view:rule.view,section:rule.section,displayLabel:rule.label??field.sourceLabel,meaning:rule.meaning,caution:rule.caution}];
  });
  if(view==='operational/Overview'){
    const featured=example.key==='sck23'
      ? new Set(['product-generation','sensing-component','supported-measurement','physical-assembly'])
      : example.key==='trss'
        ? new Set(['selected-detector-type','estimated-capacity-remaining'])
        : example.key==='core2'
          ? new Set(['reported-transducer-label'])
          : new Set(['reported-battery-voltage','source-mode']);
    return mapped.filter(f=>featured.has(f.term));
  }
  return mapped.filter(f=>f.view===view);
}
export function unmappedFields(example:SourceCase):SourceField[] {
  return example.fields.filter(f=>!candidateRules[f.term]&&!termsRetainedAsProvenance.has(f.term));
}
