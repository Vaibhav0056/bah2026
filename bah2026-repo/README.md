# 🚀 Bharatiya Antariksh Hackathon 2026

> **Event:** [Bharatiya Antariksh Hackathon 2026 by ISRO × Hack2Skill](https://hack2skill.com/event/bah2026/)

---

## 📌 Problem Statement

---

## 🗂️ Folder Structure

```
bah2026/
│
├── data/
│   ├── raw/            # Original, unmodified datasets (don't edit these)
│   ├── processed/      # Cleaned and preprocessed data
│   └── sample/         # Small sample files for quick testing
│
├── notebooks/          # Jupyter notebooks for exploration & experiments
│   └── 01_eda.ipynb    # Example: Exploratory Data Analysis
│
├── src/                # Source code (reusable Python scripts)
│   ├── preprocessing/  # Data loading, cleaning, feature engineering
│   ├── models/         # Model definitions and training scripts
│   └── utils/          # Helper functions used across the project
│
├── outputs/
│   ├── predictions/    # Model outputs and result files
│   └── visualizations/ # Charts, plots, and figures
│
├── docs/               # Documentation, references, research papers
├── tests/              # Unit tests for your code
├── scripts/            # One-off scripts (setup, download data, etc.)
│
├── .gitignore          # Files Git should ignore
├── requirements.txt    # Python dependencies
└── README.md           # You are here!
```

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Vaibhav0056/bah2026.git
cd bah2026
```

### 2. Create a Virtual Environment

```bash
# Create
python -m venv venv

# Activate (Mac/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Then open any notebook from the `notebooks/` folder.

---

## 🤝 Team Collaboration Guide (Read Before You Touch Anything!)

### ⚡ Golden Rules

1. **NEVER push directly to `main`**
2. **ALWAYS pull before you start working**
3. **ALWAYS work on your own branch**
4. **ALWAYS write a clear commit message**

---

### 🌿 Branch Structure

```
main        → final, working code only (no direct pushes)
dev         → combines everyone's work (merge here first)
your-name   → your personal working branch
```

---

### 🚀 Daily Workflow (Follow This Every Day)

#### 1. Before Starting Work — Always Pull First
```bash
git checkout dev          # switch to dev branch
git pull origin dev       # get latest changes from teammates
```

#### 2. Switch to Your Own Branch
```bash
git checkout your-name    # e.g. git checkout vaibhav
```
> First time only — create your branch:
> ```bash
> git checkout -b your-name
> ```

#### 3. Make Your Changes
Edit files, write code, add notebooks — do your work.

#### 4. Save & Push Your Work
```bash
git add .
git commit -m "feat: describe what you did"
git push origin your-name
```

#### 5. Merge Into Dev (When Your Work is Ready)
```bash
git checkout dev
git pull origin dev                  # pull latest dev again
git merge your-name                  # merge your branch into dev
git push origin dev                  # push merged dev to GitHub
git checkout your-name               # go back to your branch
```

---

### 🔁 End of Day Checklist

- [ ] Pushed your branch to GitHub
- [ ] Merged into `dev` if feature is complete
- [ ] Told teammates in the group chat what you changed

---

### ⚔️ How to Handle Merge Conflicts

A conflict happens when two people edit the **same line** of the same file.

Git will mark the conflict in the file like this:
```
<<<<<<< your-name
your version of the line
=======
teammate's version of the line
>>>>>>> dev
```

**To fix it:**
1. Open the file — find all `<<<<<<<` markers
2. Decide which version to keep (or combine both)
3. Delete the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
4. Save the file, then:
```bash
git add .
git commit -m "fix: resolved merge conflict in filename"
git push origin your-name
```

> 💡 **Best way to avoid conflicts:** Always pull before starting, and don't
> edit the same file as a teammate at the same time.

---

### 🚫 Never Do These

```bash
git push origin main        # ❌ never push directly to main
git push --force            # ❌ never force push (destroys teammates' work)
git commit -m "changes"     # ❌ never write vague commit messages
```

### ✅ Always Do These

```bash
git pull origin dev         # ✅ pull before starting
git status                  # ✅ check what files changed before committing
git log --oneline           # ✅ see recent commits
```

---

### 📋 Commit Message Format

```
type: short description of what you did
```

| Type | When to use |
|------|-------------|
| `feat:` | Added something new |
| `fix:` | Fixed a bug |
| `docs:` | Updated README or docs |
| `data:` | Added or changed data files |
| `refactor:` | Cleaned up code |
| `test:` | Added tests |

**Examples:**
```bash
git commit -m "feat: added cloud mask preprocessing function"
git commit -m "fix: corrected null values in dataset loader"
git commit -m "docs: added setup instructions to README"
```

---

### 🆘 Messed Something Up?

| Problem | Fix |
|---------|-----|
| Committed wrong file | `git reset HEAD~1` |
| Want to discard all local changes | `git checkout -- .` |
| Pushed to wrong branch | Tell the team lead immediately |
| Conflict you can't resolve | Don't panic — call a teammate |

---

### 📞 Before Pushing — Quick Sanity Check

```bash
git status          # see what's changed
git diff            # see exact line changes
git log --oneline   # see your recent commits
```

---

## 📓 Notebook Naming Convention

Name notebooks with a number prefix to keep them ordered:

```
01_eda.ipynb               ← Exploratory Data Analysis
02_preprocessing.ipynb     ← Data Cleaning
03_model_baseline.ipynb    ← First model attempt
04_model_improved.ipynb    ← Better version
05_results_analysis.ipynb  ← Final results
```

---

## 📦 Data

> ⚠️ **Do NOT commit large data files to Git.** Use `.gitignore` to exclude them.

- Download data from: _(add link when available)_
- Place raw files in `data/raw/`
- Use `data/sample/` for tiny test files that are okay to commit

---

## 🔗 Resources

- [Hack2Skill BAH 2026 Page](https://hack2skill.com/event/bah2026/)
- [ISRO Official Site](https://www.isro.gov.in/)
- [Mosdac Data Portal](https://www.mosdac.gov.in/) — ISRO satellite data
- [Bhuvan Portal](https://bhuvan.nrsc.gov.in/) — ISRO geo-platform
### PS7
- [AstroNet-Vetting: A Neural Network for TESS Light Curve Vetting](https://github.com/yuliang419/Astronet-Vetting)
- [Machine learning models and utilities for exoplanet science](https://github.com/google-research/exoplanet-ml)
---

## 📝 Notes & Decisions

Use this section to log important team decisions:

- [ ] Finalise problem statement
- [ ] Agree on tech stack (PyTorch / TensorFlow / sklearn)
- [ ] Set up shared data storage
- [ ] Assign roles

---

*Made with ❤️ for BAH 2026 — Team [Your Team Name]*