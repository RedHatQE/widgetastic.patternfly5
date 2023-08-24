import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import Dropdown
from widgetastic_patternfly5 import DropdownItemDisabled
from widgetastic_patternfly5 import DropdownItemNotFound
from widgetastic_patternfly5 import GroupDropdown

TESTING_PAGE_URL = "https://patternfly-react-main.surge.sh/components/menus/dropdown"


@pytest.fixture
def view(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-dropdown-basic-dropdowns']/parent::div"
        dropdown_txt_locator = Dropdown("Dropdown")
        dropdown_custom_locator = Dropdown(
            locator=".//div[@id='ws-react-c-dropdown-basic-dropdowns']"
        )
        dropdown_default_locator = Dropdown()

    browser.url = "https://patternfly-react-main.surge.sh/components/menus/dropdown/react/basic-dropdowns/"  # noqa
    view = TestView(browser)
    view.wait_displayed("10s")
    return view


@pytest.fixture(
    params=["dropdown_txt_locator", "dropdown_custom_locator", "dropdown_default_locator"]
)
def dropdown(view, request):
    return getattr(view, request.param)


@pytest.fixture()
def group_dropdown(browser):
    browser.url = "https://patternfly-react-main.surge.sh/components/menus/dropdown/react/with-groups-of-items/"  # noqa
    dropdown = GroupDropdown(
        browser,
        locator=".//div[@id='ws-react-c-dropdown-with-groups-of-items']",
    )
    dropdown.wait_displayed("10s")
    return dropdown


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


def test_group_dropdown(group_dropdown):
    assert group_dropdown.is_displayed
    assert group_dropdown.is_enabled
    assert group_dropdown.items == [
        "Action",
        "Link",
        "Group 2 action",
        "Group 2 link",
        "Group 3 action",
        "Group 3 link",
    ]
    assert group_dropdown.has_item("Group 2 link")
    assert group_dropdown.item_enabled("Group 3 action")
    assert group_dropdown.groups == ["", "Group 2", "Group 3"]
    group_dropdown.item_select("Group 3 action", group_name="Group 3")
    with pytest.raises(DropdownItemNotFound):
        group_dropdown.item_select("Group 3 action", group_name="Group 2")
    group_dropdown.item_select("Link")
