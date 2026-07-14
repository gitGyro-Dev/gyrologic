# Relative Influence Formalization Study v0

## 1. Purpose

This document takes the next mathematical step from the idea of weighted incorporated readability.

The central question is:

```text
Given many incorporated readability elements,
how can their relative influence on a current Slice be represented?
```

The invariant Core remains unchanged:

```text
Structure
↓
Slice
↓
Stability
```

This study does not introduce a new Core element and does not adopt a final mathematical model.

---

## 2. Incorporated Readability as a Family

Let the incorporated readability available before Slice `n` be:

```text
Q_n = {q_{n,1}, q_{n,2}, ..., q_{n,m}}
```

Each `q_{n,i}` may represent a retained readability condition such as:

```text
recognized distinction
Difference pattern
Boundary
continuity criterion
semantic association
habitual expectation
prior successful response
prior error pattern
identity criterion
contextual expectation
```

The family may be heterogeneous.

No assumption is made that all elements have the same mathematical type.

Therefore:

```text
Q_n
```

should initially be treated as an indexed family rather than a simple vector.

---

## 3. Influence Is Condition-relative

The influence of an element `q` is not fixed globally.

Let the current conditions be represented provisionally by:

```text
C_n = (S_n, B_n, c_n, Σ_n)
```

where:

```text
S_n = current Structure
B_n = Operator Orientation
c_n = Context
Σ_n = current Slice condition or process
```

A candidate influence function is:

```text
w_n(q ; C_n)
```

or more explicitly:

```text
w_n(q ; S_n, B_n, c_n, Σ_n)
```

The intended meaning is:

```text
the relative degree to which q influences the current Slice
under the present Structure, Orientation, Context, and Slice conditions
```

This is not yet assumed to be a real-valued function.

---

## 4. Scalar Weight Is Only One Candidate

The simplest candidate is:

```text
w_n(q ; C_n) ∈ ℝ
```

A larger value would indicate stronger influence.

However, a scalar may erase important distinctions.

An element may be influential in different ways:

```text
salience
relevance
admissibility
suspicion
expectedness
urgency
confidence
suppression
```

Therefore, a richer candidate is:

```text
w_n(q ; C_n) ∈ W
```

where `W` is a structured influence space.

For example:

```text
w_n(q ; C_n)
=
(salience,
 relevance,
 admissibility,
 suspicion,
 confidence)
```

This is illustrative only.

No influence dimensions are adopted yet.

---

## 5. Relative Order May Be More Fundamental Than Numeric Weight

The theory may not require an absolute numerical score.

A weaker and safer structure is a Context-relative preorder:

```text
q_i ≽_{C_n} q_j
```

The intended meaning is:

```text
under current conditions C_n,
q_i influences the Slice at least as strongly as q_j
```

A preorder allows:

```text
ties
partial incomparability
context-dependent reordering
```

Therefore, the current incorporated readability state may be represented as:

```text
ρ_n = (Q_n, ≽_{C_n})
```

This is currently more compatible with Gyro Logic than a single fixed global ranking.

---

## 6. Partial Order Rather Than Total Ranking

A total ranking would require that every pair be comparable.

```text
q_i > q_j
or
q_j > q_i
```

But two incorporated elements may influence different dimensions of the Slice.

For example:

```text
device continuity
```

and:

```text
geographical anomaly
```

may not be meaningfully comparable before a specific authentication Context is applied.

Thus:

```text
q_i ∥ q_j
```

may be allowed, meaning that the two elements are currently incomparable.

This suggests that a partial order or preorder may be more suitable than a total order.

---

## 7. Foreground and Background

A current Slice may foreground only part of `Q_n`.

Let:

```text
F_n ⊆ Q_n
```

be the currently foregrounded subset.

A provisional foregrounding operator is:

```text
F_n = Foreground(Q_n ; C_n)
```

The remaining elements:

```text
Q_n \ F_n
```

are not necessarily deleted or irrelevant.

They may remain:

```text
backgrounded
suppressed
currently inaccessible
low influence
available for Re-Slice
```

Therefore:

```text
not foregrounded
≠
not incorporated
```

---

## 8. Influence and Slice

A candidate process image is:

```text
Q_n
+
C_n
→
relative influence relation
→
foregrounded readability conditions
→
Slice_n
```

More explicitly:

```text
ρ_n = (Q_n, ≽_{C_n})
```

```text
F_n = Foreground(ρ_n, C_n)
```

```text
Σ_n = Slice(S_n ; B_n, c_n, F_n)
```

