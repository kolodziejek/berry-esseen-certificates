#!/usr/bin/env python3
"""Independent exact join, normalization and logical-scope controls."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json,sys
if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Assertions required')

checks=[];controls=[]
def check(name,x):
    assert x,name
    checks.append(name)
def reject(name,x):
    assert not x,name
    controls.append(name)
def strata(endpoints):
    e=sorted(set(endpoints))
    return sorted(set(e+[(a+b)/2 for a,b in zip(e,e[1:])]))
def atan_bounds(m,N):
    s=sum((-1)**k*F(1,(2*k+1)*m**(2*k+1)) for k in range(N))
    next_term=(-1)**N*F(1,(2*N+1)*m**(2*N+1))
    return min(s,s+next_term),max(s,s+next_term)
a5,b5=atan_bounds(5,16);a239,b239=atan_bounds(239,4)
pi_lo=16*a5-4*b239;pi_hi=16*b5-4*a239
sigma_lo=F(3162277660,10**9);sigma_hi=F(3162277661,10**9)
check('sqrt10 endpoints',sigma_lo**2<10<sigma_hi**2)
ce2lo=(19+6*sigma_lo)/(72*pi_hi)
ce2hi=(19+6*sigma_hi)/(72*pi_lo)
check('left penalty lower bound',F(819,2000)**2<ce2lo)
check('left penalty upper bound',ce2hi<F(41,100)**2)
check('right penalty lower bound',F(2,5)**2<ce2lo)
check('global displacement implies right',F(17,250)<F(9,125))
check('coarse raw H implies comparison H',F(183605680,10**8)<F(46,25))
check('left phase length',F(391,500)-F(-109,500)==1)
check('right phase length',F(91,125)-F(-34,125)==1)

# A finite common refinement proves coverage of axis-aligned domains:
# membership is constant on each open stratum; every boundary is separate.
right_phase=strata([F(-34,125),F(-3,20),F(0),F(91,125)])
right_noise=strata([F(0),F(3,100),F(3,40)])
right_cells=0
for lam in right_noise:
    if lam==0:continue
    for u in right_phase:
        old=lam<=F(3,100)
        outer=(lam<=F(3,40) and
               (F(-34,125)<=u<=F(-3,20) or 0<=u<=F(91,125)))
        inner=F(3,100)<=lam<=F(3,40) and F(-3,20)<=u<=0
        check('v12 right phase/noise stratum',old or outer or inner)
        right_cells+=1
for lam in strata([F(0),F(1,100),F(8,25)]):
    check('left full-noise join',lam==0 or 0<lam<=F(1,100) or F(1,100)<=lam<=F(8,25))
for lam in strata([F(0),F(3,40),F(9,25)]):
    check('right full-noise join',lam==0 or 0<lam<=F(3,40) or F(3,40)<=lam<=F(9,25))
for theta in strata([F(0),F(91,125),F(391,500),F(1)]):
    if theta==1:continue
    ul=theta if theta<=F(391,500) else theta-1
    ur=theta if theta<=F(91,125) else theta-1
    check('left shifted integer anchor',F(-109,500)<=ul<=F(391,500))
    check('right shifted integer anchor',F(-34,125)<=ur<=F(91,125))

# Geometry does not permit silently dropping the variance denominator.
# Recheck the positive derivative guard used by the retained v13 theorem.
check('noise-monotonicity guard',
      30*(1-F(11,750)/(2*F(3,16)))-3*F(9,25)/(2*F(3,16))>0)
def Qlo(p):
    v=p*(1-p)
    return sigma_lo*(1-2*v)+2*p-1-6*v
B=F(3220665378,10**8)
p=F(53,100);v=p*(1-p)
check('high-p positive Q',Qlo(p)>0)
check('high-p excluded from index106',106**2*Qlo(p)**2>B**2*v)
check('low-p excluded from index169',169**2*Qlo(F(1,3))**2>B**2*F(2,9))
check('pstar below high-p range',(4-sigma_lo)/2<F(53,100))
check('coarse p upper bound below one',F(27,50)<1)
# Retained 28 closed panels, rather than an assumed .53 cutoff.
panels=[(F(i,100),F(i+1,100)) for i in range(25,53)]
for p in strata([F(i,100) for i in range(25,54)]):
    check('retained panel incidence',any(a<=p<=b for a,b in panels))

# Entire widened coarse probability domain at n>=700.
# The end-point p=.4 can use the weaker left strip; neither strip is inferred
# from its neighbor. The high-p row is a geometric contradiction, not counts.
for p in strata([F(1,4),F(1,3),F(2,5),F(53,100),F(27,50)]):
    rows=[p<=F(1,3),
          F(1,3)<=p<=F(2,5),
          F(2,5)<=p<=F(53,100),
          F(53,100)<=p<=F(27,50)]
    check('complete coarse probability join',any(rows))
check('left index meets its component',700>=700 and 700>=42)
check('right index meets its component',700>=200 and 200>=42)

# Actual two/three/four-point conditional laws and algebraic standardization.
zero=((F(0),F(1)),)
def two(x,y):return ((x,y/(y-x)),(y,-x/(y-x)))
def mom(law,r):return sum(prob*x**r for x,prob in law)
mapping_cases=0
for p in [F(1,3),F(2,5),F(53,100)]:
    q=1-p;v=p*q
    for law0,law1 in [(zero,zero),(two(F(-1,2),F(1,100)),zero),
                      (zero,two(F(-1,100),F(1,2))),
                      (two(F(-3,5),F(1,200)),two(F(-1,300),F(3,5)))]:
        s0=mom(law0,2);s1=mom(law1,2);s=q*s0+p*s1
        lawY=tuple((x,q*r) for x,r in law0)+tuple((1+x,p*r) for x,r in law1)
        check('conditional centering',mom(law0,1)==mom(law1,1)==0)
        check('actual mean',mom(lawY,1)==p)
        var=sum(r*(y-p)**2 for y,r in lawY)
        check('actual total variance',var==v+s)
        ell2=1/var;theta=s/var
        check('noise coordinate mapping',theta/ell2==s)
        check('conditional gap scale',v*ell2+theta==1)
        for rawY in [F(0),F(1,2),F(1)]:
            # H=(rawY-p)/sqrt(var), ell=1/sqrt(var).
            check('raw threshold exact mapping',p+(rawY-p)==rawY)
        if s>0:reject('replace s by standardized theta',theta==s)
        mapping_cases+=1

# Logical and endpoint controls; these are not counterexamples to Berry--Esseen.
reject('extend right comparison to coarse p=.535',F(107,200)<=F(53,100))
reject('infer common .6 strip from .7 strip',F(13,20)<=F(3,5))
reject('infer left C range from C>=.4 alone',F(1,2)<=F(41,100))
reject('delete compound negative-inner component',
       F(1,20)<=F(3,100) or F(-1,20)<=F(-3,20) or F(-1,20)>=0)
reject('delete zero-noise Bernoulli branch',0<F(0))
reject('equate reflected closed error with original negative closed error',
       F(3,4)-F(1,2)==F(1,2)-F(3,4))
reject('reflect probability interval without reacquisition',1-F(2,5)<=F(53,100))
# Logical model: every row >=42 fails. The conditional implication at n>=700
# has a false predecessor premise, while BASE41 remains true.
base41=True;pred699=False;row700_good=False
check('conditional induction model is consistent',base41 and (not pred699 or row700_good))
reject('infer unconditional700 from BASE41 plus conditional tail',row700_good)

parser=argparse.ArgumentParser()
parser.add_argument('--right-root',type=Path)
parser.add_argument('--left-root',type=Path)
args=parser.parse_args()
here=Path(__file__).resolve().parent;root=here.parents[2]
manifest=here/'join-review-sources.json'
pins=json.loads(manifest.read_text())
actualpins={}
for label,entry in pins.items():
    owner=args.right_root if entry['owner']=='right' else args.left_root if entry['owner']=='left' else root
    owner=(owner or root).resolve()
    path=owner/entry['path']
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    check('source pin '+label,digest==entry['sha256'])
    actualpins[label]={'path':str(path),'sha256':digest}
print(json.dumps({'result':'PASS','checks':len(checks),'right_phase_noise_strata':right_cells,
 'mapping_cases':mapping_cases,'negative_controls':controls,
 'source_pins':actualpins,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Component-domain composition; does not reprove component inequalities or acquisition.'},indent=2))
