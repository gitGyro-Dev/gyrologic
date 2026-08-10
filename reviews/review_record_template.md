# External Review Record Template

## Review metadata

- Topic:
- Source file:
- Source commit SHA:
- Review round:
- Review date:
- Reviewer/service:
- Model/version if known:
- Review prompt:
  - `reviews/critical_review_prompt.md`

## Source status

- [ ] Exploratory note
- [ ] Revised exploratory note
- [ ] Paper candidate
- [ ] Pre-submission manuscript

## External review

Paste the external review below without substantive rewriting.

---

<external review>

---

## Claim-by-claim assessment

| ID | Review criticism | Type | Decision | Reason / verification | Required change |
|---|---|---|---|---|---|
| R1 |  | logical / factual / definitional / prior-work / counterexample / generalization / other | accept / partial / reject / verify / defer |  |  |

## Factual verification

For each factual criticism, record the verification source separately.

### F1

- Review claim:
- Verified result:
- Evidence/source:
- Status: confirmed / contradicted / unresolved

## Counterexamples

### C1

- Counterexample:
- Target definition/claim:
- Does it actually break the claim?:
- Revision required?:

## Existing-theory comparison

- Candidate overlapping theory:
- Similarity:
- Difference:
- Source checked:
- Remaining uncertainty:

## Fix now / keep provisional

### Can be fixed now

- 

### Should remain provisional

- 

## Revision outcome

- Updated file:
- Revision commit SHA:
- Major changes:
- Remaining open questions:
- Another external review round required?: yes / no

## Review gate status

```text
DRAFT
INTERNAL_REVIEW
EXTERNAL_REVIEW_PENDING
EXTERNAL_REVIEWED
REVISION_REQUIRED
REVIEW_ACCEPTABLE
PAPER_CANDIDATE
```

Current status:

## Layer consistency check

- Gyro Logic theory only:
- GyroOS requirements imported?: no / yes
- GyroAuth requirements imported?: no / yes
- Core changed?: no / yes
- If Core challenged by reviewer, preserved as review criticism rather than automatically adopted?: yes / no
