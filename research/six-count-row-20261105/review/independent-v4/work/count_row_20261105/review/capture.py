"""Create-only subprocess evidence capture for bounded independent reviews."""
from pathlib import Path
import hashlib,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[3]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    run=ROOT/sys.argv[1];script=ROOT/sys.argv[2]
    run.mkdir(parents=True,exist_ok=False)
    sources=[Path(__file__),script]+sorted(script.parent.glob('*.md'))
    before={str(p.relative_to(ROOT)):digest(p) for p in sources}
    args=[sys.executable,'-I','-B',str(script),str(run/'checked')]+sys.argv[3:]
    start=time.time()
    with (run/'stdout.txt').open('wb') as out,(run/'stderr.txt').open('wb') as err:
        result=subprocess.run(args,cwd=ROOT,stdout=out,stderr=err,check=False)
    after={str(p.relative_to(ROOT)):digest(p) for p in sources}
    rec=dict(argv=args,cwd=str(ROOT),actual_returncode=result.returncode,elapsed_seconds=time.time()-start,
      executable=sys.executable,version=sys.version,source_sha256_before=before,source_sha256_after=after,
      sources_unchanged=before==after,stdout_sha256=digest(run/'stdout.txt'),stderr_sha256=digest(run/'stderr.txt'))
    (run/'PROCESS.json').write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps(rec));raise SystemExit(result.returncode or int(before!=after))
if __name__=='__main__':main()
