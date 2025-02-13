from widgetastic.exceptions import NoSuchElementException
from widgetastic.widget import TextInput

from .dropdown import Dropdown, DropdownItemDisabled, DropdownItemNotFound


class SelectItemDisabled(DropdownItemDisabled):
    pass


class SelectItemNotFound(DropdownItemNotFound):
    pass


class BaseSelect:
    """Represents the Patternfly Select.

    https://www.patternfly.org/components/menus/select
    """

    BUTTON_LOCATOR = ".//button"
    ITEMS_LOCATOR = (
        ".//ul[contains(@class, '-c-menu__list') or contains(@class, '-c-select__menu')]/"
        "li[contains(@class, '-c-menu__list-item') or contains(@class, '-c-select__menu-wrapper')]"
    )
    ITEM_LOCATOR = (
        ".//*[(contains(@class, '-c-menu__list-item') or contains(@class, '-c-select__menu-item'))"
        " and normalize-space(.)={}]"
    )
    SELECTED_ITEM_LOCATOR = (
        ".//span[contains(@class, 'ins-c-conditional-filter') and normalize-space(.)={}]"
    )
    TEXT_LOCATOR = ".//div[contains(@class, '-c-select') and child::button[normalize-space(.)={}]]"

    def item_element(self, item, close=True):
        """Returns a WebElement for given item name."""
        try:
            return super().item_element(item, close)
        except DropdownItemNotFound:
            raise SelectItemNotFound(
                f"Item {item!r} not found in {repr(self)}. Available items: {self.items}"
            )

    def item_select(self, item):
        """Opens the Select and selects the desired item.

        Args:
            item: Item to be selected

        Raises:
            SelectItemDisabled: if item is disabled
        """
        try:
            return super().item_select(item)
        except DropdownItemDisabled:
            raise SelectItemDisabled('Item "{}" of {} is disabled')

    def fill(self, value):
        """Fills a Select with a value."""
        if self.read() == value:
            return False
        self.item_select(value)
        return True

    def read(self):
        """Returns a string of the text of the selected option."""
        return self.browser.text(self.BUTTON_LOCATOR)


class Select(BaseSelect, Dropdown):
    DEFAULT_LOCATOR = './/div[contains(@class, "-c-select")][1]'


class BaseCheckboxSelect(BaseSelect):
    """Represents the Patternfly Checkbox Select.

    https://www.patternfly.org/components/menus/select/#checkbox
    """

    ITEMS_LOCATOR = (
        ".//*[contains(@class, '-c-menu__list-item') or contains(@class, '-c-select__menu-item')]"
    )
    ITEM_LOCATOR = (
        f"{ITEMS_LOCATOR}[.//span[starts-with(normalize-space(.), {{}})]]//input[@type='checkbox']"
    )

    def item_select(self, items, close=True):
        """Opens the Checkbox and selects the desired item.

        Args:
            item: Item to be selected
            close: Close the dropdown when finished
        """
        if not isinstance(items, list | tuple | set):
            items = [items]

        try:
            for item in items:
                element = self.item_element(item, close=False)
                if not self.browser.is_selected(element):
                    element.click()
        finally:
            if close:
                self.close()

    def item_deselect(self, items, close=True):
        """Opens the Checkbox and deselects the desired item.

        Args:
            item: Item to be selected
            close: Close the dropdown when finished
        """
        if not isinstance(items, list | tuple | set):
            items = [items]

        try:
            for item in items:
                element = self.item_element(item, close=False)
                if self.browser.is_selected(element):
                    element.click()
        finally:
            if close:
                self.close()

    def fill(self, items):
        """Fills a Checkbox with all items.
        Example dictionary: {"foo": True, "bar": False, "baz": True}

        Args:
            items: A dictionary containing what items to select (True) or deselect (False)
        """
        current_values = self.read()
        has_changed = False
        try:
            for item, value in items.items():
                if value == current_values.get(item, None):
                    continue
                if value:
                    self.item_select(item, close=False)
                else:
                    self.item_deselect(item, close=False)
                has_changed = True
        finally:
            self.close()
        return has_changed

    def read(self):
        """Returns a dictionary containing the selected status as bools."""
        selected = {}
        with self.opened():
            items_element = self.browser.elements(self.ITEMS_LOCATOR) or self.root_browser.elements(
                self.ITEMS_LOCATOR
            )
            for el in items_element:
                item = self.browser.text(el)
                try:
                    # get the child element of the label
                    selected[item] = self.browser.element(
                        parent=el, locator=".//input"
                    ).is_selected()
                except NoSuchElementException:
                    selected[item] = False

        return selected

    def _get_items(self, close=False):
        """Returns a list of all checkbox items as strings.

        Args:
            close: Close the dropdown when finished
        """
        self.open()
        items_element = self.browser.elements(self.ITEMS_LOCATOR) or self.root_browser.elements(
            self.ITEMS_LOCATOR
        )
        result = [self.browser.text(el) for el in items_element]

        if close:
            self.close()

        return result

    @property
    def items(self):
        """Returns a list of all CheckboxSelect items as strings."""
        return self._get_items(close=True)


class CheckboxSelect(BaseCheckboxSelect, Dropdown):
    DEFAULT_LOCATOR = './/div[contains(@class, "-c-select")][1]'


class BaseTypeaheadSelect(BaseSelect):
    BUTTON_LOCATOR = (
        ".//button[(contains(@class, '-c-select__toggle') "
        "or contains(@class, '-c-menu-toggle')) "
        "and not(contains(@class, '-c-select__toggle-clear'))]"
    )
    input = TextInput(locator=".//input")

    def read(self):
        return self.browser.get_attribute("value", self.input)


class TypeaheadSelect(BaseTypeaheadSelect, Dropdown):
    DEFAULT_LOCATOR = './/div[contains(@class, "-c-select")][1]'
