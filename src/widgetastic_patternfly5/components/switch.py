from widgetastic.widget import GenericLocatorWidget


class SwitchDisabled(Exception):
    pass


class BaseSwitch:
    """Represents the Patternfly Switch.

    https://www.patternfly.org/components/switch
    """

    CHECKBOX_LOCATOR = "./input"

    @property
    def is_enabled(self):
        """Returns a boolean detailing if the switch is enabled."""
        return self.browser.get_attribute("disabled", self.CHECKBOX_LOCATOR) is None

    def click(self):
        """Click on a Switch."""
        if not self.is_enabled:
            raise SwitchDisabled("{} is disabled".format(repr(self)))
        else:
            self.browser.click(self.CHECKBOX_LOCATOR)
            return True

    def __repr__(self):
        return "{}({!r})".format(type(self).__name__, self.locator)


class Switch(BaseSwitch, GenericLocatorWidget):
    pass
