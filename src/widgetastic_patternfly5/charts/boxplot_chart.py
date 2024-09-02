from widgetastic_patternfly5.charts.line_chart import LineChart


class BoxPlotChart(LineChart):
    """Represents the Patternfly Boxplot Chart.

    https://patternfly-react-main.surge.sh/charts/box-plot-chart#embedded-legend

    Args:
        id: If you want to look the input up by id, use this parameter, pass the id.
        locator: If you have specific locator else it will take pf-chart.
    """

    def read(self, offset=(0, -100)):
        """Read chart data.

        Note: This method has some limitations as we are reading the tooltip for x-axis labels
        with some offset. So only applicable for the chart which shows all Legend data in a single
        tooltip for the respective x-axis label.

        Args:
            offset: offset to move the cursor from the x-axis label so that the tooltip can appear.
        """
        _data = {}

        for lab_el in self._x_axis_labels_map.values():
            self.browser.move_to_element(lab_el)
            self.browser.click(lab_el)
            self.browser.move_by_offset(*offset)
            tooltip_el = self.browser.wait_for_element(self.TOOLTIP, timeout=5)

            x_axis_label = self.browser.text(self.TOOLTIP_X_AXIS_LABLE, parent=tooltip_el)
            # print("X axis label",x_axis_label)
            label_data = {}

            for label_el, value_el in zip(
                self.browser.elements(self.TOOLTIP_LABLES, parent=tooltip_el),
                self.browser.elements(self.TOOLTIP_VALUES, parent=tooltip_el),
            ):
                # print("Value is",self.browser.text(value_el))
                # pdb.set_trace()
                label = self.browser.text(label_el).strip()
                if not label:
                    label = "Data"
                if label in label_data:
                    if isinstance(label_data[label], list):
                        label_data[label] = self.browser.text(value_el)
                    else:
                        label_data[label] = [label_data[label], self.browser.text(value_el)]
                else:
                    label_data[label] = self.browser.text(value_el)
            # print("label_data",label_data)
            _data[x_axis_label] = label_data
            # print("Data Value is", _data[x_axis_label])
            self._parse_data_entries(label_data)
            # print("converted label_data",label_data)

        # Just move cursor to avoid mismatch of legend and tooltip text.
        self.root_browser.move_to_element(".//body")
        return _data

    def _parse_data_entries(self, label_data):
        """Parse 'Data' entries into a dictionary of key-value pairs."""
        if "Data" in label_data and isinstance(label_data["Data"], list):
            parsed_data = {}
            for entry in label_data["Data"]:
                sub_entries = entry.split(",")
                for sub_entry in sub_entries:
                    key_value = sub_entry.split(":")
                    if len(key_value) == 2:
                        key = key_value[0].strip()
                        value = key_value[1].strip()
                        parsed_data[key] = value
            label_data["Data"] = parsed_data

    def read_single_datapoint(self, x_axis_label, offset=(0, -100)):
        """Read chart data for a single data point.

        Note: This method is applicable for the chart which shows all Legend data in a single
        tooltip for the respective x-axis label.

        Args:
            x_axis_label: The x-axis label to fetch data for.
            offset : Offset to move the cursor from the x-axis label so that the tooltip can appear.
        """
        _data = {}

        # Locate the element for the given x-axis label
        lab_el = self._x_axis_labels_map.get(x_axis_label)

        if lab_el is None:
            raise ValueError(f"X-axis label '{x_axis_label}' not found in the x-axis labels map.")

        # Move to the element, click to activate tooltip, and move to show tooltip
        self.browser.move_to_element(lab_el)
        self.browser.click(lab_el)
        self.browser.move_by_offset(*offset)
        tooltip_el = self.browser.wait_for_element(self.TOOLTIP, timeout=5)

        # Initialize label_data dictionary
        label_data = {}

        # Extract label and value pairs from the tooltip
        for label_el, value_el in zip(
            self.browser.elements(self.TOOLTIP_LABLES, parent=tooltip_el),
            self.browser.elements(self.TOOLTIP_VALUES, parent=tooltip_el),
        ):
            # print("Value is",self.browser.text(value_el))
            # pdb.set_trace()
            label = self.browser.text(label_el).strip()
            if not label:
                label = "Data"
            if label in label_data:
                if isinstance(label_data[label], list):
                    label_data[label] = self.browser.text(value_el)
                else:
                    label_data[label] = [label_data[label], self.browser.text(value_el)]
            else:
                label_data[label] = self.browser.text(value_el)

        # Store the extracted data in the _data dictionary with x_axis_label as key
        _data[x_axis_label] = label_data

        # print("Extracted label_data:", label_data)
        self._parse_data_entries(label_data)

        # Just move cursor to avoid mismatch of legend and tooltip text.
        self.root_browser.move_to_element(".//body")

        return _data

    def update_chart_data_dict(self, data_dict, key_to_remove, key_to_update):
        """
        Updates a dictionary by removing a specified key
        and appending its data to another key's value.

        Args:
            data_dict: The dictionary to update.
            key_to_remove : The key to remove and get its data from.
            key_to_update : The key whose value will be updated with data from the removed key.

        Returns:
            dict: The updated dictionary.
        """
        # Iterate over each year in the dictionary
        for year, sub_dict in data_dict.items():
            # Get the data to remove and append
            data = sub_dict.pop(key_to_remove, None)

            if data:
                # If the data to remove is a dictionary, append its entries to the target key
                if isinstance(data, dict):
                    target_dict = sub_dict.get(key_to_update, {})
                    if isinstance(target_dict, str):
                        # Convert the existing string to a dictionary if needed
                        target_dict = dict(
                            item.split(":", 1) for item in target_dict.split(", ") if ":" in item
                        )

                    # Append each item from the data dictionary
                    target_dict.update(data)
                    sub_dict[key_to_update] = target_dict
                elif isinstance(data, list):
                    # If data is a list, join the list items into a single string
                    # data_string = ", ".join(data)
                    target_dict = sub_dict.get(key_to_update, "")
                    if isinstance(target_dict, str):
                        # Convert the existing string to a dictionary if needed
                        target_dict = dict(
                            item.split(":", 1) for item in target_dict.split(", ") if ":" in item
                        )

                    # Add new data items
                    for item in data:
                        key_value_pair = item.split(":", 1)
                        if len(key_value_pair) == 2:
                            key = key_value_pair[0].strip()
                            value = key_value_pair[1].strip()
                            target_dict[key] = value

                    sub_dict[key_to_update] = target_dict

        return data_dict
