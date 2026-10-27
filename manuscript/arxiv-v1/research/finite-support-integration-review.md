# Independent review: finite-support integration at n=5

Date: 2026-10-27. Reviewer worktree: `manuscript-finite`, branch `manuscript/finite-20261027`, starting commit `559e898ffebc9c697e7db3d4197fbcdecd444021`. The reviewer authored `finite-analysis.tex`; this is **not** independent review of that appendix. It is independent review of the separate constructor's `finite-support.tex`, with the review focused on the interface into the former appendix. No constructor file was modified.

Reviewed source snapshot:

- `/Users/bkolodziejek/Downloads/BE_Codex_Handoff/work/fork_audit_20261027/manuscript-finite-support/manuscript/arxiv-v1/appendices/finite-support.tex`, SHA256 `f36222ddc38a88e0b0529d94216f8d26087172c8d4bcf32bab7cb37b9600faa1` (596 lines; constructor's file was still uncommitted during this review).
- Reference comparison: `paper/analytic-supplement.txt:342–797`, especially the direct support proof at 375–478, heat expansion and finite bands at 480–678, and bounded-threshold/strip derivation at 680–797. Original source SHA256 `dad4a3558b01bda4acfdfc9120a50ecbcd7a6f2389886ba3ce72a6602ec39018`.
- Consumer: `finite-analysis.tex:2174–2306`, especially the zero-allowance lemma and the six required support radii in the C5 Fourier-band table.

## Conclusion

The new direct support lemma is an analytically valid route at **n=5**. It supplies a proof of the conditional support implication that the finite appendix needs, but **does not establish the six actual support-radius predicates**. Those still require whole-threshold endpoint inequalities, both signs, exact elementary enclosures, and their complete coverage. The new theorem restricted to n≥42 cannot replace them. No BASE41 or C5 completion follows.

I found no mathematical defect in the bounded continuous derivations reviewed below. Two visible TeX concatenations (`\suppP`, `\CEQ(t)`) were reported to the constructor and were corrected in the snapshot named above. I did not compile or alter the constructor's file; its separate build evidence belongs to its constructor.

| Item | Mathematical status | Execution status |
|---|---|---|
| Direct n≥2 support implication, including the complete-H method | Independently re-derived from the stated contact/predecessor inputs and Gaussian derivative bounds | No native support checker run |
| Applicability of its non-endpoint gates to six C5 Fourier rows | Independently derived and checked with exact rational arithmetic, conditional on the C5 contrary owner and genuine C4 bound | Fresh bounded Fraction-only gate check PASS |
| Whole-H endpoint inequalities at the six C5 radii | Still conditional; not provided by the new appendix's historical n27 or n≥36/n≥47 rows | Not run, not proved |
| Fifth-order remainder, Gaussian far bound, finite-band clearing and bounded-threshold series | Independently checked derivation at the declared scopes; no review of every historical numerical row | No polynomial/cell acceptance run |
| Historical strip/resource schedules | Conditional as presented; their actual acquired input rows and complete native acceptance remain separate | No historical receipts rerun |

## Direct n=5 derivation and exact hypotheses

At a contrary unrestricted maximizing owner, assume C4≤CE<C5. In the support appendix's notation,

`A = 2 Delta_4(P)/rho = R_4(P) ≤ CE < C5`, so `d_P=5(A-C5)<0` and `q=0`.

This is a statement about the same marginal. It does not use a maximizer constrained to a rho band and does not assume C5≤C4. The owner and its contact equality must have been supplied by the global attainment/contact theorem.

At n=5 use `s=sqrt(5)/2` and `e=5s-11/2`. Fixed safe rational enclosures are

`S=1119/1000`, `E=91/1000`, `c=819/2000`.

They obey `S²>5/4` and `((E+11/2)/5)²>5/4`, with both compared quantities positive; hence s<S and e<E. The manuscript's certified CE>c gives c<C5.

For each moment band use its upper rho endpoint r and its required radius R. The sign-moment condition

`(1+beta²)² ≤ rho²(1-beta²)`

follows directly from signwise Cauchy: with a±=(1±beta)/2 and mu=E X+=E X-, one has mu²≤a+a- and rho≥(a+²+a-²)/mu. The beta bound is therefore derived from the same owner, not an independent relaxed choice. Since `(1+b²)²-r²(1-b²)` increases with b≥0, its strictly positive value at the displayed rational b implies |beta|<b.

The independent rational audit used exactly these rows:

| r | R | b | Q(R),Q′(R),Q″(R),L(R),L′(R) |
|---|---|---|---|
| 5/4 | 13/5 | 194587/500000 | all strictly negative |
| 7/5 | 117/40 | 47871/100000 | all strictly negative |
| 3/2 | 25/8 | 525521/1000000 | all strictly negative |
| 8/5 | 133/40 | 282707/500000 | all strictly negative |
| 17/10 | 7/2 | 600001/1000000 | all strictly negative |
| 7361/4000 | 15/4 | 641563/1000000 | all strictly negative |

Here `Q(v)=-v³+(3r/2)v²+3bv+rE`, `L(v)=(2/5)(v²/2+1/2+E)+cQ′(v)`; the additional gate `1/5-3c<0` also holds. Thus no failure of these algebraic ray gates blocks the n=5 application.

**Remaining endpoint obligation for each row:** prove, for both eta=±1,

`sup_{H in R} H_5(H,eta R) < -c Q(R)`.

The appendix gives a valid finite method for this: on every closed H cell bound midpoint value, derivative and curvature remainder; add both infinite tails after checking H0≥5sqrt(5) and H0-R≥10. Its identity `H_n(H,-R)=-H_n(-H,R)` preserves the signed branch; it does not make an upper bound on only the positive function sufficient without also bounding its negative.

The exact allowable right-hand sides from the bounded audit are respectively

`112080969/156250000`, `17888993577/16000000000`, `228118527/160000000`, `145482196041/80000000000`, `8489409201/4000000000`, `85589497539/32000000000`.

The generic all-threshold cubic Gaussian upper bound alone does **not** close these endpoints: `R³/15+R/5+1/2+cQ(R)` is positive in every row, with exact values

`691132093/468750000`, `26164556423/16000000000`, `832206919/480000000`, `431312661877/240000000000`, `23231772397/12000000000`, `66910502461/32000000000`.

These positive upper bounds are not counterexamples to support exclusion. They show only that this coarse analytic majorant cannot prove the required negative endpoint bound. A sharper whole-H certificate or another independently justified estimate is still necessary.

## Independently checked continuous calculations

1. **Contact scaling, direct lemma (support appendix 59–122).** Insert the same-law predecessor discrepancy bound in contact and use `n(sA-C)=s d_P+n(s-1)C`. Combining the constant C-rho terms leaves exactly `rho e`, not an omitted half-scale term. Replacing rho,beta,e by r,b,E is safe because E≥0 and v=|t|≥0. Only after Q<0 may C≥c be replaced by c. q≥0 and S,r>0 control the signed predecessor term.

2. **Ray monotonicity.** With z=H/sqrt(n), y=z-t/sqrt(n), differentiation gives `∂t H_n=n phi(z)+Ht phi(z)-ns phi(sy)`. Taylor expansion of phi(y) about z and `∂s[s phi(sy)]=-phi''(sy)` yield the stated absolute derivative bound. Since Q‴=-6 and L″=2/5-6c<0, the endpoint derivative gates propagate to both complete support rays. Contact equality on the full closed support then excludes endpoints, atoms of arbitrary small mass and accumulation points.

3. **Whole-H curvature and tails (124–152).** The second H derivative of the CDF-difference term is bounded by `(sqrt(n)/4)(n/(n-1)+1)`. The nt-phi term contributes at most `(2/5)R`; differentiating H phi(H/sqrt(n)) twice contributes at most `2|R²-1|/(5sqrt(n))`. The Taylor cell bound is therefore valid. On both remote tails the two Gaussian CDF values lie in the same interval of length tau, so the CDF difference costs tau, not an unjustified cancellation or missing factor two. The stated H0 gates license both this fact and monotonicity of |H|phi(H/sqrt(n)).

4. **Scale correction and fifth heat identity (34–52, 171–251).** The exact scale endpoint is 823/4050000 (fresh rational check). Heat Taylor expansion gives coefficients `(t/2-t³/6)`, `(t⁴-6t²+3)/24`, and `(t/8-t⁵/120)` on the third through fifth spatial derivatives. The residual coefficient is `u⁶/720+1/48+(u²-1)/16`; with u>sqrt(3) it is nonnegative. Gaussian Fourier norms yield exactly the displayed powers and constants 51/14400, 51/960, and 1/8 after division by s³. The fourth-derivative tangent follows from integrating cos(yz)≥1-(yz)²/2 against the nonnegative Gaussian y⁴ weight.

5. **Signed envelope and finite-band polynomial (253–423).** The positive inner threshold region is bounded by a concave quadratic; the negative sign and outside region require the explicit domination gate. For a band, using D+ in the adverse curvature and D- in the favourable constant is safe; its proof uses a common worst-case envelope and does not infer monotonicity of a signed coefficient. The factor 9B+²/4 is exactly `(u⁴-6u²+3)²/[256(N-1)]`. The new positive ell requirement and the explicit rational remainder are appropriate. The u≥5/2 condition ensures nonnegative A,B,D. This method has N≥36 and cannot itself be called at n=5.

6. **Far-Gaussian bound (286–334).** Spatial second-order Taylor has remainder ≤phi(0)|t|³/6. For f(lambda)=Phi(u/sqrt(1-lambda)), direct differentiation gives the displayed f″; the global Gaussian first/third-power bounds give |f″|<5/4 on [0,1/2]. The scale remainder is therefore <5/(8sqrt(n))<1/2. The surviving mean-value term is bounded by phi(0)|t|/2. All cancellations and signs are valid also at t=0. This is an independently checked all-H, both-t, n≥2 derivation.

7. **Bounded-threshold series and panel scope (454–582).** Expanding S(z) gives the displayed P0 and general coefficient formula. At z0=1/4, the separate positive coefficient majorants sum to the displayed B_r; a degree≥7 tail in S divided by z gives `4^7 B_r/n^6`. It is uniform only on the declared bounded H,t rectangle. The panel test additionally fixes floor47, score excess .7/n, predecessor loss .19, acquired support and signed beta. Its signed coefficient directions are correct, but it cannot be moved to n=5 by referring only to the more general n≥4 series lemma.

This review did not establish the root attainment/contact theorem, published structural inequalities or every finite resource row anew. They remain named inputs; the derivations above show their exact use rather than promote source labels to proofs.

## Executed bounded check

Only Python's standard-library `fractions.Fraction` was used. The operative code, run in the reviewer worktree, was:

```python
from fractions import Fraction as F
c,E,S=F(819,2000),F(91,1000),F(1119,1000)
assert S*S>F(5,4)
assert ((E+F(11,2))/5)**2>F(5,4)
rows=[(F(5,4),F(13,5)),(F(7,5),F(117,40)),
      (F(3,2),F(25,8)),(F(8,5),F(133,40)),
      (F(17,10),F(7,2)),(F(7361,4000),F(15,4))]
for r,R in rows:
    lo,hi=0,1000000
    while hi-lo>1:
        mid=(lo+hi)//2; b=F(mid,1000000)
        if (1+b*b)**2>r*r*(1-b*b): hi=mid
        else: lo=mid
    b=F(hi,1000000)
    assert 0<b<1 and (1+b*b)**2>r*r*(1-b*b)
    Q=-R**3+F(3,2)*r*R**2+3*b*R+r*E
    Q1=-3*R**2+3*r*R+3*b; Q2=-6*R+3*r
    L=F(2,5)*(R**2/2+F(1,2)+E)+c*Q1
    L1=F(2,5)*R+c*Q2
    assert all(v<0 for v in [Q,Q1,Q2,L,L1])
    assert F(1,5)-3*c<0
    print(r,R,b,-c*Q,R**3/15+R/5+F(1,2)+c*Q)
cc,x=F(48,125),F(1,36)
assert (2*cc-F(3,4)-(cc+F(1,4))*x
        +(cc*cc-cc)*x*x-cc*cc*x**3)==F(823,4050000)
```

Exit code0; all six rows and the scale identity passed. The exact stdout values are recorded above. This is a bounded rational gate audit, not a Gaussian endpoint evaluation or a support-certificate PASS. No inherited module, native driver, quadrature campaign, remote service or compiler was run by this review.

## Integration recommendation

Accept the finite-support appendix as a **conditional analytic support module**, after its constructor's normal compilation checks. Link the C5 support-method input to `ms:legacy-support:direct` and its complete-H paragraph if helpful, while retaining the six whole-threshold numerical predicates explicitly. Do not replace those predicates with the n27 historical rows, the n≥36 heat-band rows, the n≥47 strip test, or the new n≥42 zero-loss theorem. A concise conditional n=5 instantiation using the checked rational gates above would make the interface more reviewable; it would still not claim numerical completion.
