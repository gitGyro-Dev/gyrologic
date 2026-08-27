# Structural Analysis and Open Questions

## 0. Position

This document analyzes discrepancies found by the 2026-08-27 intuition reverse review.

It is deliberately **non-canonical**.

The invariant Core remains:

```text
Structure
↓
Slice
↓
Stability
```

The main finding is that the recovered intuitions do not currently require a Core replacement. They instead expose insufficient distinctions in auxiliary concepts around:

```text
readability
reachability
limit-reaching
transition
evaluation scope
response
```

---

# 1. Void — structural discrepancy

## 1.1 Existing theory

The current Gyro Logic documents already preserve several important points:

```text
Void != absolute nothing
Void is Slice-relative
Void is Operator-relative
Void may change under Orientation / Re-Slice
```

Thus the recovered intuition does **not** overturn the existing Void concept.

The stronger mismatch lies elsewhere.

The current formulation mainly classifies a region by present inferability / readability:

```text
readable / inferable
vs
non-readable / non-inferable
```

The recovered intuition additionally distinguishes **how unreachable** a currently unreadable region is.

This introduces a new axis:

```text
current readability
!=
accessibility / reachability under allowed transformations
```

## 1.2 Proposed distinction

Let:

```text
Readable(V ; Σ, B, c)
```

mean whether a region is readable under the current Slice conditions.

Separately, define a provisional reachability relation:

```text
Reach(V ; A)
```

where `A` is a family of admissible changes such as:

```text
Orientation change
Re-Slice
granularity change
instrument change
Context extension
Structure transformation
```

Then two regions can both be Void now while differing structurally:

```text
V1: unreadable now, reachable under small admissible changes
V2: unreadable now, unreachable unless the access mode or Structure changes substantially
```

This captures the shallow / deep Void intuition without treating depth as an intrinsic metaphysical property of Void.

## 1.3 Important caution

Do not define:

```text
VoidDepth = fixed property of region
```

because the recovered intuition itself says depth depends on Operator, method, time, place, and mode of access.

A safer formulation is:

```text
Void accessibility is relational.
```

Candidate notation:

```text
A_V(V ; B, c, M)
```

where `M` is the currently available family of transformations or access modes.

## 1.4 Snap recognition

The optical-illusion intuition does not imply that no processing occurs before recognition.

It suggests instead:

```text
continuous or extended slice-ing
can terminate in
discrete readability at slice-done
```

This is already compatible with the Core Definition's distinction:

```text
slice-ing != slice-done
```

Therefore snap recognition likely needs **no new Core state**.

It may instead be modeled as a discontinuity in readability:

```text
Readable_t = false
Readable_{t+ε} = true
```

without assuming a 50% established intermediate state.

---

# 2. Collapse — structural discrepancy

## 2.1 Problem with the current word

`Collapse` implies at least one of the following:

```text
destruction
loss of internal organization
failure of the current Structure
forced breakdown
```

The recovered intuition asserts none of these as necessary.

The intended phenomenon is:

```text
the currently active mode can no longer open materially further progress
within its present range
```

The mode may remain internally coherent.

## 2.2 Candidate terms

### A. Impasse

Strength:
- close to `cannot advance further`.

Weakness:
- sounds situational and may imply blockage by an obstacle.

### B. Limit Reaching

Strength:
- neutral and accurate.

Weakness:
- too generic; does not indicate that the usable range has been consumed.

### C. Exhaustion

Strength:
- captures `available possibilities under this mode have been used up`.

Weakness:
- can sound like resource depletion or fatigue.

### D. Saturation

Strength:
- captures reaching a regime where further input / continuation within the same mode yields little or no additional effective progress.
- is neutral rather than destructive.
- fits the gear / RPM analogy well.

Weakness:
- in mathematics and engineering, saturation often carries specific quantitative meanings.

### E. Current-Mode Saturation

Recommended working term.

```text
Current-Mode Saturation
= a condition in which the currently active mode of Slice has reached the effective range within which it can produce further usable establishment without changing that mode.
```

Japanese working label:

```text
現行モード飽和
```

or more explanatory:

```text
現在の切り取り方の到達限界
```

This term is not canonical yet.

