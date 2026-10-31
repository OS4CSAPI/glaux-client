import { node } from './resource-details-template';
import { attributionCase } from '../profile/bennetts-point';

function addLink(parent: HTMLElement, label: string, url: string): void {
  const a = node('a', undefined, label); a.href = url; a.target = '_blank'; a.rel = 'noopener noreferrer'; parent.append(a);
}

/** Render one evidence-backed observation-attribution case. The UI uses record fields, not station-name branching. */
export function renderBennettsPoint(content: HTMLElement, view: string, raw: boolean): void {
  if (view === 'management/Sources') {
    const section = node('section', 'rdp-section');
    section.append(node('h3', undefined, 'Operator records and Profile mapping'));
    const list = node('ul', 'rdp-sources-list');
    for (const source of attributionCase.sources) {
      const li = node('li'); addLink(li, source.label, source.url); list.append(li);
    }
    section.append(list, node('p', 'rdp-footnote', attributionCase.note)); content.append(section); return;
  }

  if (view !== 'operational/Overview') {
    const div = node('div', 'rdp-no-data');
    div.append(node('p', undefined, 'This case tests observation attribution across a documented equipment swap. Open Operational → Overview for the readings or Management → Sources for evidence.'));
    content.append(div); return;
  }

  const panel = node('section', 'pub-measures');
  panel.setAttribute('aria-label', 'Bennett’s Point observation attribution');
  panel.append(node('h3', undefined, raw ? 'Encoded observation facts' : 'Same station and model — different physical probe'));
  panel.append(node('p', 'pub-intro', 'Historical operator measurements. The station and EE181 model stay the same; the identified sensing unit changes across the documented swap.'));

  const summary = node('dl', 'rdp-field-grid');
  const summaryRows = [
    ['Station', attributionCase.station.name + ' · ' + attributionCase.station.code],
    ['Probe model', attributionCase.model.manufacturer + ' ' + attributionCase.model.designation],
    ['Measured property', attributionCase.records[0].property],
  ];
  for (const [label, value] of summaryRows) {
    const row = node('div', 'rdp-field'); row.append(node('dt', undefined, label), node('dd', undefined, value)); summary.append(row);
  }
  panel.append(summary);

  const list = node('div', 'pub-list');
  attributionCase.records.forEach((record, index) => {
    const section = node('section', 'pub-group');
    const heading = node('h4', undefined, record.displayTime);
    heading.append(node('small', undefined, index === 0 ? 'Before documented swap' : 'After documented swap'));
    section.append(heading);
    const dl = node('dl');

    const rows: Array<[string, string, string?]> = raw
      ? [
          ['Timestamp', record.timestamp],
          ['Air temperature', String(record.value) + ' ' + record.unit],
          ['Temperature flag', record.quality, record.qualityMeaning],
          ['Attributed probe label', record.probe.label],
          ['Attributed probe serial', record.probe.serial],
        ]
      : [
          ['Air temperature', String(record.value) + ' ' + record.unit],
          ['Quality', record.quality + ' · ' + record.qualityMeaning],
          ['Sensing probe', record.probe.label],
          ['Serial number', record.probe.serial],
        ];

    for (const [label, value, qualifier] of rows) {
      const item = node('div', 'pub-row');
      const dd = node('dd'); dd.append(node('strong', undefined, value));
      if (qualifier) dd.append(node('small', undefined, qualifier));
      item.append(node('dt', undefined, label), dd); dl.append(item);
    }
    section.append(dl); list.append(section);
  });
  panel.append(list);

  if (!raw) {
    const explain = node('p', 'rdp-footnote',
      'The client does not decide the probe from the manufacturer, model, temperature value or unit. The prepared observation records carry the attributed sensing-unit identity. That is why the serial changes while station, model and property remain the same.');
    panel.append(explain);
  }
  content.append(panel);
}
