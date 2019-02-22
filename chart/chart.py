#!/usr/bin/env python

"""Command Line Interface for Nielsen CSV to Chart Exercise."""


import csv
import time
import sys


class Chart(object):
    """Create a chart from a CSV."""

    def __init__(self, file, show_values, style=None):
        """Initialize the Chart creation.

        :param (object) self
        :param (str) file
        :param (str) show_values
        :param (list) style

        """
        self.file = file
        self.style = [
            u'\u2591',
            u'\u2593'
        ]

        self.show_values = show_values

        self.load()

    def is_number(self, n):
        """Validate if n is a valid positive or negative number.

        :param (object) self
        :param (str) n

        :return (bool)
        """
        try:
            float(n)

        except ValueError:
            return False

        return True

    def get_value(self, columnValue):
        """Get a valid integer based on column value.

        :param (object) self
        :param (str) columnValue

        :return (int)
        """
        if self.is_number(columnValue):
            return int(round(float(columnValue)))

        return 0

    def get_styled_value(self, index, columnValue, current_style, adjust_zero):
        """Return a styled bar value based on column value and style.

        :param (object) self
        :param (str) columnValue
        :param (int) current_style

        :return (str)
        """
        labels = ""

        if self.show_values:
            labels = "(%s)" % (columnValue)

        """Check that value is a number before proceeding."""
        value = self.get_value(columnValue)
        
        """First bar in each group has label, accomodate for year label."""
        buffer = ""

        if index != 1:
            buffer = "     "
        
        """Determine if display is positive or negative."""
        if value < 0:
            display = (-value*self.style[current_style])
            adjust_zero_ = ""
            if adjust_zero:
                adjust_zero_ = (value-adjust_zero)*" "
            return ("%s%s%s| %s") % (adjust_zero_, buffer, display, labels)
        else:
            display = (value*self.style[current_style])
            adjust_zero_ = ""
            if adjust_zero:
                adjust_zero_ = -adjust_zero*" "
            return ("%s%s|%s %s") % (adjust_zero_, buffer, display, labels)

    def get_legend(self, row):
        """Return a styled legend/key for the chart.

        :param (object) self

        :return (str)
        """
        key = "\nKey:"

        """Reset current style."""
        current_style = 0

        for column_index, column in enumerate(row):

            if column_index != 0:
                key = key + (" %s %s") % (column, self.style[current_style])
                current_style = 0 if current_style == 1 else 1

        key = key + (" zero |")

        return key

    def get_lowest_value(self, data):

        lowest = 0

        for row in data:
            for item in row:
                value = self.get_value(item)
                if value < lowest:
                    lowest = value

        return lowest

    def load(self):
        """Load data for chart and draw bar chart.

        :param (object) self

        :return None
        """
        chart_output_filename = "output/chart-%s.txt" % (time.time())
        chart_output = open(chart_output_filename, "w")

        try:
            with open(self.file) as csvfile:
                reader = csv.reader(csvfile)

                adjust_zero = self.get_lowest_value(reader)
                
                csvfile.seek(0)

                for row_index, row in enumerate(reader):

                    current_style = 0

                    if row_index == 0:
                        legend = self.get_legend(row)
                        print legend                        
                        chart_output.write(legend.encode('utf-8'))
                        chart_output.write("\r")
                    else:
                        column_ = self.get_styled_value(1, 
                                                        row[1], 
                                                        current_style,
                                                        adjust_zero)
                        group_row = "%s %s" % (row[0], column_)

                        print group_row
                        chart_output.write(group_row.encode('utf-8'))

                        for column_index, column in enumerate(row):

                            current_style = 0 if current_style == 1 else 1

                            if column_index != 0 and column_index != 1:
                              col_group = self.get_styled_value(column_index, 
                                                                column,
                                                                current_style,
                                                                adjust_zero)
                              print col_group
                              chart_output.write("\r")
                              chart_output.write(col_group.encode('utf-8'))

                        chart_output.write("\r")

                    print "\r"
                    chart_output.write("\r")

        except Exception:
            print "Unable to open your CSV file"

        chart_output.close()

        print "A copy of this chart was saved to %s" % chart_output_filename