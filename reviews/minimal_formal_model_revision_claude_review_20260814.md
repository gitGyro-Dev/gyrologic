# External Review Record — Minimal Formal Model Revision — Claude Review

## Review metadata

- Topic: full-manuscript revision of the published Minimal Formal Model paper (Jxiv DOI `10.51094/jxiv.5641`)
- Source file: `paper/minimal_formal_model_full_en.md`
- Source commit SHA: `80adcd297d84149b6f82d21875477f85d94d9e2f` ("Revise Minimal Formal Model manuscript after review cycle")
- Baseline compared against: `main` at commit `50c76b5` (published/pre-revision manuscript, 3039 lines)
- Revision plan reviewed: `paper/minimal_formal_model_revision_plan_20260814.md` (commit `603313b`)
- Review round: 1 (first review of this manuscript-level revision)
- Review date: 2026-08-14
- Reviewer/service: Claude (Anthropic), reading the repository directly in a working-directory session
- Review prompt: `reviews/critical_review_prompt.md`

## Source status

- [ ] Exploratory note
- [x] Revised exploratory note / manuscript revision
- [ ] Paper candidate
- [ ] Pre-submission manuscript

## Method

Compared `paper/minimal_formal_model_full_en.md` at `main` (3039 lines) against the same file at `revise-minimal-formal-model` (1076 lines, a 65% reduction), section by section, against the scope declared in `paper/minimal_formal_model_revision_plan_20260814.md`. The plan explicitly scopes the revision to ~11 named subsections/items (Abstract, Introduction, Contribution Statement, RQ3–RQ5, §2.3, §4.4, §5.5, §7, the compact integrated schema, Limitations, Conclusion) and lists a separate "Claims expected to remain unchanged" set that should not be rewritten merely for novelty.

## Finding 1 — Sections 11–14 reduced to single-paragraph summaries; none were in the revision plan's scope

### Claim

`§11 Figures`, `§12.2–12.9 Existing Partial Models`, `§13 Comparison with Existing Mathematical Fields`, and `§14 Illustrative Examples` were each compressed from substantial, itemized content to one short paragraph:

| Section | Old | New | Old→New |
|---|---|---|---|
| §11 Figures | 44 lines, 3 worked figures with interpretation notes | 4 lines, no figures | -91% |
| §12.2–12.9 (9 subsections, one per comparison framework) | 46 lines, one paragraph per framework | 4 lines, one merged paragraph | -91% |
| §13 (16 subsections: per-field comparison + composite model + result) | 189 lines | 4 lines | -98% |
| §14 (6 worked examples + cross-example observations) | 171 lines | 8 lines, no examples retained | -95% |

None of these four sections appear in the revision plan's "High-priority sections to revise" list (items 1–11). §12/§13's comparative claims and §14's worked examples are exactly the kind of content the plan's "Claims expected to remain unchanged" section says should not be rewritten for novelty — yet the demonstrations of those claims were deleted outright rather than merely qualified.

### Why this is load-bearing

The paper's claim to have surveyed ~12 mathematical fields and rejected each as an insufficient universal ontology, and to have stress-tested the model against 6 concrete cases (math problem solving, batter→cake, authentication, historical norm formation, missing-data/gaps, negative search), is now *asserted* in one sentence rather than *shown*. A reader or reviewer can no longer check the comparison or examples — only trust the summary conclusion. This is precisely the kind of unsubstantiated-claim gap that motivated the original external critical review.

### Verification of surviving claims

The specific dichotomy claims from "Claims expected to remain unchanged" (stored history, chronological log, metric distance, global closure, etc.) were checked and confirmed still present as stated assertions in the Abstract, Introduction, and Conclusion (`new.md` lines 38–100, 1042). So no claim was silently dropped — but its argument and worked demonstration were removed from the body.

Status: **blocking**

## Finding 2 — Near-uniform ~60–75% compression across sections not named in the revision plan

### Claim

Every major section shrank by roughly the same proportion, regardless of whether it was in scope:

| Section | Old lines | New lines | In revision plan scope? |
|---|---|---|---|
| §3 Structure | 133 | 38 | No |
| §4 Slice | 209 | 132 | Partial (§4.4 only) |
| §5 Stability | 236 | 84 | Partial (§5.5 only) |
| §6 Incorporated Readability | 183 | 58 | No |
| §7 Continuity Readability | 318 | 108 | Yes |
| §8 Trajectory | 242 | 95 | No |
| §9 Difference and Boundary | 236 | 62 | No |
| §10 Integrated schema | 378 | 80 | Yes |

