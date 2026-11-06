# Count-specific comparison: transfer and sharper normal bounds

This continues the six-count method in `../six-count-row-20261105/`.
The objective is a shorter, understandable proof with explicitly checked
computational comparisons. The journal-v21 manuscript remains 86 pages:
none of its still-needed arguments has been deleted at this checkpoint.

The new mathematical improvement is to retain more of the normal term before
bounding it. Its numerator and variance depend on the same probability, so
their joint endpoint bound is better than separate extrema. A quadratic lower
polynomial retains its variation across a whole probability/phase cell. For
later indices, a tangent lower bound for the third-moment normalization avoids
the loss from using a single constant denominator. These are sufficient
inequalities for the original target, with explicit curvature checks.

Read `gaussian_endpoint.pdf` (four pages) for the derivations, then the proof
notes in the packages below. The additive curvature proof in
`later-curvature/` explains how to allow either sign of the normal argument:
subtract a rigorous upper bound for its curvature from the quartic Hessian,
then verify that the resulting matrix is positive semidefinite. All
certificates use one common pair of
conditional laws across every binomial count. Discovery and acceptance remain
separate: floating-point optimization proposes quartics; ordinary Python with
exact rational arithmetic checks their global real rays, moment bounds and
closed-domain polynomial inequalities. No sampled positivity is an acceptance
criterion.

| Result | Mathematical status | Execution status |
| --- | --- | --- |
| Entire original n5 B0/p50 comparison | Conditional positive closed-score implication at the original C_E target | Fresh complete replay: 383 baseline leaves (`n5-two-rows/`) and **11 all-Taylor leaves** (`n5-all-taylor/`) |
| Entire original n5 B2 S3/p34 comparison | Same original conditional target | Fresh complete replay: 54 baseline leaves (`n5-two-rows/`) and **7 all-Taylor leaves** (`n5-all-taylor/`) |
| Entire original n5 BN/p39 comparison | Same original conditional target; 11 leaves use the new Gaussian polynomial in mixed mode, and all 18 leaves in all-Taylor mode | Fresh complete replay: 1,126 mixed leaves (`n5-bn39/`) and **18 all-Taylor leaves** (`n5-all-taylor/`) |
| Entire original n5 BN/p38, B0/p53 (`k4`), B3 S0/p59 (`k4`), B3 S2/p59 (`k4`) comparisons | Same original conditional target across all active nearest-count roots (`k=1,2,3` or `k=2,3,4`) with curvature-corrected both-half Gaussian Taylor bounds | Fresh complete replay in `n5-all-taylor/`: **13** (`BN38`), **5** (`B0_53`), **4** (`B3_S0_59`), and **5** (`B3_S2_59`) leaves (**63 leaves total across 7 rows** vs. 2,736 old `COUNT` leaves) |
| Sharp39, k15, full original p in [.38,.39], u in [-.01,.01], full original noise | Conditional comparison on this entire bounded rectangle, including both signs of the normal argument | Fresh two-cell exact replay: 160 ray checks, 11,880 score coefficients, 3,006 corrected PSD coefficients |
| n6, fixed p=77/200, k2, u=0 | Conditional comparison over all noise compatible with the original mean premise | Fresh exact replay and canonical-input controls; no p/phase interval claim |
| Full manuscript shortening | Not completed | 86 pages unchanged; about 60 pages remains the objective |

Original acquisition remains a premise of each comparison. These results do
not independently re-establish compactness, acquisition, the full finite base,
reflection conventions or the all-index theorem. An exact arithmetic PASS
proves the stated computational obligations only after their mathematical
reduction and domain coverage have been justified.

## Reproduction and evidence

- `n5-two-rows/`: two completed original rows, sources, objects, complete
  captures, original source contracts, controls and portable commands.
  `portable.py replay --row B0_50 --out /absolute/NEW` and the corresponding
  `B2_S3_34` command recompute every leaf. Run with `python3 -I -B` from that
  package. `verify`, `controls` and the small-root `smoke` are distinct actions.
