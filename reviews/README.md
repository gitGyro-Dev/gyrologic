# External Critical Review

This directory manages external AI-assisted critical review for Gyro Logic working notes before paper drafting.

The goal is to prevent the theory from being refined only through one conversational path or one model's internal framing.

Documents in this directory are **review-process artifacts**, not canonical Gyro Logic definitions.

## Intended lifecycle

```text
ChatGPT wall-bouncing / idea organization
        ↓
ideas/<topic>.md
        ↓
external critical review
  ├─ Claude
  └─ Gemini
        ↓
review record / GitHub Issue
        ↓
revision with ChatGPT
        ↓
ideas/<topic>.md update
        ↓
repeat review if necessary
        ↓
review gate passed
        ↓
paper candidate
```

## Recommended directory roles

```text
ideas/
  exploratory theory notes before paperization

reviews/
  review process, prompts, templates, and review records

paper/
  manuscript candidates after sufficient review
```

## Review principle

External review is not a voting mechanism.

Agreement among multiple AI systems does not establish truth or validity. Review is used to expose:

- logical contradictions;
- ambiguous definitions;
- hidden assumptions;
- overlap with existing theories;
- counterexamples;
- overgeneralization;
- weak falsifiability;
- premature fixation of provisional concepts.

A criticism should be checked against the actual source document before being accepted. Factual claims about references, definitions, dates, or repository contents must be verified independently.

## Paperization gate

A note may become a paper candidate when:

1. its central definitions and distinctions are explicit;
2. major contradictions identified by review have been resolved or documented;
3. important counterexamples have been tested;
4. relation to existing theory has been checked at least provisionally;
5. unresolved points are clearly separated from fixed points;
6. at least two independent external reviews have been recorded;
7. review comments have been assessed rather than merely copied into the theory.

Passing this gate does not imply that the theory is correct. It only means that the note is sufficiently disciplined to enter manuscript development.

## Files

- `critical_review_prompt.md` — fixed prompt for Claude, Gemini, or other external reviewers.
- `review_workflow.md` — operational review cycle.
- `review_record_template.md` — template for preserving reviews and responses.

## Layer consistency

This directory belongs to research-process governance around Gyro Logic.

It does not alter the invariant Core:

```text
Structure
↓
Slice
↓
Stability
```

GyroOS and GyroAuth implementation requirements must not be imported into Gyro Logic through the review process.
