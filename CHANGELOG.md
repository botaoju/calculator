# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive GitHub Actions CI/CD pipeline
- Security and quality checks workflow
- Dependabot configuration for automated dependency updates
- Modern Python project configuration with pyproject.toml
- Code quality tools configuration (.flake8, black, isort, etc.)
- Comprehensive documentation (README, CONTRIBUTING, LICENSE)
- Pre-commit hooks support
- Android build optimization with caching
- Network retry mechanisms for build stability

### Changed
- Updated Android API level from 30 to 33
- Updated Android NDK from 25b to 25c
- Improved buildozer.spec configuration
- Enhanced GitHub Actions workflow with better error handling
- Modernized project structure and documentation

### Fixed
- Android build issues with missing dependencies
- Network connectivity problems in CI/CD
- Buildozer configuration inconsistencies
- Missing system dependencies for Android builds

### Security
- Added security scanning with Bandit
- Added dependency vulnerability scanning with Safety
- Implemented secure build practices
- Added proper permissions to GitHub Actions workflows

## [1.0.0] - 2024-01-XX

### Added
- Initial release of Calculator App
- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Scientific calculator functions
- Material Design UI with KivyMD
- Cross-platform support (Android, iOS, Windows, macOS, Linux)
- Responsive design for different screen sizes
- Memory functions
- Calculation history
- Dark/light theme support

### Technical Features
- Built with Python, Kivy, and KivyMD
- Buildozer configuration for Android builds
- GitHub Actions for automated builds
- Comprehensive test suite
- Code quality tools integration

---

## Release Types

- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for any bug fixes
- **Security** for vulnerability fixes

## Version Numbering

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version when you make incompatible API changes
- **MINOR** version when you add functionality in a backwards compatible manner
- **PATCH** version when you make backwards compatible bug fixes

## Links

- [Repository](https://github.com/botaoju/calculator)
- [Issues](https://github.com/botaoju/calculator/issues)
- [Releases](https://github.com/botaoju/calculator/releases)