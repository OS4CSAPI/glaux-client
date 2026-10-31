"""Offline acceptance example for the proposed component/output Profile. Python 3.10+.

Run: python3 check_s31.py. Reads the adjacent design and the retained Dragino sheet.
Checks this mapping, not general SensorML schema validity or a deployed station.
"""
from copy import deepcopy
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
VOCAB = 'http://vocab.nerc.ac.uk/standard_name/'
EXPECTED = {'temperature': ('air_temperature', 'Cel'),
            'relativeHumidity': ('relative_humidity', '%')}


def require(ok: bool, reason: str) -> None:
    if not ok:
        raise ValueError(reason)


def check_design(d: dict) -> None:
    """Fixture-specific acceptance criteria, not a universal one-probe constraint."""
    parts = d['components']
    require(d['type'] == 'PhysicalSystem' and len(parts) == 1, 'Expected one probe in this scoped design')
    p = parts[0]
    require(p['type'] == 'PhysicalComponent' and p['name'] == 'probe', 'Wrong probe role')
    require(p['uniqueId'] != d['uniqueId'], 'Distinct design descriptions required')
    for owner in (p, d):
        require(len(owner['outputs']) == 1, 'Expected one grouped environmental output')
        record = owner['outputs'][0]
        require((record['name'], record['type']) == ('environment', 'DataRecord'), 'Wrong output shape')
        fields = record['fields']
        require(len(fields) == len(EXPECTED) and {f['name'] for f in fields} == set(EXPECTED), 'Missing or duplicate field')
        for f in fields:
            term, unit = EXPECTED[f['name']]
            require((f['type'], f['definition'], f['uom']['code']) == ('Quantity', VOCAB + term + '/', unit), 'Property or unit changed')
    require(d['connections'] == [{'source': 'components/probe/outputs/environment', 'destination': 'outputs/environment'}], 'Output not linked to the documented probe')


def environmental_result(raw: bytes) -> dict | None:
    """Project only the two fields of one FPort 3 example; not a full decoder."""
    require(len(raw) == 11, 'Expected one 11-byte historical entry')
    if raw == bytes(11):
        return None  # Documented no-data reply, not two zero measurements.
    return {'temperature': int.from_bytes(raw[4:6], 'big', signed=True) / 10,
            'relativeHumidity': int.from_bytes(raw[2:4], 'big') / 10}


def reject(action, reason: str) -> None:
    try:
        action()
    except ValueError:
        return
    raise AssertionError(reason)


if __name__ == '__main__':
    design = json.loads((HERE / 's31-lb-design.sml.json').read_text(encoding='utf-8'))
    check_design(design)
    sheet = (HERE.parents[1] / 'Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md').read_text(encoding='utf-8')
    ids = []
    for line in sheet.splitlines():
        if not re.match(r'^\| C-E\d{2} \|', line):
            continue
        key, hex_input, rh, temp, *_ = [s.strip() for s in line.strip('|').split('|')]
        result = environmental_result(bytes.fromhex(hex_input))
        require(result == {'temperature': float(temp), 'relativeHumidity': float(rh)}, f'Value mismatch: {key}')
        ids.append(key)
    require(ids == [f'C-E{i:02d}' for i in range(1, 9)], 'Expected all eight distinct retained entries')
    bad = deepcopy(design)
    bad['components'].append(deepcopy(bad['components'][0]))
    reject(lambda: check_design(bad), 'Invented second probe accepted')
    bad = deepcopy(design)
    bad['outputs'][0]['fields'][1]['uom']['code'] = 'Cel'
    reject(lambda: check_design(bad), 'Humidity in degrees Celsius accepted')
    bad = deepcopy(design)
    bad['connections'][0]['source'] = 'components/other/outputs/environment'
    reject(lambda: check_design(bad), 'Missing source component accepted')
    require(environmental_result(bytes(11)) is None, 'No-data reply became an observation')
    reject(lambda: environmental_result(bytes(10)), 'Truncated entry accepted')
    print('PASS: scoped design; 8 published entries; 3 invalid designs rejected; no-data and length guards.')
