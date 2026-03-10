#!/usr/bin/env bash
set -euo pipefail

pytest -q backend/tests --maxfail=1 -x
pre-commit run --all-files
