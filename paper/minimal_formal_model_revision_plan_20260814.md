# A Minimal Formal Model for Gyro Logic — Revision Plan

Date: 2026-08-14
Target: `paper/minimal_formal_model_full_en.md`
Published reference: Jxiv DOI `10.51094/jxiv.5641`
Status: Revision planning / pre-manuscript update

## Purpose

This revision updates the published Minimal Formal Model in light of the multi-AI review cycle and the subsequent focused studies on `Readable`, `slice-done`, local-establishment boundaries, and retrospective establishment.

The objective is not to replace the paper with a new theory and not to modify the invariant Core:

```text
Structure → Slice → Stability
```

The objective is to bring the manuscript into line with the current, narrower and better-scoped interpretation of several provisional concepts while preserving the paper's role as an exploratory formalization.

## Revision policy

The revision should preserve claims that survived review, weaken claims whose semantics were shown to be underdetermined, and explicitly move unresolved questions into limitations / future work rather than manufacturing stronger definitions.

The revised manuscript should remain a revision of the same paper rather than a new standalone preprint unless the revision produces a substantively new independent contribution.

## Required manuscript changes

### 1. `slice-done` and local articulation

Current manuscript wording treats `slice-done` primarily as the point at which a local articulation becomes available.

The revised manuscript should clarify that:

- Slice remains an unfolding process;
- a local articulation is distinguishable from the process itself;
- `slice-done` is best treated as the local unitization by which an Operator, under current Orientation and Context or an inherited frame, treats a range of the unfolding Slice as one local establishment;
- the underlying event or process may continue after this local unitization;
- `slice-done` does not imply Stability, global closure, irreversible completion, or objective termination of the underlying event.

This clarification must not insert a new Core element between Slice and Stability.

### 2. `Readable` should be weakened as an independent formal object

The current manuscript uses `Readable(...)` in several formal expressions and treats readability as a necessary condition for Stability and Continuity Readability.

The post-publication review cycle did not establish a stable independent operational semantics for `Readable`. The active working position is narrower:

- `Readable` is not a fourth Core element;
- no independently validated operational distinction between `Readable` and the local-establishment condition around `slice-done` is currently demonstrated;
- `Readable` should therefore be treated as provisional explanatory / relational wording unless a domain-specific model supplies a justified semantics;
- earlier candidate decompositions of Readable are historical exploration, not active universal semantics.

Accordingly, the revised manuscript should avoid presenting `Readable(...)` as if it were already a universally defined predicate.

Where a formal expression currently contains `Readable`, the manuscript should either:

1. qualify it explicitly as a domain-relative placeholder relation; or
2. rewrite the expression so the formal commitment is to an establishment / continuity condition rather than to a universal Readable predicate.

No universal necessary-and-sufficient definition should be introduced in this revision.

### 3. Stability must remain distinct from `slice-done`

The revised manuscript must preserve:

```text
Slice process
≠
local articulation / local unitization
≠
Stability
```

The weakening of `Readable` must not collapse Stability into `slice-done`.

Stability remains the state in which an opened path can be treated as an establishment that can continue. The manuscript may continue to use a structured Stability Scene as a provisional formal candidate.

### 4. Boundary origin and anti-post-hoc limitation

The revised manuscript should acknowledge that local-establishment boundaries may arise from different sources, including:

- current Operator judgment;
- inherited protocol or rule;
- institutional criteria;
- strong event-side transitions or constraints.

A boundary may be locally fixed while still having a history.

The manuscript should also record, at least as a limitation / methodological constraint, that Operator-relativity and inherited-boundary claims must not be used as unrestricted post-hoc rescue mechanisms.

The current review cycle leaves full boundary-admissibility semantics open. In particular:

- temporal priority alone is not a sufficient admissibility condition;
- a prior frame that constrains no plausible alternative does little evaluative work;
- the claimed provenance of an inherited boundary can itself be asserted post hoc unless independently supported.

This revision should document these limits without attempting a universal admissibility theorem.

### 5. Retrospective establishment

The revised manuscript should not promote `retrospective establishment` into a new primitive or Core element.

The paper already allows retrospective reinterpretation, Re-Slice, gaps, and later contextual tracing. The revision should add a focused distinction where useful:

