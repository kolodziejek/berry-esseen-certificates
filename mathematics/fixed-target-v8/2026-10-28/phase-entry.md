# Signed phase resource: proof, complete export, and acceptance

The sign of the raw threshold can be retained in the last accepted entry pass.
This gives a tighter bound on the **same** defect/excess/leakage resource; it
does not replace that resource by three separately affordable quantities.
The full derivation is in [phase-proof/main.tex](phase-proof/main.tex).

| Result | Mathematical status | Execution status |
|---|---|---|
| Signed quadratic bound and endpoint maximization in the fixed target | Locally derived, independently reviewed under the retained entry hypotheses | All1,364 endpoint quadratics independently reconstructed |
| Noise and probability restrictions for every n>=42 | Derived from exact conditional-moment identities, both orientations retained | Actual-law and closed-interval controls pass |
| Fourth-pass export:2048 boxes,682 active cells | Conditional on the previously accepted first three passes and analytic inputs | Fresh complete deterministic replay, exact identical output |
| Closed-region results | Conditional consequences of this complete cover | Nine exact region evaluations independently matched |
| Full confinement/count comparison/finite base | Not a consequence of this note alone | Separate obligations |

The source export SHA256 is
`b18599468c975032f4078e7a5f734fd6430b2b7da583789de58d9537d323f690`.
Its complete saved object is `runs/fixed-target-v8-20261028/phase01/stdout.json`.
The source instrumentation in `build_phase_core.py` is exactly reversible to
the frozen v7 arithmetic. Signed slopes are additional output; every original
bound, target, and cell remains unchanged. A strict guard rejects exporting a
cell without the already required actual gap.

For p in[.41,.42], H in[1.20,1.30], and lambda in[0,.15], the resource upper
bound is at most `-.033287706`. Thus that whole closed region cannot contain a
nonnegative-excess maximizing witness satisfying the entry premises. For the
negative threshold the corresponding resource is at most `.265382458`; this
is a useful ceiling, not an exclusion. All displayed decimals are outward
rational bounds, not numerical samples or existence assertions.

## Reproduction

From the repository root:

```
python3 -I -B mathematics/fixed-target-v8/2026-10-28/accept_phase.py runs/fixed-target-v8-20261028/phase01/stdout.json
python3 -I -B mathematics/fixed-target-v8/2026-10-28/phase-review-check.py .
python3 -I -B mathematics/fixed-target-v8/2026-10-28/phase_region.py
```

The first command pins project sources before execution, executes their `.py`
bytes at explicit paths, isolates imports/cache in the child interpreter, and
compares the entire ordered JSON export. It has13 negative controls. The
second independently reconstructs coefficients, phase prices, probability
filters, the source transformation, and all nine region results; it imports
no inherited kernel. The third evaluates those selected regions and is not an
authenticity checker for an arbitrary supplied export.

`phase01`, `phase02`, `phase-accept01`, and `phase-accept02` preserve the actual
commands, streams, versions, source snapshots, hashes and return codes. The
selected acceptance is **phase-accept02**, using acceptor
`416ab9b7bf957c57062e929743dad200f9ac002f879cb2516eeb9c6a2ac2e6b7`
and producer
`90ca756fde0425505013444ab1a5ff5ffa9fb9bb0ff125fbdda6a132eb64167d`.
It reproduces the original output byte-for-byte.

## Defect found and repaired during review

The original `-B` child invocation prevented cache writes, but did not prevent
reading existing bytecode. The independent reviewer demonstrated that poisoned
bytecode could alter the exported cells while the pinned `.py` files remained
unchanged. Import search order also allowed an unpinned same-name file to
shadow the intended phase module. This was an acceptance defect; it was not a
mathematical counterexample or evidence that the clean saved cells were wrong.

The repaired producer loads all project modules by compiling their explicitly
named source bytes. The acceptor uses an isolated interpreter and an empty
temporary bytecode prefix. The independent review verifies that both attacks
no longer alter the replay: the genuine export passes and the poisoned export
is rejected. The old source snapshot and runs remain available. The same
cache limitation must be considered for inherited acceptors; v8 provides a
separate isolated reproduction wrapper without rewriting those sources.

The trusted stack remains the Python interpreter/standard library, exact
integer and rational arithmetic, the reviewed program semantics, and the
analytic reduction. Hashes and agreement alone do not establish those premises.

## Dependency removal permitted by this result

Downstream estimates may use these signed cellwise envelopes instead of a
single global absolute-phase ceiling, because both bound the identical
actual-law resource and every active source cell is retained. Keeping this
information requires no additional Fourier integration beyond replaying the
last accepted pass. This note by itself removes no complete confinement job,
finite-base certificate, or proof object. The later confinement note states
the precise panel on which its additional contact argument closes the join.
