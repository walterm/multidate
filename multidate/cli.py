# -*- coding: utf-8 -*-

"""Console script for multidate."""

import datetime
import sys


def usage():
    return '''
    Usage:

    $ multidate <comma separated list of unix timestamps
    '''


def main():
    try:
        hours = sys.argv[1]
    except Exception:
        print usage()
        return

    hour_strs = hours.split(',')
    parsed_hours = [int(hour_str) for hour_str in hour_strs]
    for hour in parsed_hours:
        print datetime.datetime.utcfromtimestamp(hour)


if __name__ == "__main__":
    main()
