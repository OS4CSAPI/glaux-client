"""Offline example reader; run with Python 3.10+. No network, Glaux or OGC service.

The two adapters select source documents. rows() has no product names, expected
field counts, vendor field keys, or temperature-specific display branches.
"""
import json
from pathlib import Path
from collections.abc import Iterator

HERE = Path(__file__).resolve().parent
SHEETS = HERE.parents[1] / 'Controlled_Corpus' / 'System_Data_Sheets'


def rows(descriptions: list[dict], examples: list[dict]) -> list[tuple]:
    """Join at source context + output name + field name, never unit or row order."""
    selected = {}
    for description in descriptions:
        output = description['output']
        for field in output['fields']:
            key = (description['context'], output['name'], field['name'])
            if key in selected:
                raise ValueError(f'Duplicate field identity: {key}')
            selected[key] = field
    values = {}
    for entry in examples:
        for name, value in entry['values'].items():
            key = (entry['context'], entry['output'], name)
            if key not in selected or key in values:
                raise ValueError(f'Unmatched or duplicate example: {key}')
            values[key] = value
    return [(key[0], f['label'], f['definition'], f['uom']['code'], values.get(key))
            for key, f in selected.items()]


def sheet_row(filename: str, row_id: str) -> list[str]:
    matches = [line for line in (SHEETS / filename).read_text(encoding='utf-8').splitlines()
               if line.startswith(f'| {row_id} |')]
    if len(matches) != 1:
        raise ValueError(f'Expected one source row: {row_id}')
    return [cell.strip() for cell in matches[0].strip('|').split('|')]


def check(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def preview() -> Iterator[tuple]:
    dragino = json.loads((HERE / 's31-lb-design.sml.json').read_text(encoding='utf-8'))
    output = dragino['components'][0]['outputs'][0]
    d = sheet_row('Dragino_S31_LB.md', 'C-E01')
    drag_rows = rows([{'context':'S31-LB probe example','output':output}],
                     [{'context':'S31-LB probe example','output':output['name'],
                       'values':{'temperature':float(d[3]),'relativeHumidity':float(d[2])}}])
    packet = json.loads((HERE / 'campbell-temperature-roles.json').read_text(encoding='utf-8'))
    descriptions, examples = packet['descriptions'], packet['examples']
    camp_rows = rows(descriptions, examples)
    panel = sheet_row('Campbell_CR1000X_ClimaVue50.md', 'D-S02')
    check(panel[1].strip('`') == 'PanelTemp' and float(panel[2]) == 25.91098, 'Recheck source panel example')
    by_label = {r[1]:r for r in camp_rows}
    check(len(camp_rows) == len(by_label) == 3, 'Three documented temperature roles expected in this case')
    check(by_label['Wiring panel temperature'][4] == float(panel[2]), 'Lost wiring panel sample')
    check(by_label['Air temperature'][4] is None and by_label['Humidity sensor temperature'][4] is None,
          'A sensor capability acquired an unsupported sample')
    check(len({r[2] for r in camp_rows}) == 3 and {r[3] for r in camp_rows} == {'Cel'},
          'Shared unit must not erase distinct property definitions')
    air = by_label['Air temperature'][2]
    check(drag_rows[0][2] == air and by_label['Wiring panel temperature'][2] != air,
          'Air temperatures should align across designs; wiring panel is not air')
    dictionary = {p['uniqueId']:p for p in packet['propertyDictionary']}
    panel_def, sensor_def = [dictionary[by_label[n][2]] for n in ('Wiring panel temperature','Humidity sensor temperature')]
    check(panel_def['baseProperty'] == sensor_def['baseProperty'] and panel_def['objectType'] != sensor_def['objectType'],
          'The same base quantity applies to different types of object')
    try:
        rows(descriptions, [dict(examples[0], context=descriptions[1]['context'])])
    except ValueError:
        pass
    else:
        raise AssertionError('Misassigned logger example was accepted')
    yield from drag_rows
    yield from camp_rows


if __name__ == '__main__':
    for context, label, definition, unit, value in preview():
        display = 'No example reading supplied' if value is None else f'{value} {unit} (published example)'
        print(f'{context} | {label} | {display}')
