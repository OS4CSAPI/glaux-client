#!/usr/bin/env python3
"""Publish ISA-01 and normalize text exactly as the repository stores it.

The original transfer is verified first. CSV normalization changes line endings,
not field values (including meaningful trailing spaces in source data). Markdown
normalization removes only extra end-of-file blank lines. Published hashes are
then regenerated so the fresh-checkout verification checks actual Git bytes.
"""
import csv
import io
import json
from pathlib import Path
import recover_isa01_publication as recovery


def main():
    recovery.publish()
    report_path=recovery.D/recovery.REPORT
    report=json.loads(report_path.read_text(encoding='utf-8'))
    normalization=[]
    for name in report['published_file_sha256']:
        path=Path(name)
        original=path.read_bytes()
        revised=original
        if path.suffix=='.md':
            revised=original.rstrip(b'\r\n')+b'\n'
        elif path.suffix=='.csv':
            revised=original.replace(b'\r\n',b'\n')
            before=list(csv.reader(io.StringIO(original.decode('utf-8'))))
            after=list(csv.reader(io.StringIO(revised.decode('utf-8'))))
            recovery.need(before==after,'CSV content changed during line-ending normalization: '+name)
        if revised!=original:
            path.write_bytes(revised)
            normalization.append({'path':name,'change':'CRLF to LF only' if path.suffix=='.csv' else 'Remove extra EOF blank lines only','before_sha256':recovery.sha(original),'after_sha256':recovery.sha(revised),'semantic_content_changed':False})
        report['published_file_sha256'][name]=recovery.sha(path.read_bytes())
    report['repository_text_normalization']=normalization
    recovery.writejson(report_path,report)
    recovery.verify()
    print('PASS: Git-compatible LF and Markdown EOF normalization; every CSV field unchanged.')


if __name__=='__main__':
    main()
