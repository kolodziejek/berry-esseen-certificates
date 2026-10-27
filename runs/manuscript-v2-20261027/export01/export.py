from pathlib import Path
import subprocess,json,hashlib,sys,zipfile,shutil,re,tempfile,time
from pypdf import PdfReader
root=Path.cwd();m=root/'manuscript/arxiv-v1';run=root/'runs/manuscript-v2-20261027';build=run/'build03/texlive';out=run/'export01';out.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
shutil.copy2(build/'main.pdf',m/'main.pdf')
files=[m/'main.tex',*sorted((m/'sections').glob('*.tex')),*sorted((m/'appendices').glob('*.tex')),*sorted(m.glob('*.bib')),m/'README.md']
archive=m/'source-arxiv-v1.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in files:z.write(p,str(p.relative_to(m)))
 z.write(build/'main.bbl','main.bbl')
rebuild=Path(tempfile.mkdtemp(prefix='be-manuscript-v2-source-'))
with zipfile.ZipFile(archive) as z:z.extractall(rebuild)
passes=[];cmd=['/Library/TeX/texbin/pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','main.tex']
for i in range(1,4):
 t=time.perf_counter();p=subprocess.run(cmd,cwd=rebuild,capture_output=True)
 (out/f'pass{i}.stdout.txt').write_bytes(p.stdout);(out/f'pass{i}.stderr.txt').write_bytes(p.stderr)
 passes.append({'pass':i,'command':cmd,'exit_code':p.returncode,'duration_seconds':time.perf_counter()-t});assert p.returncode==0
shutil.copy2(rebuild/'main.log',out/'main.log')
a=PdfReader(m/'main.pdf');b=PdfReader(rebuild/'main.pdf');assert len(a.pages)==len(b.pages)==164
matches=[x.extract_text()==y.extract_text() for x,y in zip(a.pages,b.pages)];assert all(matches)
old=PdfReader(run/'build02/texlive/main.pdf');changed=[i+1 for i,(x,y) in enumerate(zip(old.pages,a.pages)) if x.extract_text()!=y.extract_text()]
log=(rebuild/'main.log').read_text();warnings=[s for s in log.splitlines() if any(x in s for x in ['Warning','Overfull','Underfull','undefined'])]
assert all('Shell escape feature is not enabled' in x for x in warnings)
receipt={'archive':str(archive.relative_to(root)),'archive_sha256':sha(archive),'archive_bytes':archive.stat().st_size,'pdf':str((m/'main.pdf').relative_to(root)),'pdf_sha256':sha(m/'main.pdf'),'pdf_bytes':(m/'main.pdf').stat().st_size,'python':sys.version,'source_rebuild_directory':str(rebuild),'passes':passes,'archive_inputs':{str(p.relative_to(m)):sha(p) for p in files},'pages':len(a.pages),'all_page_text_matches_exported_pdf':all(matches),'final_layout_and_reference_warnings':warnings,'pages_changed_since_rendered_build02':changed}
(out/'receipt.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False))
print(json.dumps({k:receipt[k] for k in ['pages','all_page_text_matches_exported_pdf','final_layout_and_reference_warnings','pages_changed_since_rendered_build02']},indent=2))
render=run/'render03';render.mkdir(exist_ok=False)
for i in changed:
 cmd=['/Users/bkolodziejek/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm','-f',str(i),'-l',str(i),'-r','120','-png',str(m/'main.pdf'),str(render/'page')]
 subprocess.run(cmd,check=True,capture_output=True)
print('rendered changed pages at120dpi')
