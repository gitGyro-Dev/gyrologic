# Readable Formal Semantics Study

Date: 2026-08-10
Status: Exploratory / non-canonical
Target layer: Gyro Logic

## 1. Purpose

This study asks:

> When does `Readable(...)` become true in Gyro Logic?

The purpose is not to replace the invariant Core:

```text
Structure → Slice → Stability
```

and not to introduce `Readable` as a fourth Core element.

The purpose is to make explicit the minimum conditions under which a relation, articulation, distinction, or continuation can count as readable in the current Gyro Logic framework.

This study is motivated by a known limitation of the Minimal Formal Model: `Readable(...)` is used in Stability, Continuity Readability, Boundary, Trajectory, and Incorporated Readability, but its semantics are not yet sufficiently specified.

---

## 2. Existing constraints from Gyro Logic

The current Core definitions already constrain the meaning of readability.

### 2.1 Slice

The current definition states:

```text
Slice is the process by which a path is opened through a Structure toward an establishment.
```

The current internal reading also states:

```text
slice-done
= the state in which the Slice has become readable as an established result
```

Therefore, readability cannot be reduced to the mere existence of some candidate relation or object in Structure.

A relation may exist, or may later prove to have existed, without having become available as an established result under the current Slice.

### 2.2 Stability

The current definition states:

```text
Stability is the state in which an opened path becomes readable as an establishment that can continue.
```

Therefore:

```text
Readable ≠ Stable
```

Readability is necessary to the current reading of Stability, but readability alone is not sufficient for Stability because continuation support is also required.

### 2.3 Residual not-yet

A Stability Scene may remain Stable while unresolved local not-yet remains.

Therefore:

```text
Readable(x) does not imply that all related Structure is readable.
```

and:

```text
Readable(x) does not imply global closure.
```

Readability is local.

---

## 3. First candidate definition

A useful first candidate is:

```text
Readable(x; B, c, Σ, Γ)
```

is true when, under the current Orientation `B`, Context `c`, Slice `Σ`, and available readability context `Γ`, `x` has become locally available in a form that can be taken as an articulated relation or establishment by the current Gyro realization.

Japanese working reading:

```text
Readableとは、現在のOrientation・Context・Slice・readability contextのもとで、
対象xが、後続の成立判断や関係づけに用いることのできる局所的な形として現れていること。
```

This is a working characterization, not a canonical definition.

---

## 4. Minimal conditions

The first candidate can be decomposed into four minimum conditions.

Let:

```text
Readable(x; B, c, Σ, Γ)
```

Then at least the following should hold.

### R1. Local availability

`x` must have become locally available under the current realization.

```text
Available(x; B, c, Σ, Γ)
```

This excludes relations that may exist in Structure but have not become available through the current Slice.

Thus:

```text
Exists(x) ⇏ Readable(x)
```

### R2. Articulability

The available content must possess enough local distinction to be treated as a candidate `this is how it has become` rather than as undifferentiated process residue.

```text
Articulable(x; B, c, Σ, Γ)
```

This separates readability from mere signal presence, intermediate computation, or unresolved slice-ing.

Thus:

```text
Detected(x) ⇏ Readable(x)
```

in general.

### R3. Contextual addressability

The articulation must be addressable under the current Orientation and Context.

That is, the current realization must have some admissible way to refer to, distinguish, compare, relate, or use `x`.

```text
Addressable(x; B, c, Γ)
```

This does not require a human observer, a linguistic label, or explicit symbolic representation.

It requires only that `x` is no longer operationally indistinguishable from everything else under the current reading conditions.

### R4. Downstream usability

The articulation must be usable by at least one admissible downstream relation, evaluation, continuation, or later Slice.

```text
Usable(x; B, c, Σ, Γ)
```

This condition is important because something may appear locally present while remaining unavailable to every subsequent operation.

A provisional conjunction is therefore:

```text
Readable(x; B, c, Σ, Γ)
⇒ Available(x; B, c, Σ, Γ)
 ∧ Articulable(x; B, c, Σ, Γ)
 ∧ Addressable(x; B, c, Γ)
 ∧ Usable(x; B, c, Σ, Γ)
```

At this stage the converse is treated as a candidate, not yet a theorem:

```text
Available ∧ Articulable ∧ Addressable ∧ Usable
?⇒ Readable
```

Whether these four conditions are jointly sufficient requires counterexamples.

---

## 5. Readable is not a property of x alone

The strongest immediate conclusion is:

```text
Readable(x)
```

is generally too weak a notation.

The same `x` may be readable under one realization and unreadable under another.

Therefore the more appropriate form is relational:

```text
Readable(x; B, c, Σ, Γ)
```

or, if Structure must be explicit:

```text
Readable(x; S, B, c, Σ, Γ)
```

This means readability is not assumed to be an intrinsic property permanently possessed by `x`.

