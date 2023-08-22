from widgetastic.widget import Checkbox

from widgetastic_patternfly5 import Dropdown


class BaseSplitButtonDropdown:
    """Represents the Patternfly Split Button Dropdown.

    https://www.patternfly.org/components/menus/menu-toggle#split-button-toggle-with-text-label
    """

    toggle_check = Checkbox(locator=".//input[@type='checkbox']")
    LABEL = ".//span[@class='pf-v5-c-check__label']"

    def check(self):
        """Check toggle checkbox."""
        return self.toggle_check.fill(True)

    def uncheck(self):
        """Uncheck toggle checkbox."""
        return self.toggle_check.fill(False)

    @property
    def selected(self):
        """Returns selected or not"""
        return self.toggle_check.selected

    def read(self):
        if self.browser.elements(self.LABEL):
            return self.browser.text(self.LABEL)
        return self.browser.text(self)


class SplitButtonDropdown(BaseSplitButtonDropdown, Dropdown):
    pass
