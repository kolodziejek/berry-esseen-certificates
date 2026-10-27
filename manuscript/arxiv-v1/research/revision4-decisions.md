# Fourth round: new proof routes and conservative manuscript edits

Start: fork main `ca4943aae7a85ffa85d5d4d7166987dc055cb3e6` (PR #4 merged).
Reference baseline: `6346fc1b4432bc5982822aa696eb566ed9e1e1ee`.
Branch: `manuscript/strategy-v4-20261027`, with separate excess, discrete,
unification and independent-review branches. Earlier PRs #1–4 are merged;
historical statements that they are still draft are superseded by this note.

The user asked for a genuinely shorter, complete and readable argument.
We assessed the Astra, Opus and Argon attachments as proposals. The full
decision and dependency map is in
`mathematics/strategy-v4/2026-10-27/README.md` and its linked audits.

## Changes in this manuscript

1. `sections/03-smoothing.tex` adds a general first-failure formulation
   with monotone predecessor allowances. It retains the real deletion
   and index gates and does not assert a new floor or finite base.
2. `sections/05-geometry-counts.tex` proves the moment circle and the sharp
   one-parameter gap inequality with only a finite third absolute moment.
   It explains the defect as a sum of moment and gap losses. The endpoint
   decomposition and simultaneous quantitative stability proof are retained.
3. `sections/06-resources.tex` and `appendices/fourier-analysis.tex` reference
   those shared inequalities instead of repeating the same proof. Weighted
   index bounds, signed terms and the downstream resource hypotheses remain.
   References were updated; the shared resource theorem keeps its alias.

These edits remove genuine duplication and simplify a foundational proof.
They do not replace the finite-index Gaussian estimates with a weaker bound
or hide the Fourier derivations. The revised paper remains 158 pages; no
arbitrary page or line target was imposed.

## Separate 14-page companion

The new `mathematics/strategy-v4/2026-10-27/main.pdf` develops the fixed-target
excess route, the weighted common noise measure, the binomial margin and the
fixed-law finite contact test. It includes the compensated inversion proof
used in the new derivation. It explicitly lists the scalar and local-exclusion
premises that are not proved by changing the extremal problem.

The new conserved identity has `(n+H^2)a`, not `na`, as its exact excess term.
The conditional transfer proof can remove the old entry recurrence for a
new zero-barrier tail argument, but does not remove its finite-base consumers.
We therefore retain the existing manuscript's conditional global assembly
until a complete transported numerical schedule has actually been accepted.

## Review and validation

An independent reviewer rederived the excess transfer and requested explicit
specialization to `c=C_E`, `N>=3`, the binomial bound at positive-noise leaves,
and strictness at the equality boundary. These conditions are in the accepted
source. The exact reviewed fragment is pinned in `transport-review.md`.
The geometry, unification and alternate-route arguments received a separate
bounded analytic review. This is AI-assisted review, not human peer review
or formal verification of the whole manuscript.

Eight bounded checks passed, including the new conservation/count identities,
moment/cost identities, exact skeleton counterexamples, endpoint/collision
controls and source references. There are 478 labels and 271 manuscript
references. All 2,748 original baseline entries remain unchanged. No complete
native campaign or Lean build was run.

The 158-page manuscript compiles without warnings; the 14-page companion
compiles with one harmless underfull table box and no unresolved references
or overfull boxes. All companion pages and 14 affected manuscript pages were
inspected in overview, with selected dense equations inspected at full render
size. Both portable ZIPs are rebuilt with shell escape disabled; exact logs,
commands, input hashes and output comparisons are under
`runs/strategy-v4-20261027/`. Initial authoring/checker failures are preserved.

The recommendation is to review this as rigorous, delimited research
progress. BASE41, a complete uniform local exclusion and all numerical
premises remain obligations. No theorem is promoted to an unconditional
proof of the sharp conjecture, and no automatic merge is performed.
