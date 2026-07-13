# Mathematical Object Candidate Table v0

## 1. Purpose

This document begins the mathematical formalization study of Gyro Logic after the Core Definition Refinement and Boundary Integration of v3.1.

The invariant Core remains unchanged:

```text
Structure
↓
Slice
↓
Stability
```

This document does not define a final mathematical model.

Its purpose is to identify the mathematical properties required by Gyro Logic, compare candidate mathematical objects, and record where each candidate may distort or lose the existing theory.

The primary theoretical reference is:

```text
docs/01_Core_Definitions.md
```

---

## 2. Formalization Policy

The order of work is:

```text
required properties
↓
mathematical object candidates
↓
candidate comparison
↓
minimal formal model
↓
examples
↓
failure cases
↓
possible definition
```

The following must not occur at this stage:

- selecting a mathematical field before identifying required properties;
- reducing Structure to a static set merely for convenience;
- reducing Slice to a completed function while ignoring slice-ing;
- reducing Stability to a scalar without preserving its status as an established and continuing state;
- promoting Trajectory, Difference, Boundary, or another derivative concept into the Core;
- changing the invariant order `Structure → Slice → Stability`.

---

## 3. Primary Candidate Table

| Gyro concept | Required properties | Mathematical candidates | Advantages | Problems / risks |
|---|---|---|---|---|
| **Structure** | Holds multiple possible establishments; does not determine one result before Slice; permits different Slices under different Contexts or Operator Orientations; may produce multiple Stability states; may change while retaining prior transformation and openness to another Slice | relational structure; state space; constrained possibility space; directed graph or hypergraph; topological space; manifold or stratified space; category-like object; sheaf-like local/global structure; independent Gyro object | Relational structures preserve heterogeneous relations; state spaces connect to implementation and dynamical systems; constrained possibility spaces represent establishability without requiring one outcome; graphs make paths and relations explicit; topology represents continuity and neighbourhood without requiring metric distance; category-like models express transformations and composition | A set or state space may appear too static; graphs may discretize relations prematurely; topology may not represent direction or Operator Orientation; manifolds assume smoothness that Jump or Void may violate; category theory may become too abstract and hide readable state content; possibility spaces may remain descriptive rather than operational |
| **Slice** | Is a process, not only a result; opens a path through Structure toward an establishment; distinguishes slice-ing from slice-done; may localize a target while expanding readable relations; depends on Orientation and Context; may reveal, generate, or stabilize Difference and Boundary; may be redirected, repeated, interrupted, or re-sliced | parameterized process; partial map; relation; morphism; path-generation operator; observation operator; restriction or projection; conditional transformation; transition system; process-algebra term; functor-like transformation; independent Gyro process object | A parameterized process can include Orientation and Context; partial maps represent unreadable or undefined regions; relations permit one-to-many outcomes; morphisms and composition connect repeated Slices; transition systems represent intermediate states; process algebra distinguishes ongoing process from completed result | A total function falsely implies one determined output; projection suggests mere reduction; observation operators may make Slice purely epistemic; morphisms may identify process only by endpoints; transition systems may confuse runtime implementation with theory; process algebra may overemphasize operational sequencing; path-generation models require a prior definition of path and space |
| **Stability** | Is the state in which an opened path becomes readable as an establishment that can continue; is not Stop, Success, or an evaluator; may coexist with change; may have local, relational, temporal, or multidimensional form; must support Stable / Critical / Unstable readings without being exhausted by those labels; may relate to but not be identical with a scalar score | state predicate; region or subset of admissible continuing states; local stability condition; invariant or approximately invariant property; viability condition; fixed-point neighbourhood; attractor or metastable region; Lyapunov-like quantity plus state condition; probability distribution or confidence representation; vector-valued or structured state quantity | Predicates preserve the distinction between a state and its numerical evaluation; viability captures continuation; regions allow non-binary and local readings; invariants represent continuity under change; attractor and metastability models connect to dynamical systems; structured quantities can retain multiple stability dimensions | A scalar alone loses the readable establishment; a fixed point wrongly suggests immobility; an attractor may impose asymptotic convergence not required by Gyro Logic; probabilities may confuse uncertainty with Stability; invariants may be too strict for evolving Structure; viability requires a defined future-transition model; labels may become decisions rather than descriptions |
| **Difference / Δ** | Represents a readable difference under a Slice; may compare expected and actual results, successive states, Orientation and establishment, Boundary-relative positions, or Trajectory deviation; may be directional, asymmetric, Context-dependent, partially defined, or non-scalar; need not satisfy metric axioms | metric or pseudometric; divergence; directed distance or quasi-metric; residual; error vector; discrepancy relation; signed or ordered difference; context-indexed family of differences; path-dependent functional; distribution-valued difference; independent Gyro Difference object | Metrics provide interpretable scale; pseudometrics allow distinct states with zero readable difference; divergences and quasi-metrics allow asymmetry; residuals connect expectations to results; vectors preserve direction; context-indexed measures express Slice relativity; path-dependent functionals connect Δ to Trajectory | A metric may falsely require symmetry and triangle inequality; one scalar may erase the kind and direction of Difference; residual notation may privilege an expected target; path dependence may make local evaluation difficult; Context indexing can make comparison across Slices non-canonical; zero Δ must not automatically imply identity or absolute equality |
| **Trajectory** | Is not a Core element; temporally reads repeated or continuing Core realizations; retains history and prior transformation; may be non-Markovian; may contain local Stability, redirection, Re-Slice, Defer, Stop, and Jump; may be continuous, discrete, hybrid, or partially unreadable | state sequence; path in a state or possibility space; composable morphism sequence; labelled transition trace; history-dependent stochastic process; non-Markov process; hybrid trajectory; càdlàg-like path with jumps; event structure; path in a graph or category | Sequences are minimal and implementation-friendly; paths support continuity; morphism composition represents successive transformations; traces preserve response labels; non-Markov processes retain history; hybrid paths handle continuous and discrete changes; jump paths represent discontinuity | A state sequence may treat each Structure as independent; continuous paths may exclude Jump; Markov models lose memory; stochastic models introduce probability unnecessarily; morphism sequences may omit internal slice-ing; event structures may not represent Stability as a state; a single global time parameter may not fit all Slices |

