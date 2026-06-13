# 🚀 Bharatiya Antariksh Hackathon 2026

> **Event:** [Bharatiya Antariksh Hackathon 2026 by ISRO × Hack2Skill](https://hack2skill.com/event/bah2026/)

---

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
git clone https://github.com/YOUR_USERNAME/bah2026.git
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

## 🧠 How to Contribute (Team Guide)

### First Time Setup

1. **Fork** or **clone** this repo (You get direct access via invite).
2. Always create a **new branch** before making changes.

### Branching Convention

```
main          → stable, working code only
dev           → ongoing work, merge here first
feature/name  → your personal branch for a specific task
```

**Example:**
```bash
git checkout -b feature/data-preprocessing
```

### Making Changes

```bash
# 1. Pull latest changes first
git pull origin dev

# 2. Make your changes...

# 3. Stage and commit
git add .
git commit -m "feat: add cloud mask preprocessing script"

# 4. Push your branch
git push origin feature/data-preprocessing

# 5. Open a Pull Request on GitHub → merge into dev
```

### Commit Message Tips

Use a short prefix to describe the type of change:

| Prefix | Use for |
|--------|---------|
| `feat:` | New feature or file |
| `fix:` | Bug fix |
| `data:` | Data-related changes |
| `docs:` | Documentation updates |
| `test:` | Adding tests |
| `refactor:` | Code cleanup |

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

---

## 📝 Notes & Decisions

Use this section to log important team decisions:

- [ ] Finalise problem statement
- [ ] Agree on tech stack (PyTorch / TensorFlow / sklearn)
- [ ] Set up shared data storage
- [ ] Assign roles

---

*Made with ❤️ for BAH 2026 — Team [Your Team Name]*
