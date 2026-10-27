from fractions import Fraction as F
from pathlib import Path
import json, re, subprocess
SOURCE = Path('manuscript/arxiv-v1/appendices/fourier-analysis.tex')
old = subprocess.check_output(['git','show','6299d97:'+str(SOURCE)], text=True)
new = SOURCE.read_text()
labels = lambda s: re.findall(r'\\label\{([^}]+)\}',s)
a,b=labels(old),labels(new)
assert set(a) <= set(b)
assert len(b)==len(set(b))
assert new.count('\\section{')==1
assert 'ms:fourier:appendix' in b
assert '\\begin{verbatim}' not in new
assert 'Assume the finite Bernstein positivity condition specified in the proof' in new
assert r'\min_{0\le r\le80,\ 0\le k\le13}B_{r,k}' in new

def norm(s):
    s=re.sub(r'\\mathbb E(?=[A-Za-z])',r'\\E ',s)
    s=s.replace(r'\mathbb E',r'\E').replace(r'\mathbb P',r'\Pp').replace(r'\Pr',r'\Pp')
    s=re.sub(r'(?<![A-Za-z\\])EX',r'\\E X',s)
    s=re.sub(r'(?<![A-Za-z\\])E(?=\[)',r'\\E',s)
    s=s.replace('$E(X|X|',r'$\E(X|X|').replace("P(XX'<0)",r"\Pp(XX'<0)")
    s=re.sub(r'\bLOW\b','low-frequency',s)
    s=re.sub(r'\bHIGH\b','high-frequency',s)
    return re.sub(r'\s+','',s)

def proof(s,label):
    start=s.index('\\begin{proof}',s.index('\\label{'+label+'}'))
    return s[start:s.index('\\end{proof}',start)+len('\\end{proof}')]
protected=[
'ms:fourier:afcore:lem:anchor','ms:fourier:afcore:lem:sine-circle',
'ms:fourier:afcore:lem:modulus','ms:fourier:afcore:lem:rectangle',
'ms:fourier:rescore:fourier-early-low','ms:fourier:rescore:entry189-mills',
'ms:fourier:rescore:lem:finite-low','ms:fourier:rescore:entry201-event',
'ms:fourier:rescore:u-asymmetric','ms:fourier:rescore:u-product',
'ms:fourier:rescore:u-phase-interface','ms:fourier:cut49:shortloc:quartic',
'ms:fourier:cut49:shortloc:tails']
for label in protected:
    assert norm(proof(old,label))==norm(proof(new,label)),label
# Fine directed pi endpoints are analytic consequences of Machin and
# alternating remainders; only the rational comparisons are executed here.
A=lambda m,k:sum((F((-1)**j,(2*j+1)*k**(2*j+1)) for j in range(m)),F(0))
coarse=16*A(6,5)-F(4,239)
lo=16*A(32,5)-4*(A(10,239)+F(1,21*239**21))
hi=16*(A(32,5)+F(1,65*5**65))-4*A(10,239)
assert coarse>F(333,106)
assert F(3141592653589793,10**15)<lo<hi<F(3141592653589794,10**15)
# Negative controls for the guards, without modifying any manuscript file.
assert not set(a)<=set(labels(new.replace('\\label{'+a[0]+'}','',1)))
assert len(labels(new+'\\label{'+b[0]+'}'))!=len(set(labels(new+'\\label{'+b[0]+'}')))
assert not hi<F(3141592653589793,10**15)
assert norm(proof(new,protected[4]).replace('251','252',1))!=norm(proof(old,protected[4]))
print(json.dumps({'status':'PASS_EDITORIAL_PRESERVATION_AND_DIRECTED_PI',
 'old_labels':len(a),'new_labels':len(b),'protected_proofs':protected,
 'pi_comparisons':'333/106 < coarse lower; directed 15-place endpoints enclose high-precision interval',
 'negative_controls':['missing old label','duplicate label','wrong directed upper endpoint','mutated Gaussian-transfer coefficient'],
 'limits':'No cosine Bernstein coefficients or native proof objects executed; no whole analytic chain acceptance.'},indent=2))
