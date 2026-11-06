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


def main() -> None:
    doc = json.loads((BASE / (NAME + ".json")).read_text(encoding="utf-8"))
    with (BASE / (NAME + ".csv")).open(newline="", encoding="utf-8") as f:
        mirror = list(csv.reader(f))
    md = (BASE / (NAME + ".md")).read_text(encoding="utf-8")

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
