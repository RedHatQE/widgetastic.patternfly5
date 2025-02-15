import pytest
from widgetastic.widget import View

from widgetastic_patternfly5.ouia import Alert as AlertOUIA

TESTING_PAGE_COMPONENT = "components/alert"

ALERT_TYPES = ["InfoAlert", "SuccessAlert", "WarningAlert", "DangerAlert"]


@pytest.fixture(params=ALERT_TYPES)
def alert(browser, request):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-alert-alert-variants']"
        alert = AlertOUIA(request.param)

    view = TestView(browser)
    return view.alert


def test_alert_is_displayed(alert):
    assert alert.is_displayed


def test_alert_title(alert):
    alert_type = alert.type if alert.type != "error" else "danger"
    assert alert.title == f"{alert_type.capitalize()} alert title"
