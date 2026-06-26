import numpy as np
import pytest

from strandings_from_space.raster_utils import (
    get_raster_filename,
    get_raster_sensor,
    make_plotting_array,
)


def test_get_raster_filename():
    assert get_raster_filename(r"C:\\Test\\strandings_from_space\\inputs\\site_geoeye1_IMG001_20221014_213434_50.tif") == "site_geoeye1_IMG001_20221014_213434_50.tif"


def test_get_raster_sensor_from_standard_name():
    assert get_raster_sensor("site_geoeye1_IMG001_20221014_213434_50.tif") == "geoeye1"


def test_make_plotting_array_for_four_band_optical_image():
    full_arr = np.arange(4 * 3 * 3, dtype=float).reshape(4, 3, 3)

    rgb, sar = make_plotting_array(full_arr, sensor_bands=4, sensor_name="geoeye1")

    assert sar is None
    assert rgb.shape == (3, 3, 3)
    assert np.nanmin(rgb) >= 0
    assert np.nanmax(rgb) <= 1


def test_make_plotting_array_for_sar_image():
    full_arr = np.arange(1 * 3 * 3, dtype=float).reshape(1, 3, 3)

    rgb, sar = make_plotting_array(full_arr, sensor_bands=1, sensor_name="tsx-1")

    assert rgb is None
    assert sar.shape == (3, 3)


def test_make_plotting_array_unknown_sensor_returns_none():
    full_arr = np.arange(4 * 3 * 3, dtype=float).reshape(4, 3, 3)

    rgb, sar = make_plotting_array(full_arr, sensor_bands=4, sensor_name="unknown")

    assert rgb is None
    assert sar is None


def test_get_raster_sensor_rejects_short_name():
    with pytest.raises(ValueError):
        get_raster_sensor("image.tif")
