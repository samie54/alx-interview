#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This script reads stdin line by line and computes metrics.

Example:
    $ ./0-generator.py | ./0-stats.py

"""


import sys


def print_statistics(total_size, status_codes):
    """print statistics.

    Args:
        total_size (int): total file size.
        status_codes (dict): status codes.

    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 402: 0, 403: 0, 404: 0,
                405: 0, 500: 0}
line_count = 0
try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) >= 9 and parts[-2].isdigit() and parts[-1].isdigit():
            status = int(parts[-2])
            if status in status_codes:
                total_size += int(parts[-1])
                status_codes[status] += 1
        if line_count == 10:
            line_count = 0
            print_statistics(total_size, status_codes)

except KeyboardInterrupt:
    pass
finally:
    print_statistics(total_size, status_codes)
