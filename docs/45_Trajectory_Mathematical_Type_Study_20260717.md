# Trajectory Mathematical Type Study v0

## 1. Purpose

This document begins **A-3 Trajectory** after the preliminary studies of:

```text
A-1 Incorporated Readability
A-2 Continuity Readability
```

The invariant Core remains unchanged:

```text
Structure
↓
Slice
↓
Stability
```

Trajectory remains a derivative concept.

The present question is:

```text
What kind of mathematical object is Trajectory?
```

The purpose is not to select one final formalism immediately.

It is to separate several candidates that are easily collapsed:

```text
a sequence of local realizations
relations among local realizations
a tracing operation
a readable traced configuration
```

---

## 2. Starting Intuition

The current theoretical image is:

```text
Gyro realizations accumulate, overlap, and fold.

Their traces and relations may later be followed
under a particular Orientation and Slice.

When followed, a trajectory becomes readable.
```

Japanese:

```text
成立や変化が積み重なり、折り重なり、痕跡を残す。

それらをあるOrientationとSliceのもとで辿ると、
軌跡として読める。
```

Therefore:

```text
Trajectory
≠
pre-existing road
```

```text
Trajectory
≠
simple continuation
```

```text
Trajectory
≠
stored history
```

```text
Trajectory
≠
final result
```

---

## 3. Four Mathematical Layers

A first mathematical distinction is:

```text
1. local Gyro realizations
2. retained traces and relations
3. tracing operation
4. readable trajectory
```

These should not be represented by one symbol too early.

### 3.1 Local realizations

Let a local Gyro realization be:

```text
g_i = (S_i, Σ_i, a_i, K_i)
```

where:

```text
S_i = Structure section
Σ_i = Slice process
a_i = local “こうなった”
K_i = Stability scene or state
```

The indexed family:

```text
G = {g_i}_{i∈I}
```

contains local realizations.

But:

```text
G
≠
Trajectory
```

A collection or sequence of local realizations does not automatically constitute one trajectory.

### 3.2 Retained traces and relations

Let:

```text
E ⊆ G × ℛ × G
```

be a family of labelled relations.

An element:

```text
(g_i, r, g_j) ∈ E
```

means that `g_i` and `g_j` may be connected through relation `r`.

Possible labels include:

```text
causal succession
functional succession
semantic inheritance
material transfer
incorporated readability
Difference correspondence
Boundary correspondence
Operator Response linkage
identity continuity
transformation relation
```

No universal relation type is adopted.

### 3.3 Tracing operation

Let the current tracing conditions be:

```text
C_T = (B,c,Σ_T)
```

where:

```text
B = Operator Orientation
c = Context
Σ_T = Trajectory-oriented Slice
```

A provisional tracing operation is:

```text
Trace_{C_T}(G,E)
```

This operation does not freely invent connections.

It may:

```text
select admissible relations
follow some relations
ignore or defer others
allow gaps
connect branches
re-read earlier traces
```

### 3.4 Readable trajectory

The result of tracing is provisionally written:

```text
T_{C_T} = Trace_{C_T}(G,E)
```

However, `T_{C_T}` must not be interpreted as a final answer or a permanently fixed line.

It is a readable relational configuration under the current tracing conditions.

---

## 4. Trajectory Is Not Merely a Sequence

The simplest candidate is:

```text
T = (g_0,g_1,g_2,...)
```

This is useful when:

```text
one temporal order is sufficient
there is no branching
there are no merges
gaps are negligible
reinterpretation is unnecessary
```

However, Gyro Trajectory may include:

```text
branching
merging
Jump
Re-Slice
Defer
partial unreadability
retrospective reinterpretation
multiple valid tracings
```

Therefore:

```text
Trajectory
≠
ordered state sequence in general
```

A sequence may be one special case.

---

## 5. Trajectory Is Not Merely a Graph

A labelled directed graph is a stronger candidate:

```text
𝒢 = (G,E)
```

where local realizations are vertices and traceable relations are edges.

Advantages:

```text
branching and merging are expressible
relations may be labelled
gaps may be represented
multiple paths may coexist
```

However:

```text
𝒢
≠
Trajectory
```

The graph represents available traces and relations.

A readable Trajectory is one relational tracing through or across that graph under current conditions.

Thus:

```text
trace-bearing graph
≠
traced trajectory
```

---

## 6. Trajectory Is Not Merely a Path

In graph theory or topology, a path is usually a specified sequence or continuous map.

This is useful, but it may be too narrow.

