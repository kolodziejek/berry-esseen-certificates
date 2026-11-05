# Additive review of mean and closest-sign constraints

Read `construct/model_v4.py` in full. The new constraints are valid conditional
uses of the original fields. No full row, acquisition replay, or successful V4
numerical cover is claimed here.

Here the acquired mean is `m=E X_+=v/sqrt(w)`, half the absolute first moment.
Consequently `m>=m_lo>0` implies
`lambda<=n(v²/m_lo²-v)`. On this row the right side is increasing in v because
`2v>m_lo²`, and v increases with p<1/2. Evaluation at p_hi gives the correct
upper noise ceiling.

The positive numbers in `negative_endpoint_lower` and `positive_endpoint_lower`
must mean the acquired gaps from zero in the standardized X coordinate. They
give `U0<=p-negative_endpoint_lower*sqrt(w)` and
`-U1<=q-positive_endpoint_lower*sqrt(w)`. The code uses a directed lower root of
`v_min+lambda_lo/n`, then p_hi and q_hi. Those directions yield upper inward
caps. Taking the minimum with the original inward cap is valid. These fields'
historical conditional status is not changed by reading or hashing the file.

The remaining moment and target algebra matches V3, with these new constants.
The source conservatively rejects empty or degenerate slab polygons. Such a
rejection does not itself prove that a slab is empty, and cannot be used as an
accepted exclusion by a future cover collector.

Fresh exact evidence:
`runs/count_row_20261105/review_v4_constraints01/checked/RESULT.json` and its
parent `PROCESS.json`. Actual return code zero, stable sources, empty stderr.
It checks 48 actual-law signed-cube and mean identities; 45 pairs satisfy the
tested mean/sign premises and yield 135 successful cap checks. Independent
inverse expansion matches all 4,050 moment coefficients of 81 selected V4
rows. Two explicit sign controls are retained.

Reviewed model SHA256:
`38576e0da4fe5663008b9268aea15ea2540045bda188c2a95737a46a73cd9a99`.

An optional further common-moment strengthening is derived separately in
`POSSIBLE_DUAL_STRENGTHENING.md`. It is an analytic proposal, not an executed
comparison certificate.
