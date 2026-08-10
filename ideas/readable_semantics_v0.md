# Readable Semantics v0

Date: 2026-08-10
Status: Idea draft / pre-review
Target layer: Gyro Logic
Review state: DRAFT_FOR_EXTERNAL_REVIEW

## 1. Purpose

This note consolidates the current working hypothesis for `Readable(...)` in Gyro Logic before external critical review.

It is not a canonical definition and does not modify the invariant Core:

```text
Structure → Slice → Stability
```

`Readable` remains a supporting relation used to explain how a local articulation becomes available as an establishment and how later Stability, Continuity Readability, Boundary, Trajectory, and Incorporated Readability may be formed.

The present question is:

> What must have been established for a particular articulation or relation to count as readable under a given Gyro realization?

---

## 2. Current strongest working hypothesis

The current safest working statement is:

```text
Readable is a local and condition-relative judgment that a particular articulation or relation has become available in a sufficiently distinguished form to be selectively addressed and admitted as an input or condition for at least one downstream judgment, relation, evaluation, or operation.
```

Japanese working reading:

```text
Readableとは、特定のarticulationまたはrelationが、現在のStructure・Orientation・Context・Slice・readability contextのもとで局所的に利用可能となり、他と区別して参照でき、少なくとも一つの許容された後続の判断・関係づけ・評価・作用に入力または条件として渡せる状態になった、という条件相対的な判断である。
```

This is a working hypothesis only.

---

## 3. Readable is articulation-relative

The automatic-door and ball-recognition studies show that readability should not normally attach to an underlying object as a whole.

The same physical or domain occurrence may support multiple local articulations at different granularities:

```text
moving signal
→ bounded moving object
→ round moving object
→ ball
→ ball approaching me
→ collision risk
```

Each can become readable at a different point, under a different Orientation, Context, Slice, or downstream criterion.

Therefore the preferred form is:

```text
Readable(a; S,B,c,Σ,Γ)
```

where `a` is the particular articulation or relation being judged.

The informal form:

```text
Readable(object)
```

should be treated as underspecified unless the articulation level is explicit.

---

## 4. Readable is not existence, detection, or truth

The current study preserves the following separations.

### 4.1 Existence

A relation or occurrence may exist in Structure without becoming available under the present Slice.

```text
Exists(x) ⇏ Readable(x)
```

### 4.2 Detection

A signal may be detected while remaining indistinguishable from noise or unresolved process residue.

```text
Detected(x) ⇏ Readable(x)
```

### 4.3 Truth and correctness

A mistaken articulation may still become locally available, selectively addressable, and used by later processing.

Example:

```text
plastic bag
→ articulated as "ball"
→ avoidance action
→ later Re-Slice
→ corrected to "plastic bag"
```

The current model therefore favors:

```text
Readable(a) ⇏ True(a)
Readable(a) ⇏ Correct(a)
```

unless a domain-specific admissibility rule explicitly incorporates truth or correctness.

This prevents Readable from silently becoming an epistemic truth predicate.

---

## 5. Candidate minimum conditions

A second candidate decomposition is:

```text
Readable(a; S,B,c,Σ,Γ)
```

requires at least:

```text
Available(a; S,B,c,Σ,Γ)
∧ Articulated(a; S,B,c,Σ,Γ)
∧ SelectivelyAddressable(a; B,c,Γ)
∧ AdmissiblyReferableNext(a; S,B,c,Σ,Γ)
```

The four conditions are not yet proven jointly sufficient.

### R1. Available

The articulation must have become locally available under the current realization.

This excludes relations that may exist in Structure but have not become available through the present Slice.

### R2. Articulated

The available content must possess enough local distinction to count as a candidate `this is how it has become` rather than undifferentiated process residue.

This does not require high-level semantic classification.

For an automatic door, the articulation:

```text
opening-relevant presence
```

may be sufficient even when neither `person` nor identity is readable.

### R3. SelectivelyAddressable

The articulation must be distinguishable enough that at least one admissible relation, comparison, judgment, or operation can refer to that articulation rather than to everything else indiscriminately.

