"""Exact scalar gates for large-index.tex; not an analytic proof or grid."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize: raise RuntimeError('Assertions required')
gates={}
def gate(name,lhs,rhs,strict=True):
    lhs,rhs=F(lhs),F(rhs)
    assert lhs<rhs if strict else lhs<=rhs, name
    gates[name]={'lhs':str(lhs),'rhs':str(rhs),'strict':strict}
N=6000;lo=F(3,40);hi=F(9,25);v=F(6,25);d=F(9,125)
gate('variance root',F(1,4)+hi/N,F(501,1000)**2)
gate('raw displacement',F(46,25)*F(501,1000),F(47,50))
gate('curvature displacement',F(46,25)*F(501,1000)-F(47,100),F(23,50))
gate('mesh interior lower',3,F(2,5)*N-F(47,50))
gate('mesh interior upper',F(53,100)*N+F(47,50),N-3)
gate('window interior',12,F(2,5)*N)
transport=2*(3+F(9,10)*(F(60,49)+F(125,116)**2+F(125,116)))
gate('selected transport',transport,13)
gate('sqrt three lower',F(17,10)**2,3)
gate('cosine first interval',3,2*F(51,40)**2)
gate('cosine second interval',3*F(84,125)**2,2*(F(17,20)-F(44,2625))**2)
gate('age cap',F(3,10),F(41,125))
gate('phase Lipschitz constant',F(3,10)*F(22,7),1)
gate('fixed count variance factor',F(37,42),1-F(5,N))
gate('CF loss per noise',F(1,5),F(3,20)*3*F(37,42)/(1+3*F(37,42)*hi))
tail=F(153,20)*(F(5,42)**4+F(5,42)**3/3+F(5,52)**4+F(5,52)**3/3)
gate('full fourth moment tail',tail,F(1,100))
for z in [F(199,500),F(133,250)]:gate('window variance '+str(z),F(23,100),z*(1-z))
gate('normal density lower',2*F(22,7)*F(199,500)**2,1)
gate('Stirling exponent',(72+F(1,12))/(N*F(23,100)),F(53,1000))
gate('window mass',F(3,4),F(199,250)*(1-F(53,1000)))
gate('positive window loss',0,F(19,100)*lo-F(39,N))
# On [.399,.531], concavity bounds z(1-z) below by its endpoint minimum;
# |1-2z| is bounded by .202. These imply both derivative bounds.
zmin=min(z*(1-z) for z in [F(399,1000),F(531,1000)])
gate('log variance derivative',F(202,1000)/zmin,1)
gate('entropy third derivative',F(202,1000)/zmin**2,4)
gate('upper mass remainder',1+F(1,12)+F(16,3*N),F(11,10))
gate('phase bracket',F(37,20)+F(72,25)/(2*v),8)
gate('density upper squared',F(2,5)**2,F(41,50)**2*v)
# A'(u)=22/25+(53/25)u-2u^2 >=22/25 on [0,1].
gate('integrated phase derivative',2,F(53,25))
assert F(47,50)+F(1,3)==F(191,150)
gate('integrated phase',F(41,50)*F(750,749)*(F(37,20)+F(191,72)),F(15,4))
gate('variance anchor squared',(F(2,5)*F(47,50)*hi/2)**2,v**3)
gate('complete phase correction',F(15,4)+1,5)
gate('cubic correction',0,F(87,250)-F(13,16)*hi/N)
gate('sqrt index',77**2,N)
gate('sqrt minimum noise',F(27,100)**2,lo)
margin=F(57,400)-F(137,4*N)/lo-F(25,24*77)-F(23,24*77)/F(27,100)
gate('final relative margin',F(1,200),margin)
# Acquisition join: sqrt(v+s)<.501; s/v <=1/4000.
gate('acquisition variance ratio',F(501,1000)*(1+hi/(N*v)),F(251,500))
gate('acquisition inward displacement',F(129,4)*F(251,500)/(6*(1-d)),3)
gate('coarse budget',F('32.20665378'),F(129,4))
gate('first noise coefficient',0,18*F(2,5)-11*d)
gate('second noise coefficient',0,12*F(47,100)-9*d)
# Disposable negative controls: these alleged strengthenings must reject.
negative={
 'unit weighted loss': F(3,4)>1,
 'zero selected transport cost': transport<0,
 'cutoff 100 with same estimates': F(57,400)-F(137,400)/lo-F(25,24*10)-F(23,24*10)/F(27,100)>F(1,200),
 'margin doubled without proof': margin>F(1,100),
}
assert not any(negative.values())
source=Path(__file__).with_name('large-index.tex')
print(json.dumps({'status':'PASS_EXACT_SCALAR_GATES','gates':gates,'gate_count':len(gates),
 'negative_controls_rejected':list(negative),'margin_after_target':str(margin-F(1,200)),
 'proof_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'scope':'Finite scalar gates supporting the written all-law proof; no grid, convolution coverage or acquisition proof is asserted.'},indent=2))
