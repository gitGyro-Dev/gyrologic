#!/usr/bin/env python3
"""Assemble and review the Gyro Logic Minimal Formal Model paper.

This script combines the bilingual chapter sources under paper/sections with the
shared introductory drafts, normalizes chapter numbering and selected notation,
and writes both integrated manuscripts and a consistency-review report.

It uses only the Python standard library.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
SECTIONS = PAPER / "sections"


@dataclass(frozen=True)
class LanguageConfig:
    code: str
    title: str
    base_file: Path
    abstract_file: Path
    output_file: Path
    section_suffix: str
    canonical_definitions: tuple[str, ...]


CONFIGS = (
    LanguageConfig(
        code="en",
        title=(
            "A Minimal Formal Model for Gyro Logic: "
            "Local Articulation, Stability Scenes, and Contextual Tracing"
        ),
        base_file=PAPER / "minimal_formal_model_en.md",
        abstract_file=SECTIONS / "01_abstract_en.md",
        output_file=PAPER / "minimal_formal_model_full_en.md",
        section_suffix="en",
        canonical_definitions=(
            "Structure is the mode in which something can be established.",
            "Slice is the process by which a path is opened through a Structure toward an establishment.",
            "Stability is the state in which an opened path becomes readable as an establishment that can continue.",
        ),
    ),
    LanguageConfig(
        code="jp",
        title=(
            "Gyro Logicの最小形式モデル："
            "局所的表出・Stability Scene・文脈的Tracing"
        ),
        base_file=PAPER / "minimal_formal_model_jp.md",
        abstract_file=SECTIONS / "01_abstract_jp.md",
        output_file=PAPER / "minimal_formal_model_full_jp.md",
        section_suffix="jp",
        canonical_definitions=(
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
    "11_mathematical_field_comparison_{lang}.md",
    "12_illustrative_examples_{lang}.md",
    "13_limitations_open_problems_{lang}.md",
    "14_conclusion_{lang}.md",
)

CHAPTER_START = 3


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Required source file does not exist: {path}")
    return path.read_text(encoding="utf-8").strip()


def strip_front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    match = re.match(r"\A---\n.*?\n---\n", text, flags=re.DOTALL)
    if not match:
        raise ValueError("Malformed YAML front matter")
    return text[match.end() :].lstrip()


def remove_first_heading(text: str) -> tuple[str, str]:
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("Section source must start with one level-one heading")
    title = lines[0][2:].strip()
    return title, "\n".join(lines[1:]).lstrip()


def number_subheadings(body: str, chapter: int, start_index: int = 1) -> str:
    index = start_index
    out: list[str] = []
    for line in body.splitlines():
        if line.startswith("## "):
            heading = re.sub(r"^##\s+(?:\d+(?:\.\d+)*\s+)?", "", line).strip()
            out.append(f"## {chapter}.{index} {heading}")
            index += 1
        else:
            out.append(line)
    return "\n".join(out)


def split_base_sections(text: str) -> dict[str, str]:
    """Split the shared draft into its four top-level source sections."""
    body = strip_front_matter(text)
    matches = list(re.finditer(r"(?m)^# (.+)$", body))
    result: dict[str, str] = {}
    for pos, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[pos + 1].start() if pos + 1 < len(matches) else len(body)
        result[title] = body[start:end].strip()
    return result


def normalize_terms(text: str, lang: str) -> str:
    text = text.replace("Stability scene", "Stability Scene")
    text = text.replace("stability scene", "Stability Scene")
    text = text.replace("\\operatorname{StableScene}", "\\operatorname{StabScene}")

    text = text.replace("Incorporated Readability Context", "readability context")
    if lang == "jp":
        text = text.replace("可読性Context", "readability context")

    compact_pattern = re.compile(
        r"\\operatorname\{CR\}\(g_i,g_j\)\s*\\iff\s*"
        r"\\exists r:\s*"
        r"\\operatorname\{Adm\}\(r\)\s*\\land\s*"
        r"\\operatorname\{Traceable\}\(r\)\s*\\land\s*"
        r"\\operatorname\{Readable\}\(r\)",
        flags=re.DOTALL,
    )
    full_formula = (
        r"\\operatorname{CR}(g_i,g_j;B,c,\\Sigma,\\Gamma)"
        "\n\\iff\n"
        r"\\exists r\,\\Bigl("
        "\n"
        r"\\operatorname{Adm}(r;B,c,\\Sigma,\\Gamma)"
        "\n\\land\n"
        r"\\operatorname{Traceable}(g_i,g_j;r)"
        "\n\\land\n"
        r"\\operatorname{Readable}(r;B,c,\\Sigma,\\Gamma)"
        "\n"
        r"\\Bigr)"
    )
    text = compact_pattern.sub(full_formula, text)
    return text


def build_front_matter(config: LanguageConfig) -> str:
    return (
        "---\n"
        f'title: "{config.title}"\n'
        'author: "Gyro Logic Lab"\n'
        'date: "2026"\n'
        'status: "Integrated Draft"\n'
        'paper_type: "Independent formalization paper"\n'
        'formal_model: "Minimal Formal Model v1"\n'
        'canonical_core: "unchanged"\n'
        "---"
    )


def build_manuscript(config: LanguageConfig) -> str:
    abstract_title, abstract_body = remove_first_heading(read_text(config.abstract_file))
    base_sections = split_base_sections(read_text(config.base_file))

    required_base = (
        "Introduction",
        "Contribution Statement",
        "Research Questions",
        "The Invariant Core and Formalization Constraints"
        if config.code == "en"
        else "不変Coreと形式化制約",
    )
    missing = [name for name in required_base if name not in base_sections]
    if missing:
        raise ValueError(f"Missing base sections for {config.code}: {missing}")

    parts: list[str] = [build_front_matter(config), "", f"# {abstract_title}", "", abstract_body]

    intro_title = required_base[0]
    intro_body = base_sections[intro_title]
    contribution_body = base_sections[required_base[1]]
    rq_body = base_sections[required_base[2]]
    constraints_body = base_sections[required_base[3]]

    parts.extend(
        [
            "",
            f"# 1 {intro_title}",
            "",
            intro_body,
            "",
            "## 1.1 Contribution Statement",
            "",
            contribution_body,
            "",
            "## 1.2 Research Questions",
            "",
            rq_body,
            "",
            f"# 2 {required_base[3]}",
            "",
            number_subheadings(constraints_body, 2),
        ]
    )

    chapter = CHAPTER_START
    for pattern in SECTION_FILES:
        path = SECTIONS / pattern.format(lang=config.section_suffix)
        title, body = remove_first_heading(read_text(path))
        parts.extend(["", f"# {chapter} {title}", "", number_subheadings(body, chapter)])
        chapter += 1

    manuscript = "\n".join(parts).strip() + "\n"
    return normalize_terms(manuscript, config.code)


def count_pattern(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, flags=re.MULTILINE))


def review_manuscript(config: LanguageConfig, text: str) -> list[str]:
    findings: list[str] = []

    chapter_numbers = [int(x) for x in re.findall(r"(?m)^# (\d+) ", text)]
    expected = list(range(1, 15))
    if chapter_numbers != expected:
        findings.append(f"FAIL: chapter sequence is {chapter_numbers}; expected {expected}.")
    else:
        findings.append("PASS: chapter numbering is continuous from 1 through 14.")

    for definition in config.canonical_definitions:
        if definition in text:
            findings.append(f"PASS: canonical definition preserved: {definition}")
        else:
            findings.append(f"FAIL: canonical definition missing or altered: {definition}")

    required_terms = (
        "local articulation",
        "Stability Scene",
        "Incorporated Readability",
        "Continuity Readability",
        "Trajectory",
        "Difference",
        "Boundary",
    )
    for term in required_terms:
        if term in text:
            findings.append(f"PASS: term present: {term}")
        else:
            findings.append(f"FAIL: required term absent: {term}")

    if "StableScene" in text:
        findings.append("FAIL: non-canonical constructor StableScene remains.")
    else:
        findings.append("PASS: Stability constructor normalized to StabScene.")

    required_formulas = (
        r"g_n\s*=.{0,180}S_n",
        r"\\xRightarrow\{\\Sigma_\{B_n,c_n\}\}",
        r"\\operatorname\{Inc\}\(g_n\)",
        r"\\operatorname\{Update\}_\{\\Gamma\}",
        r"\\operatorname\{CR\}",
        r"\\mathcal\{G\}_R\s*=\s*\(G,E\)",
        r"\\operatorname\{Trace\}",
        r"\\Delta_\{B,c,\\Sigma\}",
    )
    for formula in required_formulas:
        if re.search(formula, text, flags=re.DOTALL):
            findings.append(f"PASS: formula family present: `{formula}`")
        else:
            findings.append(f"FAIL: formula family absent: `{formula}`")

    top_headings = count_pattern(text, r"^# ")
    findings.append(f"INFO: top-level headings including Abstract/要旨: {top_headings}.")
    findings.append(f"INFO: manuscript length: {len(text.split())} whitespace-delimited tokens.")
    return findings


def build_review_report(results: dict[str, tuple[LanguageConfig, str, list[str]]]) -> str:
    lines = [
        "# Minimal Formal Model Paper — Cross-document Consistency Review",
        "",
        "## Review Scope",
        "",
        "The review covers chapter order, heading numbering, canonical definitions, terminology, notation, bilingual structure, and the distinction between full and compact formulas.",
        "",
        "## Normalization Decisions",
        "",
        "- The Abstract / 要旨 remains unnumbered.",
        "- Contribution Statement and Research Questions are integrated as Sections 1.1 and 1.2 of the Introduction.",
        "- Main chapters are numbered 1–14.",
        "- `Stability Scene` is the preferred paper term; `StabScene` is the preferred constructor.",
        "- `Context` represented by `c` is kept distinct from the incorporated-readability context represented by `Γ`.",
        "- The full Continuity Readability formula retains `g_i`, `g_j`, `B`, `c`, `Σ`, and `Γ`; compact forms are explanatory abbreviations only.",
        "- `Difference` remains weakly typed as a partial heterogeneous mapping; pairwise forms are specializations rather than a second universal type.",
        "- Boundary remains a derivative supporting characterization and is not promoted into the invariant Core.",
        "",
        "## Results",
    ]
    for code, (config, _text, findings) in results.items():
        label = "English" if code == "en" else "Japanese"
        lines.extend(["", f"### {label}", ""])
        lines.extend(f"- {item}" for item in findings)

    lines.extend(
        [
            "",
            "## Review Conclusion",
            "",
            "The integrated manuscripts preserve the invariant Core and the intended conceptual separations. The assembly process normalizes chapter structure and notation without replacing the canonical definitions. Remaining work before submission includes citation insertion, bibliography construction, figure preparation, external mathematical review, and a final language edit.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    results: dict[str, tuple[LanguageConfig, str, list[str]]] = {}
    for config in CONFIGS:
        manuscript = build_manuscript(config)
        findings = review_manuscript(config, manuscript)
        failures = [item for item in findings if item.startswith("FAIL:")]
        if failures:
            raise RuntimeError(
                f"Consistency review failed for {config.code}:\n" + "\n".join(failures)
            )
        config.output_file.write_text(manuscript, encoding="utf-8")
        results[config.code] = (config, manuscript, findings)

    report = build_review_report(results)
    (PAPER / "minimal_formal_model_consistency_review.md").write_text(report, encoding="utf-8")

    for config in CONFIGS:
        print(config.output_file.relative_to(ROOT))
    print((PAPER / "minimal_formal_model_consistency_review.md").relative_to(ROOT))


if __name__ == "__main__":
    main()
