# Related Work and Formal Positioning

## Relation to the Foundational Gyro Logic Paper

This paper is a formalization companion to the foundational Gyro Logic paper rather than a replacement for it. The earlier paper introduced the invariant Core and addressed the question of what Gyro Logic is [@kawakami2026gyro_logic_en]. The present paper addresses a narrower methodological question: how the distinctions currently developed around that Core can be organized into a provisional formal schema without changing the canonical definitions.

The distinction between the two papers is therefore:

```text
foundational paper
=
conceptual introduction and theoretical orientation
```

```text
present paper
=
minimal formal organization and comparison boundary
```

The present model should consequently be evaluated by whether it preserves the established distinctions and makes their assumptions inspectable, not by whether it replaces the broader theory with one closed mathematical system.

## Relational and Graph-Based Models

Relational structures and graph theory provide natural resources for representing heterogeneous local realizations and retained relations. Standard graph theory supplies explicit accounts of vertices, edges, paths, connectedness, branching, and graph transformations [@diestel2017graph]. These resources are directly useful for the relation-bearing trace field

\[
\mathcal{G}_R=(G,E).
\]

However, a represented graph normally presupposes that the relevant nodes and edges have already been individuated. The Gyro Logic distinction between a relation-bearing field and a readable Trajectory therefore remains additional: the graph stores candidate relations, whereas Trajectory is the result of contextual tracing under admissibility and readability conditions.

## Event Structures and Concurrency

Event structures were developed to represent occurrence, causal dependency, conflict, and concurrency without reducing a system to one interleaved sequence. The classical relation among Petri nets, event structures, and domains provides a rigorous account of how events and causal organization can support configuration-based semantics [@nielsen1981petri]. Later work further clarified correspondences among configuration structures, event structures, and Petri nets [@vanglabbeek2009configuration].

These approaches are especially relevant to branching, merging, conflict, partial order, and non-linear Trajectory. They nevertheless begin with formally represented events and enabling or conflict relations. Gyro Slice addresses an earlier or weaker commitment: the process through which a local articulation becomes available. Event structures are therefore strong candidates for domain-specific representations of realized Gyro processes, but they are not adopted as the universal ontology of Structure or Slice.

## Transition Systems, Model Checking, and Process Algebra

Transition systems and model checking provide precise techniques for state evolution, branching behavior, temporal properties, and verification once states, labels, and transition relations have been specified [@baier2008principles]. Process algebra similarly provides compositional languages for interaction, concurrency, synchronization, and continuation. Milner's Calculus of Communicating Systems is a foundational example [@milner1980ccs; @milner1982combinators].

These methods are relevant to Gyro Process, Gyro Loop, Operator Response, Re-Slice, Defer, and Jump. Their operational precision is valuable for GyroOS implementations. Their reduction risk is that a predefined transition or action vocabulary may be mistaken for the more general Structure through which an articulation becomes available. The present paper therefore treats process algebra and transition systems as implementation-level or domain-level formalizations, not as replacement definitions of the invariant Core.

## Dynamical Systems and Stability

Dynamical systems provide established models of trajectories, equilibria, attractors, oscillation, convergence, bifurcation, and perturbation [@strogatz2015nonlinear]. These models are useful when a state space and evolution law are justified, particularly for measurable GyroOS or GyroAuth behavior.

Gyro Stability is deliberately broader than dynamical stability. It concerns a locally readable and continuable establishment and may coexist with ongoing change and residual not-yet. Likewise, Gyro Trajectory is not universally identified with a time-indexed state solution. Dynamical systems are therefore important specializations, but equilibrium, convergence, or invariance cannot serve as universal definitions of Stability.

## Topology, Locality, and Sheaf-Like Structures

Topology provides formal accounts of neighborhoods, continuity, closure, separation, and boundaries [@munkres2000topology]. It is useful for representing local persistence and admissible variation around a local articulation. Sheaf theory provides a richer language for local information, restriction, compatibility, and the possible failure of local data to glue into one global object [@maclane1992sheaves].

These ideas correspond to the local character of Stability Scenes and to the distinction between local establishment and global non-closure. They may also support context-dependent readability across overlapping domains. Nevertheless, topology and sheaf theory require a specified underlying space, site, covering, or restriction structure. The present model does not assume that such structures are available before Slice in every domain.

## Category Theory and Composition

Category theory offers a general language for objects, morphisms, composition, identity, functors, and structure-preserving translation [@maclane1998categories]. It is a promising framework for composing domain-specific Gyro models and for relating different forms of continuity without requiring one homogeneous state type.

The principal caution is that an ordinary morphism has a specified domain and codomain. The general Slice relation does not assume that the local articulation is already available as a fully individuated codomain before the Slice process. Category theory may therefore provide a later compositional framework once suitable local objects and morphisms have been justified, but it is not imposed as the initial universal type of Structure or Slice.

## Belief Revision and Non-Monotonic Context Update

The AGM theory of belief revision formalizes rational contraction and revision of belief sets through explicit postulates [@alchourron1985logic]. It is directly relevant to the non-monotonic aspects of Incorporated Readability, particularly addition, revision, invalidation, and reweighting of what later reasoning can use.

Incorporated Readability is broader than belief revision. The readability context \(\Gamma\) need not be a deductively closed belief set, and incorporation may be material, procedural, perceptual, institutional, or operational rather than propositional. AGM-style revision is therefore a strong partial model for logical contexts, not a universal interpretation of incorporation.

## Probabilistic and Statistical Models

Probability and statistics can quantify uncertainty, confidence, evidence, and heterogeneous observations once an event model and measurable variables have been specified. Probabilistic graphical models provide one mature framework for structured dependency and inference under uncertainty [@koller2009probabilistic].

Such methods may instantiate graded Readability, Stability confidence, Difference distributions, or competing Trajectory hypotheses. They do not explain by themselves how the relevant variables, events, or distinctions become locally articulable. Probability is therefore treated as a domain-specific quantitative layer rather than as the general semantics of Gyro Logic.

## Position of the Present Model

The reviewed fields provide substantial formal resources, but each begins with commitments that are appropriate only after particular objects, relations, spaces, events, or operations have been specified. The Minimal Formal Model occupies a coordination role. It states which distinctions must remain visible when these mathematical resources are applied.

The position can be summarized as follows:

```text
Gyro Logic Minimal Formal Model
≠
a replacement for established mathematics
```

```text
Gyro Logic Minimal Formal Model
=
a formal boundary for selecting and coordinating partial models
```

The novelty claimed here is therefore not a new graph theory, topology, dynamics, probability theory, or process algebra. It is the explicit organization of Structure, Slice process, local articulation, Stability Scene, Incorporated Readability, Continuity Readability, contextual Trajectory, Difference, and Boundary so that domain-specific formalizations can be compared without silently collapsing these distinctions.