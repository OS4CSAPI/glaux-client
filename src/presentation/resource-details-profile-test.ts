import { node, renderResourceDetailsTemplate } from './resource-details-template';
import {
  smartCitizenDesign, inputFixtures, candidateRules, termsRetainedAsProvenance,
  mappedFieldCount, mappingsForView, unmappedFields, projectSourceFixture,
  type SourceCase, type SourceField, type MappedField, type ViewKey,
} from '../profile/resource-details-proof';
import { caseKey, measures } from '../profile/published-measurements';
import { renderPublished } from './published-measurements';
import { attributionCaseKey, attributionCase } from '../profile/bennetts-point';
import { renderBennettsPoint } from './bennetts-point';
import { buildPacketPresentation, type PacketPresentation } from '../profile/source-packet-presentation';
import { loadNativeSourceProfile, type NativeSourceLoad } from '../profile/native-source-profile';
import { renderSourcePacketDetails } from './source-packet-details';
import './resource-details-profile-test.css';

type PresentationMode = 'profile' | 'generic';
// Only selector/file locations are case-specific. ALL interpretations share one
// Step 33 reader and one Step 38 presentation rule set. These are local research
// packets, NOT native CSAPI resources or verified live physical Systems.
const packetCases = [
  { key: 'step38-dragino', label: 'Dragino S31-LB — manufacturer reference packet', path: '/fixtures/source-packets/dragino.reference.packet.json' },
  { key: 'step38-airgradient', label: 'AirGradient Open Air Max — reference packet', path: '/fixtures/source-packets/airgradient.reference.packet.json' },
  // 41R-03 expanded source-coverage selections; still local research JSON, not native CSAPI/Profile.
  { key: 'step41r03-dragino', label: 'Dragino S31-LB — expanded documented design coverage', path: '/fixtures/source-packets/dragino.coverage.packet.json' },
  { key: 'step41r03-airgradient', label: 'AirGradient Open Air Max — expanded documented design coverage', path: '/fixtures/source-packets/airgradient.coverage.packet.json' },
  // 41R-04 source-selected field-level Campbell reference and 2024 Bennett station context;
  // both remain separate LOCAL project packets, not a native CSAPI Profile response.
  { key: 'step41r04-campbell', label: 'Campbell CR1000X + first-gen ClimaVue 50 — full selected response and Status fields', path: '/fixtures/source-packets/campbell.coverage.packet.json' },
  { key: 'step41r04-bennett', label: "Bennett's Point — original station/site/maintenance coverage", path: '/fixtures/source-packets/bennetts-point.coverage.packet.json' },
  { key: 'step38-campbell', label: 'Campbell CR1000X + ClimaVue 50 — reference packet', path: '/fixtures/source-packets/campbell.reference.packet.json' },
  { key: 'step38-bennett', label: "Bennett's Point — historical source packet", path: '/fixtures/source-packets/bennetts-point.historical.packet.json' },
] as const;
type PacketCase = typeof packetCases[number];
const options:ReadonlyArray<{key:string;label:string}> = [
  ...packetCases,
  { key:'native-csapi',label:'Native CSAPI resource URL — discover linked evidence' },
  { key:'sck23',label:'Smart Citizen Kit 2.3 — product design' },
  { key:caseKey,label:'Dragino + Campbell — published measurement examples' },
  { key:attributionCaseKey,label:"Bennett's Point — real probe swap and measurements" },
  { key:'trss',label:'TRSS ETU-II — synthetic configuration' },
  { key:'core2',label:'OmniSense Core2 — synthetic equipment' },
  { key:'core5',label:'OmniSense Core5ADS — synthetic condition' },
];

