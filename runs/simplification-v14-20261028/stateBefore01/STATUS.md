# Current research status — v13, 28 October 2026

Existing review target: https://github.com/kolodziejek/berry-esseen-certificates/pull/5
Keep it draft. No merge, main push, force-push, branch deletion or upstream change.
Original reference commit: 6346fc1b4432bc5982822aa696eb566ed9e1e1ee.
V13 starts at reviewed/published dde37e6f2fc8bfe654d6af8bf250756c6e2984d1.

## Current result map

| Result | Mathematical status | Execution status |
|---|---|---|
| General crossing kernel and exact weighted identity | Locally derived and independently checked under separated support, centering, width and interior-threshold hypotheses |109constructor cases; independent366cases/9192checks and24direct-product controls PASS |
| Inward-cubic geometric budget | Proved conditional on retained actual-gap/coarse-entry inputs; no outer-strip heat input in the new inequality |139coefficients independently reconstructed;22gates;832actual budgets PASS |
| Global noise lambda<.36; left p<=.4 lambda<.32 | Same geometric implication; stronger smaller-p bounds and index cutoffs in proof |Fresh exact continuous-domain polynomial checks PASS |
| Count concentration and signed curvature | Proved with stated moment/support hypotheses |32laws,160curvature,96interval controls PASS |
| Symmetric central full comparison | Proved for even positive n,p=.5,reflected conditional laws and explicit central interval, any positive noise |3exact symmetric controls PASS |
| n4 moment-polytope endpoint reduction | Refuted by exact actual iid five-point family |374finite checks,12negative controls PASS |
| Finite contact collision restriction | Conditional on finite atomic support and global contact; at most2noncolliding atoms,<=6only with unique active multiset |Exact collision controls PASS |
| General weighted closure,C4,BASE41,full conjecture | Open |No full acceptance claimed |

The selected general v12 comparisons remain lambda<=.01 left and<=.075right.
V13 shrinks their remaining acquired noise ranges to left(.01,.32),right(.075,.36),
with additional local ceilings. Geometry p<=1/3 forcesn<=168; p<=.4 forcesn<=3598.
The geometry range extends to.54; no count theorem is added on(.53,.54].

## Sources and evidence

Canonical package: mathematics/simplification-v13/2026-10-28/ in the fork.
Start with README.md,crossing.pdf(3pages),geometry-noise.pdf(4pages),
counts-tools.pdf(4pages),finite-contact.pdf(4pages). Optional renewal.pdf(2pages)
is superseded as a dependency by the general crossing proof.
Fresh integrated11checkPASS: runs/simplification-v13-20261028/integration01/receipt.json.
All2748baseline entries preserved(182materialized,2566sparse bindings);
all85manuscript files unchanged. The89-page manuscript remains as before.

Research worktree: work/fork_audit_20261027/simplification-v13.
Integration worktree/branch: work/fork_audit_20261027/strategy-v4,
manuscript/strategy-v4-20261027. V13 publication receipt is stored separately
once the normal push and draft-PR metadata update have been verified.

Earlier state snapshots are retained under the stateBefore01 evidence directory.
Historical success labels in startup documents are not independent proof.
