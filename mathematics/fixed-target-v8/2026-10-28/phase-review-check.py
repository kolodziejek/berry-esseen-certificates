#!/usr/bin/env python3
"""Independent exact checks of the bounded exported phase interface.

Reads inert JSON/Python source; imports or executes no producer/kernel.
"""
import ast
import hashlib
import json
import sys
from collections import Counter
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

C0,C1=F('0.4097321837023'),F('0.4097321837025')


def unique(pairs):
    out={}
    for k,v in pairs:
        assert k not in out, 'duplicate JSON field'
        out[k]=v
    return out


def dec(v):
    if isinstance(v,str):
        try:return F(v)
        except ValueError:return v
    if isinstance(v,list):return [dec(x) for x in v]
    if isinstance(v,dict):return {k:dec(x) for k,x in v.items()}
    return v


def root_pair(x,scale):
    k=isqrt(x.numerator*scale*scale//x.denominator)
    l,u=F(k,scale),F(k+1,scale)
    assert l*l<=x<=u*u
    return l,u


def upper9(x):
    return str(F(-((-x.numerator*10**9)//x.denominator),10**9))


def maximum(B,L,Q,a,b):
    assert Q>0 and a<=b
    candidates=[B+L*a-Q*a*a,B+L*b-Q*b*b]
    if 2*Q*a<=L<=2*Q*b:
        candidates.append(B+L*L/(4*Q))
    return max(candidates)


def region(cells,pl,pu,hl,hu,lam,scale=10**12):
    assert 0<pl<=pu<1 and 0<=hl<=hu
    v0=min(pl*(1-pl),pu*(1-pu))
    v1=max(pl*(1-pl),pu*(1-pu),F(1,4) if pl<=F(1,2)<=pu else F(0))
    if lam is not None:
        assert lam>=0
        th=lam/(42*v0+lam)
        ml=root_pair(v0*v0/(v0+lam/42),scale)[0]
        mu=root_pair(v1,scale)[1]
        bl=1-2*pu-2*(1-pl)*th
        bu=1-2*pl+2*pu*th
    selected=[]
    for c in cells:
        if c['pl']>pu or c['pu']<pl or c['H']<hl:continue
        if lam is not None and (c['m'][1]<ml or c['m'][0]>mu or c['beta'][1]<bl or c['beta'][0]>bu):continue
        selected.append(c)
    assert selected
    out={}
    for sign in ('plus','minus','absolute'):
        out[sign]=max(min(c['raw'],max(maximum(z['B'],z[sign],z['Q'],hl,min(hu,c['H']))
                            for z in c['quadratics'])) for c in selected)
    return len(selected),out


def main(src):
    archive=src/'runs/fixed-target-v8-20261028/phase01'
    v7=src/'mathematics/fixed-target-v7/2026-10-27'
    original=(v7/'signed_core.py').read_text()
    assert hashlib.sha256(original.encode()).hexdigest()=='1f40ccb90eb58a7f84dc61a0a5dd9bf6e6eb4e341aa6c9c6d049d08451f5211b'
    builder=ast.parse((archive/'build_phase_core.py').read_text())
    assignments=[x for x in builder.body if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='patches' for t in x.targets)]
    assert len(assignments)==1
    patches=ast.literal_eval(assignments[0].value)
    assert len(patches)==3
    generated=original
    for a,b in patches:
        assert generated.count(a)==1
        generated=generated.replace(a,b)
    assert generated==(archive/'phase_core.py').read_text()
    reversed_text=generated
    for a,b in reversed(patches):
        assert reversed_text.count(b)==1
        reversed_text=reversed_text.replace(b,a)
    assert reversed_text==original
    artifact=json.loads((archive/'stdout.json').read_text(),object_pairs_hook=unique)
    z=dec(artifact)
    proof_blob=(v7/'entry-proof.json').read_bytes()
    assert hashlib.sha256(proof_blob).hexdigest()==artifact['source_proof_sha256']=='61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae'
    proof=dec(json.loads(proof_blob,object_pairs_hook=unique))
    cells=z['phase_cells'];assert len(cells)==z['active_cells']==682
    rows=z['rows'];assert z['total_cells']==128*len(rows)==2048
    assert [r['index'] for r in rows]==[i for i,t in enumerate(proof['steps'][3]) if not t.get('prior_excluded')]
    byrow=Counter();cell_outputs={}
    for c in cells:
        rl,rh=c['rho'];bl,bu=c['beta'];gl,gh=c['gamma'];ml,mu=c['m']
        index=(rl-1)*96000/3361
        assert index.denominator==1;index=int(index)
        assert rh==1+F(3361*(index+1),96000)
        byrow[index]+=1
        prior=proof['steps'][2][index]
        assert c['old_defect']==prior['defect'] and c['radius']==proof['steps'][3][index]['radius']
        assert c['density']==[F(997,2500)*(1-prior['raw']/(42*C0*rl)),F(2,5)]
        assert c['eta']==(C0*rl-c['raw']/42)/2>0
        assert c['pl']==2*ml*ml/(1+bu) and c['pu']==1-2*ml*ml/(1-bl)
        assert 0<c['pl']<=c['pu']<1
        kl,ku=c['K1'];wl,wu=c['W'];phl,phu=c['density']
        assert kl<=ku and wl<=wu and 0<phl<=phu
        budgets=[]
        assert [q['c'] for q in c['quadratics']]==[C0,C1]
        for q in c['quadratics']:
            cc=q['c']
            # Independent closed-form support of the rectangle, not its 8-corner loop.
            linhi=cc*ku+(phu if wu>=0 else phl)*wu
            linlo=cc*kl+(phl if wl>=0 else phu)*wl
            assert q['plus']==linhi+c['slope']
            assert q['minus']==-linlo+c['slope']
            assert q['absolute']==max(linhi,-linlo)+c['slope']
            assert q['B']==c['Fourier']+cc*c['A']
            assert q['Q']==cc*rl+(phl if gl>=0 else phu)*gl/2+c['eta']>0
            assert q['plus']<=q['absolute'] and q['minus']<=q['absolute']
            budgets.append(q['B']+q['absolute']**2/(4*q['Q']))
            assert c['H']>=q['absolute']/(2*q['Q'])
            assert q['B']+q['absolute']*c['H']-q['Q']*c['H']**2<=0
        d=min(c['old_defect'],F(15000,997*42)*max(budgets))
        r0,d0=cell_outputs.get(index,(F(-1),F(-1)))
        cell_outputs[index]=max(r0,c['raw']),max(d0,d)
    for r in rows:
        i=r['index'];target=proof['steps'][3][i]
        assert byrow[i]==r['active']==target['active']
        assert r['active']+r['excluded']==128
        assert cell_outputs.get(i,(F(-1),F(-1)))==(r['raw'],r['D'])
        assert r['raw']<=target['raw'] and r['D']<=target['defect']
    # Match the exact saved point probe with its original outward-root precision.
    for name,lam in [('panel_phase',None),('panel_phase_noise',F(3,20))]:
        count,values=region(cells,F(41,100),F(42,100),F(5,4),F(5,4),lam,10**8)
        assert count==z['probe']['summary'][name]['cells']
        for sign,value in values.items():assert value==z['probe']['summary'][name][sign]
    saved_regions=dec(json.loads((src/'runs/fixed-target-v8-20261028/phase02/stdout.json').read_text(),object_pairs_hook=unique))
    assert saved_regions['source_sha256']==hashlib.sha256((archive/'stdout.json').read_bytes()).hexdigest()
    assert len(saved_regions['regions'])==9
    regions=[]
    for a,b in [(F(5,4),F(5,4)),(F(31,25),F(63,50)),(F(6,5),F(13,10))]:
        for lam in (None,F(3,20),F(4,25)):
            count,values=region(cells,F(41,100),F(42,100),a,b,lam)
            expected=saved_regions['regions'][len(regions)]
            assert expected['H_lower']==a and expected['H_upper']==b and expected['lambda_upper']==lam
            assert expected['cells']==count and expected['resource']==values
            regions.append({'H':[str(a),str(b)],'lambda_upper':str(lam),'cells':count,
                            'resource_upper_1e9':{k:upper9(v) for k,v in values.items()}})
    # Exact actual-law control for the beta/theta formulas, including p>1/2.
    p=F(4,5);q=1-p;t=F(1,100)
    a=2*(1-F(16,5)*t*t)/(1+F(16,5)*t*t)
    eps=4*t/(1+F(16,5)*t*t);b=q*a/p
    law=[(-a,q),(b-eps,p/2),(b+eps,p/2)]
    assert all(x>0 for x,_ in law[1:])
    E=lambda f:sum(w*f(x) for x,w in law)
    assert E(lambda x:x)==0 and E(lambda x:x*x)==1
    m=E(lambda x:max(x,0));beta=E(lambda x:x*abs(x))
    theta=1-m*m/(p*q)
    assert theta==p*eps*eps>0
    assert beta==1-2*p+2*p*theta>1-2*p+theta
    for n in (42,43,100,10000):
        lam=n*p*q*theta/(1-theta)
        assert m*m==(p*q)**2/(p*q+lam/n)
    # All-H endpoint substitution is false without the concave vertex.
    assert maximum(F(0),F(2),F(1),F(0),F(2))==1
    assert max(F(0),F(2)*2-F(1)*4)==0
    # Closed overlap keeps touching cells; wrong strict filters would lose them.
    assert not (F(42,100)>F(42,100))
    return {'status':'PASS_INDEPENDENT_PHASE_EXPORT_AND_REGION_ARITHMETIC',
        'source_proof_sha256':hashlib.sha256(proof_blob).hexdigest(),
        'export_sha256':hashlib.sha256((archive/'stdout.json').read_bytes()).hexdigest(),
        'export_cells':len(cells),'source_box_census':z['total_cells'],'reconstructed_endpoint_quadratics':2*len(cells),
        'source_transform_exactly_reversible':True,'saved_probe_exactly_reproduced':True,'saved_nine_regions_exactly_reproduced':True,
        'regions':regions,'negative_controls':['omitted concave vertex','plus-Theta beta bound above one half','strict overlap endpoints'],
        'inherited_code_imported_or_executed':False,'full_confinement_claim':False}


if __name__=='__main__':
    print(json.dumps(main(Path(sys.argv[1])),indent=2))
