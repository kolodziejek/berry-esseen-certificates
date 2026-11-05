"""Independent corrected-Hessian reconstruction for the two accepted cells."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import isqrt
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
SRC=ROOT/'work/count_transfer_20261105/later/gaussian_curvature01'
RESULT=ROOT/'runs/count_transfer_20261105/later_gaussian_curvature_two01/checked/RESULT.json'
sys.path.insert(0,str(HERE));import check_tangent_rectangle_independent as independent
sys.path.insert(0,str(SRC));import check_two_cells as reader
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    need(__debug__ and not sys.flags.optimize,'ordinary Python')
    out=Path(sys.argv[1]);need(not out.exists(),'fresh output')
    pins=json.loads((SRC/'TWO_CELL_SOURCE_PINS.json').read_text())
    sources=[Path(__file__),HERE/'check_tangent_rectangle_independent.py',SRC/'check_two_cells.py',SRC/'TWO_CELL_SOURCE_PINS.json',RESULT]+[SRC/k for k in pins]
    before={str(p.relative_to(ROOT)):sha(p)for p in sources}
    for rel,h in pins.items():need(sha(SRC/rel)==h,'current complete source closure')
    stored=json.loads(RESULT.read_text());need(stored['status']=='PASS_EXACT_FULL_P_NARROW_PHASE_SHARP39_TWO_CELL_CURVATURE_COVER','selected complete scope')
    need(stored['closed_cover']==[['19/50','77/200'],['77/200','39/100']],'exact adjacent closed cover')
    need(stored['reader_sha256']==sha(SRC/'check_two_cells.py'),'accepted reader source epoch')
    c=reader.m.context(39,True);obj=json.loads((reader.old.BASE/'N39_TANGENT_CANDIDATE.json').read_text())
    qs=[list(map(F,q))for q in obj['q']];theta=F(obj['theta']);N=39
    one={(0,):F(1)};p={(1,):F(1)};q=independent.add(one,independent.sc(p,-1));v=independent.mul(p,q);v2=independent.mul(v,v)
    corners=list(product((-c['A0'],F(0),c['a0']),(c['A1'],F(0),-c['a1'])))
    identities=arrays=scalar_checks=mutations=0
    for idx,(pl,pu)in enumerate(((F(19,50),F(77,200)),(F(77,200),F(39,100)))):
        ul=-F(1,100);uh=F(1,100);a_min=15+ul-N*pu;a_max=15+uh-N*pl
        Dmin=N*pl*(1-pl);scale=10**30
        k=isqrt(Dmin.numerator*scale*scale//Dmin.denominator);lower=F(k,scale)
        need(lower>0 and lower*lower<=Dmin,'directed square root')
        need(min(a_min,F(0))**2<=3*Dmin,'all negative numerators licensed')
        M=3*max(a_max,F(0))*reader.m.norm.PHI_HI/(4*Dmin*Dmin*lower)
        M2,_=reader.curvature(N,15,pl,pu,ul,uh);need(M==M2,'independent scalar curvature formula')
        need(stored['cells'][idx]['curvature']['gaussian_noise_curvature_upper']==str(M),'actual captured curvature bound')
        W=pu*(1-pu)+c['L']/N
        coef=reader.m.norm.CE_LO/(2*independent.rational_upper_sqrt(F(N))*W*W*independent.rational_upper_sqrt(W))
        correction=independent.sc(v2,N*N*M)
        for corner_idx,(g0,g1)in enumerate(corners):
            original=independent.independent_hessian(qs,g0,g1,coef,theta,W)
            corrected=[independent.add(z,independent.sc(correction,-1))for z in original]
            baseline=reader.r.hessian_polynomials(qs,c,coef,theta,g0,g1)
            from_reader=[independent.from_list(reader.r.add(z,reader.r.scale(reader.r.V2,-N*N*M)))for z in baseline]
            need(corrected==from_reader,'complete independent corrected Hessian arrays');arrays+=3
            det=independent.add(independent.mul(corrected[0],corrected[2]),independent.sc(independent.mul(corrected[1],corrected[1]),-1))
            mins=[]
            for poly,degree in ((corrected[0],41),(corrected[2],41),(det,82)):
                coefficients=[poly.get((i,),F(0))for i in range(degree+1)]
                b=reader.r.bern(coefficients,pl,pu,degree)
                need(independent.inverse_univariate(b)==independent.local_univariate(poly,pl,pu),'independent inverse PSD polynomial')
                need(min(b)>=0,'whole closed-cell PSD');mins.append(str(min(b)));identities+=degree+1
            need(mins==stored['cells'][idx]['corrected_psd'][corner_idx]['minima'],'exact captured PSD readback')
            if M>0:
                wrong=[independent.add(z,correction)for z in original]
                need(wrong!=corrected,'wrong curvature sign rejected')
                need([independent.add(z,independent.sc(v2,-N*M))for z in original]!=corrected,'missing chain-rule n rejected')
                mutations+=2
        for pp,uu,lam in product((pl,(pl+pu)/2,pu),(ul,F(0),uh),(F(0),F(37,400),F(37,200))):
            a=15+uu-N*pp;D=N*pp*(1-pp)+lam
            if a<=0:need(a*(3*D-a*a)<=0,'negative/zero actual curvature sign')
            else:
                # Bound g'' <= 3*a*phi(0)/(4*D^(5/2)); square positive terms.
                need((M/reader.m.norm.PHI_HI)**2*16*D**5>=9*a*a,'positive curvature upper via exact square')
            scalar_checks+=1
    after={str(p.relative_to(ROOT)):sha(p)for p in sources};need(after==before,'stable dependencies')
    result={'status':'PASS_INDEPENDENT_TWO_CELL_CURVATURE_HESSIANS','n':39,'k':15,'p':['19/50','39/100'],'u':['-1/100','1/100'],'noise':['0','37/200'],
      'complete_hessian_entry_arrays':arrays,'inverse_psd_coefficients':identities,'exact_scalar_checks':scalar_checks,'sign_and_chain_factor_mutations':mutations,
      'scope':'All corrected Hessian arrays and PSD coefficient readbacks on both fixed closed cells; independent sparse variance-quadratic expansion. Shared scalar constants, score/kernel and majorant reader. No independent full score replay or complete original-row claim.',
      'sources_unchanged':True,'source_sha256_before':before,'source_sha256_after':after,'full_original_row':False}
    out.mkdir();(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if not k.startswith('source_sha')}))
if __name__=='__main__':main()
