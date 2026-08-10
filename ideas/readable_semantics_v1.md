# Readable Semantics v1

Date: 2026-08-10
Status: Revised idea draft / exploratory clarification
Target layer: Gyro Logic
Review state: INTERNAL_REFRAMING

## 1. Purpose

This document records the current understanding of `Readable` after external reviews and subsequent internal reconsideration.

It remains exploratory and non-canonical. It does not modify the invariant Core:

```text
Structure → Slice → Stability
```

The central correction in this revision is methodological:

> `Readable` should not currently be forced into a universal mathematical predicate with necessary and sufficient subconditions.

The earlier v0/v1 attempts became too focused on defining `Readable` itself. The original role of the word was more modest: to help explain when an unfolding Slice may be treated, from the Operator side, as one local establishment (`slice-done`) rather than as continuing `slice-ing`.

This note therefore returns to that simpler role and separates it from a different question that became mixed into the discussion: how later Operators can retrospectively establish that some earlier event or establishment probably occurred.

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

The word is therefore subordinate to the more important question:

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

These examples suggest that the event side can supply strong changes, but the unit called `done` depends on what the Operator is treating as the establishment at issue.

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

## 7. Retrospective establishment

The earthquake example suggests a useful distinction that should be studied without prematurely assigning it to an existing Gyro term.

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

The important statement is:

```text
present establishment about a past event
≠
the past event itself
```

The present Operator establishes something closer to:

> "there appears to have been such an establishment/event"

than:

> "I directly possess the original event."

This distinction prevents retrospective reasoning from being confused with direct observation.

---

## 8. Accumulation of local establishments

The earlier expression "Readable accumulates" should now be avoided because it assigns too much theoretical load to the word `Readable`.

A simpler description is:

> One local establishment may leave relations, consequences, traces, or constraints that participate in later Structure. Later local establishments may be formed from these. By following relations among multiple establishments, an Operator may retrospectively form another local establishment about an earlier event.

This allows accumulation and retrospection without assuming that:

- the original event has been stored in full;
- every past establishment remains permanently accessible;
- current reconstruction is identical to historical reality;
- `Readable` itself is a persistent substance or memory object.

---

## 9. Relation to Trajectory — intentionally not fixed yet

This retrospective structure appears related to existing Gyro discussions of Trajectory, continuity, and incorporated readability.

However, this note deliberately does **not** identify them.

At this stage the safer order is:

1. describe the phenomenon in ordinary language;
2. distinguish continuing event, local establishment, remaining traces/relations, and retrospective establishment;
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

> Slice unfolds as `slice-ing`. The underlying event or phenomenon may continue independently of where an Operator places a local boundary. Under the current Orientation and Context, the Operator may treat some range of the unfolding process as one local establishment; that is the role currently associated with `slice-done`. `Readable` is only a provisional explanatory word for the condition in which such a local establishment can be treated as established. The Operator need not have observed the original event directly: later relations and local establishments may support a retrospective present establishment that something of that kind probably occurred.

Japanese working reading:

> Sliceは `slice-ing` として進行する。事象・現象そのものは、Operatorがどこで区切るかとは独立に、その後も続き得る。Operatorは現在のOrientationやContextのもとで、その進行のある範囲を「ここまでを一つの局所的成立として扱ってよい」と区切ることができ、その位置づけが現在の `slice-done` の理解に近い。`Readable` は、現時点ではその「一つの成立として扱える状態」を説明するための暫定的な言葉に留める。またOperatorは元の事象をその場で直接観測している必要はなく、後に残った関係や複数の局所的成立を辿ることで、「過去にそのような事象・成立があったと考えられる」という現在の成立を作ることができる。

---

## 12. What is relatively safe to preserve

The following points currently appear useful enough to preserve as working guidance:

1. `Readable` is not a fourth Core element.
2. `Readable` should not currently be forced into a universal necessary-and-sufficient definition.
3. `slice-done` should not be confused with the objective end of an underlying event.
4. Local establishment is primarily an Operator-side unitization under Orientation and Context.
5. Event-side transitions may constrain a unit boundary without uniquely determining it.
6. The underlying event may continue after a local establishment has been treated as `done`.
7. Direct contemporaneous observation is not required for a later Operator to establish something about a past event.
8. Retrospective establishment is a present establishment supported by later traces/relations; it is not the past event itself.
9. Multiple local establishments and their relations may support retrospective reconstruction.
10. The relation to Trajectory, Incorporated Readability, and formal Readable semantics should remain open until this simpler distinction is tested further.

---

## 13. Open questions

The next questions should remain simple and example-driven:

1. Are there cases where an event side itself appears to force exactly one `done` boundary independent of Operator Orientation and Context?
2. What kinds of event-side changes strongly constrain where Operators tend to place local establishment boundaries?
3. When two Operators place different `done` boundaries over the same continuing event, what makes both admissible or one inadmissible?
4. What exactly remains after a local establishment such that later Operators can use it?
5. What distinguishes a reliable retrospective establishment from a merely possible story about the past?
6. How much can be lost while retrospective establishment remains possible?
7. Does retrospective establishment require a continuous relation chain, or can gaps be bridged?
8. When should this structure be identified with Trajectory, if ever?
9. Is `Readable` still the best explanatory word, or should the theory eventually use a different expression?

---

## 14. Review note

The previous external reviews from Gemini and Claude remain valuable records because they exposed the danger of over-formalizing the word `Readable` before its role had been conceptually stabilized.

The present revision does not reject those reviews. Instead, it changes the immediate research question from:

```text
What are the universal necessary and sufficient conditions of Readable?
```

to:

```text
How does an Operator treat part of a continuing Slice/event as one local establishment,
and how can later Operators form retrospective establishments from what remains?
```

Only after this simpler structure becomes stable should formal semantics be reconsidered.
