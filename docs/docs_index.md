# Gyro Logic Documentation Index

This directory contains theoretical notes and structured documents for **Gyro Logic**.

Gyro Logic is organized around the invariant Core principle:

```text
Structure → Slice → Stability
```

All other concepts are auxiliary, derivative, temporal, relational, operational, or interpretive extensions. They do not replace the Core.

---

## 1. Core Definitions

The primary definition document is:

```text
01_Core_Definitions.md
```

The refined Core definitions are:

```text
Structure = the mode in which something can be established.

Slice = the process by which a path is opened through a Structure toward an establishment.

Stability = the state in which the opened path is established and can continue.
```

The Core does not describe a static sequence of beginning, middle, and end. It describes how an establishment emerges within a continuing Trajectory.

Stability is not an evaluator. It is evaluated.

---

## 2. Core Definition Reference Structure

Boundary and Boundary State are read as derivative documents under the primary Core definition.

```text
01 Core Definitions
├── 15 Boundary
└── 16 Boundary State
```

More precisely, their conceptual dependency is:

```text
01 Core Definitions
└── 15 Boundary
    └── 16 Boundary State
```

This structure means:

- **01 Core Definitions** defines Structure, Slice, Stability, and their integrated interpretation.
- **15 Boundary** explains how a Difference becomes readable as a Slice-relative distinction.
- **16 Boundary State** explains how an object is provisionally positioned relative to that Boundary.

Boundary and Boundary State are not additional stages inserted into:

```text
Structure → Slice → Stability
```

---

## 3. Core Layer Documents

### 01. Core Definitions

Primary definition document for the invariant Core.

```text
01_Core_Definitions.md
```

### 01A. Gyro Unit

```text
Gyro Unit = Structure → Slice → Stability
```

Gyro Unit is the minimal time-free theoretical structure of Gyro Logic.

```text
01_GyroUnit_20260504.md
```

### 02. Gyro Process

Gyro Process is the time-including operational unfolding of Gyro Unit.

```text
Structure
→ Operator Orientation
→ slice-ing
→ slice-done
→ Stability
→ Operator Response
```

```text
02_GyroProcess_20260504.md
```

### 03. Gyro Loop

Gyro Loop is the iterative structure formed by repeated Gyro Processes.

```text
Gyro Process_n
→ Operator Response_n
→ Gyro Process_n+1 / Stop / Jump
```

```text
03_GyroLoop_20260504.md
```

### 04. Slice / slice-ing / slice-done

```text
Slice = the general process by which a path is opened through Structure
slice-ing = the time-including process in which Slice is progressing
slice-done = the established result of Slice
```

```text
04_Slice_20260504.md
```

### 05. Stability

Gyro Logic distinguishes between:

```text
Stability as property
Stability over time
```

Stability is a state quantity, not an evaluator or decision-maker.

```text
05_Stability_20260504.md
```

### 06. Operator

```text
Operator Orientation = directional condition at the entrance of Slice
Operator Response = post-Stability reaction
```

```text
06_Operator_20260504.md
```

---

## 4. Context Extension

The Context Extension introduces Context, Re-Slice, Context Loop, Loop Stop, Void, and Coincidence.

These concepts are derived from the Core and extend the theory of Slice, Loop, and Operator Response.

### 08. Context

```text
Context = inferable surrounding Structure not explicitly represented by a Slice
```

```text
08_Context_20260513.md
```

### 09. Re-Slice

```text
Re-Slice = secondary Slice performed on a prior Slice result, especially Context
```

Core statement:

```text
Reading Context is Re-Slice.
```

```text
09_ReSlice_20260513.md
```

### 10. Context Loop

```text
Context
→ Re-Slice
→ New Context
→ Re-Slice
→ ...
```

```text
10_Context_Loop_20260513.md
```

### 11. Loop Stop

```text
Stability does not stop the Loop.
Operator Response stops the Loop.
```

```text
11_Loop_Stop_20260513.md
```

### 12. Context / Void / Coincidence

```text
Context = inferable surrounding Structure
Void = non-inferable region under the current Slice
Coincidence = event whose relation, causality, or trajectory cannot be stably reconstructed under the current Slice
```

