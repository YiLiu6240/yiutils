# yi's utils

Various helpers that I use in my own projects.

## Using yiutils as a Package

### Adding yiutils as a Git Submodule

To include yiutils in your Python repository as a submodule, where I assume you want to place it under `./yiutils/`:

```bash
# Add as submodule in your repo
git submodule add https://github.com/YiLiu6240/yiutils.git yiutils

# Initialize and update submodules
git submodule update --init --recursive

# add yiutils as a package
uv add yiutils
```

## How to use

### `find_project_root`

Find the project root directory by searching for an anchor file.

```python
from yiutils.project_utils import find_project_root

# Find project root using default anchor file (environment.yml)
root = find_project_root()
print(root)  # /path/to/your/project

# Find project root using custom anchor file
root = find_project_root(anchor_file="pyproject.toml")
print(root)  # /path/to/your/project
```

### `calculate_chunk_start_end`

Calculate start and end indices for data chunking, useful for parallel processing.

```python
from yiutils.chunking import calculate_chunk_start_end

# Split 7000 items into 30 chunks
data_length = 7000
num_chunks = 30

for chunk_id in range(num_chunks):
    start, end = calculate_chunk_start_end(
        chunk_id=chunk_id,
        num_chunks=num_chunks,
        data_length=data_length,
        verbose=True
    )
    print(f"Chunk {chunk_id}: process items {start} to {end}")
    # Process your_data[start:end] here
```

### `failsafe`

Decorator that catches exceptions and returns them as part of a tuple instead of raising.

```python
from yiutils.failsafe import failsafe

# Basic usage
@failsafe
def divide(a, b):
    return a / b

# Returns (result, error_flag, context)
result, error, context = divide(10, 2)
print(result)    # 5.0
print(error)     # True (success)
print(context)   # None

# Handle errors gracefully
result, error, context = divide(10, 0)
print(result)    # None
print(error)     # ZeroDivisionError object
print(context)   # {'a': 10, 'b': 0}

# Silent mode (no warnings)
@failsafe(silent=True)
def risky_operation(data):
    if not data:
        raise ValueError("Data cannot be empty")
    return len(data) * 2

result, error, context = risky_operation("")
# No warning printed, but error captured in tuple
```

---

For further technical details refer to DEV.md
