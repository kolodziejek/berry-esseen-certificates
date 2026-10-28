"""Build and render the selected manuscript with recorded source/command evidence."""
from pathlib import Path
import hashlib,json,subprocess,sys,time
from pypdf import PdfReader
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[4]
m=root/'manuscript/arxiv-v1'
run=root/'runs/manuscript-v9-20261028'/sys.argv[1]
run.mkdir(parents=True,exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
for name,script in [('sources',m/'tools/check_sources.py'),('scalar',m/'research/v9_checks/scalar.py')]:
 cmd=[sys.executable,'-I','-B',str(script)]
 t=time.perf_counter();cp=subprocess.run(cmd,cwd=root,capture_output=True)
 (run/(name+'.stdout.json')).write_bytes(cp.stdout)
 (run/(name+'.stderr.txt')).write_bytes(cp.stderr)
 checks.append({'name':name,'command':cmd,'returncode':cp.returncode,
                'duration_seconds':time.perf_counter()-t,'script_sha256':sha(script)})
 if cp.returncode:raise RuntimeError(name+' failed; evidence preserved')
cmd=[sys.executable,'/Users/bkolodziejek/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py',str(m/'main.tex'),'--compiler','texlive','--output-directory',str(run/'texlive'),'--json']
t=time.perf_counter();cp=subprocess.run(cmd,cwd=root,capture_output=True)
(run/'build.stdout.json').write_bytes(cp.stdout);(run/'build.stderr.txt').write_bytes(cp.stderr)
r={'checks':checks,'command':cmd,'returncode':cp.returncode,'duration_seconds':time.perf_counter()-t,'python':sys.version,'inputs':{str(p.relative_to(m)):sha(p) for p in [*m.rglob('*.tex'),*m.glob('*.bib')]}}
if not cp.returncode:
 pdf=run/'texlive/main.pdf';r['pdf_sha256']=sha(pdf)
 r['pages']=len(PdfReader(pdf).pages)
 log=(run/'texlive/main.log').read_text()
 r['warnings']=[x for x in log.splitlines() if any(s in x for s in ['Warning','Overfull','Underfull','undefined'])]
(run/'receipt.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['returncode','pages','warnings','duration_seconds'] if k in r}))
if cp.returncode:raise RuntimeError('TeX failed; evidence preserved')
render=run/'render';render.mkdir()
cmd=['/Users/bkolodziejek/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm','-r','45','-png',str(pdf),str(render/'page')]
cp=subprocess.run(cmd,capture_output=True)
(run/'render.stderr.txt').write_bytes(cp.stderr)
if cp.returncode:raise RuntimeError('Rendering failed')
images=sorted(render.glob('page-*.png'))
assert len(images)==r['pages']
for start in range(0,len(images),12):
 sheet=Image.new('RGB',(4*380,3*555),'#d6d6d6');d=ImageDraw.Draw(sheet)
 for j,p in enumerate(images[start:start+12]):
  im=Image.open(p).convert('RGB');im.thumbnail((370,525));x,y=(j%4)*380+5,(j//4)*555+22
  sheet.paste(im,(x,y));d.text((x,y-18),str(start+j+1),fill='black')
 sheet.save(render/f'overview-{start+1:03d}-{min(start+12,len(images)):03d}.png')
print('Rendered '+str(len(images))+' pages.')
