import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import Card
from widgetastic_patternfly5 import CardWithActions

TESTING_PAGE_URL = "https://patternfly-react-main.surge.sh/components/card"


@pytest.fixture
def view(browser):
    class TestView(View):
        card = Card(locator='.//div[@id="ws-react-c-card-basic-cards"]')
        card_with_actions = CardWithActions(
            locator='.//div[@id="ws-react-c-card-header-images-and-actions"]'
        )

    return TestView(browser)


def test_cards_displayed(view):
    assert view.card.is_displayed
    assert view.card_with_actions.is_displayed


def test_card_content(view):
    assert view.card.title == "Title"
    assert view.card.body.text == "Body"
    assert view.card.footer.text == "Footer"


def test_card_actionable_items_displayed(view):
    assert view.card_with_actions.dropdown.is_displayed
    assert view.card_with_actions.checkbox.is_displayed
