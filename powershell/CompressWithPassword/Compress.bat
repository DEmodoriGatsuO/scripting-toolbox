@echo off
setlocal

set "psScriptPath=%~dp0CompressWithPassword.ps1"
set /p password="Enter password for the zip file: "

:processFile
if "%~1"=="" goto end
PowerShell -NoProfile -ExecutionPolicy Bypass -File "%psScriptPath%" -filePath "%~1" -password %password%
shift
goto processFile

:end
endlocal
