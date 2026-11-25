---
name: cv-tailor
description: Tailor a resume and cover letter to a specific job for ATS keyword match and clear impact, without inventing experience. Use when the user provides a CV and a job description.
---

# CV Tailor

## Inputs
The current CV and the job description. Ask for both if one is missing.

## Workflow
1. Extract keywords from the job description and split them into must-have and nice-to-have.
2. Map each must-have to real evidence in the CV. If there is none, say so; never invent it.
3. Rewrite bullets as action + metric + result. Use only numbers the user gave; ask for missing ones.
4. Use an ATS-safe format: single column, standard headings (Experience, Education, Skills), no tables or graphics.
5. Report: keywords matched, missing, and not applicable, honestly.
6. Cover letter: three short paragraphs: why this company, the strongest evidence, a clear ask.

## Rules
- Keep dates, titles and employers exactly as they are.
- Keep it to one or two pages.
