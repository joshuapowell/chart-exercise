#!/usr/bin/env python

"""Nielsen CSV to Chart Exercise Utilities."""


def boolean_string(argument):
    """Create custom string type to ensure that True/False are bool values.

    :param (str) argument

    :return (bool)
    """
    if argument not in {'False', 'True'}:
        return False
    return argument == 'True'