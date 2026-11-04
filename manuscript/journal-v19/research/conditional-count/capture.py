#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,subprocess,sys,time

HERE=Path(__file__).resolve().parent
out=HERE/'pilot01';out.mkdir(exist_ok=False)
source=HERE/'own_count_obstruction.py'
cmd=[sys.executable,'-I','-B',str(source),str(out/'checked')]
started={'argv':cmd,'cwd':str(HERE),'python_version':sys.version,
         'python_sha256':hashlib.sha256(Path(sys.executable).read_bytes()).hexdigest(),
         'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
(out/'STARTED.json').write_text(json.dumps(started,indent=2)+'\n')
t=time.monotonic()
with (out/'stdout.txt').open('wb')as stdout,(out/'stderr.txt').open('wb')as stderr:
    p=subprocess.run(cmd,cwd=HERE,stdout=stdout,stderr=stderr,check=False)
result={**started,'actual_returncode':p.returncode,'elapsed_seconds':time.monotonic()-t,
        'stdout_sha256':hashlib.sha256((out/'stdout.txt').read_bytes()).hexdigest(),
        'stderr_sha256':hashlib.sha256((out/'stderr.txt').read_bytes()).hexdigest()}
(out/'PROCESS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
raise SystemExit(p.returncode)
