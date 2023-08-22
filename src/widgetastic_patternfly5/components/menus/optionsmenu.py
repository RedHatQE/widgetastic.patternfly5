from .dropdown import Dropdown


class BaseOptionsMenu:
    BUTTON_LOCATOR = ".//button[contains(@class, 'pf-v5-c-menu-toggle')]"
    ITEMS_LOCATOR = ".//ul[contains(@class, 'pf-v5-c-menu__list')]/li"
    ITEM_LOCATOR = ".//*[contains(@class, 'pf-v5-c-menu__list-item') and normalize-space(.)={}]"
    TEXT_LOCATOR = (
        './/div[contains(@class, "c-options-menu") and child::button[normalize-space(.)={}]]'
    )
    DEFAULT_LOCATOR = './/div[contains(@class, "c-options-menu")][1]'

    SELECTED_ITEMS_LOCATOR = (
        f"{ITEMS_LOCATOR}/button[.//*[name()='svg'] or descendant::i[not(@hidden)]]"
    )

    @property
    def selected_items(self):
        """Returns a list of all selected items in the options menu."""
        with self.opened():
            return [
                self.browser.text(el) for el in self.browser.elements(self.SELECTED_ITEMS_LOCATOR)
            ]


class OptionsMenu(BaseOptionsMenu, Dropdown):
    pass
