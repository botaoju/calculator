#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
计算器打包脚本
使用PyInstaller将calculator.py打包成独立的EXE程序
"""

import os
import sys
import subprocess

def install_pyinstaller():
    """安装PyInstaller"""
    print("正在检查PyInstaller...")
    try:
        import PyInstaller
        print("PyInstaller已安装")
        return True
    except ImportError:
        print("PyInstaller未安装，正在安装...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("PyInstaller安装成功")
            return True
        except subprocess.CalledProcessError:
            print("PyInstaller安装失败，请手动安装: pip install pyinstaller")
            return False

def build_exe():
    """构建EXE文件"""
    if not install_pyinstaller():
        return False
    
    print("正在打包计算器程序...")
    
    # PyInstaller命令参数
    cmd = [
        "pyinstaller",
        "--onefile",  # 打包成单个文件
        "--windowed",  # 不显示控制台窗口
        "--name=计算器",  # 设置程序名称
        "--icon=calculator.ico",  # 图标文件（如果存在）
        "--add-data=README.md;.",  # 包含README文件
        "--distpath=dist",  # 输出目录
        "--workpath=build",  # 工作目录
        "--specpath=.",  # spec文件位置
        "calculator.py"  # 主程序文件
    ]
    
    # 如果没有图标文件，移除图标参数
    if not os.path.exists("calculator.ico"):
        cmd = [arg for arg in cmd if not arg.startswith("--icon")]
    
    try:
        # 设置环境变量以避免编码问题
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        
        # 执行打包命令，使用实时输出
        print("开始执行PyInstaller...")
        process = subprocess.Popen(
            cmd, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            encoding='utf-8',
            errors='replace',
            env=env
        )
        
        # 实时显示输出
        output_lines = []
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
                output_lines.append(output)
        
        return_code = process.poll()
        
        if return_code == 0:
            print("\n✅ 打包成功！")
            print(f"EXE文件位置: {os.path.abspath('dist/计算器.exe')}")
            print("\n📁 文件结构:")
            print("├── dist/")
            print("│   └── 计算器.exe  (可执行文件)")
            print("├── build/  (临时文件，可删除)")
            print("└── 计算器.spec  (打包配置文件)")
            
            # 检查文件大小
            exe_path = "dist/计算器.exe"
            if os.path.exists(exe_path):
                size_mb = os.path.getsize(exe_path) / (1024 * 1024)
                print(f"\n📊 文件大小: {size_mb:.1f} MB")
            
            print("\n🎉 现在可以直接运行 dist/计算器.exe")
            return True
        else:
            print("❌ 打包失败")
            print("完整输出:")
            for line in output_lines[-20:]:  # 显示最后20行
                print(line.strip())
            return False
            
    except Exception as e:
        print(f"❌ 打包过程中出现错误: {e}")
        return False

def clean_build():
    """清理构建文件"""
    import shutil
    
    dirs_to_clean = ['build', '__pycache__']
    files_to_clean = ['计算器.spec']
    
    print("\n🧹 清理构建文件...")
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"已删除目录: {dir_name}")
    
    for file_name in files_to_clean:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"已删除文件: {file_name}")

if __name__ == "__main__":
    print("=" * 50)
    print("🔧 Python计算器打包工具")
    print("=" * 50)
    
    # 检查主程序文件
    if not os.path.exists("calculator.py"):
        print("❌ 找不到calculator.py文件")
        sys.exit(1)
    
    # 构建EXE
    success = build_exe()
    
    if success:
        # 询问是否清理构建文件
        while True:
            choice = input("\n是否清理构建文件? (y/n): ").lower().strip()
            if choice in ['y', 'yes', '是']:
                clean_build()
                break
            elif choice in ['n', 'no', '否']:
                print("保留构建文件")
                break
            else:
                print("请输入 y 或 n")
    
    print("\n完成！")