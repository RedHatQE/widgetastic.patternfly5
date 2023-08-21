import pytest
from widgetastic.widget import View

from widgetastic_patternfly5.ouia import Switch as SwitchOUIA

TESTING_PAGE_URL = "https://patternfly-react-main.surge.sh/components/switch"


@pytest.fixture
def view(browser):
    class TestView(View):
        switch = SwitchOUIA("BasicSwitch")

    return TestView(browser)


def test_switch_is_displayed(view):
    assert view.switch.is_displayed


def test_switch_is_enabled(view):
    assert view.switch.is_enabled


def test_switch_click(view):
    assert view.switch.click()
