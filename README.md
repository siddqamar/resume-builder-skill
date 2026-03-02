# 📄 Resume Builder Skill for Gemini CLI

A specialized agent skill for **Gemini CLI** that automates building, updating, and personalizing resumes. It uses a master JSON data source and applies ATS (Applicant Tracking System) optimization standards to tailor your resume for specific job descriptions.

---

## 🚀 Installation Guide

If you have cloned this repository, follow these steps to enable the skill in your Gemini CLI environment.

### 1. Global Installation (Recommended)
This makes the skill available in **any** terminal window or project.

**Option A: Manual Folder Copy (Most Reliable on Windows)**
Copy the `resume-builder` folder to your global agents directory:
```powershell
# Windows (PowerShell)
xcopy /E /I /H /Y .esume-builder "$HOME\.agents\skillsesume-builder"
```

**Option B: Package Installation**
If you have a `.skill` file:
```bash
gemini skills install resume-builder.skill --scope user
```

### 2. Workspace Installation
Use this if you only want the skill available within a specific project folder.
```bash
# From your project root
gemini skills install path/to/resume-builder.skill --scope workspace
```

### 3. Activate the Skill
After installation, you **must** reload your Gemini CLI session:
```bash
/skills reload
```
Verify it is active by running `/skills list`.

---

## 🛠️ Configuration

### Master Resume
Update `references/master_resume.json` with your personal information, experience, and skills. This serves as the "Source of Truth" for the agent.

### ATS Standards
The logic for keyword optimization and formatting is stored in `references/ats_standards.md`. You can modify this to match specific industry standards.

---

## 🤖 How to Use

Once active, you can trigger the skill using natural language:

- **Tailor for a Job:** 
  > "@resume-builder personalize my resume for this Job Description: [Paste JD here]"
- **Update Experience:**
  > "@resume-builder add my new role as Senior Developer at Google to my master resume."
- **Generate Markdown:**
  > "@resume-builder generate a clean markdown resume from my master data."

---

## 📂 Project Structure
- `SKILL.md`: Core instructions and triggers for the agent.
- `references/`: Contains `master_resume.json` and `ats_standards.md`.
- `assets/templates/`: Contains the `resume_markdown.md` structure.
