#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Android APK构建脚本
使用Buildozer将Kivy应用打包成Android APK
"""

import os
import sys
import subprocess
import platform

def check_system():
    """检查系统环境"""
    print("🔍 检查系统环境...")
    
    system = platform.system()
    if system == "Windows":
        print("❌ Windows系统不支持直接构建Android APK")
        print("📋 推荐方案:")
        print("1. 使用WSL2 (Windows Subsystem for Linux)")
        print("2. 使用虚拟机运行Linux")
        print("3. 使用在线构建服务 (如GitHub Actions)")
        print("4. 使用Docker容器")
        return False
    elif system == "Linux":
        print("✅ Linux系统，支持构建Android APK")
        return True
    elif system == "Darwin":
        print("✅ macOS系统，支持构建Android APK")
        return True
    else:
        print(f"❓ 未知系统: {system}")
        return False

def install_dependencies():
    """安装构建依赖"""
    print("\n📦 安装构建依赖...")
    
    dependencies = [
        'buildozer',
        'kivy[base]',
        'kivymd',
        'cython'
    ]
    
    for dep in dependencies:
        print(f"安装 {dep}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            print(f"✅ {dep} 安装成功")
        except subprocess.CalledProcessError:
            print(f"❌ {dep} 安装失败")
            return False
    
    return True

def check_android_tools():
    """检查Android开发工具"""
    print("\n🔧 检查Android开发工具...")
    
    # 检查Java
    try:
        result = subprocess.run(['java', '-version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Java已安装")
        else:
            print("❌ Java未安装")
            return False
    except FileNotFoundError:
        print("❌ Java未安装")
        return False
    
    # 检查Android SDK环境变量
    android_home = os.environ.get('ANDROID_HOME') or os.environ.get('ANDROID_SDK_ROOT')
    if android_home:
        print(f"✅ Android SDK路径: {android_home}")
    else:
        print("⚠️  未设置ANDROID_HOME环境变量")
        print("buildozer会自动下载Android SDK")
    
    return True

def build_apk():
    """构建APK"""
    print("\n🏗️  开始构建Android APK...")
    
    # 检查buildozer.spec文件
    if not os.path.exists('buildozer.spec'):
        print("❌ 找不到buildozer.spec文件")
        return False
    
    # 检查main.py文件
    if not os.path.exists('main.py'):
        print("❌ 找不到main.py文件")
        return False
    
    try:
        # 初始化buildozer（首次运行）
        print("初始化buildozer...")
        subprocess.run(['buildozer', 'android', 'clean'], check=False)
        
        # 构建debug版本APK
        print("构建debug APK...")
        result = subprocess.run(['buildozer', 'android', 'debug'], 
                              capture_output=False, text=True)
        
        if result.returncode == 0:
            print("\n🎉 APK构建成功！")
            
            # 查找生成的APK文件
            bin_dir = './bin'
            if os.path.exists(bin_dir):
                apk_files = [f for f in os.listdir(bin_dir) if f.endswith('.apk')]
                if apk_files:
                    apk_path = os.path.join(bin_dir, apk_files[0])
                    apk_size = os.path.getsize(apk_path) / (1024 * 1024)
                    print(f"📱 APK文件: {os.path.abspath(apk_path)}")
                    print(f"📊 文件大小: {apk_size:.1f} MB")
                    print(f"🎯 支持Android 5.0+ (API 21+)")
                    
                    print("\n📋 安装说明:")
                    print("1. 将APK文件传输到Android设备")
                    print("2. 在设备上启用'未知来源'安装")
                    print("3. 点击APK文件进行安装")
                    
                    return True
            
            print("⚠️  APK文件未找到")
            return False
        else:
            print("❌ APK构建失败")
            return False
            
    except FileNotFoundError:
        print("❌ buildozer命令未找到，请先安装buildozer")
        return False
    except Exception as e:
        print(f"❌ 构建过程中出现错误: {e}")
        return False

def create_github_workflow():
    """创建GitHub Actions工作流"""
    print("\n📝 创建GitHub Actions工作流...")
    
    workflow_dir = '.github/workflows'
    os.makedirs(workflow_dir, exist_ok=True)
    
    workflow_content = '''name: Build Android APK

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install buildozer kivy[base] kivymd cython
        sudo apt-get update
        sudo apt-get install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
    
    - name: Build APK
      run: |
        buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: calculator-apk
        path: bin/*.apk
'''
    
    workflow_file = os.path.join(workflow_dir, 'build-android.yml')
    with open(workflow_file, 'w', encoding='utf-8') as f:
        f.write(workflow_content)
    
    print(f"✅ GitHub Actions工作流已创建: {workflow_file}")
    print("💡 提交到GitHub后会自动构建APK")

def main():
    print("=" * 60)
    print("🤖 Android计算器APK构建工具")
    print("=" * 60)
    
    # 检查系统环境
    if not check_system():
        print("\n💡 替代方案:")
        print("1. 使用GitHub Actions在线构建 (推荐)")
        print("2. 使用WSL2或虚拟机")
        
        choice = input("\n是否创建GitHub Actions工作流? (y/n): ").lower().strip()
        if choice in ['y', 'yes', '是']:
            create_github_workflow()
        return
    
    # 检查必要文件
    required_files = ['main.py', 'calculator_mobile.py', 'buildozer.spec']
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ 找不到必要文件: {file}")
            return
    
    print("✅ 所有必要文件都存在")
    
    # 安装依赖
    if not install_dependencies():
        print("❌ 依赖安装失败")
        return
    
    # 检查Android工具
    if not check_android_tools():
        print("⚠️  Android工具检查失败，但buildozer会自动处理")
    
    # 构建APK
    success = build_apk()
    
    if success:
        print("\n🎉 构建完成！")
    else:
        print("\n❌ 构建失败")
        print("\n💡 故障排除:")
        print("1. 检查网络连接")
        print("2. 确保有足够的磁盘空间 (至少5GB)")
        print("3. 查看构建日志中的错误信息")
        print("4. 尝试运行: buildozer android clean")

if __name__ == '__main__':
    main()