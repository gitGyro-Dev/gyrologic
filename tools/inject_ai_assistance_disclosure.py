#!/usr/bin/env python3
"""Insert the bilingual AI-assistance disclosure into generated manuscripts."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"

TARGETS = {
    PAPER / "minimal_formal_model_full_en.md": {
        "anchor": "## Code and Materials Availability",
        "heading": "## Use of AI-Assisted Tools",
        "body": (
            "AI-assisted tools were used in preparing this manuscript to support structural organization, "
            "drafting, language refinement, and consistency checking. The author reviewed and edited the "
            "content, claims, references, and final manuscript and assumes full responsibility for them."
        ),
    },
    PAPER / "minimal_formal_model_full_jp.md": {
        "anchor": "## コードおよび関連資料の利用可能性",
        "heading": "## AI支援ツールの使用",
        "body": (
            "本稿の作成にあたり、構成整理、草稿作成補助、表現調整、整合性確認のためにAI支援ツールを使用した。"
            "本文の内容、主張、参考文献、最終原稿については著者が確認・編集し、全責任を負う。"
        ),
    },
}


def inject(path: Path, anchor: str, heading: str, body: str) -> None:
    text = path.read_text(encoding="utf-8")
    if heading in text:
        return
    marker = f"\n{anchor}\n"
    if marker not in text:
        raise ValueError(f"Disclosure insertion anchor not found in {path}: {anchor}")
    insertion = f"\n{heading}\n\n{body}\n"
    text = text.replace(marker, insertion + marker, 1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for path, spec in TARGETS.items():
        inject(path, **spec)
        print(f"AI-assistance disclosure present: {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
