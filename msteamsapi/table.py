from typing import List
from msteamsapi.enums import ContainerStyle, TextSize, TextWeight, TextBlockStyle, TextColor


class TableCell(object):
    def __init__(self, content: object, show_border=True, rounded_corners=False, background_image_url=None):
        self.table_cell = {
            "type": "TableCell",
            "items": [content.to_dict()],
            "showBorder": show_border,
            "roundedCorners": rounded_corners,
        }
        if background_image_url:
            self.table_cell["backgroundImage"] = dict(url=background_image_url)

    def to_dict(self):
        return self.table_cell


class TextBlock(object):
    def __init__(
        self,
        text,
        size=TextSize.DEFAULT,
        weight=TextWeight.DEFAULT,
        color=TextColor.DEFAULT,
        style=TextBlockStyle.DEFAULT,
        wrap=True,
    ):
        self.text_block = {
            "type": "TextBlock",
            "text": text,
            "wrap": wrap,
            "style": style.value,
            "size": size.value,
            "weight": weight.value,
            "color": color.value
        }

    def to_dict(self):
        return self.text_block


class CompoundButton(object):
    def __init__(self, title: str, badge: str | None, separator: bool, description: str):
        """
        a CompoundButton

        Args:
            title (str): the title
            badge (str): the badge on it
            separator (bool): use a separator or not
            description (str): describe what this element is for
        """
        self.compound_button = dict(
            type="CompoundButton", title=title, badge=badge, separator=separator, description=description
        )

    def to_dict(self):
        return self.compound_button


class Table(object):
    def __init__(
        self,
        width_of_columns: List[int],
        grid_style=ContainerStyle.DEFAULT,
        first_row_as_headers=False,
        show_grid_lines=True,
    ):
        """Basic Table initialization, with number of columns and the width
           of each column provided in the width_of_columns list (i.e. length of the list = nr_of_columns)

           add content later by calling the

        Args:
            width_of_columns (List[int]): _description_
            grid_style (_type_, optional): _description_. Defaults to ContainerStyle.DEFAULT.
            first_row_as_headers (bool, optional): _description_. Defaults to False.
            show_grid_lines (bool, optional): _description_. Defaults to True.
        """
        self.table = {
            "type": "Table",
            "columns": [dict(width=int(width)) for width in width_of_columns],
            "rows": [],
            "gridStyle": grid_style.value,
            "firstRowAsHeaders": first_row_as_headers,
            "showGridLines": show_grid_lines,
        }
        self._nr_of_columns = len(width_of_columns)

    @property
    def _nr_of_rows(self):
        return len(self.table["rows"])

    def add_row(self, column_items: List[TableCell], style=ContainerStyle.DEFAULT):
        """add a row to the table
           The column_items list must contain an object to put in the cell of each column
        Args:
            column_items (List[object]): _description_
            style (_type_, optional): _description_. Defaults to ContainerStyle.DEFAULT.
        """
        assert len(column_items) == self._nr_of_columns
        self.table["rows"].append(
            {"type": "TableRow", "cells": [column_item.to_dict() for column_item in column_items], "style": style.value}
        )

    def to_dict(self):
        return self.table