Spot-checked §5 (Stability) and §9 (Difference/Boundary) line-by-line. In both, subsections *not* touched by the plan (e.g. §5.2 scalar-vs-Stability distinction, §5.3 equilibrium/fixed-point discussion, §5.6 residual not-yet, §5.7 neighborhood interpretation, §5.8–5.9 Operator Response boundary and later-Structure transition; §9.1–9.3 Difference-not-Distance/Error/structured-non-coincidence) lost their explanatory prose, motivating counterexamples, and formal notation (e.g. `σ_n`, `U_n ≠ ∅`, `K_n ⇝ q_n ⇝ Γ_{n+1}`, `N(a_n)`, the metric-special-case formula, the "small deviation may be operationally decisive" example), leaving only a bare restated assertion. §5.11 ("Transition to Incorporated Readability") was deleted entirely.

The one exception is §15 (Limitations), which was also compressed (258→115 lines) but where the *actually planned* additions (§15.4 Readability, §15.6 Boundary Admissibility/Anti-Post-Hoc, §15.8 Retrospective Establishment) are substantive, correctly scoped, and non-overclaiming — this section shows what a properly scoped edit looks like, in contrast to the rest of the manuscript.

### Why this matters

This indicates the revision was not executed as a set of targeted edits per the plan, but as a wholesale rewrite/compression pass applied to the entire manuscript. The effect is to turn a formalization-with-argument into a list of bare assertions in sections where nothing about the underlying claim actually changed. This works against the stated revision policy ("preserve claims that survived review... weaken claims whose semantics were shown to be underdetermined") since it also strips the *support* for claims that were never challenged.

Status: **blocking** (for freezing this as the revised manuscript, not for the direction of the targeted edits themselves)

## Positive findings — targeted plan items were implemented correctly

- §4.4: `slice-done` reworded to "local unitization," explicitly does not imply Stability/global closure — matches revision plan item 1, no overclaim.
- §5.5: `Readable(...)` replaced by a domain-relative `EstablishedFor(...)` placeholder, with `Readable_D(...)` offered only as an optional domain-specific instantiation — matches revision plan item 2, no universal predicate reintroduced.
- §15.4/§15.6/§15.8: new Limitations content on incomplete readability semantics, boundary admissibility/anti-post-hoc limits, and retrospective establishment scope — accurately reflects the review history (`readable_semantics_v1_claude_round5/6`, `retrospective_establishment_v0_claude_round1`) without overclaiming a solved criterion.
- Invariant Core (`Structure → Slice → Stability`) unchanged; no Core violation found.

## Claim-by-claim assessment

| ID | Item | Severity | Disposition | Reason | Required change |
|---|---|---|---|---|---|
| MFM1-1 | §11, §12.2–12.9, §13, §14 reduced to one paragraph each, out of revision-plan scope, losing the paper's comparison and worked-example evidence | blocking | valid | these sections were not listed for revision and their content directly supports "Claims expected to remain unchanged" | restore per-field comparison subsections (§12, §13) and worked examples (§14) at something close to original detail; a shortened but itemized form is acceptable, a single summary paragraph is not |
| MFM1-2 | Near-uniform ~60–75% compression in sections outside the plan's scope (§3, §5 minus 5.5, §6, §8, §9), deleting explanatory argument and formal notation | blocking | valid | plan explicitly scopes the revision to named subsections; unscoped sections should be preserved, not compressed | restore the deleted derivations/examples in unflagged sections, or explicitly amend the revision plan to state that broader compression was intended and justify it |

## Fix now / keep provisional

### Can be fixed now

- Restore §12.2–12.9, §13, §14 to itemized (if shortened) form rather than single-paragraph summaries.
- Restore the deleted explanatory/formal content in §3, §5.2/5.3/5.6–5.9, §6, §8, §9 that was not implicated by the Readable/slice-done semantics change.

### Should remain provisional

- The targeted §4.4, §5.5, §15.4/15.6/15.8 changes are correctly scoped as-is and do not need further revision from this review.

## Revision outcome

- Updated file: none by this review (critique only, per current role boundary — Claude does not edit `paper/*.md`)
- Another external review round required?: yes, after the scope-overrun compression is addressed or the revision plan is explicitly amended to justify it

## Review gate status

```text
REVISION_REQUIRED
```

Reason: the two targeted semantic changes (`Readable`, `slice-done`) were implemented correctly and without overclaiming. However, the manuscript as a whole was compressed far beyond the plan's declared scope, deleting the comparative and illustrative evidence (§11–§14) and the explanatory/formal support in several unflagged sections (§3, §5, §6, §8, §9). This is not a Core violation, but it is a real loss of load-bearing material relative to both the published version and the revision plan's own stated boundaries, and should be restored before this branch is treated as the frozen revised manuscript.

## Layer consistency check

- Gyro Logic theory only: yes
- GyroOS requirements imported?: no
- GyroAuth requirements imported?: no
- Core changed?: no
- If Core challenged by reviewer, preserved as review criticism rather than automatically adopted?: yes (no Core challenge raised)
