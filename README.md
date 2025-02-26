# test-pre-commit-ci

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/atloo1/test-pre-commit-ci/ci.yaml)](https://github.com/atloo1/test-pre-commit-ci/actions/workflows/ci.yaml?query=branch%3Amain)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Ftest-pre-commit-ci%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.tool.poetry.dependencies.python&label=python)](https://github.com/atloo1/test-pre-commit-ci/blob/main/pyproject.toml)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Ftest-pre-commit-ci%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.tool.poetry.version&label=version)](https://github.com/atloo1/test-pre-commit-ci/blob/main/pyproject.toml)
[![GitHub License](https://img.shields.io/github/license/atloo1/test-pre-commit-ci)](https://github.com/atloo1/test-pre-commit-ci/blob/main/LICENSE)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/atloo1/test-pre-commit-ci)

[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

test pre-commit.ci autoupdate

## prerequisites

### minimum

```
git clone https://github.com/atloo1/test-pre-commit-ci.git
cd test-pre-commit-ci
```

### recommended: virtual environment setup with [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)

```
pyenv install 3.9 --skip-existing
pyenv local 3.9
```

## run (with [Poetry](https://python-poetry.org/docs/#installing-with-pipx))

```
poetry install --without dev
poetry run python -m test_pre_commit_ci.main
```

## develop

- ### [Poetry](https://python-poetry.org/docs/#installing-with-pipx) setup
  ```
  poetry install
  poetry run pre-commit install
  ```
- ### proactively pre-commit
  ```
  poetry run pre-commit run --all-files
  ```
- ### proactively test locally, mirroring the GitHub action
  ```
  poetry run pytest
  ```
- ### [give Renovate repository access](https://github.com/apps/renovate) if setting up own CI/CD
