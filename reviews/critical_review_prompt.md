# External Critical Review Prompt

Use this prompt when asking Claude, Gemini, or another external AI system to review a Gyro Logic working note.

## Japanese

```text
この文書は確定理論ではなく、理論化前の検討メモです。
以下を重点的に講評してください。

1. 論理的矛盾
2. 定義が曖昧な箇所
3. 既存理論との重複・相違
4. 反例・反証可能性
5. 過剰一般化
6. 次に検証すべき具体例
7. 現時点で固定してよい点／まだ固定しない方がよい点

過度に好意的に解釈せず、批判的にレビューしてください。

追加ルール：
- 文書に書かれている内容と、あなた自身の推測・一般知識・外部知識を区別してください。
- 事実確認が必要な指摘（引用文献の欠落、既存理論との一致、公開日、定義の有無など）は、確認できた事実と推測を分けてください。
- 「問題がある」と指摘する場合は、可能であれば該当箇所と理由を示してください。
- 反例を提示する場合は、その反例がどの定義・命題を破るのかを明示してください。
- 理論を完成させるための提案より先に、現在のメモがどこまで成立しているかを評価してください。
```

## English

```text
This document is not a finalized theory. It is an exploratory note prior to formal theory construction.
Please review it critically, focusing on the following points:

1. Logical contradictions
2. Ambiguous or underspecified definitions
3. Overlap with and differences from existing theories
4. Counterexamples and falsifiability
5. Overgeneralization
6. Concrete examples that should be tested next
7. Points that may be fixed now versus points that should remain provisional

Do not interpret the document overly favorably. Review it critically.

Additional rules:
- Distinguish what is actually stated in the document from your own inference, general knowledge, or external knowledge.
- For factual criticisms that require verification, such as missing references, overlap with prior theories, publication dates, or whether a definition is present, separate verified facts from inference.
- When identifying a problem, cite or identify the relevant passage and explain why it is problematic whenever possible.
- When proposing a counterexample, state explicitly which definition, claim, or proposition the counterexample challenges.
- Before proposing ways to complete the theory, first evaluate how far the current note is actually justified.
```

## Usage

Append one of the following after the prompt:

```text
Review target:
<public GitHub URL>
```

or paste the full note beneath:

```text
Review target begins below.
---
<document body>
---
```

For comparison quality, use the same target revision and substantially the same prompt for each reviewer.
