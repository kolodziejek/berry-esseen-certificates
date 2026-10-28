# Independent review of the v15 domain union

The local domains join without a gap. The new right theorem and the retained small-noise comparisons cover the entire right-strip noise range at \(n\ge200\). The corresponding left union covers \(p\in[1/3,.4]\) at \(n\ge700\). With the named geometric and support-acquisition premises, these exclude every acquired nonnegative signed witness at \(n\ge700\).

The domain-union proof is conditional on the named component theorems. This review does not replace their separate mathematical reviews.

This is **not an unconditional Berry–Esseen cutoff**. The precise local, acquired-witness and least-first-failure statements are separated below.

**Independence disclosure.** This reviewer constructed loss-direct.tex, the five-count primitive. The present review independently derives the domain union, witness normalization, acquisition joins and logical scope from the component statements. It is not a second independent verification of that primitive or of the new right/left component inequalities. Their separately assigned component reviews remain necessary.

| Item | Mathematical status | Execution status |
| --- | --- | --- |
| Component-domain union, actual-law mapping and endpoint conventions | Independently derived from the exact stated hypotheses | Fresh exact checks recorded separately |
| Coarse high-probability exclusion from \(n=106\) | New elementary consequence of the retained geometric theorem | Exact rational endpoint and monotonicity gates |
| New right and left signed inequalities | Component theorem inputs; separate reviews apply | Constructor/reviewer evidence is not rerun here |
| Support and coarse-entry acquisition | Retained conditional ancestors | No acquisition campaign rerun |
| Global cutoff or independent finite base | Not established by this review | Not claimed |

## 1. Local domain-union theorem

Write
\[
\mathcal E(P,n,H)=
\sqrt n\{P(X_1+\cdots+X_n\le H)-\Phi(H/\sqrt n)\}
-C_EE|X|^3,
\qquad C_E=\frac{3+\sqrt{10}}{6\sqrt{2\pi}}.
\]
All sums use independent copies of one centered, variance-one marginal.

**Local union.** Suppose \(Y=B+U\), \(B\) is Bernoulli with parameter \(p\), and \(E(U\mid B)=0\). Set \(v=p(1-p)\), \(s=EU^2\), \(\lambda=ns\), and \(X=(Y-p)/\sqrt{v+s}\). Assume \(|H|\le1.84\). Then \(\mathcal E(P,n,H)<0\) under either row:

| Row | Index | Probability | Conditional support | Inward sum | Noise |
| --- | --- | --- | --- | --- | --- |
| Right | \(n\ge200\) | \(p\in[.4,.53]\) | \(-.6\le U_0\le a_0,\ -a_1\le U_1\le.6\) | \(a_0+a_1\le.072\) | \(0\le\lambda\le.36\) |
| Left | \(n\ge700\) | \(p\in[1/3,.4]\) | \(-.7\le U_0\le a_0,\ -a_1\le U_1\le.7\) | \(a_0+a_1\le.068\) | \(0\le\lambda\le.32\) |

The quantities \(a_0,a_1\) are nonnegative. Neither row needs contact, a predecessor theorem, a geometric budget or \(d\le3/n\) as an intrinsic hypothesis. Those premises enter only when acquiring the displayed conditions for a witness.

**Proof of the right union.** For \(0<\lambda\le.075\), the retained v12 union applies. Its exact constituents are:

- counts-v11.tex: all phases in \([-.272,.728]\), \(0<\lambda\le.03\), and \(C\ge.4\);
- outer.tex: phases \([-.272,-.15]\cup[0,.728]\), \(0<\lambda\le.075\), and \(C\ge.4\);
- compound-proof.tex: phases \([-.15,0]\), \(.03\le\lambda\le.075\), and \(C\ge.4\).

The same \(n\ge42\), support, centering, inward and raw-threshold premises occur in all three statements. The domains overlap at \(\lambda=.03\), \(u=-.15\) and \(u=0\), with closed endpoints. Their phase union has length one. Thus every actual threshold admits a legal integer anchor.

