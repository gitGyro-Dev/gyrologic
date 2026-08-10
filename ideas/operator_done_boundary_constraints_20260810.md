# Operator-Side `done` Boundary Constraints

Date: 2026-08-10
Status: Exploratory / non-canonical
Target layer: Gyro Logic

## 1. Purpose

This note studies a narrower question that emerged from the current `Readable` reframing:

> What constrains an Operator when it treats part of a continuing event or Slice as one local `done` establishment?

The goal is not to define `Readable` and not to modify the invariant Core:

```text
Structure → Slice → Stability
```

The current working baseline is:

- events / phenomena may continue independently of where an Operator places a local boundary;
- `slice-done` is primarily an Operator-side unitization under Orientation and Context;
- however, the Operator is not assumed to be free to place a boundary arbitrarily anywhere;
- event-side changes may strongly constrain plausible boundary placement.

The immediate test is whether apparently strong event-side endings uniquely determine `done`, or instead provide strong candidate regions that remain Operator-relative.

---

## 2. Working distinction

The present working picture is:

```text
Event side
────────────────────────────────────→
continuous / ongoing change

Operator side
        [ local establishment ]
                ↑
         `done` boundary
```

The Operator-side boundary is not assumed to create the event-side change.

Likewise, the event-side change is not yet assumed to determine one unique Operator-side boundary.

A safer working statement is:

> Event-side changes may constrain where a local establishment can reasonably be placed, while Orientation and Context determine which constrained boundary is relevant to the current Slice.

This statement is provisional and must survive examples.

---

## 3. Case 1 — A glass falls and breaks

A simplified event sequence is:

```text
fall
→ impact
→ first crack
→ structural fracture
→ fragmentation
→ fragment motion
→ settling
→ later physical change
→ ...
```

At first glance, `the glass broke` appears to have a natural event-side completion.

But several candidate boundaries remain available:

- first irreversible crack;
- loss of structural integrity;
- fragmentation into separate pieces;
- end of fragment motion.

These are not equally useful under every Orientation.

Examples:

- a materials researcher may care about crack initiation;
- a safety controller may care about structural integrity loss;
- an insurance report may care about functional destruction;
- a cleanup task may care about fragments becoming stationary.

### Observation G1

The event side supplies strong irreversible transitions.

However, the expression `the glass broke` still depends on which relation counts as the establishment at issue.

Candidate conclusion:

```text
strong event-side transition
⇏ unique `done` boundary
```

Instead:

```text
strong event-side transition
⇒ constrained boundary candidates
```

is more plausible.

---

## 4. Case 2 — A person dies

This is a deliberately strong case because `death` appears more naturally final than many ordinary transitions.

Possible event-side markers include:

- cessation of heartbeat;
- cessation of circulation;
- irreversible loss of whole-brain function;
- irreversible loss of brainstem function;
- irreversible cellular failure;
- legal declaration of death.

The underlying biological processes do not all stop at one instant.

After one criterion is satisfied:

- cellular processes continue;
- chemical reactions continue;
- decomposition begins;
- organ viability may differ by tissue;
- legal and medical consequences continue.

### Observation D1

Even in a case with strong practical and legal boundary conventions, the event side does not obviously provide one universally privileged physical instant that satisfies every Orientation.

The boundary is highly constrained, but its admissible placement depends on what is being established:

```text
medical death
legal death
organ viability loss
cellular death
```

### Important caution

This does **not** imply that an Operator may freely declare death at any arbitrary point.

The available boundary candidates are strongly restricted by biological, medical, legal, and operational relations.

This case therefore suggests the useful distinction:

```text
Operator-relative
≠ arbitrary
```

---

## 5. Case 3 — Phase transition

Consider water freezing.

A naive description is:

```text
liquid
→ freezing point
→ solid
```

But real systems may contain:

- supercooling;
- nucleation;
- coexistence of phases;
- latent heat release;
- spatially nonuniform freezing;
- delayed equilibrium.

