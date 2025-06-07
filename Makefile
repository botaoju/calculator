# Makefile for Calculator App
# Provides convenient commands for development tasks

.PHONY: help install install-dev clean format lint test security build-android run docs

# Default target
help:
	@echo "Calculator App - Development Commands"
	@echo ""
	@echo "Available commands:"
	@echo "  install      Install production dependencies"
	@echo "  install-dev  Install development dependencies"
	@echo "  clean        Clean build artifacts and cache"
	@echo "  format       Format code with black and isort"
	@echo "  lint         Run all linting tools"
	@echo "  test         Run tests with coverage"
	@echo "  security     Run security scans"
	@echo "  build-android Build Android APK"
	@echo "  run          Run the application"
	@echo "  docs         Generate documentation"
	@echo "  pre-commit   Install pre-commit hooks"
	@echo "  check-all    Run all quality checks"

# Installation
install:
	@echo "Installing production dependencies..."
	pip install -r requirements.txt

install-dev:
	@echo "Installing development dependencies..."
	pip install -r requirements.txt
	pip install -r requirements_dev.txt
	pip install -e .

# Cleaning
clean:
	@echo "Cleaning build artifacts and cache..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .buildozer/
	rm -rf bin/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

# Code formatting
format:
	@echo "Formatting code..."
	black .
	isort .
	autoflake --in-place --remove-all-unused-imports --remove-unused-variables --recursive .

# Linting
lint:
	@echo "Running linting tools..."
	flake8 .
	pylint **/*.py || true
	mypy .
	pydocstyle . || true

# Testing
test:
	@echo "Running tests with coverage..."
	pytest --cov=. --cov-report=html --cov-report=term-missing

# Security scanning
security:
	@echo "Running security scans..."
	bandit -r . -ll
	safety check

# Android build
build-android:
	@echo "Building Android APK..."
	buildozer android debug

# Run application
run:
	@echo "Starting Calculator App..."
	python main.py

# Documentation
docs:
	@echo "Generating documentation..."
	@echo "Documentation generation not yet implemented"

# Pre-commit hooks
pre-commit:
	@echo "Installing pre-commit hooks..."
	pre-commit install
	pre-commit install --hook-type commit-msg

# Run all quality checks
check-all: format lint test security
	@echo "All quality checks completed!"

# Development setup
setup-dev: install-dev pre-commit
	@echo "Development environment setup complete!"

# Quick development cycle
dev: format lint test
	@echo "Development cycle complete!"

# Release preparation
release-check: clean check-all build-android
	@echo "Release checks completed!"

# Show project status
status:
	@echo "Project Status:"
	@echo "Python version: $$(python --version)"
	@echo "Pip version: $$(pip --version)"
	@echo "Git status:"
	git status --short
	@echo "Dependencies status:"
	pip list --outdated