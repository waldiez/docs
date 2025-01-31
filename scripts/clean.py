# SPDX-License-Identifier: Apache-2.0.
# Copyright (c) 2024 - 2025 Waldiez and contributors.
"""Cleanup."""

# pylint: disable=duplicate-code,broad-except
import glob
import os
import shutil
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DIR_PATTERNS = [
    "__pycache__",
    ".cache",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "*.egg-info",
    "htmlcov",
    "reports",
    "coverage",
    "build",
    "logs",
    "site",
]

FILE_PATTERNS = [
    "*.pyc",
    "*.pyo",
    "*.pyc~",
    "*.py~",
    "*~",
    ".*~",
    ".DS_Store",
    "._DS_Store",
    "._.DS_Store",
    ".coverage*",
]


SKIP_DIRS = [
    "node_modules",
    ".venv",
    "python_only",
    "ts_only",
    "both",
]


def _remove_dirs() -> None:
    for pattern in DIR_PATTERNS:
        for dirpath in glob.glob(f"./**/{pattern}", recursive=True):
            if any(
                f"{os.path.sep}{skip_dir}{os.path.sep}" in dirpath
                for skip_dir in SKIP_DIRS
            ):
                continue
            print(f"removing dir: {dirpath}")
            try:
                shutil.rmtree(dirpath)
            except BaseException:
                print(f"failed to remove dir: {dirpath}", file=sys.stderr)


def _remove_files() -> None:
    for pattern in FILE_PATTERNS:
        for filepath in glob.glob(f"./**/{pattern}", recursive=True):
            if any(
                f"{os.path.sep}{skip_dir}{os.path.sep}" in filepath
                for skip_dir in SKIP_DIRS
            ):
                continue
            print(f"removing file: {filepath}")
            try:
                os.remove(filepath)
            except BaseException:
                print(f"failed to remove file: {filepath}", file=sys.stderr)


def main() -> None:
    """Cleanup unnecessary files and directories."""
    _cwd = os.getcwd()
    os.chdir(ROOT_DIR)
    _remove_dirs()
    _remove_files()
    if os.getcwd() != _cwd:
        os.chdir(_cwd)


if __name__ == "__main__":
    main()
