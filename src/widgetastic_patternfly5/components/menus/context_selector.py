from .select import Select


class BaseContextSelector:
    ITEMS_LOCATOR = (
        ".//ul[contains(@class, '-c-menu__list') or @class='pf-c-context-selector__menu-list']/li"
    )
    ITEM_LOCATOR = (
        ".//*[(contains(@class, '-c-menu__list-item') or contains(@class, "
        "'pf-c-context-selector__menu-list-item'))"
        " and normalize-space(.)={}]"
    )
    SEARCH_INPUT_LOCATOR = ".//input[@type='search' or @type='text']"
    SEARCH_BUTTON_LOCATOR = ".//button[contains(@aria-label, 'Search')]"

    def item_select(self, item, use_search=False):
        """Opens the Context Selector and selects the desired item.

        Args:
            item: Item to be selected
            use_search: whether to search for item before selecting it
        """
        self.logger.info("Selecting %r in %r", item, self)
        with self.opened():
            if use_search:
                self.browser.send_keys(item, self.SEARCH_INPUT_LOCATOR)
                self.browser.click(self.SEARCH_BUTTON_LOCATOR)
            self.browser.click(self.item_element(item, close=False))


class ContextSelector(BaseContextSelector, Select):
    pass
