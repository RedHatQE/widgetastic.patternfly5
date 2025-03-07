import pytest
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
