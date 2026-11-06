"""Capture a process with its actual return code and input identities."""
from pathlib import Path
import argparse, hashlib, json, platform, subprocess, sys, time

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

p=argparse.ArgumentParser()
p.add_argument('run')
p.add_argument('--input',action='append',default=[])
p.add_argument('command',nargs=argparse.REMAINDER)
a=p.parse_args()
command=a.command[1:] if a.command[:1]==['--'] else a.command
if not command: p.error('command required')
run=Path(a.run).resolve();run.mkdir(parents=True,exist_ok=False)
inputs={str(Path(v).resolve()):sha(v) for v in a.input}
started={'command':command,'cwd':str(Path.cwd()),'inputs':inputs,
 'runtime':{'executable':sys.executable,'version':sys.version,
 'platform':platform.platform(),'optimized':sys.flags.optimize},
 'capture_driver_sha256':sha(__file__)}
(run/'STARTED.json').write_text(json.dumps(started,indent=2)+'\n')
t=time.monotonic()
with (run/'stdout.txt').open('w') as out,(run/'stderr.txt').open('w') as err:
 r=subprocess.run(command,stdout=out,stderr=err)
record={'returncode':r.returncode,'seconds':time.monotonic()-t,
 'stdout_sha256':sha(run/'stdout.txt'),'stderr_sha256':sha(run/'stderr.txt'),
 'inputs_unchanged':all(sha(k)==v for k,v in inputs.items())}
(run/'PROCESS.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
if not record['inputs_unchanged']:raise SystemExit('inputs changed')
raise SystemExit(r.returncode)
