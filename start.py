"""Nielsen Chart Exercise for Technical Interview.

Created by Joshua Powell on 02/21/2019.
"""


import argparse
import csv
import sys


class Chart:
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

    def get_styled_value(self, columnValue, current_style):
        """Return a styled bar value based on column value and style.

        :param (object) self
        :param (str) columnValue
        :param (int) current_style

        :return (str)
        """
        labels = ""

        if self.show_values:
            labels = "(%s)" % (columnValue)

        value = self.get_value(columnValue)
        style = self.style[current_style]

        display = (value*style)

        return ("%s %s") % (display, labels)

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

        return key

    def load(self):
        """Load data for chart and draw bar chart.

        :param (object) self

        :return None
        """
        try:
            with open(self.file) as csvfile:
                reader = csv.reader(csvfile)

                for row_index, row in enumerate(reader):

                    current_style = 0

                    if row_index == 0:
                        print self.get_legend(row)
                    else:
                        column_ = self.get_styled_value(row[1], current_style)
                        print "%s |%s" % (row[0], column_)

                        for column_index, column in enumerate(row):

                            current_style = 0 if current_style == 1 else 1

                            if column_index != 0 and column_index != 1:
                                column_n = self.get_styled_value(column,
                                                                 current_style)
                                print "     |%s" % (column_n)

                    print "\r"

        except Exception:
            print "Unable to open your CSV file"


if sys.argv and len(sys.argv) >= 2:

    def boolean_string(argument):
        """Create custom string type to ensure that True/False are bool values.

        :param (str) argument

        :return (bool)
        """
        if argument not in {'False', 'True'}:
            return False
        return argument == 'True'

    """Setup ability to use command line arguments to change Chart options.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--file',
                        type=str,
                        help="This can be a relative path `data/sample1.csv`"
                             " or it can be an asolute path `/[DIR]/1.csv`")
    parser.add_argument('--show_values',
                        default=True,
                        type=boolean_string,
                        help="Display bar values, defaults to True")

    args = parser.parse_args()

    """Load and display the chart based on user defined values.
    """
    chart = Chart(file=args.file, show_values=args.show_values)

else:
    print "Please include a path to your CSV file"
