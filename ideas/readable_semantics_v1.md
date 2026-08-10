# Readable Semantics v1

Date: 2026-08-10
Status: Revised idea draft / external-review response
Target layer: Gyro Logic
Review state: REVISION_REQUIRED / ROUND_2_PREP

## 1. Purpose

This document revises `ideas/readable_semantics_v0.md` in response to the first external review cycle from Gemini and Claude.

It remains exploratory and non-canonical. It does not modify the invariant Core:

```text
Structure → Slice → Stability
```

The purpose of v1 is narrower than v0:

> determine whether `Readable(...)` can be characterized without circularity, without importing downstream execution topology, and without making the relation unfalsifiably realization-relative.

The main review findings addressed here are:

1. `Available`, `Articulated`, and `SelectivelyAddressable` may not be independent conditions;
2. `SelectivelyAddressable` may merely restate `Readable`;
3. hypothetical reference relations may recreate the vacuity problem previously removed with `AdmissiblyReferableNext`;
4. distributed or holistic representations may be readable without a discrete addressable articulation;
5. the realization scope `ρ` needs at least a minimal individuation discipline;
6. representation transfer `π(a)=d` must not silently equate internal and displayed articulations.

---

## 2. Review outcome adopted in v1

The v0 candidate rule was:

```text
Available(a; ρ)
∧ Articulated(a; ρ)
∧ SelectivelyAddressable(a; ρ)
⇒ Readable(a; ρ)
```

This is no longer retained as the primary introduction-rule candidate.

The reviews correctly identified that the three conditions may be mutually entangled:

```text
Available
Articulated
SelectivelyAddressable
```

may be three descriptions of one local transition rather than three logically independent premises.

Therefore v1 does **not** treat them as three axioms whose independence is assumed.

Instead, v1 separates:

```text
formation
availability-to-the-realization
local discriminability
```

as analytical questions to be tested independently before any formal introduction rule is restored.

---

## 3. Revised strongest working statement

The current safest statement is now:

```text
Readable(a; ρ)
```

holds when articulation or relation `a` has become locally discriminable within realization `ρ` in a form that is available to that realization as a determinate local establishment.

Japanese working reading:

```text
Readableとは、特定のarticulationまたはrelationが、
あるrealization ρ の中で、未分化な他の可能性から局所的に区別可能となり、
そのrealizationにとって一つの局所的成立として利用可能な形になった、
という条件相対的な判断である。
```

This is still a working characterization, not a canonical definition.

The important revision is that v1 avoids making `addressability` itself a primitive requirement.

---

## 4. Why `SelectivelyAddressable` is removed from the minimum rule

Gemini and Claude independently identified the same weakness:

```text
SelectivelyAddressable(a)
```

may collapse into:

```text
Readable(a)
```

because "can be picked out as this distinction" is already close to saying that the distinction is readable.

There is a second problem.

If `SelectivelyAddressable` means merely:

```text
some reference relation could in principle be constructed
```

then the condition is vacuous, because hypothetical reference relations can always be invented.

If instead it means:

```text
an actually instantiated reference relation already exists in ρ
```

then Readable risks becoming dependent on explicit process topology or representation machinery, reproducing part of the problem previously found in `AdmissiblyReferableNext`.

Therefore v1 treats addressability as a possible **derived property** of some readable articulations, not as a universal minimum condition.

---

## 5. Revised analytical distinctions

### 5.1 Formation

A local distinction may begin to form during Slice.

```text
Formation(a; ρ)
```

means only that the current process contains organization compatible with a candidate articulation.

Formation does not yet imply Readable.

A weak or unstable pattern may be forming while remaining unresolved.

### 5.2 Availability to the realization

To avoid circular use of the word `available`, v1 adopts a narrower structural characterization.

Provisionally:

```text
PresentTo(a; ρ)
```

means that the current realization contains sufficient realized support for `a` such that the distinction is part of the realization's current local organization rather than merely a possible feature of the wider Structure.

This does not mean:

- stored in memory;
- symbolically named;
- visible to a human;
- successfully consumed downstream;
- true or correct.

It means that `a` has entered the realized local scene.

This gives a candidate separation:

```text
ExistsInStructure(a) ⇏ PresentTo(a; ρ)
```

### 5.3 Local discriminability

The key v1 candidate is:

