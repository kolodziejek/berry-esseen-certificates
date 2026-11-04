"""Capture only the algebra prefix of the unchanged INITIAL47 cell grid.

This is deliberately NOT a certificate acceptor. It stops before the first
Fourier call; no raw remainder, exported resource or Berry--Esseen conclusion
is computed. Supplied feedback states are inputs, not newly accepted outputs.
"""
from pathlib import Path
import ast
import gzip
import hashlib
import importlib.util
import json
import platform
import shutil
import sys
import time
from fractions import Fraction

SOURCE = Path(__file__).resolve().parent / "native"
PINS = {
    "local_signed_core.py": "f0c2df790b794413e7fd08c4f3fc20f79c15c27a6456c8eae5013b96eb093c11",
    "kernel.py": "d71f58b7527c3cf6d2146d816e5d124f6f331d1b153e5aaedee5182707647f12",
    "high_window_core.py": "53e181be63852e21abc3f44191cce7237c46d9e9d7868d3b6b94fccb606c7232",
    "initial47_proof.json": "95c5c1de0062b6a9e294a81ee8497eee8bdb2e0798299422d7ad39b885e4a951",
    "accept_initial47.py": "cd0030c8ba3fbd9fdd357f191fe519c093ce69968c292e2eaf2b40cd7d6561bd",
}
NAMES = ("local_signed_core.py", "kernel.py", "high_window_core.py", "initial47_proof.json", "accept_initial47.py")
FIELDS = ("n", "R", "K", "cap", "raw", "d", "ir", "ib", "ig", "im", "rl", "rh", "M", "eta", "bl", "bu", "l", "h", "dist", "den", "asl", "asu", "bsl", "bsu", "DU", "mlo", "mhi", "ml", "mu", "denm", "DL", "corrections", "c4u", "Mc", "etac", "dlower")


def need(c, why):
    if not c:
        raise ValueError(why)


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def enc(v):
    if v is None or type(v) is int:
        return v
    if isinstance(v, Fraction):
        return str(v)
    if type(v) is list:
        return [enc(x) for x in v]
    raise TypeError(type(v))


def make_projection(source):
    tree = ast.parse(source)
    stage = [x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name == "stage"]
    need(len(stage) == 1, "one original stage")
    stage = stage[0]
    loops = [x for x in ast.walk(stage) if isinstance(x, ast.For) and isinstance(x.target, ast.Name) and x.target.id == "im"]
    need(len(loops) == 1, "one innermost mean grid")
    loop = loops[0]
    positions = [i for i, x in enumerate(loop.body) if isinstance(x, ast.Assign) and isinstance(x.value, ast.Call) and isinstance(x.value.func, ast.Attribute) and isinstance(x.value.func.value, ast.Name) and x.value.func.value.id == "k" and x.value.func.attr == "sixth"]
    need(len(positions) == 1, "unique first Fourier assignment")
    stop = positions[0]
    original_prefix = ast.dump(ast.Module(body=loop.body[:stop], type_ignores=[]), include_attributes=False)
    prefix = loop.body[:stop]
    need(not any(isinstance(x, ast.Call) and isinstance(x.func, ast.Attribute) and x.func.attr in ("sixth", "universal_high", "high") for stmt in prefix for x in ast.walk(stmt)), "prefix contains no Fourier evaluations")
    loop.body = prefix + ast.parse("capture(locals())\nactive += 1\ncontinue\n").body
    # Keep every pre-grid initialization and all four nested source loops.
    outer = [i for i,x in enumerate(stage.body) if isinstance(x, ast.For) and isinstance(x.target, ast.Name) and x.target.id == "ir"]
    need(len(outer)==1, "one outer rho grid")
    stage.body = stage.body[:outer[0]+1] + ast.parse("k.need(active+excluded==nr*nb*ng*nm, 'complete PREFIX grid cardinality')\nreturn dict(prefix_active=active,prefix_excluded=excluded,reasons=reasons,total=nr*nb*ng*nm)\n").body
    ast.fix_missing_locations(tree)
    need(ast.dump(ast.Module(body=loop.body[:stop],type_ignores=[]),include_attributes=False)==original_prefix, "original prefix retained exactly in AST")
    return ast.unparse(tree)+"\n", {"source_prefix_statements":stop,"original_prefix_ast_sha256":hashlib.sha256(original_prefix.encode()).hexdigest(),"stop_before":"l0,lh,l2=k.sixth(n,Mc,g,etac)","fourier_evaluations":0}


