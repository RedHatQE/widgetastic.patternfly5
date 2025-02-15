import pytest
from widgetastic.widget import View

from widgetastic_patternfly5.ouia import Card as CardOUIA

TESTING_PAGE_COMPONENT = "components/card"


@pytest.fixture
def view(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-card-basic-cards']"
        card = CardOUIA("BasicCard")

    return TestView(browser)


def test_card_displayed(view):
    assert view.card.is_displayed
