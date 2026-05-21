@echo off
chcp 65001 >nul
title 彩票分析系统
echo ========================================
echo        彩票分析系统 - 启动中...
echo ========================================
echo.

cd /d "%~dp0"

:: 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到 Python，请先安装 Python 3.8+
    pause
    exit /b 1
)

:: 检查依赖
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo [INFO] 正在安装依赖...
    python -m pip install flask requests beautifulsoup4 lxml waitress
)

echo [INFO] 启动服务器...
echo [INFO] 浏览器将自动打开 http://localhost:5000
echo [INFO] 关闭此窗口将停止服务
echo.

:: 延迟3秒后自动打开浏览器
start "" cmd /c "timeout /t 3 /nobreak >nul && start http://localhost:5000"

:: 启动服务器（前台运行，关闭窗口即停止）
python server.py

pause
