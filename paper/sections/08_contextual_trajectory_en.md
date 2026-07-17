# Contextual Trajectory

## From Local Continuity to Trajectory

The previous section distinguished relation existence, traceability, continuity readability, and Identity. A Trajectory requires these distinctions to be preserved across more than one local connection. It is not introduced as an additional Core element. It is a derivative relational construction through which multiple local Gyro realizations become readable as connected under a given Orientation, Context, Slice, and incorporated readability condition.

The central claim of this section is:

```text
Trajectory
≠
state sequence
≠
chronological log
≠
event collection
≠
relation-bearing field itself
```

A Trajectory is what becomes readable when admissible relations among local realizations are contextually traced.

## Local Gyro Realizations

Let a local Gyro realization be provisionally represented by:

\[
g_i=(S_i,B_i,c_i,\Sigma_i,a_i,K_i).
\]

This representation identifies the Structure involved in the realization, its Orientation and Context, the Slice process, the local articulation made available through Slice, and the corresponding Stability scene. It does not imply that each realization is ontologically independent or separated from every other realization. The index \(i\) provides only a provisional analytical reference.

Let the family of available local realizations be:

\[
G=\{g_i\}_{i\in I}.
\]

The family \(G\) is not itself a Trajectory. It is only a collection of local realizations that may or may not support one or more readable trajectories.

## The Relation-Bearing Trace Field

Let \(\mathcal{R}\) denote a family of possible relation types. A relation-bearing trace field may then be represented as:

\[
E\subseteq G\times\mathcal{R}\times G,
\]

and:

\[
\mathcal{G}_{R}=(G,E).
\]

An element \((g_i,r,g_j)\in E\) means that a relation of type \(r\) is available, retained, inferred, or otherwise representable between the two local realizations. The relation may be causal, material, functional, semantic, procedural, institutional, identity-related, Boundary-related, Difference-related, or readability-related. The model does not require one universal relation type.

The structure \(\mathcal{G}_{R}\) is not yet a Trajectory. It stores or supports possible traces. It may contain mutually incompatible relations, disconnected components, competing interpretations, dormant links, or relations that are unavailable under the current Context. The distinction is therefore:

```text
relation-bearing trace field
≠
readable Trajectory
```

## Contextual Tracing

A tracing operation is conditioned by Orientation \(B\), Context \(c\), a Trajectory-oriented Slice \(\Sigma_T\), and an incorporated readability context \(\Gamma_T\). A readable Trajectory is provisionally represented as:

\[
T_{B,c,\Sigma_T,\Gamma_T}
=
\operatorname{Trace}_{B,c,\Sigma_T,\Gamma_T}(G,E).
\]

The tracing operation does not simply enumerate all elements of \(G\) or all relations in \(E\). It selects, composes, suppresses, weights, and interprets admissible traces under the current conditions. A different Orientation, Context, Slice, or readability context may produce a different readable Trajectory from the same relation-bearing field.

Thus:

\[
\operatorname{Trace}_{B_1,c_1,\Sigma_1,\Gamma_1}(G,E)
\neq
\operatorname{Trace}_{B_2,c_2,\Sigma_2,\Gamma_2}(G,E)
\]

may hold without any change to the underlying set of local realizations or stored relations.

## Admissibility of a Trace

Let a candidate trace be:

\[
\pi=(g_{i_0},r_1,g_{i_1},r_2,\ldots,r_m,g_{i_m}).
\]

Its inclusion in a readable Trajectory requires more than formal adjacency. A weak admissibility condition may be written as:

\[
\operatorname{AdmTrace}(\pi;B,c,\Sigma_T,\Gamma_T).
\]

This condition may depend on:

- the admissibility of each relation type;
- compatibility among successive relations;
- current relevance weights;
- retained Difference patterns;
- Boundary conditions;
- available continuity criteria;
- missing or inaccessible intermediate realizations;
- contextual constraints on interpretation.

No assumption is made that admissibility is globally fixed, binary, monotonic, or independent of later Incorporated Readability.

## Trajectory Is Not a Predefined State Sequence

A state trajectory is often represented as:

\[
x_0,x_1,x_2,\ldots,x_n.
\]

Such a sequence presupposes that the states belong to a common state space and that the ordering relation is already available. Gyro Trajectory requires weaker assumptions. The connected realizations may differ in type, representation, granularity, or identity. Their continuity may depend on heterogeneous relations rather than one transition function.