function addLink(parent:HTMLElement,label:string,url:string):void{
  const a=node('a',undefined,label);a.href=url;a.target='_blank';a.rel='noopener noreferrer';parent.append(a);
}
function appendLabelValue(parent:HTMLElement,label:string,value:string,qualifier?:string,sourceUrl?:string):void{
  const row=node('div','rdp-field');
  const name=node('dt',undefined,label);
  const val=node('dd');
  val.append(node('span',undefined,value));
  if(qualifier)val.append(node('small','rdp-qualifier',qualifier));
  if(sourceUrl)addLink(val,'Source',sourceUrl);
  row.append(name,val);parent.append(row);
}
function normalizedText(f:MappedField):string{return f.value+(f.unit?' '+f.unit:'');}
function renderCandidate(content:HTMLElement,example:SourceCase,view:ViewKey):void{
  if(view==='management/Sources'){renderSources(content,example);return;}
  const title= example.evidence==='manufacturer-design'
    ? 'Documented product capability — no individual Kit loaded'
    : 'Historical synthetic replay — not a live System';
  const top=node('div','rdp-standing',title);
  content.append(top);
  if(view.startsWith('activity/')||view.startsWith('commands/')){
    const message=view.startsWith('activity/')
      ? 'No independently verified Observations, DataStreams or event records are available for this case. Do not turn supported outputs, stored source labels or fixture values into history.'
      : 'No executable ControlStream or validated device command is supplied in this source case. This prototype cannot send device commands.';
    empty(content,message);return;
  }
  if(view==='operational/Map'){
    empty(content,'No trustworthy physical-unit position was established for this source case. A model name, software record or synthetic fixture is not a deployed map location.');return;
  }
  const fields=mappingsForView(example,view);
  if(fields.length===0){
    empty(content,view==='operational/Condition'
      ? 'No verified actual condition or appropriate reported condition is supplied for this source description.'
      : 'No source-grounded information has been mapped to this section. The underlying source fields remain available in Management → Sources.');
    return;
  }
  const sections=new Map<string,Map<string,MappedField[]>>();
  for(const f of fields){
    if(!sections.has(f.section))sections.set(f.section,new Map());
    const groups=sections.get(f.section)!;
    if(!groups.has(f.groupId))groups.set(f.groupId,[]);
    groups.get(f.groupId)!.push(f);
  }
  for(const [sectionName,groups] of sections){
    const section=node('section','rdp-section');
    section.append(node('h3',undefined,sectionName));
    for(const [groupId,items] of groups){
      const group=node('div','rdp-group');
      group.dataset.groupId=groupId;
      const showGroup=items.length>1||items[0].groupLabel!==sectionName;
      if(showGroup)group.append(node('h4',undefined,items[0].groupLabel));
      const grid=node('dl','rdp-field-grid');
      for(const item of items){
        appendLabelValue(grid,item.displayLabel,normalizedText(item),
          item.caution,item.sourceUrl);
      }
      group.append(grid);section.append(group);
    }
    content.append(section);
  }
  const lower=node('p','rdp-footnote','Manufacturer labels and individual hardware/processing roles are preserved where source evidence supports them. The mapping itself is a provisional client convention, not a published Profile.');
  content.append(lower);
}
function empty(content:HTMLElement,text:string):void{
  const p=node('div','rdp-no-data');p.append(node('p',undefined,text));content.append(p);
}
function renderGeneric(content:HTMLElement,example:SourceCase,view:ViewKey):void{
  content.append(node('p','rdp-standing','Illustrative generic inspector · raw fields remain visible'));
  if(view!=='operational/Overview'&&view!=='management/Sources'){
    empty(content,'A generic field listing does not know which source-defined values belong in this specific view. Switch to Candidate profile-aware rendering to see the same data grouped by declared meanings. This illustrates a UI limitation, not a CSAPI schema prohibition.');
    return;
  }
  const groupMap=new Map<string,SourceField[]>();
  for(const f of example.fields){
    if(!groupMap.has(f.groupId))groupMap.set(f.groupId,[]);
    groupMap.get(f.groupId)!.push(f);
  }
  for(const [id,rows] of groupMap){
    const section=node('section','rdp-section rdp-generic-section');
    const heading=node('h3',undefined,rows[0].groupLabel);
    const code=node('code','rdp-term',id);
    heading.append(code);section.append(heading);
    const grid=node('dl','rdp-field-grid');
    for(const f of rows)appendLabelValue(grid,f.sourceLabel,f.value+(f.unit?' '+f.unit:''),undefined,view==='management/Sources'?f.sourceUrl:undefined);
    section.append(grid);content.append(section);
  }
  content.append(node('p','rdp-footnote','This is an illustrative raw-property UI, not a claim that the OGC standards destroy these fields. The profile-aware view interprets declared terms and preserves unknowns in Sources.'));
}
function renderSources(content:HTMLElement,example:SourceCase):void{
  const section=node('section','rdp-section');
  section.append(node('h3',undefined,'Source identity and interpretation'));
  const info=node('dl','rdp-field-grid');
  appendLabelValue(info,'Evidence',example.evidence==='manufacturer-design'?'Pinned manufacturer product/design sources':'Synthetic SensorML-style test fixture');
  appendLabelValue(info,'Standing',example.resourceStanding);
  appendLabelValue(info,'Input fields',String(example.fields.length));
  appendLabelValue(info,'Recognized meaning terms',String(mappedFieldCount(example)));
  appendLabelValue(info,'Unknown mapped terms',String(unmappedFields(example).length),'Unknown fields are preserved; never silently assigned a meaning.');
  section.append(info);content.append(section);
  const links=node('section','rdp-section');links.append(node('h3',undefined,'Original or committed evidence'));
  const list=node('ul','rdp-sources-list');for(const src of example.links){const li=node('li');addLink(li,src.label,src.url);list.append(li);}links.append(list);content.append(links);
  const unmapped=unmappedFields(example);
  if(unmapped.length>0){
    const other=node('section','rdp-section');
    other.append(node('h3',undefined,'Uninterpreted source fields'));
    const dl=node('dl','rdp-field-grid');
    for(const f of unmapped)appendLabelValue(dl,f.sourceLabel,f.value+(f.unit?' '+f.unit:''),'Original group: '+f.groupLabel);
    other.append(dl);content.append(other);
  }
  if(example.evidence==='manufacturer-design'){
    const caveat=node('section','rdp-section');
    caveat.append(node('h3',undefined,'Identity boundary'),
      node('p',undefined,'SCK2.3 names a kind/model. A CSAPI System represents an individual. This demo correctly does not mint a System uniqueIdentifier, DataStream, Observation, deployed Configuration or hardware-to-database ID join.'));
    content.append(caveat);
  }
}
function insightText(example:SourceCase):string{
  if(example.key==='sck23')return 'The same SHT31 has temperature and humidity outputs; AS7331 has UV-A/B/C. A cabled PM module is in the normal enclosure. A vendor software Component is not physical hardware.';
  if(example.key==='trss')return 'Selected detector types retain their slot relationships. A 100% application estimate is labeled as an estimate, not a measured voltage or real-time readiness.';
  if(example.key==='core2')return 'Five reported transducer labels stay together as reported equipment information, without inventing individual part identities or an Observation.';
  return 'The 15.43 V DC source report is treated as voltage, not turned into percentage capacity; the unverified literal clock is not treated as current time.';
}
export function renderResourceDetailsProfileTest(container:HTMLElement):void {
  let selected:SourceCase=smartCitizenDesign;
  const params=new URLSearchParams(window.location.search);
  const requestedCase=params.get('case');
  const initialNativeUrl=params.get('native') ?? '';
  let nativeSelected=initialNativeUrl.length>0;
  let nativeResult:NativeSourceLoad | null=null;
  let packetCase: PacketCase | null = packetCases.find(p => p.key === requestedCase) ?? null;
  let packet: PacketPresentation | null = null;
  let packetLoadError: string | null = null;
  let published=requestedCase===caseKey;
  let attribution=requestedCase===attributionCaseKey;
  let mode:PresentationMode='profile';
  let pending=0;
  renderResourceDetailsTemplate(container,{
    pageTitle:'Profile-aware Resource Details · source-to-UI test',
    pageIntro:'Use one Resource Details frame for source-qualified local packets or a read-only native CSAPI Procedure/System URL with registered Profile/evidence links. No live telemetry or issued commands.',
    renderBlankContent({categoryId,view,content}){
      const key=(categoryId+'/'+view) as ViewKey;
      if(nativeSelected) {
        if(packet) renderSourcePacketDetails(content,packet,key,mode);
        else if(nativeResult?.kind==='raw') {
          const section=node('section','rdp-section');
          section.append(node('h3',undefined,'Native CSAPI feature — raw-only fallback'));
          section.append(node('p','rdp-footnote',nativeResult.reason ?? 'No supported source-evidence Profile discovered'));
          section.append(node('pre','raw-content',JSON.stringify(nativeResult.nativeRaw,null,2)));
          content.append(section);
        } else empty(content,packetLoadError ?? 'Loading native CSAPI GeoJSON and its discoverable project Profile evidence.');
      } else if(packetCase) {
        if(packet)renderSourcePacketDetails(content,packet,key,mode);
        else empty(content,packetLoadError ?? 'Loading the selected local research source packet. No live CSAPI request is being made.');
      }
      else if(attribution)renderBennettsPoint(content,key,mode==='generic');
      else if(published)renderPublished(content,key,mode==='generic');
      else if(mode==='profile')renderCandidate(content,selected,key);
      else renderGeneric(content,selected,key);
      return true;
    },
    sourceSummary:'What this tests — and what it does not',
    sourceDescription:'Local research packets stay available. For a user-supplied native CSAPI resource URL, the same shared interpreter reads only after registered Profile/evidence discovery and native-identity checks; producer issuer/authenticity and complete OGC requirements-class conformance remain unverified. No commands are sent.',
    designRecord:'Design/RESOURCE_DETAILS_PROFILE_TEST.md',
  });
  container.classList.add('resource-profile-prototype');
  const toolbar=container.querySelector<HTMLElement>('.rd-preview-toolbar');
  const stage=container.querySelector<HTMLElement>('.rd-canvas-stage');
  if(!toolbar||!stage)throw new Error('Resource Details template was not mounted');

  const controls=node('section','rdp-controls');
  const pickerLabel=node('label',undefined,'Source case');
  const picker=node('select');picker.id='rdp-case-select';pickerLabel.htmlFor=picker.id;
  for(const opt of options){const o=node('option',undefined,opt.label);o.value=opt.key;picker.append(o);}
  picker.value=nativeSelected ? 'native-csapi' : packetCase?.key ?? (attribution?attributionCaseKey:(published?caseKey:'sck23'));
  if(nativeSelected) packetCase=null;
  const pickerWrap=node('div','rdp-picker');pickerWrap.append(pickerLabel,picker);
  const modeGroup=node('div','rdp-mode-group');
  modeGroup.setAttribute('role','group');modeGroup.setAttribute('aria-label','Rendering mode');
  const genericBtn=node('button','rdp-mode','Generic CSAPI-style fields');genericBtn.type='button';
  const profileBtn=node('button','rdp-mode','Candidate profile-aware');profileBtn.type='button';
  modeGroup.append(genericBtn,profileBtn);
  const count=node('p','rdp-count');count.setAttribute('aria-live','polite');
  const nativeWrap=node('div','rdp-native');
  const nativeLabel=node('label',undefined,'Read-only native CSAPI Procedure/System URL');
  nativeLabel.htmlFor='rdp-native-url';
  const nativeInput=node('input');
  nativeInput.id='rdp-native-url';nativeInput.type='url';
  nativeInput.placeholder='https://producer.example/api/procedures/… (or http://127.0.0.1:<port>/api/…)';
  nativeInput.value=initialNativeUrl;
  nativeInput.autocomplete='off';
  const nativeLoad=node('button','rdp-mode','Load native resource + discover Profile');
  nativeLoad.id='rdp-load-native';nativeLoad.type='button';
  nativeWrap.append(nativeLabel,nativeInput,nativeLoad);
  controls.append(pickerWrap,modeGroup,nativeWrap,count);
  toolbar.before(controls);
  const note=node('div','rdp-case-note');
  const insight=node('p','rdp-insight');
  stage.after(note,insight);
  const frame=stage.querySelector<HTMLElement>('.rd-module');
  if(!frame)throw new Error('Resource Details frame not found');
  const title=frame.querySelector<HTMLElement>('.rd-resource-name');
  const dd=frame.querySelectorAll<HTMLElement>('.rd-identity-fields dd');
  const footer=frame.querySelector<HTMLElement>('.rd-module-footer span');
  const marker=frame.querySelectorAll<HTMLElement>('.rd-marking');
  for(const m of marker)m.textContent='Demonstration data · marking not assigned';
  const refresh=frame.querySelector<HTMLButtonElement>('.rd-refresh');if(refresh)refresh.title='No live CSAPI connection in this study';
  const repaint=():void=>{
    if(title)title.textContent=nativeSelected
      ? (nativeResult?.source?.name ?? 'Native CSAPI resource · awaiting Profile evidence')
      : packetCase ? (packet?.model.focus?.label ?? packetCase.label)
      : attribution?"Bennett's Point":(published?'Dragino + Campbell':selected.title);
    if(dd.length>=3){
      dd[0].textContent=nativeSelected ? (nativeResult?.source?.kind ?? 'Native source standing pending')
        : packetCase ? (packet?.model.focus?.standing ?? 'Loading source standing')
        : attribution?'Historical station observations':(published?'Published examples':selected.resourceStanding);
      dd[1].textContent=nativeSelected ? (nativeResult?.source?.uid ?? 'No verified bound native UID')
        : packetCase ? (packet?.model.focus?.sourceIdentity?.raw ?? 'No source-authenticated ID')
        : attribution?attributionCase.station.code:(published?'No installed unit':selected.identifier);
      dd[2].textContent=nativeSelected
        ? (nativeResult?.kind==='profile' ? 'Native CSAPI GeoJSON + linked project source evidence' : 'Native source / no accepted project Profile')
        : packetCase ? 'Project research packet · NOT native CSAPI'
        : attribution?'Operator measurement + equipment records':(published?'Manufacturer documentation':selected.source);
    }
    if(footer)footer.textContent=nativeSelected ? 'Native read-only CSAPI + project evidence · issuer/OGC class conformance NOT verified · no commands'
      : packetCase ? 'Source packet experiment · no CSAPI discovery or verified device control'
      : attribution?'Historical observations · operator records':(published?'Published examples · not live readings':'Candidate semantics · no actual device control');
    genericBtn.textContent=nativeSelected ? 'Raw native + project evidence' : packetCase ? 'Raw packet · not native CSAPI' : 'Generic CSAPI-style fields';
    genericBtn.setAttribute('aria-pressed',String(mode==='generic'));
    profileBtn.setAttribute('aria-pressed',String(mode==='profile'));
    count.textContent=nativeSelected ? (packetLoadError ? 'Native loading failed: '+packetLoadError
      : nativeResult?.kind==='raw' ? 'Native raw-only · Profile rejected: '+nativeResult.reason
      : packet ? 'Native CSAPI '+nativeResult?.source?.kind+' · '+packet.model.subjects.length+' source-described subjects · '+packet.model.claims.length+' source claims · '+packet.originalEventCount+' original source-event anchors · '+packet.experimentalRepresentationCount+' historical experiment copies'
      : 'Loading native CSAPI resource and Profile evidence…')
      : packetCase
      ? (packetLoadError ? 'Local packet load failed: '+packetLoadError : packet ? packet.model.subjects.length+' declared subjects · '+packet.model.claims.length+
        ' source claims · '+packet.originalEventCount+' original source-event anchors · '+
        packet.experimentalRepresentationCount+' historical experiment copies' : 'Loading source packet…')
      : attribution?String(attributionCase.records.length)+' historical observations · '+String(new Set(attributionCase.records.map(r=>r.probe.serial)).size)+' physical probes'
        :(published?`${measures.length} fields · ${measures.filter(r=>r.value!==undefined).length} published example values`
          :String(selected.fields.length)+' source fields · '+String(mappedFieldCount(selected))+' recognized by candidate rules · '+String(unmappedFields(selected).length)+' unknown meanings retained');
    note.textContent=nativeSelected
      ? (nativeResult?.kind==='profile'
        ? 'Actually retrieved native GeoJSON; source standing is a separate PROJECT Profile sidecar, PRODUCER_ASSERTED_UNVERIFIED. No full OGC ATS or live equipment control.'
        : 'No usable linked project Profile evidence: native resource is raw-only. Never infer source authenticity or original events.')
      : packetCase
      ? 'Local research evidence · project declarations are not independently source-authenticated, native CSAPI or live telemetry. Inspect Management → Record/Sources.'
      : attribution?attributionCase.note:(published?'Campbell’s logger example is separate from the ClimaVue manual. It is not a weather report from that instrument.':selected.warning);
    insight.textContent=nativeSelected
      ? 'Profile links are discovered from the actual resource response, never from a product-name switch. Original examples, DERIVED/UNKNOWN, and Bennett original-event/copy counts remain source-qualified; no per-probe geometry is synthesized.'
      : packetCase
      ? 'The same evidence reader and UI rules apply to all project packets. Equipment, source examples, original events/copies, DERIVED facts and UNKNOWNs are kept distinct; the Map never infers a probe location.'
      : attribution?'Read the two observation cards: same station, same EE181 model, same property — different serial number on opposite sides of the documented swap.'
        :(published?'Try “Show air temperature only.” The wiring-panel temperature disappears; the ClimaVue air-temperature field stays, without borrowing a reading.':'What this preserves: '+insightText(selected));
    const active=frame.querySelector<HTMLButtonElement>('.rd-view-tabs .rd-tab[aria-selected="true"]');
    active?.click();
  };
  const loadNative=(url:string,version:number):void=>{
    packet=null;nativeResult=null;packetLoadError=null;nativeSelected=true;packetCase=null;
    attribution=false;published=false;mode='profile';picker.value='native-csapi';
    frame.querySelector<HTMLButtonElement>('#rd-category-operational')?.click();
    repaint();
    void loadNativeSourceProfile(url).then(result=>{
      if(version!==pending)return;
      nativeResult=result;
      packet=result.kind==='profile' ? (result.presentation ?? null) : null;
      repaint();
    }).catch(error=>{
      if(version!==pending)return;
      nativeResult=null;packet=null;
      packetLoadError=error instanceof Error?error.message:String(error);
      repaint();
    });
  };
  nativeLoad.addEventListener('click',()=>{
    const inputUrl=nativeInput.value.trim();
    const version=++pending;
    if(!inputUrl){
      nativeSelected=true;packet=null;nativeResult=null;packetLoadError='Provide a native Procedure/System URL';
      picker.value='native-csapi';repaint();return;
    }
    loadNative(inputUrl,version);
  });
  const loadPacketCase=(chosen:PacketCase, version:number):void=>{
    // No vendor-dependent interpretation. The selector chooses only exact local input bytes.
    void fetch(chosen.path,{cache:'no-store'}).then(async response=>{
      if(!response.ok)throw new Error('Local source packet HTTP '+String(response.status));
      return response.json() as Promise<unknown>;
    }).then(raw=>{
      if(version!==pending)return;
      packetLoadError=null;
      packet=buildPacketPresentation(raw);
      repaint();
    }).catch(error=>{
      if(version!==pending)return;
      packet=null;
      packetLoadError=error instanceof Error?error.message:String(error);
      count.textContent='Could not load local source packet: '+packetLoadError;
      note.textContent='Local research packet load failed; no remote CSAPI request was attempted.';
      const active=frame.querySelector<HTMLButtonElement>('.rd-view-tabs .rd-tab[aria-selected="true"]');
      active?.click();
    });
  };
  genericBtn.addEventListener('click',()=>{mode='generic';repaint();});
  profileBtn.addEventListener('click',()=>{mode='profile';repaint();});
  picker.addEventListener('change',()=>{
    const key=picker.value;const current=++pending;
    const chosen=packetCases.find(p=>p.key===key);
    if(key==='native-csapi'){
      nativeSelected=true;packetCase=null;packet=null;nativeResult=null;
      packetLoadError=null;attribution=false;published=false;mode='profile';
      frame.querySelector<HTMLButtonElement>('#rd-category-operational')?.click();
      repaint();return;
    }
    nativeSelected=false;nativeResult=null;
    if(chosen){
      packetCase=chosen;packet=null;packetLoadError=null;attribution=false;published=false;mode='profile';
      frame.querySelector<HTMLButtonElement>('#rd-category-operational')?.click();
      frame.querySelector<HTMLButtonElement>('#rd-view-overview')?.click();
      repaint();loadPacketCase(chosen,current);return;
    }
    packetCase=null;packet=null;packetLoadError=null;
    if(key===attributionCaseKey){
      attribution=true; published=false; mode='profile';
      frame.querySelector<HTMLButtonElement>('#rd-category-operational')?.click();
      frame.querySelector<HTMLButtonElement>('#rd-view-overview')?.click();
      repaint(); return;
    }
    if(key===caseKey){
      attribution=false; published=true; mode='profile';
      frame.querySelector<HTMLButtonElement>('#rd-category-operational')?.click();
      frame.querySelector<HTMLButtonElement>('#rd-view-overview')?.click();
      repaint(); return;
    }
    if(key==='sck23'){attribution=false;published=false;selected=smartCitizenDesign;repaint();return;}
    const fixture=inputFixtures.find(f=>f.key===key);
    if(!fixture)return;
    count.textContent='Loading local source fixture…';
    void fetch(fixture.path,{cache:'no-store'}).then(async response=>{
      if(!response.ok)throw new Error('Fixture HTTP '+String(response.status));
      return response.json() as Promise<Parameters<typeof projectSourceFixture>[0]>;
    }).then(doc=>{
      if(current!==pending)return;
      selected=projectSourceFixture(doc,fixture.key);attribution=false;published=false;
      repaint();
    }).catch(err=>{
      if(current!==pending)return;
      picker.value=attribution?attributionCaseKey:(published?caseKey:selected.key);
      count.textContent='Could not load this source fixture: '+(err instanceof Error?err.message:String(err));
    });
  });
  if(nativeSelected){
    const current=++pending;
    loadNative(initialNativeUrl,current);
  } else if(packetCase) {
    const current=++pending;
    repaint();loadPacketCase(packetCase,current);
  } else repaint();
}
