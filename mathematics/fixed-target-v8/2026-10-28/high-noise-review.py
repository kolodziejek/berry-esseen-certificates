#!/usr/bin/env python3
"""Independent exact reading of frozen exported data; no producer imports/runs."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
from hashlib import sha256
import argparse,json

PINS={
 'mathematics/fixed-target-v8/2026-10-28/phase-confinement-sources/phase-coefficients.json':'b18599468c975032f4078e7a5f734fd6430b2b7da583789de58d9537d323f690',
 'runs/fixed-target-v8-20261028/phase-confinement05/stdout.json':'e5dd725d31b2e67a634a8ae7b6cd630e899457a96280a2f2ee3b3612eed9ba90',
}

def parse(x):
    if isinstance(x,str):
        try:return F(x)
        except ValueError:return x
    if isinstance(x,list):return [parse(y) for y in x]
    if isinstance(x,dict):return {k:parse(v) for k,v in x.items()}
    return x

def unique(items):
    out={}
    for k,v in items:
        assert k not in out
        out[k]=v
    return out

def root_down(x):
    scale=10**10
    k=isqrt(x.numerator*scale*scale//x.denominator)
    v=F(k,scale)
    assert v*v<=x<(v+F(1,scale))**2
    return v

def pos(x):return max(F(0),x)

N=42
l,h=F(41,100),F(21,50)
vl,vh=l*(1-l),h*(1-h)
E,FL=F('1.9706'),F('2.034')
th,d,sigma,tau=F('.054'),F('.069'),F('.6'),F('.2')
cl,cu,kappa=F('.4095'),F('.40974'),F(997,15000)
fd=F('1.037')
cp=2*F('5.16')*E**2*(1-h-d)**2
cm=2*F('7.16')*E**2*(l-d)**2
bs=min(3*F('4.16')*E*(1-h-d),3*F('6.16')*E*(l-d))
alpha=min(cp*l*E,cm*(1-h)*E)
bl,bu=1-2*h-2*(1-h)*th,1-2*l+th
rb=(1-2*vl)/root_down(vl)
eps=F(1,100000)
rL,rR=l-(1-l)/40,h+h/40
vs=min(rL*(1-rL),rR*(1-rR))
M=root_down(F(4,25)/(vs*(1-F(1,480))**2))+F(1,10**10)
ae=fd*M*(1/l+1/(1-h))/2

def resource(cells,sign,hl,hh,noise_hi):
    theta=noise_hi/(N*vl+noise_hi)
    ml=root_down(vl*vl/(vl+noise_hi/N));mu=root_down(vh)+F(1,10**10)
    beta_min=1-2*h-2*(1-l)*theta;beta_max=1-2*l+2*h*theta
    scores=[]
    for i,c in enumerate(cells):
        if c['pu']<l or c['pl']>h or c['H']<hl:continue
        if c['m'][1]<ml or c['m'][0]>mu:continue
        if c['beta'][1]<beta_min or c['beta'][0]>beta_max:continue
        upper=min(hh,c['H']);assert upper>=hl
        endpoints=[]
        for q in c['quadratics']:
            b,f,v=q['B'],q['plus' if sign==1 else 'minus'],q['Q']
            assert v>0
            x=min(upper,max(hl,f/(2*v)))
            endpoints.append(b+f*x-v*x*x)
        scores.append((min(c['raw'],max(endpoints)),i))
    return scores

def slopes(sign,hl,hh,noise_hi):
    rho=min(F('1.22'),rb+24*noise_hi/N)
    density=F('.39886')*(1-hh*hh/(2*N));assert density>0
    v=F('.4')*hh if sign==1 else -density*hl
    assert v+3*cu*rho>0
    negative=FL*pos((v+3*cu*rho)**2/(12*cl)-3*cl*bl)
    positive=FL*pos(F('.4')*hh*F('1.2')+3*cu*F('1.2')*F('.2')-3*cl*bl)
    Lg=E*density-max(negative,positive)/N
    Up=F('.4')*FL+FL/N*(3*cu*bu+(F('.4')*hh+3*cu*rho)**2/(12*cl))
    tmax=-E*(l+tau+eps)
    xmin=min(tmax,-rho/2);Bmin=bl+rho*xmin+xmin*xmin
    xmin=min(tmax,-(v+3*cl*rho)/(6*cl))
    qmin=3*cl*(bl+rho*xmin+xmin*xmin)+v*xmin+3*(cu-cl)*min(0,Bmin)
    L=E*density-FL*pos(-qmin)/N
    assert min(L,Lg,Up)>0
    return L,Lg,Up

def errors(S,noise_lo,noise_hi,sign,hl,hh,side):
    R=S/kappa-bs*E*E*noise_lo
    assert R>=0
    G=R/alpha
    L,Lg,Up=slopes(sign,hl,hh,noise_hi)
    if side=='lower':
        v=-hl/FL if sign==1 else hh/E
        DI,DJ=pos(v-l-tau-eps),pos(v+1-l-eps)
        ad,aj=L,1/(1-sigma-2*d)
        lhs=L*(F('.5')-tau-eps)
    else:
        DI,DJ=pos(d+tau+hh/E-l),pos(1+d+2*tau+hh/E-l)
        ad,aj=Lg+Up,1/tau
        lhs=Lg-sigma*Up
    A=fd*M*(DI/l+DJ/(1-h));B=fd*M
    prices=[(ad/l+2*ae)/(E*cp),(ad/(1-h)+2*ae)/(E*cm),kappa*aj/(1-th)]
    z=max(prices);assert z*R+A>0
    bad=min(noise_hi/(noise_hi+N*l*tau*tau),G/(N*tau+G))
    candidates=[(z*R+A)/N+B*bad]
    w=[R/(E*cp*l),R/(E*cm*(1-h)),F(0)]
    for j in range(11):
        t=G*j/10
        slope=N*tau/(N*tau+t)**2;intercept=t*t/(N*tau+t)**2
        candidates.append(A/N+max(prices[i]*R/N+B*slope*w[i] for i in range(3))+B*intercept)
    return lhs,min(candidates)

def validate_coverage(rows):
    expected=[(s,[F(907*j,4000),F(907*(j+1),4000)],[F(3*k,40),F(3*(k+1),40)])
              for s in (1,-1) for j in range(8) for k in range(8)]
    assert [(r['sign'],r['phase'],r['noise']) for r in rows]==expected

def main(root):
    assert __debug__
    data=[]
    for name,digest in PINS.items():
        blob=(root/name).read_bytes();assert sha256(blob).hexdigest()==digest
        data.append(parse(json.loads(blob,object_pairs_hook=unique)))
    cells=data[0]['phase_cells'];log=data[1];rows=log['diagnostic']['records']
    assert len(cells)==682
    validate_coverage(rows)
    assert fd*fd>max(F(42,41)**3,F(42,40))
    assert sigma+d<1-d and sigma+d-tau-eps<1-d
    assert d+2*tau<F('.5') and 1-d-tau>0 and 1-sigma-2*d>0
    assert M*M>F(4,25)/(vs*(1-F(1,480))**2)
    assert F('1.2')**2>(1-l)/l
    counters={'low_noise':0,'empty':0,'negative_resource':0,'noise_exclusion':0,'high_noise_two_rays':0}
    high_margins=[];all_failed=0
    for r in rows:
        sign=r['sign'];hl,hh=r['phase'];nl,nh=r['noise']
        scores=resource(cells,sign,hl,hh,nh)
        recorded=r['phase_resource'];assert recorded['cells']==len(scores)
        low=nh<=F(3,40)
        if low:counters['low_noise']+=1
        if not scores:
            assert recorded['empty'] and r['resource_excluded']
            if not low:counters['empty']+=1
            continue
        S,index=max(scores)
        assert not recorded['empty'] and recorded['U']==S and recorded['winner']==index
        reason='negative_resource' if S<0 else 'noise_exclusion' if S/kappa-bs*E*E*nl<0 else None
        assert r['resource_excluded']==bool(reason)
        if reason:
            if not low:counters[reason]+=1
            continue
        assert [x['side'] for x in r['sides']]==['lower','upper']
        for side in r['sides']:
            lhs,error=errors(S,nl,nh,sign,hl,hh,side['side'])
            assert (lhs,error,lhs-error)==(side['lhs'],side['error'],side['margin'])
            assert side['passed']==(lhs>error)
            all_failed+=int(lhs<=error)
            if not low:
                assert lhs>error
                high_margins.append(lhs-error)
        if not low:counters['high_noise_two_rays']+=1
    assert counters['low_noise']==16 and counters['high_noise_two_rays']==28
    assert sum(counters.values())==128 and len(high_margins)==56 and all_failed==8
    assert min(high_margins)==log['composition']['smallest_remaining_ray_margin']
    assert min(high_margins)>F('0.00892011917')
    rejected=[]
    for name,mutated in [('missing box',rows[:-1]),('duplicate box',rows[:-1]+[rows[0]]),('reversed boxes',rows[::-1])]:
        try:validate_coverage(mutated)
        except AssertionError:rejected.append(name)
        else:raise AssertionError(name)
    # Exact tangent identity, not a sampled positivity inference.
    for t in (F(0),F(1,7),F(3),F(100)):
        for x in (F(0),F(1,11),t,F(9)):
            a=N*tau
            assert a*x/(a+t)**2+t*t/(a+t)**2-x/(a+x)==a*(x-t)**2/((a+x)*(a+t)**2)
    return {'status':'PASS_INDEPENDENT_SAVED_DATA_AND_HIGH_NOISE_FORMULAS',
      'source_pins':PINS,'counts':counters,'high_noise_strict_gates':len(high_margins),
      'strict_margin_lower':'0.00892011917','preserved_failed_unassisted_gates':all_failed,
      'controls_rejected':rejected,'producer_executed':False,'inherited_modules_imported':False,
      'scope':'Checks saved-data resource maxima and high-noise formulas; analytic and original entry dependencies require the accompanying proof review.'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source-root',type=Path,required=True)
    print(json.dumps(main(ap.parse_args().source_root),indent=2))
