# SPDX-License-Identifier: Apache-2.0.
# Copyright (c) 2024 - 2025 Waldiez and contributors.
"""Format python code using isort, autoflake, black and ruff.

This script formats python code using isort, autoflake, black and ruff.

Functions
---------
run_isort()
    Run isort.
run_autoflake()
    Run autoflake.
run_black()
    Run black.
run_ruff()
    Run ruff.
"""

import sys
from pathlib import Path

HAD_TO_MODIFY_SYS_PATH = False

try:
    from _lib import ROOT_DIR, run_autoflake, run_black, run_isort, run_ruff
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _lib import (  # type: ignore[unused-ignore]
        ROOT_DIR,
        run_autoflake,
        run_black,
        run_isort,
        run_ruff,
    )

    HAD_TO_MODIFY_SYS_PATH = True


def format_root() -> None:
    """Format the root directory."""
    run_isort(in_dir=ROOT_DIR, fix=True)
    run_autoflake(in_dir=ROOT_DIR)
    run_black(in_dir=ROOT_DIR, fix=True)
    run_ruff(in_dir=ROOT_DIR, fix=True)


def main() -> None:
    """Run python formatters."""
    format_root()


if __name__ == "__main__":
    try:
        main()
    finally:
        if HAD_TO_MODIFY_SYS_PATH:
            sys.path.pop(0)
