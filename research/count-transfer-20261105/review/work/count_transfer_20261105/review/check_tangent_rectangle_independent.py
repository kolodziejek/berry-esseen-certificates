"""Independent sparse expansion of selected complete rectangle targets.

This is an algebra/semantic review, not a replacement global-majorant reader.
The constructor's exact Gaussian enclosures are shared numerical primitives.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, isqrt
import hashlib, json, sys

ROOT=Path(__file__).resolve().parents[3]
SRC=ROOT/'work/count_transfer_20261105/later/analysis'
sys.path.insert(0,str(SRC))
import check_tangent_rectangle as candidate

def need(ok,msg):
    if not ok: raise ValueError(msg)
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def trim(p):return {k:v for k,v in p.items() if v}
def add(*ps):
    r={}
    for p in ps:
        for k,v in p.items():r[k]=r.get(k,F(0))+v
    return trim(r)
def sc(p,v):return trim({k:a*v for k,a in p.items()})
def mul(a,b):
    r={}
    for ka,va in a.items():
        for kb,vb in b.items():
            k=tuple(x+y for x,y in zip(ka,kb));r[k]=r.get(k,F(0))+va*vb
    return trim(r)
def constant(v,dim):return {(0,)*dim:F(v)} if v else {}
def variable(i,dim):return {tuple(int(j==i)for j in range(dim)):F(1)}
def power(p,n,dim):
    r=constant(1,dim)
    for _ in range(n):r=mul(r,p)
    return r
def evaluate(p,values):return sum((v*product_power(k,values)for k,v in p.items()),F(0))
def product_power(k,values):
    r=F(1)
    for e,v in zip(k,values):r*=v**e
    return r
def from_list(a):return trim({(i,):x for i,x in enumerate(a)})

def expanded_mixture(qs,g0,g1,x,y,dim):
    """Taylor-expand each Q at its shift; form all four shared moments."""
    one=constant(1,dim);p=variable(0,dim);q=add(one,sc(p,-1));v=mul(p,q)
    u=variable(1,dim)if dim==2 else {}
    n=len(qs)-1;k=15;total={}
    pp=[power(p,j,dim)for j in range(n+1)]
    qq=[power(q,j,dim)for j in range(n+1)]
    for j,coef in enumerate(qs):
        shift=add(constant(j-k,dim),sc(u,-1))
        shift2=mul(shift,shift)
        shiftpowers=[power(shift,r,dim)for r in range(5)]
        zeroth=mul(mul(v,v),add(*(sc(shiftpowers[r],coef[r])for r in range(5))))
        # T/v, G/v and L/v are the variance, cubic and endpoint fourth terms.
        T=add(sc(mul(p,x),n-j),sc(mul(q,y),j))
        G=add(sc(mul(p,x),(n-j)*g0),sc(mul(q,y),j*g1))
        L=add(sc(mul(p,x),(n-j)*g0*g0),sc(mul(q,y),j*g1*g1))
        second=mul(mul(T,v),add(constant(coef[2],dim),sc(shift,3*coef[3]),sc(shift2,6*coef[4])))
        third=mul(mul(G,v),add(constant(coef[3],dim),sc(shift,4*coef[4])))
        fourth=add(sc(mul(L,v),coef[4]),sc(mul(T,T),3*F(n-1,n)*coef[4]))
        mass=sc(mul(pp[j],qq[n-j]),F(comb(n,j)))
        total=add(total,mul(mass,add(zeroth,second,third,fourth)))
    return total

def raw_cube(p,q,x,y,g0,g1,dim):
    v=mul(p,q)
    return add(mul(v,add(constant(1,dim),sc(v,-2))),sc(mul(p,x),3),sc(mul(q,y),3),sc(x,-g0),sc(y,g1))

def independent_hessian(qs,g0,g1,coef,theta,W):
    """Extract quadratic coefficients in x,y rather than using the Hessian formula."""
    dim=3;p=variable(0,dim);q=add(constant(1,dim),sc(p,-1));v=mul(p,q)
    x=variable(1,dim);y=variable(2,dim)
    Fnum=expanded_mixture(qs,g0,g1,x,y,dim)
    R=raw_cube(p,q,x,y,g0,g1,dim)
    price=sc(mul(mul(v,v),mul(R,add(constant(5*W,dim),sc(add(v,x,y),-3)))),theta*coef)
    loss=add(Fnum,sc(price,-1))
    need(all(a+b<=2 for _,a,b in loss),'quadratic variance loss')
    return [trim({(i,):factor*z for (i,a,b),z in loss.items()if (a,b)==ab})
            for ab,factor in [((2,0),2),((1,1),1),((0,2),2)]]

def independent_polygon(c,pl,pu):
    r=c['row'];A0=c['A0'];A1=c['A1'];d=F(r['d0']);L=F(r['Lambda'])
    g=F(r['gap_charge']);h=F(r['noise_charge'])
    inequalities=[(-F(1),F(0),F(0)),(F(0),-F(1),F(0)),(F(1),F(1),L/39),
      (1/((1-pl)*A0)+39*d/L,1/(pu*A1)+39*d/L,d),
      (g/((1-pl)*A0)+39*h,g/(pu*A1)+39*h,F(r['D'])-F(r['binary_charge']))]
    vertices=set()
    for (a,b,c0),(d,e,f)in combinations(inequalities,2):
        determinant=a*e-b*d
        if determinant:
            point=((c0*e-b*f)/determinant,(a*f-c0*d)/determinant)
            if all(A*point[0]+B*point[1]<=C for A,B,C in inequalities):vertices.add(point)
    need(len(vertices)>=3 and (F(0),F(0))in vertices,'bounded polygon with origin')
    return sorted(vertices)

def inverse_univariate(coeffs):
    """Expand sum b_i binom(d,i)t^i(1-t)^(d-i), independently of forward transform."""
    d=len(coeffs)-1;out={}
    for i,b in enumerate(coeffs):
        for h in range(d-i+1):
            key=(i+h,);out[key]=out.get(key,F(0))+b*comb(d,i)*comb(d-i,h)*(-1)**h
    return trim(out)
def local_univariate(p,l,h):
    out={}
    for (i,),a in p.items():
        for j in range(i+1):out[j,]=out.get((j,),F(0))+a*comb(i,j)*l**(i-j)*(h-l)**j
    return trim(out)
def local_tensor(p,l,h,a,b):
    out={}
    for (i,j),v in p.items():
        for r in range(i+1):
            for s in range(j+1):
                key=r,s;out[key]=out.get(key,F(0))+v*comb(i,r)*l**(i-r)*(h-l)**r*comb(j,s)*a**(j-s)*(b-a)**s
    return trim(out)
def inverse_tensor(rows):
    # Expand the phase Bernstein basis first, then the probability basis.
    phase=[inverse_univariate(row)for row in rows];out={}
    for s in range(5):
        polynomial=inverse_univariate([row.get((s,),F(0))for row in phase])
        for (r,),v in polynomial.items():out[r,s]=v
    return trim(out)
def rational_upper_sqrt(v):
    s=10**30;k=isqrt(v.numerator*s*s//v.denominator)
    need(F(k,s)**2<=v<F(k+1,s)**2,'directed square root');return F(k+1,s)

def actual_law_controls(c,coef,W):
    # These are bounded semantic laws, not assertions of the original contact conditions.
    p=F(77,200);q=1-p;v=p*q;A=c['A0'];d=c['a0'];checked=0;zero=0
    def law(L,R):
        if L==0 or R==0:return [(F(0),F(1))]
        return [(-L,R/(L+R)),(R,L/(L+R))]
    for L0,R0,L1,R1 in [(0,0,0,0),(A,F(1,10**6),F(1,10**6),A),
                        (F(1,100),d/4,d/4,F(1,100)),
                        (A,F(1,10**12),0,0),(0,0,F(1,10**12),A),
                        (p,d/8,d/8,q)]:
        laws=[law(F(L0),F(R0)),law(F(L1),F(R1))]
        moments=[[sum((prob*z**i for z,prob in zlaw),F(0))for i in range(5)]for zlaw in laws]
        need(all(m[1]==0 for m in moments),'actual centered components')
        x=q*moments[0][2];y=p*moments[1][2];w=v+x+y
        if w>W:continue
        mu0=moments[0][3];mu1=moments[1][3]
        raw=v*(1-2*v)+3*p*x+3*q*y-q*mu0+p*mu1
        actual=q*sum((prob*abs(z-p)**3 for z,prob in laws[0]),F(0))+p*sum((prob*abs(z+q)**3 for z,prob in laws[1]),F(0))
        need(raw==actual and raw>0,'actual raw absolute cube identity')
        factor=5*W-3*w
        need(factor>0 and 4*W**5-factor*factor*w**3>=0,'exact squared tangent inequality')
        # Fourth-moment support bound for each actual conditional law.
        for mom,L,R in zip(moments,map(F,(L0,L1)),map(F,(R0,R1))):
            need(mom[4]<=(R-L)*mom[3]+L*R*mom[2],'actual fourth support inequality')
            zero+=int(mom[2]==0)
        checked+=1
    # Omitting mixture curvature gives an indefinite price Hessian.
    r0=3*p+A;r1=3*q+A
    need(4*r0*r1-(r0+r1)**2<0,'negative control: price alone need not be convex')
    need(4*W**5-(5*W-3*(2*W))**2*(2*W)**3<0,'negative control: w<=W licenses positive tangent price')
    return checked,zero

def main():
    need(__debug__ and not sys.flags.optimize,'ordinary interpreter only')
    out=Path(sys.argv[1]);need(not out.exists(),'fresh output')
    pins=json.loads((SRC/'PUBLIC_SOURCE_PINS.json').read_text())
    closure=[Path(__file__),SRC/'PUBLIC_SOURCE_PINS.json']+[SRC/rel for rel in pins]
    before={str(p.relative_to(ROOT)):sha(p)for p in closure}
    for rel,h in pins.items():need(sha(SRC/rel)==h,'current source closure')
    c=candidate.m.context(39,True);obj=json.loads((SRC/'N39_TANGENT_CANDIDATE.json').read_text())
    qs=[list(map(F,row))for row in obj['q']];theta=F(obj['theta'])
    need(c['row']['p']==['19/50','39/100'] and c['L']==F(37,200),'original selected domain')
    need(c['a0']==c['a1']==F(233,10000)<min(F(3849,10000),1-F(3851,10000)),'same inward caps throughout rectangle')
    corners=list(product((-c['A0'],F(0),c['a0']),(c['A1'],F(0),-c['a1'])))
    moment_sets=hessian_sets=univariate_coeffs=tensor_coeffs=mutants=0
    min_margin=None
    for strip in (0,3):
        pl=F(3849,10000)+F(strip,20000);pu=pl+F(1,20000);ul=-F(1,1000);uh=F(1,1000)
        need(15+ul>=0 and 15+uh<=39,'threshold endpoint gate')
        amin=15+ul-39*pu;amax=15+uh-39*pl
        need(amax<=0 and amin*amin<=3*39*pl*(1-pl),'whole negative Gaussian concavity')
        W=pu*(1-pu)+c['L']/39
        coef=candidate.m.norm.CE_LO/(2*rational_upper_sqrt(F(39))*W*W*rational_upper_sqrt(W))
        vertices=independent_polygon(c,pl,pu)
        need(vertices==candidate.polygon(c,pl,pu),'complete polygon equality')
        need(all(39*(x+y)<=c['L'] for x,y in vertices),'whole polygon variance cap')
        for g0,g1 in corners:
            own=independent_hessian(qs,g0,g1,coef,theta,W)
            other=candidate.hessian_polynomials(qs,c,coef,theta,g0,g1)
            need(own==[from_list(a)for a in other],'full independent Hessian coefficient identity')
            hessian_sets+=1
            determinant=add(mul(own[0],own[2]),sc(mul(own[1],own[1]),-1))
            for poly,degree in ((own[0],41),(own[2],41),(determinant,82)):
                need(max((k[0]for k in poly),default=0)<=degree,'whole-p degree')
                ar=[poly.get((i,),F(0))for i in range(degree+1)]
                b=candidate.bern(ar,pl,pu,degree)
                need(inverse_univariate(b)==local_univariate(poly,pl,pu),'independent inverse Bernstein identity')
                need(min(b)>=0,'PSD positivity');univariate_coeffs+=degree+1
                bad=list(b);bad[degree//2]+=1
                need(inverse_univariate(bad)!=local_univariate(poly,pl,pu),'Bernstein mutant rejected');mutants+=1
        # One shared corner per polygon vertex, covering outward/zero/inward cases.
        for (x,y),(g0,g1)in zip(vertices,[corners[0],corners[4],corners[8]]):
            own=expanded_mixture(qs,g0,g1,constant(x,2),constant(y,2),2)
            arr=candidate.mixture(qs,x,y,g0,g1)
            other=trim({(i,j):a for j,row in enumerate(arr)for i,a in enumerate(row)})
            need(own==other,'full independent moment coefficient identity');moment_sets+=1
            need(max(i for i,j in own)<=43 and max(j for i,j in own)<=4,'score degrees')
            p=variable(0,2);q=add(constant(1,2),sc(p,-1));v=mul(p,q)
            R=raw_cube(p,q,constant(x,2),constant(y,2),g0,g1,2)
            gaussian=candidate.m.normal(amin,39*pu*(1-pu)+39*(x+y))
            floor=candidate.m.norm.CE_LO/rational_upper_sqrt(F(39))
            target=add(sc(mul(v,v),gaussian+(1-theta)*floor),
                       sc(mul(mul(v,v),mul(R,add(constant(5*W-3*(x+y),2),sc(v,-3)))),theta*coef))
            score=add(target,sc(own,-1))
            b_p=[candidate.bern([score.get((i,j),F(0))for i in range(44)],pl,pu,43)for j in range(5)]
            tensor=[candidate.bern([b_p[j][i]for j in range(5)],ul,uh,4)for i in range(44)]
            need(inverse_tensor(tensor)==local_tensor(score,pl,pu,ul,uh),'independent full tensor reconstruction')
            low=min(z for row in tensor for z in row);need(low>0,'selected whole-box positivity')
            min_margin=low if min_margin is None else min(low,min_margin);tensor_coeffs+=220
            mutated={**own};mutated[0,0]=mutated.get((0,0),F(0))+1
            need(mutated!=other,'moment coefficient mutant');mutants+=1
        if strip==0:law_cases,zero_cases=actual_law_controls(c,coef,W)
        print(json.dumps({'strip':strip,'independent_hessian_sets':hessian_sets,'independent_moment_sets':moment_sets}),flush=True)
    after={str(p.relative_to(ROOT)):sha(p)for p in closure};need(after==before,'stable source closure')
    result={'status':'PASS_INDEPENDENT_SELECTED_CONTINUOUS_TANGENT_ALGEBRA',
      'scope':'First and last closed p strips; all nine complete Hessian polynomial triples on each, three full moment/score tensors on each. Shared directed Gaussian primitive; no independent global-ray or complete original-row admission.',
      'n':39,'p':['3849/10000','3851/10000'],'u':['-1/1000','1/1000'],'noise':['0','37/200'],
      'independent_hessian_sets':hessian_sets,'independent_moment_tensors':moment_sets,
      'inverse_univariate_coefficients':univariate_coeffs,'inverse_tensor_coefficients':tensor_coeffs,
      'coefficient_mutants':mutants,'actual_law_semantic_cases':law_cases,'zero_variance_components':zero_cases,
      'negative_convexity_and_range_controls':2,'cleared_selected_margin':str(min_margin),
      'sources_unchanged':True,'source_sha256_before':before,'source_sha256_after':after,
      'full_original_row':False,'acquisition_rerun':False}
    out.mkdir();(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if not k.startswith('source_sha256')}))
if __name__=='__main__':main()
