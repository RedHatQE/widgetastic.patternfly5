from wait_for import wait_for
from widgetastic.utils import ParametrizedLocator
from widgetastic.widget import View

from widgetastic_patternfly5 import Button


class BaseDrawer:
    """Represents drawer component for pf5/pf6

    https://www.patternfly.org/components/drawer
    """

    close_btn = Button(locator=".//div[contains(@class, '-c-drawer__close')]/button")

    @property
    def is_open(self):
        """Returns True if the Drawer panel is open"""
        return "pf-m-expanded" in self.browser.classes(self)

    def close(self):
        """Close drawer."""
        if self.is_open:
            self.close_btn.click()
            wait_for(lambda: not self.is_open, num_sec=10)


class Drawer(BaseDrawer, View):
    ROOT = ParametrizedLocator("{@locator}")
    DEFAULT_LOCATOR = ".//div[contains(@class, '-c-drawer')]"

    def __init__(self, parent, locator=None, logger=None, **kwargs):
        View.__init__(self, parent, logger=logger, **kwargs)
        if locator:
            self.locator = locator
        else:
            self.locator = self.DEFAULT_LOCATOR
