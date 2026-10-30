from pathlib import Path
import re
p=Path('/Users/bkolodziejek/Downloads/BE_Codex_Handoff/work/manuscript_revision_20261029/manuscript/compact-v16')
def edit(file,old,new):
 q=p/file;t=q.read_text();assert old in t,(file,old);q.write_text(t.replace(old,new,1))
f='sections/05-geometry-counts.tex'
edit(f,r''' X=\ell(Y-p),\qquad \E[U\mid B_0]=0.''',r''' X=\ell(Y-p)=\frac{B_0+U-p}{\sqrt{pq+s}},\qquad
 \E[U\mid B_0]=0,\qquad 1=pq\ell^2+\theta,''')
# Introduce s before its occurrence in the displayed normalization.
edit(f,'Set $U=W/\\ell$ and $Y=B_0+U$. Then','Set $U=W/\\ell$, $Y=B_0+U$, and $s=\\E U^2$. Then')
# Rename only math-mode central-gap symbols; protect Bernoulli names.
q=p/f;t=q.read_text()
protect={'B_0':'@@bern@@',r'\rho_B':'@@rhob@@',r'\gamma_B':'@@gammab@@','D_B':'@@db@@',r'\Delta_A':'@@dminus@@',r'\Delta_B':'@@dplus@@',r'\bar A':'@@barminus@@',r'\bar B':'@@barplus@@'}
restore={'@@bern@@':'B_0','@@rhob@@':r'\rho_B','@@gammab@@':r'\gamma_B','@@db@@':'D_B','@@dminus@@':r'\Delta_-','@@dplus@@':r'\Delta_+','@@barminus@@':r'\bar A_-','@@barplus@@':r'\bar A_+'}
def rename(m):
 s=m[0]
 for k,v in protect.items():s=s.replace(k,v)
 s=s.replace('A','A_-').replace('B','A_+')
 for k,v in restore.items():s=s.replace(k,v)
 return s
