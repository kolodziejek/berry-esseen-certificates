"""Portable complete 32-contract n=5 BN-band all-Taylor replay; no historical success record admits a leaf."""
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
    need(__debug__ and not sys.flags.optimize,'optimized Python unsupported');mf=read(BASE/'FILES.json')
    need(set(mf)=={'schema','files'}and mf['schema']=='N5_BN_BAND_PORTABLE_FILES_V1','inventory version')
    seen=set()
    for z in mf['files']:
        need(type(z)is dict and set(z)=={'path','size','sha256'},'inventory entry');rel=Path(z['path'])
        need(not rel.is_absolute()and '..'not in rel.parts and str(rel)not in seen,'unique safe path');seen.add(str(rel))
        need(not any((BASE/Path(*rel.parts[:i])).is_symlink()for i in range(1,len(rel.parts)+1)),'no source links')
        p=BASE/rel;need(p.is_file()and p.stat().st_size==z['size']and sha(p)==z['sha256'],'file bytes '+str(rel))
    need({str(p.relative_to(BASE))for p in BASE.rglob('*')if p.is_file()}==seen|{'FILES.json'},'complete file inventory')
    target=read(BASE/'TARGET.json')
    need(set(target)=={'schema','catalogue_sha256','control_root_object','rows'}and target['schema']=='N5_BN_BAND_PORTABLE_TARGET_V1','fixed BN-band target')
    need(len(target['rows'])==32,'complete 32-contract BN-band target inventory')
    return target

def main():
    ap=argparse.ArgumentParser();ap.add_argument('action',choices=['verify','replay','controls','smoke'])
    ap.add_argument('--out',type=Path);ap.add_argument('--row');a=ap.parse_args();target=verify()
    if a.action=='verify':
        print(json.dumps(dict(status='PASS_ALL_N5_BN_BAND_PORTABLE_BYTES',files=len(read(BASE/'FILES.json')['files']),rows=len(target['rows']))));return
    need(a.out is not None,'fresh output required');out=a.out.resolve();need(not out.is_relative_to(BASE),'output outside immutable package');out.mkdir(parents=True,exist_ok=False)
    inputs=[BASE/'FILES.json',BASE/'TARGET.json',Path(__file__)]+[p for p in(BASE/'code').rglob('*')if p.is_file()]+[p for p in(BASE/'contracts').rglob('*')if p.is_file()]
    if a.action=='replay':
        rows_cfg=[r for r in target['rows']if a.row is None or r['row_id']==a.row]
        need(len(rows_cfg)>=1,'known target row')
        if a.row is not None:
            r=rows_cfg[0]
            sel=dict(schema='N5_ALL_TAYLOR_ROW_SELECTION_V1',selector=r['selector'],row_id=r['row_id'],contract_path=r['contract_path'],contract_sha256=r['contract_sha256'],
              roots=[dict(k=z['k'],object=str(BASE/z['object']),sha256=z['sha256'])for z in r['roots']])
            s=out/'SELECTION.json';s.write_text(json.dumps(sel,indent=2)+'\n')
            cmd=[sys.executable,'-I','-B','-S',str(BASE/'code/accept_bn_band.py'),str(s),str(out/'accepted'),'--mode','row']
            inputs+=[s]+[BASE/z['object']for z in r['roots']]
        else:
            sel=dict(schema='N5_ALL_TAYLOR_MULTI_ROW_SELECTION_V1',rows=[
              dict(schema='N5_ALL_TAYLOR_ROW_SELECTION_V1',selector=r['selector'],row_id=r['row_id'],contract_path=r['contract_path'],contract_sha256=r['contract_sha256'],
                roots=[dict(k=z['k'],object=str(BASE/z['object']),sha256=z['sha256'])for z in r['roots']])for r in rows_cfg])
            s=out/'SELECTION.json';s.write_text(json.dumps(sel,indent=2)+'\n')
            cmd=[sys.executable,'-I','-B','-S',str(BASE/'code/accept_bn_band.py'),str(s),str(out/'accepted'),'--mode','multi']
            inputs+=[s]+[BASE/z['object']for r in rows_cfg for z in r['roots']]
    elif a.action=='controls':
        p=BASE/target['control_root_object']
        cmd=[sys.executable,'-I','-B','-S',str(BASE/'code/controls_bn_band.py'),str(p),str(out/'accepted')];inputs+=[p]
    else:
        p=BASE/target['control_root_object']
        cmd=[sys.executable,'-I','-B','-S',str(BASE/'code/accept_bn_band.py'),str(p),str(out/'accepted'),'--mode','root','--row','BN_039','--k','3'];inputs+=[p]
    capture=[sys.executable,'-I','-B','-S',str(BASE/'tools/capture_process.py')]
    for p in sorted(set(inputs)):capture+=['--input',str(p)]
    rc=subprocess.call(capture+[str(out/'capture'),'--']+cmd);need(rc==0,'fresh exact arithmetic failed');verify()

if __name__=='__main__':main()
