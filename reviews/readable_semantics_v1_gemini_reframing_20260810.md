# External Review — Readable Semantics v1 Reframing (Gemini)

Date: 2026-08-10
Target: `ideas/readable_semantics_v1.md`
Review type: External critical review / reframing response
Reviewer/service: Gemini
Status: Recorded for analysis; not automatically adopted

## External review

今回の改訂方針の変更は、理論展開として極めて誠実であり、劇的な大転換（コペルニクス的転換）と言えます。

「`Readable` の必要十分条件を厳密な論理式（`PresentTo ∧ LocallyDiscriminable` 等）で定義しようとした試み」そのものが、概念の未成熟な段階における過度な形式化（Over-formalization）という罠にはまっていたことを自覚し、より原点（Operator側による区切り）に立ち戻った判断は100% 正しいと評価します。

## 1. Main positive findings

### 1.1 Continuing event vs local establishment

Gemini strongly endorses the separation between:

```text
continuing event / phenomenon
```

and:

```text
Operator-side local establishment / slice-done unitization
```

The review emphasizes:

```text
slice-done ≠ objective termination of the thing itself
slice-done ≠ global completion of Structure
```

and interprets event-side sharp change as a strong constraint or saliency cue, but not as a uniquely determining boundary.

### 1.2 Retrospective establishment

Gemini also strongly endorses the distinction between:

```text
past event itself
```

and:

```text
present establishment about the past
```

constructed from surviving traces, relations, and current local establishments.

The earthquake example is treated as a useful instance of this separation.

## 2. Open-question responses from Gemini

### Q1/Q2 — can event-side change force one unique boundary?

Gemini's answer:

> Event-side change can strongly constrain or suggest a candidate boundary, but does not uniquely determine the one correct `done` boundary.

Examples mentioned include phase transitions and file-transfer completion.

### Q3 — two Operators choosing different `done` boundaries

Gemini suggests that different boundaries may both be admissible when they remain coherent under each Operator's Orientation / Context.

This suggestion should be treated as provisional because `admissible` and `coherent/sustain` are not yet formalized here.

### Q9 — should `Readable` remain the main term?

Gemini recommends keeping `Readable` only as a secondary explanatory term for now.

Possible future alternatives proposed:

```text
Establishable
Unitizable
slice-done potential
```

These names are suggestions only and are not adopted by this review record.

## 3. Critical assessment of the review

The review is highly supportive, so its positive judgment should not be confused with independent validation.

The most useful parts for continued study are:

1. the separation between continuing event and Operator-side unitization;
2. the interpretation of event-side discontinuity as constraint/saliency rather than unique completion;
3. the distinction between a past event and a present establishment about that past;
4. the recommendation to keep `Readable` secondary and explanatory.

The following statements should **not** be treated as established merely because Gemini endorsed them strongly:

```text
"100% correct"
"fully aligned"
"paper candidate"
```

These are reviewer evaluations, not proofs.

## 4. Current classification

| Finding | Decision | Reason |
|---|---|---|
| Event continuity vs local establishment separation | accept-for-investigation | Strongly consistent with current reframing and examples |
| Event-side sharp change gives saliency, not unique done | accept-for-testing | Plausible, but should still be pressure-tested with strong counterexamples |
| Retrospective establishment distinction | accept-for-investigation | Important and compatible with earthquake example |
| Different Operators may choose different admissible done boundaries | verify | Needs clearer meaning of admissibility and comparison criteria |
| Keep Readable as secondary explanatory term | accept | Matches current reframing |
| Rename to Establishable / Unitizable / slice-done potential | defer | Naming should wait until concept stabilizes |

## 5. Next questions sharpened by this review

The review suggests that the next theory work should focus less on defining `Readable` and more on these questions:

```text
1. What does the Operator actually do when treating a part of continuing change as one local establishment?
2. What event-side changes constrain or bias that unitization?
3. Can two different done boundaries both be valid under different Orientation / Context?
4. What survives after a local establishment so that later Operators can trace back from it?
5. What separates a well-supported retrospective establishment from a merely plausible story?
```

## 6. Review gate status

```text
INTERNAL_REFRAMING_SUPPORTED
```

This does **not** mean the concept is fixed or publication-ready.
It means the reframing itself received a supportive external response and should now be tested with further counterexamples and cross-review.

## 7. Layer consistency

- Gyro Logic theory only: yes
- GyroOS requirements imported: no
- GyroAuth requirements imported: no
- Core changed: no
- `Structure → Slice → Stability` preserved: yes
