# Where Does the Local Establishment Boundary Come From?

Date: 2026-08-10
Status: Exploratory / non-canonical
Target layer: Gyro Logic

## 1. Purpose

This note studies a narrower question that emerged from the discussion of `slice-done` and fixed criteria:

> Where does the boundary of a local establishment come from?

The goal is not to define `Readable`, not to add a new Core element, and not to decide that every boundary is either subjective or objectively fixed.

The invariant Core remains:

```text
Structure → Slice → Stability
```

The immediate hypothesis is that different local establishment boundaries may have different origins.

---

## 2. Starting point

The current working distinction is:

```text
continuing event / process
≠
local establishment boundary
```

The underlying event or process may continue.

A local `done` is a unitization of some range of that continuation.

However, it is too simple to say:

```text
"the Operator freely chooses the boundary"
```

because in many cases the boundary is inherited from rules, protocols, institutions, prior decisions, physical changes, or previously established relations.

Therefore the question should shift from:

> Is the boundary free or fixed?

to:

> From what prior or current relations does this boundary arise?

---

## 3. Candidate sources of a boundary

At this stage, at least four distinct sources appear useful to separate.

### A. Immediate local unitization

The current Operator places a boundary under the current Orientation and Context.

Example:

```text
continuous log stream
↓
Operator treats this range as "one session"
```

The boundary is not arbitrary, but it is not necessarily inherited from an explicit external rule.

It may be motivated by:

- a change in behavior;
- a temporal gap;
- a task boundary;
- an observed transition;
- a local comparison need.

This is the most direct Operator-side case.

---

### B. Inherited protocol boundary

A current Operator may not decide the boundary from scratch.

Example:

```text
protocol specification
↓
"checksum covers bytes X..Y"
↓
current execution
↓
checksum evaluation
```

The current Operator applies a boundary that was already established in the protocol specification.

In this case:

```text
current boundary
← inherited from prior establishment
```

The current evaluation may be deterministic even though the boundary itself has a history.

This separates:

```text
fixed within current evaluation
```

from:

```text
intrinsic and timeless boundary of the underlying event
```

They are not the same claim.

---

### C. Inherited institutional boundary

A boundary may be supplied by a legal, medical, administrative, scientific, or organizational framework.

Example:

```text
medical/legal framework
↓
criteria + measurement procedure + time window
↓
current death determination
```

The individual clinician may have little or no freedom to redefine the local unit.

Nevertheless, the boundary used in the current determination is still related to a previously established institutional structure.

Thus:

```text
institutionally fixed now
```

may mean:

```text
stabilized by prior collective establishments
```

rather than:

```text
revealed as the one intrinsic end point of all biological change
```

This distinction should remain open to verification rather than assumed universally.

---

### D. Event-side strongly suggested boundary

Some boundaries are strongly suggested by changes in the event itself.

Examples:

- first fracture;
- threshold crossing;
- loss of function;
- protocol signal arrival;
- irreversible transition;
- phase change.

These may strongly pull multiple Operators toward similar local unitizations.

But even here, the strong event-side change may function as:

```text
boundary candidate / constraint
```

rather than automatically proving:

```text
one universal and Operator-independent `done`
```

This remains an empirical and conceptual question for each case.

---

## 4. A useful distinction: boundary source vs boundary application

The current discussion becomes clearer if two questions are separated.

### Question 1 — Boundary source

```text
Where did this local unit boundary come from?
```

Possible answers:

- current Operator judgment;
- prior protocol;
- institutional rule;
- inherited convention;
- earlier empirical model;
- strong event-side transition;
- combination of several of these.

### Question 2 — Boundary application

```text
Once that boundary is in use, how is the current local establishment evaluated?
```

This may involve a fixed criterion.

For example:

```text
selected checksum range
↓
fixed checksum algorithm
↓
match / mismatch
```

The application may be fully deterministic even when the boundary source is historical or inherited.

---

## 5. Checksum example revisited

Suppose a protocol defines:

```text
payload bytes 0..N
↓
CRC-32
↓
compare against transmitted checksum
```

At runtime, there may be essentially no discretion.

The current calculation can be fixed and repeatable.

However, two different questions remain:

```text
Q1. Is the checksum result correct under this specification?
Q2. Why is this byte range / algorithm / completion unit the one being used?
```

Q1 may be deterministic.

Q2 points backward to the protocol specification and its design history.

The protocol itself may have been created through earlier local establishments:

```text
requirements
↓
engineering decisions
↓
protocol design
↓
specification
↓
implementation
↓
current fixed evaluation
```

Therefore the current fixed criterion may be understood as a stabilized inheritance from earlier establishments.

This does **not** mean that the current checksum result is subjective.

It means only that:

```text
fixed local evaluation
≠
boundary without origin
```

---

## 6. Death determination revisited

A current medical or legal determination may use a tightly fixed procedure.

For example, a framework may specify:

- which functions are evaluated;
- what observations count;
- how long measurements are taken;
- what exclusions apply;
- which criterion constitutes the declaration.

