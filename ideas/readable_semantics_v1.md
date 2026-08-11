# Readable Semantics v1

Date: 2026-08-11
Status: Revised idea draft / exploratory clarification
Target layer: Gyro Logic
Review state: REVISION_REQUIRED / POST-ROUND-3-DISPOSITION

## 1. Purpose

This document records the current understanding of `Readable` after external reviews, internal reconsideration, and the first explicit review-disposition cycle.

It remains exploratory and non-canonical. It does not modify the invariant Core:

```text
Structure → Slice → Stability
```

The central methodological correction remains:

> `Readable` should not currently be forced into a universal mathematical predicate with necessary and sufficient subconditions.

The earlier attempts became too focused on defining `Readable` itself. Its original role was more modest: to help explain when an unfolding Slice may be treated, from the Operator side, as one local establishment (`slice-done`) rather than as continuing `slice-ing`.

The current note therefore keeps two questions separate:

1. how an Operator treats part of a continuing Slice/event as one local establishment;
2. how a later Operator may form a present establishment about an earlier event from what remains.

The second question is treated here only as a phenomenon to investigate. It is not yet introduced as an independent Gyro Logic construct.

---

## 2. Core distinction: continuing event versus local establishment

A physical, informational, computational, or relational event does not necessarily stop when an Operator treats some part of it as `done`.

For example:

```text
falling glass
→ floor contact
→ cracking
→ fragmentation
→ vibration
→ fragments settling
→ temperature change
→ later deterioration
→ ...
```

The event sequence continues.

The expression:

```text
"the glass broke"
```

is not the whole continuing event. It is a local establishment made by treating some portion of the continuing change as one meaningful unit.

Therefore the present working distinction is:

```text
continuing event / phenomenon
≠
local establishment made from part of that continuation
```

This distinction is essential for interpreting `slice-ing` and `slice-done`.

---

## 3. `slice-done` is primarily an Operator-side unitization

The current working understanding is:

```text
slice-ing
```

refers to the unfolding Slice process.

```text
slice-done
```

marks the point at which the Operator, under the current Orientation and Context, treats some range of that unfolding process as one local establishment.

In plain language:

> "up to here, this may be treated as one locally established result."

This does not mean that the underlying event itself has objectively or absolutely ended.

Thus:

```text
slice-done
≠
end of the underlying event
```

and:

```text
slice-done
≠
global completion of Structure
```

The event side may contain strong transitions, boundaries, interruptions, irreversible changes, or apparent endings. These may strongly constrain or motivate where an Operator places a local unit boundary, but they do not by themselves prove that there is one unique natural `done` point independent of all Orientation and Context.

### 3.1 Minimal anti-post-hoc discipline

Operator-relativity must not be used as an unrestricted after-the-fact escape hatch.

The current minimal methodological rule is:

> Orientation and Context may participate in boundary placement, but they should not be introduced or redescribed only after a boundary has been chosen in order to justify that boundary.

When two boundary placements are compared, the relevant Orientation and Context should be stated independently enough that the comparison can expose disagreement rather than absorb every disagreement by redefining the frame.

This is deliberately weaker than a universal admissibility criterion. It is only a discipline against post-hoc rescue.

---

## 4. Current modest use of `Readable`

At this stage, `Readable` should be understood only as a provisional explanatory word.

A simple working reading is:

> During Slice, some unfolding material eventually reaches a state in which the Operator can treat a certain range as one local establishment. `Readable` is currently used as a convenient word for that "can now be treated as one establishment" condition.

This is not yet a formal definition.

It should not currently be expanded into a universal conjunction such as:

```text
PresentTo ∧ LocallyDiscriminable ∧ ...
```

unless later study demonstrates that such decomposition is genuinely useful and non-circular.

### 4.1 Relation between `Readable` and `slice-done`

This note does **not** currently claim a demonstrated operational distinction between `Readable` and `slice-done`.

The working relationship is intentionally modest:

```text
Readable
```

is explanatory language for the condition under which the Operator can treat a local Slice result as established, while:

```text
slice-done
```

names the resulting local Slice status / unitization in the current process description.

No worked example is currently known in this note where one clearly holds and the other clearly fails.

Therefore the difference is presently terminological and role-based rather than a separately validated semantic distinction.

The word `Readable` remains subordinate to the more important question:

> Where and why does an Operator treat continuing `slice-ing` as one `slice-done` unit?

---

## 5. Why the event side alone is insufficient

Many examples appear at first to contain a natural event-side completion:

- a glass breaks;
- a ball lands;
- a person dies;
- a chemical reaction completes;
- a file transfer completes;
- a light bulb fails.