def main():
    need(__debug__ and not sys.flags.optimize, "unoptimized Python required")
    need(len(sys.argv)==2, "new run directory required")
    run=Path(sys.argv[1]).resolve(); run.mkdir(parents=True,exist_ok=False)
    copies=run/"native"; copies.mkdir()
    inputs={}
    for name in NAMES:
        src=SOURCE/name
        need(sha(src)==PINS[name], "fixed source identity: "+name)
        shutil.copyfile(src,copies/name)
        inputs[name]={"sha256":sha(src),"bytes":src.stat().st_size}
    proof=json.loads((copies/"initial47_proof.json").read_text())
    need(proof["name"]=="INITIAL47_R384" and len(proof["steps"])==13, "fixed 13 feedback states")
    # Recover P from its defining native assignment, not a hand-copied grid.
    accept_tree=ast.parse((copies/"accept_initial47.py").read_text())
    params=[s for s in accept_tree.body if isinstance(s,ast.Assign) and len(s.targets)==1 and isinstance(s.targets[0],ast.Name) and s.targets[0].id=="P"]
    need(len(params)==1,"fixed native parameter assignment")
    env={"F":Fraction}; exec(compile(ast.Module(body=params,type_ignores=[]),"native parameter assignment","exec"),env)
    P=env["P"]
    projection, boundary=make_projection((copies/"local_signed_core.py").read_text())
    (run/"prefix_only.py").write_text(projection)
    sys.path.insert(0,str(copies))
    spec=importlib.util.spec_from_file_location("prefix_only",run/"prefix_only.py")
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    # A tripwire rejects accidental execution of a numerical Fourier stage.
    def forbidden(*args,**kwargs): raise RuntimeError("out-of-scope Fourier call")
    mod.k.sixth=forbidden; mod.k.high=forbidden; mod.k.universal_high=forbidden
    started={"scope":"PREFIX_ONLY_NOT_CERTIFICATE_ACCEPTANCE","source_pins":inputs,"projection":boundary,"projection_sha256":sha(run/"prefix_only.py"),"driver_sha256":sha(Path(__file__)),"runtime":{"executable":sys.executable,"executable_sha256":sha(Path(sys.executable).resolve()),"version":sys.version,"platform":platform.platform(),"optimized":sys.flags.optimize},"parameters":{k:enc(v) for k,v in P.items()}}
    (run/"STARTED.json").write_text(json.dumps(started,indent=2)+"\n")
    states=[(None,None)]+[(Fraction(s["raw"]),Fraction(s["defect"])) for s in proof["steps"]]
    totals=[]; count=0; t0=time.monotonic()
    with (run/"cells.jsonl.gz").open("xb") as rawfile, gzip.GzipFile(fileobj=rawfile,mode="wb",mtime=0) as stream:
        for stage_no,(raw,d) in enumerate(states):
            before=count
            def capture(local):
                nonlocal count
                row={"stage":stage_no,"cell":{k:enc(local[k]) for k in FIELDS}}
                stream.write((json.dumps(row,sort_keys=True,separators=(",",":"))+"\n").encode()); count+=1
            mod.capture=capture
            result=mod.stage(P,raw,d)
            need(result["prefix_active"]==count-before,"every reached prefix captured")
            result.update(stage=stage_no,raw=enc(raw),defect=enc(d)); totals.append(result)
            print(json.dumps(result,sort_keys=True),flush=True)
    result={"status":"COMPLETE_ALGEBRA_PREFIX_CAPTURE_ONLY","states":len(states),"rows":count,"grid_cells":sum(x["total"] for x in totals),"stages":totals,"seconds":time.monotonic()-t0,"cells_sha256":sha(run/"cells.jsonl.gz"),"source_hashes_unchanged":all(sha(SOURCE/n)==v["sha256"] for n,v in inputs.items()),"fourier_evaluations":0,"certificate_acceptance_claimed":False,"feedback_states_reaccepted":False}
    need(result["source_hashes_unchanged"],"native sources unchanged")
    (run/"RESULT.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="stages"},sort_keys=True),flush=True)


if __name__=="__main__": main()
