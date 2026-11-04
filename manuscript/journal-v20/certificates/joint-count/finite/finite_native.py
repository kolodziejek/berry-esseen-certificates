"""Fresh original finite normalization, preserving every score and allowance premise."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,sys
from model import need,sha,unique
HERE=Path(__file__).resolve().parent
MANIFEST_PIN='59681199b6341107bf24b9be7c258e4ef96c1a23a1c45e52399f7019636b21fc'
PROJECTION_PIN='c648ff9f317844c0eb2792cb8ef5781fc65bddcced1abd55659b62977650324d'
FAMILIES=('positive39','central40','left40_42','left42_48','central42_48')
SPECS={'positive39':(78,39,39,F('.302'),'positive_allowance'),
       'central40':(48,40,42,F('.38'),'sharp'),
       'left40_42':(49,40,42,F('.282'),'binomial_reserve'),
       'left42_48':(45,42,48,F('.29'),'sharp'),
       'central42_48':(47,42,48,F('.38'),'sharp')}

def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def pinned_inputs():
    need(sha(HERE/'FINITE_NATIVE_SOURCES.json')==MANIFEST_PIN,'fixed complete finite native source manifest')
    manifest=json.loads((HERE/'FINITE_NATIVE_SOURCES.json').read_text(),object_pairs_hook=unique)
    for record in manifest['files']:need(sha(HERE/record['path'])==record['sha256'],'fixed finite native source bytes')
    need(sha(HERE/'FINITE_INPUTS.json')==PROJECTION_PIN,'fixed historical contract projection identity')
    projections={}
    for record in json.loads((HERE/'FINITE_INPUTS.json').read_text())['files']:
        need(sha(HERE/record['path'])==record['sha256'],'preserved finite projection source')
        if 'family'in record:projections[record['family']]=json.loads((HERE/record['path']).read_text())['rows']
    return manifest,projections

def rows():
    manifest,old=pinned_inputs();result=[]
    for family in FAMILIES:
        count,N,last,start,gate=SPECS[family];folder=HERE/'finite_native_sources'/family
        filename='targets39_candidate.json'if family=='positive39'else'new_central42_targets.json'if family=='central42_48'else'targets.json'
        table=json.loads((folder/filename).read_text(),object_pairs_hook=unique)
        need(len(table['rows'])==count,'complete fixed finite row count')
        if family!='left42_48':need(type(table['N'])is int and table['N']==N,'exact finite index floor')
        if family=='positive39':need(F(table['K'])==F(741,4000)and F(table['Ccap'])==F(2113,5000),'unchanged positive39 excess and score ceiling')
        normname='normalization_piecewise42_v2.py'if family=='left42_48'else'tiny42_normalization.py'if family=='central42_48'else'normalization.py'
        norm=load_module(folder/normname,'finite_normalization_'+family)
        signed=None
        if family in ('positive39','central40','left40_42'):
            prior=sys.modules.get('normalization');sys.modules['normalization']=norm
            try:signed=load_module(folder/'signed_normalization.py','finite_signed_'+family)
            finally:
                if prior is None:del sys.modules['normalization']
                else:sys.modules['normalization']=prior
        for i,row in enumerate(table['rows']):
            need(type(row['index'])is int and row['index']==i,'ordered finite native index')
            need(list(map(F,row['p']))==[start+F(i,500),start+F(i+1,500)],'complete closed finite probability cell')
            actual_noise=min(F('.05'),F(row['lambda_max']));need(actual_noise>0,'positive actual finite noise scope')
            H=F(row['H'])if family=='left42_48'else max(F(row['H_minus']),F(row['H_plus']))
            amplitude=F('.44')if family=='positive39'else F('.43')if family=='central40'else max(F('.435'),F(row['amplitude']))if family=='left40_42'else F('.425')
            base=dict(N=N,pl=F(row['p'][0]),pu=F(row['p'][1]),theta=F(row['theta']),H=H,d0=F(row['d0']),amplitude=amplitude,maxnoise=F('.05')if family=='positive39'else actual_noise)
            if family!='central42_48':base['Ccap']=F('.4226')if family in('positive39','left42_48')else F('.4247')
            if signed:c,g=signed.generate(base,F(row['H_plus']))
            else:c=norm._generate(base);g=norm.normalization_gates(base,c)
            need(all(F(v)>0 for v in g.values()),'all original finite normalization gates')
            if family=='positive39':c['barrier_allowance']=F(741,4000)/(39*max(F('.05'),F(row['lambda_max'])))
            if family=='left40_42':
                eps=[];index=int(base['pl']*500)
                for n in (40,41,42):
                    bins=json.loads((folder/f'binomial{n}.json').read_text())
                    need(type(bins['n'])is int and bins['n']==n,'retained finite binomial index')
                    matching=[r for r in bins['rows']if r['index']==index]
                    need(len(matching)==1 and list(map(F,matching[0]['p']))==list(map(F,row['p'])),'same finite binomial probability row')
                    eps.append(F(matching[0]['epsilon']))
                c['epsilon']=min(eps);need(c['epsilon']>0,'positive inherited binomial reserve')
                vmax=base['pu']*(1-base['pu']);c['rhoB_lower']=(1-2*vmax)/norm.rootup(vmax)
            if family in old:
                historical={k:F(v)for k,v in old[family][i]['contract'].items()}
                need(c==historical,'entire freshly regenerated contract equals selected original contract')
                need(all(F(old[family][i]['historical_gates'][k])==F(v)for k,v in g.items()),'original native gate values unchanged')
            result.append({'family':family,'index':i,'c':c,'normalization_gates':g,'gate_kind':gate,
                           'premises':{'n':[N,last],'p':row['p'],'Cmin':'2/5','Ccap':str(base.get('Ccap','not required by this repair')),
                                       'H':[-H,H]if family=='left42_48'else[-F(row['H_minus']),F(row['H_plus'])],
                                       'theta':base['theta'],'inward_d':base['d0'],'amplitude':amplitude,
                                       'positive_noise':['0',str(actual_noise)],'phase':['-1/2','1/2'],
                                       'same_law':'actual iid conditional centering/support; inherited acquired row interface',
                                       'positive_excess_K':str(F(741,4000))if family=='positive39'else None}})
    need(len(result)==267,'fixed267finitecensus')
    return result
