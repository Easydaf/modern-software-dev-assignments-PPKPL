# Week 5 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: **Muhammad Daffa Musyafa** \
SUNet ID: **TODO** \
Citations: **Warp Documentation, FastAPI Documentation, SQLAlchemy Documentation**

This assignment took me about **4** hours to do.


## YOUR RESPONSES
### Automation A: Warp Drive saved prompts, rules, MCP servers

a. Design of each automation, including goals, inputs/outputs, steps
> My inspiration came from the assignment's guidance on using Warp Drive to create a "Test runner". Since Windows users often face syntax issues with standard `Makefile` commands in PowerShell, I designed a Warp Drive workflow specifically tailored to smoothly run tests and linters in a Windows Conda environment.

b. Before vs. after (i.e. manual workflow vs. automated workflow)
> **Goal:** To automate the process of testing and formatting code directly from the terminal without typing long, OS-specific commands.
> **Inputs/Outputs:** No direct inputs. Outputs are the console logs from pytest, ruff, and black.
> **Steps:** > 1. Temporarily set the `PYTHONPATH` variable for the current Windows PowerShell session.
> 2. Run `pytest -q backend/tests`.
> 3. Run `ruff check . --fix` to catch and fix linting errors.
> 4. Run `black .` to format the code.

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)
> **Command:** Open Warp Drive (using `#`) and run the saved workflow named `Test and Format Code`.
> **Expected Output:** A green `[100%]` pass from pytest, followed by `All checks passed!` from ruff and `All done!` from black.
> **Safety Notes:** The command sequence is strictly linear. By managing this within Warp Drive, it prevents syntax typos that could lead to running linters on broken code states.

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures
> **Before:** I had to manually remember and type `$env:PYTHONPATH="."; pytest -q backend/tests; ruff check . --fix; black .` every single time I wanted to check my code, which was incredibly tedious.
> **After:** I just type `#Test` and select the workflow in Warp. It executes the entire pipeline instantly, saving significant time.

e. How you used the automation (what pain point it resolves or accelerates)
> I used this Warp Drive automation constantly while completing Tasks 7 and 8. Whenever the Warp AI agents finished their code edits, I immediately triggered this workflow to verify their logic, catch Windows-specific SQLite file-locking errors, and ensure the newly generated code was styled perfectly.



### Automation #2
a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)
> Inspired by the assignment's emphasis on "multi-agent workflows", I utilized Warp's AI Agent feature across multiple terminal tabs to simulate a team of autonomous developers working concurrently on different features.

b. Design of each automation, including goals, inputs/outputs, steps
> **Goal:** To delegate independent features (Pagination and Error Handling) to separate AI agents working simultaneously in different Warp tabs.
> **Inputs/Outputs:** Input is a natural language prompt defining the task from `TASKS.md`. Output is the modified Python routing logic and test files.
> **Steps:** > 1. Open Tab 1, prompt Agent A to implement Task 8 (Pagination).
> 2. Open Tab 2, prompt Agent B to implement Task 7 (Robust Error Handling).
> 3. Supervise the agents as they formulate plans and ask for file modification permissions.

c. How to run it (exact commands), expected outputs, and rollback/safety notes
> **Command:** Open the Warp AI panel in "Agent" mode. Paste the prompt (e.g., "Implement Task 8...").
> **Autonomy Level & Supervision:** I intentionally set the agents to **Partial Autonomy**. They could read files and make plans independently, but they required my explicit "Approve" click before executing any terminal commands or modifying files. This ensured they didn't overwrite each other's work or break the app structure.
> **Safety Notes:** Parallel editing of the same routing files (`notes.py`) carries a risk of git conflicts or logic overwrites. Strict supervision via the "Approve" step mitigated this risk.

d. Before vs. after (i.e. manual workflow vs. automated workflow)
> **Before:** I would work linearly—finish Pagination, run tests, move to Error Handling, run tests again. This serialized process is slow.
> **After:** I deployed two agents to tackle both tasks concurrently. While Agent A was planning the Pagination logic, I was reviewing Agent B's changes for Error Handling.

e. How you used the automation (what pain point it resolves or accelerates)
> This multi-agent workflow dramatically accelerated development time. It resolved the pain point of context-switching. Instead of juggling the mental overhead of two different features, I acted as an orchestrator—delegating the syntax implementation to the AI and focusing my energy solely on reviewing their proposed architectural changes before approving them.