#!/usr/bin/env python3
"""Verify registered project files and repository-local documentation links."""

import hashlib
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "Docs/ARTIFACTS.json"
REGISTER = ROOT / "Docs/ARTIFACT_REGISTER.md"
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def local_links(markdown):
    text = re.sub(r"```.*?```", "", markdown, flags=re.S)
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        parsed = urlsplit(target.strip().strip("<>"))
        if not parsed.scheme and not parsed.netloc and parsed.path:
            yield unquote(parsed.path)


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    check(manifest.get("schema_version") == 1, "Unsupported artifact manifest schema")
    date.fromisoformat(manifest["imported_on"])
    artifacts = manifest["artifacts"]
    check(bool(artifacts), "Artifact manifest is empty")
    keys, paths, directories = set(), set(), set()
    total_bytes = 0
    register_links = {
        (REGISTER.parent / link).resolve()
        for link in local_links(REGISTER.read_text(encoding="utf-8"))
    }

    for artifact in artifacts:
        key = artifact["key"]
        relative = Path(artifact["path"])
        check(key.startswith("glaux-artifact-"), f"Invalid repository artifact key: {key}")
        check(key not in keys, f"Duplicate artifact key: {key}")
        keys.add(key)
        check(not relative.is_absolute() and ".." not in relative.parts
              and relative.parts[0] == "Docs", f"Noncanonical artifact path: {relative}")
        path = (ROOT / relative).resolve()
        check(path.is_relative_to(ROOT), f"Artifact escapes repository: {relative}")
        check(path not in paths, f"Duplicate artifact path: {relative}")
        paths.add(path)
        directories.add(path.parent)
        date.fromisoformat(artifact["document_date"])
        date.fromisoformat(artifact["imported_on"])
        check(path in register_links, f"Artifact missing from readable register: {relative}")
        check(path.is_file(), f"Missing artifact: {relative}")
        if not path.is_file() or not path.is_relative_to(ROOT):
            continue
        content = path.read_bytes()
        actual = hashlib.sha256(content).hexdigest()
        total_bytes += len(content)
        check(len(content) == artifact["size_bytes"], f"Byte length mismatch: {relative}")
        check(actual == artifact["sha256"], f"SHA-256 mismatch: {relative}")
        check(actual == artifact["source_sha256"], f"Original source bytes changed: {relative}")
        for field in ("title", "role", "version", "source_location", "standing"):
            check(bool(artifact.get(field)), f"Missing {field}: {relative}")

    for directory in directories:
        for path in directory.iterdir():
            if path.suffix.lower() in {".docx", ".pdf", ".xlsx", ".zip"}:
                check(path.resolve() in paths, f"Unregistered project artifact: {path.relative_to(ROOT)}")

    documents = [ROOT / "README.md", ROOT / "AGENTS.md", *sorted((ROOT / "Docs").rglob("*.md"))]
    link_count = 0
    for document in documents:
        for target in local_links(document.read_text(encoding="utf-8")):
            link_count += 1
            resolved = (document.parent / target).resolve()
            check(resolved.is_relative_to(ROOT) and resolved.exists(),
                  f"Broken local link in {document.relative_to(ROOT)}: {target}")

    paper_check = ROOT / "scripts/verify-smart-citizen-paper.py"
    if paper_check.is_file():
        result = subprocess.run([sys.executable, str(paper_check)], capture_output=True, text=True)
        check(result.returncode == 0, result.stderr.strip() or "Smart Citizen paper verification failed")
        if result.returncode == 0:
            print(result.stdout.strip())

    if errors:
        for message in errors:
            print(f"ERROR: {message}", file=sys.stderr)
        return 1
    print(f"Verified {len(artifacts)} artifacts ({total_bytes:,} bytes) and "
          f"{link_count} local links across {len(documents)} documentation files.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyError, ValueError, TypeError, OSError) as exc:
        print(f"ERROR: Artifact verification could not complete: {exc}", file=sys.stderr)
        sys.exit(1)
