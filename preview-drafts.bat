@echo off
setlocal

cd /d "%~dp0"
if not exist "private-content" mkdir "private-content"

hugo server --buildDrafts --config hugo.toml,hugo.private.toml %*
exit /b %errorlevel%
