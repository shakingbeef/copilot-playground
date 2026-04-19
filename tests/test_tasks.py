import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

TEST_DB = "sqlite:///./test.db"
engine = create_engine(TEST_DB, connect_args={"check_same_thread": False})
TestingSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSession()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


client = TestClient(app)


def test_create_task():
    response = client.post("/tasks/", json={"title": "Buy milk", "description": "2% please"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Buy milk"
    assert data["status"] == "todo"


def test_get_task():
    created = client.post("/tasks/", json={"title": "Write tests"}).json()
    response = client.get(f"/tasks/{created['id']}")
    assert response.status_code == 200
    assert response.json()["title"] == "Write tests"


def test_get_task_not_found():
    response = client.get("/tasks/9999")
    assert response.status_code == 404


def test_update_task_status():
    created = client.post("/tasks/", json={"title": "Ship it"}).json()
    response = client.put(f"/tasks/{created['id']}", json={"status": "in_progress"})
    assert response.status_code == 200
    assert response.json()["status"] == "in_progress"


def test_delete_task():
    created = client.post("/tasks/", json={"title": "Delete me"}).json()
    response = client.delete(f"/tasks/{created['id']}")
    assert response.status_code == 204


# --- INTENTIONALLY FAILING TESTS (for Issue #2 and #3 exercises) ---

def test_complete_task():
    """Issue #2: POST /tasks/{id}/complete should mark a task as done."""
    created = client.post("/tasks/", json={"title": "Finish feature"}).json()
    response = client.post(f"/tasks/{created['id']}/complete")
    assert response.status_code == 200
    assert response.json()["status"] == "done"


def test_filter_tasks_by_status():
    """Issue #3: GET /tasks?status=done should return only done tasks."""
    client.post("/tasks/", json={"title": "Task A"})
    task_b = client.post("/tasks/", json={"title": "Task B"}).json()
    client.put(f"/tasks/{task_b['id']}", json={"status": "done"})

    response = client.get("/tasks/?status=done")
    assert response.status_code == 200
    results = response.json()
    assert all(t["status"] == "done" for t in results)
    assert len(results) == 1


def test_list_tasks_pagination():
    """Issue #1: GET /tasks should support ?skip=0&limit=10 pagination."""
    for i in range(15):
        client.post("/tasks/", json={"title": f"Task {i}"})
    response = client.get("/tasks/?skip=0&limit=5")
    assert response.status_code == 200
    assert len(response.json()) == 5
