# -*- coding: utf-8 -*-

"""Console script for multidate."""

import datetime
import sys


def usage():
    return '''
    Usage:

    $ multidate <unix hour>, <unixhour>
    $ multidate <unix hour>,<unixhour>
    $ multidate <unix hour> <unixhour>
    '''


def handle_exit():
    print usage()
    sys.exit()


def sanatize_hour(hour):
    assert isinstance(hour, str)

    hours = hour.split(',')
    sanatized_hours = []

    for hour in hours:
        try:
            sanatized_hours.append(int(hour))
        except ValueError:
            handle_exit()
    return sanatized_hours


def parse_hours_from_cli(inputs):
    parsed_hours = []
    for hour in inputs:
        sanatized_hours = sanatize_hour(hour)
        parsed_hours.extend(sanatized_hours)
    return parsed_hours


def main():
    inputs = sys.argv[1:]
    hours_from_cli = parse_hours_from_cli(inputs)
    for hour in hours_from_cli:
        print datetime.datetime.utcfromtimestamp(hour)


if __name__ == "__main__":
    main()
