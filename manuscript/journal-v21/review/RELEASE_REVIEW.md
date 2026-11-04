# Independent bounded release-preparer review

Reviewed source: `root/prepare_release.py`, SHA256
`d0f60a733ab3c2b5a1835629966b64d6e4cfdad13a8fd2debe03e1775999916c`.
This review does not execute `main`, create a release, simulate successful
completion inputs, or bypass any runtime completion gate. The central
campaign was still pending when this source epoch was inspected.

## Concrete corrections before execution

1. **The language test currently always rejects.** Its regex `pending`
   matches `depending` in retained `sections/core.tex` line 71. Use
   `\bpending\b` rather than a substring test. The actual in-memory text
   audit reaches this final assertion after every exact literal replacement
   succeeds. There are no missing references or duplicated labels.

2. **The optimized-Python rejection cannot itself be an assertion.**
   `assert __debug__ and not sys.flags.optimize` disappears under `-O`, as
   do all later completion checks. Use an explicit `if` and `raise` before
   any proof-sensitive work. Ordinary Python is already the selected runtime;
   this correction prevents an accidental future optimized invocation from
   disabling the release gates.

3. **Match the actual central capture schema.** The central union and
   controls captures use `returncode` and `inputs_unchanged`, not
   `actual_returncode` and `sources_unchanged`. Require an actual integer
   zero, so boolean `False` is not admitted. The coordinator independently
   identified this mismatch from `finalize_portable.py` during this review.

4. **Bind completion records and packaged bytes explicitly.** Before
   promotion, check each central captured stdout/stderr against its process
   hashes and check the final stdout `result_sha256` against the corresponding
   RESULT file. The complete collector already makes these joins for its
   four arithmetic shards; the release binder should preserve the join to
   the collector's own final output and the controls output. The central
   archive must have COMPLETION.json with its finite result hash equal to
   the just-accepted full union, and its selected tail result hash equal to
   the original complete tail record. Bind those members to FILES.json and
   the archive's final independent integrity/census receipt or fixed final
   SHA256. Merely finding an unpinned file called `central.zip` is not this
   join. Similarly, loading FINAL_FILES.json alone does not verify the
   listed tail bytes; the central finalizer's TAIL_STAGE/COMPLETION join is
   the useful existing implementation to retain.

5. **Two small source-scope safeguards are advisable.** Use duplicate-key
   rejecting JSON for unpinned newly generated completion records. Restrict
   the output argument to a simple fresh directory name below the integration
   directory; currently an absolute path or `../` changes the destination.
   The current planned path is safe, and this is not a request for a new
   permission step.

The source has not been edited by this reviewer. No arithmetic target or
analytic hypothesis needs changing to make these corrections.

## Textual promotion and dependency check

`audit_release_text.py` extracts only the in-memory source-to-text AST block,
rejects mutation/gate calls in that slice, and does not invoke the script's
main function. Its selected input bytes and resulting in-memory text hashes
are recorded in `runs/direct_comparison_integration_20261104/release_text_audit02/RESULT.json`.
The known language-regex false positive is the only failed text check.

The two pending numerical assertions become propositions only in the block
after all intended completion and archive gates. The transformation keeps
the original acquisition ancestors in the surrounding proof, the original
positive-39 target and prior dependency, the actual-index/floor distinction,
and the weaker uniform entry hypotheses. The equality corollary still
requires the weak all-index bound first. The final finite-base dependency
text is removed only in this intended post-completion block. No low-index
quartic pilot or other optional research is inserted as a premise.

All 18 counted exact literal replacements succeed on current source bytes.
Both assertion end markers are replaced as a pair. Generic section-level
conversion and Assertion-to-Proposition references resolve without missing
or duplicated labels. The initial draft comment stripped from each companion
is currently exactly a comment; an explicit prefix assertion would prevent
future edits from accidentally making the first removed line substantive.

The original implementation creates the release directory only after these
gates and text checks, and refuses an existing directory. Its final input
hash readback and PREPARATION receipt distinguish a completed staging from
a partial directory left after an unexpected later failure. It changes no
main repository file or frozen source object.

## Bounded draft05 layout check

The standalone `draft05/build/main.pdf` has 12 pages and SHA256
`e9c81c825b61ce3d36227f9417db63a55fc830f7638e323f956513eb3a148982`.
I actually opened its rendered pages 3 and 4, covering the coupled payoff,
the moment theorem, the updated alpha table heading and the complete
endpoint proof. No clipping, overlap, broken equation or table defect was
visible. The actual compile returned zero. This supplements, rather than
relabels, the earlier full03 visual inspection of pages 74–86. No claim of
visual inspection of all twelve standalone pages is made here.
