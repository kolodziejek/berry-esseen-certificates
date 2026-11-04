"""Complete fixed267 finite input/normalization and joint-count polynomial reader."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from model import CASE_IDS,need,unique,sha
from accept import expanded_basis,fields,fraction
from finite_native import rows,FAMILIES,SPECS
from finite_targets import parameterized_targets,scalar_gate

@lru_cache(None)
def tensors(nx,ny):
    return [[{(i,j):int(a*b)for i,a in expanded_basis(nx,k).items()for j,b in expanded_basis(ny,l).items()}
             for l in range(ny+1)]for k in range(nx+1)]

def polynomial_check(p,encoded):
    nx=max(i for i,j in p);ny=max(j for i,j in p)
    need(type(encoded)is list and len(encoded)==nx+1,'full finite coefficient row census')
    need(all(type(row)is list and len(row)==ny+1 for row in encoded),'full finite coefficient column census')
    values=[[fraction(v)for v in row]for row in encoded];minimum=min(map(min,values))
    need(minimum>=0,'finite continuous rectangle positivity')
    result={};basis=tensors(nx,ny)
    for k,row in enumerate(values):
        for l,v in enumerate(row):
            for exponent,w in basis[k][l].items():result[exponent]=result.get(exponent,F(0))+v*w
    result={k:v for k,v in result.items()if v}
    need(result==p,'finite complete inverse polynomial identity')
    return {'degree':[nx,ny],'coefficient_count':(nx+1)*(ny+1),'minimum':str(minimum)}

def plain(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:plain(v)for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [plain(v)for v in x]
    return x

def accept_object(obj):
    need(not sys.flags.optimize and __debug__,'unoptimized finite acceptance required')
    fields(obj,('schema','score_targets','rows'))
    need(obj['schema']=='FINITE267_JOINT_COUNT_TINY_V1','fixed finite proof schema')
    need(obj['score_targets']=='unchanged native sharp, positive39 and finite-binomial-reserve targets','all original finite score targets')
    expected_order=[(family,i)for family in FAMILIES for i in range(SPECS[family][0])]
    need(type(obj['rows'])is list and [(r.get('family'),r.get('index'))for r in obj['rows']]==expected_order,'complete ordered267finitecover')
    need(all(type(r['index'])is int for r in obj['rows']),'strict finite row indices')
    native=rows();records=[]
    for proposed,record in zip(obj['rows'],native):
        fields(proposed,('family','index','eta','cases'))
        need(proposed['eta']in('1/10','1/20','0','-1/20','-1/10'),'fixed finite loss-witness choices')
        eta=F(proposed['eta']);c=record['c']
        need(0<c['mass']<=1 and 0<c['ownlo']<=c['ownhi'] and c['repair']>=0,'explicit finite mass, variance and repair signs')
        targets=parameterized_targets(c,eta)
        need(type(proposed['cases'])is list and [x.get('id')for x in proposed['cases']]==list(CASE_IDS),'all four finite branches in fixed order')
        checks=[]
        for case in proposed['cases']:
            fields(case,('id','coefficients'));checks.append({'id':case['id'],**polynomial_check(targets[case['id']],case['coefficients'])})
        gate=scalar_gate(c,eta,record['gate_kind']);need(gate>0,'original finite strict target with unchanged allowance')
        coefficient=min(c['mass']*eta*c['ownlo'],eta*c['ownhi'])
        records.append({'family':record['family'],'index':record['index'],'premises':plain(record['premises']),
                        'eta':str(eta),'sign_safe_loss_per_lambda':str(coefficient),'repair_per_lambda':str(c['repair']/c['N']),
                        'gate_kind':record['gate_kind'],'strict_final_gate':str(gate),'normalization_gates':len(record['normalization_gates']),
                        'normalization_contract_sha256':__import__('hashlib').sha256(json.dumps(plain(c),sort_keys=True,separators=(',',':')).encode()).hexdigest(),
                        'original_allowance':str(c.get('barrier_allowance',c.get('epsilon',F(0)))),'polynomials':checks})
    summary=[]
    for family in FAMILIES:
        subset=[r for r in records if r['family']==family]
        summary.append({'family':family,'rows':len(subset),'minimum_strict_final_gate':str(min(F(r['strict_final_gate'])for r in subset)),
                        'eta_counts':{str(e):sum(r['eta']==str(e)for r in subset)for e in(F(1,10),F(1,20),F(0),F(-1,20),F(-1,10))}})
    return {'status':'PASS_FINITE267_JOINT_COUNT_TINY','mathematical_scope':'local implications under exact same-law finite row premises, C>=.4, native signed score ceilings, inherited positive39/binomial reserves and acquisition interfaces',
            'execution_scope':'fresh original finite normalization and exact coefficient identities; no binomial/acquisition/integral campaign rerun',
            'original_score_targets_unchanged':True,'rows':records,'families':summary,
            'total_native_normalization_gates':sum(r['normalization_gates']for r in records),
            'total_polynomial_coefficients':sum(p['coefficient_count']for r in records for p in r['polynomials']),
            'zero_noise':'separate original Bernoulli treatment','no_manuscript_promotion':True}

if __name__=='__main__':
    path=Path(sys.argv[1]);result=accept_object(json.loads(path.read_text(),object_pairs_hook=unique));result['proof_object_sha256']=sha(path)
    print(json.dumps(result,indent=2,sort_keys=True))
