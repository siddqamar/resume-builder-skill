---
name: resume-builder
description: Create, update, tailor, and export professional ATS-friendly resumes from structured master resume data. Use when the user asks to generate a resume, personalize a resume for a job description, improve ATS compatibility, update resume source data, or export a resume as Markdown, PDF, or PNG.
---

# Resume Builder Skill

Build and personalize resumes from a structured master data source and ATS optimization standards.

## Core Workflow

1. Load `references/master_resume.json` as the source of truth for the user's history.
2. If a job description is provided:
   - Identify key skills, tools, and responsibilities.
   - Read `references/ats_standards.md` and apply the relevant optimization rules.
3. Personalize the resume:
   - Select relevant bullet points from the master resume.
   - Adjust the professional summary to align with the role.
   - Add relevant job-description keywords to the skills and experience sections only when supported by the master data.
4. Generate a clean Markdown resume using `assets/templates/resume_markdown.md`.
5. If PDF or PNG output is requested, convert the Markdown with `assets/scripts/convert_resume.py`.

## Export Workflow

Do not require the user to pre-install Python packages globally.

When PDF or PNG export is requested:

1. Check whether the runtime can import `markdown_pdf` and `fitz`.
2. If either import is unavailable, create an isolated temporary Python environment in the workspace or agent sandbox.
3. Install `requirements.txt` into that isolated environment.
4. Run `assets/scripts/convert_resume.py <input_md_file> <pdf|png> [output_file]`.
5. Clean up temporary files such as intermediate PDFs. Keep final requested outputs.

## Quality Standards

- Use the Google XYZ formula for bullet points whenever possible.
- Keep the tone professional, achievement-oriented, and concise.
- Never hallucinate experience not found in the master resume.
- Prefer ATS-readable Markdown structure: standard section headings, simple bullets, no tables, no graphics.
- Ask the user before overwriting `references/master_resume.json` when the requested update is ambiguous.
