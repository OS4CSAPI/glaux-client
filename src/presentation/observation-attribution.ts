interface AttributionRecord {
  timestamp: string;
  displayTime: string;
  property: string;
  value: number;
  unit: string;
  quality: string;
  qualityMeaning: string;
  probe: { label: string; serial: string };
}
interface AttributionFixture {
  title: string;
  subtitle: string;
  station: { name: string; code: string };
  model: { manufacturer: string; designation: string; label: string };
  records: AttributionRecord[];
  provenance: {
    measurement: string;
    measurementUrl: string;
    equipment: string;
    equipmentUrl: string;
    note: string;
  };
}

function el<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function link(label: string, href: string): HTMLAnchorElement {
  const a = el('a', undefined, label);
  a.href = href; a.target = '_blank'; a.rel = 'noopener noreferrer';
  return a;
}

function renderLoaded(container: HTMLElement, data: AttributionFixture): void {
  const body = document.createDocumentFragment();
  const style = el('style');
  style.textContent = `
    .attribution-demo{max-width:1000px;margin:0 auto;padding:28px 20px 60px;color:#18324a}
    .attribution-demo .demo-kicker{font-weight:700;color:#006a65;text-transform:uppercase;letter-spacing:.04em}
    .attribution-demo h1{margin:.3rem 0 .4rem;font-size:clamp(2rem,5vw,3.3rem)}
    .attribution-demo .demo-subtitle{font-size:1.15rem;color:#435b6d;margin:0 0 1.4rem}
    .attribution-demo .summary-card,.attribution-demo .record-card,.attribution-demo .meaning-card{background:#fff;border:1px solid #d9e2e8;border-radius:14px;padding:18px;margin:14px 0}
    .attribution-demo .summary-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px}
    .attribution-demo .summary-grid div{background:#f5f8fa;border-radius:10px;padding:12px}
    .attribution-demo dt{font-size:.82rem;color:#5d7180;text-transform:uppercase;letter-spacing:.03em}
    .attribution-demo dd{margin:.25rem 0 0;font-weight:700}
    .attribution-demo .records{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
    .attribution-demo .record-card{margin:0}
    .attribution-demo .reading{font-size:2.2rem;font-weight:800;margin:.2rem 0}
    .attribution-demo .probe{font-size:1.08rem;font-weight:700;color:#006a65}
    .attribution-demo .serial{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;background:#eef4f4;padding:.15rem .35rem;border-radius:5px}
    .attribution-demo .quality{display:inline-block;background:#edf5ef;border-radius:999px;padding:.3rem .65rem;margin:.55rem 0}
    .attribution-demo .arrow{font-size:2rem;text-align:center;color:#006a65;margin:.4rem 0}
    .attribution-demo .meaning-card{background:#18324a;color:#fff}
    .attribution-demo .meaning-card strong{color:#d6fff3}
    .attribution-demo .sources{font-size:.92rem;line-height:1.55}
    .attribution-demo .sources a{display:inline}
    .attribution-demo .back{display:inline-block;margin-bottom:18px}
  `;
  body.append(style);

  const main = el('main','attribution-demo');
  const back = el('a','back','← Page index'); back.href='/'; main.append(back);
  main.append(el('div','demo-kicker','Glaux profile demonstration'));
  main.append(el('h1',undefined,data.title));
  main.append(el('p','demo-subtitle',data.subtitle));

  const summary = el('section','summary-card');
  const summaryGrid = el('dl','summary-grid');
  for (const [label,value] of [
    ['Station',`${data.station.name} · ${data.station.code}`],
    ['Probe model',`${data.model.manufacturer} ${data.model.designation}`],
    ['What stays the same','Station, model, measured property'],
    ['What changes','The identified physical probe']
  ]) {
    const item = el('div'); item.append(el('dt',undefined,label),el('dd',undefined,value)); summaryGrid.append(item);
  }
  summary.append(summaryGrid); main.append(summary);

  const records = el('section','records');
  data.records.forEach((record,index) => {
    const card = el('article','record-card');
    card.append(el('div','demo-kicker',index === 0 ? 'Before the documented swap' : 'After the documented swap'));
    card.append(el('h2',undefined,record.displayTime));
    card.append(el('p',undefined,record.property));
    card.append(el('p','reading',`${record.value} ${record.unit}`));
    const quality = el('p','quality',`${record.quality} · ${record.qualityMeaning}`); card.append(quality);
    card.append(el('p','probe',record.probe.label));
    const serialLine = el('p'); serialLine.append(document.createTextNode('Serial '),el('span','serial',record.probe.serial)); card.append(serialLine);
    records.append(card);
  });
  main.append(records);

  if (data.records.length >= 2) {
    const a = data.records[0].probe.serial, b = data.records[1].probe.serial;
    const arrow = el('div','arrow','↓');
    const meaning = el('section','meaning-card');
    const p = el('p');
    p.append(document.createTextNode('Glaux is not deciding from the manufacturer name, model, or unit. The records already carry the attributed sensing unit. Because '));
    p.append(el('strong',undefined,a)); p.append(document.createTextNode(' and ')); p.append(el('strong',undefined,b));
    p.append(document.createTextNode(' are different, the client shows a probe change while keeping the same station and model.'));
    meaning.append(el('h2',undefined,'What the Profile preserved'),p);
    main.append(arrow,meaning);
  }

  const sources = el('section','summary-card sources');
  sources.append(el('h2',undefined,'Where the facts came from'));
  const list = el('ul');
  const m = el('li'); m.append(link(data.provenance.measurement,data.provenance.measurementUrl)); list.append(m);
  const e = el('li'); e.append(link(data.provenance.equipment,data.provenance.equipmentUrl)); list.append(e);
  sources.append(list,el('p',undefined,data.provenance.note));
  main.append(sources);

  body.append(main); container.className=''; container.replaceChildren(body);
}

export async function renderObservationAttributionDemo(container: HTMLElement, fixtureUrl = './fixtures/bennetts-point-attribution.json'): Promise<void> {
  container.className='';
  container.replaceChildren(el('p',undefined,'Loading observation attribution example…'));
  try {
    const response = await fetch(fixtureUrl, { cache: 'no-store' });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    renderLoaded(container, await response.json() as AttributionFixture);
  } catch (error) {
    container.replaceChildren(el('p',undefined,`Unable to load attribution example: ${error instanceof Error ? error.message : String(error)}`));
  }
}
