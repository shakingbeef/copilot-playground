from fastapi import FastAPI
from app.database import init_db
from app.routes.tasks import router

app = FastAPI(title="Task Manager API", description="Copilot Playground App")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(router, prefix="/tasks", tags=["tasks"])

@app.get("/")
def root():
    return {"message": "Task Manager API — Copilot Playground 🤖"}
