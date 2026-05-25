from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import init_db
from app.routes.tasks import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Task Manager API", description="Copilot Playground App", lifespan=lifespan)

app.include_router(router, prefix="/tasks", tags=["tasks"])

@app.get("/")
def root():
    return {"message": "Task Manager API — Copilot Playground 🤖"}
