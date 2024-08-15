#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys


codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}


def print_stats(total_size):
    """Function to print the computed metrics."""
    print(f'File size: {total_size}')
    for k, v in codes.items():
        if v == 0:
            continue
        print(f'{k}: {v}')


def main():
    """Function to compute the metrics."""
    file_size = 0
    line_count = 0
    try:
        for line in sys.stdin:
            line_format = line.split()
            if len(line_format) < 9:
                continue

            size = int(line_format[-1])
            code = line_format[-2]

            if code in codes.keys():
                codes[code] += 1

            file_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_stats(file_size)
    except KeyboardInterrupt:
        print_stats(file_size)


main()
