from pathlib import Path


def find_project_root(anchor_file: str = "environment.yml") -> Path:
    """Find the project root directory by searching for an anchor file.

    Traverses up the directory tree from the current working directory
    until it finds a directory containing the specified anchor file,
    or reaches the filesystem root.

    Args:
        anchor_file: Name of the file to search for that indicates the
            project root (default: "environment.yml")

    Returns:
        Path to the project root directory, or current working directory
        if anchor file is not found
    """
    cwd = Path.cwd()
    test_dir = cwd
    prev_dir = None
    while prev_dir != test_dir:
        if (test_dir / anchor_file).exists():
            return test_dir
        prev_dir = test_dir
        test_dir = test_dir.parent
    return cwd
