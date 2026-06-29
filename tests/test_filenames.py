import pytest

from strandings_from_space.filenames import (
    get_observer,
    get_resolution,
    group_by_indices,
    group_by_indices_excluding_observer,
    parse_satellite_count_filename,
    resolution_to_meters,
)


STANDARD = "chatham-island_geoeye1_105001002F60AA00_20221014_213434_50_3.csv"


def test_get_observer_from_standard_filename():
    assert get_observer(STANDARD) == "3"


def test_get_resolution_from_standard_filename():
    assert get_resolution(STANDARD) == "50"


def test_parse_satellite_count_filename():
    parsed = parse_satellite_count_filename(STANDARD)

    assert parsed.location == "chatham-island"
    assert parsed.sensor == "geoeye1"
    assert parsed.image_id == "105001002F60AA00"
    assert parsed.image_date == "20221014"
    assert parsed.image_time == "213434"
    assert parsed.resolution == "50"
    assert parsed.observer == "3"


def test_group_by_indices_groups_by_resolution_and_image_id():
    files = [
        "site_geoeye1_IMG001_20221014_213434_50_1.csv",
        "site_geoeye1_IMG001_20221014_213434_50_2.csv",
        "site_geoeye1_IMG002_20221014_213434_30_1.csv",
    ]

    grouped = group_by_indices(files, indices=[5, 2])

    assert grouped[("50", "IMG001")] == files[:2]
    assert grouped[("30", "IMG002")] == [files[2]]


def test_group_by_indices_excluding_observer_for_raster_names():
    files = [
        "site_geoeye1_IMG001_20221014_213434_50.tif",
        "site_geoeye1_IMG002_20221014_213434_30.tif",
    ]

    grouped = group_by_indices_excluding_observer(files, indices=[5, 2])

    assert grouped[("50", "IMG001")] == files[0]
    assert grouped[("30", "IMG002")] == files[1]


@pytest.mark.parametrize(
    ("value", "expected"),
    [("50", 0.5), ("30", 0.3), ("15", 0.15), ("0.5", 0.5)],
)
def test_resolution_to_meters(value, expected):
    assert resolution_to_meters(value) == pytest.approx(expected)


def test_parse_satellite_count_filename_rejects_short_name():
    with pytest.raises(ValueError):
        parse_satellite_count_filename("too_short.csv")
