"""Fixed n5 BN/p38: exact whole-cell six-count CDF implication.

No acquisition or full-row status is inferred here. The complete conditional
moment reduction is documented in SOUNDNESS.md. Data supply only quartics.
"""
from fractions import Fraction as F
from math import comb
from itertools import combinations,product
from pathlib import Path
from functools import lru_cache
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('unoptimized exact Python required')
HERE=Path(__file__).resolve().parent
def need(x,msg):
    if not x:raise ValueError(msg)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def unique(pairs):
    d={}
    for k,v in pairs:
        need(k not in d,'duplicate JSON key');d[k]=v
    return d
PINS={'contract.json':'2b3f626ba3a9e954e4700bf206cf7a364f44958bb901b463198249dda2f37e48',
 'quartic_sturm.py':'1f815ccb23692f78be98691a76a5fe0605f8995abdab5d9a3964f1625a4c2617',
 'quartic_global.py':'0760d772b6cf1858ed139a1fe179490cb1e523a5d685a37a25271a10b349aa35',
 'finite_binomial_core.py':'939236711b080f9148ee3d3f7f6a0cd15b86cb24f3d2700f0e7127b2a345291f'}
for name,pin in PINS.items():need(sha(HERE/'native'/name)==pin,'fixed native source '+name)
sys.path.insert(0,str(HERE/'native'))
import quartic_sturm as sturm
import finite_binomial_core as normal
CFG=json.loads((HERE/'native/contract.json').read_text(),object_pairs_hook=unique)['rows'][0]
N=5;PL,PU=map(F,CFG['p']);A0=F(CFG['outer0']);A1=F(CFG['outer1']);D=F(CFG['acquired_inward_upper'])
LAMBDA=F(CFG['acquired_lambda_upper']);BLO,BHI=map(F,CFG['acquired_beta'])
RHO=F(CFG['rho_lower']);DEGP=9;DEGU=4
def rational(s):
    need(type(s)is str,'rational data must be strings');v=F(s)
    need(str(v)==s,'canonical rational string');return v
def cell(k,ps,us):
    need(type(k)is int and k in(1,2,3),'licensed count center')
    p0,p1=map(F,ps);u0,u1=map(F,us)
    need(PL<=p0<p1<=PU and -F(1,2)<=u0<u1<=F(1,2),'closed nondegenerate cell within original row')
    return k,p0,p1,u0,u1
def add(a,b):
    return tuple((a[i]if i<len(a)else F(0))+(b[i]if i<len(b)else F(0))for i in range(max(len(a),len(b))))
def scale(a,c):return tuple(x*c for x in a)
def mul(a,b):
    r=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
      for j,y in enumerate(b):r[i+j]+=x*y
    return tuple(r)
def power(a,n):
    r=(F(1),)
    for _ in range(n):r=mul(r,a)
    return r
def evaluate(a,x):
    r=F(0)
    for c in reversed(a):r=r*x+c
    return r
@lru_cache(maxsize=2048)
def bernstein(a,l,h,d):
    need(len(a)<=d+1 and l<h,'degree and nondegenerate Bernstein interval')
    local=[sum(a[j]*comb(j,i)*l**(j-i)*(h-l)**i for j in range(i,len(a)))for i in range(d+1)]
    return tuple(sum(local[j]*F(comb(i,j),comb(d,j))for j in range(i+1))for i in range(d+1))
P=(F(0),F(1));Q=(F(1),-F(1));V=mul(P,Q);V2=mul(V,V)
@lru_cache(maxsize=128)
def polygon(pl,pu):
    # Cubic upper envelopes imply a single OUTER polygon for every p in cell.
    rhi=mul(V,(BHI-1,F(2)))
    rlo=mul(V,(1-BLO,-F(2)))
    planes=[(-F(1),F(0),F(0)),(F(0),-F(1),F(0)),(F(1),F(1),LAMBDA/N),
      (-(1+BHI),1-BHI,max(bernstein(rhi,pl,pu,3))),
      (1+BLO,-(1-BLO),max(bernstein(rlo,pl,pu,3)))]
    vs=set()
    for(a,b,c),(d,e,f)in combinations(planes,2):
        det=a*e-b*d
        if not det:continue
        x=(c*e-b*f)/det;y=(a*f-c*d)/det
        if all(A*x+B*y<=C for A,B,C in planes):vs.add((x,y))
    need(len(vs)>=3,'nonempty compact outer polygon')
    return tuple(sorted(vs))
