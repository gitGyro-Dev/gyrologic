#!/usr/bin/env python3
"""Validate SVG figure sizing and fonts in the generated bilingual PDFs."""

from __future__ import annotations

import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
FIGURES = PAPER / "figures"
PDF_DIR = PAPER / "pdf"
REPORT = PDF_DIR / "minimal_formal_model_figure_review.md"
TEXT_WIDTH_MM = 210.0 - 2 * 25.0
PT_PER_MM = 72.0 / 25.4
MIN_RENDERED_FONT_PT = 8.0


@dataclass(frozen=True)
class FigureSpec:
    number: int
    filename: str
    width_percent: float


SPECS = (
    FigureSpec(1, "fig1_invariant_core.svg", 94.0),
    FigureSpec(2, "fig2_local_realization.svg", 96.0),
    FigureSpec(3, "fig3_contextual_trajectory.svg", 96.0),
)

PDFS = (
    ("English", PDF_DIR / "minimal_formal_model_full_en.pdf"),
    ("Japanese", PDF_DIR / "minimal_formal_model_full_jp.pdf"),
)


def run(*args: str) -> str:
    completed = subprocess.run(
        args,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return completed.stdout


def parse_svg(spec: FigureSpec) -> dict[str, object]:
    path = FIGURES / spec.filename
    root = ET.parse(path).getroot()
    width = float(root.attrib["width"])
    height = float(root.attrib["height"])
    viewbox = [float(value) for value in root.attrib["viewBox"].split()]
    if len(viewbox) != 4 or viewbox[2] <= 0 or viewbox[3] <= 0:
        raise ValueError(f"Invalid viewBox in {path}")

    fonts: set[str] = set()
    font_sizes: list[float] = []
    for element in root.iter():
        family = element.attrib.get("font-family")
        if family:
            fonts.add(family)
        size = element.attrib.get("font-size")
        if size:
            font_sizes.append(float(size))

    if not font_sizes:
        raise ValueError(f"No text font sizes found in {path}")
    if any(family in {"sans-serif", "serif", "monospace"} for family in fonts):
        raise ValueError(f"Generic font family remains in {path}: {sorted(fonts)}")

    target_width_mm = TEXT_WIDTH_MM * spec.width_percent / 100.0
    target_height_mm = target_width_mm * height / width
    scale_pt_per_unit = target_width_mm * PT_PER_MM / width
    min_rendered_font_pt = min(font_sizes) * scale_pt_per_unit

    if target_width_mm > TEXT_WIDTH_MM + 0.01:
        raise ValueError(f"Figure {spec.number} exceeds text width")
    if min_rendered_font_pt < MIN_RENDERED_FONT_PT:
        raise ValueError(
            f"Figure {spec.number} minimum rendered font is too small: "
            f"{min_rendered_font_pt:.2f} pt"
        )

    return {
        "path": path,
        "source_width": width,
        "source_height": height,
        "aspect_ratio": width / height,
        "fonts": sorted(fonts),
        "min_source_font": min(font_sizes),
        "target_width_mm": target_width_mm,
        "target_height_mm": target_height_mm,
        "min_rendered_font_pt": min_rendered_font_pt,
    }


def pdf_page_count(path: Path) -> int:
    info = run("pdfinfo", str(path))
    match = re.search(r"^Pages:\s+(\d+)$", info, flags=re.MULTILINE)
    if not match:
        raise ValueError(f"Could not determine page count for {path}")
    page_size = re.search(r"^Page size:\s+(.+)$", info, flags=re.MULTILINE)
    if not page_size or "A4" not in page_size.group(1):
        raise ValueError(f"PDF is not reported as A4: {path}")
    return int(match.group(1))


def find_figure_pages(path: Path, pages: int) -> dict[int, int]:
    found: dict[int, int] = {}
    for page in range(1, pages + 1):
        text = run(
            "pdftotext",
            "-f",
            str(page),
            "-l",
            str(page),
            "-layout",
            str(path),
            "-",
        )
        for spec in SPECS:
            if spec.number not in found and f"Figure {spec.number}." in text:
                found[spec.number] = page
    missing = [spec.number for spec in SPECS if spec.number not in found]
    if missing:
        raise ValueError(f"Figure captions not found in {path}: {missing}")
    return found


def inspect_fonts(path: Path) -> tuple[list[str], list[str]]:
    output = run("pdffonts", str(path))
    lines = [line.rstrip() for line in output.splitlines() if line.strip()]
    data = lines[2:] if len(lines) >= 2 else []
    font_names: list[str] = []
    failures: list[str] = []
    for line in data:
        columns = line.split()
        if len(columns) < 7:
            continue
        font_names.append(columns[0])
        embedded = columns[4]
        if embedded != "yes":
            failures.append(line)
    if failures:
        raise ValueError(f"Non-embedded PDF fonts in {path}: {failures}")
    return sorted(set(font_names)), lines


def main() -> int:
    figure_data = [(spec, parse_svg(spec)) for spec in SPECS]
    pdf_data = []
    for language, path in PDFS:
        if not path.is_file() or path.stat().st_size == 0:
            raise FileNotFoundError(f"Missing generated PDF: {path}")
        pages = pdf_page_count(path)
        figure_pages = find_figure_pages(path, pages)
        font_names, _font_table = inspect_fonts(path)
        pdf_data.append((language, path, pages, figure_pages, font_names))

    lines = [
        "# Minimal Formal Model PDF Figure Review",
        "",
        "## Result",
        "",
        "```text",
        "PASS",
        "```",
        "",
        "The SVG figures fit within the configured A4 text area, use explicit font families, retain readable minimum text sizes, appear in both generated PDFs, and all PDF fonts reported by `pdffonts` are embedded.",
        "",
        "## Layout Assumptions",
        "",
        "- Paper size: A4 (210 mm wide)",
        "- Left/right margins: 25 mm",
        f"- Available text width: {TEXT_WIDTH_MM:.1f} mm",
        f"- Minimum accepted rendered figure font: {MIN_RENDERED_FONT_PT:.1f} pt",
        "",
        "## SVG Size and Font Review",
        "",
        "| Figure | Source size | Aspect ratio | PDF width | Estimated PDF height | Minimum rendered font | Explicit SVG fonts |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for spec, data in figure_data:
        lines.append(
            f"| Figure {spec.number} | {data['source_width']:.0f} x {data['source_height']:.0f} | "
            f"{data['aspect_ratio']:.3f}:1 | {data['target_width_mm']:.1f} mm ({spec.width_percent:.0f}%) | "
            f"{data['target_height_mm']:.1f} mm | {data['min_rendered_font_pt']:.2f} pt | "
            f"{', '.join(f'`{font}`' for font in data['fonts'])} |"
        )

    lines.extend(["", "## PDF Placement and Embedded Fonts", ""])
    for language, path, pages, figure_pages, font_names in pdf_data:
        lines.extend(
            [
                f"### {language}",
                "",
                f"- PDF: `{path.relative_to(ROOT)}`",
                f"- Total pages: {pages}",
                "- Figure pages: "
                + ", ".join(
                    f"Figure {number} = page {page}"
                    for number, page in sorted(figure_pages.items())
                ),
                f"- Embedded font programs reported: {len(font_names)}",
                "- Font names: " + ", ".join(f"`{name}`" for name in font_names),
                "",
            ]
        )

    lines.extend(
        [
            "## Review Boundary",
            "",
            "This check verifies deterministic figure sizing, estimated rendered text size, explicit SVG font selection, A4 placement, caption presence, and PDF font embedding. It does not replace a final human visual inspection for aesthetic balance, line weight, or journal-specific figure preferences.",
            "",
        ]
    )
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Figure review failed: {exc}", file=sys.stderr)
        raise
