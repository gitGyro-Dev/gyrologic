# External Review Record — Readable Semantics v1 — Claude Round 3

## Review metadata

- Topic: `Readable(...)` / `slice-done` relation, current fully-reframed revision
- Source file: `ideas/readable_semantics_v1.md`
- Source commit SHA: `b33fe7f58c861ab1f9a29f08587ac9a1cc527a13` ("Reframe Readable as retrospective local establishment guidance")
- Review round: 3 (first review of this specific revision)
- Review date: 2026-08-11
- Reviewer/service: Claude (Anthropic), reading the repository directly in a working-directory session
- Model/version if known: Claude Sonnet 5
- Review prompt:
  - `reviews/critical_review_prompt.md`

## Context established before this review

Commit history for this file:

```text
19744a3  2026-08-10 14:03  Create Readable semantics v1 after external review
b33fe7f  2026-08-10 14:49  Reframe Readable as retrospective local establishment guidance
```

`19744a3` is the revision reviewed by `readable_semantics_v1_claude_round2_20260810.md` and `readable_semantics_v1_gemini_round2_20260810.md` (both cite this SHA explicitly and both discuss a `PresentTo ∧ LocallyDiscriminable` candidate definition that is present in `19744a3`).

`b33fe7f`, produced 46 minutes later, replaces roughly 578 lines and adds 208, dropping the `PresentTo ∧ LocallyDiscriminable` formalization entirely and returning to a non-decompositional, "provisional explanatory word" framing plus a new retrospective-establishment discussion. **This is the current HEAD content of the file, and it has not previously been reviewed.** The round-2 reviews' findings (RC1–RC11, GR2-1–GR2-10) therefore do not describe the document as it currently reads; only the earlier `readable_semantics_v1_claude_reframing_20260810.md` review (of a still-earlier version) is actually reviewing content close to what survives in `b33fe7f`.

## Source status

- [x] Revised exploratory note
- [ ] Paper candidate
- [ ] Pre-submission manuscript

## External review

### 1. RC1 from the reframing review (falsifiability / missing admissibility constraint) does not appear to have been addressed, only re-asked

The earlier reframing review (`readable_semantics_v1_claude_reframing_20260810.md`) accepted, as a major open problem requiring a required response:

> restore at least a minimal notion of constraint/admissibility without returning immediately to universal necessary-and-sufficient conditions.

The current revision (`b33fe7f`) does not add any such constraint. Section 13, Open questions, Q3 asks:

> When two Operators place different `done` boundaries over the same continuing event, what makes both admissible or one inadmissible?

This is the same question, unanswered, not a response to it. As written, the document currently permits an Operator to treat *any* range of a continuing process as a local establishment, constrained only by "Operator-side Orientation and Context participates in where a local boundary is placed" (Section 12, point 3) — a statement too weak to rule out any placement, since Orientation/Context can themselves be redescribed post hoc to justify whatever boundary was chosen. This is the same escape-hatch problem already identified independently in the companion note's blind review (`operator_done_boundary_constraints_claude_blind_20260810.md`, C4: "if every fixed-looking criterion can be handled this way [convergence pressure], the theory risks becoming unfalsifiable").

Status: **accept — unresolved, carried over from prior round**

### 2. `Readable` and `slice-done` remain close to coextensive, and the document does not test whether they diverge

Section 3 defines `slice-done` as the point at which "the Operator... treats some range of that unfolding process as one local establishment." Section 4 defines `Readable` as a "provisional word for that 'can now be treated as one establishment' condition." No example in the document distinguishes a case where `slice-done` holds for some articulation while `Readable` fails for it, or vice versa. The earlier reframing review flagged exactly this (RC3, accepted) and asked for a "safer working statement" separating the two; the current text (Section 4) restates the separation in words but still gives no example that would let a reader tell the two apart operationally.

Status: **accept — request at least one worked example where the two terms give different verdicts, or state explicitly that no such example is currently known and the distinction is provisional/terminological only**

### 3. Retrospective establishment (Sections 6–9) currently has no falsifying condition

Open question 5 ("What distinguishes a reliable retrospective establishment from a merely possible story about the past?") is left fully open. As it stands, the section's content — traces/relations persist after an event and later Operators may infer from them that "something of that kind probably occurred" — is compatible with essentially any inference from present evidence to a past state. Nothing in the document currently distinguishes this from ordinary abductive/inferential reasoning in general, so it is not yet clear what a Gyro-specific claim is being made here versus a restatement of "evidence can support inference about the past."

Status: **accept-for-investigation — recommend proposing at least one candidate (even weak/provisional) criterion to test against counterexamples, rather than leaving the question fully open indefinitely**

### 4. No comparison against existing event/process theory, despite this being the review prompt's own criterion 3

The core distinction the note relies on — a continuing, unbounded event/phenomenon versus an Operator-chosen bounded local establishment carved out of it — closely resembles existing treatments of event boundedness and aspect in event semantics (e.g., the activity/accomplishment/achievement distinctions traceable to Vendler, and telicity/boundedness as developed by Bach and others), and more loosely resembles the process/actual-occasion distinction in process philosophy (Whitehead). `reviews/critical_review_prompt.md` explicitly asks reviewers to check "overlap with and differences from existing theories." This note (unlike some other repository documents, e.g. `docs/48_Mathematical_Field_Comparison`) does not attempt this check at all for the "continuing event vs. local establishment" distinction specifically.

Status: **accept-for-investigation — this is a concrete, checkable literature comparison, not a speculative concern; worth at least one pass before further iteration**

### 5. Process-note: the document's own review-response discipline was not applied to itself

