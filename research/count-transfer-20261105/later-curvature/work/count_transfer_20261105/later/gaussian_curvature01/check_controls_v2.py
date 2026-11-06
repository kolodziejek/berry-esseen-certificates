"""Cheap exact scalar/algebra controls for the additive curvature lemma."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import check_full_p as c
def need(x,m):
    if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    need(__debug__ and not sys.flags.optimize and len(sys.argv)==2,'ordinary Python NEW_OUTPUT')
    out=Path(sys.argv[1]);need(not out.exists(),'fresh output');out.mkdir()
    M,rec=c.curvature(c.N,c.K,c.PL,c.PU,c.UL,c.UH);checks=0;identities=0
    # Rationally bound g''/phi at both signs, collisions, and closed endpoints.
    for p in [c.PL,(c.PL+c.PU)/2,c.PU]:
      for u in [c.UL,F(0),c.UH]:
       for lam in [F(0),F(37,400),F(37,200)]:
        a=c.K+u-c.N*p;D=c.N*p*(1-p)+lam;slo=c.m.norm.root(D)[0]
        if a<=0:need(a*(3*D-a*a)<=0,'negative branch sign')
        else:
            upper=a*(3*D-a*a)*c.m.norm.PHI_HI/(4*D**3*slo)
            need(upper<=M,'positive branch directed curvature upper')
        # Differentiate -a*phi/(2*D^(3/2)), using phi'/phi=a²/(2D²).
        left=-a*F(1,2)*(a*a/F(2)*D**-3-F(3,2)*D**-2)
        right=a*(3*D-a*a)/(4*D**3)
        need(left==right,'second derivative after multiplying by sqrt(D)')
        checks+=1;identities+=1
    # a=0 is an exact collision regardless of noise.
    for D in [F(1),F(22971,2500),F(10)]:
        a=F(0);need(a*(3*D-a*a)==0,'zero numerator');checks+=1
    # Matrix correction identity, including an indefinite H0: no PSD inference
    # is made until the corrected matrix's three minors are separately checked.
    matrix_checks=0
    for A,B,D in [(F(2),F(1),F(3)),(F(-1),F(4),F(2))]:
      for g in [-F(1),F(0),M]:
        for z in (A,B,D):need((z-c.N*c.N*M)+c.N*c.N*(M-g)==z-c.N*c.N*g,'rank-one correction identity')
        matrix_checks+=1
    rejected=0
    for args in [(0,15,c.PL,c.PU,c.UL,c.UH),(39,15,F(0),c.PU,c.UL,c.UH),(39,15,c.PU,c.PL,c.UL,c.UH),(39,15,c.PL,c.PU,c.UH,c.UL),(39,-100,c.PL,c.PU,c.UL,c.UH)]:
        try:c.curvature(*args)
        except ValueError:rejected+=1
        else:raise ValueError('bad curvature domain accepted')
    need(rejected==5,'all malformed domains reject')
    result=dict(status='PASS_CURVATURE_SCALAR_CONTROLS',scalar_domain_checks=checks,exact_derivative_identities=identities,rank_one_matrix_identities=matrix_checks,domain_rejections=rejected,reader_sha256=sha(HERE/'check_full_p.py'),source_sha256=sha(__file__),no_continuous_score_claim=True)
    (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
