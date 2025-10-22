import pytest

from widgetastic_patternfly5 import (
    DropdownItemNotFound,
    GroupDropdown,
)

TESTING_PAGE_COMPONENT = "components/menus/dropdown"


@pytest.fixture()
def group_dropdown(browser):
    dropdown = GroupDropdown(
        browser,
        locator=".//div[@id='ws-react-c-dropdown-with-groups-of-items']",
    )
    dropdown.wait_displayed("10s")
    return dropdown


def test_group_dropdown(group_dropdown, pf_version):
    assert group_dropdown.is_displayed
    assert group_dropdown.is_enabled
    assert group_dropdown.items == [
        "Action",
        "Link",
        "Group 2 action",
        "Group 2 link",
        "Group 3 action",
        "Group 3 link",
    ]
    assert group_dropdown.has_item("Group 2 link")
    assert group_dropdown.item_enabled("Group 3 action")
    expected_group = ["", "Group 2", "Group 3"] if pf_version == "v5" else ["Group 2", "Group 3"]
    assert group_dropdown.groups == expected_group
    group_dropdown.item_select("Group 3 action", group_name="Group 3")
    with pytest.raises(DropdownItemNotFound):
        group_dropdown.item_select("Group 3 action", group_name="Group 2")
    group_dropdown.item_select("Link")
