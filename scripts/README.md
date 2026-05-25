# Scripts Directory

## Tech Debt Management

### `create_tech_debt_issues.py`

This script creates GitHub issues for identified technical debts.

**Purpose**: Converts tech debt definitions from `.github/tech-debts.json` into trackable GitHub issues.

**Usage**:
```bash
# Requires GitHub CLI (gh) to be installed and authenticated
python3 scripts/create_tech_debt_issues.py
```

**Prerequisites**:
- GitHub CLI (`gh`) installed: https://cli.github.com
- Authenticated with: `gh auth login`
- Run from repository root directory

**What it does**:
1. Reads `.github/tech-debts.json` (tech debt definitions)
2. Creates a GitHub issue for each tech debt
3. Applies appropriate labels and priority information
4. Reports success/failure for each issue

**Tech Debts Tracked**:
The following tech debts are currently identified:

1. **SQLAlchemy 2.0 Migration** (`app/database.py:10`)
   - Replace deprecated `declarative_base()` import
   - Priority: Medium

2. **FastAPI Lifespan Events** (`app/main.py:7`)
   - Migrate from `@app.on_event()` to lifespan handlers
   - Priority: Medium

3. **Pydantic v2 Migration** (`app/routes/tasks.py:57`)
   - Replace `.dict()` with `.model_dump()`
   - Priority: Low

4. **Python 3.12 Datetime** (SQLAlchemy internals)
   - Address `utcnow()` deprecation warning
   - Priority: Low

**Automated Workflow**:
Issues can also be created automatically via GitHub Actions:
- Manually trigger: `.github/workflows/create-tech-debt-issues.yml`
- Click "Actions" > "Create Tech Debt Issues" > "Run workflow"

**Adding New Tech Debts**:
1. Update `.github/tech-debts.json` with the new tech debt
2. Run the script or wait for automated workflow
3. Issues will be created with appropriate labels

**Removing Addressed Tech Debts**:
1. When a tech debt is resolved, remove its entry from `.github/tech-debts.json`
2. Close the corresponding GitHub issue
