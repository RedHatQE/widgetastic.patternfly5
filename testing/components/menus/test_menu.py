from urllib.parse import urljoin

import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import CheckboxMenu, Menu, MenuItemNotFound

TESTING_PAGE_COMPONENT = "components/menus/menu"


@pytest.fixture
def menu(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-menu-option-single-select-menu']"
        menu = Menu(locator=".//div[contains(@class, '-c-menu')]")

    return TestView(browser).menu


@pytest.fixture
def multi_select_menu(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-menu-option-multi-select-menu']"
        menu = Menu(locator=".//div[contains(@class, '-c-menu')]")

    # In the testing page, the menu does not open as expected; instead, it displays a list of items,
    # and all the widgets being tested are shown on the same page. In PF-v6, item selection requires
    # the use of the `root_browser`, as the item locators are located outside the ROOT. To ensure
    # proper testing, we need to navigate to the specific widget by redirecting to the appropriate page.
    current_url = browser.url
    browser.url = urljoin(current_url, "react/option-multi-select-menu")
    yield TestView(browser).menu
    browser.url = current_url


@pytest.fixture
def checkbox_menu(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-menu-item-checkbox']"
        menu = CheckboxMenu(locator=".//div[contains(@class, '-c-menu')]")

    return TestView(browser).menu


def test_menu_is_displayed(menu):
    assert menu.is_displayed


def test_menu_items(menu):
    assert set(menu.items) == {"Option 1", "Option 2", "Option 3"}
    assert menu.has_item("Option 1")
    assert not menu.has_item("Non existing item")
    assert menu.item_enabled("Option 2")


def test_menu_item_select(menu):
    menu.fill("Option 1")
    assert menu.selected_items == ["Option 1"]
    assert menu.is_open
    with pytest.raises(MenuItemNotFound):
        menu.fill("Non existing item")
    menu.fill("Option 3")
    assert menu.selected_items == ["Option 3"]


def test_menu_multi_item_select(multi_select_menu):
    menu = multi_select_menu
    menu.fill(["Option 1"])
    assert menu.selected_items == ["Option 1"]
    menu.fill(["Option 2", "Option 3"])
    assert menu.selected_items == ["Option 1", "Option 2", "Option 3"]


def test_menu_checkbox(checkbox_menu):
    assert checkbox_menu.is_displayed
    assert checkbox_menu.is_enabled
    assert checkbox_menu.items == ["Checkbox 1", "Checkbox 2", "Checkbox 3"]
    checkbox_menu.fill({"Checkbox 1": True, "Checkbox 2": True})
    assert checkbox_menu.read() == {"Checkbox 1": True, "Checkbox 2": True, "Checkbox 3": False}
    assert checkbox_menu.item_enabled("Checkbox 1")
    assert not checkbox_menu.item_enabled("Checkbox 3")
