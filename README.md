# 🤖 Copilot Playground

A hands-on repo for learning GitHub Copilot CLI features:

| Feature | How to learn it |
|---|---|
| ☁️ **Cloud Agent** | Delegate the pre-loaded GitHub issues to Copilot — it will open PRs |
| 🔌 **MCP** | Connect the SQLite and filesystem MCP servers, then query your app live |
| 🛠️ **Skills** | Use the built-in skills, then write your own in `.github/skills/` |
| 🤖 **Custom Agents** | Try the pre-defined agents in `.github/agents/`, then build your own — includes `api-designer`, `code-reviewer`, and `doc-writer` |
| 🪝 **Hooks** | Hooks are pre-configured to lint on save and test before commit |

## 📁 Structure

```
copilot-playground/
├── app/                        # FastAPI task manager (the playground app)
│   ├── main.py                 # Entry point
│   ├── models.py               # Task model
│   ├── database.py             # SQLite connection
│   └── routes/
│       └── tasks.py            # Task CRUD routes
├── tests/                      # Pytest test suite (some intentionally failing!)
├── scripts/
│   ├── README.md               # Scripts documentation
│   └── create_tech_debt_issues.py  # Tech debt issue creator
├── .github/
│   ├── skills/                 # Custom Copilot skills
│   ├── agents/                 # Custom Copilot agent definitions
│   ├── workflows/              # GitHub Actions workflows
│   ├── tech-debts.json         # Tech debt registry
│   ├── copilot-instructions.md # Project-level Copilot instructions
│   └── mcp.json                # MCP server configuration
├── docs/
│   └── exercises.md            # Step-by-step learning exercises
└── requirements.txt
```

## 🚀 Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API available at: http://localhost:8000  
Interactive docs: http://localhost:8000/docs

## 🎓 Start Here

Open `docs/exercises.md` for step-by-step exercises for each feature.

## 🛠️ Tech Debt Management

This repository includes a systematic approach to tracking and managing technical debt:

- **Tech Debt Registry**: `.github/tech-debts.json` documents all identified tech debts with details, priority, and suggested fixes
- **Issue Creation Script**: `scripts/create_tech_debt_issues.py` converts tech debt definitions into GitHub issues
- **Automated Workflow**: `.github/workflows/create-tech-debt-issues.yml` can automatically create issues

### Current Tech Debts

4 tech debts have been identified:
1. SQLAlchemy 2.0 migration (declarative_base) — **Medium**
2. FastAPI lifespan event handler migration — **Medium**
3. Pydantic v2 `.model_dump()` migration — **Low**
4. Python 3.12 datetime.utcnow() deprecation — **Low**

### Create Issues

```bash
# Option 1: Run the script directly
python3 scripts/create_tech_debt_issues.py

# Option 2: Use GitHub Actions (via web UI)
# Go to Actions > Create Tech Debt Issues > Run workflow
```

For more details, see `scripts/README.md`.
