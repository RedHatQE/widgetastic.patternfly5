import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import (
    Dropdown,
    DropdownItemDisabled,
    DropdownItemNotFound,
)

TESTING_PAGE_COMPONENT = "components/menus/dropdown/react/basic-dropdowns"


@pytest.fixture
def view(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-dropdown-basic-dropdowns']/parent::div"
        dropdown_txt_locator = Dropdown("Dropdown")
        dropdown_custom_locator = Dropdown(
            locator=".//div[@id='ws-react-c-dropdown-basic-dropdowns']"
        )
        dropdown_default_locator = Dropdown()

    view = TestView(browser)
    view.wait_displayed("10s")
    return view


@pytest.fixture(
    params=["dropdown_txt_locator", "dropdown_custom_locator", "dropdown_default_locator"]
)
def dropdown(view, request):
    return getattr(view, request.param)


def test_dropdown_is_displayed(dropdown):
    assert dropdown.is_displayed


def test_enabled_dropdown(dropdown):
    assert dropdown.is_enabled


def test_dropdown_items(dropdown):
    assert dropdown.items == [
        "Action",
        "Link",
        "Disabled Action",
        "Disabled Link",
        "Aria-disabled Link",
        "",
        "Separated Action",
        "Separated Link",
    ]
    assert dropdown.has_item("Action")
    assert not dropdown.has_item("Non existing items")
    assert dropdown.item_enabled("Link")
    assert not dropdown.item_enabled("Disabled Link")


def test_dropdown_open(dropdown):
    assert not dropdown.is_open
    dropdown.open()
    assert dropdown.is_open
    dropdown.close()
    assert not dropdown.is_open


def test_dropdown_item_select(dropdown):
    dropdown.item_select("Action")
    assert not dropdown.is_open
    with pytest.raises(DropdownItemDisabled):
        dropdown.item_select("Disabled Link")
    with pytest.raises(DropdownItemNotFound):
        dropdown.item_select("Non existing items")
