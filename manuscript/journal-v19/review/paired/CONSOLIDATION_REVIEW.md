# Paired Fourier consolidation

The proposed change is fully justified at the previous domains and numerical
constants. It combines the two Gaussian-norm derivations, proves the positive
Pearson rectangle as a corollary of one shared envelope, and removes the local
copy of the triangle Pearson proof already present in the Fourier chapter.
No analytic step is moved outside the paper and no native target is changed.

The controlled whole-paper comparison is **102 pages before, 101 after**.
This is a modest, genuine improvement in organization and length. It does not
provide a route to a sixty-page paper by itself.

## Exact integration instructions

Only the following two substitutions are needed. The current v18 source is
unchanged; `baseline/` and `candidate/` are disposable text-only work copies.

1. In `sections/local.tex`, replace from the unique marker
   `\subsection{Paired Fourier cancellation}` up to, but excluding,
   `\subsection{Confinement from the remaining defect budget}` with
   `replacement.tex`.
2. In `sections/fourier.tex`, replace from the unique sentence
   `In the selected enclosure one has actual support` up to, but excluding,
   `\subsection{The complete high-frequency half-line}` with
   `fourier-envelope-replacement.tex`. This adds the shared label
   `j:fourier:pearson-envelope`, retains its full proof, and explicitly names
   the exact native `Z_0` and `Z_r` values. It does not replace them by a
   larger unproved minimum or a tighter value requiring new acceptance.

All seven existing labels in the local replacement range are retained.
The order of numbered statements changes; use labels, not hard-coded numbers.
The supporting `prepare_comparison.py` is create-only, and checks label
preservation and byte integrity of its v18 input. `PREPARATION.json` records
the initial preparation; the final text and validation hashes are in
`FINAL_MANIFEST.json` because subsequent corrections included a normalized
moment premise and a two-line display layout.

## Source-to-target mathematical proof

The shared Pearson proof starts from the actual normalized marginal and
`Q=X^2-gamma X-1`. The nonnegative measure `Q^2 dP` gives the signed bounds

`-Q_R(t) <= 120 z <= P_R(t)`, where `t=|gamma|` after auxiliary reflection.

The coefficients of the unknown fourth moment are `R-2t` and `R+2t`.
The existing radius condition makes both nonnegative before substituting its
upper bound. The two native quadratics dominate these cubics because their
residuals are exactly `t^2(g-t)` and `t^3`. Their clipped vertices and the
separate radius-six derivative test therefore give literally the previous
`Z_r` and `Z_0` branches. All these details remain in the Fourier chapter.

For the positive rectangle, Pearson's lower bound `mu4>=1+t^2` gives the
fourth-coefficient and product-coefficient endpoints. The derivative of the
lower fifth coefficient is `10-2M+2Rt+3t^2>0` on the retained `M<3` domain.
The sixth-moment identity has a nonnegative kernel; bounding each factor by
the same row's radius and moment ceilings yields the native sixth-moment
bound. The old `M<=2` choice is a specialization, not another theorem. The
damping constant changes from 43 to `45-M` when necessary.

For the Fourier estimate, the only new leading quantity is the convex norm
`J(z,c)=integral exp(-x^2/2)|zx^2-cx^4| dx`. Its rectangle maximum is at
corners because the exact norm is convex. The manuscript now computes its
split integral once. Finite integration-by-parts recurrences for positive
Laplace integrals prove the alternating Mills bounds, including the parity
choice 11/12. No limiting continued-fraction theorem is used. Negative
Gaussian coefficients still consume a lower enclosure for `sqrt(pi/2)`.

The leading sine/cosine remainder and the Gaussian moment recurrence give
the unchanged coefficients `35/48`, `35/24`, `1`, `5/2`. The common Taylor,
power and signed Gaussian comparator proofs remain in Proposition
`j:fourier:low`; the two 251 constants and the entire `L_2` expression are
unchanged. Positive decreasing index factors retain uniformity when the
marginal and threshold vary with the index.

The actual lower third-moment bound is still derived from the conditional
cubic identity, not from an unsupported inequality `rho>=rho_B`. Its result
is retained in every downstream score corner, curvature, budget and signed
fourth-moment error. The actual contact orientation is never reflected.

