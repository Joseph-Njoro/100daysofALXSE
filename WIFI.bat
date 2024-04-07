@echo off
setlocal enabledelayedexpansion

rem Save list of saved WiFi interfaces to a text file called interfaces.txt
netsh wlan show profiles | find "All User Profile" | findstr /r /c:"[ ]*All User Profile *: .*" > interfaces.txt

rem Display list of saved WiFi interfaces
echo List of saved WiFi interfaces:
for /f "tokens=5 delims=: " %%a in (interfaces.txt) do (
    echo %%a
)

rem Prompt user to input WiFi interface name
set /p interface="Enter WiFi interface name: "

rem Get password for the specified WiFi interface
for /f "tokens=2 delims=: " %%b in ('netsh wlan show profile name="%interface%" key=clear ^| findstr /c:"Key Content"') do (
    set password=%%b
)

rem Check if password retrieval was successful
if "%password%"=="" (
    echo Error: Unable to retrieve the password for %interface%.
) else (
    echo %password% > "%interface%_password.txt"
    echo Password for WiFi interface %interface% has been saved to %interface%_password.txt.
)

endlocal