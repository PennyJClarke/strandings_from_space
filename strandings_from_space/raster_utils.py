"""Raster helper functions used by the notebook workflows."""

from __future__ import annotations

from pathlib import Path, PureWindowsPath

import numpy as np
import pandas as pd
from skimage import exposure


def get_raster_filename(raster_path: str | Path) -> str:
    """Return the raster filename from a POSIX or Windows-style full path."""
    text = str(raster_path)
    if "\\" in text:
        return PureWindowsPath(text).name
    return Path(text).name


def get_raster_sensor(raster_path: str | Path) -> str:
    """Extract the sensor field from a standard raster filename."""
    parts = get_raster_filename(raster_path).rsplit(".", 1)[0].split("_")
    if len(parts) < 2:
        raise ValueError(f"Cannot extract sensor from filename: {raster_path!s}")
    return parts[1]


def open_raster(raster_path: str | Path):
    """Open a raster with rasterio.

    Importing rasterio lazily keeps simple unit tests lightweight.
    """
    import rasterio

    return rasterio.open(raster_path)


def get_raster_as_array(raster_path: str | Path) -> np.ndarray:
    """Read a raster into a NumPy array with shape ``(bands, rows, cols)``."""
    import rasterio

    with rasterio.open(raster_path) as dataset:
        return dataset.read()


def get_raster_band_count(raster_path: str | Path) -> int:
    """Return the number of bands in a raster."""
    import rasterio

    with rasterio.open(raster_path) as dataset:
        return int(dataset.count)


def get_crs(raster_path: str | Path):
    """Return a raster's coordinate reference system."""
    import rasterio

    with rasterio.open(raster_path) as dataset:
        return dataset.crs


def convert_coordinates(df: pd.DataFrame, src_crs, dst_crs) -> pd.DataFrame:
    """Transform longitude/latitude columns from ``src_crs`` to ``dst_crs``."""
    from pyproj import Transformer

    required = {"longitude", "latitude"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    out = df.copy()
    transformer = Transformer.from_crs(src_crs, dst_crs, always_xy=True)
    out["converted_lon"], out["converted_lat"] = zip(
        *out.apply(lambda row: transformer.transform(row["longitude"], row["latitude"]), axis=1)
    )
    return out


def latlon_to_pixel(lat: float, lon: float, transform) -> tuple[int, int]:
    """Convert coordinates into pixel coordinates using an affine transform."""
    row, col = ~transform * (lon, lat)
    return int(row), int(col)


def make_plotting_array(
    full_arr: np.ndarray,
    sensor_bands: int,
    sensor_name: str,
    percent_clip: float = 2,
) -> tuple[np.ndarray | None, np.ndarray | None]:
    """Create an RGB plotting array for optical imagery or a SAR array.

    Returns ``(rgb_array, None)`` for optical sensors and ``(None, sar_array)``
    for the one-band TerraSAR-X case.
    """
    sensor_band_mapping = {
        "geoeye1": {4: [2, 1, 0], 8: [4, 2, 1]},
        "wv2": {4: [2, 1, 0], 8: [4, 2, 1]},
        "wv3": {4: [2, 1, 0], 8: [4, 2, 1]},
        "pleiades": {4: [2, 1, 0], 8: [3, 2, 1]},
        "pleiades-neo": {4: [2, 1, 0], 8: [3, 2, 1]},
        "skysat": {4: [2, 1, 0], 8: [3, 2, 1]},
        "pleiades-sentinel-hub": {4: [0, 1, 2]},
    }

    if sensor_name == "tsx-1" and sensor_bands == 1:
        return None, full_arr[0]

    if sensor_name not in sensor_band_mapping or sensor_bands not in sensor_band_mapping[sensor_name]:
        return None, None

    band_indices = sensor_band_mapping[sensor_name][sensor_bands]
    if full_arr.shape[0] <= max(band_indices):
        raise ValueError(
            f"Input array has {full_arr.shape[0]} bands but sensor mapping requires band index {max(band_indices)}"
        )

    rgb_arr = np.array([full_arr[i] for i in band_indices])
    p1, p2 = np.percentile(rgb_arr, (percent_clip, 100 - percent_clip))
    rgb_rescale = exposure.rescale_intensity(rgb_arr, in_range=(p1, p2), out_range=(0, 1))
    return rgb_rescale.transpose(1, 2, 0), None
