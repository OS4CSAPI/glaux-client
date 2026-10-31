import { node, renderResourceDetailsTemplate } from './resource-details-template';
import {
  smartCitizenDesign, inputFixtures, candidateRules, termsRetainedAsProvenance,
  mappedFieldCount, mappingsForView, unmappedFields, projectSourceFixture,
  type SourceCase, type SourceField, type MappedField, type ViewKey,
} from '../profile/resource-details-proof';
import { caseKey, measures } from '../profile/published-measurements';
import { renderPublished } from './published-measurements';
import './resource-details-profile-test.css';

type PresentationMode = 'profile' | 'generic';
const options:ReadonlyArray<{key:string;label:string}> = [
  { key:'sck23',label:'Smart Citizen Kit 2.3 — product design' },
  { key:caseKey,label:'Dragino + Campbell — published measurement examples' },
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
  let published=new URLSearchParams(window.location.search).get('case')===caseKey;
  let mode:PresentationMode='profile';
  let pending=0;
  renderResourceDetailsTemplate(container,{
    pageTitle:'Profile-aware Resource Details · source-to-UI test',
    pageIntro:'Compare published measurement examples, a product design or historical synthetic fixtures in the same Resource Details frame.',
    renderBlankContent({categoryId,view,content}){
      const key=(categoryId+'/'+view) as ViewKey;
      if(published)renderPublished(content,key,mode==='generic');
      else if(mode==='profile')renderCandidate(content,selected,key);
      else renderGeneric(content,selected,key);
      return true;
    },
    sourceSummary:'What this tests — and what it does not',
    sourceDescription:'This client reads documented source meanings. Dragino and Campbell use manufacturer examples and interface definitions; Smart Citizen is a product design; TRSS and OmniSense are synthetic. No live device or observation service is connected in this test.',
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
  picker.value=published?caseKey:'sck23';
  const pickerWrap=node('div','rdp-picker');pickerWrap.append(pickerLabel,picker);
  const modeGroup=node('div','rdp-mode-group');
  modeGroup.setAttribute('role','group');modeGroup.setAttribute('aria-label','Rendering mode');
  const genericBtn=node('button','rdp-mode','Generic CSAPI-style fields');genericBtn.type='button';
  const profileBtn=node('button','rdp-mode','Candidate profile-aware');profileBtn.type='button';
  modeGroup.append(genericBtn,profileBtn);
  const count=node('p','rdp-count');count.setAttribute('aria-live','polite');
  controls.append(pickerWrap,modeGroup,count);
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
    if(title)title.textContent=published?'Dragino + Campbell':selected.title;
    if(dd.length>=3){
      dd[0].textContent=published?'Published examples':selected.resourceStanding;
      dd[1].textContent=published?'No installed unit':selected.identifier;
      dd[2].textContent=published?'Manufacturer documentation':selected.source;
    }
    if(footer)footer.textContent=published?'Published examples · not live readings':'Candidate semantics · no actual device control';
    genericBtn.setAttribute('aria-pressed',String(mode==='generic'));
    profileBtn.setAttribute('aria-pressed',String(mode==='profile'));
    count.textContent=published?`${measures.length} fields · ${measures.filter(r=>r.value!==undefined).length} published example values`:String(selected.fields.length)+' source fields · '+String(mappedFieldCount(selected))+' recognized by candidate rules · '+String(unmappedFields(selected).length)+' unknown meanings retained';
    note.textContent=published?'Campbell’s logger example is separate from the ClimaVue manual. It is not a weather report from that instrument.':selected.warning;
    insight.textContent=published?'Try “Show air temperature only.” The wiring-panel temperature disappears; the ClimaVue air-temperature field stays, without borrowing a reading.':'What this preserves: '+insightText(selected);
    const active=frame.querySelector<HTMLButtonElement>('.rd-view-tabs .rd-tab[aria-selected="true"]');
    active?.click();
  };
  genericBtn.addEventListener('click',()=>{mode='generic';repaint();});
  profileBtn.addEventListener('click',()=>{mode='profile';repaint();});
  picker.addEventListener('change',()=>{
    const key=picker.value;const current=++pending;
    if(key===caseKey){
      published=true; mode='profile';
      frame.querySelector<HTMLButtonElement>('#rd-category-operational')?.click();
      frame.querySelector<HTMLButtonElement>('#rd-view-overview')?.click();
      repaint(); return;
    }
    if(key==='sck23'){published=false;selected=smartCitizenDesign;repaint();return;}
    const fixture=inputFixtures.find(f=>f.key===key);
    if(!fixture)return;
    count.textContent='Loading local source fixture…';
    void fetch(fixture.path,{cache:'no-store'}).then(async response=>{
      if(!response.ok)throw new Error('Fixture HTTP '+String(response.status));
      return response.json() as Promise<Parameters<typeof projectSourceFixture>[0]>;
    }).then(doc=>{
      if(current!==pending)return;
      selected=projectSourceFixture(doc,fixture.key);published=false;
      repaint();
    }).catch(err=>{
      if(current!==pending)return;
      picker.value=published?caseKey:selected.key;
      count.textContent='Could not load this source fixture: '+(err instanceof Error?err.message:String(err));
    });
  });
  repaint();
}
