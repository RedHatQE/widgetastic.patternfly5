from .dropdown import Dropdown


class BaseSplitButtonDropdown:
    """Represents the Patternfly Split Button Dropdown.

    https://www.patternfly.org/components/menus/menu-toggle#split-button-toggle-with-text-label
    """

    INPUT = ".//input[@type='checkbox']"
    LABEL = ".//span[contains(@class, '-c-check__label')]"

    def check(self):
        """Check toggle checkbox."""
        if self.selected:
            return False
        self.browser.click(self.INPUT)
        return True

    def uncheck(self):
        """Uncheck toggle checkbox."""
        if not self.selected:
            return False
        self.browser.click(self.INPUT)
        return True

    @property
    def selected(self):
        """Returns selected or not"""
        return self.browser.is_selected(self.INPUT)

    def read(self):
        if self.browser.elements(self.LABEL):
            return self.browser.text(self.LABEL)
        return self.browser.text(self)


class SplitButtonDropdown(BaseSplitButtonDropdown, Dropdown):
    pass
