start cmd /k python.exe "./manage.py" %1 "runserver" "0.0.0.0"
for /f "tokens=1-2 delims=:" %%a in ('ipconfig^|find "IPv4"') do set ip=%%b
set ip=%ip:~1%
start firefox -kiosk -private-window http://%ip%:7777/start