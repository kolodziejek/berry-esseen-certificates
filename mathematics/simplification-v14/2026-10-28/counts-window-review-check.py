"""Independent exact controls for the all-law window/tail/final review.

No constructor/checker imports. The universal proof is in the review report;
actual binomial cases supplement, rather than replace, its continuum bounds.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse,hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path,required=True)
args=parser.parse_args()
PIN='ad48f1eae57817b955016c6a12114e3929852a3e636afcfbb91646697b4c6509'
data=args.source.read_bytes()
if hashlib.sha256(data).hexdigest()!=PIN:raise RuntimeError('Reviewed source changed')
A=F(3,5);N=6000;L=F(3,40);U=F(9,25)
# Kernel support, actual residual variance, and the complete fourth-moment tail.
M=A*A*F(5,2)+3*F(5,2)**2*U
assert M==F(153,20)
S=(F(5,42)**4+F(5,42)**3/3+F(5,52)**4+F(5,52)**3/3)*M
assert S==F(5536030025,631986840576)<F(1,100)
assert F(46,25)**2*(F(1,4)+U/N)<F(47,50)**2
assert F(47,50)+1+10<12
# Independent finite-Stirling mass bound, deliberately different from constructor.
xlo=F(199,500);xhi=F(133,250)
assert min(xlo*(1-xlo),xhi*(1-xhi))>F(19,80)
assert xlo>F(1,3) and xhi<F(2,3)
alpha=F(144,1)/(2*N*F(19,80))+F(1,2*N)
assert alpha==F(24,475)+F(1,12000)<1
masssquare=F(7,11)*(1-alpha)**2
assert masssquare>F(9,16)
# Strict positivity of the retained-window loss and the final exact residual.
assert F(19,100)*L-F(39,N)>0
assert F(3,4)*F(19,100)==F(57,400)
assert F(3,4)*39==F(117,4)
assert N>77**2 and L>F(27,100)**2
assert F(117,4)+5==F(137,4)
residual=F(57,400)-F(137,4)/(N*L)-F(25,24*77)-F(23,24*77)/F(27,100)
assert residual==F(2411,356400)>F(1,200)
assert residual-F(1,200)==F(629,356400)
# The curvature coefficient c is strictly below .46 on the complete domain.
assert F(46,25)**2*(F(1,4)+U/N)<(F(47,100)+F(23,50))**2
assert 1/(4*F(6,25))==F(25,24)
assert F(23,50)/(2*F(6,25))==F(23,24)
# Actual exact binomial controls at near-boundary means and both window edges.
records=[];minimum=None
for n in [6000,6001,10000]:
 for p in [F(2,5),F(1,2),F(53,100)]:
  k=(n*p).__floor__()
  for offset in [-11,0,11]:
   i=k+offset;assert abs(i-n*p)<12
   pi=F(comb(n,i))*p**i*(1-p)**(n-i)
   value=n*pi*pi;assert value>F(9,16)
   if minimum is None or value<minimum:minimum=value
   records.append({'n':n,'p':str(p),'i':i,'offset_from_floor_np':offset})
# A genuinely too-wide window fails the same 3/4 normalized-mass claim.
n=6000;i=3050;pi=F(comb(n,i),2**n)
assert n*pi*pi<F(9,16)
# A residual variance cannot be replaced by lambda without allocation inflation.
# Actual U0 centered on {-3/5,1/6000}, U1=0, n6000,p2/5,lambda9/25.
n=6000;p=F(2,5);eps=F(1,6000);var=A*eps;lam=n*(1-p)*var
assert lam==U
terms=n-1;residual_var=terms*var;assert residual_var>lam
fourth=terms*var*(A*A-A*eps+eps*eps)+3*terms*(terms-1)*var*var
false=A*A*lam+3*lam*lam
assert fourth>false and fourth<=M*lam
print(json.dumps({'status':'PASS_INDEPENDENT_WINDOW_TAIL_FINAL','reviewed_source_sha256':PIN,'complete_tail_coefficient':str(S),'independent_mass_squared_bound':str(masssquare),'final_residual':str(residual),'margin_above_lambda_over_200':str(residual-F(1,200)),'actual_binomial_cases':len(records),'minimum_actual_normalized_mass_squared_lower_12decimals':str(F((minimum*10**12).__floor__(),10**12)),'negative_controls':{'wide_window':'sqrt(n)pi_(np+50) < 3/4 at n6000,p1/2','false_common_residual_variance':'actual residual fourth moment exceeds A^2 lambda+3lambda^2'},'records':records,'scope':'Independent continuum window, complete-tail and terminal-scalar audit, conditional on the separately reviewed unweighted gain and phase/normal bounds. No constructor code imported.','python':sys.version},indent=2))
