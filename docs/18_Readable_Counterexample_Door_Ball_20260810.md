# Readable Counterexample Study: Automatic Door and Ball Recognition

Date: 2026-08-10
Status: Exploratory / non-canonical
Target layer: Gyro Logic

## 1. Purpose

This study tests the current working semantics of `Readable(...)` against two concrete cases:

1. an automatic door sensor and opening decision;
2. visual ball recognition and avoidance/action.

The goal is not to confirm the current definition, but to find where it fails.

The current working condition is:

```text
Readable(x; S,B,c,Σ,Γ)
⇒ Available(x) ∧ Articulable(x) ∧ Addressable(x) ∧ Usable(x)
```

with the converse still unproven.

The Core remains unchanged:

```text
Structure → Slice → Stability
```

`Readable` is not introduced as a fourth Core element.

---

## 2. Test frame

For both examples, distinguish the following stages analytically:

```text
physical / domain occurrence
↓
signal or candidate availability
↓
local articulation
↓
Readable judgment
↓
possible Stability
↓
downstream response
```

This ordering is only for analysis. It is not a replacement for the Gyro Core.

The test questions are:

1. What exists independently of the present reading?
2. What becomes available to the current Slice?
3. What becomes locally articulated?
4. What becomes addressable?
5. What can participate in downstream processing?
6. At what point, if any, should `Readable=true` hold?
7. Does `Readable=true` imply Stability?
8. What remains residual not-yet?
9. Can later processing retroactively change how an earlier stage is described without changing what was readable then?

---

# Part I — Automatic Door

## 3. Minimal scenario

Consider an automatic door equipped with a proximity or motion sensor.

A person approaches the entrance.

The physical scene may include:

- the person;
- background motion;
- reflected infrared energy;
- sensor noise;
- distance change;
- direction of motion;
- the door state;
- configured detection thresholds;
- safety logic;
- timing constraints.

The door system does not need to understand `person` semantically in order to open.

A minimal operational chain may be represented as:

```text
environmental change
→ sensor response
→ candidate detection
→ threshold / relation becomes available
→ door-control condition
→ open / remain closed
```

---

## 4. Structure

A candidate Structure for the example is not merely the raw sensor input.

It includes the mode in which a relevant establishment may become available, including at least:

```text
sensor field
sensor configuration
current door state
admissible detection relations
threshold conditions
control connectivity
```

Thus:

```text
S_door ≠ raw sensor value
```

The approaching person may exist in the environment before any present Slice makes that approach available to the door system.

Therefore:

```text
Exists(person approaching) ⇏ Readable(person approaching)
```

for the door realization.

---

## 5. Slice and availability

Let the current Orientation be operationally expressed as:

```text
B_door = detect a condition relevant to opening the door
```

and let Context include current threshold, sensor mode, door state, and safety settings.

The Slice process may unfold as signal sampling and relation formation.

At first, a sensor may produce a nonzero value.

That gives a useful negative case:

```text
SignalPresent(x)
```

but not necessarily:

```text
Readable(x)
```

because a raw fluctuation may still be indistinguishable from noise.

This supports the current claim:

```text
Detected(x) ⇏ Readable(x)
```

provided `Detected` is used broadly enough to include low-level sensing.

---

## 6. Local articulation in the door case

Suppose the sensor-processing stage reaches a local articulation such as:

```text
motion/proximity condition exceeds the currently relevant criterion
```

Call this articulation `a_door`.

At this point, the system does not need to articulate:

```text
this is Shuntaro Kawakami
```

or even:

```text
this is a human being
```

The relevant local articulation can be much weaker:

```text
opening-relevant presence is established
```

This is important for Readable semantics.

### Observation D1

`Articulable` must not require semantic classification at a higher conceptual level than the current Slice requires.

A relation can be readable as:

```text
opening-relevant presence
```

without being readable as:

```text
person
```

Therefore readability is not only Context-relative but also **type-of-articulation-relative**.

---

## 7. Addressability

Once the local relation can be distinguished by the control process as the condition to which an opening rule applies, it is addressable in the minimal operational sense.

For example:

```text
if opening_relevant_presence then request_open
```

The system need not possess a human-readable label.

Thus the previous working statement remains plausible:

