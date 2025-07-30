import re

from widgetastic.utils import ParametrizedLocator
from widgetastic.widget import ParametrizedView


class Legend(ParametrizedView):
    """Represents Legend of chart."""

    PARAMETERS = ("label_text",)

    LEGEND_LABEL = ParametrizedLocator(
        ".//*[name()='text' and (contains(@id, 'legend') or contains(@id, 'Legend'))]"
        "/*[name()='tspan' and contains(., {label_text|quote})]"
    )
    ROOT = ParametrizedLocator(".//*[name()='g' and {@LEGEND_LABEL}]")
    LEGEND_LABEL_ITEMS = (
        ".//*[name()='text' and (contains(@id, 'legend') or "
        "contains(@id, 'Legend'))]/*[name()='tspan']"
    )
    LEGEND_ICON_ITEMS = ".//*[name()='rect']/following-sibling::*[name()='path']"

    # Need to overwrite as per need.
    VALUE_REGEX = r"\b\d+\.\d+|\b\d+\b"
    LABEL_REGEX = r"[^a-zA-Z\s]"

    @property
    def _legend_color_map(self):
        _data = {}

        for icon, label_el in zip(
            self.browser.elements(self.LEGEND_ICON_ITEMS),
            self.browser.elements(self.LEGEND_LABEL_ITEMS),
        ):
            color = icon.value_of_css_property("fill")
            if not color:
                color = icon.value_of_css_property("color")
            _data[self.browser.text(label_el)] = color
        return _data

    def _label(self, text):
        string = re.sub(self.LABEL_REGEX, "", text)
        return string.strip()

    @property
    def label(self):
        """Returns the label of a Legend"""
        return self._label(self.browser.text(self.LEGEND_LABEL))

    def _value(self, text):
        numbers = re.findall(self.VALUE_REGEX, text)
        try:
            return next(float(number) if "." in number else int(number) for number in numbers)
        except StopIteration:
            return None

    @property
    def value(self):
        """Returns the value of a Legend"""
        return self._value(self.browser.text(self.LEGEND_LABEL))

    @property
    def color(self):
        """Returns the color of a Legend"""
        return self._legend_color_map.get(self.browser.text(self.LEGEND_LABEL))

    def click(self):
        """Click on a Legend"""
        self.browser.click(self.LEGEND_LABEL)

    @classmethod
    def all(cls, browser):
        """Returns a list of all items"""
        return [(browser.text(el),) for el in browser.elements(cls.LEGEND_LABEL_ITEMS)]

    def __repr__(self):
        return f"Legend({self.browser.text(self.LEGEND_LABEL)})"


class DataPoint:
    """Represents DataPoint on chart."""

    def __init__(self, label, value=None, color=None):
        self.label = label
        self.value = value
        self.color = color

    def __gt__(self, other):
        return isinstance(other, DataPoint) and self.value > other.value

    def __eq__(self, other):
        return (
            isinstance(other, DataPoint) and self.label == other.label and self.value == other.value
        )

    def __hash__(self):
        return hash((self.label, self.value))

    def __repr__(self):
        return f"DataPoint({self.label}: {self.value})"
