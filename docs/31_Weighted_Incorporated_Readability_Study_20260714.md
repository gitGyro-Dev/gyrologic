# Weighted Incorporated Readability Study v0

## 1. Purpose

This document extends the preliminary idea of incorporated readability:

```text
once readability is acquired,
it becomes incorporated into subsequent Structure
```

The present question is:

```text
If many kinds of readability may be incorporated,
why do some elements influence a later Slice more strongly than others?
```

The invariant Core remains unchanged:

```text
Structure
↓
Slice
↓
Stability
```

This document does not introduce a new Core element or a final mathematical definition.

---

## 2. Central Intuition

Incorporated readability may include many heterogeneous elements:

```text
recognized distinctions
prior relations
Difference patterns
Boundaries
habits
affective reactions
social norms
learned rules
prior errors
successful responses
contextual expectations
semantic associations
identity criteria
continuity criteria
```

In that sense, almost anything that has altered later readability may become incorporated.

However:

```text
anything may become incorporated
≠
everything influences every Slice equally
```

When a later Slice occurs, some incorporated elements become more influential than others.

The current image is:

```text
incorporated readability
=
heterogeneous retained readability conditions
+
Context- and Orientation-relative influence ordering
```

---

## 3. Priority Is Not a Fixed Global Ranking

The word `priority` is useful but may be misleading if understood as one permanent list.

```text
q_1 > q_2 > q_3 > ...
```

may hold under one Context and fail under another.

For example:

```text
location history
```

may strongly influence an authentication Slice during international travel, while:

```text
device behavior
```

may dominate during ordinary local use.

Therefore:

```text
priority
is not necessarily global
```

A safer interpretation is:

```text
relative influence under the current Orientation, Context, and Slice conditions
```

---

## 4. Influence Is Not Truth

