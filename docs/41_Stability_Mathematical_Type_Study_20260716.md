# Stability Mathematical Type Study v0

## 1. Purpose

This document begins the S-3 study of the mathematical type of **Stability**.

The invariant Core remains unchanged:

```text
Structure
↓
Slice
↓
Stability
```

The primary definition remains:

```text
Stability is the state in which an opened path becomes readable
as an establishment that can continue.
```

Japanese:

```text
Stabilityとは、開かれた道筋が、
一つの成立として継続可能な状態である。
```

The present question is whether Stability should be modeled as:

```text
state quantity
condition
relation
```

The current intuition suggests that none of these alone is sufficient.

---

## 2. Starting Intuition: A Locally Inspectable Scene

The current image is:

```text
Structure remains globally not-yet.

Through Slice, one local articulation appears.

At Stability, that articulation has settled enough
for it to be inspected, read, or handled as one continuing establishment.
```

Japanese image:

```text
Structure全体には、なお未が残る。

Sliceによって局所的な「こうなった」が現れる。

Stabilityでは、その局所が一旦落ち着き、
確認しやすい一つの場面として読める。
```

The word `scene` is provisional.

It does not mean a static visual frame.

It refers to a locally readable configuration in which one can inspect:

```text
what has become articulated
what remains unresolved
what relations currently hold
what can continue from here
```

---

## 3. Stability and the Two Kinds of Not-Yet

The present theory suggests a distinction between:

```text
global not-yet
```

and:

```text
residual local not-yet
```

Before Slice:

```text
Structure S
=
globally not-yet
```

After Slice:

```text
a_Σ
=
one local articulation has appeared
```

At Stability:

```text
that articulation is readable as a continuing establishment
```

However:

```text
Stability
≠
all local uncertainty is removed
```

A stable scene may still contain:

```text
unread details
unresolved relations
remaining Difference
Boundary ambiguity
future branching
possible Re-Slice
unknown continuation
```

Therefore:

```text
local establishment
+
residual not-yet
```

may coexist inside Stability.

This is a central mathematical requirement.

---

## 4. Stability Is Not Only a State Quantity

A state quantity may represent:

```text
how stable
how much deviation remains
how much confidence exists
```

For example:

```text
s ∈ [0,1]
```

or:

```text
s = exp(-Δ)
```

However:

```text
Stability
≠
scalar stability score
```

A scalar cannot by itself represent:

```text
what is locally established
what remains unread
which relations are retained
what continuation is possible
```

Therefore, a state quantity may be one coordinate or evaluation of Stability, not its complete mathematical type.

---

## 5. Stability Is Not Only a Condition

A condition model may write:

```text
Stable(a_Σ ; S,B,c)
```

or:

```text
Readable(a_Σ)
∧
Continuable(a_Σ)
```

This is useful because it distinguishes Stability from a score.

However, a predicate alone says only whether a condition holds.

It does not preserve the locally readable content or scene in which it holds.

```text
predicate value
≠
locally established scene
```

Therefore, a condition may characterize Stability without being identical to the whole Stability object.

---

## 6. Stability Is Not Only a Relation

A relational model may represent:

```text
a_Σ is readable relative to S, B, and c
```

or:

```text
a_Σ can continue into later Structure
```

This captures Context dependence and continuability.

However, relation alone may omit the settled local configuration that is being related.

Thus:

```text
Stability
may contain relations
but
Stability ≠ one relation alone
```

---

## 7. Candidate: Stable Scene

A current candidate is to represent Stability as a structured local scene:

```text
K_Σ = (a_Σ, L_Σ, U_Σ, C_Σ)
```

where provisionally:

```text
a_Σ
=
the local articulation produced through Slice
```

```text
L_Σ
=
the locally readable relations, distinctions, or configuration
```

```text
U_Σ
=
the residual local not-yet
```

```text
C_Σ
=
the available continuation relations or conditions
```

This is not a definition.

It is a decomposition for testing whether Stability is better represented as a structured scene than as a scalar, predicate, or relation alone.

---

## 8. Why “Scene” May Be Useful

The word `scene` expresses that Stability provides a local point from which the current articulation becomes easier to inspect.

A scene may include:

```text
foregrounded relations
remaining unread relations
current Boundary
current Difference
current establishment reading
possible next directions
```

It also avoids implying:

```text
final completion
permanent equilibrium
complete closure
zero change
```

A stable scene is locally readable, but not globally finished.

---

## 9. Mathematical Image: Local Readability Region

A second candidate is a local readability region around the Slice articulation.

Let:

```text
a_Σ
```

be the local articulation produced through Slice.

Let:

```text
N(a_Σ)
```

be a provisional local region of configurations related to `a_Σ`.

Then Stability may require a subregion:

```text
K_Σ ⊆ N(a_Σ)
```

such that:

```text
Readable(K_Σ ; S,B,c)
```

and:

```text
Continuable(K_Σ ; S,B,c)
```

This resembles a neighbourhood model, but no topology is assumed yet.

The term `region` only means that Stability may include more than one exact point or snapshot.

This is important because:

```text
small variation
may remain inside the same stable scene
```

Thus Stability may tolerate Difference without requiring exact equality.

---

## 10. Residual Not-Yet Inside a Stable Scene

To represent remaining uncertainty, let:

```text
U_Σ ⊆ K_Σ
```

or more generally:

```text
U_Σ = ResidualNotYet(K_Σ)
```

The intended meaning is:

```text
parts, relations, or future directions within the stable scene
remain unresolved or unread
```

However:

