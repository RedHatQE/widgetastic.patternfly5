import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import ContextSelector, SelectItemNotFound

TESTING_PAGE_COMPONENT = "components/menus/context-selector"


@pytest.fixture
def view(browser):
    class TestView(View):
        contextselector = ContextSelector(
            locator=".//div[@id='ws-react-demos-c-context-selector-context-selector-menu']"
        )

    return TestView(browser)


def test_contextselector_is_displayed(view):
    assert view.contextselector.is_displayed


def test_contextselector_items(view):
    assert set(view.contextselector.items) == {
        "Action",
        "Link",
        "Disabled action",
        "Disabled link",
        "My project",
        "OpenShift cluster",
        "Production Ansible",
        "AWS",
        "Azure",
        "My project 2",
        "Production Ansible 2",
        "AWS 2",
        "Azure 2",
    }
    assert view.contextselector.has_item("AWS")
    assert not view.contextselector.has_item("Non existing item")


def test_contextselector_open(view):
    assert not view.contextselector.is_open
    view.contextselector.open()
    assert view.contextselector.is_open
    view.contextselector.close()
    assert not view.contextselector.is_open


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_contextselector_item_select(view):
    view.contextselector.fill("AWS")
    assert view.contextselector.read() == "AWS"
    assert not view.contextselector.is_open
    with pytest.raises(SelectItemNotFound):
        view.contextselector.fill("Non existing item")
    assert not view.contextselector.is_open
