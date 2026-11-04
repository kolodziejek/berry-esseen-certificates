"""Externally fixed two-panel theorem, unchanged native normalizer and four targets."""
from pathlib import Path
from fractions import Fraction as F
import ast,hashlib,importlib.util,json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from polynomials import X,Y,add,scalar,scale,mul,power,encode
HERE=Path(__file__).resolve().parent
CASE_IDS=('negative_quartic','negative_Cantelli','positive_quartic','positive_normal')
ETA=F(1,10)
EXPECTED_TABLES={
 'conditional_input47.json':'b9d2aa15ad96181f5a8eb846e76ae296d2c2c8ed1a5975c6f389c2f7d14ff2b7',
 'left270_input47_table.json':'4b7bb259e469ee57ca6a61d89fd0b3385443508129138899fe597fd82dc9521a',
}
EXPECTED_NATIVE={
 'tiny47wide_normalization.py':'f1e2606359e321d17db11c7240467a597f00094d1747d40ed4f69ceae18d4b71',
 'tiny47wide_kernel.py':'daa468b6b825dbb692c8a1930cc1cf94ffd9bd143c354fe22dde9575752b2626',
 **EXPECTED_TABLES,
 'sperner47_contract.py':'f815e4d0b0124709f4f5922726cd20ef224d115dbd6251de6a633c955c60b8a2',
 'left_sperner47_contract.py':'4444fbd3c361ca76f21fe72f67059a9fbe44a045c45dc3b72d64b4c2813bf19e',
}

def need(ok,message):
    if not ok:raise ValueError(message)

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def unique(pairs):
    d={}
    for k,v in pairs:
        need(k not in d,'duplicate JSON field');d[k]=v
    return d

def load_native():
    need(not sys.flags.optimize,'unoptimized Python')
    selection=json.loads((HERE/'SELECTED_INPUTS.json').read_text(),object_pairs_hook=unique)
    need(len(selection['source_pins'])==6,'complete native source census')
    need({p['copy']:p['sha256']for p in selection['source_pins']}=={'native/'+k:v for k,v in EXPECTED_NATIVE.items()},'externally fixed source identities')
    for name,pin in EXPECTED_NATIVE.items():need(sha(HERE/'native'/name)==pin,'fixed native source identity')
    norm=HERE/'native/tiny47wide_normalization.py'
    spec=importlib.util.spec_from_file_location('joint_count_native_normalization',norm)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    c=m.CFG;g=m.check()
    need(all(F(v)>0 for v in g.values()),'all original normalization gates')
    need(c['N']==47 and c['lmax']==F(1,20),'fixed n/noise target')
    need([r['id']for r in selection['rows']]==['central','left'],'complete selected two-row census')
    for rec,name,index,contract in zip(selection['rows'],EXPECTED_TABLES,(10,28),('sperner47_contract.py','left_sperner47_contract.py')):
        table=json.loads((HERE/'native'/name).read_text(),object_pairs_hook=unique)
        row=table['panels'][index]
        need(rec['input_file']=='native/'+name and rec['input_index']==index and rec['unchanged_row']==row,'exact native selected row')
        need(rec['target']=='rho_B(C-C_B)<-lambda/1000','unchanged target')
        need(rec['scope']=={'N':47,'noise':['0','1/20'],'noise_zero':'separate Bernoulli case','phase':['-1/2','1/2'],'amplitude':'17/40'},'complete fixed continuous scope')
        amplitudes=[ast.literal_eval(node.value)for node in ast.parse((HERE/'native'/contract).read_text()).body
                    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name)and t.id=='AMPLITUDES'for t in node.targets)]
        need(len(amplitudes)==1,'one native amplitude table')
        need(F(amplitudes[0][index])<=c['amplitude'],'conservative actual amplitude')
        need(c['pl']<=F(row['p'][0])<F(row['p'][1])<=c['pu'],'probability normalization')
        need(F(row['theta'])<=c['theta'] and F(row['d0'])<=c['d0'],'inward/variance normalization')
        need(max(F(row['H_minus']),F(row['H_plus']))<=c['H'],'both threshold signs')
        need(F(row['lambda_max'])>=c['lmax'],'entire chosen noise interval acquired')
    return c,g,selection

def targets(c):
    K=F(9)/(4*F('.4641'));a=F('.4784');A=c['amplitude'];gap=1-c['d0']
    den=K*a**4;T=c['ownhi']*c['lmax'];t=scale(X,T)
    need(gap>F(1,2) and 3*gap-F(1,2)>0,'whole staircase domain')
    need(((K-F(9,4))*F(2,3))**2>3 and K>F(9,4),'quartic bound on entire real line')
    need(F(5,3)*T<F(1,2) and F(6,5)*T<F(1,2),'nonempty near/far phase partition')
    output={}
    # The positive right-hand polynomial is O/t minus ETA minus incoming/t,
    # with the strictly positive fourth-power denominator cleared.
    for sign,zmax,name in [(-1,F(5,3),'negative_quartic'),(1,F(6,5),'positive_quartic')]:
        z=scale(Y,zmax);r=mul(t,z)
        base=add(scalar((3*a*a-A*A)/den-ETA),scale(t,-3/den),scale(r,-4*A/den),
                 scale(power(r,2),-6/den),scale(mul(power(t,3),power(z,4)),-1/den),
                 scale(mul(t,power(z,2)),3*a*a/den),
                 scale(z,(-2*sign*a**3)/den+(c['derivative_lo']if sign>0 else -c['derivative_hi'])))
        d=add(scalar(gap),scale(r,-sign))
        output[name]=add(mul(base,power(d,4)),scale(add(scalar(A*A),scale(t,3)),-c['ratio']))
    # Far wedges use r=z0*t+(1/2-z0*t)*v, 0<=v<=1.
    for sign,zmax,name in [(-1,F(5,3),'negative_Cantelli'),(1,F(6,5),'positive_normal')]:
        r=add(scale(t,zmax),mul(add(scalar(F(1,2)),scale(t,-zmax)),Y))
        d=add(scalar(gap),scale(r,-sign));incoming=scale(mul(t,add(scalar(A*A),scale(t,3))),c['ratio'])
        if sign<0:
            vden=add(t,power(r,2))
            numerator=add(power(r,2),scale(mul(add(scale(r,c['derivative_hi']),scale(t,ETA)),vden),-1))
            output[name]=add(mul(numerator,power(d,4)),scale(mul(incoming,vden),-1))
        else:
            numerator=add(scale(r,c['derivative_lo']),scale(t,-ETA))
            output[name]=add(mul(numerator,power(d,4)),scale(incoming,-1))
    need(tuple(output)==('negative_quartic','positive_quartic','negative_Cantelli','positive_normal'),'internal formula census')
    return {name:output[name]for name in CASE_IDS}

def final_margin(c):
    return c['mass']*ETA*c['ownlo']-c['repair']/c['N']-F(1,1000)
