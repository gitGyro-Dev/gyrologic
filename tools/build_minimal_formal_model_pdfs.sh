#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PAPER_DIR="${ROOT_DIR}/paper"
OUTPUT_DIR="${PAPER_DIR}/pdf"
LATEX_HEADER="${PAPER_DIR}/latex/pandoc_header.tex"

mkdir -p "${OUTPUT_DIR}"
cd "${PAPER_DIR}"

test -s "${LATEX_HEADER}"

COMMON_ARGS=(
  --from=markdown+tex_math_dollars
  --standalone
  --citeproc
  --pdf-engine=lualatex
  --resource-path=".:figures"
  --metadata=bibliography:references.bib
  --include-in-header="${LATEX_HEADER}"
  -V papersize=a4
  -V geometry:margin=25mm
  -V fontsize=11pt
  -V mainfont="TeX Gyre Pagella"
  -V sansfont="TeX Gyre Heros"
  -V monofont="DejaVu Sans Mono"
  -V mathfont="Latin Modern Math"
  -V colorlinks=true
  -V linkcolor=blue
  -V urlcolor=blue
  -V citecolor=blue
)

pandoc \
  minimal_formal_model_full_en.md \
  "${COMMON_ARGS[@]}" \
  -o "${OUTPUT_DIR}/minimal_formal_model_full_en.pdf"

pandoc \
  minimal_formal_model_full_jp.md \
  "${COMMON_ARGS[@]}" \
  -V CJKmainfont="Noto Serif CJK JP" \
  -V CJKsansfont="Noto Sans CJK JP" \
  -V CJKmonofont="Noto Sans Mono CJK JP" \
  -o "${OUTPUT_DIR}/minimal_formal_model_full_jp.pdf"

for pdf in \
  "${OUTPUT_DIR}/minimal_formal_model_full_en.pdf" \
  "${OUTPUT_DIR}/minimal_formal_model_full_jp.pdf"; do
  test -s "${pdf}"
  pdfinfo "${pdf}" | grep -E '^(Pages|Page size):'
  pdftotext "${pdf}" - | head -n 20
  echo "Validated ${pdf}"
done
