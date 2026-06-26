"""
Refactor filename helper functions in cetacean_strandings_from_space_comparing_counts.ipynb.

Run from the repository root, for example:

    cd /d C:\Test\strandings_from_space
    conda activate sfs-dev
    python scripts\refactor_count_notebook_filename_helpers.py

What it does:
- Creates a .bak_filename_helpers backup of the notebook.
- Adds imports from the new strandings_from_space.filenames module.
- Removes duplicated notebook definitions for:
  - group_by_indices
  - group_by_indices_exc_observer
  - get_observer
  - get_resolution

It intentionally does NOT refactor raster, coordinate, plotting, or clustering code yet.
"""

from __future__ import annotations

import json
from pathlib import Path


NOTEBOOK_NAME = "cetacean_strandings_from_space_comparing_counts.ipynb"

IMPORT_BLOCK = """\
# Import tested helper functions from the local strandings_from_space package.
from strandings_from_space.filenames import (
    get_observer,
    get_resolution,
    group_by_indices,
    group_by_indices_excluding_observer as group_by_indices_exc_observer,
)
"""

FUNCTIONS_TO_REMOVE = {
    "group_by_indices",
    "group_by_indices_exc_observer",
    "get_observer",
    "get_resolution",
}


def source_to_text(source) -> str:
    if isinstance(source, list):
        return "".join(source)
    return str(source)


def text_to_source_lines(text: str) -> list[str]:
    return text.splitlines(keepends=True)


def remove_named_function_blocks(source_text: str, names: set[str]) -> tuple[str, list[str]]:
    """Remove Python function definitions by name from a notebook code cell.

    This uses indentation and is designed for notebook cells where functions are
    defined directly in the cell. It preserves non-function code in the same cell.
    """
    lines = source_text.splitlines(keepends=True)
    output: list[str] = []
    removed: list[str] = []
    i = 0

    while i < len(lines):
        stripped = lines[i].lstrip()
        indent = len(lines[i]) - len(stripped)

        matched_name = None
        for name in names:
            if stripped.startswith(f"def {name}("):
                matched_name = name
                break

        if matched_name is None:
            output.append(lines[i])
            i += 1
            continue

        removed.append(matched_name)
        # Skip the function definition line and its indented body.
        i += 1
        while i < len(lines):
            next_line = lines[i]
            next_stripped = next_line.lstrip()

            # Blank/comment lines immediately following the function are skipped
            # if they are still part of the function body spacing.
            if next_stripped.strip() == "":
                i += 1
                continue

            next_indent = len(next_line) - len(next_stripped)

            # A new line at the same or lower indentation means the function block ended.
            if next_indent <= indent:
                break

            i += 1

        # Leave one readable marker where the notebook function used to be.
        output.append(
            f"# Function `{matched_name}` is imported from strandings_from_space.filenames.\n"
        )

    return "".join(output), removed


def add_import_block(cells: list[dict]) -> bool:
    """Add the helper import block to the main import cell if missing."""
    for cell in cells:
        if cell.get("cell_type") != "code":
            continue

        text = source_to_text(cell.get("source", ""))
        if "import pandas as pd" in text and "from strandings_from_space.filenames import" not in text:
            if not text.endswith("\n"):
                text += "\n"
            text += "\n" + IMPORT_BLOCK
            cell["source"] = text_to_source_lines(text)
            return True

        if "from strandings_from_space.filenames import" in text:
            return False

    raise RuntimeError("Could not find the main import cell to update.")


def main() -> None:
    repo_root = Path.cwd()
    notebook_path = repo_root / NOTEBOOK_NAME

    if not notebook_path.exists():
        raise FileNotFoundError(
            f"Could not find {NOTEBOOK_NAME}. Run this script from the repository root."
        )

    backup_path = notebook_path.with_suffix(notebook_path.suffix + ".bak_filename_helpers")
    if not backup_path.exists():
        backup_path.write_bytes(notebook_path.read_bytes())

    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    cells = notebook["cells"]

    import_added = add_import_block(cells)

    removed_all: list[str] = []
    for cell in cells:
        if cell.get("cell_type") != "code":
            continue

        text = source_to_text(cell.get("source", ""))
        new_text, removed = remove_named_function_blocks(text, FUNCTIONS_TO_REMOVE)
        if removed:
            cell["source"] = text_to_source_lines(new_text)
            removed_all.extend(removed)

    notebook_path.write_text(
        json.dumps(notebook, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Updated: {notebook_path}")
    print(f"Backup:  {backup_path}")
    print(f"Import block added: {import_added}")
    print(f"Removed notebook function definitions: {sorted(set(removed_all))}")
    print()
    print("Next checks:")
    print("  python -m pytest")
    print("  git diff --stat")
    print("  git status")


if __name__ == "__main__":
    main()
