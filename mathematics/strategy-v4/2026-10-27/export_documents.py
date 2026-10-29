#!/usr/bin/env python3
"""Package the reviewed documents and rebuild each archive in a fresh directory.

Requires the already installed pdfLaTeX and pypdf. This is document validation,
not a mathematical acceptance program. It refuses an existing run directory.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from zipfile import ZipFile, ZIP_DEFLATED

from pypdf import PdfReader


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pdf_text(path):
    return [page.extract_text() for page in PdfReader(path).pages]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-id', default='export01')
    args = parser.parse_args()
    if not args.run_id.replace('-', '').replace('_', '').isalnum():
        parser.error('run-id must contain only letters, numbers, hyphens or underscores')
    note = Path(__file__).resolve().parent
    root = note.parents[2]
    run_root = root / 'runs/strategy-v4-20261027'
    out = run_root / args.run_id
    out.mkdir(exist_ok=False)
    compiler = Path('/Library/TeX/texbin/pdflatex')
    receipt = {
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'interpreter': sys.executable, 'python': platform.python_version(),
        'driver_sha256': digest(Path(__file__)),
        'compiler': subprocess.check_output([str(compiler), '--version'], text=True).splitlines()[0],
        'documents': [],
        'scope': 'Portable TeX reproduction and page-text comparison, not proof validation.',
    }
    projects = [
        ('companion', note, run_root / 'note-build02', 'source-strategy-v4.zip', 14),
        ('manuscript', root / 'manuscript/arxiv-v1', run_root / 'manuscript-build02', 'source-arxiv-v1.zip', 158),
    ]
    for name, source, build, archive_name, expected_pages in projects:
        files = [source / 'main.tex']
        if name == 'companion':
            files += [source / f for f in ('excess.tex', 'geometry.tex', 'alternatives.tex', 'inversion.tex', 'references.bib')]
        else:
            files += sorted((source / 'sections').glob('*.tex'))
            files += sorted((source / 'appendices').glob('*.tex'))
            files += sorted(source.glob('*.bib'))
        members = {str(p.relative_to(source)): p for p in files}
        members['main.bbl'] = build / 'main.bbl'
        members['README.md'] = source / ('BUILD.md' if name == 'companion' else 'README.md')
        for p in members.values():
            assert p.is_file(), p
        shutil.copy2(build / 'main.pdf', source / 'main.pdf')
        archive = source / archive_name
        with ZipFile(archive, 'w', ZIP_DEFLATED) as z:
            for member, path in sorted(members.items()):
                z.write(path, member)
        work = out / (name + '-source')
        work.mkdir()
        with ZipFile(archive) as z:
            assert len(z.namelist()) == len(set(z.namelist()))
            assert set(z.namelist()) == set(members)
            z.extractall(work)  # The archive above contains only controlled relative paths.
        result = {
            'name': name, 'archive': str(archive.relative_to(root)),
            'archive_sha256': digest(archive),
            'member_sha256': {k: digest(v) for k, v in members.items()},
            'passes': [],
        }
        receipt['documents'].append(result)
        for attempt in range(1, 4):
            command = [str(compiler), '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', 'main.tex']
            process = subprocess.run(command, cwd=work, capture_output=True, text=True)
            (out / f'{name}-pass{attempt}.stdout.txt').write_text(process.stdout)
            (out / f'{name}-pass{attempt}.stderr.txt').write_text(process.stderr)
            result['passes'].append({'command': command, 'cwd': str(work), 'returncode': process.returncode})
            (out / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
            if process.returncode:
                raise RuntimeError(f'{name} pass {attempt} failed; see saved streams')
        log = (work / 'main.log').read_text()
        (out / f'{name}-final-log.txt').write_text(log)
        assert 'Overfull' not in log, name
        assert 'undefined references' not in log.lower(), name
        assert 'undefined citations' not in log.lower(), name
        assert 'Label(s) may have changed' not in log, name
        original_text = pdf_text(source / 'main.pdf')
        rebuilt_text = pdf_text(work / 'main.pdf')
        assert len(original_text) == len(rebuilt_text) == expected_pages, name
        assert original_text == rebuilt_text, f'{name}: page text differs'
        result.update({
            'pages': expected_pages, 'page_text_identical': True,
            'delivered_pdf_sha256': digest(source / 'main.pdf'),
            'rebuilt_pdf_sha256': digest(work / 'main.pdf'),
            'underfull_notices': log.count('Underfull'),
            'warning_lines': [line for line in log.splitlines() if 'Warning' in line],
        })
        (out / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    receipt['status'] = 'PASS_PORTABLE_DOCUMENT_REBUILDS'
    receipt['completed_utc'] = datetime.now(timezone.utc).isoformat()
    (out / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(receipt['status'])
    for item in receipt['documents']:
        print(item['name'], item['pages'], 'pages; page text identical')


if __name__ == '__main__':
    main()
