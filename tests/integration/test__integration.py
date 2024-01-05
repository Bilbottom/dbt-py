"""
Integration tests for the package.
"""
import os
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


def test__integration() -> None:
    """
    Placeholder integration test.
    """
    os.environ["DBT_PY_PACKAGE_ROOT"] = "tests.integration.jaffle-shop.dbt_py"
    os.environ["DBT_PY_PACKAGE_NAME"] = "dbt_py"

    with unittest.mock.patch("sys.argv", ["", "compile", *ARGS]):
        dbt_py.main()

    assert EXAMPLE_FILE.read_text(encoding="utf-8").strip() == EXAMPLE_COMPILED.strip()
