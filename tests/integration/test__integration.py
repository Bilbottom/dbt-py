"""
Integration tests for the package.
"""
import textwrap
import unittest.mock

import pytest

import dbt_py

pytestmark = pytest.mark.integration

DBT_PROJECT_DIR = dbt_py.PROJECT_ROOT / "tests/integration/jaffle-shop"
ARGS = [
    "--project-dir",
    str(DBT_PROJECT_DIR),
    "--profiles-dir",
    str(DBT_PROJECT_DIR),
]
EXAMPLE_FILE = DBT_PROJECT_DIR / "target/compiled/jaffle_shop/models/example.sql"
EXAMPLE_COMPILED = textwrap.dedent(
    """
    select * from final
    Hello, World!

    select * from final
    Hello, World!
    """
)


@pytest.fixture
def mock_env(monkeypatch) -> None:
    """
    Mock the environment variables used by dbt_py.
    """
    monkeypatch.setenv(
        "DBT_PY_PACKAGE_ROOT", "tests.integration.jaffle-shop.dbt_py_test"
    )
    monkeypatch.setenv("DBT_PY_PACKAGE_NAME", "dbt_py_test")


def test__integration(mock_env) -> None:
    """
    Placeholder integration test.
    """
    with unittest.mock.patch("sys.argv", ["", "compile", *ARGS]):
        dbt_py.main()

    assert EXAMPLE_FILE.read_text(encoding="utf-8").strip() == EXAMPLE_COMPILED.strip()
