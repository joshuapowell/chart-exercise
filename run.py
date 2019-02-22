#!/usr/bin/env python

"""Command Line Interface for Nielsen CSV to Chart Exercise."""


from chart import cli
from chart.chart import Chart


if __name__ == "__main__":
    """Instantiate the Application Arguments.
    
    Setup the Application Arguments in order to pass user defined command
    line interface arguments to the Application
    
    :param None
    """
    arguments = cli.ChartCLI()

    """Load and display the chart based on user defined values.
    """
    if 'file' not in arguments.args or not arguments.args.file:
        print("Please include a path to a CSV file to parse")
    else:
        chart = Chart(**{
            "file": arguments.args.file, 
            "show_values": arguments.args.show_values
        })
