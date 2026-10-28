# Independent review of the geometric Bernoulli-reserve exclusion

Reviewed 28 October 2026. Outcome: **no mathematical blocker at the stated scope**. This review independently reconstructs the signed curvature estimate, finite binomial normalization, geometric noise reduction and complete signed excess comparison. Its checker imports no constructor code.

| Item | Mathematical status | Execution status |
| --- | --- | --- |
| Signed curvature lemma, including actual conditional variance allocation | Independently derived and checked | Fresh exact PASS |
| Exclusion when \(p\in[1/3,2/5]\) and \(nQ(p)/\sqrt{pq}\ge24\) | Locally derived and independently reviewed, using the named retained and external theorems | Fresh exact PASS |
| Five integer cutoffs | Exact consequences of the exclusion and the specified monotonicity | Fresh exact PASS |
| Acquisition of the support strips, budget and raw threshold | Retained, sign-specific dependency | Not rerun here |
| Full conjecture, reflected acquisition, finite base through 41 | Not established by this component | Not claimed |

## Source identity and scope

The reviewed constructor commit is 88b7dff029ae95ad815f9f0dd3e0a6e1af58cc29. Paths below are repository-relative.

| File | SHA256 |
| --- | --- |
| mathematics/simplification-v14/2026-10-28/geometry-slack.tex | 8eb6fc89d82eb458fef45fb9a2f9783c1cae2705c908dcb8bebba725a4a36461 |
| mathematics/simplification-v14/2026-10-28/geometry-slack-check.py | ee7ca3ad6ed5f500ecb6b075e212686d07b08fb3a24c7244340360dd74af2c19 |
| mathematics/simplification-v14/2026-10-28/geometry-slack-actual.py | ad738d3c0dc34efb91d99ad271debfbda0cbe3f3c7f279c2b05bc8403f17bfe2 |
| mathematics/simplification-v13/2026-10-28/crossing.tex | 0dda285adb9aaa24277fdc1d74843c20bc6100b2a64a0cd5ae34bb696a68a6ec |
| mathematics/simplification-v13/2026-10-28/geometry-noise.tex | f538debff3c902dc03aea4a3ebee64e19f414a6e8cc68aae0c803ccdb886e9de |

The constructor's lines 30–43 assert a signed CDF exclusion for actual iid marginals with centered conditional laws
\[
-.7\le U_0\le a_0,\quad -a_1\le U_1\le .7,\quad a_0+a_1\le .068,
\]
\[
n\ge42,\quad 1/3\le p\le.4,\quad \lambda=n(qEU_0^2+pEU_1^2)\le.32,
\quad nD\le129/4,\quad |H|\le1.84.
\]
The cost \(D\) is the actual support-gap cost, not an independently chosen moment coordinate. If \(nQ(p)/\sqrt{pq}\ge24\), the signed excess is less than \(-1/(10n)\). Both signs of \(H\), all phases and threshold atoms are included. An absolute-error assertion additionally needs this exclusion or another result on the reflected law, with the reflected acquisition premises. The theorem does not acquire its own hypotheses.

## 1. Signed curvature reconstructed from stop-loss expectations

For the actual conditional sum \(W_j\), put \(a=t-j\) and
\[
B_j=E(a-W_j)_+-a_+.
\]
Centering gives \(B_j=\{E|a-W_j|-|a|\}/2\ge0\). Cauchy–Schwarz gives \(B_j\le\sqrt T/2\); for \(a>0\),
\[
aB_j\le \frac a2(\sqrt{a^2+T}-a)\le T/4.
\]
The fourth-moment majorant follows from the exact factorization
\[
27x^4-256x+256=(3x-4)^2(3x^2+8x+16)\ge0.
\]
After scaling and applying this to \(W_j\) or \(-W_j\),
\[
B_j\le \frac{27M}{256|a|^3}\qquad(a\ne0).
\]
This derivation agrees with lines 95–106 without reusing the constructor's arithmetic implementation.

