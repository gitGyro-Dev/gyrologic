# External Review Workflow

## Purpose

This workflow introduces a repeatable external critical-review cycle before exploratory Gyro Logic notes are promoted into paper development.

The process is designed to reduce confirmation bias, self-reference loops, unnoticed ambiguity, and premature formalization.

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

#### 3a. Claude

Open Claude.ai and provide:

1. `reviews/critical_review_prompt.md`;
2. the exact GitHub URL or exact document body under review.

Do not revise the note before the other reviewer has seen the same revision unless the review round is intentionally restarted.

#### 3b. Gemini

Provide the same review prompt and the same target revision.

The purpose is not to make the reviewers agree. Divergent criticism is useful evidence.

### 4. Preserve review output

Preferred method:

- create one GitHub Issue for the review round;
- record the reviewed file and commit SHA;
- add each AI review as a separate comment or preserve it in a review record file;
- clearly identify reviewer, date, model/service if known, and source revision.

Alternative:

```text
reviews/<topic>/<date>_<reviewer>.md
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

### 6. Re-open the topic with ChatGPT

Use the collected reviews as adversarial input.

For every substantive criticism, decide:

```text
accept
partially accept
reject
needs verification
defer
```

Record the reason.

Then update:

```text
ideas/<topic>.md
```

with a new commit.

### 7. Repeat when necessary

Return to external review when:

- a central definition changes;
- a counterexample forces structural revision;
- a new mathematical commitment is introduced;
- a previously provisional concept is about to become fixed;
- the note is being promoted toward a paper.

A minor wording edit does not automatically require a new full review round.

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

`REVIEW_ACCEPTABLE` does not mean that reviewers agreed. It means that major criticism has been assessed and unresolved issues are explicit.

## Pre-paper gate

Before moving a note from `ideas/` to `paper/`, check:

- [ ] Current source revision is identified.
- [ ] Claude review recorded.
- [ ] Gemini review recorded.
- [ ] Factual criticisms independently checked.
- [ ] Counterexamples assessed.
- [ ] Existing-theory overlap assessed at least provisionally.
- [ ] Accepted criticisms incorporated or explicitly deferred.
- [ ] Remaining ambiguities listed.
- [ ] Fixed versus provisional concepts separated.
- [ ] Core consistency checked.

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
