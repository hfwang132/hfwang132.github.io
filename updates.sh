#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${repo_dir}"

python_cmd="python"
if [[ -x ".venv/bin/python" ]]; then
  python_cmd=".venv/bin/python"
elif [[ -x ".venv/Scripts/python.exe" ]]; then
  python_cmd=".venv/Scripts/python.exe"
fi

if (($# == 0)); then
  echo "Validating the production site..."
  hugo --minify --renderToMemory

  echo "Running local tests..."
  "${python_cmd}" -m unittest discover -s tests -v

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
  echo "Building locally and publishing generated files to gh-pages..."
  "${python_cmd}" scripts/deploy_pages.py
  exit 0
fi

"${python_cmd}" scripts/import_zhihu.py "$@"

deploy_after_import=false
for argument in "$@"; do
  if [[ "${argument}" == "--publish" ]]; then
    deploy_after_import=true
    break
  fi
done

if [[ "${deploy_after_import}" == true ]]; then
  echo "Building locally and publishing generated files to gh-pages..."
  "${python_cmd}" scripts/deploy_pages.py
fi
