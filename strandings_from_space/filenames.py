"""Filename parsing helpers for strandings_from_space workflows."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path, PureWindowsPath
from typing import DefaultDict, Iterable


@dataclass(frozen=True)
class SatelliteCountFilename:
    """Parsed fields from a standard satellite count CSV filename.

    Expected pattern::

        location_sensor_image-id_YYYYMMDD_HHMMSS_resolution_observer.csv

    The location and sensor names may contain hyphens, but the parser expects
    fields to be separated with underscores.
    """

    location: str
    sensor: str
    image_id: str
    image_date: str
    image_time: str
    resolution: str
    observer: str


def _name(file_name: str | Path) -> str:
    """Return the final path component for POSIX or Windows-style paths."""
    text = str(file_name)
    if "\\" in text:
        return PureWindowsPath(text).name
    return Path(text).name


def _stem(file_name: str | Path) -> str:
    return _name(file_name).rsplit(".", 1)[0]


def split_standard_name(file_name: str | Path, separator: str = "_") -> list[str]:
    """Split a standard repository filename into underscore-separated parts."""
    return _stem(file_name).split(separator)


def parse_satellite_count_filename(file_name: str | Path) -> SatelliteCountFilename:
    """Parse a standard satellite count CSV filename.

    Raises
    ------
    ValueError
        If the filename does not contain the expected seven underscore-separated
        parts.
    """
    parts = split_standard_name(file_name)
    if len(parts) < 7:
        raise ValueError(
            "Expected at least 7 underscore-separated fields: "
            "location_sensor_image-id_date_time_resolution_observer.csv"
        )
    return SatelliteCountFilename(
        location=parts[0],
        sensor=parts[1],
        image_id=parts[2],
        image_date=parts[3],
        image_time=parts[4],
        resolution=parts[5],
        observer=parts[-1],
    )


def get_observer(file_name: str | Path) -> str:
    """Return the observer identifier from the final filename field."""
    return split_standard_name(file_name)[-1]


def get_resolution(file_name: str | Path) -> str:
    """Return the image resolution field from a standard filename."""
    parts = split_standard_name(file_name)
    if len(parts) < 2:
        raise ValueError(f"Cannot extract resolution from filename: {file_name!s}")
    return parts[-2]


def group_by_indices(
    names: Iterable[str | Path],
    separator: str = "_",
    indices: Iterable[int] | None = None,
) -> dict[tuple[str, ...], list[str]]:
    """Group filenames by selected underscore-separated field indices.

    By default this matches the notebook convention of grouping by resolution
    and image catalogue ID: indices ``[5, 2]``.
    """
    selected_indices = list(indices if indices is not None else [5, 2])
    groups: DefaultDict[tuple[str, ...], list[str]] = defaultdict(list)
    for name in names:
        file_name = _name(name)
        parts = _stem(file_name).split(separator)
        try:
            key = tuple(parts[i] for i in selected_indices)
        except IndexError as exc:
            raise ValueError(f"Filename does not contain required fields: {file_name}") from exc
        groups[key].append(file_name)
    return dict(groups)


def group_by_indices_excluding_observer(
    names: Iterable[str | Path],
    separator: str = "_",
    indices: Iterable[int] | None = None,
) -> dict[tuple[str, ...], str]:
    """Group image filenames by selected fields when there is no observer ID.

    This mirrors the notebook's ``group_by_indices_exc_observer`` helper.
    """
    selected_indices = list(indices if indices is not None else [5, 2])
    groups: dict[tuple[str, ...], str] = {}
    for name in names:
        file_name = _name(name)
        parts = _stem(file_name).split(separator)
        try:
            key = tuple(parts[i] for i in selected_indices)
        except IndexError as exc:
            raise ValueError(f"Filename does not contain required fields: {file_name}") from exc
        groups[key] = file_name
    return groups


def resolution_to_meters(resolution: str | int | float) -> float:
    """Convert common centimetre-style filename resolutions to metres.

    Examples: ``"50"`` -> ``0.5``, ``"30"`` -> ``0.3``, ``"15"`` -> ``0.15``.
    If a value already looks like metres, it is returned as a float.
    """
    value = float(resolution)
    if value > 1:
        return value / 100.0
    return value
