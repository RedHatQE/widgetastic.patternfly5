import pytest
from widgetastic.widget import View

from widgetastic_patternfly5.components.title import Title

TESTING_PAGE_COMPONENT = "components/title"


class TitleTestView(View):
    @View.nested
    class pf5(View):
        h1 = Title("h1 defaults to 2xl")
        h2 = Title("h2 defaults to xl")
        h3 = Title("h3 defaults to lg")
        h4 = Title("h4 defaults to md")
        h5 = Title("h5 defaults to md")
        h6 = Title("h6 defaults to md")

    @View.nested
    class pf6(View):
        h1 = Title("H1-styled title")
        h2 = Title("H2-styled title")
        h3 = Title("H3-styled title")
        h4 = Title("H4-styled title")
        h5 = Title("H5-styled title")
        h6 = Title("H6-styled title")


@pytest.fixture
def view(pf_version, browser):
    main_view = TitleTestView(browser)
    if pf_version == "v5":
        return main_view.pf5
    return main_view.pf6


def test_title_text_and_size(view):
    for name in view.widget_names:
        widget = getattr(view, name)
        assert widget.is_displayed
        assert widget.text == widget.expected
        assert widget.read() == widget.expected
        assert str(widget.heading_level) == str(name)