```text
LocallyDiscriminable(a; ρ)
```

which means that within realization `ρ`, the support for `a` is sufficiently organized that `a` is not merged with all relevant alternatives as one undifferentiated remainder.

This definition deliberately avoids requiring:

- a unique symbol;
- a unique memory address;
- a single neuron or feature;
- a discrete object boundary;
- an explicit reader;
- an actual downstream consumer.

This makes the condition compatible with distributed or holistic representations.

A distributed pattern may be locally discriminable at the level of a population, field, relation, manifold region, activation configuration, or other domain-specific structure.

Thus:

```text
LocallyDiscriminable
≠
individually addressable by one token or location
```

---

## 6. Candidate minimum relation v1

At this stage the strongest candidate is reduced to:

```text
Readable(a; ρ)
⇒ PresentTo(a; ρ) ∧ LocallyDiscriminable(a; ρ)
```

The converse is an explicit hypothesis to test:

```text
PresentTo(a; ρ) ∧ LocallyDiscriminable(a; ρ)
?⇒ Readable(a; ρ)
```

v1 does not yet promote this converse to a theorem or formal introduction rule.

The central question for the next review round is:

> Can an articulation be present to a realization and locally discriminable, yet still intuitively fail to count as Readable?

If yes, a third condition is required.

If no robust counterexample is found, the two-condition form may be closer to the minimal semantics than v0's three-condition form.

---

## 7. Worked independence tests

The reviews requested concrete examples where candidate conditions separate.

### Case A — support present, not discriminable

A weak sensor pattern is physically represented in the current processing field, but noise and overlapping alternatives prevent any local discrimination.

```text
PresentTo(a; ρ) = true
LocallyDiscriminable(a; ρ) = false
```

Candidate result:

```text
Readable(a; ρ) = false
```

This separates presence-to-realization from discriminability.

### Case B — distinction exists in Structure, not present to the realization

A security event exists in the underlying log archive, but the current Slice does not load, expose, or otherwise realize any support for it.

```text
ExistsInStructure(a) = true
PresentTo(a; ρ) = false
```

Candidate result:

```text
Readable(a; ρ) = false
```

This preserves the earlier separation:

```text
Exists ⇏ Readable
```

### Case C — discriminability at a distributed level

A neural representation encodes a class-relevant distinction across a distributed activation pattern. No single component uniquely identifies the class, but the population configuration separates one pattern family from another.

At the population-level articulation:

```text
LocallyDiscriminable(a_population; ρ) = true
```

without requiring:

```text
SelectivelyAddressable(single_unit; ρ)
```

This is intended to remove the discrete-addressability bias of v0.

### Case D — provisional articulation during transition

A visual pattern begins to organize as a moving object, but competing organizations remain unresolved and the distinction cannot yet be locally separated.

```text
Formation(a; ρ) = true
PresentTo(a; ρ) = true
LocallyDiscriminable(a; ρ) = false
```

Candidate result:

```text
Readable(a; ρ) = false
```

This gives a more explicit boundary case between slice-ing and a readable articulation.

---

## 8. Readable remains separate from truth and correctness

The v0 conclusion is retained:

```text
Readable(a; ρ) ⇏ True(a)
Readable(a; ρ) ⇏ Correct(a)
```

A misrecognized ball may still be locally discriminable and present as the current articulation.

Later Re-Slice may revise the articulation without requiring the earlier readability judgment to be reinterpreted as having never occurred.

This remains important because Readable must not become a hidden truth predicate.

---

## 9. Readable remains separate from downstream use

The v0 pressure test is also retained.

```text
Readable(a; ρ)
```

must not require:

```text
ActualDownstreamConsumption(a)
```

or:

```text
SuccessfulDownstreamExecution(a)
```

or merely hypothetical future consumers.

A measurement, diagnostic result, mathematical intermediate result, or observation may be readable even if no later process uses it.

Thus:

```text
Readable
≠ downstream participation
≠ continuation
```

This preserves the distinction with Stability.

---

## 10. Readable and Stability

The current Gyro Logic interpretation remains:

```text
Stability is the state in which an opened path becomes readable as an establishment that can continue.
```

Therefore the following remains a strong cross-document candidate:

```text
Stable(a; ρ) ⇒ Readable(a; ρ)
```

while generally:

