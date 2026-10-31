import { node, renderResourceDetailsTemplate } from './resource-details-template';
import { renderResourceMap } from './resource-details-map';
import './resource-details-profile-test.css';

const base = 'https://129-80-248-53.sslip.io/csapi-pygeoapi';

interface SystemRecord {
  id: string;
  type?: string;
  name?: string;
  label?: string;
  description?: string;
  definition?: string;
  uniqueId?: string;
  typeOf?: { href?: string; uid?: string; title?: string; type?: string };
  identifiers?: Array<{ definition?: string; label?: string; value?: string }>;
  contacts?: Array<{ role?: string; organisationName?: string; individualName?: string }>;
  validTime?: [string | null, string | null] | string[];
  position?: { type?: string; coordinates?: number[] };
  [key: string]: unknown;
}
interface Collection<T> { type?: string; features?: T[]; items?: T[]; links?: unknown[]; }
interface DataStream {
  id?: string; name?: string; description?: string; live?: boolean; resultType?: string;
  observedProperties?: Array<{ definition?: string; label?: string; description?: string }>;
  formats?: string[]; schema?: unknown; phenomenonTime?: unknown; resultTime?: unknown;
  [key: string]: unknown;
}
interface Observation { id?: string; phenomenonTime?: unknown; resultTime?: unknown; result?: unknown; [key:string]:unknown; }
interface LiveState {
  systems: SystemRecord[];
  selected?: SystemRecord;
  datastreams: DataStream[];
  deployments: unknown[];
  subsystems: SystemRecord[];
  observations: Array<{ stream: DataStream; rows: Observation[] }>;
  loading: boolean;
  error?: string;
  partial?: string;
  relatedLoading?: boolean;
  fetchedAt?: string;
  raw: Record<string, unknown>;
}

