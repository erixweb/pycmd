title Pywarp

if NOT exist C:\pywarp\pywarp.py (
    cls
    mkdir C:\pywarp
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/erixweb/pycmd/master/main.py', 'C:\pywarp\pywarp.py')"
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/erixweb/pycmd/master/pywarp.bat', 'C:\pywarp\pywarp.bat')"
    cls
) else (
    exit
)
pause