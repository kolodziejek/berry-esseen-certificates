"""Disposable corrupt objects and independent finite-law/pathwise controls."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import comb
import copy,json,shutil,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
import model
from accept import accept_object
from model import need,sha,unique
HERE=Path(__file__).resolve().parent

def convolution(a,b):
    out={}
    for x,p in a.items():
        for y,q in b.items():out[x+y]=out.get(x+y,F(0))+p*q
    return out

def law_power(law,n):
    out={F(0):F(1)}
    for _ in range(n):out=convolution(out,law)
    return out

def structural_controls():
    records=[];paths=0;atoms=0
    for label,A,h,deterministic in [('zero',F(1,3),F(0),True),('small',F(1,3),F(1,100),False),
                                  ('tiny_atom',F(2,5),F(1,10**6),False),('one_deterministic',F(1,3),F(1,1000),True)]:
        u0={-A:h/(A+h),h:A/(A+h)} if h else {F(0):F(1)}
        u1={-h:A/(A+h),A:h/(A+h)} if h and not deterministic else {F(0):F(1)}
        need(sum(x*p for x,p in u0.items())==sum(x*p for x,p in u1.items())==0,'actual conditional centering')
        gap=1-2*h
        for p in (F(2,5),F(9,25)):
            n=3;k=1
            pi=[F(comb(n,j))*p**j*(1-p)**(n-j)for j in range(n+1)]
            R0=max(pi[j]/pi[k]for j in range(k+1,n+1))
            own=convolution(law_power(u1,k),law_power(u0,n-k))
            t=sum(w*w*mass for w,mass in own.items())
            m4=sum(w**4*mass for w,mass in own.items())
            need(m4<=A*A*t+3*t*t,'independent exact own-law fourth moment')
            # Direct iid convolution checks the whole count decomposition.
            marginal={}
            for w,mass in u0.items():marginal[w]=marginal.get(w,F(0))+(1-p)*mass
            for w,mass in u1.items():marginal[1+w]=marginal.get(1+w,F(0))+p*mass
            actual_sum=law_power(marginal,n)
            counts=[convolution(law_power(u1,j),law_power(u0,n-j))for j in range(n+1)]
            phases=sorted(set([F(-1,2),F(-1,10),F(0),F(1,10),F(1,2)]+[w for w in own if abs(w)<=F(1,2)]))
            for u in phases:
                actual=sum(mass for w,mass in actual_sum.items()if w<=k+u)
                conditioned=sum(pi[j]*sum(mass for w,mass in counts[j].items()if j+w<=k+u)for j in range(n+1))
                need(actual==conditioned,'full same-marginal closed CDF identity')
                Q=actual-sum(pi[:k+1])
                upper=-sum(mass for w,mass in own.items()if w>u)+R0*m4/(gap-u)**4
                need(Q/pi[k]<=upper,'joint fourth-moment expectation bound')
                atoms+=int(u in own)
            supports0=tuple(u0);supports1=tuple(u1)
            for arr0 in product(supports0,repeat=n):
                for arr1 in product(supports1,repeat=n):
                    ws=[sum(arr1[:j],F(0))+sum(arr0[j:],F(0))for j in range(n+1)]
                    for u in phases:
                        last=max([j for j in range(n+1)if j+ws[j]<=k+u]or[-1])
                        G=(sum(pi[:last+1])-sum(pi[:k+1]))/pi[k]
                        bound=-int(ws[k]>u)+R0*ws[k]**4/(gap-u)**4
                        need(G<=bound,'pathwise joint-count bound at both phase signs and atoms')
                        paths+=1
            records.append({'law':label,'p':str(p),'variance':str(t),'phase_count':len(phases),'deterministic_component':len(u1)==1})
    return {'actual_laws':records,'pathwise_checks':paths,'exact_own_threshold_atoms':atoms,
            'scope':'structural finite-law controls, not acquired maximizers or a substitute for the continuous proof'}

def main():
    out=Path(sys.argv[1]);out.mkdir()
    original=json.loads((HERE/'proof_objects.json').read_text(),object_pairs_hook=unique)
    accept_object(original);rejections=[]
    def rejected(name,obj):
        path=out/(name+'.json');path.write_text(json.dumps(obj,sort_keys=True)+'\n')
        try:accept_object(obj)
        except (ValueError,TypeError,KeyError,IndexError,ZeroDivisionError) as exc:
            rejections.append({'case':name,'reason':str(exc),'sha256':sha(path)})
        else:raise RuntimeError('corruption accepted: '+name)
    for name,change in [('missing_case',lambda x:x['cases'].pop()),('duplicate_case',lambda x:x['cases'].append(copy.deepcopy(x['cases'][0]))),
                        ('reordered_case',lambda x:x['cases'].reverse()),('changed_target',lambda x:x.update(comparison='rho_B(C-C_B)<0')),
                        ('changed_loss',lambda x:x.update(loss_per_own_variance='1/100')),('extra_claim',lambda x:x.update(all_laws=True))]:
        x=copy.deepcopy(original);change(x);rejected(name,x)
    for i in range(4):
        for name,change in [('negative',lambda v:'-1'),('false_positive',lambda v:str(F(v)+1)),('noncanonical',lambda v:'0/2'),('float',lambda v:0.0)]:
            x=copy.deepcopy(original);x['cases'][i]['tree']['coefficients'][0][0]=change(x['cases'][i]['tree']['coefficients'][0][0]);rejected(f'{name}_{i}',x)
        x=copy.deepcopy(original);x['cases'][i]['tree']['coefficients'].pop();rejected(f'missing_coefficient_row_{i}',x)
        x=copy.deepcopy(original);x['cases'][i]['tree']['coefficients'][0].pop();rejected(f'missing_coefficient_{i}',x)
    x=copy.deepcopy(original);x['cases'][0]['tree']['axis']=0;rejected('unlicensed_tree_schema',x)
    # Alter input evidence only in distinct disposable copies.
    source_rejections=[]
    for name,change in [('source_substitution',None),('changed_phase',lambda x:x['rows'][0]['scope'].update(phase=['0','1/2'])),
                        ('changed_row',lambda x:x['rows'][1]['unchanged_row'].update(d0='0'))]:
        trial=out/name;trial.mkdir();shutil.copytree(HERE/'native',trial/'native')
        data=json.loads((HERE/'SELECTED_INPUTS.json').read_text())
        if change:change(data)
        else:
            with (trial/'native/tiny47wide_normalization.py').open('a')as f:f.write('\n# substituted bytes\n')
        (trial/'SELECTED_INPUTS.json').write_text(json.dumps(data)+'\n')
        saved=model.HERE;model.HERE=trial
        try:
            try:accept_object(original)
            except ValueError as exc:source_rejections.append({'case':name,'reason':str(exc)})
            else:raise RuntimeError('source substitution accepted')
        finally:model.HERE=saved
    duplicate='{"schema":0,"schema":1}'
    try:json.loads(duplicate,object_pairs_hook=unique)
    except ValueError:rejections.append({'case':'duplicate_JSON_key','reason':'duplicate JSON field'})
    else:raise RuntimeError('duplicate JSON accepted')
    result={'status':'PASS_JOINT_COUNT_CORRUPTION_AND_ACTUAL_LAW_CONTROLS','object_rejections':rejections,
            'source_rejections':source_rejections,'structural_controls':structural_controls(),
            'original_object_accepted_after_controls':accept_object(original)['status']}
    (out/'RESULT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'object_rejections':len(rejections),'source_rejections':len(source_rejections),
                      'pathwise_checks':result['structural_controls']['pathwise_checks']}))

if __name__=='__main__':main()
