# External Review Record — Readable Semantics v0 — Claude Round 2

## Review metadata

- Topic: `Readable(...)` candidate minimal conditions (v0.1)
- Source file: `ideas/readable_semantics_v0.md`
- Source commit SHA: `bf3c073c4f1bde9f1ee8c66db201b1dd82dd812d`
- Review round: 2
- Review date: 2026-08-10
- Reviewer/service: Claude (Anthropic)
- Model/version if known: Claude Sonnet 5
- Review prompt:
  - `reviews/critical_review_prompt.md`

## Source status

- [x] Revised exploratory note
- [ ] Paper candidate
- [ ] Pre-submission manuscript

## External review

Claude judged the revision as still requiring another pass before Paper Candidate status. The main issue is that the current three-condition introduction rule may not be minimal or non-circular.

Primary criticisms:

1. R1 (`Available`) lacks a non-circular structural characterization and may not be independent of R3.
2. R2 (`Articulated`) and R3 (`SelectivelyAddressable`) may be near-synonyms unless separated by worked examples.
3. The vacuity problem removed with `AdmissiblyReferableNext` may reappear inside R3 unless the reference relation is required to be instantiated in the current realization rather than merely possible in principle.
4. Realization scope `ρ` lacks individuation criteria, creating a risk that any apparent contradiction can be dismissed as a different `ρ`.
5. The representation map `π(a)=d` is load-bearing in the human/machine asymmetry example but remains undefined.
6. `Stable ⇒ Readable` depends on Stability/Continuable semantics external to this note and should be verified against the canonical Stability documents.
7. Distributed / holistic representation is a serious counterexample candidate to R3.

## Claim-by-claim assessment

| ID | Review criticism | Type | Decision | Reason / verification | Required change |
|---|---|---|---|---|---|
| CR1 | R1 `Available` is under-characterized / potentially circular | definitional | accept | The current text says locally available without giving a lower-level criterion comparable to R3. | Either give a non-circular characterization or demote `Available` from independent premise. |
| CR2 | R2/R3 may be logically redundant | definitional / logical | accept | `a distinction has formed` and `that distinction can be picked out` are too close without separating examples. | Produce worked examples or collapse conditions. |
| CR3 | R3 may reintroduce vacuity | logical / counterexample | accept | If reference relation need only be possible in principle, the same hypothetical-consumer problem returns. | Require actual instantiation in `ρ`, or remove R3 from minimum conditions. |
| CR4 | `ρ` individuation criteria are missing | definitional | defer / investigate | This is a real falsifiability concern, but complete individuation likely depends on broader formal semantics. | Add a minimum identity sketch or explicit bounded use of `ρ`. |
| CR5 | `π(a)=d` is undefined but load-bearing | definitional | defer | The distinction is useful, but the mapping semantics should not be treated as solved. | Keep P2 provisional; later specify minimum preservation relation. |
| CR6 | P-R7 depends on Continuable/Stability semantics outside this file | prior-work / factual | verify | Requires cross-check against canonical Stability docs. | Verify before preserving as a proposition. |
| CR7 | Distributed / holistic representation may counterexample R3 | counterexample | accept for investigation | Strongly converges with Gemini review. | Add explicit counterexample and reconsider individual addressability. |

## Factual verification

### F1

- Review claim: P-R7 depends on Stability/Continuable semantics not fully defined in this file.
- Verified result: pending repository cross-check.
- Evidence/source: `docs/01_Core_Definitions.md`, `docs/05_Stability_20260504.md`, Minimal Formal Model.
- Status: unresolved

## Counterexamples

### C1 — Distributed / holistic readability

- Counterexample: a distributed latent pattern may be decodable at pattern level although no individual component is selectively addressable as the articulation.
- Target definition/claim: necessity of R3 and articulation-relative single-`a` treatment.
- Does it actually break the claim?: potentially yes. If R3 is widened to pattern-level addressability, the meaning of `a` must also be widened.
- Revision required?: yes.

### C2 — Vacuity replay

- Counterexample: if a merely possible reference relation is enough for R3, a hypothetical relation can always be invented just as a hypothetical downstream consumer could be invented under the discarded condition.
- Target definition/claim: R3 non-vacuity.
- Does it actually break the claim?: yes if possible-in-principle is sufficient; no if an actually instantiated relation in `ρ` is required.
- Revision required?: yes.

## Existing-theory comparison

- Candidate overlapping theory: information-theoretic distinguishability; epistemic accessibilism; distributed representation.
- Similarity: Readability currently relies on accessibility / distinguishability-like conditions.
- Difference: Gyro Logic avoids requiring an epistemic agent and keeps readability Slice/Context/realization-relative.
- Source checked: no dedicated literature review in this round.
- Remaining uncertainty: exact correspondence and whether existing formalisms already supply a cleaner primitive.

## Fix now / keep provisional

### Can be fixed now

- Do not continue presenting R1/R2/R3 as three independently justified minimum conditions.
- Clarify whether any retained reference relation must actually be instantiated in `ρ`.
- Add the distributed / holistic case to formal counterexamples.
- Verify `Stable ⇒ Readable` against the Stability documents.

### Should remain provisional

- Full individuation criteria for `ρ`.
- Formal properties of `π`.
- Full proof-theoretic treatment of Readable.

## Revision outcome

- Updated file: pending
- Revision commit SHA: pending
- Major changes: pending
- Remaining open questions: R1/R2/R3 independence, R3 vacuity, distributed readability, `ρ` individuation, representation mapping `π`, Stability consistency.
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
