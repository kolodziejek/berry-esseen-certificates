# The sharp iid Berry–Esseen inequality

Bartosz Kołodziejek and Kacper Rodziewicz — extended manuscript, November 2026.

[PDF](main.pdf) · [TeX](main.tex) · [Proof dependencies](PROOF_DEPENDENCIES.md) ·
[Reproduction instructions](reproduction/REPRODUCE.md)

This extension proves, by a computer-assisted argument,

\[
\sup_x\left|\mathbb P\!\left(\frac{X_1+\cdots+X_n}{\sqrt n}\le x\right)
-\Phi(x)\right|\le
\frac{3+\sqrt{10}}{6\sqrt{2\pi}}\frac{\mathbb E|X_1|^3}{\sqrt n}
\]

for every positive integer `n` and every iid law with mean zero, variance one,
and finite third absolute moment. The constant is globally sharp. The optimal
constant at a fixed index is strictly smaller for `n >= 700`.

The finite induction establishes the bound through **42**. At a first later
failure, a one-step smoothing estimate supplies small excess and sharp
predecessors. A finite local comparison excludes indices 43–48, and a uniform
local comparison excludes every larger index. Thus no separate verification
of all indices through 699 is needed. The compact manuscript's comparison then
proves the additional strictness from 700 onward.

The introduction and reading guide explain this structure before the detailed
estimates. The appendices supply the continuous reductions and inequalities
implemented by the checkers. No eventual two-point optimality or proof-assistant
formalization is claimed. The manuscript discloses its substantial AI assistance.

## What the computation establishes

Acceptance uses integer and rational arithmetic, with proved rational enclosures
for transcendental functions. It checks complete parameter regions, including
shared boundaries and threshold atoms. Each numerical module retains its
explicit support, moment, contact and predecessor hypotheses. The mathematical
induction discharges those hypotheses for the same marginal law; a numerical
success flag alone does not prove this implication.

The reproduction directory contains the checking sources and static inputs,
a complete command index, and preserved execution records. It distinguishes:

- untrusted supplied candidates whose complete acceptance was repeated;
- newly constructed and recomputed bounds;
- full native executions and subsequent checks of their input interfaces;
- failed or interrupted attempts, with their actual observations preserved.

In particular, the four-summand result uses a complete fresh recomputation of
all 260 parent dispositions and all 1300 HIGH request slots. It does not claim
an unavailable exit observation for the earlier producer. Some later parents
were checked in disjoint runs, then admitted by complete case and domain
readers. The records identify these choices explicitly.

All required selected numerical families and their final joins have been
completed. The separate 114-command **fresh reproduction recipe** has not been
executed again as one relocated campaign. Full source restoration, selected
relocated executions, the archive restoration, and the execution supervisor's
rejection checks are documented separately. The distinction prevents a package
integrity check from being mistaken for a new arithmetic proof.

Start with [REPRODUCE.md](reproduction/REPRODUCE.md). It gives the exact inputs,
runtime requirements, safe restoration commands and full execution command.
The current process transport is for macOS; the three-summand checker also
requires a C++17 compiler and Boost.Multiprecision headers. Python assertions
must remain enabled.

## Build the manuscript

With TeX Live or MacTeX, run from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The build requires no shell escape. Compiling the document verifies its
presentation, not the mathematical or numerical assertions.

## Earlier revisions

The compact starting manuscript remains in `manuscript/compact-v16/`.
The earlier editorial notes, scalar receipts and compact-entry audit copied
into this directory retain their original dates and scopes. They are historical
records; the extension's current proof dependencies and reproduction package
are linked above. Original research sources are pinned at commit
`3d053204f30eab39da39bfb7b85e380d83ec0646` of the earlier certificate repository.
