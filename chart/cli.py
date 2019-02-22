#!/usr/bin/env python

"""Command Line Interface for Nielsen CSV to Chart Exercise."""


from . import argparse


class ChartCLI(object):
    """Command Line Interface.
    
    Setup named application arguments and command line interface help
    information.
    
    :param (class) self
        The representation of the instantiated Class Instance
    :param (class) parser
        The name of the application
    :param (class) args
        The name of the enviornment in which to load the application
    """

    def __init__(self, parser=None, args=None):
        """Command Line Interface constructor.
        
        :param (object) self
        :param (object) parser
        :param (object) args
        """
        self.parser = argparse.ArgumentParser(**{
            'prog': 'Nielsen Chart Exercise',
            'description': 'Joshua Powell\'s Technical CSV to Chart exercise.'
        })

        self.parser.add_argument('--file', **{
            'type': str,
            'help': 'This can be a relative path `data/sample1.csv`'
                    ' or it can be an asolute path `/[DIR]/1.csv`'
        })

        self.parser.add_argument('--show_values', **{
            'type': utilities.boolean_string,
            'help': 'Display bar values, defaults to True',
            'default': True
        })

        self.args = self.parser.parse_args()
