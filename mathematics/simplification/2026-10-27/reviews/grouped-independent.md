# Independent review of the grouped zero-loss support certificate

Reviewed constructor commit: `65c1beb002988a6ceefdfcc2d067def6eedfa80e`. Review performed on the separate branch `simplify/review-grouped-20261027`. This reviewer did not construct `grouped-support.md` or `check_grouped_support.py`.

**Verdict:** no blocking defect found. The14-interval certificate proves the stated new zero-loss support polynomial and whole-ray signs. An independent construction directly in the Bernstein basis matches every one of the672 coefficients exactly; all exceed `1/4`, and all84 ray gates are negative. The original65 support invocations are bound to these14 groups. For this alternative support proof, the old finite support positivity predicates are no longer necessary premises.

This accepts a numerical support component conditional on the contact/heat reduction and the actual preceding resources. It does not accept the full resource acquisition, uniform LOCAL42, BASE41, the conjecture, a production composition adapter, or deletion of an existing certificate.

| Result | Mathematical status | Execution status |
|---|---|---|
| Direct zero-loss infinite-index polynomials encode the original heat/contact envelope | Independently rederived below | No archived code imported or executed |
| Group majorization and closed-interval Bernstein positivity | Independently proved; exact new certificate verified | Fresh submitted PASS plus separate independent direct-basis PASS |
| Both complete exterior rays for every raw threshold | Follows from the reviewed direct derivative bound and strict endpoint gates | All84 exact signs freshly checked |
| All65 source bindings, including ordered LEFT ancestry | Independently checked static identity and input ancestry | Fresh bounded check PASS |
| Actual law satisfies each recorded moment/resource ceiling | Retained acquisition premise | Not established by this run |

## Statement and analytic encoding

At each actual integer `n>=42`, consider an unrestricted attained positive closed maximizing pair `(P,H)` with `C=C_n>=C_E` and `n(C_(n-1)-C_n)_+=0`. For the initial radius and each subsequent LEFT radius, assume the original named contact/heat/moment implications and that the relevant previously acquired resource ceilings hold for this same law. Then the new grouped certificate excludes both closed exterior rays from that radius onward. The same recorded radius applies; the actual conditional noise and defect need not be zero.

The source contact inequality and signed fifth-order reduction are `paper/analytic-supplement.txt:350–410,455–640`; they were independently examined in the preceding support review. The exact finite-source kernel expressions are blobs `09a6e27ef42847cef0ac258504546eaef3a3035e83171143f1c2fd848736ac6c` and `650d7f3617775102fe92977605dfda5fb68a11e0ad738eb799aab77bc4a79e18`. The essential formulas can be rederived without importing either kernel.

Let `u=|t|>=5/2`, `c=819/2000`, `ell=6403124237432/10^12`, and `S=1012121654695/10^12`. Put

\[
A=(u^3-3u)/6,\quad J=u^5-15u,\quad H_4=u^4-6u^2+3,
\quad W=A-J/656,\quad B_2=H_4^2/10496,
\]

\[
E=\frac{51u^6}{590400\ell}
 +\frac{51(3u^2-2)}{39360\ell}+\frac{u}{13448},
\qquad Q=-u^3+\frac32ru^2+3bu+\frac{48r}{5250}.
\]

These are precisely the source infinite-upper-index quantities, with the favorable lower fifth-order term set to zero. The adverse fifth term is `D_+=J/4920`. Since `9B_+^2/4=H4^2/(256*41)=B2`, clearing the positive denominator `W` gives

\[
G=(A/2-J/1640-H_4/(12\ell))W+B_2,
\qquad P=\frac25S^3(AW+B_2)+S^3EW+cQW.
\]

There is no old `.19rSW` predecessor term in `P` and no favorable `D_-=J/(120*47)` term in either polynomial. These are direct zero-loss infinite-index polynomials, not a finite theorem applied outside42–48.

The seven sign requirements `A,H4,J,W,G,-Q,-P>0` have exactly the stated meaning. The `G` inequality gives the source outer-domination condition, conservatively using `H4/(12ell)>=2B_+`; `P<0` gives negative contact after using that condition and `W>0`. Although `E` has a negative constant power coefficient, its displayed summands are nonnegative on `u>=5/2`; hence the outward replacement of `sqrt(41)` by `ell` and the positive-scale replacement by `S` have the proper direction. Both `t` signs and every real raw `H` are covered by the original signed envelope, whose positive/interior, positive/exterior and negative-`t` cases were explicitly checked in the prior independent support review.