## 2.3 Why saturation must be independent of Jump

The recovered intuition requires four possibilities:

```text
saturation + Jump
saturation + no Jump
no saturation + Jump
no saturation + no Jump
```

Therefore:

```text
Saturation
!=
Jump trigger by definition
```

and:

```text
Jump
!=
mandatory response to Saturation
```

Saturation should be treated as a readable condition of the current mode, while Jump is a transition relation / response event.

---

# 3. Jump — structural discrepancy

## 3.1 Existing weakness

When Jump is tied tightly to threshold excess or collapse, three distinct questions become conflated:

```text
Why did the transition become available?
How did the transition occur?
What kind of relation was established at the landing?
```

## 3.2 Proposed separation

Use three layers provisionally:

```text
Jump Condition
Jump Transition
Jump Landing
```

### Jump Condition

Any condition under which a discontinuous transition becomes available or selected.

Possible examples:

```text
Current-Mode Saturation
new relation becomes readable
external cue
Operator Response
unexpected Difference
Re-Slice result
```

No single trigger is mandatory.

### Jump Transition

The discontinuous change itself.

```text
J : q^- ↝ q^+
```

The minimal concept of Jump should live here.

### Jump Landing

The relation established after the Jump.

Candidate landing classes:

```text
Identity Landing
Relational Landing
Orientation Landing
Structure Landing
Boundary Landing
```

These are examples only, not a final taxonomy.

## 3.3 Constrained landing

The recovered auxiliary-line intuition suggests:

```text
Jump destination is neither arbitrary creation nor simple retrieval.
```

A useful provisional idea is a **landing admissibility set**:

```text
L_n = admissible / reachable landing relations given prior Structure, incorporated readability, Context, and Orientation
```

Then:

```text
Jump_n lands in some l ∈ L_n
```

without requiring deterministic selection.

This is compatible with the current minimal formal model because `ρ_n` already represents incorporated readability and later Structure / Orientation may depend on it.

Thus Jump landing constraints may be modeled using existing retained conditions rather than adding a new Core element.

---

# 4. Guard, ROLLBACK, and widening the observation scope

## 4.1 Existing GyroAuth meaning must be preserved

In GyroAuth:

```text
ROLLBACK
= restore a verified prior criterion state
```

This is a legitimate application-layer recovery operation.

It should **not** be renamed merely because another intuition was mistakenly grouped with it.

The proper correction is conceptual separation.

## 4.2 New candidate concept

The recovered intuition refers to changing the **evaluation scope**, not the criterion itself.

Candidate working name:

```text
Evaluation Scope Expansion
```

Japanese:

```text
評価範囲拡張
```

Alternative names:

```text
Observation Scope Expansion
Review Scope Expansion
Evidence Aperture Expansion
Evaluation Aperture
```

Recommended plain term:

```text
Evaluation Scope Expansion
```

because it naturally includes both:

```text
higher detail / resolution for the current case
broader comparison window across related prior cases
```

## 4.3 Formal separation

Let:

```text
E_t
```

be the current evidence / observation scope.

Then scope expansion is:

```text
E_t ⊂ E'_t
```

or more generally:

```text
E'_t = Expand(E_t ; angle, time, resolution, comparison set, context)
```

while keeping the evaluation criterion `q` unchanged:

```text
q' = q
```

This expresses the VAR analogy correctly:

```text
same criterion
+
more / differently resolved evidence
```

not:

```text
weaker criterion
```

## 4.4 Evaluation and judgment

The intuition also strongly supports:

```text
Evaluation
!=
Decision / Response
```

This distinction already exists partly in GyroAuth, where authentication decisions and criterion-update responses are separated.

At the general theory level, the safer formulation is:

```text
expanded Slice / evidence
→ richer readable evaluation
→ Stability or other establishment
→ Operator Response
```

Do not make scope expansion itself a final judgment.

## 4.5 Guard import policy

`Guard` should remain application-layer unless a domain-independent theoretical necessity is demonstrated.

The general theory may need concepts such as:

```text
admissibility
constraint
protected relation
non-compensable condition
```

but these should not be called `Guard` solely because GyroAuth uses that implementation term.

---

# 5. Clutch-disengagement state

