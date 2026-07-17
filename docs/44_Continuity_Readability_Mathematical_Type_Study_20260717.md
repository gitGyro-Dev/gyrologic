# Continuity Readability Mathematical Type Study v0

## 1. Purpose

This document begins the mathematical study of **Continuity Readability** as Priority A-2.

The invariant Core remains unchanged:

```text
Structure
↓
Slice
↓
Stability
```

The Core captures one local realization.

Continuity Readability concerns what allows multiple local realizations to be read as connected.

This document does not introduce a new Core element and does not define one universal continuity relation.

---

## 2. Starting Position

The current conceptual distinction is:

```text
Identity
=
whether two changed realizations may be treated as the same entity
```

```text
Continuity Readability
=
whether one local realization can be meaningfully traced to another
```

Therefore:

```text
Identity
≠
Continuity Readability
```

A continuity relation may remain readable even when identity changes.

Likewise, identity may be asserted while the relation connecting two realizations remains unreadable.

---

## 3. Local Gyro Realizations

Let one local Gyro realization be represented provisionally as:

```text
g_i = (S_i, Σ_i, a_i, K_i)
```

where:

```text
S_i = Structure
Σ_i = Slice
a_i = local articulation produced through Slice
K_i = Stability scene or state
```

The exact internal representation of `g_i` is not fixed.

The important point is that each `g_i` represents one local realization of:

```text
Structure
→
Slice
→
Stability
```

---

## 4. Continuity Requires a Relation

Two local realizations are not continuous merely because they occur one after another.

```text
temporal adjacency
≠
continuity
```

Likewise:

```text
similarity
≠
continuity
```

A minimum requirement is that some relation can be traced between them.

Let:

```text
r ∈ ℛ_{ij}
```

where `ℛ_{ij}` is the family of possible relations between `g_i` and `g_j`.

Examples may include:

```text
causal succession
functional succession
semantic correspondence
material transfer
Boundary correspondence
Difference-pattern continuity
retained readability
response-to-orientation linkage
```

No single relation is assumed to be universal.

---

## 5. Traceable Relation

A provisional relation may be written:

```text
g_i \leadsto_r g_j
```

The intended meaning is:

```text
under relation r,
g_j can be traced from g_i
```

This does not imply:

```text
g_i = g_j
```

nor:

```text
Identity(g_i,g_j)
```

The relation only expresses that the transition, correspondence, or succession is followable.

---

## 6. Admissibility

Not every imaginable relation should count.

The relation must be admissible under the relevant conditions.

Let:

```text
Adm(r ; B,c)
```

mean:

```text
relation r is admissible
under Operator Orientation B and Context c
```

Then a minimal condition is:

```text
Conn(g_i,g_j ; B,c)
⇔
∃r ∈ ℛ_{ij} : Adm(r ; B,c) ∧ (g_i \leadsto_r g_j)
```

This means:

```text
there exists at least one admissible relation
through which g_i and g_j can be traced
```

This is a candidate schema, not a final definition.

---

## 7. Continuity Readability Is More Than Relation Existence

A relation may exist without being currently readable.

Therefore:

```text
relation existence
≠
Continuity Readability
```

Continuity Readability also requires that the relation can become readable under a Slice.

A provisional form is:

```text
CR(g_i,g_j ; B,c,Σ)
```

with the intended meaning:

```text
under Orientation B, Context c, and Slice Σ,
g_i and g_j are readable as connected
```

A candidate condition is:

```text
CR(g_i,g_j ; B,c,Σ)
⇔
∃r ∈ ℛ_{ij} :
Adm(r ; B,c,Σ)
∧
Traceable(g_i,g_j ; r)
∧
Readable(r ; Σ)
```

This separates:

```text
relation
traceability
readability
```

---

## 8. Continuity Readability Is Slice-relative

The same two realizations may be connected under one Slice and disconnected under another.

For example:

```text
legal succession
```

may remain readable while:

```text
material identity
```

does not.

Therefore:

```text
CR_{Σ_1}(g_i,g_j)
≠
CR_{Σ_2}(g_i,g_j)
```

may occur.

This does not make continuity arbitrary.

The Slice is constrained by available traces, relations, Context, Difference, Boundary, and incorporated readability.

Thus:

```text
Slice-relative
≠
freely invented
```

---

## 9. Incorporated Readability as a Continuity Resource

A later Structure may already include readability acquired from earlier realizations.

Let:

```text
Γ_i
```

be the context of definitions, distinctions, relations, and locally established readings available after `g_i`.

