#!/usr/bin/env python


""" Calculate the number of increases in a list of subsequent measurements read from file """


import fileinput
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: day1_sonar_sweep.py <measurements file>")
        sys.exit(-1)
    input_file = sys.argv[1]
    measurements = [int(line) for line in fileinput.input(files=input_file) if line.strip() != '']
    increases = sum(((m2-m1) > 0 for (m1, m2) in zip(measurements, measurements[1:])))
    print(increases)
