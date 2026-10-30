from pathlib import Path
import hashlib,subprocess,json,sys,time,shutil
r=Path(__file__).resolve().parent;repo=Path('/Users/bkolodziejek/Downloads/BE_Codex_Handoff/work/manuscript_revision_20261029');m=repo/'manuscript/compact-v16';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
for name,cmd in [('notes',[sys.executable,'-I','-B',str(r/'check_notes.py')]),('retained-geometry',[sys.executable,'-I','-B',str(m/'tools/check_revision_geometry_constants.py')])]:
 start=time.monotonic();x=subprocess.run(cmd,cwd=repo,capture_output=True)
 (r/(name+'.stdout.json')).write_bytes(x.stdout);(r/(name+'.stderr.txt')).write_bytes(x.stderr)
 checks.append(dict(name=name,command=cmd,returncode=x.returncode,seconds=time.monotonic()-start,stdout_sha256=hashlib.sha256(x.stdout).hexdigest(),stderr_sha256=hashlib.sha256(x.stderr).hexdigest()));assert x.returncode==0
src=r/'compile-source';src.mkdir();paths=subprocess.check_output(['git','ls-tree','-r','--name-only','HEAD','manuscript/compact-v16'],cwd=repo).decode().splitlines()
for name in paths:
 q=Path(name)
 if q.suffix in ['.tex','.bib','.bbl']:
  target=src/q.relative_to('manuscript/compact-v16');target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(subprocess.check_output(['git','show','HEAD:'+name],cwd=repo))
owned=['sections/05-geometry-counts.tex','sections/03-conservation.tex','sections/07-direct-acquisition.tex']
for name in owned:shutil.copy2(m/name,src/name)
# Guide's label now aliases the relocated canonical equation. Match coordinator's intended removal.
guide=src/'sections/01b-guide.tex';t=guide.read_text().replace(r'\label{revision:canonical-decomposition}','');guide.write_text(t)
for i in range(1,4):
 cmd=['/Library/TeX/texbin/pdflatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','main.tex'];start=time.monotonic();x=subprocess.run(cmd,cwd=src,capture_output=True)
 (r/f'compile{i}.stdout.txt').write_bytes(x.stdout);(r/f'compile{i}.stderr.txt').write_bytes(x.stderr)
 checks.append(dict(name=f'compile{i}',command=cmd,returncode=x.returncode,seconds=time.monotonic()-start));assert x.returncode==0
log=(src/'main.log').read_text();warnings=[line for line in log.splitlines() if 'Overfull' in line or 'undefined' in line or 'multiply defined' in line]
(r/'receipt.json').write_text(json.dumps(dict(python=sys.version,checks=checks,owned_sources_sha256={name:sha(m/name) for name in owned},diagnostic_source_sha256=sha(r/'check_notes.py'),compile_warnings=warnings,scope='Owned three-file compilation over HEAD baseline, guide duplicate label removed in scratch only; final integrated build and visual review belong to coordinator.'),indent=2)+'\n')
print(json.dumps(dict(status='PASS_OPUS_GEOMETRY_COMPONENT',warnings=warnings,pdf=str(src/'main.pdf'))))