The independent program verifies the positive outward constants

`ell^2<41<(ell+10^-12)^2` and `(S-10^-12)^2<42/41<S^2`.

The initial third-moment upper parameter is independently recomputed from the two published bound formulas as `r=7361/4000`. Its chosen `0<b<1` satisfies `(1+b^2)^2>r^2(1-b^2)`. The analytic moment implications remain premises; the outward rational checks are fresh arithmetic facts.

## Why grouping preserves every original call

For one fixed radius, let `r_g,b_g` be the componentwise maxima of all original input ceilings at that radius. Every law formerly covered by an individual call satisfies `rho<=r_g`, `|beta|<=b_g`. It is unnecessary for the two maxima to occur in the same source row or to be simultaneously attained by any law.

Alternatively, for `u>0` and `W>0`,

\[
\partial_rP=cW(3u^2/2+48/5250)>0,\qquad
\partial_bP=3cuW>0.
\]

Thus the grouped contact polynomial is an upper bound for each original one; grouped `Q` also upper-bounds each original `Q`. Positivity of grouped `-Q,-P` implies every required original sign. The other five polynomials are independent of `r,b`. For rays, `Q'=-3u^2+3ru+3b` has the same componentwise direction. These directions would reverse if one were trying to preserve a lower bound for `P`; that is not the claim here.

The independent ancestry check reads the pinned acquisition proof `419ba79a8967665c998602dc421300ae8ee6f5c59901880175b9618f63c27393`, fixed route `df1631620cf1135a5bb6fb9cd28f6c514f6a0451f7c1699ad55054fa1b23dcd0`, and INITIAL source `bd2a808005703ac1fbdb5fb17bc63637f48ebb568f65220f99c47692108a23e0`. It checks the15 coarse cells, eleven surviving parents, five subdivisions per parent, all55 fine cells, strict radius order, no continuation after exclusion, final-resource identity, common first maxima and each later preceding resource. This yields one common plus63 later LEFT calls. Grouping them by their exact rational radius produces:

| Radius | LEFT multiplicity |
|---|---:|
| `5/2` |17|
| `101/40` |5|
| `51/20` |4|
| `103/40` |5|
| `13/5` |4|
| `21/8` |5|
| `53/20` |4|
| `107/40` |4|
| `27/10` |4|
| `109/40` |4|
| `11/4` |4|
| `111/40` |3|
| `121/40` |1|

The additional initial radius `96/25` has multiplicity1, giving65 total invocations. All group maxima, multiplicities and order agree exactly with the submitted `TABLE` at `check_grouped_support.py:19–34`. The source table was parsed as literal syntax, not imported as code.

## Transform proof and independent coefficient construction

The submitted transform at `check_grouped_support.py:54–66` is correct. For `p(u)=sum_i a_i u^i` and `u=l+(h-l)t`, expansion gives

\[
q_j=(h-l)^j\sum_{i=j}^d a_i\binom ij l^{i-j}.
\]

The identity `t^j=sum_(k=j)^d [binom(k,j)/binom(d,j)] B_k^d(t)` follows by cancelling binomial factors and applying the binomial theorem. This gives the submitted forward transform. Expanding `B_k^d(t)=binom(d,k)t^k(1-t)^(d-k)` in powers of `t` gives its inverse

\[
q_j=\binom dj\sum_{k=0}^j(-1)^{j-k}\binom jk\,b_k.
\]

To avoid merely duplicating that implementation, the independent program constructs all seven polynomials **directly in Bernstein form**. The affine coordinate `u` has coefficients `[l,h]`, a constant has degree-zero coefficients, and products use

\[
B_i^m(t)B_j^n(t)
=\frac{\binom mi\binom nj}{\binom{m+n}{i+j}}B_{i+j}^{m+n}(t).
\]

