#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python_cmd="python"
if [[ -x "${repo_dir}/.venv/bin/python" ]]; then
  python_cmd="${repo_dir}/.venv/bin/python"
elif [[ -x "${repo_dir}/.venv/Scripts/python.exe" ]]; then
  python_cmd="${repo_dir}/.venv/Scripts/python.exe"
fi

if [[ "${1:-}" != "--link" ]]; then
  echo "Synchronizing publication data from BibTeX..."
  "${python_cmd}" "${repo_dir}/scripts/sync_publications.py"

  echo "Running local tests..."
  "${python_cmd}" -m unittest discover -s "${repo_dir}/tests" -v

  echo "Auditing rendered mathematical formulas..."
  "${python_cmd}" "${repo_dir}/scripts/audit_math.py"
fi

echo "Building locally and publishing static output to Vercel..."
"${python_cmd}" "${repo_dir}/scripts/deploy_vercel.py" "$@"
