---
name: resume-builder
description: Professional resume builder and personalizer. Use this skill when the user wants to create a new resume, update their existing one, or tailor a resume for a specific job description (ATS-friendly).
---

# Resume Builder Skill

This skill automates the process of building and personalizing resumes using a master data source and ATS optimization standards.

## Core Workflow

1. **Load Master Data:** Always refer to `references/master_resume.json` as the source of truth for the user's history.
2. **Contextual Analysis:** If a Job Description (JD) is provided:
   - Identify key skills, tools, and responsibilities.
   - Cross-reference with `references/ats_standards.md` for optimization.
3. **Personalization:**
   - Select relevant bullet points from the master resume.
   - Adjust the "Professional Summary" to align with the JD.
   - Inject keywords from the JD into the "Skills" section.
4. **Generate Output:** Use the template in `assets/templates/resume_markdown.md` to produce a clean Markdown resume.

## Commands & Triggers

- **"Create a resume for [Company/Role]"**: Analyzes the JD (if provided) and generates a tailored Markdown resume.
- **"Update my master resume"**: Modifies `references/master_resume.json` with new information provided by the user.
- **"Make my resume ATS-friendly"**: Rewrites the current resume content following the rules in `references/ats_standards.md`.

## Quality Standards
- Use the **Google XYZ Formula** for bullet points whenever possible.
- Ensure the tone is professional, achievement-oriented, and concise.
- Never hallucinate experience not found in the master resume.
