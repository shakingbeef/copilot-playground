# 🎓 Copilot CLI — Hands-On Exercises

Work through these in order. Each exercise targets one feature.

---

## Exercise 1: MCP — Connect to Your App's Database

**Goal:** Query live app data with natural language.

1. Start the app: `uvicorn app.main:app --reload`
2. Create some tasks via the API: `curl -X POST http://localhost:8000/tasks/ -H "Content-Type: application/json" -d '{"title":"Buy milk"}'`
3. In Copilot CLI, run `/mcp` and enable the `sqlite` server
4. Ask Copilot: *"How many tasks are in the database, and what are their statuses?"*
5. Ask Copilot: *"Which task was created most recently?"*

**What you're learning:** MCP lets Copilot read live data from your app, not just the source code.

---

## Exercise 2: MCP — Browse Source with Filesystem MCP

**Goal:** Let Copilot navigate your codebase as a tool.

1. In Copilot CLI, run `/mcp` and enable the `filesystem` server
2. Ask: *"What routes are defined in this project?"*
3. Ask: *"What fields does the Task model have?"*
4. Ask: *"Which endpoints are missing tests?"*

**What you're learning:** With filesystem MCP, Copilot can reason about your codebase structure, not just what's in the current context window.

---

## Exercise 3: Skills — Use a Built-In Skill

**Goal:** Discover and invoke built-in Copilot skills.

1. Run `/skills` to see available skills
2. Open `app/routes/tasks.py` and ask: *"Explain this file"*
3. Ask Copilot to use the `explain-route` skill on the `update_task` function

**What you're learning:** Skills are reusable task modules you can invoke by name.

---

## Exercise 4: Skills — Use a Custom Skill

**Goal:** Use the project's custom `add-endpoint` skill.

1. Run `/skills` — you should see `add-endpoint` and `write-test` listed
2. Ask: *"Use the add-endpoint skill to add POST /tasks/{id}/archive that sets status to 'archived'"*
3. Then ask: *"Use the write-test skill to write a test for the archive endpoint"*

**What you're learning:** Custom skills encode your project's conventions so Copilot doesn't have to rediscover them each time.

---

## Exercise 5: Custom Agents — Switch Roles

**Goal:** See how different agents give different responses.

1. Run `/agent` and select `code-reviewer`
2. Share the contents of `app/routes/tasks.py` and ask for a review
3. Note what it says (it should flag missing pagination, missing complete endpoint)
4. Run `/agent` and switch to `api-designer`
5. Ask: *"Design the complete endpoint for tasks"*

**What you're learning:** Custom agents let you lock Copilot into a specific role and perspective.

---

## Exercise 6: Cloud Agent — Delegate Issue #1 (Pagination)

**Goal:** Let Copilot autonomously fix a bug and open a PR.

1. Go to the GitHub repo and open Issue #1 (Add pagination to GET /tasks)
2. In Copilot CLI, type: *"Fix the pagination issue in the task list endpoint"*
3. Type `/delegate` to send this to the cloud agent
4. Watch GitHub — Copilot will open a PR with the fix
5. Review the PR diff and merge it (or request changes)

**What you're learning:** `/delegate` hands off work to the cloud agent, which works asynchronously and opens a real PR.

---

## Exercise 7: Cloud Agent — Delegate Issue #2 (Complete Endpoint)

**Goal:** Delegate a feature request.

1. In Copilot CLI: *"Implement POST /tasks/{id}/complete that marks a task as done. There's a failing test for it already."*
2. `/delegate`
3. The cloud agent should find the failing test and make it pass

**What you're learning:** The cloud agent can use existing failing tests as a spec to drive implementation.

---

## Exercise 8: Hooks — Auto-run Tests on Save

**Goal:** Configure a hook to run tests automatically.

1. Ask Copilot: *"Set up a hook that runs `pytest tests/ -v` whenever I save a Python file"*
2. Make a change to `app/routes/tasks.py` and save
3. Observe the test output appearing automatically

**What you're learning:** Hooks turn Copilot into a proactive assistant that reacts to your workflow.

---

## Exercise 9: Custom Agents — Document an Endpoint

**Goal:** Use the `doc-writer` agent and `write-docs` skill to add real documentation to the API.

1. Run `/agent` and select `doc-writer`
2. Ask: *"Document the GET /tasks/{id} endpoint — I want OpenAPI annotations, a docstring, and a one-liner for the README"*
3. Review the output (it should never touch implementation logic)
4. Run `/agent` to exit the agent, then invoke the `write-docs` skill to apply the changes
5. Start the app and visit http://localhost:8000/docs — verify your annotations appear in the Swagger UI

**What you're learning:** The `doc-writer` agent is constrained to documentation only, so it can't accidentally change behavior. Pairing a focused agent with a skill makes the workflow repeatable.

---

## 🏆 Bonus: Chain Everything

1. Use `api-designer` agent to spec a new `/tasks/{id}/assign` endpoint
2. Use `add-endpoint` skill to implement it
3. Use `write-test` skill to add coverage
4. Use `doc-writer` agent to draft the documentation
5. Use `write-docs` skill to apply the docs
6. Use `code-reviewer` agent to review your changes
7. Delegate the whole thing to cloud agent via `/delegate`
