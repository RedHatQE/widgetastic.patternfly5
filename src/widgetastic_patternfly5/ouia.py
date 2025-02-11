from widgetastic.ouia import OUIAGenericView, OUIAGenericWidget
from widgetastic.ouia.input import TextInput as BaseOuiaTextInput
from widgetastic.ouia.text import Text as BaseOuiaText
from widgetastic.widget.table import Table
from widgetastic.xpath import quote

from widgetastic_patternfly5.components.alert import BaseAlert
from widgetastic_patternfly5.components.breadcrumb import BaseBreadCrumb
from widgetastic_patternfly5.components.button import BaseButton
from widgetastic_patternfly5.components.card import BaseCard
from widgetastic_patternfly5.components.clipboard_copy import BaseClipboardCopy
from widgetastic_patternfly5.components.forms.form_select import BaseFormSelect
from widgetastic_patternfly5.components.menus.dropdown import BaseDropdown
from widgetastic_patternfly5.components.menus.menu import BaseCheckboxMenu, BaseMenu
from widgetastic_patternfly5.components.menus.select import BaseSelect, BaseTypeaheadSelect
from widgetastic_patternfly5.components.modal import BaseModal
from widgetastic_patternfly5.components.navigation import BaseNavigation
from widgetastic_patternfly5.components.pagination import BaseCompactPagination, BasePagination
from widgetastic_patternfly5.components.switch import BaseSwitch
from widgetastic_patternfly5.components.table import BaseExpandableTable, BasePatternflyTable
from widgetastic_patternfly5.components.title import BaseTitle


# TODO: Restore "PF5/<name>" once everyone has moved to using PF5
class Alert(BaseAlert, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "Alert"


class BreadCrumb(BaseBreadCrumb, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "Breadcrumb"


class Button(BaseButton, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "Button"


class Card(BaseCard, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "Card"


class CheckboxMenu(BaseCheckboxMenu):
    OUIA_COMPONENT_TYPE = "Menu"


class FormSelect(BaseFormSelect, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "FormSelect"


class Menu(BaseMenu):
    OUIA_COMPONENT_TYPE = "Menu"


class Modal(BaseModal, OUIAGenericView):
    OUIA_COMPONENT_TYPE = "ModalContent"


class Navigation(BaseNavigation, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "Nav"


class Pagination(BasePagination, OUIAGenericView):
    OUIA_COMPONENT_TYPE = "Pagination"


class CompactPagination(BaseCompactPagination, Pagination):
    pass


class PatternflyTable(BasePatternflyTable, Table):
    def __init__(
        self,
        parent,
        component_id,
        column_widgets=None,
        assoc_column=None,
        rows_ignore_top=None,
        rows_ignore_bottom=None,
        top_ignore_fill=False,
        bottom_ignore_fill=False,
        logger=None,
    ):
        self.component_type = "Table"
        self.component_id = component_id
        super().__init__(
            parent,
            locator=(
                f".//*[contains(@data-ouia-component-type,{quote(self.component_type)}) "
                f"and @data-ouia-component-id={quote(self.component_id)}]"
            ),
            column_widgets=column_widgets,
            assoc_column=assoc_column,
            rows_ignore_top=rows_ignore_top,
            rows_ignore_bottom=rows_ignore_bottom,
            top_ignore_fill=top_ignore_fill,
            bottom_ignore_fill=bottom_ignore_fill,
            logger=logger,
        )


class ExpandableTable(BaseExpandableTable, PatternflyTable):
    pass


class Switch(BaseSwitch, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "Switch"


class Title(BaseTitle, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "Title"


class Text(BaseOuiaText):
    OUIA_COMPONENT_TYPE = "Text"


class TextInput(BaseOuiaTextInput):
    OUIA_COMPONENT_TYPE = "TextInput"


class Dropdown(BaseDropdown, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "Dropdown"


class Select(BaseSelect, Dropdown):
    OUIA_COMPONENT_TYPE = "Select"


class TypeaheadSelect(BaseTypeaheadSelect, Dropdown):
    OUIA_COMPONENT_TYPE = "Select"


class ClipboardCopy(BaseClipboardCopy, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "ClipboardCopy"