---

## 4. Candidate Families by Concept

### 4.1 Structure

The current leading interpretation is not a single mathematical type but a family of compatible readings:

```text
Structure
≈ relational possibility-bearing object
  + constraints
  + current readable state
  + retained transformation
```

This suggests that a bare set is insufficient unless additional relations, constraints, and admissible transformations are supplied.

A tentative generic notation is:

```text
𝒮 = (X, R, C, A)
```

where, provisionally:

- `X` is a carrier of possible elements or states;
- `R` is a family of relations;
- `C` is a family of constraints or conditions;
- `A` is a family of admissible establishments or transitions.

This is not yet a definition.

The notation only records the minimum suspicion that Structure must carry more than membership.

### 4.2 Slice

A Slice likely requires explicit dependence on Orientation and Context.

A tentative schema is:

```text
Σ_{o,c} : 𝒮 ⇝ P
```

where:

- `𝒮` is a Structure;
- `o` is Operator Orientation;
- `c` is Context;
- `P` is an opened path or process toward establishment;
- `⇝` deliberately does not yet mean an ordinary total function.

The notation must preserve:

```text
slice-ing ≠ slice-done
```

A completed Slice result may later be written separately, for example:

```text
D_{o,c}(𝒮)
```

but `D` must not replace the Slice process itself.

### 4.3 Stability

The primary definition must remain visible in any formalization:

```text
Stability is the state in which an opened path becomes readable
as an establishment that can continue.
```

A minimal candidate therefore separates:

```text
Stability state
```

from:

```text
Stability evaluation or score
```

Tentatively:

```text
Stab(P, 𝒮, c) ∈ 𝒦
```

where `𝒦` may be a structured space of continuing-establishment conditions rather than only a real interval.

A scalar such as:

```text
s = exp(-Δ)
```

may be an evaluation derived from part of `𝒦`, not necessarily Stability itself.

### 4.4 Difference / Δ

A single global metric is not assumed.

A safer initial form is a Context- and Slice-relative discrepancy:

```text
Δ_{o,c,Σ}(x, y)
```

The codomain is left open:

```text
Δ_{o,c,Σ}(x, y) ∈ D
```

where `D` may be scalar, vector, ordered, relational, distributional, or partially defined.

This permits later testing of whether a metric, pseudometric, divergence, quasi-metric, or independent Difference structure is appropriate.

### 4.5 Trajectory

Trajectory is provisionally represented as an indexed family of Core realizations:

