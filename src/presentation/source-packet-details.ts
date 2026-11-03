import { node } from './resource-details-template';
import { renderResourceMap } from './resource-details-map';
import type { ClaimView, SubjectView } from '../profile/source-packet';
import { packetClaimsForView, type PacketPresentation } from '../profile/source-packet-presentation';
import type { ViewKey } from '../profile/resource-details-proof';

/**
 * One presentation rule set, in the EXISTING Resource Details frame.
 * The SAME interpretation covers local packets and source evidence linked from
 * a real native CSAPI Feature. Native resource body and sidecar remain distinct;
 * source authenticity, full OGC conformance and live telemetry are NOT inferred.
 */
function section(content: HTMLElement, title: string): HTMLElement {
  const s = node('section', 'rdp-section');
  s.append(node('h3', undefined, title)); content.append(s); return s;
}
function field(parent: HTMLElement, name: string, value: string, note?: string): void {
  const row = node('div', 'rdp-field'), def = node('dd');
  def.append(node('span', undefined, value));
  if (note) def.append(node('small', 'rdp-qualifier', note));
  row.append(node('dt', undefined, name), def); parent.append(row);
}
function list(s: HTMLElement): HTMLElement {
  const dl = node('dl', 'rdp-field-grid'); s.append(dl); return dl;
}
function note(content: HTMLElement, message: string): void {
  content.append(node('p', 'rdp-footnote', message));
}
function empty(content: HTMLElement, message: string): void {
  const div=node('div','rdp-no-data'); div.append(node('p',undefined,message)); content.append(div);
}
function sourceUrl(parent: HTMLElement, name: string, url: string): void {
  // A research fixture cannot use an arbitrary URL as an executable href.
  if (!/^https:\/\//i.test(url)) { parent.append(node('span', undefined, name)); return; }
  const link=node('a', undefined, name);
  link.href=url; link.target='_blank'; link.rel='noopener noreferrer'; parent.append(link);
}
function rawText(claim: ClaimView): string {
  if (claim.kind === 'unknown') return 'UNKNOWN — ' + (claim.reason ?? 'Source did not establish this fact');
  if (claim.target) return 'Relationship to subject: ' + claim.target;
  if (claim.value) {
    const value = claim.value.raw;
    // Make empty and whitespace-sensitive native source tokens inspectable.
    const literal = !value || value.trim() !== value ? JSON.stringify(value) : value;
    return literal + (claim.value.unit ? ' ' + claim.value.unit : '');
  }
  return 'Not supplied';
}
function qualifiedClaim(content: HTMLElement, item: ClaimView, model: PacketPresentation): void {
  const group=node('div','rdp-group');
  group.dataset.assertionId=item.id;
  const label=node('h4', undefined, item.concept);
  group.append(label);
  const dl=list(group);
  const standing = item.standing === 'SOURCE_EXAMPLE' ? 'SOURCE_EXAMPLE — published illustration; not actual telemetry'
    : item.standing === 'DERIVED' ? 'DERIVED — project transformation, not original issuer-authored'
      : item.standing === 'UNKNOWN' ? 'UNKNOWN — no asserted source value'
        : 'SOURCE_FACT — project-declared original-source fact, not independently authenticated';
  field(dl,'Standing',standing);
  field(dl,'About',model.model.subjects.find(s=>s.id===item.about)?.label ??
    model.model.events.find(e=>e.id===item.about)?.recordLocator ?? item.about);
  field(dl,item.kind === 'relationship' ? 'Declared relationship' : 'Source value',rawText(item),
    item.value?.nativeField ? 'Native source field: '+item.value.nativeField : undefined);
  if (item.target) {
    const target: SubjectView | undefined = model.model.subjects.find(s=>s.id===item.target);
    if (target) field(dl,'Target standing',target.standing+' · '+target.label);
  }
  if (item.time !== undefined) field(dl,'Source/qualified time',JSON.stringify(item.time),
    'Retain native calendar-day or explicitly DERIVED precision. Not an automatic Deployment or resultTime.');
  if (item.derivation) field(dl,'Derivation',item.derivation.method,
    'Inputs: '+item.derivation.inputs.join(', '));
  if (!item.recognized) field(dl,'Unknown concept','Unrecognized; retained in original source packet',
    'No interpretation was invented from the name.');
  const sources=item.evidence.map(e=>e.sourceId+': '+e.locator).join('; ');
  field(dl,'Evidence locators',sources,'Original source claims must be independently verified');
  // Machine-readable raw tokens, including trailing whitespace and blank F_Record, remain visible.
  const tokens=item.evidence.filter(e=>e.nativeToken!==undefined).map(e=>JSON.stringify(e.nativeToken));
  if(tokens.length) field(dl,'Original literal tokens',tokens.join(' · '));
  content.append(group);
}
function claims(content:HTMLElement, model:PacketPresentation, view:ViewKey):void {
  const selected=packetClaimsForView(model,view);
  if (!selected.length) {
    empty(content,'No assertions for this area are available in the selected project packet. This is not proof that the equipment lacks the capability.');
    return;
  }
  for (const item of selected) qualifiedClaim(content,item,model);
}
function sources(content: HTMLElement, packet: PacketPresentation): void {
  const s=section(content,'Original-source pointers retained in the project packet');
  const ul=node('ul','rdp-sources-list');
  for(const doc of packet.sourceDocuments){
    const li=node('li');
    sourceUrl(li,doc.issuer+' — '+doc.title,doc.url);
    li.append(node('small','rdp-qualifier','Edition: '+doc.edition+' · Authority declared: '+doc.authority));
    ul.append(li);
  }
  s.append(ul);
  const holds=section(content,'Unresolved evidence and interoperability conditions');
  const dl=list(holds);
  for(const h of packet.holds)field(dl,h.gap+' · '+h.topic,h.reason);
}
function originalEvents(content: HTMLElement, packet: PacketPresentation): void {
  if (!packet.model.events.length) {
    empty(content,'No original performed source events are asserted. A source EXAMPLE is not a recorded Observation.');
    return;
  }
  const s=section(content,'Source-original reports — count each original ONCE');
  note(s,'Historical original event IDs and experimental copy links are declared by this research packet, not a native CSAPI same-event relation.');
  for(const event of packet.model.events){
    const box=node('div','rdp-group'), dl=list(box);
    box.append(node('h4',undefined,'Original report · '+event.recordLocator));
    field(dl,'Source/report identity',event.sourceId+' · '+event.nativeField);
    field(dl,'Packet-declared subject',packet.model.subjects.find(x=>x.id===event.subject)?.label ?? event.subject);
    field(dl,'Prior experimental API copies',String(event.copies.length),
      'Multiple project resources do not create additional NOAA measurements.');
    for(const copy of event.copies)field(dl,'Historical project copy',copy.resourceRef,
      copy.carrier+' · '+copy.standing+' · Not independently revalidated live');
    s.append(box);
  }
}
function overview(content: HTMLElement, packet: PacketPresentation): void {
  const s=section(content,packet.nativeResource
    ? 'Native CSAPI Resource + separately linked project evidence'
    : 'Evidence-qualified resource overview (project input)');
  const dl=list(s), focus=packet.model.focus;
  if(packet.nativeResource) {
    field(dl,'Native CSAPI resource',packet.nativeResource.url);
    field(dl,'Native class',packet.nativeResource.kind,
      'Actual source-backed Procedure/System GeoJSON; producer full OGC requirements-class conformance is not established.');
    field(dl,'Native UID (integrator)',packet.nativeResource.uid);
    field(dl,'Registered Profile link',packet.nativeResource.profileUrl);
    field(dl,'Linked project evidence',packet.nativeResource.evidenceUrl);
    field(dl,'Producer assertion standing',packet.nativeResource.verification,
      'Not a digitally verified original manufacturer or NOAA issuer.');
  }
  field(dl,'Focal referent',focus?.label ?? 'Unresolved');
  field(dl,'Declared referent standing',focus?.standing ?? 'UNKNOWN',
    'REFERENCE design does not constitute a registered physical System. Source standing requires independent corroboration.');
  field(dl,'Source-described subjects',String(packet.model.subjects.length));
  field(dl,'Selected assertions',String(packet.model.claims.length));
  field(dl,'Original source-report anchors',String(packet.originalEventCount));
  field(dl,'Prior experimental API representations',String(packet.experimentalRepresentationCount),
    'Representations are not additional original reports.');
  field(dl,'Packet accepted by parser',String(packet.model.accepted),
    'Structure/link validation only, not source truth, official OGC schema conformance or native API discoverability.');
  const uncertainty=packet.model.claims.filter(x=>x.standing==='UNKNOWN').length;
  const derived=packet.model.claims.filter(x=>x.standing==='DERIVED').length;
  const examples=packet.model.claims.filter(x=>x.standing==='SOURCE_EXAMPLE').length;
  field(dl,'Uncertainty and example standing',uncertainty+' UNKNOWN · '+derived+' DERIVED · '+examples+' SOURCE_EXAMPLE');
  note(s,'Overview summarizes provenance and source-defined meaning. Equipment, Activity and Management retain individual assertions and raw source text.');
}
function rawRecord(content: HTMLElement, packet: PacketPresentation): void {
  const s=section(content,packet.nativeResource
    ? 'Linked project evidence — complete raw source packet'
    : 'Original project packet — complete raw JSON');
  note(s,packet.nativeResource
    ? 'Evidence was retrieved through a genuine native GeoJSON resource’s versioned Profile links. This local project description is not itself an OGC-native object or publisher-authenticated record.'
    : 'Unmodified raw project input, including unknown fields, literal source QA whitespace, original time precision, derivations and copy IDs. This is not a native CSAPI response.');
  if(packet.nativeResource) {
    const feature=section(content,'Original native CSAPI GeoJSON Feature — unmodified');
    feature.append(node('pre','raw-content',JSON.stringify(packet.nativeResource.nativeRaw,null,2)));
    const rawSidecar=section(content,'Linked producer evidence document — unmodified');
    rawSidecar.append(node('pre','raw-content',JSON.stringify(packet.nativeResource.evidenceRaw,null,2)));
  }
  const pre=node('pre','raw-content',JSON.stringify(packet.model.raw,null,2));
  s.append(pre);
  const link=node('p','rdp-footnote');sourceUrl(link,'Open existing live native CSAPI inspector (separate workflow)','https://glaux-client.pages.dev/?page=resource-details-live-csapi');s.append(link);
}
function generic(content: HTMLElement, packet: PacketPresentation, view:ViewKey):void {
  if(view==='management/Record'){rawRecord(content,packet);return;}
  if(view==='management/Sources'){sources(content,packet);rawRecord(content,packet);return;}
  const s=section(content,packet.nativeResource
    ? 'Uninterpreted project source claims (underlying native Feature preserved)'
    : 'Uninterpreted project evidence — not native CSAPI');
  const dl=list(s);
  field(dl,'Packet discriminator',packet.packetId || 'Not supplied');
  field(dl,'Original payload kind',packet.nativeResource
    ? 'Actual retrieved native CSAPI GeoJSON ' + packet.nativeResource.kind + ', plus separately linked project source evidence'
    : 'Locally supplied project source packet, not an OGC System/DataStream/Observation');
  field(dl,'Selected assertions',String(packet.model.claims.length));
  field(dl,'Original source-event anchors',String(packet.originalEventCount));
  field(dl,'Original raw payload','Available under Management → Record and Sources');
  note(s,'Generic mode does not infer operational categories from manufacturer labels or case IDs. Existing live CSAPI/Standard inspector remains a separate, unchanged view.');
}

/**
 * Called from the EXISTING Resource Details template's renderBlankContent path.
 * The shared Map component is reused with null: none of the four packets has a
 * validated, subject-specific GeoJSON position. This NEVER maps a station site
 * point to a physical probe or opens map tiles for missing positions.
 */
export function renderSourcePacketDetails(content: HTMLElement, packet: PacketPresentation,
  view: ViewKey, mode: 'profile' | 'generic'): void {
  content.append(node('p','rdp-standing',packet.nativeResource
    ? 'NATIVE CSAPI GEOJSON FEATURE + LINKED PROJECT PROFILE EVIDENCE · issuer UNVERIFIED · no live commands or full class conformance'
    : 'RESEARCH PACKET · locally declared source standing only · not native CSAPI, live data, or source-authenticated Profile'));
  if(!packet.model.accepted){
    const s=section(content,'Packet structure or references rejected');
    const dl=list(s);
    for(const x of packet.model.issues)field(dl,x.path,x.message);
    rawRecord(content,packet);return;
  }
  if(mode==='generic'){generic(content,packet,view);return;}
  switch(view){
    case 'operational/Overview': overview(content,packet);break;
    case 'operational/Map':
      note(content,'No validated subject-specific geographic position is provided by this packet. A station-site location is NOT a serial-numbered sensor location.');
      renderResourceMap(content,packet.mappablePosition);break;
    case 'operational/Equipment':{
      const s=section(content,'Equipment reference and source-identified referents');
      const dl=list(s);
      for (const subject of packet.model.subjects) {
        field(dl,subject.label,subject.standing,
          subject.sourceIdentity ? subject.sourceIdentity.scheme+': '+subject.sourceIdentity.raw+' · issuer: '+subject.sourceIdentity.issuer
            : 'No source-issued individual identity provided');
      }
      claims(content,packet,view);break;
    }
    case 'activity/Table': originalEvents(content,packet);claims(content,packet,view);break;
    case 'activity/Charts':
      empty(content,'No chart is drawn from author-declared observations or SOURCE_EXAMPLE values. Source/derived time and original event count require validation before charting.');break;
    case 'commands/Available':
    case 'commands/Requests':
      empty(content,'No authenticated ControlStream, user permission, issued Command, status or physical effect is established by this research packet.');break;
    case 'management/Record':rawRecord(content,packet);break;
    case 'management/Sources':sources(content,packet);claims(content,packet,view);break;
    case 'management/Configuration':claims(content,packet,view);break;
    default:claims(content,packet,view);break;
  }
  note(content,packet.warnings.join(' '));
}
