"""
Sample module for testing dbt-py.
"""


def select_final() -> str:
    return "select * from final"


def salutation(name: str) -> str:
    return f"Hello, {name}!"
