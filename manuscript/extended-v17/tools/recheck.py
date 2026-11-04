"""Bounded checks of the unchanged v16 inputs plus the compact source graph.
No Fourier generation, finite-base acceptance or full-conjecture claim.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime,hashlib,json,re,subprocess,sys,time
here=Path(__file__).resolve().parents[1]
root=here.parents[1]
source=root/'mathematics/simplification-v16/2026-10-29'
out=here/(sys.argv[1] if len(sys.argv)>1 else 'checks')
out.mkdir(exist_ok=False)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pins=json.loads((source/'reviewed-sources.json').read_text())
assert all(sha(root/k)==v for k,v in pins.items())
files=[]
def expand(p):
    files.append(p)
    return re.sub(r'\\input\{([^}]+)\}',lambda m:expand(here/(m[1]+'.tex')),p.read_text(encoding='utf-8'))
text=expand(here/'main.tex')
labels=re.findall(r'\\label\{([^}]+)\}',text)
refs=re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}',text)
assert not(set(refs)-set(labels))
assert len(set(labels))==len(labels)
assert all(text.count('\\begin{'+x+'}')==text.count('\\end{'+x+'}') for x in ['theorem','proof','lemma','proposition','corollary','equation','align','gather'])
keys=set()
for p in here.glob('*.bib'):
    keys.update(re.findall(r'@\w+\s*\{\s*([^,]+),',p.read_text(encoding='utf-8')))
cites=[]
for m in re.finditer(r'\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}',text):
    cites.extend(x.strip() for x in m[1].split(','))
assert not(set(cites)-keys)
jobs=[(n,[])for n in ['acquisition-check.py','unified-check.py','unified-actual.py','small-check.py','small-review-actual.py','counts-check.py']]
jobs += [('small-review-check.py',['--proof',str(source/'small-common.tex')]),('unified-review-check.py',[str(root)]),('acquisition-review.py',['--source-root',str(root)])]
def run(item):
    name,args=item
    cmd=[sys.executable,'-X','int_max_str_digits=0','-I','-B',str(source/name),*args]
    t=time.monotonic()
    r=subprocess.run(cmd,cwd=root,capture_output=True,timeout=180)
    (out/(name+'.stdout.json')).write_bytes(r.stdout)
    (out/(name+'.stderr.txt')).write_bytes(r.stderr)
    obj=json.loads(r.stdout) if r.returncode==0 else {}
    status=obj.get('status',obj.get('result','FAILED'))
    record={'command':cmd,'returncode':r.returncode,'seconds':time.monotonic()-t,'status':status,'source_sha256':sha(source/name),'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(r.stderr).hexdigest()}
    print(json.dumps({'check':name,'status':status,'returncode':r.returncode}),flush=True)
    return name,record
with ThreadPoolExecutor(max_workers=3) as pool:
    records=dict(pool.map(run,jobs))
assert all(sha(root/k)==v for k,v in pins.items())
ok=all(x['returncode']==0 and x['status'].startswith('PASS') for x in records.values())
receipt={'status':'PASS_COMPACT_V16_BOUNDED_RECHECK'if ok else'FAILED','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':sys.version,'scope':'Nine unchanged v16 mathematical bounded checks and compact TeX labels, citations and environment balance. No complete source-ancestry replay, finite-base acceptance or full theorem. Historical preservation.py is not run: its old no-new-manuscript-files scope is intentionally inapplicable to this new parallel manuscript. Original tracked files are checked separately.','source_pin':'1aa1dd015e3d73fbeecc1a7acbfa395cbb560b5f','checks':records,'tex_files':len(files),'labels':len(labels),'citations':len(set(cites)),'compact_tex_sha256':{str(p.relative_to(here)):sha(p) for p in files},'reviewed_inputs_sha256':pins}
(out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':receipt['status'],'checks':len(records)}))
assert ok
