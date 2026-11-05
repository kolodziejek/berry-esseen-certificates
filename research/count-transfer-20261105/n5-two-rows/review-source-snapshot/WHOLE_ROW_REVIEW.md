# Complete-row selector review

I reviewed `construct/accept_row.py` and its two completed row selections. This is a source/coverage audit and a readback of captured results, not another full numerical replay.

The current reader has SHA-256 `bb1a3cd733790238deffbbb88dbe87594094146b60d734fb17bb703b143b4568`. It preserves the already reviewed model and exact leaf acceptor. A selection must bind the original row identifier and contract hash, provide every derived threshold root in exact order, use distinct regular objects with matching hashes, and cover the full original probability and noise intervals. A root may use its exact clipped phase interval or explicitly enlarge it to the full closed interval `[-1/2,1/2]`; no smaller alternative is accepted. The child reader verifies the complete closed split tree.

The threshold-root census is derived from the acquired threshold range. It does not truncate the possible nearest-count integer to the six mixture counts. All six mixture counts remain present in every leaf. Half-integer ties remain included on both neighboring roots. The selected two rows have nondegenerate root intervals; the reader rejects degeneracy rather than silently dropping an endpoint.

A minor provenance issue in the first draft was corrected before the completed captures: the original selected path is now checked for being a symlink before resolution. This correction did not change any mathematical target or accepted leaf arithmetic. Source, selection and object hashes are checked again after complete acceptance.

The completed scopes are:

| Original acquired row | Probability | Full noise ceiling | Required nearest roots | Accepted leaves |
| --- | --- | --- | --- | --- |
| `B2_S3_34` | `[17/50,7/20]` | `206391/1000000` | `1,2,3` | 54 |
| `B0_50` | `[1/2,51/100]` | `32813/125000` | `2,3` | 383 |

The B2 result is `runs/count_transfer_20261105/construct_B2_complete01/accepted/RESULT.json`, SHA-256 `dd6fde86aaad2ff58d7fdd89c039bf3cd3e31194622a4c802b2d83bb51b6b82d`. Its process record reports actual return code 0, stable inputs, empty stderr, and 23.870499707991257 seconds. It accounts for 648 global rays and 121,500 score coefficients.

The B0 result is `runs/count_transfer_20261105/construct_B0_complete01/accepted/RESULT.json`, SHA-256 `722ecb69e3bcac17206cc2035cd3f86802935bdd0cf9bb2d19eb590358099b9a`. Its process record reports actual return code 0, stable inputs, empty stderr, and 179.83274174999679 seconds. It accounts for 4,596 global rays and 816,750 score coefficients.

Both are conditional positive closed-score implications under their **original acquired row**. Their proof covers the right-half cell touching `p=1/2` and the selected left-half row without a reflected reorientation. Acquisition, other rows and an all-`n=5` replacement are not established by these two receipts. At this checkpoint the third new row, `BN39`, has no complete-row receipt reviewed here.

Mathematical status: the generic reduction and full-row coverage are locally derived and audited; the row implications retain original acquisition premises. Execution status: both full row readers freshly passed in the constructor's separate acceptance runs. My independent model/moment checks are separately recorded in `REVIEW.md` and `runs/count_transfer_20261105/review_model01/`; I did not repeat those full leaf campaigns.
