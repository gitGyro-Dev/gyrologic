# Release Candidate

Project: Gyro Logic  
Version: v3.1  
Date: 2026-07-12  
Status: Draft

---

## Summary

Gyro Logic v3.1 is a Core Definition Refinement release.

This release does not change the invariant Core:

```text
Structure
↓
Slice
↓
Stability
```

It refines how Structure, Slice, and Stability are interpreted within a continuing Trajectory and integrates Boundary / Boundary State under the refined Core definition structure.

The main purpose of this release is to establish a consistent theoretical and document structure across README, docs, and paper while preserving the existing Core order and layer responsibilities.

---

## Purpose

- Refine the formal interpretation of Structure, Slice, and Stability.
- Establish `docs/01_Core_Definitions.md` as the primary Core definition document.
- Integrate Boundary and Boundary State as derivative concepts under the Core definition.
- Create new English and Japanese v3.1 paper drafts without overwriting prior paper versions.
- Prepare the repository for Jxiv, Zenodo, and X publication planning through Gyro Project Cycle.

---

## Major Changes

### Structure

```text
Structure is the mode in which something can be established.
```

```text
Structure は、何かが成立し得る様式である。
```

### Slice

```text
Slice is the process by which a path is opened through a Structure toward an establishment.
```

```text
Slice は、Structure の中に一つの成立へ向かう道筋が開かれる過程である。
```

### Stability

```text
Stability is the state in which the opened path is established and can continue.
```

```text
Stability は、開かれた道筋が一つの成立として現れ、そのまま継続可能な状態である。
```

### Core Interpretation

```text
Structure → Slice → Stability
```

does not describe a static sequence of beginning, middle, and end.

It describes how an establishment emerges within a continuing Trajectory.

Trajectory is not a new Core element. It is a temporal and continuity-oriented interpretation of the invariant Core.

### Boundary Integration

```text
Boundary is a Slice-relative distinction that has become readable through Slice.
```

```text
Boundary State is the provisional relational state of an object
with respect to a Boundary that has become readable through Slice.
```

Boundary and Boundary State are derivative concepts. They are not inserted into the Core sequence as mandatory stages.

---

## Completed

- Core definitions theoretically reviewed and accepted.
- `docs/01_Core_Definitions.md` added.
- `README.md` updated.
- `README_jp.md` updated.
- `docs/15_Boundary_20260610.md` updated.
- `docs/16_Boundary_State_20260610.md` updated.
- `docs/docs_index.md` updated.
- `paper/paper_final_v3_1.md` added.
- `paper/paper_final_jp_v3_1.md` added.
- Boundary / Boundary State consistency review completed.
- Repository document dependency structure clarified.

---

## Remaining

- Final paper review for v3.1.
- Determine whether figures require updates.
- Prepare Jxiv submission package.
- Decide Zenodo archive timing.
- Draft X announcement.
- Finalize GitHub Release title and release notes.
- Confirm whether v3.1 should be released before or after Jxiv submission.
- Obtain final user approval before public release.

---

## GitHub Updates

### Added

```text
docs/01_Core_Definitions.md
paper/paper_final_v3_1.md
paper/paper_final_jp_v3_1.md
release_candidates/gyrologic_v3.1.md
```

### Updated

```text
README.md
README_jp.md
docs/15_Boundary_20260610.md
docs/16_Boundary_State_20260610.md
docs/docs_index.md
```

### Comparison Base

```text
Base: v3.0
Head: main
```

Before adding this Release Candidate document, `main` was 8 commits ahead of `v3.0`.

---

## Papers

### English

```text
paper/paper_final_v3_1.md
```

Status: Draft created.

### Japanese

```text
paper/paper_final_jp_v3_1.md
```

Status: Draft created.

### Paper Positioning

- v3.0: Boundary Extension release.
- v3.1: Core Definition Refinement and Boundary Integration paper version.
- Prior paper versions remain preserved.

---

## Figures

Current status: Review required.

No figure update has been confirmed in this cycle.

Decision required:

- Reuse existing figures.
- Update Core figure only.
- Add a new document dependency figure.
- Defer all figure updates until Jxiv preparation.

---

## Documentation

Primary definition document:

```text
docs/01_Core_Definitions.md
```

Document reference structure:

```text
01 Core Definitions
├── 15 Boundary
└── 16 Boundary State
```

Conceptual dependency:

```text
01 Core Definitions
└── 15 Boundary
    └── 16 Boundary State
```

Boundary and Boundary State are interpreted as derivative documents under the invariant Core.

README, docs, and paper now refer to the same refined definitions.

---

## Repository Structure

```text
README.md
README_jp.md
    │
    ▼
docs/
    ├── 01_Core_Definitions.md
    ├── 15_Boundary_20260610.md
    ├── 16_Boundary_State_20260610.md
    └── docs_index.md
    │
    ▼
paper/
    ├── paper_final_v3_1.md
    └── paper_final_jp_v3_1.md

release_candidates/
    └── gyrologic_v3.1.md
```

Theory dependency:

```text
Core
Structure → Slice → Stability
    │
    ▼
01_Core_Definitions.md
    │
    ├── 15_Boundary_20260610.md
    │       │
    │       └── 16_Boundary_State_20260610.md
    │
    ├── README.md
    ├── README_jp.md
    ├── paper_final_v3_1.md
    └── paper_final_jp_v3_1.md
```

---

## Release Notes

Status: Draft required.

