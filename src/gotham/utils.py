"""
This file contains utility functions for the Gotham API.
It defines a function for getting the version of a package.
"""

from pathlib import Path


def get_package_version(package_name: str) -> str:
    """Get the version of a package.

    Args:
        package_name: The name of the package to get the version of

    Returns:
        The version of the package
    """
    return __import__(package_name).__version__


def load_sql_file(path: Path) -> str:
    """Load SQL from a file.

    Args:
        path (Path): Path to the SQL file.

    Returns:
        str: SQL query as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If the file cannot be read.
    """
    if not path.exists():
        raise FileNotFoundError(f"SQL file not found: {path}")
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        raise IOError(f"Error reading SQL file {path}: {e}")