This does not require:

- a human observer;
- natural-language naming;
- symbolic representation;
- full object identity.

### R4. AdmissiblyReferableNext

At least one admissible downstream judgment, relation, evaluation, or operation must be able to take the articulation as an input, condition, distinction, or reference.

This does **not** require successful downstream execution.

Example:

```text
opening-relevant presence
```

may be readable even if the door actuator is physically broken.

Thus:

```text
Readable(a)
```

should not depend on whether every downstream process succeeds.

---

## 6. Why `Usable` was revised

The first candidate used:

```text
Usable(a)
```

as a readability condition.

The automatic-door counterexample showed this term was too ambiguous.

If `Usable` means that the later action must actually succeed, then a correctly read door-opening condition would become unreadable merely because the actuator failed.

That is undesirable.

The revised concept is therefore closer to:

```text
AdmissiblyReferableNext(a)
```

which concerns availability to a legitimate next relation or operation, not success of that later operation.

The exact name remains provisional and should be challenged in external review.

---

## 7. Readable and slice-done

The current Core interpretation states:

```text
slice-done
= the state in which the Slice has become readable as an established result
```

The present hypothesis interprets this more precisely as:

```text
slice-done_n
⇒ Readable(a_n; S_n,B_n,c_n,Σ_n,Γ_n)
```

where `a_n` is the local articulation made available through the current Slice.

This does not imply:

```text
Readable(a_n) ⇒ Stable(a_n)
```

because Stability requires continuation support beyond mere readability.

An analytical decomposition is therefore:

```text
slice-ing
→ local articulation becomes available
→ articulation becomes readable
→ slice-done
→ readability + continuation support
→ Stability
```

This decomposition does not alter the Core.

---

## 8. Readable and Stability

The following implication remains a strong candidate:

```text
Stable(a; S,B,c,Γ)
⇒ Readable(a; S,B,c,Σ,Γ)
```

but generally:

```text
Readable(a; S,B,c,Σ,Γ)
⇏ Stable(a; S,B,c,Γ)
```

Concrete examples support this distinction.

### Automatic door

A threshold relation may become readable at each sample while oscillating around the threshold too rapidly to support a robust opening decision.

### Ball recognition

`ball` may become readable in one frame while an interception-relevant Stability Scene still requires motion, spatial relation, and continuation estimation.

Therefore Readable is currently treated as a lower threshold than Stability.

---

## 9. Readable is local and non-exhaustive

Readable concerns a particular articulation or relation under particular conditions.

Therefore:

```text
Readable(a; S,B,c,Σ,Γ)
```

does not imply:

```text
all of S is readable
```

or:

```text
Structure is complete
```

A Stability Scene may likewise remain compatible with residual not-yet.

Examples:

- an automatic door may read opening-relevant presence without identity, intent, or future direction;
- a vision system may read an approaching object without reading it as a ball;
- a ball may be readable while exact trajectory or collision outcome remains unresolved.

---

## 10. Context-relativity and revision

The same articulation may be readable under one realization and unreadable under another.

Thus:

```text
Readable(a; S,B1,c1,Σ1,Γ1)
```

does not imply:

```text
Readable(a; S,B2,c2,Σ2,Γ2)
```

Likewise:

```text
Readable_n(a)
```

does not imply:

```text
Readable_{n+1}(a)
```

A later Re-Slice or Context update may:

- revise an articulation;
- invalidate it;
- make it inaccessible;
- replace it with a stronger articulation;
- expose a relation that was not previously readable.

This does not mean the earlier readability judgment was necessarily false at the time it held.

---

## 11. Readability and Incorporated Readability

If an articulation is readable in realization `g_n`, some part of that local establishment may become incorporated into later readability conditions.

But:

```text
Readable_n(a) ⇏ Readable_{n+1}(a)
```

and:

```text
Readable_n(a) ⇏ permanent accessibility of a
```

What may persist is a change in the later conditions of readability rather than the same readability judgment itself.

