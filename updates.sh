#!/usr/bin/env bash
set -euo pipefail

python_cmd="python"
if [[ -x ".venv/bin/python" ]]; then
  python_cmd=".venv/bin/python"
elif [[ -x ".venv/Scripts/python.exe" ]]; then
  python_cmd=".venv/Scripts/python.exe"
fi

if (($# == 0)); then
  echo "Validating the production site..."
  hugo --minify --renderToMemory

  echo "Auditing rendered mathematical formulas..."
  "${python_cmd}" scripts/audit_math.py

  echo "Staging the current repository changes..."
  git add -A
  diff_status=0
  git diff --cached --quiet || diff_status=$?
  if ((diff_status > 1)); then
    exit "${diff_status}"
  elif ((diff_status == 1)); then
    git commit -m "daily updates"
  else
    echo "No new changes to commit."
  fi
  git push
  exit 0
fi

"${python_cmd}" scripts/import_zhihu.py "$@"
