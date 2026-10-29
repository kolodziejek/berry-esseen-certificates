# A combined response for the raw moment polynomial

This is a conditional uniform improvement on one recorded central probability
domain. It bounds all the moment responses in the fixed-target raw remainder
together, retaining the negative fifth-moment response. It does not establish
that a fixed-target maximizing law enters this domain, bound the remaining
Fourier term, or exclude a certificate cell.

The complete proof is [response-proof/response.tex](response-proof/response.tex),
with a four-page standalone wrapper [response-proof/main.tex](response-proof/main.tex).
The exact acceptance program is [response_check.py](response_check.py).

## Exact result

Let P have mean zero, variance one and a central support gap (-A,B), with
A,B>0. Let p=P(X>0), q=1-p, m=E X_+=E X_-, and let V be the conditional
expectation of X given its sign. Write W=X-V, theta=E W², a=m/q, b=m/p.
The law V has variance 1-theta; it is not silently standardized.

Assume the following simultaneous closed-domain bounds for the same law:

| Quantity | Bound |
| --- | --- |
| p | [209/500,21/50] |
| support magnitude | at most 46/25 |
| theta | at most 12657/1000000 |
| rho=E\|X\|³ | at most 214889/200000 |
| beta=EX\|X\| | [72659/500000,174581/1000000] |
| A | at least 810731/1000000 |
| B | at least 284079/250000 |

These are the fields of zero-based CENTRAL row 19; the field N=42 records
the historical acquisition setting. Given the displayed domain, the new
response bound itself holds for every n>=1 and every real raw threshold H.
It does not extend the acquisition statement to n=1 or to another optimizer.

Let c=C_E, varphi=phi(H/sqrt(n)), and let T_c be the entire polynomial part
of the raw remainder, as explicitly displayed in the proof. Thus
R_c(H)=T_c(M(P);J(P),J1(P),J2(P),H,varphi)+E_n(H).
Put sigma=sqrt(10), p_*=(4-sigma)/2, and

```text
D = (3+sigma)rho - gamma - 3J,
B0 = (6+2sigma)(1-theta)^(3/2)(p-p_*)²/sqrt(pq),
E0 = 6m[(A+B)(a-A+b-B)+(a-A)(b-B)],
r = D-B0-E0 >= 0.
```

The proved bound is

```text
R_c(H) <= T_c(M(V);J(P),J1(P),J2(P),H,varphi)
          + c[221/200 + (9/50)|H|] r + E_n(H).
```

The baseline on the right retains the original law's gap integrals. It is
not the raw remainder of V and is not covered merely by the Bernoulli theorem.

## Why this is a common response

The proof uses the two positive measures dmu_±=W² 1_{±X>0}dP. Exact
conditional Taylor identities express the response of every required moment
against these same measures. Product differences are split exactly; for
example rho M4-rho0 M40=rho delta(M4)+M40 delta(rho). The resulting signed
polynomial has degree three in the support magnitude and includes -Q5/4.

The gap-defect budget pays for both sign classes once:

```text
integral k_+ dmu_+ + integral k_- dmu_- <= r,
k_+(x)=(sigma-1)(x+2b)+6B,
k_-(x)=(sigma+1)(x+2a)+6A.
```

Both weights are strictly positive on the domain. The constant response
is bounded by a cubic divided by a positive affine lower cost. Its derivative
numerator is a cubic with negative derivative throughout the domain, so
there is exactly one stationary maximum. Both endpoints and that stationary
point are enclosed with rational arithmetic. Four signed quadratic checks
cover the linear H response. The quadratic H response is nonpositive because
0<=varphi/c<=6/(3+sqrt(10))<1.

One useful analytic ingredient is the same-law gap estimate J1<1. It follows
from the acquired support and

```text
J1 <= E X_+^4/3 + A m B²/2
   < (46/25)(43/40)/3 + (213/250)(119/100)²/4
   = 28828879/30000000 < 1.
```

This uses bounded support before the fourth moment is invoked. Negative
threshold portions of J1 have the favorable sign; the positive outer gaps
and the central gap are treated separately.

## Quantified gain and actual-law control

For comparison, define a particular split-response relaxation at H=0 by
discarding -Q5/4 and taking the positive-class supremum of the remaining
upper polynomial with the same lower cost. Evaluating that relaxation at
x=46/25, b=119/100 proves

```text
K_split >= 173316497/113512320 > 1.52685,
K_combined = 221/200 = 1.105,
K_split-K_combined >= 239426917/567561600 > 0.4218.
```

