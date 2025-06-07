# Contributing to Calculator App

Thank you for your interest in contributing to Calculator App! We welcome contributions from everyone.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- A GitHub account

### Setting Up Your Development Environment

1. **Fork the repository**
   - Click the "Fork" button on the GitHub repository page
   - Clone your fork locally:
     ```bash
     git clone https://github.com/YOUR_USERNAME/calculator.git
     cd calculator
     ```

2. **Set up the upstream remote**
   ```bash
   git remote add upstream https://github.com/botaoju/calculator.git
   ```

3. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -e ".[dev,security]"
   ```

5. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

## 🔄 Development Workflow

### Before Making Changes

1. **Sync with upstream**
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Making Changes

1. **Write your code**
   - Follow the coding standards outlined below
   - Add tests for new functionality
   - Update documentation as needed

2. **Run quality checks**
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
   
   # Run tests
   pytest
   ```

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

### Submitting Changes

1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request**
   - Go to the GitHub repository page
   - Click "New Pull Request"
   - Select your feature branch
   - Fill out the PR template

## 📝 Coding Standards

### Python Code Style

- **PEP 8**: Follow Python's official style guide
- **Black**: Use Black for code formatting (line length: 127)
- **isort**: Use isort for import sorting
- **Type Hints**: Add type hints for function parameters and return values
- **Docstrings**: Use Google-style docstrings for functions and classes

### Example Code Style

```python
from typing import Optional, Union

def calculate_result(expression: str, precision: int = 2) -> Optional[Union[int, float]]:
    """Calculate the result of a mathematical expression.
    
    Args:
        expression: The mathematical expression to evaluate
        precision: Number of decimal places for the result
        
    Returns:
        The calculated result or None if invalid
        
    Raises:
        ValueError: If the expression is invalid
    """
    try:
        result = eval(expression)  # Note: Use safe evaluation in production
        return round(result, precision)
    except (SyntaxError, ZeroDivisionError) as e:
        raise ValueError(f"Invalid expression: {e}") from e
```

### Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/) format:

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `ci`: CI/CD changes

**Examples:**
- `feat(calculator): add scientific functions`
- `fix(ui): resolve button alignment issue`
- `docs(readme): update installation instructions`

## 🧪 Testing

### Writing Tests

- Write unit tests for all new functions
- Use pytest for testing framework
- Aim for high test coverage (>90%)
- Test both positive and negative cases

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_calculator.py

# Run with verbose output
pytest -v
```

### Test Structure

```python
import pytest
from calculator import Calculator

class TestCalculator:
    """Test cases for Calculator class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calculator = Calculator()
    
    def test_addition(self):
        """Test basic addition functionality."""
        result = self.calculator.add(2, 3)
        assert result == 5
    
    def test_division_by_zero(self):
        """Test division by zero raises appropriate error."""
        with pytest.raises(ZeroDivisionError):
            self.calculator.divide(5, 0)
```

## 📚 Documentation

### Code Documentation

- Use clear, descriptive variable and function names
- Add docstrings to all public functions and classes
- Include type hints for better code understanding
- Comment complex algorithms or business logic

### README Updates

- Update README.md if you add new features
- Include usage examples for new functionality
- Update installation instructions if needed

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Clear description** of the problem
2. **Steps to reproduce** the issue
3. **Expected behavior** vs **actual behavior**
4. **Screenshots** (if applicable)
5. **System information**:
   - Operating System
   - Python version
   - App version
   - Relevant dependencies

## 💡 Feature Requests

When suggesting new features:

1. **Describe the feature** clearly
2. **Explain the use case** and benefits
3. **Provide examples** of how it would work
4. **Consider implementation** complexity

## 🔍 Code Review Process

### For Contributors

- Ensure all checks pass before requesting review
- Respond to feedback promptly and professionally
- Make requested changes in additional commits
- Keep PRs focused and reasonably sized

### Review Criteria

- **Functionality**: Does the code work as intended?
- **Code Quality**: Is the code clean, readable, and well-structured?
- **Tests**: Are there adequate tests with good coverage?
- **Documentation**: Is the code properly documented?
- **Performance**: Are there any performance implications?
- **Security**: Are there any security concerns?

## 🏷️ Release Process

1. **Version Bumping**: Follow semantic versioning (MAJOR.MINOR.PATCH)
2. **Changelog**: Update CHANGELOG.md with new features and fixes
3. **Testing**: Ensure all tests pass and manual testing is complete
4. **Tagging**: Create a git tag for the release
5. **GitHub Release**: Create a GitHub release with release notes

## 📞 Getting Help

If you need help or have questions:

- 💬 **Discussions**: Use [GitHub Discussions](https://github.com/botaoju/calculator/discussions)
- 🐛 **Issues**: Create an issue for bugs or feature requests
- 📧 **Email**: Contact maintainers directly for sensitive issues

## 📜 Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please:

- **Be respectful** and considerate in all interactions
- **Be collaborative** and help others learn
- **Be patient** with newcomers and different skill levels
- **Focus on constructive feedback** rather than criticism
- **Respect different viewpoints** and experiences

## 🎉 Recognition

Contributors will be recognized in:

- **README.md**: Listed in the contributors section
- **Release Notes**: Mentioned in relevant releases
- **GitHub**: Contributor status on the repository

Thank you for contributing to Calculator App! 🚀