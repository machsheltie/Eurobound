@echo off
rem Installs the Claude Notes addon into Blender. Close Blender first, then double-click this file.
set "BLENDER=C:\Program Files\Blender Foundation\Blender 5.2\blender.exe"
if not exist "%BLENDER%" (
  echo Blender was not found at %BLENDER%
  echo Edit this file and fix the path, or ask a Claude session to install it.
  pause
  exit /b 1
)
tasklist /FI "IMAGENAME eq blender.exe" | find /I "blender.exe" >nul
if not errorlevel 1 (
  echo Blender is running. Close it, then run this again.
  pause
  exit /b 1
)
"%BLENDER%" --background --python "%~dp0install_addon.py" 2>&1 | findstr "CLAUDE_NOTES_INSTALL"
pause
