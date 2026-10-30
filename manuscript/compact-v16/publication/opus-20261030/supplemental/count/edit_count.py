from pathlib import Path
import re
root=Path('/Users/bkolodziejek/Downloads/BE_Codex_Handoff/work/manuscript_revision_20261029')
p=root/'manuscript/compact-v16/sections/08-direct-comparison.tex'
r=Path(__file__).resolve().parent
old=p.read_text();(r/'before.tex').write_text(old);t=old

def change(a,b):
 global t
 assert a in t,a[:90]
 t=t.replace(a,b,1)

change('''The proof below uses only the displayed hypotheses. Contact and the sharp
predecessor are needed earlier to acquire this strip, not for its local
comparison. The small- and larger-noise intervals meet at $\\lambda=1/100$.
For small noise, we keep every error proportional to $\\lambda$ and use
the loss from one count. For larger noise, five neighboring counts give a
uniform crossing loss. That second estimate has an error of order $1/n$
which does not vanish at $\\lambda=0$, so it cannot cover arbitrarily small
positive noise. At zero noise the law is exactly Bernoulli.''',r'''To prove the theorem, condition on $K=\sum_{i=1}^nB_i$, which has law
$\operatorname{Bin}(n,p)$. Given $K=j$, the count-unit noise $W_j$ is the
sum of $j$ independent copies of $U_1$ and $n-j$ independent copies of
$U_0$. The threshold in these units is
\[
 t=np+H\sqrt{v+s},\qquad
 \left\{\sum X_i\le H\right\}=\{K+W_K\le t\}.
\]
We compare this probability with the binomial CDF and then account for
the changes in the normal term and the third absolute moment.
A count below $t$ can leave the event, while a count above $t$ can enter.
The aim is to show that the loss and the favorable corrections exceed
the total gain from all counts above the threshold.

For $0<\lambda\le1/100$, the argument keeps both the loss and every
error proportional to $\lambda$. It uses the count nearest the threshold
and a fourth-moment bound for all entering counts. For
$1/100\le\lambda\le7/20$, a finite summation identity separates the
crossing loss from errors in interpolating the binomial CDF. A periodic
sine function then gives a loss from five counts that is uniform in the
phase $t-\lfloor t\rfloor$. Its interpolation error has an upper bound
of order $1/n$ that does not vanish with $\lambda$, which explains the
separate small-noise argument. The two ranges share their endpoint.
At $\lambda=0$ the law is exactly Bernoulli. These comparisons use the
explicit hypotheses of this theorem; the preceding sections obtain
those hypotheses for a maximizer.''')

# Local notation repairs: probability masses, ratio bound, normal increment.
t=re.sub(r'\\pi_(?=[ijk01]|\{)',lambda m:'b_',t)
t=t.replace('RT_{\\rm in}',r'r_{\max}T_{\rm in}')
t=t.replace(r'\le R$',r'\le r_{\max}$').replace(r' R\text{ upper bound}',r' r_{\max}\text{ upper bound}').replace('$R<','$r_{\\max}<')
small,large=t.split(r'\subsection{Larger noise: five counts and two endpoint checks}',1)
small=small.replace("f'(z)","g_k'(z)").replace(" f'\\text",r" g_k'\text").replace('f(u)',r'g_k(u)')
# Small-noise threshold L is a local noise limit, not conservation leakage.
small=small.replace(r'\lambda\le L=1/100',r'\lambda\le\lambda_s=1/100').replace('3L',r'3\lambda_s').replace('(43/100)L',r'(43/100)\lambda_s')
# Self-contained count floor and separated call, kernel, bump notation.
large=re.sub(r'\bN\b','n_0',large)
large=large.replace(r'L_j',r'\mathcal L_j').replace(r'L_{i-1}',r'\mathcal L_{i-1}').replace(r'L_i',r'\mathcal L_i').replace(r'L_0',r'\mathcal L_0').replace(r'L_n',r'\mathcal L_n')
large=large.replace(r'B_j',r'\mathcal B_j')
large=large.replace('h(x)',r'\chi(x)').replace('h(t-i+1-V_i)',r'\chi(t-i+1-V_i)').replace('g_i',r'\chi_i')
large=large.replace('f(',r'\psi(').replace('f_',r'\psi_')
large=large.replace('$f$',r'$\psi$').replace('$f\\le',r'$\psi\le')
large=large.replace(r'c_-=6',r'c_\tau=6').replace(r'c_-r',r'c_\tau r')
large=large.replace(r'\tau^2',r'\sigma_V^4').replace(r'\tau',r'\sigma_V^2')
# The preceding replacement also transforms the suffix on c_tau; restore its name.
large=large.replace(r'c_\sigma_V^2',r'c_{\rm var}')
large=large.replace(r'Writing $\alpha=1-6/n_0$, $b=1+3/n_0$ and $z=\kappa\alpha$, we obtain',r'Writing $b=1+3/n_0$ and $\kappa_0=\kappa(1-6/n_0)$, we obtain')
large=large.replace(r'z\lambda',r'\kappa_0\lambda').replace(r'z^2',r'\kappa_0^2').replace(r'z^3',r'\kappa_0^3').replace(r'z^4',r'\kappa_0^4')
# W and P denote quantities distinct from noise W_j and the underlying law P.
large=large.replace(r'W(\lambda)',r'\mathcal W(\lambda)').replace(r"W''(\lambda)",r"\mathcal W''(\lambda)").replace(r'P(\lambda)',r'\Pi(\lambda)').replace('Thus $P$','Thus $\\Pi$').replace('$P>0$','$\\Pi>0$').replace(' P(1/100)',r' \Pi(1/100)').replace(' P(7/20)',r' \Pi(7/20)')
t=small+r'\subsection{Larger noise: five counts and two endpoint checks}'+large

