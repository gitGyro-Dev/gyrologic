# Structure Identity Case Study v0

## 1. Purpose

This document examines the question:

```text
How far may a Structure change while remaining the same Structure,
and at what point should it be treated as a different Structure?
```

The analysis uses the following examples:

```text
ocean
society
human body
document
runtime
cake
country / national border
```

This is a preliminary theoretical study.

It does not change the invariant Core:

```text
Structure
↓
Slice
↓
Stability
```

It also preserves the following distinction:

```text
Structure may exist without a particular Slice.

Slice is required for a particular readability or establishment,
not for the existence of Structure itself.
```

Structure is not identical to Trajectory.

```text
Structure may retain traces of Trajectory.
Trajectory may connect successive Structure sections.
Structure Identity concerns whether those sections may be treated
as continuations of the same Structure.
```

---

## 2. Identity Dimensions

The examples suggest that Structure Identity cannot be reduced to one universal condition such as material sameness.

Candidate identity dimensions include:

```text
material continuity
relational continuity
organizational continuity
causal / historical continuity
functional continuity
continuity of establishment possibilities
continuity of admissible Slices
boundary continuity
social or institutional recognition
```

No single dimension is sufficient for every Structure.

A preliminary distinction is:

```text
Existence
= whether Structure exists

Identity
= whether changed Structure sections remain continuations
  of the same Structure

Readability
= whether that existence or continuity becomes readable
  under a particular Slice
```

Structure existence is not created by Slice.

Structure Identity may hold even when it is not currently readable.

A Slice may provide evidence for or against a particular identity relation.

---

## 3. Case Table

| Example | What may change while identity persists | What may preserve identity | Possible identity break | Important Slice dependence |
|---|---|---|---|---|
| **Ocean** | water molecules, temperature, salinity, currents, coastline, ecosystems | hydrological and geographical continuity; basin and circulation relations; continued readability as one oceanic system | loss of basin or circulation continuity; complete separation into independently sustained bodies; transformation into a fundamentally different hydrological organization | geographic, ecological, legal, climatic, and hydrological Slices may identify different boundaries and continuities |
| **Society** | members, generations, laws, customs, institutions, economy, language use | continuity of relations, institutions, shared practices, communication, historical succession, and capacity for further social establishment | collapse of relational and institutional continuity; inability to connect successor arrangements to prior social organization; complete replacement without meaningful succession | legal, cultural, economic, demographic, and political Slices may disagree about whether the same society continues |
| **Human body** | cells, molecules, microbiome, weight, age, organs, appearance, learned behaviour | organismic regulation, metabolism, integrated physiological coordination, causal bodily continuity, retained developmental history | irreversible loss of organismic integration; division or replacement that no longer preserves one organismic continuation | biological, legal, personal, neurological, medical, and material Slices may preserve different identities; after death, the physical body may remain while organismic identity no longer does |
| **Document** | wording, formatting, sections, metadata, file location, authors, translations | version lineage, editorial continuity, semantic purpose, reference identity, maintained revision history | fork without a privileged continuation; total semantic replacement; loss of lineage; copies becoming independent documents | file identity, semantic identity, publication identity, legal identity, and version-control identity may produce different answers |
| **Runtime** | memory values, requests, threads, loaded modules, resource usage, internal states | process or session continuity, control-loop continuity, namespace, retained runtime memory, causal execution chain, accepted hot updates | termination and restart without continuity; loss of session or process lineage; state replacement that cannot be connected to the prior execution | OS process, application session, distributed service, user session, and logical-runtime Slices may disagree about whether a restart is the same runtime |
| **Cake** | temperature, moisture, decoration, slicing, minor ingredient loss, aging | material and causal continuity from preparation; maintained organization as one edible whole; social designation as the same cake | mixing into another mass, complete destruction, division into independently treated products, transformation into a different food organization | material, culinary, ownership, event, recipe, and naming Slices may differ; batter-to-cake may be one causal Trajectory but not necessarily the same Structure type |
| **Country / national border** | population, government, constitution, territory, borders, currency, institutions, official name | sovereignty, institutional succession, legal continuity, recognition, historical and administrative continuity, continued capacity for national establishment | state dissolution, succession into multiple states, annexation without accepted continuity, loss of institutional and sovereign correspondence | legal, political, geographical, historical, diplomatic, cultural, and population Slices may disagree; the national border is a derivative Boundary and is not identical to the country Structure |

