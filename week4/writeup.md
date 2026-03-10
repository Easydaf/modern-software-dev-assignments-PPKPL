# Week 4 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: **Muhammad Daffa Musyafa** \
SUNet ID: **TODO** \
Citations: **GitHub Copilot, FastAPI Documentation, SQLAlchemy Documentation**

This assignment took me about **4** hours to do.


## YOUR RESPONSES
### Automation #1
a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)
> Due to the paid nature of Claude Code, I received permission to use GitHub Copilot. My inspiration for this automation came from the assignment's guidance on creating custom slash commands (like `/tests.md`) to streamline developer workflows. I designed a Windows-compatible batch script to simulate this autonomous testing behavior.

b. Design of each automation, including goals, inputs/outputs, steps
> **Goal:** To automate the process of running unit tests and formatting code in a Windows Conda environment, preventing unformatted or broken code from being committed.
> **Inputs/Outputs:** No direct inputs. Outputs are the console logs from pytest and pre-commit hooks.
> **Steps:** > 1. Set the `PYTHONPATH` to the current directory.
> 2. Run `pytest -q backend/tests --maxfail=1 -x`.
> 3. If tests pass (exit code 0), automatically trigger `pre-commit run --all-files`.

c. How to run it (exact commands), expected outputs, and rollback/safety notes
> **Command:** `run_tests.bat` (executed in the terminal).
> **Expected Output:** A green `[100%]` pass from pytest, followed by the pre-commit checks indicating if files were reformatted by `black` or `ruff`. 
> **Safety Notes:** The script uses `if %errorlevel% neq 0 exit /b %errorlevel%` to ensure that formatting only occurs if the code is functionally correct (tests pass), preventing the formatting of broken code.

d. Before vs. after (i.e. manual workflow vs. automated workflow)
> **Before:** I had to manually type `set PYTHONPATH=.`, run the pytest command, wait for the result, and then manually run the pre-commit command. It was tedious and prone to typos.
> **After:** A single `run_tests.bat` command handles the entire verification and formatting pipeline, saving time and mental energy.

e. How you used the automation to enhance the starter application
> I used this script continuously while implementing Tasks 2 through 6. After using Copilot to generate the Search Endpoint, CRUD operations, and the Regex extraction logic, I immediately ran `run_tests.bat` to verify the logic and ensure the newly added code adhered to the repository's styling standards.


### Automation #2
a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)
> Inspired by the `CLAUDE.md` repository guidance concept, I utilized GitHub Copilot's prompt templating and contextual chat features to act as an automated coding assistant that already understands the specific stack (FastAPI + Vanilla JS) of the project.

b. Design of each automation, including goals, inputs/outputs, steps
> **Goal:** To automate the generation of boilerplate code and complex logic (like SQLAlchemy queries and Regex) without needing to manually look up syntax.
> **Inputs/Outputs:** Input is a natural language prompt describing the desired endpoint or feature. Output is fully functional Python or JavaScript code integrated into the existing structure.
> **Steps:** > 1. Open the target file (e.g., `notes.py`).
> 2. Provide Copilot with specific instructions via Inline Chat or panel (e.g., "Create a GET /search endpoint using SQLAlchemy ilike").
> 3. Review, accept, and slightly adapt the generated code to fit the exact routing structure.

c. How to run it (exact commands), expected outputs, and rollback/safety notes
> **Command:** Use `Ctrl + I` for Inline Chat or open the Copilot panel and provide the prompt.
> **Expected Output:** Code snippets that correctly utilize FastAPI paradigms (like `Depends(get_db)`) and SQLAlchemy ORM.
> **Safety Notes:** Always review the generated code. For example, Copilot initially generated a `db.flush()` for creating notes, which caused UI race conditions. I had to manually step in and change it to `db.commit()`.

d. Before vs. after (i.e. manual workflow vs. automated workflow)
> **Before:** I would have to manually write the SQLAlchemy query, figure out the `ilike` syntax, build the HTML structure, and write the JavaScript `fetch` logic from scratch, which would take hours of documentation reading.
> **After:** I just describe the behavior, and Copilot generates the structural code in seconds, allowing me to focus on fixing integration bugs (like Windows OS permission errors) rather than typing syntax.

e. How you used the automation to enhance the starter application
> I used Copilot to completely generate the `extract_tags` function using Regex in Task 4, the full CRUD endpoints (`PUT` and `DELETE`) for notes in Task 5, and the Pydantic validation rules in Task 6.