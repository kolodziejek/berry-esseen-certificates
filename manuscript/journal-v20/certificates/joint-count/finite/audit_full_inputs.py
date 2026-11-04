"""Separate source-bound applicability census for the unchanged common TINY proof."""
from pathlib import Path
from fractions import Fraction as F
import ast,json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from model import HERE,load_native,need,sha,unique,final_margin
from accept import accept_object

def main():
    c,g,_=load_native()
    proof=accept_object(json.loads((HERE/'proof_objects.json').read_text(),object_pairs_hook=unique))
    rows=[]
    fixed=[('left','left270_input47_table.json','left_sperner47_contract.py',38,F('.304'),F('.38')),
           ('central','conditional_input47.json','sperner47_contract.py',45,F('.38'),F('.47'))]
    for side,name,contract,count,start,end in fixed:
        path=HERE/'native'/name;table=json.loads(path.read_text(),object_pairs_hook=unique)
        need(table['N']==47 and len(table['panels'])==count,'fixed entire native row census')
        amps=[ast.literal_eval(node.value)for node in ast.parse((HERE/'native'/contract).read_text()).body
              if isinstance(node,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='AMPLITUDES'for t in node.targets)]
        need(len(amps)==1 and len(amps[0])==count,'fixed amplitude census')
        previous=start
        for i,r in enumerate(table['panels']):
            pl,pu=map(F,r['p']);upper=min(c['lmax'],F(r['lambda_max']));amplitude=F(amps[0][i])
            need(r['index']==i and pl==previous and pl<pu,'closed ordered exact probability cover')
            need(c['pl']<=pl<pu<=c['pu'],'global probability premises')
            need(0<=F(r['theta'])<=c['theta'],'variance fraction premise')
            need(0<=F(r['d0'])<=c['d0']<pl,'inward support premise')
            need(0<=F(r['H_plus'])<=c['H'] and 0<=F(r['H_minus'])<=c['H'],'both signed threshold premises')
            need(0<amplitude<=c['amplitude'],'actual amplitude premise')
            need(0<upper<=c['lmax'],'positive full native TINY noise interval')
            previous=pu
            rows.append({'side':side,'native_index':i,'p':[str(pl),str(pu)],'positive_noise':['0',str(upper)],
                         'noise_lower_endpoint_open':True,'zero_noise':'separate Bernoulli argument',
                         'phase':['-1/2','1/2'],'amplitude':str(amplitude),'theta':r['theta'],'d0':r['d0'],
                         'H':['-'+str(F(r['H_minus'])),str(F(r['H_plus']))],
                         'row_sha256':__import__('hashlib').sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest()})
        need(previous==end,'complete final probability endpoint')
    need(len(rows)==83 and all(F(rows[i]['p'][1])==F(rows[i+1]['p'][0])for i in range(82)),'all83 closed probability union')
    output={'status':'PASS_ALL83_UNIFORM47_TINY_INPUT_APPLICABILITY','mathematical_status':'same-law acquired input premises retained; the common joint-count implication applies to each full TINY row',
            'execution_status':'fresh exact source-bound census, native normalization and common four-polynomial acceptance',
            'analytic_premises_not_inferred_from_rows':['actual iid conditional laws','C>=2/5','conditional centering','acquired support and signed threshold bounds','the inherited acquisition reduction'],
            'source_pins':{name:sha(HERE/'native'/name)for _,name,_,_,_,_ in fixed},
            'normalization_sha256':sha(HERE/'native/tiny47wide_normalization.py'),'object_sha256':sha(HERE/'proof_objects.json'),
            'N':47,'count_scope':'every integer n>=47','probability_union':['38/125','47/100'],'rows':rows,
            'four_polynomials':proof['cases'],'normalization_gates':len(g),'strict_reserve_beyond_original_target':str(final_margin(c)),
            'original_target':'rho_B(C-C_B)<-lambda/1000','no_acquisition_replay':True,'no_MID_or_LOW_replacement':True}
    print(json.dumps(output,indent=2,sort_keys=True))

if __name__=='__main__':main()
