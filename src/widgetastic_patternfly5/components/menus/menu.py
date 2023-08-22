from widgetastic.exceptions import NoSuchElementException
from widgetastic.exceptions import UnexpectedAlertPresentException
from widgetastic.utils import ParametrizedLocator
from widgetastic.widget import Widget
from widgetastic.xpath import quote

# TODO: This is basic implementation. Enhance this as per need.


class MenuItemDisabled(Exception):
    pass


class MenuItemNotFound(Exception):
    pass


class BaseMenu:
    """Represents the Patternfly Menu.

    https://www.patternfly.org/components/menus/menu
    """

    ITEMS_LOCATOR = ".//ul[contains(@class, 'pf-v5-c-menu__list')]/li"
    ITEM_LOCATOR = ".//*[contains(@class, 'pf-v5-c-menu__list-item') and normalize-space(.)={}]"

    @property
    def items(self):
        """Returns a list of menu items."""
        result = [self.browser.text(el) for el in self.browser.elements(self.ITEMS_LOCATOR)]
        return result

    def has_item(self, item):
        """Returns whether the items exists.

        Args:
            item: item name

        Returns:
            Boolean - True if enabled, False if not.
        """
        return item in self.items

    def item_element(self, item, close=True, **kwargs):
        """Returns a WebElement for given item name."""
        try:
            return self.browser.element(self.ITEM_LOCATOR.format(quote(item)), **kwargs)
        except NoSuchElementException:
            try:
                items = self.items
            except NoSuchElementException:
                items = []
            if items:
                items_string = "These items are present: {}".format(", ".join(items))
            else:
                items_string = "The menu is probably not present"
            raise MenuItemNotFound("Item {!r} not found. {}".format(item, items_string))

    def item_enabled(self, item, **kwargs):
        """Returns whether the given item is enabled.

        Args:
            item: Name of the item.

        Returns:
            Boolean - True if enabled, False if not.
        """
        el = self.item_element(item, **kwargs)
        return "pf-m-disabled" not in self.browser.classes(el)

    def item_select(self, item, handle_alert=None, **kwargs):
        """Opens the dropdown and selects the desired item.

        Args:
            item: Item to be selected
            handle_alert: How to handle alerts. None - no handling, True - confirm, False - dismiss.

        Raises:
            DropdownItemDisabled
        """
        self.logger.info("Selecting %r", item)
        if not self.item_enabled(item, close=False, **kwargs):
            raise MenuItemDisabled(
                'Item "{}" of {} "{}" is disabled\n'
                "The following items are available: {}".format(
                    item,
                    type(self).__name__.lower(),
                    getattr(self, "text", None) or self.locator,
                    ";".join(self.items),
                )
            )
        self.browser.click(
            self.item_element(item, close=False, **kwargs), ignore_ajax=handle_alert is not None
        )
        if handle_alert is not None:
            try:
                self.browser.handle_alert(cancel=not handle_alert, wait=10.0)
                self.browser.plugin.ensure_page_safe()
            except UnexpectedAlertPresentException:
                self.logger.warning("There is an unexpected alert present.")
                pass

    def __repr__(self):
        return "{}({!r})".format(type(self).__name__, getattr(self, "text", None) or self.locator)


class Menu(BaseMenu, Widget):
    ROOT = ParametrizedLocator("{@locator}")
    DEFAULT_LOCATOR = './/div[contains(@class, "pf-v5-c-menu")][1]'

    def __init__(self, parent, locator=None, logger=None):
        super().__init__(parent, logger=logger)
        if locator:
            self.locator = locator
        else:
            self.locator = self.DEFAULT_LOCATOR