Accordingly, a linear state sequence may instantiate a Gyro Trajectory in a restricted domain, but it is not the universal form of Trajectory.

## Trajectory Is Not a Log

A chronological log records that events were stored in an order. It does not by itself establish which relations among those events are admissible, traceable, or readable as continuity. A log may support a Trajectory reading, but the log is not identical to that reading.

Formally, if \(H\) is a stored event history, then:

\[
H\neq T_{B,c,\Sigma_T,\Gamma_T}.
\]

The same history may support multiple trajectories, no readable trajectory, or a later trajectory that was not available at the time of recording.

## Branching, Merging, and Multiple Trajectories

Because the relation-bearing field may support more than one admissible tracing, Trajectory is not required to be linear. The model permits:

- branching, where one local realization supports multiple continuations;
- merging, where multiple traces become readable as contributing to one later realization;
- parallel trajectories, where distinct tracings coexist;
- competing trajectories, where different interpretations remain mutually inconsistent;
- nested trajectories, where a local trace is read within a broader trace;
- partial trajectories, where only a fragment is currently readable.

The tracing result may therefore be graph-like, hypergraph-like, partially ordered, category-like, or event-structural in a particular implementation. The present theory does not fix one of these forms universally.

## Gaps and Unreadable Intervals

A missing intermediate realization does not automatically terminate a Trajectory. If an admissible relation can be traced across the gap, continuity may remain readable. Conversely, a densely recorded interval may fail to form a Trajectory if no admissible relation can be read.

This permits:

```text
record gap
≠
Trajectory break
```

and:

```text
dense history
≠
readable continuity
```

The treatment of a gap depends on the current Orientation, Context, Slice, and Incorporated Readability.

## Retrospective Tracing and Re-Slice

A later realization may introduce readability that was not previously available. Through Re-Slice, earlier realizations and retained relations may be traced differently. Thus a Trajectory may be retrospectively reconstructed or revised:

\[
T^{(n)}
=
\operatorname{Trace}_{B_n,c_n,\Sigma_n,\Gamma_n}(G,E),
\]

\[
T^{(n+1)}
=
\operatorname{Trace}_{B_{n+1},c_{n+1},\Sigma_{n+1},\Gamma_{n+1}}(G,E).
\]

The change from \(T^{(n)}\) to \(T^{(n+1)}\) need not mean that the past was altered. It means that the readable organization of retained traces changed under later conditions.

## Jump and Non-Continuous Reconstruction

Jump must not be defined merely as a large numerical discontinuity. In the present model, Jump concerns reconstruction when current continuity conditions cannot support an admissible continuation through the existing trace organization. A Jump may establish a new local relation field or new tracing conditions without erasing the prior field.

Accordingly:

```text
Jump
≠
large Difference only
```

and:

```text
Jump
≠
necessary deletion of prior Trajectory
```

A later Context may render relations across the Jump readable, or may preserve the Jump as a recognized discontinuity.

## Relation to Incorporated Readability

Incorporated Readability conditions which traces can be admitted, weighted, or interpreted. Let \(\Gamma_T\) represent the readability context used in tracing. Then changes in \(\Gamma_T\) may:

- expose a previously unreadable relation;
- invalidate a previously accepted relation;
- change the weight of competing traces;
- connect separated local realizations;
- split one readable Trajectory into several;
- merge several trajectories into a broader one.

Trajectory is therefore not independent of prior Gyro realizations, but neither is it reducible to their stored accumulation.

## Minimal Commitments

The contextual Trajectory model commits only to the following:

1. local Gyro realizations can be provisionally referenced;
2. heterogeneous relations among them can be represented;
3. relation existence is distinct from traceability and readability;
4. a tracing operation is conditioned by Orientation, Context, Slice, and Incorporated Readability;
5. the tracing result may be non-linear, partial, revisable, and plural;
6. Trajectory is derivative and does not replace the invariant Core.

It does not assume that all trajectories are linear, causal, complete, objectively unique, continuously differentiable, metrically embedded, or temporally indexed by one global clock.

## Transition to Difference and Boundary

Tracing depends on distinctions among local realizations and among possible relations. These distinctions may include differences in state, form, role, criterion, relevance, or continuity. However, Difference cannot be assumed to be a metric distance or error, and Boundary cannot be identified with Difference itself. The next section therefore develops Difference as a Slice-, Orientation-, and Context-relative structured relation of non-coincidence and examines how Boundary may arise as a derivative readable distinction.