#!/usr/bin/env python3
"""Check the maintained research paper and reject stale derived Word editions."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from xml.etree import ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT / "Docs/Research/Studies/Smart_Citizen"
MANIFEST = STUDY / "MANUSCRIPT_MANIFEST.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(value, message):
    if not value:
        raise ValueError(message)


def resolve(relative):
    path = (ROOT / relative).resolve()
    require(path.is_relative_to(ROOT) and path.is_file(), f"Missing or unsafe paper path: {relative}")
    return path


def verify(refresh=False):
    manifest = json.loads(MANIFEST.read_text())
    require(manifest["schemaVersion"] == 1, "Unsupported paper manifest")
    source = resolve(manifest["canonicalSource"])
    rendered = resolve(manifest["renderedEdition"])
    text = source.read_text()
    body, references = text.split("\n## References\n", 1)
    require(f'Working paper version {manifest["version"]}' in body, "Manuscript version disagrees with manifest")
    records = json.loads((STUDY / "REFERENCES.json").read_text())["entries"]
    labels = [record["citation"] for record in records]
    require(len(labels) == len(set(labels)), "Duplicate citation label")
    expected_refs = "\n\n".join(record["referenceMarkdown"] for record in records)
    require(references.strip() == expected_refs, "Manuscript references differ from REFERENCES.json")

    # A following year within the same parenthesis may reuse the previous author.
    by_author = {}
    for record in records:
        author = record["citation"].rsplit(" ", 1)[0]
        by_author.setdefault(author, {})[record["yearLabel"]] = record["citation"]
    used = set()
    year_pattern = r"(?:\d{4}[a-z]?|n\.d\.(?:-[a-z])?)"
    for parenthesis in re.findall(r"\(([^()]*)\)", body):
        current_author = None
        for part in parenthesis.split(";"):
            part = part.strip()
            for author in sorted(by_author, key=len, reverse=True):
                if part.startswith(author + " "):
                    current_author = author
                    part = part[len(author):].strip()
                    break
            match = re.match(year_pattern + r"(?=,|\s|$)", part)
            if match and current_author:
                year = match.group()
                require(year in by_author[current_author], f"Unknown citation: {current_author} {year}")
                used.add(by_author[current_author][year])
    require(used == set(labels), f"Uncited references: {sorted(set(labels) - used)}")
    require(not re.search(r"turn\d+(?:view|search)\d+|genui|TODO|TBD", text), "Unresolved drafting or tool-citation token in manuscript")

    listings = re.findall(r"```json\n(.*?)\n```", text, re.S)
    require(len(listings) == len(manifest["listings"]), "Listing count differs from manifest")
    for body_json, listing in zip(listings, manifest["listings"]):
        companion = resolve(listing["path"])
        require(json.loads(body_json) == json.loads(companion.read_text()), f"Listing differs from {companion.name}")
    evidence = json.loads(resolve(manifest["listings"][0]["evidenceFile"]).read_text())
    record = next(r for r in evidence["records"] if r["id"] == manifest["listings"][0]["evidenceRecord"])
    prefix = manifest["listings"][0]["sourcePointer"]
    native = json.loads(listings[0])
    for key, value in native.items():
        require(record["excerpt"]["values"][prefix + "/" + key] == value, f"Native listing drift: {key}")

    images = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", body)
    required_inputs = {str(source.relative_to(ROOT)), "scripts/build-smart-citizen-paper.py"}
    for image in images:
        path = (source.parent / image).resolve()
        require(path.is_relative_to(ROOT) and path.is_file(), f"Missing manuscript figure: {image}")
        required_inputs.add(str(path.relative_to(ROOT)))
    with zipfile.ZipFile(rendered) as archive:
        core = ET.fromstring(archive.read("docProps/core.xml"))
        provenance = core.find("{http://purl.org/dc/elements/1.1/}description")
        require(provenance is not None and provenance.text, "DOCX lacks build-input fingerprints")
        provenance_record = json.loads(provenance.text)
        require(provenance_record.get("format") == "glaux-paper-inputs-v1", "Unexpected DOCX provenance format")
        input_hashes = {relative: digest(resolve(relative)) for relative in sorted(required_inputs)}
        input_record = json.dumps(input_hashes, sort_keys=True, separators=(",", ":")).encode("utf-8")
        require(hashlib.sha256(input_record).hexdigest() == provenance_record.get("sha256"),
                "Stale Word edition: manuscript, figure inventory/content, or builder differs from its build inputs")

    require(len(manifest["files"]) == len({item["path"] for item in manifest["files"]}), "Duplicate publication file")
    for item in manifest["files"]:
        path = resolve(item["path"])
        actual_hash, length = digest(path), path.stat().st_size
        if refresh:
            item.update(sha256=actual_hash, sizeBytes=length)
        else:
            require(item["sha256"] == actual_hash and item["sizeBytes"] == length, f"Paper publication fingerprint mismatch: {item['path']}")
    if refresh:
        MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(f"Verified Smart Citizen paper {manifest['version']}: {len(records)} cited references, "
          f"{len(images)} figures, {len(listings)} listings, current Word inputs, and {len(manifest['files'])} publication files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="Refresh file fingerprints only after all content and Word-input checks pass")
    args = parser.parse_args()
    try:
        verify(args.refresh)
    except (OSError, ValueError, KeyError, StopIteration, zipfile.BadZipFile, ET.ParseError) as error:
        print(f"ERROR: Smart Citizen paper verification failed: {error}", file=sys.stderr)
        sys.exit(1)
