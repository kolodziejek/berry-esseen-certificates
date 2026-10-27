#!/usr/bin/env python3
"""Bounded support diagnostics: never an acceptance program."""
from fractions import Fraction as F
from pathlib import Path
import importlib.util,json
p=Path('mathematics/simplification/2026-10-27/check_grouped_support.py')
import sys
sys.path.insert(0,str(p.parent.resolve()))
import check_grouped_support as g
from check_support_lift import A,H4,B2,add,scale,times
for R,r,b,count in g.TABLE:
 R,r,b=map(F,(R,r,b));U=F(21,5) if R==F(96,25) else F(39,10)
 E=add(scale([0,F(3,20),0,0,0,F(1,100)],F(1,41)),scale([-2,0,3],F(51,960*41)/g.ELL),[0,F(1,8*41**2)])
 Q=[r*F(48,125)/42,3*b,F(3,2)*r,-1]
 P=add(scale(add(times(A,A),B2),F(2,5)*g.S**3),scale(times(E,A),g.S**3),times(scale(Q,g.C),A))
 polys={'A':A,'H4':H4,'quarter':add(scale(A,6*g.ELL),scale(H4,-1)),'negative_Q':scale(Q,-1),'negative_P4':scale(P,-1)}
 gate={k:min(g.coefficients(v,R,U)) for k,v in polys.items()}
 print(json.dumps({'R':str(R),'minima':{k:str(v) for k,v in gate.items()},'passed':min(gate.values())>0}),flush=True)
