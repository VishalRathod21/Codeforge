# CodeForge 🏗️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI](https://img.shields.io/pypi/v/codeforge)](https://pypi.org/project/codeforge/)
[![Documentation](https://img.shields.io/badge/docs-available-brightgreen)](https://vishalrathod21.github.io/Codeforge/)

> **CodeForge** is an AI-powered project scaffolding tool that transforms your natural language descriptions into fully functional, production-ready project structures. Designed for developers who value efficiency, it automates the tedious setup process so you can focus on writing great code.

## 🌟 Key Features

- **AI-Powered Generation**: Convert natural language descriptions into complete project structures
- **Multi-Language Support**: Supports various programming languages and frameworks
- **Smart Templates**: Pre-configured templates for different project types (Web, API, ML, etc.)
- **Git Integration**: Automatic Git repository initialization with .gitignore
- **Dependency Management**: Automatic dependency detection and requirements.txt generation
- **Customizable**: Extend with your own templates and configurations

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- [Groq API key](https://console.groq.com/) for AI features

### Install via pip (Recommended)
```bash
pip install codeforge
```

### Install from Source
```bash
# Clone the repository
git clone https://github.com/VishalRathod21/Codeforge.git
cd Codeforge

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements.txt
```

### Verify Installation
```bash
codeforge --version
```

## 🚀 Quick Start

1. **Install CodeForge**:
   ```bash
   pip install codeforge
   ```

2. **Set up your API key**:
   ```bash
   # Linux/macOS
   echo 'GROQ_API_KEY=your_api_key_here' > ~/.codeforge/.env
   
   # Windows
   echo GROQ_API_KEY=your_api_key_here > %USERPROFILE%\.codeforge\.env
   ```

3. **Create your first project**:
   ```bash
   codeforge create "A Python web app with FastAPI and React"
   ```

## 🛠️ Commands Reference

### `codeforge create`
Generate a new project from a description.

```bash
codeforge create "Project description" [OPTIONS]
```

**Options:**
- `-o, --output PATH`: Output directory (default: current directory)
- `-t, --template TEXT`: Specify a template (web, api, ml, etc.)
- `-f, --force`: Overwrite existing files
- `--no-git`: Skip Git repository initialization
- `--author TEXT`: Set project author
- `--license TEXT`: Set project license (MIT, Apache-2.0, etc.)
- `--python-version TEXT`: Set Python version (e.g., 3.10)

**Examples:**
```bash
# Basic usage
codeforge create "A REST API with FastAPI and PostgreSQL"

# Specify output directory and template
codeforge create "A machine learning project" -o ./ml-project -t ml

# With additional options
codeforge create "A web app with React and FastAPI" \
  --author "Your Name <email@example.com>" \
  --license MIT \
  --python-version 3.10
```

### `codeforge list-templates`
List all available project templates.

```bash
codeforge list-templates
```

### `codeforge version`
Show the current version of CodeForge.

```bash
codeforge version
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GROQ_API_KEY` | Required for AI features | - |
| `CODEFORGE_TEMPLATE_DIR` | Custom templates directory | `~/.codeforge/templates/` |
| `CODEFORGE_CACHE_DIR` | Cache directory | `~/.codeforge/cache/` |

### Configuration File
Create `~/.codeforge/config.yaml` to customize default settings:

```yaml
defaults:
  author: "Your Name <email@example.com>"
  license: "MIT"
  python_version: "3.10"
  git_init: true

templates:
  - name: web
    description: "Full-stack web application"
    default: true
  - name: api
    description: "REST API service"
  - name: ml
    description: "Machine Learning project"
```

## 🏗️ Project Structure

```
codeforge/
├── main.py                  # CLI entry point
├── llm_agent.py            # AI integration with Groq
├── structure_generator.py   # Project structure generation
├── templates/              # Project templates
│   ├── web/               # Web application template
│   ├── api/               # API service template
│   └── ml/                # Machine learning template
└── utils/                 # Utility functions
    ├── file_utils.py      # File operations
    └── config_utils.py    # Configuration handling
```

## 🧪 Testing

Run the test suite to ensure everything works as expected:

```bash
# Install test dependencies
pip install -e ".[test]"

# Run tests
pytest

# Run with coverage report
pytest --cov=codeforge tests/
```

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. **Report Bugs**: Open an issue with detailed reproduction steps
2. **Suggest Features**: Share your ideas for new features
3. **Submit Pull Requests**: Follow these steps:
   ```bash
   # Fork the repository
   git clone https://github.com/your-username/Codeforge.git
   cd Codeforge
   
   # Create a new branch
   git checkout -b feature/your-feature
   
   # Make your changes and commit
   git commit -am 'Add some amazing feature'
   
   # Push to the branch
   git push origin feature/your-feature
   
   # Open a Pull Request
   ```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Additional Resources

- [Documentation](https://vishalrathod21.github.io/Codeforge/)
- [Issue Tracker](https://github.com/VishalRathod21/Codeforge/issues)
- [Changelog](CHANGELOG.md)

## 🙏 Acknowledgments

- Built with ❤️ using Python
- Powered by [Groq AI](https://groq.com/)
- Inspired by modern development tools and workflows

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/VishalRathod21">Vishal Rathod</a>
  <br>
  <a href="https://github.com/VishalRathod21/Codeforge">GitHub</a> • 
  <a href="https://twitter.com/yourhandle">Twitter</a> • 
  <a href="https://linkedin.com/in/yourprofile">LinkedIn</a>
</p>
