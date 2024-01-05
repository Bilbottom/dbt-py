# Just for reference
dbt    clean   --project-dir tests/integration/jaffle-shop --profiles-dir tests/integration/jaffle-shop --no-clean-project-files-only
dbt-py compile --project-dir tests/integration/jaffle-shop --profiles-dir tests/integration/jaffle-shop
rm dbt_packages
