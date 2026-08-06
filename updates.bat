@echo off
setlocal

set "PYTHON_EXE=python"
if exist ".venv\Scripts\python.exe" set "PYTHON_EXE=.venv\Scripts\python.exe"

if not "%~1"=="" goto import_zhihu

echo Validating the production site...
hugo --minify --renderToMemory
if errorlevel 1 exit /b %errorlevel%

echo Auditing rendered mathematical formulas...
"%PYTHON_EXE%" scripts\audit_math.py
if errorlevel 1 exit /b %errorlevel%

echo Staging the current repository changes...
git add -A
if errorlevel 1 exit /b %errorlevel%

git diff --cached --quiet
if errorlevel 2 exit /b %errorlevel%
if errorlevel 1 goto commit_changes

echo No new changes to commit.
goto push_changes

:commit_changes
git commit -m "daily updates"
if errorlevel 1 exit /b %errorlevel%

:push_changes
git push
exit /b %errorlevel%

:import_zhihu
"%PYTHON_EXE%" scripts\import_zhihu.py %*
exit /b %errorlevel%
