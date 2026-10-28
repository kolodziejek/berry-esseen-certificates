from pathlib import Path
import hashlib,json,re,sys,difflib
source=Path(sys.argv[1]).resolve(); new=source.read_text()
assert hashlib.sha256(new.encode()).hexdigest()=='0dda285adb9aaa24277fdc1d74843c20bc6100b2a64a0cd5ae34bb696a68a6ec'
old=new
changes=[]
def replace(a,b):
    global old
    assert old.count(a)==1,(a,old.count(a))
    old=old.replace(a,b);changes.append(a.splitlines()[0])
replace(r'\usepackage{amsmath,amssymb,amsthm,microtype}'+'\n'+r'\usepackage[hidelinks]{hyperref}',r'\usepackage{amsmath,amssymb,amsthm,microtype,hyperref}')
replace(r'\begin{equation}\label{eq:hlow}'+'\n'+r'                         h(x)=\E(x-U_0)_+\ge0.'+'\n'+r'\end{equation}',r'\['+'\n'+r'                         h(x)=\E(x-U_0)_+\ge0.             \tag{3}'+'\n'+r'\]')
replace(r'\begin{align}\label{eq:hhigh}'+'\n'+r' h(x)&=\Pp(D>x)-\E(D-x)_+\notag\\'+'\n'+r'     &\ge(1-A_1-a_1)\Pp(D>x)\ge b\Pp(D>x).'+'\n'+r'\end{align}',r'\begin{align*}'+'\n'+r' h(x)&=\Pp(D>x)-\E(D-x)_+\\'+'\n'+r'     &\ge(1-A_1-a_1)\Pp(D>x)\ge b\Pp(D>x).                \tag{4}'+'\n'+r'\end{align*}')
replace(r'\begin{equation}\label{eq:telescoping}'+'\n'+r' \E h(R_i)=L_{i-1}(t)-L_i(t)-\Pp(T_i\le t).'+'\n'+r'\end{equation}',r'\['+'\n'+r' \E h(R_i)=L_{i-1}(t)-L_i(t)-\Pp(T_i\le t).                \tag{5}'+'\n'+r'\]')
replace(r'and \eqref{eq:hlow} is at least',r'and (3) is at least')
replace(r'Now \eqref{eq:hhigh} applies.',r'Now (4) applies.')
replace(r'Multiply \eqref{eq:telescoping} by',r'Multiply (5) by')
replace(r'\begin{equation}\label{eq:parts}'+'\n'+r' \Pp(Y_1+\cdots+Y_n\le t)'+'\n'+r' =\pi_0+\pi_1t+\sum_{j=1}^{n-1}(\pi_{j+1}-\pi_j)L_j(t)'+'\n'+r'                 -\sum_{i=1}^n\pi_i g_i(t).'+'\n'+r'\end{equation}',r'\['+'\n'+r' \Pp(Y_1+\cdots+Y_n\le t)'+'\n'+r' =\pi_0+\pi_1t+\sum_{j=1}^{n-1}(\pi_{j+1}-\pi_j)L_j(t)'+'\n'+r'                 -\sum_{i=1}^n\pi_i g_i(t).                \tag{7}'+'\n'+r'\]')
replace('preserves the actual iid mixture. Only those conditional marginals are\nneeded; no claim about the original joint law of its count and $K$ is made.', 'preserves the actual iid mixture. It does not impose independence between\n$K$ and the binomial count or substitute an optimized relaxation.')
oldhash=hashlib.sha256(old.encode()).hexdigest()
assert oldhash=='b0f2e15ff41aaeb843b8b8e0619c89cdc15f07a427f71adba4ea7c151dfd0aec',oldhash
stack=[]
for match in re.finditer(r'\\(begin|end)\{([^}]+)\}',new):
    kind,env=match.groups()
    if kind=='begin': stack.append(env)
    else: assert stack.pop()==env,(kind,env)
assert not stack
labels=re.findall(r'\\label\{([^}]+)\}',new)
assert len(labels)==len(set(labels))
refs=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',new)
assert set(refs)<=set(labels)
assert r'\tag{' not in new
run=Path(__file__).resolve().parent
(run/'reviewed-source.tex').write_text(old)
(run/'source-formatting.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='reviewed-b0f2-source.tex',tofile='final-0dda-source.tex')))
print(json.dumps({'result':'PASS','old_sha256':oldhash,'new_sha256':hashlib.sha256(new.encode()).hexdigest(),'exact_reversible_edits':len(changes),'edits':'equation numbering/hyperlink appearance plus one clarified auxiliary-coupling sentence','environment_nesting':'valid','labels_unique':True,'all_references_resolve':True,'mathematical_formulas_or_hypotheses_changed':False},indent=2))
