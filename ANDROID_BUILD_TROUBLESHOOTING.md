# Android Build Troubleshooting Guide

本指南帮助解决 Android APK 构建过程中的常见问题。

## 🚨 常见构建错误及解决方案

### 1. Buildozer 退出代码 1

**错误信息:**
```
Buildozer failed to execute the last command
The error might be hidden in the log above this error
Error: Process completed with exit code 1
```

**解决方案:**

#### A. 清理构建缓存
```bash
buildozer android clean
rm -rf .buildozer
rm -rf bin
```

#### B. 检查依赖版本兼容性
确保使用兼容的版本组合:
```
kivy==2.1.0
kivymd==1.1.1
buildozer==1.5.0
cython==0.29.36
```

#### C. 更新 buildozer.spec 配置
```ini
# 使用稳定的 API 级别
android.api = 31
android.minapi = 21
android.ndk = 23c

# 添加必要权限
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# 启用 AndroidX
android.enable_androidx = True
```

### 2. Android SDK/NDK 问题

**错误信息:**
- SDK 路径不存在
- NDK 版本不兼容
- 构建工具版本错误

**解决方案:**

#### A. 手动设置环境变量
```bash
export ANDROID_HOME=/path/to/android-sdk
export ANDROID_NDK_HOME=/path/to/android-ndk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
```

#### B. 安装正确的 SDK 组件
```bash
sdkmanager "build-tools;31.0.0"
sdkmanager "platforms;android-31"
sdkmanager "platform-tools"
sdkmanager "ndk;23.2.8568313"
```

### 3. 依赖冲突问题

**错误信息:**
- 包版本冲突
- 导入错误
- 模块未找到

**解决方案:**

#### A. 使用虚拟环境
```bash
python -m venv buildenv
source buildenv/bin/activate  # Linux/macOS
# 或
buildenv\Scripts\activate  # Windows

pip install -r requirements_android.txt
```

#### B. 固定依赖版本
在 `requirements_android.txt` 中使用精确版本:
```
kivy==2.1.0
kivymd==1.1.1
buildozer==1.5.0
cython==0.29.36
python-for-android==2023.6.0
```

### 4. 内存不足问题

**错误信息:**
- Java heap space
- Out of memory
- Gradle daemon 错误

**解决方案:**

#### A. 增加 Gradle 内存
```bash
export GRADLE_OPTS="-Xmx4096m -Dorg.gradle.daemon=false"
```

#### B. 在 buildozer.spec 中设置
```ini
[app]
# 减少并行编译
android.gradle_dependencies = 

[buildozer]
# 增加日志级别以便调试
log_level = 2
```

### 5. 网络连接问题

**错误信息:**
- 下载超时
- 连接被拒绝
- SSL 证书错误

**解决方案:**

#### A. 设置代理（如果需要）
```bash
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
```

#### B. 增加超时时间
```bash
export PIP_DEFAULT_TIMEOUT=300
```

#### C. 使用国内镜像源
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements_android.txt
```

## 🔧 调试技巧

### 1. 启用详细日志
在 `buildozer.spec` 中设置:
```ini
[buildozer]
log_level = 2
```

### 2. 分步构建
```bash
# 只初始化环境
buildozer android debug --verbose

# 清理后重新构建
buildozer android clean
buildozer android debug
```

### 3. 检查构建环境
```bash
# 检查 Python 环境
python --version
pip list

# 检查 Android 环境
echo $ANDROID_HOME
echo $ANDROID_NDK_HOME

# 检查可用的 Android 组件
sdkmanager --list
```

### 4. 使用构建脚本
运行项目提供的构建脚本:
```bash
python build_android.py debug
```

## 🌐 GitHub Actions 构建问题

### 1. 工作流失败

**检查项:**
- 确保所有依赖版本一致
- 检查 Android SDK/NDK 版本匹配
- 验证环境变量设置

### 2. 缓存问题

**解决方案:**
- 清理 GitHub Actions 缓存
- 更新缓存键值
- 重新运行工作流

### 3. 超时问题

**解决方案:**
- 增加工作流超时时间
- 优化构建步骤
- 使用更快的运行器

## 📋 构建前检查清单

- [ ] Python 3.8+ 已安装
- [ ] 虚拟环境已激活
- [ ] 依赖版本兼容
- [ ] buildozer.spec 配置正确
- [ ] Android SDK/NDK 已安装
- [ ] 环境变量已设置
- [ ] 网络连接正常
- [ ] 足够的磁盘空间（至少 10GB）
- [ ] 足够的内存（至少 8GB）

## 🆘 获取帮助

如果以上解决方案都无法解决问题，请:

1. **收集信息:**
   - 完整的错误日志
   - 系统信息（OS、Python 版本等）
   - buildozer.spec 配置
   - 依赖版本列表

2. **提交 Issue:**
   - 使用项目的 Issue 模板
   - 提供详细的重现步骤
   - 附上相关日志和配置文件

3. **社区资源:**
   - [Kivy 官方文档](https://kivy.org/doc/stable/)
   - [Buildozer 文档](https://buildozer.readthedocs.io/)
   - [KivyMD 文档](https://kivymd.readthedocs.io/)
   - [Python-for-Android 文档](https://python-for-android.readthedocs.io/)

## 📚 相关资源

- [Android 开发者文档](https://developer.android.com/docs)
- [Gradle 构建工具](https://gradle.org/guides/)
- [Android SDK 工具](https://developer.android.com/studio/command-line)
- [NDK 开发指南](https://developer.android.com/ndk/guides)