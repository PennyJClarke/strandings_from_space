import pandas as pd
import pytest

from strandings_from_space.clustering import (
    compare_clusterings,
    expand_cluster_membership,
    perform_clustering,
    rand_index_score,
    split_clusters_by_constraints,
)


def test_perform_clustering_assigns_close_points_to_same_cluster():
    df = pd.DataFrame(
        {
            "pixel_x": [0.0, 0.2, 10.0],
            "pixel_y": [0.0, 0.1, 10.0],
            "observer": ["1", "2", "1"],
        }
    )

    result = perform_clustering(df, distance_threshold=1.0, max_labels_per_cluster=3)

    assert "cluster" in result.columns
    assert result.loc[0, "cluster"] == result.loc[1, "cluster"]
    assert result.loc[2, "cluster"] != result.loc[0, "cluster"]


def test_perform_clustering_single_point():
    df = pd.DataFrame({"pixel_x": [1.0], "pixel_y": [2.0], "observer": ["1"]})

    result = perform_clustering(df, distance_threshold=1.0)

    assert result.loc[0, "cluster"] == 1


def test_split_clusters_by_constraints_moves_duplicate_observer():
    df = pd.DataFrame(
        {
            "pixel_x": [0.0, 0.1, 0.2],
            "pixel_y": [0.0, 0.1, 0.2],
            "observer": ["1", "1", "2"],
            "cluster": [1, 1, 1],
        }
    )

    result = split_clusters_by_constraints(df, distance_threshold_pixels=1.0)

    cluster_one = result[result["cluster"] == 1]
    assert cluster_one["observer"].tolist().count("1") == 1
    assert result["cluster"].nunique() == 2


def test_rand_index_score_perfect_match():
    assert rand_index_score([1, 1, 2, 2], [5, 5, 8, 8]) == pytest.approx(1.0)


def test_rand_index_score_rejects_mismatched_lengths():
    with pytest.raises(ValueError):
        rand_index_score([1, 2], [1])


def test_expand_cluster_membership():
    df = pd.DataFrame({"cluster": [1, 2], "unique_id": ["[0, 1]", "[2]"]})

    result = expand_cluster_membership(df)

    assert result.to_dict("records") == [
        {"cluster": 1, "unique_id": 0},
        {"cluster": 1, "unique_id": 1},
        {"cluster": 2, "unique_id": 2},
    ]


def test_compare_clusterings_returns_expected_keys():
    gt = pd.DataFrame({"cluster": [1, 2], "unique_id": ["[0, 1]", "[2]"]})
    pred = pd.DataFrame({"cluster": [10, 20], "unique_id": ["[0, 1]", "[2]"]})

    result = compare_clusterings(gt, pred)

    assert result["rand_index"] == pytest.approx(1.0)
    assert result["adjusted_rand_index"] == pytest.approx(1.0)
