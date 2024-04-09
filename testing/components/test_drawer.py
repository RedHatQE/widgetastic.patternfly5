import time

import pytest
from widgetastic.widget import Text
from widgetastic.widget import View

from widgetastic_patternfly5 import Button
from widgetastic_patternfly5 import Drawer


TESTING_PAGE_URL = "https://patternfly-react-main.surge.sh/components/drawer/"


@pytest.fixture(scope="module")
def view(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-drawer-basic']"

        @View.nested
        class CustomDrawer(Drawer):
            title = Text(".//div[contains(@class, '-c-drawer__head')]")

        drawer = Drawer()
        toggle_drawer = Button("Toggle drawer")

    return TestView(browser)


def test_drawer_is_displayed(view):
    assert view.drawer.is_displayed


def test_drawer_can_be_closed(view):
    assert not view.drawer.is_open
    view.toggle_drawer.click()
    assert view.drawer.is_open
    time.sleep(1)
    view.drawer.close()
    assert not view.drawer.is_open


def test_drawer_as_view(view):
    assert view.CustomDrawer.is_displayed
    time.sleep(1)
    view.toggle_drawer.click()
    assert view.CustomDrawer.is_open
    assert view.CustomDrawer.title.text == "drawer-panel"
    view.CustomDrawer.close()
