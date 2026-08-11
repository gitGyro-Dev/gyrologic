# External Review Record — Readable Semantics v1 — Claude Round 6

## Review metadata

- Topic: `Readable(...)` / `slice-done` relation, anti-post-hoc pressure test refinement
- Source file: `ideas/readable_semantics_v1.md`
- Source commit SHA: `f7908cebb82a235bac7380661bd2bceb5c60b04c` ("Refine anti-post-hoc boundary test after Claude Round 5")
- Disposition reviewed: `reviews/readable_semantics_v1_claude_round5_disposition_20260811.md` (commit `37188c8`)
- Review round: 6
- Review date: 2026-08-12
- Reviewer/service: Claude (Anthropic), reading the repository directly in a working-directory session
- Review prompt: `reviews/critical_review_prompt.md`

## Check against disposition R5-1

Required: "prior" becomes necessary-but-not-sufficient; add "specific enough to exclude at least one plausible candidate boundary."

Text check (Section 5.1, "Current stronger pressure-test requirement"): implemented exactly as scoped, with an explicit disclaimer that "this does not establish a universal specificity metric." Working guidance point 8 and Open Question 5 updated consistently. **Resolved as scoped, no overclaim.**

## New finding — "excludes at least one candidate" is a weak bar

### Claim

The current test can be satisfied by excluding a candidate that was never plausible in the first place, without meaningfully constraining the real decision.

### Example

> "The boundary will not be placed before `E1`."

This is prior, and it technically excludes a candidate boundary (before the stream begins). It passes the letter of the current test. It leaves every boundary from `E1` through `E8` equally available — i.e., it does no more constraining work than having no precommitment at all, since "before `E1`" was never a live candidate.

### Assessment

This is a real gap, but it is the third round of narrowing the same admissibility test (Round 3/4 → normative-only; Round 5 → temporal-priority loophole; this round → weak-exclusion loophole). Each fix has been honest and correctly scoped, and each new gap is smaller than the last. Continuing to chase this specific axis (what counts as a "strong enough" exclusion) risks re-approaching the "universal necessary-and-sufficient definition" the note has repeatedly and correctly declined to attempt.

**Recommendation: do not open another revision round on this specific axis.** Instead, add one sentence acknowledging the weak-exclusion case as a known, currently-undefined limitation (parallel to how Section 5.1 already names "vague precommitment" as a limitation), and treat the anti-post-hoc discipline as adequate for the note's current idea-stage purpose. Full admissibility semantics is already correctly listed as open/future work (Section 9 point 11, Open Question 4) — this finding belongs there, not as a fourth patch to the pressure test.

Status: **future work — explicitly documented limitation, not a blocking defect**

## Retrospective establishment v0 — round 2 check

Source commit: `ccb9e2f03fd985f02c067c7e71729e72e1e43ea7`.

Checked against `reviews/retrospective_establishment_v0_claude_round1_disposition_20260811.md` (RE1-1, RE1-2): both implemented as scoped — Section 3 now names historical geology, IBE/abduction, and forensic/historiographical method as explicit future comparison targets without claiming novelty or overlap; Section 6.1 adds the scorch-mark multiple-cause counterexample and the support-vs-sufficiency distinction. **Both resolved as scoped, no overclaim.**

## Claim-by-claim assessment

| ID | Item | Decision | Reason | Required change |
|---|---|---|---|---|
| R6-1 | "Excludes at least one candidate" is satisfiable by excluding an implausible candidate, doing no real constraining work | future work | third-order refinement of the same admissibility axis; diminishing returns from further patching | add one sentence naming this as a known limitation; do not spawn another pressure-test revision round |

## Revision outcome

- Updated file: none by this review (critique only)
- Recommendation: treat the anti-post-hoc discipline as sufficient for idea-stage `readable_semantics_v1.md`; move remaining admissibility work to the already-open future-work item rather than continuing incremental patches
- Another external review round required specifically for the pressure test?: no — suggest closing this sub-thread here

## Review gate status

```text
REVIEW_ACCEPTABLE
```

Reason: no unassessed criticism remains against either note. Both revisions matched their dispositions exactly, with no overclaiming across six rounds. The one new finding (R6-1) is explicitly scoped as a documented limitation rather than a blocker, to avoid over-iterating a single axis at the expense of the note's broader progress.

## Layer consistency check

- Gyro Logic theory only: yes
- Core changed?: no