A Gyro Trajectory may:

```text
contain incomplete intervals
jump between sections
follow relations of different types
include branching before later selection
be retrospectively redrawn
```

Therefore, the word `path` should be used carefully.

A Trajectory may be path-like after tracing, but the trace-bearing material need not already be one path.

---

## 7. Trajectory as a Readable Relational Configuration

The current strongest candidate is:

```text
Trajectory
=
a readable relational configuration
obtained by tracing admissible relations
among accumulated local Gyro realizations
under Orientation- and Context-relative conditions
```

Japanese candidate:

```text
Trajectoryとは、積み重なった局所的なGyro実現の間にある
許容可能な関係を、OrientationとContextに応じて辿ることで
読まれる関係的構成である。
```

This is not adopted as the final definition.

The phrase `relational configuration` is used because Trajectory may contain:

```text
order
branching
merging
gaps
relation labels
local depth
multiple overlapping courses
```

without being reducible to one line.

---

## 8. Tracing and Reading Must Be Separated

A useful distinction is:

```text
Traceability
=
whether relations can be followed
```

```text
Tracing
=
the process of following selected relations
```

```text
Trajectory Readability
=
whether the traced configuration can be read as one intelligible course
```

Therefore:

```text
Traceable relations
≠
Trajectory automatically
```

and:

```text
Tracing operation
≠
Trajectory itself
```

A provisional relation is:

```text
ReadableTrajectory(T_{C_T})
```

or more explicitly:

```text
TR(G,E ; C_T)
⇔
Readable(Trace_{C_T}(G,E) ; C_T)
```

This is only a schema.

---

## 9. Relation to Continuity Readability

Continuity Readability concerns whether two or more local realizations can be read as connected through an admissible relation.

```text
CR(g_i,g_j ; C_T)
```

Trajectory concerns a broader traced configuration:

```text
T_{C_T} = Trace_{C_T}(G,E)
```

Thus:

```text
Continuity Readability
=
local or pairwise traceability condition
```

```text
Trajectory
=
readable configuration formed through multiple traceable relations
```

However, Trajectory need not be reducible to pairwise continuity alone.

Higher-order relations may matter:

```text
a relation becomes meaningful only across three or more realizations
a pattern appears only over an interval
branching alternatives affect later interpretation
```

Therefore, a simple graph edge model may eventually require hyperedges, event structures, or another richer relation model.

---

## 10. Relation to Incorporated Readability

Incorporated Readability changes the conditions from which later Slice begins.

It may also affect which Trajectory becomes readable.

Let the incorporated readability context be:

```text
Γ_n
```

Then tracing may be written more explicitly as:

```text
T_{B,c,Γ} = Trace_{B,c,Γ}(G,E)
```

This expresses:

```text
what has already become usable in prior reasoning or recognition
changes which relations are salient, admissible, or connectable now
```

But:

```text
Γ
≠
Trajectory
```

`Γ` conditions the tracing.

Trajectory is what becomes readable through the tracing.

---

## 11. Trajectory Is Slice-relative but Not Arbitrary

Different Orientation and Context may produce different valid Trajectory readings from the same trace-bearing material.

```text
T_{B_1,c_1}
≠
T_{B_2,c_2}
```

This does not imply arbitrariness.

A valid tracing must be constrained by:

```text
available traces
admissible relations
Difference
Boundary
Context
causal or functional constraints
retained readability
```

Thus:

```text
non-unique
≠
arbitrary
```

and:

```text
Slice-relative
≠
freely invented
```

---

## 12. Trajectory May Be Retrospective

Trajectory need not be fully readable while events are occurring.

A later Slice may reveal a relation that was previously unavailable.

Therefore:

```text
T^{(n)}
```

may be the trajectory readable at stage `n`, while:

```text
T^{(n+1)}
```

may reinterpret earlier realizations.

```text
T^{(n+1)}
≠
T^{(n)} + one new point
```

The later reading may:

```text
reweight earlier traces
connect previously separate sections
split a formerly unified course
reclassify a gap as Jump or continuity
```

This suggests an update relation:

```text
T^{(n+1)} = ReTrace(T^{(n)}, g_{n+1}, Γ_{n+1}, C_{T,n+1})
```

This is a provisional schema, not an adopted equation.

---

## 13. Time Is Not Sufficient

Trajectory often involves time, but chronological order alone is insufficient.

```text
t_i < t_j
```

does not imply:

```text
g_i \leadsto g_j
```

Likewise, a long interval does not necessarily break a Trajectory.

Therefore:

