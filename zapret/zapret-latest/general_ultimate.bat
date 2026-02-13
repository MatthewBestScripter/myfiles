@echo off
chcp 65001 > nul
cd /d "%~dp0"
set "BIN=%~dp0bin\"
set "LISTS=%~dp0lists\"
cd /d "%BIN%"

start "zapret-roblox" /min "%BIN%winws.exe" ^
--wf-tcp=443 ^
--wf-udp=49152-65535 ^
--filter-tcp=443 --hostlist="%LISTS%list-roblox.txt" ^
--dpi-desync=fake ^
--dpi-desync-repeats=1 ^
--dpi-desync-fake-tls="%BIN%tls_clienthello_www_google_com.bin" ^
--dpi-desync-fake-tls-mod=sni=www.google.com --new ^
--filter-udp=49152-65535 ^
--dpi-desync=none --new
