@echo off
setlocal

if not "%~1"=="" goto import_zhihu

echo Validating the production site...
hugo --minify --renderToMemory
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
if exist ".venv\Scripts\python.exe" goto import_with_venv
python scripts\import_zhihu.py %*
exit /b %errorlevel%

:import_with_venv
".venv\Scripts\python.exe" scripts\import_zhihu.py %*
exit /b %errorlevel%
