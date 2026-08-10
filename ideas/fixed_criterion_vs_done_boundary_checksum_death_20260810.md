# Fixed Criterion vs `done` Boundary: Checksum and Death

Date: 2026-08-10
Status: Exploratory / non-canonical
Target layer: Gyro Logic

## 1. Question

This note studies a narrow question raised by the recent critique of Operator-side `done` boundaries:

> Does a fixed criterion determine `done` itself, or does it only judge something inside a local establishment that has already been selected?

The comparison uses two cases:

- checksum verification in file transfer;
- death determination.

The goal is not to deny that some criteria can be fixed and deterministic. The goal is to separate several levels that are easy to collapse into one.

---

## 2. First distinction: fixed criterion does not automatically mean fixed local unit

Suppose a criterion is fixed.

Examples:

```text
checksum_expected == checksum_actual
```

or a legally/medically specified death criterion.

Once the objects, scope, and rule are fixed, the judgment may be deterministic or highly constrained.

However, before the criterion can be applied, another question has usually already been settled:

> What exactly is being treated as the unit to which the criterion applies?

This suggests separating:

```text
A. local unit / establishment selection
B. criterion application inside that selected unit
```

A fixed answer at B does not by itself prove that A was uniquely fixed by the event as a whole.

---

## 3. Checksum case

### 3.1 Apparent fixedness

A checksum comparison can be fully deterministic once the following are fixed:

- the byte range;
- the serialization / representation;
- the checksum algorithm;
- the expected checksum;
- the actual data being checked.

Then:

```text
match / mismatch
```

is not a matter of Operator preference.

This is a genuine local fixed judgment.

### 3.2 But what is the larger establishment?

The phrase:

```text
file transfer completed
```

can refer to different ranges of one larger process:

```text
last byte sent
→ last byte received
→ checksum computed
→ checksum matched
→ buffer flushed
→ file closed
→ application accepted
```

The checksum criterion may determine:

> whether the selected transferred data matches the expected data under the selected checksum rule.

It does not automatically determine:

> which point in the whole transfer process must universally count as `done`.

A sender-side `done`, receiver-side `done`, integrity-verified `done`, storage-level `done`, and application-level `done` may all use deterministic local rules while referring to different local establishments.

### 3.3 Scope inside the checksum itself

Even checksum verification presupposes a selected scope.

For example:

```text
bytes 0..N
```

versus:

```text
header + payload
```

versus:

```text
payload only
```

may yield different checksum judgments without any arithmetic ambiguity.

The fixed criterion operates after the relevant range has been selected.

This is analogous to arithmetic:

```text
1 + 1 = 2
```

The equality is fixed under ordinary arithmetic, but that does not answer the prior question:

> Which two things are being counted as the two `1`s in this local application?

The fixed internal rule and the selection of the local establishment are different questions.

---

## 4. Death case

### 4.1 Apparent fixedness

A medical or legal system can define a criterion for declaring death.

Once the applicable rule, measurement procedure, jurisdiction, and observed conditions are fixed, the declaration can be tightly constrained.

Therefore it would be wrong to say:

> because Operator/Context may change, the result may arbitrarily become death or non-death.

The current study does not require that claim.

### 4.2 What continues below or beyond the declaration?

A death declaration does not mean that every process associated with the body ends at one universal instant.

Depending on the level under consideration:

```text
circulation
brain function
cell metabolism
organ viability
chemical reaction
decomposition
microbial activity
```

have different continuities and transitions.

Thus a legally or medically fixed declaration can establish:

> this person is to be treated as dead under this specified criterion.

That does not prove:

> every process involving the body has one identical natural `done` point.

### 4.3 The criterion also presupposes a local establishment

The criterion applies to something already treated as the relevant case:

```text
this person
this physiological state
this measurement window
this legal/medical rule
```

The rule does not itself create the entire event range from conception to decomposition.

It judges a selected local establishment within that broader continuation.

---

## 5. Common structure

The checksum and death cases differ strongly, but the same analytical separation appears:

```text
continuing process / broader Structure
        ↓
local range / establishment selected
        ↓
criterion applied within that local range
        ↓
local judgment
```

Examples:

```text
transfer process
→ selected transferred object/range
→ checksum rule
→ match / mismatch
```

and:

```text
biological / social continuation
→ selected person/state/measurement frame
→ medical/legal criterion
→ death declaration
```

The criterion may be fixed at the third step without uniquely fixing the first or second steps for every possible Orientation and Context.

---

## 6. Important correction to the current discussion

The statement:

> Operator and its criteria are always moving.

is too broad if interpreted as:

> every local criterion is always fluid during every judgment.

Some local criteria are intentionally frozen for a comparison, protocol step, calculation, proof, test, or declaration.

A safer statement is:

> Operators, Contexts, Orientations, and adopted criteria can change across the continuing process and across later evaluations, while a particular local evaluation may temporarily hold its criterion fixed.

This avoids conflating:

```text
local fixedness
```

with:

```text
global or permanent fixedness
```

---

## 7. Retrospection and verification

This distinction makes retrospective verification easier to describe.

A local establishment may be made at time `n`:

```text
E_n = "transfer complete"
```

or:

```text
E_n = "death declared"
```

Later, another Operator or later state may examine what remains:

```text
logs
checksums
measurements
records
traces
subsequent states
```

and form a new present establishment about the earlier one.

For example:

```text
E_n: transfer complete
↓
later verification
↓
E_m: the earlier transfer contained corruption
```

This does not necessarily mean the arithmetic checksum rule changed.

It may mean:

- a different object/range was later inspected;
- additional evidence became available;
- the earlier local establishment was too broad;
- the earlier criterion was applied incorrectly;
- a later establishment concerns a different relation than the earlier one.

Likewise, later review of a death declaration may concern:

- whether the specified criterion was actually satisfied;
- whether the measurements were reliable;
- whether the correct legal/medical rule was used;
- whether the earlier establishment should be revised.

The important distinction is:

```text
later re-evaluation of an establishment
≠
retroactive alteration of a fixed local calculation
```

---

## 8. Working conclusion

The comparison suggests that a fixed criterion can be real and meaningful without refuting Operator-relative local establishment.

A fixed criterion often determines a judgment **inside a selected local establishment**.

It does not automatically determine the unique `done` boundary of the entire continuing event or Structure.

Therefore the current safer picture is:

```text
continuing change
↓
Operator-side local unitization
↓
local establishment
↓
possibly fixed local criterion
↓
local judgment
↓
continued change / later evidence
↓
retrospective verification or re-evaluation
```

This keeps three questions separate:

1. What range is being treated as one local establishment?
2. What criterion is used inside that establishment?
3. How can that establishment later be verified, revised, or related to later establishments?

The current hypothesis is that many apparent counterexamples based on deterministic rules concern question 2, while the `done` discussion is primarily about questions 1 and 3.

---

## 9. Next pressure tests

The next examples should test whether this separation fails.

### T1. Criterion defines the unit itself

Find a case where the criterion does not merely judge a selected local establishment but literally defines the unit boundary, leaving no independent unitization step.

### T2. Same fixed criterion, different local units

Use one identical deterministic criterion over two different selected ranges and show whether both local establishments remain coherent.

### T3. Same local unit, changing criterion

Hold the establishment fixed while changing only the criterion and compare the resulting judgments.

### T4. Retrospective verification with no surviving trace

Ask whether an earlier establishment can be meaningfully re-evaluated when almost nothing remains from the original process.

### T5. Verification versus reconstruction

Separate:

```text
verify an earlier local establishment
```

from:

```text
construct a new present establishment about what probably happened earlier
```

These may overlap, but should not be assumed identical.
