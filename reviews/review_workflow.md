# External Review Workflow

## Purpose

This workflow introduces a repeatable external critical-review cycle before exploratory Gyro Logic notes are promoted into paper development.

The process is designed to reduce confirmation bias, self-reference loops, unnoticed ambiguity, and premature formalization **without turning review into an open-ended perfection loop**.

A strict reviewer can almost always generate another criticism. The goal is therefore not to reach a state in which no reviewer can produce any further comment. The goal is to determine whether the **current version is coherent enough to advance**, while preserving non-blocking criticism for later versions.

## Workflow

### 1. ChatGPT wall-bouncing and idea organization

Use ChatGPT for exploratory discussion, decomposition, examples, candidate definitions, and counterexample generation.

At this stage, concepts remain provisional unless explicitly fixed elsewhere in canonical documentation.

### 2. Commit a coherent note to GitHub

When a topic reaches a reviewable unit, preserve it as:

```text
ideas/<topic>.md
```

The note should include at least:

- purpose;
- current definitions or candidate definitions;
- distinctions being proposed;
- examples already tested;
- known limitations;
- unresolved questions;
- explicit non-claims where needed.

Use a public repository URL when practical so the exact revision can be shared with external reviewers.

### 3. Independent external reviews

At a meaningful breakpoint, request reviews independently.

#### 3a. Claude / Claude Code

Provide:

1. `reviews/critical_review_prompt.md`;
2. the exact GitHub URL or exact document body under review.

Claude or Claude Code may preserve critique under `reviews/`, but must not revise the reviewed `ideas/<topic>.md` note itself.

#### 3b. Gemini

Provide the same review prompt and the same target revision.

The purpose is not to make the reviewers agree. Divergent criticism is useful evidence.

Do not revise the note before the other reviewer has seen the same revision unless the review round is intentionally restarted.

### 4. Preserve review output

Preferred method:

- create one GitHub Issue for the review round; or
- preserve each review as a review record file;
- record the reviewed file and commit SHA;
- clearly identify reviewer, date, model/service if known, and source revision.

Example:

```text
reviews/<topic>_<reviewer>_<round>_<date>.md
```

Do not silently edit external criticism when preserving it. If formatting changes are necessary, mark them as formatting-only.

### 5. Verify factual criticisms

Before incorporating criticism, separate:

```text
verified factual issue
conceptual criticism
interpretive disagreement
speculative suggestion
```

Examples requiring verification include:

- a cited reference is supposedly missing;
- a definition is supposedly absent;
- a term allegedly duplicates an existing theory;
- a publication date or version is asserted;
- a mathematical property is attributed to a cited formalism.

External AI review is input to research, not an authority source.

### 6. Re-open the topic with ChatGPT and classify each criticism

Use the collected reviews as adversarial input.

For every substantive criticism, assign a **Disposition** classification first:

```text
valid
partially valid
misunderstanding
needs verification
future work
```

Meaning:

- `valid` — the criticism identifies a real problem that should be corrected or clarified in the current revision.
- `partially valid` — the criticism identifies a real issue, but only part of the claim or proposed remedy is accepted.
- `misunderstanding` — the criticism is based primarily on a misreading, scope mismatch, or conflict with an already explicit definition. Clarification may still be useful if the misunderstanding is likely to recur.
- `needs verification` — the criticism depends on factual, mathematical, bibliographic, implementation, or prior-work claims that must be checked before deciding disposition.
- `future work` — the criticism is useful but extends beyond the scope of the current note or revision and should be preserved rather than forced into the current text.

Record the reason for the classification.

Then assign a separate **Severity / publication-impact** classification:

```text
blocking
recommended
optional
```

Meaning:

- `blocking` — must be resolved before the current version advances to publication, release, or a declared stable milestone.
- `recommended` — materially useful improvement, but not sufficient by itself to block advancement.
- `optional` — non-blocking refinement, preference, edge case, speculative extension, or future-version material.

Examples:

```text
valid + blocking
valid + recommended
partially valid + recommended
misunderstanding + optional
needs verification + blocking
future work + optional
```

Disposition answers **whether the criticism is substantively accepted**.

Severity answers **whether it must stop the current version from advancing**.

The two axes must not be collapsed into one judgment.

### 7. Check criticism perspective, scale, and duplication

Before treating a criticism as a new defect, check:

1. Does it target what the current note actually claims?
2. Is it implicitly demanding a stronger theory than the current note claims to provide?
3. Is it about the present version, or about a possible future version?
4. Does the criticism duplicate or substantially overlap with an already recorded criticism?
5. Is a repeated criticism occurring at the same theoretical position, or after the note has materially changed?

A repeated criticism is not automatically independent evidence.

Likewise:

```text
same-looking criticism
≠
necessarily the same criticism at the same theoretical position
```

Gyro review may revisit similar questions after the note has changed. That revisit should be assessed at the current Slice / scope rather than mechanically copied forward.

This perspective/scale check must not be used to dismiss criticism merely because the reviewer chose a broader viewpoint. It is a guard against scope mismatch and review-loop inflation, not a defense mechanism.

### 8. Commit a disposition record before revising

Before editing the reviewed source, preserve the classification record under `reviews/`.

The disposition record should include at least:

- source file and commit SHA;
- review file / reviewer;
- criticism ID;
- disposition;
- severity;
- duplicate / near-duplicate check;
- factual verification status when relevant;
- rationale;
- whether a current revision is required;
- whether the item is preserved for future work.

