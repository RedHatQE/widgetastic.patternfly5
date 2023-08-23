from widgetastic.utils import ParametrizedLocator
from widgetastic.widget import View


class BaseDrawer:
    """Represents drawer component for pf5

    https://www.patternfly.org/components/drawer
    """

    CLOSE = ".//button[@aria-label='Close drawer panel']"

    @property
    def is_open(self):
        """Returns True if the Drawer panel is open"""
        return "pf-m-expanded" in self.browser.classes(self)

    def close(self):
        """Close drawer."""
        if self.is_open:
            self.browser.click(self.browser.element(self.CLOSE))


class Drawer(BaseDrawer, View):
    ROOT = ParametrizedLocator("{@locator}")
    DEFAULT_LOCATOR = ".//div[contains(@class, '-c-drawer')]"

    def __init__(self, parent, locator=None, logger=None, **kwargs):
        View.__init__(self, parent, logger=logger, **kwargs)
        if locator:
            self.locator = locator
        else:
            self.locator = self.DEFAULT_LOCATOR