function jsonUrl(path: string): string {
  return base + path + (path.includes('?') ? '&' : '?') + 'f=application/json';
}
async function getJson<T>(path: string): Promise<T> {
  const response = await fetch(jsonUrl(path), { headers: { Accept: 'application/json, application/sml+json' }, cache: 'no-store' });
  if (!response.ok) throw new Error(path + ' returned HTTP ' + response.status);
  return await response.json() as T;
}
function features<T>(collection: Collection<T>): T[] { return collection.features ?? collection.items ?? []; }
function empty(content: HTMLElement, text: string): void {
  const block=node('div','rdp-no-data'); block.append(node('p',undefined,text)); content.append(block);
}
function field(list: HTMLElement, label: string, value: string, note?: string): void {
  const row=node('div','rdp-field'); const dd=node('dd'); dd.append(node('span',undefined,value));
  if(note) dd.append(node('small','rdp-qualifier',note));
  row.append(node('dt',undefined,label),dd); list.append(row);
}
function link(parent: HTMLElement, label: string, href: string): void {
  const a=node('a',undefined,label); a.href=href; a.target='_blank'; a.rel='noopener noreferrer'; parent.append(a);
}
function renderOverview(content:HTMLElement,state:LiveState):void{
  const s=node('section','rdp-section'); s.append(node('h3',undefined,'Live CSAPI retrieval summary'));
  const dl=node('dl','rdp-field-grid');
  field(dl,'Selected System',state.selected?.label ?? state.selected?.name ?? state.selected?.id ?? 'None');
  field(dl,'Systems currently returned',String(state.systems.length));
  field(dl,'DataStreams currently returned',String(state.datastreams.length));
  field(dl,'Deployments currently returned',String(state.deployments.length));
  field(dl,'Subsystems currently returned',String(state.subsystems.length));
  field(dl,'Observations currently returned',String(state.observations.reduce((n,x)=>n+x.rows.length,0)));
  field(dl,'Retrieved at',state.fetchedAt ?? 'Not yet retrieved','This is the client retrieval time, not sensor phenomenon time.');
  s.append(dl,node('p','rdp-footnote','Every value on this page is reconstructed from HTTP GET responses to the live Oracle-hosted 52°North/pygeoapi CSAPI service. The server may contain test or historical resources; live retrieval does not by itself mean live sensor telemetry.'));
  if(state.relatedLoading) s.append(node('p','rdp-footnote','Related resources are still loading.'));
  if(state.partial) s.append(node('p','rdp-footnote','Some related resources could not be loaded: '+state.partial));
  content.append(s);
}
function renderMap(content:HTMLElement,state:LiveState):void{
  const p=state.selected?.position;
  if(!p?.coordinates?.length){empty(content,'The selected System does not currently return a position.');return;}
  const s=node('section','rdp-section'); s.append(node('h3',undefined,'Reported position'));
  const dl=node('dl','rdp-field-grid');
  field(dl,'Geometry',p.type ?? 'Unknown');
  field(dl,'Coordinates',p.coordinates.join(', '),'Displayed exactly in the order returned by the server; this page does not reinterpret axis order.');
  s.append(dl); content.append(s);
}
function renderEquipment(content:HTMLElement,state:LiveState):void{
  const sys=state.selected; if(!sys){empty(content,'No System selected.');return;}
  const s=node('section','rdp-section'); s.append(node('h3',undefined,'Selected System'));
  const dl=node('dl','rdp-field-grid');
  field(dl,'Label',sys.label ?? sys.name ?? 'Not supplied');
  field(dl,'Resource ID',sys.id);
  field(dl,'Unique identifier',sys.uniqueId ?? 'Not supplied');
  field(dl,'Sensor/System definition',sys.definition ?? 'Not supplied');
  field(dl,'Description',sys.description ?? 'Not supplied');
  if(sys.validTime?.length) field(dl,'Valid time',sys.validTime.map(v=>v ?? 'open').join(' → '));
  s.append(dl); content.append(s);
  if(sys.typeOf){
    const m=node('section','rdp-section'); m.append(node('h3',undefined,'Model / system kind link'));
    const md=node('dl','rdp-field-grid');
    field(md,'Title',sys.typeOf.title ?? 'Not supplied');
    field(md,'UID',sys.typeOf.uid ?? 'Not supplied');
    if(sys.typeOf.href) { const row=node('div','rdp-field'); row.append(node('dt',undefined,'Procedure link')); const dd=node('dd'); link(dd,sys.typeOf.href,sys.typeOf.href); row.append(dd); md.append(row); }
    m.append(md); content.append(m);
  }
  if(sys.identifiers?.length){
    const ids=node('section','rdp-section'); ids.append(node('h3',undefined,'Identifiers')); const idl=node('dl','rdp-field-grid');
    for(const id of sys.identifiers) field(idl,id.label ?? 'Identifier',id.value ?? 'Not supplied',id.definition);
    ids.append(idl); content.append(ids);
  }
  if(state.subsystems.length){
    const sub=node('section','rdp-section'); sub.append(node('h3',undefined,'Subsystems returned by server')); const sdl=node('dl','rdp-field-grid');
    for(const item of state.subsystems) field(sdl,item.label ?? item.name ?? item.id,item.uniqueId ?? item.id);
    sub.append(sdl); content.append(sub);
  }
  if(state.deployments.length){
    const dep=node('section','rdp-section'); dep.append(node('h3',undefined,'Deployments returned by server'),node('pre','raw-content',JSON.stringify(state.deployments,null,2))); content.append(dep);
  }
}
function renderCommunications(content:HTMLElement,state:LiveState):void{
  if(!state.datastreams.length){empty(content,'The selected System currently returns no DataStreams.');return;}
  const s=node('section','rdp-section'); s.append(node('h3',undefined,'Outward reporting resources'));
  s.append(node('p','rdp-footnote','Shown here only as reporting/interface context. A CSAPI DataStream is not automatically a physical communications channel.'));
  const dl=node('dl','rdp-field-grid');
  for(const ds of state.datastreams){
    const props=(ds.observedProperties??[]).map(p=>p.label ?? p.definition ?? 'property').join(', ') || 'No observed property supplied';
    field(dl,ds.name ?? ds.id ?? 'DataStream',props,'resultType: '+(ds.resultType ?? 'unknown')+' · live flag: '+String(ds.live ?? 'not supplied'));
  }
  s.append(dl); content.append(s);
}
function renderCondition(content:HTMLElement):void{
  empty(content,'This live page does not infer equipment condition from System/DataStream metadata. A condition view will remain empty until the server supplies an attributable condition/status fact selected by the Profile.');
}
function renderActivityTable(content:HTMLElement,state:LiveState):void{
  const streams=state.observations.filter(x=>x.rows.length);
  if(!streams.length){empty(content,'The live server currently returned no Observations for the selected System’s retrieved DataStreams.');return;}
  for(const group of streams){
    const s=node('section','rdp-section'); s.append(node('h3',undefined,group.stream.name ?? group.stream.id ?? 'DataStream'));
    const dl=node('dl','rdp-field-grid');
    group.rows.forEach((obs,index)=>field(dl,'Observation '+String(index+1),JSON.stringify(obs.result ?? 'No result'),'phenomenonTime: '+JSON.stringify(obs.phenomenonTime ?? null)));
    s.append(dl); content.append(s);
  }
}
function renderActivityCharts(content:HTMLElement,state:LiveState):void{
  const count=state.observations.reduce((n,x)=>n+x.rows.length,0);
  if(count<2){empty(content,'Fewer than two live-retrieved Observation records are available, so this page does not draw a trend chart.');return;}
  const s=node('section','rdp-section'); s.append(node('h3',undefined,'Observation series'));
  s.append(node('p',undefined,'Multiple observation records were retrieved. Chart rendering is intentionally deferred until result schemas and units are validated per DataStream.')); content.append(s);
}
function renderCommands(content:HTMLElement):void{ empty(content,'This read-only live page does not issue commands and does not infer command capability from unrelated resources.'); }
function renderRecord(content:HTMLElement,state:LiveState):void{
  const s=node('section','rdp-section'); s.append(node('h3',undefined,'Live server responses'));
  for(const [key,value] of Object.entries(state.raw)){
    const d=node('details','capture'); d.append(node('summary',undefined,key),node('pre','raw-content',JSON.stringify(value,null,2))); s.append(d);
  }
  content.append(s);
}
function renderConfiguration(content:HTMLElement):void{ empty(content,'No attributable current configuration/readback is inferred on this page.'); }
function renderSources(content:HTMLElement,state:LiveState):void{
  const s=node('section','rdp-section'); s.append(node('h3',undefined,'Live sources'));
  const ul=node('ul','rdp-sources-list');
  for(const [label,url] of [
    ['52°North / pygeoapi service root',base+'/'],
    ['Systems collection',jsonUrl('/systems')],
    ['Selected System',state.selected?jsonUrl('/systems/'+encodeURIComponent(state.selected.id)):jsonUrl('/systems')],
    ['Selected System DataStreams',state.selected?jsonUrl('/systems/'+encodeURIComponent(state.selected.id)+'/datastreams'):jsonUrl('/systems')],
  ]){ const li=node('li'); link(li,label,url); ul.append(li); }
  s.append(ul,node('p','rdp-footnote','Requests are browser-side, read-only GETs. Refreshing this page requests the service again.')); content.append(s);
}

