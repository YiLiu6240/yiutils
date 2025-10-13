# Development Guide

## Prerequisites

- Python 3.8 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- [just](https://just.systems/) command runner (optional but recommended)

## Setup for Development

```bash
# Clone the repository
git clone https://github.com/YiLiu6240/yiutils.git
cd yiutils

# Install development dependencies
uv sync --dev

# Verify installation
just test
```

## Development Workflow

### Available Commands

Using `just` (recommended):

```bash
# List all available commands
just

# Install dev dependencies
just install

# Run tests
just test

# Format code
just fmt

# Lint code
just lint

# Build package
just build

# Run sanity checks
just sanity

# Clean build artifacts
just clean
```

Using `uv` directly:

```bash
# Install dependencies
uv sync --dev

# Run tests
uv run pytest -vv

# Format and fix code
uv run ruff format .
uv run ruff check --fix .

# Lint code
uv run ruff check .
uv run ty check .

# Build package
uv build
```

## Project Structure

```
yiutils/
├── src/yiutils/          # Main package source
│   ├── __init__.py
│   ├── chunking.py       # Data chunking utilities
│   ├── failsafe.py       # Error handling decorators
│   └── project_utils.py  # Project management utilities
├── tests/                # Test suite
├── scripts/              # Utility scripts
│   └── sanity.py         # Sanity checks and examples
├── justfile              # Task runner configuration
├── pyproject.toml        # Project configuration
└── README.md             # User documentation
```
