#!/usr/bin/env python3
"""Acceptance for INITIAL42_FIXED_TARGET_COARSE_V7, not legacy INITIAL42.

Four fixed signed passes from the two-quadratic ancestor, with exact replay.
No discovery decisions or external supplied source paths are accepted.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from copy import deepcopy
import importlib.util,json,sys,argparse
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
PINS={'signed_core.py':'1f40ccb90eb58a7f84dc61a0a5dd9bf6e6eb4e341aa6c9c6d049d08451f5211b','signed_support.py':'eecb06e65d8520d7cc06fc34217e06e1c0b1840dd8d687621e6828923769a4c4'}
NAME='INITIAL42_FIXED_TARGET_COARSE_V7'
C0,C1=F('.4097321837023'),F('.4097321837025')
KEYS=('raw','D','theta','rho','beta','H')
def need(v,s):
    if not v:raise ValueError(s)
def fields(o,keys):need(type(o)is dict and set(o)==set(keys),'exact fields')
def unique(pairs):
    d={}
    for k,v in pairs:
        need(k not in d,'duplicate JSON key');d[k]=v
    return d
def rat(x):
    need(type(x)is str and len(x)<150,'bounded rational text');v=F(x);need(str(v)==x,'canonical rational');return v
def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x
def ceil(x):return F(-((-x.numerator*10**8)//x.denominator),10**8)
def modules():
    need(__debug__ and not sys.flags.optimize,'unoptimized interpreter')
    for f,h in PINS.items():need(sha256((HERE/f).read_bytes()).hexdigest()==h,'reviewed source '+f)
    import signed_core as core
    import signed_support as support
    path=ROOT/'mathematics/fixed-target-v6/2026-10-27/signed-two-pass-check.py'
    spec=importlib.util.spec_from_file_location('accepted_two_quadratic_ancestor',path)
    ancestor=importlib.util.module_from_spec(spec);spec.loader.exec_module(ancestor)
    return core,support,ancestor

def shape(o):
    fields(o,('format','name','source_pins','steps','panels'))
    need(o['format']=='FIXED_C_COARSE_ENTRY_V7' and o['name']==NAME,'distinct fixed-target theorem')
    need(o['source_pins']==PINS,'fixed reviewed sources')
    need(type(o['steps'])is list and len(o['steps'])==4,'four fixed passes')
    prior_empty=set()
    for j,rows in enumerate(o['steps']):
        need(type(rows)is list and len(rows)==24,'all rho identities')
        for i,r in enumerate(rows):
            if i in prior_empty:
                need(r==dict(index=i,prior_excluded=True),'persistent excluded cell');continue
            fields(r,('index','radius','raw','defect','active','excluded'))
            need(type(r['index'])is int and r['index']==i,'ordered rho identity')
            need(type(r['active'])is int and type(r['excluded'])is int and r['active']>=0 and r['excluded']>=0 and r['active']+r['excluded']==128,'complete signed census')
            need(F(5,2)<=rat(r['radius'])<=F(96,25),'licensed radius interval')
            T,d=rat(r['raw']),rat(r['defect']);l=1+F(3361*i,96000)
            if r['active']:
                need(0<T<42*C0*l and 0<d<4,'ordered license domain')
                if j==3:need(T<F('2.24') and d<F('.784'),'unchanged resource targets')
            else:
                need(T==d==-1,'empty cell sentinel');prior_empty.add(i)
    need(type(o['panels'])is list and len(o['panels'])==100,'full probability cover')
    for j,z in enumerate(o['panels']):
        fields(z,('pl','pu',*KEYS,'cells'))
        need(rat(z['pl'])==F(j,100) and rat(z['pu'])==F(j+1,100),'closed probability endpoints')
        need(type(z['cells'])is int and z['cells']>=0,'integer incidence count')
        vals={k:rat(z[k]) for k in KEYS}
        if z['cells']:
            need(0<vals['raw']<F('2.24') and 0<vals['D']<F('.784'),'panel resource targets')
            need(0<=vals['theta']<1 and 1<=vals['rho']<F('1.526') and 0<=vals['beta']<F('.523') and 0<vals['H']<F('1.947'),'panel moment targets')
        else:need([vals[k] for k in KEYS]==[F(-1),F(-1),F(0),F(1),F(0),F(0)],'empty panel sentinel')

def blank_panels():
    return [dict(pl=F(j,100),pu=F(j+1,100),raw=F(-1),D=F(-1),theta=F(0),rho=F(1),beta=F(0),H=F(0),cells=0) for j in range(100)]
def pool(target,source):
    need(len(source)==100,'kernel probability cover')
    for j,(t,s) in enumerate(zip(target,source)):
        need(s['pl']==F(j,100) and s['pu']==F(j+1,100),'kernel endpoints')
        need(type(s['cells'])is int and s['cells']>=0,'kernel incidences')
        t['cells']+=s['cells']
        for k in KEYS:t[k]=max(t[k],s[k])
def check_row(r,out,oldraw,oldd):
    need(r['active']==out['active'] and r['excluded']==out['excluded'] and out['total']==128,'replayed complete signed cover')
    need(sum(out['reasons'].values())==out['excluded'],'reason census')
    if out['active']:
        T,d=rat(r['raw']),rat(r['defect'])
        need(out['R']<=T<=oldraw and out['D']<=d<=oldd,'outward ordered scalar outputs')
def check_panels(target,actual):
    for t,a in zip(target,actual):
        need(t['cells']==a['cells'],'all probability incidences')
        for k in KEYS:need(rat(t[k])>=a[k],'outward panel '+k)

def verify(o):
    shape(o);core,support,ancestor=modules()
    initial=ancestor.run(ROOT/'mathematics/fixed-target-v6/2026-10-27/moment_check.py')
    need(len(initial['rows'])==24,'ancestor cover')
    states=[]
    for i,r in enumerate(initial['rows']):
        l,u=1+F(3361*i,96000),1+F(3361*(i+1),96000)
        need(r['index']==i and r['rho_lower']==l and r['rho_upper']==u,'ancestor endpoints')
        z=r['passes'][-1];states.append(dict(l=l,u=u,raw=z['raw'],d=z['defect'],empty=False))
    evidence=[];total=0;panels=blank_panels()
    for j,rows in enumerate(o['steps']):
        trace=[]
        for i,(r,st) in enumerate(zip(rows,states)):
            if st['empty']:continue
            radius,_,_=support.cell_radius(st['u'])
            need(rat(r['radius'])==radius,'recomputed contact support gate')
            p=dict(n=42,nmax=42,radius=radius,barrier=F(0),cap=C1,c_lower=C0,c_upper=C1,grid=[1,8,8,2],rho_lower=st['l'],rho_upper=st['u'])
            out=core.stage(p,st['raw'],st['d']);check_row(r,out,st['raw'],st['d'])
            trace.append((i,out,st['raw'],st['d']));total+=128
            if out['active']:
                st['raw'],st['d']=rat(r['raw']),rat(r['defect'])
                if j==3:pool(panels,out['panels'])
            else:st['empty']=True
        evidence.append(trace)
        print('PASS_SIGNED_ENTRY_STAGE',j+1,'rho_cells',sum(not s['empty'] for s in states),file=sys.stderr,flush=True)
    check_panels(o['panels'],panels)
    active=[s for s in states if not s['empty']];need(active,'nonempty conditional entry')
    summary=dict(raw=max(s['raw'] for s in active),D=max(s['d'] for s in active),weighted_nD=42*max(s['d'] for s in active),
        rho=max(s['u'] for s in active),beta=max(z['beta'] for z in panels),H=max(z['H'] for z in panels),theta=max(z['theta'] for z in panels),
        signed_cells=total,remaining_rho_cells=len(active),probability_panels=100,nonempty_probability_panels=sum(z['cells']>0 for z in panels))
    rejected=[]
    def reject(name,fn):
        try:fn()
        except (ValueError,TypeError,ZeroDivisionError):rejected.append(name)
        else:raise ValueError('negative control accepted: '+name)
    mutations=[('missing stage',lambda z:z['steps'].pop()),('missing rho row',lambda z:z['steps'][0].pop()),
      ('duplicate rho row',lambda z:z['steps'][0].__setitem__(1,z['steps'][0][0])),('reordered rho rows',lambda z:z['steps'][0].reverse()),
      ('lost cell',lambda z:z['steps'][0][0].update(excluded=z['steps'][0][0]['excluded']-1)),
      ('wrong theorem',lambda z:z.update(name='INITIAL42_R384')),('unknown field',lambda z:z.update(extra=1)),
      ('wrong source pin',lambda z:z['source_pins'].update({'signed_core.py':'0'*64})),
      ('missing panel',lambda z:z['panels'].pop()),('reordered panels',lambda z:z['panels'].reverse()),
      ('broken shared endpoint',lambda z:z['panels'][0].update(pu='1/50')),
      ('noncanonical rational',lambda z:z['panels'][0].update(pl='00')),
      ('boolean incidence',lambda z:z['panels'][0].update(cells=False))]
    for name,mut in mutations:
        bad=deepcopy(o);mut(bad);reject(name,lambda:shape(bad))
    i,out,oldraw,oldd=next(t for t in evidence[-1] if t[1]['active'] and t[1]['R']>0)
    bad=deepcopy(o['steps'][-1][i]);bad['raw']=str(out['R']/2)
    reject('false last raw ceiling',lambda:check_row(bad,out,oldraw,oldd))
    bad=deepcopy(o['panels']);j=next(j for j,z in enumerate(panels) if z['cells'] and z['H']>0);bad[j]['H']=str(panels[j]['H']/2)
    reject('false last panel phase',lambda:check_panels(bad,panels))
    bad=deepcopy(o['panels']);bad[j]['cells']+=1
    reject('false incidence count',lambda:check_panels(bad,panels))
    reject('duplicate JSON key',lambda:json.loads('{"x":1,"x":2}',object_pairs_hook=unique))
    return dict(status='PASS_INITIAL42_FIXED_TARGET_COARSE_V7',mathematical_status='Conditional on the named fixed-target contact, conservation, support and moment/gap premises; not LOCAL42 or BASE41.',
        summary=summary,rejected_controls=rejected,source_pins=PINS)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('proof',type=Path);args=ap.parse_args()
    blob=args.proof.read_bytes();o=json.loads(blob,object_pairs_hook=unique);out=verify(o);out['proof_sha256']=sha256(blob).hexdigest()
    print(json.dumps(encode(out),indent=2))
