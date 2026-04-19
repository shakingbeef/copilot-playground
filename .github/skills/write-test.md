# Skill: write-test
# Invocation: "write a test for X" or "add test coverage for X"

You are helping write a pytest test for the Task Manager API.

## Always follow these conventions:
1. Add tests to `tests/test_tasks.py`
2. Use the existing `client` TestClient — do not create a new one
3. Each test function name starts with `test_`
4. Add a docstring describing what behavior is being tested
5. Always assert the status code first, then the response body

## Template:
```python
def test_your_scenario():
    """Describe what this test verifies."""
    # Setup: create any needed data
    created = client.post("/tasks/", json={"title": "Test task"}).json()

    # Act
    response = client.post(f"/tasks/{created['id']}/your-action")

    # Assert
    assert response.status_code == 200
    assert response.json()["field"] == "expected_value"
```