---

## 4. Case Analysis

### 4.1 Ocean

An ocean does not preserve identity through identical material composition.

Its water is continuously exchanged.

Therefore:

```text
same material elements
```

cannot be the primary condition.

A stronger candidate is:

```text
continuity of hydrological and geographical organization
```

However, the boundary of an ocean is not absolute.

Different geographic, legal, ecological, and climatic Slices may produce different readable boundaries.

This suggests:

```text
Ocean Structure may persist while its readable Boundary changes.
```

A possible identity break occurs when relational continuity is lost and independently sustained bodies emerge.

Even then, whether a break occurred may depend on the Slice used to read oceanic organization.

### 4.2 Society

A society may persist despite complete generational replacement.

Therefore, member identity is insufficient.

Candidate continuity conditions include:

```text
social relations
institutions
shared practices
communication
historical succession
capacity for further social establishment
```

A revolution may radically alter institutions without necessarily creating an entirely new society.

This shows that large Difference does not automatically imply Structure replacement.

A possible break occurs when no meaningful institutional, relational, or historical correspondence can connect the prior and later arrangements.

### 4.3 Human Body

The human body is a strong example of continuity without material immobility.

Cells and molecules change while organismic continuity may remain.

Candidate identity conditions include:

```text
integrated regulation
metabolic continuity
causal bodily continuity
developmental continuity
```

Death reveals a crucial distinction.

```text
the physical body may remain
but the living organismic Structure may no longer continue
```

Therefore, multiple Structure readings may coexist over the same material carrier.

The answer depends on whether the Slice concerns material body, living organism, legal person, neurological continuity, or personal identity.

### 4.4 Document

A document may change extensively while remaining the same document through a revision lineage.

This suggests that document identity may rely on:

```text
version continuity
semantic purpose
reference continuity
editorial history
```

A byte-identical copy may be a different file instance.

A heavily edited file may remain the same document.

Therefore:

```text
static equality is neither necessary nor sufficient for document identity.
```

A fork is especially important.

One Structure may produce multiple continuations, and identity may cease to be uniquely directed unless one branch is institutionally or historically selected as canonical.

### 4.5 Runtime

A runtime changes continuously by definition.

Its identity cannot be tied to one state snapshot.

Candidate continuity conditions include:

```text
process continuity
session continuity
control-loop continuity
runtime memory
causal execution chain
namespace continuity
```

A hot update may preserve runtime identity.

A restart may break OS-process identity while preserving logical service identity or user-session identity.

Thus:

```text
same runtime
```

is always relative to an identity criterion and Slice.

This example connects directly to Runtime Continuity in GyroOS.

### 4.6 Cake

Cake exposes the difference between causal continuity and Structure-type continuity.

Batter and baked cake may belong to one preparation Trajectory.

However:

```text
batter Structure
≠ cake Structure
```

may still be the safer reading because the admissible establishments and organization change qualitatively during baking.

After baking, decoration or slicing may preserve reference to the same cake.

But dividing it into independently distributed portions may preserve part-whole lineage while ending the whole-cake Structure.

This example suggests:

```text
one Trajectory may contain a Structure transition
```

without the Trajectory itself ending.

### 4.7 Country and National Border

A country may persist while its borders, government, laws, population, and institutions change.

Therefore, country identity cannot be reduced to territory or border geometry.

Candidate continuity conditions include:

```text
sovereign succession
institutional continuity
legal continuity
international recognition
historical administration
capacity for national establishment
```

A national border is a Boundary made readable under political, legal, and geographical Slices.

It is not identical to the country Structure.

```text
country Structure
≠ national border
```

Border change does not necessarily imply country replacement.

Conversely, a state may cease while much of the territory and population remain.

This case strongly separates:

```text
Structure Identity
from
Boundary continuity
```