Possible `done` boundaries include:

- first nucleation event;
- first macroscopic solid region;
- majority solidification;
- complete macroscopic solidification;
- thermal equilibrium after solidification.

### Observation P1

A phase transition can provide a strong event-side structural change, but the exact `done` boundary still depends on what the Operator is establishing.

A microscopic Orientation and a macroscopic operational Orientation may legitimately place different local boundaries.

Again:

```text
salient physical transition
⇏ unique universal local establishment boundary
```

---

## 6. Case 4 — File transfer completes

This case appears more discrete and protocol-defined than physical examples.

Possible event sequence:

```text
last byte sent
→ last byte received
→ transport acknowledgement
→ checksum verification
→ buffer flush
→ file close
→ application-level acceptance
```

One might think the protocol itself determines a unique `done`.

But the protocol contains multiple layers, each with its own completion condition.

Examples:

```text
network-layer done
transport-layer done
storage-layer done
application-layer done
user-visible done
```

### Observation F1

This is an important case because the candidate boundaries are not merely subjective interpretations.

They are explicitly encoded by different Operators / mechanisms / protocol layers.

Therefore `done` can be strongly rule-constrained without being globally unique.

This supports:

```text
local rule-determined `done`
≠ global event completion
```

and:

```text
multiple constrained `done` boundaries
```

can coexist over one continuing computational process.

---

## 7. Case 5 — Hardware failure

Consider a light bulb or hardware component `failing`.

Possible candidate transitions include:

- material defect begins;
- electrical parameter exceeds tolerance;
- output drops below specification;
- protection circuit trips;
- component ceases operation;
- monitoring system raises failure state;
- operator declares replacement required.

The physical degradation may begin long before operational failure is declared.

Likewise, after the failure state is declared, physical changes continue.

### Observation H1

`failure` is usually not a single event-side primitive.

It is a relation between the changing system and a criterion of acceptable continuation or function.

This case makes the Operator / Orientation contribution particularly explicit.

The hardware side constrains the possible judgment through measurable change, but the `failed` establishment depends on which functional or operational criterion is active.

---

## 8. Comparison across the five cases

The examples differ strongly:

```text
glass breaking     — physical irreversible transition
death              — biological / medical / legal boundary
phase transition   — physical state change
file transfer      — protocol-defined computational completion
hardware failure   — functional / operational threshold
```

Yet a common structure appears.

### Common pattern

1. The event side contains changes that are not invented by the Operator.
2. Some changes are much more salient or constraining than others.
3. These changes reduce the plausible region in which a local `done` can be placed.
4. Orientation and Context determine which event-side relation matters for the current establishment.
5. Different Operators can therefore place different boundaries without every boundary being equally admissible.
6. The underlying event or process may continue after any one local `done` establishment.

This suggests a distinction between:

```text
boundary freedom
```

and:

```text
boundary admissibility
```

The Operator has some freedom of unitization, but not unlimited freedom.

---

## 9. First candidate constraints on Operator-side boundary placement

These are not definitions or axioms. They are only candidate constraint families suggested by the examples.

### C1. Event-side support

A `done` boundary should correspond to some identifiable change, relation, threshold crossing, transition, loss, gain, or structural difference in the event/process being sliced.

This prevents a purely arbitrary boundary with no relation to the event-side Structure.

### C2. Orientation relevance

The event-side change used as a boundary must be relevant to what the current Orientation is trying to establish.

Example:

```text
last byte sent
```

may be relevant to a sender-side transfer question but insufficient for an application-level completion question.

### C3. Context compatibility

The boundary must remain interpretable under the current Context.

A criterion that is valid under one protocol, medical definition, sensor mode, or operating regime may not transfer unchanged to another.

### C4. Local coherence

The boundary should allow the resulting unit to be treated coherently as the establishment at issue.

This does not require global truth or total closure.

It only excludes boundaries that destroy the very distinction the Slice is attempting to establish.