```text
Addressable ≠ linguistically named
```

A better interpretation is:

```text
Addressable(x)
= x can be selectively referenced by at least one admissible relation or operation in the current realization
```

This is more precise than requiring explicit representation.

---

## 8. Usability and a first pressure point

Suppose `a_door` has become available and addressable, but the control link to the door motor is broken.

Then:

```text
Available(a_door)
Articulable(a_door)
Addressable(a_door)
```

may all hold.

But if `Usable` means:

```text
actually capable of producing the later physical opening
```

then `Usable(a_door)` fails because the actuator is broken.

Would that make `a_door` unreadable?

Probably not.

The controller may still correctly read:

```text
opening-relevant presence
```

while being unable to actuate the door.

### Counterexample D2

This suggests that **downstream usability is too strong if it includes successful downstream execution**.

The safer condition is:

```text
ReferableByAdmissibleNext(x)
```

or:

```text
DownstreamAvailable(x)
```

meaning:

> at least one admissible downstream judgment, relation, or operation can take `x` as an input or condition.

It must not require the downstream operation itself to succeed.

Therefore revise the R4 candidate from:

```text
Usable
```

toward:

```text
AdmissiblyConsumable
```

or:

```text
DownstreamAddressable
```

The exact term remains open.

---

## 9. Readable versus Stability in the door case

Suppose the sensor relation becomes readable:

```text
Readable(a_door) = true
```

but rapid oscillation around the threshold produces:

```text
present
not-present
present
not-present
```

at successive samples.

The local articulation may be readable at each sample while the system does not yet possess a sufficiently stable scene for a robust opening decision.

This gives a concrete example of:

```text
Readable(a) ⇏ Stable(a)
```

A Stability Scene may require additional conditions such as:

- temporal persistence;
- hysteresis;
- confidence;
- safety compatibility;
- continuation support.

These are domain-specific Stability criteria, not universal definitions.

---

## 10. Residual not-yet in the door case

Even after the opening-relevant relation becomes readable and stable enough for operation, many things remain unresolved:

- whether the detected entity is a person, cart, animal, or reflected object;
- exact identity;
- future direction;
- intent;
- whether another entity follows behind;
- other relations outside the current sensor field.

Therefore:

```text
Readable(opening-relevant presence)
```

and even:

```text
Stable(opening-relevant presence)
```

are compatible with substantial residual not-yet.

This strongly supports locality.

---

# Part II — Ball Recognition

## 11. Minimal scenario

Consider an observer or vision system seeing a scene containing a moving ball.

A simplified chain may be:

```text
visual field
→ local contrast / edge / motion signals
→ candidate object grouping
→ ball-like articulation
→ ball recognition
→ trajectory / collision relation
→ avoidance or interception
```

The important feature is that multiple readable articulations may appear at different granularities.

---

## 12. Structure

A candidate Structure contains more than the currently recognized ball.

It may include:

```text
visual field
spatial relations
motion relations
background objects
prior learned distinctions
current task context
body relation
available action relations
```

Thus:

```text
S_ball ≠ recognized ball
```

The ball can physically exist before it becomes readable as a ball.

---

## 13. Multiple local articulations

The visual process may pass through several possible local articulations:

```text
a changing patch
→ a bounded moving object
→ a round moving object
→ a ball
→ a ball approaching me
```

This creates an important question.

Does Readable become true only at `ball`?

No.

Each stage may already be readable relative to a different Orientation and downstream relation.

For example:

```text
Readable(moving object)
```

may be true before:

```text
Readable(ball)
```

and:

```text
Readable(ball)
```

may be true before:

```text
Readable(collision risk)
```

### Observation B1

Readable cannot be modeled as one single transition from unreadable to readable for the whole underlying object.

Readability attaches to **a particular articulation or relation**.

Therefore the model should prefer:

```text
Readable(a_k; S,B,c,Σ,Γ)
```

rather than informal language such as:

```text
the object became readable
```

unless the articulation level is explicit.

---

## 14. Early readable relation without object identity

Suppose a fast-moving shape enters peripheral vision.

The observer may become able to act on:

```text
something is approaching rapidly from the right
```

before becoming able to recognize:

```text
it is a ball
```

The first relation may already support avoidance.

Therefore:

