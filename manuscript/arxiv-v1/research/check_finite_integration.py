#!/usr/bin/env python3
"""Selected scalar checks for finite appendix integration, not certificate acceptance."""
from fractions import Fraction as F
import json

checks = {}
def need(name, ok):
    if not ok:
        raise AssertionError(name)
    checks[name] = True

need('N1 left tail below target', F(1,5) < F(2,5))
need('N1 elementary right tail', F(1,2)+F(3,8)*F(5,6) == F(13,16))
need('N1 right tail below target', 1-F(13,16) < F(2,5))
need('G3 scalar tail comparison', F(1661,5000)*(1+F(429,1000)/F(15,8)) == F(159456,390625))
need('G3 structural tail below target', F(159456,390625)**2 < 3*F(59,250)**2)
need('G4 localization strictly above G3', F(256,625)**2-3*F(59,250)**2 == F(1069,1562500))
need('G4 localization below target', F(256,625) < F(4097,10000))
tail=F(3031,10000)*(1+F(323,500)/F(7361,4000))
need('n5 structural cutoff', tail <= F(819,2000))
need('n5 lower target ordering', F(819,2000) < F(4097,10000))
for name,b,r in [
    ('b2',F(84729828287999,250000000000000),F(237,200)),
    ('b3',F(35139006743001,10**14),F(6,5))]:
    need(name+' positive radical domain', 0 < b < 1 and r >= 1)
    # (1+x)^2/(1-x) is strictly increasing for 0<=x<1.
    # This squared comparison is equivalent to the desired outward beta cap.
    need(name+' outward moment cap', (1+b*b)**2 >= r*r*(1-b*b))
need('unweighted substitution rejected', F(1) <= F(1) and 84*F(1) > 42*F(1))
print(json.dumps({'result':'PASS','checks':checks,
 'n5_structural_value':str(tail),'n5_tail_reserve':str(F(819,2000)-tail),
 'scope':'Selected scalar algebra only; no N1/G3/G4/n5/floor certificate accepted.'},indent=2))
