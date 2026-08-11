# External Final Review Record — Readable Semantics v1 / Retrospective Establishment v0 — Claude

Date: 2026-08-12
Reviewer/service: Claude (manual review provided by user)
Target layer: Gyro Logic
Source status: ideas-stage review

## Overall assessment

No fatal contradiction requiring modification of the invariant Core was identified.

The review notes that the recent notes have progressively narrowed their claims, and that the v0 formal decomposition (`Available ∧ Articulated ∧ SelectivelyAddressable`) has been explicitly superseded in v1 while being preserved as review history. The reviewer considers that rollback healthy.

Invariant Core remains:

```text
Structure → Slice → Stability
```

## 1. Newly identified major issues

### A. Missing anti-post-hoc discipline for inherited-boundary provenance

`readable_semantics_v1.md` currently restricts post-hoc redescription of Orientation / Context after a boundary has already been selected.

However, `local_establishment_boundary_origin_20260810.md` separately describes boundary origin using working categories such as:

- A: immediate/current Operator placement;
- B: inherited protocol boundary;
- C: inherited institutional boundary;
- D: event-side influence.

The review identifies a remaining loophole:

> An Operator could avoid the Orientation/Context anti-post-hoc discipline by claiming only after the boundary has been chosen that the boundary was not an immediate judgment at all, but instead inherited from a prior protocol or institution.

In that case, the content of Orientation/Context has not necessarily been redescribed; instead, the claimed **provenance category of the boundary** has been changed or introduced after the fact.

The current anti-post-hoc test does not explicitly constrain this provenance claim.

Suggested future response options:

1. Extend the discipline so that a claimed inherited source (protocol, institution, prior rule, etc.) must itself have independently existing support rather than being introduced only after the boundary choice; or
2. Record this explicitly as an open question / future-work limitation.

This is identified as the highest-priority item before any `PAPER_CANDIDATE` promotion, but it does not block stopping at the current ideas-note stage.

### B. Review-state metadata inconsistency

The reviewer notes that the ideas-note headers still reportedly contain revision-required / post-disposition states even though the latest Claude Code review reported `REVIEW_ACCEPTABLE`.

This appears to be a process / metadata issue rather than a theoretical defect.

Before promotion to a later review gate, the metadata should be checked and synchronized with the actual review record.

## 2. Known but unresolved issues already acknowledged by the documents

### Weak admissibility threshold

The `readable_semantics_v1.md` pressure test currently requires a prior framing to be sufficiently specific to exclude at least one plausible candidate boundary.

The reviewer agrees that this remains a weak threshold but treats it as a known limitation rather than a new blocking defect. The document already states that this is not a universal specificity metric, and the broader admissibility problem remains open.

### Reliability of retrospective establishment

`retrospective_establishment_v0.md` still does not provide a general reliability criterion distinguishing a well-supported present establishment about the past from a merely plausible story.

The scorch-mark / multiple-cause counterexample provides a useful pressure test, but no general sufficiency principle has yet been established.

This is intentionally open and acceptable at the ideas-note stage.

### `Readable` versus `slice-done`

No independently validated operational distinction is currently demonstrated.

The current v1 treatment explicitly reduces `Readable` to explanatory wording around `slice-done`, so this is not treated as a hidden contradiction, but remains an open terminological/theoretical question.

## 3. Future work that may remain deferred

The reviewer considers the following appropriate to defer:

- relation between retrospective establishment and Trajectory / Incorporated Readability;
- comparison with telicity, aspect, boundedness, event semantics, and process philosophy;
- comparison of retrospective establishment with historical geology methodology and inference to the best explanation / abduction;
- proof of completeness or exclusivity for the current boundary-origin taxonomy.

No novelty claim is currently being made in those areas, so deferral is acceptable.

## 4. Misunderstanding / over-reading cautions

### v0 and v1 should not be read as simultaneous active semantics

The v0 formal conditions and proposition set have been explicitly superseded as the active model while preserved as historical review material.

Apparent conflicts between v0 formal claims and the narrower v1 position should therefore be treated as version evolution, not automatically as simultaneous contradiction.

### Fixed criterion study does not reject determinism

The fixed-criterion / done-boundary work should not be summarized as claiming that fixed criteria do not exist.

The relevant distinction is between deterministic judgment inside a locally selected frame and the broader question of where that local establishment / boundary comes from.

### Earthquake example is not a geology novelty claim

The retrospective-establishment note uses geology as an example but does not claim a new contribution to geology.

It explicitly leaves comparison with existing historical-geology and abductive methodology for later work.

## 5. Gate assessment

The reviewer considers it reasonable to stop these documents at the current **ideas-note** stage.

Reasons include:

- no Core modification is required;
- the earlier over-formalized Readable decomposition has been explicitly rolled back;
- the notes increasingly state what they do not claim;
- unresolved issues are generally visible as open questions rather than hidden assumptions;
- no major unacknowledged conceptual leap was identified other than the inherited-boundary provenance loophole above.

Before advancing toward `PAPER_CANDIDATE`, the inherited-boundary provenance / anti-post-hoc issue should at least be explicitly recorded or minimally constrained.

## Final review status

```text
IDEAS_STAGE_ACCEPTABLE
```

with one priority follow-up before paper-candidate promotion:

```text
anti-post-hoc provenance check for inherited boundaries
```

No revision was performed as part of this review record. The next revision/disposition cycle is intentionally deferred.
