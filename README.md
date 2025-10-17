<h1 align="center"> widgetastic.patternfly5 </h1>

<p align="center">
    <a href="https://pypi.org/project/widgetastic.patternfly5/">
    <img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/widgetastic.patternfly5.svg?style=flat">
    </a>
    <a href="https://pypi.org/project/widgetastic.patternfly5/#history">
    <img alt="PyPI version" src="https://badge.fury.io/py/widgetastic.patternfly5.svg">
    </a>
    <a href="https://codecov.io/github/RedHatQE/widgetastic.patternfly5">
      <img src="https://codecov.io/github/RedHatQE/widgetastic.patternfly5/graph/badge.svg?token=cWuTXniIPm"/>
    </a>
    <a href="https://github.com/RedHatQE/widgetastic.patternfly5/actions/workflows/tests.yaml">
    <img alt="github actions" src="https://github.com/RedHatQE/widgetastic.patternfly5/actions/workflows/tests.yaml/badge.svg">
    </a>
    <a href="https://results.pre-commit.ci/latest/github/RedHatQE/widgetastic.patternfly5/main">
    <img alt="pre: black" src="https://results.pre-commit.ci/badge/github/RedHatQE/widgetastic.patternfly5/main.svg">
    </a>
</p>

## Overview

This library offers Widgetastic Widgets for [PatternFly v5/v6](https://www.patternfly.org/), serving as an extended
iteration of [widgetastic.patternfly4](https://github.com/RedHatQE/widgetastic.patternfly4).

Built on top of [widgetastic.core](https://github.com/RedHatQE/widgetastic.core) with **Playwright** as the browser
automation engine, this library provides a robust and modern approach to UI testing for PatternFly components.

## Installation

```bash
# Install from PyPI
pip install widgetastic.patternfly5

# Or install from source
git clone https://github.com/RedHatQE/widgetastic.patternfly5.git
cd widgetastic.patternfly5
pip install -e .
```

## Supported Components

### Components
- [alert](https://www.patternfly.org/components/alert)
- [breadcrumb](https://www.patternfly.org/components/breadcrumb)
- [button](https://www.patternfly.org/components/button)
- [card](https://www.patternfly.org/components/card)
- [chip](https://www.patternfly.org/components/chip)
- [clipboard-copy](https://www.patternfly.org/components/clipboard-copy)
- date and time
  - [calendar-month](https://www.patternfly.org/components/date-and-time/calendar-month)
- [description-list](https://www.patternfly.org/components/description-list)
- [drawer](https://www.patternfly.org/components/drawer)
- [dual-list-selector](https://www.patternfly.org/components/dual-list-selector)
- [expandable-section](https://www.patternfly.org/components/expandable-section)
- forms
  - [form-select](https://www.patternfly.org/components/forms/form-select)
  - [radio](https://www.patternfly.org/components/forms/radio)
- menus
  - [dropdown](https://www.patternfly.org/components/menus/dropdown)
  - [menu](https://www.patternfly.org/components/menus/menu)
  - [menu-toggle](https://www.patternfly.org/components/menus/menu-toggle)
  - [options-menu](https://www.patternfly.org/components/menus/options-menu/)
  - [select](https://www.patternfly.org/components/menus/select)
  - [typeahedselect](https://www.patternfly.org/components/menus/select/#typeahead)
- [modal](https://www.patternfly.org/components/modal)
- [navigation](https://www.patternfly.org/components/navigation)
- [pagination](https://www.patternfly.org/components/pagination/)
- [popover](https://www.patternfly.org/components/popover)
- [progress](https://www.patternfly.org/components/progress)
- [slider](https://www.patternfly.org/components/slider)
- [switch](https://www.patternfly.org/components/switch)
- [table](https://www.patternfly.org/components/table)
- [tabs](https://www.patternfly.org/components/tabs)
- [title](https://www.patternfly.org/components/title)


### Charts:
- [bullet-chart](https://www.patternfly.org/charts/bullet-chart)
- [boxplot-chart](https://www.patternfly.org/charts/box-plot-chart)
- [donut-chart](https://www.patternfly.org/charts/donut-chart)
- [legends](https://www.patternfly.org/charts/legends)
- [line-chart](https://www.patternfly.org/charts/line-chart)
- [pie-chart](https://www.patternfly.org/charts/pie-chart)

### Patterns
- [card-view](https://www.patternfly.org/patterns/card-view)

## Development

### Contribution guide

```bash
# clone the repo
git clone https://github.com/RedHatQE/widgetastic.patternfly5.git
cd widgetastic.patternfly5

# create a virtual environment
python3 -m venv .venv_pfy5
source .venv_pfy5/bin/activate

# update pip and its friends
pip install -U pip setuptools wheel

# install the package in editable mode
pip install -e .[dev]
# if you use zsh, pip install will fail. Use this instead:
pip install -e ".[dev]"

# install Playwright browsers for testing
playwright install chromium firefox
playwright install-deps

# setup pre-commit hooks
pre-commit install
```

### Testing

The library includes comprehensive tests that run against the official PatternFly documentation pages:
- [PatternFly v6](https://www.patternfly.org) (latest)
- [PatternFly v5](https://v5-archive.patternfly.org) (archived)

Tests are powered by **Playwright**, providing fast, reliable, and modern browser automation.

#### Prerequisites

Before running tests, install Playwright browsers:

```bash
# Install Playwright (included in dev dependencies)
pip install -e ".[dev]"

# Install Playwright browsers
playwright install chromium firefox

# Install system dependencies (if needed)
playwright install-deps
```

#### Running Tests

**Basic test execution:**

```bash
# Run tests with default settings (chromium, v6, headed mode)
pytest -v

# Run tests against PatternFly v5
pytest -v --pf-version v5

# Run tests with Firefox
pytest -v --browser firefox

# Run tests in headless mode (no browser window)
pytest -v --headless
```

**Advanced options:**

```bash
# Run tests in parallel (speeds up execution)
pytest -v -n 3 --browser chromium --pf-version v6

# Run with slow motion for debugging (100ms delay between actions)
pytest -v --slowmo 100

# Run specific test file
pytest testing/components/test_button.py -v --browser firefox

# Run tests with coverage
pytest -v --cov=./ --cov-report=html
```

**Available test options:**

| Option | Choices | Default | Description |
|--------|---------|---------|-------------|
| `--browser` | `chromium`, `firefox` | `chromium` | Browser to use for testing |
| `--pf-version` | `v5`, `v6` | `v6` | PatternFly version to test against |
| `--headless` | flag | `False` | Run in headless mode (no UI) |
| `--slowmo` | milliseconds | `0` | Slow down operations for debugging |
| `-n` | number | `1` | Number of parallel workers (requires pytest-xdist) |


#### Debugging Tests

When debugging, it's helpful to:
1. Run tests in **headed mode** (without `--headless`) to see browser interactions
2. Use `--slowmo` to slow down actions and observe what's happening
3. Run a single test file or test function instead of the entire suite
4. Reduce parallelism (`-n 1` or remove `-n` flag) to avoid race conditions

```bash
# Debug specific test with visible browser and slow execution
pytest testing/components/test_modal.py::test_modal_basic -v --slowmo 1000
```
