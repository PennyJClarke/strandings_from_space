"""Path helpers for strandings_from_space workflows.

These functions avoid changing the user's working directory.  They make the
notebooks easier to test and safer to run from any location.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


COMPARE_COUNTS_DIRS: tuple[str, ...] = (
    "compare_counts/inputs",
    "compare_counts/inputs/satellite/counts",
    "compare_counts/inputs/satellite/images",
    "compare_counts/inputs/aerial_ref/counts",
    "compare_counts/inputs/aerial_ref/images",
    "compare_counts/inputs/ground_ref",
    "compare_counts/outputs",
    "compare_counts/outputs/clusters",
    "compare_counts/temp_outputs",
)

PIPELINE_DIRS: tuple[str, ...] = (
    "inputs",
    "outputs",
    "temp_outputs",
)


def repo_root(base_path: str | Path | None = None) -> Path:
    """Return the repository root as an absolute :class:`pathlib.Path`.

    Parameters
    ----------
    base_path:
        The directory containing the repository.  When ``None``, the current
        working directory is used.  This is intentionally explicit so code does
        not silently switch to the user's Desktop.
    """
    return Path(base_path or Path.cwd()).expanduser().resolve()


def ensure_directories(base_path: str | Path, relative_dirs: Iterable[str]) -> list[Path]:
    """Create a set of directories under ``base_path`` and return their paths."""
    root = repo_root(base_path)
    created: list[Path] = []
    for relative_dir in relative_dirs:
        path = root / relative_dir
        path.mkdir(parents=True, exist_ok=True)
        created.append(path)
    return created


def ensure_compare_counts_directories(base_path: str | Path) -> list[Path]:
    """Create the directory layout used by the compare-counts workflow."""
    return ensure_directories(base_path, COMPARE_COUNTS_DIRS)


def ensure_pipeline_directories(base_path: str | Path) -> list[Path]:
    """Create the directory layout used by the main annotation pipeline."""
    return ensure_directories(base_path, PIPELINE_DIRS)
