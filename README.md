# 🤖 Copilot Playground

A hands-on repo for learning GitHub Copilot CLI features:

| Feature | How to learn it |
|---|---|
| ☁️ **Cloud Agent** | Delegate the pre-loaded GitHub issues to Copilot — it will open PRs |
| 🔌 **MCP** | Connect the SQLite and filesystem MCP servers, then query your app live |
| 🛠️ **Skills** | Use the built-in skills, then write your own in `.github/skills/` |
| 🤖 **Custom Agents** | Try the pre-defined agents in `.github/agents/`, then build your own |
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
├── .github/
│   ├── skills/                 # Custom Copilot skills
│   ├── agents/                 # Custom Copilot agent definitions
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
