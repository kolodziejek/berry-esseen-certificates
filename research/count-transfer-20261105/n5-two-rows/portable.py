"""Portable orchestration only; unchanged exact readers perform all arithmetic."""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys
BASE=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def need(ok,why):
    if not ok:raise ValueError(why)
def unique(items):
    result={}
    for k,v in items:
        need(k not in result,'duplicate JSON key');result[k]=v
    return result
def read(p):return json.loads(p.read_text(),object_pairs_hook=unique)
def verify():
    need(not sys.flags.optimize,'optimized Python is not supported')
    manifest=read(BASE/'FILES.json');need(set(manifest)=={'schema','files'},'file inventory schema')
    need(manifest['schema']=='N5_TRANSFER_PORTABLE_FILES_V1','file inventory version')
    seen=set()
    for z in manifest['files']:
        need(type(z)is dict and set(z)=={'path','size','sha256'},'file inventory row')
        rel=Path(z['path']);need(not rel.is_absolute()and '..'not in rel.parts and str(rel)not in seen,'safe unique inventory path')
        seen.add(str(rel));p=BASE/rel
        need(not any((BASE/Path(*rel.parts[:i])).is_symlink()for i in range(1,len(rel.parts)+1)),'no symlinks')
        need(p.is_file()and p.stat().st_size==z['size']and sha(p)==z['sha256'],'inventory bytes: '+str(rel))
    actual={str(p.relative_to(BASE))for p in BASE.rglob('*')if p.is_file()}
    need(actual==seen|{'FILES.json'},'complete file inventory')
    targets=read(BASE/'TARGETS.json');need(set(targets)=={'schema','rows'}and targets['schema']=='N5_TRANSFER_PORTABLE_TARGETS_V1','target inventory')
    need([z['row_id']for z in targets['rows']]==['B0_50','B2_S3_34'],'fixed completed row set')
    return targets

def main():
    ap=argparse.ArgumentParser();ap.add_argument('action',choices=['verify','replay','smoke','controls']);ap.add_argument('--row',choices=['B0_50','B2_S3_34']);ap.add_argument('--out',type=Path);a=ap.parse_args()
    targets=verify()
    if a.action=='verify':print(json.dumps({'status':'PASS_ALL_PORTABLE_BYTES','files':len(read(BASE/'FILES.json')['files'])}));return
    need(a.out is not None,'fresh external output required');out=a.out.resolve();need(not out.is_relative_to(BASE),'output must be outside immutable package');out.mkdir(parents=True,exist_ok=False)
    if a.action=='smoke':
        z=next(z for z in targets['rows']if z['row_id']=='B2_S3_34');o=next(o for o in z['roots']if o['k']==3)
        cmd=[sys.executable,'-I','-B',str(BASE/'code/accept.py'),str(BASE/o['object']),str(out/'accepted'),'--row',z['row_id'],'--k','3']
        inputs=[BASE/o['object']]
    else:
        need(a.row is not None or a.action=='controls','explicit completed row required');key='B2_S3_34'if a.action=='controls'else a.row;z=next(z for z in targets['rows']if z['row_id']==key)
        selection={'schema':'N5_TRANSFER_ROOT_SELECTION_V1','row_id':z['row_id'],'contract_sha256':z['contract_sha256'],'roots':[dict(k=o['k'],object=str(BASE/o['object']),sha256=o['sha256'])for o in z['roots']]}
        s=out/'SELECTION.json';s.write_text(json.dumps(selection,indent=2)+'\n')
        cmd=[sys.executable,'-I','-B',str(BASE/'code/accept_row.py'),str(s),str(out/'accepted'),'--row',key];inputs=[s]+[BASE/o['object']for o in z['roots']]
        if a.action=='controls':
            obj=next(o for o in z['roots']if o['k']==3);cmd=[sys.executable,'-I','-B',str(BASE/'code/controls.py'),str(BASE/obj['object']),str(s),str(out/'accepted')]
    source=[p for p in (BASE/'code').rglob('*')if p.is_file()]+[BASE/'FILES.json',BASE/'TARGETS.json',Path(__file__)]
    capture=[sys.executable,'-I','-B',str(BASE/'tools/capture_process.py')]
    for p in source+inputs:capture+=['--input',str(p)]
    rc=subprocess.call(capture+[str(out/'capture'),'--']+cmd)
    need(rc==0,'fresh arithmetic replay failed')
    verify()
if __name__=='__main__':main()
