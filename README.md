# Assignments for CS146S: The Modern Software Developer

This is the home of the assignments for [CS146S: The Modern Software Developer](https://themodernsoftware.dev), taught at Stanford University fall 2025.

## Overview

This repository includes an **LLM-powered Action Item Extractor** (Week 2) — a web application that converts free-form notes into structured, actionable tasks. The application supports two extraction modes:

- **Rule-based extraction** — Uses heuristic patterns (bullet lists, keyword prefixes like `todo:`, `action:`, checkboxes) to identify action items.
- **LLM-based extraction** — Uses Ollama with a local language model (e.g., Llama 3.1) to intelligently extract action items from natural language, including Indonesian text.

Notes and action items are persisted in SQLite. A minimal HTML frontend provides extraction controls and displays results.

---

## Setup & Running the Project

These steps work with Python 3.10+ (3.12 recommended).

### 1. Install Anaconda

- Download and install: [Anaconda Individual Edition](https://www.anaconda.com/download)
- Open a new terminal so `conda` is on your `PATH`.

### 2. Create and Activate the Conda Environment

```bash
conda create -n cs146s python=3.12 -y
conda activate cs146s
```

### 3. Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python -
```

*(On Windows, you may need to use the Poetry installer or add Poetry to your PATH manually.)*

### 4. Install Project Dependencies

From the repository root:

```bash
poetry install --no-interaction
```

### 5. Run the Application

With the `cs146s` conda environment activated and dependencies installed:

```bash
poetry run uvicorn week2.app.main:app --reload
```

The server starts at `http://127.0.0.1:8000`. Open it in a browser to use the Action Item Extractor.

**Note:** For LLM-based extraction, ensure [Ollama](https://ollama.ai) is installed and the `llama3.1:8b` model is pulled (`ollama pull llama3.1:8b`).

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serves the frontend HTML |
| **Action Items** | | |
| `POST` | `/action-items/extract` | Extract action items using rule-based heuristics |
| `POST` | `/action-items/extract-llm` | Extract action items using the LLM (Ollama) |
| `GET` | `/action-items` | List all action items (optional `?note_id=` filter) |
| `POST` | `/action-items/{id}/done` | Mark an action item as done/undone |
| **Notes** | | |
| `GET` | `/notes` | List all saved notes |
| `POST` | `/notes` | Create a new note |
| `GET` | `/notes/{note_id}` | Get a single note by ID |

### Extract Endpoints Payload

Both `/action-items/extract` and `/action-items/extract-llm` accept:

```json
{
  "text": "Your notes here...",
  "save_note": true
}
```

Response:

```json
{
  "note_id": 1,
  "items": [{"id": 1, "text": "First action"}, {"id": 2, "text": "Second action"}]
}
```

---

## Running the Test Suite

From the repository root, with the `cs146s` environment activated:

```bash
poetry run pytest week2/tests/ -v
```

Or using `python -m pytest` with `PYTHONPATH` set:

```bash
PYTHONPATH=. poetry run pytest week2/tests/ -v
```

Tests use `unittest.mock.patch` to mock the Ollama LLM client, so no network calls or running Ollama instance is required. The suite covers rule-based extraction and LLM extraction (bullet lists, keyword-prefixed lines, empty input, JSON parsing, and error handling).
