import pytest
from widgetastic.widget import ParametrizedView, Text

from widgetastic_patternfly5 import (
    CardCheckBox,
    CardForCardGroup,
    CardGroup,
    CardWithActions,
    Dropdown,
)

TESTING_PAGE_URL = (
    "https://patternfly-react-main.surge.sh/patterns/card-view/react-demos/card-view/"
)


@pytest.fixture
def pfy_card(browser):
    return CardWithActions(browser, locator='.//div[@id="PatternFly"]')


def test_cards_displayed(pfy_card):
    assert pfy_card.wait_displayed()


def test_card_content(pfy_card):
    assert pfy_card.title == "PatternFly"
    assert pfy_card.body.text == (
        "PatternFly is a community project that promotes design commonality and "
        "improves user experience."
    )


def test_card_actionable_items_displayed(pfy_card):
    assert pfy_card.dropdown.is_displayed
    assert pfy_card.checkbox.is_displayed


class PageCard(CardForCardGroup):
    dropdown = Dropdown(locator=".//div[contains(@class, '-c-card__actions')]")

    def delete_action(self):
        self.dropdown.item_select("Delete")

    checked = CardCheckBox()

    header_text = Text(locator=".//div[contains(@class, '-c-card__title')]")


class Cards(CardGroup):
    def __init__(self, parent, locator=None, logger=None, **kwargs):
        super().__init__(parent, logger=logger, **kwargs)
        self.locator = locator or './/div[contains(@class, "pf-v5-l-gallery")]'

    cards = ParametrizedView.nested(PageCard)


@pytest.fixture
def cards(browser):
    cards = Cards(browser)
    cards.wait_displayed("15s")
    return cards


def test_read_and_drop_second_card(cards, browser):
    second = [*cards][1]

    assert second.header_text.read() == "PatternFly"

    second.delete_action()

    new_second = [*cards][1]

    assert new_second.header_text.read() != "PatternFly"
    # refresh to get it back :)
    browser.refresh()


def read_cards_2_checkmap(cards):
    data = cards.cards.read()
    return {card["header_text"]: card["checked"] for card in list(data.values())[1:]}


def test_select_all_cards(browser, cards):
    name2checked = read_cards_2_checkmap(cards)
    assert not any(name2checked.values())
    assert all(name2checked.keys())

    # first card doesn't have header and checkbox
    for card in list(cards)[1:]:
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", card.checked)
        card.checked.fill(True)

    name2checked_after = read_cards_2_checkmap(cards)
    assert all(name2checked_after.values())
    assert all(name2checked_after.keys())

    assert name2checked.keys() == name2checked_after.keys()
