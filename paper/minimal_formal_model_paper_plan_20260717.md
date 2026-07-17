# Paper Plan: A Minimal Formal Model for Gyro Logic

## 1. Status

```text
Document type: Paper architecture and contribution plan
Paper type: New independent paper
Repository layer: Gyro Logic
Formalization status: exploratory-integrated
Canonical Core status: unchanged
Target publication: Jxiv preprint candidate
```

This document defines the scope, novelty, structure, and writing sequence of a new Gyro Logic paper based on the mathematical studies completed in `docs/37` through `docs/48`.

The paper is not a replacement for the already published introductory Gyro Logic preprint.

The published introductory paper remains the foundational answer to:

```text
What is Gyro Logic?
```

The new paper addresses a different question:

```text
How can the current Gyro Logic concepts be given a minimal formal organization
without reducing them to existing mathematical objects or changing the invariant Core?
```

---

## 2. Proposed Titles

### 2.1 Primary English Title

```text
A Minimal Formal Model for Gyro Logic:
Local Articulation, Stability Scenes, and Contextual Tracing
```

This title is recommended because it makes the mathematical contribution explicit and identifies the three concepts that distinguish the paper from the introductory work.

### 2.2 Primary Japanese Title

```text
Gyro Logicの最小形式モデル：
局所的表出・Stability Scene・文脈的Tracing
```

The Japanese wording for the three technical expressions should be reviewed before final submission.

Candidate alternatives:

```text
局所的な「こうなった」
局所的表出
局所的成立形
```

```text
安定化場面
可読・継続可能な局所場面
Stability Scene
```

```text
文脈的追跡
文脈依存的Tracing
文脈的Trajectory読解
```

### 2.3 Broader Alternative

```text
Toward a Minimal Formal Model of Gyro Logic:
Structure, Slice, Stability, and Contextual Trajectory
```

Japanese:

```text
Gyro Logicの最小形式モデルに向けて：
Structure・Slice・Stabilityと文脈的Trajectory
```

This title is more accessible but less precise about the formal distinctions introduced by the paper.

---

## 3. Relation to the Existing Gyro Logic Paper

### 3.1 Existing Paper

The existing introductory paper presents:

```text
Gyro Logic as a theoretical framework
Invariant Core
Structure → Slice → Stability
Major derivative concepts
Layer relationship
General theoretical motivation
```

Its primary role is foundational and explanatory.

### 3.2 New Paper

The new paper presents:

```text
mathematical type studies
formal separation of process and local articulation
structured interpretation of Stability
formal treatment of incorporated readability
continuity readability
contextual construction of Trajectory
non-metric Difference
comparison with existing mathematical fields
```

Its primary role is formal and comparative.

### 3.3 Non-duplication Principle

The new paper must not repeat the introductory paper section by section.

The invariant Core should be introduced only to the degree necessary to establish the formal problem.

The paper should cite the introductory paper as the source of the framework and focus on the new formal distinctions.

---

## 4. Invariant Principle

The following remains unchanged:

```text
Structure
↓
Slice
↓
Stability
```

Canonical definitions remain unchanged:

```text
Structure is the mode in which something can be established.

Slice is the process by which a path is opened through a Structure toward an establishment.

Stability is the state in which an opened path becomes readable as an establishment that can continue.
```

The mathematical forms introduced in this paper are supporting formal candidates.

They do not replace the canonical definitions.

---

## 5. Central Problem

Existing mathematical formalisms tend to impose one or more of the following assumptions:

```text
objects are already individuated
state spaces are given in advance
relations are already available
transformations have fixed domains and codomains
trajectories are state sequences
stability is a scalar, equilibrium, or fixed point
Difference is metric distance or error
history is stored data
```

Gyro Logic requires a weaker and more heterogeneous formal organization because:

```text
Structure is not fixed as one mathematical object type.
Slice is a process in which a local articulation becomes available.
Stability is a readable and continuable local scene.
Readability acquired through one realization may alter later Structure conditions.
Trajectory becomes readable through contextual tracing of admissible relations.
Difference need not be metric, scalar, or error-like.
```

The paper therefore asks:

```text
What is the smallest formal schema that preserves these distinctions
without prematurely reducing Gyro Logic to an existing mathematical field?
```

---

## 6. Main Contributions

### Contribution 1: Formal typing without changing the Canonical Core

The paper introduces a minimal formal schema while preserving:

```text
Structure → Slice → Stability
```

The formal model is explicitly supporting and exploratory rather than a replacement definition.

### Contribution 2: Separation of Slice process and local articulation

The paper separates:

```text
Slice process
≠
slice-relative local articulation
```

A local Gyro realization is provisionally represented by:

```text
g_n = (S_n, B_n, c_n, Σ_n, a_n, K_n)
```

where:

