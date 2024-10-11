<div align="center">

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![dbt](https://img.shields.io/badge/dbt-1.5+-blue.svg)](https://github.com/dbt-labs/dbt-core/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![GitHub last commit](https://img.shields.io/github/last-commit/Bilbottom/dbt-py)](https://shields.io/badges/git-hub-last-commit)

[![tests](https://github.com/Bilbottom/dbt-py/actions/workflows/tests.yaml/badge.svg)](https://github.com/Bilbottom/dbt-py/actions/workflows/tests.yaml)
[![coverage](coverage.svg)](https://github.com/dbrgn/coverage-badge)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Bilbottom/dbt-py/main.svg)](https://results.pre-commit.ci/latest/github/Bilbottom/dbt-py/main)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)

</div>

---

# dbt-π 🧬

Python wrapper for [dbt-core](https://github.com/dbt-labs/dbt-core) to extend dbt with custom Python.

## Shimmy shimmy shim 🕺🕺🕺

This package is a [shim](<https://en.wikipedia.org/wiki/Shim_(computing)>) for [dbt-core](https://github.com/dbt-labs/dbt-core), inspired by (_cough_ stolen from _cough_) my old boss, [@darkdreamingdan](https://github.com/darkdreamingdan):

- https://gist.github.com/darkdreamingdan/c5ded709a90fc3c5b420cee5f644f499

Before using this package, it's recommended to get up to speed with the Python modules that are already available in dbt:

- https://docs.getdbt.com/reference/dbt-jinja-functions/modules

The existing Python modules are available in the dbt Jinja context under the `modules` object, for example:

```jinja
{{ modules.datetime.datetime.now() }}
```

## Installation ⬇️

While in preview, this package is only available from GitHub:

```
pip install git+https://github.com/Bilbottom/dbt-py@v0.0.3
```

This will be made available on PyPI once it's ready for general use.

## Usage 📖

This package adds a new executable, `dbt-py`, which injects your custom Python into dbt and then runs dbt. Either a custom module or a custom package can be injected. A custom module is the simplest to get started with.

The default module/package name is `custom` which would make custom Python available in the dbt Jinja context under the `modules.custom` object. This can be configured (see the [Configuration](#configuration-) section below).

### Custom Module 🐍

Create a module called `custom.py` in the root of your dbt project. This module can contain any Python code you like, for example:

```python
def salutation(name: str) -> str:
    return f"Hello, {name}!"
```

Reference this module and function in the dbt Jinja context of a dbt model:

```jinja
{{ modules.custom.salutation("World") }}
```

Rather than run dbt with the `dbt` command, instead run it with `dbt-py`:

```
dbt-py clean
dbt-py build
```

Note that `dbt-py` is a wrapper around `dbt` so all the usual dbt commands are available -- all the arguments passed to `dbt-py` are passed through to `dbt`, too.

```
dbt-py --help
dbt-py run --select my_model
dbt-py test --select tag:unit-test
```

### Custom Package 📦

Using a custom package is similar to using a custom module: create a package called `custom` in the root of your dbt project.

The submodules of this package will be available in the dbt Jinja context too. For example, suppose you have a package called `custom` with a submodule called `greetings`:

```
custom/
    __init__.py
    greetings.py
```

If the `greetings.py` submodule contains the same `salutation` function as above, then it can be referenced in the dbt Jinja context as follows:

```jinja
{{ modules.custom.greetings.salutation("World") }}
```

Alternatively, you can expose the `salutation` function via the `__init__.py` file and then reference it directly via `custom`:

```jinja
{{ modules.custom.salutation("World") }}
```

### Configuration 🛠️

The default module/package and Jinja context name is `custom` but both can be configured with the following environment variables:

- `DBT_PY_PACKAGE_ROOT`: The Python-style ref to the custom module/package, e.g. `package.module.submodule`
- `DBT_PY_PACKAGE_NAME`: The name to give the custom module/package in the dbt Jinja context, e.g. `custom_py`. Defaults to the value of `DBT_PY_PACKAGE_ROOT`

In particular, you can use the `DBT_PY_PACKAGE_ROOT` environment variable to reference a custom module/package that is not at the root of your dbt project.

> [!WARNING]
>
> If you set the `DBT_PY_PACKAGE_ROOT` environment variable to a name that already exists, this package will use the existing module/package rather than your custom one. Make sure that your custom module/package name does not clash with any existing modules/packages.
>
> This is likely to change in a future release, but for now you may choose to exploit this behaviour to use an existing module/package in your dbt Jinja context. For example, you could set `DBT_PY_PACKAGE_ROOT` to `math` and then reference the `math` standard library in your dbt Jinja context:
>
> ```jinja
> {{ modules.math.pi }}
> ```

## Future Work 🚧

This is still in preview, and there are a few things to be added before it's ready for general use:

- Support for importing any number of packages (currently only one package is supported)
- Configuration via config files and CLI arguments (currently only environment variables are supported)
- More robust testing

## Contributing 🤝

Raise an issue, or fork the repo and open a pull request.

This project uses [Poetry](https://python-poetry.org/) for dependency management and [pre-commit](https://pre-commit.com/) for linting. After cloning the repo, install the dependencies and enable pre-commit:

```
poetry install --sync --with dev,test
pre-commit install --install-hooks
```