def compact_ray(q,sign,subtract):
    q=list(q);q[0]-=subtract;r=[F(0)]*5
    for j,a in enumerate(q):
      for h in range(5-j):r[j+h]+=a*sign**j*comb(4-j,h)*(-1)**h
    return tuple(r)
def normal_lower(num,den):
    lo,hi=normal.root(den)
    if num>=0:
        z=num/hi;idx=z.numerator*normal.Z//z.denominator
        need(0<=idx<=5*normal.Z,'normal range');return F(normal.positive_cdf(idx)[0],normal.S)
    z=-num/lo;idx=-((-z.numerator*normal.Z)//z.denominator)
    need(0<=idx<=5*normal.Z,'normal range');return 1-F(normal.positive_cdf(idx)[1],normal.S)
@lru_cache(maxsize=512)
def target(k,pl,pu,ul,uh):
    num=F(k)+ul-N*pu
    den=N*pl*(1-pl)if num<0 else N*pu*(1-pu)+LAMBDA
    return normal_lower(num,den)+normal.CE_LO*RHO/normal.root(F(N))[1]
def tensors(k,pl,pu,ul,uh):
    """36 (or more) common-moment rows, each 30 degree(9,4) tensors.

    Tensor entries are exact Bernstein coefficients of v²*pi_j*E(z^d).
    Degree elevation is fixed, never taken from candidate data.
    """
    shift={(j,d):bernstein(power((F(j-k),-F(1)),d),ul,uh,DEGU)for j in range(6)for d in range(5)}
    base0=mul(mul(P,P),Q);base1=mul(P,mul(Q,Q))
    masses=[scale(mul(power(P,j),power(Q,N-j)),F(comb(N,j)))for j in range(6)]
    out=[]
    for x,y in polygon(pl,pu):
      for g0,g1 in product((-A0,F(0),min(D,pu)),(A1,F(0),-min(D,1-pl))):
        row=[]
        for j,mass in enumerate(masses):
            aa=(N-j)*x;bb=j*y
            tv=add(scale(P,aa),scale(Q,bb))
            mom=[V2,(F(0),),add(scale(base0,aa),scale(base1,bb)),
              add(scale(base0,aa*g0),scale(base1,bb*g1)),
              add(add(scale(base0,aa*g0*g0),scale(base1,bb*g1*g1)),scale(mul(tv,tv),F(12,5)))]
            bm=[bernstein(mul(mass,m),pl,pu,DEGP)for m in mom]
            for d in range(5):
                row.append(tuple(sum(F(comb(d,i))*bm[i][a]*shift[j,d-i][b]for i in range(d+1))for a in range(DEGP+1)for b in range(DEGU+1)))
        out.append(row)
    return out
def target_tensor(k,pl,pu,ul,uh):
    b=bernstein(scale(V2,target(k,pl,pu,ul,uh)),pl,pu,DEGP)
    return tuple(c for c in b for _ in range(DEGU+1))
def admit(qs,domain,rows=None):
    need(type(qs)is list and len(qs)==6,'six ordered actual count polynomials')
    exact=[]
    for row in qs:
        need(type(row)is list and len(row)==5,'five quartic coefficients')
        q=list(map(rational,row));need(q[4]>0,'strict positive leading coefficient')
        sturm.positive(compact_ray(q,-1,F(1)));sturm.positive(compact_ray(q,1,F(0)));exact.extend(q)
    k,pl,pu,ul,uh=domain
    rows=tensors(*domain)if rows is None else rows
    rhs=target_tensor(*domain);margin=None
    for row in rows:
        coeffs=[rhs[a]-sum(exact[d]*row[d][a]for d in range(30))for a in range(50)]
        z=min(coeffs);need(z>0,'strict whole-cell tensor bound')
        margin=z if margin is None else min(margin,z)
    return dict(k=k,p=list(map(str,(pl,pu))),u=list(map(str,(ul,uh))),vertices=len(polygon(pl,pu)),
      moment_pairs=9,global_rays=12,tensor_coefficients=50*len(rows),cleared_margin=str(margin))