```text
T = ((𝒮_n, Σ_n, K_n, R_n))_{n∈I}
```

where:

- `𝒮_n` is the current Structure section;
- `Σ_n` is the Slice process;
- `K_n` is the Stability state;
- `R_n` is an Operator Response or continuation relation;
- `I` may be discrete, continuous, hybrid, partially ordered, or event-indexed.

This notation does not add Trajectory to the Core.

It records repeated or continuing readings of:

```text
Structure → Slice → Stability
```

---

## 5. Preliminary Comparison

### Candidate most compatible with Structure

Current strongest family:

```text
relational constrained possibility-bearing object
```

Reason:

- a bare set does not express establishability;
- a conventional state space may imply already-determined states;
- relations and constraints are required before choosing topology, metric, graph, manifold, or category.

### Candidate most compatible with Slice

Current strongest family:

```text
Orientation- and Context-parameterized partial process
```

Reason:

- Slice is ongoing before it is complete;
- outcomes may be one-to-many or unreadable;
- the process may reveal, generate, or stabilize relations rather than merely project existing coordinates.

### Candidate most compatible with Stability

Current strongest family:

```text
structured continuing-establishment condition
```

Reason:

- Stability is a state, not only a score;
- continuation may depend on several dimensions;
- scalar, categorical, or probabilistic evaluations may be derived views.

### Candidate most compatible with Difference / Δ

Current strongest family:

```text
Slice-relative directed discrepancy
```

Reason:

- symmetry is not guaranteed;
- Context and Orientation may change what Difference is readable;
- a metric is one possible special case, not the starting assumption.

### Candidate most compatible with Trajectory

Current strongest family:

```text
history-bearing indexed composition of Core realizations
```

Reason:

- Trajectory is not one state;
- prior transformation may affect later Structure and Slice;
- discontinuity and Jump must remain representable.

---

## 6. Concepts Not Yet Promoted to Primary Rows

The external review also raised:

- Observer Slice;
- Conflict / Friction;
- Stability Landscape.

These are not yet treated as independent Core-level mathematical objects.

Initial positioning:

```text
Observer Slice
= possible specialization of Orientation- and Context-parameterized Slice

Conflict / Friction
= possible relation among constraints, paths, Differences, or competing establishments

Stability Landscape
= possible structured representation of Stability conditions across a domain of possible Slice results
```

They should be tested after the primary five concepts are minimally formalized.

---

## 7. Immediate Failure Warnings

The following reductions would lose essential Gyro Logic meaning:

| Reduction | Lost meaning |
|---|---|
| `Structure = set` | establishability, relations, constraints, retained transformation |
| `Slice = total function` | slice-ing, partial readability, interruption, one-to-many paths |
| `Slice = projection` | generation or stabilization of readable relations |
| `Stability = scalar` | Stability as an established continuing state |
| `Stability = fixed point` | continuation with change and local or metastable establishment |
| `Δ = metric` | direction, asymmetry, Context dependence, partial readability |
| `Trajectory = Markov state sequence` | retained history, prior transformation, path dependence |
| `Trajectory = continuous curve` | Jump, Defer, discontinuity, event-indexed change |

---

## 8. Non-Decisions

This document does not yet decide:

- whether Structure is fundamentally a state space, relational structure, graph, category, topology, or independent object;
- whether Slice is fundamentally a map, relation, morphism, process, or path generator;
- whether Stability has a canonical scalar representation;
- whether Δ satisfies any distance axioms;
- whether Trajectory uses discrete time, continuous time, event order, or a hybrid index;
- whether Observer Slice, Conflict / Friction, or Stability Landscape requires an independent definition;
- what the first Minimal Formal Model v0 should adopt.

---

## 9. Next Research Step

The next step is to test three competing minimal model families:

```text
Model Family A
Relational state-space model

Model Family B
Process / transition model

Model Family C
Category- or path-composition model
```

Each model should be evaluated against the same examples and failure cases before any formal definition is adopted.

---

## 10. Core and Layer Consistency

### Core

```text
Structure
↓
Slice
↓
Stability
```

No Core change is proposed.

### Layer

```text
Gyro Logic
↓
GyroOS
↓
GyroAuth
```

This document belongs only to Gyro Logic.

No implementation requirement is imposed on GyroOS, and no authentication requirement is allowed to redefine the theory.
