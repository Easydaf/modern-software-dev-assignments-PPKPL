# Week 6 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: **Muhammad Daffa Musyafa** \
SUNet ID: **TODO** \
Citations: **Semgrep Documentation, FastAPI Security Docs, SQLAlchemy Documentation, AI Assistant (Warp/Copilot)**

This assignment took me about **2** hours to do.


## Brief findings overview
> Running `semgrep scan --config auto week6` initially surfaced 6 blocking SAST (Static Application Security Testing) findings. The vulnerabilities included a wildcard CORS policy, an insecure DOM write (XSS), SQL injection via f-strings, and 3 Python-specific execution warnings (`eval-detected`, `subprocess-shell-true`, `dynamic-urllib-use-detected`). I chose to ignore the latter 3 as they are related to internal execution and focused on remediating the 3 most critical web-facing vulnerabilities (CORS, XSS, and SQL Injection).

## Fix #1
a. File and line(s)
> `week6/backend/app/main.py` (Line 24)

b. Rule/category Semgrep flagged
> `python.fastapi.security.wildcard-cors.wildcard-cors`

c. Brief risk description
> The CORS policy used a wildcard `*`, which allows any origin (any website on the internet) to make requests to the API and potentially access or steal sensitive user data.

d. Your change (short code diff or explanation, AI coding tool usage)
> I used Copilot to restrict the origins.
> **Before:** `allow_origins=["*"],`
> **After:** `allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],`

e. Why this mitigates the issue
> By specifying exact origins, the browser will block malicious external sites from interacting with the API, enforcing the Same-Origin Policy securely.

## Fix #2
a. File and line(s)
> `week6/frontend/app.js` (Line 14)

b. Rule/category Semgrep flagged
> `javascript.browser.security.insecure-document-method.insecure-document-method`

c. Brief risk description
> The code used `li.innerHTML` to inject notes content. If a malicious user inputs `<script>` tags, the browser would execute them, leading to a Cross-Site Scripting (XSS) attack.

d. Your change (short code diff or explanation, AI coding tool usage)
> Prompted AI to use safe DOM methods instead of `innerHTML`.
> **Before:** `li.innerHTML = "<strong>" + n.title + "</strong>: " + n.content;`
> **After:** > `const strong = document.createElement('strong');`
> `strong.textContent = n.title;`
> `li.appendChild(strong);`
> `li.appendChild(document.createTextNode(': ' + n.content));`

e. Why this mitigates the issue
> Using `textContent` and `document.createTextNode` ensures that the browser treats the input strictly as text, safely escaping any HTML entities or malicious scripts.

## Fix #3
a. File and line(s)
> `week6/backend/app/routers/notes.py` (Lines 71-79)

b. Rule/category Semgrep flagged
> `python.sqlalchemy.security.audit.avoid-sqlalchemy-text.avoid-sqlalchemy-text`

c. Brief risk description
> The code used an unsafe Python f-string (`{q}`) directly inside a `text()` SQL query. This allows an attacker to break out of the string and execute arbitrary SQL commands (SQL Injection).

d. Your change (short code diff or explanation, AI coding tool usage)
> I used AI to refactor the raw query to use SQLAlchemy's bound parameters.
> **Before:** `WHERE title LIKE '%{q}%' OR content LIKE '%{q}%'`
> **After:** `WHERE title LIKE :q OR content LIKE :q`
> And passed the parameters safely using `.params(q=f"%{q}%")`

e. Why this mitigates the issue
> Parameterized queries (bound parameters) separate the SQL logic from the user input. The database engine treats the input as a literal value, making it impossible for the input to alter the executable SQL logic.