### C5. Non-arbitrariness under comparison

If two boundary placements are compared under the same Orientation and Context, there should be a reason grounded in event-side relations for preferring, allowing, or rejecting each one.

This is a minimal defense against the claim:

```text
"any Operator boundary is equally valid"
```

The current study explicitly rejects that unrestricted reading.

---

## 10. Stronger provisional statement

A more precise plain-language statement now appears possible:

> `slice-done` is primarily an Operator-side unitization, but it is not an arbitrary one. The Operator places a local boundary under Orientation and Context by using event-side changes, relations, thresholds, or structural differences as constraints. Event-side structure can strongly restrict plausible boundaries without necessarily determining one unique global `done` point.

This is stronger than the earlier statement:

> the Operator simply decides where to stop.

The latter is too permissive.

The current interpretation is instead:

```text
continuing event
+
event-side constraints
+
Operator Orientation / Context
↓
constrained local unitization
↓
`slice-done`
```

This is an explanatory sketch only; it does not replace the Core.

---

## 11. What this says about apparent natural `done`

The five cases suggest that what appears to be a natural event-side `done` may usually be one of the following:

- an irreversible change;
- a sharp transition;
- a threshold crossing;
- a protocol marker;
- a loss of function;
- a conventionally privileged relation;
- a strongly salient boundary candidate.

These can make one boundary overwhelmingly natural for a given Orientation and Context.

But the current examples do not yet establish:

```text
there exists one Operator-independent universal `done`
```

for the underlying continuing event.

The safer hypothesis is:

> Some event-side changes are so constraining that many Operators converge on nearby `done` boundaries, but convergence of boundary placement should not yet be confused with proof of one intrinsic universal event boundary.

---

## 12. Relation to `Readable`

This study does not attempt to define `Readable`.

However, it clarifies the role that the word was trying to explain.

Instead of asking:

```text
What universal predicate makes a result Readable?
```

we can now ask:

```text
What constrains an Operator to treat this range of slice-ing
as one local establishment rather than another?
```

`Readable` may remain only a provisional explanatory word for the condition in which this constrained local establishment can be treated as established.

No additional formal semantics are introduced here.

---

## 13. New pressure tests

The next examples should target the current provisional statement rather than `Readable` itself.

### PT1. Boundary with no sharp event-side change

Can a valid `slice-done` occur when the event side changes only gradually, with no identifiable threshold or discontinuity?

If yes, `event-side support` must be broader than sharp transitions.

### PT2. Multiple equally supported boundaries

Can two different boundaries be equally supported by the same event-side relations under the same Orientation and Context?

If yes, admissibility may be non-unique even after Orientation and Context are fixed.

### PT3. Retrospective boundary placement

Can a later Operator place a better-supported `done` boundary than the Operator present during the original event?

This directly connects to retrospective establishment without assuming they are the same concept.

### PT4. False but locally coherent boundary

Can an Operator place a boundary that is coherent under Orientation and Context but later evidence shows that the underlying event-side interpretation was wrong?

If yes:

```text
admissible local unitization
```

must remain separate from:

```text
truth / correctness
```

### PT5. Forced local boundary

Can we construct a case where, under fixed Orientation and Context, every admissible Operator must place the boundary at the same event-side transition?

This is the strongest test for whether event-side structure can sometimes determine a unique local `done` even if it does not determine a universal event boundary.

---

## 14. Current conclusion

The examples do not support either extreme:

```text
Event side alone uniquely determines every `done`.
```

or:

```text
Operator may place `done` anywhere it wants.
```

The current middle position is:

> The event/process continues, but contains changes and relations that constrain possible local unit boundaries. The Operator, under Orientation and Context, uses those constraints to treat some range as one local establishment. Different boundaries may be admissible for different establishments, while arbitrary boundaries remain rejectable.

This is the current best plain-language understanding and should remain non-canonical until the pressure tests above are worked through.
