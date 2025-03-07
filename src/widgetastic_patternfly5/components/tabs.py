from wait_for import wait_for_decorator
from widgetastic.utils import ParametrizedLocator
from widgetastic.widget import View


class Tab(View):
    """Represents the Patternfly Tab widget.

    Selects itself automatically when any child widget gets accessed, ensuring that the widget is
    visible.

    https://www.patternfly.org/components/tabs
    """

    # The text on the tab. Can be omitted if it is the same as the tab class name capitalized
    TAB_NAME = None

    # Locator of the Tab selector
    TAB_LOCATOR = ParametrizedLocator(
        './/div[contains(@class, "-c-tabs")]/ul/li[button[normalize-space(.)={@tab_name|quote}]]'
    )

    ROOT = ParametrizedLocator(
        ".//section[@aria-labelledby=string("
        "preceding-sibling::div/ul/li/button[normalize-space(.)={@tab_name|quote}]/@id)]"
        "|"
        ".//section[@id=string(../preceding-sibling::div/ul/li"
        "/button[normalize-space(.)={@tab_name|quote}]/@aria-controls)]"
    )

    @property
    def tab_name(self):
        """Returns the tab name as a string."""
        return self.TAB_NAME or type(self).__name__.replace("_", " ").capitalize()

    def is_active(self):
        """Returns a boolean detailing of the tab is active."""
        return "pf-m-current" in self.parent_browser.classes(self.TAB_LOCATOR)

    @property
    def is_displayed(self):
        """Returns a boolean detailing of the tab is displayed."""
        return self.parent_browser.is_displayed(self.TAB_LOCATOR)

    def click(self):
        """Clicks the tab."""
        el = self.parent_browser.move_to_element(self.TAB_LOCATOR)
        if tab_btns := self.browser.elements(".//button", parent=el):
            return self.browser.click(tab_btns[0])
        return self.parent_browser.click(el)

    def select(self):
        """Selects the tab (checks if active already first)."""
        if not self.is_active():
            self.logger.info("Opening the tab %s", self.tab_name)

            @wait_for_decorator(timeout=5)
            def _click():
                self.click()
                return self.is_active()

    def child_widget_accessed(self, widget):
        # Select the tab
        self.select()

    def __repr__(self):
        return f"<Tab {self.tab_name!r}>"