## 5.1 Why it is not Void

Void concerns unreadability / non-inferability relative to current Slice conditions.

The clutch intuition instead says:

```text
internal process remains active
but the existing output coupling is temporarily disengaged
```

The system may know what is happening internally.

Therefore unreadability is not essential.

## 5.2 Why it is not Jump

Jump is the discontinuous transition.

The clutch state occurs **between couplings** or while the old coupling is disengaged and no new effective coupling has yet been established.

Thus:

```text
disengagement state
!=
transition event
```

## 5.3 Why it is not Stop

Processing need not stop.

```text
internal continuation = true
external/effective coupling = false or suspended
```

## 5.4 Candidate abstraction

Working concept:

```text
Decoupled Continuation
```

Japanese:

```text
非結合継続状態
```

or:

```text
結合解除中継続
```

Provisional definition:

```text
Decoupled Continuation is a state in which internal transformation or slice-ing continues while the currently effective coupling to an established output, relation, or continuation path is suspended, and no replacement coupling has yet become established.
```

Candidate notation:

```text
DC(q) : ActiveInternal(q) ∧ ¬CoupledCurrent(q) ∧ ¬EstablishedNewCoupling(q)
```

## 5.5 Where it may belong

This is probably **not a new Core element**.

It may be:

```text
a transitional state inside slice-ing
```

or:

```text
a relation between Operator Response and the next Slice / Structure coupling
```

The correct placement is still open.

## 5.6 Key test

Ask whether the state can occur before a completed Stability is established.

If yes, it is likely an internal Slice / transition-state concept.

If it only occurs after one Stability while selecting the next coupling, it may belong to Operator Response / inter-realization transition instead.

This distinction should be tested with multiple examples before naming it canonically.

---

# 6. Impact on the Minimal Formal Model

## 6.1 Structure

### Required change

No canonical definition change currently required.

### Possible refinement

Structure may need to expose the family of **available access transformations** or modes that constrain Void reachability and Jump landing.

Do not overload `S_n` immediately.

Candidate future auxiliary object:

```text
M_n = available modes / admissible transformations relative to S_n
```

---

## 6.2 Slice

### Required refinement candidate

Slice already supports Orientation, granularity, Context, and Re-Slice.

The new review suggests making explicit that a Slice mode can have an effective reach or operational envelope.

Candidate:

```text
Reach(Σ_{B,c})
```

This is where Current-Mode Saturation may be evaluated.

Also, Evaluation Scope Expansion is naturally represented as a change in Slice conditions:

```text
Σ_{B,c,E}
→
Σ_{B,c,E'}
```

rather than as rollback.

---

## 6.3 Stability

### Required change

No definition change currently required.

The recovered intuition reinforces that Stability is not decision, termination, or collapse.

### Open point

If Current-Mode Saturation is readable before Stability, it belongs within slice-ing.

If it is readable only after an establishment becomes stable but can no longer continue productively under the current mode, it may be a post-Stability condition.

This needs examples.

---

## 6.4 Incorporated Readability `ρ_n`

This concept becomes more important.

It can plausibly constrain:

```text
which Void becomes reachable later
which Jump landings are admissible
which new relations become available
which Orientation changes are plausible
```

Possible future refinement:

```text
ρ_n should not only mean retained readable content;
it may also alter the admissible transformation / landing space.
```

Do not formalize this yet without cross-case tests.

---

## 6.5 Continuity Readability

No direct definition change is required.

However, Decoupled Continuation raises an important test:

```text
Can continuity remain readable while effective coupling is temporarily absent?
```

If yes, continuity readability must not require continuous active coupling at every intermediate instant.

This may support a distinction between:

```text
continuous connection
vs
traceably resumable continuity
```

---

## 6.6 Trajectory

Trajectory already allows:

```text
branching
merging
gaps
Jump
reinterpretation
```

Therefore it can likely represent:

```text
saturation without Jump
Jump without saturation
decoupled intervals
later re-coupling
```

No linear sequence should be imposed.

A useful future test is whether the clutch-like interval appears as:

```text
node state
edge type
gap with retained traceability
```

in a graph/event-structure model.

---

## 6.7 Difference

