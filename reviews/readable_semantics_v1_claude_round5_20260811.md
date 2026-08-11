# External Review Record — Readable Semantics v1 — Claude Round 5

## Review metadata

- Topic: `Readable(...)` / `slice-done` relation, focused/split revision
- Source file: `ideas/readable_semantics_v1.md`
- Source commit SHA: `35e85dc0c524e7b61e32c4ff529afd7c181f004c` ("Focus Readable v1 and split retrospective establishment")
- Disposition reviewed: `reviews/readable_semantics_v1_claude_final_gate_disposition_20260811.md` (commit `0732754`)
- Review round: 5 (first review after the manual-Claude final-gate disposition + split revision cycle)
- Review date: 2026-08-11
- Reviewer/service: Claude (Anthropic), reading the repository directly in a working-directory session
- Model/version if known: Claude Sonnet 5
- Review prompt: `reviews/critical_review_prompt.md`

## Source status

- [x] Revised exploratory note
- [ ] Paper candidate
- [ ] Pre-submission manuscript

## Per-item check against the final-gate disposition

| ID | Disposition item | Carried into text? | This round's finding |
|---|---|---|---|
| C1 | `Readable` reduced to explanatory gloss only | Yes — Section 6.1 goes further than requested: "should not be treated as an additional semantic layer or independent theoretical object" | Resolved, no overclaim |
| C2 | v0 supersession status stated | Yes — Section 2, exact structure proposed in the disposition | Resolved |
| C4 | Companion boundary notes referenced | Yes — Section 4 links all three notes | Resolved |
| C5 | Terminology drift (retrospective-*) distinguished | Yes — now lives in `retrospective_establishment_v0.md` Section 8, cross-referenced correctly | Resolved |
| C6 | Split retrospective material into its own note | Yes — clean split, `readable_semantics_v1.md` retains only a pointer (Section 10 footer) | Resolved, improves review focus |
| C3 | Anti-post-hoc discipline made testable | Partially — see finding below | Substantively improved, one new gap identified |

## Finding on C3 — the pressure test is a real advance, with one open loophole

Section 5.1 adds a concrete pressure test: a boundary is placed after `E5` in a log stream, and the discipline distinguishes "Orientation stated only after the boundary was chosen, with no independent supporting record" (disallowed) from "Orientation matches a prior protocol rule that independently predates the boundary" (locally fixed by inherited rule). This is genuine progress over Round 3/4: it converts the previous purely normative statement ("should not be redescribed after the fact") into an evidentiary test — check whether independent, pre-existing evidence (a logged rule, timestamp, declared goal, protocol document) supports the stated Orientation/Context.

**New counterexample — vacuous precommitment.** The test as stated checks only the *temporal priority* of the Orientation/Context statement, not its *constraining specificity*. An Operator can satisfy the letter of the test while still choosing the boundary almost freely:

```text
Operator declares, before observing E1-E8:
  "My Orientation is: place the session boundary wherever seems
   most natural given how the stream unfolds."
```

This declaration genuinely predates every later boundary choice, so it passes the pressure test's temporal check. Yet it imposes essentially no constraint — it is compatible with placing the boundary after `E5`, `E3`, or `E7` equally, so it cannot be used to rule out any candidate boundary after the fact. The test currently has no way to distinguish a vague-but-prior precommitment from a specific-and-prior one, even though only the latter does the falsifying work the discipline is meant to provide.

This does not undo the progress in Section 5.1 — the temporal-priority check is a necessary condition and a real improvement — but it is not sufficient, and the note does not yet say so. Recommend adding one sentence acknowledging that the pressure test currently checks priority, not specificity, and that a precommitment must be specific enough to exclude at least one candidate boundary to do any admissibility work — otherwise it should not count as passing the test.

Status: **accept-for-investigation — this sharpens rather than reopens C3; the note's own Open Question 5 already flags domain-neutral vs. domain-specific checkability, but not this specificity gap specifically**

## Other observations

- No misstatement of prior review history found; the "Duplicate check" sections in the final-gate disposition are accurate against `reviews/readable_semantics_v1_claude_round4_post_disposition_20260811.md` and the Round 3 materials.
- The document does not overclaim `REVIEW_ACCEPTABLE` status for itself — the header correctly reads `REVISION_REQUIRED / POST-CLAUDE-FINAL-GATE-DISPOSITION`, leaving the gate call to external review rather than self-assessing.
- The split into `ideas/retrospective_establishment_v0.md` is reviewed separately in `reviews/retrospective_establishment_v0_claude_round1_20260811.md`.

## Claim-by-claim assessment

| ID | Review criticism | Type | Decision | Reason | Required change |
|---|---|---|---|---|---|
| R5-1 | Pressure test (Sec. 5.1) checks temporal priority of Orientation/Context but not specificity, so a vague prior precommitment vacuously passes | logical / counterexample | accept-for-investigation | vacuous-precommitment counterexample above | add one sentence noting the test requires a *specific*, not merely *prior*, precommitment to do admissibility work |

## Revision outcome

- Updated file: none by this review (critique only, per current role boundary — Claude does not edit `ideas/*.md`)
- Remaining open questions carried forward: general admissibility semantics (still explicitly open per Section 9 point 10 and Open Question 4); domain-neutral checkability of the anti-post-hoc discipline (Open Question 5); literature comparison (Open Question 7)
- New item for next ChatGPT revision pass: close, or explicitly acknowledge, the vacuous-precommitment gap in the pressure test
- Another external review round required?: yes, after the vacuous-precommitment point is addressed or explicitly deferred

## Review gate status

```text
REVISION_REQUIRED
```

Reason: five of six final-gate items are cleanly resolved with no overclaiming. The sixth (C3) made real, checkable progress via the pressure test, but this round surfaces a specific new loophole (vacuous precommitment) in that same mechanism, so the item is not yet closed.

## Layer consistency check

- Gyro Logic theory only: yes
- GyroOS requirements imported?: no
- GyroAuth requirements imported?: no
- Core changed?: no
- If Core challenged by reviewer, preserved as review criticism rather than automatically adopted?: yes (no Core challenge raised)