```text
12_Context_Void_Coincidence_20260513.md
```

### 13. Context Integration

```text
Gyro Logic integrates Context as an internal structure of Slice results,
while preserving Structure → Slice → Stability.
```

```text
13_Context_Integration_20260513.md
```

---

## 5. Dynamic Equivalence Extension

### 14. Dynamic Equivalence

Dynamic Equivalence is an equivalence relation defined over Trajectory.

```text
Dynamic Equivalence is not static equality.
It is stability-bounded continuity over Trajectory.
```

Notation:

```text
A ≈_T B
O_T(A) ≈_σ O_T(B)
```

```text
14_Dynamic_Equivalence_20260518.md
```

---

## 6. Boundary Extension

The Boundary Extension is a derivative interpretation of Slice results under the refined Core.

```text
01 Core Definitions
├── 15 Boundary
└── 16 Boundary State
```

### 15. Boundary

```text
Boundary = a Slice-relative distinction that has become readable through Slice.
```

Boundary may be generated, revealed, or stabilized by Slice, relative to Operator Orientation and Context.

Boundary is not a fixed line inherent in Structure and is not an additional Core stage.

```text
15_Boundary_20260610.md
```

### 16. Boundary State

```text
Boundary State = the provisional relational state of an object
with respect to a Boundary that has become readable through Slice.
```

Boundary State is not an intrinsic attribute of the object and is not a stage between Slice and Stability.

Candidate Boundary States:

```text
Normal
Non
Un
Absence
Blank
Unknown
Void
```

```text
16_Boundary_State_20260610.md
```

---

## 7. Layer Boundary

Gyro Logic is the theoretical layer.

```text
Gyro Logic
↓
GyroOS
↓
GyroAuth
```

- **Gyro Logic** defines the theory.
- **GyroOS** implements the theory.
- **GyroAuth** applies the theory.

Implementation concerns from GyroOS must not redefine Gyro Logic.
Application concerns from GyroAuth must not be mixed into the theory layer.

```text
07_toGyroOS_handover_20260504.md
```

---

## 8. Suggested Reading Order

For the Core and its primary interpretation:

```text
01_Core_Definitions.md
01_GyroUnit_20260504.md
02_GyroProcess_20260504.md
03_GyroLoop_20260504.md
04_Slice_20260504.md
05_Stability_20260504.md
06_Operator_20260504.md
```

For Context Extension:

```text
08_Context_20260513.md
09_ReSlice_20260513.md
10_Context_Loop_20260513.md
11_Loop_Stop_20260513.md
12_Context_Void_Coincidence_20260513.md
13_Context_Integration_20260513.md
```

For Dynamic Equivalence:

```text
14_Dynamic_Equivalence_20260518.md
```

For Boundary Extension:

```text
01_Core_Definitions.md
15_Boundary_20260610.md
16_Boundary_State_20260610.md
```

For implementation handover:

```text
07_toGyroOS_handover_20260504.md
```

---

## 9. Current Status

Current theoretical focus:

```text
Core:
Structure → Slice → Stability

Primary definition:
01 Core Definitions

Extensions:
Gyro Unit / Gyro Process / Gyro Loop
Context / Re-Slice / Context Loop
Loop Stop / Void / Coincidence
Dynamic Equivalence / Trajectory
Boundary / Boundary State
```

These documents belong to the Gyro Logic layer.

---

## 10. Minimal Summary

```text
Gyro Logic begins from Structure → Slice → Stability.

Structure is the mode in which something can be established.
Slice opens a path through Structure toward an establishment.
Stability is the state in which that path is established and can continue.

Gyro Unit defines the time-free minimal structure.
Gyro Process unfolds it into a time-including cycle.
Gyro Loop connects Processes through Operator Response.

Context is the inferable surrounding Structure produced with a Slice result.
Reading Context is Re-Slice.
Repeated Re-Slice forms a Context Loop.
Loop Stop is selected by Operator Response.

Dynamic Equivalence is stability-bounded continuity over Trajectory.

Boundary is a Slice-relative distinction that has become readable through Slice.
Boundary State is the provisional relational state of an object with respect to that Boundary.
```
