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
Readable is a local and condition-relative judgment that a particular articulation or relation has become available in a sufficiently distinguished form to be selectively addressed within the current realization.
```

Japanese working reading:

```text
Readableとは、特定のarticulationまたはrelationが、現在のStructure・Orientation・Context・Slice・readability contextのもとで局所的に利用可能となり、現在のrealizationの中で他と区別して参照可能な形として成立した、という条件相対的な判断である。
```

A previous candidate additionally required availability to a downstream judgment or operation. The pressure tests below suggest that this downstream requirement should not be part of the minimum definition of Readable itself.

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

Each can become readable at a different point, under a different Orientation, Context, Slice, or criterion.

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

## 4. Readable is not existence, detection, truth, or successful use

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

A mistaken articulation may still become locally available and selectively addressable.

Example:

```text
plastic bag
→ articulated as "ball"
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

### 4.4 Successful downstream use

A readable articulation need not produce a successful later action.

For example, an automatic-door controller may read:

```text
opening-relevant presence
```

while the actuator is broken.

Therefore:

```text
Readable(a) ⇏ SuccessfulDownstreamExecution(a)
```

---

## 5. Candidate minimum conditions v0.1

The current refinement reduces the candidate minimum conditions to three.

```text
Readable(a; S,B,c,Σ,Γ)
```

requires at least:

```text
Available(a; S,B,c,Σ,Γ)
∧ Articulated(a; S,B,c,Σ,Γ)
∧ SelectivelyAddressable(a; S,B,c,Σ,Γ)
```

These conditions are not yet proven jointly sufficient.

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

The articulation must be distinguishable enough within the current realization that it can be referred to as that articulation rather than as an undifferentiated remainder.

A working characterization is:

```text
SelectivelyAddressable(a; ρ)
```

where `ρ` denotes the current realization or reading scope.

This does not require:

- a human observer;
- natural-language naming;
- symbolic representation;
- full object identity;
- an already existing downstream consumer;
- successful later action.

The role of downstream participation is retained as a separate question for Stability, Operator Response, later Slice, or Incorporated Readability.

---

## 6. Pressure point 1: no downstream consumer

The earlier candidate required:

```text
AdmissiblyReferableNext(a)
```

meaning that at least one admissible downstream judgment or operation could take `a` as an input or condition.

This initially appeared useful because it distinguished a merely present signal from something that could participate in later processing.

However, consider:

```text
a local articulation is produced,
it is available,
it is distinguished,
it can be selectively referenced in the present realization,
but no later process currently consumes it.
```

Examples include:

- a diagnostic result generated just before a program terminates;
- a measurement displayed but never logged or acted upon;
- a mathematical intermediate result at the end of an abandoned proof attempt;
- an observation made by a human immediately before the task is stopped.

It is difficult to justify calling such an articulation unreadable merely because no later consumer happens to exist.

The key distinction appears to be:

```text
Readable
≠
ActuallyConsumedLater
```

and likely also:

```text
Readable
≠
PotentiallyConsumableBySomeHypotheticalFutureProcess
```

because hypothetical future consumers can always be invented, making the condition vacuous.

### Interim conclusion P1

`AdmissiblyReferableNext` should not currently be retained as a minimum condition of Readable.

Instead, the present model separates:

```text
Readable(a)
```

from:

```text
ParticipatesDownstream(a)
```

and from:

```text
SupportsContinuation(a)
```

This also sharpens the distinction with Stability:

```text
Readable(a)
⇏
Continuable(a)
```

while the current Stability interpretation remains:

```text
Stable(a)
⇒ Readable(a) ∧ Continuable(a)
```

This refinement removes an implementation-topology assumption from the theory-level Readable relation.

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

means the relation has become locally available in an articulated and selectively addressable form under the present conditions.

Thus:

```text
Exists(r) ⇏ Traceable(r)
Traceable(r) ⇏ Readable(r)
```

remain candidate separations.

---

## 13. Pressure point 2: human-readable display versus machine unreadability

Consider:

```text
A machine generates an internal result a.
The result is rendered to a display.
A human reads the displayed result.
The generating machine itself has no path to reference a again.
```

At first glance, this seems to create two contradictory judgments:

```text
Readable_human(a) = true
Readable_machine(a) = false
```

The contradiction disappears once the reading scope is made explicit.

The display does not make one global predicate `Readable(a)` true for every participant. Instead, the result participates in different local realizations.

A useful notation is:

```text
Readable(a; ρ)
```

where `ρ` denotes a local reading realization or scope.

For example:

```text
ρ_m = machine-internal realization before display output
ρ_h = human-display realization
```

Then it is coherent for:

```text
Readable(a; ρ_h)
```

