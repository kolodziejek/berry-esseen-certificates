"""Portable complete BN39 replay; no historical success record admits a leaf."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys
BASE=Path(__file__).resolve().parent

def need(x,s):
    if not x:raise ValueError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def unique(items):
    d={}
    for k,v in items:need(k not in d,'duplicate key');d[k]=v
    return d
def read(p):return json.loads(p.read_text(),object_pairs_hook=unique)
def verify():
    need(not sys.flags.optimize,'optimized Python unsupported');mf=read(BASE/'FILES.json')
    need(set(mf)=={'schema','files'}and mf['schema']=='N5_BN39_MIXED_PORTABLE_FILES_V1','inventory version')
    seen=set()
    for z in mf['files']:
        need(type(z)is dict and set(z)=={'path','size','sha256'},'inventory entry');rel=Path(z['path'])
        need(not rel.is_absolute()and '..'not in rel.parts and str(rel)not in seen,'unique safe path');seen.add(str(rel))
        need(not any((BASE/Path(*rel.parts[:i])).is_symlink()for i in range(1,len(rel.parts)+1)),'no source links')
        p=BASE/rel;need(p.is_file()and p.stat().st_size==z['size']and sha(p)==z['sha256'],'file bytes '+str(rel))
    need({str(p.relative_to(BASE))for p in BASE.rglob('*')if p.is_file()}==seen|{'FILES.json'},'complete file inventory')
    target=read(BASE/'TARGET.json');need(set(target)=={'schema','row_id','contract_sha256','roots','control_patch'}and target['schema']=='N5_BN39_MIXED_PORTABLE_TARGET_V1'and target['row_id']=='BN39','fixed BN39 target')
    need([z['k']for z in target['roots']]==[1,2,3],'complete root inventory');return target

def main():
    ap=argparse.ArgumentParser();ap.add_argument('action',choices=['verify','replay','controls','smoke']);ap.add_argument('--out',type=Path);a=ap.parse_args();target=verify()
    if a.action=='verify':print(json.dumps(dict(status='PASS_ALL_BN39_PORTABLE_BYTES',files=len(read(BASE/'FILES.json')['files']))));return
    need(a.out is not None,'fresh output required');out=a.out.resolve();need(not out.is_relative_to(BASE),'output outside immutable package');out.mkdir(parents=True,exist_ok=False)
    inputs=[BASE/'FILES.json',BASE/'TARGET.json',Path(__file__)]+[p for p in(BASE/'code').rglob('*')if p.is_file()]
    if a.action=='replay':
        selection=dict(schema='N5_TRANSFER_ROOT_SELECTION_V1',row_id='BN39',contract_sha256=target['contract_sha256'],roots=[dict(k=z['k'],object=str(BASE/z['object']),sha256=z['sha256'])for z in target['roots']]);s=out/'SELECTION.json';s.write_text(json.dumps(selection,indent=2)+'\n')
        cmd=[sys.executable,'-I','-B',str(BASE/'code/accept_mixed.py'),str(s),str(out/'accepted')];inputs+=[s]+[BASE/z['object']for z in target['roots']]
    elif a.action=='controls':
        p=BASE/target['control_patch'];cmd=[sys.executable,'-I','-B',str(BASE/'code/controls_mixed.py'),str(p),str(out/'accepted')];inputs+=[p]
    else:
        p=BASE/next(z['object']for z in target['roots']if z['k']==3);cmd=[sys.executable,'-I','-B',str(BASE/'code/accept.py'),str(p),str(out/'accepted'),'--row','BN39','--k','3'];inputs+=[p]
    capture=[sys.executable,'-I','-B',str(BASE/'tools/capture_process.py')]
    for p in inputs:capture+=['--input',str(p)]
    rc=subprocess.call(capture+[str(out/'capture'),'--']+cmd);need(rc==0,'fresh exact arithmetic failed');verify()
if __name__=='__main__':main()