```text
Σ_n = Slice process

a_n = local articulation appearing through that Slice
```

The central relation is:

```text
S_n \xRightarrow{Σ_{B_n,c_n}} a_n
```

This avoids treating Slice as extraction of a pre-existing object or path.

### Contribution 3: Stability is not reduced to a scalar or fixed point

Stability is represented as a structured local scene:

```text
K_n = (a_n, L_n, U_n, C_n^+)
```

where:

```text
a_n   = local articulation
L_n   = currently readable relations and distinctions
U_n   = residual local not-yet
C_n^+ = continuation conditions or available continuations
```

This permits:

```text
local establishment
+
remaining local not-yet
```

within one Stability scene.

### Contribution 4: Incorporated Readability is not history storage

The paper distinguishes incorporated readability from event logs or memory records.

```text
q_n = Inc(g_n)
```

```text
Γ_{n+1} = Update_Γ(Γ_n, q_n)
```

The update may include:

```text
addition
revision
integration
weight change
invalidation
loss of accessibility
```

### Contribution 5: Continuity Readability is separated from Identity

Continuity readability is represented as:

```text
CR(g_i, g_j ; B, c, Σ)
⇔
∃r : Adm(r) ∧ Traceable(r) ∧ Readable(r)
```

The model permits:

```text
continuity readable
+
identity false
```

and:

```text
identity asserted
+
continuity unreadable or disputed
```

### Contribution 6: Trajectory is separated from state sequences and logs

Let:

```text
G = {g_i}
```

and:

```text
E ⊆ G × ℛ × G
```

Then:

```text
𝒢_R = (G, E)
```

is a relation-bearing trace field, not the Trajectory itself.

Trajectory is read through contextual tracing:

```text
T_{B,c,Σ_T,Γ_T}
=
Trace_{B,c,Σ_T,Γ_T}(G,E)
```

This supports:

```text
branching
merging
gaps
retrospective reinterpretation
Re-Slice
Jump
```

### Contribution 7: Difference is separated from distance, error, and Boundary

Difference is provisionally typed as:

```text
Δ_{B,c,Σ} : X ⇀ D
```

where `D` may be:

```text
scalar
vector
ordered object
partial order
relation
distribution
field-like object
```

The paper preserves:

```text
Difference
≠
Distance
≠
Error
≠
Boundary
```

### Contribution 8: Comparison with existing mathematical fields

The paper compares the model with:

```text
relational structures
graphs and hypergraphs
order theory
topology
dynamical systems
transition systems and event structures
category theory
logic and proof theory
constraint propagation
probability and statistics
sheaf-like structures
process algebra
```

The comparison identifies which concepts each field can model and where premature reduction would lose Gyro-specific distinctions.

---

## 7. Proposed Research Questions

### RQ1

How can Structure, Slice, and Stability be minimally typed without redefining the invariant Core?

### RQ2

How can Slice be represented as a process that yields a local articulation without assuming a pre-existing result object?

### RQ3

How can Stability represent readable continuation while retaining unresolved local not-yet?

### RQ4

How can acquired readability alter later conditions without being reduced to stored history?

### RQ5

How can Trajectory be modeled as contextual tracing rather than a predefined state sequence?

### RQ6

Which existing mathematical fields provide useful partial models, and where do their assumptions become too restrictive?

---

## 8. Proposed Paper Structure

### 1. Introduction

- relation to the introductory Gyro Logic paper
- need for a formal model
- risk of premature reduction
- paper contributions

### 2. The Invariant Core and Formalization Constraints

- canonical Core
- canonical definitions
- distinction between definition and formal candidate
- formalization requirements

### 3. Structure as Establishability Without Fixed Mathematical Type

- Structure is not state, object, space, or relation alone
- current state and bearer distinctions
- not-yet and local establishability
- minimal commitments

### 4. Slice as Process and Local Articulation

- rejection of extraction and filtering models
- distinction between Slice process and articulation
- `S_n \xRightarrow{Σ_{B_n,c_n}} a_n`
- slice-ing and slice-done reconsideration

### 5. Stability as a Readable and Continuable Scene

- Stability is not evaluator
- not scalar-only
- not fixed-point-only
- structured scene
- residual local not-yet

### 6. Incorporated Readability and Context Update

- local establishment available to later reasoning
- `Γ_n`
- non-monotonic update possibilities
- distinction from memory and logs

### 7. Continuity Readability and Identity

- admissible relation
- traceability
- readability
- Identity separation

### 8. Contextual Trajectory

- local realizations
- trace-bearing relation field
- tracing operation
- readable Trajectory
- branching, merging, gaps, and reinterpretation

### 9. Difference and Boundary

- Difference as structured non-coincidence
- partial and heterogeneous codomain
- distinction from distance and error
- relation to Boundary

### 10. Minimal Formal Model

