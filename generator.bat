@echo off
chcp 65001 >nul
cd /d "%~dp0"
py "%~dp0generator.py"
pause
