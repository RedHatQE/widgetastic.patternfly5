from widgetastic.exceptions import NoSuchElementException
from widgetastic.widget import GenericLocatorWidget


class SwitchDisabled(Exception):
    pass


class BaseSwitch:
    """Represents the Patternfly Switch.

    https://www.patternfly.org/components/switch
    """

    CHECKBOX_LOCATOR = "./input"
    PF_5_LABEL_ON = "./span[contains(@class, 'pf-m-on')]"
    PF_5_LABEL_OFF = "./span[contains(@class, 'pf-m-off')]"
    PF_6_LABLE = "./span[contains(@class, '-c-switch__label')]"

    @property
    def is_enabled(self):
        """Returns a boolean detailing if the switch is enabled."""
        return self.browser.get_attribute("disabled", self.CHECKBOX_LOCATOR) is None

    def click(self):
        """Click on a Switch."""
        if not self.is_enabled:
            raise SwitchDisabled(f"{repr(self)} is disabled")
        else:
            self.browser.click(self.CHECKBOX_LOCATOR)
            return True

    @property
    def selected(self):
        """Returns a boolean detailing if the Switch is on (True) of off (False)."""
        return self.browser.get_attribute("checked", self.CHECKBOX_LOCATOR) is not None

    def fill(self, value):
        """Fills a Switch with the supplied value."""
        if not self.is_enabled:
            raise SwitchDisabled(f"{repr(self)} is disabled")
        if bool(value) == self.selected:
            return False
        else:
            self.browser.click(self.CHECKBOX_LOCATOR)
            return True

    @property
    def label(self):
        """Returns the label of the Switch."""
        if self.selected:
            return self._read_locator(self.PF_5_LABEL_ON) or self._read_locator(self.PF_6_LABLE)
        else:
            return self._read_locator(self.PF_5_LABEL_OFF) or self._read_locator(self.PF_6_LABLE)

    def read(self):
        """Returns a boolean detailing if the Switch is on (True) of off (False)."""
        return self.selected

    def _read_locator(self, locator):
        try:
            return self.browser.text(locator)
        except NoSuchElementException:
            return None

    def __repr__(self):
        return f"{type(self).__name__}({self.locator!r})"


class Switch(BaseSwitch, GenericLocatorWidget):
    pass
