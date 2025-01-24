from widgetastic_patternfly5.charts.line_chart import LineChart


class AlertsTimelineChart(LineChart):
    """Represents the Patternfly Alerts Timeline.

    https://v5-archive.patternfly.org/charts/bar-chart/#alerts-timeline

    Args:
        id: If you want to look the input up by id, use this parameter, pass the id.
        locator: If you have specific locator else it will take pf-chart.
    """

    Y_AXIS_ROW = "./*[name()='svg']/*[name()='g'][3]/*[name()='g']"
    Y_AXIS_ROW_LINE = "./*[name()='path']"

    TOOLTIP = "./*[name()='svg']/*[name()='g'][5]"
    TOOLTIP_X_AXIS_LABLE = None
    TOOLTIP_LABLES = None
    TOOLTIP_VALUES = ".//*[name()='text']/*[name()='tspan']"

    @property
    def _y_axis_labels_map(self):
        """Labels and its webelements in the Y axis
        NOTE: Y labels might not match the number of rows in Y axes.
        """
        return {self.browser.text(el): el for el in self.browser.elements(self.Y_AXIS_LABELS)}

    @property
    def labels_y_axis(self):
        """Return Y-Axis labels."""
        return list(self._y_axis_labels_map.keys())

    @property
    def _y_axis_map(self):
        """Dict with Y axis row number as key and the contained lines in each row as values."""
        y_axis_rows_els = self.browser.elements(self.Y_AXIS_ROW)
        y_axis_map = {}
        for row_n, row_el in enumerate(y_axis_rows_els):
            y_axis_map[row_n] = self.browser.elements(self.Y_AXIS_ROW_LINE, parent=row_el)
        return y_axis_map

    def read(self):
        """Read chart data."""
        _data = []

        for lines_el in self._y_axis_map.values():
            _row_data = []
            for line_el in lines_el:
                self.browser.move_to_element(line_el)
                self.browser.click(line_el)
                tooltip_el = self.browser.wait_for_element(self.TOOLTIP)

                label_data = {}
                value_els = self.browser.elements(self.TOOLTIP_VALUES, parent=tooltip_el)
                for value_el in value_els:
                    key, value = self.browser.text(value_el).lower().split(": ")
                    label_data[key] = value

                _row_data.append(label_data)
            _data.append(_row_data)

        # Just move cursor to avoid mismatch of legend and tooltip text.
        self.root_browser.move_to_element(".//body")
        return _data
