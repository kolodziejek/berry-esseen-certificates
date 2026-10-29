# Geometry and acquisition revision review

Review target: `cd10654222f4b63d50f9d8f108597b140d263ec5`, revised in the local `manuscript/revision-v16-20261029` branch. External advice: `/Users/bkolodziejek/Downloads/manuscript_revision_plan.md`, Sections 5.1–5.3. This note records a reconstruction of those proposed substitutions, not independent validation of the entire inherited entry/contact chain.

## Status and unchanged scope

| Change | Mathematical status | Execution status |
|---|---|---|
| Joint defect budget, with the old simultaneous-gap inequality as a corollary | Locally derived from the gap integral bound and conditional centering; valid for the original standardized finite-third-moment domain with a positive central gap | Actual finite-law identities freshly checked; these examples are diagnostics, not the analytic proof |
| One-endpoint probability exclusion | Locally derived from the unchanged reduction `D >= Q(p)/sqrt(pq)` and the exact location of `p_*` | Fresh PASS for the new rational surplus and root brackets |
| Two contact rays by monotonicity | Conditional on the retained contact upper expression and all-threshold heat/derivative estimates; same two rays and same strict endpoint conclusion | Fresh PASS for all six advertised boundary inequalities, both radius conditions and constant second derivative |
| Acquired conclusions `3/8<p<93/200`, `theta<.0036`, `d<.004`, `ell>1.996`, `rho<9/8`, `.066148<beta<.2527`, `lambda<.35` | Original proposition hypotheses and conclusions preserved; compact support retained | Unchanged acquisition driver is left for the coordinator's bounded replay |

No theorem about the finite base or the full conjecture is added. The two-ray step still requires fixed-target attainment, nonnegative excess, and the sharp predecessor. The geometry proposition continues to require compact support. The broader scope of the geometric corollary is retained: finite third moments already suffice for the gap integrals and conditional-cubic identities.

## Reconstruction of the shared budget

For the central gap `(-A,B)`, put `M_{j,+}=E X_+^j`, `M_{j,-}=E X_-^j`, `m=E X_+=E X_-`, and `J_o=J-m(A+B)^2`. An outer positive gap `(a,b)` has `a>=B` and

`(b-a)^2 <= 2 integral_a^b (t-B) dt`.

Summing with its constant nonnegative `tau` value, and then applying Tonelli, gives

`J_o^+ <= E[X_+(X_+-B)^2] = M_{3,+}-2B M_{2,+}+B^2 m`.

The negative side is identical in magnitudes. Substitution into `D=(3+sqrt(10))*rho-gamma-3J` yields

`D >= (sigma-1)M_{3,+} + (sigma+1)M_{3,-} + 6B M_{2,+} + 6A M_{2,-} - 6m(A^2+AB+B^2)`.

Writing `bar A=ell p`, `bar B=ell q`, `W=X-E(X|B_0)`, conditional centering gives

`M_{2,+}=m bar B+E[W^2;X>0]`,

`M_{3,+}=m bar B^2+E[(X+2 bar B)W^2;X>0]`,

and the analogous negative formulas. This follows directly by writing `X=bar B+W`, expanding the square/cube, and using `E[W;X>0]=0`.

With `A=ell(p-a0)`, `B=ell(q-a1)`, `d=a0+a1`, `m=pq ell`, the constant part is `ell*w*Q(p)` plus

`6 ell*w [q(q-a1)+p(p-a0)-(p-a0)^2-(p-a0)(q-a1)-(q-a1)^2+pq]`

`=6 ell*w [d(1-d)+a0*a1]`,

where `w=pq ell^2`. The two remaining kernels are exactly those in the new `ms:joint-defect-budget`. Their integrands grow at most cubically in `|X|`, so the finite third moment justifies their expectations, including for unbounded support. Gap sums use monotone convergence; atoms at gap endpoints do not change any Lebesgue integral.

On the positive support, `X>=B` and `bar B>=B`, so the positive kernel is at least `3(sigma+1)B`. On the negative support, `-X>=A` and `bar A>=A`, giving `3(sigma+3)A`. These two estimates recover the original `ms:simultaneous-gap-formula` verbatim. Its source label is preserved; it is now a corollary of the more informative lemma.