```text
past event itself
≠
present establishment about that past event
```

and note that:

```text
a remaining trace may support retrospective establishment
≠
a single trace is sufficient to uniquely determine the past event
```

This belongs primarily in discussion / limitations / future work unless the integrated model requires a local clarification.

The relation to Trajectory, Incorporated Readability, abduction / IBE, historical geology, forensic reasoning, and historiographical method remains open.

### 6. Minimality language

The manuscript already states that no formal proof of unique / cardinal / ordered minimality is provided.

The revision should make this limitation visible earlier, especially in the Abstract and Introduction.

`Minimal` should be stated to mean:

> an exploratory set of minimum formal commitments currently judged sufficient to preserve the intended Gyro distinctions,

not a proven mathematically unique minimal theory.

### 7. Incorporated Readability and Trajectory

These sections should largely be preserved.

The review cycle strengthened, rather than overturned, the paper's distinctions:

```text
stored history
≠
Incorporated Readability
```

and:

```text
relation-bearing field
≠
Trajectory
```

However, wording that depends on a universal semantics of `Readable` should be reviewed and qualified.

The existing non-monotonic update, revision, invalidation, loss of accessibility, branching, merging, gaps, retrospective reinterpretation, and Re-Slice claims remain compatible with the current theory.

## High-priority sections to revise

1. Abstract
2. Introduction
3. Contribution Statement
4. RQ3 / RQ4 / RQ5 wording where readability is treated too strongly
5. Section 2.3 Minimal Formal Commitments
6. Section 4.4 Slice-ing and Slice-done
7. Section 5.5 Readability and Continuability
8. Section 7 Continuity Readability formulas using `Readable(...)`
9. Compact integrated schema where `Readable(...)` appears as if fully defined
10. Limitations — readability, admissibility, boundary provenance, retrospective reconstruction, minimality
11. Conclusion

## Claims expected to remain unchanged

The following should not be rewritten merely for novelty:

- invariant Core `Structure → Slice → Stability`;
- canonical definitions unless a separate canonical-theory decision is made;
- Slice is processual and not universally extraction / filtering / projection;
- Slice process ≠ local articulation;
- local articulation ≠ Stability;
- Stability is not universally a scalar / equilibrium / fixed point / terminal state;
- local Stability does not imply global closure of Structure;
- Stability does not decide Operator Response;
- Incorporated Readability ≠ stored history;
- Identity ≠ Continuity Readability;
- Trajectory ≠ chronological log / predefined state sequence;
- Difference ≠ metric distance ≠ numerical error ≠ Boundary;
- formal notation remains supporting and non-canonical.

## Review provenance

Primary post-publication materials informing this revision include:

```text
ideas/readable_semantics_v1.md
ideas/retrospective_establishment_v0.md
ideas/operator_done_boundary_constraints_20260810.md
ideas/fixed_criterion_vs_done_boundary_checksum_death_20260810.md
ideas/local_establishment_boundary_origin_20260810.md
reviews/readable_semantics_v1_claude_round3_disposition_20260811.md
reviews/readable_semantics_v1_claude_final_gate_disposition_20260811.md
reviews/readable_semantics_v1_claude_round5_disposition_20260811.md
reviews/readable_semantics_v1_claude_final_review_20260812.md
reviews/review_perspective_scale_note_20260812.md
```

## Publication sequence after revision

Proposed sequence:

```text
English manuscript revision
↓
internal consistency / source-impact review
↓
Multi-AI critical review gate
↓
Disposition + severity
↓
revised English manuscript frozen
↓
PDF regeneration and validation
↓
Jxiv revision / revised publication decision
↓
Japanese edition produced from the frozen revised English manuscript
```

The Japanese edition should not be generated from the superseded English wording if the English revision materially changes the Readable / slice-done structure.

## Gate for this revision

The manuscript does not need to solve every open question before revision publication.

The revision may advance when:

- no unresolved blocking contradiction remains;
- the manuscript accurately distinguishes active claims from provisional placeholders;
- `Readable` is no longer presented more strongly than current review supports;
- `slice-done` / local unitization and Stability remain non-collapsed;
- boundary-admissibility limitations are explicit;
- retrospective-establishment claims remain scoped;
- remaining recommended / optional / future-work items are recorded.
