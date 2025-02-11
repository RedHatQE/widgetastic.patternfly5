import pytest
from widgetastic.widget import View

from widgetastic_patternfly5.ouia import PatternflyTable as PatternflyTableOUIA

TESTING_PAGE_URL = "https://patternfly-react-main.surge.sh/components/table"

SORT = [
    ("Repositories table header that goes on for a long time.", "ascending", ["a", "one", "p"]),
    ("Repositories table header that goes on for a long time.", "descending", ["p", "one", "a"]),
    ("Pull requests table header that goes on for a long time.", "ascending", ["a", "b", "k"]),
    ("Pull requests table header that goes on for a long time.", "descending", ["k", "b", "a"]),
]


@pytest.mark.parametrize("sample", SORT, ids=lambda sample: f"{sample[0]}-{sample[1]}")
def test_sortable_table(browser, sample):
    header, order, expected_result = sample

    class TestView(View):
        ROOT = ".//div[contains(@id, 'ws-react-c-table-sortable')]"
        table = PatternflyTableOUIA("SortableTable")

    view = TestView(browser)
    view.table.sort_by(header, order)
    column = [row[header] for row in view.table.read()]
    assert column == expected_result
