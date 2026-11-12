@echo off
cd /d "%~dp0"
if not "%~1"=="" goto passthrough
set /p BRIEF=What's the task for the room? 
python room.py go "%BRIEF%"
goto end
:passthrough
python room.py %*
:end
pause