This remains consistent with the non-monotonic interpretation of Incorporated Readability.

---

## 12. Readability and Continuity Readability

The current Minimal Formal Model distinguishes:

```text
relation existence
≠
traceability
≠
continuity readability
```

The present Readable hypothesis supports that separation.

For a relation `r`:

```text
Exists(r)
```

means only that the domain model treats the relation as obtaining.

```text
Traceable(r; Γ)
```

means support exists for following the relation.

```text
Readable(r; B,c,Σ,Γ)
```

means the relation has become locally available in a selectively addressable and admissibly referable form under the present conditions.

Thus:

```text
Exists(r) ⇏ Traceable(r)
Traceable(r) ⇏ Readable(r)
```

remain candidate separations.

---

## 13. Candidate judgment notation

A useful notation remains:

```text
S,B,c,Σ,Γ ⊢_R a
```

read as:

> under Structure `S`, Orientation `B`, Context `c`, Slice `Σ`, and readability context `Γ`, articulation `a` counts as readable.

Working equivalence:

```text
S,B,c,Σ,Γ ⊢_R a

iff

Readable(a; S,B,c,Σ,Γ)
```

This is not yet a proof-theoretic commitment.

No introduction or elimination rule is fixed at this stage.

---

## 14. Candidate introduction rule v0

The current candidate is:

```text
Available(a; S,B,c,Σ,Γ)
Articulated(a; S,B,c,Σ,Γ)
SelectivelyAddressable(a; B,c,Γ)
AdmissiblyReferableNext(a; S,B,c,Σ,Γ)
-------------------------------------------------
S,B,c,Σ,Γ ⊢_R a
```

This should be treated as a hypothesis to attack, not as a theorem.

The following questions remain open:

1. Can all four premises hold while `a` still should not count as readable?
2. Is `AdmissiblyReferableNext` still too strong?
3. Could something be readable even if no downstream process currently exists?
4. Does `SelectivelyAddressable` already include some form of downstream referability?
5. Is `Articulated` distinct enough from `SelectivelyAddressable` to justify both?
6. Is `Γ` required for every local readability judgment, or only for context-dependent later readability?
7. Must `S` be explicit in the judgment, or can it be reconstructed from the Slice realization?
8. Does the rule accidentally make Readable implementation-centric rather than theory-level?

---

## 15. Important unresolved pressure point: no downstream consumer

The strongest unresolved counterexample is this case:

```text
an articulation is locally available,
distinguished,
and selectively addressable,
but no actual downstream process currently consumes it.
```

Question:

> Is it still Readable?

Two candidate answers remain open.

### Candidate A — yes

Readable requires only that the articulation **could** be admitted by at least one compatible downstream relation if such a relation were present.

This weakens `AdmissiblyReferableNext` toward potential admissibility.

### Candidate B — no

Readable requires participation in the current relational scene, so an articulation with no admissible downstream relation remains only articulated, not yet readable.

This makes Readable more relational but risks coupling it too strongly to implementation or current process topology.

This issue should be tested before external review is considered complete.

---

## 16. Important unresolved pressure point: human-readable display versus machine unreadability

Another useful case is:

```text
A machine generates an internal result.
The result is rendered to a display.
A human can read the displayed result.
The generating machine itself has no path to reference that result again.
```

There may be at least two different readability judgments:

```text
Readable_human(a)
Readable_machine(a)
```

The first may hold while the second does not.

This suggests Readable may need an explicit **reading relation or realization scope**, rather than being interpreted globally.

It also warns against assuming:

```text
visible somewhere
⇒ readable everywhere
```

---

## 17. Candidate propositions for review

The following are candidate propositions, not established theorems.

### P-R1 Context relativity

```text
Readable(a; S,B1,c1,Σ1,Γ1)
⇏ Readable(a; S,B2,c2,Σ2,Γ2)
```

### P-R2 Locality

```text
Readable(a; S,B,c,Σ,Γ)
⇏ global readability of S
```

### P-R3 Existence separation

