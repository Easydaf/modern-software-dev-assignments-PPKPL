@echo off
set PYTHONPATH=.
pytest -q backend/tests --maxfail=1 -x
if %errorlevel% neq 0 exit /b %errorlevel%
pre-commit run --all-files