# CodeForge 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI](https://img.shields.io/pypi/v/codeforge)](https://pypi.org/project/codeforge/)
[![Documentation](https://img.shields.io/badge/docs-available-brightgreen)](https://vishalrathod21.github.io/Codeforge/)

CodeForge is an AI-powered project scaffolding tool that transforms natural language descriptions into fully functional, production-ready project structures. It automates project setup, allowing developers to focus on writing code rather than configuration.

## 📋 Table of Contents
- ✨ [Features](#features)
- ⚙️ [Installation](#installation)
- 🚀 [Quick Start](#quick-start)
- 💻 [Usage](#usage)
- 🛠️ [Commands](#commands)
- ⚙️ [Configuration](#configuration)
- 📂 [Project Structure](#project-structure)
- 🤝 [Contributing](#contributing)
- 📄 [License](#license)

## ✨ Features

- **AI-Powered Generation**: Convert natural language to project structures
- **Multi-Language Support**: Supports various programming languages and frameworks
- **Templates**: Pre-configured templates for different project types
- **Git Integration**: Automatic repository initialization
- **Dependency Management**: Automatic requirements detection
- **Customizable**: Extensible with custom templates

## ⚙️ Installation

### 📋 Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- [Groq API key](https://console.groq.com/) for AI features

### 📦 Install via pip (Recommended)
```bash
pip install codeforge
```

### 🔧 Install from Source
```bash
git clone https://github.com/VishalRathod21/Codeforge.git
cd Codeforge
pip install -e .
pip install -r requirements.txt
```

### ✅ Verify Installation
```bash
codeforge version
```

## 🚀 Quick Start

1. Set up your API key:
   ```bash
   # Linux/macOS/Windows
   mkdir -p ~/.codeforge
   echo 'GROQ_API_KEY=your_api_key_here' > ~/.codeforge/.env
   ```

2. Create projects with simple commands:
   ```bash
   # Web app
   codeforge create "A blog with Django and React"
   
   # API service
   codeforge create "REST API using FastAPI and MongoDB" -t api
   ```

## 💻 Usage

### 🔍 Basic Commands

#### 🏗️ Create a Project
```bash
codeforge create "Project description" [OPTIONS]
```

#### 📋 List Templates
```bash
codeforge list-templates
```

#### ℹ️ Show Version
```bash
codeforge version
```

## 🛠️ Commands

### 🏗️ Create Command
```bash
codeforge create "Description" [OPTIONS]
```

**Options:**
- `-o, --output PATH`: Output directory (default: current)
- `-t, --template TEXT`: Template (web, api, ml, etc.)
- `-f, --force`: Overwrite existing files
- `--no-git`: Skip Git initialization
- `--author TEXT`: Project author
- `--license TEXT`: License (MIT, Apache-2.0, etc.)
- `--python-version TEXT`: Python version (e.g., 3.10)

**Examples:**
```bash
# Create a project in current directory
codeforge create "A task manager with FastAPI"

# Specify template and output
codeforge create "Data analysis with PyTorch" -t ml -o ./ml-project

# With custom options
codeforge create "Python CLI tool" --author "Dev" --license MIT
```

## Configuration

### 🔧 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GROQ_API_KEY` | Required for AI features | - |
| `CODEFORGE_TEMPLATE_DIR` | Custom templates directory | `~/.codeforge/templates/` |
| `CODEFORGE_CACHE_DIR` | Cache directory | `~/.codeforge/cache/` |

### ⚙️ Configuration File
Create `~/.codeforge/config.yaml` to customize settings:

```yaml
defaults:
  author: "Your Name <email@example.com>"
  license: "MIT"
  python_version: "3.10"
  git_init: true

templates:
  - name: web
    description: "Web application"
    default: true
  - name: api
    description: "API service"
  - name: ml
    description: "Machine Learning project"
```

## 📂 Project Structure

```
codeforge/
├── main.py                 # CLI entry point
├── llm_agent.py           # AI integration
├── structure_generator.py  # Project generation
├── prompts/               # AI prompt templates
└── templates/             # Project templates
    ├── web.json
    ├── api.json
    └── ml.json
```

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/VishalRathod21">Vishal Rathod</a>
</p>
