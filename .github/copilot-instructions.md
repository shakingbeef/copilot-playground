# Copilot Instructions — Task Manager API Playground

## Project Overview
This is a FastAPI Task Manager API using SQLite via SQLAlchemy. It's a learning playground for Copilot CLI features.

## Code Conventions
- Python 3.11+, FastAPI, SQLAlchemy ORM, Pydantic v2
- Routes live in `app/routes/`, models in `app/models.py`, DB setup in `app/database.py`
- All endpoints return JSON; use HTTPException for errors
- Status values for tasks are strictly: `todo`, `in_progress`, `done`
- Always add a corresponding test in `tests/test_tasks.py` when adding a new endpoint

## Testing
- Run tests with: `pytest tests/ -v`
- Use the `TestClient` pattern already in `tests/test_tasks.py`
- Tests use an in-memory SQLite test DB — never touch `tasks.db` in tests

## MCP
- A SQLite MCP server can be pointed at `tasks.db` to query live app data
- The filesystem MCP server is configured to browse the `app/` directory

## Skills Available
- `add-endpoint`: Add a new FastAPI route following project conventions
- `write-test`: Write a pytest test for an existing or new endpoint
- `explain-route`: Explain what a route does and its edge cases
- `write-docs`: Add OpenAPI annotations, docstrings, or docs/README updates for an endpoint

## Agents Available
- `api-designer`: Design new API endpoints (spec only, no implementation)
- `code-reviewer`: Review code changes for bugs, missing error handling, and test coverage
- `doc-writer`: Write documentation (OpenAPI annotations, docstrings, README updates) — never writes implementation code
