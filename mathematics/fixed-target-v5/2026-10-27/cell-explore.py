"""Bounded probe of read scalar kernels, never a full stage or acceptance run."""
from pathlib import Path
from fractions import Fraction as F
import sys,json
base=Path(__file__).resolve().parent/'cell-sources'
sys.path.insert(0,str(base))
import kernel as k
import high_window_core as hw
hw.install(k)
k.RADIUS=F(96,25);r=k.RADIUS
k.K4=(r+1)**2/(r+F(1,2));k.K5=(r**3+2*r*r+3*r+F(3,2))/(r+F(1,2));k.constants()
rows=[]
for lo,hi in [(F(1),F(26,25)),(F(9,5),F(1841,1000))]:
 out={}
 for name,lower,upper in [('old',F('.4095'),F('.4247')),('fixed',F('.4097321837023'),F('.4097321837025'))]:
  a=k.initial_cell(42,lo,hi,None,'universal','lower',score_floor=lower,own_cap=upper)
  b=k.initial_cell(42,lo,hi,None,'universal','upper',score_floor=lower,own_cap=upper)
  out[name]={'lower_endpoint':float(a),'upper_endpoint':float(b),'max':float(max(a,b))}
 rows.append({'rho':[str(lo),str(hi)],'bounds':out})
print(json.dumps(rows,indent=2))
