import pytest

from widgetastic_patternfly5 import SplitButtonDropdown

TESTING_PAGE_URL = "https://www.patternfly.org/components/menus/menu-toggle"


@pytest.fixture(
    params=[
        "ws-react-c-menu-toggle-split-button-toggle-with-checkbox",
        "ws-react-c-menu-toggle-split-button-toggle-with-text-label",
    ],
    ids=["without_text", "with_text"],
)
def split_button_dropdown(request, browser):
    browser.move_to_element(f".//div[@id='{request.param}']")
    split_drop = SplitButtonDropdown(
        browser, locator=f".//div[@id='{request.param}']/div[contains(@class, 'pf-m-primary')]"
    )
    return split_drop, request.param


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_split_button_dropdown(split_button_dropdown):
    dropdown, dropdown_type = split_button_dropdown
    assert dropdown.is_displayed
    assert dropdown.is_enabled
    assert dropdown.check()
    assert dropdown.selected
    expected_text = "10 selected" if "with-text-label" in dropdown_type else ""
    assert dropdown.read() == expected_text

    assert dropdown.uncheck()
    assert not dropdown.selected
