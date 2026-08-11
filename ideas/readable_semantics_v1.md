# Readable Semantics v1

Date: 2026-08-11
Status: Revised idea draft / focused clarification
Target layer: Gyro Logic
Review state: REVISION_REQUIRED / POST-CLAUDE-FINAL-GATE-DISPOSITION

## 1. Purpose

This document records the current focused understanding of `Readable` and its relation to `slice-done`.

It remains exploratory and non-canonical. It does not modify the invariant Core:

```text
Structure → Slice → Stability
```

The current methodological position is:

> `Readable` should not currently be forced into a universal mathematical predicate with necessary and sufficient subconditions.

Earlier attempts became too focused on decomposing `Readable` itself. Its original role was more modest: to help explain when an unfolding Slice may be treated, from the Operator side, as one local establishment (`slice-done`) rather than as continuing `slice-ing`.

This revision therefore narrows the document to that problem only.

The separate question of how later Operators may form present establishments about earlier events has been moved to:

```text
ideas/retrospective_establishment_v0.md
```

so that the two topics can be reviewed independently.

---

## 2. Version relation to v0

`ideas/readable_semantics_v0.md` is preserved as historical review material.

Its earlier candidate decomposition:

```text
Available
∧ Articulated
∧ SelectivelyAddressable
```

and the related P-R proposition set are **not active formal semantics in v1**.

They are not deleted from the repository because they remain useful records of the path that led to the current reframing.

The current status is:

```text
v0 formal decomposition
→ superseded as the active working model
→ preserved for review history and possible future re-examination
```

No claim is made that every individual distinction explored in v0 is permanently false or unusable. The point is only that v1 does not currently rely on that conjunction or proposition set as its formal basis.

---

## 3. Core distinction: continuing event versus local establishment

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

## 4. `slice-done` as Operator-side unitization

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

The event side may contain strong transitions, boundaries, interruptions, irreversible changes, inherited protocol markers, or institutional criteria. These may strongly constrain or determine a local boundary within a chosen frame, but they do not by themselves establish one universal completion point for the larger continuing event.

For related exploration of where local boundaries come from, see:

```text
ideas/operator_done_boundary_constraints_20260810.md
ideas/fixed_criterion_vs_done_boundary_checksum_death_20260810.md
ideas/local_establishment_boundary_origin_20260810.md
```

---

## 5. Minimal anti-post-hoc discipline

Operator-relativity must not be used as an unrestricted after-the-fact escape hatch.

The current minimal methodological rule is:

> Orientation and Context may participate in boundary placement, but they should not be introduced or redescribed only after a boundary has been chosen in order to justify that boundary.

When two boundary placements are compared, the relevant Orientation and Context should be stated independently enough that disagreement can remain visible rather than being absorbed automatically by redefining the frame.

This is deliberately weaker than a universal admissibility criterion.

It is a methodological discipline against post-hoc rescue, not yet a complete operational theory of admissible boundaries.

### 5.1 Pressure test for the discipline

Consider a continuous log stream:

```text
E1 E2 E3 E4 E5 E6 E7 E8 ...
```

An Operator first places a session boundary after `E5`.

Only after that choice, the Operator states:

> "My Orientation was always to define a session as E1–E5."

If no independent record, prior rule, protocol, declared goal, or previously stated Context supports that claim, then the boundary has not been independently justified; the Orientation/Context description merely restates the chosen result.

By contrast, if a prior protocol already states:

```text
session ends after event class X
```

and `E5` is the first matching `X`, then the boundary may be locally fixed by an inherited rule. The relevant issue is no longer arbitrary post-hoc justification, but the source and application of that rule.

This test does not solve all admissibility questions. It only demonstrates the type of circular rescue the current discipline is intended to block.

---

## 6. Current modest use of `Readable`

At this stage, `Readable` is retained only as provisional explanatory language.

A simple working reading is:

> During Slice, some unfolding material reaches a state in which the Operator can treat a certain range as one local establishment. `Readable` is currently a convenient way of describing that "can now be treated as one establishment" condition.

This is not a formal definition.

It should not currently be expanded into a universal conjunction such as:

```text
PresentTo ∧ LocallyDiscriminable ∧ ...
```

unless later study demonstrates that such decomposition is genuinely useful and non-circular.

### 6.1 Relation between `Readable` and `slice-done`

No independently validated operational distinction between `Readable` and `slice-done` is currently claimed.

For the present document:

```text
Readable
```

should be understood as an explanatory paraphrase for the condition associated with treating a Slice result as locally established, while:

```text
slice-done
```

remains the process term used for that local Slice status / unitization.

No worked example is currently known in this study where one clearly holds and the other clearly fails.

Therefore, until such a divergence is demonstrated, `Readable` should **not** be treated as an additional semantic layer or independent theoretical object.

The practical priority is:

```text
slice-ing
↓
Operator-side local unitization
↓
slice-done
```

`Readable` is secondary explanatory wording around this transition.

---

## 7. Why the event side alone is insufficient

Many examples appear at first to contain a natural event-side completion:

