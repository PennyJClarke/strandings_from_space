"""Clustering and agreement metrics for multi-observer annotations."""

from __future__ import annotations

import re
from math import comb
from typing import Iterable

import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import fcluster, linkage
from sklearn.metrics import adjusted_rand_score


def _euclidean_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return float(np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


def split_clusters_by_constraints(
    data: pd.DataFrame,
    distance_threshold_pixels: float,
    max_labels_per_cluster: int = 3,
) -> pd.DataFrame:
    """Split clusters that violate observer/count constraints.

    A valid cluster may contain at most ``max_labels_per_cluster`` points and no
    duplicate observer.  Duplicate observer points are reassigned to the nearest
    valid neighbouring cluster within ``distance_threshold_pixels`` or to a new
    cluster if no valid neighbour exists.
    """
    required = {"cluster", "pixel_x", "pixel_y", "observer"}
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    out = data.copy()
    if out.empty:
        return out

    new_cluster_id = int(out["cluster"].max()) + 1

    for cluster_id in list(out["cluster"].dropna().unique()):
        cluster_data = out[out["cluster"] == cluster_id]
        if cluster_data.empty:
            continue

        centroid_x = float(cluster_data["pixel_x"].mean())
        centroid_y = float(cluster_data["pixel_y"].mean())

        for observer, observer_points in cluster_data.groupby("observer", observed=False):
            if len(observer_points) <= 1:
                continue

            distances = observer_points.apply(
                lambda row: _euclidean_distance(row["pixel_x"], row["pixel_y"], centroid_x, centroid_y),
                axis=1,
            )
            ordered_indices = list(distances.sort_values().index)

            # Keep the closest duplicate in the current cluster; move the rest.
            for idx in ordered_indices[1:]:
                point_x = float(out.at[idx, "pixel_x"])
                point_y = float(out.at[idx, "pixel_y"])

                candidate_rows = out[out["cluster"] != cluster_id].copy()
                candidate_rows["distance_to_point"] = np.sqrt(
                    (candidate_rows["pixel_x"] - point_x) ** 2
                    + (candidate_rows["pixel_y"] - point_y) ** 2
                )
                candidate_rows = candidate_rows[
                    candidate_rows["distance_to_point"] < distance_threshold_pixels
                ].sort_values("distance_to_point")

                reassigned = False
                for nearby_cluster_id in candidate_rows["cluster"].dropna().unique():
                    nearby_cluster = out[out["cluster"] == nearby_cluster_id]
                    observers = set(nearby_cluster["observer"].astype(str))
                    if len(nearby_cluster) < max_labels_per_cluster and str(observer) not in observers:
                        out.at[idx, "cluster"] = nearby_cluster_id
                        reassigned = True
                        break

                if not reassigned:
                    out.at[idx, "cluster"] = new_cluster_id
                    new_cluster_id += 1

    return out


def perform_clustering(
    data: pd.DataFrame,
    distance_threshold: float,
    max_labels_per_cluster: int = 3,
) -> pd.DataFrame:
    """Run Ward hierarchical clustering on ``pixel_x`` and ``pixel_y`` columns."""
    required = {"pixel_x", "pixel_y", "observer"}
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if data.empty:
        raise ValueError("Data is empty")

    out = data.copy()
    if len(out) == 1:
        out["cluster"] = 1
        return out

    coords = out[["pixel_x", "pixel_y"]].to_numpy(dtype=float)
    linkage_matrix = linkage(coords, method="ward")
    out["cluster"] = fcluster(linkage_matrix, distance_threshold, criterion="distance")
    return split_clusters_by_constraints(out, distance_threshold, max_labels_per_cluster)


def rand_index_score(labels_true: Iterable[int], labels_pred: Iterable[int]) -> float:
    """Calculate the Rand index for two cluster-label sequences."""
    true = list(labels_true)
    pred = list(labels_pred)
    if len(true) != len(pred):
        raise ValueError("labels_true and labels_pred must have the same length")
    n = len(true)
    if n < 2:
        return 1.0

    agreements = 0
    total_pairs = comb(n, 2)
    for i in range(n):
        for j in range(i + 1, n):
            same_true = true[i] == true[j]
            same_pred = pred[i] == pred[j]
            if same_true == same_pred:
                agreements += 1
    return agreements / total_pairs


def expand_cluster_membership(df: pd.DataFrame, id_column: str = "unique_id") -> pd.DataFrame:
    """Expand rows whose unique-id column contains one or more integer IDs.

    The notebook stores grouped IDs as strings in some outputs.  This helper
    converts each row into one row per integer ID while preserving ``cluster``.
    """
    if "cluster" not in df.columns or id_column not in df.columns:
        raise ValueError(f"DataFrame must contain 'cluster' and '{id_column}' columns")

    rows: list[tuple[int, int]] = []
    for cluster, raw_ids in zip(df["cluster"], df[id_column]):
        ids = [int(value) for value in re.findall(r"\d+", str(raw_ids))]
        rows.extend((int(cluster), unique_id) for unique_id in ids)
    return pd.DataFrame(rows, columns=["cluster", "unique_id"]).sort_values("unique_id")


def compare_clusterings(ground_truth: pd.DataFrame, predicted: pd.DataFrame) -> dict[str, float]:
    """Return Rand and adjusted Rand indices for two cluster-output tables."""
    gt = expand_cluster_membership(ground_truth)
    pred = expand_cluster_membership(predicted)

    merged = gt.merge(pred, on="unique_id", suffixes=("_true", "_pred"), how="inner")
    if merged.empty:
        raise ValueError("No matching unique_id values found between cluster tables")

    labels_true = merged["cluster_true"].astype(int).to_numpy()
    labels_pred = merged["cluster_pred"].astype(int).to_numpy()
    return {
        "rand_index": rand_index_score(labels_true, labels_pred),
        "adjusted_rand_index": adjusted_rand_score(labels_true, labels_pred),
    }
