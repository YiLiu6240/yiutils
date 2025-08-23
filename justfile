# justfile for yiutils development

# Default recipe
default:
    @just --list --unsorted

# ==== Development ====

# Install development dependencies
[group('development')]
install:
    uv sync --dev

# Run tests with pytest
[group('development')]
test:
    uv run pytest -vv

# Format code with ruff
[group('development')]
fmt:
    uv run ruff format .
    uv run ruff check --fix .

# Lint code with ruff and ty
[group('development')]
lint:
    uv run ruff check .
    uv run ty check .

# ==== Build ====

# Build the wheel package
[group('build')]
build:
    uv build

# ==== Scripts ====

# Run sanity check script
[group('scripts')]
sanity:
    uv run python scripts/sanity.py

# ==== Cleanup ====

# Clean build artifacts
[group('cleanup')]
clean:
    rm -rf dist/
    rm -rf build/
    rm -rf *.egg-info/
    find . -type d -name __pycache__ -delete
    find . -type f -name "*.pyc" -delete
