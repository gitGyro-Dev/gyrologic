# Slice as Local Articulation — Provisional Mathematical Expression v0

## 1. Purpose

This document proposes a first mathematical expression of the current Slice intuition:

```text
Sliceしたら、こうなった。
```

The invariant Core remains unchanged:

```text
Structure
↓
Slice
↓
Stability
```

The primary Slice definition also remains unchanged:

```text
Slice is the process by which a path is opened
through a Structure toward an establishment.
```

The purpose is not to define a final mathematical model.

It is to express the distinction between:

```text
local articulation through Slice
```

and:

```text
readable continuability in Stability
```

---

## 2. Why an Ordinary Function Is Too Strong

The simplest expression would be:

```text
Σ(S) = a
```

where:

```text
S = Structure
Σ = Slice
a = result
```

However, this notation suggests:

```text
one fixed input
→
one completed output
```

It may falsely imply that:

```text
- the output was already determined;
- Slice is instantaneous;
- Slice is only a completed mapping;
- a is already stable;
- a is a final result;
- the Structure is exhausted by a.
```

Therefore, an ordinary total function is insufficient as the primary model.

---

## 3. Articulation Space

For a Structure `S`, let:

```text
𝒜(S)
```

be a provisional family of local articulations that may become expressed through Slice.

An element:

```text
a ∈ 𝒜(S)
```

is not necessarily:

```text
- a complete state;
- a final answer;
- an independently existing object before Slice;
- a stable establishment;
- a globally determined section of Structure.
```

It means only:

```text
a local “this is how it has become”
that is articulated through Slice.
```

The notation `𝒜(S)` does not imply that all possible articulations are already enumerable before Slice.

It is a mathematical placeholder for the codomain of local articulation.

---

## 4. Slice as a Process Relation

Let:

```text
B = Operator Orientation
c = Context
```

A first candidate is:

```text
Σ_{B,c} : S ⇝ 𝒜(S)
```

or relationally:

```text
S \xRightarrow{Σ_{B,c}} a
```

where:

```text
a ∈ 𝒜(S)
```

The intended reading is:

```text
through Slice Σ under Orientation B and Context c,
Structure S becomes locally articulated as a.
```

Japanese:

```text
Orientation BとContext cのもとでSliceしたところ、
Structure Sは局所的にaとして「こうなった」。
```

The double arrow does not mean ordinary equality or deterministic transition.

It indicates a provisional process relation.

---

## 5. Slice-ing as an Indexed Process

To preserve the distinction between `slice-ing` and `slice-done`, let:

```text
τ ∈ I_Σ
```

be an internal Slice-process index.

This index is not necessarily physical time.

A Slice process may be represented provisionally as:

```text
α_Σ : I_Σ → 𝒜^*(S)
```

where `𝒜^*(S)` is a family of partial, emerging, or not-yet-completed articulations.

Then:

```text
α_Σ(τ)
```

means:

```text
the local articulation appearing at Slice-process position τ
```

The completed Slice position is represented by:

```text
τ = τ_Σ^*
```

and:

```text
a_Σ = α_Σ(τ_Σ^*)
```

Thus:

```text
slice-ing
=
{α_Σ(τ)}_{τ∈I_Σ}
```

and:

```text
slice-done
=
a_Σ
```

However:

```text
slice-done
≠
Stability
```

---

## 6. “こうなった” as Local Articulation

The simplest current expression is:

```text
S \xRightarrow{Σ_{B,c}} a_Σ
```

with the reading:

```text
Sliceしたら、局所的にa_Σとしてこうなった。
```

This is not:

```text
S = a_Σ
```

and not:

```text
a_Σ = final result
```

Instead:

```text
a_Σ
```

is a Slice-relative local articulation of `S`.

Therefore:

```text
a_Σ ⊏ S
```

may be used informally to mean:

```text
a_Σ is locally articulated through S
without exhausting S
```

But `⊏` is not adopted because it may be confused with subset, substructure, or strict order.

No containment relation is assumed yet.

---

## 7. Stability as a Separate Relation

Let:

```text
K(a_Σ ; S,B,c)
```

represent the Stability state associated with the articulated result `a_Σ`.

A candidate predicate is:

```text
Stable(a_Σ ; S,B,c)
```

with the intended meaning:

```text
a_Σ is readable as an establishment that can continue
under the relevant Structure, Orientation, and Context.
```

Thus:

```text
S \xRightarrow{Σ_{B,c}} a_Σ
```

does not imply:

```text
Stable(a_Σ ; S,B,c)
```

The Core distinction becomes:

```text
S
\xRightarrow{Σ_{B,c}}
a_Σ
\xrightarrow{Stability}
K_Σ
```

More explicitly:

```text
Slice:
S \xRightarrow{Σ_{B,c}} a_Σ
```

```text
Stability:
K_Σ = Stab(a_Σ ; S,B,c)
```

This preserves:

```text
こうなった
≠
継続可能な成立として読める
```

---

## 8. “こうなった。どう？”

The conversational image:

```text
こうなった。どう？
```

may be expressed as:

```text
S \xRightarrow{Σ_{B,c}} a_Σ
```

followed by an open Stability evaluation:

```text
Stab(a_Σ ; S,B,c) = ?
```

This question mark is conceptual, not a formal value.

The intended structure is:

```text
local articulation has appeared
+
its readable continuability is not yet settled
```

Therefore:

```text
Slice
=
articulation-producing process
```

but not:

```text
Slice
=
evaluation
```

---

## 9. Non-deterministic and Partial Character

The same Structure under different Orientation or Context may produce different local articulations:

```text
S \xRightarrow{Σ_{B_1,c_1}} a_1
```

