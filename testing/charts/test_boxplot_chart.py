import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import BoxPlotChart

TESTING_PAGE_COMPONENT = "charts/box-plot-chart/react/embedded-legend"

TEST_DATA = {
    "2015": {"Limit": "12", "Cats": "no data"},
    "2016": {"Limit": "12", "Cats": "Min: 2, Max: 10", "Unknown": "Median: 5.5, Q1: 2.75, Q3: 8.5"},
    "2017": {"Limit": "12", "Cats": "Min: 2, Max: 8", "Unknown": "Median: 5.5, Q1: 4.25, Q3: 6.5"},
    "2018": {"Limit": "12", "Cats": "Min: 1, Max: 9", "Unknown": "Median: 2.5, Q1: 1.75, Q3: 4.5"},
}


@pytest.fixture
def view(browser):
    class TestView(View):
        ROOT = ".//div[@id='ws-react-c-box-plot-chart-embedded-legend']"
        chart = BoxPlotChart(locator=".//div[contains(@class, '-c-chart')]")

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