change('''Outgoing events are strict and incoming events closed; this convention
includes all threshold atoms.''',r'''The event is closed: count $k-i$ is lost when $W_{k-i}>u+i$,
whereas count $k+i$ enters when $W_{k+i}\le u-i$. Thus an atom at the
threshold remains in the event in both sums.''')

change(r'''\paragraph{The own-count loss at the central phases.}
Set $\alpha=1/2$''',r'''\paragraph{The loss at the threshold count.}
The variance of the count-unit noise already predicts the scale of this
loss. For any centered $W$ with $t=\E W^2>0$, Cauchy--Schwarz and
H\"older give
\[
 \Pp(W>0)\ge\frac{(\E|W|)^2}{4t}
             \ge\frac{t^2}{4\E W^4}.
\]
Indeed $\E W_+=\E|W|/2$ and
$t\le(\E|W|)^{2/3}(\E W^4)^{1/3}$.
For $W=W_k$, the fourth-moment bound below makes this at least
$t_0/[4(A^2+3t_0)]> (16/25)t_0$ on $t_0\le T_*$.
This zero-threshold estimate explains why a loss proportional to the
variance is possible. We use a quartic minorant to obtain a bound that
also pays for moving the threshold and for the normal increment.

\begin{lemma}[Loss at a nearby count threshold]
\label{short:count:central-loss-lemma}
Under the small-noise hypotheses and for $|u|\le b_*$,
\begin{equation}\label{short:count:small-own}
 O>\frac35t_0>.59\lambda.
\end{equation}
\end{lemma}
\begin{proof}
We first use a moment minorant when $|u|\le3t_0/2$, then a one-sided
variance bound for the remaining phases. Set $\alpha=1/2$''')
change(r'''Thus
\begin{equation}\label{short:count:small-own}
 O>\frac35t_0>.59\lambda\qquad(|u|\le b_*).
\end{equation}
The value $u=0$ is included, with $h_\alpha(0)=0$.''',r'''The value $u=0$ is included, with $h_\alpha(0)=0$.
\end{proof}''')
change('''Thus it may be integrated against the conditional sum $W_k$, which need
not be bounded by $3/5$. Only its individual summands have that bound.''','''Thus it may be integrated against the conditional sum $W_k$. Each
summand is bounded by $3/5$, whereas the sum can exceed that bound;
the minorant is valid on the entire real line.''')
change(r'''                 -\frac2{700}>\frac1{100}.''',r'''                 -\frac2{700}=\frac{4787}{140000}>\frac1{100}.''')

