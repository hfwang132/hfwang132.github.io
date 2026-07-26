@echo off
setlocal

set "PYTHON_EXE=python"
if exist "%~dp0.venv\Scripts\python.exe" set "PYTHON_EXE=%~dp0.venv\Scripts\python.exe"

if /I "%~1"=="--publish" goto publish

"%PYTHON_EXE%" "%~dp0scripts\sync_cv.py" %*
exit /b %errorlevel%

:publish
"%PYTHON_EXE%" "%~dp0scripts\sync_cv.py"
if errorlevel 1 exit /b %errorlevel%
call "%~dp0updates.bat"
exit /b %errorlevel%