```text
Readable(approaching-object relation)
```

can hold while:

```text
¬Readable(ball identity/classification)
```

### Observation B2

Readable does not require object identity.

This is consistent with Gyro Logic's separation between continuity, relation, and Identity.

It also reinforces that `Readable` should be typed or scoped by the articulation being judged.

---

## 15. Misrecognition

Now consider a visual illusion or classification error.

A round moving plastic bag is articulated as:

```text
ball
```

and the system acts accordingly.

Was `ball` readable?

There are two possible interpretations:

### Interpretation A

Readable means:

```text
available as an articulated and operationally addressable result
```

Then the mistaken ball articulation was readable, even though false relative to a later or broader account.

### Interpretation B

Readable additionally requires domain truth or correctness.

Then the mistaken articulation was not readable.

The current Gyro Logic framework appears to favor Interpretation A because readability concerns local establishment under current Slice conditions, while later Re-Slice may revise what was established.

### Counterexample B3

If this reading is accepted, then:

```text
Readable(x) ⇏ True(x)
```

and:

```text
Readable(x) ⇏ Correct(x)
```

must be stated explicitly.

Otherwise Readable risks silently becoming an epistemic truth predicate.

This is a major formal clarification.

---

## 16. Retrospective correction

Suppose the observer first reads:

```text
ball
```

and later recognizes:

```text
plastic bag
```

The later correction should not require saying that the earlier state was never readable.

Instead:

```text
Readable_n(ball-articulation)
```

may have held at realization `n`, while:

```text
Readable_{n+1}(ball-articulation)
```

no longer holds or is superseded after Re-Slice and Context update.

This supports the prior proposition:

```text
Readable_n(x) ⇏ Readable_{n+1}(x)
```

and clarifies that readability is **historically situated without being identical to stored history**.

---

## 17. Ball recognition and Stability

A single frame may make a ball-like articulation readable.

But Stability for an action such as interception may require a richer scene:

```text
ball articulation
+ motion relation
+ spatial relation to observer
+ continuation estimate
```

Thus:

```text
Readable(ball)
```

is weaker than:

```text
Stable(ball-as-action-relevant scene)
```

Again:

```text
Readable ⇏ Stability
```

is supported.

---

# Part III — Comparison

## 18. Common structure across the two cases

The two examples support the following shared chain:

```text
domain occurrence
↓
locally available signal/relation
↓
articulation at some granularity
↓
selective addressability
↓
Readable judgment for that articulation
↓
possible Stability Scene
↓
response
```

The decisive point is not semantic richness.

For the automatic door, the readable articulation may be only:

```text
opening-relevant presence
```

For visual recognition, a readable articulation may be:

```text
moving object
```

before `ball` becomes readable.

Therefore Readable is not a synonym for complete recognition or understanding.

---

## 19. What survived the test

The following parts of the current working model survive both cases reasonably well.

### T1. Existence does not imply readability

```text
Exists(x) ⇏ Readable(x)
```

### T2. Detection does not necessarily imply readability

Low-level signal presence can remain below articulation.

```text
Detected(x) ⇏ Readable(x)
```

### T3. Readability is condition-relative

The same underlying occurrence may support different readable articulations under different Orientation, Context, and Slice.

### T4. Readability is local

Readable articulation does not exhaust Structure.

### T5. Readability does not imply Stability

Both cases admit readable local results that are insufficient for robust continuation.

### T6. Readability need not persist

Re-Slice or Context update can revise later readability.

---

## 20. What requires revision

### R-REV1. `Usable` is too ambiguous and may be too strong

If `Usable` requires successful downstream action, the broken-door-actuator case becomes a counterexample.

Replace the working condition with something closer to:

```text
AdmissiblyReferableNext(x)
```

meaning:

> `x` can serve as an input, condition, distinction, or reference for at least one admissible downstream judgment or operation.

This does not require that the downstream operation completes successfully.

### R-REV2. Readable must be articulation-relative

The ball case shows that `moving object`, `ball`, and `collision risk` may become readable at different stages.

Therefore:

```text
Readable(object)
```

is often under-specified.

Prefer:

```text
Readable(a; S,B,c,Σ,Γ)
```

where `a` denotes the local articulation or relation being judged.

### R-REV3. Readability must be separated from truth/correctness

