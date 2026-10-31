"""Python 3.10+, standard library. Run `python3 check.py` from any directory."""
from copy import deepcopy
from datetime import date, datetime, timedelta, timezone
from math import isfinite
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
TIME = 'http://www.opengis.net/def/property/OGC/0/SamplingTime'
AIR = 'https://vocab.nerc.ac.uk/standard_name/air_temperature/'
BASE = 'urn:example:bp:'
SERIAL = 'http://sensorml.com/ont/swe/property/SerialNumber'
EST = timezone(timedelta(hours=-5))


def require(ok, why):
    if not ok:
        raise ValueError(why)


def instant(value):
    t = datetime.fromisoformat(value.replace('Z', '+00:00'))
    require(t.tzinfo is not None, 'missing UTC offset')
    return t


def read(cache, response):
    """Consumer: no station extract, task-specific dates, serials or expected values."""
    schema, body = cache['schema'], response['body']
    require(response['parent'] == cache['stream'], 'wrong parent stream')
    require((schema['obsFormat'], schema['encoding']['type'], schema['recordSchema']['type']) ==
            ('application/swe+json', 'JSONEncoding', 'DataRecord'), 'unsupported representation')
    fields = schema['recordSchema']['fields']
    by_role = {f['definition']: f for f in fields}
    require(len(by_role) == len(fields) == len({f['name'] for f in fields}), 'ambiguous schema')
    require(set(body) <= {f['name'] for f in fields}, 'undeclared field')
    require(all(f['name'] in body for f in fields if not f.get('optional')), 'missing required field')
    def get(role, kind):
        f = by_role[role]
        require(f['type'] == kind, 'unexpected field type')
        return body.get(f['name'])
    stamp = instant(get(TIME, 'Time'))
    start, end = map(instant, get(BASE+'nominal-averaging-window', 'TimeRange'))
    require(start < end == stamp, 'invalid nominal window')
    value, flag = get(AIR, 'Quantity'), get(BASE+'air-temperature-source-flag', 'Text')
    require(type(value) in (int, float) and isfinite(value), 'not a finite number')
    require(isinstance(flag, str), 'quality flag must be text')
    uid = get(BASE+'attributed-sensing-unit', 'Text')
    serial = None
    if uid is not None:
        systems = [s for s in cache['systems'] if s['uniqueId'] == uid]
        require(len(systems) == 1, 'unresolved or duplicate unit UID')
        ids = [t['value'] for t in systems[0]['identifiers'] if t['definition'] == SERIAL]
        require(len(ids) == 1 and bool(ids[0]), 'missing or ambiguous unit serial')
        serial = ids[0]
    return stamp, start, value, by_role[AIR]['uom']['code'], flag, serial


def expected(source, row):
    """Oracle: native columns and operator history; never the preassigned serial in readings."""
    f = row['source_fields']
    end = datetime.strptime(f['DatetimeStamp'], '%m/%d/%Y %H:%M').replace(tzinfo=EST)
    start = end - timedelta(minutes=int(f['Frequency']))
    units = [h['serial'] for h in source['unit_use_history']
             if h['station_code'] == f['StationCode'].strip() and h['model'] == 'EE181'
             and date.fromisoformat(h['first_date_of_use']) < start.date()
             and end.date() < date.fromisoformat(h.get('last_date_of_use_listed') or h['still_in_use_as_of'])]
    return end, start, float(f['ATemp']), 'Cel', f['F_ATemp'], units[0] if len(units) == 1 else None


def main():
    cache = json.loads((ROOT/'example.json').read_text())
    source = json.loads((ROOT.parent/'bennetts-point-ee181.json').read_text())
    expected_rows = [expected(source, row) for row in source['readings']]
    truth = {row[0]: row for row in expected_rows}
    rows = [read(cache, r) for r in reversed(cache['responses'])]
    require(len(rows) == len(truth) == 2 and {r[0]: r for r in rows} == truth, 'source round trip differs')
    for stamp, _, value, unit, flag, serial in sorted(rows):
        print(stamp.isoformat(), value, unit, repr(flag), serial)
    first, second = cache['responses']
    def changed(**patch):
        return {**first, 'body': {**first['body'], **patch}}
    wrong = read(cache, changed(probe=second['body']['probe']))
    require(wrong != truth[wrong[0]], 'probe swap undetected')
    altered = read(cache, changed(qc=source['excluded_example']['F_ATemp']))
    require(altered[4] == '<-3> [GPR] (CSM)' and altered != truth[altered[0]], 'flag lost')
    unknown = deepcopy(first); del unknown['body']['probe']
    require(read(cache, unknown)[2:] == (rows[-1][2], 'Cel', rows[-1][4], None), 'unresolved probe lost result')
    try:
        read(cache, changed(probe='urn:example:missing'))
    except ValueError:
        pass
    else:
        raise ValueError('dangling link accepted')
    missing = deepcopy(first); del missing['body']['qc']
    try:
        read(cache, missing)
    except ValueError:
        pass
    else:
        raise ValueError('absent flag silently accepted')
    print('PASS: two historical rows and five deliberately altered controls')


if __name__ == '__main__':
    main()
