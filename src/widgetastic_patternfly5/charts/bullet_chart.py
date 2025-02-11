import re

from widgetastic.utils import ParametrizedLocator
from widgetastic.widget import Text, View
from widgetastic.xpath import quote

from .legend import DataPoint, Legend


class BulletChart(View):
    """Represents the Patternfly Bullet Chart.

    https://www.patternfly.org/charts/bullet-chart

    Args:
        id: If you want to look the input up by id, use this parameter, pass the id.
        locator: If you have specific locator else it will take pf-chart.
        offset_denominator: Denominator for offset value calculation.
    """

    ROOT = ParametrizedLocator("{@locator}")

    DEFAULT_LOCATOR = ".//div[contains(@class, 'chartbullet')]"
    ITEMS = ".//*[name()='g']/*[name()='path' and not(contains(@style, 'type:square'))]"
    TOOLTIP_REGEX = re.compile(r"(.*?): ([\d]+)")
    APPLY_OFFSET = True

    tooltip = Text(
        ".//*[name()='svg' and contains(@aria-labelledby, 'victory-container')]/"
        "following-sibling::div[contains(@style, 'z-index')]/*[name()='svg']"
    )
    _legends = View.nested(Legend)

    def __init__(self, parent=None, id=None, locator=None, logger=None, *args, **kwargs):
        View.__init__(self, parent=parent, logger=logger)
        if id:
            self.locator = f".//div[@id={quote(id)}]"
        elif locator:
            self.locator = locator
        else:
            self.locator = self.DEFAULT_LOCATOR

        self.args = args
        self.kwargs = kwargs

    def _offsets(self, el):
        """Calculate offset. Need to set offset with try and error method."""
        offset_denominator = self.kwargs.pop("offset_denominator", 2.5)
        size = self.browser.size_of(el)
        width = size.width
        height = size.height
        dx = int(width / offset_denominator) if (width > 10 and height > 10) else 0
        dy = int(height / offset_denominator) if (width > 10 and height > 10) else 0
        return dx, dy

    @property
    def legends(self):
        return [leg for leg in self._legends]

    @property
    def legend_names(self):
        """Return all legend names."""
        return [leg.label for leg in self.legends]

    def get_legend(self, label):
        """Get specific Legend object.

        Args:
            label: Name of legend label.
        """
        try:
            return next(leg for leg in self.legends if leg.label == label)
        except StopIteration:
            return None

    @property
    def data(self):
        """Read graph and returns all Data Point objects."""
        _data = []
        # focus away from graph
        self.parent_browser.move_to_element("//body")

        for el in self.browser.elements(self.ITEMS):
            self.browser.move_to_element(el)
            self.browser.click(el)

            if self.APPLY_OFFSET:
                dx, dy = self._offsets(el)
                self.browser.move_by_offset(dx, dy)

            match = self.TOOLTIP_REGEX.match(self.tooltip.text)
            if match:
                _data.append(
                    DataPoint(
                        label=match.groups()[0],
                        value=int(match.groups()[1]),
                        color=el.value_of_css_property("fill"),
                    )
                )
        return _data

    def get_data_point(self, label):
        """Get specific data point object.

        Args:
            label: Name of respective data point label.
        """
        try:
            return next(dp for dp in self.data if dp.label == label)
        except StopIteration:
            return None

    def read(self):
        """Read graph and returns label, value dict."""
        return {dp.label: dp.value for dp in self.data}
