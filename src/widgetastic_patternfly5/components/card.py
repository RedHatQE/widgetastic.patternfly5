from widgetastic.utils import ParametrizedLocator
from widgetastic.widget import Checkbox
from widgetastic.widget import GenericLocatorWidget

from widgetastic_patternfly5.components.menus.dropdown import Dropdown


class BaseCard:
    """Represents the Patternfly Card.

    https://www.patternfly.org/components/card
    """

    TITLE = ".//div[contains(@class, '-c-card__title-text')]"
    BODY = ".//div[contains(@class, '-c-card__body')]"
    FOOTER = ".//div[contains(@class, '-c-card__footer')]"

    @property
    def title(self):
        """Get title of the card."""
        return self.browser.text(self.browser.element(self.TITLE))

    @property
    def body(self):
        """Get WebElement of the card body."""
        return self.browser.element(self.BODY)

    @property
    def footer(self):
        """Get WebElement of the card footer."""
        return self.browser.element(self.FOOTER)


class Card(BaseCard, GenericLocatorWidget):
    def __init__(self, parent, locator=None, logger=None):
        locator = locator or ".//div[contains(@class, '-c-card')]"
        super().__init__(parent, locator, logger=logger)

    ROOT = ParametrizedLocator("{@locator}")


class CardWithActions(Card):
    dropdown = Dropdown(locator=".//div[contains(@class, '-c-card__actions')]")
    checkbox = Checkbox(locator=".//input[contains(@class, '-c-check__input')]")
