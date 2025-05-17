"""
This file contains utility functions for the Gotham API.
It defines a function for getting the version of a package.
"""


def get_package_version(package_name: str) -> str:
    """Get the version of a package.

    Args:
        package_name: The name of the package to get the version of

    Returns:
        The version of the package
    """
    return __import__(package_name).__version__
