import { node, renderResourceDetailsTemplate } from './resource-details-template';
import { renderResourceMap } from './resource-details-map';
import './resource-details-profile-test.css';

const base='https://129-80-248-53.sslip.io/csapi-pygeoapi';
const cases=[
  {system:'b171318e-8efe-550d-be99-bec5364984c0',uid:'urn:merlin:v2:bennetts:ee181:probe4',serial:'222016000109CE',stream:'351545ac-6ad6-418e-9688-7bba0329bb38',expectedTime:'2024-04-15T17:00:00Z',expectedValue:29.1},
  {system:'378df868-d52f-4847-b783-865ec0c1df5e',uid:'urn:merlin:v2:bennetts:ee181:probe3',serial:'21281600077814',stream:'d97c6dcc-d09d-4c70-aae9-a1b63c29e4b9',expectedTime:'2024-04-18T17:00:00Z',expectedValue:27.3},
] as const;

interface SystemRec{ id:string;label?:string;description?:string;uniqueId?:string;definition?:string;typeOf?:{href?:string;uid?:string;title?:string};identifiers?:Array<{label?:string;value?:string;definition?:string}>;position?:unknown;[k:string]:unknown }
interface Stream{ id?:string;name?:string;description?:string;observedProperties?:Array<{label?:string;definition?:string}>;live?:boolean;schema?:unknown;[k:string]:unknown }
interface Obs{ id?:string;phenomenonTime?:unknown;resultTime?:unknown;result?:unknown;[k:string]:unknown }
interface Loaded{caseDef:typeof cases[number];system:SystemRec;stream:Stream;observations:Obs[]}
interface State{loading:boolean;error?:string;loaded:Loaded[];fetchedAt?:string;raw:Record<string,unknown>}

