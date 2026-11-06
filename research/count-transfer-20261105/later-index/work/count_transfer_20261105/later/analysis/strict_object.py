"""Canonical, unambiguous rational proof-object data; no arithmetic decision."""
from fractions import Fraction
import json
def need(ok,msg):
 if not ok:raise ValueError(msg)
def unique(items):
 d={}
 for key,value in items:need(key not in d,'duplicate JSON key');d[key]=value
 return d
def read(path,n=39):
 obj=json.loads(path.read_text(),object_pairs_hook=unique);validate(obj,n);return obj
def validate(obj,n=39):
 need(type(obj)is dict and set(obj)=={'q','theta'},'exact proof object fields')
 need(type(obj['q'])is list and len(obj['q'])==n+1,'all ordered mixture quartics')
 values=[obj['theta']]
 for row in obj['q']:
  need(type(row)is list and len(row)==5,'five ordered coefficients');values.extend(row)
 for value in values:
  need(type(value)is str,'rational data must be strings')
  try:f=Fraction(value)
  except(ValueError,ZeroDivisionError):raise ValueError('finite rational')
  need(str(f)==value,'canonical rational string')
 need(0<=Fraction(obj['theta'])<=1,'convex price blend')
 return obj
