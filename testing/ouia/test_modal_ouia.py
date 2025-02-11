import pytest
from widgetastic.widget import Text, View

from widgetastic_patternfly5 import ModalItemNotFound
from widgetastic_patternfly5.ouia import Button as ButtonOUIA
from widgetastic_patternfly5.ouia import Modal as ModalOUIA

TESTING_PAGE_URL = "https://patternfly-react-main.surge.sh/components/modal"


@pytest.fixture()
def modal(browser):
    class ModalTestView(View):
        ROOT = ".//div[@id='ws-react-c-modal-basic-modals']"
        show_modal = ButtonOUIA("ShowBasicModal")

    modal = ModalOUIA(browser, "BasicModal")

    view = ModalTestView(browser)
    view.show_modal.click()
    yield modal
    if modal.is_displayed:
        modal.close()


class CustomModal(ModalOUIA):
    """Model use as view and enhance with widgets"""

    custom_body = Text(".//div[contains(@class, 'pf-v5-c-modal-box__body')]")


def test_title(modal):
    assert modal.title


def test_body(modal):
    body = modal.body
    assert body.text.startswith("Lorem")


def test_close(modal):
    modal.close()
    assert not modal.is_displayed


def test_footer_items(modal):
    items = modal.footer_items
    assert len(items) == 2
    assert "Cancel" in items
    assert "Confirm" in items


def test_footer_item(modal):
    item = modal.footer_item("Confirm")
    assert item.text == "Confirm"
    item.click()
    assert not modal.is_displayed


def test_footer_item_invalid(modal):
    items = modal.footer_items
    with pytest.raises(ModalItemNotFound) as e:
        modal.footer_item("INVALID")
    assert str(e.value) == f"Item INVALID not found. Available items: {items}"


def test_modal_as_view(browser, modal):
    view = CustomModal(browser, "BasicModal")
    assert view.is_displayed
    assert view.custom_body.text == modal.body.text