The existing Difference definition is broad enough.

But the old tendency to derive collapse mechanically from thresholded Difference should be weakened.

Safer relation:

```text
Difference may provide evidence of Current-Mode Saturation
or may contribute to a Jump Condition,
but neither implication is universal.
```

Therefore avoid:

```text
Δ > θ ⇒ Collapse ⇒ Jump
```

as a general Gyro Logic law.

A domain-specific implementation may still use such a rule.

---

## 6.8 Boundary

Void should not be reduced to one Boundary State.

Boundary may express where a distinction becomes readable, while Void concerns what remains currently non-readable / non-inferable relative to the Slice.

The new accessibility axis further strengthens:

```text
Boundary classification
!=
Void accessibility
```

A Boundary can be readable even when what lies beyond it remains inaccessible.

Likewise, a previously Void relation may become readable after changing access mode without requiring Boundary to be the causal mechanism.

---

# 7. Revised provisional topology

The current review suggests the following non-canonical map:

```text
Structure
  ↓
Slice under Orientation / Context / Evaluation Scope / Access Mode
  ↓
slice-ing
  ├─ ordinary continuation
  ├─ currently unreadable region → Void
  │      └─ accessibility depends on admissible transformations
  ├─ Current-Mode Saturation
  │      ├─ Re-Slice
  │      ├─ change Orientation / scope / mode
  │      ├─ Defer / Stop
  │      └─ Jump (optional)
  ├─ Jump without prior Saturation (possible)
  └─ possible Decoupled Continuation interval
  ↓
slice-done
  ↓
Stability
  ↓
Operator Response
  ↓
later Structure / Slice / Jump / Re-Slice / other continuation
```

This diagram is exploratory only.

---

# 8. Main conclusions

## C1. Core change is not currently justified

```text
Structure → Slice → Stability
```

survives the intuition reverse review.

## C2. Void needs a second axis

Current readability and transformation-relative accessibility should be separated.

## C3. Collapse should be deprecated as a general term

Recommended working replacement:

```text
Current-Mode Saturation
```

with Japanese explanatory form:

```text
現在の切り取り方の到達限界
```

## C4. Jump must be decoupled from saturation / collapse

Separate:

```text
condition
transition
landing
```

## C5. ROLLBACK remains valid in GyroAuth

The intuition about widening observation belongs to a new concept:

```text
Evaluation Scope Expansion
```

not to ROLLBACK.

## C6. Clutch disengagement is a plausible third state

Working name:

```text
Decoupled Continuation
```

but its placement between slice-ing and inter-realization transition remains unresolved.

---

# 9. Open questions for the next session

1. Is Current-Mode Saturation a property of Slice, of the Slice path `P_n`, or of the relation between Orientation and Structure?
2. Can saturation be detected before `slice-done`, or only retrospectively?
3. What is the minimum structure needed to distinguish shallow and deep Void without inventing a scalar `Void depth`?
4. What families of admissible transformation should determine Void reachability?
5. Is Jump fundamentally an Operator Response, a Structure transition, or a relation between local Gyro realizations?
6. What are the minimal Jump landing classes, if any taxonomy is needed at all?
7. Can incorporated readability `ρ_n` be understood as modifying a later admissible-landing set without becoming an excessively broad catch-all variable?
8. Does Decoupled Continuation preserve Continuity Readability while suspending current effective coupling?
9. Is Decoupled Continuation internal to Slice, between Stability and the next Structure, or possible in both locations?
10. Should Evaluation Scope Expansion be represented simply as Re-Slice with changed parameters, or does it deserve a named auxiliary operation?
11. Which of these concepts belong only to GyroOS runtime semantics rather than Gyro Logic?
12. Which published statements use a mandatory `collapse → Jump` implication and therefore need a future-version clarification note?

---

# 10. Change status

```text
Core change: none
Published-paper change: none
GyroAuth ROLLBACK definition: preserve
Candidate terminology change: Collapse → Current-Mode Saturation
Candidate new distinction: Void readability vs accessibility
Candidate Jump refinement: condition / transition / landing
Candidate operation: Evaluation Scope Expansion
Candidate transitional state: Decoupled Continuation
Canonical adoption: none yet
```
