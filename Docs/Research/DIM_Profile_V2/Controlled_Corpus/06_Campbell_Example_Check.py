#!/usr/bin/env python3
"""Offline checks of Campbell's published CR1000X status example; not telemetry.

Usage: python 06_Campbell_Example_Check.py path/to/status_example.json
Source: https://help.campbellsci.com/datalogger-api/mqtt/status.html
Section: CR1000X Example; footer observed 2026-09-21 (ced60094).
Audit access: 2026-10-30, America/New_York.

The audit used a whitespace-reformatted transcription of the complete example
returned by the browser, not downloaded original bytes. The source JSON is not
bundled. Obtain the example separately; preserve names, order, types and values.
This original checker does not contact a logger, execute CRBasic, interpret
weather observations, or establish a ClimaVue installation or Profile mapping.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def check(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    document = json.loads(raw)
    require(document.get("type") == "Feature", "Expected the published Feature example.")
    props = document["properties"]
    names = props["observationNames"]
    require(isinstance(names, list) and all(isinstance(x, str) for x in names),
            "Expected ordered field names.")
    require(len(names) == len(set(names)), "Duplicate names would make pairing ambiguous.")
    observations = props["observations"]
    require(isinstance(observations, dict) and bool(observations), "No example rows.")
    require(len(names) == 31 and len(observations) == 1, "Not the audited 31-field example.")
    checks = []
    for timestamp, values in observations.items():
        require(isinstance(values, list) and len(names) == len(values),
                "A length mismatch would silently lose values during pairing.")
        require(timestamp.endswith("Z"), "Audited example uses an explicit UTC suffix.")
        parsed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        paired = dict(zip(names, values))
        require(paired["Battery"] == 13.2368, "Unexpected illustrative supply voltage.")
        require(paired["LithiumBattery"] == 3.70477, "Unexpected backup-battery example.")
        require(paired["PanelTemp"] == 25.91098, "Unexpected panel-temperature example.")
        require(type(paired["SW12Volts(1)"]) is bool and
                type(paired["SW12Volts(2)"]) is bool, "Switched-output states must remain Boolean.")
        require(isinstance(paired["CommsMemFree"], str), "Memory summary must remain text.")
        counts = Counter("boolean" if type(v) is bool else
                         "number" if isinstance(v, (int, float)) else
                         "string" if isinstance(v, str) else "other" for v in values)
        require(counts == {"number": 18, "string": 3, "boolean": 10},
                "Unexpected type distribution in the published example.")
        checks.append({"example_timestamp": timestamp, "parsed_utc": parsed.isoformat(),
                       "field_count": len(names), "value_count": len(values),
                       "types": dict(counts),
                       "illustrative_values": {key: paired[key] for key in
                           ("Battery", "LithiumBattery", "PanelTemp", "SW12Volts(1)")}})
    canonical = json.dumps(document, sort_keys=True, separators=(",", ":"),
                           ensure_ascii=False).encode("utf-8")
    return {"evidence": "PRIMARY_PUBLISHED_EXAMPLE; locally transcribed",
            "input_sha256": hashlib.sha256(raw).hexdigest(),
            "canonical_json_sha256": hashlib.sha256(canonical).hexdigest(),
            "checks": checks,
            "limits": "Format/types/positional pairing only; no original-byte or hardware verification."}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("example", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(check(args.example), indent=2))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f"Example check failed: {exc}\n")


if __name__ == "__main__":
    main()
