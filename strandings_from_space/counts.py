"""Small data-frame helpers for annotation count workflows."""

from __future__ import annotations

from pathlib import Path
from typing import Mapping

import pandas as pd

from .filenames import get_observer, get_resolution, resolution_to_meters


def assign_observer_from_filename(df: pd.DataFrame, file_name: str | Path) -> pd.DataFrame:
    """Return a copy of ``df`` with ``observer`` set from the filename."""
    out = df.copy()
    out["observer"] = str(get_observer(file_name))
    out["observer"] = pd.Categorical(out["observer"])
    return out


def assign_resolution_from_filename(df: pd.DataFrame, file_name: str | Path) -> pd.DataFrame:
    """Return a copy of ``df`` with ``gsd_m`` set from the filename resolution."""
    out = df.copy()
    out["gsd_m"] = resolution_to_meters(get_resolution(file_name))
    return out


def prepare_observer_dataframe(df: pd.DataFrame, file_name: str | Path) -> pd.DataFrame:
    """Set standard ``observer`` and ``gsd_m`` columns from a count filename."""
    return assign_resolution_from_filename(assign_observer_from_filename(df, file_name), file_name)


def concatenate_grouped_dataframes(
    grouped_dataframes: Mapping[tuple[str, str], list[pd.DataFrame]],
) -> dict[tuple[str, str], pd.DataFrame]:
    """Concatenate observer dataframes for each ``(resolution, image_id)`` group.

    A sequential ``unique_id`` column is added per group, matching the notebook's
    downstream Rand-index workflow.
    """
    concatenated: dict[tuple[str, str], pd.DataFrame] = {}
    for group, dataframes in grouped_dataframes.items():
        if not dataframes:
            concatenated[group] = pd.DataFrame()
            continue
        out = pd.concat(dataframes, ignore_index=True)
        out["unique_id"] = range(len(out))
        concatenated[group] = out
    return concatenated


def total_counts_by_observer(df: pd.DataFrame) -> pd.DataFrame:
    """Count annotations by resolution and observer."""
    required = {"gsd_m", "observer"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return df.groupby(["gsd_m", "observer"], observed=False).size().reset_index(name="counts")


def certainty_counts_by_observer(df: pd.DataFrame) -> pd.DataFrame:
    """Count annotations by resolution, observer, and certainty label."""
    required = {"gsd_m", "observer", "certainty"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return (
        df.groupby(["gsd_m", "observer"], observed=False)["certainty"]
        .value_counts()
        .reset_index(name="counts")
    )
