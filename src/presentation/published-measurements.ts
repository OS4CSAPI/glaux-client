import { node } from './resource-details-template';
import { measures, readingText, researchRoot, sourceGroups } from '../profile/published-measurements';
import './published-measurements.css';

const air = 'http://vocab.nerc.ac.uk/standard_name/air_temperature/';
function sourceLink(label: string, url: string): HTMLAnchorElement {
  const a = node('a', undefined, label); a.href = url; a.target='_blank'; a.rel='noopener noreferrer'; return a;
}

/** One rendering path. The fixtures declare source scope, field definition, unit and example value. */
export function renderPublished(content: HTMLElement, view: string, raw: boolean): void {
  if (view === 'management/Sources') {
    const section=node('section','rdp-section'); section.append(node('h3',undefined,'Where the examples come from'));
    const list=node('ul','rdp-sources-list');
    for (const s of sourceGroups) {const li=node('li'); li.append(sourceLink(s.source,s.url)); list.append(li);}
    const li=node('li'); li.append(sourceLink('Draft Profile and worked mappings',researchRoot+'Candidate_Specification/CSAPI_Profile.md#campbell-temperature-of-what')); list.append(li);
    section.append(list); content.append(section); return;
  }
  if (view !== 'operational/Overview') {
    const div=node('div','rdp-no-data'); div.append(node('p',undefined,'This comparison has no installed station or live activity. See Operational → Overview for the published examples, or Management → Sources for their origins.')); content.append(div); return;
  }
  const panel=node('section','pub-measures'); panel.setAttribute('aria-label','Published measurement examples');
  panel.append(node('h3',undefined,raw?'Fields as published':'Temperature of what?'));
  panel.append(node('p','pub-intro','Separate manufacturer examples and manual definitions. Not live data or readings from a single station.'));
  const label=node('label','pub-filter'); const toggle=node('input'); toggle.type='checkbox';
  label.append(toggle,document.createTextNode(' Show air temperature only')); if (!raw) panel.append(label);
  const list=node('div','pub-list'); panel.append(list); content.append(panel);
  const paint=():void=>{
    list.replaceChildren();
    for (const group of sourceGroups) {
      const rows=measures.filter(r=>r.context===group.context && (raw || !toggle.checked || r.field.definition===air));
      if (!rows.length) continue;
      const section=node('section','pub-group'); section.dataset.context=group.context;
      const h=node('h4',undefined,group.title); h.append(node('small',undefined,group.detail)); section.append(h);
      const dl=node('dl');
      const native: Readonly<Partial<Record<string,string>>> = group.raw;
      for (const r of rows) {
        const item=node('div','pub-row'); item.dataset.definition=r.field.definition;
        const term=node('dt',undefined,raw?(native[r.field.name]??r.field.name):r.field.label);
        const dd=node('dd'); const present=r.value!==undefined;
        if (present) {dd.append(node('strong',undefined,readingText(r)),node('small',undefined,'Published example'));}
        else {dd.append(node('span','pub-absent',readingText(r)),node('small',undefined,'Defined in the manual'));}
        item.append(term,dd); dl.append(item);
      }
      section.append(dl); list.append(section);
    }
  };
  toggle.addEventListener('change',paint); paint();
}
