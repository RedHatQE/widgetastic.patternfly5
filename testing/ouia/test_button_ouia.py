import pytest
from widgetastic.widget import View

from widgetastic_patternfly5.ouia import Button as ButtonOUIA

TESTING_PAGE_COMPONENT = "components/button"

BUTTON_TYPES = ["Primary", "Secondary", "DangerSecondary", "Tertiary", "Danger", "Warning"]


@pytest.fixture(params=BUTTON_TYPES)
def button(browser, request):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-button-variant-examples']"
        button = ButtonOUIA(request.param)

    view = TestView(browser)
    return view.button


def test_button_is_displayed(button):
    assert button.is_displayed


def test_button_is_active(button):
    assert not button.disabled
