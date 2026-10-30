# Local-count revision: derivations and scope

Review target: `sections/08-direct-comparison.tex`, based on commit
`cd10654222f4b63d50f9d8f108597b140d263ec5`. The external model's plan was
treated as a proposal; the two substitutions below were reconstructed from
the manuscript's displayed definitions. No theorem hypothesis or conclusion
was weakened, and no optional Schulz strengthening was added.

| Result | Mathematical status | Execution status |
|---|---|---|
| Global strict-event minorant with alpha=1/2 | Locally derived and checked from the factorization and stationary points | Fresh PASS for exact factorization, rectangle edges and diagnostics |
| E_minus dominates E_plus, one final concave quartic | Locally derived coefficient identity and sign proof | Fresh PASS for coefficient identity, curvature identity and two rational endpoint bounds |
| Exact finite crossing identity | Existing argument preserved and exposed as a lemma; Jensen and boundary explanation added | Source reviewed; no independent full convolution checker added in this component |
| Full comparison over all admissible laws | Original analytical proof retained, with the two proved substitutions | Changed scalar assertions checked; full theorem not proved by this scalar run |

## 1. The small-noise replacement

The retained hypotheses are bounded centered conditional summands
`|U_j| <= A=3/5`, own-count variance `0<t_0<=T_*=101/10000`, and the
existing derivative bounds `99/100<=f'<=101/100` on the central phases.
Independence gives

\[
|E W_k^3|\le A t_0,\qquad E W_k^4\le A^2t_0+3t_0^2.
\]

The sum itself need not satisfy `|W_k|<=A`; the revised text explicitly
distinguishes that point. The polynomial

\[
h(x)=\tfrac45x(1-x)(2x+1)^2
=(-16x^4+12x^2+4x)/5
\]

is nonpositive off `(0,1)`. Its derivative factors as
`(4/5)(2x+1)(-8x^2+4x+1)`; the only stationary point in `(0,1)` is
`(1+sqrt(3))/4`, where the value is `(9+6sqrt(3))/20<1` because
`108<121`. At zero, `h(0)=0`, which preserves the strict outgoing-event
convention. Therefore it is a valid minorant on the whole real line,
including every threshold atom.

Integrate `h(W_k+r)` for `u=-r`, or `h(W_k-r)` for `u=r`, then put
`r=z t_0`. The negative leading term permits the retained fourth-moment
upper bound; the signed third-moment term is bounded below by
`-4 A r t_0/(5 alpha^4)`. The normal correction contributes `-101 r/100`
or `99 r/100`, respectively. Division by positive `t_0` gives exactly the
displayed `F_{1,-101/100}` and `F_{-1,99/100}` with
`alpha=1/2`, `m_h=5/16`. No other small-noise estimate changes.

For fixed `z in [0,3/2]`,

\[
\partial_t^2F=-(12z^2+6tz^4)/m_h\le0.
\]

At `t=0,T_*`, replace `-t^3 z^4/m_h` by the lower bound
`-(9/4)t^3 z^2/m_h`. The resulting quadratic has nonnegative quadratic
coefficient. The negative-phase quadratic has negative largest derivative
at `z=3/2`; the positive-phase one has positive smallest derivative at
`z=0`. Thus the four computed minima suffice for the entire rectangle,
not merely its corners. They are

| Phase | t=0 | t=T_* |
|---|---:|---:|
| negative, z=3/2 | 933/1000 | 3849022385619/5000000000000 |
| positive, z=0 | 156/125 | 3597/3125 |

All exceed `3/5`. The original Cantelli switch, complete incoming series,
normalization correction and final `-lambda/100` margin are unchanged.

## 2. The common large-noise envelope

Retain both sign-specific normal-correction derivations and the original
complete crossing and curvature estimates. Rename only local quantities:
`q_* -> q_min`, `beta_0 -> c_mass`, `J(lambda) -> L_var(lambda)`, and the
fourth-moment envelope `M -> M_4`. These remove collisions with the global
extremal Bernoulli probability, signed second moment and gap functional.

Subtract the displayed error polynomials before any upper replacement:

\[
V_*(E_--E_+)=\frac{7889}{100000}+\frac{1751}{8000}\lambda
+c_{\rm mass}\frac{27M_4}{256}\frac{5\bar c}{4}.
\]

The last term is nonnegative for every `lambda>=0`; the constant is
strictly positive. Hence `E=E_-` bounds either sign. The new single
polynomial `P=W-E/700-lambda/100` is strictly concave: `E` has positive
quadratic coefficient, and direct polynomial differentiation gives the
same negative square-form expression for `W''` as in the original text.
Exact endpoint substitution gives

\[
P(1/100)=\frac{19409025049390417531054861}{8386908849900000000000000000}
>0.002314,
\]
\[
P(7/20)=\frac{16788798784733560132189}{273858248160000000000000}
>0.061304.
\]

Concavity controls the closed interval. Since `E>=0` and `n>=700`, it
gives exactly the old theorem conclusion at every actual index in scope.
The small-noise proof is still needed: `W(0)=0<E(0)/n`.

## 3. Exposition and finite-sum identity

The revised opening explains incoming and outgoing count crossings and the
need for the noise split. The finite summation-by-parts argument is now
Lemma `short:count:crossing-lemma`; the original equation label remains.
The proof explicitly uses `E T_j=j` for Jensen and
`T_0<=na_0<=t<n(1-a_1)<=T_n` for the boundary terms. These follow from
the existing support and threshold assumptions. The nonnegativity of
`g_i` is still proved separately by the original kernel argument. All
five-count omissions are still charged by `E V^4/16`, and the complete
curvature and incoming tails remain present.

All old labels are retained. Added labels are `short:count:minorant` and
`short:count:crossing-lemma`; automatic theorem numbering therefore changes
after the added lemma. The main document should use references, not copied
theorem numbers. The abstract and guide should describe one quartic and
two endpoints; those files are owned by the coordinating agent.

## 4. Fresh reproduction

Command, from the repository root:

```sh
python3 -I -B manuscript/compact-v16/tools/check_revision_count_constants.py
```

Fresh run directories: `count01/` and the final source-bound `count02/` under
`/Users/bkolodziejek/Downloads/BE_Codex_Handoff/runs/manuscript_revision_20261029/`.
It contains `stdout.json`, `stderr.txt`, and `receipt.json` with interpreter,
command, actual return code and input hashes. Python 3.9.6 returned 0 with
status `PASS_REVISION_COUNT_CONSTANTS`. No optimization switches were used.
The checker uses integers and `fractions.Fraction`; it reconstructs the
polynomials and comparisons from their rational definitions.

There are 32 actual finite-law diagnostic events, including centered
symmetric/skew noise, tiny noise, a tiny remote atom, exact zero-threshold
atoms, and sums larger than the individual summand amplitude. These are
diagnostics only. Eight in-memory corruptions are rejected: wrong phase
slopes, an oversized variance rectangle, an oversized summand amplitude,
a positive value at the threshold atom, a positive leading quartic term,
a spoiled endpoint margin and a changed domination identity. The new
checker does not consume a serialized proof-object format. These controls
test its predicates; they are not an independent implementation of the
continuous-domain proof.

Full LaTeX compilation, page inspection, the historical bounded suite,
entry replay and independent review are coordinated separately. This
component does not claim they have already occurred. No finite-base bound
or unrestricted Berry--Esseen theorem is established by this revision.
