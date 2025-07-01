# CodeForge 🏗️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI](https://img.shields.io/pypi/v/codeforge)](https://pypi.org/project/codeforge/)
[![Downloads](https://static.pepy.tech/badge/codeforge/month)](https://pepy.tech/project/codeforge)

CodeForge is an intelligent CLI tool that generates complete, production-ready project structures using AI. Simply describe your project idea in natural language, and CodeForge will create a well-organized directory structure with all necessary files, configurations, and best practices.

## ✨ Features

- 🚀 **One-command project generation** - Start new projects in seconds
- 🎯 **Multi-language support** - Python, JavaScript, TypeScript, and more
- 🧩 **Template system** - Extensible templates for various project types
- 🤖 **AI-Powered** - Understands natural language project descriptions
- 📦 **Dependency management** - Automatic dependency detection and installation
- 🔄 **Git integration** - Automatic repository initialization with proper .gitignore
- 🛠️ **Configurable** - Customize templates and project structure
- 📝 **Documentation** - Auto-generated README and documentation

## 📦 Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git (optional but recommended)
- [Groq API key](https://console.groq.com/) (for AI features)

## 🚀 Installation

### Using pip (Recommended)
```bash
pip install codeforge
```

### Development Installation
```bash
# Clone the repository
git clone https://github.com/VishalRathod21/Codeforge.git
cd Codeforge

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with all dependencies
pip install -e ".[dev]"

# Set up pre-commit hooks
pre-commit install
```

## 🏁 Quick Start

1. **Configure your API key**:
   ```bash
   # Create a .env file in your project directory
   echo "GROQ_API_KEY=your_api_key_here" > .env
   ```
   Replace `your_api_key_here` with your actual Groq API key.

## 🛠️ Usage

### Basic Commands

```bash
# Show help
codeforge --help

# Show version
codeforge version
# or
codeforge --version

# List available templates
codeforge list-templates
```

### Creating a New Project

```bash
# Basic usage
codeforge create "A Python web app with FastAPI and React"

# Specify output directory
codeforge create "A data science project with PyTorch" --output ./my-ds-project

# Use a specific template
codeforge create "A CLI tool in Python" --template cli

# Force overwrite existing files
codeforge create "A REST API with Flask" --force

# Enable debug mode for troubleshooting
codeforge create "A machine learning project" --debug
```

### Available Templates

- `default` - Basic project structure
- `web` - Web application template (Frontend + Backend)
- `api` - REST API template
- `cli` - Command-line application template
- `ml` - Machine learning project template

## 📂 Project Structure

CodeForge generates a well-organized project structure based on best practices:

```
project-name/
├── .github/               # GitHub workflows and templates
├── docs/                  # Project documentation
├── src/                   # Source code
│   ├── __init__.py
│   └── main.py            # Main application entry point
├── tests/                 # Test files
├── .env.example           # Example environment variables
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
└── requirements.txt       # Project dependencies
```

## 🔧 Configuration

CodeForge can be configured using environment variables:

- `GROQ_API_KEY`: Your Groq API key (required for AI features)
- `CODEFORGE_TEMPLATE_DIR`: Custom templates directory
- `CODEFORGE_CACHE_DIR`: Directory for caching generated templates

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ using Python
- Powered by [Groq](https://groq.com/) for AI capabilities
- Inspired by modern project templates and best practices

## 📬 Contact

For questions or feedback, please open an issue on [GitHub](https://github.com/VishalRathod21/Codeforge/issues).
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   ```

2. **Create your first project**:
   ```bash
   codeforge create "A Python web application using FastAPI and React" --output my-project
   ```

3. **Navigate and explore**:
   ```bash
   cd my-project
   ls -la
   ```

## 📚 Usage

### Basic Commands

```bash
# Create a new project
codeforge create "Project description" --output project-name

# Show help
codeforge --help

# Show version
codeforge --version
```

### Project Generation Options

```bash
# Specify a template
codeforge create "Project description" --template python-fastapi --output my-api

# Skip git initialization
codeforge create "Project" --no-git --output my-project

# Set project author and license
codeforge create "Project" --author "Your Name <email@example.com>" --license MIT --output my-project

# Generate with specific Python version
codeforge create "Project" --python-version 3.10 --output my-project
```

## 🎯 Examples

### Web Applications

```bash
# Full-stack application
codeforge create "A blog with user authentication using FastAPI and React" --output blog-app

# REST API
codeforge create "REST API for a todo app with FastAPI and PostgreSQL" --output todo-api

# Static website
codeforge create "A personal portfolio website with HTML, CSS, and JavaScript" --output portfolio
```

### Data Science & ML

```bash
# Machine learning project
codeforge create "Image classification with PyTorch and torchvision" --output image-classifier

# Data analysis project
codeforge create "Data analysis of sales data with pandas and matplotlib" --output sales-analysis

# ML API service
codeforge create "ML model serving API with FastAPI and scikit-learn" --output ml-api
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in your project root:

```env
# Required for AI features
GROQ_API_KEY=your_groq_api_key_here

# Default project settings
DEFAULT_AUTHOR="Your Name <email@example.com>"
DEFAULT_LICENSE=MIT
DEFAULT_PYTHON_VERSION=3.9
```

### Global Configuration

Create `~/.config/codeforge/config.yaml` for global settings:

```yaml
defaults:
  author: "Your Name <email@example.com>"
  license: "MIT"
  python_version: "3.9"
  
templates:
  - name: python-fastapi
    description: "Python FastAPI web application"
    default: true
  - name: react-app
    description: "React application with Vite"
  - name: data-science
    description: "Jupyter-based data science project"
```

## 🧪 Testing

Run the test suite:

```bash
# Install test dependencies
pip install -e ".[test]"

# Run tests
pytest

# Run with coverage
pytest --cov=codeforge tests/
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to contribute to the project.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ using Python
- Powered by [Groq AI](https://groq.com/)
- Inspired by modern development workflows and best practices
- Thanks to all contributors who help improve this project

---

<p align="center">
  Made with ❤️ by Your Name | <a href="https://github.com/yourusername/codeforge">GitHub</a> | <a href="https://twitter.com/yourhandle">Twitter</a>
</p>
