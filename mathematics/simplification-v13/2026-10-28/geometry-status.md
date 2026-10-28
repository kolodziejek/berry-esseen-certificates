# An inward-moment noise budget

The selected result is the four-page [proof](geometry-noise.pdf), with
[source](geometry-noise.tex). It improves geometry before any count comparison.
It does not close the remaining count range or prove the full conjecture.

For one actual centered variance-one law, let `p=P(X>0)`, `v=p(1-p)`,
`X=ell(B+U-p)`, `E(U|B)=0`, `s=E U^2`, and `lambda=n s`.
The inward endpoint displacements are `a0,a1`, with `a0+a1<=dbar<1`.
The theorem retains the physical variance allocations
`lambda0=n(1-p) E(U0^2)` and `lambda1=n p E(U1^2)`.
Its new cost is

    n D >= [n v Q(p) + lambda0 Y0(p) + lambda1 Y1(p)]/(v+lambda/n)^(3/2),

with the explicit square-root functions `Y0,Y1` in the proof. The essential
step is the elementary one-sided inequality
`E Z^3 <= a E Z^2 - (E Z^2)^2/a` for centered `Z<=a`.
Combining its reciprocal cost with inward displacement by AM–GM yields
coercivity without any outer support radius. The zero-endpoint case is
handled by degeneracy, never by division by zero.

## Scope and status

| Result | Mathematical status | Execution status |
|---|---|---|
| Common-law allocation budget | Locally derived for compact support and an actual central gap, including countably many outer gaps; no contact/predecessor premise in this algebraic theorem | 832 exact budget controls on 208 original and 208 reflected positive-noise laws; 14 exact Bernoulli identities |
| Four noise ceilings below | Complete analytic reduction to eight polynomial inequalities on closed intervals; independent coordinator review pending | Fresh PASS: 22 rational scalar gates and 139 positive Bernstein coefficients on 11 closed polynomial intervals |
| Six sample-size ceilings and near-critical localization | Locally derived from monotonicity in noise and sample size | Fresh positive rational comparisons, including the `23/(20 sqrt(n))` gate |
| Geometric obstruction at `p=.3, lambda=.1` | Actual three-point standardized law; shows these necessary data cannot finish all left cases | Exact moment, atom, gap, support and budget checks PASS; `26<nD<27` |
| Quantitative Bernoulli-gap scope | External theorem is used only in its stated range; see proof section 3 | Its published counterexample to unrestricted extrapolation reproduced with an explicitly reused, source-pinned rational-normal kernel |
| Full count comparison, acquisition, finite base, full conjecture | Not established here | No new Fourier replay, count campaign, finite-base acceptance or formal proof |

Given the retained acquired inputs
`n>=42`, `p in [.25,.54]`, `d<=.068`, `lambda<=.616`, and
`nD<=32.20665378`, the consequences are:

| Probability range | New strict noise ceiling |
|---|---|
| `[.25,.30]` | `lambda<1/6` |
| `[.25,1/3]` | `lambda<1/4` |
| `[.25,.40]` | `lambda<8/25=.32` |
| `[.25,.54]` | `lambda<9/25=.36` |

| `p` at most | `.30` | `1/3` | `.35` | `.375` | `.39` | `.40` |
|---|---|---|---|---|---|---|
| Integer `n` at most | 84 | 168 | 262 | 657 | 1530 | 3598 |

In particular all acquired witnesses below `p=1/3` have `42<=n<=168`;
all with `p<=.4` have `42<=n<=3598`. The exact full allocation budget can
also be retained instead of discarding allocation to obtain these ceilings.

## Dependency changes, with reasons

- The incoming numerical premises are the v10 direct geometric output:
  [geometry.tex lines 85–106](../../simplification-v10/2026-10-28/geometry.tex).
  Its coarse entry, actual central gap, compact support, and upstream
  contact/predecessor/acquisition obligations remain. We do not regenerate
  or certify that ancestry here.
- The raw expansion is rederived from the outer-gap integral in
  [geometry.tex lines 49–81](../../simplification-v10/2026-10-28/geometry.tex).
  Its conditional cubic terms are retained and improved. No old iteration,
  `.6/.7` outer strip, heat/ray estimate, Bernoulli theorem or count bound is
  an input to the new geometric inequality or noise ceilings.
- Count calculations at `lambda>=.36` are unnecessary for witnesses satisfying
  the acquired inputs. On `p<=.4`, the same holds already at `lambda>=.32`;
  the smaller probability ranges have the stronger table entries. This is
  because their necessary geometric budget already exceeds its acquired
  upper bound. It is not a theorem about arbitrary iid laws.
- Count calculations with `p<=.4` and `n>=3599`, or `p<=1/3` and `n>=169`,
  are unnecessary under those same inputs. These exclusions are uniform
  interval arguments, not sample-size grids.
- For the previously completed v12 scopes, the remaining count gaps narrow
  to `.01<lambda<.32` on `[.25,.4]` and `.075<lambda<.36` on `[.4,.53]`,
  subject also to the sharper probability/allocation budget. Those gaps
  are still open. The geometric theorem also covers `p in (.53,.54]`; it
  does not provide count comparison there or replace the acquisition that
  narrows probability to the selected count domain.
- Signed/reflected acquisition is unchanged. The algebraic theorem can be
  applied to a reflected law using that law's actual `p`, cubic moment and
  variance allocations; it does not establish reflection/attainment itself.
  The independent finite base through 41 remains an obligation.

The explicit obstruction has `n=42`, `p=3/10`, `U1=0` and centered
`U0` on `{-3/5,5/882}`. Its `lambda=1/10`, `d=5/882`, and standardized
law satisfy the retained support, moment and geometric bounds. No maximizing
contact or nonnegative excess is claimed. Thus the new method removes large
regions but cannot finish the left range from these necessary data alone.

## Evidence and reproduction

From the checkout root, with assertions enabled:

```sh
python3 -I -B mathematics/simplification-v13/2026-10-28/geometry-noise-check.py
python3 -I -B mathematics/simplification-v13/2026-10-28/geometry-noise-actual.py
```

Final source-bound runs are `runs/geometry-v13-20261028/scalar03/` and
`actual03/`; each preserves command, interpreter, input/output hashes,
stdout, stderr and return code. The actual-law checks include tiny noise,
zero-noise degeneracy, pure and balanced allocations, both signs, endpoint
probabilities and actual gap weights. Two generated laws outside the inward
cap are explicitly recorded as excluded controls. They are not accepted
instances of the capped theorem. Algebraic reflected controls may have
probability outside the acquired interval; their scope is recorded.

Negative controls retain the failure of a square-root tangent as a lower
bound, unrestricted-noise monotonicity, deletion of the positive term in
the one-sided cubic inequality, the two geometric overclaims, and
unrestricted extrapolation of the sharper Bernoulli formula. The last
uses the pinned v10 rational-normal implementation openly; it is not a
second independent implementation of that helper.

`discovery01/` preserves an earlier variance-cap candidate and the selected
AM–GM prototype, including a prototype probability endpoint `.53` before
the accepted `.54` extension. These are diagnostics, not acceptance.
The final acceptance constructs every coefficient from the theorem;
it reads no discovery object or fitted certificate. Earlier scalar/actual
runs remain preserved and are superseded only for final source binding.

The final build and visual-review receipt are in `build03/`. The first build
had one long inline display; the later source only reformats it and makes
the integer-index convention and countable-gap passage explicit. No
manuscript, original proof, original certificate, external repository or
main branch was edited.