`reviews/review_workflow.md` step 6 asks that, for every substantive criticism, a decision (accept / partial / reject / verify / defer) be recorded with a reason before revising the note. Section 14 of the current file ("Review note") gives a prose gloss on the prior reviews rather than a claim-by-claim disposition of RC1–RC5 from the reframing review. Given how large the rewrite between `19744a3` and `b33fe7f` was, it is not possible from the file alone to tell which specific prior criticisms (from either the round-2 reviews on `19744a3` or the reframing review) were deliberately dropped versus incidentally lost in the rewrite.

Status: **verify — process hygiene point, not a content defect; low severity while the note remains pre-paper-candidate, but should not carry forward silently if this note is promoted**

## Claim-by-claim assessment

| ID | Review criticism | Type | Decision | Reason / verification | Required change |
|---|---|---|---|---|---|
| CR3-1 | No admissibility constraint on Operator-side boundary placement; RC1 from prior round appears unaddressed | logical / counterexample | accept | Section 13 Q3 restates the same open question rather than answering it; Orientation/Context can be redescribed post hoc | Add at least a minimal non-circular constraint, or explicitly argue why none is currently possible without over-formalizing |
| CR3-2 | `Readable` and `slice-done` remain effectively coextensive in this text | definitional | accept | Section 3 and Section 4 definitions do not diverge in any given example | Provide one worked example where the two verdicts differ, or state the distinction is currently terminological only |
| CR3-3 | Retrospective establishment has no falsifying condition | counterexample / logical | accept-for-investigation | Open question 5 unaddressed; content currently indistinguishable from generic abductive inference | Propose at least one provisional criterion and test it against a counterexample |
| CR3-4 | No comparison to existing event/aspect/process theory | prior-work | accept-for-investigation | Review prompt criterion 3 not applied to this specific distinction | Check against event semantics (telicity/boundedness) and process philosophy before further iteration |
| CR3-5 | Review-response discipline (accept/partial/reject/verify/defer per criticism) not applied to the large `19744a3`→`b33fe7f` rewrite | process | verify | Cannot determine from the file alone which prior criticisms were deliberately resolved vs. incidentally dropped | Not urgent at idea-note stage; required before paper-candidate promotion |

## Factual verification

### F1

- Review claim: the current file content has not previously been reviewed in this form.
- Verified result: confirmed via `git log` and `git show` — round-2 reviews cite commit `19744a3`; current HEAD is `b33fe7f`, a near-total rewrite of that commit produced 46 minutes later.
- Evidence/source: `git log --follow -- ideas/readable_semantics_v1.md`; `git diff --stat 19744a3 b33fe7f -- ideas/readable_semantics_v1.md` (578 deletions, 208 insertions).
- Status: confirmed

## Counterexamples

### C1 — Post-hoc Orientation/Context redescription

- Counterexample: an Operator places a `done` boundary anywhere in a continuing process, then justifies it after the fact by describing "the current Orientation and Context" as having favored exactly that boundary.
- Target definition/claim: Section 12 point 3 ("Operator-side Orientation/Context participates in where a local boundary is placed") as a meaningful constraint.
- Does it actually break the claim?: yes, if Orientation/Context are not independently fixed before the boundary is chosen (this is the same discipline already proposed elsewhere in the repository for `ρ`, e.g. `readable_semantics_v1_claude_round2_20260810.md` RC6, but not yet imported into this note).
- Revision required?: yes.

## Existing-theory comparison

- Candidate overlapping theory: event semantics / aspect theory (telicity, boundedness — Vendler, Bach); process philosophy (Whitehead's process/actual-occasion distinction).
- Similarity: both frameworks already formally separate an unbounded ongoing process from a bounded, perspective-dependent unit carved out of it, which is structurally close to this note's "continuing event vs. local establishment."
- Difference: unverified — no check has been performed yet.
- Source checked: none (this review only identifies the comparison as owed, per the review prompt's own criterion 3; it does not perform the literature check itself).
- Remaining uncertainty: whether Gyro Logic's version adds anything beyond a restatement of existing boundedness/aspect distinctions under new vocabulary.

## Fix now / keep provisional

### Can be fixed now

- Add at least one worked example distinguishing `Readable` from `slice-done`, or state plainly that none exists yet.
- Add a minimal, explicit (even if weak) admissibility constraint on boundary placement, addressing Q3 rather than re-listing it.

### Should remain provisional

- Full criterion for "well-supported retrospective establishment" vs. "merely plausible story."
- Formal relation between retrospective establishment and Trajectory/Incorporated Readability.
- Whether existing event-semantics/process-philosophy literature already subsumes the continuing-event/local-establishment distinction.

## Revision outcome

- Updated file: pending
- Revision commit SHA: pending
- Major changes: pending
- Remaining open questions: admissibility constraint for boundary placement; Readable/slice-done divergence; falsifiability of retrospective establishment; literature comparison; reconciliation with the three companion boundary-origin notes' shared regress/falsifiability problem.
- Another external review round required?: yes

## Review gate status

```text
REVISION_REQUIRED
```

Current status: `REVISION_REQUIRED`

Reason: the central falsifiability/admissibility gap flagged in the prior reframing review round is still open in the current revision — it was not fixed, only re-asked as an open question. This is the same underlying issue now shared across `ideas/readable_semantics_v1.md` and all three boundary-origin notes (`fixed_criterion_vs_done_boundary`, `local_establishment_boundary_origin`, `operator_done_boundary_constraints`): none of the four current notes yet states what would make a boundary/criterion placement inadmissible, as opposed to merely different.

## Layer consistency check

- Gyro Logic theory only: yes
- GyroOS requirements imported?: no
- GyroAuth requirements imported?: no
- Core changed?: no
- If Core challenged by reviewer, preserved as review criticism rather than automatically adopted?: yes (no Core challenge raised in this review)