This notation does not mean that foregrounded elements mechanically determine the Slice.

Operator Orientation may:

```text
accept
resist
suppress
reweight
ignore
request Re-Slice
```

Therefore:

```text
relative influence
≠
Slice decision rule
```

---

## 9. Update of Influence

After Stability and Operator Response, incorporated readability may be updated.

A provisional update relation is:

```text
ρ_{n+1}
=
U(ρ_n, Σ_n, K_n, R_n, c_n)
```

where:

```text
K_n = Stability state
R_n = Operator Response
```

The update may include:

```text
adding a new readability condition
strengthening an existing relation
weakening an influence
reordering priorities
suppressing an obsolete pattern
splitting one condition into several
merging related conditions
marking a condition as disputed
```

This model permits learning without requiring irreversible accumulation.

---

## 10. Forgetting, Suppression, and Inaccessibility

An incorporated element need not remain permanently active.

Possible states include:

```text
retained and active
retained but backgrounded
retained but inaccessible
weakened
suppressed
reinterpreted
removed
```

Therefore:

```text
incorporated
≠
permanently influential
```

A later Slice may reactivate a previously backgrounded element.

This suggests that forgetting and loss should not be represented only as deletion.

---

## 11. Influence Is Not Truth or Validity

The formal model must preserve:

```text
high influence
≠
truth
```

```text
high influence
≠
validity
```

```text
high influence
≠
correct decision
```

A false pattern may receive high influence.

An accurate but rare pattern may receive low influence.

Therefore, a later model may need to separate:

```text
influence
reliability
validity
confidence
```

These dimensions must not be collapsed into one weight without justification.

---

## 12. GyroAuth Example

Let incorporated authentication readability include:

```text
q_1 = device continuity
q_2 = behavioral rhythm
q_3 = network relation
q_4 = geographical movement
q_5 = motion pattern
q_6 = prior recovery behavior
q_7 = known attack pattern
```

During ordinary local use:

```text
q_1 ≽ q_4
q_2 ≽ q_4
```

may hold.

During international travel:

```text
q_4
```

may become strongly foregrounded.

During a suspected credential attack:

```text
q_7
```

may dominate even when individual events are formally valid.

Thus the same incorporated readability family may generate different influence orders under different Contexts.

This supports:

```text
valid event
≠
stable authenticated trajectory
```

---

## 13. Relation to Trajectory

The influence relation itself may leave traces.

A Trajectory reading may include not only:

```text
what happened
```

but also:

```text
what became foregrounded
what was ignored
which readability condition dominated
how influence order changed
```

Thus a later Trajectory may be based on:

```text
(g_n, ρ_n, F_n)
```

rather than only:

```text
g_n
```

This may be important for explaining:

```text
learning
bias formation
adaptation
attack-induced drift
recovery
institutional change
```

No Trajectory formalization is changed at this stage.

---

## 14. Minimal Candidate Model

The current minimal candidate is:

```text
Q_n = incorporated readability family
```

```text
C_n = (S_n, B_n, c_n, Σ_n)
```

```text
ρ_n = (Q_n, ≽_{C_n})
```

```text
F_n = Foreground(ρ_n, C_n)
```

```text
Σ_n = Slice(S_n ; B_n, c_n, F_n)
```

```text
ρ_{n+1} = U(ρ_n, Σ_n, K_n, R_n, c_n)
```

This is not adopted as a final definition.

---

## 15. Current Working Position

```text
Incorporated readability may contain heterogeneous elements.

Their influence is not globally fixed.

Current Structure, Orientation, Context, and Slice conditions
produce a relative influence relation.

Only some elements become foregrounded in a given Slice.

Foregrounding conditions the Slice but does not decide it.

After Stability and Operator Response,
the incorporated readability and its influence relations may be updated.
```

---

## 16. Open Questions

1. Is a preorder sufficient, or is a richer influence structure needed?
2. Must influence be numeric in implementation even if theory remains ordinal?
3. Can influence be negative, suppressive, or inhibitory?
4. How should incomparable readability elements be handled?
5. Is foregrounding part of Operator Orientation or a separate pre-Slice relation?
6. How is an influence relation learned or updated?
7. What distinguishes forgetting from temporary backgrounding?
8. Can one element influence multiple Slice dimensions differently?
9. How should false but highly influential readability be represented?
10. Does Trajectory need to retain influence-order changes?

---

## 17. Core Change Status

```text
Core change: none
```

No change is made to:

```text
Structure
↓
Slice
↓
Stability
```
