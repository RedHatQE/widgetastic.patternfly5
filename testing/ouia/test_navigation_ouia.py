import pytest
from widgetastic.widget import View

from widgetastic_patternfly5.ouia import Navigation as NavigationOUIA

TESTING_PAGE_URL = "https://patternfly-react-main.surge.sh/components/navigation"


@pytest.fixture
def view(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-navigation-default']"
        nav = NavigationOUIA("DefaultNav")

    return TestView(browser)


def test_navigation(browser, view):
    assert view.nav.currently_selected == ["Default Link 1"]
    assert view.nav.nav_item_tree() == [
        "Default Link 1",
        "Default Link 2",
        "Default Link 3",
        "Default Link 4",
    ]
