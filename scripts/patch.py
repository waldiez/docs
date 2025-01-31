"""Patch the Jupyter contrib nbextensions package."""

# pylint: disable=line-too-long
# flake8: noqa: E501
# ref: https://github.com/ipython-contrib/jupyter_contrib_nbextensions/pull/1663#issuecomment-2248001870

import difflib
import sys
from pathlib import Path
from typing import List


def find_site_packages() -> Path:
    """Find the site-packages directory.

    Returns
    -------
    Path
        The site-packages directory

    Raises
    ------
    RuntimeError
        If the site-packages directory is not found
    """
    for path in sys.path:
        if "site-packages" in path:
            return Path(path)
    raise RuntimeError("site-packages directory not found")


def find_file(site_packages: Path, relative_path: str) -> Path:
    """Find the absolute path of a given relative file in site-packages.

    Parameters
    ----------
    site_packages : Path
        The site-packages directory
    relative_path : str
        The relative path of the file

    Returns
    -------
    Path
        The absolute path of the file

    Raises
    ------
    FileNotFoundError
        If the file is not found
    """
    file_path = site_packages / relative_path
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    return file_path


def apply_patch(original_file: Path, patched_content: List[str]) -> None:
    """Apply a patch directly by modifying the file.

    Parameters
    ----------
    original_file : Path
        The path of the original file
    patched_content : List[str]
        The patched content to be written to the file
    """
    with open(original_file, "w", encoding="utf-8", newline="\n") as f:
        f.writelines(patched_content)
    print(f"Patched: {original_file}")


def generate_patch(original_file: Path, new_lines: List[str]) -> List[str]:
    """Generate a diff-style patch for a file.

    Parameters
    ----------
    original_file : Path
        The path of the original file
    new_lines : List[str]
        The new content to be compared with the original file

    Returns
    -------
    List[str]
        The patch as a list of strings
    """
    with open(original_file, "r", encoding="utf-8") as f:
        old_lines = f.readlines()

    patch = list(
        difflib.unified_diff(
            old_lines,
            new_lines,
            fromfile=str(original_file),
            tofile=str(original_file),
        )
    )
    return patch


def process_patch(file_path: Path, old_text: str, new_text: str) -> None:
    """Read, modify, and apply a patch to a file.

    Parameters
    ----------
    file_path : Path
        The path of the file to be patched
    old_text : str
        The text to be replaced
    new_text : str
        The new text to replace with
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.readlines()

    modified_content = [line.replace(old_text, new_text) for line in content]

    patch = generate_patch(file_path, modified_content)
    if patch:
        print(f"Applying patch to {file_path}")
        apply_patch(file_path, modified_content)
    else:
        print(f"No changes needed for {file_path}")


def main() -> None:
    """Apply the patches."""
    site_packages = find_site_packages()
    patches = [
        (
            "jupyter_contrib_nbextensions/nbconvert_support/collapsible_headings.py",
            "from notebook.services.config import ConfigManager",
            "from jupyter_server.services.config import ConfigManager",
        ),
        (
            "jupyter_contrib_nbextensions/nbconvert_support/execute_time.py",
            "import notebook._tz as nbtz",
            "import jupyter_server._tz as nbtz",
        ),
    ]

    for relative_path, old_text, new_text in patches:
        try:
            file_path = find_file(site_packages, relative_path)
            process_patch(file_path, old_text, new_text)
        except FileNotFoundError as e:
            print(e)


if __name__ == "__main__":
    main()