Recommended title:

```text
Gyro Logic v3.1 — Core Definition Refinement
```

Recommended Japanese subtitle:

```text
Core定義の精緻化とBoundary統合
```

Release notes should contain:

- Overview
- Core Definition Refinement
- Structure
- Slice
- Stability
- Core Interpretation
- Boundary Integration
- Documentation Updates
- Paper v3.1
- Compatibility
- Repository Structure
- Next Steps

Required statement:

```text
This release does not change the invariant Core:
Structure → Slice → Stability
```

---

## DOI

Status: Pending decision.

Questions:

- Is a new DOI required for v3.1?
- Should DOI registration follow GitHub Release, Jxiv, or Zenodo publication?
- Should the existing DOI remain the primary citation until v3.1 is archived?

---

## Jxiv

Status: Not started for v3.1.

Required work:

- Finalize English and Japanese paper versions.
- Confirm submission order.
- Prepare title, abstract, keywords, figures, and metadata.
- Decide whether GitHub Release should precede or follow Jxiv submission.

---

## Zenodo

Status: Pending decision.

Options:

- Archive immediately after GitHub Release.
- Archive after Jxiv submission.
- Archive after both English and Japanese Jxiv publications.

---

## X

Status: Not drafted.

Recommended timing:

- After GitHub public release.
- Coordinate with Jxiv publication status.
- Avoid announcing a DOI before it resolves publicly.

---

## Project Cycle Notes

### Dashboard

Update candidate:

```text
Gyro Logic v3.1 — Release Candidate
```

### Weekly

Record:

- Core Definition Refinement completed.
- Boundary Integration completed.
- README / docs updated.
- v3.1 papers created.
- Release Candidate created.

### Roadmap

Suggested status:

```text
v3.1
- Core Definitions: Complete
- README: Complete
- Boundary Integration: Complete
- Paper: Draft
- Figures: Review
- Release Notes: Pending
- Jxiv: Pending
- Zenodo: Pending decision
- X: Pending
```

### Artifacts

Add or update:

```text
docs/01_Core_Definitions.md
docs/15_Boundary_20260610.md
docs/16_Boundary_State_20260610.md
paper/paper_final_v3_1.md
paper/paper_final_jp_v3_1.md
release_candidates/gyrologic_v3.1.md
```

### Links

Add dependency links between:

```text
Core Definitions
→ Boundary
→ Boundary State
→ Paper v3.1
```

---

## Developer Toolkit Reflection

### Automation Candidates

- Compare previous release tag with `main`.
- Generate Release Candidate documents.
- Generate release notes drafts.
- Generate release checklists.
- Validate README / docs / paper definition consistency.
- Validate internal links.
- Visualize repository document dependencies.
- Track Jxiv / Zenodo / X publication state.

### JSON Candidates

```json
{
  "project": "Gyro Logic",
  "release_candidate": "v3.1",
  "release_status": "draft",
  "base_tag": "v3.0",
  "target_branch": "main",
  "release_title": "Gyro Logic v3.1 — Core Definition Refinement",
  "paper_status": "draft",
  "figures_status": "review_required",
  "jxiv_status": "not_started",
  "zenodo_status": "pending_decision",
  "x_announcement_status": "pending",
  "user_approval_required": true
}
```

### CLI Candidates

```text
gyro release diff
gyro release candidate
gyro release draft
gyro release checklist
gyro release validate
```

---

## Checklist

### Repository

- [x] README
- [x] README_jp
- [x] docs
- [x] docs_index
- [x] paper
- [ ] figures
- [ ] examples

### Theory

- [x] Core definitions
- [x] Structure definition
- [x] Slice definition
- [x] Stability definition
- [x] Boundary consistency
- [x] Boundary State consistency
- [x] Layer consistency

### Publication

- [ ] Release Notes
- [ ] DOI decision
- [ ] Jxiv preparation
- [ ] Zenodo decision
- [ ] X announcement
- [ ] Final user approval

### Validation

- [x] Existing Core order preserved
- [x] Trajectory not promoted to a new Core
- [x] Boundary not inserted into the Core sequence
- [x] Boundary State not inserted into the Core sequence
- [x] Existing paper versions preserved
- [ ] Final link validation
- [ ] Final paper review

---

## Layer Consistency Check

### Gyro Logic

Responsible for Core Definition Refinement, Boundary Integration, and theoretical papers.

### GyroOS

No implementation change is included in this Release Candidate.

### GyroAuth

No application-layer change is included in this Release Candidate.

### Gyro Project Cycle

Responsible for release decision, publication order, Dashboard, Weekly, Roadmap, Artifact, and Links management.

### Gyro Developer Toolkit

Responsible for automation, validation, diff generation, checklist generation, and release support.

No management or tooling layer may redefine the Gyro Logic Core.

---

## Recommended Release

- [x] Draft
- [ ] Prerelease
- [ ] Public

Recommendation:

Keep this Release Candidate in **Draft** until the following are decided:

- Figure update requirement
- Jxiv publication order
- Zenodo archive timing
- Final Release Notes
- Final user approval

---

## User Decision Required

- Confirm version `v3.1`.
- Confirm release title.
- Decide whether figures must be updated before release.
- Decide whether Jxiv precedes or follows GitHub Release.
- Decide Zenodo timing.
- Approve Release Notes.
- Approve transition from Draft to Public.

Important:

```text
Do not publish the GitHub Release without explicit user approval.
```