The `short:acq:budget` display remains as convenient notation for the same inequality, but its duplicate derivation has been replaced by a reference. The `mu_+` and `mu_-` notation is explicitly described as variance-weighted expectations of the actual law.

## Probability exclusion

After the unchanged `d` and `theta` monotonicity arguments, `D>=Q(p)/sqrt(pq)>=2Q(p)`. The exact brackets give

`3/8 < p_* < 21/50 = (3/8+93/200)/2`.

For `p<=3/8`, its distance from `p_*` is at least the left-endpoint distance. For `p>=93/200`, the right-endpoint distance is strictly larger than the left-endpoint distance, because the midpoint lies to the right of `p_*`. Hence both outside rays have `Q(p)>=Q(3/8)`. Since `Q` increases in `sigma` with coefficient `p^2+q^2>0`, the rational lower replacement is valid and gives

`Q_-(3/8)=37936011/1600000000`,

`Q_-(3/8)-47/2000=336011/1600000000>0`.

This contradicts `D<.047` on both rays, including their boundaries. The discarded ratio-monotonicity and right-endpoint calculations are no longer needed. The earlier bootstrap `.36<p<.48` is preserved because subsequent derivative signs rely on it.

## Rays and strictness

The revised proof evaluates only `h+c0 Q_b`, `L=g+c0 Q_b'`, and `L'` at each boundary. The checker reconstructs all functions from their rational definitions. Exact values are saved in the fresh stdout JSON. The advertised conservative upper bounds are

| Quantity | Negative ray, `t=19461/10000` | Positive ray, `t=113273/50000` |
|---|---|---|
| `h+c0 Q_b` | `<-2/5` | `<-13/100` |
| `L` | `<-1` | `<-8/5` |
| `L'` | `<-13/5` | `<-16/5` |

`L''=2/5-6*(819/2000)=-2057/1000`. Thus `L'` and then `L` stay negative for every larger magnitude. As `g>0`, `Q_b'=(L-g)/c0<0`. At each boundary `t^2>3` implies `h>=0`, so the first test implies `Q_b<0`; that sign persists outward. Therefore replacing `CE` by its lower bound `c0` in each negative product is justified both at the boundary and in the derivative estimate. The actual contact upper expression starts negative and decreases. This proves exclusion of the entire closed ray, including its boundary atom, for every raw threshold admitted by the retained heat estimate. The absolute-value majorant `h` is not differentiated.

## Fresh evidence and controls

Command from the repository root:

```sh
python3 -I -B manuscript/compact-v16/tools/check_revision_geometry_constants.py
```

Fresh run directory:

`/Users/bkolodziejek/Downloads/BE_Codex_Handoff/runs/manuscript_revision_20261029/geometry02/`

It contains `stdout.json`, `stderr.txt`, and `receipt.json`, recording the command, interpreter version, UTC time, return code, source hashes and output hashes. Return code was 0 and the result was `PASS_REVISION_GEOMETRY_CONSTANTS`.

The new check includes 14 rational comparisons, 11 actual-law diagnostics, and 5 rejection controls. The laws cover symmetric and skew Bernoulli, a rational probability close to `p_*`, both probability boundaries, three/four-point laws, several outer gaps with strict slack, a tiny remote atom, an exact atom collision, and nearby four-point atoms. They are centered exactly and the homogeneous cubic budget is checked before dividing by the positive variance power. The separate `sqrt(10)` coefficient cancels identically in each diagnostic comparison.

Rejection controls deliberately request an invalid probability target, reverse the ray-curvature sign, inflate a support-gap sum, omit probability mass, and put an atom at zero outside the central-gap domain. These test the specified predicates; they do not claim to be mutation tests for the untouched entry certificate.

The program does not import any inherited checker. It uses Python integer arithmetic and `fractions.Fraction`; no floating-point evaluation or sampling establishes a continuous-domain conclusion. No source pins or historical results were changed.

## Remaining integration work

The coordinator should independently read the displayed proofs, run the combined historical bounded checks plus the new scalar check, and compile/inspect the revised document. The exact run above binds the source bytes as they stood before any later relocation or prose edits by the coordinator. Such edits require a final source-bound replay. No independent audit of the entire inherited entry/heat theorem or missing finite base is claimed here.
