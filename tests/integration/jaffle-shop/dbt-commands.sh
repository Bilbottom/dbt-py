# Just for reference
# $env:DBT_PY_PACKAGE_ROOT = "tests.integration.jaffle-shop.dbt_py_test"
# $env:DBT_PY_PACKAGE_NAME = "custom_py"
dbt    clean   --project-dir tests/integration/jaffle-shop --profiles-dir tests/integration/jaffle-shop --no-clean-project-files-only
dbt-py compile --project-dir tests/integration/jaffle-shop --profiles-dir tests/integration/jaffle-shop
rm dbt_packages