Degree elevation is multiplication by the constant-one coefficient vector of the needed degree. Weighted addition is performed only after degree elevation. Hence no power-to-Bernstein transform or submitted evaluator is imported or reused. Direct scalar formulas and de Casteljau evaluation provide392 further exact consistency checks at the endpoints and two interior rational points; these are implementation diagnostics, not the positivity argument.

For each LEFT group the closed interval is `[R,39/10]`; for the initial group it is `[96/25,21/5]`. The degrees are `3,4,5,5,10,3,11`, giving `4+5+6+6+11+4+12=48` coefficients per group and672 in total. Every independently constructed coefficient exactly equals the fresh submitted transcript and is strictly greater than `1/4`. Since the Bernstein basis is nonnegative and sums to one on the **closed** unit interval, all seven polynomials exceed `1/4` everywhere on their respective closed intervals.

The exact global coefficient minimum is

\[
\frac{168770300272604270966158879019623858439411520950319456559}
{650737668933625093816320000000000000000000000000000000000}>
\frac14.
\]

It occurs at coefficient0 of degree11 `negative_P` for radius `5/2`, so it includes the left endpoint rather than relying on an open-domain margin. No grid of sampled polynomial values, numerical optimizer or floating-point tolerance is used for acceptance.

## Complete rays and strict support

At each splice `U`, the six independently checked signs are

`Q(U), Q'(U), Q''(U), L(U), L'(U), L''(U)<0`,

where `L(u)=(2/5)(u^2/2+1/2+48/5250)+cQ'(u)`. There are84 checks across14 groups. Since `Q'''=-6` and `L''=2/5-6c=-2057/1000<0`, the signs propagate to every `u>=U`.

The direct derivative inequality bounds `|partial_t H_n|` for every `H,t`, and the scale correction is uniform: the cubic after clearing positive factors has endpoint value `118707/42875000>0` at `1/42`, giving `e_n<.384/n<=.384/42`. For each sign `eta`, the derivative of `H_n(H,eta*u)+cQ(u)` is bounded above by `L(u)<0`. Its value at `U` is already negative from the direct grouped polynomial certificate. Both whole rays are therefore strictly excluded. Grouping is harmless here as the grouped parameters themselves are valid upper bounds for each original call.

The bracket multiplying the actual score `C` is at most the negative grouped `Q`; only then is `C>=c` replaced by `c`. The same-owner predecessor loss has nonpositive signed value because its positive part is bounded by the global zero decrement. The contact equality on the full closed support then excludes `|t|>=R`, including boundary atoms and exterior accumulation points. No old coarse ray estimate at4.5 or finite48 support sign is used.

## Evidence, negative controls and limits

Evidence is committed under `runs/grouped-support-20261027/review-grouped01/`:

- Fresh submitted output and empty stderr, with return0 and measured runtime about0.12s.
- Independent direct-basis script, all672 reconstructed rational coefficients,84 ray values, empty stderr, return0 and measured runtime about0.46s.
- Receipt with interpreter version CPython3.9.6, commands, input/script hashes, source commit and output hashes. Neither run enables Python optimization. The independent run uses `-I -B`; the submitted run uses `-B` to permit its explicit import of the new source-binding helper.

The submitted nine rejection controls passed. Independent controls reject a corrupt constant representation, omitted radial prefix, false ray moment cap, changed preceding moment and missing support edge; direct tests also verify `t*t=t^2` in Bernstein coordinates and elevation of the linear function to degree3. In a disposable in-memory copy, deleting every old `minimum_contact`, `scale_positive_gate`, `gate_sha256`, `gates` and `closed_cells` annotation leaves the reconstructed source tuples unchanged. No old certificate bytes were modified. This confirms that historical positivity and radial-cover annotations are not proof premises of the new coefficient construction.

**Findings:** no blocking error in the new certificate or its analytic encoding. The grouped argument strengthens the preceding transfer proof by replacing the old finite sign assumption with fresh exact signs for a zero-loss infinite-index polynomial. The preceding resource bounds and their same-law provenance remain indispensable; the old JSON is used to identify those inputs, not to certify their physical truth.

The reviewed change does not by itself supply the rest of uniform LOCAL42, equality-compatible attainment, the complete finite base, actual provider integration or whole-repository dependency closure. It supplies a small independently checked numerical support certificate that can be composed with those explicitly retained obligations. Existing proofs and certificates should remain preserved.
