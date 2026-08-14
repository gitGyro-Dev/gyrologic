# External Review Record — Minimal Formal Model Revision — Claude Round 2

## Review metadata

- Topic: full-manuscript revision of the published Minimal Formal Model paper (Jxiv DOI `10.51094/jxiv.5641`)
- Source file: `paper/minimal_formal_model_full_en.md`
- Source commit SHA: `da0cbfb7d770ad82a2af3590b0a7b59025fb3539` ("Apply targeted Minimal Formal Model revisions to published manuscript")
- Prior commit reviewed: `e7073c9c0f93bba675241bfb60ffe3b3183d1e08` ("Restore published manuscript before targeted revision")
- Round 1 review: `reviews/minimal_formal_model_revision_claude_review_20260814.md` (commit `12ba7eb`)
- Baseline compared against: `main` at commit `50c76b5` (3039 lines)
- Review round: 2
- Review date: 2026-08-14
- Reviewer/service: Claude (Anthropic), reading the repository directly in a working-directory session
- Review prompt: `reviews/critical_review_prompt.md`

## Source status

- [x] Revised exploratory note / manuscript revision
- [ ] Paper candidate
- [ ] Pre-submission manuscript

## Check against Round 1 findings

| ID | Round 1 finding | Resolved? |
|---|---|---|
| MFM1-1 | §11–14 reduced to one paragraph each | **Yes.** §11 (2192–2236), §12 (2236–2330), §13 (2330–2519), §14 (2519–2690) fully restored — all figures, all 9 comparison-framework subsections, all 16 field comparisons, and all 6 worked examples are present at essentially original length (68 diff lines out of ~330 in this range, all wording-level). |
| MFM1-2 | Near-uniform ~60–75% compression outside plan scope (§3, §5 minus 5.5, §6, §8, §9) | **Yes.** §3 is byte-identical to `main`. §5, §6, §8, §9 retain their full explanatory prose and formal notation; the only changes are targeted word-level substitutions (`readable` → `usable` / `established` / domain-relative subscripted predicates) propagated consistently to sections that depend on the weakened `Readable` semantics. No paragraph-level deletion found. |

Total file: 3039 → 3124 lines (net **growth**, not reduction), consistent with the new Limitations content (§15.4, §15.6) while everything else is preserved.

## New check — did the "readable → usable/established" propagation introduce inconsistency?

Spot-checked §6 (Incorporated Readability), §8 (Trajectory), §9 (Difference/Boundary): the substitutions are consistent with the §5.5 formal change (canonical `Readable` retained as explanatory word; `Readable(...)` no longer asserted as a universal predicate). No section reintroduces `Readable(...)` as an unqualified universal predicate. §9.6's formal Boundary condition correctly drops the `Readable(d;...)` conjunct in favor of an unqualified functional statement plus a note that a domain model may supply a stronger condition — consistent with round 1's finding on §5.5.

No new counterexample or inconsistency found in this pass.

## Claim-by-claim assessment

| ID | Item | Decision | Reason | Required change |
|---|---|---|---|---|
| MFM2-1 | §11–14 restoration | resolved | full content restored at original scope | none |
| MFM2-2 | Unflagged-section compression (§3/§5/§6/§8/§9) | resolved | full prose and notation restored; only targeted wording substitution remains | none |

## Revision outcome

- Updated file: none by this review (critique only)
- Another external review round required?: not for the scope-overrun issue; a normal review round would still be appropriate before this branch is merged into `main` and treated as the new published-revision candidate, per standard practice (independent Gemini pass, human confirmation).

## Review gate status

```text
REVIEW_ACCEPTABLE
```

Reason: both Round 1 findings are resolved without overclaiming — the manuscript's comparative and illustrative evidence (§11–14) and its unflagged explanatory sections are fully restored, while the intended `Readable`/`slice-done` semantic weakening is now consistently and correctly propagated where relevant. No Core violation. No new blocking finding from this round.

## Layer consistency check

- Gyro Logic theory only: yes
- Core changed?: no
