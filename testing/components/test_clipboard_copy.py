import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import ClipboardCopy

TESTING_PAGE_COMPONENT = "components/clipboard-copy"


@pytest.fixture
def view(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-clipboard-copy-basic']"
        clipboardEditable = ClipboardCopy(
            locator="//div[@id='ws-react-c-clipboard-copy-basic']/div[1]"
        )
        clipboardReadOnly = ClipboardCopy(
            locator="//div[@id='ws-react-c-clipboard-copy-read-only']/div[1]"
        )
        clipboardInline = ClipboardCopy(
            locator="//div[@id='ws-react-c-clipboard-copy-inline-compact']/div[1]"
        )

    return TestView(browser)


def test_clipboardcopy_displayed(view):
    assert view.clipboardEditable.is_displayed


def test_clipboardcopy_is_inline(view):
    assert view.clipboardEditable.is_inline is False
    assert view.clipboardInline.is_inline


def test_clipboardcopy_is_editable(view):
    assert view.clipboardEditable.is_editable


def test_clipboardcopy_is_read_only(view):
    assert view.clipboardReadOnly.is_editable is False
    assert view.clipboardInline.is_editable is False


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_clipboardcopy_text(view):
    assert "This is editable" in view.clipboardEditable.read()

    assert view.clipboardEditable.fill("Test")
    assert "Test" in view.clipboardEditable.read()

    assert "This is read-only" in view.clipboardReadOnly.read()

    assert view.clipboardInline.read() == "2.3.4-2-redhat"


def test_clipboardcopy_copy(view):
    assert view.clipboardEditable.button.is_displayed
    assert view.clipboardReadOnly.button.is_displayed
    assert view.clipboardInline.button.is_displayed
    view.clipboardReadOnly.copy()
    view.clipboardEditable.copy()
    view.clipboardInline.copy()
