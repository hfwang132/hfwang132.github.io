@echo off
setlocal

git submodule update --init --recursive
if errorlevel 1 exit /b 1

if not exist .venv python -m venv .venv
if errorlevel 1 exit /b 1

.venv\Scripts\python.exe -m pip install --upgrade pip
if errorlevel 1 exit /b 1

.venv\Scripts\python.exe -m pip install -r requirements.txt
