#!/usr/bin/env python3
"""Assemble submission-stage bilingual manuscripts for the Minimal Formal Model paper."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
SECTIONS = PAPER / "sections"

AUTHOR_NAME = "Shuntaro Kawakami"
AUTHOR_AFFILIATION_EN = "Independent Researcher"
AUTHOR_AFFILIATION_JP = "Independent Researcher（個人研究者）"
AUTHOR_ORCID = "0009-0004-0091-1303"
AUTHOR_EMAIL = "dev.jxiv@gyro-wedge.com"


@dataclass(frozen=True)
class Config:
    code: str
    title: str
    base: Path
    abstract: Path
    output: Path
    canonical: tuple[str, str, str]


CONFIGS = (
    Config(
        "en",
        "A Minimal Formal Model for Gyro Logic: Local Articulation, Stability Scenes, and Contextual Tracing",
        PAPER / "minimal_formal_model_en.md",
        SECTIONS / "01_abstract_en.md",
        PAPER / "minimal_formal_model_full_en.md",
        (
            "Structure is the mode in which something can be established.",
            "Slice is the process by which a path is opened through a Structure toward an establishment.",
            "Stability is the state in which an opened path becomes readable as an establishment that can continue.",
        ),
    ),
    Config(
        "jp",
        "Gyro Logicの最小形式モデル：局所的表出・Stability Scene・文脈的Tracing",
        PAPER / "minimal_formal_model_jp.md",
        SECTIONS / "01_abstract_jp.md",
        PAPER / "minimal_formal_model_full_jp.md",
        (
            "Structureとは、何かが成立し得る様式である。",
            "Sliceとは、Structureの中に、一つの成立へ向かう道筋が開かれる過程である。",
            "Stabilityとは、開かれた道筋が、一つの成立として継続可能な状態である。",
        ),
    ),
)

SECTION_FILES = (
    "03_structure_{lang}.md",
    "04_slice_{lang}.md",
    "05_stability_{lang}.md",
    "06_incorporated_readability_{lang}.md",
    "07_continuity_identity_{lang}.md",
    "08_contextual_trajectory_{lang}.md",
    "09_difference_boundary_{lang}.md",
    "10_minimal_formal_model_{lang}.md",
    "11_visual_overview_{lang}.md",
    "11_related_work_{lang}.md",
    "11_mathematical_field_comparison_{lang}.md",
    "12_illustrative_examples_{lang}.md",
    "13_limitations_open_problems_{lang}.md",
    "14_conclusion_{lang}.md",
)


def read(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8").strip()


def strip_front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    match = re.match(r"\A---\n.*?\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError("Malformed YAML front matter")
    return text[match.end():].lstrip()


def split_h1(text: str) -> dict[str, str]:
    text = strip_front_matter(text)
    matches = list(re.finditer(r"(?m)^# (.+)$", text))
    result: dict[str, str] = {}
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        result[match.group(1).strip()] = text[match.end():end].strip()
    return result


def remove_h1(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("Section source must begin with an H1 heading")
    return lines[0][2:].strip(), "\n".join(lines[1:]).lstrip()


def number_h2(body: str, chapter: int) -> str:
    n = 1
    out: list[str] = []
    for line in body.splitlines():
        if line.startswith("## "):
            heading = re.sub(r"^##\s+(?:\d+(?:\.\d+)*\s+)?", "", line).strip()
            out.append(f"## {chapter}.{n} {heading}")
            n += 1
        else:
            out.append(line)
    return "\n".join(out)


def normalize(text: str, lang: str) -> str:
    text = text.replace("Stability scene", "Stability Scene")
    text = text.replace("stability scene", "Stability Scene")
    text = text.replace("\\operatorname{StableScene}", "\\operatorname{StabScene}")
    text = text.replace("../figures/", "figures/")
    if lang == "jp":
        text = text.replace("可読性Context", "readability context")
    return text


def front_matter(config: Config) -> str:
    affiliation = AUTHOR_AFFILIATION_EN if config.code == "en" else AUTHOR_AFFILIATION_JP
    return "\n".join(
        (
            "---",
            f'title: "{config.title}"',
            f'author: "{AUTHOR_NAME}"',
            f'affiliation: "{affiliation}"',
            f'orcid: "{AUTHOR_ORCID}"',
            f'corresponding-author: "{AUTHOR_NAME}"',
            f'email: "{AUTHOR_EMAIL}"',
            'date: "2026"',
            'status: "Submission Candidate"',
            'paper_type: "Independent formalization paper"',
            'formal_model: "Minimal Formal Model v1"',
            'canonical_core: "unchanged"',
            'bibliography: "references.bib"',
            'link-citations: true',
            "---",
        )
    )


def author_information(config: Config) -> str:
    if config.code == "en":
        return "\n".join(
            (
                "**Author:** Shuntaro Kawakami  ",
                "**Affiliation:** Independent Researcher  ",
                "**ORCID:** [0009-0004-0091-1303](https://orcid.org/0009-0004-0091-1303)  ",
                "**Correspondence:** [dev.jxiv@gyro-wedge.com](mailto:dev.jxiv@gyro-wedge.com)",
            )
        )
    return "\n".join(
        (
            "**著者:** Shuntaro Kawakami  ",
            "**所属:** Independent Researcher（個人研究者）  ",
            "**ORCID:** [0009-0004-0091-1303](https://orcid.org/0009-0004-0091-1303)  ",
            "**連絡先:** [dev.jxiv@gyro-wedge.com](mailto:dev.jxiv@gyro-wedge.com)",
        )
    )


def assemble(config: Config) -> str:
    abstract_title, abstract_body = remove_h1(read(config.abstract))
    base = split_h1(read(config.base))
    intro = "Introduction"
    constraints = "The Invariant Core and Formalization Constraints" if config.code == "en" else "不変Coreと形式化制約"
    required = (intro, "Contribution Statement", "Research Questions", constraints)
    missing = [name for name in required if name not in base]
    if missing:
        raise ValueError(f"Missing base sections for {config.code}: {missing}")

    parts = [front_matter(config), "", author_information(config), "", f"# {abstract_title}", "", abstract_body]
    parts.extend(
        (
            "",
            f"# 1 {intro}",
            "",
            base[intro],
            "",
            "## 1.1 Contribution Statement",
            "",
            base["Contribution Statement"],
            "",
            "## 1.2 Research Questions",
            "",
            base["Research Questions"],
            "",
            f"# 2 {constraints}",
            "",
            number_h2(base[constraints], 2),
        )
    )

    chapter = 3
    for pattern in SECTION_FILES:
        title, body = remove_h1(read(SECTIONS / pattern.format(lang=config.code)))
        parts.extend(("", f"# {chapter} {title}", "", number_h2(body, chapter)))
        chapter += 1

    parts.extend(("", "# References" if config.code == "en" else "# 参考文献", ""))
    return normalize("\n".join(parts).strip() + "\n", config.code)


def review(config: Config, text: str) -> list[str]:
    findings: list[str] = []
    chapters = [int(n) for n in re.findall(r"(?m)^# (\d+) ", text)]
    expected = list(range(1, 17))
    findings.append("PASS: chapter numbering is continuous from 1 through 16." if chapters == expected else f"FAIL: chapter sequence {chapters}, expected {expected}.")
    for definition in config.canonical:
        findings.append(("PASS" if definition in text else "FAIL") + f": canonical definition: {definition}")
    checks = {
        "bibliography metadata": 'bibliography: "references.bib"',
        "author metadata": f'author: "{AUTHOR_NAME}"',
        "affiliation metadata": "affiliation:",
        "ORCID metadata": f'orcid: "{AUTHOR_ORCID}"',
        "correspondence metadata": f'email: "{AUTHOR_EMAIL}"',
        "Related Work chapter": "Related Work" if config.code == "en" else "Related Workと形式的位置づけ",
        "Figure 1": "fig1_invariant_core.svg",
        "Figure 2": "fig2_local_realization.svg",
        "Figure 3": "fig3_contextual_trajectory.svg",
        "local realization": "g_n=(S_n,B_n,c_n,\\Sigma_n,a_n,K_n)",
        "Incorporated Readability": "\\operatorname{Inc}(g_n)",
        "Continuity Readability": "\\operatorname{CR}",
        "Trajectory": "\\operatorname{Trace}",
        "Difference": "\\Delta_{B,c,\\Sigma}",
    }
    compact = re.sub(r"\s+", "", text)
    for label, token in checks.items():
        haystack = compact if label == "local realization" else text
        needle = re.sub(r"\s+", "", token) if label == "local realization" else token
        findings.append(("PASS" if needle in haystack else "FAIL") + f": {label} present.")
    findings.append("PASS: StabScene constructor normalized." if "StableScene" not in text else "FAIL: StableScene remains.")
    findings.append(f"INFO: {len(text.split())} whitespace-delimited tokens.")
    return findings


def report(results: dict[str, tuple[Config, str, list[str]]]) -> str:
    lines = [
        "# Minimal Formal Model Paper — Submission-stage Consistency Review",
        "",
        "## Scope",
        "",
        "This automated review covers bilingual chapter order, Canonical Definitions, author metadata, bibliography metadata, Related Work, figures, preferred notation, and submission-stage assembly.",
        "",
        "## Author Metadata",
        "",
        f"- Author: {AUTHOR_NAME}",
        f"- Affiliation: {AUTHOR_AFFILIATION_EN}",
        f"- ORCID: {AUTHOR_ORCID}",
        f"- Correspondence: {AUTHOR_EMAIL}",
        "",
        "## Structural Decisions",
        "",
        "- Abstract / 要旨 and References / 参考文献 remain unnumbered.",
        "- Contribution Statement and Research Questions remain Sections 1.1 and 1.2.",
        "- Main chapters are numbered 1–16.",
        "- Chapter 11 provides the visual overview; Chapter 12 provides Related Work and formal positioning.",
        "- Existing mathematical-field comparison, examples, limitations, and conclusion follow without changing their conceptual order.",
        "- Citation processing uses `paper/references.bib` and Pandoc-style citation keys.",
        "- SVG figures are referenced from `paper/figures/`.",
        "",
        "## Results",
    ]
    for code, (config, _text, findings) in results.items():
        lines.extend(("", f"### {'English' if code == 'en' else 'Japanese'}", ""))
        lines.extend(f"- {item}" for item in findings)
    lines.extend(
        (
            "",
            "## Submission Boundary",
            "",
            "The generated manuscripts are submission candidates, not final accepted versions. Remaining human checks include journal-specific metadata, citation style rendering, figure sizing after PDF conversion, and final native-language proofreading.",
        )
    )
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    results: dict[str, tuple[Config, str, list[str]]] = {}
    for config in CONFIGS:
        text = assemble(config)
        config.output.write_text(text, encoding="utf-8")
        findings = review(config, text)
        results[config.code] = (config, text, findings)
    (PAPER / "minimal_formal_model_consistency_review.md").write_text(report(results), encoding="utf-8")
    print("Assembled bilingual submission candidates with author metadata.")


if __name__ == "__main__":
    main()
