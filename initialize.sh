#!/usr/bin/env bash
set -euo pipefail

git submodule update --init --recursive
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
