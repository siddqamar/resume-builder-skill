# Resume Builder

Reusable resume-building skill for Codex and OpenClaw.

The repository is also packaged as a Codex plugin through `.codex-plugin/plugin.json`.

The standalone skill lives at `skills/resume-builder/`, which keeps it discoverable by skills.sh and compatible with agents that load the shared `SKILL.md` format.

## Install from skills.sh

Install the skill globally for both Codex and OpenClaw:

```bash
npx skills add siddqamar/resume-builder-skill --skill resume-builder -g -a codex -a openclaw -y
```

Install it only for Codex:

```bash
npx skills add siddqamar/resume-builder-skill --skill resume-builder -g -a codex -y
```

Install it only for OpenClaw:

```bash
npx skills add siddqamar/resume-builder-skill --skill resume-builder -g -a openclaw -y
```

Use `--copy` instead of the default symlink behavior when the host does not support symlinks.

The same repository can be installed into a project instead of globally by removing `-g`.

## Codex plugin

The repository root is a valid Codex plugin package.

It contains `.codex-plugin/plugin.json` and points to the bundled skill under `skills/`.

The public Codex plugin directory is a separate publishing channel from skills.sh.

Submit the plugin through the OpenAI plugin submission flow when you want it listed in the universal Codex and ChatGPT plugin directory.

Until then, install the nested skill with the skills.sh CLI or test the plugin from a local Codex marketplace.

## Configure private resume data

The bundled `skills/resume-builder/references/master_resume.json` contains placeholders only.

Do not commit personal contact details or private work history to this public repository.

For a project-local setup, create `references/master_resume.json` in the user's workspace and populate it with the real profile.

The agent should use user-provided resume data first, then workspace-local `references/master_resume.json`, and only then the bundled starter template.

## Dependencies and export

Markdown resume generation has no Python dependency.

PDF and PNG export use the bundled `skills/resume-builder/assets/scripts/convert_resume.py` script.

The preferred runner is `uv`, which reads the script's inline dependency metadata and creates an isolated environment on demand:

```bash
uv run --script skills/resume-builder/assets/scripts/convert_resume.py resume.md pdf
uv run --script skills/resume-builder/assets/scripts/convert_resume.py resume.md png
```

If `uv` is unavailable, use an isolated Python environment and the fallback requirements file:

```bash
python -m venv .resume-builder-venv
.resume-builder-venv/bin/python -m pip install -r skills/resume-builder/requirements.txt
.resume-builder-venv/bin/python skills/resume-builder/assets/scripts/convert_resume.py resume.md pdf
```

On Windows, use `.resume-builder-venv\\Scripts\\python.exe` instead of `.resume-builder-venv/bin/python`.

The agent should create the environment outside the installed skill directory when possible.

The first PDF or PNG export may need network access to download Python packages.

Neither the skill installer nor the plugin installer silently installs Python, `uv`, or packages globally.

## Use

Examples for Codex:

```text
Use $resume-builder to tailor my resume for this job description: ...
Use $resume-builder to generate an ATS-friendly Markdown resume from my career data.
Use $resume-builder to export my resume as PDF.
```

Examples for OpenClaw or other compatible hosts:

```text
Use resume-builder to tailor my resume for this job description: ...
Use resume-builder to make this resume ATS-friendly.
```

The skill reads the source data, applies ATS guidance, generates Markdown, and runs the converter only when PDF or PNG output is requested.

## Publish to skills.sh

skills.sh indexes public GitHub repositories containing valid Agent Skills.

After pushing the repository, validate it with the GitHub CLI:

```bash
gh skill publish --dry-run
```

For the first release, publish an immutable versioned release interactively:

```bash
gh skill publish --tag v0.2.0
```

The command validates the skill, can add the recommended `agent-skills` repository topic, and creates a GitHub release.

After the release and the first install, the skill should be discoverable at a URL similar to:

`https://skills.sh/siddqamar/resume-builder-skill/resume-builder`

Future releases should use a new semantic version tag and be validated before publishing:

```bash
gh skill publish --dry-run
gh skill publish --tag v0.3.0
```

You can also install directly from GitHub before the skills.sh listing refreshes.

## Structure

- `.codex-plugin/plugin.json`: Codex plugin manifest.
- `skills/resume-builder/SKILL.md`: Agent-facing instructions and trigger description.
- `skills/resume-builder/references/master_resume.json`: Placeholder source-data schema.
- `skills/resume-builder/references/ats_standards.md`: ATS and personalization guidance.
- `skills/resume-builder/assets/templates/resume_markdown.md`: Markdown resume template.
- `skills/resume-builder/assets/scripts/convert_resume.py`: Optional PDF/PNG conversion script with inline `uv` dependencies.
- `skills/resume-builder/requirements.txt`: Fallback Python packages for isolated virtualenv setup.

## References

- [Codex skills documentation](https://developers.openai.com/codex/skills).
- [OpenAI plugin packaging documentation](https://developers.openai.com/plugins/build/plugins).
- [skills.sh CLI documentation](https://www.skills.sh/docs/cli).
- [GitHub `gh skill` documentation](https://cli.github.com/manual/gh_skill_publish).
- [OpenClaw skills documentation](https://docs.openclaw.ai/skills).
