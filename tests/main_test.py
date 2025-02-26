"""
test ../test_pre_commit_ci/main.py

run with:
```
poetry run pytest tests/main_test.py
"""

import pytest

from test_pre_commit_ci import main


def test_main():
	with pytest.raises(NotImplementedError):
		main.main()
