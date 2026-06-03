import pytest
from widgetastic.widget import Checkbox, View

from widgetastic_patternfly5 import (
    Dropdown,
    DropdownDisabled,
)

TESTING_PAGE_COMPONENT = "components/menus/dropdown/react-templates/simple"

# In PF5 the Dropdown renders a wrapper div (pf-vX-c-dropdown) around the
# MenuToggle button. In PF6 the Dropdown uses Popper inline rendering, so the
# button's parent is a plain wrapper div with no PF class.
#
# The original locator relied on data-ouia-component-id="default-1" which
# PF6 never generates (OUIA IDs are auto-generated, not "default-1").
#
# This locator finds the first MenuToggle button with text "Dropdown" then
# steps up to its parent — the natural ROOT for the Dropdown widget regardless
# of PF version.
_DROPDOWN_LOCATOR = (
    ".//button[contains(@class, '-c-menu-toggle') and normalize-space(.)='Dropdown'][1]/.."
)


@pytest.fixture
def view(browser):
    class TestView(View):
        dropdown_custom_locator = Dropdown(locator=_DROPDOWN_LOCATOR)
        disable_checkbox = Checkbox(id="simple-example-disabled-toggle")

    view = TestView(browser)
    view.wait_displayed("10s")
    return view


@pytest.fixture
def dropdown(view):
    return getattr(view, "dropdown_custom_locator")


def test_dropdown_is_displayed(dropdown):
    assert dropdown.is_displayed


def test_enabled_dropdown(view, dropdown):
    view.disable_checkbox.fill(False)
    assert dropdown.is_enabled


def test_disabled_dropdown(view, dropdown):
    view.disable_checkbox.fill(True)
    assert not dropdown.is_enabled


def test_disabled_dropdown_items(view, dropdown):
    view.disable_checkbox.fill(True)
    with pytest.raises(DropdownDisabled):
        assert dropdown.items == [
            "Action",
            "Link",
            "Disabled Action",
            "",
            "Second Action",
        ]


def test_disabled_dropdown_open(view, dropdown):
    view.disable_checkbox.fill(True)
    with pytest.raises(DropdownDisabled):
        dropdown.open()


def test_disabled_dropdown_item_select(view, dropdown):
    view.disable_checkbox.fill(True)
    with pytest.raises(DropdownDisabled):
        dropdown.item_select("Action")