```text
U_Σ
≠
K_Σ \ ReadablePart(K_Σ)
```

is not assumed.

As with the prior foreground/background discussion, unread or unresolved aspects need not be a simple set-theoretic remainder after subtraction.

Residual not-yet may overlap with readable relations and may become visible under another Slice.

---

## 11. Stability as Local Inspectability

A provisional predicate may be:

```text
Inspectable(K_Σ ; B,c)
```

The intended meaning is not human observation alone.

It means that the local scene is sufficiently articulated for distinctions, relations, and continuation conditions to be checked or handled.

A candidate Stability condition is:

```text
StableScene(K_Σ ; S,B,c)
⇔
Readable(K_Σ ; S,B,c)
∧
Inspectable(K_Σ ; B,c)
∧
Continuable(K_Σ ; S,B,c)
```

This is only illustrative.

Risks include:

```text
making inspectability Operator-dependent in every case
reducing readability to conscious observation
forcing binary truth values
assuming continuation can already be completely known
```

No predicate is adopted yet.

---

## 12. Stability as a Temporary Resting Configuration

The phrase:

```text
一旦、落ち着く
```

is useful but must be handled carefully.

It does not mean:

```text
motion stops
Difference disappears
no further Slice is needed
```

It means:

```text
the current articulation has enough coherence
for it to be treated as one continuing establishment
```

A provisional mathematical analogy is a metastable or viable region rather than a fixed point.

However, Gyro Stability must not be identified directly with metastability or viability until the necessary assumptions are checked.

---

## 13. Candidate Mathematical Types

| Candidate | What it captures | What it loses |
|---|---|---|
| Scalar state quantity | degree, confidence, deviation tolerance | local content, residual not-yet, continuation structure |
| Predicate / condition | whether readable and continuable | internal scene and structure |
| Relation | Context dependence and connection | local settled configuration |
| Region / neighbourhood | tolerance, local variation, non-point stability | may assume space or topology too early |
| Structured local scene | articulation, readable relations, residual not-yet, continuation | requires a new composite object or schema |
| Viability set | ability to continue under transitions | requires a defined transition dynamics |
| Metastable region | temporary settlement under movement | may impose physical or probabilistic assumptions |

The current strongest candidate is:

```text
structured local scene
+
readability condition
+
continuation relation
```

rather than any one candidate alone.

---

## 14. Relation to Slice

The prior Slice notation was:

```text
S \xRightarrow{Σ_{B,c}} a_Σ
```

Stability may then be represented as:

```text
a_Σ
\xRightarrow{Stab_{S,B,c}}
K_Σ
```

where:

```text
K_Σ
```

is not merely a score.

It is the local scene in which `a_Σ` becomes readable and continuable.

Thus:

```text
S
\xRightarrow{Σ_{B,c}}
a_Σ
\xRightarrow{Stab_{S,B,c}}
K_Σ
```

The second arrow should not be interpreted as Stability actively evaluating or transforming the articulation.

It only indicates that the articulation is now represented in a Stability state.

---

## 15. Relation to the Next Structure

A stable scene may become incorporated into the next Structure:

```text
K_Σ
→
ρ_Σ
→
S_{n+1}
```

where:

```text
ρ_Σ
```

is the readability condition retained or incorporated from the scene.

However:

```text
K_Σ
≠
ρ_Σ
```

The whole stable scene need not be retained.

Only some distinctions, relations, criteria, or continuation conditions may be incorporated.

---

## 16. Failure Cases

### 16.1 Score Collapse

```text
Stability = scalar score
```

This loses the local established scene.

### 16.2 Predicate Collapse

```text
Stability = true / false
```

This loses internal readable content and residual not-yet.

### 16.3 Fixed-point Collapse

```text
Stability = no further change
```

This contradicts continuation through change.

### 16.4 Complete-determination Collapse

```text
Stability = all local not-yet disappears
```

This removes Re-Slice, Difference, ambiguity, and future branching.

### 16.5 Global-closure Collapse

```text
one stable scene = Structure fully completed
```

This contradicts the global not-yet character of Structure.

### 16.6 Observation Collapse

```text
Stability exists only when a human verifies it
```

This makes Stability unnecessarily anthropocentric.

---

## 17. Current Working Position

The present working position is:

```text
Stability is not adequately represented by a scalar,
predicate, or relation alone.

It is provisionally better understood as a structured local scene
in which the Slice articulation has settled enough
for it to be read and handled as a continuing establishment.

The scene may still contain residual local not-yet,
Difference, ambiguity, and multiple possible continuations.

Therefore, Stability is local inspectability and continuability
without global or complete local closure.
```

Japanese:

```text
Stabilityとは、Sliceによって現れた局所的な「こうなった」が、
一旦落ち着いて確認しやすくなり、
継続可能な一つの成立として扱える場面である。

ただし、その場面の内部にも別の未が残り得る。
```

This is not a replacement definition.

---

## 18. Open Questions

1. Is `scene` too perceptual or visual as a theoretical term?
2. Should Stability be modeled as a local region, structured object, or pair of object and predicate?
3. Is inspectability essential, or only one form of readability?
4. How should residual local not-yet be represented without simple subtraction?
5. Can one Slice articulation support multiple Stability scenes under different Orientations?
6. Does Continuability belong inside the Stability object or as a relation from it?
7. What minimum variation may occur while the same stable scene remains readable?
8. How should Critical and Unstable states relate to the candidate scene model?
9. Can a stable scene include a Jump possibility?
10. What part of a stable scene becomes incorporated readability in the next Structure?

---

## 19. Core Change Status

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
