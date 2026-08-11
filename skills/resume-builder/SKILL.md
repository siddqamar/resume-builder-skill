---
name: resume-builder
description: Create, update, tailor, and export professional ATS-friendly resumes from structured career data. Use when the user asks to generate a resume, personalize a resume for a job description, improve ATS compatibility, update resume source data, or export a resume as Markdown, PDF, or PNG.
license: MIT
---

# Resume Builder Skill

Build and personalize resumes from structured career data and ATS optimization standards.

## Core workflow

1. Identify the user's source data.
   - Use a user-provided resume, profile, or structured JSON when available.
   - Otherwise check the user's workspace for `references/master_resume.json` or `master_resume.json`.
   - Otherwise read `references/master_resume.json` from this skill directory.
   - Treat the bundled file as a starter template until the user replaces its placeholders with their own data.
   - Never expose or commit private contact details from a user's working copy to a public repository.
2. If a job description is provided:
   - Identify relevant skills, tools, responsibilities, and keywords.
   - Read `references/ats_standards.md` and apply the relevant optimization rules.
3. Personalize the resume:
   - Select relevant evidence from the source data.
   - Adjust the professional summary to align with the role.
   - Add job-description keywords only when supported by the source data.
   - Do not invent experience, metrics, employers, dates, education, or skills.
4. Generate a clean Markdown resume using `assets/templates/resume_markdown.md`.
5. Preserve the user's requested output location and ask before overwriting an existing file when the request is ambiguous.

## Export workflow

Markdown generation does not require Python.

PDF and PNG export use `assets/scripts/convert_resume.py` and install dependencies only when export is requested.

1. Resolve the absolute path to this skill directory from the location of `SKILL.md`.
2. Prefer `uv` when it is available:
   ```text
   uv run --script <skill-dir>/assets/scripts/convert_resume.py <input.md> <pdf|png> [output]
   ```
   The script declares its Python dependencies inline, so `uv` creates or reuses an isolated environment without modifying global packages.
3. If `uv` is unavailable, use an isolated virtual environment outside the installed skill files:
   - Create it with `python -m venv`, `python3 -m venv`, or `py -m venv`, depending on the host.
   - Install `<skill-dir>/requirements.txt` into that environment.
   - Run the converter with that environment's Python executable.
4. If neither `uv` nor Python is available, explain the missing prerequisite and provide the host's official installation guidance.
5. Do not install packages globally and do not silently install system runtimes.
6. Keep temporary environments and intermediate PDFs outside the skill directory when possible.
7. Keep the requested final PDF or PNG and report its exact path.

PNG export renders the first PDF page.

## Quality standards

- Use the Google XYZ formula for bullet points whenever possible.
- Keep the tone professional, achievement-oriented, and concise.
- Prefer ATS-readable Markdown structure: standard section headings, simple bullets, no tables, and no graphics.
- Use `references/ats_standards.md` for detailed ATS guidance instead of duplicating it here.
- Ask before changing a user's source data when the requested update is ambiguous.
