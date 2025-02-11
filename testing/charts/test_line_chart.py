import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import LineChart

TESTING_PAGE_COMPONENT = "charts/line-chart/react/green-with-bottom-aligned-legend"

TEST_DATA = {
    "2015": {"Cats": "1", "Dogs": "2", "Birds": "3", "Mice": "3"},
    "2016": {"Cats": "2", "Dogs": "1", "Birds": "4", "Mice": "3"},
    "2017": {"Cats": "5", "Dogs": "7", "Birds": "9", "Mice": "8"},
    "2018": {"Cats": "3", "Dogs": "4", "Birds": "5", "Mice": "7"},
}


@pytest.fixture
def view(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-line-chart-green-with-bottom-aligned-legend']"
        chart = LineChart(locator=".//div[contains(@class, '-c-chart')]")

    return TestView(browser)


def test_line_chart(view):
    """Test LineChart widget."""

    legend_names = view.chart.legend_names
    assert view.chart.is_displayed

    expected_legends = list(TEST_DATA.values())[0].keys()

    for leg, expected_leg in zip(view.chart.legends, expected_legends):
        assert leg.label == expected_leg

    assert set(legend_names) == set(expected_legends)

    # get data point and check values
    birds_legend = view.chart.get_legend("Birds")
    assert birds_legend.label == "Birds"
    assert birds_legend.color in ["rgb(35, 81, 30)", "rgb(32, 77, 0)"]  # [pf5, pf6]

    # read graph
    assert view.chart.read() == TEST_DATA
