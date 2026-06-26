import pandas as pd
import pytest

from strandings_from_space.counts import (
    certainty_counts_by_observer,
    concatenate_grouped_dataframes,
    prepare_observer_dataframe,
    total_counts_by_observer,
)


def test_prepare_observer_dataframe_sets_observer_and_resolution():
    df = pd.DataFrame({"certainty": ["definite_90-100", "likely_70-89"]})
    file_name = "site_geoeye1_IMG001_20221014_213434_50_2.csv"

    result = prepare_observer_dataframe(df, file_name)

    assert list(result["observer"].astype(str)) == ["2", "2"]
    assert list(result["gsd_m"]) == [0.5, 0.5]


def test_concatenate_grouped_dataframes_adds_unique_id_per_group():
    grouped = {
        ("50", "IMG001"): [
            pd.DataFrame({"observer": ["1"], "certainty": ["definite_90-100"]}),
            pd.DataFrame({"observer": ["2"], "certainty": ["likely_70-89"]}),
        ]
    }

    result = concatenate_grouped_dataframes(grouped)

    out = result[("50", "IMG001")]
    assert len(out) == 2
    assert list(out["unique_id"]) == [0, 1]


def test_total_counts_by_observer():
    df = pd.DataFrame(
        {
            "gsd_m": [0.5, 0.5, 0.5],
            "observer": ["1", "1", "2"],
        }
    )

    result = total_counts_by_observer(df)

    counts = {(row.gsd_m, row.observer): row.counts for row in result.itertuples()}
    assert counts[(0.5, "1")] == 2
    assert counts[(0.5, "2")] == 1


def test_certainty_counts_by_observer():
    df = pd.DataFrame(
        {
            "gsd_m": [0.5, 0.5, 0.5],
            "observer": ["1", "1", "2"],
            "certainty": ["definite_90-100", "likely_70-89", "likely_70-89"],
        }
    )

    result = certainty_counts_by_observer(df)

    assert set(result.columns) == {"gsd_m", "observer", "certainty", "counts"}
    assert result["counts"].sum() == 3


def test_total_counts_requires_columns():
    with pytest.raises(ValueError):
        total_counts_by_observer(pd.DataFrame({"observer": ["1"]}))