The misrecognition case suggests:

```text
Readable(a) ⇏ True(a)
Readable(a) ⇏ Correct(a)
```

unless a specialized domain explicitly incorporates correctness into its admissibility criteria.

This prevents `Readable` from becoming an implicit truth predicate.

---

## 21. Revised candidate conditions

A stronger second candidate is:

```text
Readable(a; S,B,c,Σ,Γ)
```

when:

```text
Available(a; S,B,c,Σ,Γ)
∧ Articulated(a; S,B,c,Σ,Γ)
∧ SelectivelyAddressable(a; B,c,Γ)
∧ AdmissiblyReferableNext(a; S,B,c,Σ,Γ)
```

where:

### C1. Available

The articulation is locally available in the present realization.

### C2. Articulated

The available content has sufficient local distinction to count as a particular relation or result rather than undifferentiated process residue.

### C3. Selectively Addressable

At least one current admissible relation or operation can distinguish and refer to this articulation rather than treating it as indistinguishable background.

### C4. Admissibly Referable Next

At least one admissible downstream judgment, relation, evaluation, or operation can take this articulation as a condition or input.

This is weaker than requiring successful downstream execution.

The sufficiency direction remains unproven:

```text
C1 ∧ C2 ∧ C3 ∧ C4
?⇒ Readable
```

---

## 22. Candidate propositions added by the test

### P-R6: Readability is articulation-relative

For one underlying occurrence `o`, it is possible that:

```text
Readable(a1(o))
∧ ¬Readable(a2(o))
```

under the same broad physical scene.

Example:

```text
Readable(moving object)
∧ ¬Readable(ball)
```

### P-R7: Readability does not entail truth

```text
Readable(a; S,B,c,Σ,Γ)
⇏ True(a)
```

unless truth is explicitly included in a specialized admissibility model.

### P-R8: Downstream execution failure does not negate readability

If an articulation is already selectively addressable and available to an admissible downstream operation, failure of a later actuator or executor does not by itself imply:

```text
¬Readable(a)
```

This proposition preserves the distinction between readable establishment and downstream response success.

---

## 23. Remaining counterexamples to test

The two examples do not settle the semantics.

Next pressure tests should include:

1. **A result visible to a human but inaccessible to the machine that produced it.**
2. **A machine-internal state consumed automatically but never exposed as an explicit object.**
3. **A relation that becomes readable only retrospectively.**
4. **Two contradictory articulations that are simultaneously addressable.**
5. **A readable but unusable archival record.**
6. **A highly actionable signal that cannot yet be articulated beyond `act now`.**
7. **A false articulation that remains Stable for a long period.**
8. **A relation readable to one Operator but not another under the same Structure.**

These cases are especially important for determining whether `Articulated`, `SelectivelyAddressable`, and `AdmissiblyReferableNext` are independent conditions or partially redundant.

---

## 24. Current result

The automatic-door and ball-recognition cases do not break the overall direction of the Readable study, but they do force three refinements.

```text
1. downstream usability must not mean successful execution;
2. readability must attach to a specific articulation/relation;
3. readability must not silently imply truth or correctness.
```

The current strongest working statement is therefore revised to:

```text
Readable is a local and condition-relative judgment that a specific articulation or relation has become available in a sufficiently distinguished form to be selectively addressed and admitted as an input or condition for at least one downstream judgment, relation, evaluation, or operation.
```

Japanese working reading:

```text
Readableとは、特定のarticulationまたはrelationが、現在のStructure・Orientation・Context・Slice・readability contextのもとで局所的に利用可能となり、他と区別して参照でき、少なくとも一つの許容された後続の判断・関係づけ・評価・作用に入力または条件として渡せる状態になった、という条件相対的な判断である。
```

This remains exploratory and non-canonical.

---

## 25. Layer consistency check

### Gyro Logic

This study concerns theory-level semantics of Readable only.

### GyroOS

The automatic door and machine-processing examples are illustrative instantiations only. No runtime API or implementation contract is added to Gyro Logic.

### GyroAuth

No authentication criterion is introduced. The ball and door examples do not modify the GyroAuth application model.

The invariant layering remains:

```text
Gyro Logic
↓
GyroOS
↓
GyroAuth
```
