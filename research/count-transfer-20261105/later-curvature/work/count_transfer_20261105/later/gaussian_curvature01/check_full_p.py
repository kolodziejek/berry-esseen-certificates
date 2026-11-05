"""One source-bound full-p/narrow-phase test; fixed forty quartics, no discovery."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import sys,json,time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'gaussian_taylor01'))
import check_broad as old
r=old.r;m=old.m
N=39;K=15;PL=F(19,50);PU=F(39,100);UL=-F(1,100);UH=F(1,100)

def curvature(n,k,pl,pu,ul,uh):
    """Uniform upper bound on d²/dlambda² Phi((k+u-np)/sqrt(npq+lambda))."""
    m.need(type(n)is int and n>0 and 0<pl<pu<F(1,2) and ul<uh,'ordered curvature domain')
    amin=F(k)+ul-n*pu;amax=F(k)+uh-n*pl
    dmin=n*pl*(1-pl);sqrtlo=m.norm.root(dmin)[0]
    m.need(dmin>0 and sqrtlo>0 and sqrtlo*sqrtlo<=dmin,'positive directed denominator')
    m.need(min(amin,F(0))**2<=3*dmin,'negative numerator has nonpositive noise curvature')
    M=3*max(amax,F(0))*m.norm.PHI_HI/(4*dmin*dmin*sqrtlo)
    m.need(M>=0,'nonnegative uniform curvature upper bound')
    return M,dict(numerator=[str(amin),str(amax)],D_lower=str(dmin),sqrt_D_lower=str(sqrtlo),phi_zero_upper=str(m.norm.PHI_HI),gaussian_noise_curvature_upper=str(M))

def check(obj,progress):
    c=m.context(N,True);qs=[list(map(F,z))for z in obj['q']];theta=F(obj['theta'])
    m.need(len(qs)==N+1 and all(len(q)==5 for q in qs) and 0<=theta<=1,'original complete count family')
    m.need(c['a0']<=PL and c['a1']<=1-PU,'same fixed inward caps valid throughout')
    M,record=curvature(N,K,PL,PU,UL,UH);progress['curvature']=record
    for q in qs:
        m.need(q[4]>0,'positive fourth coefficient')
        m.sturm.positive(m.compact(q,-1,F(1)));m.sturm.positive(m.compact(q,1,F(0)))
    progress['global_rays']=2*len(qs)
    W=PU*(1-PU)+c['L']/N
    coef=m.norm.CE_LO/(2*m.norm.root(F(N))[1]*W*W*m.norm.root(W)[1])
    floor=m.norm.CE_LO/m.norm.root(F(N))[1]
    corners=list(product((-c['A0'],F(0),c['a0']),(c['A1'],F(0),-c['a1'])))
    vertices=r.polygon(c,PL,PU);psd=[];correction=r.scale(r.V2,N*N*M)
    for g0,g1 in corners:
        a,b,d=r.hessian_polynomials(qs,c,coef,theta,g0,g1)
        a=r.add(a,r.scale(correction,-1));b=r.add(b,r.scale(correction,-1));d=r.add(d,r.scale(correction,-1))
        det=r.add(r.mul(a,d),r.scale(r.mul(b,b),-1))
        mins=[min(r.bern(a,PL,PU,41)),min(r.bern(d,PL,PU,41)),min(r.bern(det,PL,PU,82))]
        psd.append(dict(gamma=list(map(str,(g0,g1))),minima=list(map(str,mins))))
        progress['corrected_psd']=psd
        m.need(min(mins)>=0,'whole-p curvature-corrected exact PSD polynomials')
    reserve=None;gaussians=[]
    for x,y in vertices:
        G,record=old.gaussian(N,K,PL,PU,UL,UH,N*(x+y));gaussians.append(record)
        for g0,g1 in corners:
            expect=r.mixture(qs,x,y,g0,g1)
            raw=r.add(r.mul(r.V,r.add([F(1)],r.scale(r.V,-2))),r.add(r.add(r.scale(r.P,3*x),r.scale(r.Q,3*y)),[-g0*x+g1*y]))
            tangent=r.scale(r.mul(r.V2,r.mul(raw,r.add([5*W-3*(x+y)],r.scale(r.V,-3)))),theta*coef)
            target=[r.mul(r.V2,g)for g in G]+[[F(0)],[F(0)]]
            target[0]=r.add(target[0],r.add(r.scale(r.V2,(1-theta)*floor),tangent))
            loss=[r.add(target[h],r.scale(expect[h],-1))for h in range(5)]
            bp=[r.bern(a,PL,PU,43)for a in loss]
            for i in range(44):
                z=min(r.bern([bp[h][i]for h in range(5)],UL,UH,4))
                reserve=z if reserve is None else min(reserve,z)
    progress['score_minimum']=str(reserve)
    m.need(reserve>0,'strict full-p continuous score tensor')
    return dict(status='PASS_EXACT_FULL_P_NARROW_PHASE_SHARP39_CURVATURE_RECTANGLE',n=N,k=K,p=list(map(str,(PL,PU))),u=list(map(str,(UL,UH))),noise=['0','37/200'],variance_vertices=len(vertices),global_rays=2*len(qs),score_coefficients=44*5*len(vertices)*9,psd_coefficients=9*167,cleared_margin=str(reserve),curvature=progress['curvature'],gaussian_enclosures=gaussians,corrected_psd=psd,full_original_row=False)

def main():
    m.need(__debug__ and not sys.flags.optimize and len(sys.argv)==2,'ordinary Python NEW_OUTPUT')
    out=Path(sys.argv[1]);m.need(not out.exists(),'fresh output')
    pins=json.loads((HERE/'SOURCE_PINS.json').read_text())
    for name,h in pins.items():m.need(m.sha(HERE/name)==h,'pinned complete source and object closure')
    obj=old.strict_object.read(old.BASE/'N39_TANGENT_CANDIDATE.json');out.mkdir();tt=time.monotonic();progress={}
    try:result=check(obj,progress)
    except ValueError as e:
        (out/'FAILED.json').write_text(json.dumps(dict(status='REQUESTED_BOUND_NOT_ESTABLISHED',reason=str(e),n=N,k=K,p=list(map(str,(PL,PU))),u=list(map(str,(UL,UH))),noise=['0','37/200'],progress=progress,full_original_row=False),indent=2)+'\n')
        raise
    for name,h in pins.items():m.need(m.sha(HERE/name)==h,'stable complete source and object closure')
    result.update(source_sha256=pins,reader_sha256=m.sha(__file__),object_sha256=m.sha(old.BASE/'N39_TANGENT_CANDIDATE.json'),seconds=time.monotonic()-tt)
    (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k not in('source_sha256','gaussian_enclosures','corrected_psd')}))
if __name__=='__main__':main()