Direct cancellation of binomial factorials gives
\[
\pi_{j+1}-\pi_j=
\frac{np-q-j}{(n+1)pq}\,
P\{\operatorname{Bin}(n+1,p)=j+1\}.
\]
Only nonpositive coefficients may be discarded because \(B_j\ge0\). Write \(c=(np-q-t)_+\le1\). The remaining positive numerator is at most \((a+c)_+\). There is at most one mesh point in each of \((-c,0)\) and \([0,1)\). Their contributions are at most \(c\sqrt T/2\) and \(T/4+c\sqrt T/2\). For all remaining points, \(a=b+i\), \(0\le b<1\), \(i\ge1\), and the bound is
\[
\frac{27M}{256}\sum_{i\ge1}(i^{-2}+ci^{-3})
<\frac{27M}{256}(5/3+5c/4).
\]
The square series is bounded by its first five terms plus \(\int_5^\infty x^{-2}dx<5/3\); the cube series by its first two terms plus \(\int_2^\infty x^{-3}dx=5/4\), with strict integral domination. The mass estimate and \(\sqrt n/(n+1)^{3/2}\le1/n\) give precisely lines 87–90.

The moment envelope retains the actual two laws. A positive mass difference requires \(j<np-q<np\). Relative to \(nqs_0\) and \(nps_1\), the coefficients of \((n-j)s_0+js_1\) are at most \(1/q\) and 1, so \(T=\lambda/q\) is valid for every such count. Independence gives
\[
EW_j^4=\sum EU_i^4+3(EW_j^2)^2-3\sum(EU_i^2)^2
\le A^2T+3T^2.
\]
No common-noise assumption is made.

## 2. The finite binomial maximum

For \(N=n+1\ge43\), let \(m=\lfloor(N+1)p\rfloor\), \(r=m/N\), and \(\delta=m-Np\in[-q,p]\). Then
\[
r(1-r)=v+(q-p)\delta/N-\delta^2/N^2
\ge v(1-1/N-2/N^2)>39v/40.
\]
Here \(q(q-p)/v=(q-p)/p\le1\) and \(q^2/v=q/p\le2\), using the actual interval \(p\in[1/3,.4]\). The mode is interior. Explicit finite Stirling, discarding the nonpositive relative-entropy exponent and the negative denominator remainders, yields
\[
\max\pi_N\le\frac{\phi_0e^{1/(12N)}}{\sqrt{Nr(1-r)}}
<\frac{(2/5)\sqrt{40/39}(516/515)}{\sqrt{Nv}}
<\frac{.41}{\sqrt{Nv}}.
\]
The last step is an exact squared rational comparison. The exponential bound follows from \(e^x<(1-x)^{-1}\) for \(0<x<1\), at \(x=1/516\).

