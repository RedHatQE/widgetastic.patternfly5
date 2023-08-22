import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import Menu
from widgetastic_patternfly5 import MenuItemDisabled
from widgetastic_patternfly5 import MenuItemNotFound

TESTING_PAGE_URL = "https://patternfly-react-main.surge.sh/components/menus/menu"


@pytest.fixture
def view(browser):
    class TestView(View):
        basic_menu = Menu(".//div[@id='ws-react-c-menu-basic-menus']")

    return TestView(browser)


def test_menu_is_displayed(view):
    assert view.basic_menu.is_displayed


def test_menu_items(view):
    assert view.basic_menu.items == [
        "Action",
        "Link",
        "Disabled action",
        "Disabled link",
        "Aria-disabled action",
        "Aria-disabled link",
    ]
    assert view.basic_menu.has_item("Action")
    assert not view.basic_menu.has_item("Non existing items")
    assert view.basic_menu.item_enabled("Link")
    assert not view.basic_menu.item_enabled("Disabled link")


def test_menu_item_select(view):
    view.basic_menu.item_select("Link")
    with pytest.raises(MenuItemDisabled):
        view.basic_menu.item_select("Disabled link")
    with pytest.raises(MenuItemNotFound):
        view.basic_menu.item_select("Non existing items")
