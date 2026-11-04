"""Propose finite-row eta witnesses; does not change any original score target."""
from pathlib import Path
from fractions import Fraction as F
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from finite_native import rows
from finite_targets import parameterized_targets,scalar_gate
from polynomials import bernstein
from model import CASE_IDS,need

def main():
    out=Path(sys.argv[1]);need(not out.exists(),'create-only finite candidate');objects=[]
    for row in rows():
        c=row['c'];chosen=None
        for eta in (F(1,10),F(1,20),F(0),F(-1,20),F(-1,10)):
            if scalar_gate(c,eta,row['gate_kind'])<=0:continue
            p=parameterized_targets(c,eta);coeff={name:bernstein(p[name],(F(0),F(1),F(0),F(1)))for name in CASE_IDS}
            if min(v for a in coeff.values()for b in a for v in b)<0:continue
            chosen={'family':row['family'],'index':row['index'],'eta':str(eta),
                    'cases':[{'id':name,'coefficients':[[str(v)for v in a]for a in coeff[name]]}for name in CASE_IDS]};break
        need(chosen is not None,'finite row has no proposed witness '+row['family']+'/'+str(row['index']))
        objects.append(chosen)
    obj={'schema':'FINITE267_JOINT_COUNT_TINY_V1','score_targets':'unchanged native sharp, positive39 and finite-binomial-reserve targets','rows':objects}
    out.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PROPOSED_FINITE267_NOT_YET_ACCEPTED','rows':len(objects),'bytes':out.stat().st_size,
                      'eta_counts':{eta:sum(r['eta']==eta for r in objects)for eta in sorted(set(r['eta']for r in objects))}}))

if __name__=='__main__':main()
