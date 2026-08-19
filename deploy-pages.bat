@echo off
setlocal
cd /d "%~dp0"

set "PYTHON_EXE=python"
if exist "%~dp0.venv\Scripts\python.exe" set "PYTHON_EXE=%~dp0.venv\Scripts\python.exe"

echo Synchronizing publication data from BibTeX...
"%PYTHON_EXE%" "%~dp0scripts\sync_publications.py"
if errorlevel 1 exit /b %errorlevel%

echo Running local tests...
"%PYTHON_EXE%" -m unittest discover -s "%~dp0tests" -v
if errorlevel 1 exit /b %errorlevel%

echo Auditing rendered mathematical formulas...
"%PYTHON_EXE%" "%~dp0scripts\audit_math.py"
if errorlevel 1 exit /b %errorlevel%

echo Building locally and publishing generated files to gh-pages...
"%PYTHON_EXE%" "%~dp0scripts\deploy_pages.py" %*
exit /b %errorlevel%
