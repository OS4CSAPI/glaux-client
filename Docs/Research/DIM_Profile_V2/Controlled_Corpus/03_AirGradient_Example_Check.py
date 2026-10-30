"""Offline format checks of published AirGradient README examples, not device telemetry.
Source: Open-Air-Foundation/firmware-openair-max, commit
84e479a415d81151e7a81aea9a2f7449a15e98cc, README.md, two Example Payload Breakdown sections.
https://github.com/Open-Air-Foundation/firmware-openair-max/blob/84e479a415d81151e7a81aea9a2f7449a15e98cc/README.md
Examples transcribed from the GitHub connector's inspected text. No original file bytes downloaded.
Example material: AirGradient, CC BY-SA 4.0, repository LICENSE.
License: https://creativecommons.org/licenses/by-sa/4.0/
This checker and its comment-stripped derivative: CC BY-SA 4.0; no source values corrected.
Run with Python 3.8+; standard library only. Prints results; no network or file writes.
"""
import json, re, hashlib, datetime
CELLULAR = '''180,452,285,751,163,277,295,34012,20429,3225,-69,1124,14,580981,581369,581319,582400,5796,450,286,751,170,283,300,34140,20589,3272,-69,1124,15,581000,581400,581388,582456,5795,446,286,753,167,287,302,34139,20577,3237,-69,1124,15,581013,581438,581350,582494,5796'''
WIFI = '''{
  "rco2": 452, // CO2
  "atmp": 28.5, // Temperature
  "rhum": 75.1, // Humidity
  "pm01": 16.3, // PM1.0
  "pm25": 27.7, // PM2.5
  "pm10": 29.5, // PM10
  "tvocRaw": 34012, // TVOC Raw
  "noxRaw": 20429, // NOx Raw
  "pm003Count": 3225, // PM 0.3 Particle Count
  "wifi": -69, // Wifi Signal
  "volt": 11.24, // Battery Volt
  "light": 1.4, // Solar Panel Volt
  "measure0": 580.981, // O3 WE
  "measure1": 581.369, // O3 AE
  "measure2": 581.319, // NO2 WE
  "measure3": 582.400, // NO2 AE
  "measure4": 579.6 // AFE Temperature
}'''
values = [int(x) for x in CELLULAR.split(',')]
assert len(values) == 52 and (len(values) - 1) % 17 == 0
rows = [values[i:i+17] for i in range(1, len(values), 17)]
try:
    json.loads(WIFI)
    strict_result = 'unexpected success'
except json.JSONDecodeError as exc:
    strict_result = f'REJECTED: {exc.msg} (line {exc.lineno}, column {exc.colno})'
# Only these inspected examples are supported; this is not a general JSON-comment parser.
derived = re.sub(r'//[^\n]*', '', WIFI)
parsed = json.loads(derived)
assert len(parsed) == 17
assert rows[0][1]/10 == parsed['atmp']
assert rows[0][10]/100 == parsed['volt']
assert rows[0][11]/100 != parsed['light']
result = {
 'source_commit':'84e479a415d81151e7a81aea9a2f7449a15e98cc',
 'source_blob_from_connector':'1322b58c7ed70ec0f4900bd557ec09fa65e03732',
 'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'evidence':'PRIMARY_PUBLISHED_EXAMPLE; manually transcribed inspected excerpt',
 'cellular':{'integer_tokens':len(values),'interval_seconds':values[0], 'groups':len(rows),'values_per_group':17,'first_temperature_C':rows[0][1]/10,'first_battery_V':rows[0][10]/100,'first_panel_V':rows[0][11]/100},
 'wifi':{'strict_json':strict_result,'comment_stripped_key_count':len(parsed),'battery_V':parsed['volt'],'panel_V':parsed['light'],'derivative_label':'SYNTHETIC_OR_DERIVED; comments removed only'},
 'panel_comparison':'Examples differ: cellular 14/100 = 0.14 V; Wi-Fi light = 1.4 V. They are not established as one synchronized measurement; neither was repaired.',
 'limits':'No original-file byte checksum, firmware execution, device measurement, calibration verification, timestamp reconstruction, API interoperability or CSAPI transformation.',
 'excerpt_checksums':{'scope':'SHA-256 of UTF-8 strings above, not the upstream file', 'cellular':hashlib.sha256(CELLULAR.encode()).hexdigest(),'wifi_annotated':hashlib.sha256(WIFI.encode()).hexdigest()}
}
print(json.dumps(result,indent=2))
