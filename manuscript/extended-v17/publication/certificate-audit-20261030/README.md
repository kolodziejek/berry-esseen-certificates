# Certificate audit and fresh verification

The former D.3/D.5 conditions are now computer-assisted propositions. See
[the decision and scope record](../../CERTIFICATE_AUDIT_NOTES.md).

- `entry/`: complete source-isolated Python 3.12.14 replay, fixed input hashes,
  return code, stdout/stderr, 19 checker and five wrapper rejection controls.
- `reports/`: mathematical derivations and code correspondence for coarse,
  signed and Fourier steps, plus coordinating and promotion reviews.
- `coarse/`: separately reconstructed non-Fourier coefficients and all 48
  quadratic updates; the Fourier pairs are explicitly shared inputs.
- `fourier/`: independently reconstructed LOW/HIGH scalar maps on the entire
  accepted trace, and Fourier identity/adversarial checks.
- `signed/`: import-free checks of sharper fixed-object constants, actual-law
  diagnostics and delicate sign/zero-denominator/endpoint cases.
- `support/`: import-free exact initial and cellwise support-gate evaluation;
  the continuous heat/ray proof remains in Appendix D.
- `claims/`: fresh execution of the shipped `tools/check_entry_claims.py`.
- `build/`, `layout.json`, `validation.json`: compilation, rendered-page review,
  source/PDF hashes and preservation evidence for this release.

The supplemental audit scripts are preserved with their exact recorded paths
and commands; they are evidence of this run. Some use the original workspace
path. For portable reproduction use the commands in Appendix E and the main
README. Use a fresh output directory and never enable Python optimization.
Diagnostic samples are not substitutes for the continuous inequalities in the
paper and reports. The standard-library interpreters and exact arithmetic are
part of the stated trusted stack.

The fixed certificate and all pinned checkers are unchanged. Frozen status
strings saying “conditional” are preserved verbatim: their analytic premises
are discharged by the paper and correspondence audit, not by the numerical
module alone. The finite base through 699 remains open.
