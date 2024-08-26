import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import BoxPlotChart

TESTING_PAGE_URL = "https://patternfly-react-main.surge.sh/charts/box-plot-chart"

TEST_DATA = {
    "2015": {"Cats": "q1: 1.75, q3: 3.5", "Limit": "12"},
    "2016": {"Cats": "q1: 2.75, q3: 8.5", "Limit": "12"},
    "2017": {"Cats": "q1: 4.25, q3: 6.5", "Limit": "12"},
    "2018": {"Cats": "q1: 1.75, q3: 4.5", "Limit": "12"},
}


@pytest.fixture
def view(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-box-plot-chart-embedded-legend']"
        chart = BoxPlotChart(locator=".//div[@class='pf-v5-c-chart']")

    return TestView(browser)


def test_boxplot_chart(view):
    legend_names = view.chart.legend_names

    # check chart is displayed
    assert view.chart.is_displayed

    # validate chart data
    assert view.chart.read() == TEST_DATA

    expected_legend_names = list(TEST_DATA.values())[0].keys()

    # validate legend names
    assert set(legend_names) == set(expected_legend_names)

    # validate x-axis keys
    assert view.chart.labels_x_axis == list(TEST_DATA.keys())

    # Validate Legends
    cats_legend = view.chart.get_legend("Cats")
    assert cats_legend.label == "Cats"
