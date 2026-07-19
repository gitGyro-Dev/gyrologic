# Daily Log — 2026-07-19

## Topic

Gyro Logic Minimal Formal Model paper: final PDF review, Jxiv compliance review, and English submission.

## Completed

- Completed the final visual review of the English and Japanese PDFs.
- Confirmed Figure 1, Figure 2, and Figure 3 rendering, captions, page layout, and bilingual consistency.
- Confirmed author information, ORCID, correspondence address, conflict-of-interest statement, funding statement, data availability, code and materials availability, and references.
- Prepared Jxiv submission metadata in Japanese and English:
  - title
  - subtitle candidate
  - abstract
  - keywords
  - conflict of interest
  - references
- Revised the Japanese keyword set while preserving Gyro Logic-specific terms where direct translation could reduce conceptual precision.
- Reviewed the Jxiv submission manual, guidelines, and submission rules.
- Confirmed that Jxiv requires authors who use general-purpose AI tools in manuscript preparation to state how they were used and to assume full responsibility for the resulting work.
- Added a bilingual AI-use disclosure generation step to the paper workflow.
- Revised the AI-use statement to identify the actual uses:
  - structural organization
  - drafting assistance
  - language refinement
  - consistency checking
- Revised the responsibility statement to cover:
  - manuscript content
  - theoretical claims
  - citations
  - references
  - final text
- Submitted the English version to Jxiv.

## Submission Status

- Platform: Jxiv
- Language: English
- Status: Screening pending
- Submission date: 2026-07-19
- DOI: Not yet assigned
- Public URL: Not yet available

## Important Note

The PDF initially uploaded to Jxiv was submitted before the Jxiv-compliant AI-use disclosure had been incorporated into the final generated PDF. The corrected manuscript and PDF are being prepared in GitHub. Replacement of the submitted PDF will likely require communication with Jxiv staff during screening.

This does not change the theoretical content of the paper. The correction concerns disclosure and submission compliance.

## GitHub Work

### Paper generation and validation

- Bilingual manuscript assembly
- Pandoc and LuaLaTeX PDF generation
- Figure rendering validation
- Caption duplication validation
- English and Japanese consistency review

### AI-use disclosure

English heading:

```text
Use of Generative AI and AI-Assisted Tools
```

Japanese heading:

```text
生成AI等のAI支援ツールの使用
```

### Current disclosure intent

The manuscript states that generative AI and AI-assisted tools were used for structural organization, drafting assistance, language refinement, and consistency checking. The author reviewed, verified, and edited the content and assumes full responsibility for the work.

## Decisions

- The duplicate display of the author name on the title page is acceptable and will not block submission.
- The English paper will proceed first.
- The Japanese version will be handled after the English submission process becomes clear.
- Jxiv publication metadata must match the PDF metadata.
- CC BY 4.0 will be selected in the Jxiv submission interface.
- Submission status and publication status must be treated as separate states.

## Remaining Work

1. Confirm generation of the corrected English and Japanese PDFs.
2. Review the corrected English PDF.
3. Respond to Jxiv staff if a replacement or correction is requested.
4. Replace the originally submitted PDF with the compliant version.
5. Record the Jxiv screening result.
6. Record the DOI and public URL after publication.
7. Decide the Japanese submission timing and translation-version procedure.
8. Update Hub Dashboard, Weekly, Roadmap, Artifacts, and Links.
9. Prepare publication announcement text after the English version is public.

## Risks and Notes

- Jxiv may request correction before screening proceeds.
- The uploaded file and Jxiv bibliographic fields are published largely as submitted; metadata consistency requires final manual confirmation.
- The Japanese version may fall under Jxiv translation-version requirements if submitted after publication of the English version. Permission and cover requirements must be checked at that time.
- A submission should not be treated as a publication until Jxiv screening is complete and a public DOI or URL is assigned.

## Result

The Minimal Formal Model paper has moved from manuscript preparation into the publication process. The English version has been submitted, the compliance gap has been identified, and the corrected bilingual generation path has been established.

This marks a clear project-cycle boundary:

```text
Formalization
→ manuscript assembly
→ PDF validation
→ Jxiv submission
→ screening and correction coordination
```

## Project Cycle Reflection

The detailed reflection and Hub handoff are recorded in:

```text
project_cycle/2026-07-19_minimal_formal_model_jxiv_submission_reflection.md
```
