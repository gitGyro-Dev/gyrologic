# External Review Record — Readable Semantics v0 — Gemini

## Review metadata

- Topic: `Readable(...)` candidate minimal semantics
- Source file: `ideas/readable_semantics_v0.md`
- Source commit SHA: `bf3c073c4f1bde9f1ee8c66db201b1dd82dd812d`
- Review round: 1
- Review date: 2026-08-10
- Reviewer/service: Gemini
- Model/version if known: not provided
- Review prompt:
  - `reviews/critical_review_prompt.md`

## Source status

- [x] Revised exploratory note
- [ ] Paper candidate
- [ ] Pre-submission manuscript

## External review

The review judged the current revision positively overall, especially the removal of downstream-consumer dependence, the separation of readability from truth/correctness, and the use of realization scope instead of introducing a primitive Reader.

The main criticisms were:

1. `SelectivelyAddressable` may be circular with `Readable`.
2. Distributed / holistic representations may be readable without discrete selective addressability.
3. `Available`, `Articulated`, and `SelectivelyAddressable` may not be independent minimal conditions.

The review recommended strengthening the non-circular characterization of `SelectivelyAddressable`, testing boundary cases where only two of the three candidate conditions hold, and formally testing distributed representations.

## Claim-by-claim assessment

| ID | Review criticism | Type | Decision | Reason / verification | Required change |
|---|---|---|---|---|---|
| GR1 | `SelectivelyAddressable` may be a restatement of `Readable` | definitional | accept for investigation | This is already an acknowledged pressure point and is load-bearing for the introduction rule. | Test whether R3 can be removed or replaced by a lower-level non-circular condition. |
| GR2 | Distributed / holistic representation may break R3 | counterexample | accept for investigation | Strong counterexample candidate; discrete addressability may be too restrictive. | Add a formal counterexample section and test pattern-level readability. |
| GR3 | R1/R2/R3 may be redundant | logical / definitional | accept for investigation | If R3 implies R1 and R2, the three-condition rule is not minimal. | Produce worked examples separating the conditions or collapse redundant conditions. |
| GR4 | Downstream-consumer removal improves the model | logical | accept | The broken-actuator and unused-result cases support this revision. | Preserve unless later counterexamples overturn it. |
| GR5 | `Readable ⇏ True / Correct` is an important separation | logical | accept | Fits current Gyro interpretation of local establishment and later Re-Slice. | Preserve as a candidate proposition. |
| GR6 | Realization scope is preferable to a primitive Reader | definitional | partial | Useful, but later reviewer pressure may require individuation criteria for `ρ`. | Keep provisional and define realization identity later. |

## Factual verification

No external factual claims were relied upon strongly enough to require immediate verification in this review. The neural/distributed-representation example is treated as a counterexample candidate, not as an established empirical claim.

## Counterexamples

### C1 — Distributed representation

- Counterexample: A pattern is represented across a distributed latent state and is decodable as a whole without a single discrete addressable component corresponding to the articulation.
- Target definition/claim: necessity of `SelectivelyAddressable`.
- Does it actually break the claim?: potentially yes, depending on whether addressability is allowed at pattern/set level.
- Revision required?: yes, if R3 is retained as necessary.

### C2 — Two-of-three boundary cases

- Counterexample family: construct cases satisfying only two of `Available`, `Articulated`, `SelectivelyAddressable`.
- Target definition/claim: independence and minimality of R1/R2/R3.
- Does it actually break the claim?: to be tested.
- Revision required?: likely.

## Existing-theory comparison

- Candidate overlapping theory: distinguishability / accessibility / distributed representation
- Similarity: Readability may depend on local discriminability rather than explicit symbolic addressability.
- Difference: Gyro Logic keeps the relation local, Slice-relative, and non-truth-theoretic.
- Source checked: none in this review record.
- Remaining uncertainty: exact correspondence to information-theoretic or representational frameworks remains open.

## Fix now / keep provisional

### Can be fixed now

- Add the distributed / holistic counterexample explicitly.
- Stop treating R1/R2/R3 as independently justified until worked examples demonstrate independence.
- Reconsider `SelectivelyAddressable` as a necessary condition.

### Should remain provisional

- Exact mathematical type of Readable.
- Whether pattern-level discriminability replaces addressability.
- Exact realization-scope semantics.

## Revision outcome

- Updated file: pending
- Revision commit SHA: pending
- Major changes: pending
- Remaining open questions: R1/R2/R3 independence; non-circular R3; distributed readability.
- Another external review round required?: yes

## Review gate status

```text
REVISION_REQUIRED
```

Current status: `REVISION_REQUIRED`

## Layer consistency check

- Gyro Logic theory only: yes
- GyroOS requirements imported?: no
- GyroAuth requirements imported?: no
- Core changed?: no
- If Core challenged by reviewer, preserved as review criticism rather than automatically adopted?: yes
