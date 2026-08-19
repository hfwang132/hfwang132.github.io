#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python_cmd="python"
if [[ -x "${repo_dir}/.venv/bin/python" ]]; then
  python_cmd="${repo_dir}/.venv/bin/python"
elif [[ -x "${repo_dir}/.venv/Scripts/python.exe" ]]; then
  python_cmd="${repo_dir}/.venv/Scripts/python.exe"
fi

"${python_cmd}" "${repo_dir}/scripts/sync_publications.py" "$@"