Then:

```text
Γ_{i+1} = Update(Γ_i, q_i)
```

where `q_i` is some newly incorporated readability.

This may make a later relation easier to trace:

```text
Γ_i
→
relation becomes available
→
continuity becomes readable
```

Therefore, incorporated readability may function as a resource or condition for Continuity Readability.

However:

```text
incorporated readability
≠
Continuity Readability itself
```

It changes what can later be connected and traced.

---

## 10. Continuity Readability as a Relation on Local Realizations

The simplest mathematical candidate is a binary relation:

```text
CR_{B,c,Σ} ⊆ G × G
```

where `G` is a family of local Gyro realizations.

Then:

```text
(g_i,g_j) ∈ CR_{B,c,Σ}
```

means:

```text
g_i and g_j are readable as connected
under B, c, and Σ
```

This relation need not be:

```text
symmetric
transitive
reflexive
```

For example:

```text
g_i may be traceable into g_j
```

without:

```text
g_j being traceable back into g_i
```

Therefore, an ordinary equivalence relation is currently too strong.

---

## 11. Directed Graph Candidate

Another candidate is a directed graph:

```text
𝒢 = (G,E)
```

where:

```text
G = local Gyro realizations
E = admissible traceable connections
```

An edge:

```text
g_i → g_j
```

means that `g_j` can be traced from `g_i` under some admissible relation.

Advantages:

```text
branching can be represented
merging can be represented
Jump can be represented
gaps can be represented
multiple relation types can be labelled
```

Risks:

```text
realizations may not be discrete points
relations may be higher-order
one edge may oversimplify internal Slice processes
Context dependence may be hidden
```

Thus, a graph is useful but not yet adopted as the final model.

---

## 12. Category-like Candidate

A category-like model may represent local realizations as objects and traceable transformations as morphisms.

```text
g_i \xrightarrow{r} g_j
```

This is attractive because transformations may compose:

```text
g_i \xrightarrow{r_1} g_j
\xrightarrow{r_2} g_k
```

However, composition may fail or change meaning when Context, Orientation, or Slice changes.

Thus:

```text
r_2 ∘ r_1
```

may not always be available or meaningful.

This makes ordinary category structure potentially too rigid unless enriched, indexed, or partial forms are used.

No category-theoretic model is adopted at this stage.

---

## 13. Continuity Is Not Necessarily Linear

A simple sequence:

```text
g_0 → g_1 → g_2 → ...
```

is only one case.

Gyro Logic must allow:

```text
branching
merging
multiple simultaneous relations
retrospective reinterpretation
Re-Slice
Jump
Void intervals
partial loss of traceability
```

Therefore, Continuity Readability should not be reduced to a single linear time series.

---

## 14. Current Mathematical Position

The current strongest minimal model is:

```text
local realizations G
+
possible relation families ℛ
+
admissibility conditions Adm
+
traceability
+
Slice-relative readability
```

represented provisionally as:

```text
CR(g_i,g_j ; B,c,Σ)
⇔
∃r ∈ ℛ_{ij} :
Adm(r ; B,c,Σ)
∧
Traceable(g_i,g_j ; r)
∧
Readable(r ; Σ)
```

This is intentionally weak.

It does not define what the meaningful relation must be.

It only states that continuity becomes readable when some admissible relation can be traced and read under the current Slice.

---

## 15. Current Interpretation

```text
Continuity Readability is not identity,
similarity, chronology, or stored history.

It is the condition under which one local realization
can be traced to another through an admissible relation
and read as connected under a particular Slice.
```

Japanese:

```text
Continuity Readabilityとは、
前後の局所的な成立の間にある何らかの関係が、
現在のOrientation・Context・Sliceのもとで辿ることができ、
接続したものとして読める状態である。
```

This is not yet a final definition.

---

## 16. Open Questions

1. Is Continuity Readability best treated as a relation, predicate, or structured state?
2. Does every traceable relation require direction?
3. Can continuity be readable without temporal order?
4. When may traceable relations compose?
5. How should multiple competing continuity relations be represented?
6. Can one relation be readable while another remains Void-like?
7. How should retrospective reinterpretation update earlier connections?
8. Is a graph, hypergraph, category, or indexed relation family the most suitable next model?
9. How should Difference constrain traceability?
10. How should Continuity Readability contribute to Trajectory without becoming Trajectory itself?

---

## 17. Core Change Status

```text
Core change: none
```

The invariant Core remains:

```text
Structure
↓
Slice
↓
Stability
```
