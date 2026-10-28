#!/usr/bin/env python3
"""Bounded acceptor tests and independent saved-panel reconstruction.

Only the acceptor's pure validation functions are loaded by AST selection.
No constructor, ancestor, support or Fourier module is imported or executed.
"""
import argparse
import ast
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


def need(ok, why):
    if not ok: raise ValueError(why)


def ceil8(x):
    return F(-((-x.numerator*10**8)//x.denominator), 10**8)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source-root',type=Path,default=Path('.'));args=ap.parse_args()
    root=args.source_root; here=root/'mathematics/fixed-target-v7/2026-10-27'
    raw=(here/'accept_entry.py').read_bytes();tree=ast.parse(raw)
    fnames={'need','fields','unique','rat','shape','check_row','check_panels'}
    cnames={'PINS','PRELOAD_PINS','NAME','C0','C1','KEYS'}
    nodes=[]
    for n in tree.body:
        if isinstance(n,ast.FunctionDef) and n.name in fnames:nodes.append(n)
        elif isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in cnames for x in n.targets for t in ast.walk(x)):nodes.append(n)
    ns={'F':F};exec(compile(ast.Module(body=nodes,type_ignores=[]),'<pure-entry-validation>','exec'),ns)
    for f,pin in ns['PINS'].items():need(sha256((here/f).read_bytes()).hexdigest()==pin,'direct source pin')
    need(len(ns['PRELOAD_PINS'])==9,'nine transitive preflight pins')
    for f,pin in ns['PRELOAD_PINS'].items():need(sha256((root/f).read_bytes()).hexdigest()==pin,'transitive source pin')
    proof=json.loads((here/'entry-proof.json').read_text(),object_pairs_hook=ns['unique']);ns['shape'](proof)
    source=root/'runs/fixed-target-v7-20261027/signed07/stdout.json'
    discovery=json.loads(source.read_text(),object_pairs_hook=ns['unique'])
    keys=ns['KEYS'];pooled=[dict(pl=F(j,100),pu=F(j+1,100),raw=F(-1),D=F(-1),theta=F(0),rho=F(1),beta=F(0),H=F(0),cells=0)for j in range(100)]
    tested=0;last=None
    for stage,rows in enumerate(proof['steps']):
        for i,r in enumerate(rows):
            saved=discovery['history'][stage]['rows'][i]
            if r.get('prior_excluded'):
                need(saved==r,'excluded identity reconstruction');continue
            out=deepcopy(saved['output']);out['R']=F(out['R']);out['D']=F(out['D'])
            ns['check_row'](r,out,F(saved['prior_raw']),F(saved['prior_defect']))
            need(F(r['radius'])==F(saved['radius']),'saved support radius equality')
            tested+=128
            if stage==3 and out['active']:
                if last is None:last=(i,out,F(saved['prior_raw']),F(saved['prior_defect']))
                need(len(out['panels'])==100,'saved full panel census')
                for j,p in enumerate(out['panels']):
                    need(F(p['pl'])==F(j,100) and F(p['pu'])==F(j+1,100),'saved closed endpoints')
                    pooled[j]['cells']+=p['cells']
                    for k in keys:pooled[j][k]=max(pooled[j][k],F(p[k]))
    ns['check_panels'](proof['panels'],pooled)
    need(tested==11264,'four-pass scheduled signed census')
    for target,p in zip(proof['panels'],pooled):
        need(all(F(target[k])==ceil8(p[k])for k in keys),'exported outward rounding')
    rejected=[]
    def reject(name,fn,expected=None):
        try:fn()
        except ValueError as e:
            if expected is not None:need(str(e)==expected,'intended rejection layer: '+name)
            rejected.append(dict(name=name,reason=str(e)));return
        raise ValueError('mutation accepted: '+name)
    loc=next((j,i)for j,rows in enumerate(proof['steps'])for i,r in enumerate(rows)if r.get('prior_excluded'))
    mutations=[
      ('numeric excluded flag',lambda z:z['steps'][loc[0]][loc[1]].update(prior_excluded=1)),
      ('floating excluded index',lambda z:z['steps'][loc[0]][loc[1]].update(index=float(loc[1]))),
      ('extra excluded field',lambda z:z['steps'][loc[0]][loc[1]].update(extra=0)),
      ('missing stage',lambda z:z['steps'].pop()),
      ('legacy theorem name',lambda z:z.update(name='INITIAL42_R384')),
      ('bad source binding',lambda z:z['source_pins'].update({'signed_core.py':'0'*64})),
      ('open probability seam',lambda z:z['panels'][12].update(pl='1/8')),
      ('duplicate probability panel',lambda z:z['panels'].__setitem__(12,z['panels'][11])),
      ('boolean incidence',lambda z:z['panels'][0].update(cells=False)),
      ('noncanonical zero',lambda z:z['panels'][0].update(pl='0/1')),
    ]
    for name,mut in mutations:
        bad=deepcopy(proof);mut(bad);reject(name,lambda:ns['shape'](bad))
    i,out,oldraw,oldd=last
    bad=deepcopy(proof);bad['steps'][3][i]['raw']=str(ceil8(out['R']/2));ns['shape'](bad)
    reject('arithmetically false raw ceiling',lambda:ns['check_row'](bad['steps'][3][i],out,oldraw,oldd),'outward ordered scalar outputs')
    j=next(j for j,p in enumerate(pooled)if p['cells'] and p['H']>0)
    bad=deepcopy(proof);bad['panels'][j]['H']=str(ceil8(pooled[j]['H']/2));ns['shape'](bad)
    reject('arithmetically false phase ceiling',lambda:ns['check_panels'](bad['panels'],pooled),'outward panel H')
    bad=deepcopy(proof);bad['panels'][j]['cells']+=1;ns['shape'](bad)
    reject('false incidence count',lambda:ns['check_panels'](bad['panels'],pooled),'all probability incidences')
    reject('duplicate JSON key',lambda:json.loads('{"x":0,"x":1}',object_pairs_hook=ns['unique']),'duplicate JSON key')
    def enc(x):
        if isinstance(x,F):return str(x)
        if isinstance(x,dict):return{k:enc(v)for k,v in x.items()}
        if isinstance(x,list):return[enc(v)for v in x]
        return x
    print(json.dumps(enc(dict(status='PASS_BOUNDED_SCHEMA_AND_POOL_REVIEW',signed_cells=tested,
       probability_panels=len(pooled),nonempty_probability_panels=sum(p['cells']>0 for p in pooled),
       panel_incidences=sum(p['cells']for p in pooled),panel_ceilings={k:max(F(p[k])for p in proof['panels'])for k in keys},
       rejected_controls=rejected,source_sha256={str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest()for p in [here/'accept_entry.py',here/'entry-proof.json',here/'export_entry.py',source]},
       direct_pins=ns['PINS'],preload_pins=ns['PRELOAD_PINS'],
       limitations='Pure validation tests plus saved-result accounting; no full acceptor, signed arithmetic or Fourier replay.')),indent=2,sort_keys=True))


if __name__=='__main__':main()
