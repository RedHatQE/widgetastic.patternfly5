import pytest
from widgetastic.widget import View

from widgetastic_patternfly5 import FormSelectOptionNotFound
from widgetastic_patternfly5.ouia import FormSelect as FormSelectOUIA

TESTING_PAGE_URL = "https://patternfly-react-main.surge.sh/components/forms/form-select"


@pytest.fixture
def view(browser):
    class FormSelectTestView(View):
        ROOT = ".//div[@id='ws-react-c-form-select-basic']"
        input = FormSelectOUIA("BasicFormSelect")

    return FormSelectTestView(browser)


def test_formselect_visibility(view):
    assert view.input.is_displayed


def test_formselect_enablement(view):
    assert view.input.is_enabled


def test_formselect_validity(view):
    assert view.input.is_valid


def test_formselect_value(view):
    assert len(view.input.all_options) == 7
    assert len(view.input.all_enabled_options) == 6
    assert "Mrs" in view.input.all_options
    view.input.fill("Mrs")
    assert view.input.read() == "Mrs"


def test_formselect_option_enablement(view):
    expected_enabled_options = {"Mr", "Miss", "Mrs", "Ms", "Dr", "Other"}
    expected_disabled_options = {"Please Choose"}
    assert set(view.input.all_enabled_options) == expected_enabled_options
    assert expected_disabled_options not in set(view.input.all_enabled_options)


def test_formselect_fill_nonexistent_option(view):
    with pytest.raises(FormSelectOptionNotFound):
        view.input.fill("foo")