- integrated schema
- assumptions
- non-assumptions
- compact notation

### 11. Comparison with Existing Mathematical Fields

- comparison table
- useful partial models
- limits of reduction
- proposed heterogeneous composition

### 12. Illustrative Examples

Candidate examples:

```text
mathematical proof context
batter to cake transformation
photograph and video framing
search for absence and negation
authentication trajectory
vulnerability response trajectory
```

Examples should validate distinctions rather than serve as application specifications.

### 13. Discussion

- theoretical implications
- strengths
- limitations
- open mathematical questions

### 14. Conclusion

- minimal formal result
- Core unchanged
- future validation and specialization

---

## 9. Minimal Integrated Model to Present

The current candidate is:

```text
g_n = (S_n,B_n,c_n,Σ_n,a_n,K_n)
```

```text
S_n \xRightarrow{Σ_{B_n,c_n}} a_n
```

```text
K_n = StabScene(a_n ; S_n,B_n,c_n)
```

```text
q_n = Inc(g_n)
```

```text
Γ_{n+1} = Update_Γ(Γ_n,q_n)
```

```text
(S_n,Γ_{n+1},e_n) ↝ S_{n+1}
```

```text
CR(g_i,g_j)
⇔
∃r : Adm(r) ∧ Traceable(r) ∧ Readable(r)
```

```text
𝒢_R = (G,E)
```

```text
T = Trace(G,E)
```

```text
Δ_{B,c,Σ} : X ⇀ D
```

The paper must state clearly that this model is minimal in commitment, not minimal in symbol count.

---

## 10. Claims the Paper Must Not Make

The paper must not claim:

```text
Structure is a topological space.
Slice is universally a function or morphism.
Stability is an attractor or equilibrium.
Trajectory is a graph path.
Difference is a metric.
Incorporated Readability is identical to logical context Γ.
Gyro Logic has been reduced to one established mathematical field.
The formal model is complete or final.
```

It must also avoid implying:

```text
all Structure change is caused by Slice
all relations are readable
all readable continuity implies identity
all Stability requires zero Difference
all histories form a Trajectory
```

---

## 11. Validation Strategy

The first paper should use conceptual validation rather than numerical benchmarking.

Each example should test whether the model can preserve the following distinctions:

```text
Structure vs current state
Slice process vs local articulation
local articulation vs Stability
Stability vs score
readability context vs stored history
relation existence vs continuity readability
history vs Trajectory
Difference vs distance
Difference vs Boundary
continuity vs Identity
```

A later specialized paper may introduce executable or quantitative models.

---

## 12. Source Documents

Primary sources:

```text
docs/01_Core_Definitions.md
docs/37_Structure_Ontological_Type_Study_20260716.md
docs/38_Slice_Mathematical_Type_Study_20260716.md
docs/39_Slice_As_Provisional_Becoming_Study_20260716.md
docs/40_Slice_Provisional_Mathematical_Expression_20260716.md
docs/41_Stability_Mathematical_Type_Study_20260716.md
docs/43_Incorporated_Readability_As_Context_Extension_Study_20260717.md
docs/44_Continuity_Readability_Mathematical_Type_Study_20260717.md
docs/45_Trajectory_Mathematical_Type_Study_20260717.md
docs/46_Difference_Mathematical_Type_Study_20260717.md
docs/47_Minimal_Formal_Model_v1_20260717.md
docs/48_Mathematical_Field_Comparison_20260717.md
```

Supporting sources:

```text
docs/15_Boundary_20260610.md
docs/16_Boundary_State_20260610.md
docs/17–36 concept reconsideration studies
```

The existing Gyro Logic introductory preprint should be cited as the foundational framework paper.

---

## 13. Writing Sequence

The recommended writing order is:

```text
1. Contribution statement
2. Formalization constraints
3. Slice and Stability sections
4. Incorporated Readability and Trajectory sections
5. Integrated Minimal Formal Model
6. Comparison with existing mathematics
7. Examples
8. Introduction
9. Discussion and Conclusion
10. Abstract
```

This order avoids forcing the argument into an abstract before the formal distinctions have been stabilized.

---

## 14. Planned Paper Files

After the paper architecture is accepted, create:

```text
paper/minimal_formal_model_en.md
paper/minimal_formal_model_jp.md
```

The English and Japanese manuscripts should share the same section structure but should not be maintained as mechanically literal translations when a technical expression requires different clarification.

---

## 15. Current Decision

The work completed in `docs/37` through `docs/48` supports an independent new paper.

The recommended paper identity is:

```text
A Minimal Formal Model for Gyro Logic:
Local Articulation, Stability Scenes, and Contextual Tracing
```

The paper's defining contribution is not a final axiomatization.

It is the construction of a minimal formal organization that preserves Gyro Logic's distinctions while explicitly showing the limits of reduction to existing mathematical fields.
