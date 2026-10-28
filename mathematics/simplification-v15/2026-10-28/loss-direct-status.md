# Direct five-count loss: v15 status

The selected result is a variance-proportional lower bound for five actual crossing losses. It removes the additive displacement error in this part of the argument. No manuscript, existing certificate or prior proof was changed.

| Result | Mathematical status | Execution status |
| --- | --- | --- |
| Pointwise kernel minorant \(h(x)\ge(2/5)\sin^2(\pi x)1_{[0,1]}(x)\) | Locally derived with full proof | Scalar gates freshly checked |
| Regrouped four-replacement comparison | Locally derived; centering and disjoint translates explicitly required | Actual convolution controls freshly checked |
| Five-count reserve and seven index-dependent constants | Locally derived and checked; independent review pending | Fresh PASS |
| Complete signed CDF comparison | Separate composition obligation; not proved by this component alone | Not claimed here |

## Exact statement

For centered conditional laws

\[
-.6\le U_0\le a_0,\qquad -a_1\le U_1\le.6,\qquad a_0+a_1\le.072,
\]

let \(n\ge42\), \(p\in[.4,.53]\), \(\lambda=n(qEU_0^2+pEU_1^2)\le.36\), and \(|t-np|<.94\). Put \(k=\lfloor t\rfloor\), \(a=1-5/n\), \(b=1+3/n\). The local crossing losses of the same actual law satisfy

\[
\sum_{i=k-1}^{k+3}g_i(t)\ge\frac25\left\{
\frac{1-e^{-3a\lambda}}2
-\frac{(9/25)b\lambda+3b^2\lambda^2}{16}
-\frac{10\pi^2\lambda}{n}\right\}.
\]

Consequences, each uniform in all smaller nonnegative noise:

| Minimum \(n\) | Lower coefficient of \(\lambda\) |
| --- | --- |
| 125 | 1/250 |
| 150 | 1/20 |
| 200 | 1/8 |
| 250 | 1/6 |
| 300 | 19/100 |
| 400 | 9/40 |
| 500 | 6/25 |

The raw threshold \(|H|\le1.84\), with \(t=np+H\sqrt{pq+\lambda/n}\), automatically gives the required displacement. All phases and closed threshold collisions are included. Zero noise requires no limiting argument. No support-gap budget, \(d\le3/n\), equality of conditional laws, or independence at a selected count is used.

## Why this is different from the previous transport bound

The compact sine-square bump is continuously differentiable, with derivative Lipschitz constant \(2\pi^2\). Comparing centered summands therefore costs \(\pi^2(s_0+s_1)\), rather than their first absolute moment. Before applying this bound, the two positive and two negative count changes are regrouped into four replacements of sums of disjoint translated bumps. These sums retain the same derivative bound.

The frozen sum has \(n-1\) actual independent summands and variance in \([(1-5/n)\lambda,(1+3/n)\lambda]\). Its first characteristic function gives the positive reserve. The omitted translated bumps require frozen noise outside \([-2,2]\), so one fourth-moment estimate supplies their entire tail. The resulting lower bound already concerns five local losses: multiplying by their minimum binomial mass restores the weights without an additional remote-count argument.

Proof: loss-direct.tex; compiled four-page version: loss-direct.pdf.

## Dependencies and limits

The new reserve uses elementary calculus, moment identities and characteristic functions of bounded variables. The proof includes the kernel's nonnegativity; it needs no external probability theorem or finite certificate. Joining it to \(t-EK\) or to the actual CDF uses the exact v13 crossing identity and its closed-lower/strict-upper event conventions.

This is not a complete Berry–Esseen proof or a claim about unrestricted \(n<125\). It does not pay the binomial curvature or normal interpolation errors by itself. The coordinator's signed-comparison composition is a separate claim requiring review. No certificate deletion follows solely from this local theorem.

## Fresh evidence

Replay from the worktree:

    python3 -I -B mathematics/simplification-v15/2026-10-28/loss-direct-run.py NEW_RUN_ID

Final receipt: runs/loss-v15-20261028/check02/receipt.json. Result: PASS, 519 exact checks, 97 actual finite-law/threshold cases, five negative controls, 0.849 seconds under Python 3.9.6. The previous check01 also passed; check02 binds the expanded explicit proof of global kernel nonnegativity.

The actual controls reconstruct independent conditional convolutions directly. They include zero noise, symmetric noise, tiny symmetric noise, each rare-jump variance-allocation endpoint, unequal four-atom marginals, \(\lambda=.075,.36\), and actual atom collisions, at \(n=42,125,200\). At \(n=42\), local kernel expectations are separately compared with the stop-loss telescoping formula. These tests support the analytic proof; they are not continuous-domain coverage.

Negative controls explicitly reject:

1. Removing centering from the smooth replacement estimate: a nonzero constant increment and the affine test function already contradict it.
2. Treating overlapping bump translates as disjoint: the multiplicity is two, so the unchanged derivative bound cannot follow from that argument.
3. Removing the conditional diameter premise from characteristic-function contraction: \(Z=\pm1/2\) has modulus one at frequency \(2\pi\) despite positive variance.
4. Deleting the omitted-translate term: at \(u=1/4,V=5/2\), the omitted \(j=-3\) bump equals \(1/2\).
5. Claiming the same crude coefficient is positive at \(n=42\): even its optimistic linear reserve loses to the replacement term. This rejects that inference, not the existence of another bound at \(n=42\).

Final source SHA256: a63ffae381844c45559f6637fc62ce0312d847109b2fc9cd1c3f0d6257bff0c9.
Checker SHA256: c71b195c6c8c67334e17e16740e85738e67a6f916fcc212d7b6589606fb303d5.
Runner SHA256: 5978ff54d0a585a954b2ba56b5244719952138620f699e0901080af4f79492aa.

Build01 compiled successfully without warnings. All four rendered pages were inspected. No dense search or certificate-generation campaign was run.
