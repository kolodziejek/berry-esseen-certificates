# Signed moment bounds before any central gap

The new signwise Cauchy bound reduces the last initial rho cell's K1 cap
from 5.8704858543 to below 3.964267. It requires only centering, unit variance,
the actual support radius 96/25 and the stated rho interval. It uses neither
a central gap nor a small defect/noise premise. A separate existing
fifth-moment inequality improves the same cell's coarse constant A from
10.6950063919 to below 10.406486.

These are coefficient improvements. They do not independently prove a raw
Fourier bound, a conserved-resource bound, initial acquisition, or a local
exclusion. In particular this report does not claim D<4 from these changes
alone. The new phase estimate being investigated elsewhere is a separate edge.

## Statement and proof

The complete three-page proof is [signed-proof/signed.tex](signed-proof/signed.tex),
with standalone wrapper [signed-proof/main.tex](signed-proof/main.tex).
Write rho=E|X|³, beta=EX|X|, gamma=EX³ and
K1=EX|X|³−3beta−3rho gamma/2. For either sign epsilon, put

```text
h=1−epsilon beta >0, delta=rho−epsilon gamma,
C(r)=Rr−3r²/2−3, a(r)=3r/2−R/2.
```

Signwise Cauchy and the support bound prove the universal, same-law inequality

```text
delta >= h²,
epsilon K1 <= C(rho)+3h+a(rho)delta−delta²/(2h).
```

The key point is to retain the *lower* fourth moment on the opposite sign:
E X_-⁴ >= (rho−gamma)²/[2(1−beta)], alongside E X_+⁴<=R(rho+gamma)/2.
The same law also forces delta>=h². No vector of independent moment extrema
is asserted to correspond to an iid distribution.

For rho in [l,u], |beta|<=b<1, h*=1+b, the following three rational gates
give a finite acceptance rule:

```text
h* >= a(u),
3+2a(l)h*−3h*²/2 >=0,
R−3u+3h*²/2 >=0.
```

If they hold, then

```text
|K1| <= R*u−3u²/2−3+3h*+(3u/2−R/2)h*²−h*³/2.
```

The proof maximizes the concave quadratic in delta subject to delta>=h²,
then proves monotonicity in h and rho. Closed endpoints are included. Where
a gate fails, the stronger formula is not used; the general square-completion
bound or an already valid retained cap is used instead.

For the last cell,
l=173303/96000, u=7361/4000, b=32078117/50000000. All gates are positive;
the h-derivative gate exceeds 1.5445. Its exact result is below 3.964267,
so the simpler rational 397/100 is also a valid conservative cap.

## All 24 cells and the constant improvement

The exact table is
`runs/fixed-target-v6-20261027/signed02/stdout.json`. Each row contains
the general new universal bound, all three strong-gate margins, its new
strong bound when licensed, the retained cap and their minimum. The strong
gates pass on rows 10–23 and row 0. Row 0 retains the sharper old bound.
The other rows use the safe general bound and retained minimum. This keeps
coverage intact; rows with a failed gate are not omitted.

| Zero-based row | Safe rational K1 cap | Safe rational A cap |
| --- | ---: | ---: |
| 19 | 3.558417 | 9.102626 |
| 20 | 3.661560 | 9.417692 |
| 21 | 3.763656 | 9.739693 |
| 22 | 3.864593 | 10.069209 |
| 23 | 3.964267 | 10.406486 |

All displayed decimal caps are exact upward-rounded rationals.
The constant improvement follows directly from

```text
0 <= E[|X|³(|X|−rho)²] = M5−2rho M4+rho³,
rho M4/2−M5/4 <= rho³/4.
```

It replaces the old 8rho³/27 contribution in the first unsigned A branch
by rho³/4, retaining the other branch and every other term. This inequality
already occurs in the retained signed implementation at
`mathematics/fixed-target-v5/2026-10-27/cell-sources/local_signed_core.py:122`.
The new work is its earlier unsigned application, not a claim of a new
moment inequality. Validity of the gap coefficient Gamma remains an input
to the A-envelope application.

## Sources and exact evidence

The worktree starts at 43f9f820a981d858181735c533e3d98dcc9eda79. No existing
source or certificate was changed.

| Source | Use and scope |
| --- | --- |
| `mathematics/fixed-target-v5/2026-10-27/cell_check.py:77–118` | Original closed rho partition, elementary moment caps and comparison formulas. |
| `runs/fixed-target-v5-20261027/cell02/check.stdout.json` | Pinned row data; SHA256 `7525713bd06a30b9c13693d01949d4f186890128eed3432771953ef9eafef082`. The new program reconstructs the moment caps rather than treating these bytes as proof. |
| `manuscript/arxiv-v1/appendices/fourier-analysis.tex:1947–1984` | Retained coarse gap estimate and Gamma definition, needed only when inserting the improved fifth-moment term into A. |
| Same appendix `2089–2110,2465–2545` | Retained unsigned K1 and A comparison rules. Their numerical source formulas are reconstructed; they are not silently re-proved by the new scalar run. |
| `mathematics/strategy-v4/2026-10-27/excess.tex:267,273,295–306` | Actual fixed-target Kq, K1 and raw-remainder placement. The contact/transfer and Fourier hypotheses remain separate. |

Run from the repository root, without optimization:

```sh
python3 mathematics/fixed-target-v6/2026-10-27/signed-check.py
```

The new standard-library program imports no archived program and runs no
Fourier kernel. It independently reconstructs all 24 scalar moment caps,
checks the beta cap by the polynomial inequality
(1+b²)²>=u²(1−b²), and evaluates the complete endpoint/vertex and gate lists.
The signed02 directory records stdout, stderr, Python version, source/output
hashes and return code. Python 3.9.6 returned 0 with empty stderr. The preceding
signed01 run and its exact script snapshot are preserved; its 24 row results
are unchanged. The second run adds an explicit support guard to the actual-law
helper and a sparse-tail support-rejection control.

| Component | Mathematical status | Execution status |
| --- | --- | --- |
| Signed Cauchy enclosure and three-gate theorem | Locally derived universal inequalities under stated moment/support hypotheses | Exact 24-cell checks freshly passed |
| Fifth-moment square | Direct identity; existing retained ingredient | Exact sharp control passed |
| Scalar insertion into old A and minimum with old K caps | Conditional on retained coefficient inequalities | Fresh exact reconstruction and comparisons passed |
| Fixed-target witness support and Fourier/resource consequences | Separate analytic and numerical obligations | Not accepted or run here |

Negative controls reject reversed rho endpoints, an invalid beta cap,
the too-small last-cell target 3.96, missing coverage, forcing the failed
monotonicity gate on row 1, the false sign premise beta gamma>=0, and a
standardized sparse-tail law outside the acquired support.
These are bounded controls, not exhaustive malformed-proof testing.

Actual-law controls include symmetric and skew Bernoulli, the sharp law on
{-46/25,0,46/25}, and a three-point law at
(-96/25,-1/2,37/25) with masses (325/22211,11708/16533,3650/13167).
The last law lies in the final rho cell and has beta>0, gamma<0 and K1<0.
It disproves both beta gamma>=0 and K1 gamma<=0 as universal sign shortcuts
on that cell. It is not asserted to be an extremizer or a counterexample to
Berry--Esseen.

The proof was compiled and rendered separately. Build receipts record its
source hashes, diagnostics and visual inspection. None of the execution or
layout evidence establishes missing analytic acquisition or Fourier premises.