const url=(path:string)=>base+path+(path.includes('?')?'&':'?')+'f=application/json';
async function get<T>(path:string):Promise<T>{const r=await fetch(url(path),{cache:'no-store',headers:{Accept:'application/json, application/sml+json'}});if(!r.ok)throw new Error(path+' HTTP '+r.status);return await r.json() as T;}
const rows=(d:any):any[]=>d?.features??d?.items??[];
function field(dl:HTMLElement,label:string,value:string,note?:string):void{const row=node('div','rdp-field');const dd=node('dd');dd.append(node('span',undefined,value));if(note)dd.append(node('small','rdp-qualifier',note));row.append(node('dt',undefined,label),dd);dl.append(row);}
function empty(content:HTMLElement,text:string):void{const d=node('div','rdp-no-data');d.append(node('p',undefined,text));content.append(d);}
function overview(content:HTMLElement,state:State):void{
 const s=node('section','rdp-section');s.append(node('h3',undefined,'Live Bennett’s Point V2 round trip'));const dl=node('dl','rdp-field-grid');
 field(dl,'Physical probes',String(state.loaded.length));
 field(dl,'Shared model','Campbell Scientific EE181');
 field(dl,'Historical observations',String(state.loaded.reduce((n,x)=>n+x.observations.length,0)));
 field(dl,'Retrieved at',state.fetchedAt??'Not loaded','Glaux retrieval time, not observation time.');
 s.append(dl,node('p','rdp-footnote','This page is reconstructed from live GET responses to the Oracle-hosted 52°North/pygeoapi server. The measurements are historical; the retrieval is live.'));content.append(s);
}
function equipment(content:HTMLElement,state:State):void{
 const model=node('section','rdp-section');model.append(node('h3',undefined,'Shared product model'));const mdl=node('dl','rdp-field-grid');
 field(mdl,'Manufacturer / model','Campbell Scientific EE181');
 field(mdl,'Model description','urn:merlin:v2:datasheet:campbell:ee181','Both live System records link to the same project-authored model description.');model.append(mdl);content.append(model);
 const units=node('section','rdp-section');units.append(node('h3',undefined,'Individual physical Systems from live CSAPI'));const dl=node('dl','rdp-field-grid');
 for(const x of state.loaded){const serial=x.system.identifiers?.find(i=>i.label==='Serial Number')?.value??x.caseDef.serial;field(dl,x.system.label??x.system.id,serial,(x.system.uniqueId??'No UID')+' · server id '+x.system.id);}
 units.append(dl,node('p','rdp-footnote','Same model does not collapse the two physical probes into one System.'));content.append(units);
}
function communications(content:HTMLElement,state:State):void{
 const s=node('section','rdp-section');s.append(node('h3',undefined,'Live-retrieved DataStreams'),node('p','rdp-footnote','These are reporting resources, not automatically physical communication channels.'));const dl=node('dl','rdp-field-grid');
 for(const x of state.loaded){field(dl,x.stream.name??x.stream.id??'DataStream',(x.stream.observedProperties??[]).map(p=>p.label??p.definition??'property').join(', '),'live flag: '+String(x.stream.live??'not supplied'));}
 s.append(dl);content.append(s);
}
function activity(content:HTMLElement,state:State):void{
 const s=node('section','pub-measures');s.append(node('h3',undefined,'Historical observations retrieved live from CSAPI'));const list=node('div','pub-list');
 for(const x of state.loaded){for(const o of x.observations){const g=node('section','pub-group');g.append(node('h4',undefined,String(o.resultTime??o.phenomenonTime??'Time not supplied')));const dl=node('dl');
 for(const [l,v] of [['Air temperature',String(o.result)+' °C'],['Sensing System',x.system.label??x.system.id],['Serial number',x.caseDef.serial],['Observation ID',o.id??'Not supplied']]){const r=node('div','pub-row');r.append(node('dt',undefined,l),node('dd',undefined,v));dl.append(r);}g.append(dl);list.append(g);}}
 s.append(list);content.append(s);
}
function record(content:HTMLElement,state:State):void{const s=node('section','rdp-section');s.append(node('h3',undefined,'Live server responses'));for(const [k,v] of Object.entries(state.raw)){const d=node('details','capture');d.append(node('summary',undefined,k),node('pre','raw-content',JSON.stringify(v,null,2)));s.append(d);}content.append(s);}
function sources(content:HTMLElement):void{const s=node('section','rdp-section');s.append(node('h3',undefined,'Evidence and live endpoints'));const ul=node('ul','rdp-sources-list');for(const [label,href] of [
 ['52°North / pygeoapi service',base+'/'],
 ['Probe 4 live System',url('/systems/'+cases[0].system)],
 ['Probe 3 live System',url('/systems/'+cases[1].system)],
 ['Candidate Profile — Bennett’s Point attribution','https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Candidate_Specification/CSAPI_Profile.md#which-probe-measured-the-air-temperature'],
 ['ACE Basin operator metadata','https://cdmo.baruch.sc.edu/waf/YearlyFiles/ACE%20Basin/meteorological/metadata/acemet01-12.24m.pdf'],
 ]){const li=node('li');const a=node('a',undefined,label);a.href=href;a.target='_blank';a.rel='noopener noreferrer';li.append(a);ul.append(li);}s.append(ul);content.append(s);}

/** Reuse Codex's existing map renderer for one identified physical System at a time.
 * A station label or past observation is never used to manufacture coordinates.
 */
function renderBennettMap(content:HTMLElement,state:State,chosenId:string|undefined,onSelect:(id:string)=>void):()=>void{
 const section=node('section','rdp-section');
 section.append(node('h3',undefined,'Reported location of an identified probe'));
 section.append(node('p','rdp-footnote','Choose a physical EE181 System. This map uses only that System’s returned position; a station name, deployment history, or observation timestamp does not establish probe coordinates.'));
 const selectorLabel=node('label',undefined,'Physical System');
 const selector=node('select');selector.id='rd-bennett-map-system';selectorLabel.htmlFor=selector.id;
 for(const item of state.loaded){const option=node('option',undefined,item.system.label??item.system.id);option.value=item.system.id;selector.append(option);}
 selector.value=state.loaded.some(item=>item.system.id===chosenId)?chosenId!:state.loaded[0]?.system.id??'';
 const host=node('div','rd-bennett-map-host');
 const selection=node('div','rdp-picker');selection.append(selectorLabel,selector);
 section.append(selection,host);content.append(section);
 let cleanup:()=>void=()=>{};
 const draw=()=>{
   cleanup();
   host.replaceChildren();
   const selected=state.loaded.find(item=>item.system.id===selector.value);
   if(!selected){empty(host,'No physical System is selected.');cleanup=()=>{};return;}
   onSelect(selected.system.id);
   cleanup=renderResourceMap(host,selected.system.position);
 };
 selector.addEventListener('change',draw);
 draw();
 return ()=>{selector.removeEventListener('change',draw);cleanup();};
}

