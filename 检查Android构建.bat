@echo off
chcp 65001 >nul
echo ========================================
echo      Android APK构建检查工具
echo ========================================
echo.
echo 正在检查Android构建环境...
echo.
python build_android.py
echo.
echo 按任意键退出...
pause >nul