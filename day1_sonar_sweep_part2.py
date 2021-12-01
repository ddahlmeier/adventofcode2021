#!/usr/bin/env python

""" Calculate the number of increases in a list of subsequent measurements which are smoothed
in a sliding window. Measurements are read from file
"""

import fileinput
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day1_sonar_sweep_part2.py <measurements file>")
        sys.exit(-1)
    input_file = sys.argv[1]
    measurements = [int(line) for line in fileinput.input(files=input_file) if line.strip() != '']
    sliding_window = [sum(window) for window in zip(measurements, measurements[1:], measurements[2:])]
    increases = sum(((m2-m1) > 0 for (m1, m2) in zip(sliding_window, sliding_window[1:])))
    print(increases)
