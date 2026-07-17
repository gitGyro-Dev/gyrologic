# Minimal Formal Model PDF Figure Review

## Result

```text
PASS
```

The SVG figures fit within the configured A4 text area, use explicit font families, retain readable minimum text sizes, appear in both generated PDFs, and all PDF fonts reported by `pdffonts` are embedded.

## Layout Assumptions

- Paper size: A4 (210 mm wide)
- Left/right margins: 25 mm
- Available text width: 160.0 mm
- Minimum accepted rendered figure font: 8.0 pt

## SVG Size and Font Review

| Figure | Source size | Aspect ratio | PDF width | Estimated PDF height | Minimum rendered font | Explicit SVG fonts |
|---|---:|---:|---:|---:|---:|---|
| Figure 1 | 1200 x 360 | 3.333:1 | 150.4 mm (94%) | 45.1 mm | 8.88 pt | `Noto Sans CJK JP` |
| Figure 2 | 1400 x 620 | 2.258:1 | 153.6 mm (96%) | 68.0 mm | 8.09 pt | `Noto Sans CJK JP`, `Noto Serif CJK JP` |
| Figure 3 | 1400 x 700 | 2.000:1 | 153.6 mm (96%) | 76.8 mm | 8.09 pt | `Noto Sans CJK JP` |

## PDF Placement and Embedded Fonts

### English

- PDF: `paper/pdf/minimal_formal_model_full_en.pdf`
- Total pages: 65
- Figure pages: Figure 1 = page 43, Figure 2 = page 44, Figure 3 = page 45
- Embedded font programs reported: 17
- Font names: `AVAPJL+TeXGyrePagella-Regular`, `CPHUYV+LatinModernMath-Regular`, `DQSSQI+DejaVuSans`, `GBGNAT+DejaVuMathTeXGyre-Regular`, `GVZHTD+LatinModernMath-Regular`, `GWJQAP+MSAM10`, `HTUTBN+TeXGyreHeros-Regular`, `IPIBCK+NotoSansCJKjp-Regular`, `ITGIMR+DejaVuSansMono`, `OJLQTF+NotoSansCJKjp-Regular`, `SSWGJM+NotoSerifCJKjp-Regular`, `TPFSGP+TeXGyrePagella-Bold`, `TUIUYI+DejaVuSans`, `VVEUAL+NotoSansCJKjp-Regular`, `WYMHDN+LatinModernMath-Regular`, `YWZBGJ+TeXGyrePagella-Italic`, `ZFNJQW+TeXGyrePagella-Regular`

### Japanese

- PDF: `paper/pdf/minimal_formal_model_full_jp.pdf`
- Total pages: 60
- Figure pages: Figure 1 = page 41, Figure 2 = page 41, Figure 3 = page 42
- Embedded font programs reported: 19
- Font names: `AVAPJL+TeXGyrePagella-Regular`, `CPHUYV+LatinModernMath-Regular`, `DQSSQI+DejaVuSans`, `GBGNAT+DejaVuMathTeXGyre-Regular`, `GOEBAI+TeXGyrePagella-Bold`, `GWJQAP+MSAM10`, `HNBHJG+LatinModernMath-Regular`, `HTUTBN+TeXGyreHeros-Regular`, `IPIBCK+NotoSansCJKjp-Regular`, `LAYSBM+NotoSerifCJKjp-Bold`, `LJXSHK+TeXGyrePagella-Regular`, `LMGHPT+DejaVuSansMono`, `OJLQTF+NotoSansCJKjp-Regular`, `SSWGJM+NotoSerifCJKjp-Regular`, `TUIUYI+DejaVuSans`, `VVEUAL+NotoSansCJKjp-Regular`, `WMFKGY+NotoSerifCJKjp-Regular`, `WYMHDN+LatinModernMath-Regular`, `YWZBGJ+TeXGyrePagella-Italic`

## Review Boundary

This check verifies deterministic figure sizing, estimated rendered text size, explicit SVG font selection, A4 placement, caption presence, and PDF font embedding. It does not replace a final human visual inspection for aesthetic balance, line weight, or journal-specific figure preferences.