The external source was inspected directly: [Schulz's original thesis](https://d-nb.info/1197702695/34), Theorem 1 on printed page 1, gives the all-\(p\) binomial bound and the sharper bound only on \(p\in[1/3,2/3]\). Its explicit Stirling remainder appears on printed page 139 (PDF page 149). Neither external result is being claimed as newly proved here.

## 3. Geometric reduction and its hypotheses

The retained v13 geometric theorem concerns one compactly supported actual sign law, its actual central gap, conditional centering and the inward sum bound. These premises follow here: \(a_0<p\) and \(a_1<q\), so \(B=0\) and \(B=1\) give strictly negative and positive standardized values. In particular there is no atom at zero. If the supplied \(a_j\) are loose support bounds, choose the actual compact-support extrema instead; their inward sum is no greater than .068. The central-gap cost in \(D\) then has the required meaning.

The retained inequality at geometry-noise.tex lines 78–85 gives
\[
nD\ge\frac{nQ/\sqrt v+\lambda\min(Y_0,Y_1)/v^{3/2}}
{(1+\lambda/(nv))^{3/2}}.
\]
For \(\bar d=.068\), the two \(Y_j\) are those at constructor lines 159–165. To rederive their uniform lower bound, maximize the four squared denominators. Their derivatives have factors \(1-4p,2-5p,3-4p,3-5p\); hence the maxima occur at \(1/3,.4,.4,.4\), respectively. Their exact squared values are
\[
8/81,\quad108/3125,\quad24/625,\quad72/3125,
\]
strictly below the squares of \(63/200,93/500,49/250,19/125\). Also \(v^{3/2}>13/125\), the two radical numerators exceed \(24/5\) and \(69/20\), and
\[
3.162277660<\sqrt{10}<3.162277661.
\]
Substituting the lower radical endpoint into positive terms and the upper endpoint into negative terms proves \(Y_0/v^{3/2}>100\) and \(Y_1/v^{3/2}>100\).

The original \(\lambda\le.32\) gives \(x=\lambda/(nv)\le6/175\). Since
\[
(1+x)^{3/2}\le1+3x/2+3x^2/8\le1+(31/20)x,
\]
the stated geometry and reserve threshold imply
\[
24+100\lambda\le(129/4)\{1+(31/20)(3/28)\lambda\}.
\]
Thus \(\lambda\le1680/19273<.09\). This reduction is uniform and has no phase or allocation grid.

## 4. Complete excess comparison, including signs and atoms

Write \(t=np+w\), \(w=H\sqrt{v+s}\), \(k=\lfloor t\rfloor\), \(u=t-k\). Now \(v+s<.25\), so \(|w|<.92\) and \(c=(-q-w)_+<.32\). The hypotheses of the retained crossing identity hold: positive separation \(1-a_0-a_1\), width \(.7+a_1<1\), and \(na_0\le t<n(1-a_1)\), the last following already from \(n\ge42\) and \(|w|<.92\). Discarding its nonnegative weighted loss yields the interpolation-plus-curvature bound at lines 198–200. The identity's closed lower and strict upper crossing events retain atoms at equality.

The sharper external binomial inequality has normalized constant
\(\phi_0(4-2p)/(6\sqrt v)\) on this interval. Algebra gives
\[
(\sqrt{10}+3)(1-2v)-(4-2p)=Q(p).
\]
Consequently each of the two Bernoulli CDF values has strict reserve at least \(4\phi_0/n\) after subtracting \(C_E\rho_B\). Convex interpolation preserves strictness even when \(u=0\). There is no extrapolation below \(p=1/3\).

For \(G(x)=\Phi((x-np)/\sqrt{nv})\), the signed bound
\[
G''(x)\le\phi_0(np-x)_+/(nv)^{3/2}
\]
on the full interpolation segment gives
\[
\sqrt n\{(1-u)G(k)+uG(k+1)-G(t)\}
\le\frac{\phi_0}{2nv^{3/2}}u(1-u)(u-w)_+.
\]
For \(H\le0\), changing to the actual variance is favorable and the interpolation cost is at most
\((2/5)(23/200+2/27)/(nv^{3/2})\).
For \(H\ge0\), \(c=0\); the interpolation cost is at most
\((2/5)(2/27)/(nv^{3/2})\), and the variance cost is at most
\((2/5)(23/25)(9/100)/(2nv^{3/2})\).
These bounds use \(u(1-u)\le1/4\), \(u^2(1-u)\le4/27\), and
\(1-(1+x)^{-1/2}\le x/2\). They cover the whole closed threshold range without a phase grid.

For the actual marginal the raw absolute third moment is
\[
v(1-2v)+3v(s_0+s_1)-qEU_0^3+pEU_1^3.
\]
The inward support bounds give \(EU_0^3\le a_0s_0\), \(EU_1^3\ge-a_1s_1\). Since \(p\le q\), the raw gain is at least \((3p-.068)s\). Subtract the normalization Taylor bound to obtain
\[
(v+s)^{3/2}(\rho-\rho_B)\ge
s\{3p-\tfrac32(1-2v)-.068-\tfrac38(1-2v)s/v\}>0
\]
for \(s>0\). Its braces are bounded below using \(p\ge1/3\), \(v\ge2/9\), \(1-2v\le5/9\) and \(s<.09/42\). At \(s=0\) the difference is exactly zero.

Finally take \(T=.15\), \(M=.141\), \(\sqrt T<.388\), \(\beta=.41\), and \(v^{3/2}>.104\). Reconstructing both complete error budgets gives
\[
E_-=\frac{2669950133}{1797120000},\qquad
E_+=\frac{49577387}{71884800}.
\]
Both are less than \(4(19943/50000)-1/10<4\phi_0-1/10\). The exact gap between the larger error and this conservative target is
\[
\frac{87674999}{8985600000}>0.
\]
Combining all terms proves the claimed \(-1/(10n)\) signed excess margin.

## 5. Integer cutoffs and retained limitations

On \([1/3,.4]\), \(Q>0\) decreases because \(p_* >.4\), while \(v\) increases. Thus \(Q/\sqrt v\) decreases. The independent checker works in \(\mathbb Q(\sqrt{10})\), verifies signs before squaring, and proves
\[
N^2Q(b)^2>576\,b(1-b),\qquad
(N-1)^2Q(b)^2<576\,b(1-b)
\]
for \((b,N)=(1/3,126),(.35,196),(.375,491),(.39,1141),(.4,2682)\).
Therefore the displayed upper cutoffs 125, 195, 490, 1140, 2681 are correct. The independent exact comparison also verifies the retained geometric endpoint giving \(n\le168\) below \(1/3\). This extends the columns with \(b\ge.35\) to the acquired interval \([.25,b]\); it does not extend the 125 cutoff below \(1/3\).

The result removes the need for count-tail computations in the excluded region, once the stated acquisition premises are available. It does not justify deleting any existing certificate. The remaining region \(nQ/\sqrt v<24\), the finite base, acquisition and the reflected branch retain their previous obligations.

## 6. Fresh evidence and adversarial controls

Replay from a worktree containing both the review and constructor sources:

    python3 -I -B mathematics/simplification-v14/2026-10-28/geometry-slack-review-run.py RUN_ID

In this separate review worktree, the recorded command additionally used:

    --source ../geometry-v14/mathematics/simplification-v14/2026-10-28/geometry-slack.tex

Final receipt: runs/geometry-slack-review-v14-20261028/check03/receipt.json. Fresh PASS: 2,638 exact gates and actual-law checks, 72 actual curvature cases, four negative controls; elapsed 0.395 seconds under Python 3.9.6. Checker SHA256: b647fe55bbde358bf55ed7c59d94e0dd90b7c77df85e9869500d6dcfc594e5e7. It imports only the Python standard library and reconstructs finite conditional sums directly. It binds the reviewed TeX bytes; hashes are integrity evidence, not proofs.

The 72 actual cases include zero noise, tiny noise, exact threshold collisions, symmetric conditional noise and each physical variance-allocation endpoint, at \(n=42\), three probabilities and three threshold shifts. They test the curvature lemma; they do not assert that every fixture meets the main theorem's geometric reserve premise.

The controls distinguish genuine counterexamples from proof-premise checks:

1. **Genuine failure if the \(c\sqrt T\) term is deleted.** Take \(n=42,p=7/20,t=14\), common independent conditional noise \(U=\pm10^{-5}\). Only the \(j=14\) stop-loss term is nonzero. Since \(\pi_{15}/\pi_{14}=196/195\), its curvature is positive of order noise amplitude, while the proposed bound with the square-root term deleted is of order amplitude squared. Exact outward square-root comparisons reject it, within the raw threshold range.
2. **Genuine failure of the favorable rho sign below \(1/3\).** For \(p=13/50\), let \(U_0=\pm10^{-3}\) symmetrically and \(U_1=0\). Exact positive squaring proves \(\rho<\rho_B\). This is a counterexample to that intermediate extension, not to Berry–Esseen.
3. **Invalid cutoff inference rejected.** The inherited bound \(n\le168\) cannot imply \(n\le125\). This control checks the proposed inference, not an actual counterexample to a stronger theorem.
4. **Near-mesh counting premise rejected without \(c\le1\).** With \(c=3/2\) and mesh \(a=3/4-j\), two points lie in \((-c,0)\). This invalidates that proof step after removing its hypothesis; it is not asserted to disprove every possible extended curvature bound.

Development receipts are preserved. check01 failed because the initial last-control fixture had only one near-mesh point and therefore did not exercise its intended rejection. check02 failed on a literal escaped newline introduced while adding the allocation fixtures. check03 corrects these test-source defects; the theorem, arithmetic targets and source pin were unchanged.
