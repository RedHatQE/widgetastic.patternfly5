import pytest
from widgetastic.widget import Checkbox, View

from widgetastic_patternfly5 import (
    Dropdown,
    DropdownDisabled,
)

TESTING_PAGE_COMPONENT = "components/menus/dropdown/react-templates/simple"


@pytest.fixture
def view(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-templates-c-dropdown-simple']/parent::div"
        dropdown_custom_locator = Dropdown(
            locator=".//button[contains(@data-ouia-component-type, '/MenuToggle') and contains(@data-ouia-component-id, 'default-1')]/parent::div"
        )
        disable_checkbox = Checkbox(locator=".//input[@id='simple-example-disabled-toggle']")

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
