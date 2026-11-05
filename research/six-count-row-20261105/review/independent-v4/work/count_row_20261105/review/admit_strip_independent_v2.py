"""Independent polynomial admission of one fixed eight-leaf V3 strip.

Uses direct cleared moment polynomials, an independent sparse transform,
Bernstein subdivision (not Sturm) on global rays, and a direct rational normal
integral Taylor enclosure. Only the pinned Gaussian normalization constants
and original contract are shared numerical primitives.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
from math import comb,isqrt,factorial
from functools import lru_cache
import copy,hashlib,json,sys
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];sys.path.insert(0,str(HERE))
import check_tensors as t
if not __debug__ or sys.flags.optimize:raise RuntimeError('unoptimized exact Python')
OBJ=ROOT/'runs/count_row_20261105/construct_cubic_pilot01/objects/proof_object.json'
OBJ_SHA='32c59ab41623b34832ac7ecc21986ef04e1760ee2f9f79df2fc10fd17cad4f0c'
def need(x,msg):
    if not x:raise ValueError(msg)
def unique(pairs):
    d={}
    for k,v in pairs:need(k not in d,'duplicate key');d[k]=v
    return d
def rat(z):
    need(type(z)is str,'rational string');a=F(z);need(str(a)==z,'canonical rational');return a
def sqrt_bounds(x):
    need(x>0,'positive root radicand');S=10**36
    a=isqrt(x.numerator*S*S//x.denominator)
    lo,hi=F(a,S),F(a+1,S);need(lo*lo<=x<hi*hi,'directed square root');return lo,hi
@lru_cache(maxsize=128)
def gaussian_lower(a,d):
    lo,hi=sqrt_bounds(d);z=abs(a)/(lo if a<0 else hi)
    need(z<=2,'bounded independent normal series domain')
    M=40
    integral=sum(F((-1)**i,2**i*factorial(i)*(2*i+1))*z**(2*i+1) for i in range(M))
    err=F(1,2**M*factorial(M)*(2*M+1))*z**(2*M+1)
    need(integral>=0,'positive lower integral')
    low=F(1,2)+t.m.normal.PHI_LO*integral
    high=F(1,2)+t.m.normal.PHI_HI*(integral+err)
    return 1-high if a<0 else low
def bernstein(poly):
    # Input is in local coordinates. Expand in the fixed degree(9,4) basis.
    need(all(0<=i<=9 and 0<=j<=4 for i,j in poly),'fixed degree')
    return [sum(a*F(comb(r,i),comb(9,i))*F(comb(s,j),comb(4,j))
        for (i,j),a in poly.items() if i<=r and j<=s) for r in range(10) for s in range(5)]
def uni_bern(a,lo,hi):
    b=[]
    for r in range(5):
        b.append(sum(a[j]*comb(j,i)*lo**(j-i)*(hi-lo)**i*F(comb(r,i),comb(4,i))
          for j in range(len(a)) for i in range(min(j,r)+1)))
    return b
def ray(q,sgn,minus):
    # A separate expansion of (1-t)^4[P(sign*t/(1-t))-minus].
    a=[F(0)]*5
    for r in range(5):
      c=q[r]-(minus if r==0 else 0)
      for j in range(5-r):a[r+j]+=c*sgn**r*comb(4-r,j)*(-1)**j
    count=0
    def visit(lo,hi,depth):
        nonlocal count;count+=1
        if min(uni_bern(a,lo,hi))>0:return
        need(depth<24,'ray positivity unresolved');mid=(lo+hi)/2
        visit(lo,mid,depth+1);visit(mid,hi,depth+1)
    visit(F(0),F(1),0);return count
def polygon(pl,pu,lo,hi):
    # Independent cubic Bernstein upper values via evaluation of local monomials.
    def upper(poly):
        lc=t.local(poly,pl,pu,F(0),F(1));need(all(j==0 for i,j in lc),'univariate cubic')
        return max(sum(a*F(comb(r,i),comb(3,i)) for (i,j),a in lc.items() if i<=r) for r in range(4))
    bh,bl=t.m.BHI,t.m.BLO
    rhi=t.mul(t.V,t.add(t.scale(t.ONE,bh-1),t.scale(t.P,2)))
    rlo=t.mul(t.V,t.add(t.scale(t.ONE,1-bl),t.scale(t.P,-2)))
    hs=[(-F(1),F(0),F(0)),(F(0),-F(1),F(0)),(F(1),F(1),hi/5),(-F(1),-F(1),-lo/5),
      (-(1+bh),1-bh,upper(rhi)),(1+bl,-(1-bl),upper(rlo))]
    vs=set()
    for (a,b,c),(d,e,f) in combinations(hs,2):
        det=a*e-b*d
        if not det:continue
        x=(c*e-b*f)/det;y=(a*f-c*d)/det
        if all(A*x+B*y<=C for A,B,C in hs):vs.add((x,y))
    need(len(vs)>=3,'nonempty full polygon');return sorted(vs)
def leaf(qs,theta,domain):
    k,pl,pu,ul,uh,lo,hi=domain;theta=rat(theta);need(0<=theta<=1,'convex blend')
    need(type(qs)is list and len(qs)==6,'all six ordered counts')
    qs=[[rat(v) for v in q] for q in qs]
    need(all(len(q)==5 and q[4]>0 for q in qs),'quartic positive leading')
    rays=sum(ray(q,s,h) for q in qs for s,h in ((-1,F(1)),(1,F(0))))
    amin=k+ul-5*pu;amax=k+uh-5*pl
    correlated=amax<=0 and amin*amin<=15*pl*(1-pl)
    whi=pu*(1-pu)+hi/5
    floor=t.m.normal.CE_LO*t.m.RHO/sqrt_bounds(F(5))[1]
    c=t.m.normal.CE_LO/(sqrt_bounds(F(5))[1]*whi*sqrt_bounds(whi)[1])
    best=None;rows=0
    for x,y in polygon(pl,pu,lo,hi):
      for g0,g1 in product((-t.m.A0,F(0),min(t.m.D,pu)),(t.m.A1,F(0),-min(t.m.D,1-pl))):
        den=5*pl*(1-pl)+5*(x+y) if correlated else (5*pl*(1-pl)+lo if amin<0 else 5*pu*(1-pu)+hi)
        normal=gaussian_lower(amin,den)
        R=t.add(t.mul(t.V,t.add(t.ONE,t.scale(t.V,-2))),t.scale(t.P,3*x),t.scale(t.Q,3*y),t.scale(t.ONE,-g0*x+g1*y))
        target=t.mul(t.V2,t.add(t.scale(t.ONE,normal+(1-theta)*floor),t.scale(R,theta*c)))
        gap=t.add(target,t.scale(t.direct(k,x,y,g0,g1,qs),-1))
        b=bernstein(t.local(gap,pl,pu,ul,uh));need(min(b)>0,'strict direct continuous score gap')
        best=min(b) if best is None else min(best,min(b));rows+=1
    return dict(ray_nodes=rays,moment_rows=rows,coefficients=50*rows,cleared_margin=str(best))
def admit(obj):
    need(type(obj)is dict and set(obj)=={'schema','contract_sha256','n','k','p','u','noise','tree'},'exact object fields')
    need(obj['schema']=='N5_BN38_SIX_COUNT_CELL_V3' and obj['contract_sha256']==t.m.PINS['contract.json'],'fixed conditional contract')
    need(type(obj['n'])is int and obj['n']==5 and type(obj['k'])is int and obj['k']==2,'fixed n and threshold')
    need(obj['p']==['19/50','39/100'] and obj['u']==['-1/2','-49/100'] and obj['noise']==['0','7687/25000'],'complete independently fixed strip')
    root=(2,F(19,50),F(39,100),-F(1,2),-F(49,100),F(0),F(7687,25000));found=[];nodes=0
    def visit(z,d,path):
        nonlocal nodes;nodes+=1
        need(type(z)is dict and len(path)<=20,'finite exact tree')
        if set(z)=={'q','theta'}:found.append(dict(path=path,**leaf(z['q'],z['theta'],d)));return
        need(set(z)=={'axis','children'} and z['axis']in('p','u') and type(z['children'])is list and len(z['children'])==2,'both closed children')
        axis=1 if z['axis']=='p' else 3;mid=(d[axis]+d[axis+1])/2
        dl=list(d);dr=list(d);dl[axis+1]=mid;dr[axis]=mid
        visit(z['children'][0],tuple(dl),path+'0');visit(z['children'][1],tuple(dr),path+'1')
    visit(obj['tree'],root,'');return nodes,found
def main(out):
    files=[Path(__file__),HERE/'check_tensors.py',OBJ]+[t.CONSTRUCT/n for n in ('model.py','model_v2.py','model_v3.py')]+[p for p in sorted((t.CONSTRUCT/'native').glob('*')) if p.is_file()]
    before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    need(before[str(OBJ)]==OBJ_SHA,'selected actual proof object bytes')
    obj=json.loads(OBJ.read_text(),object_pairs_hook=unique)
    nodes,leaves=admit(obj)
    controls=[]
    for name,edit in [('wrong region',lambda z:z.update(u=['-1/2','1/2'])),('missing closed half',lambda z:z['tree']['children'].pop())]:
        z=copy.deepcopy(obj);edit(z)
        try:admit(z)
        except ValueError:controls.append(name)
        else:raise ValueError('invalid cover accepted')
    after={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files};need(before==after,'source/object stability')
    result=dict(status='PASS_INDEPENDENT_FIXED_STRIP_ADMISSION',scope='n5,k2,p[.38,.39],u[-.5,-.49], full original noise; conditional same-law implication, not original acquisition or full row.',
      nodes=nodes,leaves=leaves,controls=controls,source_sha256=before,
      independent_routes='Direct moment polynomial plus sparse power-to-Bernstein; adaptive Bernstein ray check instead of Sturm; direct 40-term rational Gaussian integral instead of grid recurrence. Gaussian normalization constants shared.')
    out=Path(out);out.mkdir(parents=True,exist_ok=False);(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('leaves','source_sha256')}))
if __name__=='__main__':main(sys.argv[1])
