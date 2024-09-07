@echo off
set "psFile=C:\path\to\ConvertToPDF.ps1"

:loop
if "%~1"=="" goto :eof
PowerShell -NoProfile -ExecutionPolicy Bypass -File "%psFile%" "%~1"
shift
goto loop
