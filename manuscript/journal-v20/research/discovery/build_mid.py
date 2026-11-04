"""Rationalize discovered quartics and produce exact subdivided witnesses."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from mid_math import targets,loss_gates,bernstein_forward

def certify(p,a=F(0),b=F(1),depth=0):
    beta=bernstein_forward(p,a,b)
    if min(beta)>=0:return {'bernstein':[str(x)for x in beta]}
    if depth>=24:raise ValueError(('subdivision failed',str(a),str(b)))
    m=(a+b)/2
    return {'split':[certify(p,a,m,depth+1),certify(p,m,b,depth+1)]}

def main():
    src=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
    discovered=json.loads(src.read_text());rows=[]
    assert len(discovered['results'])==200
    for i,r in enumerate(discovered['results']):
        a,b=F(i-100,200),F(i-99,200)
        q=[F(round(x*10**8),10**8)for x in r['q']]
        q[0]+=F(1,10000)
        assert q[4]>=0 and min(loss_gates(q,a))>0,(i,loss_gates(q,a))
        rows.append({'index':i,'phase':[str(a),str(b)],'q':[str(x)for x in q],
                     'proofs':[certify(p)for p in targets(q,b)]})
    obj={'schema':'JOINT_STAIRCASE_MID47_V1','rows':rows}
    (out/'proof_objects.json').write_text(json.dumps(obj,indent=2)+'\n')
    print(json.dumps({'status':'CONSTRUCTED_NOT_ACCEPTED','rows':len(rows),
      'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
      'proof_sha256':hashlib.sha256((out/'proof_objects.json').read_bytes()).hexdigest()}))
if __name__=='__main__':main()
