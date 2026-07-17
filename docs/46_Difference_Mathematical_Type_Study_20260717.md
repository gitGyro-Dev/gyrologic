# Difference Mathematical Type Study v0

## 1. Purpose

This document begins the mathematical study of **Difference** in Gyro Logic.

The invariant Core remains unchanged:

```text
Structure
↓
Slice
↓
Stability
```

Difference is not added to the Core.

The central question is:

```text
What mathematical kind of object is Difference?
```

Candidate answers include:

```text
metric distance
residual
relation
directed discrepancy
local field
comparison result
structured difference object
```

No candidate is adopted yet.

---

## 2. Starting Position

Difference should not be identified with a pre-existing numeric gap.

A safer starting point is:

```text
Difference is what becomes readable as non-coincidence,
misalignment, contrast, deviation, or distinction
under a particular Slice.
```

Japanese:

```text
Differenceとは、あるSliceのもとで、
非一致・ずれ・対比・偏差・区別として読めるようになった差異である。
```

This does not mean that Slice freely creates every Difference.

Structure may already contain:

```text
variation
gradient
heterogeneity
asymmetry
change
latent distinction
```

But these are not automatically readable as one particular Difference.

Thus:

```text
latent variation
≠
readable Difference
```

---

## 3. Difference Is Relational

Difference does not normally exist as an isolated property of one item.

It appears relative to some comparison relation.

```text
Difference
=
Difference between or among something
```

The compared terms may be:

```text
state and state
expected and observed
Orientation and local articulation
prior and later realization
inside and outside
one Boundary-relative position and another
one Trajectory reading and another
one Context and another
```

Therefore, a minimal candidate form is:

```text
Δ(x,y ; B,c,Σ)
```

where:

```text
x,y = compared terms
B = Operator Orientation
c = Context
Σ = Slice
```

However, binary comparison may be too narrow.

Some Differences may emerge only across:

```text
multiple elements
an interval
a distribution
a trajectory
a relational configuration
```

Therefore, a more general provisional form is:

```text
Δ_{B,c,Σ}(X)
```

where `X` may be a tuple, family, region, process, or relational configuration.

---

## 4. Difference Is Slice-relative

The same Structure may yield different Differences under different Slices.

Examples:

```text
authentication event
→ device Difference
→ behavioral Difference
→ temporal Difference
→ geographical Difference
```

```text
society
→ legal Difference
→ economic Difference
→ gender Difference
→ cultural Difference
```

```text
ocean
→ salinity Difference
→ temperature Difference
→ current Difference
→ ecological Difference
```

Thus:

```text
Δ
is not globally fixed independently of Slice
```

A safer notation is:

```text
Δ_{B,c,Σ}
```

rather than one global `Δ`.

This does not make Difference arbitrary.

The Slice-relative Difference remains constrained by Structure, evidence, relation, and Context.

---

## 5. Difference Is Not Error

Difference may indicate error, but need not.

```text
Difference
≠
Error
```

Examples:

```text
age Difference
language Difference
version Difference
role Difference
cultural Difference
expected behavioral variation
```

These may be meaningful without being wrong.

Error requires an additional norm, target, or admissibility condition.

A possible distinction is:

```text
Difference
=
readable non-coincidence

Error
=
Difference judged against a norm or target
```

Therefore:

```text
Error(x)
may depend on
Δ(x,target)
+
criterion
```

but Difference itself does not perform that judgment.

---

## 6. Difference Is Not Boundary

Boundary and Difference are related but distinct.

```text
Difference
=
readable non-coincidence, gradient, or distinction
```

```text
Boundary
=
a Difference that has become usable as a Slice-relative distinction
```

Thus:

```text
Difference
may remain distributed, gradual, multidimensional, or ambiguous
```

while:

```text
Boundary
provides a readable distinction or separation
```

A provisional relation is:

```text
Difference
+
Slice-relative stabilization
→
Boundary
```

This is conceptual, not a formal equation.

Not every Difference becomes Boundary.

For example:

```text
gradual temperature variation
```

may remain a field of Difference without one clear Boundary.

---

## 7. Difference Is Not Necessarily Distance

The simplest mathematical candidate is a metric:

```text
d(x,y) ∈ ℝ_{>=0}
```

