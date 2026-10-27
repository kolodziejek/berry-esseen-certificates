"""Package and independently recompile portable TeX sources; no shell escape."""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys, tempfile, time, zipfile
from pypdf import PdfReader

root = Path(__file__).resolve().parents[4]
m = root/'manuscript/arxiv-v1'
build = root/'runs/manuscript-v3-20261027'/sys.argv[1]/'texlive'
out = root/'runs/manuscript-v3-20261027'/(sys.argv[2] if len(sys.argv)>2 else 'export01')
out.mkdir(parents=True, exist_ok=False)
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
shutil.copy2(build/'main.pdf', m/'main.pdf')
files = [m/'main.tex', *sorted((m/'sections').glob('*.tex')),
         *sorted((m/'appendices').glob('*.tex')), *sorted(m.glob('*.bib')), m/'README.md']
archive = m/'source-arxiv-v1.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:
        z.write(p,str(p.relative_to(m)))
    z.write(build/'main.bbl','main.bbl')
rebuild = Path(tempfile.mkdtemp(prefix='be-manuscript-v3-source-'))
with zipfile.ZipFile(archive) as z:
    z.extractall(rebuild)
passes = []
cmd = ['/Library/TeX/texbin/pdflatex','-no-shell-escape','-interaction=nonstopmode',
       '-halt-on-error','main.tex']
for i in range(1,4):
    t = time.perf_counter()
    p = subprocess.run(cmd,cwd=rebuild,capture_output=True)
    (out/f'pass{i}.stdout.txt').write_bytes(p.stdout)
    (out/f'pass{i}.stderr.txt').write_bytes(p.stderr)
    passes.append({'pass':i,'command':cmd,'exit_code':p.returncode,
                   'duration_seconds':time.perf_counter()-t})
    assert p.returncode == 0
shutil.copy2(rebuild/'main.log',out/'main.log')
a, b = PdfReader(m/'main.pdf'), PdfReader(rebuild/'main.pdf')
assert len(a.pages) == len(b.pages)
matches = [x.extract_text() == y.extract_text() for x,y in zip(a.pages,b.pages)]
assert all(matches)
warnings = [s for s in (rebuild/'main.log').read_text().splitlines()
            if any(x in s for x in ['Warning','Overfull','Underfull','undefined'])]
assert all('Shell escape feature is not enabled' in s for s in warnings)
receipt = {'archive':str(archive.relative_to(root)), 'archive_sha256':sha(archive),
           'pdf_sha256':sha(m/'main.pdf'), 'python':sys.version,
           'source_rebuild_directory':str(rebuild), 'passes':passes,
           'archive_inputs':{str(p.relative_to(m)):sha(p) for p in files},
           'pages':len(a.pages), 'all_page_text_matches_exported_pdf':all(matches),
           'final_layout_and_reference_warnings':warnings}
(out/'receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:receipt[k] for k in ['pages','all_page_text_matches_exported_pdf',
                                       'final_layout_and_reference_warnings']}))
