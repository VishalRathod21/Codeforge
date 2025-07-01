# Contributing to CodeForge

First off, thank you for considering contributing to CodeForge! We appreciate your time and effort in making this project better.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Code Style](#code-style)
- [License](#license)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

- **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/VishalRathod21/Codeforge/issues).
- If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/VishalRathod21/Codeforge/issues/new). Be sure to include:
  - A clear and descriptive title
  - A description of the expected behavior and the observed behavior
  - Steps to reproduce the issue
  - Any relevant screenshots or logs

### Suggesting Enhancements

- Use GitHub Issues to submit enhancement suggestions
- Clearly describe the enhancement and why it would be useful
- Include any relevant code, mockups, or design assets

### Your First Code Contribution

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Add tests if applicable
5. Ensure all tests pass
6. Submit a pull request

## Development Setup

1. Fork and clone the repository
   ```bash
   git clone https://github.com/your-username/Codeforge.git
   cd Codeforge
   ```

2. Set up a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies
   ```bash
   pip install -e ".[dev]"
   pre-commit install
   ```

4. Create a `.env` file with your Groq API key
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a build.
2. Update the README.md with details of changes to the interface, including new environment variables, exposed ports, useful file locations, and container parameters.
3. Increase the version number in any examples files and the README.md to the new version that this Pull Request would represent.
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use [Black](https://github.com/psf/black) for code formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Include type hints for all function parameters and return values
- Write docstrings for all public functions and classes following [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)

## License

By contributing, you agree that your contributions will be licensed under its MIT License.
