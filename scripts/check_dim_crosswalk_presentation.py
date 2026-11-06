#!/usr/bin/env python3
"""Read-only Step05 presentation contract checker for the approved donor→DIM sample.

Usage:
  python3 scripts/check_dim_crosswalk_presentation.py

Tests exact original sample geometry, CSV/JSON/ledger alignment, evidence pointers
and preliminary donor-roster separation. NEVER produces an XLSX, edits source,
confirms original publisher clauses, or ranks donor standards. Step06 will make
the actual workbook and must satisfy these invariants.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
from collections import Counter
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk"
CONFIG = CONTROL / "Step05_Approved_Master_Table_Presentation_Contract_v0.1_05NOV2026.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read_source(relative: str) -> tuple[Path, bytes]:
    destination = (CONTROL / relative).resolve()
    require(destination.is_relative_to(ROOT), "Unsafe path beyond repository: " + relative)
    require(destination.is_file(), "Source file does not exist: " + relative)
    return destination, destination.read_bytes()


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def read_csv_bytes(data: bytes) -> list[list[str]]:
    return list(csv.reader(io.StringIO(data.decode("utf-8-sig"), newline="")))


def validate() -> dict[str, object]:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    require(cfg["status"] == "STEP05_PRESENTATION_CONTRACT_ONLY_NOT_MASTER_WORKBOOK", "Not Step05 contract")
    require(cfg["master"]["donorColumnOrientation"] == "HORIZONTAL_LEFT_TO_RIGHT_FIXED", "Donor orientation changed")
    require(cfg["master"]["dimAlwaysFarRight"] is True, "DIM is no longer far-right")
    require(cfg["master"]["explicitLeftmostIdColumn"] is False, "Unexpected ID column on visible master")
    require(cfg["master"]["firstRowIsDonorHeader"] is True, "First row is not donor headers")
    require(cfg["workbook"]["iterationOfFirstCreation"] == "STEP06_ONLY", "Premature spreadsheet generation")
    require(cfg["workbook"]["freeze"]["dimRightEdgePinned"] is False, "Impossible right-edge freeze claim")
    require(cfg["workbook"]["filtering"]["master"] is False, "Merged sections cannot share ordinary filter table")
    require(cfg["master"]["sections"]["fullWidthAcrossDonorsAndDim"], "Section divider must span all columns")
    require(cfg["master"]["donorCells"]["useBlankCellNotNAOrDash"], "Unsupported matches must stay genuinely blank")
    require(cfg["dataContract"]["defaultSourceVerification"] == "PRIOR_SOURCE_EXTRACT_ONLY", "Do not auto-verify sources")

    sources = cfg["inputs"]
    data_by_kind: dict[str, bytes] = {}
    for source_key, blob_key in [
        ("canonicalSampleJson", "sampleJsonGitBlob"),
        ("baselineCsv", "baselineCsvGitBlob"),
        ("evidenceLedger", "evidenceLedgerBlob"),
        ("donorRoster", "donorRosterBlob"),
    ]:
        _, raw = read_source(sources[source_key])
        require(git_blob_sha(raw) == sources[blob_key], f"Frozen input changed: {source_key}")
        data_by_kind[source_key] = raw

    sample = json.loads(data_by_kind["canonicalSampleJson"])
    order = sample["order"]
    require(order == cfg["master"]["sampleOrderKeys"], "Donor order differs from approved sample")
    require(len(order) == cfg["master"]["sampleColumnCount"]["donors"] == 7, "Unexpected donor count")
    require(len(order) + 1 == cfg["master"]["sampleColumnCount"]["totalWithDim"], "DIM not last column")
    require(len(set(order)) == len(order), "Duplicate donor header")

    table = read_csv_bytes(data_by_kind["baselineCsv"])
    header = [sample["donors"][key]["name"] for key in order] + [cfg["master"]["dimensionLastColumn"]]
    require(table[0] == header, "Header differs from approved donor order/DIM")
    require(all(len(row) == len(header) for row in table), "CSV width/orientation changed")

    groups: list[str] = []
    dim_rows: list[str] = []
    expected_rows = [header]
    observed_fits = Counter()
    all_matches: dict[tuple[str, str, str], tuple[str, str]] = {}
    current_group = ""
    for entry in sample["rows"]:
        if "g" in entry:
            require(entry["g"] and entry.get("desc"), "Missing section header or description")
            groups.append(entry["g"])
            current_group = entry["g"]
            expected_rows.append([entry["g"]] + [""] * len(order))
            continue

        require(current_group, "Concept row outside section")
        dim = entry["dim"]
        require(dim and dim not in dim_rows, "DIM row label missing or duplicated in sample: " + dim)
        dim_rows.append(dim)
        cells = []
        for donor_key in order:
            cell = entry["d"].get(donor_key)
            if cell is None:
                cells.append("")
                continue
            require(cell["term"] and cell["fit"] and cell["clause"], "Incomplete cell for " + dim)
            require(cell["fit"] in cfg["master"]["donorCells"]["fitSymbol"], "Unknown sample relation")
            display = cfg["master"]["donorCells"]["fitSymbol"][cell["fit"]] + cell["term"]
            cells.append(display)
            observed_fits[cell["fit"]] += 1
            ekey = (current_group, dim, sample["donors"][donor_key]["name"])
            require(ekey not in all_matches, "Duplicate source cell key")
            all_matches[ekey] = (cell["term"], cell["fit"])
        expected_rows.append(cells + [dim])
    require(expected_rows == table, "JSON row/section order or native term values differ from CSV")
    require(len(groups) == cfg["validation"]["sectionDividerCount"] == 5, "Wrong divider count")
    require(len(dim_rows) == cfg["validation"]["sampleRowCount"] == 22, "Wrong sample row count")
    require(len(all_matches) == cfg["validation"]["sampleEvidenceCellCount"] == 51, "Wrong source-claim count")
    require(observed_fits == Counter({"DIRECT": 16, "PARTIAL": 27, "RELATED": 7, "CONDITIONAL": 1}),
            "Source correspondence count changed")
    require(len(table) == 1 + len(groups) + len(dim_rows), "Unexpected blank/phantom CSV rows")

    evidence_rows = read_csv_bytes(data_by_kind["evidenceLedger"])
    evidence_cols = evidence_rows.pop(0)
    expect_evidence = [
        "Section", "Proposed DIM element", "Donor", "Donor-native term",
        "Alignment", "Original source locator", "Publisher source URL",
        "Why not assume full equivalence",
    ]
    require(evidence_cols == expect_evidence, "Evidence ledger columns unexpectedly changed")
    observed_ledger: set[tuple[str, str, str]] = set()
    for row in evidence_rows:
        require(len(row) == len(expect_evidence), "Missing evidence field")
        section, dim, donor, native, alignment, locator, url, caution = row
        key = (section, dim, donor)
        require(key not in observed_ledger, "Duplicate evidence for " + str(key))
        observed_ledger.add(key)
        require(key in all_matches, "Orphan evidence record " + str(key))
        require((native, alignment) == all_matches[key], "Evidence term/fit mismatch " + str(key))
        require(locator.strip() and url.startswith("https://") and caution.strip(),
                "Missing locator/URL/limitation " + str(key))
    require(observed_ledger == set(all_matches), "Missing evidence records for displayed cells")

    # The owner actually approved a GitHub-visible TABLE, not just the hidden
    # JSON/CSV. Verify its full-width group rows and DIM-last header too.
    markdown_path = sources["canonicalSampleJson"].removesuffix(".json") + ".md"
    _, markdown_bytes = read_source(markdown_path)
    markdown = markdown_bytes.decode("utf-8")
    table_start = markdown.find("<table>")
    table_end = markdown.find("</table>", table_start)
    require(table_start >= 0 and table_end > table_start, "Approved Markdown table missing")
    html_table = markdown[table_start:table_end]
    require(html_table.count("<th colspan=\"8\">") == len(groups),
            "GitHub sample divider rows no longer span all eight columns")
    require(html_table.count("<tr>") == len(expected_rows),
            "GitHub sample table gained or lost a row")
    require(html_table.find("PROPOSED DIM ELEMENT") > html_table.find(sample["donors"][order[-1]]["name"]),
            "GitHub sample no longer displays DIM after the last donor")
    for group in groups:
        require(escape(group) in html_table, "GitHub sample is missing section " + group)

    roster = json.loads(data_by_kind["donorRoster"])
    require(len(roster["columns"]) == 46, "Step04 potential roster changed")
    require(all(c["rank"] is None for c in roster["columns"]), "Cannot claim final rank before mappings")
    require(cfg["dataContract"]["candidateColumnCountsForContext"]["automaticallyIncluded"] == 0,
            "Provisional donor candidates were automatically inserted")

    # Literal source baseline preservation: the existing sample's broad status
    # label must NOT be silently upgraded in generated workbooks.
    require(sample["status"] == "SOURCE-VERIFIED SAMPLE / NOT ADOPTED",
            "The historical baseline status label was silently edited")
    return {
        "result": "PASS",
        "scope": "APPROVED_SAMPLE_LAYOUT_AND_SOURCE_POINTER_CONSISTENCY_ONLY",
        "sourceSemanticVerification": "NOT PERFORMED",
        "masterXlsxGenerated": False,
        "donorColumns": len(order),
        "dimFinalColumn": header[-1],
        "sectionDividers": len(groups),
        "proposedDimRows": len(dim_rows),
        "populatedCells": len(all_matches),
        "ledgerRecords": len(evidence_rows),
        "priorClaimCounts": dict(observed_fits),
        "step04PotentialColumnsNotInserted": 46,
        "frozenSourceInputsMatched": 4,
        "githubMarkdownDividersChecked": len(groups),
    }


if __name__ == "__main__":
    print(json.dumps(validate(), indent=2))
