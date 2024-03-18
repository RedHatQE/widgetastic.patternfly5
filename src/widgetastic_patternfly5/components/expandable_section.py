from wait_for import wait_for_decorator
from widgetastic.widget import View


class ExpandableSection(View):
    """Represents the Patternfly Expandable section widget.

    Expands itself automatically when any child widget gets accessed, ensuring
    that the widget is visible.

    https://www.patternfly.org/components/expandable-section

    NOTE: When using this in your code you need to set the ROOT yourself!

    Example code with a button underneath the section:

        class MySection(ExpandableSection):
            ROOT = ".//div[contains(@data-testid, 'my-expandable-section')]"
            my-button = Button(locator=".//button")

    After creating the view you can run `MySection.my-button.click()` and it
    will automatically expand and click on your button.
    """

    ROOT = './/div[contains(@class, "-c-expandable-section")]'
    BUTTON_LOCATOR = ".//button"

    @property
    def is_expanded(self):
        """Returns a boolean."""
        if self.browser.get_attribute("aria-expanded", self.BUTTON_LOCATOR) == "true":
            return True
        else:
            return False

    def click(self):
        """Clicks the expandable section button."""
        return self.browser.click(self.BUTTON_LOCATOR)

    def expand(self):
        """Expands the section (checks if not expanded already first)."""
        if not self.is_expanded:

            @wait_for_decorator(timeout=3)
            def _click():
                self.click()
                return self.is_expanded

    def collapse(self):
        """Collapses the section (checks if expanded already first)."""
        if self.is_expanded:

            @wait_for_decorator(timeout=3)
            def _click():
                self.click()
                return not self.is_expanded

    def child_widget_accessed(self, widget):
        # Expand the section
        self.expand()
