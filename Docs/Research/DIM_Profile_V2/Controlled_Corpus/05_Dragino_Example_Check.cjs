/* Offline documentary-example check; no device contact, networking or CSAPI mapping.
 * Usage: TZ=UTC node 05_Dragino_Example_Check.cjs /path/to/S31-LB_v1.3_TTN_decoder.txt
 * Obtain the vendor file separately from its pinned source. It is NOT bundled here.
 * Source: dragino/dragino-end-node-decoder, commit 635417693adb215b32ac367c8e8909d9d609a120
 * Path: S31-LB&S31B-LB/S31-LB_v1.3_TTN_decoder.txt
 * Blob: 59af776a4b7ce287dc4c3030763e215b31f645f8
 * The 88-byte numeric example below is transcribed from Dragino's manual,
 * section 2.5.4, accessed 30 October 2026 (America/New_York):
 * https://wiki.dragino.com/docs/LoRaWAN-End-Node/temperature-humidity-sensors/s31-lb/
 * All other payloads are explicitly SYNTHETIC_OR_DERIVED test inputs, NOT telemetry.
 * Original audit harness; no change to the vendor decoder. Standard Node.js only.
 */
'use strict';
const fs = require('node:fs');
const vm = require('node:vm');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const expectedBlob = '59af776a4b7ce287dc4c3030763e215b31f645f8';
const sourceUrl = 'https://github.com/dragino/dragino-end-node-decoder/blob/635417693adb215b32ac367c8e8909d9d609a120/S31-LB%26S31B-LB/S31-LB_v1.3_TTN_decoder.txt';
const exampleHex = `00 00 02 36 01 10 40 64 6D 84 E1 00 00 02 37 01 10 40 64 6D 84 F8 00 00 02 37 01 0F 40 64 6D 85 04 00 00 02 3A 01 0F 40 64 6D 85 18 00 00 02 3C 01 0F 40 64 6D 85 36 00 00 02 3D 01 0E 40 64 6D 85 3F 00 00 02 3F 01 0E 40 64 6D 85 60 00 00 02 40 01 0E 40 64 6D 85 6A`;
function bytes(hex) {
  const compact = hex.replace(/\s+/g, '');
  if (!/^(?:[0-9a-f]{2})+$/i.test(compact)) throw new Error('Invalid hex input');
  return Buffer.from(compact, 'hex');
}
try {
  if (!process.argv[2]) throw new Error('Supply a path to the separately obtained pinned decoder');
  const source = fs.readFileSync(process.argv[2]);
  const gitBlob = crypto.createHash('sha1').update(`blob ${source.length}\0`).update(source).digest('hex');
  assert.equal(gitBlob, expectedBlob, 'Decoder bytes do not match the audited source');
  function decode(payload, port) {
    // Fresh context prevents leaked globals from one example affecting another.
    // The already-reviewed vendor source has no network, file, or process access.
    const ctx = vm.createContext({ input: { bytes: Array.from(payload), fPort: port } });
    vm.runInContext(source.toString('utf8'), ctx, { timeout: 1000 });
    return JSON.parse(vm.runInContext('JSON.stringify(decodeUplink(input))', ctx, { timeout: 1000 }));
  }
  const original = bytes(exampleHex);
  assert.equal(original.length, 88);
  const records = [];
  for (let i = 0; i < original.length; i += 11) {
    const entry = original.subarray(i, i + 11);
    const epochSeconds = entry.readUInt32BE(7);
    records.push({ humidity: entry.readUInt16BE(2) / 10,
      temperature: entry.readInt16BE(4) / 10, flagHex: entry[6].toString(16),
      epochSeconds, utc: new Date(epochSeconds * 1000).toISOString() });
  }
  assert.equal(records.length, 8);
  assert.equal(records[0].humidity, 56.6);
  assert.equal(records[0].temperature, 27.2);
  assert.equal(records[0].epochSeconds, 1684899041);
  assert.equal(records[7].epochSeconds - records[0].epochSeconds, 137);
  const nativeHistory = decode(original, 3);
  assert.equal(typeof nativeHistory.data.DATALOG, 'string');
  assert.equal((nativeHistory.data.DATALOG.match(/\[/g) || []).length, 8);
  assert.ok(nativeHistory.data.DATALOG.startsWith('[56.6,27.2,Low,False,'));
  // Tests constructed from documented scalar values; NOT manufacturer full messages.
  const measurement = decode(bytes('0B45646D84E100FF3F0197'), 2);
  assert.equal(measurement.data.BatV, 2.885);
  assert.equal(measurement.data.TempC_SHT31, -19.3);
  assert.equal(measurement.data.Hum_SHT31, 40.7);
  assert.equal(measurement.data.Door_status, 'OPEN');
  const settings = decode(bytes('0B45646D84E17C001E4600'), 2);
  assert.equal(settings.data.SHTEMP_MAX, 30);
  assert.equal(settings.data.SHHUM_MIN, 70);
  const status = decode(bytes('0A010001000B45'), 5);
  assert.equal(status.data.FIRMWARE_VERSION, '1.0.0');
  assert.equal(status.data.FREQUENCY_BAND, 'EU868');
  // Boundary condition specified by the manual; zero bytes are constructed here.
  const noData = decode(Buffer.alloc(11), 3);
  assert.ok(noData.data.DATALOG.startsWith('[0,0,Low,False,'));
  const unsupported = decode(Buffer.from([0]), 99);
  assert.ok(unsupported.errors);
  assert.equal(0x0197, 407);
  assert.equal(0x7c >> 2, 31); // decimal 31, hexadecimal 0x1f, NOT hexadecimal 0x31
  console.log(JSON.stringify({
    standing: 'OFFLINE_DOCUMENTARY_AND_SYNTHETIC_CHECKS_ONLY',
    sourceUrl, gitBlob, sourceByteCount: source.length,
    sourceSha256: crypto.createHash('sha256').update(source).digest('hex'),
    nodeVersion: process.version,
    runtimeTimezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
    originalExample: { evidence: 'PRIMARY_PUBLISHED_EXAMPLE', byteCount: original.length,
      sha256OfTranscribedPayloadBytes: crypto.createHash('sha256').update(original).digest('hex'),
      independentlyDerivedRecords: records, vendorOutput: nativeHistory },
    syntheticTests: { evidence: 'SYNTHETIC_OR_DERIVED', measurement, settings, status, noData, unsupported },
    checks: 'All assertions passed; no hardware, calibration, firmware, or Profile conformance proven'
  }, null, 2));
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
}
