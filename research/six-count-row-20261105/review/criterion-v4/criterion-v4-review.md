# Bounded review of the V4 criterion and assembly

Read the complete release02 TeX source, all new Gaussian/cubic/mean/sign
subsections and selected row constants, against the frozen V4 source.
The exact source identities are recorded in criterion-v4-review.json.
No numerical integrations or full certificate replays were run for this
review. The separate assembly performs those exact readers.

The Gaussian second derivative and uniform concavity guard have the
correct signs; the Gaussian is subtracted before the variance maximum.
The cubic formula uses the same conditional marginals and signed moment
orientation. Its fixed positive lower coefficient is rounded on the
actual domain before extending the polynomial to nonrealizable corners.
Mean/noise monotonicity and the signed endpoint ceilings match V4.
All selected n, p, rho, beta, noise, mean, support, endpoint and H/scale
constants match the original contract and current executable targets.

No mathematical blocker was found. Two presentation clarifications were
sent to root: explicitly retain a_i<=d before formula15; specify that
root selections cannot be duplicated, while identical valid coefficient
lists at distinct cells need not be rejected. Neither changes arithmetic.

Also read complete_v4.py and select_v4.py in full. The fixed three-root
census, source/object identities, actual argv/returncode/streams,
reconstructed native-result comparison and before/after byte checks are
consistent. No stored-success admission or coverage hole was identified.
This review is not an independently implemented full-row certificate.
