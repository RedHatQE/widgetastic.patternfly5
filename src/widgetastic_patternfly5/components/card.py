from widgetastic.utils import ParametrizedLocator
from widgetastic.widget import Checkbox, GenericLocatorWidget, ParametrizedView, View

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
    DEFAULT_LOCATOR = ".//div[contains(@data-ouia-component-type, '/Card')] | .//article[contains(@class, '-c-card')]"

    def __init__(self, parent, locator=None, logger=None):
        locator = locator or self.DEFAULT_LOCATOR
        super().__init__(parent, locator, logger=logger)

    ROOT = ParametrizedLocator("{@locator}")


class CardForCardGroup(BaseCard, ParametrizedView):
    DEFAULT_LOCATOR = "(.//div[contains(@data-ouia-component-type, '/Card')] | .//article[contains(@class, '-c-card')])"

    def __init__(self, parent, locator=None, logger=None, **kwargs):
        View.__init__(self, parent, logger=logger, **kwargs)
        self.locator = locator or self.DEFAULT_LOCATOR

    PARAMETERS = ("position",)

    ROOT = ParametrizedLocator("{@locator}[{position}]")

    def __locator__(self):
        return self.ROOT

    @classmethod
    def all(cls, browser):
        # todo: OUIA versions should return component ids
        elements = browser.elements(cls.DEFAULT_LOCATOR)
        result = []
        for index, item in enumerate(elements):
            result.append((index + 1,))
        return result


class CardGroup(GenericLocatorWidget, View):
    def __init__(self, parent, locator=None, logger=None, **kwargs):
        View.__init__(self, parent, logger=logger, **kwargs)
        self.locator = locator

    cards = ParametrizedView.nested(CardForCardGroup)

    def __iter__(self):
        return iter(self.cards)


class CardWithActions(Card):
    dropdown = Dropdown(locator=".//div[contains(@class, '-c-card__actions')]")
    checkbox = Checkbox(locator=".//input[contains(@class, '-c-check__input')]")


class CardCheckBox(Checkbox):
    ROOT = ".//input[contains(@class, '-c-check__input')]"
