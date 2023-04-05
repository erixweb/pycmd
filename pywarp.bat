@echo off

title pywarp

if NOT exist C:\pywarp\pywarp.py (
    cls
    mkdir C:\pywarp
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/erixweb/pycmd/master/main.py', 'C:\pywarp\pywarp.py')"
    cls
) else (
    cls
    python C:\pywarp\pywarp.py
)
pause