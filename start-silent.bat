@echo off
chcp 65001 >nul
cd /d "%~dp0"

:: 后台静默启动，不显示命令行窗口
start /min "" cmd /c "python server.py"

:: 等待服务启动后打开浏览器
timeout /t 4 /nobreak >nul
start http://localhost:5000