This is a strict improvement of that specified uniform bound when r>0.
It does not claim that any law realizes the independent bounding endpoints,
or that the result beats every historical coefficient-atlas bound.

The domain is nonempty with positive noise. The rational four-point law
with atoms (-533,-517,717,733)/617 and masses (29,29,21,21)/100 has mean zero,
variance one, and theta=64/380689>0. Its moments and support satisfy all the
displayed domain bounds. This law checks non-vacuity and exact identities;
it is not asserted to be a maximizing witness. Its original gaps differ
from its conditional-mean law's gaps.

## Sources and dependency boundary

All paths below are repository relative; the preserved starting checkout
for this task is 78f0b7c.

| Input | Exact use |
| --- | --- |
| `mathematics/strategy-v4/2026-10-27/excess.tex:267,273,295–306` | Kq, K1 and the complete fixed-target raw remainder; the conserved excess coefficient is n+H², not n. |
| `mathematics/strategy-v4/2026-10-27/geometry.tex:66–113` | Actual-law weighted defect budget, including B0 and endpoint-displacement E0. |
| `mathematics/strategy-v4/2026-10-27/geometry.tex:127–133` | General integration rule for a response divided by positive costs; the present work supplies a concrete response and finite acceptance. |
| `verification/finite-tail/sources/backend.zip`, `finite61/MANIFEST.json` | Manifest path binding and exact archived JSON bytes, read as data only. |
| Archived `work/toward40_20261007/audit43/capsule/work/below49_20261006/acquisition/central42_confinement_candidate.json`, row 19 | Simultaneous selected probability, support and moment bounds. Its acquisition is conditional here. |

The archive SHA256 is
`43b606138f826b47e3f174957088285349aebc82a928627e9e66fe370471be52`;
the manifest SHA256 is
`c8d6228d6a1abd0b25a2f69ed35ae78f1e719a58e27e4fedf5af28e942469cdf`;
the row-file SHA256 is
`2f95d0271996eb9868c2fffcdfb0fa2646a99c2cf588e70d063178e27d07246d`.
Fresh output records the geometry, raw-remainder and checker hashes too.
Hashes establish byte identity, not the acquisition theorem.

| Component | Mathematical status | Execution status |
| --- | --- | --- |
| Exact combined moment response | Locally derived identity for bounded-support laws with a central gap | Exact positive-noise controls passed at ten (H,varphi) pairs; proof is algebraic for all H |
| Uniform conditional bound above | Locally derived using the stated same-law domain and weighted gap estimate | Fresh rational endpoint/stationary and sign checks passed |
| Specified split-bound improvement | Proved rational comparison | Fresh PASS |
| Historical row acquisition and its transfer to a fixed-target optimizer | Conditional; not established by this task | No native acquisition program executed |
| Remaining baseline with actual gaps; signed E_n; nonlinear characteristic-function remainder | Still required | Not discharged |
| Complete cell exclusion or global theorem | Not established | No such acceptance run |

## Reproduction and remaining obstruction

From the worktree root, run without optimization:

```sh
python3 mathematics/fixed-target-v5/2026-10-27/response_check.py
```

`runs/fixed-target-v5-20261027/response02/` contains stdout, stderr, Python
version and return code for the latest checker (3.9.6, return code 0).
The earlier response01 run and its exact checker snapshot are preserved.
The latest four-page proof compiled with TeX Live 2025; response-build03
contains a sanitized receipt, with the full compiler transcript preserved
locally. All four pages were
rendered at 100 dpi and inspected, with no clipping or overlap observed.

The checker rejects a too-small ratio constant, a reversed stationary
interval, omitted sign coverage, a false zero-noise claim for the control
law, and substituting conditional-mean gaps for the original gaps. These
are bounded scalar controls, not a comprehensive verifier-fuzzing campaign.
It also checks a nonzero fifth-moment response in the actual-law example.
No archived code is imported or executed.

The specific unresolved obstruction is the term
T_c(M(V);J(P),J1(P),J2(P),H,varphi)+E_n(H). Conditional-mean replacement
does not identify its gaps with Bernoulli gaps. A linear characteristic
function response does not remove the quadratic and higher terms in
f^n-g^n-n g^(n-1)(f-g), and the present bound gives no high-frequency
decay. Consequently no numerical job, cell, certificate, acquisition gate,
or analytic premise is removed by this result.
