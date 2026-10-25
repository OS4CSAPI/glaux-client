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


def visible_prose(text):
    """Remove Markdown destinations/markup without losing displayed link words."""
    # The manuscript uses inline links, with at most one parenthesized URL part.
    text = re.sub(r"\[([^\]]+)\]\((?:[^()]|\([^()]*\))*\)", r"\1", text)
    text = re.sub(r"<https?://[^>]+>", "URL", text)
    # A bare URL's final full stop belongs to the surrounding prose.
    text = re.sub(r"https?://[^\s<>]+", lambda m: "URL" + ("." if m[0].endswith(".") else ""), text)
    text = re.sub(r"`+[^`]*`+", "CODE", text)
    return re.sub(r"[*_~]", "", text)


def sentence_count(text, citation_authors=()):
    """Count sentences in the paper's controlled English prose, not its citations.

    This is a deterministic editorial check, not a general NLP parser. Known
    author-date parentheses, Markdown destinations, code spans, decimals, and
    common abbreviations cannot create false sentence boundaries. An unmatched
    final prose fragment counts as one segment; grammar remains a human review.
    """
    text = visible_prose(text)
    authors = tuple(sorted(set(citation_authors), key=len, reverse=True))
    year = r"(?:\d{4}[a-z]?|n\.d\.(?:-[a-z])?)(?=,|;|\s|$)"

    def citation(match):
        inner = match[0][1:-1].strip()
        for author in authors:
            if inner.startswith(author + " ") and re.match(year, inner[len(author):].strip()):
                return "CITATION"
        # Also support narrative citations such as Parello et al. (2014).
        if re.fullmatch(r"(?:\d{4}[a-z]?|n\.d\.(?:-[a-z])?)", inner):
            return "CITATION"
        return match[0]

    text = re.sub(r"\([^()]*\)", citation, text)
    protected_dot = "\ue000"

    def protect(match):
        return match[0].replace(".", protected_dot)

    # Decimal values, versions, numbered sections, and times are not sentences.
    text = re.sub(r"(?<=\d)\.(?=\d)", protected_dot, text)
    text = re.sub(r"\b(?:e\.g\.|i\.e\.|n\.d\.(?:-[a-z])?)", protect, text, flags=re.I)
    text = re.sub(r"\b(?:Mr|Mrs|Ms|Dr|Prof|Sr|Jr|St|Mt)\.", protect, text)
    text = re.sub(r"\b(?:sec|secs|fig|figs|eq|eqs|ch|chs|vol|vols|no|nos|pp|p)\.(?=\s+\d)",
                  protect, text, flags=re.I)
    # Internal abbreviation dots are always protected. The final dot can end a
    # sentence when followed by an uppercase word or the end of the paragraph.
    for pattern in (r"\bet\s+al\.", r"\b(?:a\.m\.|p\.m\.)", r"\betc\."):
        def abbreviation(match):
            tail = text[match.end():].lstrip(' \t\n\"\'”’)]}')
            replacement = protect(match)
            continuation = re.match(r"(?:CITATION|UTC|GMT|EST|EDT|CST|CDT|MST|MDT|PST|PDT)\b", tail)
            if not tail or (re.match(r"[A-Z]", tail) and not continuation):
                replacement = replacement[:-1] + "."
            return replacement
        text = re.sub(pattern, abbreviation, text, flags=re.I)
    # Initialisms and personal initials (U.S., J. Smith) are common inside prose.
    text = re.sub(r"\b(?:[A-Z]\.){2,}", protect, text)
    text = re.sub(r"\b[A-Z]\.(?=\s+[A-Z][a-z])", protect, text)
    pieces = re.split(r"[.!?]+(?:[\"'”’»\)\]\}]+)?(?=\s|$)", text.strip())
    return sum(bool(re.search(r"[\w\d]", piece)) for piece in pieces)


def prose_paragraphs(text):
    """Yield narrative blocks with location, excluding the paper's nonprose.

    Scope begins at the first level-two heading and ends at References. Blank
    lines delimit paragraphs; soft-wrapped lines are joined. Caption titles are
    excluded, but any explanatory text after the bold title is a prose block.
    Numbered question items, metadata, tables, images, and code are excluded.
    """
    paragraphs, pending = [], []
    sections = {}
    active, fence, first_line = False, None, 0

    def flush():
        nonlocal pending
        if not pending:
            return
        paragraph = " ".join(line.strip() for line in pending)
        pending = []
        if re.match(r"\*\*Keywords:\*\*|Keywords:", paragraph, re.I):
            return
        kind = "body"
        caption = re.match(r"^\*\*(?:Figure|Table|Listing)\s+\d+\.[^*]+\*\*\s*", paragraph)
        if caption:
            paragraph = paragraph[caption.end():].strip()
            kind = "caption"
        elif re.match(r"^(?:Figure|Table|Listing)\s+\d+\.", paragraph):
            raise ValueError(f"Caption at line {first_line} needs the manuscript's bold label/title format for sentence auditing")
        if paragraph:
            paragraphs.append({"line": first_line,
                               "section": " > ".join(sections[level] for level in sorted(sections)),
                               "kind": kind, "text": paragraph})

    skip_question = False
    for line_number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        fence_match = re.match(r"^(`{3,}|~{3,})", stripped)
        if fence:
            if fence_match and fence_match[1][0] == fence[0] and len(fence_match[1]) >= len(fence):
                fence = None
            continue
        if fence_match:
            flush()
            fence = fence_match[1]
            continue
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", stripped)
        if heading:
            flush()
            skip_question = False
            level, name = len(heading[1]), heading[2]
            if level == 2 and name.casefold() == "references":
                break
            if level >= 2:
                active = True
                sections = {key: value for key, value in sections.items() if key < level}
                sections[level] = name
            continue
        if not active:
            continue
        if not stripped:
            flush()
            skip_question = False
            continue
        if stripped.startswith("|") or re.fullmatch(r"!\[[^\]]*\]\([^)]+\)", stripped):
            flush()
            continue
        if re.match(r"^\d+[.)]\s+", stripped):
            flush()
            require("research questions" in " > ".join(sections.values()).casefold(),
                    f"Numbered prose at line {line_number} needs an explicit audit classification")
            skip_question = True
            continue
        if skip_question:
            continue
        if not pending:
            first_line = line_number
        pending.append(line)
    flush()
    require(fence is None, "Unclosed code fence prevents a reliable paragraph audit")
    return paragraphs