A relation can become readable, cease to be readable, or become readable differently after Re-Slice or Context update without requiring the underlying relation itself to have appeared or disappeared at that same moment.

---

## 6. Relation existence, traceability, readability

The Minimal Formal Model already separates:

```text
relation existence
≠
traceability
≠
continuity readability
```

This distinction should be generalized.

For a relation `r`:

```text
Exists(r)
```

means only that the relation is taken to obtain in the domain model.

```text
Traceable(r; Γ)
```

means that an admissible path or support for following the relation is available.

```text
Readable(r; B, c, Σ, Γ)
```

means that the relation has become locally available as a usable articulated relation under the current reading conditions.

Therefore:

```text
Exists(r) ⇏ Traceable(r)
Traceable(r) ⇏ Readable(r)
Readable(r) does not imply universal readability under other B, c, Σ, Γ
```

---

## 7. Readable and slice-done

The current Core document says:

```text
slice-done
= the state in which the Slice has become readable as an established result
```

This suggests a useful refinement.

The object of readability at slice-done is not necessarily the entire Structure and not necessarily Stability.

Rather:

```text
slice-done
```

marks the point at which a local articulation `a_n` becomes readable as the result of the current Slice.

Provisionally:

```text
slice-done_n
⇒ Readable(a_n; S_n, B_n, c_n, Σ_n, Γ_n)
```

But:

```text
Readable(a_n; ...)
⇏ Stable(a_n; ...)
```

because Stability additionally requires continuability and the structured conditions of a Stability Scene.

This gives a cleaner separation:

```text
slice-ing
→ local articulation becomes readable
→ slice-done
→ readability + continuation support
→ Stability
```

This sequence is an internal explanatory decomposition only. It does not change the invariant Core.

---

## 8. Readable and Stability

A previous candidate states:

```text
Stable(a; S, B, c)
⇒ Readable(a; S, B, c) ∧ Continuable(a; S, B, c)
```

The present study keeps this direction.

It does not adopt:

```text
Readable(a) ⇒ Stable(a)
```

A readable articulation may still be:

- contradictory;
- too weakly supported;
- locally isolated;
- unable to continue;
- pending another relation;
- readable only as unresolved Difference;
- readable as a Boundary candidate but not yet Stable.

Thus readability is a lower formal threshold than Stability.

---

## 9. Readable and Incorporated Readability

Something that was readable in one local realization does not automatically remain readable later.

Let:

```text
Readable_n(x)
```

hold in realization `g_n`.

Incorporation may produce:

```text
q_n = Inc(g_n)
Γ_{n+1} = UpdateΓ(Γ_n, q_n, e_n)
```

but this does not require:

```text
Readable_n(x) ⇒ Readable_{n+1}(x)
```

because later accessibility may be revised, reweighted, invalidated, suppressed, or lost.

What can persist is not the truth-value of readability itself, but a change in the later conditions under which readability may be established.

This is consistent with Incorporated Readability being non-monotonic.

---

## 10. Readable is not necessarily Boolean at implementation level

At the theory level, the notation:

```text
Readable(...)
```

can function as a judgment-form candidate: the relation counts as readable under stated conditions.

This does not require every implementation to use a Boolean variable.

A domain may instantiate the judgment using:

- a threshold;
- a confidence interval;
- a partial order;
- proof availability;
- access rights;
- evidence sufficiency;
- a neighborhood condition;
- a convergence criterion;
- a multi-criteria evaluation.

The Gyro Logic layer should therefore distinguish:

```text
Readable judgment
```

from:

```text
mechanism used to establish the judgment
```

This preserves the theory/implementation boundary.

---

## 11. Candidate judgment form

A more disciplined notation is:

```text
S, B, c, Σ, Γ ⊢_R x
```

read as:

> under Structure `S`, Orientation `B`, Context `c`, Slice `Σ`, and readability context `Γ`, `x` is readable.

This notation has one advantage over an ordinary predicate: it makes the conditioning scene explicit and avoids suggesting that readability belongs intrinsically to `x`.

The current working equivalence is:

```text
S, B, c, Σ, Γ ⊢_R x

iff

Readable(x; S, B, c, Σ, Γ)
```

This is not yet a proof-theoretic commitment. The turnstile notation is only a candidate judgment notation until introduction and elimination rules are established.

---

## 12. Candidate introduction rule

A first formalization target is an introduction rule of the form:

```text
Available(x; S,B,c,Σ,Γ)
Articulable(x; S,B,c,Σ,Γ)
Addressable(x; B,c,Γ)
Usable(x; S,B,c,Σ,Γ)
---------------------------------
S,B,c,Σ,Γ ⊢_R x
```

This should not yet be treated as canonical.

The next study must attempt to break it with counterexamples.

Questions include:

