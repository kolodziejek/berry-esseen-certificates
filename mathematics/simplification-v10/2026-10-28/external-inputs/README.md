# Near-resonance test behind the "Version 4" review

`nearres.py` reproduces the table in Option 1: at n = 42 and n = 100, p = p*,
the negative-class atom gets a rare outward jump of d lattice steps
(d = 0.5, 0.8, 0.9, 0.95; rate 0.005 or 0.02), compensated by a small drift so
the conditional mean stays zero. For each law it prints lambda, the score C,
the skeleton's score C_B(k) at the same count, and the first-order prediction.

It reuses the helper functions in `experiments.py` (run both from the same
directory). Arithmetic is double precision and sum locations are rounded to
1e-10, so this is evidence, not a certificate; the audit in the repository
(strategy-v4/opus-audit.md) explains the limits. Requires numpy and scipy;
runtime is a few minutes.