Only after this record exists should ChatGPT revise:

```text
ideas/<topic>.md
```

### 9. Independent re-review of the revised note

A revised note should be re-reviewed when:

- a central definition changes;
- a counterexample forces structural revision;
- a new mathematical commitment is introduced;
- a previously provisional concept is about to become fixed;
- a blocking issue was addressed;
- the note is being promoted toward a paper.

A minor wording edit, metadata update, or documented non-blocking limitation does not automatically require a new full review round.

## Convergence / stop criteria

The review loop is **not** required to continue until reviewers have no remaining comments.

A strict reviewer can almost always generate another criticism, so:

```text
no more comments
```

is not a valid convergence criterion.

The current version may normally advance when all of the following are satisfied:

1. No unresolved `blocking` item remains.
2. The current version is internally coherent: its definitions, assumptions, claims, and conclusions do not directly contradict one another.
3. Core factual, mathematical, bibliographic, and implementation-dependent claims classified as `needs verification + blocking` have been checked.
4. Material disagreements between reviewers are recorded rather than hidden.
5. Remaining `recommended`, `optional`, or `future work` items are either addressed or explicitly preserved for later work.
6. A new review round is not merely restating already-resolved criticism without identifying a new blocking defect.

If these conditions are met, further critique should normally be treated as:

```text
refinement
or
input to the next version
```

rather than as a reason to keep the current version open indefinitely.

A version may therefore be publishable while still provisional.

The requirement is not that the theory never change again. The requirement is that the **current version is coherent about what it currently claims**.

Thus:

```text
internal inconsistency in v1
≠
legitimate evolution from v1 to v2
```

A theory or paper may evolve between versions without the earlier version having been a review failure.

## Suggested review states

```text
DRAFT
  ↓
INTERNAL_REVIEW
  ↓
EXTERNAL_REVIEW_PENDING
  ↓
EXTERNAL_REVIEWED
  ↓
REVISION_REQUIRED / REVIEW_ACCEPTABLE
  ↓
PAPER_CANDIDATE
```

`REVIEW_ACCEPTABLE` does not mean that reviewers agreed, that every criticism was fixed, or that the theory is final.

It means that:

- major criticism has been assessed;
- unresolved blocking issues are absent;
- remaining limitations are explicit;
- the current version may reasonably proceed to the next phase.

## Pre-paper gate

Before moving a note from `ideas/` to `paper/`, check:

- [ ] Current source revision is identified.
- [ ] Claude / Claude Code review recorded.
- [ ] Gemini review recorded where required by the project publication plan.
- [ ] Every material criticism has a disposition classification.
- [ ] Every material criticism has a severity classification.
- [ ] No unresolved `blocking` item remains.
- [ ] Factual criticisms independently checked where required.
- [ ] Counterexamples assessed.
- [ ] Existing-theory overlap assessed at least provisionally where material to the current claim.
- [ ] Accepted criticisms incorporated or explicitly deferred with rationale.
- [ ] Remaining ambiguities listed.
- [ ] Fixed versus provisional concepts separated.
- [ ] Duplicate / recurring criticisms checked.
- [ ] Current-version internal consistency checked.
- [ ] Core consistency checked.

## Review strictness and the perfection trap

Reviewers may be instructed to be skeptical or strict. This is useful, but it changes the distribution of comments produced.

A strict reviewer is more likely to surface:

- minor edge cases;
- alternative formulations;
- speculative objections;
- future-theory requirements;
- increasingly narrow loopholes in already-known limitations.

The existence of further criticism alone is therefore **not evidence that the theory is fundamentally defective**.

The workflow must distinguish:

```text
real blocking defect
from
non-blocking refinement
from
future-version research
```

The review process should stop patching one narrow axis when further iterations show diminishing returns and no new blocking defect is being found.

## Version stability versus theory evolution

Gyro notes may explicitly be provisional.

The project therefore distinguishes:

```text
current-version stability
```

from:

```text
permanent immutability of the theory
```

The former is required before publication or promotion. The latter is not.

A paper may state the best stabilized understanding available at one point in the research cycle and later be revised, extended, or replaced by a new version.

This is normal research development, not automatically a contradiction.

## Gyro Logic invariants

The review workflow must not change the invariant Core by process convention:

```text
Structure
↓
Slice
↓
Stability
```

A reviewer may challenge the theory, including the Core, as criticism. Such criticism should be preserved accurately. However, changing the canonical Core remains a separate theoretical decision and must never occur automatically because an external AI suggested it.

## Multi-AI caution

Multiple AI reviews are not statistically independent experiments and should not be treated as consensus proof.

Use them as distinct adversarial readings, not as votes.

When all reviewers agree, still ask:

```text
Is this agreement supported by an argument,
or merely by similar learned conventions?
```

When reviewers disagree, preserve the disagreement rather than averaging it away.

## Project-as-practice note

The Gyro Project review process itself may function as a practical environment for observing iteration, re-evaluation, re-slicing, inherited constraints, and versioned stabilization.

This may provide useful design feedback for the project.

However:

```text
project workflow behaving in a Gyro-like way
≠
proof that Gyro Logic is theoretically correct
```

Operational resemblance is evidence for improving the workflow and generating testable questions, not validation of the theory by itself.
