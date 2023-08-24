import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import Switch
from widgetastic_patternfly5 import SwitchDisabled

TESTING_PAGE_URL = "https://patternfly-react-main.surge.sh/components/switch"


@pytest.fixture
def view(browser):
    class TestView(View):
        switch = Switch(locator='.//label[@for="simple-switch"]')
        disabled_switch_on = Switch(locator='.//label[@for="disabled-switch-on"]')

    return TestView(browser)


def test_switch_is_displayed(view):
    assert view.switch.is_displayed
    assert view.disabled_switch_on.is_displayed


def test_switch_is_enabled(view):
    assert view.switch.is_enabled
    assert not view.disabled_switch_on.is_enabled


def test_switch_click(view):
    assert view.switch.click()
    with pytest.raises(SwitchDisabled):
        view.disabled_switch_on.click()
