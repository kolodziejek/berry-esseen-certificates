from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
HERE=Path(__file__).resolve().parent
ours=HERE.parent/'low-noise-panels01/stdout.json';peer=HERE/'independent-stdout.json'
a=json.loads(ours.read_text());b=json.loads(peer.read_text());d=[]
assert len(a['panels'])==len(b['panels'])==13
for x,y in zip(a['panels'],b['panels']):
 assert x['index']==y['index'] and x['p']==y['p']
 for key in ('vmin','vmax','theta_upper'):assert F(x[key])==F(y[key])
 assert [F(x['beta_lower']),F(x['beta_upper'])]==[F(t)for t in y['beta']]
 assert 0<=F(y['ell_lower'])-F(x['ell_lower'])<F(1,10**10)
 assert 0<=F(x['rho_upper'])-F(y['rho_upper'])<F(1,10**8)
 for side in ('negative','positive'):
  xu,yu=F(x[side]['heat_upper']),F(y[side]['contact_upper'])
  assert xu<0 and yu<0 and abs(xu-yu)<F(1,10**7)
  assert all(F(t)<0 for t in x[side]['ray_signs'])
  assert all(F(t)<0 for t in y[side]['Q_derivatives']+y[side]['L_derivatives'])
  d.append(abs(xu-yu))
print(json.dumps({'status':'PASS_EXACT_ROW_COMPARISON','rows':13,'boundaries':26,'both_sets_strict_ray_signs':156,'maximum_boundary_difference':str(max(d)), 'constructor_sha256':sha256(ours.read_bytes()).hexdigest(),'independent_output_sha256':sha256(peer.read_bytes()).hexdigest(),'scope':'Exact outputs compared; independent checker not imported or rerun here. Different directed-root grids retained.'},indent=2))
