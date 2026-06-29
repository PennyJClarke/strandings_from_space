# Pytest starter files for `strandings_from_space`

Copy the contents of this folder into the root of your cloned repository, for example:

```text
C:\Test\strandings_from_space
```

The notebooks remain the main user-facing workflows.  These files add a small importable Python package and tests for pure helper logic such as filename parsing, count preparation, clustering, path creation, and RGB/SAR plotting-array selection.

## Windows / Anaconda workflow

Open **Anaconda Prompt**.

```bat
cd /d C:\Test
git clone https://github.com/PennyJClarke/strandings_from_space.git
cd strandings_from_space
```

Copy these starter files into this folder. Then create the development environment:

```bat
conda env create -f environment-dev.yml
conda activate sfs-dev
pip install -e .
pytest
```

If you prefer to use the existing `compare_counts.yml`, activate that environment and only add pytest:

```bat
conda env create -f compare_counts.yml
conda activate compare_counts
conda install -c conda-forge pytest
pip install -e .
pytest
```

## Suggested Git workflow

```bat
git switch -c add-pytest-core-utilities
git status
pytest
git add pyproject.toml environment-dev.yml strandings_from_space tests docs/pytest_readme_snippet.md
git commit -m "Add pytest coverage for core workflow utilities"
```

For the README, I suggest adding only the short snippet in `docs/pytest_readme_snippet.md`.
