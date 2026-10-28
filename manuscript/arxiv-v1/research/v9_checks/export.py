"""Package selected TeX inputs and rebuild offline with shell escape disabled."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from pypdf import PdfReader

root = Path(__file__).resolve().parents[4]
m = root / 'manuscript/arxiv-v1'
build = root / 'runs/manuscript-v9-20261028' / sys.argv[1]
out = root / 'runs/manuscript-v9-20261028' / sys.argv[2]
out.mkdir(parents=True, exist_ok=False)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
sources = json.loads((build / 'sources.stdout.json').read_text())
if not sources['passed']:
    raise RuntimeError('The selected build did not pass its source check')
for name, digest in sources['source_sha256'].items():
    if sha(m / name) != digest:
        raise RuntimeError('Source changed after build: ' + name)
build_receipt = json.loads((build / 'receipt.json').read_text())
for p in m.glob('*.bib'):
    if sha(p) != build_receipt['inputs'][p.name]:
        raise RuntimeError('Bibliography changed after build: ' + p.name)
shutil.copy2(build / 'texlive/main.pdf', m / 'main.pdf')
files = [m / name for name in sorted(sources['source_sha256'])]
files += sorted(m.glob('*.bib')) + [m / 'README.md']
archive = m / 'source-arxiv-v1.zip'
inputs = {str(p.relative_to(m)): sha(p) for p in files}
inputs['main.bbl'] = sha(build / 'texlive/main.bbl')
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in files:
        z.write(p, str(p.relative_to(m)))
    z.write(build / 'texlive/main.bbl', 'main.bbl')
rebuild = Path(tempfile.mkdtemp(prefix='be-manuscript-v9-source-'))
with zipfile.ZipFile(archive) as z:
    z.extractall(rebuild)
for name, digest in inputs.items():
    if sha(rebuild / name) != digest:
        raise RuntimeError('Archive mismatch: ' + name)
passes = []
cmd = ['/Library/TeX/texbin/pdflatex', '-no-shell-escape',
       '-interaction=nonstopmode', '-halt-on-error', 'main.tex']
for i in range(1, 4):
    t = time.perf_counter()
    p = subprocess.run(cmd, cwd=rebuild, capture_output=True)
    (out / f'pass{i}.stdout.txt').write_bytes(p.stdout)
    (out / f'pass{i}.stderr.txt').write_bytes(p.stderr)
    passes.append({'pass': i, 'command': cmd, 'exit_code': p.returncode,
                   'duration_seconds': time.perf_counter() - t})
    if p.returncode:
        raise RuntimeError('Portable build failed; command output preserved')
shutil.copy2(rebuild / 'main.log', out / 'final-tex-log.txt')
a, b = PdfReader(m / 'main.pdf'), PdfReader(rebuild / 'main.pdf')
matches = [x.extract_text() == y.extract_text() for x, y in zip(a.pages, b.pages)]
if len(a.pages) != len(b.pages) or not all(matches):
    raise RuntimeError('Portable PDF text differs from the reviewed PDF')
warnings = [s for s in (rebuild / 'main.log').read_text().splitlines()
            if any(x in s for x in ['Warning', 'Overfull', 'Underfull', 'undefined'])]
if any('Shell escape feature is not enabled' not in s for s in warnings):
    raise RuntimeError('Unexpected portable-build warning')
receipt = {
    'archive': str(archive.relative_to(root)), 'archive_sha256': sha(archive),
    'pdf_sha256': sha(m / 'main.pdf'), 'python': sys.version,
    'export_script_sha256': sha(Path(__file__)),
    'build_receipt_sha256': sha(build / 'receipt.json'),
    'source_rebuild_directory': str(rebuild), 'passes': passes,
    'archive_inputs': inputs, 'pages': len(a.pages),
    'all_page_text_matches_exported_pdf': all(matches),
    'final_layout_and_reference_warnings': warnings,
}
(out / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({k: receipt[k] for k in [
    'pages', 'all_page_text_matches_exported_pdf',
    'final_layout_and_reference_warnings']}))
