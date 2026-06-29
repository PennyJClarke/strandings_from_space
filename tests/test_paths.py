from strandings_from_space.paths import (
    ensure_compare_counts_directories,
    ensure_pipeline_directories,
)


def test_ensure_compare_counts_directories_creates_expected_layout(tmp_path):
    created = ensure_compare_counts_directories(tmp_path)

    assert tmp_path.joinpath("compare_counts", "inputs", "satellite", "counts").is_dir()
    assert tmp_path.joinpath("compare_counts", "outputs", "clusters").is_dir()
    assert tmp_path.joinpath("compare_counts", "temp_outputs").is_dir()
    assert created


def test_ensure_pipeline_directories_creates_expected_layout(tmp_path):
    ensure_pipeline_directories(tmp_path)

    assert tmp_path.joinpath("inputs").is_dir()
    assert tmp_path.joinpath("outputs").is_dir()
    assert tmp_path.joinpath("temp_outputs").is_dir()
