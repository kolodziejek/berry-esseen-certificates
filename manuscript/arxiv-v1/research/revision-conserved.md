# Promoted conserved identity and phase resource

This revision is based on `ec370aa`, on branch
`manuscript/v2-conserved-20261027`. It edits only the Fourier appendix,
adds `sections/05b-conserved.tex`, and records the bounded checks below.
The reference baseline and all certificate sources are unchanged.

## Mathematical and execution status

| Result | Mathematical status | Execution status |
|---|---|---|
| Contact-slack identity, zero-bias evaluation and compensated hinge inversion | Independently derived here under the displayed fixed-index contact hypotheses, with compact support obtained before higher moments | Exact symbolic coefficient checks passed; no native certificate execution |
| Removing the Gaussian weight | Derived under `C >= C_E`, `n >= N >= 2`, and an established raw remainder ceiling `r_0 < 2N/5` | Exact regrouping checked; a negative control rejects a nonpositive density floor |
| Additional phase-curvature charge | Derived under the preceding hypotheses, `r < 2N/5`, a weighted defect ceiling, and the explicit positive lower bound `0.4095 rho - d_D/15 > 0` | Sign control checked; no particular resource row is accepted by this check |
| Complete LOW/HIGH, confinement and local-comparison composition | Retained supplied analytic and certificate obligations; not newly verified by this revision | No historical checker or generation driver run |
| Manuscript layout | Integration into the reorganized main article is owned by the coordinating task | Full integrated compilation and page inspection pending there |

The two explicit positivity gates clarify the exact scope of the phase
argument. They do **not** discharge the downstream obligation to prove
complete raw remainder bounds and acquire suitable moment/defect inputs.

## Human-readable derivation and notation

The new subsection follows the physical defect and joint geometry. It
starts from one common standardized iid marginal, an actual integer
`n >= 2`, the raw threshold `H`, and the normalized threshold
`z = H/sqrt(n)`. It retains the current law's signed moments. It uses
`h_P` for the deleted-sum survival function and writes `sqrt(n)`
explicitly, avoiding the article's existing reciprocal `h` and moment
coordinate `s`.

The proof proceeds in this order:

1. State the contact polynomial and its equality on the closed support.
   Its positive cubic coefficient gives bounded support before fourth
   and fifth moments are introduced.
2. Evaluate the contact slack over support gaps. The measure interval is
   `[a,b)`: `h_P(a)-h_P(b)=nu([a,b))`. Upper-endpoint atoms must be
   excluded. Absolute convergence of the `J_1`, `J_2` and leakage sums
   is justified before summation.
3. Derive the zero-bias integration identity by signwise Fubini. Apply
   it conditionally to the common marginal and use exchangeability to
   identify the zero-bias sum. This gives the second slack evaluation
   and the contact-weighted truncated first-moment identity.
4. Prove quadratic-hinge inversion for a signed measure of zero mass
   and first moment with finite absolute second moment. Absolute
   Fubini follows from the exact compensated integral
   `pi (x-H)^2/4`; no midpoint convention for a CDF atom is used.
   The signed Gaussian cubic comparator has transform
   `exp(-n t^2/2)(1-i n gamma t^3/6)`. The change from raw to normalized
   hinges contributes the factor `n`.
5. Equate the two slack evaluations. The resulting identity contains
   the score excess, phase cost, physical defect and leakage with their
   original signs and powers of `n`. Both frequency ranges remain in
   the error ledger.
6. Regroup the identity before removing the Gaussian weight. The small
   initial raw ceiling proves positivity of `gamma+3J`; positivity is
   not inferred from `D >= 0` alone. A later weighted defect ceiling
   and the separate positive phase coefficient license subtracting the
   additional quadratic phase price exactly once. The score-excess
   charge remains on the left.

## Preservation and labels

The main subsection has label `ms:conserved`. It retains the original
labels for the contact input and polynomial, auxiliary gap definitions,
both slack evaluations, truncated moment, inversion, conserved identity,
error ledger, raw remainder, unweighting lemma and phase-price formulas.
New labels are `ms:conserved:regrouped` and
`ms:conserved:phase-resource`.

The duplicate proof of the already-present `tau`, `J`, `D` lemma is
removed from the appendix. The coordinator places its old alias
`ms:fourier:afcore:lem:physical-defect` beside the main
`ms:physical-defect` lemma; the new subsection refers to the existing
main definitions. The unique `J_1`, `J_2` and leakage arguments are
fully retained in the main text.

All 212 original appendix labels are accounted for by the retained
appendix, the promoted subsection, or that one main-geometry alias.
There are no duplicate labels in the two owned TeX files. The entire
coefficient atlas from “Signed moments with a common first moment”
through the end of the appendix is unchanged apart from adding leading
zeros to terminating decimals. A navigation paragraph explains the
atlas's sequence; no unique analytic argument is replaced by a
repository pointer. The score-update formula stays in the appendix.

## Reproduction evidence and limits

`runs/manuscript-conserved-v2-20261027/algebra01/check.py` is a new,
standard-library exact Laurent-polynomial check, not an import or wrapper
of the inherited certificate programs. It checks the zero-bias contact
integral, truncated first moment, second slack, conserved identity,
regrouping, original-label accounting and atlas preservation. Its
`stdout.json` reports
`PASS_PROMOTED_IDENTITY_ALGEBRA_AND_PRESERVATION`; `stderr.txt` is empty
and `receipt.json` records Python 3.9.6, return code 0, the relative
command, base revision and SHA-256 hashes of all inputs.

The six deliberate controls concern a wrong hinge-remainder sign,
missing square-root scale, omitted leakage, an incorrectly included
upper-endpoint atom, a loose defect cap producing a negative phase price,
and an initial ceiling producing a nonpositive density floor. All are
detected. `git diff --check` also passes.

These checks establish formal coefficient agreement and preservation;
the surrounding analytic proof supplies the measure-theoretic
justifications. They do not validate the complete Fourier coefficient
atlas, its numerical providers, the finite base, the uniform bridge, or
the global conjecture. The inherited analytic chain remains subject to
the manuscript's explicit conditions. No mathematical completion is
inferred from a fresh symbolic PASS or from the editorial promotion.
