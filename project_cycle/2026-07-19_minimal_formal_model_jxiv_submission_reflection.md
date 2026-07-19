# Project Cycle Reflection — Minimal Formal Model Jxiv Submission

Date: 2026-07-19
Project: Gyro Logic
Repository: `gitGyro-Dev/gyrologic`

## Current Status

- The English preprint, **A Minimal Formal Model for Gyro Logic: Local Articulation, Stability Scenes, and Contextual Tracing**, was submitted to Jxiv.
- The submission is currently awaiting Jxiv screening.
- The PDF initially submitted does not yet include the revised Jxiv-compliant disclosure concerning the use of generative AI and AI-assisted tools.
- A corrected English manuscript and PDF are being prepared in the repository. Replacement of the submitted file is expected to be coordinated with Jxiv staff during screening.
- The Japanese manuscript has been prepared but has not yet been submitted.
- The bilingual paper generation workflow now inserts the AI-use disclosure before PDF generation.

# 1. Hubへ反映する内容

## Dashboard更新

更新が必要。

Suggested status:

- Gyro Logic / Minimal Formal Model: **English version submitted to Jxiv — screening pending**
- Submission note: **Corrected Jxiv-compliant PDF pending replacement coordination**
- Japanese version: **Prepared, not yet submitted**

## Weeklyへ記録する内容

- Minimal Formal Model英語版をJxivへ投稿。
- 投稿後にJxiv投稿規約・ガイドライン・投稿マニュアルを再確認。
- AI利用について、使用方法と著者責任をプレプリント本文に明記する必要があることを確認。
- 英語版・日本語版の双方に、Jxiv準拠のAI利用声明を生成時に挿入するWorkflowを追加。
- 初回投稿PDFは修正版への差替えが必要になる可能性があり、Jxiv担当者との調整待ち。
- 図1〜3、英日PDF、著者情報、利益相反、研究資金、データ／コード利用可能性を最終確認。

## Roadmap変更

大幅な変更は不要。次の公開工程を明示する。

1. Jxiv screening response
2. Corrected English PDF replacement
3. English version publication and DOI confirmation
4. Japanese version submission decision
5. Hub publication records and links update
6. Release candidate closure and publication release preparation

## Artifact追加

追加が必要。

- English submission candidate PDF
- Corrected English Jxiv-compliant PDF
- Japanese submission candidate PDF
- Minimal Formal Model full English manuscript
- Minimal Formal Model full Japanese manuscript
- PDF figure review report
- Submission-stage consistency review
- Jxiv submission metadata package

Artifact status should distinguish:

- `submitted_original`
- `replacement_candidate`
- `screening_pending`
- `published`

## Links追加

現時点ではJxiv公開URLおよびDOIが未発行のため、公開リンク追加は保留。

Temporary internal links:

- Gyro Logic repository
- English and Japanese PDF paths
- Paper generation workflow
- Jxiv submission tracking note

# 2. Developer Toolkitへ反映する内容

## 新しい自動化候補

### Jxiv compliance validation

PDF生成前に、次の記載を自動検査する。

- title
- author name
- affiliation
- corresponding author and email
- abstract
- keywords
- conflict of interest
- funding
- data availability
- code and materials availability
- AI-use disclosure when applicable
- references

### Submission metadata export

Jxiv入力用に、英語版・日本語版それぞれについて以下をMarkdownまたはJSONで出力する。

- title
- subtitle
- abstract
- keywords
- authors
- affiliations
- corresponding author
- conflict of interest
- references
- license recommendation

### Submission state tracker

`prepared → submitted → screening → correction_requested → replacement_submitted → published`

## 新しいJSON項目

Suggested publication fields:

```json
{
  "submission_platform": "Jxiv",
  "submission_language": "en",
  "submission_status": "screening_pending",
  "submitted_at": "2026-07-19",
  "replacement_required": true,
  "replacement_reason": "Jxiv-compliant AI-use disclosure",
  "replacement_status": "prepared",
  "publication_url": null,
  "doi": null
}
```

Suggested artifact fields:

```json
{
  "compliance_profile": "jxiv-2026",
  "ai_disclosure_present": true,
  "pdf_text_extractable": true,
  "figure_validation": "passed",
  "submission_role": "replacement_candidate"
}
```

## 新しいCLIコマンド

Candidates:

```text
gyro paper validate --profile jxiv
gyro paper metadata --platform jxiv --lang en
gyro publication status set --platform jxiv --status screening_pending
gyro publication replacement prepare --reason ai-disclosure
gyro hub reflect --source gyrologic --date 2026-07-19
```

## Dashboard生成改善案

- `Submitted`と`Published`を分離する。
- `Screening Pending`、`Correction Required`、`Replacement Pending`を可視化する。
- DOI未発行でも投稿済み状態を記録可能にする。
- 原稿版と差替え候補版をArtifact上で明確に区別する。

## その他ツール化できる内容

- Jxiv規約・ガイドラインの要求事項チェックリスト化
- PDFと投稿フォーム用メタデータの一致検査
- 英日メタデータ対応表の生成
- 公開後のDOI、URL、X告知、Hub Links更新の一括処理

# 3. GitHub更新候補

## README

公開前は大幅な更新不要。Jxiv公開後にPublicationセクションへ追加する。

## docs

追加候補:

- `docs/jxiv_submission_compliance.md`
- `docs/publication_workflow.md`
- `docs/ai_assistance_disclosure_policy.md`

## paper

継続対応:

- Jxiv準拠AI利用声明を含む英語版・日本語版PDFの生成
- 英語版差替え候補PDFの最終確認
- 日本語版投稿前確認

## Roadmap

Minimal Formal Modelの次工程を「論文作成」から「投稿・スクリーニング・公開」に更新する。

## Release

Jxiv公開およびDOI確定後に、論文成果物を含むリリース候補を検討する。

# 4. 次回 Gyro Project Cycle で扱う内容

- Jxiv screening結果の記録
- Jxiv担当者との原稿差替え対応
- 差替え版PDFの提出確認
- 英語版公開後のDOI・URL反映
- 日本語版を翻訳版として投稿する場合のJxiv要件確認
- Dashboard、Weekly、Roadmap、Artifacts、Linksの更新
- Xおよび公開告知のタイミング判断
- Minimal Formal Model publication cycleの完了条件定義

# Layer Consistency Check

## Gyro Logic

理論、定義、Minimal Formal Model、論文本文を担当。今回の主成果はGyro Logicの形式化論文であり、責務内にある。

## GyroOS

実装およびRuntime具体化を担当。今回の投稿作業では理論を再定義していない。

## GyroAuth

認証応用を担当。論文中の認証例は例示であり、GyroAuth要件をGyro Logicへ逆流させていない。

## Gyro Project Cycle

投稿状況、公開工程、Dashboard、Weekly、Roadmap、Artifacts、Linksの統合管理を担当する。

## Gyro Developer Toolkit

GitHub Actions、PDF生成、検証、投稿メタデータ生成など、運営支援ツールを担当する。

## Fixed Principles

Core remains unchanged:

```text
Structure
↓
Slice
↓
Stability
```

Layer remains unchanged:

```text
Gyro Logic
↓
GyroOS
↓
GyroAuth
```

Project Cycle and Developer Toolkit do not redefine the theory.