```text
Readable(a; ρ) ⇏ Stable(a; ρ)
```

v1 explicitly marks this as a **cross-document dependency** rather than pretending the claim is proven inside this file.

Verification target:

```text
docs/01_Core_Definitions.md
docs/05_Stability_20260504.md
```

No separate formal meaning of `Continuable` is introduced here.

---

## 11. Realization scope ρ and falsifiability

Claude correctly identified a major risk:

```text
Readable(a; ρ1) ≠ Readable(a; ρ2)
```

can become unfalsifiable if every contradiction is dismissed by inventing a new `ρ`.

v1 therefore adds a minimal individuation discipline.

Let:

```text
ρ := (S, B, c, Σ, Γ)
```

be an analytical description of the current realization.

Two readability claims may be compared under the **same realization scope** only when the parameters relevant to the claim are held fixed under the chosen comparison criterion.

A realization must not be split merely to save a threatened Readable judgment.

Provisional methodological rule:

```text
ρ may be refined only when an independently identifiable change in S, B, c, Σ, or Γ is specified.
```

Therefore:

```text
"the result differs, therefore ρ must have changed"
```

is not an admissible argument by itself.

The change in realization scope must be grounded in an independently stated structural, contextual, Slice, Orientation, or readability-context change.

This does not yet provide full mathematical identity criteria for every component, but it blocks the most direct unfalsifiability escape.

---

## 12. Human/machine asymmetry and representation transfer

The human/machine case remains useful, but v1 weakens the previous claim that the pressure point is fully resolved.

Suppose:

```text
machine internal articulation a
↓ π
rendered representation d
↓
human realization ρ_h
```

The human judgment is safely stated as:

```text
Readable(d; ρ_h)
```

not automatically:

```text
Readable(a; ρ_h)
```

To claim that the human has read `a` through `d`, an additional representation relation must be justified.

v1 does **not** define `π` universally.

Instead it records the minimum open question:

```text
What properties must π preserve for readability of d to support a claim about readability of a?
```

Possible domain-specific requirements include:

- distinguishability preservation;
- relevance preservation;
- partial fidelity;
- traceable provenance;
- relation preservation.

No one of these is yet adopted universally.

Therefore the v1 conclusion is:

```text
scope relativity removes the apparent contradiction,
but representation transfer remains an open relation problem.
```

---

## 13. Distributed and holistic representation as a formal counterexample class

The Gemini and Claude reviews both identified distributed representation as a serious challenge to v0.

v1 therefore promotes it from an open question to a formal counterexample class.

### Counterexample class DHR-1

A domain representation may encode a distinction across:

- a population activation pattern;
- a field;
- a relational configuration;
- a manifold region;
- a distributed constraint pattern;
- a holistic perceptual organization.

No single component may be individually addressable as `a`.

Yet the pattern as a whole may be locally discriminable within the realization.

Therefore v1 rejects the universal requirement:

```text
Readable(a) ⇒ discretely addressable token/location for a
```

and retains only the weaker candidate:

```text
Readable(a; ρ) ⇒ LocallyDiscriminable(a; ρ)
```

where the articulation unit may itself be distributed.

---

## 14. Articulation granularity

The distributed case raises a second question:

> what counts as `a`?

v1 does not assume that `a` must be:

- a discrete object;
- one symbol;
- one node;
- one memory cell;
- one semantic category.

`a` may be a local relational or distributed articulation if that is the level at which the distinction becomes discriminable.

Therefore:

```text
articulation-relative
```

must not be misread as:

```text
atomically individuated-object-relative
```

This is important for keeping the model compatible with both symbolic and distributed domains.

---

## 15. Candidate judgment notation v1

The compact notation is retained:

```text
ρ ⊢_R a
```

with:

```text
ρ := (S,B,c,Σ,Γ)
```

read as:

> under realization scope `ρ`, articulation or relation `a` counts as readable.

Working equivalence:

```text
ρ ⊢_R a
iff
Readable(a; ρ)
```

This remains judgment notation only.

No proof-theoretic introduction or elimination rules are yet fixed.

---

## 16. Candidate propositions retained for testing

### P-R1 Existence separation

```text
ExistsInStructure(a) ⇏ Readable(a; ρ)
```

### P-R2 Detection/formation separation