However, closer inspection shows that each description already contains an Operator-side choice of what counts as the relevant establishment.

For example:

### Glass breaking

Possible candidate boundaries include:

- first crack;
- structural fracture;
- separation into fragments;
- fragments becoming stationary.

The physical process continues beyond each candidate.

### Ball landing

Possible candidate boundaries include:

- first contact;
- first rebound;
- completion of bouncing;
- final rest.

### File transfer

Possible candidate boundaries include:

- final byte sent;
- final byte received;
- acknowledgement received;
- checksum verified;
- buffer flushed;
- file closed.

These examples suggest that the event side can supply strong changes, while the unit called `done` still depends on what is being treated as the establishment at issue.

A fixed local criterion may make one boundary determinate inside a chosen protocol, rule set, or evaluation frame. That does not by itself establish one universal completion point for the larger continuing event.

---

## 6. Observation is not limited to being present at the event

A second issue had become mixed with the `Readable` discussion: whether an Operator must directly observe an event while it occurs in order to establish something about it.

The current answer is no.

An Operator does not need to be present at the original event if later Structure contains relations, traces, consequences, or other local establishments from which the earlier occurrence can be reconstructed or inferred.

Example:

```text
past earthquake
↓
fault displacement
↓
sediment deformation
↓
tsunami deposits
↓
later geological structure
↓
present investigation
```

A present-day Operator does not observe the past earthquake itself.

Instead, the Operator obtains present local establishments such as:

```text
fault relation
sediment relation
dating result
deposit pattern
...
```

and, by relating them, may establish:

> "an earthquake of this kind probably occurred in the past."

This is a present local establishment about a past event, not a direct replay or complete recovery of the past event itself.

---

## 7. Retrospective establishment — phenomenon under investigation

The earthquake example suggests a useful phenomenon that should be studied without prematurely assigning it to an existing Gyro term or promoting it to a new formal construct.

```text
past event
↓
changes later relations / Structure
↓
those effects participate in later establishments
↓
present Operator slices currently available relations
↓
multiple local establishments are obtained
↓
relations among them are followed backward
↓
a present establishment about the past is formed
```

The important distinction is:

```text
present establishment about a past event
≠
the past event itself
```

The present Operator establishes something closer to:

> "there appears to have been such an establishment/event"

than:

> "I directly possess the original event."

At present, `retrospective establishment` is only a working descriptive label for this pattern.

It is **not yet claimed** to be:

- an independent Gyro Logic primitive;
- a new Core element;
- a formally distinct mechanism from Re-Slice, Context-relative revision, Trajectory, or other already-existing structures.

A central open test remains:

> What distinguishes a well-supported present establishment about the past from a merely plausible story?

No universal criterion is proposed here yet.

---

## 8. Accumulation of local establishments

The earlier expression "Readable accumulates" should now be avoided because it assigns too much theoretical load to the word `Readable`.

A simpler description is:

> One local establishment may leave relations, consequences, traces, or constraints that participate in later Structure. Later local establishments may be formed from these. By following relations among multiple establishments, an Operator may form another present local establishment about an earlier event.

This allows accumulation and retrospection without assuming that:

- the original event has been stored in full;
- every past establishment remains permanently accessible;
- current reconstruction is identical to historical reality;
- `Readable` itself is a persistent substance or memory object.

---

## 9. Relation to Trajectory — intentionally not fixed yet

This retrospective pattern appears related to existing Gyro discussions of Trajectory, continuity, and incorporated readability.

However, this note deliberately does **not** identify them.

At this stage the safer order is:

1. describe the phenomenon in ordinary language;
2. distinguish continuing event, local establishment, remaining traces/relations, and present establishment about the past;
3. test concrete examples;
4. only then decide whether an existing Gyro term already covers the relation.

Therefore:

```text
retrospective establishment
?= Trajectory
```

remains open.

---

## 10. Working picture

The current conceptual picture is:

```text
Event / phenomenon side
────────────────────────────────────────→
change continues whether or not it is currently observed

Operator side
       [ local establishment A ]
                 [ local establishment B ]
                           [ local establishment C ]

Later Operator
A/B/C and remaining relations
             ↓
      retrospective Slice
             ↓
"an earlier event / establishment probably occurred"
```

This picture is analytical only. It does not replace the Core.

---

## 11. Current strongest plain-language understanding

At present, the following wording is intentionally preferred over a mathematical definition:

> Slice unfolds as `slice-ing`. The underlying event or phenomenon may continue independently of where an Operator places a local boundary. Under the current Orientation and Context, the Operator may treat some range of the unfolding process as one local establishment; that is the role currently associated with `slice-done`. Orientation and Context should not be redescribed only after the fact to rescue an arbitrary boundary. `Readable` is only a provisional explanatory word for the condition in which such a local establishment can be treated as established, and no independent operational distinction from `slice-done` is currently claimed. The Operator need not have observed the original event directly: later relations and local establishments may support a present establishment that something of that kind probably occurred, but this retrospective pattern is not yet treated as an independent Gyro Logic construct.

Japanese working reading:

> Sliceは `slice-ing` として進行する。事象・現象そのものは、Operatorがどこで区切るかとは独立に、その後も続き得る。Operatorは現在のOrientationやContextのもとで、その進行のある範囲を「ここまでを一つの局所的成立として扱ってよい」と区切ることができ、その位置づけが現在の `slice-done` の理解に近い。ただしOrientationやContextは、境界を置いた後にその境界を正当化するためだけに後付けで書き換えるべきではない。`Readable` は現時点ではその「一つの成立として扱える状態」を説明するための暫定的な言葉に留め、`slice-done` との独立したoperationalな差はまだ主張しない。またOperatorは元の事象をその場で直接観測している必要はなく、後に残った関係や複数の局所的成立を辿ることで、「過去にそのような事象・成立があったと考えられる」という現在の成立を作ることができる。ただし、この遡及的なパターンはまだ独立したGyro Logic概念とはしない。

---

## 12. What is relatively safe to preserve

The following points currently appear useful enough to preserve as working guidance:

1. `Readable` is not a fourth Core element.
2. `Readable` should not currently be forced into a universal necessary-and-sufficient definition.
3. `slice-done` should not be confused with the objective end of an underlying event.
4. Local establishment is primarily an Operator-side unitization under Orientation and Context.
5. Operator-relativity does not license post-hoc redefinition of Orientation / Context solely to rescue a boundary judgment.
6. Event-side transitions may constrain a unit boundary without necessarily determining one universal boundary.
7. The underlying event may continue after a local establishment has been treated as `done`.
8. No independently validated operational distinction between `Readable` and `slice-done` is currently claimed.
9. Direct contemporaneous observation is not required for a later Operator to establish something about a past event.
10. A present establishment about a past event is not the past event itself.
11. `retrospective establishment` is currently a working description of a phenomenon, not a new formal Gyro Logic construct.
12. The relation to Trajectory, Incorporated Readability, formal Readable semantics, and existing event/process theories should remain open until separately verified.

---

## 13. Open questions

The next questions should remain simple and example-driven:

1. Are there cases where an event side itself appears to force exactly one `done` boundary independent of Operator Orientation and Context?
2. What kinds of event-side changes strongly constrain where Operators tend to place local establishment boundaries?
3. When two Operators place different `done` boundaries over the same continuing event, what minimal non-post-hoc discipline allows them to be compared?
4. Can a stronger admissibility criterion be stated without returning immediately to circular necessary-and-sufficient definitions?
5. What exactly remains after a local establishment such that later Operators can use it?
6. What distinguishes a well-supported present establishment about the past from a merely possible story?
7. How much can be lost while such retrospective establishment remains possible?
8. Does retrospective reasoning require a continuous relation chain, or can gaps be bridged?
9. When should this structure be identified with Trajectory, if ever?
10. Is `Readable` still useful as explanatory language, or should it eventually be removed or replaced?
11. Does existing work on event boundedness, telicity, aspect, process theory, or related frameworks already cover part or all of the continuing-event / local-establishment distinction?

---

## 14. Review disposition and revision note

The previous external reviews remain valuable records because they exposed the danger of over-formalizing `Readable` before its role had been conceptually stabilized.

The current revision follows the explicit disposition record:

```text
reviews/readable_semantics_v1_claude_round3_disposition_20260811.md
```

The Round 3 findings were not adopted wholesale. They were classified before revision, including checks for repetition of already-known concerns.

The present revision therefore makes only the changes judged appropriate now:

- adds a minimal anti-post-hoc discipline for Orientation / Context;
- states plainly that no independent operational distinction between `Readable` and `slice-done` is currently demonstrated;
- keeps retrospective establishment as a phenomenon under investigation rather than promoting it to a new formal construct;
- preserves literature comparison and stronger admissibility semantics as verification / future-work tasks rather than importing them prematurely.

The immediate research question remains:

```text
How does an Operator treat part of a continuing Slice/event as one local establishment,
and what can later Operators establish from what remains?
```

Only after this simpler structure becomes more stable should formal semantics be reconsidered.
