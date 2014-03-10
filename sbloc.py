#!/usr/bin/env python
# sbloc
# Converts Sloop Betty Locations to HTML Table
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Mar 10 11:57:40 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: sbloc.py [] benjamin@bengfort.com $

"""
Coverts Sloop Bety locations to an HTML table.

Takes as input a Google Spreadsheets csv download file and exports an HTML
table formatted in the Sloop Betty locations.html structure. Will export
the table to the screen or saved to a file if given optional flags.
"""

##########################################################################
## Imports
##########################################################################

import sys
import argparse

try:
    import unicodecsv as csv
except ImportError:
    print "Warning: unicodecsv not installed, may not work on UTF-8 encoding."
    import csv

##########################################################################
## Helper functions
##########################################################################

def parseargs(**config):
    """
    Returns an argument parser
    """
    parser = argparse.ArgumentParser(**config)
    parser.add_argument('locations', type=argparse.FileType('r'), nargs='+', help="Address CSV file")
    return parser, parser.parse_args()

def tabelize(csvfile, indent=4):
    """
    Takes a CSV file and turns it into an HTML table
    """

    def cell_from_row(row, indent):
        """
        Helper function that creates an Address cell.
        """
        output = []
        output.append('%s<td width="225">' % (indent*2))
        output.append('%s<h3>%s</h3>' % (indent*3, row['Establishment']))
        output.append('%s<address>' % (indent*3))
        output.append('%s<span>%s</span>' % (indent*4, row['Address']))
        output.append('%s<span>%s, %s</span>' % (indent*4, row['City'], row['State']))
        output.append('%s</address>' % (indent*3))
        output.append('%s</td>' % (indent*2))
        return output

    # Create Table output
    output = []
    indent = " " * indent
    output.append('<table width="683" border="0" cellpadding="0">')
    output.append('%s<tr>' % indent)

    reader = csv.DictReader(csvfile)
    for idx, row in enumerate(reader):
        if idx % 3 == 0 and idx != 0:
            output.append('%s</tr>' % indent)
            output.append('%s<tr>' % indent)
        cell = cell_from_row(row, indent)
        output.extend(cell)

    # Close Table and return
    output.append('%s</tr>' % indent)
    output.append('</table>')
    return "\n".join(output)

##########################################################################
## Main functionality
##########################################################################

def main(*args, **kwargs):
    """
    Main entry point for sbloc functionality.
    """

    # Configure parser and get options
    config = {
        "description": "Coverts Sloop Bety locations to an HTML table.",
        "epilog": "Please report any issues to Ben."
    }
    if "config" in kwargs:
        config.update(kwargs["config"])

    parser, options = parseargs(**config)

    # For every CSV, generate & output an HTML table
    for location in options.locations:
        print tabelize(location)

if __name__ == '__main__':
    main()
