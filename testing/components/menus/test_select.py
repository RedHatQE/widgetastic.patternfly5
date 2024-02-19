import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import CheckboxSelect
from widgetastic_patternfly5 import Select
from widgetastic_patternfly5 import SelectItemNotFound
from widgetastic_patternfly5.components.menus.select import TypeaheadSelect

TESTING_PAGE_URL = "https://patternfly-react-main.surge.sh/components/menus/select"


@pytest.fixture
def select(browser):
    class TestView(View):
        select = Select(locator=".//div[@id='ws-react-c-select-single']")

    return TestView(browser).select


def test_select_is_displayed(select):
    assert select.is_displayed


def test_select_items(select):
    assert set(select.items) == {"Option 3", "Option 2", "Option 1"}
    assert select.has_item("Option 1")
    assert not select.has_item("Non existing item")
    assert select.item_enabled("Option 1")


def test_select_open(select):
    assert not select.is_open
    select.open()
    assert select.is_open
    select.close()
    assert not select.is_open


def test_select_item_select(select):
    select.fill("Option 3")
    assert select.read() == "Option 3"
    assert not select.is_open
    with pytest.raises(SelectItemNotFound):
        select.fill("Non existing item")
    assert not select.is_open


@pytest.fixture
def checkbox_select(browser):
    class TestView(View):
        checkbox_select = CheckboxSelect(locator='.//div[@id="ws-react-c-select-checkbox"]')

    return TestView(browser).checkbox_select


def test_checkbox_select_is_displayed(checkbox_select):
    assert checkbox_select.is_displayed


def test_checkbox_select_items(checkbox_select):
    assert set(checkbox_select.items) == {"Error", "Warn", "Info", "Debug"}
    assert checkbox_select.has_item("Info")
    assert not checkbox_select.has_item("Non existing item")
    assert checkbox_select.item_enabled("Info")
    assert not checkbox_select.item_enabled("Error")


def test_checkbox_select_open(checkbox_select):
    assert not checkbox_select.is_open
    checkbox_select.open()
    assert checkbox_select.is_open
    checkbox_select.close()
    assert not checkbox_select.is_open


def test_checkbox_select_item_checkbox_select(checkbox_select):
    checkbox_select.fill({"Debug": True, "Warn": True})
    assert checkbox_select.read() == {"Debug": True, "Info": False, "Warn": True, "Error": False}

    checkbox_select.fill({"Error": False, "Warn": False, "Info": False, "Debug": False})
    assert checkbox_select.read() == {"Debug": False, "Info": False, "Warn": False, "Error": False}

    assert not checkbox_select.is_open
    with pytest.raises(SelectItemNotFound):
        checkbox_select.fill({"Non existing item": True})
    assert not checkbox_select.is_open


@pytest.fixture
def typeahead_select(browser):
    class TestView(View):
        typeahead_select = TypeaheadSelect(locator=".//div[@id='ws-react-c-select-typeahead']")

    return TestView(browser).typeahead_select


def test_typeahead_select_is_displayed(typeahead_select):
    assert typeahead_select.is_displayed


def test_typeahead_select_items(typeahead_select):
    assert set(typeahead_select.items) == {
        "Alabama",
        "Florida",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
    }
    assert typeahead_select.has_item("Alabama")
    assert not typeahead_select.has_item("Non existing item")
    assert typeahead_select.item_enabled("Alabama")


def test_typeahead_select_open(typeahead_select):
    assert not typeahead_select.is_open
    typeahead_select.open()
    assert typeahead_select.is_open
    typeahead_select.close()
    assert not typeahead_select.is_open


def test_typeahead_select_item_select(typeahead_select):
    typeahead_select.fill("New Mexico")
    assert typeahead_select.read() == "New Mexico"
    assert not typeahead_select.is_open
    # try again to verify it works when an item was selected previously (or in
    # case there is a default value)
    typeahead_select.fill("Florida")
    assert typeahead_select.read() == "Florida"
    assert not typeahead_select.is_open
    with pytest.raises(SelectItemNotFound):
        typeahead_select.fill("Non existing item")
    assert not typeahead_select.is_open
