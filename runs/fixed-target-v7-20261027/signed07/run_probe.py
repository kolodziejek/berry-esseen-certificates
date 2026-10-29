#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys,time,json,platform,hashlib
here=Path(__file__).resolve().parent;root=here.parents[2]
if len(sys.argv)<2:raise ValueError('unique run id and optional probe args')
name=sys.argv[1]
if not name.replace('-','').isalnum():raise ValueError('simple run id')
out=root/'runs/fixed-target-v7-20261027'/name;out.mkdir(parents=True,exist_ok=False)
cmd=[sys.executable,'-B',str(here/'signed_probe.py')]+sys.argv[2:]
t=time.monotonic()
for p in here.glob('*.py'):(out/p.name).write_bytes(p.read_bytes())
with (out/'stdout.json').open('w') as stdout,(out/'stderr.txt').open('w') as stderr:
 try:rc=subprocess.run(cmd,stdout=stdout,stderr=stderr,timeout=180,cwd=root).returncode
 except subprocess.TimeoutExpired:rc=124
receipt=dict(command=cmd,returncode=rc,elapsed_seconds=time.monotonic()-t,python=platform.python_version(),optimization=sys.flags.optimize,
 source_sha256={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in list(here.glob('*.py'))+list((root/'mathematics/fixed-target-v6/2026-10-27').glob('*.py'))+list((root/'mathematics/fixed-target-v5/2026-10-27').glob('*.py'))+list((root/'mathematics/fixed-target-v5/2026-10-27/cell-sources').glob('*.py'))+[root/'mathematics/fixed-target-v5/2026-10-27/cell-input.json']})
(out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt));print((out/'stderr.txt').read_text()[-4000:])