```text
Formation(a; ρ) ⇏ Readable(a; ρ)
```

### P-R3 Truth separation

```text
Readable(a; ρ) ⇏ True(a)
```

### P-R4 Correctness separation

```text
Readable(a; ρ) ⇏ Correct(a)
```

### P-R5 Locality

```text
Readable(a; ρ) ⇏ global readability of S
```

### P-R6 Non-persistence

```text
Readable_n(a) ⇏ Readable_{n+1}(a)
```

### P-R7 Stability dependency

Cross-document candidate:

```text
Stable(a; ρ) ⇒ Readable(a; ρ)
```

while generally:

```text
Readable(a; ρ) ⇏ Stable(a; ρ)
```

### P-R8 Distributed admissibility

```text
Readable(a; ρ)
```

does not require `a` to have one discrete address, token, node, or physical locus.

---

## 17. What appears stronger after external review

The following points now survive both internal pressure tests and the first Gemini/Claude review cycle:

1. Readable is not a fourth Core element.
2. Readable is local and realization-relative.
3. Readable applies to a particular articulation or relation at an explicit granularity.
4. Existence does not imply Readable.
5. Detection or formation does not necessarily imply Readable.
6. Readable does not imply truth or correctness.
7. Readable does not require downstream consumption or successful action.
8. Readable does not imply Stability.
9. Stability appears to require Readable under the current Core definition.
10. Readable may later be revised, lost, superseded, or become inaccessible.
11. Readable is compatible with residual not-yet.
12. Readable does not require discrete symbolic addressability.
13. Distributed or holistic articulations must remain admissible.
14. realization relativity requires explicit individuation discipline to remain falsifiable.
15. representation transfer between machine/internal/display/human articulations is a separate relation problem.

These remain provisional, not canonical.

---

## 18. What remains unresolved before the next review gate

The following questions remain open:

1. Is `PresentTo(a; ρ)` sufficiently non-circular?
2. Is `LocallyDiscriminable(a; ρ)` genuinely distinct from Readable or merely another paraphrase?
3. Are both conditions necessary?
4. Are both jointly sufficient?
5. Can a case be found where both hold but Readable should still fail?
6. Can a case be found where Readable intuitively holds while one fails?
7. How should articulation granularity be constrained so it cannot be chosen arbitrarily after the fact?
8. What exact changes in `S`, `B`, `c`, `Σ`, or `Γ` are sufficient to individuate a new realization?
9. Is `Γ` necessary in every local Readable judgment?
10. How should representation transfer `π` be constrained?
11. How does Readable relate formally to Unknown, Blank, None, Absence, Void, inaccessible, and unresolved states?
12. Does Readable compose under any restricted conditions?
13. Is readability monotonic under any restricted class of Context expansion?
14. Can the two-condition candidate be connected to an established mathematical notion without prematurely reducing Gyro Logic?

---

## 19. External review targets for v1

The next Claude/Gemini review should focus specifically on:

1. whether `PresentTo` is non-circular and independently testable;
2. whether `LocallyDiscriminable` is still a disguised synonym for Readable;
3. whether the worked cases actually establish independence;
4. whether the two-condition candidate is too weak;
5. counterexamples satisfying both conditions but intuitively unreadable;
6. counterexamples intuitively readable while one condition fails;
7. whether the distributed-representation treatment is coherent;
8. whether articulation granularity can be manipulated to evade counterexamples;
9. whether the minimal individuation discipline for `ρ` is sufficient to preserve falsifiability;
10. whether the separation between scope relativity and representation transfer is logically clean;
11. whether any established formal theory provides a cleaner account of the same relation;
12. which claims can now move from exploratory to relatively stable, and which must remain open.

Use:

```text
reviews/critical_review_prompt.md
```

The review gate remains:

```text
major criticisms identified
→ factually checked
→ addressed, explicitly deferred, or rejected with reasons
```

not external-AI agreement or approval.

---

## 20. Review state

```text
ideas/readable_semantics_v1.md

Status:
ROUND_2_PREP
```

Recommended next sequence:

```text
Claude review v1
→ Gemini review v1
→ record both reviews in reviews/
→ classify findings
→ revise if central definitional criticism remains
→ REVIEW_ACCEPTABLE
→ PAPER_CANDIDATE
```

No canonical Gyro Logic definition is changed by this document.
