from datetime import datetime

import pytest
from widgetastic.widget import View

from widgetastic_patternfly5.charts.alerts_timeline_chart import AlertsTimelineChart

TESTING_PAGE_COMPONENT = "charts/bar-chart/react/alerts-timeline"


TEST_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"
LABEL_DATE_FORMAT = "%b %-d %H:%M:%S"

TEST_EXPECTED_LABELS = ["Danger", "Info", "Warning"]
# Start = "start", end = y
TEST_DATA = [
    [
        {
            "start": datetime.strptime("2024-08-06T01:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-09T02:30:00", TEST_DATE_FORMAT),
            "severity": "danger",
        },
        {
            "start": datetime.strptime("2024-08-10T05:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-10T20:00:00", TEST_DATE_FORMAT),
            "severity": "danger",
        },
        {
            "start": datetime.strptime("2024-08-12T10:00:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-13T10:30:00", TEST_DATE_FORMAT),
            "severity": "danger",
        },
    ],
    [
        {
            "start": datetime.strptime("2024-08-06T01:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-07T02:30:00", TEST_DATE_FORMAT),
            "severity": "danger",
        },
        {
            "start": datetime.strptime("2024-08-07T07:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-09T09:30:00", TEST_DATE_FORMAT),
            "severity": "danger",
        },
        {
            "start": datetime.strptime("2024-08-10T05:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-10T20:00:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-12T10:00:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-13T10:30:00", TEST_DATE_FORMAT),
            "severity": "danger",
        },
    ],
    [
        {
            "start": datetime.strptime("2024-08-06T01:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-07T02:30:00", TEST_DATE_FORMAT),
            "severity": "danger",
        },
        {
            "start": datetime.strptime("2024-08-08T07:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-09T09:30:00", TEST_DATE_FORMAT),
            "severity": "danger",
        },
        {
            "start": datetime.strptime("2024-08-10T05:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-10T20:00:00", TEST_DATE_FORMAT),
            "severity": "info",
        },
        {
            "start": datetime.strptime("2024-08-12T10:00:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-13T10:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
    ],
    [
        {
            "start": datetime.strptime("2024-08-06T01:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-08T02:30:00", TEST_DATE_FORMAT),
            "severity": "info",
        },
        {
            "start": datetime.strptime("2024-08-08T07:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-09T09:30:00", TEST_DATE_FORMAT),
            "severity": "info",
        },
        {
            "start": datetime.strptime("2024-08-10T05:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-11T20:00:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-12T10:00:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-13T10:30:00", TEST_DATE_FORMAT),
            "severity": "info",
        },
    ],
    [
        {
            "start": datetime.strptime("2024-08-06T01:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-07T02:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-08T07:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-09T09:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-09T05:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-10T20:00:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-12T10:00:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-13T10:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
    ],
    [
        {
            "start": datetime.strptime("2024-08-06T01:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-08T02:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-08T07:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-09T09:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-10T05:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-11T20:00:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-12T10:00:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-13T10:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
    ],
    [
        {
            "start": datetime.strptime("2024-08-06T01:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-07T02:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-07T04:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-08T05:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-08T07:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-09T09:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-10T05:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-10T20:00:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-11T05:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-11T20:00:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-12T10:00:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-13T10:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
    ],
    [
        {
            "start": datetime.strptime("2024-08-06T01:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-08T02:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-08T07:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-09T09:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-10T05:30:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-11T20:00:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
        {
            "start": datetime.strptime("2024-08-12T10:00:00", TEST_DATE_FORMAT),
            "end": datetime.strptime("2024-08-13T10:30:00", TEST_DATE_FORMAT),
            "severity": "warn",
        },
    ],
]


@pytest.fixture
def view(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-bar-chart-alerts-timeline']"
        chart = AlertsTimelineChart(locator=".//div[contains(@class, '-c-chart')]")

    return TestView(browser)


def test_alert_timeline(view):
    """Test LineChart widget."""
    legend_names = set(view.chart.legend_names)
    assert view.chart.is_displayed

    expected_legends = set()
    for test_row in TEST_DATA:
        for test_line in test_row:
            severity = test_line["severity"].capitalize()
            severity = (
                severity if severity != "Warn" else "Warning"
            )  # Graph label doesn't match with legend
            expected_legends.add(severity)

    assert legend_names == expected_legends

    # get data point and check values
    danger_legend = view.chart.get_legend("Danger")
    assert danger_legend.label == "Danger"
    assert danger_legend.color in ["rgb(201, 25, 11)", "rgb(177, 56, 11)"]  # [pf5, pf6]

    # read graph
    chart_read = view.chart.read()
    for row_n, row in enumerate(chart_read):
        for line_n, line in enumerate(row):
            TEST_DATA_LINE = TEST_DATA[row_n][line_n]
            assert line["severity"] == TEST_DATA_LINE["severity"]
            assert line["start"] == TEST_DATA_LINE["start"].strftime(LABEL_DATE_FORMAT).lower()
            assert line["end"] == TEST_DATA_LINE["end"].strftime(LABEL_DATE_FORMAT).lower()
