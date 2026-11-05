"""Bounded exact algebra/actual-law controls and named n39 gate obstruction."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from itertools import product
import json,sys,copy
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import pilot as m
def moments(law):return [sum(prob*x**k for x,prob in law)for k in range(5)]
def convolve_moments(a,b):return [sum(F(comb(k,j))*a[j]*b[k-j]for j in range(k+1))for k in range(5)]
def law(L,R):return [(F(0),F(1))]if not L or not R else[(-L,R/(L+R)),(R,L/(L+R))]
def main():
 m.need(__debug__ and not sys.flags.optimize,'ordinary Python');out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
 obj=json.loads((HERE/'N6_FIXED_CANDIDATE.json').read_text());c=m.context(6,False);baseline=m.check(c,obj['q'],obj['theta']);rejects=[]
 bads=[('missing count',obj['q'][:-1],obj['theta']),('duplicate count',obj['q']+[obj['q'][0]],obj['theta']),('short coefficient',[[*obj['q'][0][:-1]]]+obj['q'][1:],obj['theta']),('negative blend',obj['q'],'-1/10'),('blend over one',obj['q'],'11/10')]
 z=copy.deepcopy(obj['q']);z[0][0]='-1';bads.append(('failed closed atom',z,obj['theta']))
 z=copy.deepcopy(obj['q']);z[1][4]='0';bads.append(('nonpositive leading coefficient',z,obj['theta']))
 for name,q,t in bads:
  try:m.check(c,q,t)
  except ValueError:rejects.append(name)
  else:raise ValueError('mutation admitted '+name)
 comparisons=0;cube_checks=0;variance_checks=0
 for n in [6,39]:
  p=F(77,200);q=1-p;v=p*q
  pairs=list(product([law(F(1,2),F(1,10)),law(F(2,3),F(1,20)),law(F(0),F(0))],[law(F(1,10),F(1,2)),law(F(1,20),F(3,5)),law(F(0),F(0))]))
  for l0,l1 in pairs:
   a=moments(l0);b=moments(l1);x=q*a[2];y=p*b[2]
   raw=q*sum(prob*(p-z)**3 for z,prob in l0)+p*sum(prob*(q+z)**3 for z,prob in l1)
   m.need(raw==v*(1-2*v)+3*p*x+3*q*y-q*a[3]+p*b[3],'same-law absolute cubic identity');cube_checks+=1
   for j in range(n+1):
    acc=[F(1),F(0),F(0),F(0),F(0)]
    for _ in range(n-j):acc=convolve_moments(acc,a)
    for _ in range(j):acc=convolve_moments(acc,b)
    t=(n-j)*a[2]+j*b[2];s3=(n-j)*a[3]+j*b[3]
    fourth=(n-j)*a[4]+j*b[4]+3*(t*t-(n-j)*a[2]**2-j*b[2]**2)
    m.need(acc[2]==t and acc[3]==s3 and acc[4]==fourth,'independent moment convolution')
    m.need(fourth<=(n-j)*a[4]+j*b[4]+3*F(n-1,n)*t*t,'finite Cauchy fourth bound');comparisons+=1
    m.need((n-j)*a[2]**2+j*b[2]**2>=t*t/n,'Cauchy variance allocation');variance_checks+=1
 # An exact obstruction only to the current fixed-multiplier convex blend.
 c39=m.context(39,True);n,p,q,v,k=(c39[z]for z in('n','p','q','v','k'))
 m.need((F(0),F(0))in c39['vertices'],'retained zero-noise vertex')
 ph=m.normal(F(k)-n*p,n*v);cdf=sum(F(comb(n,j))*p**j*q**(n-j)for j in range(k+1));wmax=v+c39['L']/n
 floor=m.norm.CE_LO/m.norm.root(F(n))[1];priced=m.norm.CE_LO*v*(1-2*v)/(m.norm.root(F(n))[1]*wmax*m.norm.root(wmax)[1])
 current=ph+max(floor,priced)-cdf;binary=ph+m.norm.CE_LO*(1-2*v)/(m.norm.root(F(n))[1]*m.norm.root(v)[1])-cdf
 m.need(current<0<binary,'fixed-price gate obstruction, not theorem obstruction')
 r={'status':'PASS_BOUNDED_ALGEBRA_CONTROLS_AND_FIXED_GATE_OBSTRUCTION','baseline_cdf_margin':baseline['exact_cdf_margin'],'rejected_mutations':rejects,'actual_law_cube_checks':cube_checks,'exact_moment_convolution_checks':comparisons,'cauchy_checks':variance_checks,
  'n39_obstruction':{'scope':'Only fixed full-noise lower cubic-price convex-blend gate; not no-go for new certificates, original acquired extremizers or the theorem.','p':str(p),'k':k,'u':'0','current_target_minus_binary_cdf':str(current),'actual_binary_target_margin_lower':str(binary)},'source_sha256':m.sha(__file__)}
 (out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
if __name__=='__main__':main()
