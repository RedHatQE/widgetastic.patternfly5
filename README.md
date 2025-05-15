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

This library offers Widgetastic Widgets for [PatternFly v5/v6](https://www.patternfly.org/), serving as an extended
itteration of [widgetastic.patternfly4](https://github.com/RedHatQE/widgetastic.patternfly4).


### Components:
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

### Patterns:
- [card-view](https://www.patternfly.org/patterns/card-view)


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

pre-commit install
```

### Testing

The library has selenium tests that are performed against [Patternfly v6 docs](https://www.patternfly.org) and [Patternfly v5 docs](https://v5-archive.patternfly.org).
It's also configured to run the tests every time when a new version of that page is released.

Tests spawn a container from official selenium image - [selenium/standalone-{chrome/firefox}](https://hub.docker.com/u/selenium).
We can check local runs via vnc `http://localhost:7900`

**Note:** Tests use `podman` to manage containers. Please install it before running.

It's possible to run tests in parallel to speed up the execution. Make sure that you have **xdist** python plugin installed.

Use `-n` key to specify a number
of workers:

```bash
pytest --browser-name firefox --pf-version v5 -n 2 -vv
```
