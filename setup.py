from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="codeforge",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered project structure generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/codeforge",
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
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