```text
chronology
≠
continuity
```

Time may be one relation label or one constraint among others.

The index set `I` may be:

```text
discrete
continuous
partially ordered
event-indexed
hybrid
```

No single global time model is adopted yet.

---

## 14. Candidate Mathematical Families

### 14.1 Sequence

Useful for:

```text
simple linear implementation
ordered observations
basic runtime history
```

Risk:

```text
forces one line
```

### 14.2 Labelled directed graph

Useful for:

```text
branching
merging
multiple relation types
```

Risk:

```text
confuses available relation structure with the readable Trajectory
```

### 14.3 Hypergraph

Useful for:

```text
higher-order relations
patterns requiring multiple realizations
```

Risk:

```text
complexity may exceed current needs
```

### 14.4 Event structure or partial order

Useful for:

```text
concurrency
non-total temporal order
causal dependence
```

Risk:

```text
may overemphasize events and causality
```

### 14.5 Category-like path or morphism family

Useful for:

```text
composition
transformation
identity and non-identity continuity
```

Risk:

```text
may hide local state content and readability
```

### 14.6 Independent Gyro trajectory object

Useful if no existing family preserves:

```text
accumulation
folding
traceability
retrospective reading
Slice relativity
non-arbitrariness
```

Risk:

```text
premature invention of new mathematics
```

---

## 15. Current Leading Position

The current leading position is not one mathematical object alone.

It is a layered representation:

```text
Trace-bearing substrate
+
labelled admissible relations
+
Orientation-relative tracing
+
readable relational configuration
```

Provisionally:

```text
𝔗 = (G,E,Trace,Read)
```

where:

```text
G = local Gyro realizations
E = retained labelled relations
Trace = tracing process under current conditions
Read = trajectory readability condition
```

Then:

```text
T_{C_T} = Read(Trace_{C_T}(G,E))
```

should be read conceptually, not as a conventional numeric function equation.

The distinction among `G`, `E`, `Trace`, and `T` is currently more important than choosing graph theory, topology, category theory, or another field.

---

## 16. Failure Cases

### 16.1 Sequence Collapse

```text
Trajectory = chronological list
```

This loses branching, merging, gaps, and retrospective reinterpretation.

### 16.2 Graph Collapse

```text
Trajectory = all available relations
```

This confuses trace-bearing material with a currently readable tracing.

### 16.3 Path Collapse

```text
Trajectory = one continuous line
```

This excludes Jump and overlapping courses.

### 16.4 History Collapse

```text
Trajectory = stored past
```

This ignores relation selection and readability.

### 16.5 Operator Creation Collapse

```text
Trajectory exists only because Operator draws it
```

This ignores retained constraints and admissible relations.

### 16.6 Objective Unique Line Collapse

```text
there is always one uniquely correct Trajectory
```

This ignores Slice-relative readings.

### 16.7 Arbitrary Narrative Collapse

```text
any coherent story is a valid Trajectory
```

This ignores relation and evidence constraints.

---

## 17. Current Working Expression

The current working expression is:

```text
Trajectory is not the accumulated realizations themselves.

It is not all relations among them.

It is not the tracing operation alone.

Trajectory is the relational configuration that becomes readable
when admissible relations among accumulated and folded Gyro realizations
are traced under a particular Orientation, Context, and Slice.
```

Japanese:

```text
Trajectoryとは、積み重なった局所的実現そのものでも、
それらの間にある関係の総体でも、辿る操作そのものでもない。

積み重なり折り重なった局所的実現の間にある
許容可能な関係を、特定のOrientation・Context・Sliceのもとで
辿ることによって読まれる関係的構成である。
```

This remains a mathematical study position, not a final Core definition.

---

## 18. Open Questions

1. Is a graph sufficient, or are higher-order relations required?
2. Is Trajectory itself a mathematical object, or a readable property of a tracing?
3. Must every Trajectory contain temporal ordering?
4. How should Jump and gaps be represented?
5. Can multiple incompatible but valid Trajectories coexist?
6. What makes one tracing sufficiently coherent to count as one Trajectory?
7. How does retrospective reinterpretation change prior connections?
8. Is Trajectory Readability a Stability-like condition at a broader scale?
9. What is the exact relation between Trajectory and Dynamic Equivalence?
10. How should GyroAuth represent a current authenticated Trajectory without assuming a fixed line?

---

## 19. Core Change Status

```text
Core change: none
```

Trajectory remains derivative.

No change is made to:

```text
Structure
↓
Slice
↓
Stability
```