- `n5-bn39/`: the completed third row. Run
  `python3 -I -B portable.py replay --out /absolute/NEW` there to recheck all
  1,126 leaves. The mixed reader uses the original bound on 1,115 leaves and
  an explicitly tagged Gaussian Taylor bound on 11; both prove the same target.
- `n5-all-taylor/`: additive all-Taylor curvature-corrected $n=5$ package and
  general 295-contract external selector (`code/selector.py`,
  `contracts/CENSUS_295.json`). Generalizes the quadratic Gaussian Taylor scalar
  to both probability halves ($0 < p_l < p_u < 1$) using
  $v_{\min} = \min(p_l(1-p_l), p_u(1-p_u))$, certifies the uniform noise-curvature
  bound $g''(\lambda) \le M$ via $v^2(H_F(p) - 25 M J) \succeq 0$ on every leaf,
  and closes **7 complete original $n=5$ rows** (`BN39`, `B0_50`, `B2_S3_34`,
  `BN38`, `B0_53`, `B3_S0_59`, `B3_S2_59`, 19 roots) in **63 total leaves**
  (18 on `BN39` vs. 1,126 mixed leaves; 49 across `BN39`, `B0_50`, `B2_S3_34`,
  `BN38` vs. 2,296 baseline/mixed leaves; 63 across all 7 rows vs. 2,736 old
  `COUNT` leaves). Run `python3 -I -B -S portable.py replay --out /absolute/NEW`
  from that package.
- `later-index/`: the general n+1-count proof, tangent normalization, Gaussian
  polynomial proof, fixed-n6 evidence and bounded sharp39 checks. Run
  `python3 -I -B -S replay.py /absolute/NEW` there to reproduce the entire
  earlier p in [.385,.39], u in [-.01,.01] sharp39 rectangle, with the standard
  library alone.
- `later-curvature/`: the additive full-probability extension. Its `replay.py`
  rechecks the two closed probability cells covering [.38,.39], u in [-.01,.01].
  Run `python3 -I -B -S replay.py /absolute/NEW` from that package.
  The analytic curvature correction and the earlier unsuccessful one-cell
  score check are both preserved. No new quartics were needed.
- `review/`: independently derived scalar/moment/Hessian identities,
  coefficient reconstruction, actual-law controls and corruption tests, with
  frozen source snapshots and actual captures. Their extent of independence
  is explicit; there is no claim of a second complete independently written
  full-row checker.
- `delivery-evidence/`: source-bound TeX build, four-page visual review and
  relocation evidence. Historical absolute command paths are provenance;
  the package entry points create new location-specific commands.

Every output directory must be new and outside its immutable package. Do not
use Python -O or -OO. The existing full three-row computations were not repeated
merely to copy the bytes; relocated checks tested inventories, controls and a
small complete root. The short sharp39 rectangle did receive a complete
relocated replay. Hashes establish integrity, not mathematical correctness.
`RESULTS.json` binds the current completed claims to their actual receipts;
`FILES.json` inventories the entire publication folder. To check the latter,
run `python3 -I -B -S verify_inventory.py`. That command checks bytes only;
use the package replay commands for mathematical acceptance.

`n5-two-rows/research/` preserves the earlier unresolved BN39 construction.
The separate `n5-bn39/` epoch supersedes its status, preserving its bytes and
failures. Its fresh complete replay is what admits the new mixed object.

## Why this is not yet a shorter manuscript

The previous census found 295 original n5 comparison contracts and 1,243 count
objects overall. Seven n5 rows now have complete replacements by this method in
`n5-all-taylor/` (`BN39`, `B0_50`, `B2_S3_34`, `BN38`, `B0_53`, `B3_S0_59`,
`B3_S2_59`, spanning `B0`, `BN`, `B2`, `B3`, right-half $p \ge 1/2$, and active
$k=4$ roots in 63 total leaves vs. 2,736 old `COUNT` leaves); 288 remain. Even replacing every
n5 row leaves the generic count proof used by n6--38 and sharp39. The signed
fifth-index corner, Fourier complements
and the 17-page acquisition argument also remain. The new criterion must
replace a complete family and all consumers of a proposed deletion before a
net page saving can be measured. The bounded experiments here support that
research direction; they do not establish the final saving.
