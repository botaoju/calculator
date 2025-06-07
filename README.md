# Calculator App 🧮

A modern, feature-rich scientific calculator built with Python, Kivy, and KivyMD. This app provides a beautiful Material Design interface with comprehensive mathematical functions.

## ✨ Features

- **Basic Operations**: Addition, subtraction, multiplication, division
- **Scientific Functions**: Trigonometric, logarithmic, exponential functions
- **Advanced Features**: Memory functions, history, parentheses support
- **Modern UI**: Material Design interface with dark/light theme support
- **Cross-Platform**: Runs on Android, iOS, Windows, macOS, and Linux
- **Responsive Design**: Adapts to different screen sizes

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/botaoju/calculator.git
   cd calculator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 🔧 Development Setup

### Install Development Dependencies

```bash
pip install -e ".[dev,security]"
```

### Code Quality Tools

This project uses several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **pylint**: Advanced linting
- **bandit**: Security scanning
- **safety**: Dependency vulnerability scanning

### Running Quality Checks

```bash
# Format code
black .
isort .

# Lint code
flake8 .
pylint **/*.py

# Type checking
mypy .

# Security checks
bandit -r .
safety check
```

## 📱 Building for Android

### Prerequisites

- Java Development Kit (JDK) 11
- Android SDK
- Android NDK 25c
- Buildozer

### Build Steps

1. **Install Buildozer**
   ```bash
   pip install buildozer
   ```

2. **Build APK**
   ```bash
   buildozer android debug
   ```

3. **Build Release APK**
   ```bash
   buildozer android release
   ```

### GitHub Actions

This project includes automated CI/CD pipelines:

- **Build Android APK**: Automatically builds APK on push to main branch
- **Security & Quality Checks**: Runs code quality and security scans

## 🏗️ Project Structure

```
calculator/
├── .github/
│   └── workflows/          # GitHub Actions workflows
├── main.py                 # Main application entry point
├── buildozer.spec         # Buildozer configuration
├── requirements.txt       # Python dependencies
├── pyproject.toml        # Modern Python project configuration
├── .gitignore            # Git ignore rules
├── .flake8               # Flake8 configuration
└── README.md             # This file
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Run quality checks**
5. **Commit your changes**
6. **Push to your branch**
7. **Open a Pull Request**

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [Kivy](https://kivy.org/) - Amazing cross-platform framework
- [KivyMD](https://kivymd.readthedocs.io/) - Beautiful Material Design components
- [Material Design](https://material.io/) - Design system inspiration

## 功能特点

### 基本运算
- ✅ 加法 (+)
- ✅ 减法 (-)
- ✅ 乘法 (×)
- ✅ 除法 (÷)
- ✅ 小数点运算
- ✅ 负数处理

### 高级功能
- ✅ 平方根 (√)
- ✅ 平方 (x²)
- ✅ 倒数 (1/x)
- ✅ 正负号切换 (±)
- ✅ 退格删除 (⌫)
- ✅ 清除当前输入 (CE)
- ✅ 全部清除 (C)

### 历史记录功能
- ✅ 自动保存计算历史
- ✅ 双击历史记录重新使用
- ✅ 一键清除所有历史记录
- ✅ 实时显示计算过程

### 用户界面
- ✅ 现代化深色主题
- ✅ 响应式按钮设计
- ✅ 清晰的数字和运算符显示
- ✅ 实时计算预览
- ✅ 错误提示对话框

### 键盘支持
- ✅ 数字键 (0-9)
- ✅ 运算符键 (+, -, *, /)
- ✅ 小数点键 (.)
- ✅ 回车键计算 (Enter)
- ✅ 退格键删除 (Backspace)
- ✅ C键清除

## 使用方法

### 启动程序
```bash
python calculator.py
```

### 基本操作
1. **数字输入**: 点击数字按钮或使用键盘输入
2. **运算**: 点击运算符按钮进行计算
3. **等号**: 点击 = 按钮或按Enter键获得结果
4. **清除**: 使用C键清除所有，CE键清除当前输入

### 历史记录
1. **查看历史**: 所有计算结果自动保存在下方历史记录区域
2. **重用历史**: 双击任意历史记录项可重新加载该表达式
3. **清除历史**: 点击"清除历史"按钮删除所有历史记录

### 高级功能
1. **平方根**: 点击√按钮计算当前数值的平方根
2. **平方**: 点击x²按钮计算当前数值的平方
3. **倒数**: 点击1/x按钮计算当前数值的倒数
4. **符号切换**: 点击±按钮切换正负号

## 技术特点

- **安全计算**: 使用安全的表达式评估，防止恶意代码执行
- **错误处理**: 完善的异常处理机制，友好的错误提示
- **实时预览**: 输入过程中实时显示计算结果
- **内存管理**: 高效的历史记录管理
- **跨平台**: 基于tkinter，支持Windows、macOS、Linux

## 系统要求

- Python 3.6+
- tkinter (通常随Python安装)
- math模块 (Python标准库)

## 文件结构

```
jisuanqi/
├── calculator.py    # 主程序文件
└── README.md       # 说明文档
```

## 界面预览

计算器采用现代化深色主题设计：
- 深蓝色主背景 (#2c3e50)
- 灰蓝色显示区域 (#34495e)
- 蓝色数字按钮 (#3498db)
- 橙色运算符按钮 (#e67e22)
- 灰色功能按钮 (#95a5a6)
- 红色清除按钮 (#e74c3c)

## 打包成EXE程序

### 方法一：使用批处理文件（推荐）
1. 双击运行 `打包.bat` 文件
2. 等待打包完成
3. 在 `dist` 文件夹中找到 `计算器.exe`

### 方法二：手动打包
1. 安装依赖：`pip install -r requirements.txt`
2. 运行打包脚本：`python build_exe.py`
3. 等待打包完成

### 打包后的文件结构
```
├── dist/
│   └── 计算器.exe  (可执行文件，约15-20MB)
├── build/  (临时文件，可删除)
└── 计算器.spec  (打包配置文件)
```

### 注意事项
- 打包后的EXE文件可以在没有Python环境的Windows系统上运行
- 首次运行可能需要几秒钟启动时间
- 文件大小约15-20MB，包含了所有必要的运行库
- 可以将EXE文件复制到任何位置独立运行

## 打包成Android APK

### 🤖 支持的Android版本
- **最低支持**: Android 5.0 (API 21)
- **目标版本**: Android 11 (API 30)
- **推荐版本**: Android 9.0+ 以获得最佳体验

### 📱 构建方法

#### 方法一：GitHub Actions在线构建（推荐）
1. 将项目上传到GitHub仓库
2. GitHub Actions会自动构建APK
3. 在Actions页面下载构建好的APK文件
4. 支持自动发布到Release

#### 方法二：本地构建（Linux/macOS）
```bash
# 安装依赖
pip install -r requirements_android.txt

