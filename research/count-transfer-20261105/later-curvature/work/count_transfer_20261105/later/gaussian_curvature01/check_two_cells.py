"""Two fixed closed p cells, same moment/curvature kernel and forty quartics."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import sys,json,time
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import check_full_p as original
old=original.old;r=original.r;m=original.m;curvature=original.curvature
N=39;K=15
CELLS=((F(19,50),F(77,200)),(F(77,200),F(39,100)))
UL=-F(1,100);UH=F(1,100)
def validate_cover(cells):
    m.need(type(cells)is tuple and cells==((F(19,50),F(77,200)),(F(77,200),F(39,100))),'exact complete two-cell cover')
    m.need(all(type(z)is F for c in cells for z in c),'exact rational cover endpoints')
    m.need(cells[0][0]<cells[0][1]==cells[1][0]<cells[1][1],'closed ordered shared boundary')

def check_cell(obj,progress,PL,PU,UL,UH):
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
    out=Path(sys.argv[1]);m.need(not out.exists(),'fresh output');validate_cover(CELLS)
    pins=json.loads((HERE/'TWO_CELL_SOURCE_PINS.json').read_text())
    for name,h in pins.items():m.need(m.sha(HERE/name)==h,'pinned complete source and object closure')
    obj=old.strict_object.read(old.BASE/'N39_TANGENT_CANDIDATE.json');out.mkdir();tt=time.monotonic();cells=[]
    for index,(pl,pu) in enumerate(CELLS):
        progress={}
        try:cell=check_cell(obj,progress,pl,pu,UL,UH)
        except ValueError as e:
            (out/'FAILED.json').write_text(json.dumps(dict(status='TWO_CELL_BOUND_NOT_ESTABLISHED',reason=str(e),failed_cell=index,progress=progress,completed=cells,full_original_row=False),indent=2)+'\n');raise
        cells.append(cell)
        print(json.dumps(dict(cell=index,status=cell['status'],cleared_margin=cell['cleared_margin'])),flush=True)
    for name,h in pins.items():m.need(m.sha(HERE/name)==h,'stable complete source and object closure')
    result=dict(status='PASS_EXACT_FULL_P_NARROW_PHASE_SHARP39_TWO_CELL_CURVATURE_COVER',n=N,k=K,p=['19/50','39/100'],u=['-1/100','1/100'],noise=['0','37/200'],closed_cover=[list(map(str,c))for c in CELLS],cells=cells,score_coefficients=sum(c['score_coefficients']for c in cells),psd_coefficients=sum(c['psd_coefficients']for c in cells),global_rays=sum(c['global_rays']for c in cells),source_sha256=pins,reader_sha256=m.sha(__file__),object_sha256=m.sha(old.BASE/'N39_TANGENT_CANDIDATE.json'),seconds=time.monotonic()-tt,full_original_row=False)
    (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in('source_sha256','cells')}))
if __name__=='__main__':main()
