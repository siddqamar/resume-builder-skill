# Resume Builder Skill

Reusable agent skill for building, updating, tailoring, and exporting ATS-friendly resumes. The skill is platform-neutral: it is designed for SKILL.md-compatible agents such as Codex, Antigravity, and OpenClaw rather than being tied to the discontinued Gemini CLI.

The skill uses `references/master_resume.json` as the source of truth, `references/ats_standards.md` for resume optimization rules, `assets/templates/resume_markdown.md` for Markdown output, and `assets/scripts/convert_resume.py` for optional PDF/PNG export.

## Install

Install directly from GitHub:

```bash
npx skills add https://github.com/siddqamar/resume-builder-skill
```

You can also copy this folder as `resume-builder` into the skills directory used by your agent.

### Codex

Use the shared installer:

```bash
npx skills add https://github.com/siddqamar/resume-builder-skill
```

For a manual global install, copy the folder into the Codex skills directory:

```powershell
Copy-Item -Recurse -Force . "$HOME\.codex\skills\resume-builder"
```

Or keep it workspace-local by copying the folder into the current project's skill/plugin area if your Codex setup loads workspace skills.

### Antigravity

Use the shared installer when Antigravity is configured to read installed skills:

```bash
npx skills add https://github.com/siddqamar/resume-builder-skill
```

For a manual install, add this folder to Antigravity as a local custom skill. Use the app's configured skills directory or workspace skills directory, then reload skills from Antigravity so it can discover `SKILL.md`.

### OpenClaw

Use the shared installer when OpenClaw is configured to read installed skills:

```bash
npx skills add https://github.com/siddqamar/resume-builder-skill
```

For a manual install, add this folder to OpenClaw as a local skill. Prefer a local audited install over marketplace redistribution because skills can include executable scripts. Reload or rescan skills after copying the folder so OpenClaw can discover `SKILL.md`.

## Dependencies

There is no separate user setup step for normal Markdown resume generation.

PDF and PNG export use the bundled Python script at `assets/scripts/convert_resume.py`. When export is requested, the agent should run the script from the skill folder and, if needed, create an isolated temporary Python environment and install `requirements.txt` there. Do not require users to pre-run `pip install` globally.

Example agent execution pattern:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python assets\scripts\convert_resume.py resume.md pdf
```

Agents may adapt the environment path for their own sandbox or temporary directory.

## Configure

Update `references/master_resume.json` with the user's real profile, work history, education, skills, and contact information. Treat it as the source of truth and do not invent experience that is not present there.

Update `references/ats_standards.md` only when the resume strategy or ATS formatting rules need to change.

## Use

Trigger the skill with natural language in any supported agent:

- `Use resume-builder to tailor my resume for this job description: ...`
- `Use resume-builder to generate a clean Markdown resume from my master data.`
- `Use resume-builder to export my resume as PDF.`
- `Use resume-builder to update my master resume with this new role: ...`
- `Use resume-builder to make this resume ATS-friendly.`

Expected workflow:

1. Read `references/master_resume.json`.
2. If a job description is provided, compare it with the master data and `references/ats_standards.md`.
3. Generate a concise ATS-friendly Markdown resume using `assets/templates/resume_markdown.md`.
4. Use `assets/scripts/convert_resume.py` only when PDF or PNG output is requested.

## Structure

- `SKILL.md`: Agent-facing instructions and trigger description.
- `references/master_resume.json`: Source resume data.
- `references/ats_standards.md`: ATS and personalization guidance.
- `assets/templates/resume_markdown.md`: Markdown resume template.
- `assets/scripts/convert_resume.py`: Optional PDF/PNG conversion script.
- `requirements.txt`: Python packages needed only for PDF/PNG export.
