from widgetastic.ouia import OUIAGenericView
from widgetastic.ouia import OUIAGenericWidget
from widgetastic.ouia.input import TextInput as BaseOuiaTextInput
from widgetastic.ouia.text import Text as BaseOuiaText
from widgetastic.widget.table import Table
from widgetastic.xpath import quote

from widgetastic_patternfly5.components.alert import BaseAlert
from widgetastic_patternfly5.components.breadcrumb import BaseBreadCrumb
from widgetastic_patternfly5.components.button import BaseButton
from widgetastic_patternfly5.components.card import BaseCard
from widgetastic_patternfly5.components.forms.formselect import BaseFormSelect
from widgetastic_patternfly5.components.menus.menu import BaseCheckboxMenu
from widgetastic_patternfly5.components.menus.menu import BaseMenu
from widgetastic_patternfly5.components.modal import BaseModal
from widgetastic_patternfly5.components.navigation import BaseNavigation
from widgetastic_patternfly5.components.pagination import BaseCompactPagination
from widgetastic_patternfly5.components.pagination import BasePagination
from widgetastic_patternfly5.components.table import BaseExpandableTable
from widgetastic_patternfly5.components.table import BasePatternflyTable
from widgetastic_patternfly5.components.title import BaseTitle


class Alert(BaseAlert, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "PF5/Alert"


class BreadCrumb(BaseBreadCrumb, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "PF5/Breadcrumb"


class Button(BaseButton, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "PF5/Button"


class Card(BaseCard, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "PF5/Card"


class FormSelect(BaseFormSelect, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "PF5/FormSelect"


class Menu(BaseMenu):
    OUIA_COMPONENT_TYPE = "PF5/Menu"


class CheckboxMenu(BaseCheckboxMenu):
    OUIA_COMPONENT_TYPE = "PF5/Menu"


class Modal(BaseModal, OUIAGenericView):
    OUIA_COMPONENT_TYPE = "PF5/ModalContent"


class Navigation(BaseNavigation, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "PF5/Nav"


class Pagination(BasePagination, OUIAGenericView):
    OUIA_COMPONENT_TYPE = "PF5/Pagination"


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
        self.component_type = "PF5/Table"
        self.component_id = component_id
        super().__init__(
            parent,
            locator=(
                f".//*[@data-ouia-component-type={quote(self.component_type)} "
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


class Title(BaseTitle, OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "PF5/Title"


class Text(BaseOuiaText):
    OUIA_COMPONENT_TYPE = "PF5/Text"


class TextInput(BaseOuiaTextInput):
    OUIA_COMPONENT_TYPE = "PF5/TextInput"
