"""Replay the precisely scoped continuous-region and domain results."""
from pathlib import Path
import hashlib,json,platform,subprocess,sys,time

ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def need(ok,msg):
    if not ok:raise ValueError(msg)
def main():
    need(__debug__ and not sys.flags.optimize,"unoptimized Python required")
    need(len(sys.argv)==2,"usage: reproduce.py NEW_OUTPUT")
    out=Path(sys.argv[1]).resolve()
    need(ROOT!=out and ROOT not in out.parents,"output must be outside the package")
    out.mkdir(parents=True,exist_ok=False)
    inputs={str(p.relative_to(ROOT)):sha(p) for p in ROOT.rglob("*")
            if p.is_file() and (p.suffix==".py" or p.name in ("contract.json","proof_object.json","domain.json"))}
    native=ROOT/"certificates/region-v1"; domain=ROOT/"domain-package/work/count_row_20261105/domain"
    jobs=[
      ("region",[str(native/"accept.py"),str(native/"proof_object.json"),str(out/"region/accepted"),"--k","2","--p","0.38","0.39","--u","-0.01","0.01"],"PASS_EXACT_COMPLETE_CLOSED_RECTANGLE"),
      ("region-controls",[str(native/"controls_v1.py"),str(native/"proof_object.json"),str(out/"region-controls/accepted")],"PASS_V1_CONTROLS"),
      ("domain",[str(domain/"check_domain.py"),str(out/"domain/accepted")],"PASS_EXACT_SOURCE_BOUND_DOMAIN_AND_ALGEBRA_CONTROLS")]
    records=[]
    for name,args,status in jobs:
        target=out/name;target.mkdir()
        argv=[sys.executable,"-I","-B","-S"]+args
        started={"argv":argv,"cwd":str(ROOT),"runtime":sys.version,"platform":platform.platform(),"inputs":inputs}
        (target/"STARTED.json").write_text(json.dumps(started,indent=2)+"\n")
        tick=time.monotonic()
        with(target/"stdout.txt").open("wb")as so,(target/"stderr.txt").open("wb")as se:
            child=subprocess.run(argv,cwd=ROOT,stdout=so,stderr=se)
        result=target/"accepted/RESULT.json"
        process={"returncode":child.returncode,"seconds":time.monotonic()-tick,
                 "stdout_sha256":sha(target/"stdout.txt"),"stderr_sha256":sha(target/"stderr.txt"),
                 "inputs_unchanged":all(sha(ROOT/p)==h for p,h in inputs.items()),
                 "result_sha256":sha(result)if result.exists()else None}
        (target/"PROCESS.json").write_text(json.dumps(process,indent=2)+"\n")
        need(child.returncode==0 and process["inputs_unchanged"],name+" actual execution failed")
        value=json.loads(result.read_text());need(value["status"]==status,name+" unexpected result scope")
        if name=="region":
            need(value["n"]==5 and value["k"]==2 and value["p"]==["19/50","39/100"] and value["u"]==["-1/100","1/100"],"exact original rectangle")
            need(len(value["leaves"])==10 and value["rays"]==120 and value["tensor_coefficients"]==18000,"complete region census")
        records.append({"name":name,**process})
    summary={"status":"PASS_RELOCATED_CONTINUOUS_REGION_AND_DOMAIN","full_row_proved":False,
             "scope":"n5 BN/p38, all p and acquired noise, k2, phase[-1/100,1/100]; full threshold domain audited separately.",
             "runs":records}
    (out/"RESULT.json").write_text(json.dumps(summary,indent=2)+"\n");print(json.dumps(summary,indent=2))
if __name__=="__main__":main()