A highly influential incorporated element is not necessarily correct.

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
final decision
```

Highly influential elements may include:

```text
accurate learned distinctions
useful expertise
obsolete assumptions
bias
fear
institutional norms
attack-induced false patterns
misclassification
```

Therefore, the theory must distinguish:

```text
influence
from
correctness
```

and:

```text
priority
from
Operator Response
```

---

## 5. Influence Is Not Operator Decision

The current process image is:

```text
incorporated readability
↓
relative influence under current conditions
↓
Operator Orientation
↓
Slice
↓
Stability
↓
Operator Response
```

This does not mean that incorporated readability independently decides the Slice.

It conditions what becomes:

```text
salient
relevant
admissible
suspicious
expected
ignorable
worthy of further Slice
```

Operator Orientation may use, resist, update, or suppress such influence.

Thus:

```text
influence condition
≠
decision rule
```

---

## 6. Candidate Components

Let incorporated readability before Slice `n` be provisionally represented as a family:

```text
ρ_n = {q_{n,1}, q_{n,2}, ..., q_{n,m}}
```

where each `q_{n,k}` is one incorporated readability condition.

Examples include:

```text
recognized device pattern
learned social distinction
known Boundary
previously readable Difference pattern
continuity criterion
expected temporal rhythm
semantic association
```

A Context- and Orientation-relative influence may be written provisionally as:

```text
w_n(q_{n,k} ; B_n, c_n, S_n)
```

The intended meaning is:

```text
how strongly q_{n,k} influences the current Orientation and Slice
under Structure S_n, Orientation B_n, and Context c_n
```

No assumption is made that `w_n` must be a real-valued scalar.

It may instead be:

```text
an ordering
a preorder
a partial order
a qualitative rank
a vector of influence dimensions
a Context-indexed relation
a probability-like value
a measure of salience or relevance
```

---

## 7. Why a Scalar Weight May Be Insufficient

A simple mathematical form would be:

```text
w_n(q) ∈ [0,1]
```

However, one scalar may collapse distinct kinds of influence.

For example, an incorporated element may be:

```text
highly salient but weakly reliable
highly reliable but currently irrelevant
strongly restrictive but rarely activated
weak individually but dominant in combination
```

Therefore, a richer provisional representation may be:

```text
w_n(q)
=
(relevance, salience, reliability, persistence, compatibility, urgency)
```

This tuple is illustrative only.

The dimensions are not adopted.

The important point is:

```text
influence may be structured rather than scalar
```

---

## 8. Priority May Emerge Relationally

An element may not have a meaningful influence value in isolation.

Its importance may arise only relative to other elements.

For example:

```text
new device
```

may have low influence when combined with:

```text
normal location
normal motion
known network
expected time
```

but high influence when combined with:

```text
new country
impossible travel speed
unknown network
privilege escalation
```

Thus:

```text
influence of q
may depend on relations among multiple q-elements
```

A candidate relation is:

```text
q_i ≽_{B,c,S} q_j
```

meaning:

```text
under the current Structure, Orientation, and Context,
q_i has at least as much influence on the Slice as q_j
```

This relation need not produce a total order.

Some elements may be incomparable.

---

## 9. Foreground and Background

The current intuition may also be expressed as:

```text
incorporated readability
forms a background condition
```

while:

```text
highly influential elements
move toward the foreground of the current Slice
```

This is not a spatial claim.

It means that some elements become more available to condition:

```text
what is noticed
what is compared
what counts as Difference
which Boundary appears
which relation is followed
which evidence is requested
```

Therefore:

```text
later Slice
=
not a neutral operation over all retained readability
```

It is selectively conditioned by what is foregrounded under the current Orientation and Context.

---

## 10. Update Through Stability

The relative influence structure itself may change after a new Stability state.

A provisional process is:

```text
ρ_n
+
B_n
+
c_n
↓
weighted or ordered influence condition
↓
Slice_n
↓
Stability_n
↓
incorporation / revision
↓
ρ_{n+1}
```

The update may:

```text
increase influence
decrease influence
add a new readability condition
merge conditions
split one condition
suppress a condition
reinterpret a condition
make a prior condition inaccessible
```

Therefore:

```text
ρ_{n+1}
≠
ρ_n + one stored event
```

The update may alter both content and relative influence relations.

---

## 11. Relation to Trajectory

Trajectory may be affected by weighted incorporated readability in two ways.

First, it changes which local realizations are connected or foregrounded during tracing.

Second, prior Trajectory readings may themselves become incorporated and influence later tracing.

```text
prior Trajectory reading
↓
incorporated readability
↓
later Orientation and Slice
↓
new Trajectory reading
```

This suggests possible retrospective reorganization:

```text
the same accumulated traces
may produce a different readable Trajectory
when influence ordering changes
```

The accumulated past does not need to change for its readable organization to change.

---

## 12. Relation to GyroAuth

GyroAuth provides a practical example.

A current authentication event may include:

```text
device
behavior
time
space
network
motion
risk Context
```

These dimensions are not always equally influential.

Their influence may depend on:

```text
prior authenticated course
current risk Context
known recovery patterns
recent attack evidence
newly incorporated behavior
Operator Orientation
```

For example:

```text
new device alone
```

may be weak evidence.

But:

```text
new device
+
new country
+
impossible transition
+
privilege deviation
```

may move several elements to the foreground and strongly redirect the Slice.

Thus, GyroAuth is not merely:

```text
sum of historical features
```

It is closer to:

```text
Context-relative reordering of incorporated readability
for the current authentication Slice
```

---

## 13. Minimal Formal Candidate

A first minimal candidate is:

```text
ρ_n = (Q_n, ≽_n)
```

where:

```text
Q_n
=
family of incorporated readability conditions
```

and:

```text
≽_n
=
Context- and Orientation-relative influence relation
```

More explicitly:

```text
≽_n
=
≽_{S_n,B_n,c_n}
```

A Slice may then be conditioned as:

```text
Σ_n
=
Σ(S_n ; B_n, c_n, ρ_n)
```

This does not mean that Slice is a conventional deterministic function.

The notation only records that the current Slice is conditioned by incorporated readability and its relative influence structure.

---

## 14. Important Distinctions

```text
incorporated
≠
currently influential
```

```text
influential
≠
selected
```

```text
selected
≠
true
```

```text
high priority
≠
final decision
```

```text
low priority
≠
absent
```

```text
background
≠
forgotten
```

```text
weight change
≠
content deletion
```

These distinctions should be preserved in later mathematical models.

---

## 15. Failure Cases

### 15.1 Equal Influence Collapse

```text
all incorporated elements affect every Slice equally
```

This does not explain selective attention, relevance, or Context dependence.

### 15.2 Fixed Ranking Collapse

```text
one permanent priority list determines all future Slices
```

This ignores Context, Orientation, learning, and re-interpretation.

### 15.3 Truth Collapse

```text
high influence = correct
```

This cannot represent bias, outdated learning, or attack-induced patterns.

### 15.4 Scalar Collapse

```text
one number fully represents influence
```

This may lose reliability, relevance, salience, persistence, and relational effects.

### 15.5 Decision Collapse

```text
highest-weight element determines Operator Response
```

This collapses influence conditions into decision logic.

### 15.6 Storage Collapse

```text
ρ_n = all stored history
```

This confuses records with changed readability conditions.

---

## 16. Current Working Position

The current working position is:

```text
Many heterogeneous forms of readability may become incorporated
into later Structure.

However, they do not influence every Slice equally.

Under the current Structure, Context, and Operator Orientation,
some incorporated elements become more influential or foregrounded.

This relative influence conditions the direction, relevance,
granularity, and admissibility of the Slice.

Influence is not truth, validity, decision, or Stability.
```

A minimal mathematical candidate is:

```text
ρ_n = (Q_n, ≽_{S_n,B_n,c_n})
```

where `Q_n` is the heterogeneous family of incorporated readability conditions and `≽` is a Context- and Orientation-relative influence relation.

No final mathematical object is adopted yet.

---

## 17. Open Questions

1. Is an influence relation sufficient, or is a structured weight required?
2. Is the relation a total order, partial order, preorder, or Context-dependent family?
3. Can incomparable readability conditions jointly dominate a Slice?
4. How is influence revised after Stability?
5. Can an incorporated condition remain latent indefinitely?
6. What makes an element move from background to foreground?
7. How are bias and useful prior knowledge distinguished?
8. Can Operator Orientation resist a highly influential incorporated condition?
9. How should conflicting incorporated readability conditions be represented?
10. Does Trajectory tracing use the same influence structure as local Slice?
11. Can attack behavior deliberately manipulate the influence ordering in GyroAuth?
12. What is the minimum formal structure needed before implementation?

---

## 18. Core Change Status

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
