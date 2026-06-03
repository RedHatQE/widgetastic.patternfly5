import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import Alert

TESTING_PAGE_COMPONENT = "components/alert"
ALERT_TYPES = ["success", "danger", "warning", "info"]

# The "Alert variants" demo section ID on patternfly.org.
# Scoping to this section avoids the site-wide "Website update" info
# notification that appears as the first pf-m-info alert on PF6.
ALERT_VARIANTS_SECTION = "ws-react-c-alert-alert-variants"


@pytest.fixture(params=ALERT_TYPES)
def alert(browser, request):
    class TestView(View):
        ROOT = f".//div[@id='{ALERT_VARIANTS_SECTION}']"
        alert = Alert(locator=f".//div[contains(@class, '-c-alert pf-m-{request.param}')][1]")

    return TestView(browser).alert


def test_alert_is_displayed(alert):
    assert alert.is_displayed


def test_alert_title(alert):
    alert_type = alert.type if alert.type != "error" else "danger"
    assert alert.title == f"{alert_type.capitalize()} alert title"