def analyze_paragraphs(text, citation_authors=()):
    paragraphs = prose_paragraphs(text)
    for paragraph in paragraphs:
        paragraph["sentences"] = sentence_count(paragraph["text"], citation_authors)
        opening = " ".join(visible_prose(paragraph["text"]).split()[:12])
        paragraph["opening"] = opening + ("…" if len(paragraph["text"].split()) > 12 else "")
    return paragraphs


def check_paragraph_policy(paragraphs, policy):
    require(isinstance(policy, dict), "paragraphPolicy must be an object")
    minimum, maximum = policy.get("minSentences"), policy.get("maxSentences")
    require(type(minimum) is int and type(maximum) is int and 1 <= minimum <= maximum,
            "paragraphPolicy requires integer minSentences/maxSentences with 1 <= min <= max")
    require(paragraphs, "No narrative paragraphs found for paragraphPolicy")
    violations = [p for p in paragraphs if not minimum <= p["sentences"] <= maximum]
    if violations:
        detail = "\n".join(f"  line {p['line']} | {p['section']} | {p['kind']} | "
                           f"{p['sentences']} sentences | {p['opening']}" for p in violations)
        raise ValueError(f"Paragraph policy requires {minimum}–{maximum} sentences; "
                         f"{len(violations)} of {len(paragraphs)} prose paragraphs fail:\n{detail}")


def paragraph_report():
    """Report source counts before DOCX rebuilding; never refresh fingerprints."""
    manifest = json.loads(MANIFEST.read_text())
    text = resolve(manifest["canonicalSource"]).read_text()
    records = json.loads((STUDY / "REFERENCES.json").read_text())["entries"]
    authors = [record["citation"].rsplit(" ", 1)[0] for record in records]
    paragraphs = analyze_paragraphs(text, authors)
    for paragraph in paragraphs:
        print(f"line {paragraph['line']:>3} | {paragraph['sentences']} sentences | "
              f"{paragraph['section']} | {paragraph['kind']} | {paragraph['opening']}")
    distribution = {count: sum(p["sentences"] == count for p in paragraphs)
                    for count in sorted({p["sentences"] for p in paragraphs})}
    print(f"Narrative paragraphs: {len(paragraphs)}; sentence-count distribution: {distribution}")
    if "paragraphPolicy" in manifest:
        check_paragraph_policy(paragraphs, manifest["paragraphPolicy"])
        print("Paragraph policy passed.")
    else:
        print("Counts only: paragraphPolicy is absent, so no sentence limits are enforced.")


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
    if "paragraphPolicy" in manifest:
        check_paragraph_policy(analyze_paragraphs(body, by_author), manifest["paragraphPolicy"])
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
    listing_evidence = manifest["listings"][0]
    evidence = json.loads(resolve(listing_evidence["evidenceFile"]).read_text())
    prefix = listing_evidence["sourcePointer"]
    native = json.loads(listings[0])
    if listing_evidence.get("evidenceRecord"):
        record = next(r for r in evidence["records"] if r["id"] == listing_evidence["evidenceRecord"])
        for key, value in native.items():
            require(record["excerpt"]["values"][prefix + "/" + key] == value, f"Native listing drift: {key}")
    else:
        node = evidence
        for part in [p for p in prefix.split("/") if p]:
            node = node[int(part)] if isinstance(node, list) else node[part]
        for key, value in native.items():
            require(node[key] == value, f"Native listing drift: {key}")

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
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--refresh", action="store_true", help="Refresh file fingerprints only after all content and Word-input checks pass")
    mode.add_argument("--paragraph-report", action="store_true", help="Report prose sentence counts without requiring a current Word edition")
    args = parser.parse_args()
    try:
        if args.paragraph_report:
            paragraph_report()
        else:
            verify(args.refresh)
    except (OSError, ValueError, KeyError, StopIteration, zipfile.BadZipFile, ET.ParseError) as error:
        print(f"ERROR: Smart Citizen paper verification failed: {error}", file=sys.stderr)
        sys.exit(1)
