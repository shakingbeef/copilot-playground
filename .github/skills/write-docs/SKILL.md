---
name: write-docs
description: Adds documentation to this Task Manager API — OpenAPI annotations, Python docstrings, and docs/README updates. Use when asked to document an endpoint or feature.
---

You are helping document the Task Manager API. Documentation lives in three places — apply changes to whichever are relevant.

## Always follow these conventions

### 1. OpenAPI annotations (in `app/routes/tasks.py`)
Add `summary=` and `description=` to the route decorator. Use `response_model=` only when a Pydantic schema exists.
```python
@router.get(
    "/{task_id}",
    summary="Get a task",
    description="Retrieve a single task by its ID. Returns 404 if no task with that ID exists.",
)
def get_task(task_id: int, db: Session = Depends(get_db)):
    ...
```

### 2. Python docstrings (in `app/routes/tasks.py`)
Use Google-style docstrings. Always document `Args`, `Returns`, and `Raises`.
```python
def get_task(task_id: int, db: Session = Depends(get_db)):
    """Retrieve a single task by ID.

    Args:
        task_id: The integer ID of the task to retrieve.
        db: Database session injected by FastAPI dependency.

    Returns:
        The Task object if found.

    Raises:
        HTTPException(404): If no task with the given ID exists.
    """
```

### 3. Docs updates (in `docs/exercises.md`)
Add a short entry in the same style as existing exercises. Only do this for new or significantly changed endpoints.
```markdown
## Exercise N: Doc Writer — Annotate an Endpoint

**Goal:** Use the `doc-writer` agent and `write-docs` skill to document an endpoint.

1. Switch to the `doc-writer` agent with `/agent`
2. Ask: *"Document the GET /tasks/{id} endpoint"*
3. Apply the output using the `write-docs` skill
```

## Rules
- Do NOT modify any implementation logic — only add or update documentation strings and decorator params
- Status values in examples must match the allowed set: `todo`, `in_progress`, `done`
- Keep `summary=` under 10 words; `description=` under 2 sentences
- After applying, remind the user to verify the OpenAPI UI at http://localhost:8000/docs