## Native-expression correspondence

`NATIVE_MAP.json` pins the complete inspected files and relevant AST bodies.
The sources are read-only representatives of the selected formula families,
not a claim to have enumerated every repeated source copy.

| Native expression or gate | Replacement and retained justification |
| --- | --- |
| `kernel.sixth`, identical in `contracted_kernel.sixth`: radius-six `z` branches | Shared `Z_0`, with the same `M<=5`, derivative-at-`g`, and `M>5` cases. |
| `r0=max(RADIUS,2*g)`, `tg`, `zr`, then `min(z,zr,eta+10*g)/120` | Shared `r_0`, clipped `t_*`, `Z_r`, and the identical minimum in `j:local:fourier:z0`. All positive denominators remain licensed. |
| `a`, `e`, `B`, `a0`, `b0`, `c0`, `c1` in `sixth` | Existing triangle LOW theorem and the common Pearson recipe; `c1=c0/2` remains allowed there. |
| Original `paired`: `rBmax`, variance-reserve gate, `rmin` | Final conditional-cubic paragraph. The original nonnegative reserve gate sets the possible downward correction to zero. |
| Extended `paired`: `reserve`, `rbmin-reserve*theta`, and `max(1,...)` | Exactly the new paragraph's `r_*`. Its conclusion also covers the original zero-reserve special case. |
| `gl=max(0,SL*rmin-3-d, gamma_conditional)` when the conditional enhancement is present | The positive rectangle accepts any previously proved lower bound `gamma_l`. The defect and conditional cubic lower bounds remain in the preceding acquisition atlas. No stronger `gl` is inferred by this replacement. |
| `tstar`, `sig`, `Z`, `zl`, `zu`, `cl`, `cu`, optional `3*g*g<=2` improvement | Literal displayed formulas in `j:local:paired-rectangle`, with the same support and moment gates. |
| Nested `J` in all three inspected implementations | Identical ASTs. The exact opposite-sign case, zero case, `old` bound and finite Mills `improved` bound are all retained; the mathematical text does not weaken native nonnegativity/domain assertions. |
| `lc`, `lh`, `m6`, `e`, `B`, `l2` | `j:local:fourier:paired` and the positive rectangle; exact constants and outward directions are unchanged. |
| `b0=43(1-2/n)/96` versus `(45-M)(1-2/n)/96` | Both are explicitly distinguished. The former is licensed only for `M<=2`; the extended `M<3` implementation uses the latter. |
| `paired_eligible` | The same probability interval, radius, fourth moment, gamma, conditional variance and rectangle-order conditions remain necessary. The replacement supplies no acquisition merely from eligibility. |

The original tail source's radius condition `RADIUS>g` is supplemented by its
global radius lower bound 2.3 and `g<=1`; hence it also has `RADIUS>2g`.
The contracted and extended sources check this condition explicitly.

## Validation and limitations

- `paired_algebra02/PROCESS.json` records a real exit 0 with empty stderr.
  Its exact rational polynomial audit verifies eleven identities, the four
  Gaussian coefficients, eight rejected changed identities, and the strict
  failure of the old 43 damping value at `M=5/2,N=47`. This is bounded algebra
  evidence, not an independent proof of integration or native coverage.
- Baseline and final candidate builds used the same copied full project and
  typography. The final candidate has 101 pages, zero undefined references,
  zero overfull boxes, and one benign underfull paragraph elsewhere in the
  local chapter. Baseline has 102 pages. Both actual compiler exits are 0.
- Candidate rendered pages 24, 75, 76 were visually inspected. The revised
  shared Pearson display and the complete replacement fit without clipping
  or overlaps. No essential proof has been relegated to a supplement.
- No native integration, certificate discovery, or old acceptance campaign
  was rerun. Published inputs and all prior numerical dependencies remain.
  The improvement is a rigorous textual consolidation, not a new theorem
  or a formal verification of the manuscript.

Paths beginning `paired_` in this section are under
`runs/certificate_consolidation_20261104/`.