```text
S \xRightarrow{Σ_{B_2,c_2}} a_2
```

with:

```text
a_1 ≠ a_2
```

Even under apparently similar conditions, Slice may be non-deterministic or only partially determined.

Therefore, the mathematical object may be closer to a relation:

```text
R_Σ ⊆ S × B × C × 𝒜(S)
```

where:

```text
(S,B,c,a) ∈ R_Σ
```

means:

```text
a is one local articulation that may appear
through Slice under B and c.
```

This relation does not imply that every `S,B,c` combination has an articulation.

Thus Slice may be partial.

---

## 10. Structure Is Not Consumed

The articulation `a_Σ` is not subtracted from Structure.

```text
S - a_Σ
```

is not defined as the remaining background.

Likewise:

```text
S = a_Σ ∪ remainder
```

is not assumed.

The relation is better understood as:

```text
S remains globally not-yet
while a_Σ becomes locally articulated
```

A provisional notation is:

```text
Articulated(a_Σ | S,Σ,B,c)
```

rather than:

```text
a_Σ ⊆ S
```

This avoids premature set-theoretic reduction.

---

## 11. Local Determination Without Global Closure

The integrated mathematical image is:

```text
S \xRightarrow{Σ_{B,c}} a_Σ
```

subject to:

```text
Local(a_Σ ; S)
```

and:

```text
¬Exhausts(a_Σ ; S)
```

The intended meaning is:

```text
a_Σ is local relative to S
and does not exhaust S
```

A Stability state may then be represented as:

```text
K_Σ = Stab(a_Σ ; S,B,c)
```

Therefore:

```text
Structure
=
globally not exhausted
```

```text
Slice
=
local articulation process
```

```text
Stability
=
readable continuability of the articulation
```

---

## 12. Minimal Candidate Model

The current minimal candidate is:

```text
Σ_{B,c}
=
a partial process relation from Structure to local articulation
```

Formally:

```text
R_Σ ⊆ 𝒮 × 𝓑 × 𝓒 × 𝒜
```

where:

```text
𝒮 = family of Structures
𝓑 = family of Orientations
𝓒 = family of Contexts
𝒜 = family of local articulations
```

For one realization:

```text
(S,B,c,a_Σ) ∈ R_Σ
```

or:

```text
S \xRightarrow{Σ_{B,c}} a_Σ
```

Then Stability is separate:

```text
K_Σ = Stab(a_Σ ; S,B,c)
```

The entire local Core realization is:

```text
S
\xRightarrow{Σ_{B,c}}
a_Σ
\xrightarrow{Stab}
K_Σ
```

This is the current strongest minimal mathematical expression.

---

## 13. Example: Ocean

Let:

```text
S_o = ocean Structure
```

A salinity-oriented Slice may yield:

```text
S_o \xRightarrow{Σ_{salinity,c}} a_{salinity}
```

where `a_{salinity}` may be:

```text
a locally articulated salinity pattern
```

A current-flow-oriented Slice may yield:

```text
S_o \xRightarrow{Σ_{current,c}} a_{current}
```

These are not extracted pieces that consume the ocean.

They are different local articulations of how the ocean becomes readable under different Slices.

Whether either articulation is sufficiently readable and continuing belongs to Stability.

---

## 14. Example: GyroAuth

Let:

```text
S_u = current authentication Structure
```

An authentication Slice may yield:

```text
S_u \xRightarrow{Σ_{auth,c}} a_{auth}
```

where `a_auth` may include a locally articulated relation among:

```text
device behavior
location
motion
network
prior attack patterns
incorporated readability
current Difference
```

This does not yet mean:

```text
AUTH_STABLE
```

Stability is evaluated separately:

```text
K_{auth} = Stab(a_{auth} ; S_u,B_{auth},c)
```

Operator Response then reacts to `K_auth`.

---

## 15. Risks of This Model

### 15.1 Articulation-object Risk

Treating `a_Σ` as an object may falsely reify the local articulation.

### 15.2 Hidden-function Risk

The arrow notation may still be read as deterministic function application.

### 15.3 Process-index Risk

The internal index `τ` may be mistaken for physical time.

### 15.4 Stability-predicate Risk

A Boolean predicate may oversimplify multidimensional Stability.

### 15.5 Pre-enumeration Risk

The family `𝒜(S)` may be mistaken for a completed list of all possible articulations.

### 15.6 Operator-dependence Risk

Including `B` may make it appear that Operator creates Structure or freely invents articulation.

These risks must remain explicit.

---

## 16. Current Working Position

The present working position is:

```text
Slice is not best represented as a total function,
selection, extraction, filter, or completed transformation.

It is provisionally represented as a partial process relation
through which Structure becomes locally articulated as “this way.”

The articulation is not final, does not exhaust Structure,
and does not itself guarantee Stability.
```

Mathematically:

```text
S \xRightarrow{Σ_{B,c}} a_Σ
```

followed by:

```text
K_Σ = Stab(a_Σ ; S,B,c)
```

This is a candidate expression, not a final definition.

---

## 17. Open Questions

1. Should `a_Σ` be an object, relation, predicate, or event?
2. Is `𝒜(S)` a genuine mathematical space or only notation?
3. Does Slice require an internal process index?
4. Can local articulation be represented without reifying it as an object?
5. Is the Slice relation monotone in any sense?
6. Can two Slice processes yield the same articulation through different internal courses?
7. How should incomplete or interrupted Slice be represented?
8. How should Re-Slice relate to the prior articulation?
9. Is Stability a predicate, region, structured quantity, or viability relation over articulation?
10. Can this model support branching, merging, Jump, and Void without adding premature structure?

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
