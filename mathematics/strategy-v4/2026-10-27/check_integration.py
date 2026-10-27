"""Cheap integration checks only; never starts a certificate campaign."""
from pathlib import Path
import hashlib, json, platform, subprocess, sys

root=Path(__file__).resolve().parents[3]
out=root/'runs/strategy-v4-20261027/integration01'
out.mkdir(parents=True,exist_ok=False)
sources=Path(__file__).resolve().parent
programs=[sources/name for name in ['check_geometry.py','argon-audit.py',
 'excess-check.py','excess-transport-check.py','opus_exact_checks.py','opus_adversarial.py']]
programs += [root/'runs/strategy-v4-20261027/transport-review01/check_review.py',
             root/'manuscript/arxiv-v1/tools/check_sources.py']
records=[]
for script in programs:
    cmd=[sys.executable,str(script)]
    p=subprocess.run(cmd,cwd=root,capture_output=True)
    name=script.stem
    (out/(name+'.stdout.txt')).write_bytes(p.stdout)
    (out/(name+'.stderr.txt')).write_bytes(p.stderr)
    records.append(dict(command=cmd,returncode=p.returncode,
       source_sha256=hashlib.sha256(script.read_bytes()).hexdigest()))
    assert p.returncode==0,(name,p.stderr[-2000:])

def tree(ref):
    data=subprocess.check_output(['git','ls-tree','-r',ref],cwd=root,text=True)
    return {line.split('\t',1)[1]:line.split('\t',1)[0] for line in data.splitlines()}
baseline=tree('6346fc1b4432bc5982822aa696eb566ed9e1e1ee')
head=tree('HEAD')
assert all(head.get(path)==entry for path,entry in baseline.items())
changed=subprocess.check_output(['git','diff','--name-only','HEAD'],cwd=root,text=True).splitlines()
assert not set(changed).intersection(baseline)
ms=json.loads((out/'check_sources.stdout.txt').read_text())
assert ms['passed']
note='\n'.join((sources/name).read_text() for name in ['main.tex','excess.tex','geometry.tex','alternatives.tex','inversion.tex'])
import re
labels=re.findall(r'\\label\{([^}]+)\}',note)
refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',note)
assert len(labels)==len(set(labels)) and set(refs)<=set(labels)
report=dict(status='PASS_BOUNDED_V4_INTEGRATION',python=platform.python_version(),
 checks=records,baseline_entries_unchanged=len(baseline),manuscript_labels=ms['labels'],
 manuscript_references=ms['references'],companion_labels=len(labels),
 mathematical_scope='Checks supplement the written arguments; no full BASE41, LOCAL42 or Lean acceptance.',
 note_sources={name:hashlib.sha256((sources/name).read_bytes()).hexdigest()
   for name in ['main.tex','excess.tex','geometry.tex','alternatives.tex','inversion.tex','references.bib']})
(out/'receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','baseline_entries_unchanged','manuscript_labels','manuscript_references','companion_labels']},indent=2))