Each comparison states \(\Delta_C=\mathcal E_C-B_{C,k}<0\), where
\[
B_{C,k}=\sqrt n\{F_B(k)-\Phi((k-np)/\sqrt{nv})\}-C\rho_B,
\qquad \rho_B=(1-2v)/\sqrt v.
\]
At \(C=C_E>.4\), the external strict finite-binomial theorem gives \(B_{C_E,k}<0\). Consequently \(\mathcal E<0\). The negative-inner component does not claim a margin \(-\lambda/100\); the union preserves its weaker strict conclusion.

For \(.075\le\lambda\le.36\), right-direct.tex gives the full signed excess directly, with margin \(-\lambda/100\), at every \(n\ge200\). The shared endpoint .075 is covered twice. Its floor anchor need not equal the shifted v12 anchor: both theorems conclude a statement about the same \(\mathcal E(P,n,H)\).

**Proof of the left union.** For \(0<\lambda\le.01\), LEFT-01 in leftcount.tex applies on the larger interval \(p\in[.25,.4]\), with amplitude .7, inward sum .068 and \(C\in[.4095,.41]\). The phase interval \([-.218,.782]\) has length one. Since \(.4095<C_E<.41\), its comparison and the finite-binomial theorem give \(\mathcal E<0\). For \(.01\le\lambda\le.32\), geometry-left.tex supplies the full signed inequality at \(n\ge700\). The endpoint .01 is included in both.

At \(\lambda=0\), \(EU^2=0\), hence \(U=0\) almost surely and the marginal is standardized Bernoulli. Apply the external theorem directly. No limiting argument in the noise, or inference from a positive-noise strict margin, is used.

The rational checker independently encloses \(C_E^2=(19+6\sqrt{10})/(72\pi)\), using finite alternating sums in Machin's formula for \(\pi\) and rational squared enclosures for \(\sqrt{10}\). It checks both coefficient ranges, rather than assuming that the left theorem allows arbitrary \(C\ge.4\).

