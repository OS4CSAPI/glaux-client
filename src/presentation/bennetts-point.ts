import { node } from './resource-details-template';
import { attributionCase } from '../profile/bennetts-point';

function field(list:HTMLElement,label:string,value:string,note?:string):void{
  const row=node('div','rdp-field'); const dd=node('dd'); dd.append(node('span',undefined,value));
  if(note) dd.append(node('small','rdp-qualifier',note));
  row.append(node('dt',undefined,label),dd); list.append(row);
}
function empty(content:HTMLElement,text:string):void{
  const block=node('div','rdp-no-data'); block.append(node('p',undefined,text)); content.append(block);
}
function overview(content:HTMLElement):void{
  const s=node('section','rdp-section'); s.append(node('h3',undefined,'Bennett’s Point probe-swap summary'));
  const dl=node('dl','rdp-field-grid');
  field(dl,'Station',attributionCase.station.name+' · '+attributionCase.station.code);
  field(dl,'Probe model',attributionCase.model.manufacturer+' '+attributionCase.model.designation);
  field(dl,'Historical observations',String(attributionCase.records.length));
  field(dl,'Physical probes',String(new Set(attributionCase.records.map(r=>r.probe.serial)).size));
  s.append(dl,node('p','rdp-footnote','Overview summarizes the case. Detailed equipment, observation, quality and source facts are in their dedicated views.'));
  content.append(s);
}
function equipment(content:HTMLElement):void{
  const m=node('section','rdp-section'); m.append(node('h3',undefined,'Equipment model'));
  const mdl=node('dl','rdp-field-grid');
  field(mdl,'Manufacturer',attributionCase.model.manufacturer);
  field(mdl,'Model',attributionCase.model.designation);
  field(mdl,'Role',attributionCase.model.label,'Model information, not an individual-unit identity.');
  m.append(mdl); content.append(m);

  const u=node('section','rdp-section'); u.append(node('h3',undefined,'Identified physical probes'));
  const udl=node('dl','rdp-field-grid'); const seen=new Map<string,string>();
  for(const r of attributionCase.records) seen.set(r.probe.serial,r.probe.label);
  for(const [serial,label] of seen) field(udl,label,serial,'Individual EE181 unit.');
  u.append(udl); content.append(u);

  const d=node('section','rdp-section'); d.append(node('h3',undefined,'Documented use periods'));
  const ddl=node('dl','rdp-field-grid');
  for(const p of attributionCase.deployments){
    field(ddl,p.label+' · '+p.serial,p.start+' → '+(p.end ?? 'still in use at 2024 report cutoff'),p.note);
  }
  d.append(ddl,node('p','rdp-footnote','Sensor 3 keeps the same identity when it returns; the later period is not a new probe.'));
  content.append(d);
}
function activityTable(content:HTMLElement):void{
  const s=node('section','pub-measures'); s.append(node('h3',undefined,'Historical air-temperature observations'));
  const list=node('div','pub-list');
  for(const r of attributionCase.records){
    const g=node('section','pub-group'); g.append(node('h4',undefined,r.displayTime)); const dl=node('dl');
    for(const [label,value,note] of [
      ['Air temperature',String(r.value)+' '+r.unit,undefined],
      ['Quality',r.quality,r.qualityMeaning],
      ['Sensing probe',r.probe.label,undefined],
      ['Serial number',r.probe.serial,undefined],
    ] as Array<[string,string,string|undefined]>){
      const row=node('div','pub-row'); const dd=node('dd'); dd.append(node('strong',undefined,value));
      if(note) dd.append(node('small',undefined,note)); row.append(node('dt',undefined,label),dd); dl.append(row);
    }
    g.append(dl); list.append(g);
  }
  s.append(list); content.append(s);
}
function activityCharts(content:HTMLElement):void{
  const s=node('section','rdp-section'); s.append(node('h3',undefined,'Temperature series'));
  s.append(node('p',undefined,'Only two observations are included in this bounded case, so the view does not claim an environmental trend.'));
  const dl=node('dl','rdp-field-grid');
  for(const r of attributionCase.records) field(dl,r.displayTime,String(r.value)+' '+r.unit,r.probe.label+' · '+r.probe.serial);
  s.append(dl); content.append(s);
}
function record(content:HTMLElement):void{
  const s=node('section','rdp-section'); s.append(node('h3',undefined,'Prepared observation records'));
  s.append(node('p','rdp-footnote','Prepared demonstration records, not live server responses.'));
  for(const r of attributionCase.records){
    const details=node('details','capture'); details.append(node('summary',undefined,r.displayTime),
      node('pre','raw-content',JSON.stringify({timestamp:r.timestamp,property:r.property,value:r.value,unit:r.unit,quality:r.quality,probe:r.probe},null,2)));
    s.append(details);
  }
  content.append(s);
}
function sources(content:HTMLElement):void{
  const s=node('section','rdp-section'); s.append(node('h3',undefined,'Operator records and Profile mapping'));
  const ul=node('ul','rdp-sources-list');
  for(const src of attributionCase.sources){const li=node('li');const a=node('a',undefined,src.label);a.href=src.url;a.target='_blank';a.rel='noopener noreferrer';li.append(a);ul.append(li);}
  s.append(ul,node('p','rdp-footnote',attributionCase.note));content.append(s);
}

export function renderBennettsPoint(content:HTMLElement,view:string,raw:boolean):void{
  if(view==='operational/Overview'){overview(content);return;}
  if(view==='operational/Equipment'){equipment(content);return;}
  if(view==='operational/Map'){empty(content,'No coordinates were selected for this bounded case. Deployment periods remain under Equipment.');return;}
  if(view==='operational/Communications'){empty(content,'No communications-interface evidence was selected for this case.');return;}
  if(view==='operational/Condition'){empty(content,'No current equipment-condition report is represented. Historical temperature observations belong under Activity.');return;}
  if(view==='activity/Table'){activityTable(content);return;}
  if(view==='activity/Charts'){activityCharts(content);return;}
  if(view.startsWith('commands/')){empty(content,'No command or control evidence is represented in this case.');return;}
  if(view==='management/Record'){record(content);return;}
  if(view==='management/Configuration'){empty(content,'No current configuration or attributable setting readback is represented in this case.');return;}
  if(view==='management/Sources'){sources(content);return;}
  empty(content,raw?'No raw placement is defined for this view.':'No placement is defined for this view.');
}