with properties such as:

```text
d(x,y) = 0 iff x = y
symmetry
triangle inequality
```

Gyro Difference does not necessarily satisfy these.

### 7.1 Zero Difference

```text
Δ(x,y)=0
```

need not imply absolute identity.

Two distinct objects may be indistinguishable under the current Slice.

Thus a pseudometric-like model may be more appropriate than a metric in some cases.

### 7.2 Asymmetry

```text
Δ(x,y)
```

may differ from:

```text
Δ(y,x)
```

For example:

```text
deviation from expected behavior
```

is directional.

Therefore a divergence or quasi-metric may be more suitable.

### 7.3 Triangle Inequality

The relation among three realizations may not satisfy triangle inequality.

Context, Boundary, or Orientation may change between comparisons.

Therefore:

```text
Difference
≠
metric by default
```

Metric distance remains a special case.

---

## 8. Difference May Be Structured

A single scalar may erase the kind of Difference.

For example, in authentication:

```text
Δ
=
(device,
 behavior,
 time,
 space,
 network,
 motion)
```

A provisional form is:

```text
Δ_{B,c,Σ}(x,y) ∈ D
```

where `D` is a structured Difference space.

Possible forms of `D` include:

```text
scalar
vector
ordered tuple
partially ordered set
relation-valued object
distribution
field
partially defined object
```

The theory should not assume that all Difference dimensions are directly comparable.

Thus:

```text
Δ_i ∥ Δ_j
```

may be allowed, meaning that two Difference dimensions are not currently comparable.

---

## 9. Difference May Be Local or Field-like

Difference need not appear only between two points.

It may vary across a Structure or local articulation.

A field-like candidate is:

```text
δ : U → D
```

where:

```text
U = a local region or articulated scene
D = Difference values or types
```

This may represent:

```text
gradient
local irregularity
spatial variation
temporal variation
relational tension
```

A Boundary may then correspond to a region where the Difference field becomes readable as a distinction.

However, field notation assumes that `U` and locality are already defined.

It should therefore remain a later candidate, not the starting definition.

---

## 10. Difference and Slice

Slice does not merely calculate Difference after the fact.

Through Slice, a Difference may become:

```text
localized
comparable
directional
weighted
readable
relevant
```

A provisional process image is:

```text
Structure S
↓
Slice Σ_{B,c}
↓
local articulation a_Σ
↓
Difference becomes readable within or across a_Σ
```

A candidate notation is:

```text
Δ_Σ = Diff(a_Σ ; S,B,c)
```

But `Diff` must not be interpreted as an evaluator that decides correctness.

It only represents the Difference made readable under the Slice.

---

## 11. Difference and Stability

Stability does not require zero Difference.

```text
Stability
≠
Δ = 0
```

A local scene may remain readable and continuable while Difference persists.

Therefore, Stability may depend on the compatibility of Difference with continuation.

A provisional relation is:

```text
Compatible(Δ_Σ, K_Σ ; B,c)
```

meaning:

```text
the readable Difference remains compatible
with the continuing establishment of the Stability scene
```

This is not yet a Stability definition.

It only preserves the principle:

```text
Difference may remain inside Stability
```

---

## 12. Difference and Trajectory

Difference may be read:

```text
between local realizations
within one local realization
across a traced trajectory
between alternative trajectory readings
```

A Trajectory-relative Difference may be written provisionally as:

```text
Δ_T(g_i,g_j ; B,c,Σ_T)
```

or more generally:

```text
Δ_T(T_1,T_2)
```

However:

```text
Difference sequence
≠
Trajectory
```

A sequence of Difference values is only one readable aspect of Trajectory.

Trajectory also contains relations, gaps, branches, Stability scenes, and reinterpretations.

---

## 13. Difference and Incorporated Readability

Once a Difference pattern has become readable, it may become incorporated into later Structure.

For example:

```text
recognized attack pattern
recognized behavioral deviation
recognized social inequality
recognized temperature anomaly
```

The later Slice may then begin with a changed Difference sensitivity.

A provisional update relation is:

```text
Γ_{n+1}
=
Update(Γ_n, pattern(Δ_n))
```

This means:

```text
the way later Difference is read
is altered by previously readable Difference patterns
```