At the current evaluation point, the clinician may be constrained to follow that rule.

But the biological process remains broader:

```text
circulation
brain function
cellular metabolism
organ viability
decomposition
...
```

The present declaration is therefore a local establishment under a previously stabilized medical/legal boundary system.

The important distinction is:

```text
"this rule fixes the current declaration"
```

versus:

```text
"all biological change has one intrinsic and universal completion point"
```

The first may be true locally without proving the second.

---

## 7. This is not a regress answer yet

A natural objection is:

> If the current boundary comes from an earlier rule, where did that earlier rule come from?

This note does not solve that question by simply pushing the answer backward forever.

Instead, it records the structure that appears to be present:

```text
current establishment
↑
inherited rule / boundary
↑
earlier establishment
↑
earlier relations / criteria / decisions
↑
...
```

This may be an infinite regress problem.

But it may also be the wrong way to frame the phenomenon.

Gyro Logic already studies continuity, local establishment, and repeated Slice / Stability cycles.

Therefore a historical chain of prior establishments may not be an anomaly to eliminate. It may be part of the normal structure being studied.

The key question is not necessarily:

```text
Where is the absolutely first boundary?
```

but rather:

```text
What prior establishments and relations currently constrain this boundary,
and how far can those relations be traced or revised?
```

This remains exploratory.

---

## 8. Boundary inheritance and later verification

A boundary inherited from an earlier rule can later be re-examined.

Example:

```text
protocol v1 boundary
↓
years of use
↓
new failure case discovered
↓
protocol review
↓
revised boundary in v2
```

The old runtime evaluations do not become mathematically different retroactively.

Instead:

```text
old evaluation under rule R1
```

may later be judged differently from the standpoint of:

```text
new establishment under rule R2
```

Likewise, an earlier medical or legal criterion may later be revised without implying that past clinicians failed to apply the then-current rule correctly.

This separates:

```text
correct application of a local criterion
```

from:

```text
later evaluation of whether that criterion or boundary was adequate
```

This distinction is central to retrospection and verification.

---

## 9. A simpler current picture

The current picture can be written as:

```text
continuing event / process
        ↓
current or inherited boundary source
        ↓
local establishment unit
        ↓
criterion / evaluation may be fixed locally
        ↓
local `done`
        ↓
later relations / consequences remain
        ↓
re-Slice / verification / revision may occur
```

The boundary may therefore be:

```text
currently chosen
inherited
institutionally stabilized
event-constrained
or mixed
```

without requiring all cases to share one universal source.

---

## 10. What should not yet be claimed

This note does not claim that:

1. every boundary is subjective;
2. every boundary is arbitrary;
3. every fixed rule is merely an illusion;
4. every formal criterion can later change its result;
5. every boundary ultimately reduces to one individual Operator choice;
6. every historical chain must have a recoverable first origin;
7. protocol, institution, convention, and event-side transition are already one formal category.

These distinctions should remain visible.

---

## 11. Current strongest working statement

A simple current formulation is:

> A local establishment boundary does not always originate in an immediate choice by the current Operator. It may be inherited from earlier protocols, institutional rules, conventions, prior models, or strongly constraining event-side changes. A boundary may therefore be locally fixed while still having a history. Once inherited or established, the boundary can support deterministic local evaluation; later Operators may nevertheless trace, verify, or revise the establishment or the rule from which the boundary was inherited.

Japanese working reading:

> local establishment の boundary は、現在の Operator がその場で自由に決めるものとは限らない。過去に成立した protocol、制度、慣習、モデル、あるいは事象側の強い変化から継承されることもある。そのため、現在の局所的な評価では boundary が固定されていても、その boundary 自体には成立の履歴があり得る。現在の criterion による判定は固定的に行えても、後の Operator は、その成立や boundary の由来を遡って検証し、必要であれば別の局所的成立として見直すことができる。

---

## 12. Open questions

The next questions are intentionally limited.

1. When does a current Operator actually create a new boundary, rather than inherit one?
2. How can an inherited boundary be distinguished from an event-side boundary that many Operators independently adopt?
3. When a protocol or institution fixes both the unit and the criterion, should they be treated analytically as two layers or as one stabilized establishment package?
4. What exactly is preserved when a boundary is inherited across Operators or generations?
5. How far can the history of a boundary be traced before the available relations become insufficient?
6. What makes a later revision a revision of the same establishment rather than a new establishment about the old one?
7. Is boundary inheritance already explainable by existing Gyro concepts such as Structure, Slice, Stability, Trajectory, or Incorporated Readability, without adding a new term?

---

## 13. Current conclusion

The useful distinction is no longer:

```text
free boundary
vs
fixed boundary
```

but:

```text
Where did this boundary come from?
```

A locally fixed boundary can still be historically derived.

A current Operator may inherit a boundary rather than invent it.

A deterministic criterion can therefore coexist with an Operator-relative or historically accumulated establishment structure.

This appears to connect the `done` discussion to the earlier questions of accumulated establishments, retrospection, and verification without requiring a new formal concept yet.