export function renderResourceDetailsLiveBennett(container:HTMLElement):void{
 const state:State={loading:true,loaded:[],raw:{}};
 let disposeMap: (()=>void)|undefined;
 let selectedMapSystemId: string|undefined;
 renderResourceDetailsTemplate(container,{pageTitle:'Bennett’s Point · live CSAPI V2 case',pageIntro:'The controlled two-probe Bennett’s Point case read back from the live Oracle-hosted 52°North/pygeoapi server.',renderBlankContent({categoryId,view,content}){
   disposeMap?.(); disposeMap=undefined;
   if(state.loading){empty(content,'Loading controlled case from live CSAPI server…');return true;} if(state.error){empty(content,'Live retrieval failed: '+state.error);return true;}
   const k=categoryId+'/'+view;
   if(k==='operational/Overview')overview(content,state); else if(k==='operational/Equipment')equipment(content,state); else if(k==='operational/Communications')communications(content,state);
   else if(k==='operational/Map')disposeMap=renderBennettMap(content,state,selectedMapSystemId,(id)=>{selectedMapSystemId=id;}); else if(k==='operational/Condition')empty(content,'No current equipment-condition assertion is published in this case.');
   else if(k==='activity/Table')activity(content,state); else if(k==='activity/Charts')empty(content,'Only two bounded historical observations are loaded; this page does not infer a trend.');
   else if(k.startsWith('commands/'))empty(content,'No command/control resources are part of this controlled case.'); else if(k==='management/Record')record(content,state);
   else if(k==='management/Configuration')empty(content,'No current configuration/readback is published in this case.'); else if(k==='management/Sources')sources(content); else empty(content,'No content for this view.');
   return true;
 },sourceSummary:'What is live here?',sourceDescription:'Glaux performs browser GETs against the deployed 52°North/pygeoapi CSAPI service on each load. The two temperature measurements are historical April 2024 observations that were deliberately loaded as a controlled V2 experiment; they are not current sensor telemetry.',designRecord:'Design/BENNETT_LIVE_MAP_INTEGRATION.md'});
 container.classList.add('resource-profile-prototype');
 const stage=container.querySelector<HTMLElement>('.rd-canvas-stage');const frame=stage?.querySelector<HTMLElement>('.rd-module');if(!frame)throw new Error('Resource Details template missing');
 const title=frame.querySelector<HTMLElement>('.rd-resource-name');if(title)title.textContent="Bennett's Point · live V2";
 const ids=frame.querySelectorAll<HTMLElement>('.rd-identity-fields dd');if(ids.length>=3){ids[0].textContent='Controlled live CSAPI case';ids[1].textContent='2 EE181 Systems';ids[2].textContent='52°North / pygeoapi live GET';}
 const footer=frame.querySelector<HTMLElement>('.rd-module-footer span');if(footer)footer.textContent='Live CSAPI retrieval · historical observations';
 const rerender=()=>{const active=frame.querySelector<HTMLButtonElement>('.rd-view-tabs .rd-tab[aria-selected="true"]');active?.click();};
 void (async()=>{try{for(const c of cases){const system=await get<SystemRec>('/systems/'+c.system);const stream=await get<Stream>('/datastreams/'+c.stream);const obsDoc=await get<any>('/datastreams/'+c.stream+'/observations');const observations=rows(obsDoc) as Obs[];state.loaded.push({caseDef:c,system,stream,observations});state.raw['system:'+c.system]=system;state.raw['datastream:'+c.stream]=stream;state.raw['observations:'+c.stream]=obsDoc;}state.fetchedAt=new Date().toISOString();}catch(e){state.error=e instanceof Error?e.message:String(e);}finally{state.loading=false;rerender();}})();
}