The only external probability theorem used by this join is [Schulz, Theorem 1, printed page 1](https://d-nb.info/1197702695/34): its all-\(p\), finite-\(n\), strict binomial bound applies at every anchor. The sharper middle-probability reserve is unnecessary for this union.

## 2. Exact normalization of an acquired marginal

Let \(Z\) be the original centered, variance-one marginal, with actual sign \(B=1_{\{Z>0\}}\), no atom at zero, and \(p=P(B=1)\). Put \(m_j=E(Z\mid B=j)\) and \(\ell=m_1-m_0>0\). Centering gives
\[
m_0=-p\ell,\qquad m_1=(1-p)\ell.
\]
Define \(U=(Z-m_B)/\ell\) and \(Y=B+U\). Then \(E(U\mid B)=0\) and
\[
Z=\ell(Y-p).
\]
For \(\theta=E(Z-m_B)^2\), total variance gives
\[
1=\theta+v\ell^2,\qquad
s=EU^2=\theta/\ell^2,\qquad v+s=\ell^{-2}.
\]
Therefore \((Y-p)/\sqrt{v+s}=Z\) pointwise. In particular \(\lambda=ns=n\theta/\ell^2\), not \(n\theta\). This preserves the actual conditional laws and their actual iid convolutions.

For sums,
\[
\sum Z_i\le H\quad\Longleftrightarrow\quad
\sum Y_i\le np+H/\ell.
\]
The raw threshold \(H\) is unchanged, and its normal term remains \(\Phi(H/\sqrt n)\). The comparison does not replace raw \(H\) by the standardized sum threshold.

If \((-A_-,A_+)\) is the actual central gap, then
\[
a_0=p-A_-/\ell,\qquad a_1=(1-p)-A_+/\ell,\qquad
d=a_0+a_1.
\]
Conditional mean ordering gives \(a_j\ge0\), while the actual gap gives \(U_0\le a_0\) and \(U_1\ge-a_1\). This identifies the same inward coordinates used by the geometric and local-comparison theorems.

## 3. Acquired-witness exclusion at every index at least 700

**Conditional acquired-domain theorem.** Assume an actual standardized marginal with compact support, no zero atom and its actual central gap satisfies the retained coarse geometric premises
\[
n\ge700,\quad p\in[.25,.54],\quad d\le.068,\quad
0\le\lambda\le.616,\quad nD\le32.20665378,\quad |H|\le1.84,
\]
where \(D\) is the actual support-gap cost defined in geometry-noise.tex. Suppose also that the left amplitude .7 is available when \(p\in[1/3,.4]\), and the right amplitude .6 when \(p\in(.4,.53]\). Then \(\mathcal E(P,n,H)<0\).

**Proof.** The retained v13 geometric theorem gives \(\lambda<.36\) throughout the coarse probability interval and \(\lambda<.32\) for \(p\le.4\). It also gives \(n\le168\) for \(p\le1/3\), excluding that probability region at the present indices.

There are two valid ways to handle the high-probability end:

1. The retained v10 connection proposition explicitly excludes entry panels 24 and 53 and retains panels 25 through 52. With its named premises, their closed union is \([.25,.53]\). Thus the refined probability upper bound .53 is already an acquisition output.
2. Even if only the widened coarse interval \([.25,.54]\) is retained, the geometric theorem excludes \(p\ge.53\) for \(n\ge106\). This gives a separate fallback for the present \(n\ge700\) union.

For the second argument, use the actual v13 monotonicity in \(\lambda\) to obtain
\[
D\ge Q(p)/\sqrt{p(1-p)}.
\]
One cannot get this by dropping the noise from the variance denominator. The retained proof uses the positive prices \(H_j>30\), \(Q\le9/25\), \(v\ge3/16\), \(\lambda/n\le11/750\) and the positive derivative guard
\[
30\{1-(11/750)/(2(3/16))\}-3(9/25)/(2(3/16))>0.
\]
For \(p\ge.53\), \(Q(p)=(6+2\sqrt{10})(p-p_*)^2\) increases, \(p_*<.53\), and \(p(1-p)\) decreases. Thus the ratio is increasing. At \(p=.53\), positive-base rational squaring with a lower enclosure for \(\sqrt{10}\) proves
\[
106^2Q(.53)^2>(32.20665378)^2(.53)(.47).
\]
This contradicts the coarse budget for \(n\ge106\). It is a geometric exclusion, not an extension of the right count theorem to \((.53,.54]\).

The remaining probabilities are in \((1/3,.4]\) or \((.4,.53)\). Their geometric noise ceilings and the stated strips meet the local union theorem exactly. This proves the conditional exclusion.

At \(p=.4\), the left row already suffices at \(n\ge700\) under the weaker amplitude .7. If the right amplitude .6 is also acquired, either row applies. Overlap never licenses an inference from the .7 support bound to the .6 bound.

### Where the acquired premises come from

These are literal source-to-theorem joins, not a new audit of the whole acquisition chain:

- manuscript/arxiv-v1/sections/04-fixed-entry.tex, the four-signed-pass condition and selected coarse-entry theorem, exports \(nD\le32.20665378\) and raw \(|H|\le1.83605680<1.84\). It retains the attained fixed-target, nonnegative excess, sharp predecessor, external structural inequality and complete coarse proof-object premises.
- mathematics/simplification-v10/2026-10-28/geometry.tex, the connection proposition, supplies the retained probability panels and the .6 right strips through the all-threshold heat/ray argument. Its raw-threshold input still comes from the preceding signed entry.
- mathematics/simplification-v11/2026-10-28/leftpanels.tex supplies \(-.6<U_0\le a_0\), \(-a_1\le U_1<.7\), \(d<.068\) on all fifteen closed panels 25–39. These imply the closed .7 left hypotheses.
- mathematics/simplification-v13/2026-10-28/geometry-noise.tex uses the actual gap and the coarse geometric premises to derive the strict noise ceilings and the low-\(p\) index bound.

The stronger acquired displacement \(d<.068\) implies the right theorem's \(d\le.072\). The converse is neither needed nor asserted. A hypothetical law supplied only with the abstract right-strip bound .072 cannot be inserted into v13's .068 geometric theorem.

## 4. Reflection and first-failure logic

For any sum \(S\), with \(z=H/\sqrt n\),
\[
P(-S\le-H)-\Phi(-z)
=\Phi(z)-P(S<H)
\ge\Phi(z)-P(S\le H).
\]
The difference between the two sides is the atom \(P(S=H)\). Thus a negative closed-CDF discrepancy is dominated by a positive closed-CDF discrepancy of the reflected marginal; equality at atoms is not assumed.
Equivalently, \(P(S>H)=P(-S<-H)\le P(-S\le-H)\) gives the required bound at the same threshold. No threshold limit or extension of the raw-\(H\) domain is needed.

The reflected law has \(p'=1-p\), \(U'_0=-U_1\), \(U'_1=-U_0\), and swapped inward endpoints. The probability interval \([.25,.53]\) is not invariant under this operation. Knowing that one oriented law satisfies a strip does not acquire the required probability, gap, contact or predecessor information for its reflection. The retained fixed-target reflection/attainment argument chooses an oriented positive witness; the acquisition must then be applied to that witness.
The geometric cost contains the signed term \(-\gamma\); its acquired numerical bound is likewise not copied to a reflected law without justification.

**Conditional least-first-failure corollary.** Assume a genuine base \(C_j\le C_E\) for \(1\le j\le41\), together with the named attainment/reflection and acquisition implications at every least failing index \(n\ge42\). If a strict row bound fails somewhere at or above 42, its least failing index must lie in
\[
42\le n\le699.
\]
Indeed minimality supplies the true sharp predecessor. The acquired-domain theorem excludes \(n\ge700\). This corollary does not settle any of the remaining indices.

BASE41 plus this conditional tail exclusion does **not** prove an unconditional cutoff at 700. An unresolved earlier failure would invalidate the sharp-predecessor premise at a later failing row. To deduce strict bounds for all \(n\ge700\) by this least-failure argument alone, one needs a genuine base through 699, or an independently established argument covering 42–699 in addition to BASE41. Historical C4/C5 headers are not substituted for such a base.

## 5. What becomes unnecessary, and what remains

After acquisition, the new five-count signed proofs replace the older larger-noise count comparison on:

- the right strip at \(n\ge200\), \(.075\le\lambda\le.36\);
- the left strip \(p\in[1/3,.4]\) at \(n\ge700\), \(.01\le\lambda\le.32\).

The local union uses the retained small-noise results below these endpoints. In particular, the v12 negative-inner 291-cell certificate remains an ancestor where it supplies the right small-noise join. Coarse Fourier entry, the signed raw-threshold export, actual-gap geometry, support acquisition, reflection/attainment and a genuine finite base remain separate dependencies. No deletion is authorized by this review.

The new union does not close general larger noise on right indices 42–199 or on the remaining left indices below 700. The retained geometric and v14 reserve exclusions remove portions of those domains, but no complete finite-range conclusion follows here. Nor does a result for both signs of \(H\) become an absolute-CDF theorem without the reflected-law step.

## 6. Evidence, source binding and negative controls

The exact checker imports no constructor program. It verifies the complete right small-noise phase/noise refinement, both new noise joins, shifted-anchor coverage, coefficient ranges, panel incidence, the low/high probability exclusions and twelve actual normalization examples. The common-refinement checks examine each boundary and every open stratum; they are exact interval-cover arguments, not sampled positivity.

Its controls reject the coarse .535 probability as a right-count input, the inference from amplitude .7 to .6, the extension of the left coefficient range to arbitrary \(C\ge.4\), removal of the negative-inner component, removal of the zero-noise branch, equality under reflected atoms, reflected probability coverage without reacquisition, and the invalid BASE41-to-unconditional700 inference. These are counterexamples to intermediate implications, not counterexamples to Berry–Esseen.

All reviewed source paths and SHA256 pins are in join-review-sources.json. The checker verifies those bytes. Hashes establish identity, not correctness. Final run evidence is under runs/join-review-v15-20261028/. No component-generation campaign or inherited suite was rerun.

The recorded checks verify 240 exact conditions, 28 right phase/noise strata and twelve actual marginal mappings, with seventeen negative-control instances. Nine instances reject confusing standardized residual variance with Bernoulli-coordinate noise; the remaining eight test domain or logical implications. The initial check01 passed against the pre-clarification component sources. check02 binds the final source versions with their shorter concavity explanations; all theorem domains and numerical targets are unchanged.

Replay after integration:

    python3 -I -B mathematics/simplification-v15/2026-10-28/join-review-check.py

In the separate review worktree, supply the two constructor locations:

    --right-root ../simplification-v15 --left-root ../geometry-left-v15