pat=r'\$[^$]*\$|\\\[[\s\S]*?\\\]|\\begin\{(?:align\*?|equation\*?|gather\*?)\}[\s\S]*?\\end\{(?:align\*?|equation\*?|gather\*?)\}'
t=re.sub(pat,rename,t);q.write_text(t)
edit(f,'In particular the defect separates two losses:',r'''\begin{corollary}[The lattice consequence]\label{opus:lattice-gap}
Let $P\in\mathcal P$ be a lattice law with maximal span $h>0$. Then
\[
 J\ge h,\qquad |\gamma|+3h\le(3+\sqrt{10})\rho.
\]
Equality in the second inequality holds exactly for the law of
Corollary~\ref{ms:zero-defect} and its reflection. If successive support
points are all separated by $h$, then $J=h$.
\end{corollary}
\begin{proof}
The support is a closed subset of a translate of $h\mathbb Z$, so its
points have Lebesgue measure zero and every bounded gap has length
$k_gh$ for an integer $k_g\ge1$. The density $\tau$ vanishes outside
the convex hull of the support. Hence, by nonnegative integration,
\[
 \sum_g\tau_gk_gh=\int_\R\tau(t)\,dt=1,
 \qquad J=\sum_g\tau_gk_g^2h^2\ge h.
\]
These identities also hold for unbounded support: the gaps are
countable and their contributions increase to the full integral.
If all $k_g=1$, the inequality is an equality. Reflection preserves
$\rho$, $J$ and $h$, and changes the sign of $\gamma$. Apply
Lemma~\ref{ms:physical-defect} to the orientation with nonnegative
third moment. Equality forces $D=0$, and the equality law has
$J=h$, so Corollary~\ref{ms:zero-defect} proves both directions.
\end{proof}
For a lattice law, $J$ is therefore a weighted average of support-gap
lengths, with weights $\tau_g|g|$ summing to one. The same functional
is defined for arbitrary support, which is why it can replace the
lattice span in the defect inequality.

In particular the defect separates two losses:''')
edit(f,'''All terms on the right are nonnegative. They measure, respectively,
probability displacement, inward motion of the two gap endpoints, and
conditional variance at its actual support locations.''',r'''All terms on the right are nonnegative. In order, they charge
$p\ne p_*$, inward motion of the gap endpoints away from their conditional
means, and the spread within each sign class. The last two expectations
retain the actual locations of the conditional fluctuations.''')
f='sections/03-conservation.tex'
edit(f,'''The equality case in Section~\ref{ms:geometry-counts} identifies the
extremal Bernoulli law. We now connect this geometry to the excess:
contact gives an identity in which $D$ appears with a positive
coefficient. Bounding its remainder will then bound the distance from
that equality case.''',r'''The equality case in Section~\ref{ms:geometry-counts} identifies the
extremal Bernoulli law. To connect that geometry to the excess, we
integrate the nonnegative contact difference $\Delta=Q-h$ against the
zero-bias density. This integral has two useful descriptions. Since
$\Delta$ vanishes on the support, integration over the gaps produces
$J$ and a nonnegative leakage term. The identity
$\int\tau g'=\E[Xg(X)]$ gives a second description in terms of
moments and the sum distribution. Equating them yields conservation.
The coefficient $\CE=(3+\sqrt{10})\phi(0)/6$ then combines the
third-moment penalty with the gap term into the nonnegative defect $D$.''')
edit(f,'''Here $\tau_{u,v}$ is the constant interior value; $J$ and $\tau$ agree
with the definitions in Section~\ref{ms:geometry-counts}. The leakage
$L$ is nonnegative.''',r'''Here $\tau_{u,v}$ is the constant interior value; $J$ and $\tau$ agree
with the definitions in Section~\ref{ms:geometry-counts}. The leakage
$L$ is a weighted contribution of the law of $H-S_{n-1}$ inside support
gaps, and is nonnegative because its measure and integrand are
nonnegative. This sign needs no estimate for $C_{n-1}$.''')
edit(f,'''In \eqref{v9:core:positive}, the four terms retain the excess, the loss
from a nonzero normal threshold, the departure from the zero-defect law,
and the nonnegative leakage of the reflected predecessor sum through
support gaps. When $a\ge0$, all four are nonnegative. The proof must
therefore bound $\mathcal R_c$ from above without assuming that the
excess is already negative. The coefficient of the unnormalized excess
is $n+H^2$.''',r'''The terms in \eqref{v9:core:positive} have separate roles:
\begin{center}\small
\begin{tabular}{@{}p{.40\linewidth}p{.54\linewidth}@{}}
\toprule
Term & Role \\
\midrule
$(n+H^2)a$ & The excess, weighted by $n+H^2$. \\
$nc\rho(1-e)$ & The loss from moving the normal threshold away from zero. \\
$n\phi(0)eD/6$ & The moment and gap defect from Section~\ref{ms:geometry-counts}. \\
$n^{3/2}L$ & A weighted contribution inside the support gaps. \\
$\mathcal R_c$ & The moment, threshold and Fourier terms to be bounded. \\
\bottomrule
\end{tabular}
\end{center}
The four terms on the right are nonnegative when $a\ge0$. Solving for
the excess makes the role of the remainder explicit:
\begin{equation}\label{opus:excess-identity}
 a=\frac{\mathcal R_c-n\CE\rho(1-e)-n\phi(0)eD/6-n^{3/2}L}
             {n+H^2}.
\end{equation}
In particular, if $a\ge0$, $\mathcal R_c\le T$ and $|H|\le H_0$
for $n\ge N$, with $T\ge0$, then
\[
 D\le\frac{6T\exp(H_0^2/(2N))}{n\phi(0)}.
\]
Theorem~\ref{v9:entry:theorem} supplies such numerical bounds under
its stated hypotheses. Thus the $1/n$ control of the defect comes from
uniform quantitative estimates, rather than from a fixed-law limit.''')
edit(f,'''We evaluate $\mathcal A=\int\tau(Q-h)$ in two ways. Gapwise integration
uses contact at both endpoints. Zero-bias integration converts the
polynomial part to moments and the conditional CDF part to a truncated
moment of the sum. Equating these expressions gives the identity.
Since $h(t)=\nu([t,\infty))$,''',r'''\emph{1. Integration over the gaps.}
Let $\mathcal A=\int\tau(Q-h)$. Since $h(t)=\nu([t,\infty))$,''')
edit(f,'For the second evaluation, signwise Fubini proves',r'\emph{2. Zero-bias integration.} Signwise Fubini proves')
edit(f,'Set $M=\\E[Z\\mathbf1_{Z\\le z}]$. Since',r'\emph{3. The first-moment identity.} Set $M=\E[Z\mathbf1_{Z\le z}]$. Since')
edit(f,'The pointwise identity\n$q_z(x)',r'\emph{4. Gaussian comparison and assembly.} The pointwise identity'+'\n'+r'$q_z(x)')
edit(f,'''Specialize from now on to $c=\CE$ and $a\ge0$. A first bound for
$\mathcal R_c$ proves a positivity condition; only then can the
threshold term improve the bound for the nonnegative expression below.''',r'''Specialize from now on to $c=\CE$ and $a\ge0$. The sharper estimate
below keeps the threshold loss. Its coefficient is not known positive
until a bound on $\mathcal R_c$ has first been established.''')
edit(f,'$\\rho\\ge l>0$, $0<c_-\\le c$, and a proved raw bound','$\\rho\\ge l>0$, $0<c_-\\le c$, and a proved remainder bound')
edit(f,'''Every conclusion holds at each actual index and raw threshold. Common
bounds on a closed moment cell make the result uniform even when the
maximizing law varies with $n$. There is no exchange of a limit with
contact, support gaps, moments, or an integral. In particular, the order
of use is essential: a raw ceiling first proves $M_c>0$ and a density
floor; only then may the Gaussian phase term be subtracted to improve
$\mathcal U$. A smaller resource ceiling is not a replacement for the
raw ceiling in that first step.''',r'''The corollary is used in two steps. First, an upper bound for
$\mathcal R_c$ proves $M_c>0$ and a positive lower bound for $e$.
Second, the now nonnegative term $n(1-e)M_c$ can be subtracted to
improve the bound for $\mathcal U$ by a multiple of $H^2$. This is the
improvement that helps bound the threshold. It is a bound on
$\mathcal U$, so it cannot be substituted for the initial upper bound
on $\mathcal R_c$. Every inequality holds separately at each $n,H$;
common bounds on a closed moment cell therefore also apply when the
maximizing law varies with $n$.''')
f='sections/07-direct-acquisition.tex'
edit(f,'''The entry calculation supplies the weighted defect and raw-threshold
bounds. The defect bound first locates the sign probability and controls
the inward endpoints and conditional variance. Two applications of
contact then bound the entire conditional support. This last step uses
the sharp predecessor bound; the preceding geometric estimates do not.''',r'''The localization theorem bounds $nD$. Lemma~\ref{ms:joint-defect}
bounds $D$ below by nonnegative costs, so a small defect makes each
cost small: the sign probability must be close to $p_*$, the support
gap must nearly reach the conditional means, and the spread within each
sign class must be small. Proposition~\ref{short:acq:geometry} makes
these conclusions quantitative using the defect alone.
Proposition~\ref{short:acq:strip} then uses contact and the sharp
predecessor bound to control the entire conditional support. Together
they give the domain needed by Theorem~\ref{short:count:local}.''')
edit(f,'''$(-A_-,A_+)$, so that its endpoints are not confused with the sign indicator
$B_0=\ind_{\{X>0\}}$.''',r'''$(-A_-,A_+)$, using the notation of
Section~\ref{ms:geometry-counts}. The first use of $n\ge700$ is the
inequality $B_*/700<.047$ below; the count comparison also uses this
sample-size bound in its error estimates.''')
edit(f,'''\begin{proof}
We have $D<D_0:=.047$,''',r'''\begin{proof}
\emph{1. A central gap and preliminary bounds.}
We have $D<D_0:=.047$,''')
edit(f,'''$0\le d<1$. Put $v=pq$ and $w=1-\theta=v\ell^2$, and define
\[
 \mathcal Q(p)=(\sigma+1)p^2+(\sigma-1)q^2-6pq
       =(6+2\sigma)(p-p_*)^2.
\]
We first retain all the costs of the actual conditional noises.''',r'''$0\le d<1$. Put $v=pq$ and $w=1-\theta=v\ell^2$, and use the
probability polynomial $\mathcal Q$ from
Section~\ref{ms:geometry-counts}.
We first retain all the costs of the actual conditional noises.''')
edit(f,'''Their masses sum to $\theta$. The outer-gap estimate gives the common budget''',r'''Their masses sum to $\theta$. In this notation the joint budget
\eqref{ms:joint-defect-budget} reads''')
edit(f,'''This is Lemma~\ref{ms:joint-defect} with $A=A_-$ and $B=A_+$.
The measures $\mu_\pm$ are only notation for the displayed
variance-weighted expectations; no new law is introduced.''',r'''The measures $\mu_\pm$ abbreviate the displayed variance-weighted
expectations under the same marginal $P$.''')
edit(f,'On $.36<p<.48$, $\\ell\\ge2\\sqrt z>1.67$, and the noise prices satisfy',r'\emph{2. Preliminary noise and inward-displacement bounds.}'+'\n'+r'On $.36<p<.48$, $\ell\ge2\sqrt z>1.67$, and the noise coefficients satisfy')
edit(f,'After replacing $d$ by zero, the derivative',r'\emph{3. The final probability and variance bounds.}'+'\n'+r'After replacing $d$ by zero, the derivative')
edit(f,'''the bound $D\ge\ell\theta C$, with $\ell>1.99$, improves
$\theta<.0036$ and consequently $\ell>1.996$.''',r'''the bound $D\ge\ell\theta C$, with $\ell>1.99$, improves
$\theta<.0036$ and consequently $\ell>1.996$.
Here the $d$-dependent terms may be dropped together, since
$6w(1-d)-\theta b_\pm>0$ on the current domain. Dropping only the
positive displacement term while keeping its negative noise correction
would not give this bound.''')
edit(f,'The exact conditional cubic expansion gives',r'\emph{4. The remaining moment bounds.} The exact conditional cubic expansion gives')
edit(f,'''To bound the scaled noise $\lambda$, retain the cubic cost rather than
only its sign.''',r'''\emph{5. From conditional spread to total count variance.}
A bound on $\theta$ alone would not control $\lambda=n\theta/\ell^2$
uniformly in $n$. We therefore retain more of the cubic cost. A
one-sided moment inequality supplies a variance-squared term divided by
the inward displacement; pairing it with the displacement cost by
AM--GM will give a larger linear coefficient of $\lambda$.''')
edit(f,'''Under Proposition~\ref{short:acq:geometry}, suppose $(P,H)$ is an attained
fixed-target pair at $\CE$ with nonnegative excess and true predecessor
$C_{n-1}\le\CE$.''',r'''Under the hypotheses of Proposition~\ref{short:acq:geometry}, suppose
in addition that $C_{n-1}\le\CE$ and that $(P,H)$ maximizes the excess
at $\CE$, with nonnegative maximum.''')
edit(f,'''Use the contact upper expression \eqref{v9:entry:contact}. The
all-threshold Gaussian heat estimate''',r'''A support point too far from its conditional mean would make the
contact upper expression \eqref{v9:entry:contact} negative. The
all-threshold Gaussian heat estimate''')
# Rename only the locally defined radial auxiliaries, avoiding the conservation L.
q=p/f;t=q.read_text();i=t.index(r'\begin{proposition}[Two contact rays]');before=t[:i];s=t[i:]
s=s.replace('h(t)',r'\overline H(t)').replace('g(t)',r'g_{\rm rad}(t)').replace('L(t)',r'\Xi(t)').replace("L'(t)",r"\Xi'(t)").replace("L''",r"\Xi''").replace("$L'$",r"$\Xi'$").replace('$L$',r'$\Xi$').replace('(L-g)',r'(\Xi-g_{\rm rad})').replace('$g>0$',r'$g_{\rm rad}>0$').replace('$h\\ge0$',r'$\overline H\ge0$').replace('majorant $h$',r'majorant $\overline H$')
s=s.replace('boundary atoms. Only the actual radial function is differentiated;\nthe absolute-value majorant $\\overline H$ is used solely at the boundary.','boundary atoms. We differentiate $H_n$ itself; the absolute-value\nmajorant $\\overline H$ is used only at the two boundary points.')
q.write_text(before+s)
