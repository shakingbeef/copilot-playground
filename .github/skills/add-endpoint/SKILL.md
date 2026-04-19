---
name: add-endpoint
description: Adds a new FastAPI route to this Task Manager API. Use when asked to add an endpoint, create a route, or implement a new API action.
---

You are helping add a new FastAPI endpoint to this Task Manager API.

## Always follow these conventions:
1. Add the route to `app/routes/tasks.py`
2. Use the existing `get_db` dependency for database access
3. Use `Task` model from `app/models.py`
4. Return 404 with `HTTPException` if a task is not found
5. Status values are strictly: `todo`, `in_progress`, `done`
6. After adding the route, remind the user to add a test in `tests/test_tasks.py`

## Template for a new route:
```python
@router.post("/{task_id}/your-action")
def your_action(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    # ... your logic here
    db.commit()
    db.refresh(task)
    return task
```
