"""Bounded discovery of a rational closed-box plan, never acceptance."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys,time
p=Path(__file__).with_name('compound-cover-discovery.py');raw=p.read_bytes()
s={'__name__':'box_discovery','__file__':str(p)};exec(compile(raw,str(p),'exec'),s)

def trial(box):
    fb=tuple(map(float,box));tail,y,anchors=s['tails'](fb)
    best=(-1e100,None,None)
    for a in range(45,81):
        margin,witness=s['bound'](fb,a/100,tail)
        if margin>best[0]:best=(margin,a,witness)
    cm=s['cantelli'](fb,tail)
    if cm>best[0]:best=(cm,'cantelli',None)
    return {'box':[str(x) for x in box],'method':best[1],
            'hinge_y':str(F(y,200)),'later_anchors':anchors,
            'diagnostic_margin':best[0],'diagnostic_witness':best[2]}

ls=[F(3,100)+F(3,200)*i for i in range(4)]
rs=[F(1,80)*i for i in range(13)]
ws=[F(i,8) for i in range(9)]
queue=[(ls[i],ls[i+1],rs[j],rs[j+1],ws[k],ws[k+1],0) for i in range(3) for j in range(12) for k in range(8)]
accepted=[];rejected=[];tested=0;beg=time.monotonic()
while queue:
    item=queue.pop(0);box=item[:6];depth=item[6]
    row=trial(box);tested+=1
    if row['diagnostic_margin']>1e-5:
        accepted.append(row)
    elif tested+len(queue)+len(accepted)>=1900 or depth>=4:
        rejected.append(row)
    else:
        # Refine physical allocation first, then noise, then phase.
        axis=[4,0,2,4][depth];lo,hi=box[axis:axis+2];mid=(lo+hi)/2
        left=list(box);right=list(box);left[axis+1]=mid;right[axis]=mid
        queue.extend([(*left,depth+1),(*right,depth+1)])
    if tested%48==0:
        print(json.dumps({'progress_boxes_tested':tested,'remaining':len(queue),'leaves':len(accepted),'failed_leaves':len(rejected),'elapsed_seconds':time.monotonic()-beg}),file=sys.stderr,flush=True)
print(json.dumps({'status':'DISCOVERY_PLAN_ONLY','helper_sha256':hashlib.sha256(raw).hexdigest(),'tested_boxes':tested,'accepted_diagnostic_leaves':len(accepted),'failed_leaves':len(rejected),'rows':accepted,'failures':rejected,'elapsed_seconds':time.monotonic()-beg},indent=2))
