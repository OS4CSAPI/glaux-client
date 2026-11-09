#!/usr/bin/env python3
"""Read-only verification of the Step06 committed binary XLSX and its JSON/CSV mirrors.
This is file-integrity and presentation testing, NOT source semantic verification.
"""
from __future__ import annotations

import csv
import io
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

BASE = Path("Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk")
NAME = "Master_Donor_Concept_to_DIM_Crosswalk"
S = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"


def fail(message: str) -> None:
    raise AssertionError(message)


def required(cond: bool, message: str) -> None:
    if not cond:
        fail(message)


def colnum(label: str) -> int:
    result = 0
    for char in label:
        result = 26 * result + ord(char) - ord("A") + 1
    return result - 1


def data_rows(xml_bytes: bytes, width: int) -> tuple[ET.Element, list[list[str]]]:
    root = ET.fromstring(xml_bytes)
    out = []
    sheet_data = root.find(S + "sheetData")
    required(sheet_data is not None, "worksheet lacks sheetData")
    for row in sheet_data.findall(S + "row"):
        values = [""] * width
        for c in row.findall(S + "c"):
            ref = c.attrib.get("r", "")
            m = re.match(r"^([A-Z]+)([0-9]+)$", ref)
            required(m is not None, f"bad cell reference {ref}")
            col = colnum(m.group(1))
            required(col < width, f"cell outside expected width: {ref}")
            x = c.find(S + "is")
            if x is None:
                v = c.find(S + "v")
                value = v.text if v is not None and v.text is not None else ""
            else:
                value = "".join(t.text or "" for t in x.iter(S + "t"))
            values[col] = value
        out.append(values)
    return root, out


