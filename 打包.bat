@echo off
chcp 65001 >nul
echo ========================================
echo        Python计算器打包工具
echo ========================================
echo.
echo 正在启动打包程序...
echo.
python build_exe.py
echo.
echo 按任意键退出...
pause >nul