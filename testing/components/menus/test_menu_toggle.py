import pytest

from widgetastic_patternfly5 import SplitButtonDropdown

TESTING_PAGE_COMPONENT = "components/menus/menu-toggle"


@pytest.fixture(
    params=[
        "ws-react-c-menu-toggle-split-toggle-with-checkbox",
        "ws-react-c-menu-toggle-split-toggle-with-checkbox-and-toggle-text",
    ],
    ids=["without_text", "with_text"],
)
def split_button_dropdown(request, browser):
    browser.move_to_element(f".//div[contains(@id, '{request.param}')]")
    split_drop = SplitButtonDropdown(
        browser,
        locator=f".//div[contains(@id, '{request.param}')]/div[contains(@class, 'pf-m-primary')]",
    )
    return split_drop, request.param


def test_split_button_dropdown(split_button_dropdown):
    dropdown, dropdown_type = split_button_dropdown
    assert dropdown.is_displayed
    assert dropdown.is_enabled
    assert dropdown.check()
    assert dropdown.selected
    expected_text = "10 selected" if "text" in dropdown_type else ""
    assert dropdown.read() == expected_text

    assert dropdown.uncheck()
    assert not dropdown.selected
