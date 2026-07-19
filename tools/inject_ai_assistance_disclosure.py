#!/usr/bin/env python3
"""Insert Jxiv-compliant bilingual AI-use disclosures into generated manuscripts."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"

TARGETS = {
    PAPER / "minimal_formal_model_full_en.md": {
        "anchor": "## Code and Materials Availability",
        "heading": "## Use of Generative AI and AI-Assisted Tools",
        "body": (
            "Generative AI and other AI-assisted tools were used in preparing this manuscript for "
            "structural organization, drafting assistance, language refinement, and consistency checking. "
            "The author reviewed, verified, and edited the manuscript content, theoretical claims, citations, "
            "references, and final text, and assumes full responsibility for all aspects of the work."
        ),
    },
    PAPER / "minimal_formal_model_full_jp.md": {
        "anchor": "## コードおよび関連資料の利用可能性",
        "heading": "## 生成AI等のAI支援ツールの使用",
        "body": (
            "本稿の作成にあたり、構成整理、草稿作成補助、表現調整、整合性確認のために、生成AIを含むAI支援ツールを使用した。"
            "本文の内容、理論的主張、引用、参考文献および最終原稿については、著者が確認、検証および編集を行い、"
            "本研究のすべての内容について全責任を負う。"
        ),
    },
}


def inject(path: Path, anchor: str, heading: str, body: str) -> None:
    text = path.read_text(encoding="utf-8")

    # Remove an earlier disclosure version before inserting the current
    # Jxiv-aligned statement. This keeps regeneration idempotent across revisions.
    old_sections = (
        "## Use of AI-Assisted Tools",
        "## Use of Generative AI and AI-Assisted Tools",
        "## AI支援ツールの使用",
        "## 生成AI等のAI支援ツールの使用",
    )
    for old_heading in old_sections:
        marker = f"\n{old_heading}\n\n"
        if marker not in text:
            continue
        start = text.index(marker)
        next_heading = text.find("\n## ", start + len(marker))
        if next_heading == -1:
            raise ValueError(f"Unable to locate end of disclosure section in {path}")
        text = text[:start] + text[next_heading:]

    marker = f"\n{anchor}\n"
    if marker not in text:
        raise ValueError(f"Disclosure insertion anchor not found in {path}: {anchor}")

    insertion = f"\n{heading}\n\n{body}\n"
    text = text.replace(marker, insertion + marker, 1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for path, spec in TARGETS.items():
        inject(path, **spec)
        print(f"Jxiv AI-use disclosure present: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