- a glass breaks;
- a ball lands;
- a person dies;
- a chemical reaction completes;
- a file transfer completes;
- a light bulb fails.

Closer inspection shows that each description already specifies, explicitly or implicitly, what establishment is at issue.

### Glass breaking

Possible candidate boundaries include:

- first crack;
- structural fracture;
- separation into fragments;
- fragments becoming stationary.

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

These examples suggest that event-side change can strongly constrain a local boundary while the larger process continues.

A fixed local criterion may make one boundary determinate inside a protocol, rule set, legal framework, medical procedure, or other chosen frame. That does not by itself establish one universal `done` point for the entire continuing event.

---

## 8. Current strongest plain-language understanding

At present, the following wording is intentionally preferred over a mathematical definition:

> Slice unfolds as `slice-ing`. The underlying event or phenomenon may continue independently of where a local boundary is placed. Under the current Orientation and Context, an Operator may treat some range of that unfolding process as one local establishment; this is the role currently associated with `slice-done`. The boundary may be influenced or locally fixed by event-side changes, inherited protocols, rules, or institutional criteria. Orientation and Context should not be redescribed only after the fact merely to rescue a chosen boundary. `Readable` is retained only as provisional explanatory wording for the condition associated with treating the local Slice result as established; no independent operational distinction from `slice-done` is currently claimed.

Japanese working reading:

> Sliceは `slice-ing` として進行する。事象・現象そのものは、局所的な境界がどこに置かれるかとは独立に、その後も続き得る。Operatorは現在のOrientationやContextのもとで、その進行のある範囲を「ここまでを一つの局所的成立として扱ってよい」と区切ることができ、この位置づけが現在の `slice-done` の理解に近い。境界は、事象側の変化だけでなく、継承されたprotocol、rule、制度的criterionなどによって局所的に強く拘束・固定される場合もある。ただしOrientationやContextを、選んだ境界を正当化するためだけに後付けで書き換えることはしない。`Readable` は現時点では、このlocal Slice resultを成立として扱える状態を説明するための暫定的な言い換えに留め、`slice-done` とは別の独立したoperational概念としては扱わない。

---

## 9. What is relatively safe to preserve

The following points currently appear useful enough to preserve as working guidance:

1. `Readable` is not a fourth Core element.
2. `Readable` is not currently an independent operational concept from `slice-done`.
3. The v0 necessary/sufficient-condition model is superseded as the active working model, while retained as historical review material.
4. `slice-done` should not be confused with the objective end of an underlying event.
5. Local establishment is primarily an Operator-side unitization under Orientation and Context.
6. Operator-side does not mean arbitrary: boundaries may be strongly constrained or locally fixed by event-side change, inherited rules, protocols, or institutional criteria.
7. Operator-relativity does not license post-hoc redefinition of Orientation / Context solely to rescue a boundary judgment.
8. The underlying event may continue after a local establishment has been treated as `done`.
9. Fixed local evaluation does not by itself imply one universal completion point for the larger continuing event.
10. Formal Readable semantics and stronger boundary admissibility semantics remain open.

---

## 10. Open questions

The next questions should remain focused and example-driven:

1. Are there cases where the event side itself appears to force exactly one `done` boundary independent of Operator Orientation and Context?
2. What kinds of event-side changes strongly constrain where local establishment boundaries are placed?
3. How should boundaries inherited from protocol, institution, or prior establishment be represented relative to boundaries introduced in the current Slice?
4. When two boundary placements differ, what minimal comparison discipline is possible without returning immediately to circular necessary-and-sufficient definitions?
5. Can the anti-post-hoc discipline be made operationally checkable in a domain-neutral way, or only through domain-specific evidence such as prior rules, logs, timestamps, or declared criteria?
6. Is `Readable` still useful as explanatory language, or should the term eventually be removed entirely from this line of analysis?
7. Does existing work on event boundedness, telicity, aspect, process theory, or related frameworks already cover part or all of the continuing-event / local-establishment distinction?

Questions about later reconstruction of past events are now maintained separately in:

```text
ideas/retrospective_establishment_v0.md
```

---

## 11. Review disposition and revision note

This revision follows:

```text
reviews/readable_semantics_v1_claude_final_gate_disposition_20260811.md
```

The final-gate criticisms were classified before revision rather than adopted wholesale.

This revision therefore:

- makes the v0 → v1 supersession status explicit;
- narrows `Readable` to an explanatory paraphrase around `slice-done` rather than preserving an unsupported independent semantic object;
- adds a concrete pressure test for the anti-post-hoc discipline;
- links boundary-origin companion notes rather than silently treating all boundaries as immediate Operator choices;
- removes retrospective-establishment material from this document and places it in a focused reviewable note;
- keeps stronger admissibility semantics and literature comparison as open verification tasks.

The immediate research question is now intentionally narrow:

```text
How does an unfolding Slice become locally unitized as slice-done,
and what constrains or supplies that local boundary?
```

Only after this question becomes more stable should independent formal semantics for `Readable` be reconsidered.