and:

```text
¬Readable(a; ρ_m')
```

where `ρ_m'` is a later machine realization in which the generated result is no longer internally addressable.

### Important refinement: representation versus articulation identity

The human may not literally read the same internal object `a` that existed inside the machine. The display may produce a representation:

```text
π(a) = d
```

where `d` is the displayed articulation or representation available to the human.

The safer description may therefore be:

```text
Readable(d; ρ_h)
```

rather than automatically:

```text
Readable(a; ρ_h)
```

A relation between `a` and `d` must itself be justified if one wants to say the human read the machine's internal result rather than merely a derived display representation.

This prevents a silent collapse of:

```text
internal result
=
displayed representation
=
human articulation
```

### Interim conclusion P2

Readable should be treated as realization-relative, but an additional primitive `Reader` parameter is not yet required.

The existing conditioning terms may already identify the reading scope:

```text
Readable(a; S,B,c,Σ,Γ)
```

provided the realization to which those parameters belong is explicit.

A compact notation may be used analytically:

```text
ρ = (S,B,c,Σ,Γ)
Readable(a; ρ)
```

This is preferable, for now, to introducing:

```text
Readable(a; reader, S,B,c,Σ,Γ)
```

because `reader` risks reifying a human-like observer where none is required.

---

## 14. Selective addressability after the two pressure tests

The pressure tests make `SelectivelyAddressable` more central, but also expose a possible circularity.

It cannot be defined as:

```text
SelectivelyAddressable(a)
= a can be read
```

because that merely renames Readable.

A safer provisional characterization is structural:

```text
SelectivelyAddressable(a; ρ)
```

holds when, within realization `ρ`, there exists at least one distinction or reference relation that can pick out `a` as the articulation at issue rather than leaving it merged with undifferentiated alternatives.

This reference relation may be:

- symbolic;
- perceptual;
- relational;
- positional;
- causal;
- indexical;
- procedural;
- domain-specific.

It does not need to be linguistic and does not need to lead to a later operation.

This suggests the following separation:

```text
Articulated(a)
= a local distinction has formed

SelectivelyAddressable(a; ρ)
= that local distinction can be picked out as this distinction within ρ

Readable(a; ρ)
= the articulation is locally available as an addressable establishment under ρ
```

Whether `Articulated` and `SelectivelyAddressable` are genuinely independent remains an external-review target.

---

## 15. Candidate judgment notation v0.1

A useful notation remains:

```text
S,B,c,Σ,Γ ⊢_R a
```

read as:

> under Structure `S`, Orientation `B`, Context `c`, Slice `Σ`, and readability context `Γ`, articulation `a` counts as readable.

For compact analysis:

```text
ρ := (S,B,c,Σ,Γ)
ρ ⊢_R a
```

may be used.

Working equivalence:

```text
ρ ⊢_R a

iff

Readable(a; ρ)
```

This is not yet a proof-theoretic commitment.

No introduction or elimination rule is fixed at this stage.

---

## 16. Candidate introduction rule v0.1

After the two pressure tests, the current candidate is reduced to:

```text
Available(a; ρ)
Articulated(a; ρ)
SelectivelyAddressable(a; ρ)
---------------------------------
ρ ⊢_R a
```

This should be treated as a hypothesis to attack, not as a theorem.

Open questions now become sharper:

1. Can all three premises hold while `a` still should not count as readable?
2. Is `Available` already implied by `SelectivelyAddressable`?
3. Is `Articulated` already implied by `SelectivelyAddressable`?
4. Is selective addressability actually the decisive criterion, making the other premises explanatory rather than logically independent?
5. Does this formulation still depend too strongly on an implicit notion of reference?
6. Can `SelectivelyAddressable` be given non-circular formal semantics?
7. Is `Γ` required in an initial local realization with no incorporated readability?
8. Must `S` be explicit or can it be recovered from `ρ` or the Slice relation?
9. Are there domains where an articulation is readable without being individually addressable, for example distributed or holistic pattern recognition?

---

## 17. Candidate propositions for external review

The following are candidate propositions, not established theorems.

### P-R1 Context relativity

```text
Readable(a; ρ1)
⇏ Readable(a; ρ2)
```

### P-R2 Locality

```text
Readable(a; ρ)
⇏ global readability of S
```

### P-R3 Existence separation

```text
Exists(a)
⇏ Readable(a; ρ)
```

### P-R4 Detection separation

```text
Detected(a)
⇏ Readable(a; ρ)
```

### P-R5 Truth separation

```text
Readable(a; ρ)
⇏ True(a)
```

### P-R6 Correctness separation

```text
Readable(a; ρ)
⇏ Correct(a)
```