export function renderResourceDetailsLiveCsapi(container:HTMLElement, mapPage = false):void{
  const state:LiveState={systems:[],datastreams:[],deployments:[],subsystems:[],observations:[],loading:true,raw:{}};
  let selectedId='';
  let loadVersion=0;
  let disposeMap: (() => void) | undefined;
  renderResourceDetailsTemplate(container,{
    pageTitle:mapPage ? 'Resource Details · live resource map' : 'Resource Details · live 52°North CSAPI retrieval',
    pageIntro:mapPage ? 'Explore a selected live-server System’s reported location in the Resource Details Map view.' : 'A separate read-only page that queries the deployed Oracle-hosted 52°North/pygeoapi Connected Systems API instead of local fixtures.',
    renderBlankContent({categoryId,view,content}){
      disposeMap?.(); disposeMap = undefined;
      if(state.loading){empty(content,'Loading live CSAPI responses…');return true;}
      if(state.error){empty(content,'Live retrieval failed: '+state.error);return true;}
      const key=categoryId+'/'+view;
      if(key==='operational/Overview')renderOverview(content,state);
      else if(key==='operational/Map') {
        if(mapPage) disposeMap=renderResourceMap(content,state.selected?.position);
        else renderMap(content,state);
      }
      else if(key==='operational/Equipment')renderEquipment(content,state);
      else if(key==='operational/Communications')renderCommunications(content,state);
      else if(key==='operational/Condition')renderCondition(content);
      else if(key==='activity/Table')renderActivityTable(content,state);
      else if(key==='activity/Charts')renderActivityCharts(content,state);
      else if(key.startsWith('commands/'))renderCommands(content);
      else if(key==='management/Record')renderRecord(content,state);
      else if(key==='management/Configuration')renderConfiguration(content);
      else if(key==='management/Sources')renderSources(content,state);
      else empty(content,'No live placement is defined for this view.');
      return true;
    },
    sourceSummary:'Live-server scope and limits',
    sourceDescription:'This page performs live read-only browser requests to the Oracle-hosted 52°North/pygeoapi CSAPI service. It does not write resources, poll a physical sensor directly, or treat the server’s stored resources as current physical-device state unless the returned data explicitly supports that meaning.',
    designRecord:'Research/DIM_Profile_V2/Candidate_Specification/Resource_Details_Placement_Matrix.md',
  });
  container.classList.add('resource-profile-prototype');
  const toolbar=container.querySelector<HTMLElement>('.rd-preview-toolbar');
  const stage=container.querySelector<HTMLElement>('.rd-canvas-stage');
  const frame=stage?.querySelector<HTMLElement>('.rd-module');
  if(!toolbar||!frame)throw new Error('Resource Details template was not mounted');

  const controls=node('section','rdp-controls');
  const label=node('label',undefined,'Live System'); const select=node('select'); select.id='live-system-select'; label.htmlFor=select.id;
  const pick=node('div','rdp-picker'); pick.append(label,select);
  const refresh=node('button','rdp-mode','Refresh live server'); refresh.type='button';
  const status=node('p','rdp-count'); status.setAttribute('aria-live','polite');
  controls.append(pick,refresh,status); toolbar.before(controls);

  const title=frame.querySelector<HTMLElement>('.rd-resource-name');
  const identity=frame.querySelectorAll<HTMLElement>('.rd-identity-fields dd');
  const footer=frame.querySelector<HTMLElement>('.rd-module-footer span');
  const refreshTemplate=frame.querySelector<HTMLButtonElement>('.rd-refresh');
  if(refreshTemplate) refreshTemplate.hidden=true;

  const rerender=(refreshContent=true):void=>{
    if(title)title.textContent=state.selected?.label ?? state.selected?.name ?? 'Live CSAPI';
    if(identity.length>=3){
      identity[0].textContent=state.selected?.type ?? 'System';
      identity[1].textContent=state.selected?.id ?? 'Not loaded';
      identity[2].textContent='52°North / pygeoapi live GET';
    }
    if(footer)footer.textContent=state.loading?'Live retrieval in progress':'Live read-only CSAPI retrieval';
    status.textContent=state.loading?'Loading…':state.error?state.error:(state.fetchedAt?'Retrieved '+state.fetchedAt+(state.relatedLoading?' · Loading related resources':state.partial?' · Some related resources failed to load':''):'Not loaded');
    if(refreshContent){const active=frame.querySelector<HTMLButtonElement>('.rd-view-tabs .rd-tab[aria-selected="true"]'); active?.click();}
  };

  const load=async(id?:string):Promise<void>=>{
    const version=++loadVersion;
    state.loading=true; state.error=undefined; state.partial=undefined;state.relatedLoading=false;
    if(mapPage){state.selected=undefined;state.datastreams=[];state.deployments=[];state.subsystems=[];state.observations=[];state.raw={};state.fetchedAt=undefined;}
    rerender();
    try{
      const systemsDoc=await getJson<Collection<SystemRecord>>('/systems');
      if(version!==loadVersion)return;
      state.raw.systems=systemsDoc; state.systems=features(systemsDoc);
      const chosen=id && state.systems.some(s=>s.id===id) ? id : (selectedId && state.systems.some(s=>s.id===selectedId)?selectedId:state.systems[0]?.id);
      if(!chosen)throw new Error('The live Systems collection is empty.');
      selectedId=chosen;
      const selected=await getJson<SystemRecord>('/systems/'+encodeURIComponent(chosen));
      if(version!==loadVersion)return;
      state.selected=selected;
      state.raw.selectedSystem=state.selected;
      if(mapPage){
        select.replaceChildren();
        for(const sys of state.systems){const option=node('option',undefined,sys.label ?? sys.name ?? sys.id);option.value=sys.id;select.append(option);}
        select.value=selectedId;
        state.fetchedAt=new Date().toISOString();state.loading=false;state.relatedLoading=true;rerender();
      }
      const failures:string[]=[];
      const related = async <T>(path:string):Promise<Collection<T>> => {
        try{return await getJson<Collection<T>>(path);}
        catch(error){if(!mapPage)throw error;failures.push(path+': '+(error instanceof Error?error.message:String(error)));return {items:[]};}
      };
      const [dsDoc,depDoc,subDoc]=await Promise.all([
        related<DataStream>('/systems/'+encodeURIComponent(chosen)+'/datastreams'),
        related<unknown>('/systems/'+encodeURIComponent(chosen)+'/deployments'),
        related<SystemRecord>('/systems/'+encodeURIComponent(chosen)+'/subsystems'),
      ]);
      if(version!==loadVersion)return;
      state.raw.datastreams=dsDoc; state.raw.deployments=depDoc; state.raw.subsystems=subDoc;
      state.datastreams=features(dsDoc); state.deployments=features(depDoc); state.subsystems=features(subDoc);
      const observations=await Promise.all(state.datastreams.slice(0,10).filter(ds=>ds.id).map(async ds=>{
        const doc=await related<Observation>('/datastreams/'+encodeURIComponent(ds.id!)+'/observations');
        if(version===loadVersion)state.raw['observations:'+ds.id]=doc; return {stream:ds,rows:features(doc)};
      }));
      if(version!==loadVersion)return;
      state.observations=observations;
      state.partial=failures.length?failures.join('; '):undefined;
      state.fetchedAt=new Date().toISOString();
      select.replaceChildren();
      for(const sys of state.systems){
        const option=node('option',undefined,sys.label ?? sys.name ?? sys.id); option.value=sys.id; select.append(option);
      }
      select.value=selectedId;
    }catch(error){if(version===loadVersion)state.error=error instanceof Error?error.message:String(error);}
    finally{if(version===loadVersion){state.loading=false;state.relatedLoading=false;rerender(!(mapPage && !state.error && frame.querySelector('.rd-map-widget')));}}
  };
  select.addEventListener('change',()=>void load(select.value));
  refresh.addEventListener('click',()=>void load(selectedId));
  void load();
}