```text
Exists(a)
⇏ Readable(a; ...)
```

### P-R4 Detection separation

```text
Detected(a)
⇏ Readable(a; ...)
```

### P-R5 Truth separation

```text
Readable(a)
⇏ True(a)
```

### P-R6 Correctness separation

```text
Readable(a)
⇏ Correct(a)
```

### P-R7 Stability implication

```text
Stable(a)
⇒ Readable(a)
```

while generally:

```text
Readable(a)
⇏ Stable(a)
```

### P-R8 Non-persistence

```text
Readable_n(a)
⇏ Readable_{n+1}(a)
```

These propositions should be challenged by external review and explicit countermodels.

---

## 18. What appears relatively stable enough to preserve for review

The following points currently survive the available examples and should be preserved unless counterexamples overturn them:

1. Readable is not a fourth Core element.
2. Readable is local rather than global.
3. Readable is condition-relative.
4. Readable should normally apply to an articulation or relation, not to an underlying object without specifying granularity.
5. Existence does not imply Readable.
6. Detection does not necessarily imply Readable.
7. Readable does not imply truth or correctness.
8. Readable does not imply Stability.
9. Stability appears to require Readable under the current Core interpretation.
10. Readability may later be revised, lost, superseded, or become inaccessible.
11. Readability does not exhaust Structure and is compatible with residual not-yet.
12. The mechanism used to establish a Readable judgment belongs to domain instantiation and should not redefine the Gyro Logic relation universally.

These points are still reviewable; `relatively stable` does not mean canonical.

---

## 19. What should not yet be fixed

The following points should remain open before Paper Candidate status:

1. whether Readable is fundamentally a predicate, judgment, relation, accessibility condition, or heterogeneous family;
2. whether the four candidate conditions are individually necessary;
3. whether the four candidate conditions are jointly sufficient;
4. the exact meaning and name of `AdmissiblyReferableNext`;
5. whether potential downstream referability is sufficient without an actual downstream consumer;
6. whether `SelectivelyAddressable` and `Articulated` are genuinely separate conditions;
7. whether `Γ` belongs in all readability judgments;
8. whether Readable requires an explicit reader/realization parameter;
9. whether readability composes transitively;
10. whether readability is monotonic under any restricted class of Context expansion;
11. how Readable relates formally to Unknown, Blank, None, Absence, Void, inaccessible, and unresolved states;
12. whether the turnstile notation should eventually receive formal introduction/elimination rules.

---

## 20. External review targets

When this file is sent to Claude and Gemini, reviewers should pay particular attention to:

1. whether `AdmissiblyReferableNext` is circular or unnecessary;
2. whether the model confuses readability with operational accessibility;
3. whether the truth/correctness separation is logically coherent;
4. whether the distinction among Available, Articulated, SelectivelyAddressable, and Readable is non-redundant;
5. whether a known formal framework already captures the same relation more cleanly;
6. counterexamples where all current candidate conditions hold but readability should fail;
7. counterexamples where Readable intuitively holds despite one candidate condition failing;
8. whether the relation is still too dependent on an implicit Operator or observer;
9. whether the candidate semantics can be expressed without introducing implementation assumptions;
10. which claims are mature enough to preserve and which should remain provisional.

Use the repository review prompt:

```text
reviews/critical_review_prompt.md
```

The goal of review is not consensus or approval. The gate is passed when major criticisms have been identified, factually checked, and either addressed, explicitly deferred, or rejected with reasons.

---

## 21. Current state

```text
ideas/readable_semantics_v0.md

Status:
DRAFT_FOR_EXTERNAL_REVIEW
```

Next sequence:

```text
ChatGPT internal refinement
→ Claude critical review
→ Gemini critical review
→ record reviews in reviews/
→ classify findings: accept / partial / reject / verify / defer
→ revise readable_semantics_v0.md
→ repeat if major unresolved criticism remains
→ REVIEW_ACCEPTABLE
→ PAPER_CANDIDATE
```

No canonical Gyro Logic definition is changed by this document.