### P-R7 Stability implication

```text
Stable(a; ρ)
⇒ Readable(a; ρ)
```

while generally:

```text
Readable(a; ρ)
⇏ Stable(a; ρ)
```

### P-R8 Non-persistence

```text
Readable(a; ρ_n)
⇏ Readable(a; ρ_{n+1})
```

### P-R9 Downstream-consumer independence

```text
Readable(a; ρ)
```

does not require that an actual later process consume `a`.

### P-R10 Scope separation

```text
Readable(a; ρ_1)
```

does not imply:

```text
Readable(a; ρ_2)
```

merely because `ρ_1` and `ρ_2` concern the same underlying bearer or system.

These propositions should be challenged by external review and explicit countermodels.

---

## 18. What appears relatively stable enough to preserve for review

The following points currently survive the available examples and pressure tests and should be preserved unless counterexamples overturn them:

1. Readable is not a fourth Core element.
2. Readable is local rather than global.
3. Readable is condition-relative and realization-relative.
4. Readable should normally apply to an articulation or relation, not to an underlying object without specifying granularity.
5. Existence does not imply Readable.
6. Detection does not necessarily imply Readable.
7. Readable does not imply truth or correctness.
8. Readable does not imply Stability.
9. Stability appears to require Readable under the current Core interpretation.
10. Readability may later be revised, lost, superseded, or become inaccessible.
11. Readability does not exhaust Structure and is compatible with residual not-yet.
12. Readable does not require successful downstream execution.
13. Readable probably does not require an actual downstream consumer.
14. A displayed representation and the internal articulation from which it was produced must not automatically be identified.
15. An explicit human-like `Reader` primitive is not yet justified; realization scope may be sufficient.
16. The mechanism used to establish a Readable judgment belongs to domain instantiation and should not redefine the Gyro Logic relation universally.

These points are still reviewable; `relatively stable` does not mean canonical.

---

## 19. What should not yet be fixed

The following points should remain open before Paper Candidate status:

1. whether Readable is fundamentally a predicate, judgment, relation, accessibility condition, or heterogeneous family;
2. whether `Available`, `Articulated`, and `SelectivelyAddressable` are individually necessary;
3. whether the three candidate conditions are jointly sufficient;
4. whether `SelectivelyAddressable` can be defined non-circularly;
5. whether `Available` and `Articulated` are redundant once selective addressability is given;
6. whether distributed or holistic readability can occur without individually addressable articulation;
7. whether `Γ` belongs in all readability judgments;
8. whether a formal realization parameter `ρ` should become part of the model or remain shorthand;
9. whether Readable ever requires an explicit reader/agent parameter in specialized domains;
10. whether readability composes transitively;
11. whether readability is monotonic under any restricted class of Context expansion;
12. how Readable relates formally to Unknown, Blank, None, Absence, Void, inaccessible, and unresolved states;
13. whether the turnstile notation should eventually receive formal introduction/elimination rules;
14. what formal relation connects an internal articulation `a` to an external representation `π(a)` and whether readability transfers across that relation.

---

## 20. External review targets

When this file is sent to Claude and Gemini, reviewers should pay particular attention to:

1. whether removing `AdmissiblyReferableNext` makes Readable too weak;
2. whether requiring an actual or potential downstream consumer was in fact necessary;
3. whether the three remaining conditions are redundant or circular;
4. whether `SelectivelyAddressable` is simply Readable under another name;
5. whether the truth/correctness separation is logically coherent;
6. whether realization-relative readability can be expressed more cleanly using an established formal framework;
7. whether an explicit reader/agent parameter is unavoidable;
8. whether the distinction between internal articulation and displayed representation is adequate;
9. counterexamples where all current candidate conditions hold but readability should fail;
10. counterexamples where Readable intuitively holds despite one candidate condition failing;
11. whether holistic or distributed patterns defeat selective addressability;
12. whether the candidate semantics can be expressed without introducing implementation assumptions;
13. which claims are mature enough to preserve and which should remain provisional.

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

Internal ChatGPT pressure tests completed in this revision:

```text
1. no downstream consumer
2. human-readable display versus machine unreadability
```

Current direction:

```text
Readable
≈ local availability
+ articulation
+ selective addressability
within an explicit realization scope
```

but this remains provisional and is now ready for external critical attack.

Next sequence:

```text
Claude critical review
→ Gemini critical review
→ record reviews in reviews/
→ classify findings: accept / partial / reject / verify / defer
→ revise readable_semantics_v0.md
→ repeat if major unresolved criticism remains
→ REVIEW_ACCEPTABLE
→ PAPER_CANDIDATE
```

No canonical Gyro Logic definition is changed by this document.