# Isolate the two distinct probabilistic claims in the large-noise device.
change(r'''It is continuously differentiable with derivative Lipschitz constant
$2\pi^2$. We claim
\begin{equation}\label{short:count:kernel}
 \chi(x)\ge\eta \psi(x)\ge0.
\end{equation}
For $x<1-a_1$''',r'''It is continuously differentiable with derivative Lipschitz constant
$2\pi^2$.
\begin{lemma}[A nonnegative crossing kernel]
\label{short:count:kernel-lemma}
For every real $x$,
\begin{equation}\label{short:count:kernel}
 \chi(x)\ge\eta\psi(x)\ge0.
\end{equation}
\end{lemma}
\begin{proof}
For $x<1-a_1$''')
change('''At $x=0,1$ both comparisons are weak, as required for atoms.

Freeze $V=V_{k+1}$''',r'''At $x=0,1$ both comparisons are weak, as required for atoms.
\end{proof}

The useful feature of the sine bump is its phase-uniform average:
\[
 \E\sin^2(\pi(u-V))
 =\frac{1-\Re\{e^{2\pi i u}\E e^{-2\pi iV}\}}2
 \ge\frac{1-|\E e^{2\pi iV}|}{2}.
\]
The characteristic function factorizes for a sum of independent noises.
To use this observation, we compare five neighboring count sums with
one fixed sum, paying for four centered replacements.

\begin{lemma}[Five-count crossing loss]
\label{short:count:five-loss-lemma}
Under the larger-noise hypotheses,
\begin{equation}\label{short:count:reserve}
 \sum_{i=k-1}^{k+3}\chi_i\ge\eta\left\{
 \frac{1-e^{-\kappa(1-6/n)\lambda}}2
 -\frac{A^2(1+3/n)\lambda+3(1+3/n)^2\lambda^2}{16}
 -\frac{4\pi^2\lambda}{nr}\right\}.
\end{equation}
\end{lemma}
\begin{proof}
Fix $V=V_{k+1}$''')
change('''These five indices are interior, because $|i-np|<\\xi+3<4$.
No independence between different count sums is asserted.''',r'''These five indices are interior, because $|i-np|<\xi+3<4$.
The summands within each sum are independent; neighboring count sums
share the unchanged summands in the replacement argument.''')
change(r'''Altogether,
\begin{equation}\label{short:count:reserve}
 \sum_{i=k-1}^{k+3}\chi_i\ge\eta\left\{
 \frac{1-e^{-\kappa(1-6/n)\lambda}}2
 -\frac{A^2(1+3/n)\lambda+3(1+3/n)^2\lambda^2}{16}
 -\frac{4\pi^2\lambda}{nr}\right\}.
\end{equation}''',r'''Combining the replacement cost, the omitted translates, and the
characteristic-function bound proves the displayed inequality.
\end{proof}''')
change('''The three terms in \\eqref{short:count:crossing} are the interpolated
binomial probability, an error from variation in the binomial masses,
and the crossing loss.''',r'''The functions $\mathcal L_j(t)$ are expectations of the convex
positive-part function; their Jensen gaps $\mathcal B_j$ measure how
noise changes those expectations. Thus the three terms in
\eqref{short:count:crossing} are the interpolated binomial probability,
an error from variation in the binomial masses, and the crossing loss.''')

# Make the complete curvature estimate a target before its proof.
start=t.index('Put $c=(np-q-t)_+$.')
eqstart=t.index(r'\begin{equation}\label{short:count:curvature}',start)
eqend=t.index(r'\end{equation}',eqstart)+len(r'\end{equation}')
eq=t[eqstart:eqend]
proofpre=t[start:eqstart].replace('Put $c=(np-q-t)_+$. For $a=t-j$ and $W_j=T_j-j$, centering gives','For $a=t-j$ and $W_j=T_j-j$, centering gives',1)
proofpre=proofpre.replace(' yields\n',' proves the asserted bound.\n')
replacement=r'''\begin{lemma}[Variation of the binomial weights]
\label{short:count:variation-lemma}
Put $c=(np-q-t)_+\le\bar c$. If $T$ and $M_4$ bound respectively
the second and fourth moments of $W_j$ whenever $b_{j+1}>b_j$, then
'''+eq+r'''
\end{lemma}
\begin{proof}
'''+proofpre+r'''
\end{proof}'''
t=t[:start]+replacement+t[eqend:]
# Replace an ambiguous global-sounding final defensive claim by its positive role.
change('''The scalar checks used here involve only rational inequalities and
$199/500<\\phi(0)<2/5$, $25/8<\\pi<22/7$; no parameter grid or tail
truncation is involved.''',r'''The endpoint calculations are rational after using
$199/500<\phi(0)<2/5$ and $25/8<\pi<22/7$.
Concavity supplies the bounds between the endpoints, while
\eqref{short:count:small-tail} and \eqref{short:count:curvature} retain
all entering counts.''')

# Verify original labels and basic environment balance before replacing source.
labels=lambda x:re.findall(r'\\label\{([^}]+)\}',x)
assert set(labels(old))<=set(labels(t))
assert len(labels(t))==len(set(labels(t)))
for env in ['theorem','lemma','proof','equation','align']:
 assert t.count('\\begin{'+env+'}')==t.count('\\end{'+env+'}'),env
p.write_text(t)
print('Original labels',len(labels(old)),'new labels',len(labels(t)))
