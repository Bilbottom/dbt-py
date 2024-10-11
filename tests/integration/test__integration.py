"""
Integration tests for the package.
"""

import pathlib
import shutil
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
        "DBT_PY_PACKAGE_ROOT",
        "tests.integration.jaffle-shop.dbt_py_test",
    )
    monkeypatch.setenv(
        "DBT_PY_PACKAGE_NAME",
        "custom_py",
    )


@pytest.fixture
def teardown() -> None:
    """
    Remove the compiled directory if it exists.
    """
    yield
    # TODO: I think this should be dynamic
    target = pathlib.Path("tests/integration/jaffle-shop/target")
    if target.exists():
        shutil.rmtree(target)


def test__dbt_can_be_successfully_invoked(mock_env, teardown) -> None:
    """
    Test that dbt can be successfully invoked.
    """
    with unittest.mock.patch("sys.argv", ["", "compile", *ARGS]):
        dbt_py.main()

    assert EXAMPLE_FILE.read_text(encoding="utf-8").strip() == EXAMPLE_COMPILED.strip()