---

## 5. Cross-case Findings

### 5.1 Material sameness is neither necessary nor sufficient

Oceans, bodies, societies, and runtimes persist while their components change.

A document copy may preserve all bytes while becoming a different instance.

Therefore:

```text
Structure Identity ≠ component equality
```

### 5.2 Boundary continuity is neither necessary nor sufficient

Oceans and countries may preserve identity while their boundaries change.

A cake may retain its visible boundary while its internal organization is destroyed.

Therefore:

```text
Structure Identity ≠ Boundary identity
```

### 5.3 Functional continuity alone is insufficient

Two different systems may perform the same function.

Two countries may provide similar institutions.

Two cakes may satisfy the same recipe.

Therefore:

```text
same function does not imply same Structure
```

### 5.4 Historical continuity matters but does not settle every case

A causal lineage helps connect documents, organisms, runtimes, cakes, and states.

However, one lineage may fork.

A single Trajectory may also contain a Structure transition.

Therefore:

```text
Structure Identity ≠ Trajectory identity
```

### 5.5 Identity judgement is Slice-relative

Different Slices may preserve different identity dimensions.

However, this does not mean that Structure existence is created by Slice.

A safe distinction is:

```text
Structure existence
= not dependent on a particular Slice

Structure Identity judgement
= may be Slice- and Context-relative

Structure Identity itself
= may hold even before or outside current readability
```

---

## 6. Preliminary Identity Criterion

The examples suggest the following candidate characterization:

```text
Two Structure sections may be treated as continuations of the same Structure
when a relevant correspondence preserves enough of the organization,
relations, constraints, history, and establishment possibilities
required by the applicable identity criterion.
```

This is not yet a definition.

The phrase:

```text
preserves enough
```

is deliberately unresolved.

Different Structure types may require different identity invariants.

A tentative schema is:

```text
S_a ≈_{I,c,Σ} S_b
```

where:

- `S_a` and `S_b` are Structure sections;
- `I` is an identity criterion;
- `c` is Context;
- `Σ` is the Slice under which continuity is evaluated;
- `≈` does not yet mean ordinary equality or a proven equivalence relation.

This notation concerns readable identity judgement.

It does not imply that Structure existence depends on `Σ`.

---

## 7. Structure, Slice, Stability, and Trajectory

The cases support the following separation:

```text
Structure
= the mode in which establishment is possible

Slice
= the process that opens a path toward a particular establishment
  and may make identity-relevant relations readable

Stability
= the state in which that opened path becomes readable
  as an establishment that can continue

Trajectory
= the historical or temporal connection of successive Core realizations

Structure Identity
= the question of whether changed Structure sections remain continuations
  of the same Structure
```

Important:

```text
Structure ≠ Trajectory
```

because:

```text
Structure may exist without an actual Slice or actual Trajectory.

A Trajectory may contain multiple Structure sections.

A Trajectory may continue across a Structure transition.

A Structure may participate in multiple Trajectories.
```

---

## 8. Open Questions

1. Does every Structure type require its own identity criterion?
2. Is there a minimum common invariant across all Structure types?
3. Is continuity of establishment possibilities necessary, sufficient, or only supportive?
4. Can identity fork into multiple valid successor Structures?
5. Can identity remain real while no current Slice can read it?
6. How should Jump be distinguished from Structure replacement?
7. Can Stability establish only local identity continuity rather than global identity?
8. Is Structure Identity an equivalence relation, a directed continuity relation, or a family of Context-relative relations?
9. How should national, personal, document, and runtime identity disagreements be represented without reducing them to observer preference?
10. What exactly must be lost before no valid identity-preserving correspondence remains?

---

## 9. Current Position

The current safest position is:

```text
Structure Identity is not material sameness,
not boundary sameness,
not functional sameness,
and not Trajectory itself.
```

Instead, it appears to concern:

```text
continuity of an establishment-bearing organization
under a relevant identity criterion
```

while preserving the stronger principle:

```text
Structure may exist without Slice.

Slice may make Structure and its identity readable,
but does not create Structure existence.
```

No Core change is made in this document.