Thus Difference is not only measured against a fixed background.

The criteria and sensitivity by which Difference becomes readable may themselves change.

---

## 14. Candidate Mathematical Types

### 14.1 Metric or Pseudometric

Useful when:

```text
Difference is scalar
symmetry is meaningful
local geometry matters
```

Risk:

```text
forces too much regularity
```

### 14.2 Divergence or Quasi-metric

Useful when:

```text
Difference is directional or asymmetric
```

Risk:

```text
still assumes a numeric codomain
```

### 14.3 Residual

Useful when:

```text
observed result is compared with expected result
```

Risk:

```text
privileges one target or norm
```

### 14.4 Relation

Useful when:

```text
Difference is qualitative, typed, or nonnumeric
```

Risk:

```text
may not express magnitude or direction
```

### 14.5 Structured Difference Object

Useful when:

```text
Difference has multiple heterogeneous dimensions
```

Risk:

```text
may become descriptive without mathematical discipline
```

### 14.6 Field-like Object

Useful when:

```text
Difference varies locally across a scene or Structure
```

Risk:

```text
requires prior spatial or topological assumptions
```

---

## 15. Current Strongest Candidate

The current strongest general position is:

```text
Difference is a Slice-relative structured relation of non-coincidence.
```

Japanese:

```text
Differenceとは、
あるOrientation・Context・Sliceのもとで読める、
非一致・ずれ・対比・偏差を表す構造化された関係である。
```

This is not adopted as a final definition.

The phrase `structured relation` is used because Difference may carry:

```text
direction
type
magnitude
locality
comparability
Context dependence
Trajectory dependence
```

No single scalar is assumed.

---

## 16. Preliminary Mathematical Schema

Let:

```text
S = Structure
B = Operator Orientation
c = Context
Σ = Slice
a_Σ = local articulation
X = compared terms or relational configuration
D = Difference codomain
```

Then:

```text
Δ_{B,c,Σ} : X ⇀ D
```

where `⇀` indicates that Difference may be partially defined.

The intended meaning is:

```text
under Orientation B, Context c, and Slice Σ,
a Difference becomes readable for X
with value or structure in D
```

A binary special case is:

```text
Δ_{B,c,Σ} : X × X ⇀ D
```

But the general theory should also allow:

```text
Δ_{B,c,Σ} : Rel(X) ⇀ D
```

for differences that arise from multi-element or relational configurations.

---

## 17. Failure Cases

### 17.1 Metric Collapse

```text
Difference = ordinary distance
```

This imposes symmetry, triangle inequality, and scalar comparability too early.

### 17.2 Error Collapse

```text
Difference = error
```

This treats all non-coincidence as failure.

### 17.3 Boundary Collapse

```text
Difference = Boundary
```

This loses gradual, distributed, or ambiguous Difference.

### 17.4 Scalar Collapse

```text
Difference = one number
```

This erases type, direction, and Context.

### 17.5 Structure-inherent Collapse

```text
Difference exists in one globally fixed form inside Structure
```

This ignores Slice-relative readability.

### 17.6 Operator-arbitrary Collapse

```text
Difference exists only because Operator invents it
```

This ignores retained variation, constraints, and evidence in Structure.

---

## 18. Current Working Position

```text
Difference is not necessarily distance, error, or Boundary.

It is a Slice-relative structured relation
by which non-coincidence, deviation, contrast, or distinction
becomes readable.

It may be scalar, vector-valued, relational, asymmetric,
partially ordered, field-like, or partially defined.

Stability may coexist with non-zero Difference.

Previously readable Difference patterns may become incorporated
and alter how later Difference becomes readable.
```

---

## 19. Open Questions

1. Does every Difference require explicit comparison terms?
2. Can Difference be intrinsic to one local scene rather than relational between scenes?
3. Is direction a necessary property of Gyro Difference?
4. Should Difference be represented by one object or a family of typed relations?
5. When does Difference become Boundary?
6. What makes a Difference admissible within Stability?
7. Can two Difference dimensions be incomparable?
8. How should latent variation be distinguished mathematically from readable Difference?
9. Can Difference change retrospectively when Trajectory is re-read?
10. What is the minimum structure of the Difference codomain `D`?

---

## 20. Core Change Status

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
