from urllib.parse import urljoin

import pytest
from widgetastic.browser import Browser
from widgetastic.widget import View

from widgetastic_patternfly5 import CategoryChipGroup, ChipGroup

TESTING_PAGE_COMPONENT = "components/chip"


@pytest.fixture(scope="module")
def chip_group_view(browser):
    class TestView(View):
        ROOT = './/h3[text()="Chip groups"]/ancestor::div[@class="ws-example" or contains(@class, "pf-m-gutter")][1]'

        non_existent_chip_group = ChipGroup(locator="foobar-locator")
        chip_group = ChipGroup()

    return TestView(browser)


@pytest.fixture(scope="module")
def category_chip_group_view(browser):
    class TestView(View):
        ROOT = './/h3[text()="Chip groups with removable categories"]/ancestor::div[@class="ws-example" or contains(@class, "pf-m-gutter")][1]'
        category_one = CategoryChipGroup(label="Category one")
        category_two = CategoryChipGroup(label="Category two has a very long name")

    return TestView(browser)


def test_non_existent_chips(chip_group_view):
    assert not chip_group_view.non_existent_chip_group.is_displayed


def test_chipgroup_simple(chip_group_view):
    assert chip_group_view.is_displayed
    assert chip_group_view.chip_group.is_displayed

    chips = [
        "Chip one",
        "Really long chip that goes on and on",
        "Chip three",
        "Chip four",
        "Chip five",
    ]
    assert chip_group_view.chip_group.read() == chips

    chip_group_view.chip_group.show_less()
    chips = ["Chip one", "Really long chip that goes on and on", "Chip three"]
    assert [chip.text for chip in chip_group_view.chip_group.get_chips(show_more=False)] == chips

    chips = ["Chip one", "Chip three", "Chip four", "Chip five"]
    chip_group_view.chip_group.remove_chip_by_name("Really long chip that goes on and on")
    assert chip_group_view.chip_group.read() == chips

    chip_group_view.chip_group.remove_all_chips()
    assert not chip_group_view.chip_group.has_chips


def test_chipgroup_category(category_chip_group_view):
    assert category_chip_group_view.category_one.is_displayed
    assert category_chip_group_view.category_one.label == "Category one"

    chips = ["Chip one", "Chip two", "Chip three"]
    assert category_chip_group_view.category_one.read() == chips

    category_chip_group_view.category_one.close()
    assert not category_chip_group_view.category_one.is_displayed

    # This tests that a category disappears after all chips are removed
    # category_chip_group_view.category_two.remove_all_chips()
    # assert not category_chip_group_view.category_two.is_displayed


@pytest.fixture(scope="module")
def label_overflow_view(browser_context, pf_version):
    """Navigate to the PF6 Label page to test overflow exclusion on label-based chips."""
    testing_pages = {"v6": "https://www.patternfly.org", "v5": "https://v5-archive.patternfly.org"}
    page = browser_context.new_page()
    page.goto(urljoin(testing_pages[pf_version], "components/label"), wait_until="networkidle")
    b = Browser(page)

    class TestView(View):
        ROOT = './/h3[text()="Label group with overflow"]/ancestor::div[@class="ws-example" or contains(@class, "pf-m-gutter")][1]'
        label_group = ChipGroup()

    yield TestView(b)
    page.close()


@pytest.mark.skip_if_pf5
def test_overflow_text_excluded_from_label_chips(label_overflow_view):
    """Overflow button text must not appear in chip list when matching via -c-label class."""
    group = label_overflow_view.label_group
    assert group.is_displayed
    assert group.overflow.is_displayed
    chips = [chip.text for chip in group.get_chips(show_more=False)]
    overflow_text = group.overflow.text
    assert len(chips) > 0
    assert overflow_text not in chips
