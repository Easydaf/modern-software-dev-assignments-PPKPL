# Week 2 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: **TODO** \
SUNet ID: **TODO** \
Citations: **TODO**

This assignment took me about **TODO** hours to do.


## YOUR RESPONSES
For each exercise, please include what prompts you used to generate the answer, in addition to the location of the generated response. Make sure to clearly add comments in your code documenting which parts are generated.

### Exercise 1: Scaffold a New Feature
Prompt:
```
I need to implement TODO 1. Please add a new function called extract_action_items_llm(text: str) -> list[str] in this file. This function should use the ollama python package to send the text to an LLM (use 'llama3.1:8b'). The prompt to the LLM should instruct it to extract a list of actionable items from the text and return ONLY a JSON array of strings. Parse the LLM response using the json module and return the python list. Include basic error handling for JSON decoding.
```

Generated Code Snippets:
```
File: week2/app/services/extract.py Fungsi extract_action_items_llm, baris kode sekitar 69 117 line 15 sampai akhir fungsi
```

### Exercise 2: Add Unit Tests
Prompt:
```
I need to implement TODO 2. Please write unit tests for the extract_action_items_llm function located in week2/app/services/extract.py. Add these tests to this file. Make sure to cover multiple inputs: bullet lists, keyword-prefixed lines, and empty input. Please use unittest.mock.patch to mock the ollama.chat response so the tests run quickly and don't make actual network calls to the LLM.
```

Generated Code Snippets:
```
File: week2/tests/test_extract.py (Seluruh isi file test yang baru saja di-generate).
```

### Exercise 3: Refactor Existing Code for Clarity
Prompt:
```
I need to implement TODO 3. Please refactor the application to use the newly created extract_action_items_llm function instead of the old extract_action_items function in the API endpoint. Update the relevant route handler (likely in main.py or a router file) to call the LLM function and return its results. Update any necessary imports.
```

Generated/Modified Code Snippets:
```
File: week2/app/routers/action_items.py (Mengubah import dari extract_action_items menjadi extract_action_items_llm, dan mengubah pemanggilan fungsinya di dalam route handler POST /action-items/extract).
```


### Exercise 4: Use Agentic Mode to Automate a Small Task
Prompt:
```
TODO
```

Generated Code Snippets:
```
TODO: List all modified code files with the relevant line numbers.
```


### Exercise 5: Generate a README from the Codebase
Prompt:
```
TODO
```

Generated Code Snippets:
```
TODO: List all modified code files with the relevant line numbers.
```


## SUBMISSION INSTRUCTIONS
1. Hit a `Command (⌘) + F` (or `Ctrl + F`) to find any remaining `TODO`s in this file. If no results are found, congratulations – you've completed all required fields.
2. Make sure you have all changes pushed to your remote repository for grading.
3. Submit via Gradescope.
