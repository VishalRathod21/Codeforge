from setuptools import setup, find_packages
from pathlib import Path
import re

# Read the README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Get version from __init__.py
def get_version():
    init_file = Path("codeforge/__init__.py").read_text()
    version_match = re.search(r'^__version__ = ["\']([^"\']+)["\']', init_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name="codeforge",
    version=get_version(),
    author="Vishal Rathod",
    author_email="vishal.rathod@example.com",
    description="AI-powered project structure generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VishalRathod21/Codeforge",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0.1",
        "requests>=2.31.0",
        "rich>=13.7.0",
        "typer>=0.9.0",
    ],
    entry_points={
        'console_scripts': [
            'codeforge=codeforge.main:app',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    keywords='ai code generator project-structure scaffolding',
    project_urls={
        'Bug Reports': 'https://github.com/VishalRathod21/Codeforge/issues',
        'Source': 'https://github.com/VishalRathod21/Codeforge',
    },
)