def verify_current_master(doc: dict, mirror: list[list[str]], md: str) -> None:
    """Read-only successor for the current source-backed, 26-sheet ISA22 master.

    The archived six-sheet Step06 checker below remains intact for historic
    content. This branch no longer contains the 2026-11-06 8-column schema.
    """
    import hashlib
    state = json.loads((BASE / "ISA_Correction_Status_07NOV2026.json").read_text(encoding="utf-8"))
    evidence = json.loads((BASE / "ISA21_Source_First_31_Targets_25_Findings_6_Questions_09NOV2026.json").read_text(encoding="utf-8"))
    record = json.loads((BASE / "ISA22_Validated_Workbook_Record_09NOV2026.json").read_text(encoding="utf-8"))
    mirror_md = (BASE / "ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    grid = doc["review_grid"]
    required(len(grid) == 346 and len(doc["rows"]) == 329 and len(doc["columns"]) == 14, "current grid / row / column counts")
    required(all(len(row) == 14 for row in grid) and mirror == grid, "current JSON/CSV 346x14 exact parity")
    required(md.split("\n", 1)[1] == mirror_md.split("\n", 1)[1], "current Markdown and review mirror bodies")
    required(len(doc["originalDonorEvidence"]) == 58 and len(doc["caseEvidence"]) == 73, "original donor/case evidence preserved")
    required(doc["columns"][-1]["key"] == "DIM" and [x["key"] for x in doc["columns"][:4]] == ["Dragino", "AirGradient", "Campbell", "Bennett"], "case-left / DIM-right layout")
    required(len(evidence["original_row_and_case_targets"]) == 31 and len(evidence["original_earlier_findings"]) == 25 and len(evidence["six_precise_source_questions"]) == 6, "31/25/six source audit")
    required(all(x["question_closed"] is False for x in evidence["six_precise_source_questions"]), "six exact source questions remain open")
    required(doc["ISAEvidence"]["currentPrimaryReviews"] == 480 and doc["ISAEvidence"]["sourceSupportedPrimary"] == 474 and doc["ISAEvidence"]["specificQuestions"] == 6, "480/474/six catalogue")
    required(state["technicalIterationsCompleted"] == 41 and state["nextOnOwnerProceed"] == "BROADER-DONOR-CROSSWALK-STEP16-OWNER-REVIEW", "ISA22 completion and owner Step16 route")
    binary = (BASE / (NAME + ".xlsx")).read_bytes()
    digest = hashlib.sha256(binary).hexdigest()
    required(digest == doc["currentWorkbookSha256"] == state["workbookSnapshot"]["sha256"] == record["workbook_sha256"], "GitHub current saved workbook SHA-256")
    with zipfile.ZipFile(io.BytesIO(binary)) as book:
        required(book.testzip() is None, "current workbook ZIP CRC")
        for path in book.namelist():
            if path.endswith((".xml", ".rels")):
                ET.fromstring(book.read(path))
        root = ET.fromstring(book.read("xl/workbook.xml"))
        sheets = [x.get("name") for x in root.find(S+"sheets")]
        required(sheets == record["sheets"] and len(sheets) == 26, "26 original workbook sheets in order")
        required(len(record["updated_tabs"]) == 10 and len(record["untouched_original_tabs"]) == 16, "ten current and sixteen preserved worksheet views")
        rels={x.attrib["Id"]:x.attrib["Target"] for x in ET.fromstring(book.read("xl/_rels/workbook.xml.rels"))}
        master_path=None
        for node in root.find(S+"sheets"):
            if node.get("name") == "Master Crosswalk":
                target=rels[node.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")]
                master_path=target.lstrip("/") if target.startswith("/") else "xl/"+target
                break
        required(master_path is not None, "current primary sheet target found")
        master, actual = data_rows(book.read(master_path), 14)
        required(actual == grid, "every current saved master XLSX cell matches source JSON")
        merges = [x.attrib["ref"] for x in master.find(S+"mergeCells").findall(S+"mergeCell")]
        want = ["A1:D1", "E1:H1", "I1:M1"] + [f"A{i+1}:N{i+1}" for i in doc["review_sections"]]
        required(merges == want, "case and donor group/section full-width merges")
        view = master.find(S+"sheetViews").find(S+"sheetView")
        pane = view.find(S+"pane")
        required(pane is not None and pane.get("xSplit") == "4" and pane.get("ySplit") == "2", "frozen case and column header panes")
        for node in book.namelist():
            if node.startswith("xl/worksheets/") and node.endswith(".xml"):
                bad = [c.get("r") for c in ET.fromstring(book.read(node)).iter(S+"c") if c.get("t") == "e"]
                required(not bad, f"Excel error-value cells in {node}: {bad[:5]}")
    required(record["counts"]["source_blocks"] == 279 and record["counts"]["DMS_outcomes"] == 480 and record["counts"]["DIM_adopted"] == 0, "source inventory and no DIM adoption")
    print("PASS: current ISA22 26-sheet workbook exact cell/merge/freeze/ZIP/XML/error scan and SHA-256 parity with source master.")
    print("PASS: 329 rows, 346 display rows, 14 columns, 480 DMS entries, 279 original source blocks, 31/25/six audit, 58 donor and 73 case records, no DIM adoption.")
    print("LIMIT: original-source interpretation, vendor authenticity, full ISA/OGC ATS and actual equipment conformance are separate from this scoped workbook verification.")


def main() -> None:
    doc = json.loads((BASE / (NAME + ".json")).read_text(encoding="utf-8"))
    with (BASE / (NAME + ".csv")).open(newline="", encoding="utf-8") as f:
        mirror = list(csv.reader(f))
    md = (BASE / (NAME + ".md")).read_text(encoding="utf-8")

    if "review_grid" in doc and "columns" in doc:
        verify_current_master(doc, mirror, md)
        return

    expected = [([x["name"] for x in doc["donorColumns"]] + ["PROPOSED DIM ELEMENT"])]
    divider_rows = []
    for row in doc["rows"]:
        if row["type"] == "section":
            divider_rows.append(len(expected) + 1)
            expected.append([row["title"]] + [""] * 7)
        else:
            expected.append(row["display"])
    required(len(expected) == 28, "master not 1 header + 5 dividers + 22 rows")
    required(expected == mirror, "CSV differs from structured JSON source")
    required(len(doc["evidence"]) == 51, "expected exactly 51 evidence claims")
    required(all(x["sourceVerification"] == "PRIOR_SOURCE_EXTRACT_ONLY" for x in doc["evidence"]), "a claim was falsely promoted to original checked")
    required(all(x["disposition"] == "PROPOSED_NOT_ADOPTED" for x in doc["evidence"]), "unapproved mapping decision")
    required(md.count('colspan="8"') == 5, "Markdown lacks 5 full-width section rows")
    required(doc["display"]["finalDonorUsageRanking"] == "UNDETERMINED", "unapproved final donor ordering")

    with zipfile.ZipFile(BASE / (NAME + ".xlsx"), "r") as book:
        required(book.testzip() is None, "ZIP CRC mismatch in XLSX")
        all_names = book.namelist()
        required("[Content_Types].xml" in all_names, "missing OOXML content types")
        for n in all_names:
            if n.endswith(".xml") or n.endswith(".rels"):
                ET.fromstring(book.read(n))

        wb = ET.fromstring(book.read("xl/workbook.xml"))
        sheets = wb.find(S + "sheets")
        names = [node.attrib["name"] for node in sheets.findall(S + "sheet")]
        required(names == ["Master Crosswalk", "Evidence", "DIM Definitions", "Donor Sources", "Holds & Decisions", "Read Me"], f"worksheet mismatch: {names}")

        master, actual = data_rows(book.read("xl/worksheets/sheet1.xml"), 8)
        required(actual == expected, "XLSX Master Crosswalk differs from original JSON/CSV cells")
        merge_root = master.find(S + "mergeCells")
        merges = [x.attrib["ref"] for x in merge_root.findall(S + "mergeCell")] if merge_root is not None else []
        wanted = [f"A{i}:H{i}" for i in divider_rows]
        required(merges == wanted, f"incorrect section merges: {merges} != {wanted}")
        required(master.find(S + "autoFilter") is None, "invalid AutoFilter across merged section rows")
        view = master.find(S + "sheetViews").find(S + "sheetView")
        pane = view.find(S + "pane")
        required(pane is not None and pane.attrib.get("ySplit") == "1", "master header is not frozen")

        evidence, evalues = data_rows(book.read("xl/worksheets/sheet2.xml"), 15)
        required(len(evalues) == 52, "Evidence sheet not 51 records plus header")
        required(all(row[7] == "PRIOR_SOURCE_EXTRACT_ONLY" for row in evalues[1:]), "Evidence sheet source statuses incorrect")
        required(len(evidence.find(S + "hyperlinks").findall(S + "hyperlink")) == 51, "Evidence source URL hyperlinks not complete")
        for n in [2, 3, 4, 5]:
            root, table = data_rows(book.read(f"xl/worksheets/sheet{n}.xml"), [15,7,9,9][n-2])
            required(root.find(S + "autoFilter") is not None, f"sheet {n} lacks supporting filter")

        definitions, dvalues = data_rows(book.read("xl/worksheets/sheet3.xml"), 7)
        required(len(dvalues) == 23, "DIM Definitions has wrong row count")
        required(all("PROPOSED" in row[5] for row in dvalues[1:]), "definition accidentally treated as adopted")
        sources, svalues = data_rows(book.read("xl/worksheets/sheet4.xml"), 9)
        required(len(svalues) == 8, "Donor Sources is not seven original columns")
        required(all(row[7] == "UNDETERMINED" for row in svalues[1:]), "donor ranking prematurely finalized")

    print("PASS: GitHub-stored Step06 XLSX ZIP and XML parse; 6 editable sheets; 7 donors, DIM last; 5 full-width merges; 22 original proposed rows; 51 identical source claims; all 51 PRIOR_SOURCE_EXTRACT_ONLY; matching Markdown/CSV/JSON; 51 Evidence links; 4 companion filters; no new donor ranking.")
    print("LIMIT: source-semantic verification, original publisher clauses, complete DIM adoption and external CSAPI interoperability were NOT tested.")


if __name__ == "__main__":
    main()
