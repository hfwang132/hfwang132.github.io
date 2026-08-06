@echo off
setlocal
cd /d "%~dp0"

set "PYTHON_EXE=python"
if exist "%~dp0.venv\Scripts\python.exe" set "PYTHON_EXE=%~dp0.venv\Scripts\python.exe"

if /I "%~1"=="--link" goto deploy

echo Running local tests...
"%PYTHON_EXE%" -m unittest discover -s "%~dp0tests" -v
if errorlevel 1 exit /b %errorlevel%

echo Auditing rendered mathematical formulas...
"%PYTHON_EXE%" "%~dp0scripts\audit_math.py"
if errorlevel 1 exit /b %errorlevel%

:deploy
echo Building locally and publishing static output to Vercel...
"%PYTHON_EXE%" "%~dp0scripts\deploy_vercel.py" %*
exit /b %errorlevel%