1. Can something satisfy all four conditions and still not count as readable?
2. Is `Usable` too strong because readability may precede any actual downstream use?
3. Should `Usable` instead mean `available to at least one admissible downstream operation`?
4. Does `Articulable` already include Addressability?
5. Is Γ necessary for every readability judgment, or only later-context readability?
6. Must Structure `S` be explicit in the judgment, or can it remain implicit in Σ?

---

## 13. Candidate negative cases

The following cases should not automatically satisfy Readable.

### 13.1 Existing but unavailable

A relation exists in Structure but no present Slice makes it locally available.

```text
Exists(r) ∧ ¬Available(r)
```

Result candidate:

```text
¬Readable(r)
```

### 13.2 Detected but not articulated

A sensor, process, or observer receives a change, but it has not become distinguishable as a relation or candidate establishment.

```text
Detected(x) ∧ ¬Articulable(x)
```

Result candidate:

```text
¬Readable(x)
```

### 13.3 Articulated but inaccessible downstream

Something appears locally established in form but no admissible subsequent operation can refer to or use it.

This case is especially important because it tests whether "became available" alone is sufficient.

### 13.4 Previously readable but currently inaccessible

An earlier realization established `x`, but a later Context update removes access.

```text
Readable_n(x) ∧ ¬Access_{n+1}(x)
```

Result candidate:

```text
¬Readable_{n+1}(x)
```

without requiring that `x` never existed or that the prior readability judgment was false.

### 13.5 Readable Difference without readable Boundary

A Difference may become readable while no stable distinction has yet become available as Boundary.

Thus:

```text
Readable(Δ) ⇏ Readable(Boundary)
```

This preserves the derivative status of Boundary.

---

## 14. First propositions to test

The following are candidate propositions, not established theorems.

### P-R1: Context-relativity

```text
Readable(x; S,B1,c1,Σ1,Γ1)
```

does not imply:

```text
Readable(x; S,B2,c2,Σ2,Γ2)
```

### P-R2: Locality

```text
Readable(x; S,B,c,Σ,Γ)
```

does not imply global readability of `S`.

### P-R3: Readability precedes Stability

```text
Stable(a; S,B,c,Γ)
⇒ Readable(a; S,B,c,Σ,Γ)
```

but generally:

```text
Readable(a; S,B,c,Σ,Γ)
⇏ Stable(a; S,B,c,Γ)
```

### P-R4: Non-persistence

```text
Readable_n(x)
```

does not imply:

```text
Readable_{n+1}(x)
```

### P-R5: Existence separation

```text
Exists(x)
```

does not imply:

```text
Readable(x; ...)
```

These propositions should be tested by explicit domain examples and countermodels before being promoted into the formal model.

---

## 15. What this study does not decide

This study does not yet decide:

- whether readability is fundamentally Boolean, graded, relational, inferential, or heterogeneous;
- whether the four candidate conditions are necessary and sufficient;
- whether Readable requires an Operator in every domain;
- whether addressability can be defined without circular reference to readability;
- whether downstream usability belongs to Readable or only to Stability;
- whether readability judgments compose transitively;
- whether readability is monotonic under Context expansion;
- whether unreadability should be separated into Unknown, Blank, Void, inaccessible, and unresolved states;
- whether formal judgment rules should be proof-theoretic, relational, categorical, operational, or hybrid.

---

## 16. Current strongest working statement

At this stage, the strongest safe working statement is:

```text
Readable is a local, condition-relative judgment that a relation or articulation has become available in a sufficiently articulated and addressable form to participate in at least one admissible downstream establishment, relation, evaluation, or continuation.
```

Japanese:

```text
Readableとは、ある関係またはarticulationが、現在のStructure・Orientation・Context・Slice・readability contextのもとで、
少なくとも一つの許容された後続の成立・関係づけ・評価・継続に参加できる程度に、
局所的に区別可能かつ参照可能な形として現れた、という条件相対的な判断である。
```

This is deliberately stronger than mere detection and deliberately weaker than Stability.

The intended ordering is provisionally:

```text
existence / occurrence
↓
availability
↓
articulation
↓
Readable
↓
Readable + continuation support
↓
Stability
```

This is an analytical ordering, not a replacement Core.

The invariant Core remains:

```text
Structure → Slice → Stability
```

---

## 17. Next validation step

The next step should not add more terminology.

It should test the candidate Readable rule against concrete counterexamples.

Recommended test cases:

1. automatic door sensor;
2. visual ball recognition;
3. log aggregation and alert escalation;
4. mathematical intermediate result;
5. authentication trajectory;
6. previously readable information rendered inaccessible;
7. relation that exists but is only retrospectively traceable.

For each case, record:

```text
What exists?
What becomes available?
What becomes articulated?
What is addressable?
What can be used downstream?
At what point would Readable become true?
At what point would Stability become true?
What remains residual not-yet?
```

If one definition cannot survive these cases without ad hoc exceptions, revise the definition before integrating it into the Minimal Formal Model.
