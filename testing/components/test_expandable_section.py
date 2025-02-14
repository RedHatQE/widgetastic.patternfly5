from widgetastic.widget import Text, View

from widgetastic_patternfly5 import ExpandableSection

TESTING_PAGE_COMPONENT = "components/expandable-section"


class SectionView(View):
    @View.nested
    class basic(ExpandableSection):
        text = Text(".//div[contains(@class, '-c-expandable-section__content')]")


def test_section_expansion(browser):
    view = SectionView(browser)
    view.basic.expand()
    assert view.basic.is_expanded
    view.basic.collapse()
    assert not view.basic.is_expanded


def test_section_text(browser):
    view = SectionView(browser)
    assert view.basic.is_displayed
    assert view.basic.text.is_displayed
    assert view.basic.text.read() == "This content is visible only when the component is expanded."
    view.basic.collapse()
