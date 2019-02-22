#!/usr/bin/env python

"""Command Line Interface for Nielsen CSV to Chart Exercise."""


from chart import chart_cli
from chart import Chart
from chart import utilities


if __name__ == "__main__":
    """Instantiate the Application Arguments.
    
    Setup the Application Arguments in order to pass user defined command
    line interface arguments to the Application
    
    :param None
    """
    arguments = chart_cli.ChartCLI()

    """Load and display the chart based on user defined values.
    """
    if 'file' not in chart_cli or not chart_cli.file:
        print "Please include a path to a CSV file to parse"
    else:
        chart = Chart(**{
            "file": chart_cli.file, 
            "show_values": chart_cli.show_values
        })
