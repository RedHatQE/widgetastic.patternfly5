from .dropdown import Dropdown


class BaseOptionsMenu:
    BUTTON_LOCATOR = (
        ".//button[contains(@class, '-c-menu-toggle') or "
        "contains(@class, '-c-options-menu__toggle')]"
    )
    ITEMS_LOCATOR = (
        ".//ul[contains(@class, '-c-menu__list') or contains(@class, '-c-options-menu__menu')]/li"
    )
    ITEM_LOCATOR = (
        ".//*[(contains(@class, '-c-menu__list-item') or "
        "contains(@class, '-c-options-menu__menu-item')) and normalize-space(.)={}]"
    )
    TEXT_LOCATOR = (
        './/div[contains(@class, "-c-options-menu") and child::button[normalize-space(.)={}]]'
    )
    # PF4/5 backward compatibility locator
    DEFAULT_LOCATOR = (
        ".//div[contains(@data-ouia-component-type, 'PaginationOptionsMenu')] | "
        "(.//button[contains(@class, '-c-menu-toggle') or contains(@class, '-c-options-menu')]/parent::div)[1]"  # noqa
    )

    SELECTED_ITEMS_LOCATOR = (
        f"{ITEMS_LOCATOR}/button[.//*[name()='svg'] or descendant::i[not(@hidden)]]"
    )

    @property
    def selected_items(self):
        """Returns a list of all selected items in the options menu."""
        with self.opened():
            selected_items_elements = self.browser.elements(
                self.SELECTED_ITEMS_LOCATOR
            ) or self.root_browser.elements(self.SELECTED_ITEMS_LOCATOR)
            return [self.browser.text(el) for el in selected_items_elements]


class OptionsMenu(BaseOptionsMenu, Dropdown):
    pass