# 运行构建脚本
python build_android.py

# 或直接使用buildozer
buildozer android debug
```

#### 方法三：Docker构建
```bash
# 使用官方buildozer Docker镜像
docker run --rm -v "$(pwd)":/home/user/hostcwd kivy/buildozer android debug
```

### 📋 构建要求
- **操作系统**: Linux或macOS（Windows需要WSL2）
- **Python版本**: 3.7-3.9
- **磁盘空间**: 至少5GB可用空间
- **内存**: 建议4GB以上
- **网络**: 稳定的网络连接（下载Android SDK等）

### 📦 APK特性
- **文件大小**: 约20-30MB
- **权限**: 无需特殊权限
- **架构**: 支持ARM64和ARMv7
- **安装**: 支持侧载安装

### 🔧 构建文件说明
- `main.py` - Android应用入口文件
- `calculator_mobile.py` - 移动端计算器实现（基于Kivy）
- `buildozer.spec` - Android构建配置文件
- `build_android.py` - 本地构建脚本
- `requirements_android.txt` - Android构建依赖
- `.github/workflows/build-android.yml` - GitHub Actions工作流

### 📱 安装说明
1. 下载构建好的APK文件
2. 在Android设备上启用"未知来源"安装
3. 传输APK到设备并点击安装
4. 首次启动可能需要几秒钟加载时间

## 开发说明

本项目使用Python 3.x开发，主要使用了以下技术：
- tkinter：GUI界面开发
- math：数学函数计算
- PyInstaller：打包成独立可执行文件
- 面向对象编程：代码结构清晰，易于维护

本计算器使用面向对象设计，主要包含以下组件：

1. **Calculator类**: 主计算器类，管理所有功能
2. **界面组件**: 显示屏、按钮、历史记录列表
3. **计算引擎**: 安全的数学表达式评估
4. **事件处理**: 按钮点击和键盘输入处理
5. **历史管理**: 计算历史的存储和管理

代码结构合理，注释详细，适合学习和二次开发。

## 许可证

本项目为开源项目，可自由使用和修改。